---
title: "Mistakes Were Made"
person: selena-deckelmann
section: by
type: talk-transcript
year: 2012
venue: "linux.conf.au 2012, Ballarat"
source_url: https://www.youtube.com/watch?v=SL7pbj7B1hk
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 46
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Mistakes Were Made

*Speakers (inferred):* speaker_0=Host, speaker_1=Audience, speaker_2=Selena Deckelmann, speaker_3=Audience, speaker_4=Audience, speaker_5=Audience

## Transcript
**Host** [00:00]: Deckelman. And, um, please make her welcome. Thank you.

**Audience** [00:07]: [clapping]

**Selena Deckelmann** [00:08]: All right. Hi. Thank you. And thank you for bringing me a glass of water. Awesome. Uh, so my name is Selena Deckelman, and I founded a company called Prime Radiant that's actually working on these issues of failure, uh, trying to help companies fail a little bit less. Thank you. Um, so yeah, so this talk is about failure. And I've heard people use various euphemisms to describe this, such as prevention, risk management, risk mitigation. Um, there's some metrics around it, meantime between failure, meantime to recovery, and I think the most saccharine and not very useful one is success engineering. [laughs]

**Audience** [00:48]: [laughs]

**Host** [00:49]: That's engineering, right?

**Selena Deckelmann** [00:51]: [laughs] That clearly will work, right? Um, but, uh, so I think about this a lot. Sorry, I don't know why there's feedback, but, um, and what I've kind of distilled this down to... And I gave this talk once before, and I tried to learn a little bit from that talk as well, and I realized there was one thing that I had left out of my list before. But, um, I've kind of distilled out the lessons I've learned. I've worked in IT, system administration, network, uh, engineering, um, and as a DBA, which was probably the most full of fail. Uh, and these are the things that I try to remind myself of every time I'm in a situation where I'm dealing with a software upgrade, a maintenance window, an outage, you know, any- anything like that. Uh, the first thing is to plan for the worst. The second thing is to minimize the risk, and I actually don't think that you can eliminate risk. I don't know. Is there anybody here that thinks you can eliminate risk? Aw. Good.

**Audience** [01:50]: [laughs]

**Selena Deckelmann** [01:51]: [laughs] Pessimism. I like it.

**Audience** [01:53]: [laughs]

**Selena Deckelmann** [01:53]: Uh, third thing is you're gonna fail. Um, I, I don't know if it's gonna be a small failure or a big failure, but just preparing yourself for that and knowing that it's going to happen is actually quite helpful. And then finally, uh, recovering gracefully. Um, and I add the gracefully there because recovery can come in many forms. Those of you who are familiar with the, uh, alt system in recovery know all about this. Um, but I think gracefully is an important, is an important aspect of learning from your mistakes. And fortunately, I'm not the only one that talks about this. There's a lot of talk about failure. Um, there's Fail Blog, there's The Daily WTF, which is great for stories. Uh, and recently, Jim Hightower actually talked specifically about, uh, risk management and risk mitigation, and he was, uh, I think, actually working on a software project where a project manager came to and told him that they did not need a risk management plan and did not wanna spend the time or money on it because the project could not be allowed to fail.

**Audience** [03:00]: [laughs]

**Selena Deckelmann** [03:00]: [laughs] And the response to this was so great. There was so much great, uh, commentary on this, and I think this was my favorite. The, "Oh dear, they don't really know how this works, do they?" No, they don't. So the first step in any of this is admitting that failure is an option, and that it will happen. Um, and I think particularly in web operations and in free and open source software, um, we fail and we fix things all the time, and this is actually, uh, kind of a core competency of ours. Like, that we do pretty well in our projects and something that we can export out to the world. Uh, but I don't know that we do it systematically enough to really export it right now, but, you know, maybe. Fortunately, there are some people out there studying failure-

**Audience** [03:47]: [laughs]

**Selena Deckelmann** [03:48]: ... which I love. There's this guy, um, Jerker Denrel, and sorry about... I hope nobody has any seizures. This will all be over soon. Um, uh, [laughs] so this guy, Jerker Denrel, he's done a lot of studying in the business world about failure, and he publishes these fantastically titled, uh, papers about his research. And most of it is focused on the fact that business, uh, schools in general focus on only the success stories out there and not so much on the failure, which, you know, fundamentally is a problem since most businesses fail. And his latest paper that he published had this great title, which I'll just read it from over here. Um, Predicting the Next Big Thing: Success as a Signal of Poor Judgment. And what they had done is they looked at people who were, you know, uh, predicting, uh, important events, you know, kind of black swan type events, and then looked at the rest of their track record. Um, and they did this both in kind of an experimental way, and they also just took The Wall Street Journal and pulled predictions from people, so they have this, like, great data s- data source for this now. And they found that, uh, you know, uh, it was negatively correlated with judgment. [laughs] Predicting an important event. Thought that was awesome. Um, there's this other book called Everything Is Obvious that I've been reading, and it's all about common sense, causality, and hindsight, and most of us are familiar with the, you know, cau- uh, causa- or correlation is not causality, right? Um, and this book talks a lot about those issues and some of the problems with, uh, the way that history is interpreted, um, and how that important events... So is my laptop the one that's doing this? AV in the back? Hello?

**Audience** [05:31]: I think it might be.

**Selena Deckelmann** [05:33]: Is my laptop the one that keeps cycling through the-

**Host** [05:35]: You changed your resolution to ten twenty-four by seven sixty-eight. That will solve the issue.

**Selena Deckelmann** [05:38]: Yeah, I did.

**Host** [05:40]: No losing points.

**Audience** [05:44]: It's not.

**Selena Deckelmann** [05:44]: Sorry. I wanna fix that, 'cause that's really distracting, isn't it? Yes.

**Audience** [05:48]: Yeah. Thank you.

**Host** [05:50]: Failure isn't an option here.

**Audience** [05:52]: [laughs]

**Host** [05:53]: All right. Did you recover gracefully?

**Selena Deckelmann** [05:56]: Okay.

**Host** [05:56]: The current CD is your one.

**Selena Deckelmann** [05:58]: Okay.

**Host** [05:59]: There's another one to the-

**Selena Deckelmann** [06:00]: There's another one. There it is. Hello. Oh, yeah Do it

**Host** [06:11]: And this one can go onto-

**Audience** [06:15]: Confirm. Confirm.

**Selena Deckelmann** [06:17]: Confirm. Oh, God.

**Audience** [06:20]: [laughing]

**Selena Deckelmann** [06:22]: It takes a room full of engineers. Okay.

**Audience** [06:24]: [laughing]

**Host** [06:25]: Watch it, and it's like [laughing]

**Selena Deckelmann** [06:29]: [laughs] I didn't hear that. I'm sure it was sarcastic. Thank you.

**Audience** [06:33]: [laughing]

**Selena Deckelmann** [06:33]: [laughs] Um, so everything is obvious, even configuring your laptop, uh, for presentations. And, um, there's just some really great stuff in this book about social phenomena, the social phenomena that produces successes and how we attribute, um, causality to those successes, and that there's a fundamental problem with society if we don't start studying more of the failures instead of the successes. So there's, there's research out there supporting this, and I think that you're gonna see more really interesting science about this, uh, in the near future. So anyway, so whatever science, blah. Um, so, uh, this really... this talk is really a series of anecdotes that friends of mine, uh, people actually that I didn't know very well even. This one, uh, comes from New Zealand, um, which I met somebody at AusCon last year that told me this story, and I did actually look it up, uh, in the news so that I wouldn't get it wrong now that I'm actually in the part of the world that would know about it. Um, so, uh, basically, what happened is that all of New Zealand went offline. Um, this was about in two thousand and five. Some of you here may have-- Anyone present for that? Yeah, many of you, right? So you know this story. Um, so, uh, long story short, uh, there was a little rat, maybe a whole nest of rats, I don't know, that made a home in a very important fiber optic cable. And eventually, they chewed through it, right? So they chewed through this cable and okay, of course, there's a backup cable, right? And yeah, guess what? There was. There was totally a backup cable on the other side of the island. Unfortunately, on the day that this happened, there was a construction crew.

**Audience** [08:14]: [laughing]

**Selena Deckelmann** [08:14]: And they cut through that other cable. Um, and this in and of itself isn't the end of the world, right? Like, surely, you know, surely you can recover from that. But the problem was that the phone service was also running through this. So internets, internet and phone were taken offline at the same time. So, um, what was really great about the news articles is this totally like, oh, this is like perfectly, uh, [laughs] reinforcing my point, um, in this talk. Uh, getting two accidents of this type at the same time are freak occurrence. And what's funny is, um, so I was sitting in Melbourne just a couple days ago, and I was sitting with my friend Karen, and she's like, "Oh, this is an amazing story. I never heard of rats, like, taking down an entire country."

**Audience** [08:59]: [laughing] [clapping]

**Selena Deckelmann** [09:01]: She found another one. [laughs] But so that's not the end, right? Like, this is a great... This is so amazing. I was like, "I can't believe this happened again," right? Rats, like, in our cabling. So it happened on a Monday.

**Audience** [09:16]: Yeah. [laughing]

**Selena Deckelmann** [09:18]: And then it [laughing] happened again on Tuesday. It happened again. So okay, yeah, sure. It's freak occurrence, but wow. Yeah, it happens. So anyway, um, the point in all this is I think that we all need to plan for when things are going to fail, and we need to use the stories, uh, that are out there about these failures to help inform how we protect ourselves and our customers and our friends from what inevitably happens. So, um, there's another person in the DevOps community that, uh, occasionally dresses up in a firefighter's costume 'cause he's actually a vol-volunteer firefighter. Um, and so when I was thinking about this, the-- this is a very classic. I don't know. Do they do this in Australia, New Zealand, the stop, drop, and roll?

**Audience** [10:02]: Yeah. Yeah.

**Selena Deckelmann** [10:03]: [laughs] So I looked through-

**Audience** [10:06]: [laughing]

**Selena Deckelmann** [10:07]: [laughs] I know about you. Sorry, I laughed too loud, but, um, [laughs] trying to protect you from my laugh here. Uh, so this was the most hilarious one. I looked at thousands of these, and this was by far the best. Um, and so I thought I would translate this into what-

**Audience** [10:20]: [laughing] [clapping]

**Selena Deckelmann** [10:20]: ... Ops people should do. [laughs] 'Cause I think it's pretty simple, right? Um, and, like, who better to help us than Cookie Monster? Yeah. So anyway, so I hope you don't find this too insulting. I just thought it was hilarious. I really, I really think that it's three basic things to prevent, uh, well, maybe not prevent, but to, to help you, help you deal with, uh, failure: uh, document, test, and verify. Um, and this is also something that's really easy to explain to your management, right? Simple words, small. Um, so all the rest of this are just some stories. Um, people, people were really generous with their awesome stories. So this first one is about a failure to document. Um, I forget the name of this blog right now. Um, it's something like There I Did It. Something-

**Host** [11:12]: There, There I Fixed It.

**Selena Deckelmann** [11:13]: There I Fixed It, yes. Best blog ever. Love it. Um, so, uh, this one, that is actually a server rack that someone was moving from-

**Audience** [11:22]: [laughing]

**Selena Deckelmann** [11:23]: [laughs] data center to data center. They were actually moving it to another data center. Uh, so, uh, this guy, David, uh, contacted me and let me know that he, he had installed a server at, you know, some major hosting provider or whatever, and they were doing a maintenance window. And they, you know, notified him, let him know what was going on, uh, told him the times, like everything was good. Uh, and then the engineers get to the data center, and they take everything out of the rack. Well, almost. They get to his server, David's server, and they couldn't unscrew it. It was stuck. So I-I've totally had this happen to me before. But anyway, so that happened, and they were like, "Oh, okay. So well, what we'll do is we'll just leave it in that rack. We'll move everything else, and we'll come back and fix that server in some future maintenance window." So a couple days go by, David's server's not back up. And he's like, "What's going on?" And it wasn't that important of a thing. I think it was, like, a test server or something. So he contacts them, tries to figure out what is going on, and they're like, "No, it was totally-- It was in our scripts. Like, it totally should come back up. I don't know. Okay, we'll send somebody out there to check it out." So he looked at it, and it was still off. And basically, what had happened is that they went through, and they had left that server there, and their startup script, um, relied on someone saying that the server had moved. And when the server moved, everything could come back up. Well, that server didn't move.

**Audience** [12:42]: Mm.

**Selena Deckelmann** [12:42]: So yeah, so really simple failure, but one that resulted in two or three days of downtime. Um, so I think failures to document often come down to one thing, which is writing documentation. Um, that didn't happen in that case. But, uh, I think the first step for all of us is to write documentation. Um, and that may be actually in the form of code, but leave that as an exercise to the audience. Um, and then the second biggest failure that I see in my work life is updating that documentation. I count myself among those people. Updating documentation sucks. Um, there's a lot of reasons why it sucks, but it's hard. Um, so one of the things that I've tried doing in all of my operations work is making updating the documentation a step in the plan. Um, whether it's, you know, step ten or step two, I don't know. But, uh, adding it to your plan makes a huge difference because it's right in front of you when you're going through. Hopefully, you have a checklist, uh, going through your plan and executing it. Um, and then the other trick that I've added over time is putting a fixed amount of time to it 'cause often these documentation updates, it's seriously, like, sixty seconds, and you would fix a small typo or something important so the next person that comes along doesn't stumble on it. But when you don't have a fixed amount of time set to it, you're like, "Ugh, it's gonna take, like, a month. Like, ugh, an hour maybe to fire up the browser and log in," blah, whatever. But if you just say, "Okay, I'm gonna spend five or ten minutes on this, um, and then I'm gonna stop," then at least you get something in there rather than nothing. Um, some of the documentation tools out there are really terrible. I think one thing that would help us all are having some graphic designers come in and show us how it's done. Wikis are-- have terrible user interfaces. They just look truly awful, and I don't blame people for not wanting to update them. Um, I have seen some pretty neat stuff out of Sphinx and some default templates that look quite nice for those of us that use Python around here. I mean, I think small diagrams, um, even if they're sketched out, you know, and you take a photograph of it with your phone and put it up, that can solve a lot of confusion. You know, a picture's worth a thousand words, right? Doing that can help a lot. Uh, having timelines for the documentation that explain, um, you know, when you're supposed to update it, uh, also, uh, how long operational changes are gonna take. That really helps. Having a bug tracker really helps, which I'm kind of a hypocrite here. I work for-- you know, w-work with the Postgres project, and we don't have a bug tracker. But bug tracking really helps. Um, and finally, I think ordered to-do lists. Whenever you're dealing with, uh, maintenance operations, actually making the list and sharing it with people and numbering it, uh, helps everyone know what's actually gonna happen. So my second failure story, or I guess this is, like, the third failure story, um, is about the failure to test. So in my first job, I made a lot of really awesome friends. Um, and one of my friends told me about when she first started as a sysadmin, and she was actually hired as a, a technical writer, but, you know, they gave her root. And so-

**Audience** [15:52]: [laughing]

**Selena Deckelmann** [15:53]: She was-

**Audience** [15:54]: Oh no.

**Selena Deckelmann** [15:55]: She, she was, uh, sitting one day, and it was, like, her first day on the job, and she's like, "Oh, nobody really gave me anything to do. What should I do? Oh, I should tidy this up." So she starts looking around. She's like, "Oh, there's all these zero-length files. That seems really messy." Um, she's like, "Oh, I just learned how to use this command find." Okay, so find./n zero length, blah, blah, blah, blah. "Oh, there's a lot of these. All right. I'm gonna just use dash delete return." [laughing] Oops. Um, fortunately, they had a backup, and they had to restore from backup. It's a Solaris box. But anyway, um, yeah, so, uh, oops. So this I do really think is a failure to test. Um, and one of the things about testing is that you need to verify what your success criteria is. What does success look like? It probably doesn't look like needing to restore from a backup, for starters. And had she taken a moment and asked someone, I'm sure that someone would have been like, "Oh, God, don't do that," you know? But she didn't. Um, so anyway, yeah, first of all, verify your su-success criteria. Um, second of all, actually write the tests. Uh, and this can be very simple, right? It can just be a shell script. It doesn't have to be complicated. Um, the third thing is testing with a buddy. I, I think that, um, you know, again, having that second set of eyes on what you're doing is super helpful. And finally, just having a plan. Like, she didn't really have a plan. [laughs] Just wanted to tidy things up a little bit. Um, and when you have a plan, uh, I would say that that plan should involve other people. Uh, so yeah. Um, for testing tools, there's a lot of testing frameworks out there in whatever language that you wanna use. So if you're a developer, um, you can go out there and use, use your favorite one. Um, I think repeatable shell scripts are incredibly underutilized. Uh, I know that, uh, configuration management and, uh, deployment tools are super important, but you don't always need those to test changes. So try shell scripts. Um, and finally, having a staging environment. You know, like, if, if only my friend had had, you know, a spare server to run her cleanup routine on, she would have maybe, uh, you know- Notice that the server was going to crash before she ran it in production. Um, so yeah, one major failure can often convince management that you really need a staging environment. Not that I'm saying that you should, you know, engineer one. But, [laughing] um, yeah, staging environments, great. So another failure out there is the failure to verify. And lest you think that I just point my fingers at other people, I'm gonna tell you a story from my own life, having failure recently that was actually kind of inspiration for this talk. Uh, so I work a lot with Postgres, and I was a consultant for a few years. Um, and it was my birthday. And, uh, we had this customer that had a very important data migration. They were in AWS, you know, and they were a startup, whatever, and they really wanted to do it at midnight on my birthday. And I was like, "Oh, man, this sucks." You know, my husband had already, like, gotten us, like, a place to stay. We're gonna go to a show. It's gonna be awesome. So I was like, "Okay, here's what I'll do. I'll have my, uh, coworker actually, like, write all the scripts and do everything, and I'll just kinda run shotgun, you know, while we're... or not shotgun, but, you know, uh, on the side. I'll be, I'll be copilot for this thing." So go to the show, have a great birthday, go to my hotel room, it's midnight, fire up my computer, and we begin. Um, and this involved doing a pg_dump. So how many of you here are familiar with eight dot four and earlier Postgres? Anybody? A few of you? So what does dash D do? Anyone? No wrong answers.

**Host** [19:41]: Based on guess amount.

**Selena Deckelmann** [19:42]: [laughs] Well, not necessarily bad. Well, the correct answer before eight dot four is it does something different depending on which command line tool you're using.

**Host** [19:53]: [laughs]

**Selena Deckelmann** [19:54]: So I did not test his scripts, and so I did not notice that, uh, his dump script dumped out insert statements instead of copy. Uh, and what that means is that, uh, when you restore it, it's gonna be really, really slow. And this was in AWS, which for those of you who are familiar, is really, really slow. Um, so anyway, uh, two hours later we're like, "This isn't done yet. [laughs] What's going on?" And we discovered the mistake. And, uh, twelve hours later, we were mostly done. So what did I learn? [laughs] First of all, have a plan for when things go wrong. Uh, we did not discuss what we were going to do if this would fail because all of the tests that had run had finished in about twenty minutes, uh, in the staging environment. Uh, and so we hadn't talked to the customer really about, you know, when the cutoff time would be, when we would really, like, stop things, pull the plug, uh, 'cause we were like, "Oh, this is such an easy, simple change on my birthday at midnight." [laughing] Um, second, uh, when I say staging environment, definitions of this may vary, but one important thing about a staging environment is that it is the same or, you know, really a lot the same as a production environment. We were testing with data that had just been generated from some silly script that really had nothing to do with the data that we were migrating. And so it was in fact like that big when the data we were migrating was this big. It's very different, right? So, uh, yeah, we, we failed in that regard. And finally, um, you need to test your rollback plan. And I guess that presupposes that you have a rollback plan, [laughs] um, not just your implementation plan. Uh, and, you know, we, we had tested a rollback plan, but not one in a production environment, and so we were kinda stuck and just had to move forward. So verification tools here, I really think it's people a lot. It's having the staging environment and then having the people to really look at it and then not flaking out [laughs] uh, when you're getting ready for a maintenance window. You really do need to run through all this stuff yourself because you might just catch like a little typo like dash D. [laughs] Um, so now we go into the other couple failures that I added at the end. Um, first one is the failure to imagine. Um, so my friend Maggie works for a fairly large, uh, university system. And the bottom line for them was that they [laughs] couldn't trust anyone anymore. Um, they're responsible for a bunch of data centers, and they were having a very interesting power problem. Um, and none of the existing systems to monitor it detected it. Uh, they had, you know, failover. They had UPSs and, you know, surge protection and all that stuff. But what they got was a brownout. And it was a sustained brownout that lasted for, you know, I think something on the order of three to four hours. And none of their systems detected it. In fact, their primary and secondary and then tertiary systems failed, uh, before it was, before they root caused what the issue was. Um, that was a very expensive, uh, problem. And when they got together to kind of assess, like, what they were going to do to solve this and have it never happen again in the future, um, a lot of fingers got pointed around. They were like, "Oh, the power company really needs to be monitoring this and detecting this and notifying us when something like this happens." The power company is not equipped to do that, at least not in, you know, in her part of the world. I don't know if they could do better here, but they really didn't even know how to begin to do this, uh, properly for them. And so what they ended up doing after they bought, you know, rebought all of this really expensive UPS, uh, rebought UPSs, was they installed their own monitoring, um, at the point where power was coming into the university so that they would know in the future when they had a brownout. Um, and this is something that is still used as a lesson in their group today about how you just shouldn't trust incoming power or information. So failures of imagination are really difficult to deal with, right? Like it's your imagination. Like if you can't imagine it, how can you imagine it? I think really the most important thing is sharing stories of failure, 'cause hearing about how other people are feeling helps you learn before maybe you make exactly that same mistake. I think another thing that's really important is just talking to people that are different than yourself. Um, I often learn a lot from people who are not in IT, who work in the business world, who are artists, who, um, are musicians, whatever. They experience very different types of failure than I experience on a daily basis, and sometimes that helps me, you know, think outside the box there. And then the last thing I think that really helps with imagination is actually acting out your implementation scenario. Um, sometimes this is impossible, um, in person because, you know, I work from home. I work with a distributed team. But I still think that we can take lessons from the construction industry. Um, whenever you build something, at the end, you create a punch list. You walk through with people. You don't just sit in a room and talk about what's working and what's not working. You go out there and you look at it. And I think that, um, particularly for maintenance windows, when you're moving equipment, you know, like that example of the screws not coming out, you know. Um, if you were to actually, like, go to the data center and look at what you needed to move, saw that several cables were just a little bit too short to reach when you plug them back in, um, that would help prevent a lot of wasted time and money. So the last failure that I like to talk about is the failure to implement, which is probably the worst failure, right? Now you're rolling back or maybe you're just, like, utterly failing and running away, trying not to get burned on your way out. Um, and the only way to recover from this is really to try to re-implement what it was that you were doing in the first place. Uh, and to me, that is learning from your mistakes. And this is the postmortem, right? Reflection is a part of pretty much any profession. Um, my husband's a teacher and, you know, one of the, uh, courses that they taught, like an entire course on keeping a notebook and reflecting on a daily basis on your teaching so that you can learn from day to day about what's happening with your students, what's happening with yourself, and then to try to apply that, um, to be a better teacher. And I think that we can learn a lot from that. Um, and so anyway, so whenever I'm planning, uh, maintenance windows and outages, the first thing I plan to do is plan to have a postmortem and making it clear with everyone from the beginning that this is going to be something that's going to happen whether or not everything is successful. Uh, because honestly, like, even if everything goes totally right, something went wrong, and I wanna talk about it. So, uh, yeah, if you set that expectation, I think that people also deal with the idea of a postmortem in a much better way. I wish there was a better name for it, but I don't really know that there is, uh, 'cause everybody thinks that, you know, you go into this room and you're gonna get blamed for things, but-

**speaker_6** [27:18]: Debrief.

**Selena Deckelmann** [27:19]: Yeah, debrief. Yeah, you could say debrief.

**speaker_6** [27:21]: [laughs]

**Selena Deckelmann** [27:25]: [laughs] Yeah. Yeah, I wish we had a better name. I don't know. I've, I've tried a few different things. [laughs] But everybody knows what this means and those other things, I don't know. We-- Let's talk about that after this. All right. Um, so anyway, so beforehand, you wanna document your plan with numbered steps and also a timeline. Um, I even do this with my meetings, which is kinda, I guess, weird. But, um, uh, you know, I say that there's a certain amount of time that's gonna be allocated for each one of these steps, and when I'm running through it, I try to see, am I gonna meet those timelines? Am I gonna meet my expectations? Um, also test the plan and test the rollback plan. And then there's always gonna be a point of no return where you don't wanna spend that much time. You know, you don't wanna spend twelve hours, maybe two might be okay. Um, and you also have to ensure that there's enough time for you to actually roll everything back. So identifying that, that time and then having someone that's gonna check on that time is really important. Um, during maintenance windows, so I often work with a distributed team where nobody's, like, in the same room. But even when people are in the same room, I tend to do this anyway. Um, setting up some kind of screen sharing so that, you know, if for some reason I have to, you know, I don't know, go to the bathroom, somebody else can, uh, pick up, uh, where I left off immediately without too much, you know, IT wrangling. Um, we also have a chat room, set up IRC, um, AIM, Campfire, like, whatever. Something that has logging. You know, setting up a bot in IRC is great because then you, you know, anybody can jump in and then look at the history and figure out what had happened. I also set up a voice line and have a headset. Um, people-- You can communicate so much faster when you're speaking, um, and you can also be typing at the same time, which is awesome. You don't have to take your hands off the keyboard when you're watching something that maybe is going well or not. And also, I like to designate a timekeeper, somebody whose sole job it is, not the person that's running the maintenance window, but someone else who can do time checks and make sure that if you reach that point of no return, that you actually start your rollback plan. And afterward, like I said before, I try to schedule documentation updates as part of the whole plan, um, and schedule the postmortem to identify those areas of concerns. And when we do the postmortem, we talk about the successes, we talk about the failures, and then we really only identify, uh, one or two things that we're actually going to try to change. Um, often people will come up with these, like, insanely long lists of every single thing that you can change, but really, let's be honest, one or two is probably what we're going to change. [laughs] So just limit it to that, and then you can succeed when you actually do try to change things. So this is-- If there's one thing you take away, this is it. I think that that just about covers it. Plan for the worst, minimize risk, fail, and recover gracefully. Um- And you can also use this if it makes, you know, people on your team laugh. [laughs] Talking to me test to verify. So, um, I think I ended just a little bit early, so-

**speaker_7** [30:35]: You've got 15 minutes.

**Selena Deckelmann** [30:36]: We've got 15 minutes, so, um, anybody wanna tell some horrifying stories? I love it.

**speaker_7** [30:40]: [laughs]

**Selena Deckelmann** [30:42]: Bring on the fail. Yes, in the front.

**speaker_7** [30:46]: [laughs]

**Audience** [30:47]: So initially, one thing, not a story, but, uh, you mentioned earlier on that, uh, define success and that restoring from backup is not success. But I actually completely disagree with that one, and in fact, in many of our change control processes, the rollback is restore from backup because we define success as restoration of service, not that we've succeeded to change. Um, and-

**Selena Deckelmann** [31:09]: Yeah. No, I agree with that.

**Audience** [31:11]: Yeah. Uh, as for a story, failure to plan, um, would be, uh, in the construction industry, in the road, roading industry, which is very relevant, which was digging up the southern motorway in Auckland, which is a rather important motorway, at, uh, one AM on a Sunday night/Monday morning with a plan that it'll be done by three AM. Uh, nobody thought about what to do when they made a mistake, and when they were gonna call the rollback, and how long it would take to do a rollback. At five AM, they decided they'd better roll back this change. Unfortunately, the change was not a, uh, script. The change was a ginormous hole in the middle of the motorway that was full-

**Selena Deckelmann** [31:53]: [laughs]

**speaker_7** [31:54]: [laughs]

**Audience** [31:54]: That was completely filled to the brim with sewage.

**Selena Deckelmann** [31:57]: Oh. [laughs]

**speaker_7** [31:59]: [laughs]

**Audience** [32:00]: That was constantly being pumped out.

**Selena Deckelmann** [32:02]: Oh.

**Audience** [32:02]: So putting a metal plate over it and tar sealing it, which is a one-hour job, and theoretically could have been done-

**Selena Deckelmann** [32:08]: [laughs]

**Audience** [32:08]: Would not work when sewage was pouring out of said hole.

**Selena Deckelmann** [32:12]: [laughs]

**speaker_7** [32:13]: [laughs]

**Audience** [32:13]: Uh, Aucklanders here may remember that day because it was the day when the motorway was effectively shut on a Monday morning.

**Selena Deckelmann** [32:18]: [laughs]

**speaker_7** [32:19]: That's true.

**Selena Deckelmann** [32:20]: See, stories like that make me really happy to work in IT. I'm like, "Yes."

**Audience** [32:24]: Yeah.

**Selena Deckelmann** [32:24]: [laughs]

**Audience** [32:25]: We deal with shit when routers fail. They deal with shit when shit fails.

**Selena Deckelmann** [32:30]: [laughs]

**speaker_7** [32:31]: [laughs]

**Selena Deckelmann** [32:32]: Perfect. I'm so glad that was recorded. Yes.

**speaker_7** [32:35]: [laughs]

**speaker_8** [32:39]: Um, yeah, I've had two of the power failures that... Well, power failures like you mentioned there. I've had the one where the UPS, the feed into the UPS was not, was not good enough, and it was running low, and I'm like, "Okay. Okay. Final. I'll monitor the inpa- inbound power on my UPSs to catch this one."

**Selena Deckelmann** [32:55]: Yeah. My, my friend Maggie calls that, uh, you know, there's, there's, like, you know, brown outs to an individual computer. That sucks, right? And you're probably gonna lose your computer. But, uh, you know, when you're talking about data centers and that much power, it's logarithmically more bad. And yeah, it's just terrible.

**speaker_8** [33:11]: Well, then I, then I learned to really not trust anything when the voltage regulator that we'd put in upstream from our one stopped working as well. It, it-

**Selena Deckelmann** [33:19]: [laughs]

**speaker_8** [33:20]: 'Cause previously I'd been monitoring for gross mistakes 'cause, like, I'm expecting two 30, tell me if it plops below two 20, and I'll worry.

**Selena Deckelmann** [33:29]: Right.

**speaker_8** [33:29]: This time the A- the voltage regulator here just stopped working, and it just fed through dirty power. And now it's like, "Oh, so I actually have to monitor if you go out of band by a volt?"

**Selena Deckelmann** [33:39]: [laughs]

**speaker_8** [33:40]: "'Cause that means you've failed." So it's like-

**Selena Deckelmann** [33:42]: Wow

**speaker_8** [33:42]: ... catch me once. Oh, wait, you caught me twice. [laughs]

**Selena Deckelmann** [33:45]: Yep. Awesome. Brianna's here. Oh, oops.

**speaker_7** [33:56]: So in a recent history w- our organization did, developed a cut-over plan for a service to DR because that was the higher avail-- that is the higher availability plan for that service if we need to do anything to the service.

**Selena Deckelmann** [34:10]: Right.

**speaker_7** [34:11]: So we, we developed the plan. We tested the plan. Then we had server hardware failure in the production site, and we'd gone, "Cool. We've got a plan."

**Selena Deckelmann** [34:20]: [laughs]

**speaker_7** [34:22]: "We're gonna cut over to DR for a week, take this server out, replace the RAM in it," 'cause I had RAM failure. Who has RAM failures? Anyway.

**Selena Deckelmann** [34:30]: I do all the time. [laughs]

**speaker_7** [34:33]: Anyway. ECC errors on, in main memory. Anyway.

**Selena Deckelmann** [34:37]: Yeah.

**speaker_7** [34:39]: Three days after cutting over to DR, the archive logs on the database server filled the box.

**Selena Deckelmann** [34:49]: [laughs]

**speaker_7** [34:50]: Because when we tested the DR plan, we tested it for a day.

**Selena Deckelmann** [34:56]: [laughs]

**speaker_8** [34:58]: Yeah. [laughs]

**speaker_7** [34:59]: [laughs]

**Selena Deckelmann** [34:59]: Yeah. Yeah. Yeah, test the whole plan.

**speaker_7** [35:01]: [laughs]

**Selena Deckelmann** [35:01]: Yeah. Not just a fifth of it or a seventh of it. Yeah. Great.

**speaker_7** [35:04]: And, and someone said, "No, it was only a DR plan for going to DR for a day." And I said, "No, it wasn't." [laughs]

**Selena Deckelmann** [35:12]: [laughs] Yeah. That might also be read the plan. Sorry, I didn't include that in the slide.

**speaker_7** [35:15]: [laughs]

**Selena Deckelmann** [35:15]: That was good. Nice.

**speaker_7** [35:16]: Okay.

**Selena Deckelmann** [35:17]: So, uh, Brianna down here, and then maybe we can move the thing to the other side. Person with the mic, she's down here.

**speaker_9** [35:28]: Uh, I just wanted to mention a report that might be of interest to people who like reading about failure, um, that the Victorian government, uh, ombudsman released called Own Motion Investigation into ICT-Enabled Projects, uh, where it was about public sector IT projects. And, uh, I think actually it was an excuse after we had a change of government for the new government to dump on the handling of these projects by the previous government.

**Selena Deckelmann** [35:56]: Oh, yeah.

**speaker_9** [35:56]: But it is quite interesting reading. And so it covers, uh, 10 projects in a bunch of different departments, including, uh, MyKi is one of them. Uh-

**Selena Deckelmann** [36:06]: Oh, wow. Nice

**speaker_9** [36:06]: ... and so they talk about the themes which are, like, leadership, accountability, governance, planning, uh, project management. And so it's probably on a little bit larger scale than this, but, uh-

**Selena Deckelmann** [36:15]: [laughs]

**speaker_9** [36:15]: For anyone who's interested, there's a lot of fail in there.

**Selena Deckelmann** [36:18]: [laughs] That's awesome. Want a link. Maybe move over to the other side. Sorry, I'm making you go everywhere. Yes.

**speaker_10** [36:29]: Just on Victorian government fails-

**Selena Deckelmann** [36:31]: [laughs]

**speaker_10** [36:31]: Um, there's also an excellent book on the Longford gas explosion. Um-

**Selena Deckelmann** [36:36]: The what?

**speaker_10** [36:37]: So, um-

**Selena Deckelmann** [36:39]: Sorry, I missed.

**speaker_10** [36:39]: Okay, this is a better anecdote than the one I was gonna tell anyway. So there was a gas processing plant that handled around 90% of Victoria's natural gas per- needs.

**Selena Deckelmann** [36:50]: [laughs]

**speaker_10** [36:51]: Now, over time, the engineers moved off site, and let's just say the, um, the management system for the plant became noisy. So it became routine to ignore-

**Selena Deckelmann** [37:08]: [laughs] Processing.

**speaker_10** [37:10]: Um, yeah, ignore alerts-

**Selena Deckelmann** [37:12]: Never mind that noise.

**speaker_10** [37:13]: I- yeah.

**Selena Deckelmann** [37:14]: [laughs]

**speaker_10** [37:14]: Uh, th- those are just routine alerts.

**Selena Deckelmann** [37:17]: [laughs]

**speaker_10** [37:17]: You can ignore those.

**Selena Deckelmann** [37:18]: Yeah.

**speaker_10** [37:19]: Um, eventually what happened was there was, um ... It got too cold. It boiled over. There was a massive explosion. The entirety of Melbourne was without gas for ... Was it two weeks?

**Selena Deckelmann** [37:31]: About two weeks.

**speaker_10** [37:32]: Oh, yeah.

**Selena Deckelmann** [37:33]: Oh, Vic- all of Victoria. No, just-

**speaker_10** [37:34]: In the middle of winter.

**Selena Deckelmann** [37:36]: [laughs] Oh. Except for Southbank. [laughs]

**speaker_10** [37:41]: Yes. Yes, except for Crown Casino. Um-

**Selena Deckelmann** [37:45]: [laughs]

**speaker_10** [37:46]: Who, who, who, for two days were quite visibly using their very large gas burners-

**Selena Deckelmann** [37:51]: Oh. Yeah.

**speaker_10** [37:52]: For two days.

**Selena Deckelmann** [37:53]: Wow. All right.

**speaker_11** [37:59]: I sus- I suspect, I suspect we can collect a lot of great fail stories like that. One I was told a-

**Selena Deckelmann** [38:07]: [laughs]

**speaker_11** [38:07]: About, uh, the year 2000, uh, problem in Queensland, um, in the ... with the electricity generation. The, uh ... I was told by one of the engineers working there that they, they knew that the whole, um, system for monitoring the boilers that maintain the steam pressure for the generators, um, was not year 2000 compliant. They had no idea what would happen when it, when year 2000 rolled over. So the engineers were trained, you'd go up to a boiler and hum at a certain frequency, and if it hummed back at a different frequency, you knew it was okay.

**Selena Deckelmann** [38:54]: [laughs] That's the UI?

**speaker_11** [38:56]: Yeah. [laughs]

**Selena Deckelmann** [38:58]: [laughs]

**speaker_11** [38:58]: But the other, the one I wanted to ask about was-

**Selena Deckelmann** [39:01]: Yeah

**speaker_11** [39:01]: ... you ... I, um, I was speaking to one of the developers in the, one of the projects that I work with-

**Selena Deckelmann** [39:09]: Yeah

**speaker_11** [39:09]: ... uh, who said, uh, "We don't need to ... We just don't have time to write any documentation, um, because it's all there in the code. You know, the, the code is the documentation anyway."

**Selena Deckelmann** [39:23]: Yeah.

**speaker_11** [39:23]: Uh, and I really liked your idea of saying, "Okay, well, every process you do should just include a five-minute or a 10-minute or whatever, a, a, an amount of time for updating the documentation."

**Selena Deckelmann** [39:35]: Yeah. Thank you.

**speaker_11** [39:36]: Do you have other ideas that, uh, you fi- uh, can turn around people who are saying, "Oh, no, you know, it's way too expensive for us to actually, you know, test our software," to, to get them to implement some of those things?

**Selena Deckelmann** [39:50]: Put them on the on-call roster. [laughs]

**speaker_11** [39:54]: Right.

**Selena Deckelmann** [39:57]: Ah, spoken like someone who's been working at 4:00 AM.

**speaker_11** [39:59]: That, that might be something that the sysadmins are working on right now, but-

**Selena Deckelmann** [40:02]: Yeah. [laughs] Um- Make them carry their personal cell phone. Yeah. It's really ... Yeah, so dealing, dealing with people who really don't wanna document anything, it's really hard. I mean, um, unless you have a management structure that is going to reinforce good behavior, um, it's often very difficult to change an individual person's behavior. Um, so yeah. So I don't have a great answer for that. I think the five-minute thing often will help a lot. Um, the other thing is sometimes I, uh, show people that they often can take, uh, user bug reports, uh, good ones, and turn that into documentation 'cause often the user will, you know, say, "I did this, this, this and this, and then it exploded." And then you fix it, and that's a piece of documentation. Um, and we've done that quite a bit actually for, uh, certain things in Postgres, you know, for certain types of setting up the database things. That seeded a lot of wiki content, people just taking their, their emails. That was authoritative. Yes.

**speaker_11** [41:00]: [laughs]

**Selena Deckelmann** [41:01]: Um, uh, but yeah, so sorry. Individual behavior is really difficult to change, but if maybe you can, like, you know, management beat them and tell them that they have to do it, then sometimes.

**speaker_10** [41:08]: If it's valuable enough, hire a tech writer to document for them.

**Selena Deckelmann** [41:11]: Yeah. Find a person that's willing. [laughs] You know, I generally try to convert the willing, so.

**Audience** [41:16]: I just wanna reinforce, um, one of your comments earlier about the timekeeping.

**Selena Deckelmann** [41:22]: Yeah.

**Audience** [41:22]: Um, our fi- our maintenance fails, we had a timekeeper, but the timekeeper was not independent of the people who were doing the maintenance procedure. That was me.

**Selena Deckelmann** [41:30]: Right.

**Audience** [41:30]: And the problem is with that, you get completely emotionally invested in seeing the thing through to a success.

**Selena Deckelmann** [41:38]: Yeah.

**Audience** [41:38]: If, if-

**speaker_10** [41:38]: It's only five minutes away.

**Audience** [41:39]: Yeah, exactly.

**Selena Deckelmann** [41:41]: [laughs]

**Audience** [41:41]: And five minutes later, it's still only five minutes away.

**Selena Deckelmann** [41:44]: Yeah.

**Audience** [41:45]: And double the length of your maintenance window later, you still have to execute your rollback plan.

**Selena Deckelmann** [41:49]: Right.

**Audience** [41:49]: So it's critically important that the timekeeper is not one of the people who's emotionally invested in seeing the change through.

**Selena Deckelmann** [41:55]: Yeah. And one thing that I would say is, um, for people that have good relationships with their customers ... And so I've often worked for IT departments that are inside a company, and so my customers are inside my own company. Uh, we often would invite a customer to be part of the maintenance window so that they get to enjoy, you know, staying up until 4:00 AM with the rest of us. Um, and then you give them a job, which is the timekeeping. Uh, so you know, that may be one way to get them involved from the beginning and have them see what's going on, and it also might help convince them that, you know, maintenance windows that end at 4:00 AM are a bad idea. Do your customers really smile if they can do that? Uh, they can keep time? Yeah. [laughs] Ha ha. Not true. Okay, next.

**Host** [42:33]: Um, I've been told that in the health industry, they have a culture of a morbidity and mortality analysis when something bad happens.

**Selena Deckelmann** [42:41]: Mm.

**Host** [42:41]: Which is specifically a closed-door conversation where no blame is attributed. And we started doing that where I work, and it works quite well as a postmortem when something bad does happen.

**Selena Deckelmann** [42:52]: That sounds awesome. I wanna know more about that.

**Host** [42:54]: Tell us more about it then.

**Selena Deckelmann** [42:56]: Yeah. Maybe we should have a boff about morbidity and mortality.

**speaker_12** [43:00]: [laughs]

**Selena Deckelmann** [43:03]: And stickers. Okay. [laughs] Yes? Any stickers?

**Host** [43:09]: We've got about three or four minutes left.

**Selena Deckelmann** [43:10]: Uh, anybody... Oh, up here. Right up here.

**speaker_12** [43:14]: [murmuring]

**speaker_13** [43:16]: So, documentation is great, but if it's too cumbersome, nobody r- bothers reading it.

**Selena Deckelmann** [43:21]: True.

**speaker_13** [43:21]: And a large Australian bank about seven or eight years ago, they have a great change management system. It's exhaustive. You document everything. No one ever reads the changes because it's too painful.

**Selena Deckelmann** [43:33]: I love rape on documentation.

**speaker_13** [43:33]: So one day, the guy who needed to w- do work on the city power came in when his change was scheduled, and the guy who was doing work on the UPS came in when the change was scheduled, and the guy who was doing work on the generators came in when the work was-

**speaker_12** [43:51]: [laughs]

**speaker_13** [43:53]: And on that day, one of the big four Australian banks went down for a long, long, long time.

**Selena Deckelmann** [43:59]: [laughs] Oh.

**speaker_13** [44:02]: But nobody wants to read the documentation. There's too much, and it's too hard to use.

**Selena Deckelmann** [44:06]: Yeah. Oh, man. Yeah, there was this terrible story in the Daily WTF just the other day, um, about a guy that this company, they were not really very happy with his work, so they were kind of excited to send him off to decommission this, um, uh... How many-- Have you guys already heard this? A couple of you probably have. Yeah, they sent him off to, I think it was like the Cayman Islands or something, um, to decommission a, a mothballed data center, and they had... Mm, the crux of the story is that, that there were two data centers on the island.

**speaker_12** [44:37]: [laughs]

**Selena Deckelmann** [44:39]: I don't need to finish that sentence. Okay, next. [laughs]

**Host** [44:42]: This will be the, the last question.

**Selena Deckelmann** [44:44]: Okay.

**speaker_14** [44:45]: Hey, it's actually a comment rather than a question.

**Selena Deckelmann** [44:47]: Okay.

**speaker_14** [44:47]: I agree with and appreciate everything you said about checklists and, uh, go, no-go points and things like that. One thing I would add to that is it's really good to have some decision-making guidelines before you go into a, you know, a push or a migration, whatever you're gonna do.

**Selena Deckelmann** [45:00]: Right.

**speaker_14** [45:00]: Um, and one of the rules that we implemented early on was three strikes rule, um, for rollbacks. If three things go wrong, we're gonna roll back.

**Selena Deckelmann** [45:08]: Oh, that's really good.

**speaker_14** [45:08]: Um, because at some point you're just scrambling and scrambling, and you should probably, like, sit back and try again another day.

**Selena Deckelmann** [45:13]: Yeah, I really like that. Yeah.

**speaker_14** [45:15]: Yeah.

**Selena Deckelmann** [45:15]: Three strikes. Uh, it's Laura from Mozilla. Hey. All right. Cool. Thank you all so much. Really appreciate it. [clapping]

**Host** [45:31]: And on behalf of Linux Australia, I would like to thank you for your talk by presenting you with this gift.

**Selena Deckelmann** [45:36]: Oh, thank you. Thanks.

**Host** [45:37]: Thank you. [clapping] Uh, ten-minute break and then a talk from Robert Mebus.

