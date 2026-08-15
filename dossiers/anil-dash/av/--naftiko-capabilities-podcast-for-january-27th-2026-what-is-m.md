---
title: "Naftiko Capabilities Podcast for January 27th, 2026 - What is Markdown?"
person: anil-dash
section: by
type: talk-transcript
year: n.d.
venue: ""
source_url: https://www.youtube.com/watch?v=OXYS6qCp8OQ
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 17
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Naftiko Capabilities Podcast for January 27th, 2026 - What is Markdown?

*Speakers (inferred):* speaker_0=Ken Lane, speaker_1=Anil Dash

## Transcript
**Ken Lane** [00:00]: [upbeat music] Hello, welcome to the Navtico Capabilities Podcast. My name is Ken Lane. I'm the chief community officer for Navtico, but you might also know me as API Evangelist, where I've been talking about the technology, business, and politics of APIs since 2010. This is my podcast. We're three to four weeks in, so I, I don't think I need to talk about it being new anymore. But, uh, I'm producing two of them a week, Tuesdays and Thursdays, and trying to keep them to about 15 to 20 minutes. But let's dive in. This is another one of those episodes where, uh, it's just one guest and one topic. Um, I sat down with my friend and, and blogger and creator and just all around interesting personality, Anil Dash. I've known him... I don't know, he's always been there. [laughs] He's always been part of the, the, the web and the blogosphere, and kind of that, what I would consider that first wave in this century. And, uh, but more recently, he created Glitch, which is a really interesting, uh, coding and collaboration platform. It got acquired by Fastly. And then now Anil's back to blogging and kind of, uh, back to his roots doing, uh, what he's done, done for years. Uh, so he had published a blog post on Markdown that I thought was an interesting kind of history and explainer of Markdown, because he was there in the beginning. But also kind of h- what it's become as this ubiquitous format that, that, that is everywhere. Um, and, uh, so I sat down with Anil, and I asked him, "What is Markdown?"

**Anil Dash** [01:38]: You know, at the simplest level, Markdown is a pl- format for a plain text file, which, um, you know, there's a lot of precedent going back many, many years, which is sort of just the convention a lot of people follow. If you want to do a bulleted list, you put an asterisk at the beginning of the line, and then you, you know, put your text after it. And, um, you know, what John Gruber did was sort of recognize, one, that that's a behavior that people have, and two, that that was how he liked to write his blog posts. And then, you know, made a little, basically a Perl script that would take that and, and in a consistent way, transform that into HTML markup for his blog. Um, and, and he made that a plugin for, um, a content management system called Movable Type, uh, which I was the product manager for, you know, back in the day. We're going back now at this point 25 years ago, which is... I'm starting to feel, uh, you know, the age of saying that.

**Ken Lane** [02:31]: [laughs]

**Anil Dash** [02:31]: Um, but, but it was, um, you know, kind of the WordPress of its time. And, and it's, and it's hard to remember, you know, how small the internet was back then. But at that time, it was sort of, uh, you know, to, to be a little immodest, it was kind of the entirety of, like, influencer media and social media. You know, it was if you took all of WordPress and all of Sub Stack and kind of all of the influencers on even, you know, YouTube and all, and, and stuff, all those things didn't exist then, or Instagram. Everybody who wanted to have a presence online as an individual and have a voice online was on that platform.

**Ken Lane** [03:06]: Yeah.

**Anil Dash** [03:06]: And so that, that, you know, was a super, super influential platform. And John had recognized that because a lot of those other folks weren't very technical, the easier you could make it to make rich formatting, and not just bullet points, but bold, italics, and links, and images, without having to learn HTML, and without the risk of breaking the formatting of your site, the more powerful it was gonna be. And my personal lens on it was, um... I mean, this is again one of those things that tell, tells you how long ago it was. There was no such field or practice in the industry as developer relations or developer experience. You know, I, I had that role, but there wasn't a title for it. Um, and so I was creating, you know, what would today be called sort of a, you know, a developer platform or whatever, and it was really part of me launching our ability to have plugins. [laughs] And, and that was really one of the first ones. And so, um, I, I would say from my POV, it was probably the greatest success I've had in developer relations-

**Ken Lane** [04:17]: Wow

**Anil Dash** [04:17]: ... was, was helping to shepherd, you know, Markdown out to the internet. And, and he made a brilliant thing. He beta tested it with our mutual late friend, um, Aaron Swartz, who had great feedback for him, and put it out in the world, and it was immediately a success. Everybody could sort of saw the value of it. And then, you know, for a couple of years, it was sort of a slow roll. And then, you know, you go maybe five, six years down the road, and, um, it was picked up in short order then in rapid succession by, um, by GitHub. And, you know, and, and I'd, I'd seen the founders sort of there, uh, implement it in, in, in, you know, their, um... As soon as they made that ability to show a README, and, and Stack Overflow, where I was, you know, very close with the founding team and on the board and, um, saw them, you know, especially Jeff Atwood, who was very vocal about sort of trying to standardize the way that Markdown worked on that site. And of course, those two sites also both each had their own flavors of Markdown. But particularly because everybody on Stack Overflow and everybody on GitHub were developers, since they were exposed to Markdown in the place where developers got together, they then perpetuated it building into their own tools.

**Ken Lane** [05:40]: It's a fascinating journey in, in the history of how, how something so simple and, and creative, uh, can be, can be produced and, and put out there, but then also, uh, spread like wildfire everywhere. But what I was also interested in is this kind of collision with this AI moment, and I wanted to understand what the relationship between Markdown and, and AI is as, as Anil saw it.

**Anil Dash** [06:06]: Yeah. Yeah. I mean, it is... It's interesting 'cause it's sort of the control plane for AI, you know? And you could have the most cutting edge, advanced LLM, you know, frontier model from a trillion dollar company, and you're making a plain text markdown file to try, [laughs] to try and orchestrate it, right? And w- i- in the most low tech, basic pla- Like, you can use a Windows Notepad. Well, I guess Notepad has an LLM in it these days.

**Ken Lane** [06:34]: Uh-huh.

**Anil Dash** [06:34]: But, like, [laughs] you can, you can use, you know, you know, you can be in Vim and making this plain text file and, and it's gonna be how you control it. And I think that's a pretty extraordinary thing. I, I was talking to a friend the other day and saying it, it, it's a... It almost feels like, um, what Unix pipes are, but the next layer of the stack up.

**Ken Lane** [06:55]: Mm-hmm.

**Anil Dash** [06:55]: It's that, you know, pervasive and that default a level of, of, of piping information sort of connecting through and, and, and a default assumption. And, um, and there is one other thing that I think was really non-obvious to me at the beginning, but that has stuck with me, is in the early days, in the first several years, I, as a coder and a person that builds systems, it made me very itchy that it was so non-standard. I knew there were edge cases where it's like, "Well, you didn't tightly specify what to do with this," you know?

**Ken Lane** [07:29]: Mm-hmm.

**Anil Dash** [07:29]: And I was like, "That, that's wrong. It's not technically correct," you know?

**Ken Lane** [07:33]: Yeah.

**Anil Dash** [07:33]: And now with the hindsight of 20-plus years, I, I, again, I, I still... It makes me itchy to say this. I think that's part of why it succeeded.

**Ken Lane** [07:46]: Yeah.

**Anil Dash** [07:47]: And I hate to say that, but that is the real world. And, and the example I would point to that, that illustrates this is HTML itself, right? Which is that... And now, you, you, you and I know that there is a, there is a tight specification, right? So HTML5, like post-5 era is tightly specified. But HTML that got adopted w-

**Ken Lane** [08:08]: Yeah

**Anil Dash** [08:08]: ... you know, w- was, might as well have been scrawled on the back of an envelope, you know? And, and, and, and around the same era, actually f- within months of when Markdown was created is really when RSS became what it was. Like, the spec had been around and people were adopting, but when RSS, like, really took off, and the way that it would be used to support podcasting and all these things that took off, um, it was, you know, subject to quite emotional and pointed and k- you know, very tense battles within the community by people who were like, "We absolutely have to standardize it and there needs to be a formal XML spec and we're gonna take it to IETF." And, and I was very much a part of that community and very big believer in it. And none of that amounted to a hill of beans.

**Ken Lane** [08:55]: Yeah.

**Anil Dash** [08:55]: Like, the thing that actually worked was, like, just kinda make it work, and, like, we'll run some conformance tests and somebody make a little, you know, a profile that's, like, kinda good enough. And, um, and, and, you know, that's one of those things that I think has been a really interesting lesson and, especially for me, been very instructive about how I look at community and developer relations-

**Ken Lane** [09:18]: Yeah

**Anil Dash** [09:18]: ... the technical specs of what it takes to make things succeed, and also that the bias I had towards, understandably, technical correctness and standardization also makes things easier for big companies to take over and for capture by the people who have a budget to send somebody to a standards meeting-

**Ken Lane** [09:37]: Mm-hmm

**Anil Dash** [09:37]: ... or to run a standards body and to what becomes [laughs] gentrification and, you know, all these other things. Or, or to being tied into a, a, you know, a SaaS service and a subscription and, and enterprise, you know, suitability. And I'm like, maybe I don't want enterprise extensions in my spec.

**Ken Lane** [09:55]: Yeah.

**Anil Dash** [09:55]: Right?

**Ken Lane** [09:55]: Yeah.

**Anil Dash** [09:55]: 'Cause I, uh, uh, I, you know, Markdown enterprise grade would've probably been a nightmare actually.

**Ken Lane** [10:02]: Yeah.

**Anil Dash** [10:02]: And, and so the, the fact that it isn't... That it is a little bit of a toy is, is part of why it's so good. And so that, that was a real... That's a difference between what I thought then and what I know now-

**Ken Lane** [10:16]: Yeah

**Anil Dash** [10:16]: ... with h- you know, half my life has passed.

**Ken Lane** [10:19]: There's a lot of wisdom in there and a lot of, uh, I think w- things we can learn, uh, from as we build other standards and, and cultivate new standards and, and grow the ones that we've had for a while and kinda make them work together. But I wanted to understand more, uh, what, what is an optimal kinda ecosystem for this growth when it comes to open source commercial interests and, and community? How does it work? And, and, and what he learned from the, the, the journey with Markdown.

**Anil Dash** [10:50]: We go through these expansion/contraction cycles and, and, you know, I, I've seen that go through so many times. So, so, you know, in the same company, this company called Six Apart that we made, um, at CMS Movable Type, and later on we acquired, um, LiveJournal, which was one of the first social networks and, and, and they did so much pioneering work. They made Memcache. And in the room with these guys, you know, these folks, we, we, um, created the first versions of OpenID and worked with teams to make OAuth and OEmbed and, you know, and other things. And the first versions were, you know, Markdown style. [laughs] Like, I could implement them even as a lousy coder.

**Ken Lane** [11:32]: Mm-hmm.

**Anil Dash** [11:33]: And then they all kinda got enterprised up. And at the time, as a dev rel, DevX kinda person, I was so excited. I'm like, "Oh, Microsoft's on board? Awesome." [laughs]

**Ken Lane** [11:45]: Yeah.

**Anil Dash** [11:45]: You know?

**Ken Lane** [11:46]: Yeah.

**Anil Dash** [11:46]: And then you got to the version that was enterprise grade, and IBM was on board, and what I thought was validation made it impossible to implement. All of a sudden I was like, how do you... What... How... What do... Like, I don't understand this.

**Ken Lane** [12:06]: Yeah.

**Anil Dash** [12:06]: I can't... Now what I used to be able to hack together by viewing source- It's gonna take me all weekend just to get it running and none of this has to do with my actual app.

**Ken Lane** [12:17]: Yeah.

**Anil Dash** [12:17]: You know? And that was a real, um... That was really humbling about what I thought mattered and, and, you know, w- what am I really trying to achieve here, and how much of it was ego about me wanting to have a thing on my resume, and later my LinkedIn-

**Ken Lane** [12:34]: Mm-hmm

**Anil Dash** [12:34]: ... that said, "Created standard that was adopted by"-

**Ken Lane** [12:38]: Mm-hmm

**Anil Dash** [12:39]: ... "insert billion-dollar company name here."

**Ken Lane** [12:42]: Yeah.

**Anil Dash** [12:42]: Versus what I really care about, which was, here's the thing all these people use that they make-

**Ken Lane** [12:48]: Yeah

**Anil Dash** [12:48]: ... real things with.

**Ken Lane** [12:50]: Yeah.

**Anil Dash** [12:50]: And, and that's a, you know, that's a thing that only... It does come with experience and does come with what do you really care about, what do you value. And, um, and also, you know, one of the reasons I wrote this piece about Markdown very unapologetically was to remember, you know, my friend Aaron Swartz.

**Ken Lane** [13:08]: Yeah.

**Anil Dash** [13:09]: You know? And, and to have it be the real version of him. He, you know, he was an activist, very much so, and, and proudly so. Um, but one of the double, you know, edged parts of that is that since he passed when he was very young, there's sort of been a mythology that sprung up around him, and people will put, you know, this sort of halo, exalted. And he, he was a wonderful person and had great values, but, but it, it makes it a little less real version of him. And so I wanted to give a little bit of the sort of funnier and pricklier and, and, and whatever version of him. And so, a- and even John too. You know, John's been a friend for, again, 25 years now. And to... If s- somebody, I think on Hacker News or something was kind of like... I, I'd opened the piece by mentioning, like, he's a [laughs] he's a friend of, I think it said a indefensible sports team, and they were like, "Why does he say this terrible thing about, you know, this guy?" And I'm like, you know, you, you gotta be able to, like, poke your friend, you know what I mean? [laughs] Like, it's kind of like you're just busting shop. And I think they just didn't realize, like, these are people.

**Ken Lane** [14:11]: Mm-hmm.

**Anil Dash** [14:12]: You know, this is somebody I, you know, text to ask how his kid is doing. You know, you know, this is, like, it's real life, and I think people have not understood that the entire internet is made of, like, regular people who in between, you know, going out for beers together or, or, or, um, uh, h- did you plant your seeds for your garden this spring yet?

**Ken Lane** [14:37]: Mm-hmm.

**Anil Dash** [14:37]: Are, are, are viewing source and copying and pasting, and that's what it is. That's how it was made, and that's how it could be made again.

**Ken Lane** [14:46]: I love these organic kind of accidental happy accidents of standards and specifications that happen, 'cause I think they, they start with, you know, trying to solve a problem, and then they kind of spread intentionally but unintentionally and grow in different ways. And I think there's a lot we can learn from Markdown and i- uh, its simplicity, uh, its, its kind of, uh, roughness. Um, there's, there's a lot to it that I think we need to think about, uh, when we evolve other standards, and definitely embrace, uh, Markdown as part of whatever new standard you're, you're producing. It's, it's one of those cross-cutting standards that, that matter a, a lot. All right. Well, I think that's it for the Capabilities podcast today. Um, hope you enjoyed it, and, uh, I'll see you next time. Hey, I wanna talk about my, uh, Navtico Signals program. I'm looking for design partners who have integration, governance, and, uh, other issues when it comes to, uh, API reusability as well as, uh, context engineering. So how do you take those APIs and, and spin them into the, the MCP servers and, and other things you're gonna need, uh, to plug in and integrate AI into the enterprise. And then, uh, anything to do with the automation, the agentic, anything around that. So those are the top three use cases I'm looking to talk to folks on, and I'm studying how, uh, different enterprises are, are tackling this. Um, and, uh, and I would love to talk to you if, if, if, if you've got the time. So reach out, easy to find on LinkedIn and Blue Sky, and then you can just ping me at kenlane@navtico.io. All right. Thanks. [outro music]

