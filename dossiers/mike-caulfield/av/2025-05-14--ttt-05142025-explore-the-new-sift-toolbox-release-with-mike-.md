---
title: "TTT 05.14.2025: Explore the New SIFT Toolbox Release with Mike Caulfield"
person: mike-caulfield
section: by
type: talk-transcript
year: 2025-05-14
venue: ""
source_url: https://www.youtube.com/watch?v=yVZTHFSoqKA
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 63
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# TTT 05.14.2025: Explore the New SIFT Toolbox Release with Mike Caulfield

*Speakers (inferred):* speaker_0=Host, speaker_1=Debbie Abelock, speaker_2=Chris Sloan, speaker_3=Steph Gamble, speaker_4=Kristina Cantrell, speaker_5=Linda Hoiseth, speaker_6=Fred Haase, speaker_7=Meredith Cranston, speaker_8=Mike Caulfield, speaker_9=David Cole, speaker_10=Suzanne Durisi

## Transcript
**Host** [00:03]: Here it goes. Welcome to Teachers Teaching Teachers. And we, uh, I c- I have a co-host tonight, which I'm so happy about. [laughs] Debbie Abelock is going to, um, handle some of the, uh, introductions here at the beginning. Um, Mike Caulfield is here, um, and others are joining us. Welcome, uh, as we go here. Um, and so we wanna give Mike as much time to present and talk about his, uh, sense-making with Sift Toolbox, um, as possible. Deb- Debbie, do you wanna, um, start-

**Debbie Abelock** [00:39]: Sure

**Host** [00:39]: ... by giving an example of, um-

**Debbie Abelock** [00:41]: Yeah

**Host** [00:42]: ... then invite others? Go for it.

**Debbie Abelock** [00:44]: Sure. So I thought what would be most helpful to Frank, it's be- um, to Mike, sorry. [laughs] I'm looking at-

**Host** [00:50]: Mike, yeah

**Debbie Abelock** [00:51]: ... [laughs] I'm looking at Frank and I was saying Fr- yeah. Um, is to tell him who, who, uh, you know, who we are other than our first name quickly, and then give him some information about the connection that we have, either the touchpoint with him or a touchpoint with AI that we bring to the table-

**Host** [01:16]: Mm

**Debbie Abelock** [01:16]: ... relevant. I thought that would be helpful. So, uh, I'll go first. Um, I'm Debbie Abelock, I live in Northern California, and, uh, my touchpoint is that I, uh, was looking at the Sift Toolbox and wondering how we could teach AI to teach kids how to do the kind of thinking that it's doing, and then to teach kids what, what... when- once you have that kind of information, how do you think with it? So that part interests me about what you've done. Anybody wanna go next or should we just go around the table clockwise? Is that all right?

**Host** [02:06]: Let's, let's do that. Chris.

**Debbie Abelock** [02:07]: All right, Chris, you're next.

**Chris Sloan** [02:09]: Hi. Uh, my name's Chris Sloan. I teach high school, uh, English and photography and media at Judge Memorial in Salt Lake City, Utah. And, um, coincidentally, I had a student today who was, who put together a little podcast asking, uh, some students whether the headlines she generated, uh, and ones she found were, um, fake news or real headlines. And so she actually consulted ChatGPT to come up with some headlines, uh, some fake headlines, and, um, they had a really good time doing that. They had a ball doing that podcast. So, uh, yeah.

**Host** [02:49]: Cool.

**Debbie Abelock** [02:50]: Stephanie?

**Steph Gamble** [02:51]: Hi. I'm Steph Gamble. I'm a upper school librarian at Sidwell Friends School in Washington, DC. Um, so I teach information literacy, um, in all sorts-

**Host** [03:01]: Mm

**Steph Gamble** [03:01]: ... to our students, and definitely, uh, trying to figure out how to incorporate these AI bits, especially as we are a school that's not really doing a whole lot with actively, um, engaging our students on AI so far.

**Debbie Abelock** [03:18]: Katin.

**Host** [03:19]: Kristina, Kristina and Jack.

**Kristina Cantrell** [03:21]: Hi. Uh, I'm Kristina Cantrell from the National Writing Project, and, uh, I'm here in Philadelphia with Jack, my partner. And, um, I guess most recently we used the Sift Toolbox, um, when we were developing some curriculum for a civic journalism, a rural civic journalism project, and making some student-facing modules. And, um, so I was just thinking about sort of how, you know, the different it- just following the different iterations of it over time, so interested to see where things are go- get, have gotten to.

**Debbie Abelock** [03:56]: Linda, I'm wondering if you can unmute yourself and show your face 'cause we can't do it. [laughs]

**Linda Hoiseth** [04:02]: Good morning. [laughs] Hi. Uh, this is L- Linda Hoiseth, and I'm in Dubai, and it's 5:00 in the m-

**Debbie Abelock** [04:09]: [laughs]

**Linda Hoiseth** [04:09]: And I'm getting, and I'm getting ready for school, so I'm gonna not turn my camera on.

**Debbie Abelock** [04:14]: Okay. We forgive you. [laughs]

**Linda Hoiseth** [04:17]: Thank you. Uh, but I, I will listen in, and I'm currently working with, um, physics classes, and they are doing source evaluation as part of their research into trying to identify if a, if a claim about electromagnetic radiation is true or not. And it's just been fascinating to watch them as they, as they dig into authors and sources, and trying to, to find out whether or not they can trust the information that they found. So it's been, it's been a great week.

**Debbie Abelock** [04:45]: Great. Thank you. Good morning. [laughs] Paul, you're morning.

**Linda Hoiseth** [04:50]: Good morning.

**Host** [04:51]: Hi. I'm Paul Allison from New York City Writing Project and, uh, Writing Partners, and, um, I've been, uh, diving in and, uh, going into the code and playing with, uh, the toolbox. So I'm a little overwhelmed and excited about, uh, meeting and hearing Mike's thinking around it.

**Debbie Abelock** [05:13]: And Fred?

**Fred Haase** [05:15]: Uh, my name is Fred Haase. I am an English and journalism teacher in Hopkinton, Massachusetts, which is right outside of Boston. Um, I am here because, uh, mostly, uh, 'cause I, I'm always kinda interested in what Paul is doing. I'm a bit of an AI skeptic, pretty admitted, like pretty outspoken about that, but, um, I've also used a lot of Mike's work in my classes, and I'm actually in the middle of a research project with a bunch of kids right now, and I wasn't as familiar with the toolbox bit, so I'm here to kind of find out more about that.

**Debbie Abelock** [05:54]: Meredith?

**Meredith Cranston** [05:56]: Uh, my name is Meredith Cranston. I am an upper school librarian at the Harker School in San Jose. Uh, we do a lot of information literacy instruction with our students, particularly with lateral reading. Um, I am also an AI skeptic, but my students aren't, so [laughs] I wanna know kind of more productive ways that we can use it to do good things.

**Mike Caulfield** [06:20]: Uh, I'm Mike Caulfield, and I'll talk at length. Um, uh, I was a, a former AI skeptic, and I'm now, um, I don't think I'm a booster, but, uh, I, I think, uh, I think we kind of get to shape the AI we want, and so that's what I'm trying to do, uh, lately is shape AI to be the AI we want.

**Host** [06:41]: You're an AI maker. [laughs] Yeah.

**Mike Caulfield** [06:44]: I'm an AI maker or shaper.

**Host** [06:46]: Yeah. Yeah, cool, cool.

**Debbie Abelock** [06:48]: Okay. Lizne? I... We can't hear you because you're... Now-

**Host** [07:02]: Maybe David. Are you there? Can you unmute?

**Debbie Abelock** [07:05]: David, can you unmute and un-

**David Cole** [07:07]: I can

**Debbie Abelock** [07:08]: ... and view?

**David Cole** [07:09]: Yes. Yeah. I apologize for the sitting in the middle of the table. Um, I have a terrible-

**Debbie Abelock** [07:14]: [laughs]

**David Cole** [07:14]: I have terrible connection. It just l- it just came back. Uh, nice to be here. My name's David Cole. I'm based in, uh, Berkeley, California. I was a former writing teacher for many years and worked in education technology with schools and teachers in the National Writing Project on a number of literacy tech initiatives there and, and that's how I know Paul and Christina and, uh, others, and, uh, have been tracking this AI work that Paul's been facilitating with Writing Partners for a couple years now. I'm pretty glad to be here.

**Debbie Abelock** [07:45]: Elizabeth, can you... Uh, are you still muted or... Try again. Hmm. We can't hear you, so w- I'll give you some time to sit, perhaps to see if you can either come... Maybe just rejoining might work. Oh, now, now it looks like-

**Host** [08:03]: Yeah. Try to unmute. Yeah. Does it... Nope.

**Debbie Abelock** [08:08]: Not yet. Okay. We'll move on and come back. Go ahead.

**Suzanne Durisi** [08:15]: Me?

**Debbie Abelock** [08:17]: Yeah.

**Suzanne Durisi** [08:17]: Oh, hi. I'm Suzanne Durisi. I teach at, uh, Synergy School TK through eight in San Francisco. Um, and I have been teaching the Sift method with my sixth, seventh, and eighth graders since 2019. So they all have seen Mike Caulfield's face at least one time in a video.

**Host** [08:33]: [laughs]

**Suzanne Durisi** [08:33]: Uh, and so I'm really excited because, you know, we started to, uh, teach, um, you know, some, uh, prompt writing and things in, in, um, in middle school, so I think that prompt engineering and using that to cut through the, uh, the stuff, [laughs] the, the lies that are online will be a really, uh, fun tool for our, um, for our middle schoolers to use, a good use of AI.

**Debbie Abelock** [08:59]: Um, Wendy, I left you, um, alone because I didn't wanna bug you. But, um, what you can do first is unmute and, um, turn on your camera, and then if you double click on any chair, it will move you to that chair. That's the first way I've done it. Yeah, you did it.

**Host** [09:19]: Perfect.

**Debbie Abelock** [09:22]: Perfect. All right, Paul.

**Host** [09:25]: All right. All right, Mike, go for it. And, and, you know-

**Mike Caulfield** [09:27]: Oh, great

**Host** [09:28]: ... we, we, we do want this to be as interactive as possible. Um, I... So you... If-

**Mike Caulfield** [09:34]: Yeah

**Host** [09:34]: ... if you don't have a dog barking in the background-

**Mike Caulfield** [09:37]: Uh-huh

**Host** [09:37]: ... uh, leaving yourself unmuted is a, is a fine thing to do in this space, I wanna say, and, uh, so we can hear your amens and, you know, laughter and everything else. Okay. [laughs] Go for it.

**Mike Caulfield** [09:50]: All right. Uh, yeah, so I'm, I'm Mike Caulfield. Uh, some of you, uh, probably know me, some of you don't. Um, I'm probably, uh, most famous for the Sift method, um, and for my lateral reading, uh, work with Sam Wineberg. Uh, I wrote a book with Sam Wineberg. You see the book there on the table, uh, Verified. Um, and really, uh, um, people often talk about what I do as teaching people to do fact-checking. I, I tend to think of it as, uh, teaching people how to contextualize things that they find. So, um, especially online, the, the web is a, is a gigantic stripper of context. Uh, something kind of arrives at your virtual doorstep. You have no idea where it's from. Very often you don't know who posted it. Uh, you'll have video. You don't know what happened before the video started and after the video ended. You don't know who's behind the camera. Um, so, uh, the web kind of strips context away from things, and that's, um, you know, that's not a new phenomenon, you know, uh, w- with the web, but it's, it's been accelerated by the web. Uh, one of the things I tell people is, um, you know, the, that, um, you know, before the web, um, if a book or a newspaper arrived on your doorstep, you at least knew what it was. You didn't, like, go out and find a newspaper you subscribed to and were like, "What's this newspaper? I've never heard of it before." No. I mean, you've kind of done some of your contextualization up front. And, and now, uh, things hit us, and we kind of have to step back and contextualize things, uh, figure out what the context is. And that could be something about facts, and I'll, I'll give an ex- I'll show an example today with the toolbox about facts. Um, but it could be other things. It could just be like, where is this from? Or one of the things, uh, I, I find is something I'm always using, uh, tools do is someone makes a joke online that I do not get, [laughs] and I'm just... I'm searching to figure out what is this joke. Um, and so, um, it can be anything along, along those lines. Um, I was AI skeptic, uh, for a while, uh, because the AI tools were not good. Um, then I tried the AI tools again in last fall, early last fall, and it was just as they were starting to add some of these search features in where you would get links and things like that added to stuff. And that, um- That changed things a lot, actually, uh, in terms of what you could do, uh, with these tools. So I'm gonna show a tool, um, that I, that I built, um, talk a little bit about the, the thinking behind it, and, um, and it's available to all of you. Uh, so don't worry, you can get all this, uh, all this stuff. Um, let's make this-- let's embigen this a little bit here. Um, all right. So, uh, at checkplease.neocities.org where I pay the princely sum of five bucks a month to host basic HTML pages, um, I have, uh, this sense-making with SIFT toolbox. And the important thing to realize is in here, in this list, if you go into that box and you, you select all and you copy that, um, you'll get something that you can paste actually into any, um, actually into any, uh, uh... Let's, uh, put it there. Actually into any, um, AI platform you want, you can paste it in like that and then then upload it, or you can load it into a project. But it's kind of like a pre-prompt that makes the AI act in certain ways, right? Um, and I can show that like this. Uh, let's, um, let's actually do something... Do I wanna do it with this or do I wanna do it with Claude? I tend to like Claude. Eh, let's do it with ChatGPT. Uh, you can go in this and you can say something like, um, um, "Was the snow in-

**Kristina Cantrell** [14:06]: We can't, we can't see you.

**Mike Caulfield** [14:09]: To, to-

**Kristina Cantrell** [14:09]: Claude, we wanna see the toolbox window.

**Mike Caulfield** [14:14]: All right.

**Host** [14:15]: Yeah.

**Mike Caulfield** [14:15]: Oh, it's o- oh, it's only showing, it's only showing the-

**Kristina Cantrell** [14:18]: Yeah, it shows the tab. You have to switch tabs.

**Mike Caulfield** [14:20]: Oh, sh- okay. Maybe that works?

**Kristina Cantrell** [14:22]: Yep.

**Host** [14:22]: There you go. Perfect.

**Kristina Cantrell** [14:23]: Yeah.

**Mike Caulfield** [14:23]: Switch it. Okay. I guess every time I swish, switch a tab, I have to hit a button. All right. Got it.

**Host** [14:29]: We'll remind you. Yep.

**Mike Caulfield** [14:30]: Uh, yeah. [laughs] Okay. Uh, so, uh, was the snow in Wizard, uh, of Oz, um, asbestos? So this is something, you see this thing online. There's a TikTok that's circulating right now that's like, "The snow in Wizard of Oz was asbestos," right? Um, and maybe that's true, and maybe that's false, right? Um, or maybe it's somewhere in between, right? Uh, maybe once you know the context, it turns out it feels a little different, right? So this is without the tool, and this is kind of the way that this will answer something. Oh, I forgot I'm on, on Mini, where it takes, like, forever to answer a question. Okay. I, I'm gonna go to, uh, Claude after this one.

**Debbie Abelock** [15:15]: Forever is really relative. It takes a lot longer for a human being. [laughs]

**Mike Caulfield** [15:19]: Oh, oh, yeah. No, I know. I know, I know. But I, I, I ki- I've kind of grown up on the web here. Let's, um... You know, while it's, while it's doing that, let's, uh, let's do this in Claude, and I'll just do a new chat in Claude.

**Debbie Abelock** [15:36]: Oh, it's done.

**Mike Caulfield** [15:38]: Yeah, I'll do it. All right. Uh, so, uh, was the snow in Wizard of Oz asbestos? So this is without the tool in here. Uh, and i- if you do that in Claude, it's really the same across different, um, different models. Um, it'll go and searches the web, and it, it'll give you an answer that looks sorta like this. Say, "Yes, the snow used in Wizard of Oz was made of asbestos. I can share these details." And it has some links here, right? Uh, the snow in The Wizard of Oz was a hundred percent asbestos from MovieWeb. A classic movies from Meso- the Meolia. A Snopes article. It's really, uh, the re- the answers are really much better than they used to be. Uh, and you know, if you know AI at all, they're, they're-- the, the, the key now is this idea of grounding, that these things are grounded in these, um, in these, um, uh, in these, uh, uh, uh, sites. Um, all right. So that's the sort of answer that you get, right? Uh, it has links. It's kind of one opinion, uh, and it's presented really in this, uh, way that actually is a little bit wordy, um, which I've found that AI seems to be getting more and more wordy. But, uh, okay. So now we put in the, um, put in the prompt. Just paste in that whole prompt. And again, that whole prompt is this sorta thing here. I'll talk a little bit about what's in that. Upload it. Takes a second to process that prompt. And then we can ask... [typing] And it's gonna do a different sort of thing here. It's going to, um... Live demos are always risky. [laughs] So maybe I won't say anything until it does it, uh, just to be sure. Um-

**Debbie Abelock** [17:40]: Live demos is what really happens, so and we-

**Mike Caulfield** [17:43]: Yeah, it's what really happens. It's, it-- I, I feel like it's the most honest way to, uh, to do these things. One of the things you notice is it's doing a bunch of these in sequence. It's showing us what it's searching for. Um, and it's, it's looking at various things, right, right? And you can see the sorts of searches it does. Um, and, uh, here, um, it says, "Multiple reliable sources confirm asbestos say it was asbestos." It has that link. It has a statement. "The Snow in Wizard of Oz's Poppy Field scene was made of cr- chrysotile asbestos." Um, and then, um, it says, "Asbestos was widely used," right? So there's a link for that. Uh, asbestos was also used in other parts. Scarecrow's costume, witch's broom. Health risks of asbestos were already known at the time of the filming. Uh, and then it gives a, um, a site for that. And so each one of these is a site. And again, it's, um- It's a different format. It's not-- What I'm trying to do with this is kinda get out of the idea that it's going to do writing for you, right? I want it to think of it less as an author, uh, and more as, um, more as a research assistant or maybe even just a machine that gives research assistance, right? Maybe not even anything anthropomorphized. Um, now there's this thing here. It says, "The snow in 'Wizard of Oz' was gypsum salt, not asbestos," and it says, "That's incorrect. Multiple authoritative sources confirm it was chrysotile asbestos." Now, this is the same thing that the, um, the previous, uh, example said, right? Basically, uh, it's asbestos, right? Um, no cast members suffered health, uh, consequences. It says, "Well, you know, uh, we don't really know that." Um, uh, and again, uh, uh, a claim that Jack Haley, uh, the Tin Man actor, died from asbestos, uh, exposure, uh, through his father, and again, unable to substantiate. So it kinda breaks these things, uh, down, uh, does this confirmation and so forth. Now, what, uh... And g- it goes to this. I'll talk about this part later. But it's-- Part of the idea is this is interactive. So there's a feature in it where you can say, "Okay, I just wanna see all the sources," right? And so you can type "sources table," um, and it will generate you a table of the sources and then outline what each of them brings to this question, right? So think of this as, uh, you know, I don't know how long ago y'all went to school. But when I went to school, like, we'd get the little index cards. You know, we'd find a source, and then we'd write down on the index card, uh, like, "Well, okay, what, what does this source tell me that I need for my, um, I need for my paper," right? Um, and so this says, um... We can wait till it stops jumping around for a second. Um, this says Atlas Obscura. Um, it tells us that it's chrysot- chrysotile. Uh, I should learn how to pronounce this. Chrysotile, uh, as-asbestos, whatever that type of asbestos is. Uh, it has the link. Um, and I don't give a credibility rating. I actually do this usefulness rating, and the usefulness isn't credibility. Credibility is a part of it. But one of the things I learned when I was developing Sift is sometimes, you know, sometimes the most specific source you have is not the most credible, but it deals specifically with your claim, and, and so maybe you have to deal with that, right? Sometimes, um, sometimes the, the, um, most, uh, you know... So sometimes, uh, sometimes, uh, you'll have a credible source that's not particularly specific about your claim. Sometimes you'll have a less credible source that's very specific. Sometimes you'll have a source that is useful even though it's not credible 'cause it, it just shows what people think, right? It might be wrong, right, but it shows what people think. Um, and so this goes through, and one of the things that we're noticing here is when we start to read this ourselves, right? Asbestos, uh, was used as snow. Atlas Obscura says this. But then look at this. Now that we're pulling out these things, now that we're not really hiding the r- the, the links, Oz Wiki, right, says it's white gypsum, not asbestos. Now, that's interesting to me. It's specific about the material. Um, um, it mentions that MGM makeup artist Charles Schram, like this is a source, right, uh, recalled using gypsum. This is a wiki that is dedicated to Oz. If you know fandoms, you know that fandoms, you know, when you say something wrong on a fandom, right, [chuckles] uh, uh, generally you get, you get, um, you get hit. Uh, and so as we start to pull these out, right, it's not quite the simple answer that that initial, um, that initial thing was giving us, right? Um, one of the things you can do... So, so as we go through it, we start to see these things break down a little differently than we might have thought. Atlas Obscura says asbestos. Oz Wiki says it's gypsum and cites a source. Uh, History.com, uh, says gypsum and, and says, not only says the source, but says that Charles Schram, the makeup artist, um, uh, notes that it was used for the Scarecrow's costume but not, uh, for everything. Snopes says it was asbestos but says it's not really sure, right? So we saw that Snopes link when we were in there, right? But that Snopes link, right, made us feel like, oh, this is really firm. But if you actually look at what's in the Snopes article, and you can click through to this link, what it says is, "Eh, probably, but, eh, we'd like to see more evidence," which isn't quite, like, what it looked like at first, right? Uh, and so w- as we start to scan this, we start to see this, and it does this analysis, uh, here. It says, "With the asbestos-claimed sources mostly rely, uh, mostly rely on each other in secondary reporting," right? The original source seems to be this Atlas Obscura art- article. That's what it can find. I c- I dug deep into this. I can tell you it actually goes back further, but, um, but it doesn't cite MGM production records or first-hand accounts. And the gypsum claim, uh, sources, um, cite a specific makeup artist, uh, who worked directly with the snow material and recalled it as gypsum. Um, also appear, appears in reputable, uh, sources. Um, and you know, and basically, [chuckles] okay, uh, either one of these is incorrect, uh, different materials were used at different times. Um, uh, and this is not, uh, really either/or. Uh, the misconception about asbestos snow has been perpetuated through repetition, right? So we don't quite know what it is. Now, I have this other thing in here. I don't know how much it'll do here. But I have another feature I built in called Another Round. And, and what Another Round is supposed to do is we found a bunch of sources, and Another Round is supposed to go out, and it's supposed to try to find things that conflict with the stuff we already have, right? Um, and then, uh, or things that have an entirely different theory, so that we're not really missing things. Sometimes it's good, sometimes it's not so good. Um, but you see what it does here. I've, I've got it set up to, um, try to find a source that conflicts with the majority view. Try to find a source that supports the majority view with new evidence. Try to find a source with a completely different perspective. A lot of times those won't be available, but, you know, since we can ask it to do something, we're gonna ask it to do that. Um, and it's found someone named William Stillman here, uh, who seems to be a source for the gypsum claim. So that seems to be-- I don't know if that's majority view with new evidence or a source that conflicts with the, uh, majority view, right? Um, but here we have author Oz historians who say the snow was made of crushed gypsum, not asbestos, right? And again, what are we doing as we do this, and what are we trying to teach students to do as they do this? We're trying to get the-- try to have them get the feel-- Like, as I go further into this, what does it feel like? What is, what is emerging that's interesting? What's new? How am I gonna update, uh, update my beliefs, uh, on this? And it's, and, and as, you know, as I'm saying, you know, we have, um, uh, we have, uh, um, a variety of things here, um, which says, uh, we have a book, The Making of Wizard of Oz, which seems to say asbestos was used for snow. We have another book, um, that's actually on The Wizardry of Oz, which is actually the special effects, which is more specific, right? More the, the expertise is more specific. Uh, and so it's unfolding here, right? So we can do a number of things at this point, right? Uh, and again, the th- the idea of Sift Toolbox is, one, it goes out, and it tries to find these ev- these pieces of evidence and summarize for you. And I, I just think of that as a, a type of search that is more evidence-aware, right? Like, when you get into a search on Google, and you type in your keyword, it knows what you're looking for in terms of the keyword but doesn't really know what your research project is, right? Like, it has no idea of what your research project is and, and why you might want these things for your research project. This does, right? This is starting-- This is understanding, here's the thing we're looking into. Here's what we've seen. Here's the sort of things that we might want to, uh, you know, the sort of gaps in the logic we might wanna fill. So part of this is just better search results. And then the other thing is this sort of reading the room thing that I talk about in the book, uh, with Sam Weinberg. Um, okay, we have all these sources. It can be a little bit overwhelming. Are there ways to think about the groups that these are falling into? Uh, and in this case, what we tr- teaching the students to do here, and it's kind of scaffolding, but we're teaching them to say, "Okay, well, what, what do the gypsum claims have in common?" Right? "What do the asbestos claims have in common?" Uh, is there, is there sort of a, a group of people that are siding with gypsum, a group of people that are siding with asbestos? And this is kind of the, the bread and butter of doing research is, is as you kind of do the research, you're also mapping out the existing discourse, right? Um, so primary source supporting gypsum claim, uh, Charles Schram, uh, makeup artist, first-hand account, uh, Oz historians Stillman and Scarfone, um, personally handled the gypsum snow, had to pick it out from the actors' wigs and costumes. That's very specific. Uh, and I can imagine if you were sitting there picking out gypsum flakes out of the Cowardly Lion's mane between each take, that that would be-- You know, even if it's much later in life, that would have been a very memorable experience that would not have left you. Um, and then, uh, uh, asbestos claim stems largely from Alice Obscura is one of the first, uh, online places that really popped this to the, um, uh, into the, uh, uh, public consciousness. Um, here's something it notes. The sources with the strongest claims about asbestos are actually law firms. [chuckles] I, I don't know if you noticed that, but there's, like, Ka- you know, Kazan law firm. Uh, there's a bunch of law firms that are doing asbestos litigation, and it's just kind of like SEO bait that they're putting on their site to get people over to their site to join class action lawsuits, right? Um, so again, does it say one way or the other? Uh, maybe not. Um, but it's starting to, it's starting to give us a sense of this. And, and what I always say with this stuff with students is, you know, I kinda don't care where you land in terms of your opinion. If you've mapped out the discourse, and you actually know where the discourse lies, you know, look, it's these sorts of people that are saying this. It's these sorts of people that are saying this. This claim has this behind the evidence. This claim has this behind the evidence, strengths, weaknesses, et cetera. If you can map all that out, and then you can say, "Okay, this is where I am on the map." And even if it's a place where I'm like, "I don't... Okay, I don't know how you got there." Um, if you've done the map, and that's where you think you are, I'm fine with that, right? I'm not here to tell you what you b- you know, what you should believe. I'm here to make sure that before you decide what you believe, you understand the sort of existing conversation, the existing discourse, the existing evidence. And once you have all that, um, you know, go with God. It's, it's your, it's your choice. Uh, so, um-

**Host** [30:23]: Mike, could we-

**Mike Caulfield** [30:24]: Yeah.

**Host** [30:24]: Mike, could we, could we jump in, um-

**Mike Caulfield** [30:26]: Yeah, yeah, absolutely. Sorry, I keep going

**Host** [30:27]: ... with some thoughts?

**Mike Caulfield** [30:28]: Yeah.

**Host** [30:28]: No, no. I, I wanna give you enough time to kind of lay it out. Um-

**Mike Caulfield** [30:32]: Oh, yeah.

**Host** [30:34]: And I, I just wanna say, if this is the first time you've seen the toolbox, you may, you may be like, "Oh my God." [chuckles] But whatever, you know, how... There's a lot, right? Um- But you asked a question earlier about, um, what are we trying to teach.

**Mike Caulfield** [30:50]: Yeah.

**Host** [30:51]: And you started to answer that. Um, I'm wondering if other people wanna kinda comment on that.

**Mike Caulfield** [30:56]: Yeah.

**Host** [30:56]: When you see this, what do you think Mike's trying to teach? Or what, what could you use this for teaching for? Or what are your questions or thoughts? Anything. Don't be shy. Jump in, please.

**Steph Gamble** [31:12]: So I started playing with this a little bit, um, yesterday, and not in terms of more, like, current events type things, like a lot of the examples you showed, but thinking about, um, the, the sort of traditional research that we do is mostly in-

**Host** [31:26]: Mm

**Steph Gamble** [31:26]: ... in art history papers. And one of the things that our students are woefully unable to do for a variety of reasons is historiography, and most of our faculty, I think, are like, "That's too much for students to do." Um, so I played around with it as a way to, like, kinda help jump a student in to be like, you know, use this read the room feature. So like, what on... Here's my topic, like, read the room for me, and then kinda create the, um, the source list and, uh... And I, I did ask it to s- put it then in chronological order for s- you know, more of that historiographical perspective, um, when it created the source table, and I thought it was really quite good at that, and would be something that wouldn't replace any work that our students are currently being asked to do, but would really augment their ability to understand what they're doing as they start on a research project. Because the way I do it now, you know, I talk to them about scholarship as a discourse, and I, you know, point to the fact that they can kinda look for this in the notes, especially in an introduction. But often then when I see the books that they request and pull from the shelf, they're, they're looking for stuff that's out of date. So, like, the discor- they're not gonna find the newer discourse because it's not in the notes of the source that they pulled because they pulled the one that had a title that sounded most spot on, which is, you know, not the most relevant source for them to be at, and it would help get them to that point. So it's a, it seemed like it, it's doing the exact same work, but kind of in a slightly different direction. I thought it would be really helpful for our students in that way.

**Mike Caulfield** [33:01]: Cool. I, and I... And one of the things that you mentioned that I think is really neat about this is, so, um, it's, you know, it's a set of instructions that allows it to act this way, but it's also just behind it is still whatever that, um, model can do. So, like, uh, when, when you say, like, they're doing this sort of thing, and then you see this, and you're like, "Hey, can you put this in chronological order?" Like, there's nothing that I wrote [laughs] in there that allows it to be put in chronological order, but it's, it's on top of everything else the model can do, right? And so, yeah, if you have all this stuff and, and it can put it in chronological order, you can ask it to do that. Or, um, you know, could you, uh, could you flo- you know, could you group this into things that are references to books versus things that are references to websites? You know, that, that sort of thing. Again, I haven't put anything in there, but that's something that these models can do. So that's, that's super cool.

**Debbie Abelock** [33:54]: You know, one of the things I was thinking is that, um, when we do research projects with kids, we always start with, you know, kind of wondering and searching, and we often get stuck with kids who search and search and search, and they never really get to analysis and synthesis. And one of the things that this does is that you could, in teaching the research process, say, "I don't want you to focus on search. I want you to get these sources. We're gonna work on today is how to compare sources, how to analyze sources, how to synthesize information out of sources." Or, and what this does is it, it puts the raw material, it puts the evidence, it puts the conte- text on our plate and says, "Okay, now what are you gonna do with this?" So I feel it, it depends on your goal of teaching research when you would wanna use this, but it certainly has a place in the teaching of research.

**Mike Caulfield** [34:57]: So one of the things Sam and I found in our research, uh, with students in, in searching and in research, uh, was exactly that, Debbie, that, um, uh, the, the people that are really accomplished at this are always in a, a process of, um, you know, grab some sources, pull them, synthesize, step back, look, say, "Okay, what does it look like now? What... Uh, am I still on the right path? Is this still the right question? Does this raise other questions? What am I seeing?" Back in, pull some sources and so forth. And so those are the people that are really accomplished. And, uh, the thing we found was the students that just got overwhelmed by search just started foraging, right? And they're just, like, they're just, like, throwing everything into the bucket, bam, bam, bam, bam, bam. Uh, and then, and then at some point they're done. And, uh, and then they go and they take that bucket, and then whatever's in the bucket is, is, is, you know, uh, what they'll do. And some students, you know, some students just put, like, two things in the bucket [laughs] and that's its own sort of problem. But even the students that go and they find a bunch of stuff, you know, they'll click through. Maybe they, maybe they get to the second page and maybe they click through. But it's kind of this process that do- it doesn't have that, doesn't have that, uh, iterative aspect. Uh, whereas the others, like the minute, uh, when we looked at fact-checkers, like professional fact-checkers, before they would click the link, they would, in their mind, imagine what they thought they were gonna find on the other end of that link. And then when they clicked the link, they would ask themselves, "Is this what I thought I would find?" Right? So it's always, like, building an expectation, building a model, going a little further, seeing if that model is still holding up, refining the model, getting more information. Is that model still right? Yeah, I, I... Like, that's e- exactly it.

**Host** [36:49]: Mike, one of the, one of the question, one of the things that Steph said, um, and if there are AI skeptics, and there are AI skeptics in the room, there's a concern about replacing work that we want students to do.

**Mike Caulfield** [37:02]: Mm.

**Host** [37:02]: Right? Um, to what degree is, uh, I mean, have you, have you thought about that with this tool? Like-

**Mike Caulfield** [37:11]: Yeah, I'm worried about it, to, to tell you the truth. I mean, I worry about it. Like, it's probably my biggest worry, is, um, I even have a thing in there that says, um, used to say verdict, now it says what a fact-checker might say. And I'm thinking, like, I th- I think maybe I'll strip that out. Um, and then I thought, the reason I ke- kept that in, uh, and I can scroll up and show that here. Um, uh, the reason I kept that in is I, I'm, I'm, uh, I'm thinking of the tool now as something where it has a bunch of pieces, and if you're an instructor, maybe what you wanna do, which you maybe wanna delete out some pieces, and it's just easier to delete out stuff. But i- if I was g- you know, if, if... Well, like now, when we're talking about using the tool, uh, when I present it, I tell people, "I put in st- more stuff here than you need, right, for your students. And maybe what you wanna do is maybe you want to, you can go, uh, into the code here, very easily find, just do a search and find the section that says, 'What a fact-checker might say.' It has a little description of what it puts out. Just delete it out before you give it to the students, right? If, if, if that's getting in the way of what you teach, right? Um, if you, um, if you don't like this assessment of source reliability, right? If you think, 'Okay, I actually want the students to go and do a little more of that themselves and do that a little manually,' you know, delete it out. Um, or, you know, alternatively, have everything in the begin, like sort of scaffold that up, and then, you know, maybe, maybe kick some pieces out as you go. Um, but I, I worry about it all the time. It's my biggest worry is, you know, when does scaffolding, you know, um, become a crutch, you know, instead of a, a way to get somewhere. Uh, and I think of this right now as scaffolding. I try to make sure that everything that's happening on this page is modeling something, um, that the students can learn from. Uh, but, but yeah, I don't know. [laughs] Uh, you know, this is where, this is where research comes into play, and we haven't done research on it yet.

**Host** [39:24]: Let's, let's hear what other people think about that. A- any thoughts given what you've seen so far?

**speaker_11** [39:30]: Does my microphone work now?

**Host** [39:32]: Yep, it does.

**speaker_11** [39:33]: Yes.

**Host** [39:33]: Okay.

**speaker_11** [39:33]: Great. So I, like Steph sa- I, I'm a high school librarian and in the middle of research, and I wonder with the AI finding resources for us that the paywalled information that we give to them, that they're... Like, maybe after this, I would say, "See what you can find in these databases to see if it confirms," or like, I would bring it to some other sources too just to give them that, um, experience to add with this. I think this is really interesting. I'm not sure that my teachers would allow it. They like them to find their sources on their own, but I gotta work on them. [laughs]

**Mike Caulfield** [40:16]: One, one thing you could build yourself, and this is, I think once you see the stuff in it, um, you can build a section of this, uh, which is, um, uh, you know, suggested library resources that you, you know? So, like, if, if you were looking at this, um, is, you know, it actually... Sometimes it still hallucinates books. Claude actually is doing much better with not hallucinating. Uh, some of the other ones still hallucinate books, but they've done better.

**Host** [40:46]: And links. Right, yeah.

**Mike Caulfield** [40:46]: You know? Um-

**Host** [40:47]: Yeah. Go ahead.

**Mike Caulfield** [40:48]: And maybe you could. Maybe you could build a little section that says, "Hey, for further library research, here are some things you might look at. Here are some search terms you might plug into your, uh, database."

**speaker_11** [41:00]: I'm also next year teaching an AI literacy course, which I feel like this could be a big, a big interesting part of for them. Thank you. [laughs]

**Mike Caulfield** [41:13]: Thank you.

**Debbie Abelock** [41:15]: I really appreciate that you talk about contextualize rather than, uh, fact-check, because fact-check gives kids the idea that they're looking for, you know, people to confirm, to triangulate or whatever. But really, it's not about locating the answer. It's about locating the raw mat- that what's so nice is it's about lo- locating the raw material that can help build an answer.

**Mike Caulfield** [41:47]: Yeah, exactly.

**speaker_12** [41:49]: Yeah, Deb- Deborah, that's, Debbie, that's what I was kind of thinking as I was listening, because I've been seeing so many students that when you see their paper, it's as if they've only taken whatever the conclusion or the finding of a study was, if they are engaging, Elizabeth, with, like, scholarly database sources and things like that. Um, but there's no evidence that they've actually looked at the experiment that was done or, you know, the, the mechanics of the study. And one of the things I appreciate, um, Mike, about this, um, and this is my first time seeing it, so it's, it's been like, whoa, [laughs] um, is that it does model looking at, um, that context that Debbie was pointing out, how the sources relate to each other and, and, and really thinking about it

**speaker_11** [42:52]: Like you described earlier by stepping away and kind of looking at the relationship. It, and, and unlike something like Research Rabbit, which I also just, you know, discovered recently, um, it's not just a map of the relationships, right? You're modeling what kinds of questions to ask about the relationship. Um, so I do appreciate that.

**Mike Caulfield** [43:24]: Any other sort of-

**Fred Haase** [43:24]: Yeah, no, absolutely. Go, go ahead.

**Mike Caulfield** [43:27]: No, I was just gonna ask any other sort of skeptical or questionings or... 'Cause-

**Fred Haase** [43:34]: I have something.

**Mike Caulfield** [43:35]: Oh.

**Fred Haase** [43:35]: Well, c- c-

**Mike Caulfield** [43:36]: Go ahead

**Fred Haase** [43:36]: ... 'cause I'm a little, I'm, I'm actually trying to, I'm torn in how I would, um, express it. I mean, so there's a part of me that wonders about, like, the speed of the results that you're getting and how they're assembled, if that doesn't sort of artificially maybe limit what you're looking at or... Like, I could see a lot of students being like, "Well, I'm all done," you know? [laughs]

**Mike Caulfield** [44:07]: Yeah. Yeah.

**Fred Haase** [44:08]: And, and, and, and then the, the second part to that is I, I can only really think about it in metaphorical terms, but I- it's a little bit like, um, you know, the difference between being, using an analog dictionary or thesaurus and a digital dictionary and th- thesaurus. And I think one of the things that, like, gets lost in that transition is all of those potentially meaningful sort of like digressions where you, you know, like, where you discover something that you did- you weren't actually intending to discover, but you happen upon it, and it ends up being, like, really useful-

**Mike Caulfield** [44:43]: Uh-huh

**Fred Haase** [44:44]: ... somehow. And I, and I, and, like, it just seems like the more that there's a tool, like there's less, there's an opportunity for that, I guess, that's making me wonder. But I mean, that's maybe a lot.

**Mike Caulfield** [44:55]: No, no, no. I mean, e- exactly the right questions. Um, uh, so the speed thing, uh, I, you know, I think you're right. But one thing I'll say is, like, when I present, I just present fast, and when people use it, they use it slower. Um, it's, it's-

**Fred Haase** [45:10]: Mm-hmm

**Mike Caulfield** [45:11]: ... just not as fun watching someone use it slower, [laughs] slowly. So, so, you know, you can watch me read the, uh, Alice obscure, uh, um, article, but you'll also wonder-

**Fred Haase** [45:22]: Mike, can I, can I add to that fast and slow?

**Mike Caulfield** [45:25]: Yeah.

**Fred Haase** [45:25]: It's also, like, whether you're doing it individually or you're doing it in a group is different as well.

**Mike Caulfield** [45:30]: Yeah. Yeah, yeah.

**Fred Haase** [45:31]: But go ahead, yeah.

**Mike Caulfield** [45:32]: Yeah. So, so I, I present fast. It, I think people generally use it a, a little more slowly, but I, but I do also agree that there's, you know, there's some, sometimes there's no replacement for time, right? Like, like sometimes you need a little time for things to settle, and if you, if you're looping in too fast, it's not settling, right? And so, um, again, I th- I think that's where, I think that's where, you know, module and lesson design, uh, come in. I think that's where other people might come in, uh, you know, to Paul's point. Um, on the second question, um, one of the reasons why I put in that, um, thing where you do another round, and, and one of the things is, like, find something completely new about this, right? Is that when I initially, uh, did it, of course, it would just, it would just keep on finding more stuff that was more of the same stuff, right? And it wouldn't give me that feeling I get sometimes in a Google search where I just see something out in left field, you know? And then I click on that, and I'm like, "Actually, that's the more interesting question." Um, and I haven't got a thing in it right now that formalizes maybe following down another trail. Um, but I think it could, I think we could do something like that in it. It's, it's a double-edged sword, of course. I mean, one of the things that we found in our research is that some students follow those unexpected trails a little too easily, you know, and just sort of go on a endless, you know, journey of forking paths, uh-

**Fred Haase** [47:05]: Sure

**Mike Caulfield** [47:05]: ... and end up, you know, somewhere a million miles from where, uh, they were, but it's not necessarily a productive place because they haven't reflected to get there. Um, but yeah, I'm open, I'm open to ways to, to build a little even more randomness into it, more ambient awareness, right? Of, uh, when you go through this thesaurus, you're not only seeing the word you need, but you're seeing the words around it, to your point. You're also flipping through it and seeing words on your way to that page, right? Like I- I'm, I'm open to building that stuff in. Uh, and I think, I think we could, uh, we could do that.

**speaker_11** [47:40]: I think there are-

**speaker_12** [47:41]: Mike.

**speaker_11** [47:41]: Oh.

**speaker_12** [47:43]: Go ahead.

**speaker_11** [47:43]: There are a couple trails in here, even just on the screen here. It, my, you know, 10th graders, if they were studying this question, would think about the '30s and where else was asbestos being used-

**Mike Caulfield** [47:56]: Yeah

**speaker_11** [47:56]: ... asbestos being, they already knew it was bad, or what do the costume designers at The Wizard of Oz, what was their life like every day, or, you know, things like that, that there, where there are actually some things in here that might take them somewhere else with The Wizard of Oz or with asbestos.

**Mike Caulfield** [48:13]: Yeah. There's, there's a really interesting parallel question on this, which is just, um, occupational health and safety generally, right? Like, um, you know, it doesn't matter if it's asbestos or gypsum, they turn out to both be not particularly good for you. Asbestos is worse, but, uh, gypsum is, is no good. And Charles, uh, the, the, the thing that says gypsum says, "These actors were told, 'Just don't breathe in too deeply.'" [laughs] You know? Um, uh, and, and of course, that wouldn't happen on a set today, right? Like, we just have a different sense of what occupational health and safety is that we've developed, uh, over... And, um, yeah, you want something that, like I, like the same way when it says another round, it says, "Find some, some out of left field evidence." Um, we could say, uh- We could put something in there that when you do that says, uh, "Note another potential topic," or something like that, you know? And maybe that is, um, [beep] hey, like whether it's gypsum or asbestos, like how do people get away with [laughs] this stuff?

**Debbie Abelock** [49:16]: Yeah, but you know, Mike-

**speaker_12** [49:17]: So my question-

**Debbie Abelock** [49:17]: ... there's something that hit me when you said that. Uh, we're thinking that this is the research.

**Mike Caulfield** [49:24]: Mm-hmm.

**Debbie Abelock** [49:25]: What if we, in our minds, flip and say, really the project that kids are really doing is we're studying The r- Wizard of Oz.

**Mike Caulfield** [49:34]: Mm-hmm. Yeah.

**Debbie Abelock** [49:36]: Let's look at this particular thing, and from this, let's pull out a topic about The Wizard of Oz that's, that you learn about. Something that, for example, you mentioned the whole idea of the, you know, the, the, these, these various things like gypsum and so forth, and pulling that out and doing something entirely different. It would be very interesting to know what the regulations were around the use of what kind of toxic materials. You know, I mean, we could really say, "This is a social studies class. We're not interested in The Wizard of Oz. We're interested in the time period."

**Mike Caulfield** [50:16]: There's a-

**Debbie Abelock** [50:16]: What are we learning about, you know?

**Mike Caulfield** [50:18]: There's a really fascinating piece with this too, uh, which is, you know, the reason why they were using asbestos was that, um, for these things, uh, and also the reason why they used gypsum, uh, which is, which is it hard to light on fire, was, uh, before this they used a bunch of flammable things and people died in, in fires on movie sets, [laughs] you know? So they thought, they thought, "Oh, okay, well, you know, we don't like people dying in fires on movie sets." I mean, if you think about movie sets, they're quickly constructed, they're often quite dry. Uh, there's pyrotechnics on them. Um, and so it's quite a quite dangerous space, and so they thought they were making it-

**Fred Haase** [50:54]: Just the sheer-

**Mike Caulfield** [50:55]: Uh, more-

**Fred Haase** [50:55]: ... heat from the lamps back in those days would light fires.

**Mike Caulfield** [50:59]: That's right. Right. The cling, the cl- the, the Klieg, uh, lights that they used were just like, yeah, just absolutely could get anything, uh, lit up. Um-

**Fred Haase** [51:10]: Like-

**Mike Caulfield** [51:10]: And so, yeah, so some, some of those directions.

**speaker_12** [51:12]: So Mike, I have a question. How does, uh, these, the query samples on your, um, uh, Substack post that kind of go with your examples of what to use with this prompt language, um, are all kind of like Snopes-y, like somewhat esoteric questions.

**Mike Caulfield** [51:32]: Mm-hmm.

**speaker_12** [51:33]: How does this prompt training perform with something that students are more likely to be researching in high school, like Israel and Gaza?

**Mike Caulfield** [51:46]: Uh, uh, better. Uh, uh, the reason why I often use the esoteric stuff is-

**speaker_12** [51:51]: Mm-hmm

**Mike Caulfield** [51:51]: ... is it stress tests the system. Uh, one of the ways that... There's a guy named Thomas Rid, who looks at misinformation and also, uh, gave a, a great talk on, uh, AI that I saw. Um, and he has this, he has this, uh, metaphor for AI. He's a, he, he looks at military misinformation, and this probably informed his metaphor. He says, uh, uh, "LLMs are like a submarine," right? The deeper the water is, the more maneuverability, the more capability it has, right? But in shallow water, like, you know, you can be in real trouble. And, um, and I think that's right, right? So the, the smaller the, the, the set of information-

**speaker_12** [52:32]: The data set. Mm-hmm.

**Mike Caulfield** [52:33]: Yeah. The, the more, the more likely hallucination, the more, the more likely, uh, some of these, uh, downsides. Uh, the, the broader the, the situation, the better. I have one on my, um... If you wanna see one that is more of a, um, this one here, AzerrgAT claims. This is, this is a, uh-

**speaker_12** [52:56]: You have to refresh your screen.

**Mike Caulfield** [52:58]: Yeah.

**Fred Haase** [52:58]: Yeah, there you go. Okay.

**Mike Caulfield** [53:00]: Uh, so, uh, if you go to the, the, the Neocity site and you click the AzerrgAT claims, this is actually a very broad claim on which there's a lot of study. Um, you know, basically, were hunter-gatherers more peaceful than agricultural societies, uh, more warlike or about the same, right? Uh, and you can jump into that, uh, sort of thing where there are entire books. There's like 100 years of looking at this, right? Uh, and it will, um, it will start to, uh, map out that, um, map out that stuff for you, right? And you could do a couple other, uh, ones, uh, here. Um, you know, and so you'll have Azergat there. You'll have, uh, uh, Pinker's Better Angels of Our Nature. Um, Raymond Kelly's, uh, Warlike Societies and the Origin. Um, uh, a, a review of a couple of these things. And so it'll start to map out this debate over whether, uh, agriculture introduced a more warlike, um, society, uh, or whether, um, or whether it, you know, it was about the same or, or whether the Pinker idea that ac- actually things got, um, things got, um, less, uh, warlike. I know Pinker has some problems, but, um, but, you know, he wrote this book and, uh... But it actually does, it actually does, uh, better on that and you'll end up with better, uh, better sources. Uh, and it'll actually, as you see here, it will actually refer students to, to books and things like that, which I think is pretty useful.

**Fred Haase** [54:35]: Can I ask another question just based on the conversation? 'Cause, uh, and I might be contradicting myself here, I'm not really sure. I'm trying to think through it, but, um, can, can there be a tool perhaps or sort of some sort of sequence that might help a student refine the, or like the question, the, the actual research question? Because I, at least at the high school level, that is a real challenge. Like, you know, um, getting it narrow enough but not too narrow and not so big that, you know, like they're gonna try to write a book. Um-

**Mike Caulfield** [55:14]: Yeah

**Fred Haase** [55:14]: ... I just wonder if there'd be, like, a sequence of suggestions perhaps, or if maybe that's the, the, some of the intellectual labor that is the fruit of using a tool like this. I'm not, I'm not 100% sure.

**Mike Caulfield** [55:26]: I, I conceptualized it. And again, like, until you get it into classrooms and you see how it works when it hits the ground, you never know, right?

**Fred Haase** [55:34]: Mm.

**Mike Caulfield** [55:35]: I had conceptualized that piece of the research question kind of living at the, uh, level of sort of the lesson, classroom interaction and so forth, and not necessarily in the tool.

**Fred Haase** [55:46]: Mm-hmm.

**Mike Caulfield** [55:46]: Like, that would be a layer, a, a layer above it. Um, but, you know, I, I could, I could... Uh, part of the thing that excites me about this versus, like, going out and getting a specific piece of software to do all this, um, is it's daunting at first, but you really can go in and, uh, you really can go into that, uh, prompt and, um, you really can go into that prompt and, uh, add what you want. Like, uh, like, it's not even programming, right? You can go and, and you write in just sort of normal text what you want it to do. And, uh, so I'm... One of the things I'm really excited about, it is sort of like open source software but for everybody. Um, and the one thing I, I, you know, we, I know we're coming on time here. Uh, the one thing I'd, I'd leave you with is my experience with the prompts is the people that are best prepared to write AI prompts are teachers. Like, it's not programmers. If you want a person who has had to break down a task and explain in precise detail how to do that task, uh, to something that doesn't understand the task, um, is gonna, you know, and, and, and can conceptualize all the ways it might go wrong, that's a teacher, right? That's not a programmer. And so I actually do think that, um, there's kind of a, a dual thing here. One is the tool, but the other thing is, uh, if I can get people overcome their nervousness about, about getting into this and just, just, you know, there are little sections here. Just write a little section here. Get in this, get in here and just, you know, um, um, uh, occasional, uh, a refinement of prompts or something like that.

**Fred Haase** [57:34]: Yeah.

**Mike Caulfield** [57:34]: And write what you think that should be like, you know, and see if it works.

**speaker_12** [57:38]: And Mike, one of the things I was, I just put in the chat that strikes me about this, and it relates to what you just said, is that I do think, um, making this code freely available like you have, um, does help foster more equity between our students who can only afford the free versions of these tools and those who can subscribe and create their own custom GPT over time that just responds to them the way they want. Um, so I appreciate that aspect of what you've created.

**Mike Caulfield** [58:11]: Thank you.

**Linda Hoiseth** [58:13]: And to address the, the writing a research question topic, um, Chris Bell at the International School of Bangkok has written some code that does a feasibility study, uh, for a specific assignment. So his, his lens was the IB extended essay, and so he has the students input what the criteria are, what the rubric is, and saying, "If this is my question, how would I score?" And, and AI does an amazing version of saying, uh, "You probably need to focus on this a little bit more," or, "This is too broad," or, "This is too narrow," or, "You're gonna have a hard time finding your resources," or all sorts of things.

**Fred Haase** [58:49]: How do you spell his name?

**Linda Hoiseth** [58:52]: Uh, Christopher, and then it's B-E-L-L.

**Fred Haase** [58:56]: Oh, Bell.

**speaker_12** [58:56]: And what does he call it again?

**Linda Hoiseth** [58:58]: A feasibility study.

**Host** [59:02]: So, um, I wanna kind of, uh, give us a, a, an off-ramp here. Uh, but also say that, um, some of the things you suggested, Mike, I've done, um, on Writing Partners so that, um, we've... So for example, um, I took your code and I added, uh, give me keywords anytime-

**Mike Caulfield** [59:21]: Oh

**Host** [59:22]: ... you give me a, a link. So it gives the keywords. So, but, and, but also kind of even bigger than that in some way, it's so that it's not a, a fire hose coming at [laughs] students. Um, we have it pause at the end of every table and ask the student to reflect on what they see there, right-

**Mike Caulfield** [59:41]: Oh, that's cool

**Host** [59:42]: ... and, and comment. So-

**Mike Caulfield** [59:42]: So a way of slowing down.

**Host** [59:44]: But-

**Mike Caulfield** [59:44]: Nice.

**Host** [59:44]: Yep. So, um, anybody can go, um, join Writing Partners and, um, you automatically get the, I think we called it the fact-checking and historical analysis teammate, and you can play around with it. Um, also in this room, there's a link to it there, and next week we'll kind of look at that in more detail. But that's sort of my last thought. Anybody else wanna jump in with their last thoughts here? But yeah, but Mike, so just, uh, yeah, I, I, I will add to, I, I totally, um, am with you, everyone will know this, about teachers being the best people to build these things. Um, however, they do need the time and en- you know, the, to, to think about the process too, right?

**Mike Caulfield** [60:39]: Yeah. No, absolutely. And, and, um-

**Host** [60:42]: Yes

**Mike Caulfield** [60:42]: ... uh, you know, again, uh, you know, in my dream world I'd maybe get some, uh, funding to go, you know, out on the road with this and, you know, we'd look at it, we'd play with it, and then like, yeah, we'd get to these tables around the room and, like, decide-

**Fred Haase** [60:58]: D'oh. [laughs]

**Host** [61:01]: Hold on. We lost his last comment. All right. When we get funding, he'll come back. No, there he is. You're back. Yeah.

**Mike Caulfield** [61:11]: I don't know why. It just, it just suddenly, uh, zipped off my camera. Um, I'd love to g- get to a situation where, yeah, we go out, show this tool, and, uh, you know, and then the s- the second part of the workshop after lunch is, like, get around the table and decide what little extension module you're gonna build on it and, uh, and, you know, let's try it out. Um, like, I think, uh, again, um, there's, there's really two pieces of this. One is that I think the tool is really valuable. Uh, and then sort of a larger point is I just hear a lot of discussion that is sort of like, you know, are you an AI booster or are you an AI doomer? And, like, I, I want people to think of themselves as AI shapers, like, people that can at least try to, to shape what this technology is instead of just accepting what we're given.

**Fred Haase** [62:06]: Cool.

**Mike Caulfield** [62:07]: That's a s- a little bit of a soapbox ending.

**Host** [62:09]: That's-

**Mike Caulfield** [62:09]: So, for the world.

**Host** [62:10]: No. [laughs] You're in the right room for that.

**Mike Caulfield** [62:12]: Good. Yeah.

**Host** [62:13]: That's cool. Thank you.

**Mike Caulfield** [62:15]: All right.

**Host** [62:15]: Well, somebody's clapping.

**Mike Caulfield** [62:16]: All right. This is really-

**Host** [62:17]: Thank you all. Um, just, just so, just so you know, um, we are here every Wednesday night, um, uh, working on this stuff. Um, we don't always have as, as brilliant a guest as, as Mike Caulfield, but, um, please join us whenever, um, and, uh, we'll keep building around all of this. Debbie, you have any last thoughts?

**Debbie Abelock** [62:38]: I just think Mike's comment about if you're not at the table, don't complain about the results is a really important one, and thank you for that.

**Mike Caulfield** [62:51]: Thank you.

**Host** [62:53]: All right.

**Fred Haase** [62:54]: Yeah. Thanks folks.

**Host** [62:54]: Talk to you all soon.

**speaker_11** [62:55]: That's great. Thank you.

**speaker_12** [62:56]: Thank you so much.

**Linda Hoiseth** [62:57]: It was so...

**speaker_11** [62:57]: Thank you very much.

**speaker_12** [62:59]: Good night.

**Linda Hoiseth** [62:59]: Thank you. Good night.

**Debbie Abelock** [63:00]: Good night to everyone. [laughs]

**David Cole** [63:03]: Thank you very much, Mike. Thanks, Paul.

**Host** [63:05]: Sure.

