---
title: "ATGthePodcast 275 — A Conversation with Jason Priem, Co-Founder, CEO, OurResearch"
person: jason-priem
section: by
type: talk-transcript
year: 2025
venue: "Against the Grain podcast (Libsyn, 2025-05-05); video: https://www.youtube.com/watch?v=e-tgopynvyU (Charleston Hub, 36 min)"
source_url: https://atgthepodcast.libsyn.com/atgthepodcast-275-a-conversation-with-jason-priem-co-founder-ceo-ourresearch
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 39
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# ATGthePodcast 275 — A Conversation with Jason Priem, Co-Founder, CEO, OurResearch

*Speakers (inferred):* speaker_0=Caroline Goldsmith, speaker_1=Michael Upshaw, speaker_2=Jason Priem

## Transcript
**Caroline Goldsmith** [00:00]: [on-hold music] Hello, and thank you for joining us today for this episode of ATG the Podcast. I'm Caroline Goldsmith, associate director of the Charleston Hub. Today's episode features guest host Michael Upshaw, community and outreach manager at Core, who talks with Jason Priem, co-founder and CEO of Our Research. After a career as a middle school teacher with a degree in history, Jason became interested in technology and online communities. He decided to go back to school in the information science program at UNC Chapel Hill. Now, Jason is an academic researcher who is a proponent for open research, open knowledge, and user accessibility, who works to use technology to help communities understand themselves better. Jason co-founded Our Research, a nonprofit with a focus on open scholarly infrastructure that creates open-source tools to uncover, connect, and analyze research products. They are best known for Open Alex, inspired by the Library of Alexandria, a comprehensive, open, and inclusive bibliographic platform. We'd like to thank Michael and Jason again for this fascinating interview. I hope that you enjoy this episode and that you will join us again next week. Thanks for listening.

**Michael Upshaw** [01:41]: Welcome to ATG the Podcast. Uh, today we're talking to Jason Priem, um, co-founder of Our Research, uh, which, um, is best known for the Open Alex bibliographic platform. Jason was kind enough to talk with us in twenty twenty-two and described how Our Research, uh, uh, which was founded as Impact Story came about, and, um, uh, described the story up to the impending launch of the interface, uh, access to Open Alex. So we felt that so much has happened since then, it was worth, uh, asking him back to talk about its recent history and its future. So, uh, thanks for joining us again, Jason. And, um, um, I'd like to start by just, uh, going back in a little bit detail of digging up about your, um, your background. I believe you started as a, as a, uh, studying history. Is that correct?

**Jason Priem** [02:24]: I did, yeah. In fact, we were just talking. I, uh, did a summer in, uh, in, um, Cambridge studying history, which was a real delight. But yeah, I studied, I got my undergraduate in history at the University of Florida.

**Michael Upshaw** [02:36]: Uh, but then you followed... After history, you went to, uh, you did a master's in social science. So why the move from, uh, history to social science?

**Jason Priem** [02:43]: [lip smack] Uh, well, I, I wanted to be a teacher, so, um, so yeah, I got my master's in social science education, and so that was just, yeah, part of my, uh, my being a middle school teacher, uh, trajectory.

**Michael Upshaw** [02:53]: Okay.

**Jason Priem** [02:53]: And then I was a middle school teacher for five years, which I really enjoyed, but I just kind of missed, um, studying as well as teaching, you know, like learning stuff and just, yeah, I was ready for a change, so that's when I decided to go. I got really interested in technology and thought, "Well, I should go back to school for something related to technology." And yeah, so then information science just kind of like, uh, just happened to meet a guy online who was at the University of North Carolina Chapel Hill Information Science program, and he was doing work that I thought was cool. So I was like, "Oh, maybe I could go there." [laughs]

**Michael Upshaw** [03:23]: [laughs]

**Jason Priem** [03:23]: And they took me, which was, was very fortunate for me.

**Michael Upshaw** [03:26]: Sounds like a great accidental, um, accidental encounter.

**Jason Priem** [03:29]: Yeah.

**Michael Upshaw** [03:30]: Um, so, um, um, but, uh, there's still quite a jump from there to, uh, from, from teaching to, um, to, uh, what you specialized in, which is, uh, this, this, uh, if you like, management of metadata. So, um, why the interest in, uh, for, uh, coding and managing metadata not always go side by side?

**Jason Priem** [03:45]: Mm-hmm.

**Michael Upshaw** [03:45]: So how did you get involved in the sort of, um, uh, putting together and solving scholarly problems in this way?

**Jason Priem** [03:50]: Mm-hmm. Mm-hmm. Yeah, good question. So I was always been-- I was always really interested in communities, and I-- the-- my particular interest in, in tech was like, you know, how can we use tech to help communities understand themselves better? So not just kind of studying from the top down as a subject, but, uh, sort of as a participant. And like, uh, my early work was in like communities of bloggers. But, um, when I saw that this-- there was this really beautiful network describing the community of science already out there, right, in kind of the citation graph, I thought, "Well, this is so pretty and it's also very like useful, so this is what I should be working on." So that's why I got really excited about how can we use technology to better understand the community that makes up, you know, the sort of... that makes up science, that, that creates our, our, our, our knowledge as a human race. How can we actually, uh, get a picture of what that thing actually looks like? Something that is ephemeral, right? Like a community, what even is that? But maybe, you know, if we're clever and, and we can employ technology in an interesting way, we can actually see something that's not there in the same way that, you know, your body's full of bones and, and ligaments and everything else, and before the X-ray you kind of had to like cut it open maybe to see that or whatever, you know. Or similarly, you know, outer space is full of all kinds of amazing objects without telescope we can't really see. So if we use technology, we can like see stuff that isn't there, and one of the stuff that I want to see that I think is very pretty is, like I said, the network of how human knowledge is created.

**Michael Upshaw** [05:20]: Well, you've, uh, y- you've described very clearly how you can use technology to solve, uh, practical problems. And in fact, um, uh, two of the-- there's a whole stable of projects from, from, from Our Research and, um, uh, but, uh, two that you, I think you described before, Unsub and Unpaywall, were both, uh, very much geared around solving specific problems, uh, looking at sort of one, uh, one use case if you like and, um, and, and, and fixing it. While Open Alex is a sort of a much broader tool. So, um, how did you go from, from if you like point solutions to sort of, um, something much more general?

**Jason Priem** [05:50]: Mm-hmm. Yeah, that's a great question, and I think the answer is I always wanted to do, and my co-founder, uh, Heather Piwowar who stepped down a few years ago, um, but we always-- I'll say we even though it's like me now, um- But we always wanted to build something like OpenAlex. You know, I th- I guess for me in particular, I always had these kind of delusions of grandeur [chuckles] 'cause I always wanted something, something, you know, complete. You know, to me, that's the beauty of, of, of living on this planet, is that, like, we can actually, like, uh, you know, we can work together. We can think of ourselves as one, one, um, one collection, one group, one, one... ultimately one community, you know? And I always thought, "Wouldn't it be cool to put all the human knowledge in the same spot?" You know, 'cause it's like the Library of Alexandria, which is not coincidentally, you know, the, the inspiration behind the name OpenAlex. But even though that's quite a nice idea, it's, you know, very challenging, it's very expensive. And so, you know, we just kind of wanted to keep moving in that direction, while at the same time doing stuff that people would find useful and that there would be some money in. 'Cause although our research is a nonprofit, we've always felt like it's important for us to earn revenue. Uh, it keeps us kind of very, uh, connected to a community, connected to doing something useful. Um, I got out of academia, um, because, you know, I really wanted to... I, I love being an academic, but I found that I had more excitement about building stuff that people would really use, that would really, like, solve a problem for them. So, um, Unsub was really very, as you said, specifically designed to solve a problem with librarians. It said, "Hey, we wanna use open access to cancel stuff," and that's something I really care about. I like the idea of open access, and I like the idea of librarians moving more in that direction. So Unsub was in service of that. Unpaywall was kind of... You think of it as a junior OpenAlex because it was, uh, you know, has about 160 million records in it, and a lot of people use it as a metadata repository, even though it's quite focused on OpenAlex. Uh, sorry, on open access. It's focused on open access, but people use it as a, have, uh, we're using it as a more general metadata repository, even though that isn't what it is. So yeah, so w- I think I was always trying to move in that direction. It's just that, um, in recent years, uh, the, the technology has gotten to a point where it's easy to build something like OpenAlex compared to what it was, you know, 10, 20 years ago. And also the, the persistent identifiers, PIDs. The PID graphs have grown to a point where things like Research, uh, Organization Registry, Crossref, um, ORCID-

**Michael Upshaw** [08:19]: Mm-hmm

**Jason Priem** [08:19]: ... these other in- all nonprofit initiatives have done a great job of trying to reify and map the connections between-

**Michael Upshaw** [08:27]: Mm

**Jason Priem** [08:27]: ... um, researchers, organizations, uh, papers. Uh, they're very incomplete right now, um, which is why I think what we're doing is still important. But they give a really good jumping-off place to someone trying to do something more expansive, like what OpenAlex-

**Michael Upshaw** [08:41]: Mm-hmm

**Jason Priem** [08:42]: ... is doing.

**Michael Upshaw** [08:43]: So do you think it was simply a sort of combination of circumstances that, um... I mean, plenty of people have a great vision for sort of, um, solving all the world's scholarly problems, but not many people get to, um, uh, get a sort of a, a great grant from Arcadia to sort of, uh, to, to build it and actually carry it out. Do you think it was just a combination of circumstances that led to sort of it being, becoming easier, or, um, there was some sort of, some other magic in it?

**Jason Priem** [09:04]: Uh, well, I mean, I guess both. I guess the combination of circumstances is the magic. You know, I, I think someone would've come along and done this at some point. Um, we are doing it, so I guess I must think at some level that we have some special, like, we have some capability or some- something to add to the problem, you know? So-

**Michael Upshaw** [09:20]: Mm-hmm.

**Jason Priem** [09:21]: Um, but yeah, so... But yeah, but it's definitely, like, it's one of those things where, yeah, like I think the time was right, for sure.

**Michael Upshaw** [09:26]: Mm.

**Jason Priem** [09:26]: It wasn't, definitely wasn't like Jason Priem came along with this great idea that no one else could have ever had, for sure.

**Michael Upshaw** [09:30]: Mm.

**Jason Priem** [09:31]: I think the time was right, and then, yeah-

**Michael Upshaw** [09:32]: Mm

**Jason Priem** [09:32]: ... being the right person in the right place and right time, and having a little bit of audacity to try something before most people think that it's quite ready. So-

**Michael Upshaw** [09:40]: Mm-hmm

**Jason Priem** [09:40]: ... I think, for instance, the Arcadia grants, 'cause, you know, we had a relationship with them, and we had got off to a good start on building this thing after Microsoft Academic Graph shut down.

**Michael Upshaw** [09:49]: Mm-hmm.

**Jason Priem** [09:49]: Who, uh, you know, I, I should have mentioned earlier, 'cause their work was really fantastic and, and really like, you know, was absolutely, like, essential for, for doing what we did.

**Michael Upshaw** [09:58]: Mm.

**Jason Priem** [09:58]: Um, but then, yeah, from that, we, we, you know, kept it tr- tried to keep the momentum up and keep adding a bunch of stuff and-

**Michael Upshaw** [10:04]: Mm

**Jason Priem** [10:04]: ... I, I can definitely say that we cover a lot more than they ever did and with a lot more accuracy, um, 'cause we've had more work, more years to work on the problem now.

**Michael Upshaw** [10:12]: Yeah. Have the ideas, uh, has the idea behind OpenAlex changed since you launched it? I mean, the, we kn- we know that the, um, uh, uh, when, when we last interviewed you, the, um, the web interface was just starting. So was that, uh, was that part of the original vision, or was it, um, or did it come later?

**Jason Priem** [10:26]: No, it was definitely part of the original vision, yeah. Yeah, I, I really want it to be accessible. And, you know, I'm, I'm a... We haven't talked about it much, but I'm really obsessed with open knowledge and open science, and I really want everything that OpenAlex does to be open. And if it's got an open API and open, you know, uh, you know, 300 million line JSON, uh, lines download, it's open technically speaking, but most people don't know what to do with that. And so-

**Michael Upshaw** [10:53]: Mm

**Jason Priem** [10:53]: ... is it open to them? No. It's sort of there's already, there's a, there's a, uh, a technical obfuscation there, you know, or a technical barrier.

**Michael Upshaw** [11:00]: Mm.

**Jason Priem** [11:01]: So yeah, I would really like to make, um, and we did make, you know, a user interface that lets regular people, um, look at it. I would say we did make, I would say what we have done so far is quite basic and really, like, needs, like, an enormous amount of improvement but-

**Michael Upshaw** [11:15]: Mm

**Jason Priem** [11:15]: ... you know, I think you, you [chuckles] do your, do your best with what you got. And, uh, we got some other stuff coming up that I think is gonna really, really improve that, um, in the coming year.

**Michael Upshaw** [11:23]: But you're already in a p- in a remarkable position. Um, uh, OpenAlex has only been going for, for what? Uh, about two years, three years, and, uh, where, um, where, um, uh, the, the, the metrics that you're providing, um, you become, if you like, uh, you moved already from being, like, a follower to a leader in that, um, uh, people sort of, um, uh, people are thinking very carefully about what you're providing and you can, um, um... And this is similar to where Altmetric was some years ago in that, um, you remember lots of controversy about whether they did or includes particular social media and so on, and, uh, and, and Twitter. Um, um, so OpenAlex is already in this, uh, this, this kind of, uh, position, um, which is, um, which is quite, uh, uh, uh, remarkable that, uh, you know, what you decide to put into your interface can sort of, um, uh, people will sort of will think about and follow.

**Jason Priem** [12:07]: Yeah, agreed. And I, I think that's great, and that obviously it's, uh, represents success for us. I'm very happy that people care what we're doing because probably, yeah, I would say the majority of things that I-- like projects I've done in my life, no one cares at all, and no one even knows about them.

**Michael Upshaw** [12:19]: [laughs]

**Jason Priem** [12:19]: That's life, right? Like [laughs] but yeah, when you do something, when people actually care about it, that's a, that's a good feeling. So yeah, I'm very happy about that, and I definitely would say we take that responsibility seriously. Um, and I, and I, I... It's probably worthwhile mentioning that our, our pers- our approach to this is to actually be extremely, extremely inclusive. So what we want-

**Michael Upshaw** [12:36]: Yeah

**Jason Priem** [12:36]: ... to do is say, yeah, like we understand we have responsibility because people are using our data downstream, and w-where other providers in the past have said, "We are going to... Our, our, our reaction and responsibility is we will make sure that everything in our database is exactly perfect according to us." And that's one perspective, and again, maybe that made sense 10, 20 years ago. Today, I think that's the wrong perspective. Instead, our perspective is we will make sure that everything that's out there, we have. We're not telling you whether it's exactly perfect or not.

**Michael Upshaw** [13:06]: Mm-hmm.

**Jason Priem** [13:06]: We are gonna aggregate third-party judgments-

**Michael Upshaw** [13:09]: Mm-hmm

**Jason Priem** [13:09]: ... about the quality of these materials and the quality of the metadata, and we'll present you with that, and then you can decide yourself. So for instance, one of the things we do is-

**Michael Upshaw** [13:16]: Mm-hmm

**Jason Priem** [13:16]: ... you know, we cover-- We have records for 200,000 different sources in OpenAlex, mostly, mostly journals. 200,000. That's a lot.

**Michael Upshaw** [13:24]: Mm-hmm.

**Jason Priem** [13:24]: Um, by comparison, you know, uh, other databases may have 20,000, 50,000.

**Michael Upshaw** [13:28]: Mm-hmm.

**Jason Priem** [13:28]: Um, so it's a lot. People understand, but they wanna say, "Well, you know, some of that stuff is low quality," you know, low quality. Well, uh, obviously, it depends on your definition of quality, but depending on your definition of quality, yeah, by... Of course, for sure. Um, people sometimes wanna restrict, you know, their searches or their investigation to a certain quality threshold. Again, quality defined-

**Michael Upshaw** [13:46]: Mm-hmm

**Jason Priem** [13:46]: ... by whatever, you know, by whatever they want to define it. So we're aggregating third-party judgments to that. For instance, um, CWTS, which is a, a well-regarded bibliometrics, um, laboratory late in Netherlands. Um, they have got-- they have created an open list of what they call core journals. These are journals that have met-- they've gone through and, like, done kind of a quality assessment based on, um, a whole bunch of factors they publish on the website. It's all done openly, which is great. And now we can in-- Because that's open data, we integrate that into OpenAlex, and so we flag all of the journals and all of the articles within those journals about whether or not this is in a CWTS core journal. So you can do your search on whatever you're interested in, find what all of our 200,000 sour- sources have to say about it. And then if you want to say, "Okay, I want something that's a little closer to what I might get in a Scopus search or Web of Science search or something that I'm a little more familiar with," absolutely hit core sources, and you're gonna get something more along those lines. I'm not saying we're duplicating their work because they have their own quality stuff. Good on them. But what I am saying is that our approach, because we are sort of more ecumenical about this-

**Michael Upshaw** [14:50]: Mm-hmm

**Jason Priem** [14:50]: ... means that we're able to integrate lots of people's p- uh, you know, quality judge-- And I, I put air quotes around the quality judge because we all know that's more than one thing to more than one person. And if you want to cast a very wide net, OpenAlex allows you to do that. And so that, I think, is a little bit different than what some of the proprietary approaches, you mentioned Altmetric.com, have done in the past, um, where they, they kind of... They say, "Well, this is our approach. This is our solution, and we're gonna tell, we'll tell you what it was." I think that's fine, but it is not our approach. Our approach is say, "We're actually going to aggregate everybody's solution," 'cause again, this is my passion, right? I wanna bring the whole community in on this.

**Michael Upshaw** [15:27]: Mm-hmm.

**Jason Priem** [15:28]: And that means not just the people who are creating content, but the people who are creating content about the content.

**Michael Upshaw** [15:33]: Mm-hmm.

**Jason Priem** [15:33]: You know, all of those links, and this is the nice thing about the citation graph, is it's all people's opinions about other intellectual products. And so when we integrate that, um, you know, that CWTS core sources list, we're integrating their opinions about these products, and that too is part of the scholarly conversation. We really want to kind of treat every attestation or, um, uh, opinion about scholarly communication as itself scholarly communication.

**Michael Upshaw** [15:59]: Mm-hmm.

**Jason Priem** [16:00]: We really want a comprehensive graph.

**Michael Upshaw** [16:03]: So your model is, um, is one of, if you like, in-inclusion rather than exclusion. You're, you're, you're sort of, uh, pulling everything in [clears throat] and allowing people then to make subsets, um, if they choose, um-

**Jason Priem** [16:12]: Absolutely

**Michael Upshaw** [16:12]: ... rather than the sort of exclusive model. So if you like, you know, it's like a Google model rather than a Web of Science model. Uh, sort of, um, uh, uh, uh, bring it all in and sort of, um, uh, and, um... But doesn't that lead to a, um, [clears throat] like a... I think it's a great approach. I think it's a, it's, it's, it's the, it's the perfect approach. Nonetheless, um, one of the challenges is the, uh, the, the state of scholarly metadata is, uh, remains woeful. [laughs] And, um-

**Jason Priem** [16:34]: Mm-hmm

**Michael Upshaw** [16:35]: ... and, uh, when you try to index everything, um, uh, uh, quite apart, I mean, one problem that we all know about is PDFs, um, if, uh, it, it tend to sort of eliminate most of the metadata that was ever sort of introduced around a, around an article. And, um, um, um, don't you, uh... And, and the, the take-up of, um, of PIDs, um, uh, has been very, has been slow. So we still have to deal with, um, you know, maybe sort of 50% of all authors have now got an ORCID ID, but, um, that means that 50% haven't. So we still have terrible problems of disambiguation, of, uh, not knowing what, uh, what institution is which, and so on. Um, don't you find that, um, um, uh, you're limited by the, uh, the poor quality of the data you're trying to, trying to index?

**Jason Priem** [17:16]: Uh, well, there's, there's sort of two questions there. I'll try and answer them one at a time. One is, yes, I would say what we're doing is closer to Google than Web of Science. But I think one extremely important difference is that Google, again, adopts this sort of proprietary mindset of you ask your question, we'll tell you the answer. If I go to Google and search armadillos, I'm gonna get what Google thinks is the best ranked armadillo-

**Michael Upshaw** [17:38]: Mm-hmm

**Jason Priem** [17:39]: ... articles from what Google thinks is the journals that meet its inclusion criteria, which by the way, it won't tell me. So what they're doing is they're very opinionated, and they're very closed. And I, I love Google Scholar. I've used it my whole scholarly life. I think they've built something, again, very lovely. But that is, I think, quite a big liability of their approach, is it's very, you know, you get what Google tells you. Whereas what we're doing is, yes, we will give you some answers about what we think the answer is, but then it's... We will be explicit about where those answers come from, 'cause we can tell you what, what sources we index. And we will give you the opportunity to narrow that search to different types of quality or not as you see fit. And that's the power of doing this openly, is that you really can tailor your experience to, to what is important to you. And that's something I don't think anyone else does. So that's the answer to what I-

**Michael Upshaw** [18:29]: [chuckles]

**Jason Priem** [18:29]: ... I deem to be your first implicit question.

**Michael Upshaw** [18:31]: Mm-hmm.

**Jason Priem** [18:32]: Your second question, which is more explicit, is about the, the woeful status of scholarly metadata. And yeah, I mean, that's why we're here. Like [chuckles] I totally agree. Like that's... If, if, if that, if the status was not woeful, then yeah, there would be no necess- no, no need for us 'cause I think there's, um, lots of people are interested in what we're... Like lots of people want to solve this problem. It's just, yeah, it turns out to be a really hard problem to solve, and I think-

**Michael Upshaw** [18:58]: Really

**Jason Priem** [18:58]: ... um, the folks working in the Pitt community are making good progress, but I think you put your finger on it, is it's like there's a lot of, a lot of progress yet to be made. And in the meantime, I just don't think those of us in the open community should be sitting here saying, "Oh, yeah, but once, once everything has a PID, it'll all be solved."

**Michael Upshaw** [19:13]: [chuckles]

**Jason Priem** [19:13]: Okay, cool. But like in the meantime, right, like that's gonna be how, who knows how many years. But in the meantime, like I said, everybody else is already getting addicted to these closed sources of-

**Michael Upshaw** [19:22]: Mm-hmm

**Jason Priem** [19:22]: ... of data. So we wanna actually go out there and do the work to fill those holes-

**Michael Upshaw** [19:26]: Mm-hmm

**Jason Priem** [19:26]: ... in the, the metadata graph and to solve those problems. So we spend many hundreds of thousands of dollars and lots and lots of our lives-

**Michael Upshaw** [19:35]: It's-

**Jason Priem** [19:35]: ... trying to find ways to fill those holes. So when ORC, when authors don't have, uh, ORCIDs, for instance, and there's, you know, this John Smith studies, you know, Renaissance history, and this John Smith studies wildlife ecology, and, you know, we want to be able to look at their, uh, respective publication records and say, "Okay, well, actually, this John Smith is, is over here, and this one's over here."

**Michael Upshaw** [19:57]: Mm-hmm.

**Jason Priem** [19:58]: And we can do that automatically, right? And, and, and that's the kind of stuff that, uh, Scopus, Web of Science, even Google Scholar's been doing for a long time.

**Michael Upshaw** [20:04]: Mm-hmm.

**Jason Priem** [20:05]: Again, the difference is they've done it in a closed way. And so-

**Michael Upshaw** [20:07]: Mm-hmm

**Jason Priem** [20:07]: ... all of our algorithms for that, the way we do it, you can go download off that, uh, that off of our, um-

**Michael Upshaw** [20:13]: Mm-hmm

**Jason Priem** [20:13]: ... off of our GitHub. The models, instructions for how to create the models, everything we're doing is completely in the open.

**Michael Upshaw** [20:19]: Mm-hmm.

**Jason Priem** [20:19]: And it's... As it improves, which it is doing, you know, it's, it's a, it's a hard problem, and so-

**Michael Upshaw** [20:24]: Mm-hmm

**Jason Priem** [20:24]: ... I think we're getting better at it as time goes by. You can see how it improves, and you can see our performance on benchmarks and stuff like that.

**Michael Upshaw** [20:30]: Mm-hmm.

**Jason Priem** [20:30]: So, um, someone, someone has to have to do that, 'cause as you said, the metadata ain't great. Um, but what we feel like, and what I, what makes, what I'm really passionate, really excited about is like, let's do that in the open. Um, we-- I'll give you a quick example of that, is something people are really interested in is tagging UN Sustainable Development Goals.

**Michael Upshaw** [20:48]: Oh, yes.

**Jason Priem** [20:49]: Of course.

**Michael Upshaw** [20:49]: I noticed-

**Jason Priem** [20:50]: You know, SDGs

**Michael Upshaw** [20:50]: ... I have that, um... Yeah, you're tagging, you're, you're adding SDG codes.

**Jason Priem** [20:53]: Exactly. We're adding the SDG codes. So people, they write a paper, and it helps solve, you know, uh, I think SDG 2 is zero hunger. It helps make the world less hungry. They wanna see that tag. "Hey, my paper, not only did I like-

**Michael Upshaw** [21:05]: [chuckles]

**Jason Priem** [21:05]: ... help me get tenure, which is great, but also it's, it's addressing UN SDG number 2, zero hunger."

**Michael Upshaw** [21:12]: Mm-hmm.

**Jason Priem** [21:12]: And so they want that tagged. And now obviously, at the scale we're working, you know, hundreds of millions of articles, you need to do that automatically.

**Michael Upshaw** [21:17]: Mm-hmm.

**Jason Priem** [21:17]: And so we went, "Wow, maybe we can do this automatically." And we saw there's, there's been so much effort being done, uh, in the open by other organizations-

**Michael Upshaw** [21:24]: Mm-hmm

**Jason Priem** [21:24]: ... to create, uh, an SDG tagger.

**Michael Upshaw** [21:27]: Mm-hmm.

**Jason Priem** [21:27]: So we got involved with that community. Um, I think we contributed a little bit of code. We definitely have used the code that they've used.

**Michael Upshaw** [21:33]: Mm-hmm.

**Jason Priem** [21:33]: And that's what we're using now. And again, you can dig that up, and you can see it yourself. And when you see-

**Michael Upshaw** [21:37]: Yeah

**Jason Priem** [21:37]: ... errors, you can get involved in that community and, and make it better. I really-- Like I said, I think the really big difference between what we're doing and what has sort of ever been done, is that we really are doing this as a community.

**Michael Upshaw** [21:47]: Mm-hmm.

**Jason Priem** [21:47]: Which is how science is supposed to work, and so why shouldn't scholarly metadata work the same way that scholarship does?

**Michael Upshaw** [21:52]: Yeah. Absolutely. I love your, um, uh, uh, you mentioned sort of word ecumenical, sort of your sort of, um, open approach to sort of, uh, to, um, um, instead of providing a, um, a single fix, sort of, um, leaving people to sort of, to, to, to do what they want. And but that extends to, um, some of the most exciting areas. In the last, even before generative AI, um, there was a whole host, or there is a whole host of, uh, small scale initiatives, uh, providing tools for scholars, uh, that all sort of grown up and, uh, many of them make use of, uh, services like O- OpenAlex. So, uh, I'm ta- I'm thinking of things like, um, uh, finding peer reviewers and summarizing. Um, you, you probably know, you can list all the, all the companies. So, um, isn't it tantalizing to think that you could be, um, you could be offering some of these services yourselves? [chuckles]

**Jason Priem** [22:37]: Uh, yeah, it's a good question. So, um, yeah. And honestly, I think the reason why OpenAlex exists though is 'cause I've always, as a person who likes to make things, I've always wanted to build those kinds of questions, those kinds of, of tools. Like you said, find peer reviewers, summarize a paper, um, uh, create a map of the argumentation around-

**Michael Upshaw** [22:57]: Yeah

**Jason Priem** [22:57]: ... a certain topic. All that kind of stuff is so cool to me, and I'm 100% sure that in five years, those are gonna be ubiquitous, and in 10 years, those will have replaced, I think, journals.

**Michael Upshaw** [23:07]: Mm-hmm.

**Jason Priem** [23:08]: Um, I would love to build those things, but w- when I wanted to build those things, I found that the, the grist for my mill was not there. Like I, I didn't have this, the data that I needed to build it.

**Michael Upshaw** [23:19]: Mm-hmm.

**Jason Priem** [23:20]: And so that's when I thought, "Well, gosh, if I were to build OpenAlex, then a whole slew of creators, you know, hundreds and hundreds and thousands of people with great ideas who are way more talented than me could build on top of that infrastructure."

**Michael Upshaw** [23:33]: Mm-hmm.

**Jason Priem** [23:33]: Someone just needs to do the kinda less glamorous work. I always look at it as-

**Michael Upshaw** [23:37]: [chuckles]

**Jason Priem** [23:37]: ... the, uh, the pipes under a city, right? Like I'm-

**Michael Upshaw** [23:40]: Mm-hmm

**Jason Priem** [23:40]: ... I'm speaking from Paris right now. It's a lovely city.

**Michael Upshaw** [23:43]: Mm-hmm.

**Jason Priem** [23:43]: They've got bakeries downstairs. They've got-

**Michael Upshaw** [23:45]: Mm-hmm

**Jason Priem** [23:45]: ... uh, you know, restaurants. There's clothing stores. Like, all these different places, right?

**Michael Upshaw** [23:50]: Mm-hmm.

**Jason Priem** [23:50]: But none of those could really have a business without water. They need to be able to turn the tap on-

**Michael Upshaw** [23:54]: [chuckles]

**Jason Priem** [23:54]: ... and get water out of the tap. No one talks about Paris, the city of pipes, you know? No one cares. Like it's... But it has to be there. Those pipes have gotta be there. Everyone just knows that you turn the water, you can get there. And then they can build something really cool on top of that. And that's what OpenAlex is designed to be, the sort of-

**Michael Upshaw** [24:08]: Mm-hmm

**Jason Priem** [24:08]: ... unglamorous plumbing underneath-

**Michael Upshaw** [24:10]: Mm-hmm

**Jason Priem** [24:11]: ... a whole beautiful urbanization of scholarly communication. Something, you know, where people are building all these really cool tools-

**Michael Upshaw** [24:17]: Mm-hmm

**Jason Priem** [24:18]: ... that help us You know, do scholarship like we, we never were able to do before.

**Michael Upshaw** [24:23]: Mm.

**Jason Priem** [24:23]: But they need that plumbing, and that's, that's where we fit in. That's what we really wanna do, and I'm laser focused on that.

**Michael Upshaw** [24:28]: Mm. I can, I can echo that. Um, uh, I worked for a while for, with an AI company that did, um, concept extraction for commercial publishers and, um, um, it was predated generative AI, but it was a s- similar kind of process. Uh, you, you, you did a... You created a corpus. You, uh, yeah, then you indexed it and, um, and, uh, and you, and you created some concepts out of it. Um, but the work of, um, processing the content, uh, was always the unsexy bit. The, um, uh, the-- Within the company, the, uh, the machine learning experts were the stars, and they sort of, um, and the data processors were the sort of, um, uh, were the, the, the, uh, the, the mundane people. And yet, um-

**Jason Priem** [25:03]: Sires

**Michael Upshaw** [25:04]: ... more money was spent on processing the content than it was ever spent on the [chuckles] on, on adding the clever algorithms.

**Jason Priem** [25:11]: Yep, exactly.

**Michael Upshaw** [25:12]: Yeah. So anyway, um, uh, th- moving on to, to, um, um, you, you, you, um, you, you... When you built your library tools, um, uh, what was remarkable is that they, they, they showed a great sort of, um, awareness and understanding of what libraries were trying to do, uh, you know, finding out a particular solu- s- uh, a particular problem and solving them. So, um, are you doing the same thing with OpenAlex? I mean, uh, because of it's, uh, because it's such a, a sort of, uh, it's a platform that can be used for so many different purposes, um, are you identifying specific use cases or, um, I mean, surely you're dealing with a whole multiplicity of, um, of users and purposes, so it must be quite difficult to work out sort of on the... where to focus your efforts on sort of what to build next.

**Jason Priem** [25:54]: Yeah, it absolutely is. It's a, it's a, uh, a good insight. Thank you for the nice words about being well-targeted to libraries in the past. I appreciate that, and that definitely is our goal now. I would say, you know, we have, you know, we go really deep in the library community. We, uh, I've been hanging out with library folks for, like, a decade, and-

**Michael Upshaw** [26:15]: Mm-hmm

**Jason Priem** [26:15]: ... and so I have a lot of, you know, so I've, so does my co-founder, so is other people in our company. So we got a lot of great relationships there, and librarians have been really generous with their time and, and their help with us. But I would even say we need to go beyond that community as well, you know. Like, we have a lot of users that you mentioned in sort of the enterprise world, people making startups. You know, there's, this is a, like, this last year and this year are just, I think almost are, are, are unprecedented, like glimmer in your eye to startup idea times, you know, when, when you can use sort of these AI-based coding tools to-

**Michael Upshaw** [26:49]: Mm

**Jason Priem** [26:49]: ... turn an idea into a product really quickly.

**Michael Upshaw** [26:51]: Mm-hmm.

**Jason Priem** [26:51]: So we wanna make sure that we're serving those folks, um, people who are gonna include, have no affiliation with libraries. Uh, and the institution, the universities, you know, we also want to make sure we're helping folks like in the VPR's office, the, the Vice Provost of Research.

**Michael Upshaw** [27:06]: Mm-hmm.

**Jason Priem** [27:07]: Um, uh, Vice President of Research. Um, we got a lot of intranet 'cause they're doing a lot of analytics stuff. Um, other offices in the US, uh, in the, sorry, in the, in, in the university, um, the international office, the planning depart- uh, planning office. Like, there's just a lot of folks who are really interested in what we're doing, and we're trying to keep building those relationships just across university and then across the likes of the private sector. We got-

**Michael Upshaw** [27:30]: Mm

**Jason Priem** [27:30]: ... huge companies, you know, uh, big pharma. I think we got, uh, Bayer, GlaxoSmithKline, a bunch of these big pharma companies. Obviously, they-

**Michael Upshaw** [27:39]: Mm

**Jason Priem** [27:39]: ... are trying to do literature-based, um, discovery, which is-

**Michael Upshaw** [27:42]: Mm

**Jason Priem** [27:42]: ... I love. I, I think it's a terrific use case. So-

**Michael Upshaw** [27:45]: Mm

**Jason Priem** [27:45]: ... as you said, there's a really big community, and definitely the challenge for us is maintaining that focus. Um-

**Michael Upshaw** [27:50]: Mm

**Jason Priem** [27:50]: ... I, I don't know that we're nailing that. That's something I think we gotta try and do a little bit better maybe, uh, this coming year.

**Michael Upshaw** [27:55]: Mm-hmm. Mm. Um, one of the, one of the big issues that's, uh, that's, uh, that's, um, become far more apparent in the last, uh, uh, uh, two or three years is research misconduct, um, where there's been, uh, y- you've, you've heard about, you know, um, the, the, the Hindawi sort of, um, uh, uh, problem and, um, paper mills and all the sort of various, uh, various things about that. Do you think there's any way that, um, OpenAlex might be able to help in, uh, um, managing the situation, which is clearly, um, may or may not be getting worse, but it's certainly getting more noticed? [chuckles]

**Jason Priem** [28:25]: Oh, yeah. No, I mean, we are. I, I'm, I'm delighted to see all of the work on research misconduct that's using our data. I'm super, super happy about that.

**Michael Upshaw** [28:33]: Yeah.

**Jason Priem** [28:34]: Um, if you want, you know, to catch people, essentially, you know, fraudulent publishing practices is, is, is most of what, what people are talking about when they're talking about research misconduct right now, or at least in the context of your question. Um, if you want to catch people employing fraudulent publishing practices, you better know what their publication record is, right? There's no way to do it without that. You need to have that. That's the data, right? That's the forensic data that's being investigated, and if that forensic data is locked up in a toll access database, number one, it decidedly limits the number of people who can use it for, or mine it for clues, if you will.

**Michael Upshaw** [29:11]: Mm.

**Jason Priem** [29:11]: Um, and it also means that it's hard to share that data with other people to try and make your case. And so, um, I think that's, yeah, I think that's why we've attracted a lot, a lot of folks doing that kind of, um, forensics have turned to our data set. Um, I just saw one recently where people were, um, this was published on Archive a couple days ago, so it's stuck, sticks in my mind, but where they were, um, they were finding people who were sneaking, it was diabolical, I guess, but people who were sneaking, uh, journals who were sneaking fake, sneaking fake references into Crossref. So they were, um, they would basically like, you know, if, if I write an article and I cite maybe 20 papers from all different journals, and I publish it with your journal, if you were fraudulent, you would say, "Okay, cool. Great. We'll publish that." But then in Crossref, I'll add 200 more journals-

**Michael Upshaw** [29:58]: Mm

**Jason Priem** [29:58]: ... 200 more citations all citing my journal.

**Michael Upshaw** [30:01]: Yeah.

**Jason Priem** [30:01]: So I'm, like, boosting my... Right? Like, and since it all happens in the realm of metadata-

**Michael Upshaw** [30:05]: Yeah

**Jason Priem** [30:05]: ... no individual human researchers, readers even see it. So these folks on Archive, they had, they had created a, a, basically a, I think it was using kind of network topology to identify outliers and say-

**Michael Upshaw** [30:17]: Mm

**Jason Priem** [30:17]: ... "Well, it's kind of unusual to get cited by, you know, to cite 200 things all in the same journal."

**Michael Upshaw** [30:21]: Yeah.

**Jason Priem** [30:21]: But in a lot of these forensic, these, um, these, uh, what do they call it? Um- I don't know, like statistical forensics techniques are looking for outliers.

**Michael Upshaw** [30:29]: Yeah. Yeah, yeah.

**Jason Priem** [30:29]: And I, I love that OpenAlex is a source of data for so many of those efforts, and they can create stuff to automatically discover that kind of malfeasance. And as you say, the question is always like, is it increasing now, or is it just we can see it better now? And I think probably the answer is a little bit of both.

**Michael Upshaw** [30:45]: Bit of both. Yeah, absolutely. It's a bit like the, um, the sort of what is or isn't acceptable level of self-citation, which is the sort of thing which-

**Jason Priem** [30:51]: Right

**Michael Upshaw** [30:51]: ... um, a machine-based check can, uh, can be very helpful in, uh, assisting you. Um, so you-

**Jason Priem** [30:56]: Absolutely.

**Michael Upshaw** [30:57]: Yeah. So you haven't gone down the route of, of, um, as some organization have, uh, like sort of DOJ of moving towards, if you like, an authority list of, um, what is or isn't acceptable in terms of, you know, acceptable journals or acceptable, um, um, um... So you, you, you, you, you keep your approach sort of, um, indexing everything and then sort of... But what happens if, um, if you find that sort of, uh, journals or papers are retracted?

**Jason Priem** [31:21]: Uh, yeah. Well, I mean, uh, uh, we definitely mark that. You know, that's a big part of our data set is that if-

**Michael Upshaw** [31:26]: Mm-hmm

**Jason Priem** [31:26]: ... if things are retracted, they get marked. Uh, we have a flag-

**Michael Upshaw** [31:29]: Mm-hmm

**Jason Priem** [31:29]: ... is retracted equals true, and that's something you can filter on in the user interface.

**Michael Upshaw** [31:34]: Mm-hmm.

**Jason Priem** [31:34]: And it's something that you can investigate, um, run studies on in the data set-

**Michael Upshaw** [31:39]: Mm-hmm

**Jason Priem** [31:39]: ... or in the user interface. So yeah, I, I... It's definitely our policy to, like a lot of, I think, organizations, is, like the publishers themselves, is it's good to leave that up there for the record, um, along with a very, like, prominent flag, like this has been retracted.

**Michael Upshaw** [31:54]: Mm-hmm. Mm-hmm. Um, just to finish off the, um, um, you're in the envious position of, um, uh, having a startup that works. You know, most startups disappear withi- [chuckles] within, within 18 months or so. Um, now you've got, uh, OpenAlex, uh, running. Do you, uh, do you still have time, it sounds like you have time to do research, or is all your time spent managing the organization?

**Jason Priem** [32:13]: Oh, uh, me personally?

**Michael Upshaw** [32:15]: Yeah.

**Jason Priem** [32:15]: Um, yeah, I mean, I think, I think the nature of what we're doing means that you end up having to do a lot of, like, investigating. I, I think there's, like, small R research and big R research, you know. Like I'm, I'm, I'm researching every day, right? [chuckles] Like, and, and doing, testing hypothesis and stuff like that, whether it's like publishable or not. I think I publish like... I don't publish very much. You know, I, I published a paper about OpenAlex, which, you know, then people cite because they use OpenAlex and stuff like that.

**Michael Upshaw** [32:41]: Yeah.

**Jason Priem** [32:41]: But I haven't, I don't think, published any like actual like hypothesis-driven research for some time.

**Michael Upshaw** [32:46]: Mm-hmm.

**Jason Priem** [32:46]: But I'm happy with that. I, I get to do like small R research of like just learning stuff about the world and turning that into hopefully a better product, and that, that suits me pretty good right now.

**Michael Upshaw** [32:56]: Well, you're certainly doing, um, uh, you seem to be doing the right thing because OpenAlex has been a sort of an astonishing, uh, success. So, um, so, um, um, uh, congratulations for, for, for the, the-- what you've achieved so far, and let's hope you can continue in the next, um, the next, uh, few years. Do you have any immediate plans for that? I mean, you, uh, do you have... What's your, what's your, um, um... I know it's a sort of a, a trite question to say, what do you plan to do in three to five years? But, um, [chuckles] do you have, uh, do you have sort of plans, uh, uh, uh, uh, for it?

**Jason Priem** [33:22]: That's a good question. Oh, I should mention too, my colleague Kyle Demes has been doing, publishing some good research in-

**Michael Upshaw** [33:26]: Okay

**Jason Priem** [33:27]: ... um, association with, um, some folks, uh, Juan Pablo Alperin, a couple other researchers. I, I should give them a shout-out.

**Michael Upshaw** [33:34]: Yeah.

**Jason Priem** [33:34]: I forgot about that. But yeah, we are, we are still turning out some research. I just, I personally am not quite involved.

**Michael Upshaw** [33:37]: Mm-hmm.

**Jason Priem** [33:38]: But yeah, your three to five years question, man, I tell you, I feel like anyone who has a really concrete answer for that question has not been paying attention to like advances over the last two years, like for real. Like I, I, I really think you really, really like have to take the stance of we're going to try to stay in a reasonable financial position, try and staff up with good people, and be extremely agile and flexible and open-minded because the world at the end of this year is gonna look very different from the world at the beginning of this year. I think as we see compounding interest in open and, um, uh, in AI developments, I don't know if you saw the Chinese like MIT licensed model that dropped today, like huge improve- like, I mean, amazing improvement in the open source model space, like hugely.

**Michael Upshaw** [34:26]: Mm-hmm.

**Jason Priem** [34:27]: That kind of stuff is happening every week or two. So I just think that, um, you know, I, I think, uh, Zuckerberg was talking recently, "Oh, we're gonna replace a bunch of mid-level engineers with AI." And like that just sounds like talk. That's actually going to happen, like maybe this year, maybe next year. That for real is going to happen. Like, and I think that you really have to be super flexible in that world. Um, we are definitely looking at switching a lot of our processes over from sort of old-fashioned, you said like machine learning based, you know, approaches to more generative AI approaches. And I think there-- we're going, as the cost of that goes down, I think we're gonna be able to roll out some really, really exciting things later this year. Um, we definitely have some good targets for this year. We're gonna be lo- rolling out, um, an analytics platform.

**Michael Upshaw** [35:14]: Oh.

**Jason Priem** [35:14]: So the current UI is really kind of around search and discovery.

**Michael Upshaw** [35:17]: Mm-hmm.

**Jason Priem** [35:17]: You type the thing, you find it, and then you can facet, you know. So it's a bit more like Scopus or Google Scholar-

**Michael Upshaw** [35:22]: Mm-hmm

**Jason Priem** [35:22]: ... or you... It's a discovery thing.

**Michael Upshaw** [35:24]: Mm-hmm.

**Jason Priem** [35:25]: But a lot of people use us for analytics. They want to try and say, "Okay, well, who at our university is collaborating on oceanography-

**Michael Upshaw** [35:33]: Mm-hmm

**Jason Priem** [35:34]: ... with people in the Global South?" Like questions like that are very like ana- and how is that increasing nuclear like analytics questions. And I think those questions are very interesting. I think they can be cool. They can be sometimes, again, that data can be misused, but I think they're interesting. And what we're trying to build is something that will answer those questions. It's like a much more in-depth, um, user interface to, to allow people to really like dive into the data. Um, and it's gonna come with the ability to download, uh, millions of rows, uh, as a table, just like that, like in a minute-

**Michael Upshaw** [36:06]: Mm-hmm

**Jason Priem** [36:06]: ... um, which I'm really excited about.

**Michael Upshaw** [36:08]: Mm-hmm.

**Jason Priem** [36:08]: Um, the ability to ask, uh, it'll come with a, a new query language that you can share like in a paper-

**Michael Upshaw** [36:13]: Mm-hmm

**Jason Priem** [36:13]: ... 'cause that's something people have, have asked about a lot. Um, [lip smack] uh, a lot of other goodies like that. Um-

**Michael Upshaw** [36:19]: Mm-hmm.

**Jason Priem** [36:19]: And oh, nested queries like, like and, or, and, or, and, or to like ar- nested to an arbitrary depth. So stuff like that, that I think people, um, a lot of folks in research analytics have been asking about. So that's, that's definitely something that'll happen this year. Um, and we're also gonna add a lot of sources. Like I'm, I was looking, I was in a meeting today and like we've got another We have about 200 and some, um, 200 something million, 250 million-ish, um, works right now.

**Michael Upshaw** [36:46]: Yep.

**Jason Priem** [36:46]: And we're, we were just looking at a, a, you know, potentially, you know, increasing that by at least 100 million, um, bringing in sources from repositories. So that's something that'll happen this year as well. So those are things that I, I can say are, like, on the, on the roadmap for us-

**Michael Upshaw** [37:00]: Yep

**Jason Priem** [37:00]: ... that I would be surprised if they didn't happen this year. But for a lot of the other stuff, like, just hold on tight and see what happens.

**Michael Upshaw** [37:06]: [laughs]

**Jason Priem** [37:06]: I'm really, really excited. I, I think, I think the, like, we're gonna be able to do stuff that we can barely imagine today, and, um, we're really excited to do that. The, the key thing for us is we'll just do it in the open. We'll make sure that it's totally open, and that it can be something we do together as a community.

**Michael Upshaw** [37:20]: Well, you're the first person I've interviewed who's described machine learning as old-fashioned. So, uh [laughs]

**Jason Priem** [37:24]: [laughs]

**Michael Upshaw** [37:24]: ... I think it's, um, so I think if, um, uh, if my new res- resolutions include the words, um, um, ecumenical and flexible, it sounds like, um, uh, I'll be, I'll be doing the right thing. And let's hope I can sort of, um, uh, I can sort of achieve the kind of same-

**Jason Priem** [37:37]: That's right

**Michael Upshaw** [37:38]: ... amazing things you've done. Anyway, thanks very much, Jason, for all your time, and really good to talk to you again. Thank you.

**Jason Priem** [37:42]: Oh, yeah, you too. Thank you so much for taking the time to chat and, uh, yeah, thanks very much for inviting me. It was a delight, uh, delight, delight talking and, uh, yeah, let's stay in touch.

**Michael Upshaw** [37:51]: Thanks. Very good. Thanks very much.

**Caroline Goldsmith** [37:52]: [outro music] We're so glad that you decided to join us today for this episode of ATG the Podcast. We hope that you'll tune in again next week for more content from the world of libraries, publishing, and scholarly communications. If you have any questions or comments for us about today's show or suggestions for speakers or topics for a future episode, we'd love to hear from you. You can use the contact form on the podcast website at atgthepodcast.com.

**speaker_3** [38:29]: This podcast brought to you in part by Liberated Syndication, podcasting made easy. For more information about Liberated Syndication, visit libsyn.com. That's L-I-B-S-Y-N.com. [outro music]

