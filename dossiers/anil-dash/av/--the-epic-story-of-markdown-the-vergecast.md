---
title: "# The **epic** story of Markdown / The Vergecast"
person: anil-dash
section: by
type: talk-transcript
year: n.d.
venue: ""
source_url: https://www.youtube.com/watch?v=arjKK7fRtSA
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 32
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# # The **epic** story of Markdown / The Vergecast

*Speakers (inferred):* speaker_0=Host, speaker_1=John Gruber, speaker_2=Anil Dash

## Transcript
**Host** [00:00]: [upbeat music] Hello, and welcome to The Vergecast, the flagship podcast of asterisks and underlines. I'm your friend David Pierce, and today on the show we're gonna talk about Markdown. Now, Markdown is probably very familiar to you if you're, like, a deep nerd about note-taking apps like I am, and maybe a word you've never even heard of otherwise. If you're in that latter group, don't worry. We're gonna, we're gonna get into it. The way to understand Markdown is basically as a way of writing text that both a computer and a human can understand. So if you're, if you're writing words and you wanna bold something, right? Rather than go to, you know, file and format and bold, you just put two asterisks at the beginning and at the end of the word, and that tells the computer that this is bold. Mar- Markdown is a, a language that computers understand and know how to translate into other things. It also just looks like emphasis, right? So when you're reading it, you see a word with two asterisks on either side, and you go, "Oh, that's emphasis." Uh, you can do underlines for underlines. You can write a link in a specific way so that it can be read by Markdown, so you can see the title of the link and then the URL of the link itself. It's a way of writing text that both computers and humans can understand. It's a very powerful thing, and it is absolutely everywhere. All of a sudden, all of these note-taking apps are using it. Obsidian is a very popular one that lets you write in Markdown, and everything is stored on your computer as Markdown files, which are basically, again, just annotated text files. This is also kind of the lingua franca of the AI industry right now. When you make a Claude.md file, the MD stands for Markdown. It's a way of writing for the computer that is simple and straightforward and that lots of people understand. Markdown is not just an inherent thing of computers. It was created. It was created by a person, and that person is John Gruber, who you might also know as the writer of the blog Daring Fireball. John's gonna come on the show, as is Anil Dash, who is a longtime tech executive, was around in the early days of Markdown, and really has seen it grow up into the standard it has become. We're gonna talk about where Markdown came from, why it's so important that this thing became a crucial part of the way that we write text on computers, and where do we go from here. The conversation is very nerdy, I will just warn you in advance, but I had a really good time, and I think you will too. But first, here's everything else happening on The Verge today. This is 90 Seconds on The Verge for Monday, June 15th, 2026. Fox announced that it's buying Roku in a deal valued at $22 billion. If this deal goes through, it's always a big if, the mishmash of stuff in the combined company would include all of Fox's TV networks, Tubi, Roku's streaming devices, its smart TV software, and the Roku Channel. Fox says the plan is to keep Roku as the sort of ubiquitous Switzerland of the streaming industry that it has been, but of course, that's what everybody always says and nobody ever means it. In particular, I'm fascinated to see what comes of Tubi and the Roku Channel, which would combine to be a very big and very powerful free streaming service. The big news all weekend was the US government's bid to shut down Fable, the new super powerful AI model Anthropic released last week. The government said it was blocking its use by foreign nationals, which turns out to be such a complicated thing to enact that it works as an overall ban. It's not entirely clear that the government can actually do this, but Anthropic did, in fact, shut off the model. There's so much we still don't know here. Fable is basically the same model as Mythos, which Anthropic said was too dangerous to release a couple of months ago, only with some guardrails. Is it actually a security risk? Who bypassed the guardrails? What happens when they do? Who raised the alarm here? Is this just another strange turn in the fight between Anthropic and the US government over who gets to decide how AI gets used? Like I said, lots of questions. Finally, The Verge's Dom Preston reviewed the Honor Magic V6, a foldable phone that accomplishes three very important things. It has a battery that lasts two days, it has genuinely good ratings for dust and water resistance, and it is the thinnest foldable phone we've seen yet. It's still $2,000, which means you probably won't buy or ever even see it, but there are good things coming in foldables. You can read more about all of this at theverge.com. That's 90 Seconds on The Verge for Monday, June 15th. All right, let's talk text files. Joining me now, John Gruber, who you've been on the show many times but never as the inventor of Markdown. Welcome to The Vergecast.

**John Gruber** [04:14]: [laughs] Yes. And finally, I'm here for the thing that will go on my tombstone.

**Host** [04:18]: [laughs] I think that's right, and, and we're gonna talk about that. Also here, Anil Dash. You did not invent Markdown, but you've used it once or twice.

**Anil Dash** [04:26]: I got a front row seat when it was created.

**Host** [04:27]: That's exactly right. Um, so I think, i- strangely, I wanna talk about a very long time ago, and I wanna talk about right now, and those are sort of the two Markdown stories that I'm, I'm particularly fascinated by. But for folks who don't know the origin story, John, let's go all the way back, uh, to, like-

**John Gruber** [04:43]: [laughs]

**Host** [04:43]: ... the early aughts and, and sort of baby blogger John Gruber. Uh, tell us just the brief story of where Markdown came from.

**John Gruber** [04:50]: I went to college in the '90s. I have a computer science degree and graduated in '96, and then was doing freelance graphic design work rather than programming. But with a background in programming and being that age and being a graphic designer, what did I do? I built websites, right? It was sort of the perfect confluence of skills and interests. At least then, knew HTML. [laughs] Um-

**Host** [05:13]: [laughs] Sure. It was a lot easier then.

**John Gruber** [05:15]: And had, you know, it, it gets s- it's intertwined with the what's the origins of Daring Fireball. But I had this inkling to start Daring Fireball like '98, '99, or something, you know, some kind of blog. 'Cause I wrote. I was a writer. Finally, t- August 2002 is when I started the site. Th- the, during the year of 2002, there was this, this is where Anil comes into play. There was the, well, what do I use? What's the CMS I'm going to use? Do I build my own, which I could have done, I still could do, or use one of the things that's out there? And at the ti- like, WordPress didn't exist yet. Um, and I probably wouldn't have used it anyway. But Movable Type just came out, like, the year before. Um-

**Host** [05:57]: Yeah.

**Anil Dash** [05:57]: It was sort of the year.

**Host** [05:58]: It kind of immediately took over the blogging world, right?

**John Gruber** [06:00]: Yeah.

**Host** [06:00]: Like, Movable Type at this time was sort of the one you choose if you're gonna choose one.

**John Gruber** [06:04]: Yeah.

**Host** [06:05]: Yeah.

**John Gruber** [06:05]: And I'd more or less ruled out every other option for a CMS.

**Host** [06:09]: Okay.

**John Gruber** [06:09]: And I was like, "I've gotta, I- I gotta build my own." And then Movable Type was, like, close enough, and it's like, ooh. And it's like I know that if I built my own, it would take 10 times longer than I thought it would. But that meant every single post that I wrote on Daring Fireball was written in HTML, and I'd paste HTML into the field for the body of the article. Within a year, I'd really gotten the shit to that. Uh-

**Host** [06:34]: [laughs] I can imagine, yeah.

**John Gruber** [06:36]: I just... You know, I knew it. It wasn't the fact that I didn't know it, it's that I didn't like writing it. And so I'd-

**Host** [06:41]: Mm

**John Gruber** [06:41]: ... had this series of scripts that was getting ever more complicated on my local machine, where I could write in, like, a proto-markdown and then turn it into HTML at the end, and then paste that into Movable Type.

**Host** [06:55]: Interesting.

**John Gruber** [06:56]: But it turns out I do a lot of editing after I post, you know? So having, uh, transferring to HTML and then all subsequent edits have to be in HTML. So I was like, "I need to write something like this." And then Dean Allen, uh, who's no longer with us, uh, at textism.com, came out with a thing called Textile, uh, on 2001, 2002?

**Host** [07:16]: Mm-hmm.

**John Gruber** [07:16]: I don't know.

**Host** [07:17]: Yeah.

**John Gruber** [07:17]: Somewhere before Markdown. And I thought about using Textile, and I didn't like it enough. [laughs] And, uh, one of Anil's colleagues at Six Apart, a guy named Brad Choate, um-

**Host** [07:29]: Mm-hmm

**John Gruber** [07:29]: ... did the Movable-

**Host** [07:29]: Six Apart was the company that made Movable Type, that content manager.

**John Gruber** [07:31]: Yes, from the company that made Movable Type, did the Textile plugin for Movable Type, and it was complicated 'cause the original was in PHP and needed to be in Perl for Movable Type. And I knew Brad, and I started sending Brad and Dean sort of suggestions 'cause they were changing some things. And then Dean said to me, this is very important, it was like a seminal moment. And I knew Dean, and he was really, really a fan of Daring Fireball, and I was a huge fan of Textism, huge influence on what Daring Fireball still is to this day. And Dean just wrote back to me and said something to the effect, I have the email somewhere, but it's something to the effect of, "These are great ideas, but you should just make your own thing." So then I made my own thing.

**Host** [08:09]: There are, like, two competing ideas about what Markdown was supposed to be, and one was like, "I wanna write something where I can easily type all the characters I need in order to make it readable to the computer." And there was another one that was like, "I wanna make something that is computer language, but that is readable to humans."

**John Gruber** [08:25]: No, that was an overriding goal, and I think truly differentiated Markdown from everything else in this sphere, was not focusing on the authorship and the type ability. Even though all the characters are ASCII characters, there's, you know... And I really thought about it, 'cause I'm so Mac-centric and it's easy to type, you know, certain chara- like option eight to get a real bullet character.

**Host** [08:49]: Mm-hmm.

**John Gruber** [08:50]: There's a bunch of easily typed Unicode characters that I thought about putting in the syntax, um, and I was like, "Nah, I should just stick to the ASCII ones." But the readability was more important to me than the writability, that it should be that m- maybe the overriding goal of it is you should be able to print it out in Markdown format and hand it to somebody who's never heard of Markdown, never used a command line, and they can just read it, and they would totally understand what you mean. That they'd, they'd pick that up very quickly. Like, "Oh, I get it. These are the words you think are italics."

**Host** [09:22]: Yeah.

**John Gruber** [09:22]: The readability was more important. And it was, uh, A, I thought that was missing in all the other ones, and B, it just f- it, it was driven by the fact that the whole reason I wanted to make it is that HTML was so hard to edit, right?

**Host** [09:35]: Mm-hmm.

**John Gruber** [09:35]: And it's like once I had it written, it's like optimizing for readability. You read something over and over again. You only type the characters once. Um, I-

**Host** [09:44]: [laughs] Fair.

**Anil Dash** [09:44]: Yeah. I think it's one of the most important reasons it took off, right? So, um, to, to sort of John's point, we, we'd made this tool, you know, Movable Type, that was being used by, you know, at that time, Gawker and Huffington Post, like all, all of the big blogs, right? And none of those folks liked HTML. Like, so you had like two or three people in the office who were like, they, they really knew HTML, and everybody else was kind of like enduring it. And, and when we talk about, like, literally to put a image in a post, right? So they'd be writing about like, you know, Britney Spears was caught at this club doing this, like, which was like half the stories on Gawker at the time.

**Host** [10:22]: Yeah.

**Anil Dash** [10:22]: And then to put in an image, they're like, "This is miserable."

**Host** [10:25]: [laughs]

**Anil Dash** [10:26]: And, and then what was really important too was like when they wrote the post in Markdown, the other person didn't even have to know it was Markdown, right? It was literally-

**Host** [10:34]: Right

**Anil Dash** [10:34]: ... what they would've written in an email. And like that-

**Host** [10:36]: Mm

**Anil Dash** [10:36]: ... like they said that explicitly. They're like, "Oh, this is like normal, and like we don't feel like nerds when we see this." And so that became the default. And, and that actually was different than Textile. Like I really, I, just like John-

**Host** [10:47]: Yeah

**Anil Dash** [10:48]: ... like all of us were such huge fans of Dean. Like, he, he was just one of those super influential early folks that, um, you know, we were all just like kind of in awe of him, like he could do it all right, and code, and whatever. And, and so like I wanted like to be... Like I did a bunch of posts in Textile 'cause I was like, "I wanna be like Dean," you know? And then I was like, but it doesn't, [laughs] it just doesn't, like it's not how people write, you know? And, and so w- well, I got to see, so I was in charge of people making plugins, basically. And so like we were trying to launch, when you make a platform, you want people to make plugins, and we were really the first tool that had plugins. And so it was like a dream to be like, here's John, and everybody already loved Daring Fireball. Here's John making this thing, and here's Dean make, you know, a version of Dean's thing. And so you're like, what, like what an embarrassment of riches to have these things that people actually wanna use. But it was not even close right out of the gate that people were just using Markdown because they could type something that looked like what they were already writing. They were kind of like, "I already know this one," or at least I know two-thirds of it. And, and then they told us explicitly, like, "This works like I work."

**Host** [11:50]: So I-

**Anil Dash** [11:50]: Uh

**Host** [11:50]: ... Anil, I do wanna know about the John being John part of this.

**Anil Dash** [11:53]: Mm-hmm.

**Host** [11:53]: 'Cause I went back and found, John, the first post you wrote, uh, basically sort of, uh, launching Markdown to the world. And, and it just starts with, "I've written a tech stack HTML formatting tool called Markdown, which is now available for download," which gives real, like, open AI saying ChatGPT-

**Anil Dash** [12:08]: [laughs]

**Host** [12:08]: ... is a research preview vibes. [laughs]

**Anil Dash** [12:10]: [laughs]

**Host** [12:10]: It's like, "Hi, I've done this thing that is going to become utterly ubiquitous on the internet. Uh, so here it is. You can have it, I guess." Um, but Anil, do you, do you remember this as like, w- was this like a seismic moment on the internet, like John Gruber has made a m- a markup language?

**Anil Dash** [12:24]: Uh, no, but it didn't have to be, right? So I think it's hard to explain how different, like- It, what we used to call it, the blogosphere. Like, how different blogs were in social media world there. Like, there was a sense that everybody read every blog every day then.

**John Gruber** [12:38]: [laughs]

**Anil Dash** [12:38]: And, like, that sounds... Right? And, like, that sounds like an insane thing to say, but, but I think there was a couple things that were different. One, like, people had RSS readers, so you could kind of keep a track of a lot of stuff. And not everybody updated every day, so you just could see all the updates. It was kind of like, you know, if you had... Like, when everybody... Like, when Twitter was still Twitter and you could kind of read all the updates from everybody at a time. And, and I think the other thing was there was a, a tool that a, a researcher named Cameron Marlowe had made called Blogdex, and, and links would float up to the top when they were popular. And so even if you weren't... Like, if somebody had not been a regular reader of John's blog, if a bunch of people had linked to his post-

**John Gruber** [13:13]: Mm

**Anil Dash** [13:13]: ... it would sort of surface up. And there would only be 10 or 15, maybe 20 links that were popular in a day across all blogs. And also, I think another thing that's really kind of impossible to, to imagine, there was not that much going on in tech, right? Like, there wasn't, like-

**John Gruber** [13:29]: Sure

**Anil Dash** [13:29]: ... here's 50 new phones and d- you know, s- cameras and whatever launching every day. Like, it was just, like, the things that normal people made who were, like, good hackers was the most interesting things going on in tech. And, you know, that was the other reason that you were following what an individual developer was making, is it was way cooler... I mean, 'cause again, like you were talking about, like, what is Yahoo doing? You know, what is Cisco doing? Like, there was no way that was cooler than what John was doing. But the other thing with it, and you'll hit on, was the, the stuff in tech that was going on was blogging itself, and so that's what we wrote about. And it sounds navel-gazy, but it wasn't, 'cause it really was some of the most interesting stuff going on. The spirit of everybody was building building blocks for everybody else, right? And, like, that's-

**John Gruber** [14:16]: Yeah

**Anil Dash** [14:16]: ... very, very different than the environment now. Everything was open. Like, so almost everything everybody was assuming was gonna be open source was gonna be, you know, sort of cloned and copied. I think the only thing that kind of has that feeling these days is maybe, like, MCP, right? Where people are building things that are kind of interoperable between each other. And, you know, when we say blogs, like, it sounds very sort of, like, retrograde, but it, it, it is a super set of everything we consider social media today, right? So everything that would be Instagram and everything that would be TikTok and everything that would be WordPress. But, like, all those things together would all be under this heading. And also when people were building a fundamental component, yeah, it could be Markdown, but also somebody might be inventing podcasting, right, at this time, and somebody might be, you know, inventing... Like, so fundamental formats were things that an individual person was capable of creating in a way that would spread that now to what? Like, a billion users, right?

**John Gruber** [15:05]: Yeah.

**Anil Dash** [15:05]: So, like, the kinds of things that sort of are... So, so that thing that, like, a guy, and, you know, John's a remarkable guy, but, like, a guy can make a thing, and then you could imagine... Like, I think we could extrapolate maybe m- m- millions of people might use it. I don't think we'd be like, "A billion people are gonna use this."

**John Gruber** [15:22]: Maybe.

**Anil Dash** [15:22]: But, but, yeah. But you couldn't... It wasn't ridiculous at all to be like, "I might make a thing and a couple million people might use it." And so, like, that's so unfathomable, I think, in the current era. But it was intuitive at that sense that that might, you know, at that stage, that that might happen. So I think that was, that was such a addictive, you know, feeling when you were creating things.

**John Gruber** [15:42]: Yeah. [upbeat jingle] So okay, so let's, let's jump ahead a bunch here, because I think, like, fairly quickly, Markdown becomes sort of ubiquitous. Um, I am curious if-

**Anil Dash** [15:55]: I'm gonna disagree there. I-

**John Gruber** [15:56]: Oh, really? Okay

**Anil Dash** [15:57]: ... it was a years... It, it actually-

**John Gruber** [15:58]: It was a slow burn for a while. Okay

**Anil Dash** [16:00]: ... it, it actually took off in from 2004 to, like, twen- 2010, was very slow and actually very disappointing to me. Uh-

**John Gruber** [16:08]: Oh, okay

**Anil Dash** [16:08]: ... like, I thought, I, I'm, like, convinced. I was like, "This is the fucking shit." I'm like, "I can't go back." I, like, "I can't believe more people aren't using this." And then it did-

**John Gruber** [16:18]: It just-

**Anil Dash** [16:18]: I noticed, it just slowly grew

**John Gruber** [16:20]: ... I, I have a concrete example.

**Anil Dash** [16:22]: So we did, you know, Stack Overflow. I, I, I knew the founding team and I was on the, on the board, and Stack launched in '08, I think. And it was controversial that it supported, uh, Markdown.

**John Gruber** [16:33]: Mm.

**Anil Dash** [16:33]: Right?

**John Gruber** [16:33]: Yeah.

**Anil Dash** [16:33]: 'Cause it was, like, really... That there was a really strong argument, and I think Jeff Atwood, one of the co-founders, had been like, "We should do Markdown so they can do fancy formatted answers on..." You know, so, and Stack Overflow is the most popular, uh, you know, community for coders to answer each other's questions. But-

**John Gruber** [16:46]: A group of people who in theory would love to write in Markdown.

**Anil Dash** [16:48]: And they're all coders.

**John Gruber** [16:49]: Yeah.

**Anil Dash** [16:49]: Right?

**John Gruber** [16:50]: Yeah.

**Anil Dash** [16:50]: And, and so, like, they should know this thing, and it's really easy, and they might wanna use HTML in their answers and all these kinds of things. So it seemed like a straight down the middle, you know, uh, suggestion. And still there was a lot of debate. Well, are, are people gonna know, or are they gonna, are they gonna do too, do too much HTML? Like, all these kinds of things. And of course, like, it ended up being wildly popular. People used it all the time, but it was still a controversial thing. And then, you know, I think GitHub was the year after.

**John Gruber** [17:13]: Yeah.

**Anil Dash** [17:13]: And it was also the same thing, where, like, it was not a gimme that they-

**John Gruber** [17:17]: Yeah

**Anil Dash** [17:17]: ... were gonna do it. And then of course, both of those sites ended up adding, you know, other flavors or whatever extensions to it and all those kinds of things.

**John Gruber** [17:24]: Yeah, but GitHub, GitHub was a huge one.

**Anil Dash** [17:26]: Yeah.

**John Gruber** [17:26]: It was like a, a step change.

**Anil Dash** [17:27]: Inflection point.

**John Gruber** [17:28]: Yeah, because, and because they kind of said, "Hey, if you're using GitHub and you're gonna write something in text, it's gonna be in GitHub flavored Markdown."

**Anil Dash** [17:35]: Yeah, wow.

**John Gruber** [17:35]: "And whether you like it or not," and they didn't really ask opinions. And then that kind of forced i- uh, the technical-minded people, who I think just basically had the mindset of, "I know HTML. I don't need a baby language in front of HTML."

**Anil Dash** [17:50]: Right.

**John Gruber** [17:50]: Right? And they don't, right? I didn't either. It's not that you need it. It's that once you start using it, you're not gonna wanna go back. It really is one of those things where you have to use it for a while before you see the appeal. Whereas before you use it and you see this is the Markdown and this is the HTML that it will generate, you're like, "Yeah, I get it, but I don't need that. I could just write the HTML." But then you start using it, and you're like, "Oh, I can never go back." And that's what GitHub kind of did, and it made... It put it in the heads of technical people, and then they became the, uh, what do you call it? The, the evangelists for it. Yeah. So but John, that, that turn you just described where the technical people get into it, start using it, love it, and become the evangelists, uh-

**Host** [18:33]: Takes a really sort of weird, unexpected turn, and I think I went back and found a, a blog post you wrote almost exactly a year ago-

**John Gruber** [18:40]: [laughs]

**Host** [18:40]: ... when Apple Notes got Markdown support. Um, and this, I think, one of the questions I was gonna ask you is, like, what is the moment where you're like, you know, "Hey, look, Ma, I made it." Like, we did... I feel like I don't know how you beat Apple Notes now lets you write in Markdown for, for your particular version of-

**John Gruber** [18:55]: No, it doesn't really let you write in Markdown. Uh, and I don't think it should.

**Host** [18:58]: In a way.

**John Gruber** [18:58]: That's the thing. I'm, I'm now... I've gone from there's, like, the three stages of Markdown. For me, the creator of Markdown, is this er- there's a third of it, of its life at this point where I really felt like it wasn't popular enough. Then there's a, the middle third, where I'm like, "Ah, finally." It's like the people who should be using Markdown are using it, and it's in the places where it should be available. This is great. But the last third of its life has been the-

**Host** [19:24]: [laughs]

**John Gruber** [19:24]: ... I'm putting... I, I'm like, "Where's the brake? This is too much."

**Host** [19:28]: [laughs]

**John Gruber** [19:28]: These, this is-

**Host** [19:28]: Right

**John Gruber** [19:28]: ... being exposed to people who should have a WYSIWYG thing in front of them. This is-

**Host** [19:33]: Yeah, okay, so that, this is, this is what I'm getting at, and I think-

**John Gruber** [19:36]: Right

**Host** [19:36]: ... maybe Google Docs is a cleaner example of, like, you can-

**John Gruber** [19:38]: Oh, God

**Host** [19:38]: ... you can write a Google doc in Markdown now.

**John Gruber** [19:40]: It, it is horrible.

**Host** [19:40]: Uh, it's weird and bad, and I don't suggest doing it, but you can do it. But simultaneously, this thing has happened where a bunch of, a bunch of companies have said, rather than pure WYSIWYG, like, you, you, you, you press the button to make it bold, we're gonna let you do the carets to make it, or we're gonna let you do the asterisks to make it bold. But also, Markdown editor has become a thing and, and there's, there was this-

**John Gruber** [20:02]: Yeah

**Host** [20:02]: ... whole slew of new text editing documents where it was like, actually, the whole point is to expose the formatting structure in front of people. And I, I sort of see the idea behind that. Like, I, I use Obsidian, which is one of the better-known market Markdown editors, for everything, and their whole idea is this stuff should be readable by lots of apps. We wanna build files that aren't proprietary. Like, I get all of it. I feel like there's something about that that would drive you in particular just completely insane.

**John Gruber** [20:27]: [laughs]

**Host** [20:29]: That, like, this just, just not what Markdown was supposed to be.

**John Gruber** [20:32]: Yeah, basically.

**Host** [20:33]: [laughs]

**John Gruber** [20:33]: I mean, I like it a- and there's a fine line between it, right? Like, and, and for example, I, when I made Markdown, there was no syntax coloring for it, right?

**Host** [20:42]: Mm.

**John Gruber** [20:42]: It, it was meant to be self-evident in a text editor with no syntax coloring, just the asterisks and the brackets and the braces. They, they all speak for themselves, and it still kinda does work that way. But then with syntax coloring, it's a little better, and with syntax styling, it's even better. Like, it's nice when your editor actually does italicize the text between the asterisks.

**Host** [21:09]: Sure.

**John Gruber** [21:09]: That's... It's nice. But it still is a monospaced font, and you delete the asterisks, and it deletes the italics. There's a line that gets crossed where it's more of a fundamentally WYSIWYG product, and yet you're typing these characters, but then there's, like, a view mode and an edit mode, and the view mode makes them go away.

**Host** [21:29]: [laughs]

**John Gruber** [21:29]: And it's like, no, you've, that, you've-

**Host** [21:31]: Yeah

**John Gruber** [21:31]: ... you've gone too far, and that's-

**Host** [21:33]: Yep

**John Gruber** [21:33]: ... you're exact- Now it's exactly the sort of product that Markdown... The other thing Markdown was meant as an answer to was in addition to writing raw HTML, there were the pre-Markdown WYSIWYG HTML editors, and they were, they sounded great, right? It's like, oh, it just, you just hit Command + I, and you get italics text. But the problem was how do you, you go back to the end of an italicized word, and you wanna add a word, but no, I don't want it to be italics anymore. I want the italics to end. What do I do? Where's the thing?

**Host** [22:01]: [laughs]

**John Gruber** [22:02]: And that's where having little punctuation characters that you can just delete, either it's there or it's not, and you delete it, and then the italics stops. So I think what Apple did with Apple Notes is actually great, where they didn't turn it into a WYSI- a, a Markdown editor where you type Markdown, but what they've done is let you copy Markdown out or export as Markdown, which is great. Um, I think that's actually very appropriate for Apple Notes. I'm now the, like I said, the put the brakes on this. Don't expose it to people. People should have... The Apple Notes app should just be WYSIWYG, where you just say italics, header, and it's an actual menu item.

**Host** [22:37]: Anil, what do you think of that?

**Anil Dash** [22:38]: Uh, you know, I, I wanna pick whatever torments John the most. You know?

**Host** [22:42]: I got that. [laughs]

**Anil Dash** [22:42]: Like, I think, like-

**John Gruber** [22:43]: I support this

**Anil Dash** [22:43]: ... the punishment that he deserves.

**Host** [22:45]: [laughs]

**Anil Dash** [22:45]: So, like, the, the thing John was talking about, like, the early, um, you know, uh, visual HTML editors, those were all, like, the web version of, like, you know, Microsoft Word. You move the image, and the whole document blows up. Like, they were doing the same thing-

**Host** [22:57]: [laughs]

**Anil Dash** [22:58]: ... on the web, and so this was sort of the solution to that. Uh, but, but I, I think, you know, in- intrinsically, like, a good design is one that precludes people from being able to do the worst things. Like, it sort of saves them from that, like, the, the most nightmarish, you know, situation, and I, I think that's one of the reasons that, that Markdown has sort of persevered. Like, it's really hard, even with all the different flavors and variants and whatever, to make a Markdown document that doesn't just ultimately work.

**Host** [23:24]: Well, I go back and forth on this because I think philosophically, there's an argument to be made that just everyone should learn Markdown because, A, it's not that hard.

**Anil Dash** [23:33]: Teach it in schools. [laughs]

**Host** [23:34]: And B, it solves, it solves a certain set of problems, right? Like, the... I, I just, I am forever struck by the number of people who still don't know the keyboard shortcuts for copy and paste, right? And like-

**Anil Dash** [23:42]: Wow

**Host** [23:42]: ... it is, it is undeniably faster to write Markdown than to go looking for the italics button every time you need the italics button. So to me, it's like I... There, there's an argument to be made that actually what you invented is the most efficient way to do it, even more efficient than WYSIWYG, and there are still a lot of really broken WYSIWYG editors out there.

**Anil Dash** [24:01]: Yeah.

**John Gruber** [24:01]: Mm.

**Host** [24:01]: Um, the other part of me is like, well, actually everybody should just fix their stupid WYSIWYG editors. [laughs] And this is, this is not a problem that should exist at all. But I am, like... I, I don't know, John. Do you have a, a sort of aversion to the idea of this being, like, a, a language people, that, like, everyday people should learn and know? Does that feel like a bridge too far to you?

**John Gruber** [24:21]: No, but I don't think it should be required, right? And, and the thing-

**Host** [24:26]: Okay

**John Gruber** [24:26]: ... that I'm proudest of and the thing that I think I've been proven right about, and it skips over some controversy in the middle, is I've never seen it. Like, I'm the creator of what I would consider the canonical Markdown, or I don't know what you wanna call it, but, like, the official... And I don't, I, I stopped dicking around with it. I don't add new features. I'm not saying I never will, but I haven't, and- Decades. The- I think a lot of other people, if, if they saw it as a more of a technical thing, they would b- have been offended by all the various flavors that came out. But I- Mm ... have always been of the opinion, let a thousand markdowns bloom, and that it's not a syntax or a language per se, but a convention for writing plain text. It's taking the con- you know, plain text is the technical standard, and there were a bunch of conventions, and the thing that I'm happiest about isn't that Markdown particularly is so popular, it's that the various 100 different ways of i- i- i- italicizing something in plain text, I had strong opinions about those since like the early '90s, and I thought everybody should do it my way and use the asterisks. And then I thought the second-best way is the underscores. But all the other ways, people would use the tildes for that. People would use- Mm ... slashes for italics, and I'm like, "I wish people would do it my way." And that's really what Markdown has done, is that everybody now, when they decorate plain text, they do it my way. [laughs] And it's, it's a convention- That's gotta feel good ... more than a syntax. Yeah. And all of the popular flavors of Markdown all follow the main conventions. I had to write the original, it's not even a parser, but the original series of regular expressions that turns Markdown into HTML, and I was ruthless on myself by only making it what I wanted to see and write, no matter how hard it was for me to make it the conversion. It, but really ultimately, it's, it's a convention or a series of conventions for how you do things, and those conventions are like everywhere now. I, and I love it. But that's the thing. And it- That's, that's all we ever have, right? The spec is like ego, right? The web is just a bunch of things we're hoping works this way. Nobody ever follows a spec. Right? The, the web is all- Yeah ... just a bunch of things we slap together, and like this is the thing- Yeah. [laughs] ... that works the way people work. Yeah. And, and recognized that from the beginning, so you never had the ego to pretend, "Oh, I'm gonna write this technical spec-" Yes ... "and everybody's gonna follow it." Right. You're like, "I hope they like the way I use things, and maybe we will all do it this way." Right. And I think the fact that it worked the way people work is why it took off. Yeah. Yeah. I love that. All right. Real quick, since w- we all have to go here, I'm curious how it feels then that that kind of convention and that, that sort of the thing you built is now the like official language of every AI tool everywhere on Earth. Like, this is the most mainstream in a certain way that Markdown files have ever been, right? People are out here writing .cloud.md files for themselves all the time. Yeah. Uh, I guess, A, did you get a phone call about this? [laughs] And B, uh, how do we, how do we feel about this sort of next turn in the Markdown story? No phone call, and, uh, unfortunately no royalty check. Um. [laughs] That's, that may be the real bummer here. [laughs] Yeah. Uh, I guess I'm... It, it's, it's like, ugh, it's surprising, and I get... A- and, and I'll get more once this episode comes out, sure, and I welcome it. I do. I've gotten hundreds, hundreds of emails and DMs, uh, over the last, especially the last six months or so, from people saying exactly what you just said there, David. Like, how does it feel that it's like the lingua franca of like this huge, new, groundbreaking, breakthrough technology? Weird, a little gratifying, and while I don't profess to be an expert on LLMs, I understand them well enough that I'm not surprised because they're pattern matching and pattern predicting based on a corpus of, at least in their, their ability to emit Markdown. Forget about image and video generation. But a corpus of text that was produced for humans to read. So LLMs consume text, uh, trying to match patterns the way humans do. And so the fact, going back to your question, that I tried to... My number one priority for Markdown was to make it readable, is that it is... And readable to someone who doesn't even know the, what Markdown is, is exactly how LLMs parse text. Like, that they can parse noisily written text. Somebody can just- Mm ... bang away in a Facebook text input field that doesn't support anything like formatting and just use weird punctuation characters to sort of under- fake underlines or something, and LLMs will parse that. Well, that's what Markdown is. So of course LLMs really like it, and they like sending it too because it's lightweight and fast, and it's like just little characters. It's not complicated. So for example, um, they do... Somebody did some studies. They're, it's much better at, at... LLMs, I think, to this day, are still better at emitting Markdown than they are at JSON because JSON has very persnickety rules. Mm. Yeah. Like a JSON file, you get a character wrong, and then the whole file is bad. Right. Markdown, if you forget to end an italics run, who gives a crap, right? Yeah. [laughs] Yeah. Yeah. Doesn't matter. Yeah. So what? It's still good. And so LLMs making one little tiny mistake or something in the Markdown they, they admit, it's still fine, right? So that forgiving nature that is forgiving for humans also works for LLMs. Yeah. But it is, it's, it's kind of amazing because I'd certainly never envisioned it. I just wanted to blog and to have a good format for my writing really. Totally. Yeah, Anil- I'm, I'm less forgiving than John. I think Sam Altman should send John $100 million. [laughs] Yeah, just give or take. I couldn't agree more. But I am, I am real, I am curious real quick, Anil, before we have to go here, is, i- i... Does this feel like a good direction for like technology and the web that Markdown is becoming ever more ubiquitous this way? I, I think so, especially because it's showing a new generation of creators and coders that what actually makes the web move forward is what individuals create, right? And I think the more they take that lesson away and they're like, "Oh, the guy who writes about Apple made this?" Right? And if they sort of get that lesson in the back of their head and hear these kinds of stories and they're like, "The thing that we all use wasn't made by one of these giant trillion-dollar companies," that is actually the most important thing that they can sort of learn from. And not just using the format, but like maybe they could make one of these specs too, one of these formats too. Um, I, I think that actually like being in the back of their head and be like, "How come I would never learn that?" Like, there will be people who got, you know, uh, the, the good degree from Stanford that were never taught where the format that they use comes from, and maybe that should raise some questions for them about the history they were told about how the whole industry works. That's a really good thing. Yeah, I love that. Yeah. All right, we gotta get out of here. Thank you both for being here. This is, this is very fun. Thank you. This is like, we could talk... We're, we're gonna come back and just like litigate which does one asterisk and which does two. [laughs] But that's, we'll do that another time. Thank you both for being here. All right, that's it for the show. Thank you to John and Anil for being here, and thank you as always for listening. As always, if you want to send us emails, you can always email us, vergecast@theverge.com. If you wanna call in with some questions or thoughts or feedback, 866-VERGE11 is the hotline. Find me on social. Find us anywhere on The Verge. We're not hard to get in touch with, and we absolutely love hearing from you about everything. Also, the best thing you can do to support all of this is to subscribe to The Verge, theverge.com/subscribe. It gets you ad-free versions of all of our podcasts, including this one. It gets you all of our exclusive newsletters, including my newsletter, Installer, which selfishly I think is very good. It gets you all of our coverage of Markdown and everything else. theverge.com/subscribe to make sure we get to keep doing all of this. Thank you to everybody who subscribes. We appreciate you. The Vergecast is a Verge production and part of the Vox Media podcast network. This show is produced by Eric Gomez, Brandon Kieffer, Travis Larchuk, and Erin Locascio. We will see you tomorrow. Rock and roll.

