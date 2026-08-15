---
title: "Between the Brackets, Episode 176: Selena Deckelmann"
person: selena-deckelmann
section: by
type: talk-transcript
year: 2023
venue: "Between the Brackets (a MediaWiki podcast)"
source_url: https://betweenthebrackets.libsyn.com/episode-176-selena-deckelmann
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 71
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Between the Brackets, Episode 176: Selena Deckelmann

*Speakers (inferred):* speaker_0=Yaron Koren, speaker_1=Selena Deckelmann

## Transcript
**Yaron Koren** [00:00]: This is Between the Brackets, a MediaWiki podcast, episode 176, February 11th, 2025. [gentle music] Welcome to Between the Brackets. I'm Yaron Koren, and my guest for this episode is Salina Deckelmann, who since 2022 has been Chief Product and Technology Officer at the Wikimedia Foundation. I'm very excited to have her. This is a Wikimedia... Oh, my God. This is a MediaWiki podcast, and she is in charge of the development of MediaWiki, so it's, it's a great honor to have her on the program. Salina, welcome to the program.

**Selena Deckelmann** [00:40]: Thank you so much for having me, and I have sort of stopped saying the wrong word, MediaWiki or Wikimedia, at the wrong time at this point-

**Yaron Koren** [00:50]: [laughs]

**Selena Deckelmann** [00:50]: ... but I sometimes mix them up too.

**Yaron Koren** [00:51]: [laughs] Okay. I feel like I sh- would have stopped by now, but, uh, I guess it never actually stops.

**Selena Deckelmann** [00:57]: [laughs]

**Yaron Koren** [00:58]: Um, so, uh, so first of all, where are you located?

**Selena Deckelmann** [01:02]: Uh, I'm located in Portland, Oregon, in the US. I've been here for a long time. It's a nice place to live.

**Yaron Koren** [01:08]: Sure. Uh, very good. So, um, I, uh, there's a lot to, to, uh, cover. I don't wanna d- uh, get too much into your, uh, backstory, I guess, but, uh, it, it is, uh, quite interesting. You spent about 10 years at the M- at the Mozilla Foundation, uh, from what I understand, from 2012 to 2022. Um-

**Selena Deckelmann** [01:29]: Yep

**Yaron Koren** [01:29]: ... uh, you're, do you, you, uh, when you left you were senior vice president there?

**Selena Deckelmann** [01:37]: Yep, that's right, uh, working, uh, on Firefox.

**Yaron Koren** [01:40]: Yeah. It's so interesting. I was looking into it. I mean, obviously there's nothing quite like the Wikimedia Foundation, but it, it is really interesting the parallels between the Mozilla Foundation and the Wikimedia Foundation. Like, it's as q- it's as close to a lateral move as there can be. Like, uh, not that, not that there really can be, but, uh, uh, they both have, they're both, you know, technology-oriented non-profits. They both have a, a, uh, for-profit corporation in the middle of them. And, and actually they were f- both founded i, uh, in 2003, just about a month apart from each other. I was surprised by that also. Um-

**Selena Deckelmann** [02:19]: Hmm.

**Yaron Koren** [02:21]: [laughs] Just interesting. Uh-

**Selena Deckelmann** [02:22]: Yeah, I didn't realize that, that, that funny thing. The for-profit corporation piece of it is a little bit different though, I would say. I mean, I think a lot different, actually.

**Yaron Koren** [02:34]: Oh.

**Selena Deckelmann** [02:34]: Are you referring to Enterprise, or-

**Yaron Koren** [02:37]: Yes

**Selena Deckelmann** [02:37]: ... yeah, yeah. Yeah, I, yeah, it's super interesting to, like, think about the parallels, for sure. I feel super lucky because I got to work in two tech non-profits on open source software. I think that's pretty unusual in a person's career to be able to do that. I mean, there's a few of us, uh, around, but, uh, I feel incredibly lucky. Um, and I think-

**Yaron Koren** [03:00]: Yeah, it's just you and that, and that scrappy startup, uh, OpenAI.

**Selena Deckelmann** [03:05]: [laughs] Are they still... I thought they abandoned the nonprofit piece.

**Yaron Koren** [03:09]: Oh, are, have they? Okay. I don't know. I don't know. Yeah.

**Selena Deckelmann** [03:12]: That was... I thought it was out of here. Um, yeah. So yeah, it's been, it's been fun being able to do this kind of work. I started working with open source software in college, uh, and I was really lucky in my first job out of college also to get to contribute to open source, 'cause my coworkers at the time, I was at Intel, they were contributing. And so I didn't have to, like, talk to a lawyer or [laughs] sign some, like, special, like, intellectual property disclosure or anything like that. I... incredible. I started out actually working on the, you know, the crash reporting system. Uh, because prior to coming to Mozilla, I spent about 10 years contributing to the PostgreSQL community. So I came, came to Mozilla to work basically on Postgres, and then, um, over time I started doing more.

**Yaron Koren** [04:07]: Yeah. Um, uh, h- in, in terms of, um... Well, the, the thing I'm, I'm really i- interested about is, is the decision-making process, 'cause, uh, um, uh, you know, well, it, it's always tricky at a, at a non-profit organization to figure out what it is that, that d- you should work on, that sort of thing. But, uh, you know, uh, at the Mozilla Foundation, obviously you have all the stakeholders, but, but w- with the Medi- Me- Wikimedia Foundation, uh, there's, you know, millions of stakeholders theoretically. Um, uh, I don't know. Does, does it f- does that feel, does that part of it feel different? That, um, that y- you know, there's just an endless amount of, uh, input coming in as to, to what people should be working on?

**Selena Deckelmann** [04:57]: I, I do think it is very different. I think... I mean, it's, they're, they're both such hugely ambitious projects. Um, Firefox as a non-profit browser is a hugely ambitious thing to tackle. I mean, just the sheer amount of web standards to implement, I mean, is really intimidating. Like, the amount of, uh, I don't know, there's just, like, a lot to master, and there's so much that matters about that software, the safety of it, um, the security of people's financial transactions, their communication with, you know, their government, with their school, with their boss. [laughs] Like, there's, there's so many things that go into having a safe and secure browser. So, you know-

**Yaron Koren** [05:48]: Yeah

**Selena Deckelmann** [05:48]: ... from that standpoint, there's a lot of, like, responsibility and accountability there. Um, and it's supported by all the work that people do interacting with standards bodies. So there's quite an active, like, engagement with IETF and W3C.

**Yaron Koren** [06:04]: Yeah

**Selena Deckelmann** [06:04]: I think-

**Yaron Koren** [06:05]: And Firefox-

**Selena Deckelmann** [06:05]: Yeah

**Yaron Koren** [06:06]: ... is s- is sort of the only true open source browser, at least among, am- in wide usage. No? Or is that accurate to say? [laughs]

**Selena Deckelmann** [06:14]: Uh, I mean, I think, y- yeah. I, I would say that people feel that way for sure, right? Like, th- like, one that ha- still has some market share. Um, Firefox's market share has dwindled, like, quite a bit since the early days. Uh, yeah, and there's a lot of criticism of the, you know, um, Chrome engine and how, um, how the governance of that is done, has-

**Yaron Koren** [06:39]: Right

**Selena Deckelmann** [06:39]: ... has evolved over time. Yeah, and I think, you know, the Wikimedia universe, uh, it's profoundly different. [laughs]

**Yaron Koren** [06:50]: Okay. [laughs]

**Selena Deckelmann** [06:50]: Sort of. It's really, really different. There's, there's MediaWiki, which is a piece of that universe, very important piece of that universe, and then there's, like, everything else. [laughs] And that, that I... I mean, I, I thought I kinda knew what was going on. I don't know why I thought I knew what was going on or, or how things worked, but I really truly did not, you know, when I first joined. Um, and I, I, like, what I thought I knew was how, um, how the content communities that support, you know, all of the Wikimedia projects, how they might work. I thought I had a clue. Um, I really did not. [laughs] So that, that was kinda like the, the wow, I, I have so much to learn. And I mean, just really special opportunity to learn, but that, it's, it's very different than open source software development that I was used to.

**Yaron Koren** [07:47]: Uh, okay. Yeah, what, what's an example of that? Uh, yeah.

**Selena Deckelmann** [07:52]: Uh, the way that RFCs are conducted was nothing like anything I had seen before, and I was also more used to an approach to, um, decision making and governance where you have a much smaller group of highly engaged people rather than a very large group-

**Yaron Koren** [08:11]: [laughs]

**Selena Deckelmann** [08:11]: ... of sometimes engaged and sometimes not people.

**Yaron Koren** [08:14]: Right.

**Selena Deckelmann** [08:14]: Like, it's a very different way to solve problems together, and it's a fascinating thing. I think it's incredibly effective, but it can be, like, disorienting when you're used to going into, like, a virtual or a physical space and, like, some, y- like, you kinda know who's gonna be there. You know, kinda, you know, maybe you've, like, met them before or there's, like, some, like, you know, social norms around, like, how the conversation's gonna go. And I think RFCs, they don't feel that way. They're, they're really different.

**Yaron Koren** [08:48]: Yeah. Um, so, so, uh, just in, in terms of, uh, your, the s- your scope and so forth, there's a, uh, I looked up, there's a, there's a, a little, there's over 700, uh, employees at the Wikimedia Foundation, which is actually is very close to the number at the Mozilla Foundation, but, uh, just as a side note. Um, uh, how, how many of those, uh, uh, well, sorry, employees and contractors, how many of those people are under your purview as, uh, i- in the technology department or s- area?

**Selena Deckelmann** [09:21]: Yeah, right now it's about 300. It fluctuates just a little bit, you know, over time of course, but yeah, it's about 300.

**Yaron Koren** [09:28]: Yeah, okay. And of course that's not, that doesn't include all the volunteer developers and so on.

**Selena Deckelmann** [09:34]: No, and last time somebody gave me a number on that, uh, I, somebody was like, "Tens of thousands of volunteer-"

**Yaron Koren** [09:43]: Really?

**Selena Deckelmann** [09:44]: "... developers." But, like-

**Yaron Koren** [09:44]: Okay

**Selena Deckelmann** [09:44]: ... yeah, not, not on MediaWiki only. It's, like, the, um, all of the tools.

**Yaron Koren** [09:50]: Okay, okay. Yeah, yeah.

**Selena Deckelmann** [09:51]: Yeah.

**Yaron Koren** [09:51]: Everyone who edits a module on Wikipedia or that sort of thing. Okay.

**Selena Deckelmann** [09:56]: Mm-hmm. And in the Wikimedia cloud services, there's just, like, like, a wildly divergent, uh, community of people that do all that kind of work, and most of it's essential, you know, to the functioning of Wikipedia for sure, but, but most of the other wikis as well. I mean, one of the things that, like, I, I didn't really know that either [laughs] when I first came.

**Yaron Koren** [10:20]: Right.

**Selena Deckelmann** [10:20]: Um, like how large that group of people were, and also, you know, things like they've been doing machine learning, like, had machine learning bots going since, like, 2000s, you know? Like, that's, it's, uh-

**Yaron Koren** [10:35]: Yeah

**Selena Deckelmann** [10:36]: ... it's really impressive the kinds of things that people have been doing as volunteers at scale for a really long time.

**Yaron Koren** [10:42]: Sure. Yeah. Um, so you, you mentioned RFCs. I mean, um, uh, what is, w- how, how do you feel, how do you view your role, uh, at the Wikimedia Foundation? Uh, b- are you ultimately in, uh, in charge of deciding the outcome of, uh, of every RFC and, and that sort of thing, or do, do you feel more like a, uh-

**Selena Deckelmann** [11:06]: Yes

**Yaron Koren** [11:06]: ... uh, you know, more, more hands off, I guess?

**Selena Deckelmann** [11:10]: [laughs] I can... Um, I-

**Yaron Koren** [11:14]: That wasn't intended to be funny, but, uh, I, I-

**Selena Deckelmann** [11:18]: Um, well, I, I, I, I assume, I assume you partic- Do you participate in, like, Wikiped- Wikipedia RFCs?

**Yaron Koren** [11:26]: I've read a bunch of them. I don't know if I've ever actually... Well, actually, oh, a- actually, oh, you said Wikipedia RFCs, like the content-

**Selena Deckelmann** [11:34]: Yeah

**Yaron Koren** [11:34]: ... related stuff?

**Selena Deckelmann** [11:35]: Yeah, yeah. Have you ever?

**Yaron Koren** [11:35]: Oh, I ha- I have participated in those, yes.

**Selena Deckelmann** [11:38]: Yeah, yeah.

**Yaron Koren** [11:38]: Okay.

**Selena Deckelmann** [11:39]: Okay. Well, I, I mean, the foundation absolutely doesn't control the outcome of RFCs [laughs] ever.

**Yaron Koren** [11:44]: Oh, those kinds of RFCs. I thought you were talking about, m- uh, you know, should we switch to V- to Vue.js kind of RFCs.

**Selena Deckelmann** [11:52]: Well, I don't control the outcome of those RFCs either.

**Yaron Koren** [11:54]: Okay. All right. [laughs] But, I mean, oh-

**Selena Deckelmann** [11:57]: [laughs] Well, I mean-

**Yaron Koren** [11:57]: Yeah

**Selena Deckelmann** [11:57]: ... you tell me as a contributor if you think that I do. I, I-

**Yaron Koren** [12:01]: Well, yeah, well-

**Selena Deckelmann** [12:02]: ... that's not been my experience or observation

**Yaron Koren** [12:05]: Yeah, sure, sure. But well, I g- that, I, that I always-

**Selena Deckelmann** [12:08]: I can participate in them. I can share with people my, my views, and I do.

**Yaron Koren** [12:12]: Yeah.

**Selena Deckelmann** [12:12]: But yeah, I don't control the outcome.

**Yaron Koren** [12:14]: Okay. Yeah, no, that always, uh, interests me with, you know, it's like, uh, it, you know, the, the, the, the, the King of England, uh, you know, nominally if he really disagrees with some political decision, I think he, uh, has the power to step in and, and do something about it. Not that he has in, you know, 100 years. But, uh, I, I wonder if, if you at least have that sort of control. Like, if you really want to exert, uh, your, uh, opinion on, uh, on something that you nominally at least have that ability.

**Selena Deckelmann** [12:45]: When it comes to content decisions, I... This is not my-

**Yaron Koren** [12:48]: Well, yeah, not content

**Selena Deckelmann** [12:49]: ... area-

**Yaron Koren** [12:50]: No. [laughs]

**Selena Deckelmann** [12:50]: Area at all. Yeah. [laughs]

**Yaron Koren** [12:52]: That would be hilarious. Um-

**Selena Deckelmann** [12:53]: Uh, so, so just make that perfectly clear, and just to help, help people understand that I do know that. Um, and I, like, for other types of decisions, there are definitely... You know, there's definitely areas where I have to take into account, like, the safety and security of staff or the safety and security of editors. And actually, normally, I don't even have to, like, weigh in on that type of thing. That's more of, like, a trust and safety and legal concern, right? But maybe there's, like, a software intersection there. Uh, tho- those are the types of things where, you know, I wouldn't say it's a King of England power, [laughs] but it's more like a very accountable, uh, person who is serving this community. And sometimes there are things that I am accountable for that no one else can be accountable for. And yeah, there I have to make decisions. But when it, when it comes to the normal kinds of conversations that we have about, like, whether Vector 2022 is good enough, I can express-

**Yaron Koren** [13:56]: Right

**Selena Deckelmann** [13:56]: ... my opinion, and I can try [laughs] to help people understand why I might wanna do something and why I really encourage them. Like, this is the way that w- this probably should go for, like, best use of resources, effective use of everyone's time, for sure. Like, I, I share that. But yeah, it's not a, it's not a situation where I control what people say [laughs] or what they do with the RFCs at all.

**Yaron Koren** [14:19]: Yeah, yeah. So, uh, how, how, how would you describe your role?

**Selena Deckelmann** [14:25]: Uh, in what my job is?

**Yaron Koren** [14:27]: Yeah, sure. Sure, yeah.

**Selena Deckelmann** [14:29]: Yeah. Well, I am here, first of all, to help manage a very large group of product development professionals, right? So they've been hired into this foundation to do work. Uh, and fundamentally, I have to keep the website up, so that's a good portion of people's attention and time and energy. And I'm here to, like, look at what's going on with that, make sure that we are serving traffic well, look for ways to improve our reach, you know, worldwide. So I do things like look at places that we could deploy a new data center, you know?

**Yaron Koren** [15:08]: I see.

**Selena Deckelmann** [15:08]: So that's something that we did last year. Um, and then another part of my job is, like, talking with community members and, like, trying to figure out, like, how can we best serve their needs, and those communities are vast. [laughs]

**Yaron Koren** [15:21]: For sure.

**Selena Deckelmann** [15:21]: It's not just, like, one type of person doing one type of thing. So I spend a lot of time on that just trying to understand all of the different ways in which people benefit from, you know, the free knowledge distribution that we do and the creation of it. And I try to find ways of empowering them and making them more effective. You know, giving them tools, that type of thing.

**Yaron Koren** [15:43]: Yeah. Uh, it's interesting with, uh, the Wikimedia Foundation 'cause there are, uh, these, uh, disparate sites, uh, and projects, uh, that, that fall under the Wikimedia umbrella, and I guess there has to be some element of, of deciding... Well, obviously deciding on priorities, allocating resources. Um, it, it feels to me, uh, like there's been a concerted effort in the last few years to f- to, to focus on Wikipedia specifically. Like, that really is where the, the needs are most urgent. Uh, d- is that accurate, uh, that there's the, it, that's become a more, um, overt, uh, goal?

**Selena Deckelmann** [16:30]: Uh, I think, I think if you look back at the last several years, I don't know if you would find even in the last 10 years anything much different than that, like, in terms of what actually gets implemented in the software. I don't know. Is your impression different than that?

**Yaron Koren** [16:53]: I just read some, some things, uh, uh, that, uh, seemed to, seemed to indicate that, uh, w- you know, Wikipedia gets the focus over, well over, um, projects like Wiki News and, and so forth. Um, I, I, I mean, I, uh, there was a, there was a, a discussion or I guess an ongoing discussion related to Wikimedia Commons that I, that I find quite interesting, um, uh, where there's a real... I, I... Well, there's cer- certain people at Wikimedia Commons who think that they're, that, that, that site is getting neglected. But on the other hand, of course, uh, you know, Wikipedia is the, the face of the whole operation. Um, uh, yeah, I'm, yeah, I mean, um, well, I mean, we, we can talk about the, there's a, the, uh... I, I don't know to, I don't, I don't know to what extent this is a, a big issue in the grand scheme of things, but, but, uh, there have been some, some interesting, uh, conversations that you've been part of. Um, ag- including, I, I think, like, an o- an ongoing kind of, uh, discussion series or something with, uh, with the users at Wikimedia Commons. Um- Uh, there was, um, you, it, it, there was a, something you wrote last year that, that I thought was quite interesting on, uh, uh, relating to, uh, to sort of a, a general discussion of the future of MediaWiki com- Wikimedia Commons, sorry, uh, uh, where you wrote, um, uh... Well, okay, yeah, not, not to put you on the spot with your, with your own quote, but I, I thought this was quite interesting in terms of, uh, in terms of decision-making about allocating resources and so forth. Uh, uh, you wrote, um, uh, "WMF has an obligation to inve- to invest resources in a way that furthers not just knowledge collection, but dissemination. To what extent is the Wikimedia Commons community invested in the dissemination of knowledge via images on Wikipedia articles? To date, my observation is that the primary focus of the Commons community is the collecting of free coment- content rather than its dissemination." Um, uh, yeah. Tha- uh, so, so, uh, there was, there was, uh, some, uh, I, I guess some sort of imp- inherent, um, difference in views about th- about what, uh, Wikimedia Commons is, is, uh, good for, is useful for. Um, but I thought that was a, a, a really interesting s- uh, sort of, uh, insight into the kind of decision-making that has to be done at the Wikimedia Foundation in terms of allocating resources. I don't know, I don't know if, i- i- to what extent Wikimedia Commons, i- i- you, uh, i- is a factor in, in decision-making at all, but, uh, but I thought that was an interesting, uh, you know, observation.

**Selena Deckelmann** [19:58]: Yeah. Yeah, it totally is. I mean, I think the Commons world, like the universe that all those contributors operate in, it's not so different from the rest of the Wikimedia projects. And in fact, there were several people in that particular conversation, you know, there's... I mean, ones where I've, like, published blog posts or whatever, but, but then there's also been multiple conversations where, you know, one user, Rotatundrids, pointed out that a lot of the users of Commons are also users of Wikipedia, you know, and active contributors to both. And I, I think that's really actually one of the most important things to remember about all of the communities that exist, is they're not terri- they're not, like, super distinct, and that that overlap, I mean, I don't know that we take advantage of it as much as we could. [laughs] Uh, because-

**Yaron Koren** [20:58]: Of Commons, you mean?

**Selena Deckelmann** [20:59]: Yeah. Well, the overlap between all of the different-

**Yaron Koren** [21:01]: Oh, I see. Okay

**Selena Deckelmann** [21:02]: ... projects. Yeah, yeah, and Commons and Wikipedia in particular. And what I think is a missed opportunity is to think about with the reach that one gets from a project like Wikipedia, uh, how much more powerful and effective would it be if we were really thinking hard about the ways in which we could showcase all of the incredible images. There's not as many videos, honestly, but a lot of images, really incredible ones, um, that are in Commons and difficult to find. Uh, you know, there's a lot of different ways to, like, go about that, but one of the ways that you can make it more valuable to humanity, not just to me, like it doesn't really matter what I want, but just, like, thinking about people out there and the things that would help them and help them understand the world around them better, having images [laughs] of things. It's, it really-

**Yaron Koren** [22:03]: Sure

**Selena Deckelmann** [22:03]: ... is powerful. So, you know, my, my point is in these conversations is just trying to encourage people to think about the ways that we could be approaching solving some of the problems that we face differently. And by differently, I mean rather than thinking of each community as this distinct thing that has to be addressed distinctly and has to be dealt with separately, and there's, like, a whole s- like, set of engineers assigned only to work on Commons. Maybe actually there are some problems to solve between these projects. Same thing with Wikidata. You know, um, I think there's a lot that could be done if we were to think about this system holistically and the ways in which they, the different projects complement or don't complement each other.

**Yaron Koren** [22:53]: Sure. Yeah. Um, to what extent are you involved with Wikidata? I mean, it's, it's, uh, it's i- in theory run by Wikimedia Deutschland, although I'm sure you, the, you know, there's, uh, overlap in discussions and so forth about it.

**Selena Deckelmann** [23:08]: Well, I operate all the infrastructure for Wikidata.

**Yaron Koren** [23:11]: Oh, okay. Good to know. [laughs]

**Selena Deckelmann** [23:15]: That's been true. [laughs] Yeah, that's been true for the life of the project.

**Yaron Koren** [23:18]: I see. Um-

**Selena Deckelmann** [23:20]: Yeah.

**Yaron Koren** [23:21]: Uh, yeah, it's interesting. There are, I g- I guess you could say s- uh, four of the sites, four of the Wikimedia sites are actually more like repositories than, than places people go to directly. Uh, well, three plus one that doesn't exist yet, uh, which is Wikimedia Commons, Wikidata, Wiki Functions, and then Abstract Wikipedia, um, which I don't think exists yet, but that's, but it's on the r- roadmap. And, uh, and interestingly, three of those four were created by, uh, Denny Vrandečić.

**Selena Deckelmann** [23:52]: [laughs] Yeah.

**Yaron Koren** [23:55]: Um...

**Selena Deckelmann** [23:57]: Well, I mean, do you think of Wiki Functions and Abstract Wikipedia as being two totally separate things? I don't really.

**Yaron Koren** [24:03]: Uh-

**Selena Deckelmann** [24:04]: Because they're-

**Yaron Koren** [24:04]: Well, yes and no. Obviously Wiki P- Wiki Functions was created for the, for the case of Abstract Wikipedia, but all the functions I've seen from there so far d- just seem like, you know, just general functions. I th- I, I'm still, it's still not clear to me- ... uh, what Wiki Functions is all about. Uh, I mean, obviously it's, it's there to support abstract Wikipedia, but, uh, but I don't know if, if it's also intended to, to just serve as a general repository of functions to, for use on Wikipedia or other sites or maybe sites in general.

**Selena Deckelmann** [24:36]: Well, I can give you an example. Um, and this, you know, I think it's difficult to imagine the different use cases, and, and frankly for a single language wiki, it's pretty hard to, uh, conceptualize the, all of the use case, although there are a few kind of obvious ones for templates. But on a multilingual wiki, like for example Commons or Wikidata, the value of it is being able to, um, use functions for the kinds of things that you might have to put... I, uh, you know, I've worked with the syntax, um, for translation, marking things for translation. What if you could do that without that? So instead you could just, like, work in templates that understood how to do the translations based on whatever language the user selected.

**Yaron Koren** [25:28]: Sure. Yeah, yeah. No, no, uh, sure. The, the translation part I, I totally, uh, I, I totally, uh, I, I think I totally get. I mean, I, I, I under- I understand the, the general concept of, uh, of writing in some kind of, of a language neutral syntax. I believe that's, that's the, the ultimate goal with not just abstract Wikipedia, but in general. But again, like, again, I could be wrong. Um, where you're just b- basically writing out sentences, diagramming out sentences in some kind of, uh, in some kind of language neutral ID-heavy way.

**Selena Deckelmann** [26:09]: Yeah. I think the user interface is gonna take some iteration. [laughs] I'll say, it's like really-

**Yaron Koren** [26:14]: I'm sure. It's a challenge

**Selena Deckelmann** [26:15]: [laughs] But yeah. Right now they're working on just very basic functions to see if they can prove out a use case. Um, and that, that is interesting to me, because if it could solve some of the problems that we face, like I don't know if you've used the translation syntax.

**Yaron Koren** [26:34]: Sure, yeah. On, on, uh, on mediawiki.org, you're forced to basically all the time.

**Selena Deckelmann** [26:39]: Yeah.

**Yaron Koren** [26:39]: Yeah.

**Selena Deckelmann** [26:39]: Yeah, it's not fun. So I [laughs] first of all, I'd like that just to be better, like before, you know, we solve this, like, broader templating problem. But, um, but yeah, that, that is interesting to me is if, if we could make something like that better, and maybe there's some narrower use cases where we're focused on info boxes or, you know, things like that, um, I think it could be valuable. I, what's unsolved really are the, there's a number of, like, performance challenges with doing this type of, like, real time, um, you know, uh-

**Yaron Koren** [27:14]: Yeah

**Selena Deckelmann** [27:14]: ... parsing and rendering. You know, like, it's, it's, it's hard. So, um, I don't think this is, like, something that's gonna change this year, [laughs] but it's interesting to explore.

**Yaron Koren** [27:26]: Um, yeah. I, well, I wanna, I wanna get into that and, and all the, the f- the future of Wikimedia and all that, but I, I guess a more pedestrian question first is, um, there's, there's always, y- you know, a- a- again, around the issue of priorities, there's always, um, there's always f- bugs to fix. [laughs] Um-

**Selena Deckelmann** [27:47]: [laughs]

**Yaron Koren** [27:47]: L- you know, d- do you feel like you h- you have to push in one way or the other, like, for, for, to focus more on, for people to, to, to focus more on big picture, uh, uh, new feature type of stuff versus bug fixes or the other way around? I mean, how do you balance that, uh, the, or refactoring, which arguably is a third category, uh, of, of code for performance and that sort of thing. How, how do you balance out all the, the, the, those different, uh, uh, you know, goals?

**Selena Deckelmann** [28:21]: No, that's a great question. Well, our, the annual plan system, like, that I helped put into place, it has a category of work which is objective and key result driven, and so that's like traditional product management, you know, software development, objective and key results where we're trying to say for, you know, this period of time, usually like a year, what we're trying to accomplish with that is an increase in page views of this percent or, you know, improvements in, uh, editor workflows measured by surveys or usage of a tool, things like that. And that's probably about half of the work of the foundation at this point. The other half is dedicated to, um, what we've call essential work, and all of that is bottoms up driven. So it's like all of the teams and the individuals in those teams looking at their backlogs. Uh, some of that's coming-

**Yaron Koren** [29:27]: Right. I get it

**Selena Deckelmann** [29:27]: ... from Capital Year. Some of it might be them, like, looking at the infrastructure, looking at logs and things that are breaking and, you know, figuring out stuff from there, and so that's the other half. Um, so that's kind of where we've ended up, uh, in the last, like, couple years and me just taking a look at everything that was there and trying to, like, assess where we are. You know, I think there's some folks in some teams that would like to do less of that maintenance work. You know, they'd like it to be a lower percentage, and there are some teams that wish it was more.

**Yaron Koren** [29:57]: Huh.

**Selena Deckelmann** [29:58]: You know? And so we're, um, rather than thinking about it as, like, one team as 50/50, the percentage across the different teams is different, and it reflects, like, the local circumstances of that team and the things that it's supporting. So, um, so at a high level, it's kind of coming out to about 50%, and I imagine that that'll fluctuate, like, over time depending on what it is that we're working on. And then for individual teams, we try to give them quite a bit of autonomy 'cause, like- You know, I, there, there's a lot of work streams happening [laughs], like a lot of code that's being cranked out, a lot of challenges, like, in supporting the size of infrastructure, you know, for the billions of users. There's just, like, lots of things happening all the time that no one person or even, like, a group of 10 people could stay on top of and make decisions about all the time. So we have to figure out a way of delegating that, um, effectively. And this, so far, it's working pretty well. There are challenges, you know. Like, sometimes a team gets overwhelmed by incidents, you know, and then some important piece of work, you know, falls off the table and we have to figure out what to do about that. And so to deal with that, we have regular reporting and having people review those reports, and, like, circling back and trying to figure out solutions to challenges like that. But yeah, that-

**Yaron Koren** [31:18]: Right

**Selena Deckelmann** [31:18]: ... that's about how it works today.

**Yaron Koren** [31:21]: Yeah, okay. Um, and there's also just a, a, a, a general refactoring. Well, there's been a b- reorganization of the Wikimedia Foundation and reorganization of MediaWiki. I g- I assume those are unrelated, but, uh, but who knows? But I, I, I, but, uh, uh, Birgit, uh, Müller was on the, the podcast and she, uh, I, I guess that's the, that's, uh, in large part her project, the, the, the refactoring MediaWiki. Um, yeah, do you have any es- [laughs] is that correct? I don't know. Do you have any thoughts about that, about the, the, the need to, to, uh, to overhaul the code?

**Selena Deckelmann** [32:04]: Well, I, there's ... I, I wouldn't describe, like, Birgit's, like, project as, like, refactoring all the code, I guess.

**Yaron Koren** [32:12]: Oh, okay.

**Selena Deckelmann** [32:12]: So [laughs]

**Yaron Koren** [32:12]: Well, all right. That might, look, that might be overstating it.

**Selena Deckelmann** [32:15]: [laughs] I just-

**Yaron Koren** [32:17]: Somewhat

**Selena Deckelmann** [32:17]: ... just because I think the connotations, at least, like, in English for me as, as an American programmer are that sometimes people just, like, refactor things for, like, no reason, um, you know, just 'cause they want it to look better, and I-

**Yaron Koren** [32:28]: Sure

**Selena Deckelmann** [32:28]: ... that's not my impression of the work that that team-

**Yaron Koren** [32:31]: I see, okay

**Selena Deckelmann** [32:31]: ... is doing. [laughs] Um, so-

**Yaron Koren** [32:35]: It's the good kind of refactoring.

**Selena Deckelmann** [32:37]: Yeah, yeah, yeah. I think that there's some good kinds of refactoring that are on the table, um, with that group. But what I saw, um, again, when I came in in 2022, there wasn't a MediaWiki team, and I did a listening tour, you know, where I talked to lots and lots of people, more than 500 people, but, like, mostly, you know, the mix of staff and contributors. And what they told me were lots of stories about failed migrations, basically. So where someone starts a project to implement some new thing, either in MediaWiki or just, like, in the infrastructure to support the, uh, you know, the Wikipedias and all the other projects, uh, where someone starts something and they're not able to finish it because there's actually yet another migration happening. And so I started counting these up and [laughs] making a list of all of these projects where people were like, "Here's one technology. Let's move to this other technology," and they weren't done. So-

**Yaron Koren** [33:38]: Yeah, okay

**Selena Deckelmann** [33:38]: ... part of Birgit's work is, like, taking stock of that and, like, figuring out how can we finish some of those things. Like, one of the first things that she did was retire, um, RestBase in the infrastructure. Uh, yeah, and there's been other projects, but it's, like, trying to get a handle-

**Yaron Koren** [33:54]: Right

**Selena Deckelmann** [33:54]: ... on that, and so some people call that technical debt. You know, I, I don't know. There, there's just a quite a bit of work that ends up tripping people up for not super good reasons, and so we have to make decisions about what should continue, or stop, or be rolled back or, you know, whatever. Um, and then a thing that I see, and that Birgit and I kinda have a similar opinion about, is that, um, the way that extensions overall got implemented, they're very permissive. There's not a lot of structure. There's not [laughs] a lot of, like, you can do this or that. And as a result, a, an extension can basically do anything. And that, for many reasons, becomes problematic over long periods of time, right? 'Cause then you stop knowing, like, what it is that an extension is supposed to do or should or shouldn't do. So a task that I've asked people to look into is what would an appropriate, like, extension boundary look like? Um, and I take that from lessons I've learned working on browsers. Architecturally, it'll just be easier to support long-term if we can figure out, like, what a sane boundary is. Um-

**Yaron Koren** [35:12]: Right, okay, like browser plug-ins.

**Selena Deckelmann** [35:14]: Yeah, something like that, right? But exactly, like, where that goes, like, I'm not controlling. I think that the people that are closest to that work can tell me what they think is important to tackle, um, and when. And yeah, we're just gonna go from there.

**Yaron Koren** [35:31]: That's interesting. I don't think I'd heard about that before. I mean, it makes sense. I'm a d- I, I m- the extension developer myself. Uh, w- would that, uh, what w- would that be, um, how would that w- how would that work? Where would the, uh, the, the, the boundaries be set? Where would the fence posts or whatever it is be set? Would it be in the code or, um, or, uh, uh, d- you know, declared on the, on the extension homepage or, or-

**Selena Deckelmann** [36:03]: [laughs] Right, like just some social norms?

**Yaron Koren** [36:06]: Yeah, presumably more than that, but, uh-

**Selena Deckelmann** [36:07]: I don't know. Like, I can't tell you. Like, I'm, I'm, like, a barely a, you know, what am I? I'm, like, a pro programmer. I'm a C++ programmer. I'm barely a C programmer. Like, I haven't [laughs] worked on this code base extensively and I haven't lived in it like all of you have. Um, and just, like, as an example, we've had some challenges with things that were deployed that, uh- You know, later security issues were found. I think the graphs extension is the most recognizable challenge like that in the last, like, year and a half or so. Um, and, you know, thinking about problems like that, how do we solve them? Like, I... That's the challenge that I, like, gave to the teams to think through, not with me dictating exactly how they would do it, but I want them to think about it, and think about what would be appropriate to our communities, what would be appropriate to our ability to support extensions over long periods of time. Um, and I think it's best a problem solved, you know, within groups of people that are actually, like, really, like, close to the work. Which frankly, like, I'm not sitting there. I don't get to. [laughs] It's unfortunate. I don't get to code every day.

**Yaron Koren** [37:26]: Right.

**Selena Deckelmann** [37:26]: I have been on call, though. I did take on call and answered pages, so, um... With somebody helping me. [laughs]

**Yaron Koren** [37:33]: Oh, wait. Oh, really? W-

**Selena Deckelmann** [37:35]: Yeah

**Yaron Koren** [37:35]: ... so, so what... So, like, w- when... If, uh, if some site were to go down, like, uh, you know, Turkish Wiki News or something, you would get a, a b-

**Selena Deckelmann** [37:43]: [laughs]

**Yaron Koren** [37:43]: ... a beep about it? You'd be the person that-

**Selena Deckelmann** [37:45]: Yeah, yeah. I mean, we, we don't... Because the SREs are so good, we typically don't have challenges like that. It's more like this, like, particular cluster associated with this database as disk low. You know-

**Yaron Koren** [37:57]: Okay [laughs]

**Selena Deckelmann** [37:57]: ... it's more like, really, like, in the weeds. And so, um, yeah. I'm working on getting my root access. I have some, like, uh, tasks I need to complete before I get it, but yeah. I mean, I think that this is, like... It's such a small organization, um, I really think, why not get root?

**Yaron Koren** [38:16]: Sure.

**Selena Deckelmann** [38:16]: I think I should. So [laughs]

**Yaron Koren** [38:19]: W- uh, now I'm curious what the tasks are that you need to complete, if it's like a, like a vision quest kind of thing like-

**Selena Deckelmann** [38:23]: It is a very long list, by the way.

**Yaron Koren** [38:25]: Yeah. Wow.

**Selena Deckelmann** [38:25]: Like, it's long. Yeah.

**Yaron Koren** [38:28]: Uh, okay. Y- you... Okay. You need to go out into the woods and, like, uh-

**Selena Deckelmann** [38:33]: [laughs] Need to chop down some trees.

**Yaron Koren** [38:34]: Wow. Yeah.

**Selena Deckelmann** [38:36]: [laughs]

**Yaron Koren** [38:36]: Um, [laughs] the secret's out. Uh-

**Selena Deckelmann** [38:41]: That's right.

**Yaron Koren** [38:41]: Yeah, well, so, uh, right. W- how were we... How do we... What were we talking about? Oh, yeah, uh, the, uh... Well, you mentioned the, the graphs extension. From what I understand, the issue there was it was using some third-party library that turns out to be completely unsafe. Is that the one?

**Selena Deckelmann** [38:55]: Yeah, and it was, it was, like, ver- it was a very thin wrapper around that third-party library-

**Yaron Koren** [38:59]: Okay

**Selena Deckelmann** [38:59]: ... right?

**Yaron Koren** [39:00]: Yeah.

**Selena Deckelmann** [39:00]: And, and so, like, so there's... There, you could probably solve it with some norms about [laughs] like, whether or not we would do th- do stuff like that. But there's other examples, and-

**Yaron Koren** [39:12]: Well, you know, well-

**Selena Deckelmann** [39:13]: ... I think it's just, I'm not, I'm not... I'm just, like, telling you, I'm not gonna dictate, um, the future of that, and I think it will be slow. Um, I think it's just really important for the engineers that have been working with extensions for a really long time and kind of understand the deployment challenges and some of the regular issues that they run into to think through that and offer solutions.

**Yaron Koren** [39:33]: Yeah. Um, that's interesting. Not to, not to belabor the point, and this m- this may be already be boring to people, but I'm just wondering how, I, I mean, how there can be any sort of guardrails around that. Like, if you're using a third, third-party code, there's alwa- you were, even in your own, one's own code, there's always the chance that there's some security leak there. Ca- is there anything really that can be done? I mean, y- you know, this concept of sandboxes and stuff for software, but I don't think in PHP or JavaScript you can do anything like that, as far as I know.

**Selena Deckelmann** [40:08]: There's ways. There's, like, you know, they... There was some experimentation and messing around with, like, a WASM, um, module, right? To try to, like, contain it. It didn't work, and so we didn't do it. [laughs] But, um-

**Yaron Koren** [40:22]: Okay

**Selena Deckelmann** [40:22]: ... but there, there are ways to try to encapsulate it. Um, but, um, yeah.

**Yaron Koren** [40:28]: All right.

**Selena Deckelmann** [40:28]: I think, I think in the end, a lot of it's about norms and helping people understand, like, what's safe to do in our environment and what's not safe. Um, but, but I do think, um, there's also just defining interfaces and saying, like, "Here's, like, an appropriate interface to use for this kind of a purpose." And so when people are using that interface, it's like you're looking at the logging, you're, like, understanding, like, what's supposed to be happening, and when something is outside those bounds, you can act. And right now, we don't have that at all. And, like, that, that's kind of the future that I wanna get to, is to start, like, thinking about, like, what can those norms be? And, you know, any piece of code that has existed for as long as MediaWiki has existed, it has some elements of this, right? Because you don't just go and rewrite entire pieces of software for no reason. It's very, very expensive to do that, and as you do it, you introduce probably two bugs for every new line of code [laughs] that you add.

**Yaron Koren** [41:31]: Sure.

**Selena Deckelmann** [41:31]: So, um, or replace. So it's just not worth it most of the time to rewrite software that's like this that's already doing so much and is, um, so useful and so productive. So instead, what we have to do is just kind of adjust to our circumstances and kind of figure out, like, what are the ways that we can evolve this for it to be safer and more maintainable in the environment that we're in now?

**Yaron Koren** [41:55]: Yeah. Yeah. No, it makes sense. Sure. Yeah, yeah. Uh, the, uh, e- extensions have sort of been the Wild West, uh, and maybe they still are. It's, uh, it's, I mean, certainly third-party extensions can basically do whatever they want. Uh-

**Selena Deckelmann** [42:09]: [laughs]

**Yaron Koren** [42:10]: Um, uh, well, it's interesting, when you mentioned interfaces, I thought for a second that you, you were talking about user interfaces, uh, which w- I, I don't think you were, but, uh, that also ties into it. No, I mean the whole, uh, the whole switchover from OOUi to Codex, which is, um, uh... Well, I, I mean, that, that's, that also sort of ties into your whole migration thing. That's been, that's been slow to happen for extensions as far as I can tell. The, uh, there's not too many extensions that are, that are using the new interface approach, user interface approach. Um, yeah. All right. [laughs]

**Selena Deckelmann** [42:47]: [laughs]

**Yaron Koren** [42:47]: I don't know if you have any thoughts on that.

**Selena Deckelmann** [42:49]: Well, the, the new ones that we created, the foundation do, and we did work with Wikimedia Deutschland to use codecs, um, on something they were working on recently. I'm sorry, I don't mind remembering the, the name of the project off the top of my head, but they did-

**Yaron Koren** [43:04]: Okay

**Selena Deckelmann** [43:04]: ... work with us on it. Um, so there's that. But anytime you create a system like this, backporting it all the way is, like, pretty tough. And with OUI, I think the biggest blocker there is visual editor. So-

**Yaron Koren** [43:23]: Right

**Selena Deckelmann** [43:23]: ... the, the investment, um, y- you know, there's just a trade-off. Like, so-

**Yaron Koren** [43:30]: Sure

**Selena Deckelmann** [43:30]: ... at some point, will we decide to migrate it? Maybe. Probably, right? Like, probably eventually, but it's just very expensive thing to drop everything and do right now.

**Yaron Koren** [43:41]: Yeah. Um, so a- actually, you were, you were, uh, uh, uh, uh, uh, you were, I think we g- got switched off topic, but you were talking about the, the whole, uh, uh, you know, re- redoing the organization chart in a sense to, to streamline it, to make all of MediaWiki be one, uh, I don't know what you'd call it, department or something. Um, is that, uh, is that project basically over? Or, or th- are things in a good shape as far as the, the, uh, um, the structure within the Wikimedia Found- Foundation?

**Selena Deckelmann** [44:16]: Uh, yeah, I think so. I mean, the, so the goal was to actually have a team that was thinking about the future of MediaWiki itself, and given ... They were given enough people and enough, like... I was trying to think of another word other than scope. [laughs] This is, like, very jargony, but just, like, like-

**Yaron Koren** [44:42]: Yeah

**Selena Deckelmann** [44:42]: ... yeah, just, like, given enough authority, you know, plus a really amazing thinker and product manager in Birget, um, who, Birget coming from the open source development and the Wikimedia Cloud Services side, really is, like, thinking about, like, what the developer experience is and how to, like, make all of that better. I just thought that that was, like, a really nice way to position the team because that's, like, what operating a platform like MediaWiki is about. It is there to serve the needs of developers. And then, you know, going back to, like, your question, like, right at the top about focusing on Wikipedia, there are needs that Wikipedia has that are quite unique. It's serving, you know, billions of users. [laughs]

**Yaron Koren** [45:34]: Sure.

**Selena Deckelmann** [45:35]: You know? And, um, and, like, that kind of performance that's required and the things, you know, both in the infrastructure, the caching, the way that all of our data systems work, and then, and then how that integrates with MediaWiki, um, you know, it all, it all needs support from somebody that is really thinking about that developer experience. So anyway, so I, I feel like it's in, like, a pretty good spot, um, and I'm looking forward to the kinds of things that they do, you know, in the future. I've asked them to really think about APIs, you know, um, and how, you know, again, like, in that vein of thinking about what the, what appropriate boundaries are between different parts of the code and parts of the services that we're providing. Um, so that's gonna be a focus definitely for a little while. But yeah, I, you know, B- Birget's really gonna, like, dig in there and figure out what's im- what's most important to do first.

**Yaron Koren** [46:40]: Yeah, okay. You're talking about, uh, uh, public APIs, like, uh, e- enabling, uh, with a focus on en- enabling outside users to, to access Wikipedia data in-

**Selena Deckelmann** [46:51]: Yeah

**Yaron Koren** [46:51]: ... in more ways?

**Selena Deckelmann** [46:52]: And, and internal ones, right? Because the way that we structure those internal APIs really affects, like, data flows, um, and then, you know, the ways that, uh, the core of MediaWiki are inter- is interacting with things like extensions, 'cause that could be, like, a different kind of an internal API.

**Yaron Koren** [47:12]: Interesting.

**Selena Deckelmann** [47:12]: And it's not.

**Yaron Koren** [47:12]: Sure, sure. Yeah, yeah. Uh, let me ask a question I, I always get the same answer, which is no to, but let me ask anyway, uh-

**Selena Deckelmann** [47:20]: [laughs]

**Yaron Koren** [47:20]: ... which is, uh, is there, uh, any chance W- MediaWiki will, will become a JavaScript-based single-page application?

**Selena Deckelmann** [47:26]: [laughs] Um, not with the number of editors that we support, uh, you know, and the number of edits that we're supporting, like, every minute. No, I, I don't think that that's possible. Um-

**Yaron Koren** [47:41]: That's interesting. I know there's-

**Selena Deckelmann** [47:42]: Maybe somebody ... Maybe someone could, like, show me, like, what that architecture would look like, but, um, I can't imagine it. I think you can obviously do that with, like, a dump of all of the data and serving to readers, but for editors, like, that doesn't work.

**Yaron Koren** [47:59]: Yeah. No, that's interesting. I hadn't heard about, uh, I, I hadn't, uh, for, for, from the performance perspective, but that makes sense, yeah. Um, uh, well, so, so, uh, uh, as far as big picture stuff, I mean, you mentioned a few i- interesting, uh, things that, uh, for, for the future. We t- we talked about, um, Wiki functions and so forth and, uh, uh, better translation. Um, it ... Well, I mean, it's hard to talk about the future without talking about AI, uh, or, or it's, to talk about people's perception of the future anyway without talking about AI. Uh, I, I d- I, I don't wanna focus on AI too much, but, uh, you did write an, uh, an interesting and I, I'd, I'd say fairly widely quoted, uh, blog post, uh, about a year and a half ago, uh, saying that, saying, you know, a lot of people are asking, you know, what's the future of Wikipedia now that you can just ask a, a, a chatbot any, uh, uh, about any specific topic. And you actually said the, the opposite is true, that, uh, that LLMs make Wikipedia more valuable, uh, because it's one of the few... Well, well, it's a major source of information for LLMs, and if, if, if people are worried about, um, uh, I guess there, there are various terms for, for it, but basically AI, uh, using the, the output of previous AI to, to, to, to learn. Uh, the, the, the way to avoid that kind of, um, uh, negative feedback loop of the, of the information getting progressively worse is, is to have something human-generated like Wikipedia at the source. Uh, is that a f- is that a fair assessment of what you wrote, and do you still agree with that?

**Selena Deckelmann** [49:54]: Well, I, I definitely think that, um, the current state of AI is heavily dependent on human-created knowledge. And the thing that you described, the model collapse-

**Yaron Koren** [50:10]: Model collapse. Right, right

**Selena Deckelmann** [50:11]: ... scenario where it's just, like, consuming its own [laughs] exhaust and then eventually, uh, blows up and stops providing any useful output, these generative AI systems, they kind of get to that point. Um, it definitely is a problem. [laughs] So, uh, that problem has not gone away. Uh, I do think that there have been some amazing advancements in just the last, like, week [laughs] with-

**Yaron Koren** [50:36]: [laughs] Good thing we're talking about it

**Selena Deckelmann** [50:37]: ... with [laughs] I mean, there, I think there's been two major, you know, news items, you know, with, uh, models dropping that, you know, just way more efficient. I just did, like, a mind exploding just-

**Yaron Koren** [50:49]: Oh, model, models dropping, not in the sense of collapsing, but in sense of being released. Okay. Yeah, yeah.

**Selena Deckelmann** [50:54]: Yeah, yeah. Sorry. Like, product releases where, um, it just really took people by surprise how much more efficient, how, um, how much it didn't cost. [laughs] It was very cheap-

**Yaron Koren** [51:06]: Okay

**Selena Deckelmann** [51:06]: ... to train, you know, building on other things, and that they were open source as well. I, I just... I think no one really knows, like, where things are gonna go in terms of how quickly we'll be able to create efficient, effective models. I do think that everybody trains on data that was collected by the editors of Wikipedia. I do think that all of the image, um, you know, image synthesis models, they train on comments. And we see it. We see it in the scraping data.

**Yaron Koren** [51:40]: Okay. Sure. Yeah.

**Selena Deckelmann** [51:41]: You know, we look at our... Yeah. We see this, this dramatic increase in the last year in the amount of traffic that is coming out, you know, going out, the scraping that's happening. So, um, I know for sure that that is true, and I know for sure that it's valuable. And what I think that we don't know right now is how, how it is that we help people understand the value of this kind of knowledge over time, and how important it is that human beings contribute to it, that AIs can't just [laughs] go in and make another Wikipedia because of this model. Like, first of all, the model collapse problem itself, but human judgment is essential for understanding the world around us. Like, machines can't understand it for us. So we all need to work together to produce this knowledge. And that's the thing that worries me the most about the current systems, that they're very extractive, and they're not really thinking about how they can contribute back to this ecosystem. The web, it was founded on this idea of interlinking, and those links-

**Yaron Koren** [52:46]: Right

**Selena Deckelmann** [52:46]: ... they were inherently social, like pro-social, because they were sending you around to all of these different places that existed. And in, in a world where the products, all they do is they try to keep you in one place-

**Yaron Koren** [53:01]: Right

**Selena Deckelmann** [53:02]: ... it's not good. And it's not, it's not just not good from, like, a capitalist, you know, critique perspective. It's not good for society. It's not good for people because we need to interact with each other. [laughs] So I just think, like, it's just a really fundamental thing here. And what I want from these companies is for them to think about the ways in which they can encourage people to actually go to places where the pro-social create the knowledge that you can then use in your model. Like, w- how do we do that? And I think we can do it together. Like, I'm, I'm really not opposed to models training on... But I think it can't just be extractive. We have to attribute. We have to find ways of, um, encouraging people to participate in these, like, social experiments that produce things like Wikipedia. There's lots of them. It's not just us. You know, OpenStreetMap is amazing. There's so many, like, open knowledge projects in the world, right? Like, it is not just us. And every system that uses that data, they really need to be thinking about the ways that they can contribute back.

**Yaron Koren** [54:11]: Yeah. I assume it would help quite a bit if, uh, if, if chatbots always put their sources, uh, whether inline or at the end of their, of, uh, answers, uh, certainly in the case of, uh, Wikimedia, Wikipedia, then other Wikimedia sites.

**Selena Deckelmann** [54:27]: It might, but I think that the way that those systems work, they're, like... They're really, like, hitting something fundamental in, like, human nature of just, like, getting the answer, and then you're, "Ah, I got the answer." Are you gonna do-

**Yaron Koren** [54:42]: Okay. Right, right

**Selena Deckelmann** [54:43]: ... I don't know. [laughs] I don't know. I do, I would like them to do that, of course, but I think probably a little bit more is required, actually, to encourage people to go and contribute. I don't know exactly what that is. I think we have to work together to figure it out. We're, like, doing experiments in social media. You know, we have a TikTok account, and we're, like, trying to figure out ways of sharing, like, interesting things With people that get them excited about knowledge and wanting to learn more. But-

**Yaron Koren** [55:11]: Oh, interesting. Yeah

**Selena Deckelmann** [55:12]: ... yeah, we, we kind of need a lot of things like that to figure this problem out.

**Yaron Koren** [55:18]: Uh, yeah, okay. Um, are you involved in that kind of thing, the, the, the PR kind of stuff? [laughs]

**Selena Deckelmann** [55:24]: Um, well, I mean, this is, this is a product experiment. I mean, we're working with, like, the comms team on creating these things, but, um-

**Yaron Koren** [55:31]: Oh, okay

**Selena Deckelmann** [55:31]: Yeah

**Yaron Koren** [55:31]: ... there's, there's a, there's technical element to it too.

**Selena Deckelmann** [55:33]: Yeah. Yeah. I mean, we're y- like using AI-generated imagery, um, to do it as well as the voices and, um, you know, just trying to think about ways that we can support, you know, call them creators on these, like, social platforms. How do we encourage them to use, um, you know, Wikipedia articles for example, or images from Commons, and then teach them, like, why this is, like, a cool thing to do [laughs] and why it's, like, helpful to them. And there's actually quite a few creators that do it already. They just don't ever say that they got any of their information from Wikipedia, Commons, like any of our projects. So we're just trying to encourage them to do that, uh, so that we then have a chance of getting somebody that wants to contribute back.

**Yaron Koren** [56:19]: Uh, yeah, that's interesting. Well, yes, uh, uh, certainly Commons w- for anybody who wants, you know, royalty-free, uh, content, um, audio, photos and all that, uh, any creator and so forth, I, I think Commons is, you know, an obvious resource. Um, uh, it's interesting that you mentioned AI-generated imagery in there. [laughs] I don't know if that's controversial at all, but if that's sort- sort of, you know, uh, uh, going in the wrong direction to, to... Uh, is that what you said? That, that, that, that the Wikimedia Foundation is itself using AI-generated imagery in, in the-

**Selena Deckelmann** [57:00]: In those social media experiments that we're doing, yeah.

**Yaron Koren** [57:02]: Right. Yeah.

**Selena Deckelmann** [57:03]: And there's... Um, and if you wanna read more about it, there's, like, tons that's been published on Meta, you know, in working-

**Yaron Koren** [57:09]: Oh, okay

**Selena Deckelmann** [57:10]: ... uh, like feedback from communities, like at each iteration of this. Um, I do think that there are some members, 'cause we, m- members of our communities, 'cause, like, our communities are obviously quite vast, that, you know, wouldn't want us to do something like that. Uh, yeah. But there's also people who really support it and wanna see us find ways of, like, reaching out, um, especially to folks that otherwise are not going to come to Wikipedia, the website, right? They just kind of live in TikTok [laughs] or whatever.

**Yaron Koren** [57:47]: Sure.

**Selena Deckelmann** [57:47]: Um, so, you know, as the world's search kind of goes somewhere else, Google obviously is still the dominant force, like, in the world, but among certain age groups, it's got less and less of that market, and people are spending more and more time on different kinds of social media, especially, like, video-based social media. It's not even TikTok. There's lots and lots of these things. So, um, it's just important to recognize that there's been a shift, and the web is not experienced the same way with somebody that's, like, 18 years old as it was when I was that age.

**Yaron Koren** [58:24]: Sure. Yeah, yeah. No, uh, I mean, people have been, have been talking about this kind of trend since I don't know when.

**Selena Deckelmann** [58:30]: Yeah, for a while.

**Yaron Koren** [58:31]: I don't know.

**Selena Deckelmann** [58:31]: And we're finally, like, trying some stuff out now. [laughs]

**Yaron Koren** [58:34]: Yeah. Yeah. Um, there's another, there's an- another irony to the whole, uh, you know, uh, concerns about the future and so, which is, which at the, the same time that, uh... Well, tell, you tell me if, if it's, if it's ironic or not. Uh, if, uh, uh, at the same time the Wikimedia Foundation is making this concerted effort to, uh, to popularize Wikipedia and make sure it stays up and, and so forth, it... There's, there is a Wikimedia project meant to replace Wikipedia, which is Abstract Wikipedia. At least that's my sense of it. Uh, not to replace Wikipedi- the, the Wikipedia experience, but, but, uh, again, this is my understanding, and I, I f- I feel like I should know by, by now how it actually is supposed to work, but I don't. I still don't really. But, uh, my, my understanding is once Abstract Wikipedia is complete, whether that's, you know, 10 years from now, 20 years from now or whatever it is, uh, they'll, it'll be, you know, fully generated articles in this language neutral way that will then just be translated on the fly to any specific language. So it'll be essentially a completely different content base replacing all of what's on every language Wikipedia.

**Selena Deckelmann** [59:47]: Hmm. [laughs] It's like the dystopian-

**Yaron Koren** [59:51]: I don't know if that's actually accurate. W- what, what, what?

**Selena Deckelmann** [59:54]: It's like the dystopian path, but yes, go on.

**Yaron Koren** [59:57]: Uh, oh-

**Selena Deckelmann** [59:57]: Yeah

**Yaron Koren** [59:57]: ... oh, really? You, you don't... You, you view that as... I mean, it is, it, it's, it is or it isn't, depending on your point of view, I guess.

**Selena Deckelmann** [60:05]: [laughs]

**Yaron Koren** [60:06]: Uh, but I mean, it, the content would still be human-generated and presumably would have a large, uh, commonality with what's already on one or more language Wikipedias. Um, uh, but it's, yeah, so it's, it, it's interesting that you, that you view that as dystopian. I thought that was literally the plan. [laughs]

**Selena Deckelmann** [60:27]: [laughs] Well, I think what's dystopian about it is just, like, that idea of, like, obliterating everybody's work that they've been doing for the last however many years.

**Yaron Koren** [60:35]: Oh.

**Selena Deckelmann** [60:35]: That, that, that's what's dystopian about it.

**Yaron Koren** [60:38]: Okay. I mean, isn't that what's gonna happen though? [laughs]

**Selena Deckelmann** [60:41]: I don't think so. [laughs] No.

**Yaron Koren** [60:44]: Well, so what, what is the-

**Selena Deckelmann** [60:45]: It doesn't make any sense

**Yaron Koren** [60:45]: ... what is...

**Selena Deckelmann** [60:46]: I, I mean, I think-

**Yaron Koren** [60:46]: What-

**Selena Deckelmann** [60:47]: ... I think-

**Yaron Koren** [60:47]: Okay

**Selena Deckelmann** [60:47]: ... yeah, I, so I think that obviously the, um, idea behind Abstract Wikipedia and having, like, an abstract representation of language through functions that are implemented by a new kind of volunteer actually, um, you know, linguists, you know, but people who just wanna, like, learn how to do this, uh-

**Yaron Koren** [61:13]: Right

**Selena Deckelmann** [61:15]: Sure. Like, you can, you can paint a future vision that is just replace everybody's work and everybody can go home and, um, yeah. But I- that is absolutely not the aim of, you know... Den- Denny's been around in this, um, world for a very long time, and I think it's a very ambitious idea, and it's very interesting, and it is a small part of the [laughs] work that we do at the foundation. Uh, and what I would say is, like, I, I don't know if you've ever heard of, like, the Horizons model?

**Yaron Koren** [61:45]: No, I don't think so.

**Selena Deckelmann** [61:45]: It's this idea... It comes from, like, probably some consulting, like, company, like, maybe, like, McKinsey or something. But I think the i- the core idea is sound, and it's, like, this idea of the way that you make investments in an organization is, like, a certain percentage of it is, like, about right now, and then a certain percentage of it is about the medium term, and then a certain percentage is about the far future.

**Yaron Koren** [62:08]: Sure.

**Selena Deckelmann** [62:08]: And I would say typically when I've, like, talked to people about the Horizons model and how to invest, it's, like, 70/25/5. [laughs]

**Yaron Koren** [62:18]: Okay. Yeah.

**Selena Deckelmann** [62:19]: And so, and, and the, the work that the Abstract Wikipedia team, um, and specifically the work that they're doing on Wiki Functions right now, the work that they're doing is very interesting to me, like, on a technical and social, um, point of view. But, you know, in terms of being able to implement something that would potentially replace, you know, the way that content is created today, that's pretty far in the future, and it really is in that, that 5%, um, category. Um, and as far as, like, what might happen in the next, like, three to five years, what would be amazing is if it helped with translation in some significant way. And I think it's possible, but there's a lot of barriers, a lot of things we have to test and explore. Um, there's, like, a couple really beautiful, uh, demos that the team made that you can... I think that they posted, uh, on their... They have a very regular, um, you know, Wiki page updates you can go check out on their work. And it just, like, shows, uh, templatizing, you know, kilometers, uh, to miles. You know, like, h-

**Yaron Koren** [63:31]: Okay, right

**Selena Deckelmann** [63:31]: ... like, a automatic conversion or something like that. Very simple demo, but it had, like, a really nice user interface, and it was kind of cool to imagine, like, what this might be if it were operating at a larger scale. Um, so that's, that's, like, where it's at, and I just think that, like, the doomsday scenario, I think that that would be a silly thing for us to do, first of all. Uh, because the whole, you know, movement, broadly speaking, is based on people coming together to learn about the world around them and then share it. So I don't, I don't think that a scenario where everything is automatically [laughs] translated and no one, you know, has an input other than through functions makes a ton of sense. But I see many practical applications from the work that they've already done, and it's just a matter of does that really, like, work in our environment? I'm not sure, and so we're trying to figure that out.

**Yaron Koren** [64:25]: Yeah. Uh, what you're saying makes sense, but I, I, I literally thought that that was the plan with Abstract Wikipedia, that, um, that, you know, any sentence can be mapped as a combination of functions, like pluralize this word, and then this v- uh, v- this noun verbs this other noun, and that sort of thing. Uh, you pass everything in, and then it outputs natural language in some, in some language, uh, which for, you know, 90% of Wikipedia's, even if you made 10,000, just 10,000 of those articles, it would still be more content than what's on there now. Uh, maybe, maybe I got the numbers a little wrong, but, but, but something like that. Um-

**Selena Deckelmann** [65:10]: Yeah. I mean-

**Yaron Koren** [65:11]: And then-

**Selena Deckelmann** [65:11]: ... it, it is. It can be used that way, and if that's an effective use of the tool, and it's useful to a language community, absolutely, I'm gonna give them those tools, and they're welcome to use them. But it is not, again, like, going back to, like, do I have control on the output [laughs] of RFCs? I don't. Um, and what I primarily do is I work with the language communities as they exist, and I try to support them in the best way I can.

**Yaron Koren** [65:41]: Uh, okay. So [laughs] you... Okay. So n- right. Not your, not your department, I guess. Uh, or I mean, it's, uh, uh, or I, I guess what you're saying is it's up to any specific... Even if those tools, that, that capability exists, it's up to any specific Wikipedia or other, other Wikimedia site to decide whether they want to make use of that.

**Selena Deckelmann** [66:00]: Yeah. I mean, there's just significant governance issues that have to be taken into account in anything that we deploy. I mean, you know that. Every single thing that I deploy has so much oversight. Um-

**Yaron Koren** [66:15]: Sure.

**Selena Deckelmann** [66:15]: So yeah. I, I really think there's... Of all the things in the world to worry about, just for anybody listening, I wouldn't worry about the imminent deployment of Abstract Wikipedia-

**Yaron Koren** [66:27]: [laughs]

**Selena Deckelmann** [66:27]: ... to destroy all of the work that all the [laughs] contributors have done. It's absolutely not what's gonna happen. I think with, with... There's so many challenges with this type of technology. It's slow, you know?

**Yaron Koren** [66:41]: Yeah.

**Selena Deckelmann** [66:41]: [laughs]

**Yaron Koren** [66:41]: Okay. Sure. Sure.

**Selena Deckelmann** [66:43]: So, you know, and I, and I think... And also this idea, um, which Denny will freely admit, you know, I don't know if you've had Denny on recently to talk to him about this, but, um, you know, he, this idea he had before the, you know, these major advances in generative AI have occurred, right? So there's a possibility that some of the problems that Denny was trying to solve might be better solved with, um, a generative model, and he's, like, open to that, honestly. He's, like, thinking about it pretty deeply. But, uh, there's still lots of interesting applications of the tools that they've built.

**Yaron Koren** [67:24]: Yeah. Okay. Yeah. Yeah, no, the last time I talked to him it was, was, you know, more than five years ago. It was still, uh, the whole Wiki Functions was still even in the planning phase at that point. So, uh, it would be in- it would be good to have him back on, um, uh, but it is, it's interesting to... I mean, I, I guess it makes sense that w- that you'd view it dis- as dystopian. Maybe it's the, the, the technologist in me just sees it as, as strictly a good thing to have a single copy of every article instead of, you know, 200. Uh, obviously there's... But, uh, sure, I can see the other side of it.

**Selena Deckelmann** [67:57]: Yeah.

**Yaron Koren** [67:58]: Um-

**Selena Deckelmann** [67:58]: Yeah, I mean, I, I hear where you're coming from. I guess, like, there's, there's real complications in choosing who, and this is a piece of the governance question, right? Who wins? Who gets to be the author, right, of that, that one text that everything else is derived from? Even if it is abstractly represented, there's still a mind in there somewhere, right? And I think-

**Yaron Koren** [68:23]: Sure.

**Selena Deckelmann** [68:23]: Yeah. And that's... Yeah, I think that's, like, an important, interesting philosophical question, and the way that we've answered it so far is by saying that that context matters, that language context matters a lot. And we chose language, which was an interesting choice, right? Chose language, we didn't choose country.

**Yaron Koren** [68:40]: Right.

**Selena Deckelmann** [68:41]: So, um, within that, yeah, there's, like, a lot of, like, philosophical decisions that got made, and I am not ready to undo those. [laughs] I think they're, uh, in some ways problematic, you know, at times, but, um, they're the decisions that were made. So, uh, if we wanna make different decisions in the future, it has to be something that the communities who are, who created that, you know, they, they need to kinda come together and think through how things might change. I think that's possible, particularly with clusters of languages that are related. I bet there will be conversations about, like, ways in which... You know, and that has happened in, in some languages, right? I, it's my understanding that there was a conversation about different Chinese dialects, different points and different, um, uh, you know... I'm, I'm gonna get this, like, totally wrong and botch this [laughs] but there, there have been conversations about different, um, dialects and different scripts, and then decisions to come together, you know?

**Yaron Koren** [69:44]: Sure. Yeah, yeah. How, yeah, what's w- how different does it have to be to, to count as its own language? Th- that sort of thing.

**Selena Deckelmann** [69:50]: Yeah. And I, I just, you know, I, I think that that is something that the communities come together and decide. It's not something that I decide through, um, abstract Wikipedia. [laughs]

**Yaron Koren** [70:04]: Sure. Uh, yeah. Uh, well, all right. Um, that seems like a good place to, to wrap it up. Uh, uh, that was, uh, very interesting to, to hear your, uh, thoughts on all of this stuff, uh-

**Selena Deckelmann** [70:17]: Yeah, thanks for having me

**Yaron Koren** [70:18]: ... and, uh, yeah. Thank you, Selena. It was great talking to you.

**Selena Deckelmann** [70:22]: Yeah. Great to talk to you. [outro music]

**Yaron Koren** [70:29]: And this has been another episode of Between the Brackets. I wanna again thank my guest, Selena Deckelmann, who's chief product and technology officer at the Wikimedia Foundation. Thanks to all of you for listening. I'll see you next [outro music]

