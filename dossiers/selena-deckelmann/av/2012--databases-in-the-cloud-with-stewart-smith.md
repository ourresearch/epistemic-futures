---
title: "Databases in the Cloud (with Stewart Smith)"
person: selena-deckelmann
section: by
type: talk-transcript
year: 2012
venue: "linux.conf.au 2012"
source_url: https://www.youtube.com/watch?v=UFTp0zA4Mx8
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 20
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Databases in the Cloud (with Stewart Smith)

*Speakers (inferred):* speaker_0=Stewart Smith, speaker_1=Selena Deckelmann, speaker_2=Audience, speaker_3=Audience

## Transcript
**Stewart Smith** [00:00]: All right. Hi, this is Stewart.

**Selena Deckelmann** [00:02]: And this is Selena.

**Stewart Smith** [00:04]: Welcome. We're gonna talk about databases in the cloud.

**Selena Deckelmann** [00:08]: Why? Because all the other shapes on PowerPoint are already used for things like computers and network connections, so the cloud was the only object left, so therefore, new technology got called the cloud.

**Stewart Smith** [00:18]: [laughs]

**Selena Deckelmann** [00:19]: Um, and, and databases in the cloud are, of course, this wonderful magic solution that without explaining any of the technology behind it or coming up with any real solutions, will instantly make everything scale and be perfect.

**Stewart Smith** [00:28]: Solves all of your problems.

**Selena Deckelmann** [00:29]: All of your problems, so don't worry. All you have to do is when someone asks how you're gonna solve for scaling, you just say, "We're gonna put the database in the cloud," and then you can go home 'cause it's already done.

**Stewart Smith** [00:38]: And now our talk is done.

**Selena Deckelmann** [00:40]: Yeah, thanks. That's all you have to do. Yep.

**Stewart Smith** [00:44]: [laughs]

**Audience** [00:45]: [clapping]

**Selena Deckelmann** [00:46]: So since, uh, we're not in the world of Harry Potter, and we can't just tap a wand and make that happen, uh, we can now discuss the depressing reality of what is referred to as database in the cloud. So once you've gone off, like, the absolute hyper-speed induced, like, marketing drugs, um, you can then come back to reality and, and, and here's the problem. So thought we'd, we'd start first about, like, in the beginning. So if you think about, typically about what happens when you go and use, like, a database as a service or some, like, shared hosting thing, right? So everyone pays, you know, two dollars a month and gets some account and some machine with, you know, a MySQL or a Postgres instance on there, well, part of it or whatever, and then what happens there. So there's a bunch of problems even in that, that simple scenario if you even think of, "I'm gonna just whack it in the cloud 'cause I really don't wanna be a DBA admin," and really cloud is just a new word for, you know, shared hosting in a lot of situations, especially when it's a small app. Um, so the MySQL way has typically been that someone either writes their own little magic foo or gets somebody else's magic foo to basically say, "Every user in the cloud now gets, like, one database," and if you wanted two apps, then you better hope their table names don't conflict 'cause otherwise you're screwed. Um. [laughs] And of course you get one user account, and it has privileges to all that database. If you actually wanna do things, uh, interesting, like maybe have a read-only user and a read-write user for different tables and, like, be able to have some privilege separation, you don't, which is why every single web app in the entire world written towards MySQL has one user that it connects to that has rights to absolutely everything, uh, including drop table, and we're all sad, and little Bobby Tables doesn't get his school results. So we have problems there. We also have other issues of, like, of course in these setups generally you don't get replication because that's hard, and it turns out MySQL's replication system, of course, then you could be the one user on the machine that decides to run a query across a gigabyte of data that's very, very excessive and then locks everyone else's replication for the next four hours. Um, so you know, that has a few problems there in a, in a shared environment. So basically, it works quite well if you're writing very small apps. Uh, one of them has your user on the one machine. Uh, you don't really care too much about performance, of course, because in the time between your app last being accessed and now being accessed, probably all of your pages have dropped out of the buffer pool and out of cache, so it has to come up from disk. But you know, it kind of works for everyone's personal WordPress blog, uh, so it's done that way. Uh, but of course, as soon as someone gets beyond a limit, you've got problems. You have to go to something else, and there's a bunch of architectural problems sort of in the server to make it-- that doesn't make it any easier. And there's also a bunch of problems in the fact that it just works for so many people on a small scale that it's kind of prevalent in this odd kind of way and causes some really bad design decisions 'cause there isn't a good way to have, you know, different users and different, uh, databases in there, and there's always some script that prepends your username to the schema name and other horrible things going on, uh, that it's not necessarily very good. No one ever runs good disk IO behind the, uh, behind it anyway, but it works for a lot of situations, and this can be sort of in the cloud for small things. And for a lot of apps really, if you don't get that heavy use, it's fine, and everyone tends to do this inside an organization anyway. Why deploy seven machines you have to do admin on and DBA on when you could just have one a-and take a backup? How is the Postgres world?

**Stewart Smith** [04:08]: Well, if we're talking about in the beginning, um, if you called up a shared hosting provider and said, "Hey, I'd like to use Postgres," they'd be like, "What? Really? No."

**Selena Deckelmann** [04:17]: [laughs]

**Stewart Smith** [04:19]: So that continues to be a problem. We now do have several shared hosting providers, um, and even, like, Postgres-as-a-service being offered by a few companies, but it's relatively new. Um, so we are just young in terms of being able to provide that type of service operationally, and there hasn't been a great deal of work in our community on making that easy. So things like just doing an initdb used to be incredibly slow. We've made some fixes for that now, so it's a bit faster. But for example, you can't do an initdb copy, um, that particular database, uh, instance without bringing it up and then expect replication to work. It's kind of a problem. [laughs]

**Selena Deckelmann** [05:03]: [laughs]

**Stewart Smith** [05:03]: Um, it was just, uh, for so long we were the vertical scaling database, right? Like, why would you want to have lots of little Postgres instances, full stop? You know, like, it just really wasn't a priority for our project. So that is changing now because of companies like Heroku that do now have, um, you know, tens of thousands of instances running all the time. And they're becoming very interested in helping us move forward with some of our user interface problems that we have like that and just addressing these system administration issues. And really a lot of the same issues, uh, that Stewart just brought up about user management, you know, you set up a database, and then all of a sudden, you know, you have these unique users across every single database that's in that particular Postgres instance. That's kind of an issue. Um, we have incredible role management in Postgres, but it's, like, Byzantine and awful to administrate, and so you still end up with these applications that people write [clears throat] where it's, they're just using a single user, um, instead of actually using the role infrastructure that's there. So we, we have a lot of work to do on the user interface side to make that easier. Um, and then until very recently, most of our replication, uh, r-real replication systems that people were using in production were third party. So you'd use something like Slony. Um, there were some other things like Piccoro and there's Lontiste, but they're third party. And so there were lots of companies that just did not trust them because they were not distributed as part of core Postgres. And so then we got the reputation for just not really having proper replication. Um, now we have that, uh, and it's very exciting, but, um, you know, we're still, we're still making incremental progress every year. And, uh, it's relatively new and it's a lot of code. Um, and it's working really well, right? But, you know, it's still kind of... People are cautious. You know, we're not really sure that it's, uh, it's ready for the type of loads in the cloud that MySQL has been supporting for a long time.

**Selena Deckelmann** [07:03]: Well, half of it's by accident, and the other problem, of course, with, uh, the whole auth infrastructure is like it's all byzantine because every part of SQL to do with users and permissions is designed for someone sitting in front of a VT100 terminal writing in SQL by hand, uh-

**Stewart Smith** [07:17]: [laughs]

**Selena Deckelmann** [07:17]: ... and not at all maps to a web app.

**Stewart Smith** [07:19]: Right.

**Selena Deckelmann** [07:19]: So, like, it's complete disconnect, uh, which is, you know, absolutely ideal for the modern world, and we've wonderfully, as database developers, stuck our head in the sand and not done anything about that.

**Stewart Smith** [07:28]: [laughs]

**Selena Deckelmann** [07:28]: So, you know, you're welcome for soft-

**Audience** [07:30]: [laughs]

**Selena Deckelmann** [07:30]: -for us solving that problem.

**Stewart Smith** [07:31]: Thanks.

**Selena Deckelmann** [07:31]: Uh, and of course, this is a problem that's been in the beginning, so we've had a fair bit of warning now. You know, shared hosting's been around for a while, uh, and, you know, still not fixed. Thanks. [laughs]

**Stewart Smith** [07:42]: All right, next point.

**Selena Deckelmann** [07:43]: Yeah, so I want to say the next point was, like, if you think of, like, sort of cloud V... I don't know. It's like, oh, we can dynamically do things. It's like, here's a pre-built virtual machine image that has a database server installed on it, and precisely two people use those, and they were both the ones that created the images in the first place that fit their hardware and their specific setup. So that was, like, you know, completely a waste of time, and no one ever did it. Turned out apt get install MySQL, apt get install Postgres was really quite easy on, on your own machine, so it wasn't really a thing. Um. [laughs]

**Stewart Smith** [08:09]: Yeah, agreed.

**Selena Deckelmann** [08:10]: Yeah. And then it comes onto the other issue, which comes onto, you know, the sort of second sort of thing, which is a whole much database as a service. You start to people having actually use a database inside a virtual machine, uh, which has its own set of problems, 'cause it turns out, uh, how do virtualization performance and databases go together?

**Audience** [08:29]: Badly.

**Stewart Smith** [08:29]: [laughs]

**Selena Deckelmann** [08:31]: [laughs]

**Audience** [08:32]: It's confusing to most people.

**Stewart Smith** [08:32]: Correct.

**Selena Deckelmann** [08:34]: [laughs] Yeah, it's great if you're not used to performance in the first place.

**Stewart Smith** [08:38]: [laughs]

**Audience** [08:39]: It's as well as databases and h- uh, migrating file systems.

**Selena Deckelmann** [08:43]: Yeah, it's almost as well as pouring honey on your hard disk.

**Stewart Smith** [08:47]: [laughs]

**Selena Deckelmann** [08:48]: I've never done it. Probably works really well, but I wouldn't recommend it. Um, yeah, I mean, virtualization has a couple of issues there, right? I mean, one, you've now somehow, amazingly enough, running more than one VM on the machine does not magically give your I/O subsystem any more IOPS. Yeah.

**Stewart Smith** [09:04]: Sorry to be controversial.

**Selena Deckelmann** [09:05]: Yeah. [laughs]

**Audience** [09:06]: [laughs]

**Selena Deckelmann** [09:06]: Yeah, magic doesn't happen. Uh, [laughs] and, and you end up this wonderful situation. So instead of being able to do that, you know, like three hundred syncs per second or something on this one database instance, oh, let's just put ten of them there, right? Everyone gets thirty.

**Stewart Smith** [09:19]: [laughs]

**Selena Deckelmann** [09:19]: Which is, like, less. Uh, and it turns out that the big overhead tends to be actually when you want to write something to disk if you care about disk durability. But what turns out is, like, a bunch of virtualization people found out it's really fun. If you don't pass the flush commands down to the-

**Stewart Smith** [09:35]: Oh my God, it's so much faster

**Selena Deckelmann** [09:36]: ... from the virtualization system, it runs so much faster.

**Stewart Smith** [09:37]: So much better.

**Selena Deckelmann** [09:39]: Until your database as a service customers come back and go, "Why does none of my stuff work anymore? It's all corrupt. Why? How could this possibly happen?"

**Stewart Smith** [09:45]: So, yeah, so once again, we're back into this situation where you cannot trust the vendor at all.

**Selena Deckelmann** [09:51]: Yeah. And I mean, you know, what happens if it doesn't work and you end up that way? What can you do? You're now buying database as a service, so you can't do anything about it. You can just sort of ask them nicely to please not corrupt your data anymore, uh, or hope they use, you know, a virtualization system that actually does respect that and hope that, you know, all the files and code in the middle there is the versions that actually work. Uh, and you, you may or may ha- not have access to the underlying, you know, OS image there, so it's even more fun so that you can't fix it yourself.

**Stewart Smith** [10:19]: Question?

**Audience** [10:20]: Sure. Curious, I've been fighting a bit of a losing battle against virtualization. Um, um, you know, my argument's very simple. Hey, if you own the hardware, why are you wasting all the context switches and going at your caches swapping in metal all the time? If the, the counterargument is, is manageability, right? Have you been a-able to see it pair off or come at par as only one VM on physical hardware? Does the, does the problem away get settled or it, it's a non-starter if you're looking to VM physical hardware? I'd love for you to say physical, 'cause then I'd feel better about myself. But if, if one VM on a physical box is okay, well, then, then w-would

**Selena Deckelmann** [10:55]: Yeah. I, I'm gonna say physical just because that gives you one less problem and, you know, once you start running with too many layers, database is, uh, fragile enough as it is. Um, and like, you know, if you've got ninety-nine problems, you may as well have ninety-nine, not a hundred, uh, [laughs] with, with the extra layer of virtualization stuff there. And I think Avi's done more benchmarks on various databases that he totally cannot say numbers publicly with. Uh, but [laughs]

**Audience** [11:20]: I'm allowed to say our numbers.

**Selena Deckelmann** [11:22]: Oh, your numbers. Yeah, your, so your numbers-

**Stewart Smith** [11:24]: Oh, you, you, yeah, you can talk about us.

**Selena Deckelmann** [11:25]: [laughs]

**Audience** [11:26]: I can talk about Oracle and MySQL virtualization.

**Stewart Smith** [11:30]: Mm.

**Selena Deckelmann** [11:30]: Yeah.

**Audience** [11:30]: I've never done numbers with virtual machines.

**Selena Deckelmann** [11:32]: Yeah.

**Stewart Smith** [11:33]: Oh.

**Selena Deckelmann** [11:33]: Yeah, I... It will be less bad, 'cause the main point is that when you're restricted on IOPS, you're still gonna have your base IOPS. So it'll be less bad. Um-

**Audience** [11:41]: Ability is not the only impact though. Utilization is the other one. It's the, I mean, it's the idea of you, you bought this magnificently expensive piece of hardware, but your database is only busy for twenty minutes a day when it's doing its batch process at five o'clock. Why can't I be using all that hardware during the day for the other things that need that kind of speed? And it's, it's, you know, instead of having a database server that's ten percent utilized most of the time and peaks at a hundred percent-

**speaker_4** [12:12]: I can run all my servers at 60, 70% CPU utilization against, against

**Selena Deckelmann** [12:16]: Yeah. I mean, it depends on work, workload. Like, that can work very well when you have batch operations.

**speaker_4** [12:21]: Yeah.

**Selena Deckelmann** [12:21]: Um, unfortunately, most websites don't tend to have a giant batch operation. It tends to be more of a, a static load, and then a peak, and a sustained load, and, and down, depending on, you know, if they've acknowledged the world outside the United States yet or not. Um, and so you end up with this kind of interesting way of we tend to see, you know, people ramp up and then use at least one and more. Uh, so you end up with this kind of interesting scenario there, even just at the base layers.

**Stewart Smith** [12:45]: And there are some companies that are doing interesting work with that. There's this company called Gilt that has created, um, a great deal of infrastructure around trying to manage that load. But I mean, it involves a level of monitoring and knowledge of your systems that honestly, like, most IT organizations don't have that sophisticated level of monitoring, and then they also don't have the staff that can write the tools that you need to do that. Because the tools out there in the cloud for doing this, they don't, they don't really work.

**Selena Deckelmann** [13:15]: Mm. Yeah, I mean, I mean-

**Stewart Smith** [13:16]: In my experience.

**Selena Deckelmann** [13:17]: Yeah, I mean, you have, um, you know, a whole bunch of issues at various points where you're simply like, well, if you're buying database as a service, then you get this database server. Does that mean you can even set half the options?

**speaker_4** [13:27]: Yeah.

**Selena Deckelmann** [13:27]: And, and then you have the issue of like, you know, especially if you have public pluggable, like, replication systems, does that mean you get to choose that? Uh, you know, as MySQL, does that mean you get to choose, you know, how your storage engine is configured, like how big the log files are or, a- and, uh, how much memory is used for a buffer pool, which can be distinctly different, and can you limit, you know, the data dictionary cache, and you have all memory management issues when you hit large enough scale.

**Stewart Smith** [13:50]: Right. So the, the bigger issue for me about people trying to put large systems in the cloud is that, that it just doesn't work with the large systems, right? Like, for the smaller systems, for people who are just starting out, for prototyping things, um, for, uh, a website that you know is never going to, you know, be that large, like I, I think that it totally can work, right? But when you get to the point where you really do need that performance and you need to migrate off, I mean, that, that's, that's the question, is the first question is, can you? You know, is it possible for you to even get your data out in a reasonable way and move to something that can provide the performance that you need? And so, you know, if you have any inkling that you are going to go there, you have to, from the beginning, plan and know that it's possible for you to get out of the system you bought into.

**Selena Deckelmann** [14:36]: 'Cause remember, at a point, a SQL dump is no longer a viable way to restore.

**Stewart Smith** [14:40]: [laughs]

**Selena Deckelmann** [14:40]: It's like, "Oh, I can just do a SQL dump and connect to the socket." It's like, great, this is gonna take me two days to restore from somewhere.

**Stewart Smith** [14:45]: [laughs]

**speaker_4** [14:46]: So how do you move databases?

**Selena Deckelmann** [14:47]: How do you move databases?

**Stewart Smith** [14:49]: Very carefully.

**speaker_4** [14:53]: You know where you can buy Golden Gate?

**Selena Deckelmann** [14:54]: [laughs]

**Stewart Smith** [14:54]: [laughs]

**Selena Deckelmann** [14:55]: I'll be working for Oracle, can totally recommend Oracle Golden Gate. Um. [laughs]

**Stewart Smith** [14:59]: Perfect.

**Selena Deckelmann** [15:00]: Yeah. I mean, it depends on the system, right? So you can do, like, online binary backups, uh, for MySQL using, like, uh, either the Oracle commercial product or the Percona open source one. Full disclaimer, I work for Percona. Um, or you, you know, do it in a variety of other ways, worst case being SQL dump and sharding, or just take some downtime, uh, and the like. But we should probably, since we're running out of time, also talk about the last point here, which is, like, multi-tenancy built into the database to alleviate some of the management pain of having, uh, multiple sort of end users having, sharing one physical database server and not running into half of these problems, or at least giving the problems to someone else. Um, I've done a whole bunch of work, which I'm talking about tomorrow, uh, to make Drizzle do sort of true multi-tenancy in the database. So instead, we inherited from MySQL the whole thing of, like, you have schemas or databases in MySQL talk, and tables inside them, and sort of one global set of auth. Uh, so in Drizzle now, I've got another layer on top of that, which is catalog, which is basically like then each individual sort of, you know, cloud customer there can get their own space through their own authentication tables, their own database names, their own schemas, their own usernames, and then you can do sort of resource limits per catalog. So you can say each user gets, you know, ten gigabytes of buffer pool storage, and they all go into that particular point, and they could each get their own replication screen. Uh, and so you could replicate them differently depending on the users if they turn that on or off, which is kind of neat. And then Selena's magic word's gonna be, "Oh, we've had that for years."

**Stewart Smith** [16:24]: [laughs]

**Selena Deckelmann** [16:24]: So. [laughs]

**Stewart Smith** [16:25]: Aw, I didn't get to say it.

**Selena Deckelmann** [16:27]: [laughs]

**Stewart Smith** [16:28]: [laughs]

**Selena Deckelmann** [16:29]: So say it. Like, why, yeah, come on.

**Stewart Smith** [16:31]: We've had it for years.

**Selena Deckelmann** [16:32]: Yeah.

**Stewart Smith** [16:33]: Uh, but I... Ooh, sorry. Um, the, the area that Postgres is really focusing on right now is, uh, binary replication, and I'm gonna actually just right after this, uh, show you how that works, uh, and where we're kind of going with the future of our replication. And, um, there's a lot of things actually that Drizzle does that we are aiming for. Um, lots of cool ideas around being able to replicate individual, uh, databases, potentially individual tables and rows, uh, because the binary stream is filterable, which is, would be really exciting. Um, and then there's a lot of work because of companies, uh, that are creating these Postgres as a service services. Uh, they're really interested in, in making the UI better. Uh, psql is a super powerful tool, but it's, like, not very friendly. Um, and we don't have a lot of other tools out there for just managing, uh, Postgres itself that are very good. So-

**Selena Deckelmann** [17:28]: Yeah. We can basically summarize the last point I wanted to say, which is, like, auto magic replication, sharding, and magic that's instantly gonna make all your database and application scales. Yeah, all of those people claiming that are lying.

**Stewart Smith** [17:37]: Yeah.

**Selena Deckelmann** [17:39]: Right? It's pretty obvious. You can't magically make source different. They can't violate the CAP theorem, or Moore's law, or anything that, that way. There is something in there that you're gonna hit, so you always end up having to think as an application developer about, "Okay, so how can I partition data?" Or, "How do I actually build a high availability cluster this way and for these kind of queries?" And, "Do I have separate databases for archive stuff?" You're end up gonna have to think for that. It turns out no one's come up with the one magic algorithm to solve all your problems.

**Stewart Smith** [18:05]: Yeah, it really is the app-

**Selena Deckelmann** [18:05]: And anyone who's currently claiming it doesn't beat the your database technology is at least 10 years old to make it stable test.

**Stewart Smith** [18:11]: And also it really is the application developer's fault-

**Selena Deckelmann** [18:14]: Yeah

**Stewart Smith** [18:14]: ... for not writing

**Selena Deckelmann** [18:15]: Scalable code to begin with

**Stewart Smith** [18:16]: Yeah, right

**Selena Deckelmann** [18:17]: You know, bad queries. I mean, really, our databases are perfect.

**Stewart Smith** [18:20]: They're really great.

**Selena Deckelmann** [18:21]: [laughs]

**Stewart Smith** [18:23]: [laughs] All right.

**Selena Deckelmann** [18:25]: So yeah, that's not a very happy situation of the world of databases in the cloud, and basically everything's not ideal, but the marketing's there.

**speaker_4** [18:34]: [laughs]

**Selena Deckelmann** [18:34]: So, you know, we're all saved that way. But, uh, [laughs] at least if small, it's not too much problems. It'll kind of work.

**speaker_4** [18:40]: You're saying it's raining, effectively.

**Selena Deckelmann** [18:41]: Yeah, it's raining. It's not quite, you know, a beautiful cloud in the sky. It's, it is raining a bit and possible hail.

**speaker_4** [18:50]: What makes cloud.oracle.com special?

**Selena Deckelmann** [18:51]: 'Cause it's magic and solves everything. [laughs]

**speaker_4** [18:55]: The interesting thing about cloud.oracle.com is it's not virtual databases. It's multi-tenancy on hardware.

**Selena Deckelmann** [19:03]: Yeah.

**speaker_4** [19:03]: So the back end of cloud.oracle.com is Oracle DBs between the X data and selected hardware. So they aren't actually virtual databases. Get your database on hardware using Oracle Cloud tenancy resource management to do what you've serviced and buy up dedication and make the dedication there.

**Stewart Smith** [19:23]: Right. And there are some, uh, Postgres vendors that are offering similar, very similar things.

**Selena Deckelmann** [19:28]: And, and we'll have that for drizzle when I-

**speaker_4** [19:30]: The access-

**Selena Deckelmann** [19:30]: -get the last bits of coding

**speaker_4** [19:32]: ... to the database.

**Stewart Smith** [19:32]: Yeah.

**Selena Deckelmann** [19:32]: Yeah.

**Stewart Smith** [19:33]: Yeah. And you can, you can find, um, vendors. They are, they are somewhat boutique, but you can find them. Um, and they will provide, uh, what, what seems like a pretty excellent level of service. But again, it's not, it's not the same thing. Like a lot of these technology, uh, it's not the same thing that we have been talking about here. A lot of these technologies, they're based on top of AWS. Um, and so you are subject to whatever AWS outage du jour there is.

**Selena Deckelmann** [19:57]: Or if they like or don't like your content.

**Stewart Smith** [19:59]: [laughs] Also that.

**speaker_4** [20:01]: Now I've learned something anyway.

**Selena Deckelmann** [20:03]: [laughs]

**Stewart Smith** [20:03]: Awesome.

**Selena Deckelmann** [20:03]: We should probably stop and let you talk-

**Stewart Smith** [20:04]: I, okay

**Selena Deckelmann** [20:04]: -and offer anyone a cookie.

**speaker_4** [20:10]: [laughs] Absolutely.

**Stewart Smith** [20:13]: [laughs] Thank you.

**Selena Deckelmann** [20:13]: Totally have cookies. Thank you all.

**Stewart Smith** [20:14]: Yeah. Thank you. [audience applauding]

