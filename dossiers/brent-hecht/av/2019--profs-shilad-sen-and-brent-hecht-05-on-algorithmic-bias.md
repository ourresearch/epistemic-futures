---
title: "Profs. Shilad Sen and Brent Hecht '05 on Algorithmic Bias"
person: brent-hecht
section: by
type: talk-transcript
year: 2019
venue: "Macalester College (YouTube)"
source_url: https://www.youtube.com/watch?v=s-97c35DdvA
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 56
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Profs. Shilad Sen and Brent Hecht '05 on Algorithmic Bias

*Speakers (inferred):* speaker_0=Host, speaker_1=Brent Hecht, speaker_2=Shilad Sen

## Transcript
**Host** [00:00]: Uh, we have two distinguished computer scientists and a Luddite English professor.

**Brent Hecht** [00:05]: [laughs]

**Host** [00:06]: Uh, so we'll see how this goes. Um, first of all, thanks to both of you for, for being here. We really appreciate it. Um, let, let's start with, with the very basics. So define for us an algorithm, and then maybe talk about how an algorithm is defined in your discipline, uh, how do computer scientists, computer engineers think about algorithms?

**Shilad Sen** [00:32]: So, uh, computer scientists have a very specific and, uh, narrow version of the definition of an algorithm compared to the general public. So the, the, uh, metaphor we use most regularly is that an algorithm is like a recipe. It's a series of very explicit steps, um, that you follow to achieve some goal in service of some problem. Um, that is different from the way it's used in the general public. Uh, in the general public, um, people would think of, uh, algorithmic advances or algorithms, um, as technology, uh, that's advancing in some way. So any technological advance, I think you might think of as an algorithmic, uh, advance in, in the general public.

**Host** [01:20]: Hmm.

**Brent Hecht** [01:21]: I think that's fair. I think the colloquial term also has a particular resonance with the idea of, um, intelligent technologies that are based around, you know, large scale datasets and these types of things. When we talk about algorithmic bias, that's actually what we're talking about, um, with regards to algorithm. And when, when you hear that an algorithm's gonna automate you out of your job, that's generally what you're talking about as well.

**Host** [01:42]: So when we're asking the question tonight, are algorithms, um, essentially making a positive or negative contribution, we're really... We're not, we're not asking about what the recipes are.

**Brent Hecht** [01:51]: Yeah. [laughs]

**Host** [01:52]: We're really talking about algorithms as they're being applied today to, to technology.

**Shilad Sen** [01:57]: Right.

**Host** [01:58]: Um, so give us a sense of how each of us on a day-to-day basis would come into contact with the kind of algorithms that, uh, computer scientists, computer engineers, uh, work on and develop. Where, where do we, where do we touch those?

**Brent Hecht** [02:19]: Well, I think a, a better question in some ways is where don't we touch them at this point? Um-

**Host** [02:24]: You're correcting my questions already? [laughs]

**Brent Hecht** [02:28]: Sorry. It's the, uh, the curse of the professor, I guess. Um, the, uh, uh, one amazing thing of working in this field, and one thing that's very scary about working in this field is that, uh, the products of the field touch all aspects of our lives. So on a day-to-day basis, um, how you, uh, go from point A to point B in your car, it's an algorithm. If you use Google Maps or Apple Maps, an algorithm is telling you physically where you're going in the world. Um, if you're using, um, uh, Google Search to look something up on the internet, that's, you know, one of the world's most famous, um, algorithms in, [laughs] in a, in a broad sense. Um, I also like to remind folks that, uh, these days it's not just the day to day, it's the... it's highly influential life decisions. So, um, are you gonna get a loan for your house? Um, are you going to get an interview for that job? Uh, who you might date and then marry using a recommender system on Tinder or match.com, these types of things. These are all, uh, uh, informed by and, and, um, uh, migrated through algorithms.

**Host** [03:34]: Mm-hmm. So, um, one would think, I think, that since these are done by computer, um, that there would be something unbiased about them. Um, but both of you do work in the area of algorithmic bias. Uh, so I wanna dig into that, uh, because it seems to me that really gets at the center of the question we wanna explore. So, so talk about how you discover in your work that these algorithms really intersect with human bias and with the various kinds of inequities that exist in society broadly.

**Shilad Sen** [04:18]: Yeah. So, uh, one thing that I like to think about is, uh, an algorithm as part of a life cycle, and it's a life cycle that starts with, uh, typically in the systems we're talking about, data that an algorithm is gonna be learning from. Um, and so you can start by looking at that, that data and asking, is there, uh, biases present in that data? And we've both done, you know, separately and together various research on this, um, looking for, uh, data in the types of, um, uh, uh, bias in the types of data these algorithms learn for us. So one big example of this, uh, would be Wikipedia. Um, and you think of Wikipedia as a resource for humans, and it's actually, I don't know, would you say the primary resource for algorithms?

**Host** [05:08]: All right. How many, how many students in the audience have used Wikipedia?

**Brent Hecht** [05:11]: [laughs]

**Shilad Sen** [05:12]: Right. Right. And so algorithms also use Wikipedia, um, tremendously. So if you're an algorithm and you have to reason about the world, um, you need some knowledge to reason about that world, and there's really no, um, better first source than Wikipedia. And so if you look at Wikipedia, we've done some of this work, um, for bias along geographic lines, gender lines. What else have you done?

**Brent Hecht** [05:39]: Um, there's some work on political bias in Wikipedia. Um, there's work on, uh, uh, content type bias broadly speaking.

**Host** [05:50]: So give, give me an example of how you would see something like gender or geographic bias in Wikipedia. Would... How would that manifest itself in the work that you do?

**Brent Hecht** [06:04]: So I would say, so picture yourself as an algorithm. We'll have an-

**Host** [06:06]: [laughs]

**Brent Hecht** [06:07]: -an exercise here, and you're saying, "Okay, this is exactly what Shiloh was mentioning. I need to learn about the world quickly because I need to, for instance, uh, tell my, uh, human overlord [chuckles], you know, what the relatedness is between two concepts," is an essential idea in so many underlying systems. Anytime you search, they're accessing this type of question. Um, some deal with Wikipedia and say, "You know what? Uh, I think English Wikipedia is the, is the biggest Wikipedia. This seems like the one I should go to." Um, okay, so how related is, uh, peanut butter and jelly in the English Wikipedia? Well, for English speakers, incredibly related. But those of you from, uh, other, um, uh, language regions will know that, uh, A, you might ask, what on earth is peanut butter, right?

**Host** [06:50]: [laughs]

**Brent Hecht** [06:50]: And B, is that peanut butter and jelly? That's disgusting, right? It's like savory and sweet all together in the same sandwich. I don't know what you folks are doing. And, um, some of the work I was fortunate enough to do in my, you know, PhD thesis and, uh, surprisingly large number of years ago, about ten years ago now, um, was, uh, able to uncover that by relying on these human-generated datasets where these machines, very transparently and with a large effect size, adopt the cultural context of the humans that they're learning from, right?

**Host** [07:19]: Mm-hmm.

**Brent Hecht** [07:19]: And that cultural context won't be surprised to anyone, uh, surprise to anyone connected to the CalSTR community. Although it was a huge surprise to the computer science community, uh, that cultural context includes some things that we don't like.

**Host** [07:31]: Mm-hmm.

**Brent Hecht** [07:31]: It includes racism, it includes, um, a desire to focus on oneself versus others, um, and all sorts of, uh, other uncomfortable things that the computer, uh, we're now seeing in the media, these types of things, um, tends to absorb. So, uh, that adventure, uh, of sort of, of helping to uncover some of these issues was, was an exciting one, i-in part because I, I think it goes to some of the issues we'll be talking about the rest of today, which is the blind... broadly speaking, the blind spots that we have in the computer science community-

**Host** [08:03]: Mm-hmm

**Brent Hecht** [08:03]: ... and how that's created some of the problems that, uh, people are, uh, perceiving in algorithms today.

**Host** [08:09]: So how much does it matter that most of the people who are doing this work are white and male?

**Brent Hecht** [08:14]: A lot. Um, it, uh... as a white and male person myself, it was a, an interesting thing to be one of the first people to point out that this peanut butter and jelly effect occurred. I think there was a, an assumption that, oh, everyone eats peanut butter and jelly sandwiches. Of course, these are related, the machine is correct, right? Think about all the other blind spots that aren't being noticed by, by folks at, you know, every time they're, uh, beta testing and debugging, um, these types of, uh, software. I think that is a, that's a dramatic effect. We've seen that actually in our work with respect to urban and rural areas.

**Host** [08:52]: Mm-hmm.

**Brent Hecht** [08:52]: There are a lot of assumptions made by urban programmers that don't apply in rural areas, resulting in worse performance in rural areas.

**Host** [08:59]: Mm-hmm.

**Shilad Sen** [08:59]: And the thing I would add to that is it, it may not matter so much on an individual level. You know, um, an individual white male can make strong contributions in this area. But when you have an entire industry, uh, that is kind of devoid of, uh, of, of women or underrepresented minorities, then, um, that changes that culture of the industry. And, um, at, at least tech has recognized that and is working towards it, but there was a long period where no one really talked about it.

**Host** [09:33]: So give me an example of a really significant consequence of some of the biases that are built into these algorithms. So you... the, the peanut butter and jelly example is very clear. Um, but in, in the most serious sense, how might some of the results spit out by these algorithms actually have effects on people's lives that reflect maybe some of these larger biases? Is it we see it through criminal justice system? Do we see it through education? I mean, in, in which of these big areas do we really begin to see the effects of, uh, these algorithmic biases?

**Brent Hecht** [10:15]: So I'm on the board of a, a conference called, uh, FastAR, which is, uh, uh, the, the name is, is, uh, somewhat unfortunate, and we're actually thinking of changing it.

**Host** [10:23]: [laughs]

**Brent Hecht** [10:24]: But it is the premier-

**Host** [10:25]: FastAR?

**Brent Hecht** [10:26]: FastAR. It's the premier-

**Host** [10:27]: What does that stand for?

**Brent Hecht** [10:27]: Fairness, Accountability, and Transparency in Computing. It's the premier place you publish this type of research. So I've been privileged enough to engage with an amazing array of, um, fascinating and almost always very depressing research on that front. So you mentioned criminal justice. A very famous case right now, um, surrounds an algorithm that is used. So at, at... this is actually some, some I'm sure it's discussed in the CalSTR community. Bail is a, is a controversial thing, right? You, you know, people... it, it advantages certain types of people. It disadvantages other types of people. So some folks are trying to replace bail with an algorithm that says, "Is this person gonna... going to commit another crime, uh, while, you know, not detained before trial?" Um, and they fed in all sorts of things. They did not feed in the race of the person. Um, and they developed a model that, uh, they found to be somewhat predictive or, or quite predictive. Well, it turns out this model was, um, putting people in, uh, holding people who wouldn't, who shouldn't be held, uh, and doing so at a rate much higher for African Americans than for white people. So in terms of high impact algorithmic bias, I can't really imagine-

**Host** [11:40]: Mm-hmm

**Brent Hecht** [11:41]: ... anything more than the, the state exercising its power through an algorithm to keep someone detained.

**Host** [11:46]: Mm-hmm.

**Brent Hecht** [11:46]: That situation is an extraordinarily complex one, and we might touch back on it, it later. Um, but that is definitely a high impact case. Another one of my colleagues was, you know, at, at the FastAR conference, we're sitting on the floor, you know, trying to do some organizational stuff because we're in charge of making the whole thing, whole thing work. I'm sitting on the floor with the general chair, just casually mentioned, "Yeah, you know, I, I had a, a, a... publishing a study, you know, next month that finds that computer, um, vision systems that detect pedestrians that are being deployed in autonomous vehicles detect white people better than Black people." And that's another case where the, in terms of, uh, an impact on someone having a ca- an autonomous vehicle run into you more often when you're African American than when you're white, that's, I can't really... That's the, that's the top of the scale.

**Host** [12:30]: Mm-hmm. So both of-- We've talked about the fact that both of you were pretty early, um, uh, in pursuing this line of research. Uh, talk a little bit about the reception that at least initially you got-

**Brent Hecht** [12:46]: [laughs]

**Host** [12:46]: -within your discipline or within your disciplinary community.

**Shilad Sen** [12:49]: I remember writing some papers with you early on, and how... I can't... The number of hours we struggled with trying to write intro- We would write the introduction over three or four or five times because, um, you had to make such a careful argument that, uh, and this was probably five years ago, algorithmic bias was a real thing, um, and it w-was a real thing that impacted the world in meaningful ways. Like, it would have all these externalities. Uh, and so we would kind of collect examples and, um, and we've, I think we had one paper outright rejected by a reviewer who thought, "You know what? Th-This isn't a real thing."

**Host** [13:29]: This isn't a real thing.

**Shilad Sen** [13:29]: And another person said, "This is not computer science." Uh, uh, so now, now that would not happen. It's, it's very different now.

**Brent Hecht** [13:40]: In fact, I, I had a, a funny, uh, uh, happening this summer where I, I dusted off some old slides about some of my, uh, Wikipedia work and extending it to some of the work that Shalard and I have done together. And I used the same introduction I used maybe six years ago. Someone, someone thought I, I had spent... It was painstaking how I articulated how important this stuff is and, and how, uh, oftentimes you have a situation where people would say, "Oh yeah, I imagine that would happen, but the effect size, you know, it's not gonna have any meaningful effect on anything." So I spent forever writing these slides and I dust them off, and someone raises their hand and says, "Uh, the first ten minutes, they seem pretty obvious." [laughing]

**Host** [14:19]: Yeah. The world, the world's shifting quickly. And what is bringing about that shift? I mean, what, w-what... I mean, that's a pretty short timeframe, but with the discipline in which you work, things happen pretty fast.

**Shilad Sen** [14:29]: Mm-hmm.

**Host** [14:30]: Um, so are there, are these external things in the world that have changed the way that your intellectual community thinks about this? Is it the work that people like you have been doing that has begun to change some minds? What, what has happened to make the work that seemed almost unacceptable five years ago seem, at least to some people, pretty obvious now?

**Brent Hecht** [14:52]: So I have a, a pretty con... I, I have a co- pretty strong hypothesis, and it's the 2016 election.

**Host** [14:59]: Hmm.

**Brent Hecht** [15:00]: So I have a colleague named Moshe Vardi who describes that as a sea change in terms of how people perceive technology. Of course, there were issues in there, misinformation, um, filter bubbles, uh, the fact that people communicate through email, which is vulnerable to security concerns. All these had dramatic effects on something that's very important in our lives. But it kind of opened the box to everything else that was ready to be discussed-

**Host** [15:22]: Hmm

**Brent Hecht** [15:22]: ...in, uh, in society. And I, I think that's correct. But it, it's been amazing how, um, my area, which was once a niche and, um, had, a-and we had to spend a lot of time on introductions, now we don't have to do that, and the challenges have become quite different.

**Host** [15:39]: Hmm.

**Brent Hecht** [15:39]: Um, it happened in three or four months after the, the 2016 election.

**Host** [15:44]: Interesting.

**Shilad Sen** [15:45]: The other thing I would say is that, um, there's just so much more data about individuals now, and, and, uh, uh, correspondingly, algorithms are much, uh, more sophisticated in their use of that data, that people are, uh, encountering these types of situations where bias could really, uh, affect whether they can unlock their phone, for example, um, much more regularly than they have in the past.

**Host** [16:13]: Mm-hmm. So, um, let's broaden it, broaden it out a little bit. One of the things that the three of us talked about when we talked last week was this fundamental question that really interests me. I think, I think, Grant, the way you put it was the distinction between can and should. Uh, and as I, as I mentioned last week, I can't, I can't help but throw in a little of my English professor background, uh, and think about, uh, the very influential novel Frankenstein. So Frankenstein is essentially, um, which was published in 1818, is essentially the story of a brilliant scientist who has the ability to do something technologically that has never been done. Uh, he has the ability to create life out of non-life. Uh, and he does it because he can do it, and he imagines that in doing it, uh, he will become a savior of the world. He will be worshiped as a hero. He will change human life forever for the better. Uh, and what he doesn't spend any time thinking about are the ethical, moral, and practical consequences, uh, unintended, uh, of the work that he's doing. Uh, and so what starts out as this glorious idea turns into a disaster, uh, for him and everyone else around him. Uh, and I, I think about that novel often when I think about where we are with technology now, uh, and this question of whether because we can do something does it necessarily mean that we should do something. So where, where do you think we are now in the field of... The, the, the... You work in a broad array of fields, in, in computer programming, social media. There's a whole nexus of things that relate to this. Um, but has that question of can versus should, um, become one that the people who work in the field of technology think about now?

**Shilad Sen** [18:28]: I, um, so I feel like that type of change-- Like, how will that change happen? Why, why would companies be incented to make those types of changes? Um, it feels like they would be incented to make those changes because they're worried about their brand. Or, um, the other way that I think is actually more likely, and maybe speaks towards the people in the room, they make that change because the employees, um, who work there want those changes to be made, and it's very difficult to find, um, talented and, and capable tech workers. So those feel like the two incentive structures. I guess consumers can exert power as well, and we've seen that eminent. Um, but I, I personally feel, uh, like the fastest vehicle for change is v-via the employees. Like, tech employees exert incredible leverage right now. Um, and, uh, uh, McAllister students are working in lots of these places, and I've seen many of them make changes in, in, uh, in companies. So...

**Brent Hecht** [19:38]: You know, I think to get into the mind of, of a computer scientist or, or practitioner in our field at least five years ago, was to get to like a, a massive "Can I do this?" machine. [laughs] So it's ki- I think those of, those of us in the room who... I think this is the broader engineer instinct too. Those of us in the room who, um, who, who work that way. I, I have it in my myself. Like, I, I have this idea. I really wanna see if I can build it. Uh, it, it's just, it's, it's a, almost a subconscious drive. Um, I will say though that I, I was lucky to choose to go to McAllister and to engage in, in the education at McAllister, um, that I think activated at least part of me that was in, in the, uh, should we mode.

**Shilad Sen** [20:27]: Mm-hmm.

**Brent Hecht** [20:27]: And I think the population of us is, is growing.

**Shilad Sen** [20:31]: Mm-hmm.

**Brent Hecht** [20:32]: Um, so the people who can actively walk away from a really cool idea or, or a money-making idea because they think down the line and they say, "You know what? That's not something I think I wanna do. I'm gonna have to come up with a different really cool idea, a different really big money-making idea."

**Shilad Sen** [20:48]: Or even I'm gonna have to pause and spend some time thinking about, um, how I should help people think through the, the use of this new technology. Like, it doesn't always mean that you shouldn't introduce a new technology. It might mean that you should take a moment and kind of gather your thoughts about how it's gonna be used. And this is something that you've, you've talked about publicly before.

**Brent Hecht** [21:11]: Yeah, you're exactly right. So the, um, uh, I teach a class called Algorithms in Society, and one of the first things I say in that class is, "You're gonna have an instinct to tell me to go away because I'm reminding you of problems you don't wanna think about, and you're gonna have an in-instinct to throw your mobile phone in the garbage." [laughing] "And then maybe your, your, uh, uh, you know, computer as well and just run away," right? Um, neither of those solutions are realistic. Neither of those solutions will lead to the best outcomes. So a should-- The can we versus should we dynamic is a bit flawed. Um, I... It's one I use quite frequently in that, uh, there's a way for us to say, "Can we do this? No, not now. But if we make these three changes, then maybe..." Sorry. "Should we do this? No, not now. But if we make these three changes, then maybe, um, we should." And as a remind to get people excited or remind my students, um, those three changes might involve some really cool new can we problems.

**Shilad Sen** [22:08]: Mm-hmm.

**Host** [22:09]: Now, we don't have a great track record as a species on this question. [laughing]

**Shilad Sen** [22:13]: No, we don't. [laughing]

**Host** [22:15]: I mean, typically, wh-when there is a technology available, um, that can make people money, uh, and do something that hasn't been done before, there's always someone who's gonna do it. Uh, whether it's technology that can be weaponized, uh, or technology that can burn fuels, whatever it is. So do you have any optimism that this sort of freight train of technological advancement, um, that kind of get-- is getting out ahead of our, of our thoughts about, about should we, about ethical implications, about other implications? Do you have, do you have any, any optimism that it can be slowed down?

**Brent Hecht** [22:58]: I don't think it can be slowed down. I think the best mechanism is what Shalal was, was mentioning, diverting.

**Host** [23:04]: Mm-hmm.

**Brent Hecht** [23:04]: And take that fast moving [chuckles] freight train and move it a little bit in this direction.

**Host** [23:08]: Mm-hmm.

**Brent Hecht** [23:09]: Um, you know, I've been-- One of the more stressful experiences in my career at is-- has been, um, trying to change incentive structures in computer science research, uh, along those lines, taking that freight train and moving it in a slightly different direction. Uh, I, I'm actually curious how this audience will perceive this. I was part of a group that proposed something that turned out to be very controversial, and that was that instead of just focusing on the positive implications of a given contribution of a research paper in the introduction of a research paper and these types of things, that authors also, uh, be, uh, required to think about the possible negative implications of that contribution. So if you're some-someone who's doing work in the space of what's known as generative media, which is, uh, using machine learning to... You may have seen this on, on the internet to, uh, simulate President Obama saying something he didn't say or doing something, uh, you know, equivalent with, with video. That those papers, you know, discuss the, the potential negative implications of, of that type of, of work. And the analogy, I think, to medicine is pretty strong. It's as if we introduce a drug that has some positive effects, but has, in many cases, extraordinarily der-deleterious side effects, and we just don't mention the side effects.

**Host** [24:19]: Mm-hmm.

**Brent Hecht** [24:22]: Um, so, uh, has that-- That process is maybe a little more pessimistic given the amount of pushback we got, but we have had some, some, uh, um, uptake of our proposal.

**Host** [24:30]: So to, to use, to use the, the comparison to, to medicine or to pharmaceuticals- Does the answer ultimately lie in regulation? I mean, do you need the equivalent of a, of a consumer protection bureau or s- or the, a bureau that reviews... the FDA that looks at drugs and says, "No, here are the, here are the possible negative consequences. You need to specify that"? And we also don't have a great record of government-

**Shilad Sen** [24:56]: Yeah

**Host** [24:56]: ... doing those things particularly well.

**Shilad Sen** [24:57]: We- we've, uh, we- we've ta- I've talked about that. I mean, I- I... It's possible. Um, I feel like if there's legislation, it'll be about process rather than specific policies for specific technologies. It's hard to imagine specific policies keeping up with technologies, but maybe a process that's required. I-- This... But this... One thing this reminds me of is, um, another... a, a line of research we've been working on that's really closely related to this question, is thinking about ways that consumers can, um, leverage more consumer power, um, in specific algorithmic ways. Um, and so one thing that we've both been looking at recently is, uh, thinking about the data that you provide to tech companies, um, and the value that that data has for those companies, and the ways in which you can leverage just that data. Forget about your consumer buying power, um, uh, in, in ways that might reduce... So if you take... If you're... If you stop posting, um, or on Facebook or clicking links or on Google, um, you can, uh, reduce the performance of the algorithm for you. But if you take your data and walk, you can reduce it for everyone else. Uh, and so I guess the greatest source of optimism I have is that I can imagine a path, um, in which, uh, people are a little bit more aware of, of the value they're providing to these companies and able to exert power using that value in collective ways. It's complicated. It feels k- like there's a lot of steps between where we are now and where we are there to get there, but it doesn't seem impossible.

**Brent Hecht** [26:51]: Yeah. I think you're exactly right, Shola. That's... That is something I guess... We're both really excited about this idea. This, this paper we just had accepted, um, introduces the, the notion of a data boycott and a data strike. And these are ways for us to leverage-

**Host** [27:07]: I'm already there, by the way. [laughing]

**Brent Hecht** [27:10]: You're engaging in a data boycott. [laughing]

**Host** [27:12]: It's just ignorance. [laughing] So that's... So tell me what that means.

**Brent Hecht** [27:17]: So this, this just, uh, uh... I love this just as a, as a... just something to think about. Um, when we walk into, you know, my cousin and I up there, we're gonna go shopping on Saturday because he's the guy who I know who can help me actually, actually, you know, get nice clothes as a computer scientist. [laughing] Uh, we're gonna walk into the store, and we're gonna buy something. They, you know... We... If we decided that we didn't like what the actions and beliefs of that store owner is, right, we just not go to the store, we'll go somewhere else, and we... that store is hit by our consumer power. Turns out in the technology world, we actually have more power than just consumer power. We have this, what we call data labor power. We call it data labor power because unbeknownst to all of you who don't currently receive a paycheck for, from Google or from Amazon or from Microsoft or any data-driven company, all of you actually work for these companies generating data at all times. So you're clicking on links from Google. You're click- you're liking things on Facebook, and that is extraordinarily valuable data when viewed in aggregate, when viewed collectively, uh, that, uh, actually some economists say is much more valuable than the software engineers that work at these, uh, companies. Um, so if you are, uh, if, if instead of, uh, um, shopping at a, at a clothing store, you're thinking about protesting at a technology company, when you walk away, you not only bring your consumer power, you also bring your labor power. You take away your labor power, right? And if you do that collectively, uh, you're performing what we call a, a combined data strike and data boycott 'cause you're striking, you're not doing the work, and you're also boycotting using your consumer power. And the really cool aspect of, of this stuff is that it's as if you could boycott like Papa John's or something like this, and by boycotting you would reduce the value... You would make the pizza taste even worse to the people who aren't boycotting. [laughing] Because you're reducing the, the value of the algorithm. You're reducing the effectiveness of the algorithm.

**Host** [29:07]: Is it possible to do that? [laughing]

**Brent Hecht** [29:10]: I'm sorry. I'm sorry.

**Host** [29:11]: We've actually, uh, played around with that analogy, and I walked away in, in part because of some of these, [laughing] these jokes that might manifest.

**Brent Hecht** [29:19]: But that's really crazy. It's like you can... You essentially by boycotting would make that clothing store have worse clothes, right? It's... It, it is an, an increased amount of power and, and, um-

**Host** [29:29]: So, so is the answer then... I mean, let's stick with the, with the example of clothing. Is, is the answer to do less buying of clothing on Amazon, uh, and more buying of clothing in a local men's shop so that Amazon is... And every time you buy something from Amazon, it's just so clear that they're using that data that you give them. You go and you buy a sweater somewhere, and then every time, no matter what website you go to, ads for sweaters pop up in about five minutes.

**Brent Hecht** [30:01]: Right.

**Host** [30:02]: Uh, so you're g- you're giving... And so is, is that part of the answer?

**Shilad Sen** [30:07]: I, I th- uh, I... There's a whole, whole series of steps I think that are part of the answer. That one I feel like, um, this is maybe a question for the economists, but I feel like it's important to have options. Um, because y- if you want to do a data strike, you wanna have somewhere where you can go, um, alternatively, um, alternatively a- and have business, um, with them. And, and that business should be a place who aligns with your values, right? So I think to the extent that this small, uh, business aligns with your own personal values, um, it's important to have those small businesses. But I also feel like if... as long as you have, uh, some kind of competition, um- That you probably have enough leverage in that, in that marketplace

**Brent Hecht** [30:53]: But I definitely agree. And one thing I'd add to that is actually one nice thing about this data labor power that we all have is, um, you know, I haven't thought enough about the, the discussion about whether or not these companies are monopolies and, and what-- if they are, what to do about it. Uh, so I, I can't speak with a great deal of expertise there. But I can say though that our work suggests that even if they are, this fact that we're all working for these companies as well gives us the power to, to take action even within, even within a monopolistic context. So if, if, uh, I'm upset with company X, and company X is the only company that I can use for some service Y, right? Um, I can s-still use that service, but I might not rate products on that company's website or, or I might use private browsing mode instead of, uh, allowing everything to be tracked and providing, um, some, uh, value in my data labor in that way.

**Host** [31:49]: Is private browsing mode really private?

**Brent Hecht** [31:52]: That's a complicated question. [laughing] No. In some ways, yes. In some ways, no.

**Host** [31:57]: So this, as I expected, went really fast. But I wanna ask one last question before we open it up to the audience. And it, it sort of circles back to, to Macalester and to the work that both of you do as teachers. Um, as people who think about educating the next generation of computer scientists and computer engineers, um, what do you think about doing as teachers that will produce different outcomes, that will produce more people who do think about things like can versus should? And, and, you know, is-- You both in different ways teach in liberal arts settings, big university, small college, but both, both liberal arts. Is that... I mean, i-are there things that we can do in that setting that will produce different results ten years from now?

**Shilad Sen** [32:46]: Yeah. A-I, I think, um... So I think the computer science classroom at Macalester, whether that's for students who are taking introduct-introductory classes and are, you know, psychologists or majors who are taking their upper-level classes, um, are really different from a traditional computer science classroom. I mean, these are questions we talk about every day is... Where's Aaron Larson? Yeah, so Aaron took a... When did you take your first-year class with me?

**Host** [33:20]: Twenty ten.

**Shilad Sen** [33:21]: Twenty ten. How much of class time do we spend talking about these things?

**Host** [33:26]: Um, ninety percent.

**Shilad Sen** [33:29]: [laughing] So, I mean, Macalester students... And, and, I mean, I'm making that sound like it's about the curriculum, but it's at least as much about the students who are drawn to Macalester. I mean, they come to Macalester to learn computer science a little bit, but they come to be part of this global community. They come with this sense of, um, that-- of wanting to give back to the community, of wanting to do good in the world. And so, uh, there-- I, I say this, uh, regularly to lots of people. There is no one in the world who is better equipped, um, to handle these problems and to engage with them than the students that we graduate. I mean, they have the deep technical knowledge, but they also are, um, trained and passionate about thinking about how these, uh, technical skills relate to what's going on in the world.

**Brent Hecht** [34:18]: I, you know, I completely agree. One reason, uh, I agreed to do this is I was at Macalester giving a talk in, in October, and I met with some students. And, uh, the students expressed some concern to me that they, you know, because they had to take classes on, you know, they had to learn about Frankenstein in their, [laughs] in their English classes, and they had to learn about social science, which I think is just incredibly important for almost all computer scientists to know about. Um, and they have to, you know, learn music and, and all these types of things, that they're behind their competitors who, who go to places like at Carnegie Mellon or, um, you know, a large, uh, public university that-- where they're just like engineering class after engineering class after engineering class. And suddenly a light bulb went off in my head. I was like, "No, no, you folks, you folks are right exactly where you wanna be for the next five to ten years. You are gonna come out with good enough technical knowledge. You're all super bright. You're gonna get great training. You'll be able to figure out, you know, technical knowledge has a, is a, has a, a diminishing returns over time slow, right? So you'll be able to figure stuff out, but you're gonna have the secret sauce of ha- being able to integrate that meaningfully with what you've learned in social science, what you've learned in the humanities." Um, and that makes me incredibly bullish on the, the future of, uh, the Macalester approach to education. And I've been reflecting on that actually in how I teach my Boston classes as well.

**Host** [35:38]: Well, on that high note, we're gonna turn it over to you, uh, for questions.

**speaker_3** [35:42]: Obviously, uh, much of the use of algorithms in the computer world is targeted marketing, selective marketing. Uh, find out somebody, uh, is ordering seeds, they'll get seed advertisements thrown at them. But, um, there's been some controversy lately about housing and targeted advertisements, uh, which are leaving out large swaths of the population because they don't fit the, the, uh, um, perceived type of person they want in that housing. But I, I wondered if that kind of selective marketing via computer algorithms is really any different from, uh, say, advertising in a, in a s-magazine aimed at a particular audience. Is, is somehow the use of computers changing, uh, whether it's ethical or not to, to have selective marketing?

**Brent Hecht** [36:51]: The mechanism behind that almost certainly is the desire to scale a solution to a problem. So we wanna do targeted advertising, you know, we wanna do it in a general sense, so it'll apply to any domain. Housing's a domain, let's go for it. And then we have this emergent mechanism, which I argue now we should be responsible for predicting or knowing about ahead of time, uh, that almost certainly wasn't thought about [laughs] ahead of time. And then you, you see a substantial amount of, um, what looks like illegal behavior, you know, a-as a result.

**Shilad Sen** [37:22]: Mm-hmm.

**Brent Hecht** [37:22]: Um, with respect to, uh, how that differs from a magazine, a magazine is human understandable, and a magazine operates at a much smaller scale. So even if there is an issue, no pun intended, um, it's gonna happen, uh, in one is- in one, you know, one edition of the magazine. Um, and then secondly, uh, it's gonna happen in a way that's super legible to all sorts of people in the process. So, you know, um, if a magazine were to do what I imagine the effect size was for Facebook, it would be just obvi- just, just transparently obvious.

**Shilad Sen** [38:05]: Yeah. The other thing I would say about that is, uh, a magazine is just a much more explicit choice all around. I mean, you have to do nothing in order to receive micro-targeting on Facebook, right? You just do your, you know, usual thing, and it naturally happens. So that... It, it's just, just much more pervasive because of that.

**Brent Hecht** [38:25]: So I think to summarize, it's a difference in scale, not a difference in, in type, I would say. Scale and, and effect size. Which is often the case for criminal stuff, right? So jaywalking versus, you know, running across a, a freeway and causing all sorts of problems.

**speaker_4** [38:41]: So you mentioned the, uh, 2016 election. And I'm curious as we come into it, now the next election season, if there's anything that the computer science community is doing preemptively to raise the flags if something goes haywire again. I'm just curious if there's anything, you know, kind of traps, mousetraps that could be set up.

**Brent Hecht** [39:07]: Number one is the, some of the underlying structures that created some of the problems in 2016 are s-still there. So when you're consuming media around your political choices, put on your adult hat [laughs] uh, and say, "Is this media something that's confirming my existing priors? Is this media something that I, um, is it from a truly trusted source before I incorporate the information?" I taught the, the Russians have a seven-point recipe for spreading disinformation. I taught that in class, and was able to fool my students in the first two minutes of class using the recipe based on their existing priors and they studied them. So that's, that still exists. That's still gonna be a, a problem. I'm optimistic in that the mistakes of, of the 2016... Some of the mistakes of the 2016 election already had technical, partial technical solutions. So email security. Email security was a defining issue [laughs] in the 2016 election, which is, which is crazy to say out loud.

**Shilad Sen** [40:09]: [laughs]

**Brent Hecht** [40:10]: Um, but, uh, I imagine that any candidate worth, uh, her or his salt in 2020 will have that locked down using best practices. [laughs]

**Shilad Sen** [40:19]: [laughs]

**Brent Hecht** [40:20]: Um, so we're always fighting the last war. I feel like some of, or, uh, or what's the expression? We're always fighting the, the current war with the last war's weapons or something along these lines, right? That is, you know, part of the, the case here too. Um, so there's all sorts of new things that, that might come up. So I'm like 90% pessimistic and 10% optimistic, I'd say.

**Shilad Sen** [40:46]: Yeah. [laughs]

**Brent Hecht** [40:49]: Do you have any-

**Shilad Sen** [40:50]: The other... Well, the other reason for optimism is I think a lot of people when that happened moved into that space. And so, um, even though we aren't experts in that space, there are people who are experts and, you know, they've de-dedicated their lives towards that. And, uh, maybe w-we were different about this, but I just did not foresee the extent to which that was possible, the election manipulation. And now that we've seen it, um, people are more aware of it and worried about it on the research front.

**Brent Hecht** [41:25]: Unfortunately, there's a finding in research that if you make people aware infor- 'cause if you make people aware... If you tell people that information is disinformation, it might actually have the inverse effect that you want it to have because of some of the flaws in human psyco-psychology. It's one reason why people say Russian- Russians hacked, but they didn't hack the internet. They hacked humans' brains, right?

**Shilad Sen** [41:42]: Mm-hmm.

**Brent Hecht** [41:43]: These are all vulner-vulnerabilities that we have. Um, and it's actually something with, with my students who are, you know, significantly on the left side of the political spectrum, they think they're immune to it because of the nature of the attacks in 2016 election, and it's not at all the case. Like, someone tells you, uh, all sorts of good Trump disinformation out there right now, for instance, because it confirms existing priors. It's something that will, you know, will, uh, enhance, uh, tribal feelings in the population and all sorts of things along these lines.

**speaker_5** [42:10]: Regarding your data boycott and your data strike, what were some of the positive and negatives that you looked at in the can and shoulds?

**Brent Hecht** [42:18]: Really, really good question.

**Shilad Sen** [42:20]: Yeah. The, the, the positives are about consumer power. Uh, I guess maybe are negatives there too, but I, I, I believe, I think they're the positives. The negatives are, that we talked about in the paper, had to do with, um, kind of a roadmap for companies to put up guards against this type of effort Um, is that right?

**Brent Hecht** [42:42]: Yeah, with, we had the negative index statement at the end, [laughs] end of that paper.

**Shilad Sen** [42:46]: Yeah.

**Brent Hecht** [42:47]: Um, the other thing I'd say is I had a related project where we built a, a plugin that we called Out of Sight-

**Shilad Sen** [42:53]: Mm-hmm

**Brent Hecht** [42:53]: ... which if you decided you were boycotting a company, let's use Papa John's again, um, if you searched for pizza, it just wouldn't appear in your search results. Wouldn't be on Google Maps, it wouldn't appear anywhere in the tender links, these types of things. Taking control, injecting your value system into the algorithm. It's a really easy thing to implement. We also realized it was potentially very dangerous, so it, it automated. So it's, you know, you could do packages of companies. Companies that are particularly bad on fossil fuels, for instance. You also could do packages of companies of Black and Jewish-owned businesses. So we were really excited about this tool we built that, uh, allowed campaign organizers to very easily create these things themselves, right? Um, and we decided not to release that tool because we felt that that would emphasize the negative over the, the positive. Um, I've also had some conversations with Northwestern legal to patent the idea, um, just so that it can't be used, um-

**Shilad Sen** [43:44]: [laughs]

**Brent Hecht** [43:44]: ... in ways that I disagree with. That's very experimental.

**Shilad Sen** [43:47]: [laughs]

**Brent Hecht** [43:47]: And, and it goes to sort of, I've been thinking a lot about these types of issues lately. Um, but yeah, collective action goes both ways, and that's something that we're, we're thinking about, uh, pretty deeply.

**speaker_6** [43:57]: In addressing the impact, the negative impact and sometimes unseen impact that, uh, data and algorithms have on our lives, you've spoken a lot about collective action-

**Shilad Sen** [44:06]: [coughs]

**speaker_6** [44:06]: ... and data boycotts. Um, is there anything that can be done on the other end? So from the computer scientist perspective, and I guess what you were just talking about kind of speaks to that. But, uh, I guess, is there such a thing as an unbiased algorithm when we talk about their modern applications, or does this kind of moderation always have to be done after the fact?

**Shilad Sen** [44:29]: That-- So, uh, I think your suggestion is spot on. Um, the, the other thing, point I wanna, uh, make regarding your question is, uh, I hope you don't make it sound like you can only make this change from the outside. Many of our students, math students, and I bet I know some of them are in the room, go to work at tech companies and, um, that change I think can happen from the inside too. It's extremely important to have employees at these tech organizations who care about these issues. Um, for the algorithmic bias question, I'll try to answer it and then maybe you can touch up my answer.

**Brent Hecht** [45:11]: Touch up, yeah.

**Shilad Sen** [45:12]: So, um, there's a lot of research in this area. Um, there are techniques that can help reduce kind of bias if you can measure it. Um, none of them are perfect. And so the real solutions to this problem lie in things like understanding the structural bias in the data that you're drawing upon, and the impact those algorithms have on the humans they serve.

**Brent Hecht** [45:41]: Yeah. I'll, uh, just second exactly what Shilad said about working from the inside. I actually would say that's probably the most effective way to make sort of short-term change, at least, um, in, in this area. And I strongly encourage anyone with Macao, Vermont mindset [laughs] to, to, to, uh, uh, attain those positions and, and make change, uh, from that standpoint. With respect to the algorithmic bias question, it's a really good one, and it's actually one that theoretical computer scientists have looked at, um, which, so basically the most mathy of, of those, of those of us in computer science. And they found that in the presence of structural bias, the, really generalizing, in the presence of structural bias in society, it's actually impossible to come up with an algorithm that everyone would agree is fair. You can make an algorithm that's fair according to certain definitions, but they actually sound... And they, they sound fair when you first hear them. Oh, uh, that's good. But then you think from another perspective, you're like, "Oh, that's really, that's really not fair." And that's actually one reason you, you, you heard sort of a trajectory of our careers here. Um, we started out thinking about sort of these more traditional algorithmic bias research questions. Um, and now we've shifted into more economics-focused stuff. And that's because, you know, we had an inkling, an inkling that this was the case and the theory folks came out with their findings. Like, well, okay, sounds like the best way to address algorithmic bias is to address those structural inequalities. And we know that income inequality is a huge driver of many of the, uh, structural inequalities that are of concern in the algorithmic bias domain. We also know that computers, we don't really get to this, but we know that computer science is a huge driver of income inequality. Um, so we thought we'd try to, uh, uh, turn the ship around a bit, um, and make computer science a driver of, um, uh, a world, a world that has, that has less difference between the rich and the poor. In fact, one of my spiels I give about my research says we're trying to recreate a, a new computing paradigm that more broadly distributes the economic winnings. And I think that's a great way to address these structural issues that rely on, um, uh, that sort of, that cause algorithmic bias.

**Shilad Sen** [47:46]: The climate change question is a good one. I mean, I think to the extent that, uh, the work we're doing supports collective action, it can support collective action in lots of areas. Um, the first steps are... Well, you do have this app, but a lot of the step, other steps are a little bit boring. They're having to do with measurement and, um, like how do you measure bias? How do you measure people's, the value of people's contribution to a system? So we're taking those first steps now. Um, and I think the steps that happen after that have to do, uh, with, uh, trying to find persuasive ways to, to convey that information to consumers and have them act on it. Um...

**Brent Hecht** [48:37]: Well, I'll add two things. I think one is on the, the climate change case, you know, this is, this is not really, it's not at all my area. Um, but I, uh, as I, I don't know if I mentioned this, at Macalester I was a double major in geography and computer science, so I have some degree of, uh- awareness of some of the im-immensely useful ways that machine learning, computer science has informed our understanding of climate change, and that's important for us to all celebrate and remember when we're-- Right. That's why throwing out your mobile phone and your computer in my class is not the way to [laughs] to solve these problems. It's, you know, uh, with r- satellites that take pictures and computers that process those pictures, that's how we know how many tr-trees there are and, you know, where the carbon sinks are and these types of things. So that's an important, I think, point that I'm glad I was able to make in the question session. [laughs] The, the, uh, uh, the second thing I'd say is, is, is Shalard's exactly right on measuring and making people aware of this, and that's part of the reason I'm here too, right? That's part of my, my research mission. But we found some stuff that isn't... Like, the data strikes and data boycott stuff, to, to me, that, that, uh, is... One challenge for us is to take something that's very technical and very complex and turn it into something that people can understand. Um, but we have still a lot of opportunity there. There's another piece of work that a, a student who, uh, was my student, Shalard was on his committee led, where we, we, we... One of the easiest types of data labor to, to measure and, and understand is, is Wikipedia because the organization is so transparent about everything. So we ran a study where we had people install a, a Chrome extension that they didn't know this, but it deleted all the Wikipedia results from their Google search, um, from all their Google search results, just gone. And we had a control group. And what we found is that the presence of Wikipedia as an entity created by volunteer data labor doubles the, um, click-through rate of Google search pages, whereas click... Like, if you had a one percent improvement click-through rate, um, you'd be, like, a hero. [laughs] You know, and we're talking about doubling from this, this volunteer data labor. So I think it can... Like, if we do this right, it can be exciting and, and get people interested. Um, and I think that will get some balls rolling on, on the necessary collective action that will need to happen.

**Shilad Sen** [50:49]: What are ways to engage people who don't necessarily find themselves in a computer science classroom in these issues? Because obviously, they're ones that impact all of our lives in ways that I certainly, you know, history major, did not really understand.

**Brent Hecht** [51:03]: What is a good way to stay up to date on this stuff? Newer Times does a decent job, although it's a... As you... The tech press is a little hyperbolic. Um, read our research papers. [laughs]

**Host** [51:19]: [laughs]

**Shilad Sen** [51:19]: [laughs]

**Brent Hecht** [51:19]: Yeah. Um.

**Host** [51:21]: Do you have a favorite podcast or something like that?

**Brent Hecht** [51:23]: Yeah, that's a good one. So does anyone... People know who Karis Butcher is? Karis Butcher has a... She does tech report. She has a podcast. She's... I, I disagree with a lot of her stances, but e-even through that disagreement, she does a pretty good job of eliciting good new knowledge from interview subjects in a way that I think that's broadly understandable. For instance, I was just talking to Shalard about her. She... This is one thing I like her for. She's, she says a lot of tech executives these days m-make a, I think, a very important point, which is if they're going to... There's two options in the world. There's the China model [laughs] or, and the US model, and there's a risk of, um, us sort of, uh, creating a first circular firing squad in the United States and having the, the Chinese model, which many people in the... Many people may have heard this in the news. China is, is on the forefront of implementing some, uh, existing technologies in ways that I think many people in the United States would find very uncomfortable. So we... So essentially, if we destroy our tech institutions here or diminish them, I don't think destroying is an option, um, then that model, um, wins. And she had a, a wonderful discussion about this thing. That'd be a way that you could engage with this material, um, through your lens of history.

**Host** [52:37]: So I, I know we're, we're about out of time. Um, there will be an opportunity to continue the conversation afterward. I'm gonna exercise presidential privilege and ask you the last question because I really wanna build on that one. Um, because it seems to me it, it may be a fundamental question about what education looks like now and over the next ten years. You know, I, I have heard it argued quite credibly that for, say, a contemporary student, uh, learning to understand the way data are manipulated, uh, is as fundamental a skill and as important to being an engaged global citizen, uh, as more traditional skills like writing or mathematics or being able to speak clearly. Should some of these questions be fundamentally embedded in, in the kind of liberal arts qu- education that any student would get? Should we begin to think about this not as an add-on or a choice, um, but some of these questions as things that any student who graduates from a place like Macalester, uh, should be asked to think about at some point during their education? Are they that important?

**Shilad Sen** [53:56]: Uh, yeah. So I would say the vast majority of students already are doing this. Like, uh, I mean, we... If we had a... So sixty percent of graduating students will have taken a computer science class before they, um, leave Macalester. Separately, sixty percent of students will have taken a statistics class. So, uh, most, the vast majority of Macalester students, um, not necessarily for the require-requirements, are doing this because, um, as far as I can tell, they feel like this is a tool that, uh, enables them to think clearly and speak clearly on these issues when they arise in the world. Um, so sometimes they're doing it for other reasons, but often they're just doing it to become more facile in, in, um, engaging with these issues.

**Brent Hecht** [54:47]: Yeah. I, I would say yes, not only for the student, but also for society, right? So, um, there's a model where computer science becomes a very different field than it is today because the knowledge that... Much of the knowledge that we have is disseminated through other, um, other disciplines, and that, that model might be, you know, very effective [laughs] at solving some of, some of the problems that, that we have. So if you're a history major, you know, you have four or five computer science classes under your belt, and that allows you to, um, think in the way that machines think of, you know, a little better. Um, so yeah, I, like, uh, I guess Shalard's biased. I, I'm not, 'cause I... You know, get to be an independent alumnus and make a recommendation from that standpoint. Yeah, I think it would empower the Macalester perspective and empower every single Macalester student if that were something that was strongly suggested.

**Host** [55:41]: Well, a sign of a really good conversation is that you want more of it, and, uh, I would... I wish we had more time. But first of all, join me in thanking Shalard and Trent. [audience applauding]

