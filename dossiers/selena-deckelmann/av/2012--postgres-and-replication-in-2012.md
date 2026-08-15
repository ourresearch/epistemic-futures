---
title: "Postgres and Replication in 2012"
person: selena-deckelmann
section: by
type: talk-transcript
year: 2012
venue: "linux.conf.au 2012"
source_url: https://www.youtube.com/watch?v=Pdgzy7KoGWU
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 19
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Postgres and Replication in 2012

*Speakers (inferred):* speaker_0=Selena Deckelmann, speaker_1=Audience, speaker_2=Host

## Transcript
**Selena Deckelmann** [00:07]: All right, is this thing on? It's on. Yay. All right. Hi. Uh, I'm back. [laughs] Uh, first of all, I'm probably gonna say Postgres instead of PostgreSQL, and there's a highly scientific study that was done that it results in a thirty-two percent performance improvement, so you should say Postgres too. Just FYI. [laughs] Um, so a lot of what I tend to talk about-- So my involvement in the Postgres community is I, um, uh, do a lot of marketing actually for Postgres. Postgres is not a company. Um, we are a community of people, a collective of individuals, um, spread out all over the world, and there is not a single company that, that supports our development, but a lot of them. And we think right now that Postgres' role in the world is to disrupt the rest of the commercial database industry. Um, and we think those disruptive forces are licensing enterprise web development, um, and the proprietary DBA career path, um, which I'm so glad there's someone from Oracle here today. Um, [laughs] uh, and some of the licensing issues that we're seeing right now, um, and there's been quite a large uptick in Postgres, uh, adoption, which today having half of the room raise their hand saying that they were using Postgres was kind of amazing, 'cause typically, i- you know, I've been going to conferences, um, open source conferences for the last, uh, about seven years, and it's-- I've never seen so many hands raised, so it's really exciting for me. Um, but what we're finding is, uh, commercial software developers that are creating closed source software are finding Postgres to be, uh, an appropriate and useful drop-in replacement for something else that they're using. Um, that goes for something like, uh, Oracle. It goes for something like, um, DB2. Like, people are really pursuing this, um, because they don't have to pay the licensing costs. Um, we're seeing people adopt it kind of as a skunkworks data warehousing tool that the da- DBAs in companies can just, like, pull in and do whatever they want with, 'cause they didn't have to pay anything for it. Um, and also we're seeing quite a large upsurge in the people who are taking Postgres itself because it is BSD licensed, adopting it and then, you know, selling it as a product, uh, which is kind of exciting. A colleague of mine gave a talk about all of the different forks of PostgreSQL that are out there, and, um, there's a lot, uh, more than forty. So, um, we're also seeing a lot of enterprise-y web development for in-house stuff. Like I was saying, Postgres, um, has so many extensions, um, and we really encourage that as part of the use of the database. Um, we are the database of choice for Django, which again has resulted in a lot of new users for us, which is great. Um, and we've found also that Oracle did a great job of marketing itself to, uh, things like PHP developers, um, and then those developers feel less scared when they encounter Postgres in the end. And it just cracked me up, um, the other day I was looking at Oracle's website, you know, and some of their marketing for open source developers, uh, and they really were, like, really pushing the PHP, uh, more so than Ruby or Python, which I thought was just really interesting. Um, the other thing that we're seeing is that companies are not able to hire Postgres DBAs fast enough. It's really hard to hire anybody right now, but in particular, people are having a lot of trouble. Um, and what they're doing instead is hiring Oracle DBAs and retraining them. Uh, and we don't really have a great, uh, way to train people in Postgres itself. We don't have a certification program, so typically it's like taking Oracle DBA, sitting them in front of a terminal with a manual and letting them go. Um, but we're, we're seeing this more and more because companies just can't hire fast enough and find them. Um, and what the Oracle DBAs are saying to us is that we do a few things better, which is really encouraging. Um, and so we're seeing people join our community from the Oracle side, and we're learning things from them. Um, and the other thing is that for the last five years, we've had a major release with an incredible amount of functionality every single year. Um, there are people, I'm not recommending that you do this, but there are people that just take our, uh, current, uh, Git repo and just compile straight from head and use that in production, um, because we have such a reputation for fixing bugs and being incredibly stable. Um, and I don't know, has anybody here ever reported a Postgres bug? And has it been fixed? How long did it take?

**Audience** [04:58]: Pretty fast. A few hours.

**Selena Deckelmann** [04:59]: [laughs] Yeah. I didn't plant him, really. Um, so we have these, like, couple people in our community that, uh, have really devoted their lives to addressing the bugs in the, in the database, and they-- typical turnaround is something like forty-eight hours. So anyway, I'm gonna try to do a live demo. This is gonna be really awesome. Uh, sorry, I need my other hand.

**Audience** [05:32]: You can kill the lights.

**Selena Deckelmann** [05:34]: Kill the-- Oh, yeah, yeah. You can't see that very well. Hold on. Okay. So basically, what I'm gonna show you is how our binary replication is set up. Um, this is something that's been incredibly difficult, uh, in Postgres for a long time, and I don't-- Have any of you here ever set it up? Got a couple here. Have any of you ever tried and failed? [chuckles] There's a few. Yeah. Um, sorry to out you as, like, failed. But anyway, um, uh, it is difficult. Uh, it, uh, it was difficult, um, and things have improved dramatically. I'm actually compiling a version of... This is a current snapshot of our development tree. Um, so this is what's gonna be available in nine two, and that release will probably happen, uh, somewhere around July, August timeframe. But I'm guessing that there will be, um, uh, an alpha or a beta just within the next month or so. So, um, you could download a binary, uh, relatively soon and run this yourself. Um, but, you know, the basics of it are you create a master database. Um, I create a WAL storage directory. Um, you update your HBA, host-based authentication is what that stands for. It's kind of old school, but you set up replication user access, um, and then you update your postgresql.conf with a few different settings. Um, this is fairly well documented in the wiki, but I also pushed this repo into GitHub so you could download this and run this yourself on your laptop or something if you wanted. Um, you start up the Postgres master, 'cause like I said, we still haven't kind of fixed that yet. There's some issues with not starting the database and then trying to replicate immediately. Um, and then we have this new tool called pgbasebackup a friend of mine wrote, and it's awesome. It solves so many of the problems with creating, uh, binary backups with Postgres. It does everything. You notice there aren't very many command line switches here. I'm giving it a user, but I really don't have to, and it kinda just does everything correctly. Uh, almost everybody that I know that has worked with Postgres has written their own basebackup scripts. Um, and then down below, we have a few settings for setting up the hot standby. You turn it on, um, and then here's a recovery.conf, um, that instructs the database on how it's going to replay the binary, uh, replication, uh, packets as they're coming across. And here's the connection info locally. Um, yep, some more settings, blah, blah, blah. You start the replication. Um, and then the other, the other thing that I wanted to show you today is that we actually have cascaded slave binary replication, um, in nine dot two. Uh, and, uh, MySQL has had these types of features for a long time. [laughs] And we finally have it. Um, and it's really cool. It's awesome. You could do it before with, uh, trigger-based replication, but again, this is, this is built into core. Uh, so anyway, so blah, blah, blah, I set that up, et cetera, et cetera, and then I'm all done. So now this is really gonna work, I promise. So it's doing the init, starting the server. Now I'm making the base backup. I created a database just to prove that I could do it. Um, and then there's the output from PS showing that I've got all of these individual Postgres instances running. Um, and then have a little, uh, let's see. So then if you log into psql, um, and then I think I maybe have... Oh, yeah. You can see there my replication is going, which is pretty exciting. Um, and here I am just replicating from a master to one slave, and then on the slave, I'm replicating from that slave to two cascaded slaves. So there's that guy. Oops, sorry. Doing this with one hand is tricky. And if I go to the slave, you can see I've got two cascaded slaves, and my demo worked. Ah, awesome. Um, the other thing is that we-- This is now, um, for those of you who are familiar with previous incarnations of Postgres replication, you used to have to do WAL shipping, which was 16 megabyte files, um, that you would have to copy from system to system and then replay them. Now we do streaming replication, so essentially about when, um, a transaction commits, it can be then copied over to the slave. Um, we also do synchronous replication, so there's, uh, you know, it copies to the slave, and then it does a, "Hey, master, I got a copy of that data. It's good and saved." Um, and that's pretty much automatic. The only change that you have to make to the configuration is to give a name to the synchronous replication target, and then tell the slave what the name is. Um, that's the only change to the configuration. So it's very simple to set up. Uh, and what's really awesome about it too is that it has built-in things for detecting when things get out of sync. Um, and so if you have multiple slaves connected to a single master, it'll detect that something's out of sync and then promote someone else to be, um, in, uh, synchronous after that. Uh, so there's a lot of really neat features, um, for high availability with Postgres, which is the point of this talk, um, that are, that, uh, are available now. Um, and there are certain vendors that are, uh, aggressively pursuing implementing this now, like Heroku. I don't work for them or anything, but they, they, um, they've done a lot of work to make, uh, replication be essentially transparent, um, using our binary replication tools. And there are other companies that are pursuing, uh, making tools to support this so that you could even have your own kind of private clustered, uh, Postgres instances as, as commercial products. But our tools, the tools are there now. Um, uh, all of the open source tools are there now for you to set something like this up yourself. Um, so I have a little few more slides. How am I doing on time? Yeah, go ahead.

**Audience** [12:19]: Question.

**Selena Deckelmann** [12:19]: Question, yeah.

**Audience** [12:19]: Since you have the mic, can you just repeat the question?

**Selena Deckelmann** [12:21]: Yeah.

**Audience** [12:21]: Okay. All right, cool. Um, so, uh, o- one thing, um, when we do synchronous replication-

**Selena Deckelmann** [12:28]: Yeah

**Audience** [12:28]: ... is it always all or nothing? As in, if I have, uh, three slaves, can I say, uh, consider this transaction completed if it's been written to two, but I don't care which ones?

**Selena Deckelmann** [12:40]: Um-

**Audience** [12:41]: And then do the third one asynchronously?

**Selena Deckelmann** [12:43]: I'd have to look and see what current state of head is. I know that that is a feature that Simon Riggs wanted-

**Audience** [12:48]: Okay

**Selena Deckelmann** [12:48]: ... to support. Um, I'm not positive at what stage it is.

**Audience** [12:52]: Okay. And second question, since this... You said this is basically binary streaming replication, not statement-based.

**Selena Deckelmann** [12:57]: That's correct.

**Audience** [12:58]: So when does a sync happen? Does it happen on an actual insert and update, or does it happen on the commit? What's the consistency guarantee there?

**Selena Deckelmann** [13:07]: Um, so the consistency guarantee is about the, uh, committed transaction. So, um, once on the master you commit a change, um, if it's sync rep, then it is not considered committed in your cluster until it reaches the slave and then is covered back. The, the commit, yeah, at that point.

**Audience** [13:33]: Okay, so if I have, if I have one synchronously replicated slave-

**Selena Deckelmann** [13:35]: Yes

**Audience** [13:36]: ... I issue a commit. For whatever reason, that commit fails on the slave.

**Selena Deckelmann** [13:40]: Yes.

**Audience** [13:40]: Then that transaction is considered failed.

**Selena Deckelmann** [13:42]: Exactly.

**Audience** [13:42]: And if the slave croaks at that very moment, as in just stops responding, uh, then again, that transaction is considered failed. Is that correct?

**Selena Deckelmann** [13:50]: That's correct.

**Audience** [13:51]: Awesome.

**Selena Deckelmann** [13:52]: Yep.

**Audience** [13:52]: Thanks.

**Host** [13:55]: One more sync question.

**Selena Deckelmann** [13:56]: Yeah.

**Host** [13:56]: Is the sync on received on the slave or on disk on the slave?

**Selena Deckelmann** [14:00]: Uh, the question was, "Is the sync, uh, on received or is it on, uh, to disk?" That is configurable. Yeah, and there's actually a lot of nuance in there that I'd happy to talk about later. [laughs] Um, 'cause one of the, one of the more surprising behaviors in previous, in 9.0 version of Postgres was that, um, committed on the slave did not mean visible. And so if you had an application that was relying on commit me- being visible, you had to add an extra configuration to make that happen. Uh, but I believe at this point the default has changed, so it's less surprising to users. [laughs] I like the policy of least surprise. Look, I didn't have to use my screenshots. Yay. [laughs] Okay, so replication is hard. Sharding's hard. Things are slow. Um, [laughs] I think that the streaming cascaded replication, which is new in 9.2, is really great. Um, and it's, it's solving a lot of this issue of, of replication for Postgres. Sharding's still really hard. Um, you have to often change the way that application developers think, uh, in order to get this to work properly. Um, and then some other things that we're working on, we now have index-only scans in Postgres. Again, something that other databases have had for a long time, and we finally have implemented to our satisfaction. And what this basically means is that if you create indexes on tables in Postgres, now you can access that data in memory. Um, there's some caveats with that, but in, in certain cases, I mean, it's, it's so clearly a huge performance win. It's, um, people are very excited about this. Um, the other thing about our community is that we're really starting to address operations and performance concerns that, um, DBAs have had for a really long time. Uh, sorry this is in all caps, but, um, uh, you can now do certain things like, like this one. You're altering the type of an index column and maybe you don't wanna re-index right that second. Um, so you can del- delay or defer changes, uh, to important, uh, pieces of data in the database, uh, in a way that really helps people maintain, uh, reasonable performance. Um, you can also implement additional checks on, on data, um, either rules or, or triggers and say that, uh, existing data in an index could be maybe not valid for that check, but that doesn't mean that it's gonna recompute an index. Sorry, that was a little out there. But anyway, the bottom line is, is that that's really great for DBAs. Um, and there's a, a, a great deal of focus right now on these types of issues. So if you're a person that kinda waved around and like s- sent an email to hackers in the past and said, "Uh, like, why don't you fix this, like, really annoying problem for me as a DBA?" Now would be a really good time to bring up those issues again. Um, the other thing is pg_basebackup. It's, uh, it's creating a, a common starting point, uh, for people who are doing backups for Postgres. Um, I think I already said this in the other one. Um, one, one goal, uh, for me is to try to make Postgres as easy to install as SQLite. Big goal, [laughs] but there are people that are working on this right now, improving, improving initdb. Um, and what's happening right now, I already mentioned Heroku. They're doing 400 million write transactions per day. This is probably the largest, uh, you know, cluster of Postgres out there in the world. Um, VMware is creating really great software, um, for managing lots of instances of Postgres. There are lots of other vendors that are working on things right now. Um, and there's just, in general, a lot more interest in the hosting world in supporting Postgres, uh, which has, uh, not necessarily been true five years ago. Uh, like I said, some of the things that we're working on, UI overhaul. Um, there's a lot of work to be done there. Uh, cascaded failover. And finally, um, there's, there's been work on using, uh, changing synchronous rep into a multi-master system, um, that can have multiple cascaded slaves. So, um, that's kind of far off in the future. I'd say, you know, two or three years really before we have a significant amount of code to support that. But that's, that's on the roadmap for the people who are working on this code right now, and it's really exciting. So, thank you.

**Host** [18:18]: [audience applauding] Um, so we're at, um, um, another break time. Um, but if anybody has any questions, um, we can do that. Um, after the break, uh, Monty, Monty Taylor is gonna be talking about Swift 101, um, and Ian is going to be talking about something.

**Audience** [18:45]: Web infrastructure scaling.

**Host** [18:46]: Web infrastructure scaling and keeping it online cheaply. And right after that, there's, um, uh, two lightning talks. If anybody else wants to give one, um, please do. There's little notes down here. Um, so-

