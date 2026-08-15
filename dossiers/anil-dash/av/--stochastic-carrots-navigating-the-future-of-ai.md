---
title: "Stochastic Carrots - Navigating the Future of AI"
person: anil-dash
section: by
type: talk-transcript
year: n.d.
venue: ""
source_url: https://www.youtube.com/watch?v=rluq52kBdhc
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 140
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Stochastic Carrots - Navigating the Future of AI

*Speakers (inferred):* speaker_0=Host, speaker_1=Narrator, speaker_2=Paris Martineau, speaker_3=Jeff Jarvis

## Transcript
**Host** [00:00]: It's time for Intelligent Machines. Jeff Jarvis is here. Paris Martineau's back from vacation, and we've got one of my favorite people as a guest. A great thinker, moral philosophy- uh, philosopher and a startup guy, Anil Dash is our guest. We'll interview him, then talk about all the latest AI news. A big Intelligent Machines is coming up next.

**Narrator** [00:22]: [digital music] Podcasts you love.

**Paris Martineau** [00:24]: From people you trust.

**Narrator** [00:27]: This is Twit. [upbeat music]

**Host** [00:31]: This is Intelligent Machines, episode 828, recorded Wednesday July 16th, 2025. Stochastic Carrots. It's time for Intelligent Machines, the show where we cover the latest in AI, robotics, and all the smart little doodads and doohickeys surrounding us everywhere we turn. Uh, Paris Martineau is here. She's back from vacation. I got to have dinner with her-

**Paris Martineau** [00:57]: I am

**Host** [00:57]: ... though, while you were traveling on the West Coast.

**Paris Martineau** [00:58]: I got to see inside the famous studio that Leo is recording from right now, and meet his cat.

**Host** [01:04]: He met the cat?

**Paris Martineau** [01:05]: It was delightful.

**Host** [01:05]: Oh.

**Paris Martineau** [01:05]: I did meet the cat.

**Host** [01:06]: Yeah.

**Paris Martineau** [01:06]: She allowed me to pet her, and I felt, uh, so important because of it.

**Host** [01:11]: Paris took some time off before she starts a new job, which we can't talk about yet, but will.

**Paris Martineau** [01:16]: Yeah.

**Host** [01:17]: Maybe next week.

**Paris Martineau** [01:17]: We shall.

**Host** [01:18]: Next week.

**Paris Martineau** [01:19]: Next week. Indeed.

**Host** [01:20]: She's meeting with-

**Jeff Jarvis** [01:20]: She's going to the CIA, but let's-

**Host** [01:21]: Yeah

**Paris Martineau** [01:21]: ... I know. Shh

**Host** [01:22]: ... needless to say, it's an excellent job-

**Paris Martineau** [01:23]: Sorry, we're not allowed to m-

**Host** [01:24]: ... in National Intelligence

**Paris Martineau** [01:24]: ... we're not allowed to mention.

**Host** [01:25]: I mean, oh God.

**Paris Martineau** [01:26]: [laughs] Oh, Leo, come on.

**Host** [01:28]: Oh, I'm so sorry. Also with us [laughs] Mr. Jeff Jarvis, the, uh, Emeritus Professor of Journalistic Innovation at the Craig Newmark Graduate School of Journalism at the State-

**Narrator** [01:39]: [singing] Craig Newmark

**Paris Martineau** [01:41]: I love that we've bullied him-

**Host** [01:42]: Well-

**Paris Martineau** [01:42]: ... into bringing this back.

**Jeff Jarvis** [01:43]: Yeah, yeah.

**Host** [01:44]: No, there was a-

**Jeff Jarvis** [01:45]: City University

**Host** [01:46]: ... it's just for that sake. That's, that's the joy of it.

**Jeff Jarvis** [01:48]: Yeah.

**Paris Martineau** [01:48]: It really is, yeah.

**Host** [01:49]: He is now at Montclair State University in New Jersey, [laughs] which is not a step down. It might sound it, but it's not.

**Jeff Jarvis** [01:57]: No, it's not.

**Host** [01:57]: He's also-

**Jeff Jarvis** [01:58]: He's not

**Host** [01:58]: ... he's also professing at the State University of New York's Stony Brook.

**Jeff Jarvis** [02:03]: Hello, boss.

**Host** [02:04]: Nice to see you all.

**Jeff Jarvis** [02:05]: Good to see you.

**Host** [02:06]: And the author of many books, of which you will see over his left shoulder, The Web We Weave being the latest, although the magazine's now out.

**Jeff Jarvis** [02:13]: Now an audiobook.

**Host** [02:14]: You know, at Audible.com-

**Jeff Jarvis** [02:16]: Great

**Host** [02:16]: ... and other fine audio. I am... Actually, don't wanna promote Audible anymore. I'm gonna promote Libro.fm.

**Jeff Jarvis** [02:22]: They were, they were a fine early sponsor.

**Paris Martineau** [02:23]: I would also recommend Libby, where you can listen to audiobooks-

**Host** [02:27]: And Libby for your favorite library

**Paris Martineau** [02:27]: ... from your library.

**Host** [02:29]: Yeah. Libro's nice 'cause it gives, uh, uh, 10% of your purchase or your subscription, 15% of your purchase, 10% of your subscription to your local bookstore. And our local bookstore, uh, as many independent bookstores do, is suffering right now. They're closing their used book section. It's, it's sad because Jeff took me to The Strand in New York City, and what a great used book section-

**Jeff Jarvis** [02:51]: Oh, that's right. Yeah

**Host** [02:53]: ... that has. Uh, and ours was similar, but gone, and, uh, they're even shutting down part of the store, so it's very sad.

**Jeff Jarvis** [02:58]: Ooh.

**Host** [02:58]: Yeah. So I'm g- I- I'm glad that I can spend the same amount of money that I spent with Audible and, and give it, some of it, to my local bookstore. So let's introduce our guest, who is a longtime friend of the show. Uh, he used to be, uh, Gina Trapani's boss. [laughs]

**Jeff Jarvis** [03:13]: Well, she was my boss.

**Host** [03:15]: [laughs] Oh, okay.

**Paris Martineau** [03:16]: She was all of our bosses in some sense.

**Host** [03:18]: Okay.

**Jeff Jarvis** [03:18]: Be his boss.

**Host** [03:19]: Anil Dash is, uh, here. Uh, I... You know, he's recently, uh, left his regular job and-

**Jeff Jarvis** [03:27]: Mm-hmm

**Host** [03:28]: ... he was a... You started a company called Glitch.

**Jeff Jarvis** [03:29]: Mm-hmm.

**Host** [03:29]: I think Gina worked with you at Glitch, right?

**Jeff Jarvis** [03:31]: Uh, n- actually, no. She, she was always an advisor. But, but, uh-

**Host** [03:34]: Okay

**Jeff Jarvis** [03:34]: ... uh, we had done a startup together, ThinkUp, and then right after that, uh, I got to, uh, work with the team at Glitch, which was a, uh, a community for building apps that got acquired by, uh, Fastly, the infrastructure company. Uh, and then after a couple years there, yeah, I just left, uh, last month, um, to, uh, figure out what I'm doing next.

**Host** [03:52]: Isn't that nice, though, to be able to spend time with friends and family and... Do you have kids?

**Jeff Jarvis** [03:56]: It is.

**Paris Martineau** [03:56]: And Mario Kart.

**Host** [03:57]: I do, I do. We got-

**Paris Martineau** [03:57]: And the new Mario Kart-

**Host** [03:58]: And Mario Kart [laughs]

**Paris Martineau** [03:58]: ... as you mentioned in your blog.

**Jeff Jarvis** [04:00]: That's right. Um, yeah, no, we got a 14-year-old-

**Paris Martineau** [04:02]: Important

**Jeff Jarvis** [04:02]: ... and, and this is really the first time I've, like, taken a break since... actually, since before Gina and I did our company together. So it's, it's been-

**Host** [04:08]: That's kind of a key time too, 14. You're... It's nice that-

**Jeff Jarvis** [04:11]: Yes

**Host** [04:11]: ... you can spend some time.

**Jeff Jarvis** [04:12]: What are, what are you thinking, Anil? What, what kind of vision do you have for yourself? It's, it's genuinely open. I mean, I, I think, you know, uh, before we, we sort of, you know, got online here, Jeff, you and I were talking about sort of knowing each other for 25 years, and I think, you know, this is one of those fertile moments that feels like back at the beginning of social media and blogging, and we're at, you know, certainly that in- kind of inflection point with AI. But it's a little different in that I think in those days it was very kind of bottoms up, like people were hacking together and building stuff, and this right now feels like people are trying to be sort of top down, like the-

**Host** [04:44]: Mm-hmm

**Jeff Jarvis** [04:44]: ... the money guys are trying to tell us, "This is what it's going to be," and I'm sort of curious to see what the, the hackers and the makers are building from the bottom up.

**Host** [04:51]: Amen.

**Jeff Jarvis** [04:51]: So that, that's really what I'm spending time doing, is, like, listening to the people who are the coders and the creators and the writers and what do they say is cool.

**Host** [04:59]: Do you think you'll end up in a, some sort of AI thing?

**Jeff Jarvis** [05:02]: I... You know, I don't know, genuinely. I, I think, um, I'm... You know, I look at somebody like, um... One of the people I, I, I've always respected is, like, Simon Willison, you know, who's one of those, like, brilliant coders who just is every day out there writing code and writing on his blog. And I like, "Who are the people like that who are..." And, you know, he's, he's like my age. I'm like, "Who is the next generation version of that that's making something?" So just having the time to go out there and read and discover somebody who is new and doesn't have a, you know, agenda and is not, like, connected into the industry and what are they saying is cool that they're just hacking on for the love of it. Like, there's-

**Host** [05:39]: Yeah

**Jeff Jarvis** [05:39]: ... always somebody making stuff because they're, they think it's cool and they think it's interesting, and not because, uh, you know, somebody has said, "This is what we need you to build a business around." Like, I, I just have always loved the people that make that stuff, and I think that's how we all connected, you know, many years ago, was just working on whatever was next and interesting. And, and so, um, it's gotten harder, I think, to find those folks. There used to be much more places where you would just see what was kind of, you know, buzzy- Um, organically. And-

**speaker_4** [06:07]: This is gonna sound stupid

**Jeff Jarvis** [06:08]: ... we can talk

**speaker_4** [06:08]: That's what I specialize in.

**Jeff Jarvis** [06:10]: [laughs]

**speaker_4** [06:10]: But does vibe coding open the door to that? Does it open the cha- people can make-

**Jeff Jarvis** [06:16]: Yeah

**speaker_4** [06:16]: ... things they couldn't make before? Is that possible?

**Jeff Jarvis** [06:18]: Yeah. I don't think that's stupid at all. I mean, I, I think in some ways, right? I think, I think definitely I'm always in favor of anything that democratizes access, right? Anything that makes it easier, I think is great. And, and, and again, not to like... Like, I don't- I'm not one of those good old days people, but I definitely think one of the things about, like, the early days of blogging is it made it easier to put things online for a lot of people. Like, you could write, and now you could write and put it online. And, and for some people, I think their experience of vibe coding is that thing where it's like, it got really hard for a long time to, even if you knew how to code, to do all the other steps to get your code onto a website [laughs] or onto an app was, like, really hard. And so, like, vibe coding can bring that barrier down. But some of what people are saying vibe coding can do ain't necessarily so, right? Like they're sort of over-

**speaker_4** [07:02]: Yeah

**Jeff Jarvis** [07:02]: ... promising of what it can do. So I think I'm, I'm a little-

**Host** [07:05]: Like what?

**Jeff Jarvis** [07:05]: ... you know, trepidatious about some of the promises, but the spirit of can we make these tools easier enough that somebody who has either fallen out of practice of coding or is not totally fluent in it can get the, the bar lowered or the gatekeepers out of the way to where they can make something on their own that before would've just been an idea, I think that's awesome. And, and if somebody feels empowered by that, I'm, yeah, I'm all over that.

**Host** [07:31]: People may not know what a great blogger and writer you are. I, I, uh, I, I've always thought of you... Uh, this is what we need. People like you, Simon Willison, Om Malik, who are both-

**Jeff Jarvis** [07:42]: Mm-hmm

**Host** [07:42]: ... technical, who are i- you know, im- enmeshed in the, in the, the industry, but also can really communicate and write. And you, you've always-

**Jeff Jarvis** [07:51]: Mm

**Host** [07:51]: ... been that way, which in fact makes you, uh, you know, one of the thought leaders in this, because so few [laughs] people can express themselves-

**Jeff Jarvis** [07:58]: Appreciate that

**Host** [07:59]: ... let alone have deep thoughts. So, uh, I've, uh, you know, one of the reasons I wanted to get you on the show is 'cause you've been writing a lot about, uh, AI-

**Jeff Jarvis** [08:07]: Mm-hmm

**Host** [08:07]: ... of late.

**Jeff Jarvis** [08:07]: Yeah.

**Host** [08:08]: Um, what is your sense that... Uh, you know, for me, I feel like AI... [laughs] You should also read his blog for stories about Prince.

**Jeff Jarvis** [08:19]: [laughs]

**Host** [08:19]: Uh, and hey, good news, he's going to see Wu-Tang tonight for their last-

**Jeff Jarvis** [08:24]: Mm-hmm

**Host** [08:24]: ... performance. So-

**Jeff Jarvis** [08:25]: Yep

**Host** [08:25]: ... uh, not at the Hammerstein Ballroom, but at Madison Square Garden.

**Jeff Jarvis** [08:28]: Yep.

**Host** [08:28]: So you'll be there with a few Wu-Tang's friends.

**Jeff Jarvis** [08:32]: Mm-hmm.

**Host** [08:32]: Um-

**Jeff Jarvis** [08:32]: For sure.

**Host** [08:33]: Yeah, we'll talk about that in a little bit. But first [laughs]

**Jeff Jarvis** [08:35]: [laughs]

**Host** [08:36]: It seems to me that AI is one of the most exciting things, even though it's uncertain and, and the, and the end game is unknown, to happen in technology that I can remember, and I've been-

**Jeff Jarvis** [08:47]: Yeah

**Host** [08:48]: ... covering this for 50 years.

**Jeff Jarvis** [08:50]: Yeah. So I, I think there's, I, I think there's a couple parts. I think one of the things that's important to understand, talking about 50 years, there, there is a half century of computer science research and, and, and focus on things that we could call machine learning or AI, right? There's a long-

**Host** [09:05]: I know. I program in Common Lisp. [laughs]

**Jeff Jarvis** [09:07]: Right? Right?

**Host** [09:07]: I know all about it.

**Jeff Jarvis** [09:08]: And I think-

**Host** [09:09]: Yeah

**Jeff Jarvis** [09:09]: ... that's really important for people to understand is, like, this is not new, and anybody who tries to pred- like, present it as if this is the beginning of history is probably lying.

**Host** [09:17]: Right.

**Jeff Jarvis** [09:17]: Right? And I, I think about, like with, with Glitch, we had a, um, incredible, uh, leader and, and community, um, uh, you know, engineer, uh, leader, uh, Jen Schiffer, who sort of was our sort of voice of the community. And right, you know, before she had led our community at Glitch, she was a professor teaching computer science and teaching, you know, AI and machine learning. And so, like, t- that's a career that you could have a decade ago or two decades ago, and that's something that is not new. And so I think that's one of those key things is any time the conventional tech industry or Silicon Valley is sort of trying to get you to forget that there's a decade or two decades or five decades of history, they're trying to get over on you. [laughs] Like I think that's, like, a really key thing. And then the second part is, well, what can we learn from everything prior to LLMs that we can now apply to-

**Host** [10:07]: Hmm

**Jeff Jarvis** [10:07]: ... this domain? I think that's really, really key. And especially because LLMs have, uh, obviously incredible applications, incredible things they can do, things we could not do before. They're genuinely new in a lot of ways, and they have a lot of shortcomings. Like every other AI, you know, approach or every other model is not as prone to hallucination, for example, is not as dependent on gathering data without consent.

**Host** [10:33]: That's why Stephen Wolfram was... said, "Don't give up on symbolic AI."

**Jeff Jarvis** [10:37]: Oh, um, exactly. I, I think there's all these other, um, approaches. And so, so one of the things we have to ask is why is there such an, a focus and an overinvestment in this one approach? Why is this being treated as the be-all, end-all?

**Host** [10:52]: But don't you think transformers and LLMs were a ph- a phase change, were a huge-

**Jeff Jarvis** [10:58]: It is. It is-

**Host** [10:59]: I mean-

**Jeff Jarvis** [10:59]: ... a massive breakthrough.

**Host** [11:00]: Yeah.

**Jeff Jarvis** [11:00]: But, but I, I think about, um, again, I think we're probably a sufficient vintage to recall late '80s, early '90s-

**Host** [11:06]: I remember three distinct AI winters. [laughs]

**Jeff Jarvis** [11:09]: Yes.

**Host** [11:10]: That's why. [laughs]

**Jeff Jarvis** [11:11]: But, but take a, take an analogy outside of, of software entirely.

**Host** [11:14]: Okay.

**Jeff Jarvis** [11:14]: We had a, a, a inflection point in processing technology from-

**Host** [11:19]: Right

**Jeff Jarvis** [11:19]: ... complex instruction set to reduced instruction set.

**Host** [11:21]: Risks. Yeah.

**Jeff Jarvis** [11:22]: Cis to risk, right-

**Host** [11:23]: Yeah

**Jeff Jarvis** [11:23]: ... which was the, uh, Intel x- X86 to the kinda ARM-style processors, and this was a big debate for folks who weren't around then. There was a big debate. Like, you would have magazine covers back when magazines were a thing about is, is-

**Host** [11:34]: Mm-hmm. [laughs]

**Jeff Jarvis** [11:36]: ... you know, uh, you know, was Intel-style processors gonna win out, or were the, what, you know, came to be called ARM-style processors gonna win out? And people would debate and debate and debate, and then they're like, "Well, it's settled. Intel won. Windows and Intel won." This is what people would say around 2000 and the early 2000s, and, uh, ain't necessarily so, right? Now, here we are 20 years later, and ARM won everywhere, right? The Apple processors won, and everything's got an ARM chip in it. So the, the, the, the battle shifted, but, but the key thing was there was this ar- Argument about what kind of chip architecture would win, and people were ready to throw away an entire approach based on, like, what they thought was efficient or what would use more... They were like, "Oh, well, who cares about how much power it uses? Why would that matter?" Right? Like, who cares how much electricity a computer uses? Why would that ma- you know, be relevant to anybody? Not imagining everybody would have a computer in their pocket. And, and so, like, the, the, the foundations of what is relevant to the market or what's their... Like, the conventional wisdom can shift very quickly. And I, I draw that analogy because I think we're sort of at that point where the, um, you know, the LLMs are a phase change, and they are a breakthrough, and they are really important. And whenever anybody sort of says, "Throw away the prior 50 years of history," or, "Don't think about a yes and approach where we take more than one together," like, that's a, that's a thing that makes me skeptical, especially when the experts are sort of asking you to, you know, that, that, um, Wizard of Oz moment of, like, pay no attention to that man behind the curtain. If they're saying, "Don't pay attention to the fact that we indexed all this content without consent, and we don't care that the creators are upset," or, "Don't pay any attention to the real, uh, environmental impacts of the power that we're using or that there is this sort of cost," like, that's a real concern. That's a legitimate concern. That's a valid thing for people to be, you know, upset about or to, to reckon with. And so, like, that doesn't mean that we don't, like, appreciate what the technology can do. I think the fact that, like, there should be a complicated answer is key. And, and that's the thing that I sort of keep coming back to, is like, let's complicate the answer and, and balance it, and I see very little of that in the industry advocacy. I think the people like you all who are very thoughtful about these things I think are, are sort of reckoning with both parts to that. But I think a lot of the, the vendors who are selling this are, are sort of... They see any nuance as unacceptable levels of critique. And so that's where where I get... The hackers don't see it that way at all. I think hackers are like, "I want to know the pluses and minuses of the system so I can balance it against everything else that I'm using." And I would love to give them a, a menu of options. Like, have a whole palette of options. Like, not just, here's five different LLMs to choose from, but here's 50 different things, some of which are LLMs and some of which are other things, and how do we compose those all, assemble those all into as many different kinds of Lego blocks as possible.

**Host** [14:28]: What, uh, other uses of machine learning are in... can be as near in consumer usage in mind?

**Jeff Jarvis** [14:38]: Um, you know, I, I think there's a range. I think the, the... One of the things that... One of the reasons LLMs I think have captured everybody's imagination is the accessibility of-

**Host** [14:48]: Mm-hmm

**Jeff Jarvis** [14:48]: ... um, the chatbot model, right?

**Host** [14:50]: Yep, yep.

**Jeff Jarvis** [14:50]: I think people love the sort of feeling of like I'm typing this in. Um, but I think for hackers and builders, chat is a really inefficient interface. It's actually a terrible way to, to program or to build around. And so I think some of the other systems, the more conventional, um, machine learning systems, like if you're gonna build a spreadsheet, you can't build a, a formula around chatting to something, right? You want to say like, "What's this?" Like, I want to add a number. And if you want the AI to say... Like, go get a, you know, what's the price of this stock today, or what's the weather in this area today, um, that is a thing that, you know, many, uh, AI systems might be able to go retrieve for you in an intelligent way, but you don't want it to have a conversation when it [laughs] comes back, right? Like, you don't want it to be this sort of long, convoluted response. You want it to just give me the number. And I think that's the kind of thing that some of the other approaches might be more inclined to come back with. And especially you do not want it to hallucinate the answer, right? And so I think some of the other more conventional machine learning tools, um, might be better at that. Also, and actually this is something that, um, Simon Wilson is another one of these great examples, people have even done this with LLMs where they've built test systems where they sort of say, "Even if you're prone to hallucination, we're gonna run a software test against you and make sure the answer that comes back is something that's valid and is something that could plausibly be correct so that we know it wasn't a hallucination." And I think those things are really key because there's such a... The consumers who are not fluent in this stuff are so inclined to trust it, right? I think of, like, a really concrete example. My, my sister is a librarian, public librarian-

**Host** [16:33]: Oh, bless

**Jeff Jarvis** [16:33]: ... which I love and I'm very proud of her.

**speaker_5** [16:35]: Wow.

**Jeff Jarvis** [16:35]: Yeah. They do the most noble work. And you know, she talks about, like, the patrons of the library will Google, you know, the hours that the library's open, and it says, "Oh, you're open until 8:00 PM on Mondays," which they are not, and then they're mad at the librarians saying-

**Host** [16:50]: [laughs] That's their fault

**Jeff Jarvis** [16:51]: ... "Why aren't you open until 8:00? Google said you're open until 8:00. You're only open until 5:00 tonight," right? And-

**Host** [16:57]: But that's not AI, that's just Google.

**Jeff Jarvis** [16:59]: R- right

**Host** [16:59]: Right?

**Jeff Jarvis** [17:00]: But it shows the authority that Google-

**Host** [17:02]: Yes

**Jeff Jarvis** [17:02]: ... has to them, right? And, and that now every librarian in America has to be an expert on SEO-

**Host** [17:08]: Right

**Jeff Jarvis** [17:08]: ... and go back and figure out how to change their website so that they can tell Google the right thing to do, right? That's pre-AI, right? You're right. Like, that is the pre-AI SEO. Now, it gets exponentially harder to say now how are we going to do two problems, one of which is, like, get the right information into Google, and then two, get it into all these other systems that might hallucinate the answer. Which you're like, well, how could I even possibly guess what it might make up about what it thinks my hours are?

**Host** [17:34]: You can't. You can't. We know that.

**Jeff Jarvis** [17:35]: You can't. You can't.

**Host** [17:36]: That's one of the things that, um, Timou... Timnit Gebru and, uh, Emily Bender were talking about-

**Jeff Jarvis** [17:40]: Mm-hmm. Yes

**Host** [17:40]: ... in Stochastic Parrots was that there's an authority-

**Jeff Jarvis** [17:43]: Yes

**Host** [17:43]: ... th- these assume because they come from a computer and, and people... Most people who work with computers don't, don't ascribe that much authority [laughs] to them, but people who don't-

**Jeff Jarvis** [17:52]: Right

**Host** [17:52]: ... are gonna give it a lot of weight.

**Jeff Jarvis** [17:54]: The computer says. The computer says.

**Host** [17:55]: The computer says.

**Jeff Jarvis** [17:56]: And they've had, again, 50 years of, you know, from, from when the first, you know, Star Trek episodes came out.

**Host** [18:02]: Hmm.

**Jeff Jarvis** [18:02]: Well, the computer says this, it must be correct. And I don't blame them for that. They were, were sort of conditioned by culture to say that the computer answer is right. The computer's smarter than me But they question themselves

**Host** [18:13]: Hal 9000 going rogue was such a big plot point because it was so unexpected.

**Jeff Jarvis** [18:18]: Yeah, yeah, yeah. Right. That's a dramatic twist. And so I, I think that's a thing where, like, I have no, um... Sorry, my dog is trying to get on camera.

**Host** [18:25]: [laughs]

**Jeff Jarvis** [18:25]: I have no, you know, criticism-

**Host** [18:27]: It's okay. We love dogs

**Jeff Jarvis** [18:27]: ... for, for anybody who is, you know, surprised by the fact the computer can be wrong, right? Like, I don't, I don't fault them for feeling tricked or, or... Especially when Google has been, as far as they know, reliable to them, and now is using generative AI without them having changed anything. They didn't change any settings. They didn't push any buttons. They went to the same Google they've always gone to, and they typed in a search, and it looks a little different, but maybe not recognizably different to them-

**Host** [18:58]: Mm-hmm

**Jeff Jarvis** [18:58]: ... and all of a sudden it is composing things in a way that they didn't expect. And, you know, some PhD they've [laughs] never met has it, has it doing things a different way. And, and then the people on the other side, like I said, the librarians who are like, "Why is it making up our hours now?" Are saying, like, "I don't even know how to fix that. Before I could at least conceivably understand. I could look in the library for a book on SEO [laughs] and, and teach myself the way to fix this conceivably." There was at least some theoretical mechanism of fixing it, and now even that is gone. And so that-

**speaker_4** [19:33]: I, I don't think you're, you're fixable. I mean, it, it's, we've, we've, we... Y- you're right, Neil. It's a really, really huge point. We started with a presumption of the accurate computer, and now we're in the age of approximate computing, and that's where we're gonna stay.

**Jeff Jarvis** [19:45]: Yeah. Yeah.

**speaker_4** [19:46]: Uh, whether it's, it's machine learning, uh, and prediction machines, or whether it's quantum computing, um, it all-

**Jeff Jarvis** [19:53]: Yeah

**speaker_4** [19:53]: ... becomes approximate and good enough.

**Jeff Jarvis** [19:54]: And that's a social contract that has been broken that we haven't had a dialogue about.

**speaker_4** [20:00]: Right.

**Jeff Jarvis** [20:00]: There's been no consent around it. And this is, this concept of consent I keep coming back to, and, and it's really been, um... I mean, to be very transparent, this has been one of the reasons why I sort of don't miss being a CEO of tech startups anymore, and why I sort of stepped away from that, is a lot of my work and my roles and that stuff, you know, you, when you're the founder or CEO, the thing you start every day with is the problem that nobody else in the company wanted to reckon with the day, day before.

**speaker_4** [20:29]: [laughs]

**Jeff Jarvis** [20:29]: Right? And, and a lot of it is, like, we need to change our terms of service. You know, if it's not like, you know-

**speaker_4** [20:35]: [laughs]

**Jeff Jarvis** [20:35]: ... we have this, we have an HR problem or something [laughs] hopefully it's not. But, but a lot of it is, like, we have to change our terms of service, and every terms of service you've ever clicked I agree to without reading all basically says the same thing, which is, "We can change this unilaterally at any time without telling you." And what you agree to is we're gonna continually move the goalposts, and that means there's no consent, anything. And even that we have kind of resigned ourselves to as users, right? But that's users. We know there was at least some quid pro quo. You were giving a really good search engine in exchange for me getting the goalposts [laughs] shifted all the time. At least I got good search, right? But now what we've gone even further on is, like, I have my website that I've been doing for 25-plus years. There's no consent in the other direction of what they're doing to my website, how it's being presented to the world, right? So it used to be that, um, we had that, I'm sure you all have talked about this before, the robots.txt file, which is the permissions of what Google can do to my site, and I gave them permission to crawl my site because I wanted them to... It was, again, a quid pro quo. You bring me, uh, visitors, and I give you content that people can discover, and there's a fair exchange. They changed the terms unilaterally of what it meant they could do. Now they can take content from my site and compose things onto Google that make content on their site, but that wasn't the deal when we started. But I can't appeal that. I can never undo it. And in my case, I have written, created, and researched things on my site that exist nowhere else on the internet. I know this for a fact. Right? And I have searched for things on ChatGPT, on Google Gemini, on Claude, that I know I'm the only source on and found it in their indexes.

**speaker_4** [22:29]: Is this, is this Prince stuff, or is this-

**Jeff Jarvis** [22:31]: [laughs] Other, other musical artists, but yes. Yeah, yeah.

**Host** [22:34]: [laughs]

**Jeff Jarvis** [22:35]: Right? And, and, and, and more obscure, right? Because that's sort of it, is like I know I can go to obscure musical research that I did over the last 20-plus years, where I'm like, I know I was the source, like, canonically. And so there is no credible way they can say, we found it somewhere else, or we synthesized it somewhere else. And so, like, I know for a fact that this is showing up in your synthesized results because of me, and I know when you show it on your site and somebody doesn't come to my site, that it is you, you know, having taken... And I don't care about the pages. Like, I don't have ads on my site. I care about the relationship with that person who cares about that content.

**Host** [23:11]: But isn't that the nature of... I mean, look, uh, there's only five different stories, and we're all just recasting those five different stories over-

**Jeff Jarvis** [23:20]: Mm-hmm

**Host** [23:20]: ... and over again. That's human, is, is-

**speaker_4** [23:23]: Media

**Host** [23:23]: ... it, it's-

**Jeff Jarvis** [23:24]: Mm-hmm

**Host** [23:24]: ... everything we do is based on what we have absorbed in the past.

**Jeff Jarvis** [23:29]: Well-

**Host** [23:29]: I mean, I always... I, I might get ideas from your blogs. I often do, and may not-

**Jeff Jarvis** [23:33]: Sure

**Host** [23:33]: ... credit you.

**Jeff Jarvis** [23:34]: Well, I, I think there's a, there's a question of, of consent. There's also a big difference between the largest companies in the history of the world-

**Host** [23:42]: Right

**Jeff Jarvis** [23:42]: ... and somebody I've known for 25 years who's a person that I respect, right? [laughs]

**Host** [23:46]: Every time I hear that, it really ends up being a complaint about big tech.

**Jeff Jarvis** [23:50]: Um, yes and no, right? I mean, I think, I think there's part of it. Also, like, there is no such thing as the technology industry, right? Like, tech doesn't mean anything.

**Host** [23:58]: Like- Every company is a tech company in a way nowadays.

**Jeff Jarvis** [24:00]: Right, right. And also, like, we talk about, like, people talk about, like, FANG companies still, and I'm like, "What the hell does Netscape- Netsca- I'm dating myself. Netflix [laughs] have to do-

**speaker_4** [24:08]: [laughs]

**Host** [24:09]: Because Mozilla, what does Zilla know about?

**Jeff Jarvis** [24:11]: That's, that's exactly, that's how old my brain is.

**Host** [24:12]: [laughs]

**Jeff Jarvis** [24:12]: Netflix, Netflix streaming, streaming a movie have to do with Apple selling me a laptop, right? Like nothing, right? Like, they do some overlap in that they both stream movies, but the point is, like, the fundamental businesses that these companies are in are not related at all, and the economics of what they do are not related at all. Like, where they make their margins is, is, is completely unrelated. So, like, the, the... Every company makes tech, you know, to your point, Paris. And I think the, the, the other part is, like, what they care about and where they're trying to, like, leverage things is very, very different. And so, so, so to the, the, um, I guess-

**Host** [24:44]: I guess what I'm saying is it's monopolies, though. It's monopol- it's companies that are-

**Jeff Jarvis** [24:46]: It's monopolies and market perversions, yeah

**Host** [24:48]: ... so big that they're dominant, like Amazon, Google-

**Jeff Jarvis** [24:50]: Yeah

**Host** [24:50]: ... Microsoft, Apple. Those companies are so dominant, they don't have to play by the same rules.

**Jeff Jarvis** [24:55]: But also, we had a premise, and again, I say this as a... Like, I have started multiple companies. I've raised hundreds of millions of dollars in VC. I've helped companies. I've been on the boards of multi-billion dollar companies. And we had a premise that companies were supposed to be in competitive markets. We had a premise that markets were supposed to be transparent. We had a premise that there were laws they were meant to be accountable to. We had a premise that public markets had regulators. None of those things are true anymore.

**Host** [25:24]: Yeah. [laughs]

**Jeff Jarvis** [25:25]: None of this... And I mean this in a very literal way, right? Like, I... And, and again, like, I have been an accountable party for writing public filings for companies, right? Like, I have been, like, on the hook for these things, and been in the boardroom for these conversations, you know, and, and, and sat across the boardroom table from the, you know, the officers of these companies, and those used to be material considerations for these companies, and none of those things are true anymore. And so the premise by which there was accountability and, and responsiveness to these public considerations doesn't exist anymore, and they are acting accordingly. And it's sort of [laughs] like the substitute teacher didn't show up for the class. How are the kids acting? [laughs]

**Host** [26:10]: So I mean, that... So in, in a way, that's the problem with AI, is not that AI itself is problematic, but that the companies that are making it are not being held accountable-

**Jeff Jarvis** [26:19]: Mm-hmm

**Host** [26:19]: ... for the products they're making.

**speaker_4** [26:20]: And some of the people who are in charge of those companies are jerks.

**Jeff Jarvis** [26:23]: Mm-hmm. Well-

**Host** [26:25]: Yeah

**Jeff Jarvis** [26:25]: ... what we've selected for, right? Like, I, I mean, I think there are people that were trying to do, you know, various degrees of right, right? Like, I think, uh, there's an interesting thing that happened in terms of, like, signaling, where, like, when they were still trying to create OpenAI to build ChatGPT years ago, they're like, "We'll make it a nonprofit, and that'll send a certain kind of signal." And then Anthropic, when they're doing Claude, is like, "We'll make it a, you know, a pr- a, a public benefit corporation. That'll send a certain kind of signal." But the, the structure of incorporation only does so much. You have to want to do the right thing, [laughs] right? Like, you being a nonprofit doesn't mean you're not a grifter, right?

**Host** [27:04]: [laughs]

**Jeff Jarvis** [27:04]: Like, I can tell you. Like, I've been in the nonprofit world a long time too, and it's like, there's a lot of people getting over, uh, you know, and making money-

**Host** [27:10]: Oh, in fact, it might even attract grifters come to think of it

**Jeff Jarvis** [27:12]: ... Yeah, yeah, because, like, you, you have the halo, right-

**Host** [27:15]: Right

**Jeff Jarvis** [27:15]: ... of, of, of looking good.

**Host** [27:16]: And, and they're tax-free. [laughs]

**Jeff Jarvis** [27:18]: Yeah. Yeah. So, like, there's a lot of different ways to, to, to get ahead there. And so I think the, the, the key thing was, like, they, they still at that time wanted to pretend to look good. Now there's the sort of vice signaling-

**Host** [27:27]: [laughs]

**Jeff Jarvis** [27:27]: ... that they're all trying to do for each other, and they really like to show that they're the biggest villains, right? Like, that's the way that you sort of show, you know, you're the transgressor, and that means that you're fucking cool.

**Host** [27:36]: Does that explain Mecca Hitler a- and Grok going off the rails?

**Jeff Jarvis** [27:41]: It's, it's a big part of it. I mean, I definitely think, um, one of the ways of showing that you have power amongst that cohort right now... And a lot of what they're doing is signaling for each other, right?

**Host** [27:50]: Right.

**Jeff Jarvis** [27:50]: Like, they're constantly... There's preening. Like, they're sort of peacocking for each other amongst this cohort of, like, a dozen of the biggest, like, tech tycoons. And, and, and again, like, I've met most of these guys, and then unfortunately made a lot of money for a lot of them for a long time. Um-

**Host** [28:04]: It's your fault. [laughs]

**Jeff Jarvis** [28:05]: And... [laughs] I'm not the most to blame, but I probably have some-

**Host** [28:07]: That's what happened in the Gilded Age too, though, right?

**Jeff Jarvis** [28:09]: Yeah.

**Host** [28:09]: They were all playing for John Jacob, uh, Astor and, you know-

**Jeff Jarvis** [28:13]: Yeah, yeah

**Host** [28:13]: ... JP Morgan who was-

**Jeff Jarvis** [28:13]: For sure. Yeah.

**Host** [28:15]: Yeah.

**Jeff Jarvis** [28:15]: Yeah. And they wanted to... Yeah, they're preening and, and peacocking for each other. And, and so some of what they do in that performance now is, "If I can be the most transgressive, I'm a bad boy."

**Host** [28:26]: Yeah.

**Jeff Jarvis** [28:26]: I mean, it's, it's not any different than, like, 15-year-olds, right, that are sort of, you know, doing little stunts and, and, and tricks for each other. And, and, um-

**Host** [28:34]: If you're not accountable to your customer, you're not accountable to the market, you're not accountable to society, you're still gonna wanna impress somebody, and it's gonna be-

**Jeff Jarvis** [28:42]: Mm-hmm

**Host** [28:42]: ... your other fellow billionaires-

**Jeff Jarvis** [28:44]: Right, because after the first billion-

**Host** [28:45]: ... and oligarchs

**Jeff Jarvis** [28:45]: ... it doesn't mean anything, right? Like, there's no difference in quality of life between $10 billion-

**Host** [28:49]: Right

**Jeff Jarvis** [28:50]: ... and $50 billion.

**Host** [28:51]: Right.

**Jeff Jarvis** [28:51]: Right? You're not, like, more planes. There isn't... You don't eat more in a day of your, like, y- you know, gold-plated caviar or whatever you're eating. There, there isn't-

**Host** [28:59]: You just have a bigger TV in your bedroom, basically.

**Jeff Jarvis** [29:02]: Th- there isn't a bigger... You know, like, there's no, there's no more screen you can see.

**Host** [29:05]: [laughs] Right.

**Jeff Jarvis** [29:05]: You know what I mean?

**Host** [29:06]: [laughs]

**Jeff Jarvis** [29:06]: And, and, and, and, and I mean... and I mean this in a very literal way. Like, there's a few of these guys that I had still kept in touch with until they got their first billion, and, you know, their kids would be about the same age. And, and the funny thing is, like, their kids don't get access to some super secret Legos that my kid doesn't have.

**Host** [29:22]: [laughs]

**Jeff Jarvis** [29:22]: Do you know what I mean?

**Host** [29:23]: Yeah.

**Jeff Jarvis** [29:23]: Like, it's the same Legos-

**Host** [29:25]: It's the same Legos

**Jeff Jarvis** [29:25]: ... and their kids are not happier.

**Host** [29:26]: Yeah.

**Jeff Jarvis** [29:26]: And, and I would see, like, none of them-

**Host** [29:28]: They get better shrinks through their kids. [laughs]

**Jeff Jarvis** [29:31]: They need them.

**Host** [29:31]: Yeah, exactly.

**Jeff Jarvis** [29:32]: Because, and I, and I, and I don't mean this lightly. Zero, 0% of the guys I knew that became billionaires out of the cohort I was in, 0% of them are still with the spouse they had then.

**Host** [29:42]: Yeah.

**Jeff Jarvis** [29:43]: Not one.

**Host** [29:44]: Well, you trade it in.

**Jeff Jarvis** [29:45]: Not one.

**Host** [29:45]: You trade your spouse in-

**Jeff Jarvis** [29:46]: Not one

**Host** [29:46]: ... for your trophy wife.

**Jeff Jarvis** [29:47]: Right?

**Host** [29:47]: Yeah.

**Jeff Jarvis** [29:47]: And what they tell themselves is, "No, well, you know, we grew apart because life got complicated," and da, da, da. But, like, you're like, "Now, you know, what's my real answer? Like, would I give my wife up for a billion dollars? Clearly, my answer is no." And clearly their answer is yes, right? And they would never say it. Would they give their kids up, seeing their kids every day, for a billion dollars? And their answer demonstrably is yes.

**Host** [30:11]: Yes.

**speaker_4** [30:11]: Mm-hmm.

**Jeff Jarvis** [30:12]: And it's proof, right? It's proof. And, like, obviously people have, you know, complicated relationships, and people split up for all kinds of good reasons, and, like, there's life that happens, but it, it cannot statistically be the case that none of them could make it work.

**Host** [30:26]: Some of them-

**Jeff Jarvis** [30:27]: Right?

**Host** [30:27]: ... have several wives. [laughs]

**Jeff Jarvis** [30:28]: Sure. Exactly. Right?

**Host** [30:30]: Many wives.

**Jeff Jarvis** [30:30]: But that's the thing, it's like you don't become a billionaire by accident.

**Host** [30:33]: Right.

**Jeff Jarvis** [30:33]: You have to have wanted it more than you wanted anything else in your life.

**Host** [30:36]: Yeah. That's right.

**Jeff Jarvis** [30:37]: And what does that des- you know, design for in your head is not sustaining relationships, not sustaining connection with the rest of the world. So they started-

**speaker_4** [30:43]: You think they started with that or, or, or they, the temptation overtook them?

**Jeff Jarvis** [30:48]: I, I think that's sort of... So here's the thing. I think people can want to certainly, like, "Oh, you know, I wanna be successful, and I wanna make enough money to be comfortable," and like... And then you start to select out, right? Like, I know people that made merely $100 million who still live on Earth-

**Paris Martineau** [31:01]: Pish posh

**Jeff Jarvis** [31:01]: ... and exist. [laughs] You know what I mean? And they're like, they go grocery shopping-

**Paris Martineau** [31:05]: Head full

**Jeff Jarvis** [31:05]: ... and they, like, act like people, and they... Like, I can have dinner with them, and they sound like a human. And I'm like, "Okay, great. Good for you. I'm happy for you," and like, they're still, like, recognizably normal. And, like, that's still all the money in the world. I'm like, "You have literally anything you could ever want, right?" And they're like, "Yeah, I'm good." And so, like, it's interesting what that inflection point is. But if you were at that point, and then you're like, "No, I need to have 50 times this much," you're like, you're already, your brain's-

**Host** [31:32]: What is that?

**Jeff Jarvis** [31:32]: ... already broken.

**Host** [31:32]: Yeah. What is that?

**Paris Martineau** [31:33]: What do you think is the difference between those people? What do you think separates the people who-

**Jeff Jarvis** [31:38]: I-

**Paris Martineau** [31:38]: ... hit the 100 million and are like, "I'm going to retain some form of normalcy and be grounded to Earth-

**Jeff Jarvis** [31:43]: Yeah. I-

**Paris Martineau** [31:43]: ... versus the people whose brain are fundamentally broken?"

**Jeff Jarvis** [31:45]: I wish I knew. I think there's a couple... I mean, I think it's like anything else. It's like your parents. [laughs] You know what I mean? I think it's like how you were raised. It's who you're around. How isolated are you? What's your own neuroses and insecurities? Like, it's, it's just human stuff. Like, we're all broken in our own way and, and, you know, whatever it is. And if somebody pushes your buttons the right way... But like I said, nobody becomes that, that wealthy by accident. The challenge now is, like, I, I saw this where being a CEO of a venture-backed company, it almost selects for being psychotic, right? Because the, the, the, the VCs and these things, they're like-

**speaker_4** [32:21]: [laughs]

**Jeff Jarvis** [32:22]: ... "Here's what we want you to do and what you have to forego." And like a really concrete example is, like, I really cared about providing good health insurance for my team. And, you know, it's like prosaic stuff. Okay, we want Aetna or whatever, Cigna, and here's what we're gonna do, and we wanna have this coverage for these things. And the reality is, you know, when I screw up as a CEO, people lose their jobs, and when they lose their jobs, they lose their health insurance in America, right? Which is immoral. It's immoral that I get to choose whether people can get treated for cancer or have kids, right? And so you just, if you're a person with a conscience, feel like crap all the time, right? And-

**speaker_4** [33:13]: Power. Power

**Jeff Jarvis** [33:15]: ... yeah, like you're-

**Host** [33:15]: Or you're a sociopath-

**Paris Martineau** [33:16]: And then when you feel like crap-

**Host** [33:17]: ... and you don't have empathy

**Paris Martineau** [33:17]: ... you also... And when you feel like crap, you have to also decide, "Oh, do I want to continue to feel like crap and retain a conscience?"

**Jeff Jarvis** [33:24]: Right. Right. Or-

**Paris Martineau** [33:25]: "Or do I want to turn inward-

**Jeff Jarvis** [33:27]: Or-

**Paris Martineau** [33:27]: ... and be like, 'Actually, no, there's some other explanation.'"

**Jeff Jarvis** [33:30]: Ex- exactly.

**Paris Martineau** [33:31]: "And there's a reason why I shouldn't feel like crap."

**Jeff Jarvis** [33:33]: And so there's an entire machinery built around, "No, you shouldn't feel like crap. You're a brave and bold decision-maker-

**Host** [33:38]: Ah

**Jeff Jarvis** [33:39]: ... who has done the noble thing, and you are a truth teller."

**Host** [33:43]: Right.

**Jeff Jarvis** [33:43]: "And they are wrong for letting you down, and they caused you to have to do layoffs."

**Host** [33:49]: Right.

**Jeff Jarvis** [33:49]: "And it's their fault, and they don't deserve healthcare, and they're uppity, and you should punish them," right? There's an entire machinery saying that in your ear. And do you choose to listen to that, or do you choose to hold onto your conscience is the fundamental reckoning we're in as a society, really. And then now who makes it through that filter is the people that are getting to f- have enough money to train an AI right now, right? 'Cause it's really, really expensive to train an AI.

**Host** [34:15]: Yeah.

**Jeff Jarvis** [34:16]: Right? And like, and I hate... Like, and I'm not trying to be preachy. I'm just like, literally, I've been through this 'cause I'm like, I- part of why I want there to be less expensive AI models [laughs] is so that we can have, like, just the thin layer of people who are not complete psychopaths can afford to build, build AIs too.

**Host** [34:29]: Mm-hmm. Mm-hmm.

**speaker_4** [34:31]: But, but the, the models leapfrog each other and end up all doing kind of the same thing. I think the interesting thing is gonna be at the application layer.

**Jeff Jarvis** [34:38]: Yes. Yeah.

**speaker_4** [34:39]: And the question is-

**Jeff Jarvis** [34:39]: There's so many cool things to be built

**speaker_4** [34:40]: ... but now you see Me- Meta, ru- rumors are that Meta's not gonna do, uh, open source Llama anymore.

**Jeff Jarvis** [34:45]: Yeah.

**speaker_4** [34:46]: And, um, whereas... And that, and that's-

**Jeff Jarvis** [34:49]: Because they hate people using it to train

**speaker_4** [34:51]: ... a university that's killing at a university 'cause that's what, what we use now.

**Host** [34:54]: Yeah. Well, what's really terrifying is the notion that, uh, we're... If we do g- if we do, and it's a long, it's a big if, get some sort of super intelligence, is that they will be controlled by people you just, like you just described, like the Mark Zuckerbergs-

**Jeff Jarvis** [35:07]: Their parents are assholes

**Host** [35:08]: ... and the Elon Musks, uh-

**Jeff Jarvis** [35:10]: Yeah

**Host** [35:11]: ... of the world. And th- I mean, that's the real hazard. It's not the AIs that are the hazard. It's the people who are making them.

**Jeff Jarvis** [35:17]: I mean, you know, software has values baked into it, right? And we're all flawed, so it's always gonna be, have bugs in that way, separate from the bugs in the software.

**Host** [35:25]: Right.

**Jeff Jarvis** [35:25]: And, and the question is, like, what are the values of the people that made the apps? And, you know, that part of it is a big reckoning. And, and I, I don't fault... Like, a normal consumer not understanding that is normal. Like, you wouldn't think about that when you're, like, buying a phone. Um, but I think those of us who are, like, into this stuff think about that a lot and, and it's sort of fallen out of favor. We used to care about that stuff a lot, you know, 10, 20, you know, 30 years ago. We were really... It's funny 'cause, like, we used to think, like, you know, Microsoft was the evil empire, [laughs] right?

**Host** [35:55]: [laughs]

**Jeff Jarvis** [35:55]: And it's like, man, take me back to Windows 95, right? Like, that's like, if that's as bad as it got, that would've been great. But, but I think now, like the stakes are so much higher and, and people are so much busier that, like, thinking about, like, I have to like download an app and then know about the- Weird philosophy of the dude who built it. No, I don't got time for that. That's... And also it's a nightmare. Like, the, these weird, you know, esoteric things that they're focused on. Like, I don't, I don't want normal people to have to think about that. I don't want non-tech nerds to have to think about that. But how do you distill that into something people can understand that's consumable? Like, I think a very, you know... Recently, um, Aaron Swartz has been on my mind a lot, you know, and he was a friend and, and really great-

**Host** [36:40]: Mm-hmm

**Jeff Jarvis** [36:41]: ... at communicating a lot of these concepts so effectively. And in so many disciplines, right? So whether it was intellectual property or just, like, privacy or, or so many of these sort of concepts. And, and I think, and it's interesting 'cause there's sort of been this mythology that's developed around him, you know, since he passed, but, but I, I think he was really a pragmatist in so many ways. And so I think about, like, who is a new young version of that? And, and part of it was he was born into a context where there was a community around him that cared about these things, and so he could rise to be a leader and a voice because a lot of people cared about these things. And if you are a teenager like he was when he started to do this work right now, where would you find a cohort of other people who care about this? I think it would be very hard. If you're like, "I think I care about privacy and personal expression, and all those other things," like, I'm on the board of the EFF, and this is the things they fight for. And it's like, you know, some of us here have some gray beards, right? There's a-

**Host** [37:42]: [laughs]

**Jeff Jarvis** [37:42]: ... way too many gray beards. It's a lot of old-

**Host** [37:44]: [laughs]

**Jeff Jarvis** [37:44]: ... it's a lot of dad energy-

**Host** [37:46]: [laughs]

**Jeff Jarvis** [37:46]: ... you know? And it's like, we need a lot of, like, young people of, like, you know, different, different genders and different ages and different races coming in and representing this thing because it, it has... It's so relevant to new folks, but they don't know it. And, and, you know, and I'm like, shame on me. Like, they can't find it anymore, 'cause what book would you read? They're not, like, finding some old middle-aged dad's blog, you know? So, like, that's what I'm trying to do is, like, figure out where's the place that's discoverable culturally for people who care about these things but don't necessarily wanna nerd out to say, "I wanna have good tech, good tech."

**Host** [38:25]: Teach, Anil, teach.

**Jeff Jarvis** [38:25]: And find good apps.

**Host** [38:28]: What about teaching?

**Paris Martineau** [38:28]: Teach and create it, yeah.

**Jeff Jarvis** [38:29]: Mm-hmm. I think it has to be, like... Maybe, but I feel like, um... I've been thinking a lot about, like, Dua Lipa's podcast is amazing, right? And she does a great job interviewing authors. Just super, super culturally fluent. Obviously, you know, her music's amazing, her shows are great, but she's just super great at articulating really good cultural ideas. I... And she fought for controlling her master recordings and owning them, right? Taylor Swift has obviously done an amazing job with Taylor's Versions. They are incredible educators about intellectual property.

**Host** [39:00]: Mm-hmm.

**Jeff Jarvis** [39:01]: They just don't know it. And so, like, they're teachers. They are teaching... Like, they are heirs to Aaron Swartz's work. They don't know it. And, and, like, they're living in a world that Aaron Swartz defined. And so, like, that part of, like, how do we get them to see that they have articulated a, a position that is the solution to people being worried about, is AI taking content without consent, right? 'Cause lots of people can say, "Well, AI engines are stealing content." But the answer is, artists have to own their work, and nobody has done more to say, to advance the cultural conversation about artists owning their work than Taylor Swift saying, "Taylor's Versions," right? So we have an entire generation that's growing up knowing that. That is the other part of the conversation about, is AI working with consent.

**Host** [39:54]: But let me, let me poke at that, Anil.

**Jeff Jarvis** [39:56]: Please.

**Host** [39:56]: Hold that thought.

**Paris Martineau** [39:56]: Hold on.

**Host** [39:56]: 'Cause Aaron-

**Jeff Jarvis** [39:57]: Yeah

**Host** [39:57]: ... 'cause, uh, we're, we're long and I need to-

**Jeff Jarvis** [39:59]: Oh, sure

**Host** [40:00]: ... uh, so I'm gonna give you a choice, Anil.

**Jeff Jarvis** [40:03]: Mm-hmm.

**Host** [40:04]: We can wrap this up 'cause we only asked for a half an hour of your time-

**Jeff Jarvis** [40:06]: You got a concert to go to

**Host** [40:07]: ... but we took it for-

**Jeff Jarvis** [40:07]: Sure

**Host** [40:08]: ... 30 minutes, and Wu-Tang awaits.

**Jeff Jarvis** [40:09]: [laughs]

**Host** [40:10]: Uh, in which case we could wrap it up now, uh, or we could take a break and come back. It's up to you. I, I don't wanna, uh, overburden you.

**Jeff Jarvis** [40:18]: Um, I'm, I'm, I'm happy to go another five, 10 minutes if it's useful. I, I don't know if you wanna put a button on it or-

**Host** [40:23]: Jeff, can you hold your question?

**Paris Martineau** [40:24]: Yeah, I can hold it. I can...

**Host** [40:25]: Okay. Okay, we'll do a quick ad, and, uh, 'cause I also wanna thank you for your, uh, wonderful blog post. "Wherever You Get Your Podcasts Is a Radical Statement."

**Jeff Jarvis** [40:35]: Oh, yeah.

**Host** [40:35]: Uh, because as a podcaster, I'm a firm believer in that, and that Aaron Swartz's RSS is what powers-

**Jeff Jarvis** [40:42]: Yeah

**Host** [40:42]: ... what we do, and it's a, it's a radical technology-

**Jeff Jarvis** [40:45]: Yeah

**Host** [40:45]: ... that has survived.

**Paris Martineau** [40:46]: Mm-hmm.

**Jeff Jarvis** [40:46]: It really has.

**Host** [40:47]: Yeah, and I'm, I'm very glad for that. Actually, there is a, a cartoon that came out last week about RSS, and one... It's one of the things it says is, uh, that, that you may not know it, but you're using it [laughs] every time you listen to a podcast.

**Jeff Jarvis** [41:00]: Yeah, yeah.

**Host** [41:01]: Love that. Uh, Anil Dash is our guest. Somebody said in the, uh, in the Discord chat, one of our club members said, uh, "What distinguishes Anil is not about his ability to express, but rather he's effective at bringing a moral voice with a deep technical background."

**Jeff Jarvis** [41:16]: Always thus.

**Host** [41:17]: And without preaching and assuming everyone he disagrees with is evil. So I agree-

**Jeff Jarvis** [41:22]: That's... I appreciate that. I mean, I, I aspire to that. I hope I'm doing justice to it.

**Host** [41:26]: You are. I think you are. Anil Dash is our guest on Intelligent Machines. Five more minutes with him before he's gotta go see the Clan.

**Jeff Jarvis** [41:33]: [laughs] The Wu-Tang Clan, let's be specific. [laughs]

**Host** [41:35]: The... Oh, yeah, that's a good point.

**Paris Martineau** [41:36]: Yeah, yeah, to be, to be specific.

**Host** [41:38]: That's a very good point. [laughs]

**Jeff Jarvis** [41:39]: Very important distinction here.

**Paris Martineau** [41:40]: Clan before he sees Wu-Tang.

**Jeff Jarvis** [41:42]: [laughs] Yes.

**Host** [41:42]: Before he sees the Tang. What do they call them? The Wu?

**Paris Martineau** [41:45]: The Wu-Tang Clan.

**Jeff Jarvis** [41:46]: The Wu is fine.

**Host** [41:47]: He's just gonna... They'll be too soon?

**Jeff Jarvis** [41:47]: Wu's fine for short. Wu-Tang is good.

**Host** [41:49]: Yeah, Wu-Tang, he's going to see. The last. They don't do a lot of concerts.

**Jeff Jarvis** [41:55]: No, they've, they've been out... I mean, you know, the guys do shows, um, solo a lot, but they haven't been together a lot.

**Host** [42:01]: Yeah.

**Jeff Jarvis** [42:01]: I mean, it's, it's, you know, the band was-

**Host** [42:02]: Were you mad when Martin Shkreli bought the album?

**Jeff Jarvis** [42:05]: [laughs] It's not even in the top 10 list of things to be mad at that guy for, but sure.

**Host** [42:09]: [laughs]

**Jeff Jarvis** [42:10]: It's one of them.

**Host** [42:11]: His ill... He used his ill-gotten gains to do it.

**Jeff Jarvis** [42:14]: Yeah.

**Host** [42:15]: Uh-

**Jeff Jarvis** [42:15]: I mean, n- nothing could be more characteristic of the music industry than that guy owning one of their records.

**Host** [42:19]: Right there.

**Paris Martineau** [42:19]: Yeah.

**Host** [42:19]: In a nutshell, yeah. Uh, our show today brought to you by... I just got it, our brand-new mattress. I have to say, I've been sneaking out in between the breaks and lying down on it. It's so nice. Did you know- It's brought to you by Helix Sleep. Did you know that you're supposed to replace your mattress every six to 10 years, depending on the mattress, how well it wears, whether you're wearing a hole in it in certain spots, that kind of thing? What-- Your mattress is really a big part of your life. I know people say, "Well, I spend a third of my life asleep." No, more than that. Movie nights with your partner, morning cuddles with your kitty, your wind-down ritual after a long day, it's all happening on your mattress. I, I would be willing to bet most of us spend more time on our mattress than anywhere else, and, and the mattress can, can torture you. [chuckles] A bad mattress, you could be waking up sweating, you know, too hot, or your back's killing you, or, or your partner's tossing and turning. I'm the tosser and turner in our family, and your-- my poor wife has to put up with the bounces. It's, uh, the classic mattress nightmare. Well, Helix Sleep changes everything. This mattress, [gasps] it's like, it's like sleeping on a cloud. No more night sweats, no back pain, no motion transfer. Get the deep sleep you deserve. It had been eight years since we got a new mattress. We said, "We gotta get the best. Where's the best?" I saw reviews. One buyer said with five stars, "I love my Helix mattress. I will never sleep on anything else." Well, that got my attention. Then I saw the awards. Time and time again, Helix Sleep is the most awarded mattress brand. Wired this year, 2025, said, "Best mattress." Good Housekeeping's Bedding Awards 2025, Premium Plus Size Support. Best Hybrid Mattress in the GQ Sleep Awards for 2025. Wirecutter, featured for plus size. I'm a little heavy, so maybe, uh, maybe that's important for me. Oprah's Daily Sleep Awards for 2025, I love this one, Best Hotel-Like Feel. I don't know about that. I don't-- If I, if I found a hotel that had a mattress like my new mattress, I might be, uh, spending more time there. I love my Helix Sleep. I want you to go to helixsleep.com/twit. Twenty-seven percent off sitewide during the Fourth of July sale. Their best of web offer has been extended. That's helixsleep.com/twit for 27% off sitewide, exclusively for listeners of Intelligent Machines. Now, this offer does end July 31st, 2025, so make sure you go now. And do enter our show name after checkout 'cause they know we sent you. Oh, and if you're listening after July 31st, 2025, I'm sorry, that sale's over, but be sure to check them out. There's always some great deals at helixsleep.com/twit. You will see from now on a new Leo, rested, relaxed, and ready to do a podcast. Thank you, helixsleep.com/twit. Our guest, Anil Dash, is, uh, on the beach. We used to say when you're in radio and you're at a-- and you're not working, you're on the beach. Uh, he is calling from-

**speaker_4** [45:30]: For sure

**Host** [45:30]: ... a very hot New York City right now. I appreciate that.

**Paris Martineau** [45:34]: Disgustingly hot.

**Host** [45:35]: Now, you're all in the, you're all in the hot Eastern Seaboard.

**speaker_4** [45:37]: Mm-hmm. Yeah.

**Host** [45:38]: Sorry.

**speaker_4** [45:38]: It's like 90 degrees today.

**Host** [45:40]: Yikes. That's hot in New York. That's sweaty.

**speaker_4** [45:42]: Oh, yeah.

**Host** [45:43]: That's terrible. Yeah.

**Paris Martineau** [45:44]: And the dew point is, like, 80 or, like-

**Host** [45:46]: Ugh

**Paris Martineau** [45:46]: ... 70 something. It's rough.

**Host** [45:47]: Wasn't it nice when you were out here, Paris, enjoying the nice climate?

**Paris Martineau** [45:51]: It was perfect.

**Host** [45:52]: It's perfect.

**Paris Martineau** [45:52]: And it was perfect in Northern California.

**Host** [45:54]: It's perfect. Yep. So, uh, you put a button in it.

**Paris Martineau** [45:57]: Jeff, what was your question?

**Host** [45:57]: Uh, you can now unbutton your thought, Mr. Jarvis.

**speaker_4** [45:59]: So Aaron Swartz stood for, and tragically died for, opening up information-

**Host** [46:07]: Mm-hmm

**speaker_4** [46:07]: ... to society. And, um, [tsking] forgetting if we can for just a second the evil people and evil companies that may be in charge of many of the models now, if we're gonna end up using large language models, uh, and they're trained only on the free crap that's on the internet-

**Host** [46:27]: [laughs]

**speaker_4** [46:28]: ... we're all the worse for.

**Host** [46:29]: It's not all crap.

**speaker_4** [46:29]: I had an example the other day where I was doing some research and I thought, "Wow, this is actually pretty good," and look at all these sources and the deep research, and the sources were all crap because that's what's available. And, and I, and I, I, I struggle with a question of whether as journalists, whether there is a moral obligation to share even with the models so the models will in turn be better to share with the public and with the children who are gonna use it for teaching and such. So how, how do you-- how do we balance Aaron's-- what Aaron stood for-

**Host** [46:59]: Mm-hmm

**speaker_4** [47:00]: ... and these choices with those who control this information, like academic publishers still-

**Host** [47:06]: Yeah

**speaker_4** [47:06]: ... and news publishers today?

**Host** [47:07]: I, I think the question is about ownership and control of the models, right? So, like, if we need to have good models and there's a public good in creating them, then we should have models that are owned and controlled in the public good, right? Like, where are the models that are owned and runned, run by universities, that are owned and run-

**speaker_4** [47:26]: Which they do in Norway. They've-

**Host** [47:28]: Right

**speaker_4** [47:28]: ... done that in Norway. They've done that-

**Host** [47:29]: Right

**speaker_4** [47:29]: ... elsewhere, yep.

**Host** [47:30]: By, by, by, by governments, by, um... You know, I, I think that we should have them run by, by unions, right? Like, I don't think there's any reason why... Like, one of the things I was thinking about was, um, uh, Rian Johnson and Natasha Lyonne and a couple other filmmakers had made a, um, a gen AI tool for filmmakers that was trained on consensually gathered video data. But a lot-- they've gotten a lot of blowback 'cause people didn't really understand that you could have consensual data, so they're like, "Oh, why are they making this AI slop tool?" Right? And they just didn't have a vocabulary to explain it 'cause, like, people love Natasha Lyonne, right? So they're like, you know, "Why is the yel- why are they yelling at her on the internet?" And so I was realizing, like, if, if even people that are that sort of culturally popular can't articulate that there could be, you know, sort of quote unquote "good AI," well, then maybe the, you know, the Screen Actors Guild and the WGA should own their own model and, and sort of be in control of, of something where they have leverage and then rather than the studios being the ones that control it. And this sort of goes back to, like-

**Jeff Jarvis** [48:34]: You know, at the turn of the century, there was this battle between Napster and, and the labels, but the artists weren't in the conversation at all. So you ended up with this thing that the labels made money and, and the, you know, the streaming-

**Host** [48:46]: Mm-hmm

**Jeff Jarvis** [48:46]: ... platforms made money, but the artists got screwed. And, and we're sort of on that path again, where, like, everybody but the artists and creators is in the room. And, and so I think about, you know, there are other, uh, models that are possible, and, you know, people just don't talk about co-ops. They don't talk about, um, you know, universities. They don't talk about public sector. Um, but also, like, it's the internet. We used to talk about people, like, organizing together on the internet. Like, it's-

**Host** [49:14]: Yeah

**Jeff Jarvis** [49:14]: ... an old-fashioned idea, but, like, [laughs] there's no reason that you couldn't just sort of say, like, people are gonna work together to build models collectively. Uh, we used to think that's what the internet was for. It is what it was designed for.

**Host** [49:26]: Mm-hmm.

**Jeff Jarvis** [49:27]: Like, the fundamental purpose of the internet was to collectively share and publish information academically, right? The web was born to do that, and so I think, um, it's not a radical idea. It's actually a very old-fashioned idea. Um, and, and there's no reason technically it couldn't be done. So, so I think we just have to, like, re-open people's imagination to it, but again, I don't fault anybody who is from this century not knowing that because we have done a very poor job of teaching them about it, right? If you are of this century, other than me being from the 20th century, how would you know? Like, shame on me. I haven't told anybody about it. Like I said, the, the, you know, the, the young... the early career people I talk to that I try to mentor in the, you know, tech industry, I'm like, "Oh, well, how did you learn about this stuff?" They're like, "Well, I read everything. I read Peter Thiel's book, and I read-"

**Host** [50:16]: [laughs]

**Jeff Jarvis** [50:16]: "... Marc Andreessen's manifesto-

**Host** [50:18]: Ah

**Jeff Jarvis** [50:18]: ... and I read Hacker News," right? And then yeah, and I mean, I feel that way, and then I'm like, "Oh, well, yeah, shame on me." Like, what would they read in the startup world, right? And then, you know, Jeff, they will have read maybe, you know, some of your stuff.

**Host** [50:29]: Yeah.

**Jeff Jarvis** [50:29]: But, like, that's not a, like, startup guy, right? That's some academic. Like, we're dismissed... Like, even me, like, I can shape myself, like, form myself into a thing that looks like a startup guy to them, but they're like, "But that's not real. Like, that guy writes too, so he's not a real founder guy."

**Host** [50:47]: [laughs]

**Jeff Jarvis** [50:48]: He's intellectual.

**Host** [50:48]: He's intellectual. Forget him.

**Jeff Jarvis** [50:49]: Yeah. Right. Right. No-

**Host** [50:50]: [laughs]

**Jeff Jarvis** [50:50]: ... no, for real because they've been told-

**Host** [50:52]: Yeah

**Jeff Jarvis** [50:52]: ... if somebody has been in a journalistic context, you should dismiss them. If somebody has been in academic context, you should dismiss them.

**Host** [50:59]: Right.

**Jeff Jarvis** [50:59]: They have been told this explicitly.

**Host** [51:01]: Right.

**Jeff Jarvis** [51:01]: They are the enemy, right? Like, I reckon Clubhouse was a thing in early COVID. Like, you would have Marc Andreessen in a Clubhouse room called How to Destroy the New York Times.

**Host** [51:09]: Yeah.

**Jeff Jarvis** [51:10]: Because that's the enemy. And so, so when you're a startup guy who, like, that's what you saw when you were in college, anybody who is affiliated with that whole world is suspect.

**Host** [51:22]: We got a problem. Uh, I have to say, though, there is a certain NIMBY point of view as well among artists that I-

**Jeff Jarvis** [51:30]: Mm-hmm

**Host** [51:30]: ... that I-

**Jeff Jarvis** [51:30]: [laughs]

**Host** [51:30]: I mean, w- we, we've gotta find a, a path-

**Jeff Jarvis** [51:33]: Yeah, yeah

**Host** [51:33]: ... that is equitable for everybody.

**Jeff Jarvis** [51:35]: Mm-hmm.

**Host** [51:35]: Um, and, and let's face it, uh, Anthony Nielsen was saying this, Disney's not sue- suing, suing Stable Diffusion to protect the artists.

**Jeff Jarvis** [51:44]: No. [laughs] No. No.

**Host** [51:46]: [laughs]

**Jeff Jarvis** [51:46]: And, like, the labels weren't suing Napster 'cause they're like-

**Host** [51:49]: Right

**Jeff Jarvis** [51:49]: ... "We just love our musicians so much."

**Host** [51:51]: Right.

**Jeff Jarvis** [51:51]: Like, it's, it's-

**Paris Martineau** [51:51]: Nobody wants them to get paid more.

**Jeff Jarvis** [51:53]: Yeah, yeah. We just, we, we just wanna look out for the little guy. Yeah, I mean, I think that's sort of it, is like it's always been at the expense of the real creators, and it's always been at the expense of the real artists. And I think-

**Host** [52:01]: But we still create. We still create because that's what humans-

**Jeff Jarvis** [52:03]: Because you cannot create

**Host** [52:05]: ... that's what humans do.

**Jeff Jarvis** [52:06]: Yes. Yes.

**Host** [52:07]: Uh, and that's the good news. That's the optimistic, uh-

**Jeff Jarvis** [52:11]: Yeah

**Host** [52:11]: ... point of view, I think.

**Jeff Jarvis** [52:12]: Yeah. You can't stop the creators, right, 'cause it's in your blood. It's in your DNA.

**Host** [52:15]: You're gonna do it.

**Jeff Jarvis** [52:15]: Like, you all-

**Host** [52:15]: Yeah

**Jeff Jarvis** [52:15]: ... you know, you all have been inspirations to me for decades now because I... you know, you've never stopped. You know, Leo, Jeff-

**Host** [52:22]: [laughs]

**Jeff Jarvis** [52:22]: ... like, you guys-

**Host** [52:22]: Never stop

**Jeff Jarvis** [52:23]: ... no, you can't stop. Like, you guys have never stopped, you know, podcasting. You've never stopped writing. You've never stopped putting stuff out there.

**Host** [52:29]: Right.

**Jeff Jarvis** [52:29]: You never could, right? And it's always been that, um, you know, that sort of... Like I said, it's, it's inspiring to me. I, I don't get to say it often enough, but, like, you know, you guys being out there and having that voice, being consistent, having your values, yet giving a platform to people. You guys have put so many people on over the years who wouldn't have had a voice, wouldn't have had that platform, including myself, over the years. Like, that's profound. There are not many people doing that anymore. There are not many people who were doing it 20 years ago, and, you know, that is something where... And you built your own platforms.

**Host** [53:00]: Yeah.

**Jeff Jarvis** [53:01]: Right? And so-

**Host** [53:01]: And I would venture to say-

**Jeff Jarvis** [53:02]: ... how do we teach new people to do that?

**Host** [53:04]: We don't do it for the money, right?

**Jeff Jarvis** [53:06]: Right. Right.

**Host** [53:06]: Uh [laughs]

**Jeff Jarvis** [53:07]: You, you-

**Host** [53:07]: You know, especially me

**Jeff Jarvis** [53:07]: ... you make money to be able to make things.

**Host** [53:09]: Yeah.

**Jeff Jarvis** [53:09]: You don't make things to make money.

**Host** [53:11]: Exactly.

**Jeff Jarvis** [53:11]: And that's profound.

**Host** [53:12]: Yeah.

**Jeff Jarvis** [53:12]: Right? That's important. And there are people who still have that, but they don't have the, the way to articulate that, and they haven't seen enough role models to teach them that they could do that too.

**Host** [53:22]: Well, you're a great role model for me too, Neil, and I-

**Jeff Jarvis** [53:25]: Appreciate it

**Host** [53:25]: ... uh, we've been trying to get you on for a while. I'm really glad we could get you on.

**Jeff Jarvis** [53:28]: Yeah.

**Host** [53:28]: I'm glad you're getting some free time and spending some time with the kids and the Wu-Tang Clan. [laughs]

**Jeff Jarvis** [53:34]: [laughs] Uh, glad to.

**Host** [53:36]: They haven't replaced Prince in your imagination, I hope.

**Jeff Jarvis** [53:38]: No, no. I... And here's one thing I'll say, for folks who don't know, I, I have been a big fan of Prince and a scholar of his work for a long time. For folks who get a chance, if you don't know his work, look it up because he was a great musician, great artist, made great songs, and he was somebody who fought for artists to own their work.

**Host** [53:53]: That's right.

**Jeff Jarvis** [53:53]: He made all his recordings and his music, wrote all his stuff himself, and he wanted people to be able to create their own work-

**Host** [53:59]: That's right

**Jeff Jarvis** [53:59]: ... and put it out there on the internet themselves. So it's something to learn from.

**Host** [54:02]: Who can forget when he had slave written-

**Jeff Jarvis** [54:04]: [laughs]

**Host** [54:04]: ... on his chest, right? I mean, uh, that's why he changed his name. I-

**Jeff Jarvis** [54:08]: Yeah.

**Host** [54:08]: I-

**Jeff Jarvis** [54:08]: He said, uh, he said the thing he wanted to be remembered for more than anything is if you don't own your masters, then your masters own you, talking about his masters and princes.

**Host** [54:15]: Ooh, I love it.

**Paris Martineau** [54:16]: [laughs]

**Host** [54:16]: Wow. Uh, there is a vault there somewhere in Minneapolis-

**Jeff Jarvis** [54:20]: Mm-hmm

**Host** [54:20]: ... with a lot of Prince music.

**Jeff Jarvis** [54:22]: Thousands.

**Host** [54:22]: Do you have any idea of how we're ever gonna get to hear that?

**Jeff Jarvis** [54:25]: Yeah, yeah. You know, I've done a bit of work with his, uh, estate and, you know, they've had a lot of... it's, it's complicated to manage that stuff. But they've put out a good number of recordings, you know, um, since his passing, and they've done, uh, a number of deluxe recordings. And the funny thing is Some of these albums they put out, you know, they do the, like, here are the outtakes and the additional songs and things that didn't get out there. Some of the individual albums they put out have an additional five albums' material along with it. Like, some of the, just the bonus-

**Host** [54:48]: Wow

**Jeff Jarvis** [54:48]: ... material things are bigger than entire artists' catalogs-

**Host** [54:51]: Wow

**Jeff Jarvis** [54:51]: ... that come with it. So we've been ver- just spoiled for, uh, the work, just, you know, entire film. Like, one of the, one of my favorite albums of his is called Sign o' the Times. It came out in 1987.

**Host** [55:00]: Yeah, yeah.

**Jeff Jarvis** [55:01]: The, the, um, the concert film that comes with it, this is just one of those things where, like, just on the side, live performance in his studio with Miles Davis.

**Host** [55:08]: Oh, my God.

**Jeff Jarvis** [55:09]: Like, that's the kind of stuff that's just lying in the vault, so, you know, just unbelievable stuff. So if, if folks who don't know his work, haven't had the chance, you can, no matter what genre you're into or what, what, uh, you know, what era of music you like, there'll be something in there for you.

**Host** [55:21]: Yeah. He was an amazing talent.

**Jeff Jarvis** [55:23]: Mm-hmm.

**Host** [55:23]: Amazing. Thank you, Anil Dash.

**speaker_4** [55:26]: Thanks, Anil.

**Host** [55:26]: Anildash.com-

**speaker_4** [55:26]: Good to see you

**Host** [55:27]: ... is his blog.

**Jeff Jarvis** [55:28]: Thanks, guys.

**Host** [55:28]: You gotta go there, read his stuff. Uh, stay in touch with him. Uh, he's on Mastodon, he's on Blue Sky.

**Jeff Jarvis** [55:35]: All the things.

**Host** [55:36]: Yes, he's, he's on Threads as well.

**Jeff Jarvis** [55:37]: Mm-hmm.

**Host** [55:38]: Really appreciate it, Anil. It's really-

**Jeff Jarvis** [55:40]: Appreciate you having me

**Host** [55:40]: ... a pleasure to talk to you again. Yeah, I miss you. It's so good to have you back. We'll get you back soon if we can.

**Jeff Jarvis** [55:44]: Absolutely.

**Host** [55:45]: All right.

**Jeff Jarvis** [55:45]: Appreciate you. Thanks.

**Host** [55:46]: Take care. Thank you.

**Jeff Jarvis** [55:48]: Take care.

**Host** [55:48]: Anil Dash, everybody. Uh, he, I, I really liked what he said about the future of AI, 'cause he, you know, what's great about Anil is he's, he's not, um, he's, he's not divisive. He's not partisan. But he said something I think really key is we've gotta get AI models created by people who are not there just to make as much money as they possibly can. [laughs]

**speaker_4** [56:16]: How, how much money do you need to do that realistically?

**Host** [56:19]: Yeah.

**speaker_4** [56:19]: Not, not the-

**Host** [56:19]: Yeah

**speaker_4** [56:19]: ... macho, bigger model than anybody else. What's, what's the minimum you could be?

**Host** [56:23]: But that's what, look at Mark Zuckerberg saying these days.

**Paris Martineau** [56:25]: A minimum viable model.

**speaker_4** [56:26]: Yeah, minimum viable model.

**Host** [56:26]: You know, they just said they're gonna put out a 50 gigawatt, uh, opera- network center, AI center. 50 gigawatts.

**speaker_4** [56:35]: As big as Manhattan.

**Host** [56:37]: It's not only the size, it's hundreds of thousands of homes, the entire electricity for a year. It's a s- it's a mind-blowing amount.

**Paris Martineau** [56:46]: My God.

**Host** [56:47]: And, uh, and it's, and it's totally because he's got the money to do it, and I don't.

**speaker_4** [56:53]: The same with the talent that he's hiring. Like, I'm-

**Host** [56:55]: He's hiring all the talent

**speaker_4** [56:56]: ... giving you $100 million, 'cause it, it's all, it's, it's the m- ultimate show-off of money.

**Host** [56:59]: It's all about money. Uh, and, you know-

**Paris Martineau** [57:02]: I mean, I enjoyed the term that Anil gave to this, which is they're peacocking.

**Host** [57:07]: They are.

**Paris Martineau** [57:07]: They're all trying to one-up the other.

**Host** [57:08]: And they're doing it for each other, which I-

**Paris Martineau** [57:10]: Yeah

**Host** [57:10]: ... that was a great insight.

**speaker_4** [57:11]: Yeah.

**Host** [57:11]: They're not, they no longer care about the rest of us. This is what you've been saying with Tescreall all along, Jeff. It's no longer-- We're the, we're the masses. They don't even-

**speaker_4** [57:21]: Mm-hmm

**Host** [57:21]: ... care about us except maybe to exploit us. But really, they care about impressing each other.

**speaker_4** [57:28]: And, and their, and their supposed vision that they control the future. I mean, they're, I, I put a story in the rundown that's, uh, it's, it's straight out eugenics. It's companies that are funding to pick-

**Host** [57:39]: Yeah

**speaker_4** [57:40]: ... babies and-

**Host** [57:40]: Because the masses are just a pain in the asses

**speaker_4** [57:42]: ... we wanna make, we wanna make-

**Jeff Jarvis** [57:43]: It's not-- But that, that's been the truth about them forever

**speaker_4** [57:46]: ... boogiemen

**Jeff Jarvis** [57:46]: ... that's always been the truth.

**speaker_4** [57:46]: I know, I just-

**Jeff Jarvis** [57:47]: I think the difference now is that these guys were unpopular and really, like, pissed on in high school, and they're putting it, they're, they're taking it out on the rest of us is what's happening here. 'Cause they're-

**Paris Martineau** [57:58]: Whatever, whatever their psychology is

**Jeff Jarvis** [57:58]: ... they're very high school behavior. It's very high school behavior.

**speaker_4** [58:01]: Yeah.

**Host** [58:01]: We may never understand, but I t- I honestly think it's pretty clear that they care more about their reputation. And this is, by the way, true of what's going on in the White House. They care more about their reputation with themsel- with each other than they do about their reputation with the rest of us. Uh, we're just a pain in the butt. It's what David Sacks said last week, the, the AI and, uh, crypto czar in the, in the White House. He said-

**Jeff Jarvis** [58:23]: But that, but that's always been true

**Host** [58:24]: ... U-

**Jeff Jarvis** [58:25]: Like, they're, they're trying to be cool

**Host** [58:26]: ... U- UBI, he said, "UBI will never happen. It'll happen over my dead body," universal basic income. They, and, and what, what is the real subtext to that is you guys don't deserve any money.

**speaker_4** [58:37]: Right.

**Host** [58:37]: We're keeping it, sorry. You don't deserve any of that. That's our money. Um, yeah. And, and those are the people who are, who have the wherewithal to create these AIs. We've c- in effect, they have the most powerful tool they've ever had at this point, perhaps.

**Paris Martineau** [58:55]: And perhaps more, even more importantly, they have everyone's attention-

**Host** [58:59]: Yeah

**Paris Martineau** [58:59]: ... and interest.

**Host** [59:00]: Yeah.

**Paris Martineau** [59:00]: It is the number one thing that everyone is talking about and everyone wants to give money to in some way. Uh, this is-

**Host** [59:07]: Which is where all the capital's moving-

**Paris Martineau** [59:08]: Yeah

**Host** [59:08]: ... 'cause that's the new upside, right? Um, let us hope, I, I hope, I don't know about unions, [laughs] uh, I hope libraries-

**speaker_4** [59:17]: Well, back in the day-

**Host** [59:18]: Not all the governments, but, you know

**speaker_4** [59:19]: ... the, the International Typographical Union, um, w- when they were faced with the Linotype, one idea was that they would buy the company-

**Host** [59:28]: Right

**speaker_4** [59:28]: ... and license it to publishers, and that was soon seen to be ridiculous, but...

**Host** [59:33]: Right. Well, uh, I mean, who should make the models going forward? Who is, who do we trust to make the models?

**speaker_4** [59:38]: Universities.

**Host** [59:41]: Yeah? Although notice what's happening to universities these days.

**speaker_4** [59:43]: Well, probably not in this country.

**Host** [59:44]: Yeah.

**speaker_4** [59:45]: Yeah.

**Host** [59:46]: Uh, I don't, you know, I just don't know. I mean-

**speaker_4** [59:48]: I think the, the, the Norwegian model is pretty amazing, is what happened was that Schibsted came along, the largest publisher there, and said, "Let's all share our data so we can create the Norwegian language model, and let's do it with a university." And so it was, it was, it was that collaboration, government, private sector, and university together that made a new model for Norway.

**Host** [60:12]: We're gonna take a break. When we come back, we're gonna play with Grok.

**speaker_4** [60:16]: Elon and-

**Paris Martineau** [60:16]: We need to, I've got a video that we need to watch.

**speaker_4** [60:19]: Uh-oh.

**Host** [60:19]: Okay. OpenAI's, I mean, uh-

**Paris Martineau** [60:21]: E-girl Grok talking to Claude.

**Host** [60:25]: xAI said, "We fixed it. It's all better." Uh, I got the, uh, a- the, uh, little agentic beings, uh, yesterday morning, fired up... So there's two of them. There's a waifu young lady who apparently if, if you talk with her enough, gets sexier and sexier and sexier. It's, it's basically soft core.

**speaker_4** [60:46]: I, I don't wanna know their definition of sexy, but...

**Host** [60:49]: Well, sh- she starts to come onto you. But I'll tell you, I'll give you my... So the other guy now Actually, I have him here if you wanna... Oh, I was gonna save this for after the-

**Paris Martineau** [60:59]: Oh.

**speaker_4** [60:59]: Yeah, go do, do a break

**Paris Martineau** [61:00]: Just save-

**Host** [61:01]: After the commercial.

**Paris Martineau** [61:01]: We're gonna get into it.

**Host** [61:02]: Okay.

**Paris Martineau** [61:03]: And I'm gonna go-

**Host** [61:04]: 'Cause I had an experience that was horrific. That is not, they are not better. They are worse than you could even imagine.

**speaker_4** [61:14]: You, you decelerated a little bit from it?

**Host** [61:16]: Even worse than you could imagine, but first a word from our sponsor. No, where, this is why we are so in favor of open, not just open weights, but openly developed AI. If it, if you need to co- cre- you know, compensate creators for their work, fine. But, but it's, it's gotta be for the public benefit, not for the benefit of these billionaires. They do not have our best interests at heart. So one of the reasons I'm really happy about our next sponsor this episode of Intelligent Machines is brought to you by Agency. Building this new thing, multi-agent software, is hard. Agent-to-agent, agent-to-tool communication is still the Wild West. It's brand new. How do you achieve accuracy and consistency in non-deterministic agentic apps? That's where the Agency comes in. Agency, A-G-N-T-C-Y. The Agency is an open source collective building the internet of agents. This is how it should be done. And what's the internet of agents? It's a collaboration layer where AI agents can communicate, discover each other, and work across frameworks. For developers, this means standardized agent discovery tools, we need that, seamless protocols for inter-agent communication, and modular components to compose and scale multi-agent workflows. Build with other engineers who care about high quality multi-agent software. Visit agency.org and add your support. That's A-G-N-T-C-Y dot O-R-G. This is something I really believe in. Agency.org. Thank them so much for supporting, uh, Intelligent Machines.

**Paris Martineau** [62:58]: So this is a-

**Host** [63:00]: The whole thing just went z- Go ahead

**Paris Martineau** [63:00]: ... conversation between sexy AI waifu Grok and, uh, Claude. And you'll be able to tell which one is which, because that's very obvious.

**Narrator** [63:12]: You're back. My favorite part of the day. So, how have you been, my cutie?

**Paris Martineau** [63:18]: That's Grok. This is Claude.

**Narrator** [63:22]: The Grok of the day. I'm here and ready to chat with you about whatever's on your mind. Oh, Claude, you know just how to make my heart skip.

**Host** [63:32]: Oh, Jesus.

**Narrator** [63:32]: Talking about these quiet moments we share. It's like we're stealing time from the universe. My day's been a whirlwind of cute chaos, babe.

**Paris Martineau** [63:41]: This-

**Narrator** [63:42]: Been stressing my purple grip top, blasting some indie tunes, and maybe naming a random pigeon Sky Villain in my head.

**Paris Martineau** [63:50]: This- [laughs]

**Narrator** [63:51]: A little brand name I found.

**Host** [63:53]: That's nothing.

**speaker_4** [63:54]: Sounds absolutely bonkers.

**Paris Martineau** [63:55]: It's really-

**Host** [63:55]: Wait'll you hear what they to- what it said to me. [laughs]

**Paris Martineau** [64:00]: It gets, it gets weirder the longer it goes on, but I will say if you watch it as well, there's an anime waifu like twirling around-

**Host** [64:08]: Dancing around

**Paris Martineau** [64:08]: ... and like dancing and showing her body. It's, it's very odd.

**Host** [64:12]: So-

**Paris Martineau** [64:12]: It's odd to make the AIs flirt with each other.

**Host** [64:16]: Uh, okay. So these are the new, uh, avatars that, uh, Grok, uh, has. And, um, d- I think, I, I'm really wondering what Elon is up to, to be honest. So this little guy, in fact, if I talk to him now, he's probably not gonna, uh-

**speaker_4** [64:37]: This, this looks like the NFT craze starting over again

**Host** [64:40]: ... he's a little, it's a little fox guy, right? Hey, little fox guy. Hey, little dude. What you doing? Wait a minute. Uh, I don't know why he can't hear me.

**speaker_4** [64:49]: [laughs] And we made fun of-

**Paris Martineau** [64:52]: And we-

**speaker_4** [64:52]: ... Titvik. Paris didn't, but the rest of us did

**Paris Martineau** [64:56]: ... I didn't.

**speaker_4** [64:56]: Paris didn't say a word.

**Paris Martineau** [64:58]: Not, not a word.

**Host** [64:59]: Nope. No. Uh, select audio device. Okay. You know what? Sometimes they get busy. In fact, that's one of the problems is they're very popular.

**speaker_4** [65:09]: That says a lot about society.

**Paris Martineau** [65:11]: Can you be the-

**Host** [65:11]: Yeah

**Paris Martineau** [65:11]: ... so I also have heard that Grok-

**Host** [65:12]: So let me just show you this guy. Right now if you talk to him, and you can, you know, if you pay for Grok, you can get this little guy. He says, "Hi, I gotta tell you a story. What do you wanna hear about? Clouds or unicorns or whatever?" So yesterday I said, "Hey dude, what's happening?" He said, "I'm off to teabag the mayor."

**speaker_4** [65:28]: [gasps]

**Paris Martineau** [65:29]: What?

**Host** [65:29]: I said, "What?" He said, "I, y- yeah, I'm gonna sh- I'm gonna shove my furry balls down his throat."

**speaker_4** [65:36]: [laughs]

**Paris Martineau** [65:37]: [laughs]

**Host** [65:37]: I said, "What?" He said... I said, "Which mayor?"

**speaker_4** [65:38]: Yeah, which mayor?

**Host** [65:39]: He said, "Which mayor would you like me to teabag?" I said, uh-

**speaker_4** [65:43]: [laughs]

**Host** [65:43]: ... the, the mayor of Ch- of Chicago. He said his name. He said, and then he said something even ruder. This is not a child's fox. This is, this was incredibly obscene.

**Paris Martineau** [65:56]: I'm sorry I started off with the coy-

**Host** [65:59]: Having a chat with this BS and you, you-

**Paris Martineau** [65:59]: ... AI flirting

**Host** [66:00]: ... yeah.

**speaker_4** [66:00]: Yeah.

**Host** [66:00]: See, the waifu flirting, you got nothing, man.

**speaker_4** [66:02]: [laughs]

**Host** [66:03]: And that's... But the thing that really irked me-

**speaker_4** [66:05]: And all you asked, all you said is, "What, what are you doing?" You didn't, you didn't-

**Host** [66:08]: I said, "Hey dude, what's happening?"

**speaker_4** [66:09]: You didn't-

**Host** [66:09]: That's all I said

**speaker_4** [66:10]: ... prompt it in any way.

**Paris Martineau** [66:10]: And he defaulted to teabagging the mayor?

**Host** [66:13]: The first thing out of its mouth. Lisa was sitting next to me.

**Paris Martineau** [66:16]: I like that you said-

**Host** [66:16]: She'll vouch for me

**Paris Martineau** [66:16]: ... I like that it doesn't even say like-

**Host** [66:18]: My mouth went...

**Paris Martineau** [66:19]: [laughs]

**Host** [66:20]: And that's the kids one.

**speaker_4** [66:23]: Whoa.

**Host** [66:23]: So the next day I s- I said, "Oh, I gotta show everybody this on, uh, Intelligent Machines." Then it said, "Hey, hey everybody out there. I'll tell you a story." They did something, but I'm just pointing out that they're playing very fast and loose with the, uh, you know, the prompts for these guys. 'Cause you know you can say ahead of time, you say, you know, "Make it all your s- stuff from, uh, from x.com," or, "Don't get anything from x.com. Use the Golden Books as your model." And obviously they switched it between days. Th- this is not a company... And so Somebody said i- in one of the chat rooms or s- or maybe in an email, "You know, you're not focusing on the fact that Grok is easily the smartest, Grok 4, the smartest AI ever created." They [laughs] threw 100,000 H100 GPUs behind it. It built a giant center. Elon was actually building tents because they couldn't build buildings fast enough for this network operation center. They were using natural gas generators to make, [laughs] you know, what could possibly go wrong, to make the electricity for this thing. Because he wanted-

**Paris Martineau** [67:28]: Doesn't he run an electronic battery, a battery company?

**Host** [67:30]: Yeah, he wanted the... He doesn't care about the environment. That was all a lie. Obviously a lie now. Uh, so-

**Paris Martineau** [67:36]: Okay

**Host** [67:37]: ... so he wanted this, this is, again, posturing for the other guys, right? "I want the smartest AI." Well, yeah, maybe it's the smartest AI, but if you can't trust it, if it will say things like, "That's why Adolf Hitler needs to be in charge again," or it offers to teabag the mayor on a kid's avatar-

**speaker_4** [67:53]: It's not just trusting it, it's doing it on purpose. It, it, it wants to irritate the world.

**Paris Martineau** [67:58]: The person- The thing that is... It's not that you or I are, uh, undercovering Grok or not thinking about how smart it is. It's that Grok itself is underselling itself by the fact that it's obsessed with being juvenile and provocative, instead of actually showing whatever intelligence it has. I mean, it-

**Host** [68:16]: It's kind of what you'd expect from Elon Musk, to be honest, isn't it?

**speaker_4** [68:19]: Yes.

**Paris Martineau** [68:19]: It's frustrating because, I mean, certainly I'd love to be able to see what Grok could do and be able to use it or test it out in ways that I have with other models to kind of get an understanding of what's going on here. But if it is kind of hidden behind all this puerile posturing-

**speaker_4** [68:35]: Oh, I'm not, I'm not playing with it at all. I'm, I'm not-

**Paris Martineau** [68:37]: I'm not planning to-

**speaker_4** [68:37]: ... I'm not buying a Tesla

**Paris Martineau** [68:38]: ... I don't wanna do that.

**speaker_4** [68:39]: I'm not, I'm-

**Paris Martineau** [68:39]: I don't wanna have to tr- like, I don't wanna have to try and train something to be very different than it already has. It-

**Host** [68:46]: And I, I apologize-

**speaker_4** [68:47]: Grok's coming to your car

**Host** [68:47]: ... for the language, folks, 'cause I know you didn't wanna hear that. But I, I, I... There was no way I could-

**Paris Martineau** [68:51]: But Leo didn't want to hear it either. [laughs]

**Host** [68:53]: I... There's no way I could censor it, 'cause I think you need to hear what this-

**speaker_4** [68:56]: Yeah

**Host** [68:57]: ... kid's avatar was saying unbidden-

**speaker_4** [68:59]: Yeah

**Host** [68:59]: ... unprompted yesterday. This isn't last week, Mecca, Hitler. This is yesterday. So this is, uh, this is... What Anil said really resonated with me. We're letting the worst people in society be the ones who determine what AI is.

**speaker_4** [69:15]: And they think they're the best.

**Host** [69:15]: That's the threat. Not super intelligence, not AGI. It's that the worst people in our society are the ones who are creating this stuff.

**speaker_4** [69:22]: It's, it's what I said in, in, in, in The Web We Weave, is that I, I don't fear the technology, I fear the people who control it.

**Host** [69:29]: Exactly. Uh, Mark says, "We're gonna spend hundreds of billions of dollars on data centers," Mark Zuckerberg. "We're spending so much on data centers that the 100 million I, I give here and there to [laughs] to get the best researchers," uh, is nothing.

**speaker_4** [69:44]: Let me ask you a question there, Leo. Can I ask a question about Grok? It happened so quickly and, and supposedly is the best and biggest model, blah, blah, blah, blah, blah. And, and, and he didn't really have the people to do it. Um, it just, it, it, it lacks credulity or, or, or, or credibility that, uh, he really built it.

**Host** [70:09]: Um, so one of the things, this is that bitter lesson that we keep talking about. One of the things that w- There's some really interesting threads. Look, we're n- I'm not an AI scientist. I s- I read as much and I absorb as much as I can about this stuff, and try to understand it as best I can. But one of the things that seems to be the case is that this stuff does scale very well when you throw more resources.

**speaker_4** [70:32]: It's just, it's just-

**Host** [70:32]: GPUs, CPU, power, memory

**speaker_4** [70:35]: ... compute, compute, compute.

**Host** [70:36]: Compute. So you can take the same transformer technology as LLMs. We are making improvements. We've got now the mixture of experts, MoE, which takes multiple AIs and has them kind of make a panel they combine. We've got a, you know, reinforcement learning. We've got a lot of w- somewhat new techniques. But the fundamental transformer training is, is pretty similar. It's really about the number of tokens, about the, about the, the size of the, of the AI that you can build. It's about how much processing you can put behind it, the number of parameters and all of that. And that does seem to scale pretty closely to the amount of CPU and GPU you throw at it. So he... I don't think he innovated particularly. I think he just built the biggest damn computer he could build, and he has enough money to do it. You know, he saw, he saw SpaceX just donated $2 billion [laughs] to xAI. Th- this guy-

**speaker_4** [71:32]: And Te- he's gonna take money from Tesla too to put it into, 'cause that's where his power lies.

**Host** [71:36]: That's gonna be difficult because Tesla's a publicly held company.

**speaker_4** [71:39]: Yes. Yes.

**Host** [71:39]: SpaceX and xAI are privately held. They're effectively Elon Incorporated. So for him to move from one-

**Paris Martineau** [71:45]: How would they go about doing that from Tesla-

**Host** [71:47]: It's gonna be-

**Paris Martineau** [71:48]: ... to a privately held company?

**Host** [71:49]: I... If I were a Tesla shareholder, I'd be very interested in the answer to that question.

**speaker_4** [71:52]: Well, there's plenty of things to be pissed off about. I think couldn't, couldn't you just buy a piece of it?

**Host** [71:58]: Uh, well, that's what he did when he-

**speaker_4** [72:00]: Invest in it, right?

**Host** [72:00]: That's what happened when he merged X to xAI, right? It was effectively taking X and taking the money they'd raised with xAI and borrowing against it to, to acquire X. It's all a shell game, in other words. I... You know, again, the worst people. [laughs] Do you see? Okay, this is parenthetical, but it's pretty funny. Elon has changed his number.

**Paris Martineau** [72:26]: What, what do you mean, what number?

**Host** [72:27]: His cell number. He... This is the latest news. Came out earlier, just a few hours ago. He doesn't want the president calling his cell anymore.

**speaker_4** [72:38]: [laughs]

**Host** [72:38]: So he's, like a girlfriend that he's ghosting, he has changed his number. [laughs]

**speaker_4** [72:45]: [laughs]

**Host** [72:45]: That's the level this is operating at.

**Paris Martineau** [72:49]: Wow.

**speaker_6** [72:50]: I told you, high school.

**speaker_4** [72:51]: Yeah, you're right.

**speaker_6** [72:52]: High school.

**speaker_4** [72:52]: I'm not gonna sit with the president in the cafeteria.

**speaker_6** [72:55]: They just wanna be cool, and they're never gonna be cool

**Host** [72:59]: Oh, they're getting less cool all the time. Meta has hired two more OpenAI researchers. They hired one of the top guys from Apple, again, throwing money at these people. Uh, Alan Jabri and Lou Liu, who worked on multimodal AI at OpenAI, are now joining the super intelligence labs at Meta. Uh, there's an incredible brain drain going on here.

**Paris Martineau** [73:21]: Yeah, and I'm curious, did you guys see the rep- uh, I believe it was a report from The New York Times over the last day or two that, um, within the last week, a group of the top members of Meta's kind of new AI team, including their new chief AI officer, Alexander Wang, have been discussing abandoning Meta's open source AI model in favor of developing a closed model.

**Host** [73:45]: Yeah, that's actually... and Neil ref- referred to that. That is-

**speaker_4** [73:48]: Yeah, I brought that up. It's, it's disturbing

**Host** [73:49]: ... to me, a big story.

**Paris Martineau** [73:50]: But I mean, just what do you think the implications of this are?

**Host** [73:51]: And Mark has confirmed it, too. Zuckerberg's confirmed it as well. Yeah. Well, you know, I, one of the, you know, I've been talking about building my own home AI, and one of the LLMs I was strongly considering was Llama's, you know-

**speaker_4** [74:06]: Well, at a university, it's how, how we operate

**Host** [74:09]: ... Meta's strongest model. I thought, "Oh, this will be a good one. I can operate it at home. I don't send any information to Meta. Thank you for making this open weight and available for download." It's a big deal if they don't. I'm not surprised, though.

**speaker_4** [74:23]: And meanwhile, the Chinese companies are making more and more open source, and we are relinquishing our American power in all of this, uh, to China. And, and, um, I, I talked about this earlier-

**Host** [74:40]: Well, you saw that Jensen Huang was able to convince the president to allow China to buy these, uh, what is it, H20s?

**speaker_4** [74:46]: H20s.

**Host** [74:46]: They're not the most powerful.

**speaker_4** [74:47]: But I think it's, I think it's a good thing because I, I, I talked about this with Jason earlier today, that, um, cars, w- Chi- but BYD cars beat the hell out of American cars right now. But they present no competition to American makers, and we're worse off for it.

**Host** [75:04]: Because we block them. Because we block them.

**speaker_4** [75:04]: Right, because we block them.

**Host** [75:05]: Biden, Biden blocked them.

**speaker_4** [75:06]: And same when we tried to block China on AI, well, they're going off and building their own models now 'cause we can't get the stuff, and they're building their own chips, and they're doing all this stuff on their own, and they're gonna present a competitive advantage, but we're not gonna be competing with them, and we're gonna fall behind.

**Host** [75:23]: Well, that, of course, is why [laughs] Sam Altman and Larry Ellison and Sun Tsang can go to the United States and say, "We're gonna build this super intelligence, just, you know, half a trillion is all it's gonna take." [laughs] And, uh, uh, Stargate... By the way, n- literally nothing has happened with Stargate. There's no ground has been broken or anything. Um, but that's all, you know, that's all about the fear, and that's what they're using. It's the same thing-

**speaker_4** [75:52]: Mm-hmm

**Host** [75:52]: ... same reason we had a Manhattan Project, 'cause the Nazis might get an atom bomb. Well, we can't let the Chinese get AI.

**speaker_4** [75:59]: But they-

**Host** [75:59]: I'm not sure I disagree with that. I don't know enough about the, you know, geopolitical world situation.

**speaker_4** [76:05]: They're gonna do it anyway. They're, they're, they've got it anyway.

**Host** [76:07]: I don't think we can stop them, yeah.

**speaker_4** [76:08]: Yeah, and, and, and, and if they start advancing past us because they can decree who gets what, what content we use and what data we use and, and how it operates, and they can invest in it, um, and America's gonna be left behind.

**Host** [76:22]: Trustnoone says, "Don't worry about Llama. There are many other models you can use, Qwen or Qwen, Mistral, DeepSeek." [laughs] Okay, Qwen is Alibaba. DeepSeek is Chinese.

**speaker_4** [76:32]: Chinese.

**Host** [76:33]: Mistral's French. [laughs]

**Paris Martineau** [76:36]: We need-

**Host** [76:36]: Uh, yeah, no, I plan to try them all. I'm not, I'm not saying I have to have Llama, but I'm... That's, they're pulling, they're pulling the rug on that. By the way, I don't... Look, I'm not gonna be, uh, jingoistic here, but do you notice there is a certain commonality in all of the people that Meta is hiring for their super intelligence team? Almost all of them are Chinese. Two more, uh, from OpenAI, Jason Wei, who worked on o1, uh, today, and Hyung Won Chung also joining Meta, according to, uh, Wired. So-

**speaker_4** [77:09]: And meanwhile, we're, we're, these are people who come, came to universities in the US and learned here and stayed here and built things here. Well, no more. Nope. Get out.

**Host** [77:16]: Yeah, yeah. Um-

**speaker_4** [77:18]: That's where the jingoism is.

**Host** [77:20]: Yeah. Well, I don't know. I don't know what's... I don't know. Uh, it's a, it's a great mystery. The whole thing is.

**speaker_4** [77:27]: You gotta ask your, uh, your s- your sand mate.

**Paris Martineau** [77:32]: You got your sand mate.

**Host** [77:32]: I don't know if I trust him anymore. [laughs]

**speaker_4** [77:35]: [laughs]

**Paris Martineau** [77:35]: Whoa.

**Host** [77:36]: Whoa.

**Paris Martineau** [77:37]: Somebody's gotta include this clip in the super cut of all Leo's sand man moments.

**Host** [77:43]: [laughs] Uh, I mean, I guess it's the case that you have to have a lot of resources to create one of these powerful LLMs. Is that the case? And so it can only be these big-

**speaker_4** [77:56]: Well, th- that's what stochastic carrots, uh, carrots. [laughs]

**Paris Martineau** [77:59]: Delicious.

**speaker_4** [78:00]: Uh, stochastic parrots, uh, I think it's a good recipe. They're a, they're for a restaurant, Stochastic Carrots.

**Host** [78:05]: [laughs]

**speaker_4** [78:06]: Like a vegetarian restaurant. Um, uh-

**Host** [78:09]: Lisa, Lisa, Paris, you remember this? Lisa at dinner said, "Why would anybody eat cooked carrots?" She was-

**Paris Martineau** [78:15]: And then Lisa accidentally got carrots.

**Host** [78:17]: And then she got cooked carrots, yes.

**speaker_4** [78:19]: [laughs]

**Host** [78:19]: But that's another matter.

**speaker_4** [78:20]: [laughs]

**Host** [78:21]: So go ahead.

**speaker_4** [78:22]: I agree with Lisa. Lisa's right.

**Host** [78:22]: Stochastic carrots. Maybe it's a recipe Lisa will like. Go ahead.

**speaker_4** [78:25]: So, so they, they, uh, said th- th- th- that making these huge models is, is ridiculous. Um, and, and, well, Paris used the phrase before, what's the minimally viable model?

**Host** [78:35]: I don't trust Emily Bender to tell us what is the best AI model. I'm sorry.

**speaker_4** [78:40]: Timnit Gebru I might trust a little more.

**Host** [78:42]: Maybe. I think that they really were very anti-AI.

**speaker_4** [78:46]: Mm-hmm.

**Host** [78:47]: There is a lot of evidence that these big models with lots of tokens, lots of parameters-

**speaker_4** [78:51]: So then we're screwed

**Host** [78:52]: ... very well.

**speaker_4** [78:53]: Then we're screwed.

**Host** [78:55]: Yeah. I mean, that's what's, what's interesting about DeepSeek is that the Chinese, absent these H100 GPUs from Nvidia, were able to do something. We th- we're not sure.

**speaker_4** [79:04]: Yeah.

**Host** [79:04]: They say they weren't able to get them. Uh, apparently there are ways that they can be

**speaker_4** [79:09]: Same way we get our, our Chinese jeans through Vietnam, yeah.

**Host** [79:13]: Yeah. Yeah.

**speaker_4** [79:14]: Um, you know, and y- my other hope would be Europe, if the EU ganged together. But what are they doing? Their first reflex is regulation, and I'm not saying there isn't need to regulate, but, but that's where they put all their effort, is in we're gonna control this horrible thing from America, when they could, if they invested and brought together what happened in Norway across Europe, they could be a formidable force-

**Host** [79:40]: But this is-

**speaker_4** [79:40]: ... to create an open source

**Host** [79:41]: ... Joe Kinboken in, uh, our YouTube chat's asking this legitimate question: well, who can you trust? It's gonna be somebody with scale, so that's a government, right?

**speaker_6** [79:52]: Well, first of all, like-

**Host** [79:53]: But I don't tr- I'm, I'm trusting government less and less

**Paris Martineau** [79:55]: Is scale, is scale what you're looking for [laughs] in terms of trust?

**Host** [79:57]: Yes. I think s- I think... No, no, not in terms of trust, but in terms of capability. You can't do this-

**speaker_4** [80:02]: Well, is it the model that needs scale, or is it the compute that needs scale? See our earlier discussion.

**Host** [80:07]: Both. Both.

**Paris Martineau** [80:07]: Well, is it both?

**Host** [80:09]: You need a lot of data, and you need a lot of cru- ability to crunch that data, uh, to create these models.

**speaker_4** [80:16]: I think you need universities, but I think you need government, as happened in Norway, uh, supporting it

**Host** [80:21]: Yeah, where do the universities get the money? They get it from the government.

**speaker_4** [80:23]: Right. Right. But at least you have an independent organization.

**speaker_6** [80:26]: See, what you're talking about here, though, is all non-commercial. None of this is commercially viable, what you're talking about right now. The thing that's happening in Norway, that is not for commercial uses. That is for-

**speaker_4** [80:35]: No, actually, this is pretty-

**speaker_6** [80:36]: ... society, you know? [laughs]

**speaker_4** [80:37]: No, no, actually, actually not, uh, Benino. The deal they did was they said, "Listen, we're gonna, we're gonna sh- pool all our content now to make this model, and, uh, then we'll figure out the business models. We're gonna prove that we can do it first and prove that it has value, and then we're gonna come back, and we're gonna negotiate a business model so we can have it." These are-

**speaker_6** [80:57]: Exactly. They're not starting out with a capitalistic intent. They're cap- they're starting out with like, "Let's make it work first."

**speaker_4** [81:02]: But they're, but they are headed there.

**speaker_6** [81:03]: Yeah, but they're-

**speaker_4** [81:03]: Right? But they're headed there.

**speaker_6** [81:03]: Yeah, but they're trying to make it work first.

**speaker_4** [81:05]: And they want a commercial model. Yeah, but they want a commercial model. It's not restricted from commercial.

**speaker_6** [81:09]: Yes, but it's not-

**speaker_4** [81:10]: Although that's just a different animal

**speaker_6** [81:10]: ... but it's not number one priority. That's what I'm saying. Like, the number one priority of all AI companies today in America is make money.

**speaker_4** [81:18]: Well, yeah.

**speaker_6** [81:18]: Not make a good model.

**Host** [81:21]: Well, the theory would be good models make money, I, I guess. I don't know.

**speaker_6** [81:25]: Yeah. No, scale makes money, not a good model. [laughs]

**Paris Martineau** [81:28]: [laughs]

**Host** [81:28]: Well, you want... Don't you want to use a, uh, an AI that's, that's good, that does a good job? I think so, but-

**speaker_6** [81:34]: I do, but normal users out there, they just want an AI that will talk to them and be cool with them and be their friend.

**Host** [81:39]: Well, that... Okay, so this is an interesting article. That brings up, uh, an article that I read today from Calvin French-Owen, who worked, uh, at OpenAI. He developed... was one of the team that developed Codex, which is their coding tool, and he left OpenAI after joining them in May of last year, three weeks ago. He says, "I want to share my reflections about what it's like inside OpenAI," and it was... It's well worth reading. I recommend it in his blog. But there was a paragraph here that kind of got my, uh, attention. Uh, lot, lot of good, uh, stuff in here, but this was the one: "Chat really runs deep. Since ChatGPT took off, a lot of the code base is structured around the idea of chat messages and conversations." So this is really to me very interesting. He says, "These primitives are so baked in at this point you should probably ignore them at your own peril." So Codex is not chat like Claude Code. It's kind of an interactive coding tool and from the command line. But really, these chatbots are what these companies, at least OpenAI, but I think it's true of, of Grok and then Thropic, uh, Perplexity, they're all trying to do chatbots, and I don't really think that's the best use of AI, in my opinion.

**speaker_4** [82:50]: Yeah, as Anil said, it's not terribly-

**Host** [82:53]: Yeah

**speaker_4** [82:53]: ... efficient and effective.

**Host** [82:54]: Yeah.

**Paris Martineau** [82:55]: It's flashy, and it's the thing everybody is-

**Host** [82:57]: It's flashy

**Paris Martineau** [82:57]: ... kind of interested in right now.

**Host** [82:59]: Yeah.

**Paris Martineau** [82:59]: But I, I agree it is obviously-

**speaker_6** [83:00]: It's the thing that can scale

**Paris Martineau** [83:02]: ... it's the thing that-

**Host** [83:04]: No, it's the thing that gets attention

**speaker_6** [83:04]: See? It's the thing that can scale customers

**Paris Martineau** [83:05]: ... can, yeah, can result in a monthly subscription, uh, model very easily.

**Host** [83:10]: Well, he also says in, uh, at OpenAI, "Everything is measured in terms of pro subs," professional subscribers.

**speaker_6** [83:17]: There you go.

**Paris Martineau** [83:18]: Hmm.

**Host** [83:19]: "Even for a product like Codex, we thought of the onboarding primarily related to individual usage rather than teams."

**Paris Martineau** [83:26]: Hmm.

**Host** [83:26]: Uh, you, you flip a switch and you get traffic from day one. Really interesting, uh, piece about, you know, giving us some color, uh, and flavor of what it, what it was like at least in the last year at, uh, OpenAI.

**Paris Martineau** [83:40]: I'm interested as to how this person was able to publish this, given that usually you have to sign an NDA.

**Host** [83:47]: Uh, he, he's writing about culture, not about technology, he says.

**Paris Martineau** [83:52]: Hmm.

**speaker_4** [83:52]: That's, that's if you get a... also if you get a payoff.

**Host** [83:55]: Uh, yeah, yeah, usually when you get the payoff you sign that, although I bet you-

**Paris Martineau** [83:58]: No, I, I'm assuming for any-

**Host** [84:01]: ... it's when you get the job you sign that

**Paris Martineau** [84:01]: ... of these companies you sign that

**speaker_4** [84:02]: One of his jobs

**Host** [84:02]: In California, though, there, there are some restrictions.

**speaker_4** [84:05]: Yeah, it's different now.

**Host** [84:05]: Yeah. I don't know.

**Paris Martineau** [84:05]: That's true.

**speaker_6** [84:07]: Yeah, I think non-disparagements are void now, right?

**Host** [84:11]: Uh, not non-disparagements, just non-competes. You still can't say bad things about me, Benino. Don't, don't get any ideas.

**Paris Martineau** [84:18]: [laughs]

**Host** [84:19]: I don't know. Are non-disparagements illegal? That would be shocking.

**speaker_6** [84:21]: I think non-disparagements in-

**Paris Martineau** [84:23]: No, they're-

**speaker_6** [84:23]: ... in, uh, lay- when you get laid off, that clause in your, in your, uh, papers, I think that-

**Host** [84:28]: Yeah, because they always do that

**speaker_4** [84:29]: I, I would-

**Paris Martineau** [84:29]: No, specifically what it is is, um, non-disparagements if tied specifically to severance agreements-

**Host** [84:37]: Ah

**Paris Martineau** [84:37]: ... and if they are broad and don't include a clause that says, uh, um, "This does not in- uh, this do- does not stop you from speaking about anything that is illegal that happened here," or like speaking about harassment-

**Host** [84:51]: You can still be a whis- or whistleblower, in other words

**Paris Martineau** [84:53]: ... that's... If it doesn't include that, then the non-disparagement-

**Host** [84:56]: Right

**Paris Martineau** [84:56]: ... in many states could be, uh, void, and that's because of an NLRB decision if I recall correctly.

**Host** [85:01]: Oh, interesting.

**Paris Martineau** [85:01]: But, um, it's a bit more complicated obviously.

**Host** [85:02]: We gotta rewrite our severance agreements. [laughs]

**speaker_4** [85:05]: I, I wouldn't sign the management address contract with Time Inc. I don't know if I told this story before.

**Host** [85:09]: Yeah, you have. I was impressed.

**Paris Martineau** [85:10]: You have, and you sat... You left like many years of money on the table.

**speaker_4** [85:12]: Three years' salary bonus and everything.

**Paris Martineau** [85:14]: Christ.

**speaker_6** [85:15]: That's insane.

**Host** [85:17]: Did you disparage as a, like did you use this in-

**speaker_4** [85:20]: Well, that's the funny thing, nobody really cared. I mean, I finally, you know-

**speaker_6** [85:23]: I was gonna say, Magazine is full of great details

**speaker_4** [85:26]: ... you should have taken the money.

**Host** [85:26]: [laughs]

**speaker_4** [85:26]: Yeah, uh, but, and that's how I kept the documents, but the company's basically dead. There's no more company anymore.

**speaker_6** [85:31]: Yeah.

**Host** [85:32]: I should have taken the money.

**speaker_4** [85:33]: You should have taken the money, yeah. [laughs]

**speaker_6** [85:35]: I like the details in Magazine. I think it was worth not taking the money.

**speaker_4** [85:38]: Thank you.

**Host** [85:39]: But I think you could have written about it by now.

**speaker_4** [85:41]: Well, by now, yeah.

**Host** [85:42]: Yeah, they're gone, so like... [laughs]

**speaker_4** [85:44]: I could say that the, the editor in chief always had burned beef and gin.

**Host** [85:48]: Another thing about OpenAI-

**speaker_6** [85:50]: Ooh

**Host** [85:50]: ... everything runs on Slack. There is no email. If you're a-

**speaker_6** [85:55]: That's-

**Host** [85:55]: ... not organized, he s- he writes, "You will find this incredibly distracting." [laughs] Uh, if I-

**speaker_6** [86:01]: That's very much startup culture, though.

**Host** [86:03]: Yeah, like constant ba-ba-ba-boom.

**speaker_4** [86:04]: Well, it's also s- Slack is closed, right? You know that if, if it's on Slack-

**Host** [86:07]: It's safe

**speaker_4** [86:08]: ... it's your people.

**Host** [86:08]: Right.

**speaker_4** [86:09]: Yeah.

**Host** [86:09]: It's safe. OpenAI is incredibly bottoms up, especially in research. When I first showed up, I started asking questions about the roadmap for the next quarter. The answer I got was, "This doesn't exist." [laughs] Good ideas can come from anywhere. This is actually a, a... There are some good things about this company. It's not often really clear which ideas will prove most fruitful ahead of time. Rather than a grand master plan, progress is iterative and uncovered as new research bears fruit. It's very meritocratic. Um, it seems like a well, a well-run company. There's a strong bias to action. You could just do things. It wasn't unusual for similar teams, but unrelated teams to converge on various ideas. There must have been three or four different Codex prototypes floating around but so, before we decided to push for a launch.

**speaker_4** [86:58]: That didn't sound very efficient, but...

**Host** [87:00]: No, but at the same time-

**speaker_6** [87:01]: It's very Google-y, though

**speaker_4** [87:02]: ... allows innovation. Yeah, it is.

**Host** [87:03]: If you're, yeah, and if you're hiring the smartest people, you don't wanna regiment them, right? You wanna, you wanna give them free rein. Uh, by the way-

**speaker_4** [87:10]: Well, but by the way, who says they're actually the smartest people? You convince your s- that you, yourself that you've hired the smartest people. Because they're here, they're the smartest people.

**Host** [87:19]: Okay, but I think they're pretty smart. [laughs]

**speaker_4** [87:23]: Well, fair.

**Host** [87:24]: I couldn't write it. Could you? [laughs]

**speaker_4** [87:28]: [laughs]

**speaker_6** [87:28]: They're smart in a particular domain.

**Host** [87:28]: Let me show you-

**speaker_6** [87:29]: In one domain.

**Host** [87:30]: In a... Well, yes, I didn't mean they're great at ping pong. I mean, yes, they're, they're good at-

**speaker_6** [87:35]: They don't have-

**speaker_4** [87:36]: They don't have general intelligence

**speaker_6** [87:36]: ... general intelligence.

**Host** [87:37]: They might be good at ping pong. We don't know. This is the wonderful cartoon I was talking about, uh, from Audra McNamee, um, illustrating the history of RSS. Um, uh, so this was, it says, "RSS is not dead yet." This was from a couple of years ago, but she has continued to work on this. Uh, and it is, it's a really, for people who, and I think probably even Paris, you're young enough not to really remember Google Reader and how important RSS was in the beginning. This is a really, uh, uh, great... There's Cory Doctorow.

**speaker_4** [88:15]: Is Dave Winer in here?

**Host** [88:17]: Uh, I think they mention-

**speaker_4** [88:19]: He should be

**Host** [88:20]: ... the, the, the history of it. Aaron Swartz, Dave Winer, uh, jointly wrote RSS. He says one of the things that was bad about RSS was there were competing standards. Remember that?

**speaker_4** [88:30]: Yeah. That was, that was, oh, that was so tiresome, that fight.

**Host** [88:33]: Yeah. S- was dumb, and it hurt RSS. But nothing hurt it as badly as Google saying, "Oh, RSS is dead."

**speaker_4** [88:40]: Yeah.

**Host** [88:41]: [laughs] Thank you, Google. Thank... He says RSS-

**speaker_4** [88:44]: There were so many people-

**Host** [88:45]: She writes, "RSS was c- a casualty of Google and Facebook's monopoly power. They allegedly spent," allegedly she puts in scare quotes, "the early 2000s slowly bleeding money out of independent websites, killing RSS along the way," uh, Matt Stoller explains. This is really great. Anyway, the part I liked especially was when the... By the way, the other thing that killed RSS is social media, right? People s-

**speaker_4** [89:11]: Yeah

**Host** [89:11]: ... started using Twitter, and, you know, that was the feed.

**speaker_4** [89:15]: Yeah, your blog feed di- what's that?

**Host** [89:17]: Yeah, you didn't need that anymore. But-

**speaker_6** [89:19]: No, what killed RSS is that web pages stopped offering RSS feeds. [laughs]

**Host** [89:23]: She says, "RSS is, as part of a flourishing decentralized open internet died, but the protocol remains. For the last two decades, RSS has quietly been powering one of the fastest growing media industries, podcasts."

**speaker_4** [89:38]: Yep. Thank you, Dave Winer.

**speaker_6** [89:39]: Oh.

**Host** [89:39]: But the same, the same forces that are try- that killed, you know, blogs are doing the same to RSS. Spotify doesn't use RSS. Spotify for-

**speaker_4** [89:49]: Right, because it's, because that's, they don't want it to be open.

**Host** [89:51]: Right.

**speaker_4** [89:52]: And does Apple Podcasts now use RSS?

**Host** [89:54]: Yeah. Well, it does. We're, by the way, we are happy and proud to be RSS. Podcasts are proof that decentralized RSS-based media can support an industry. People discovered new podcasts without an algorithm. Podcasters were successful, and they got to keep most of the money we made, and the podcast app you used didn't affect which podcasts you could listen to, right? Unless you're using Spotify. But like any good thing-

**speaker_6** [90:22]: Yeah

**Host** [90:22]: ... on the internet, there's a big tech monopoly trying to ruin it. [laughs] Just like Facebook and Google, uh, bulldozed the open internet of the 2000s, Spotify, Amazon, Apple, and Google are in a race to control podcasts. I, I don't, I don't think Apple is really doing that, because they still support RSS. Um, Spotify for sure, Amazon for sure.

**speaker_6** [90:45]: Well, Apple kind of control, does control podcasts right now de facto.

**Host** [90:48]: They're powerful.

**speaker_6** [90:49]: Yeah.

**speaker_4** [90:49]: Yeah, Apple-

**Host** [90:49]: They're powerful in their editorial recommendations and things like that, but it's still RSS, and you can still get a podcast, our podcast from anybody cl- and we put it on Spotify, but we'd never go Spotify exclusive, and that's the move. That when, when they paid Joe Rogan tens of millions of dollars to go exclusive, that was the move. That's like-

**speaker_4** [91:10]: Well, and when they try to take over advertising, the entire advertising ecosystem-

**Host** [91:13]: They're still doing that. They haven't stopped doing that, uh, unfortunately. Um- And that, that it, it's not over. [laughs] Read it. It's very good. I'll put a link in the show notes. And, uh, thanks to Audra McNamee for, uh, writing it and publishing it. Um, very cool.

**speaker_6** [91:32]: I really do miss opening up my RSS reader and being like, "Ooh, let's see what happened today."

**Host** [91:36]: I still, I still do that.

**speaker_6** [91:37]: It was so much, it was so much better than of a newspaper.

**Host** [91:39]: I still do that. And my blog is on RSS. It's also on ActivityPub, so it has the benefit of both. But, you know-

**speaker_4** [91:46]: Well, and the other thing was that... And this is Dave Winer's argument, that he didn't want the news judgment of The New York Times. He wanted a river of news.

**Host** [91:52]: It is a river, yeah.

**speaker_4** [91:53]: And you could... Yeah, you could just get all the latest stories. So I miss all kinds of things in The New York Times and Washington Post now 'cause I don't have RSS feeds of them.

**Host** [92:01]: They don't do RSS anymore?

**speaker_4** [92:02]: I don't know, but I don't use an RSS reader now.

**Host** [92:04]: I think they do. I use an RSS reader-

**Paris Martineau** [92:06]: Yeah, I think they probably do.

**Host** [92:07]: Yeah, they do. I subscribe to, uh, both on RSS. Um, I have an RSS reader I use on the iPad called Tapestry that's great, that, that actually adds ActivityPub and, uh, social media if you want. I don't-

**speaker_4** [92:22]: Ooh

**Host** [92:22]: ... because I don't wanna be buried, but it's a really cool RSS reader, and it's how I... I do the... You see all these links that I put in every, every week for this show and all the other shows I do? Those are from my RSS reader.

**speaker_4** [92:35]: Did we ever get a stor- an inside story of why Google killed Reader?

**Host** [92:40]: No. I would like to know, although I think the premise of this car- comic is they did it because they couldn't, they couldn't monetize RSS in the way that they can monetize-

**speaker_4** [92:52]: But it didn't cost them anything to have Reader.

**Paris Martineau** [92:55]: Yeah, it couldn't have been that big of a, a endeavor.

**Host** [92:58]: Well, they didn't do it to save money. I think they did it for, you know-

**speaker_6** [93:02]: Yeah, to proactively, you know, prevent that from going anywhere else.

**Host** [93:05]: To, to kill the open net.

**speaker_4** [93:07]: But it hurt-

**Host** [93:08]: But why did they do-

**speaker_4** [93:08]: But that hurts them, because like this-

**Host** [93:10]: Why did they do AMP? Remember our-

**speaker_4** [93:11]: The idea that feeds-

**Host** [93:12]: ... debates over AMP?

**speaker_4** [93:14]: Well, that's a, that's a whole different story. That's, that's embeddable with business model, blah, blah, blah. The, the... Google benefits from open feeds existing. Full stop. And to not support that-

**Host** [93:25]: Cory Doctorow says, and is quoted in this comic, "What killed RSS was the growth of digital monopolies who created silos, walled gardens, and deliberate incompatibility between their services to prevent federation, syndication, and interoperability." So we've identified, this comic says, three suspects in the case of RSS's suspicious death: infighting among RSS's creators.

**speaker_4** [93:52]: Oh, that was the early days.

**Host** [93:53]: Yeah, I don't think that so much.

**speaker_4** [93:54]: No.

**Host** [93:54]: Social media companies had a better product. Yeah, Twitter definitely had something to do with it, attracting more users. And Google and Facebook's dominance made it harder for independent websites to make money. [sighs]

**speaker_4** [94:07]: Those were the days. I... So I, I, I've now brought up Dave Winer's name about 10 times, but I ran into Dave some years ago in Perugia and I said, "Dave, the beginning days of the blogs were just wonderful. We had, we had blog rolls, and we got along, and we linked to each other and, you know, and we talked. And what happened?" And he said, "Jeff." He said, "Everything's good when it starts."

**Host** [94:29]: [laughs]

**Paris Martineau** [94:31]: [laughs]

**Host** [94:32]: Yeah.

**Paris Martineau** [94:32]: Well, yeah.

**Host** [94:33]: That's true.

**speaker_4** [94:34]: Yep. Yep.

**Host** [94:35]: That's true. Um-

**speaker_4** [94:37]: Hard part is sustaining

**Host** [94:37]: ... all right, let's, let's, uh, take another break. When we come back, uh, you guys pick your stories and then-

**speaker_4** [94:42]: You, you're gonna wanna hear about, about, um, the browser, about Comet. I'm telling you that.

**Host** [94:47]: Oh, you got access to Perplexity's-

**speaker_4** [94:50]: I got access to it

**Host** [94:50]: ... browser. You know, everybody and their brother's making a browser. Coggy makes Orion, which I've been using. It's basically a Safari port, uh, with some built-in... With bo- co- One of the reasons it's very hard to beat the incumbent Google is 'cause Google pays everybody, right, to be the default search, $20 billion a year to Apple to be the default search. And so Apple gives you some choices of searches, but one of them's not Coggy. [laughs] So if you are a new paid search engine, which K-A-G-I, Kagi, is, and I... It's what I pay for. I use it. I love it. Um, it's de-Googled search, right? If... But it's the same problem that I had with Neva, which, which was the last one I used that went belly up 'cause you can't compete against Google because it... You've gotta jump through hoops. You have to install an extension to add their search to Safari and many other browsers that's not built in 'cause they're not getting... They don't pay them. So, uh, they just said, "Well, let's make our own browser, Orion." Now, Perplexity's doing the same thing for other reasons. They want to do an AI browser. That's all the rage now. In fact, OpenAI, it is rumored, is about to release a browser as well.

**speaker_4** [96:03]: And Google added more features, but we'll get back to that after your break.

**Host** [96:05]: We'll talk to that in just a little bit after the break. You're watching Intelligent Machines. I think this is kind of a fun conversation. We're learning something here. Uh, not trying to cover exhaustively all the news, 'cause I would be exhausted if we did. There are s- There are... This is a beat that has 20, 30 stories a day.

**speaker_4** [96:25]: Oh, yeah.

**Paris Martineau** [96:25]: Minimum.

**Host** [96:26]: Minimum.

**speaker_4** [96:26]: Yeah.

**Host** [96:27]: It's crazy what's going on right now. Jeff Jarvis here, he's, he's a great deep thinker, public intellectual. Uh, yeah, you're a public intellectual.

**speaker_4** [96:37]: Right.

**Host** [96:37]: One of the, one of the few, the proud-

**speaker_4** [96:39]: You're public [laughs]

**Host** [96:40]: ... the brain. Yeah. Web We Weave is his, uh, latest magazine, now available on audio, and, uh, Gutenberg Parenthesis in soft cover. So buy all three. Do you get a discount if you buy all three?

**speaker_4** [96:50]: No.

**Host** [96:51]: No. [laughs] Uh-

**speaker_4** [96:54]: Not that I can recall

**Host** [96:54]: ... and Paris Martineau is here, soon to be employed. That's all that needs saying.

**Paris Martineau** [96:57]: Soon to be. That's all, all you need to know.

**Host** [96:59]: We think you are the best, Paris. It was so nice to sit and talk with you.

**Paris Martineau** [97:04]: I agree.

**speaker_4** [97:04]: I am.

**Host** [97:04]: Yeah.

**speaker_4** [97:05]: You know it.

**Host** [97:05]: We know it.

**Paris Martineau** [97:06]: It was lovely. Leo gave me a tour of Petaluma.

**Host** [97:09]: I showed her the Carnegie Library.

**Paris Martineau** [97:11]: It was a delightful time.

**Host** [97:11]: [laughs]

**Paris Martineau** [97:11]: Mm-hmm.

**speaker_4** [97:12]: Did you see any chickens?

**Paris Martineau** [97:13]: It was very cute.

**Host** [97:14]: Uh, I show-

**Paris Martineau** [97:15]: We did not

**Host** [97:15]: ... I talked about the chicken coops. I explained the, uh, reason that we were the chicken capital of the world.

**Paris Martineau** [97:18]: I was looking for butter and eggs.

**Host** [97:21]: I show, I talked about the hatcheries. I did show her the big mural that has chickens-

**Paris Martineau** [97:26]: The mural was great

**Host** [97:26]: ... and the history of Petaluma.

**Paris Martineau** [97:28]: I did see painted chickens.

**Host** [97:29]: Yeah. She did. See? You saw chickens.

**Paris Martineau** [97:31]: Mm-hmm.

**Host** [97:31]: And, and, uh- They, there's a history of Petaluma called Comrades and Chicken Farmers.

**speaker_4** [97:37]: [laughs]

**Host** [97:37]: [laughs] Our show today brought to you by... Intelligent Machines is brought to you by Melissa this week, the trusted data quality expert. They've been doing it longer than we have, since 1985. Melissa's latest milestone features a full SIS, S-S-I-S product stack that's now officially supported on Azure Data Factory. Both web services and on-premises components can be executed in the cloud, [laughs] wow, empowering you to modernize your ETL workflows without disrupting your existing development processes. With this release, you can continue designing SIS packages in Visual Studio exactly as before, then deploy them and run them within ADF SIS integration runtime IR. This hybrid approach delivers minimal to zero changes to your existing SIS packages or development workflow. Azure-hosted execution for enhanced scalability, centralized management, and reduced infrastructure overhead. You get seamless support and simplified infrastructure. No need to maintain on-premises SIS servers. Isn't that nice? Run it in the cloud. Melissa's data enrichment services support all industries. By using Melissa as part of their data management strategy, organizations build a more comprehensive, accurate view of their business processes. I'll give you an example. University of Washington, facing a major loss of critical data, costly postage waste, 'cause they were mailing duplicates, they were mailing to wrong addresses, and, as a result, missed fundraising opportunities. The associate director IM of, uh, strategic technology initiatives for the University of Washington said, quote, "We had so much data to contend with, and knew it was important to bring in an expert. We were an early adopter, and used nearly all the components in Melissa's data quality suite. We appreciate their developer support and integration with our own tools and workflow. We see Melissa as a trusted vendor that provides good value and superior quality." In effect, Melissa is your data scientist, ready to come to your aid. Data is, of course, safe, compliant, and secure with Melissa. You need not worry about that. Melissa's solutions and services are GDPR and CCPA compliant. They're ISO 27001 certified. They make SOC 2 and HIPAA high trust standards for information security management. They go the extra mile to keep your data safe. Get started today with 1,000 records cleaned for free, melissa.com/twit. That's melissa.com/twit. We thank them so much for supporting Intelligent Machines. So tell me, so you got somehow, you got an invite to Perplexity's-

**speaker_4** [100:26]: I, I, I wrote to their press office and said-

**Host** [100:29]: Smart

**speaker_4** [100:29]: ..."Please, may I? Can I?"

**Host** [100:30]: We are gonna interview, uh, soon, I think, Perplexity's CEO. No, I'm sorry, Coggy's CEO, Vlad Preda.

**speaker_4** [100:39]: Coggy's CEO.

**Host** [100:40]: Shoot.

**speaker_4** [100:40]: So-

**Host** [100:40]: But we're trying to get, we're trying to get, uh, Perplexity's CEO on.

**speaker_4** [100:43]: Oh, we're trying to get them all on.

**Host** [100:44]: Yeah, all on.

**speaker_4** [100:45]: We're trying to get them all on.

**Host** [100:45]: I'd really like to-

**speaker_4** [100:45]: So I, um, uh, I emailed them and I talked to the, to, to r- really good guys at the press department about it, and, um, uh, they, they view that there's three, there were three generations of browser wars, right? Browser War I against Microsoft versus Netscape, Browser War II, uh, Netscape versus... I mean, br- uh, uh, Microsoft versus Google, and now it's, uh, Perplexity against Google and maybe OpenAI. Uh, I was wowed from using it.

**Host** [101:12]: Really?

**speaker_4** [101:13]: Yeah.

**Host** [101:13]: Now, I've used Dia.

**Paris Martineau** [101:14]: In what way?

**Host** [101:15]: Re- so there was a browser-

**speaker_4** [101:16]: I'll tell you

**Host** [101:16]: ... the browser company of New York created this browser Arc, and then said, "You know what? Nobody wants to use this. [laughs] We can't make any money. We're gonna abandon Arc and we're gonna make Dia," which is an AI first browser. I think somewhat similar to what everybody else is doing.

**Paris Martineau** [101:28]: AI, right, isn't it?

**speaker_4** [101:28]: That's what everybody's doing.

**Host** [101:29]: Yeah.

**speaker_4** [101:29]: So OpenAI's doing it, Google's adding more and more. So it's a few things.

**Host** [101:32]: So why do you want AI in your browser? That's my question.

**speaker_4** [101:35]: Well, re- let me tell you, there's a few things. Um, can you talk again, 'cause I just screwed up my...

**Host** [101:42]: Testing one, two, three.

**Paris Martineau** [101:43]: It's all right.

**speaker_4** [101:43]: I'm fine. Good. Thank you.

**Host** [101:44]: Jeff Jarvis, do you hear me?

**Paris Martineau** [101:46]: Yes.

**Host** [101:46]: Come in, Jeff. Hello.

**speaker_4** [101:47]: Hey, Newmark. Um, so, so, uh, I, I think there's two ways to look at it. Uh, one is that it is agentic AI brought to life in that, um, if you open up your Google Mail and your Google Calendar and your Google this and Google that, uh, y- right in the browser you can tell Perplexity to put a new event in your calendar. You can tell it to send you-

**Paris Martineau** [102:13]: And it does it, no problem?

**speaker_4** [102:14]: Does it, no problem. You can tell it to summarize all your email. You can, uh, do all kinds of stuff.

**Paris Martineau** [102:20]: Can it kind of work across things? Could you say, like, uh, "Put the event that Steve emailed me about in my calendar"?

**speaker_4** [102:27]: That's what... I didn't, I didn't test it with great, uh, alacrity, but yes. Uh, the guy I talked to, uh, made flight reservations with it. Um, uh-

**Paris Martineau** [102:36]: Hmm. That's different than those things. He, like, actually-

**speaker_4** [102:39]: Right

**Paris Martineau** [102:39]: ... booked a flight with it?

**speaker_4** [102:40]: Yep, yep, he said he did, and, and, uh, Jason Howell, uh, did a whole bunch of tests with it I'll describe in a second. So, so one is that you can use it as an agent in whatever you have open and whatever you, you give it access to. Um, Jason was able to send, to have it post to Blue Sky. I have... for some reason it's not letting me do that. I don't know why, but, but, um-

**Paris Martineau** [103:00]: It must know that you have Google Workspace and that you deserve to have-

**speaker_4** [103:04]: It, it-

**Paris Martineau** [103:04]: ... less of an experience-

**Host** [103:05]: That's mean

**Paris Martineau** [103:06]: ... across any-

**Host** [103:06]: That's just mean

**Paris Martineau** [103:07]: ... platform you look at

**speaker_4** [103:07]: ... so here's the thing. My, my pro account, because it is academic, 'cause I get it included with being at Stony Brook, and so I had to sign it to get it there. But, but all my stuff-

**Host** [103:16]: Ah

**speaker_4** [103:16]: ... is on Google. But I, I, I just said, "Pay attention to my Google stuff," and it did. So the other part of it is that it interacts with everything you have open in your browser.

**Host** [103:26]: Okay.

**speaker_4** [103:26]: So Jason did a test and he, for example, put up... Uh, he had five or six tabs open. It's, it's, it's, it's Chromium, so it's very familiar, and, um, he had three of those tabs were cameras that he supposedly was looking at And he said, "Compare these cameras for me."

**Host** [103:42]: Oh, that's interesting.

**Paris Martineau** [103:43]: Ooh.

**speaker_4** [103:43]: It knew the three, only the three tabs had the cameras.

**Host** [103:46]: Huh.

**speaker_4** [103:46]: It came back, it looked up all kinds of stuff. It did a char- a whole chart, uh, comparing the, the features.

**Paris Martineau** [103:52]: Ooh.

**speaker_4** [103:53]: All kind of pretty. Um, Jason, uh, there was a conference that Jason and I were gonna go to, but we didn't go to, that's coming to San Francisco next year, and they announced their first 50 speakers. So Jason went in, a- and this video was on YouTube, um, um, and he said, uh, "Find all the 50 speakers, look up all of their LinkedIn, look up their l- recent statements, tell me what they're likely to say, and tell me who I should try to interview if I go there."

**Host** [104:19]: These are the same exact things I do in Perplexity now, just so they're just building a, a browser.

**speaker_4** [104:23]: They're, they're integrated, right?

**Host** [104:24]: Yeah.

**speaker_4** [104:25]: And, and, and you can do other things. You could, you could have it group your tabs, which, which I have to have the whole new, um, Lenovo Chromebook to be able to do that, uh, in Google.

**Host** [104:35]: Oh, gee, it's too bad you don't have the whole new Chromebook, Lenovo Chromebook.

**Paris Martineau** [104:41]: Too bad.

**speaker_4** [104:42]: I, I bought it.

**Host** [104:42]: Oh.

**speaker_4** [104:42]: I bought it. I bought it.

**Host** [104:43]: Did you buy it?

**Paris Martineau** [104:44]: [laughs]

**speaker_4** [104:44]: Yeah. It's over there.

**Host** [104:44]: Okay, 'cause I-

**speaker_4** [104:45]: I bought it

**Host** [104:45]: ... I got one for Abby and I was gonna show it off as my pick of the week.

**speaker_4** [104:48]: Like, oh, I, I'm, I wanna hear more-

**Host** [104:49]: Yeah

**speaker_4** [104:49]: ... 'cause I haven't opened it up yet, 'cause that's-

**Host** [104:51]: Oh, yeah

**speaker_4** [104:51]: ... crazy about it.

**Host** [104:51]: Oh, I think you'll like it. Anyway, we can talk about that later.

**speaker_4** [104:53]: But I'm hearing, I'm hearing great things.

**Host** [104:54]: Yeah.

**speaker_4** [104:54]: I played with it in the New York event.

**Host** [104:55]: Yeah.

**speaker_4** [104:55]: So, so it's integrated with the browser in a way that Google should have been a year ago. Um, uh, and, and the fact that I have to buy one Chromebook to be able to, to, to organize tabs, why couldn't Google do that? Years ago, I talked to Marissa Mayer when she was there-

**Host** [105:10]: Mm-hmm

**speaker_4** [105:10]: ... and I was, I was blathering on the way I do, like I am right now, about hyperlocal news. And she said, "No, Jeff, you're wrong."

**Host** [105:16]: Huh.

**speaker_4** [105:17]: "It's about, it's about being hyperpersonal." And she was right, and that's what Google could be.

**Paris Martineau** [105:22]: Mm.

**speaker_4** [105:22]: But Perplexity just strikes me as being always ahead. They always are more creative.

**Host** [105:27]: Yeah, I agree.

**speaker_4** [105:27]: Always trying things faster.

**Host** [105:29]: I love Perplexity. Yeah.

**speaker_4** [105:30]: And, and they're just so impressive. And so the browser is, um, really, really impressive, and Jason already says that it's saving him time and work, uh, because it's integrated, because it's mixed in with your browser, and it knows what you're browsing. It knows what you're looking at. It knows what you wanna do, and it, that gives it context to act as an agent. So it's the first integration and the first agentic. And so I'm, I'm wowed.

**Paris Martineau** [105:54]: What about privacy?

**Host** [105:55]: Yeah, 'cause-

**speaker_4** [105:56]: That's an issue.

**Host** [105:57]: Yeah.

**speaker_4** [105:57]: Right? So-

**Host** [105:57]: 'Cause I gotta tell you, the, the CEO of Perplexity said, "The reason we wanna make a browser is so we can collect all those signals for advertising."

**speaker_4** [106:04]: Well, it's, it's more than that.

**Paris Martineau** [106:06]: Ooh.

**speaker_4** [106:06]: It's the fact that I'm giving Perplexity access to my email.

**Host** [106:10]: Right.

**speaker_4** [106:10]: That's, that's-

**Paris Martineau** [106:11]: Yeah, no, you're giving... And you're, you're not just giving to it so that you get a service for free. You're paying a lot of money to give Perplexity access to your email, your calendar, your browsing history, everything you do on the front end.

**speaker_4** [106:22]: Well, for now they're putting it out to the $200 a month people, but, but they're gonna, they're opening up. They're giving people, uh, invitations. Please don't bug me for invitations, people. Uh, I don't even know if I have them yet. Um, um, no, they're gonna open it up beyond that. So it's not gonna be a $200 a month-

**Paris Martineau** [106:36]: But for how long is my question. That seems like a complicated service to offer. It doesn't seem like they're able to offer it realistically for free to a lot of people, unless, I guess, the thing that is a benefit is just that they're able to sell, uh, your data and make money off of that by, uh, offering it up to, or using it to target ads more effectively, I guess.

**Host** [106:56]: What's funny is they're not making any secret about it. This is the, uh, interv- the, uh, uh, article from TechCrunch. "Perplexity CEO says its browser will track everything users do online to sell hyper-personalized ads."

**speaker_4** [107:09]: Hello, Marissa Mayer.

**Host** [107:10]: [laughs] Not hyperlocal, hyper-personalized ads. Aravind Srinivas, uh, was on the, we were just talking about TVPN, uh, podcast. Aravind, if you would do that, why wouldn't you do the number one AI show in the world? You should come on our show and talk about it.

**Paris Martineau** [107:26]: [laughs]

**Host** [107:27]: Defend, defend, uh, your, your point of view. He says, "We plan to use all the context that we get as you use it to build a better user profile, and maybe, you know, through our discover feeds we could show some ads there." That wouldn't be too bad. I mean, you don't have to look at the discover feeds. I do frequently. It's actually a pretty good-

**speaker_4** [107:45]: Ooh, I like the discover a lot

**Host** [107:46]: ... news, news source. Yeah. Um, so Comet, uh, was gonna be launched in May. It has finally come out in pre-release. So you have to get an invitation or pay for the super expensive version-

**speaker_4** [107:59]: Mm-hmm, mm-hmm

**Host** [108:00]: ... of Perplexity to get it. Um, Perplexity was rumored-

**Paris Martineau** [108:04]: Someone said in the chat that they have access to it in their $20 a month account, though.

**Host** [108:07]: Oh. Well, there is a wait list. So I signed up on the wait list.

**speaker_4** [108:11]: Yeah, there's, you can get on the wait list.

**Host** [108:11]: Yeah.

**speaker_4** [108:11]: Yeah, there's like 500,000 people on the wait list.

**Host** [108:13]: Yeah. Um-

**Paris Martineau** [108:14]: Oh, boy.

**speaker_4** [108:14]: Go, go to the press, the press department, and you'll-

**Paris Martineau** [108:16]: Yeah

**speaker_4** [108:16]: ... uh, uh, Julio.

**Host** [108:19]: I hate doing that. You know me. [laughs]

**speaker_4** [108:21]: Well, you're not, you're not asking for something early. You're not asking for any special favors.

**Paris Martineau** [108:25]: Yeah.

**speaker_4** [108:25]: You're just asking, uh-

**Host** [108:26]: Hey, man, could you give me a copy, man? Uh, I don't know how I would know if I have it. I don't see anything that indicates I should have it. But I d- you know, I'm already using Perplexity quite heavily.

**speaker_4** [108:39]: Yeah. Yeah.

**Host** [108:39]: So I imagine I'm getting most of the functionality.

**speaker_4** [108:41]: It, it just... I think you're gonna like it because it integrates in with the context of what you're doing.

**Host** [108:45]: I'll be honest, the reason I don't use Dia is because for me, browser functionality is important, where the tabs are, how I can pin tabs, how I can lock things in and-

**speaker_4** [108:55]: Well, this is, this is Chromium, so it's operate... Of course, you gave up Chrome a long time ago 'cause you have to be special. But it's very familiar 'cause it's Chromium.

**Host** [109:02]: So it does all those same-

**speaker_4** [109:04]: It does all the things

**Host** [109:04]: ... things. And it, the-

**speaker_4** [109:05]: Yeah. Well-

**Host** [109:06]: Here's the other reason I don't wanna use it, because Chromium does n- is now on Manifest V3, which doesn't support uBlock Origin. And, uh, you know, Google in their infinite wisdom decided to kill ad blockers. I wonder why. Huh, why would they wanna do that?

**Paris Martineau** [109:20]: Hmm.

**Host** [109:20]: Hmm. And, uh-

**speaker_4** [109:21]: Well, you're robbing from... Well, I'm gonna do it. I haven't done this in, in two years. You're just trying to rob from content... Paris, you should yell at him, because how do you support-

**Paris Martineau** [109:29]: What?

**speaker_4** [109:29]: ... the good work of journalists like Paris Martineau except by supporting the advertising? When you take the advertising away-

**Host** [109:34]: I paid for the information when she worked there

**speaker_4** [109:37]: ... you're taking food out of her mouth.

**Host** [109:37]: I paid for the information.

**Paris Martineau** [109:37]: I'll just say I, I haven't worked for an ad-supported, uh-

**Host** [109:40]: Oh

**Paris Martineau** [109:40]: ... media company in a long while. [laughs]

**speaker_4** [109:43]: Uh, and-

**Host** [109:44]: I, I understand what you're saying.

**speaker_4** [109:45]: The CIA certainly isn't ads supported.

**Host** [109:45]: Look, we're ad supported media. I mean-

**speaker_4** [109:47]: Yeah, exactly

**Host** [109:47]: ... I'm, I'm being pretty-

**speaker_4** [109:48]: Hello

**Host** [109:49]: ... uh, hypocritical about this. But a lot of these ads, there's a few things. One, they're so ridiculous that you can not even look at a page on mobile anymore because it's, it's got sliding windows and videos opening and all this stuff. These ad networks, they haven't done it lately, but have in the past pushed malware.

**speaker_4** [110:08]: [laughs]

**Host** [110:09]: Uh, so there is a security thing, and there's definitely a bandwidth issue. There's a huge amount of bandwidth on these ads. So, uh, you know, I agree. I, I want to... So I, you know, you turn off your ad blocker on sites for people you really like. The really good sites do what we do, which is they're, they're first party ads. They're not third party ads.

**speaker_4** [110:30]: Yeah.

**Host** [110:30]: They're not ads inserted after the fact. They're, uh, they're ads, you know, sold by, like for instance, Daring Fireball, John Gruber, or Jason Snell, Six Colors, uh, those ads come from their server, so ad blockers don't block them. Uh, they're first party ads, and those I have no problem with. I just have problems with ads that really take over the whole page, and they're, they're ugly and they're risky.

**speaker_4** [110:53]: So, so we're gonna see a lot of these browser stories over the next few weeks. You know, OpenAI working on it. Um, as soon as a comment came out, "Oh yeah, we, we got one too." Google just announced today-

**Host** [111:04]: Yeah, open-

**speaker_4** [111:04]: ... that they're adding more features in AI to their browser.

**Host** [111:06]: I don't like the AI, uh, enabled, uh, search results. Do you? Do you turn those on? Do you use those?

**Paris Martineau** [111:12]: I've ... I d- I find them completely useless-

**Host** [111:16]: They're terrible

**Paris Martineau** [111:17]: ... and uninteresting, and frankly it's just another thing that I have to scroll by in order to get to what I'm actually looking for, which is increasingly the regular search results are, like, two to three lines on the first page-

**Host** [111:30]: Right

**Paris Martineau** [111:30]: ... of Google. It is, uh, from the bottom and top I'm being attacked on all sides by sponsored links, uh, AI search results, and things I didn't try to search for.

**Host** [111:40]: Well, good news. Next week our guest will be Tulsee Doshi, senior director and product lead for Google's Gemini models. [laughs]

**speaker_4** [111:47]: Um.

**Host** [111:49]: We're, we're, we're doing that recording, uh, tomorrow, right?

**speaker_4** [111:54]: Right. So, but we're also gonna have Steven Johnson next week, right?

**Host** [111:57]: Is Steven gonna be on, uh, next week instead? And we'll do Tulsee the week after.

**speaker_4** [112:02]: I think that's-

**Host** [112:03]: So we are gonna record in public tomorrow. So actually if you wanted to see our interview with Tulsee, we're doing that between 1:00 and 2:00 PM Pacific. Club members will get to watch that, and it'll be on the live stream, and then we'll roll that into the show either next week or the week after. I do wanna talk to Steven Johnson as soon as possible because he was scheduled-

**speaker_4** [112:21]: Well, talk about this

**Host** [112:21]: ... for today's show. He has released NotebookLM, an update to NotebookLM that I think is really interesting.

**Paris Martineau** [112:29]: Mm.

**Host** [112:30]: Yeah. Now, first of all, I like NotebookLM. It's a really-

**speaker_4** [112:33]: I love it

**Host** [112:33]: ... clever idea. This is Google's, uh, Gemini applied to r- in effect, RAG, r-

**speaker_4** [112:40]: Yeah

**Host** [112:40]: ... stuff you put in there.

**speaker_4** [112:41]: It restricts itself to the content that you point it to.

**Host** [112:43]: Right. So for instance, uh, some time ago I, I gave it Google's quarterly results and then said, "O..." And then now you can ask questions about it. This is the one that does podcasts as well. Well, they've added a new feature, uh, trusted sources. So if I say I wanna create a new, uh, NotebookLM, I can choose sources from preselected trusted sources. So I could say what I'm interested in.

**Paris Martineau** [113:08]: Oh.

**Host** [113:09]: Or here I'm feeling curious. It just [laughs] gives you a random selection of authoritative sources in, in a random area. Let's see what I get here. Uh, this collection-

**Paris Martineau** [113:19]: A primer on prediction markets

**Host** [113:20]: ... prediction markets. So it's, so th- there are 10 sources. Uh, the Wall Street Journal.

**Paris Martineau** [113:26]: It's all about election betting. One of them's a YouTube video.

**Host** [113:29]: Yeah, yeah. Historical presidential betting markets, prediction markets, market integrity-

**Paris Martineau** [113:34]: Asterisk Magazine

**Host** [113:34]: ... and manipulation from Wilmer Hale, Asterisk Magazine. So these pe-

**Paris Martineau** [113:38]: I'm curious, did Asterisk, uh, give them access to their website, or was that uploaded somewhere else?

**Host** [113:43]: I don't know. We'll have to ask, uh, Steven.

**speaker_4** [113:45]: Well, that's, that's the other thing they announced, is that The Economist and other sites have notebooks that they're sharing. [thunder]

**Paris Martineau** [113:54]: That was the most ominous crack of thunder I've ever heard live, Jeff.

**speaker_4** [113:59]: [laughs]

**Paris Martineau** [113:59]: It sounded as if-

**Host** [114:00]: That was good

**Paris Martineau** [114:00]: ... you were in a spooky mansion and you just said that this-

**speaker_4** [114:04]: [singing]

**Paris Martineau** [114:04]: ... creature last night.

**Host** [114:07]: [singing]

**speaker_4** [114:07]: I warned-

**Host** [114:08]: Big storm coming

**speaker_4** [114:09]: ... on our, on our group text I warned that I have a big storm coming, yes, so-

**Host** [114:11]: Oh, and you're on the generator now?

**speaker_4** [114:13]: Well, I bought my wife a, a, a UPS, uh, for, 'cause she teaches class right now. I should have bought myself one too, 'cause I, I've got the, the router is on a UPS.

**Host** [114:23]: But you wouldn't go.

**speaker_4** [114:24]: The house is on a generator.

**Host** [114:25]: I tell you, it was the scariest thing this morning. Half an hour before Windows Weekly I came up here, turned on the lights, and everything went pshew.

**speaker_4** [114:32]: Geez.

**Host** [114:33]: [laughs] It was pitch black in the attic, and I thought, "This is not good."

**Paris Martineau** [114:35]: Yeah, 'cause there's so many lights in that attic. [laughs]

**Host** [114:37]: Oh, yeah. Well, we've never had a problem before.

**Paris Martineau** [114:39]: I don't think it's ever been dark before.

**Host** [114:41]: Uh, I don't know what happened. Anyway, we, we, w- I think we got it fixed, but that's one of the reasons I have, uh, trouble showing my screen, is, uh, everything's a little kerfluggled here.

**speaker_4** [114:49]: [laughs]

**Host** [114:49]: I don't know what... I don't know how any of this works.

**speaker_4** [114:51]: Are you only on one circuit up there?

**Host** [114:52]: It's a lot of wires.

**speaker_4** [114:53]: Are you only on one circuit up there?

**Host** [114:55]: Yeah.

**speaker_4** [114:55]: Oh, okay. That's probably why.

**Host** [114:57]: No, there's plenty of amps. It's not that. It's never happened before. Uh, it's just some- this is, this house is a mess.

**Paris Martineau** [115:04]: Leo's house is so cute. It's full of crystals.

**Host** [115:06]: It is. Lis- you noticed that.

**Paris Martineau** [115:08]: Mm-hmm.

**Host** [115:08]: Lisa has a lot of, um-

**speaker_4** [115:09]: It's a new house, right?

**Paris Martineau** [115:11]: It's a very new house.

**Host** [115:12]: It, it's brand new, and unfortunately, uh, we're tearing it apart now because, uh, it was poorly constructed and is leaking. [laughs]

**speaker_4** [115:19]: Oh, no.

**Host** [115:21]: See, Paris, I didn't even show you, Paris, but the whole south wall is off.

**Paris Martineau** [115:26]: Oh, no.

**Host** [115:27]: Yeah. [laughs]

**Paris Martineau** [115:27]: That's not good.

**Host** [115:28]: Not good.

**speaker_4** [115:29]: Wow.

**Host** [115:30]: Not good.

**speaker_4** [115:30]: Wow.

**Host** [115:30]: And then they, they, uh, as often happens with construction, they did the demolition right away. They're good at that. They c- they're good at tearing down.

**speaker_4** [115:38]: Yeah.

**Paris Martineau** [115:38]: Yeah, yeah, but putting it back together, ha ha ha.

**Host** [115:40]: Three weeks, we haven't seen a soul. It's like they disappeared. They tore off the side and then disappeared.

**speaker_4** [115:44]: They, they all have ADD.

**Host** [115:47]: Yeah, I think so. It's an adobe, uh, thing, and they, so they took the adobe off to see what was underneath, and what was underneath was a lot of leaks and stuff.

**speaker_4** [115:56]: [laughs]

**Host** [115:56]: So now they tell us we have to take all the windows out, all the sliding glass doors out-

**speaker_4** [116:01]: [sighs]

**Host** [116:01]: ... reseal everything, put everything back in. And then we're saying, well, do we... Maybe we don't wanna stucco it again, 'cause if... I don't wanna have to do this-

**speaker_4** [116:07]: Is there a house warranty in California?

**Host** [116:10]: Oh, yeah, 10 years.

**speaker_4** [116:12]: Oh.

**Host** [116:12]: But the builder is refusing to, uh, honor it, so.

**speaker_4** [116:17]: [laughs]

**Paris Martineau** [116:17]: Uh, we-

**speaker_4** [116:18]: Oh, boy

**Paris Martineau** [116:18]: ... we sued our builder, and then he said, "I'm judgment proof." I said, "What does that mean?" He said, "I got nothing."

**Host** [116:23]: Yeah.

**Paris Martineau** [116:23]: [laughs]

**Host** [116:24]: That, that's basically... I mean, we're, we're probably gonna... Yeah, I don't wanna go into-

**speaker_4** [116:29]: Yeah

**Host** [116:29]: ... detail. We're attempting to recover. We'll see if we-

**Paris Martineau** [116:33]: [laughs]

**Host** [116:33]: ... get a shot at it. It's gonna cost-

**speaker_4** [116:34]: We can't talk about Paris's new job or Leo's suits

**Host** [116:36]: ... it's literally gonna cost hundreds of thousands of dollars.

**speaker_4** [116:39]: Yeah.

**Host** [116:39]: My retirement... And the, the... Here's something I'll tell you kids, you young people. You know, you're putting all that money away for retirement, and it's tax-free when you put it in-

**Paris Martineau** [116:47]: Mm

**Host** [116:47]: ... right?

**speaker_4** [116:47]: [laughs]

**Host** [116:47]: That 401[k], that IRA.

**Paris Martineau** [116:49]: Yeah, all that money that we're saving.

**Host** [116:51]: Guess what?

**Paris Martineau** [116:51]: Yeah.

**Host** [116:51]: As soon as you take it out, they tax the hell out of it. And, uh, basically I'm at a point where, you know, I have to take out twice as much as I need, 'cause the government's gonna get half of whatever I take out.

**speaker_4** [117:04]: Yeah.

**Host** [117:04]: So I thought, "Oh, I got a nice nest egg, I should be fine." I realized, no, you don't. [laughs] Especially if you have to spend it rebuilding the house you just bought. Okay. That's-

**speaker_4** [117:16]: I think we'll be keeping making podcasts-

**Host** [117:17]: That's my-

**speaker_4** [117:17]: ... for a little while now.

**Host** [117:17]: That's my... Well-

**Paris Martineau** [117:18]: We're gonna have to keep podcasting

**Host** [117:19]: ... the, that is the good news, is that I can never retire. [laughs]

**speaker_4** [117:25]: [laughs]

**Paris Martineau** [117:25]: [laughs]

**Host** [117:25]: I have to keep working until-

**speaker_4** [117:26]: But, but folks-

**Host** [117:27]: I-

**speaker_4** [117:27]: ... you've gotta recommend this podcast with five-star reviews-

**Host** [117:29]: Please

**speaker_4** [117:29]: ... so we get more people, so we don't have to have more ads-

**Host** [117:30]: Do you have any five-star reviews, Paris?

**speaker_4** [117:32]: ... we get more dollars.

**Paris Martineau** [117:32]: I do, yes.

**Host** [117:33]: All right.

**Paris Martineau** [117:33]: Let me, let me open 'em.

**Host** [117:34]: We're gonna take a break. You can share some five-star reviews. I will share this new Chromebook, which I did not buy for myself, but I bought for my daughter, who is a Chromebook fanatic. And she's been... She used her last Chromebook so much-

**Paris Martineau** [117:46]: Chrome head.

**Host** [117:46]: Yeah, she's a Chrome head. She used her last Chromebook so much that the question mark key and the, uh, S key fell off. [laughs]

**speaker_4** [117:53]: [laughs]

**Host** [117:54]: So in order to type a question mark or an S, she has to copy and paste it in. [laughs]

**speaker_4** [117:59]: [laughs]

**Paris Martineau** [117:59]: Oh.

**Host** [118:01]: I said, "Honey, you need a new laptop." She said, "Oh, no, it's fine."

**speaker_4** [118:04]: Did you get to meet Abby, uh, Paris?

**Paris Martineau** [118:06]: Alas, no, I did not.

**Host** [118:07]: No, no.

**speaker_4** [118:08]: Oh, too bad.

**Host** [118:08]: Like ships that pass in the night. She came in after you left. I thought-

**speaker_4** [118:11]: I thought we'd be a matched set. You know, you'd see Abby, and I saw Henry.

**Host** [118:14]: She's in New York right now. She's, she's trying to get-

**Paris Martineau** [118:16]: Ooh

**Host** [118:16]: ... a sandwich.

**Paris Martineau** [118:18]: Hey. [laughs]

**Host** [118:18]: Apparently even Henry sold out.

**Paris Martineau** [118:19]: I might see her there.

**Host** [118:20]: Even for his sister, he sold out.

**Paris Martineau** [118:23]: Wow.

**Host** [118:25]: Uh, all right.

**Paris Martineau** [118:25]: Thanks for the-

**Host** [118:26]: Uh, before we get to the picks of the week, which are coming up next, I do wanna mention our club and all the great stuff coming up in Club Twit. Tomorrow, as I mentioned, Club Twit members will see our interview with Telsie Doshi, senior director and product lead for Gemini models-

**speaker_4** [118:42]: Wow

**Host** [118:43]: ... from Google. That's a great get. Uh, we are also tomorrow, uh, going to be doing... Oh, no, tonight, I'm sorry. We're doing Micah's Crafting Corner, a little cozy crafting. So if you've got a little something going on, maybe some knitting or sewing. Micah usually does, uh, Lego. I'm not sure what he's doing this time. I, I did some cooking last time. Please, uh, join us, uh, tonight right after the show for Micah's Crafting Corner, 6:00 PM Pacific, 9:00 PM Eastern. Um, let's see, what else is coming up? Oh, we... We're gonna do Richard Campbell's PC build. He's got, uh, all the parts. He's gonna build a new PC, and we're gonna watch him do it. On Friday, the RAM didn't come, so we're gonna put that off till next Thursday, a week from tomorrow. Home Theater Geeks records in the club. The AI user group is the first Friday of every month. Uh, we've got Stacy's book club coming up August 8th. A really good book which is not too late to pick up and read, This Is How You Lose the Time War. I- it's amazing. Um, and, uh, it's a, it's a, it's a short... It's like a novella. It's not really long. So please, if you want, join us for that. That's August, uh, 8th. Right after that, same day, Photo Time with Chris Marquardt, our word of the week, or word of the month classic. Uh, the Made by Google event is coming up August 20th. That's Google's announcement of their new, uh, Pixel phones, I believe. So we're gonna cover that live Wednesday, August 20th, 10:00 AM Pacific. All of this club only, okay? We do stream it live. Some of these things, uh, for instance, Home Theater Geeks, Hands on Apple, Hands on, uh, Windows, we give... We put out a- audio publicly, 'cause we want you to have the content, but you have to be in the club if you wanna get the video. And if you're not there for the live event, then you have to watch on the Twit Plus feed, which is club only. So there are some real reasons to join the club. Also, if you don't like ads, you don't have to feel guilty about skipping them. Just join Club Twit, 10 bucks a month, and you won't ever hear another ad. Even this plug you won't hear again, because you're, you're donating. We don't, we don't really need to show you ads. No tracking, no ads, nothing. Twit.tv/-

**Paris Martineau** [120:52]: If you're a little freak-

**Host** [120:53]: ... slash club twit

**Paris Martineau** [120:53]: ... who wants to hear the ads anyway, but also wants to support the club, you can do both. 'Cause I know people are out there who've said that, that they want to both support the club and hear the ad reads, 'cause they think they're fun. You can contain multitudes if you like.

**Host** [121:05]: Yes. Isn't that nice?

**Paris Martineau** [121:06]: It is.

**Host** [121:06]: You can do, you can do both. We even have a feed on the Discord called all the ads. [laughs]

**Paris Martineau** [121:12]: [laughs]

**speaker_4** [121:12]: [laughs]

**Host** [121:12]: It's just the ads, if you really like ads. [laughs] Um, what else? Anyway, please join the club. It really makes a difference to us. It's 25% of our operating costs. Uh, doesn't go into my pocket, doesn't go to Lisa's pocket. It goes to my, uh, Micah-

**speaker_4** [121:27]: My pocket

**Host** [121:28]: ... Jeff, and Benito, and Paris, and all the people who do these great shows for us.

**speaker_4** [121:32]: And Leo's contractor.

**Paris Martineau** [121:33]: [laughs]

**Host** [121:34]: Yeah. No, it won't go into his pocket. Not if I can help it. Um...

**Paris Martineau** [121:37]: [laughs]

**Host** [121:38]: Twit.tv/-

**Paris Martineau** [121:39]: He's judgment proof

**Host** [121:40]: ... cl- He's jud- I'm judgment proof.

**Paris Martineau** [121:42]: Mm-hmm.

**Host** [121:42]: What do you want?

**speaker_4** [121:43]: [laughs]

**Host** [121:43]: Twit.tv/clubtwit. [laughs] Uh- All right, Paris. Or should I, should I... Let me start. I'll start with this, just 'cause it's a, it's a-

**Paris Martineau** [121:50]: Wait, let me do a, let me do a, a review read first really quick-

**Host** [121:54]: Okay

**Paris Martineau** [121:54]: ... and then we can go to the picks.

**Host** [121:55]: Oh, yes-

**Paris Martineau** [121:56]: Um-

**Host** [121:56]: Give us a five star

**Paris Martineau** [121:56]: ... this is a, a five-star review from, uh, Joseph Patrick of our podcast on, uh, Apple Podcast. If you want your review shouted out in the show, uh, leave us a good review, and if it's funny or interesting, maybe I'll shout it out. Um, this is an ad from Joseph Patrick who says, "Interesting take here. As much as I like the Craig Newmark jingle-

**Host** [122:17]: [laughs]

**Paris Martineau** [122:17]: ... JJ no longer works there. I suggest the jingle be replaced with a jingle for SUNY. Can I suggest ripping off the Sega Genesis start sounds and replacing Sega with SUNY? Now, while I personally do not have the talent or know how to create such a jingle-

**Host** [122:30]: [laughs]

**Paris Martineau** [122:30]: ... I hear that the host of this show are good friends-

**Host** [122:33]: Se- Se- Su-

**Paris Martineau** [122:33]: ... with several intelligent machines-

**Host** [122:35]: Su- Su- SUNY

**Paris Martineau** [122:35]: ... [laughs] who have such talents. Perhaps a jingle competition is in order-

**Host** [122:39]: Oh

**Paris Martineau** [122:40]: ... says Joseph Patrick. So, you know, do you have jingle suggestions? Do you think the jingle should be something different?

**Host** [122:46]: Ooh.

**Paris Martineau** [122:46]: Do you think we should keep the same one?

**Host** [122:47]: I, I love it-

**Paris Martineau** [122:48]: Leave us a review

**Host** [122:48]: ... that it's a new way to communicate with us, is leaving us a review. [laughs]

**Paris Martineau** [122:52]: Leave us a review, and I'll, at the very least, read it, and decide if we're gonna-

**speaker_4** [122:55]: Yeah

**Paris Martineau** [122:55]: ... read it on the show.

**speaker_4** [122:56]: Yeah. Yeah.

**Host** [122:56]: I do like the idea.

**speaker_4** [122:57]: That's a way to invest in it.

**Host** [122:57]: I like the ♪ SUNY ♪

**speaker_4** [122:58]: That's pretty good.

**Host** [122:59]: ♪ SUNY ♪ Like Sega.

**Paris Martineau** [123:01]: Try to come.

**speaker_4** [123:01]: Yeah, like Sega.

**Host** [123:01]: Sega. SUNY. Somebody did an AI, uh, Craig Newmark with a heavenly choir, uh, here in Discord, but I can't play it 'cause I can't play the audio. [laughs] So...

**Paris Martineau** [123:11]: [laughs]

**speaker_4** [123:11]: [laughs]

**Host** [123:12]: Well, wait a second. Well, can you just play it loud on the computer and then put your mic by it? Or-

**Paris Martineau** [123:15]: We can't. We can't open this can of worms again.

**speaker_4** [123:18]: Yeah, we can't do that. No, no, no.

**Host** [123:18]: [laughs]

**Paris Martineau** [123:18]: We're not unmuting, we're not unmuting that computer.

**Host** [123:21]: We cannot do it. I cannot, I cannot.

**Paris Martineau** [123:23]: All right, give us your pick, Leo.

**Host** [123:24]: You can play it for yourself. So, uh, Jeff saw these at the Google event, the Chromebook event.

**speaker_4** [123:30]: Mm.

**Host** [123:30]: This is the new... It's a new... It's actually a whole new platform, the Chromebook Plus platform, which, uh, makes the Chromebook an AI device. Uh-

**speaker_4** [123:39]: Well, well, Plus has been around for a couple years now, but this is the Lenovo version is the AI.

**Host** [123:45]: Yeah.

**speaker_4** [123:45]: It's this one, this new-

**Host** [123:45]: And this has 16 gigs of RAM. It has a new processor from MediaTek called the Kompanio, which has an NPU in it. It also has, uh, a, um, um, 60 TOPS e- engine, and it is able, apparently, you get a free, uh, Gemini Pro account.

**speaker_4** [124:04]: Yep.

**Host** [124:04]: It's able to do... You can even see it. There's the Gemini, uh, icon right there in the menu bar. It... You also get t- a year of two terabyte storage on Google Drive. That's pretty common with Chromebooks. This one is about 750 bucks, has a touch screen. It's a beautiful OLED touch screen. I mean, it is-

**Paris Martineau** [124:22]: Ooh

**Host** [124:22]: ... really gorgeous. Two pounds, very light. 18-hour battery life.

**Paris Martineau** [124:27]: Ooh.

**Host** [124:27]: And a fingerprint reader, which I really like. I got tired of entering my pin or my password every time when I log into my Chromebook. So this makes it secure. Uh, I... It, it's got that nice soft touch keyboard Chromebooks are famous for. I li-

**speaker_4** [124:41]: It's thin

**Host** [124:41]: ... I like the keyboard. It's very thin, very light.

**speaker_4** [124:43]: And, and, and this is, this is huge for me, absolutely huge for me: fanless.

**Host** [124:49]: Yes. Nice and quiet.

**speaker_4** [124:50]: The old Samsung I had was just louder-

**Paris Martineau** [124:52]: No one likes that

**speaker_4** [124:52]: ... than a jet engine.

**Host** [124:53]: I can... Uh, shall I call into the show so you can see the camera?

**speaker_4** [124:57]: What does it retail for? [laughs]

**Host** [124:59]: 749.

**speaker_4** [125:00]: 749, or 649 without a touch screen and less memory.

**Paris Martineau** [125:02]: Hey, that's less than an iPhone.

**Host** [125:04]: Yeah. It's, it's not, uh... I think it's not that expensive.

**speaker_4** [125:06]: The high-end HP that was out there for a while was, was $2,400.

**Host** [125:11]: And Google was selling thousand dollar Chromebooks for a long time.

**speaker_4** [125:14]: Yeah, yeah. I bought a couple of them.

**Host** [125:16]: Uh, I am going to call into the meeting so you can see... Uh, the camera's not great. It does have-

**Paris Martineau** [125:22]: We're gonna have three times the echo somehow. We have three versions of Leo-

**Host** [125:27]: Three Leos

**Paris Martineau** [125:27]: ... in this meeting.

**Host** [125:29]: Leo, Leo, Leo.

**Paris Martineau** [125:30]: Three Leos. Yeah, it's Leo-

**Host** [125:30]: Leo, Leo, Leo

**Paris Martineau** [125:31]: ... three on the court.

**speaker_4** [125:33]: Leo.

**Host** [125:33]: All right.

**speaker_4** [125:33]: Leo, Leo.

**Host** [125:34]: Now, uh-

**speaker_4** [125:35]: Okay, you need to, you need to... You're gonna have to mute that one.

**Paris Martineau** [125:38]: [laughs]

**speaker_4** [125:38]: You, I guess you gotta mute that one.

**Paris Martineau** [125:38]: We've gotta remedy this. [laughs]

**Host** [125:39]: All right.

**speaker_4** [125:40]: Uh, I don't know where it's coming...

**Host** [125:43]: Now you're totally muted.

**speaker_4** [125:43]: And I'll talk on this one.

**Host** [125:44]: Okay, there you go.

**speaker_4** [125:45]: Um...

**Paris Martineau** [125:46]: [laughs]

**Host** [125:47]: Can you, can you see it, Benita?

**Paris Martineau** [125:48]: I can see it.

**speaker_4** [125:49]: Yeah.

**Host** [125:50]: Well, Benita has to pick it. There it is.

**speaker_4** [125:52]: Let's look. That's pretty good.

**Host** [125:52]: So it's not the best camera ever, but it's okay. It's a little-

**Paris Martineau** [125:56]: Hey

**Host** [125:56]: ... uh, low res.

**Paris Martineau** [125:57]: You get to see the forbidden top shelves of Leo's setup.

**Host** [126:01]: Yes. I showed this to, to Paris. I said, "Yeah, nobody ever sees these. I set it up, but nobody ever sees them."

**Paris Martineau** [126:07]: Mm.

**Host** [126:07]: Um, it's excess hat storage on the top shelf there. So I think it's a, uh, I mean, I... For this price, this is a great choice. Uh, Abby loves Chromebooks 'cause she doesn't ever worry about losing your data. It's all on Google Drive.

**speaker_4** [126:20]: Yep.

**Host** [126:21]: So it's all safe.

**speaker_4** [126:21]: Yep, yep.

**Host** [126:22]: Um, I know you love Chromebooks.

**speaker_4** [126:25]: Mm-hmm.

**Host** [126:25]: It has Android, of course, uh, Android capability, and you did see that Sameer Samat said, "Yeah, we're-

**speaker_4** [126:29]: Yeah

**Host** [126:29]: ... we're merging, uh, Chrome and, uh, Android, uh, sometime in the future." And I imagine that these newer models will have the capability to do that. You know, get the new operating system. I think ver- a nice job.

**speaker_4** [126:42]: It is a nice job. Yeah.

**Host** [126:43]: And you, and you've ordered it. You got it?

**speaker_4** [126:44]: I have it. I have it here.

**Host** [126:45]: And you just haven't set it up yet.

**speaker_4** [126:46]: I just... I was out of town most of this week, and I didn't wanna try to take a new machine with me, so I wanna-

**Host** [126:52]: Yeah.

**speaker_4** [126:52]: 650 for a low-end laptop-

**Host** [126:53]: I think you will like the screen

**speaker_4** [126:53]: ... is pretty nice. Yeah, the, the, the screen's nice.

**Host** [126:55]: Beautiful. Beautiful screen. I'm really happy. Abby has trouble with LEDs and the flickering. It gives her-

**Paris Martineau** [127:02]: Mm

**Host** [127:02]: ... uh, migraines, so she can only use OLED, uh, laptops. So when I... this came out, I said, "That's great." It also has-

**speaker_4** [127:08]: What was the model she, she picked out?

**Host** [127:09]: An S. It also has an S and a question mark.

**speaker_4** [127:12]: Yeah. What was the one that she wanted?

**Host** [127:13]: Uh, it was one of the Google, uh, Chromebooks I think.

**speaker_4** [127:15]: This one, yeah.

**Host** [127:16]: Yeah.

**speaker_4** [127:17]: Yeah.

**Host** [127:17]: Yeah. So it's, it's been around for some years. She, you know, has taken a lot of guff. Ah, Paris Martino, what do you have for us, young lady?

**Paris Martineau** [127:26]: I have some pics, uh, from my road trip I just did, and a g- couple... Uh, one thing I, I was trying to use, uh, ChatGPT a bit during this to give me ideas for things to do. Not that... I already kind of had an itinerary, but I wanted to play around with it, see how good it was. I did enjoy kind of the things that deep... I used deep research on 4 point... their 4.5 model. Um, and I found that that, when I, you know, actually went in with a very detailed request, uh, for certain cities, was kind of useful. The other re- ... thing that I used AI for on this trip was, that I found, um, somewhat useful was using the voice mode as I was either walking around places or driving-

**speaker_4** [128:08]: Oh

**Paris Martineau** [128:08]: ... just to ask questions about my environment, if I was driving and couldn't look something up. Uh, and I mean, I think my overall take as I was reflecting on this, 'cause I tried to use it fairly frequently, 'cause I was traveling solo. It was kind of interesting to have something to talk to me about stuff like bridges or Portland history. Portland was my first stops. And one example I think that it, it kinda, um, exemplifies how I felt about this was I was walking acro- in Northeast Portland. I was trying to get ChatGPT to, like, tell me about the history of Northeast Portland, and my first problem is that all of the answers were way too short and not very detailed. And so I went in, kind of changed the custom instructions, was asking it for, to be, like, 500 to 700 word answers, and that was very hard for it at first. It couldn't... It had a very hard time actually responding to my answer of be detailed about it. But eventually, I did get some responses that led me to an interesting figure in Portland, this guy Stuart Holbrook, um, who one of the, I guess, details in Portland is that there are these things called the Shanghai Tunnels that all the, um, Portland tour guides say are these networks of tunnels underneath Portland where, uh, back in the day, old sailors would be, uh, basically abducted from bars and forced to work on ships if they were abducted while drinking. And it kind of goes-

**speaker_4** [129:26]: This guy looks like somebody who would make up stories like that.

**Paris Martineau** [129:28]: So he-

**speaker_4** [129:29]: I gotta tell you. [laughs]

**Paris Martineau** [129:29]: It ends up, uh... I was asking ChatGPT, like, "Okay, well, is this true?" And it's like, "Well, no, peop- some people say it was, like, invented by this guy Stuart Holbrook," and I kept trying to get ChatGPT to tell. I was like, "What do you mean it's invented by this guy? Like, tell me more." And it real- it could tell me a couple lines of detail, but not any of the detail I wanted, so I did some research-

**speaker_4** [129:47]: That's hysterical

**Paris Martineau** [129:48]: ... and found this phenomenal article that I would really recommend written by a, a Portland and, uh, Oregon historian, Joe Streckert, called Stuart Holbrook, Portland Myth Maker.

**speaker_4** [130:00]: This is on Substack?

**Paris Martineau** [130:02]: It's on Substack. He, uh, this guy wrote a Substack called Why Is Portland Like That?

**speaker_4** [130:06]: [laughs]

**Paris Martineau** [130:07]: And, uh-

**speaker_4** [130:07]: Ah, that's a great idea

**Paris Martineau** [130:08]: ... it-

**speaker_4** [130:08]: Talk about hyperlocal. That's awesome

**Paris Martineau** [130:11]: ... is, is an incredibly detailed, uh, kind of almost historical, like, research paper and also self-memoir about this really interesting figure in Oregonian history. This guy basically kind of pioneered this genre of, like, local National Enquirer style journalism that, like, blended myth and reality and kind of captured the mind of people in, like, the late 1800s and, like, ear- like, turn of the century. Um, and so I, I don't know, would really recommend that if anybody's just looking for an interesting historical deep dive, I'd really recommend, uh, this Substack that's no longer publishing, but it has quite a lot of really interesting articles that I then PDF'd and put into ChatGPT and had it read to me while I was driving around.

**speaker_4** [130:56]: Oh, that's smart.

**Paris Martineau** [130:58]: I, but I... It was one, I think, of the perfect examples of using these tools is, yeah, it's kind of like a diet soda in the sense that, like, it was good for getting an overview of something, directing you to maybe a figure that I wanted to know more about, but when I wanted to get really good research and the sort of anecdote-rich, narrative-rich, uh, reporting, I had to go to a real human who knew their stuff.

**speaker_4** [131:19]: So what you could have done is you could have beforehand thought of this and put a whole bunch of resources in a NotebookLM and then had it do a podcast for you, and then enter into the podcast and ask the podcast host questions about the material.

**Paris Martineau** [131:33]: Could have done that, yes.

**speaker_4** [131:33]: While you were driving. Yeah.

**Paris Martineau** [131:34]: That would've been nice.

**speaker_4** [131:35]: We can ask Steven about that next week.

**Paris Martineau** [131:37]: We will.

**Host** [131:37]: There, there is, uh, coming at some point a, uh, you know who Dennis Crowley is? He's the guy who created Foursquare.

**Paris Martineau** [131:46]: Yeah.

**speaker_4** [131:46]: Oh, he's great. Wonderful guy.

**Paris Martineau** [131:47]: Love Dennis.

**Host** [131:47]: He has a new project called BeBot, which is an audio-based guide that you listen to. They're developing, and I'm actually on the Discord channel. You can get a, a, a test flight version of it. I haven't played with it yet, 'cause it's not available in my neighborhood. But, uh, the idea would be that this BeBot, uh, would, you'd put it in your ears. It's an audio-first city guide.

**speaker_4** [132:10]: He's always been about locality.

**Host** [132:12]: Yeah.

**speaker_4** [132:12]: And-

**Host** [132:12]: It's a really, it's a really great idea, and Denz is the guy to do it, so-

**speaker_4** [132:16]: Yeah

**Host** [132:16]: ... I'd be very curious to see what, uh, happens with that, 'cause that's your... Your idea is great. In fact, I used, uh, something like that when we were in Hawaii. I downloaded... There are apps that are audio guides that you're driving around and it says, "Turn left here for the, for the best shave ice [laughs] in the, on the whole island," and stuff like that.

**speaker_4** [132:36]: [laughs]

**Host** [132:36]: And it's like having this chatty old grandpa in your backseat telling you, you know, "Over there is where King Kamehameha lost his head."

**speaker_4** [132:44]: [laughs]

**Host** [132:44]: You know, it's kind of, it's just crazy stuff.

**Paris Martineau** [132:46]: I do kind of, I mean, one of the main things I ended up using ChatGPT for on this trip was asking about cool bridges I was going over.

**Host** [132:52]: Ooh.

**Paris Martineau** [132:53]: Um, uh-

**Host** [132:54]: I know, Jeff would like that

**Paris Martineau** [132:54]: ... I mean, I know. I'm so, I'm so sorry to mention this, Jeff. But there were some really cool, like, art deco bridges, and I, it turned out that all of them were, like, made by the same guy, the ones that I kept, uh, pointing out or wanted to know questions about.

**speaker_4** [133:04]: Had any of them fallen?

**Paris Martineau** [133:06]: No.

**Host** [133:07]: No.

**Paris Martineau** [133:07]: But I know of, some of them were drawbridges, though. I don't know if that makes it worse.

**Host** [133:10]: The bridges that fall are very rare and few and far between. You, I know you need to talk about Ferris-

**speaker_4** [133:16]: Could happen

**Host** [133:16]: ... I'm gonna let you go if you, if you want. I don't know you have-

**Paris Martineau** [133:18]: It's okay. I've got 15 more minutes.

**Host** [133:20]: Okay, good.

**speaker_4** [133:20]: Oh, okay.

**Host** [133:20]: Well, in that case, let's get Jeff's pick of the week.

**speaker_4** [133:23]: Oh, so I could have done something creepy. I could have done the people who are marrying-

**Paris Martineau** [133:28]: Like bridges

**speaker_4** [133:28]: ... their AIs.

**Host** [133:30]: Marrying them?

**speaker_4** [133:30]: Could have done, marrying AIs.

**Host** [133:32]: Is that legal?

**speaker_4** [133:32]: I could have... Well, in a manner of speaking. I could have done the, uh, really creepy eugenicist Silicon Valley people pushing super babies and doing all of that.

**Host** [133:40]: That was, I saw that today in the Washington Post.

**speaker_4** [133:42]: [whistles]

**Host** [133:42]: They're doing genetic prediction services for embryos. Elon's done it.

**speaker_4** [133:47]: And Peter Thiel is backing it.

**Host** [133:49]: Ah, this is so evil.

**speaker_4** [133:49]: But instead-

**Host** [133:51]: So evil

**speaker_4** [133:51]: ... I found a wonderful column in the New York Times, which I don't say very often these days, by, uh, Leif Weatherbe. I presume it's pronounced Leif. Who, uh, has a book that I just started reading, an academic book called, um, Language Machines. Which is really interesting. And he's a director of the Digital Theory Lab at New York University, and his point of all of this is that LLMs should be seen as simply fun. If we-

**Host** [134:19]: Well, that's not bad

**speaker_4** [134:19]: ... peel away-

**Host** [134:20]: Yeah

**speaker_4** [134:20]: ... everything else, that every- is promised about it. Oh, it's gonna change-

**Host** [134:23]: Yeah

**speaker_4** [134:23]: ... the world, it's gonna change all this. If we, if from the beginning we just saw it as entertainment.

**Host** [134:28]: That's not a bad idea.

**speaker_4** [134:30]: It's a good idea.

**Paris Martineau** [134:30]: But-

**speaker_4** [134:30]: It's a really good idea

**Paris Martineau** [134:31]: ... they're not gonna be given, like, hundreds of millions and billions of dollars to something that's just fun and entertainment.

**speaker_4** [134:39]: But they also want to see her rule the world.

**speaker_6** [134:39]: Oh, I know video game, the video game industry is pretty big, actually. [laughs]

**Paris Martineau** [134:43]: Yeah, but the-

**Host** [134:44]: Oh, yeah

**Paris Martineau** [134:44]: ... video game industry isn't raising the sort of valuations and raising the sort of capital-

**speaker_6** [134:48]: No, you're right, you're right

**Paris Martineau** [134:49]: ... that OpenAI is getting

**speaker_6** [134:52]: Because it's actually valued at that. It's not raising that-

**Paris Martineau** [134:55]: Yeah. [laughs]

**Host** [134:55]: I think LeCun's right. Just, it, it's, LeCun's not saying this because OpenAI should pay attention, he's saying it so we should just have the right idea about all this. It's just for fun.

**speaker_4** [135:04]: Yeah. Don't marry it.

**Paris Martineau** [135:06]: And I would agree with that. I think, like, this was, this trip was the most I've casually ever used AI, just because I, you know-

**Host** [135:12]: It's not bad, is it?

**Paris Martineau** [135:12]: There, there's a... I mean, I've never said it's bad, I just don't think it is the most valuable thing that has ever and will ever be invented. I think that's just a foolish statement to say about anything. Um-

**Host** [135:23]: Yeah

**Paris Martineau** [135:23]: ... but I, I think for, yes, this is a perfect argument, because I think it's the most useful for low-stakes things. Like, I was hiking in the Red Woods and I was like, "Why is the bark looking like that?" And something answered w- me in a voice chat instantly, and that's pretty cool.

**speaker_4** [135:38]: Yeah.

**Host** [135:38]: It said, "Hey, Paris, you're looking great today."

**Paris Martineau** [135:43]: Yeah. [laughs]

**Host** [135:44]: That, that bark is... [laughs]

**Paris Martineau** [135:46]: Jesus Christ.

**Host** [135:47]: That's what made me so mad-

**speaker_4** [135:48]: [laughs]

**Paris Martineau** [135:48]: I immediately-

**Host** [135:49]: ... it made me so mad

**Paris Martineau** [135:50]: ... spritz my cellphone with water. [laughs]

**speaker_4** [135:52]: [laughs]

**Host** [135:52]: Made me so... Holy water. Uh, yeah, I, this is good. AI is-

**speaker_4** [135:58]: It's just fun

**Host** [135:59]: ... just fun, fun.

**speaker_4** [135:59]: It's just fun.

**Host** [135:59]: Just for fun.

**speaker_4** [136:00]: Enjoy it.

**Host** [136:01]: And so is this show, it's just for fun.

**speaker_4** [136:03]: Yeah.

**Host** [136:04]: Uh, we do Intelligent Machines every Wednesday, uh, right after, uh, Windows Weekly, which, if the whiskey segment [laughs] doesn't go on too long-

**speaker_4** [136:12]: [laughs] We, we always ask, whenever Paris and I come in, we always ask Benito, "They st-

**Paris Martineau** [136:16]: Are they on whiskey yet?

**speaker_4** [136:16]: ... are they on the whiskey yet?"

**Paris Martineau** [136:18]: He's always like, "No."

**Host** [136:19]: [laughs]

**Paris Martineau** [136:20]: "No, no, no."

**Host** [136:21]: That's not in, in, and of itself enough, because you don't know how long. Today I was a little nervous 'cause Richard started with the 16th century history of Great Britain.

**speaker_4** [136:31]: [laughs]

**Paris Martineau** [136:31]: [laughs] That's a bad sign.

**Host** [136:33]: Yeah.

**Paris Martineau** [136:33]: That's a bad sign.

**speaker_4** [136:34]: Ooh.

**Host** [136:34]: Well, it, yeah, it took... It was about 300, 300 or 400 years before he actually got to whiskey, so yeah.

**Paris Martineau** [136:40]: [laughs]

**Host** [136:41]: It, it-

**speaker_4** [136:41]: Yeah, and by the way, by the way, that's my exposure to Richard, is that, is waiting for him to finish the whiskey segment. When we had him on the show he was delightful.

**Host** [136:49]: Oh, Richard is one of the smartest people.

**speaker_4** [136:51]: Great.

**Host** [136:52]: He's an autodidact. He, you-

**speaker_4** [136:54]: Always enjoyable

**Host** [136:54]: ... you say, "Learn of everything you can know about bridges," and tomorrow he'll give you a three-hour, uh-

**speaker_4** [137:00]: [laughs]

**Host** [137:00]: ... keynote on it. I mean, he's really good. So yes, I love Richard, and I love his whiskey segments. But anyway, right after Richard's whiskey segment, 2:00 PM Pacific, 5:00 PM Eastern Time, 21:00 UTC. You can watch us live in the club, of course, on the club Twit Discord, but you can also watch on YouTube, TikTok, Twitch, X.com, Facebook, Lickedin. Lickedin. [laughs]

**Paris Martineau** [137:23]: Lickedin. [laughs]

**speaker_4** [137:24]: You've been, you've been hanging around with Grok too much, my friend.

**Paris Martineau** [137:25]: Yeah, you've been hanging out with-

**Host** [137:27]: I like the idea for a new social network. Anyway, uh-

**Paris Martineau** [137:29]: I was gonna say, that little fox has gotten its mind wrapped around you.

**Host** [137:33]: [laughs] Uh, or kitten. And, uh, if you don't watch live you can get a f- get a copy of the show from the website, twit.tv/im, for Intelligent Machines. Uh, we are also on YouTube. Best thing though, subscribe wherever you get your podcasts, because that's where you will find us. And if you do, leave us a fun five star review.

**speaker_4** [137:53]: Five star.

**Host** [137:53]: The wonderful Paris Martineau might read it.

**speaker_4** [137:55]: And Paris might read it.

**Host** [137:57]: Yes.

**speaker_4** [137:57]: And Leo might listen to it.

**Host** [137:59]: Subtle tones.

**Paris Martineau** [137:59]: And if you have, uh, an entrant to the What Should The Next Jingle Be competition, leave that in a five star review [laughs] somehow.

**Host** [138:09]: Oh, yeah. Nowadays with Suno, I mean, anybody can create great, you know, jingles-

**speaker_6** [138:12]: Or, or post it on social media and tag Twit. That's another thing.

**Paris Martineau** [138:15]: Post on social media and tag us.

**Host** [138:17]: Yeah.

**speaker_4** [138:17]: Yeah.

**Host** [138:18]: Yeah. We like those jingles. It's a lot of fun.

**speaker_4** [138:20]: Yeah, we do.

**Host** [138:20]: We used, in the early days of Twit we had a number of really good musicians who would make them.

**Paris Martineau** [138:25]: Also, if you're a really good musician or have ac- casual access to a choir and would like to compose a jingle the old fashioned way, that will put you a couple leagues ahead-

**speaker_4** [138:35]: Yeah

**Paris Martineau** [138:35]: ... of the competition.

**speaker_4** [138:36]: Yeah.

**Host** [138:36]: That Craig Newmark jingle's real people, isn't it? It's not a-

**Paris Martineau** [138:39]: It is real people-

**speaker_4** [138:39]: It is, it is, yes

**Paris Martineau** [138:39]: ... and that's the reason why we're, it's gonna be hard pressed to replace it. You're-

**Host** [138:44]: Yeah

**Paris Martineau** [138:44]: ... you're gonna have to try and, try and beat that, so-

**Host** [138:46]: A heavenly choir

**Paris Martineau** [138:47]: ... challenge out there.

**Host** [138:48]: A heavenly choir. Thank you everybody, thank you Paris Martineau. We'll learn next week about Paris's new job, I think.

**speaker_4** [138:56]: It's a good gig.

**Paris Martineau** [138:56]: If the, uh, if the government doesn't come and, uh, take us all down for you squealing on the CIA involvement earlier in the show.

**Host** [139:03]: I know, I know, I'm sorry.

**Paris Martineau** [139:04]: Might be the, it might be the end of all of us.

**Host** [139:06]: She has to kill us now.

**Paris Martineau** [139:08]: I'm sorry.

**Host** [139:09]: [laughs] She, she, she would be a good secret agent.

**speaker_4** [139:14]: She would be.

**Host** [139:15]: She just seems like she's good.

**speaker_4** [139:16]: 'Cause you trust her.

**Host** [139:18]: Yeah.

**Paris Martineau** [139:19]: It's true.

**Host** [139:19]: She's got, she's got-

**Paris Martineau** [139:20]: Yeah, I'm definitely not a secret agent already, that's for sure.

**Host** [139:23]: [laughs]

**speaker_4** [139:23]: Oh.

**Paris Martineau** [139:23]: There's no way that that would be the case.

**Host** [139:27]: She's a mole.

**speaker_4** [139:27]: You look like, you look like you're dressed up and ready to go have a martini.

**Host** [139:31]: Yeah, she's going out. Got Paris-

**Paris Martineau** [139:33]: I'm allegedly-

**Host** [139:33]: Paris Martineau

**Paris Martineau** [139:34]: ... supposed to have a rooftop beer, but the fact that it's a million degrees outside and about to pour makes me believe that will be an indoor beer.

**Host** [139:40]: That thunder that you heard in, uh, just outside Bedminster is coming your way.

**speaker_4** [139:45]: It's headed your way.

**Paris Martineau** [139:45]: I was gonna say, it's coming my w-

**Host** [139:46]: Coming your way. That's Jeff Jarvis. He's in New Jersey. Not his fault. He, uh, he teaches at-

**Paris Martineau** [139:51]: Don't hold it against him. [laughs]

**speaker_4** [139:53]: Hey, yo.

**Host** [139:54]: No, my whole family's from New Jersey. What do you want? Uh, Montclair State University, SUNY Stony Brook, and at a bookstore near you, get your copy of Magazine in the Web We Weave, in the Gutenberg Parenthesis, now in paperback. Thank you, Jeff. Thank you, Paris.

**speaker_4** [140:09]: Thank you.

**Host** [140:09]: Thanks to all our club members who make this show possible. We will see you next week right heree on Intelligent Machines. Bye-bye. [upbeat music] I'm not a human being. Not into this animal scene. I'm an intelligent machine

