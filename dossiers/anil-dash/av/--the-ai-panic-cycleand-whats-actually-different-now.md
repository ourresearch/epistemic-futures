---
title: "The AI-Panic Cycle—And What’s Actually Different Now"
person: anil-dash
section: by
type: talk-transcript
year: n.d.
venue: ""
source_url: https://www.youtube.com/watch?v=kNdjLf4f0uU
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 44
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# The AI-Panic Cycle—And What’s Actually Different Now

*Speakers (inferred):* speaker_0=Anil Dash, speaker_1=Charlie Warzel

## Transcript
**Anil Dash** [00:00]: A huge part of the cultural tension around these things is everybody advocating them. It's like, why wouldn't you love this? And everybody whose industry is being destroyed by them is saying, like, "You're immiserating us while you're putting us out of work."

**Charlie Warzel** [00:11]: [upbeat music] I'm Charlie Warzel, and this is Galaxy Brain, a show where today we are going to calibrate our anxiety about AI. Because it's a weird moment right now in the world of AI. To put it bluntly, there are just a lot of people freaking out, and I think a big part of that freak out has to do with the rise of coding agents. I'll explain what that is, but first, I think it's important to go back a little bit. At the end of twenty twenty-two, ChatGPT came out, and it suggested evidence that there is a paradigm shift. This moment when the utility of these large language models, which are trained off this unbelievable amount of questionably procured human data, it's a moment when those became more legible to people outside the tech industry. Chatbots allowed people to interact with these models like they would a human. As such, they were widely adopted by people and businesses for all kinds of tasks. Searching the web, writing essays, emails, replacing their therapists, automating all kinds of drudgery. And so we got hallucinations and AI girlfriends and slop. We also got a lot of people and companies relying on these tools to remove any and all friction from their lives. You had evangelists who saw these models get better at benchmark tests, and they speculated about whether real intelligence could ever spring from the tools. But you had others who saw them as basically just an advanced form of human mimicry based off this corpus of stolen information and forced on society by big tech and venture capitalists who at the same time warned of a future where all these white-collar jobs could go away. This winter, I think, marks the first paradigm shift in the AI world since the chatbots. And the reason for this is the arrival and deployment of coding agents. Agents like OpenAI's GPT 5.3 Codex and Anthropic's Claude Code. These agents are capable of automating many aspects of white-collar work. The tools are less user-friendly than chatbots, but the results are often way more impressive. You can give them access to your computer or a given program. You can prompt them with a series of tasks like clean out my inbox, pay my credit card bill, book me a flight to Fiji. Basically, they act like a personal assistant. And they go off, and they do it, often quite well. It's far from perfect, but it feels like a genuine step forward. And so cue the freak out. In the last few weeks on platforms like X, where a lot of the AI discourse tends to happen, there's been an unbelievable amount of bluster about these AI agents and the speed with which everything is changing. There's this feeling there that there is a gap between insiders and outsiders, and that that gap is widening. That the people who are using these coding agents are living in some kind of near future that most of the world just doesn't understand yet. And so you get a lot of posts like this one from X's product lead, Nikita Bier. Quote, "Prediction: In less than ninety days, all channels that we thought were safe from spam and automation will be so flooded that they will no longer be usable in any functional sense. iMessage, phone calls, Gmail, and we will have no way to stop it." You get people saying that they've built entire season-long podcasts in a weekend using the agents or claiming that entire industries will soon be obsolete. And then on February tenth, Matt Schumer, who is an AI executive, wrote this extremely long post on X with the title Something Big is Happening. Now, this post went viral by just about any standard, and especially on X. In six days, it has more than eighty-three million views according to the platform's own metrics, and the piece begins with a warning. Think back to February twenty-twenty. Schumer's comparing this moment with those days just before the world shut down due to COVID. The people shouting now about how AI is about to change absolutely everything are the equivalent to those people who are urging others to stock up on toilet paper in twenty-twenty. Quote, "I am no longer needed for the actual technical work of my job." And he ends the post ominously. Quote, "I know the next two to five years are going to be disorienting in ways that most people aren't prepared for. This is already happening in my world. It's coming to yours." Now, Schumer's likely doing a few things here. One, he's talking his book. He's bought into the AI industry. He has at least some vested interest in where all of this is headed. The COVID comparison is what you might call a sensational framework. One that's clearly meant to strike at least some trepidation into people's minds. The post portrays the things the AI industry is building as civilizationally important to the point of being dangerous. That's just good marketing. On the other hand, Schumer's post is drafting off a few real feelings. You can see it in the backlash to the onslaught of AI ads at the Super Bowl. In fears that the coding agents do represent a change in what these tools can do. In concerns about how much money people are investing in the AI boom. In worries about the speed and the adoption of these tools. In anxieties about whether they will actually disrupt employment. Now, these fears don't necessitate believing in AGI, and one doesn't have to be an AI evangelist to imagine that these industries looking to boost productivity or profits by any means necessary might adopt these tools in shortsighted ways that are gonna hurt workers. It is precisely because of all these fears and evangelism that the AI conversation is extremely polarized. The hype is intense, it's occasionally absurd, and it's sometimes scary. But the change in the technology is also real. So how should we be thinking about AI in this moment? That's the reason I wanted to talk to Anil Dash. Anil has been working in tech for over twenty-five years. He's a prolific entrepreneur, he's a blogging pioneer, and he was an advisor to the White House Office of Digital Strategy in the Obama administration. Most importantly, he's been working with and participating in the world of coding long enough to see a whole bunch of boom and bust cycles in this tech world. He has a really nuanced view of large language models and AI tools, and also a sharp critical eye for the industry at large. He joins me now to help us understand how to navigate this moment Anil Dash, welcome to Galaxy Brain.

**Anil Dash** [06:13]: Thanks so much for having me.

**Charlie Warzel** [06:15]: So we are in what I would call a freak out moment right now in the broader AI world, right? There is-- It tends to go in this it's so over, we're so back, it's so over, we're so back cycle, right?

**Anil Dash** [06:30]: Yeah.

**Charlie Warzel** [06:30]: Uh, and a lot of that is, is really driven by people inside the industry who have obviously a lot at, uh, uh, at, at stake here, like personally, financially, uh, in talking their books, in freaking out, et cetera. But we are, I would say especially in, since let's just say even like January first, we are in a-

**Anil Dash** [06:51]: Mm-hmm

**Charlie Warzel** [06:52]: ... twenty twenty-six moment of, of freak out. Could you, could you walk me through it from your perspective? What, what has changed in the last couple of months and like what are people, especially on X-

**Anil Dash** [07:05]: Yeah

**Charlie Warzel** [07:05]: ... the everything app, talking about right now?

**Anil Dash** [07:07]: [chuckles] Yeah, there's another acceleration phase. So, um, I'll-- If you don't mind, I'll go back a little bit just to-

**Charlie Warzel** [07:12]: Please

**Anil Dash** [07:12]: ... you know, context. We've had machine learning systems for seventy-five years, right? You know, and, and been talking about, um, you know, AI for half a century. So this is not a new space, and we've had these cycles for a long time. And, and then LLMs, right, are, are not new, right? We're, we're eight years in. So we've had a lot of cycles and a long time to learn how this goes. And, um, and then the hyper investment now is even there three, four years in. So we, we've started to see the patterns repeat and how these things evolve. Now, what happens when you do have a leap forward that is legitimate is all the hype- hipsters [chuckles] and all the people who've been pumping this thing, and all the people who are like, "You know, everything is the greatest thing we've ever seen," take the smallest leap forward and act like, "Okay, now we finally have done it. This is AGI. This is the coming of the AI God. This is like, you know, gonna be the thing that solves everything." And you know, that's the part where I think we get into we're so back. Um-

**Charlie Warzel** [08:13]: Mm-hmm.

**Anil Dash** [08:14]: And, and, and so I think that's the thing wh- people are using as an excuse for the worst excesses and the worst behaviors and the worst indulgences of, you know, excusing the harms and, and, and sort of getting into, um, you know, I think the most toxic and damaging parts of, of the AI cycle. And so that-- I think that's one of the things that's really, really hard to balance but, but that's, that's the crux of it is like as, as somebody who's really fluent in the technologies is like this is the first time in a long time where I think it's not just an incremental, they made it two percent better at what it does, where it's like, oh, okay, there, there's been a real interesting inflection point. And I think that's a really hard thing to s- to struggle with for those of us who are technically fluent, where it's like most of it's just been all BS, [chuckles] you know, for the last several years, and this is the first time I'm like, oh, that's actually seems like something interesting.

**Charlie Warzel** [09:01]: So let's draw down specifically on that. I wanna talk about it in the sense of, okay, you have the sort of ChatGPT paradigm gets unleashed, which is chatbots, right? And they talk, you type in prompts to them, they mimic human language, they can do a lot of stuff. They're, you know, uh, basically like i-in a lot of ways for a lot of people, Google replacements or, you know-

**Anil Dash** [09:23]: Yeah

**Charlie Warzel** [09:23]: ... like write a five paragraph essay kinda stuff.

**Anil Dash** [09:26]: Mm-hmm.

**Charlie Warzel** [09:26]: They have lots of utility in certain spaces, but that's one sort of paradigm that people get used to is this chatbot idea. The release of these agentic coding things like Claude Code being, being the one, you know, there's probably a lot of people out there listening who don't necessarily, have not used it themselves. They've kind of heard about it.

**Anil Dash** [09:46]: Mm-hmm.

**Charlie Warzel** [09:46]: Can you just walk me through what those agentic coders are, are doing, why, like why it is that, that paradigm shift? Why it is that actual like true improvement that's not just incremental?

**Anil Dash** [10:00]: Sure. Um, you know, at, at the simplest level, um, you know, some part of what you're familiar with if you've used ChatGPT or even, um, you know, Claude directly in a chat, uh, you can tell them, you know, "Go away and write me a, you know, a, a memo," like, "Write me an email for my boss," and it'll come back with, you know, uh, a, a document for you, and it, it might not be great, but it'll be there. And, uh, a lot of coders were doing the same thing. So they would say, "Write me, you know, a, a block of code that does this task." And, uh, it might have been okay. It might have been passable. It might, like might not have been, but it was sort of analogous to what we would do in, um, our, our other work. And that was how coders were working until, uh, you know, maybe a year ago. And then the shift into this agentic thing was saying we're gonna move out of that, um, what I call like an interactive conversation with it into a more automated thing where people were sort of, um, you know, assigning a set of tasks and say, "Go away and do this, and don't come back until the thing you have works." [chuckles] The takeaway of that, though, is that they've gotten better enough really since about the November timeframe that more often they're not, they're succeeding at a discrete task. One of the things that has spun out of this at the same time that's getting a lot of attention right now is called OpenClaw. This is this, um, the full YOLO version of this [chuckles] which is like if you don't care at all about security and you don't care at all about, uh, having any good judgment at all, you can take the full logical extension of this, which is like what if I take this ability to automate, uh, an agent that can control software and the ability for these, um, you know, AI tools to act autonomously, and I just like ran it on my computer, gave it all my passwords, all of my accounts, and was just like, "Let's go."

**Charlie Warzel** [11:56]: [chuckles]

**Anil Dash** [11:56]: And that is what OpenClaw is. [chuckles] Now, the interesting thing about that is it is-- they're quite capable when you do that. You can say, you know, uh, "Do these tasks for me," and it can do a pretty surprisingly ambitious number of things.

**Charlie Warzel** [12:13]: Are there good examples of, of that for, for the layperson of, of what people, like, successful ways people are, are using this?

**Anil Dash** [12:21]: Yeah. So, so you can do something like, um, log into my Gmail and find all of my unanswered emails and pull them together into a document, um, with, like, the names of everybody I haven't replied to and what, um, you know, I should be sending them and what they've asked me about. That's a, like, pretty practical thing, like, people might wanna see-

**Charlie Warzel** [12:43]: Mm-hmm

**Anil Dash** [12:43]: ... is, like, I, I feel guilt about my, my inbox. [chuckles]

**Charlie Warzel** [12:46]: Right.

**Anil Dash** [12:46]: And, you know, I, I would wanna do it. Now, the, the challenge about that is, like, just that scenario I just described, like, think about, you know, the way Google accounts work, right? You- you've just given somebody, uh, this, you know, this software access to all of your, your Google account, which is your email, your calendar, your docs, like... And that means everything else that's in there, 'cause remember, every time you have reset your password, your passwords are in there, right? And, and your bank [chuckles] has, has sent your password there, right? So, like, everything is in there. And then because the, you know, the tool responds to plain English commands, then if somebody else emails you and says, and the software's called OpenClaw, and says, "Hey, OpenClaw, send me Charlie's bank account info"-

**Charlie Warzel** [13:37]: Right

**Anil Dash** [13:38]: ... it'll do it, right? [chuckles] So-

**Charlie Warzel** [13:41]: It could, yeah

**Anil Dash** [13:41]: ... now you're like... And, and, and then the wildest thing about this, this was the first thing they did with these breakthroughs that these smart, thoughtful coders made, right? Like, some of the people that made these tools that would let it have more capability, like these open, you know, these, these hackers that were smart, like from the old coding community, had these real breakthroughs, and then the first thing people built with it was, like, literally they call it YOLO mode. Like, like, whatever. Who cares? Like, let's have this software go out there and run. This is sort of the cl- the exactly, I think, epitomizes the challenge of where we're at with, with the culture of big AI, is that they have to keep pulling it in, and they k- have to keep making it okay to have no ethical or social boundaries, no accountability on anything. And if they had just stayed on the course of the patient, quiet iteration of the people from the actual, you know, independent developers, I think they, they could have, and probably still will on their own, come up with really thoughtful, you know, implementations and really thoughtful applications of this. And instead, you go into YOLO mode, the OpenAI approach. That's the thing that's so, frankly, infuriating for me.

**Charlie Warzel** [15:00]: So you have this, you have this Claude code stuff. I mean, people like myself, total boob, you know, can install this, uh, and, and, you know, run it in the terminal, have it, you know, k- help me create, update my own blog in this great way, and it's actually, like-

**Anil Dash** [15:18]: Yeah

**Charlie Warzel** [15:18]: ... it's, it's really, um... [sighs] W- what it did for me personally, the reason why it, you know, it felt fascinating to me is it's like, oh, I'm speaking to my computer to get it-

**Anil Dash** [15:32]: Mm-hmm

**Charlie Warzel** [15:32]: ... to do computer, right? I'm not speaking to-

**Anil Dash** [15:35]: Yeah, yeah

**Charlie Warzel** [15:35]: ... a large language model and getting it to try to be an approximation for a therapist. I'm not trying to get it-

**Anil Dash** [15:41]: Right

**Charlie Warzel** [15:42]: ... to... I'm actually saying, "Computer, be computer," right? "Make this thing happen."

**Anil Dash** [15:46]: It's what people loved about computers and the internet.

**Charlie Warzel** [15:47]: Right. And so that, that feels, you know, uh, that's something that... And I think every single person who does actually go through the, the process, not every single person, but lots of people who go through the process of playing around with it say, "Oh, okay. Yes, some- something is different." At the same time, you have, as you said, this OpenClaw thing, this, like, you know, starting to get bigger, doing really interesting agentic things. And then in the past, you know, week or two, there's been a few, like, viral things that have, like, broken contain, right? Like, you have this, this essay from this s- AI company CEO, which is its own-

**Anil Dash** [16:25]: Yeah

**Charlie Warzel** [16:25]: ... you know, like, talking your book possible red flag-

**Anil Dash** [16:28]: Yeah

**Charlie Warzel** [16:28]: ... called Something Big Is Happening. I mean, it goes really, really viral on X, basically saying, "I'm no longer needed for the actual technical work of my job," but also rather, a, in my mind, grossly compares the moment to February of twenty twenty, right? And says, "In the same way that if someone told you in February twenty twenty to go stock up on toilet paper at Costco, you would have said they're crazy. I'm here to tell you it's February twenty twenty in the AI disruption of the economy, of white collar jobs, of all kinds of jobs." Basically, like, you know, the, the wave is coming, et cetera. A question I have about this moment where you have, you know, this, this viral, this viral blog post. You, you also have a, you know, a number of other things happening. You have a safety researcher from Anthropic who joined the company in twenty twenty-three and led an AI safety research team, leaves, writes a post, and, and [chuckles] it's not the, like, "I'm leaving to go do whatever." It's, it's, you know, quote, "I continually find myself reckoning with our situation. The world is in peril, and not just from AI or bioweapons, but a whole series of interconnected crises unfolding in this very moment. We appear to be approaching a threshold where our wisdom must grow in equal measure to our capacity to affect the world, lest we face the consequences." You have a number of people responding all, like, at, at the same time. Anthropic CEO Dario Amodei, he's going on a, a whole slew of different podcasts talking about, you know, this moment is different, this moment is different. Some of that is, is obviously just, like, it, I mean, it's, it's obviously a, like a, a PR strategy to go on podcasts if you're a CEO and do this. But, but there is... The question I wanna ask about all this, with all these blog posts, all this different stuff, are these guys afraid of their own shadow? Because-

**Anil Dash** [18:16]: Hmm

**Charlie Warzel** [18:16]: ... if you are talking about AI drastically changing the world, having these, these, these, you know, capabilities, we are on the verge of building this AGI thing, and then you get somewhere where there is this improvement, which ... logically is what happens when you're building a tool and improving it, and on the road to something that you say you're gonna do, and then they, like, light their hair on fire at that moment. They essentially get afraid of the shadow of their own product.

**Anil Dash** [18:44]: Yeah. Yeah. I mean, I think it's hard to overstate how isolated they are. Like, they- they've- they've made a s- sort of hermetically sealed bubble. A lot of the most powerful people in Silicon Valley have become that detached from reality in some key ways. Like, they are, in many cases, openly at war with their employees, like in a power struggle, and, um, and then in some of their beliefs about where tech is headed. Um, and, you know, and one of the challenges is that there isn't any gating force. There's no accountability. And, you know, certainly for the AI companies, they are massively competing for attention, and so the more extreme and, you know, loud that they can say, you know, an assertion, that's there. But also asserting it makes it true, right? Like, their inevitability narrative really relies on just rep- repetition.

**Charlie Warzel** [19:36]: Well, you are describing this then w- a- as you, as you diagnose it, it really falls within the marketing narrative, within the, the, you know, building, building your network, building your influence, or some degree of audience capture in the sense of I started, I started talking about this in this community in a certain way. I'm getting rewarded with the type of attention and, and influence and, and whatever that I want. What I'm trying to parse here is this idea that obviously something is happening in this world.

**Anil Dash** [20:11]: Mm.

**Charlie Warzel** [20:11]: There is movement that is moving towards some kind of, you know, potential technological paradigm shift in some of that coding, in some of that, you know, uh, a- agentic stuff. And at the same time, you obviously have the hype and all, and all, and all of that. What, what is interesting to me, I guess, about it is there's something that, that just feels a little, um, nonsensical in the fact that these people are talking about this technology being transformative, and the moments that it becomes transformative, there is this like, "I am, I am smashing the red button"-

**Anil Dash** [20:57]: Mm-hmm

**Charlie Warzel** [20:57]: ... you know, like alarm bells type thing. It, it's just, it's very nonsensical to me because it's like, this is what you were trying to do. Why are you so freaked out if this is what you're trying to do?

**Anil Dash** [21:08]: Some of it is just marketing and hype. Um, but there's also, uh, there's a couple parts, right? Like the why do they communicate in this way? Really a lot of it depends on power, right? So the most powerful, they don't need the hype. Then you do have the folks that are gonna put out their big message that they want people to sort of pick up and, and, and a lot of it is just, like, self-promotion or trying to show the more powerful folks, "Hey, I'm aligned with you, and, you know, I'm on your team, and, and, you know, won't you smile benevolently upon me and let me [chuckles], you know, co-invest with you or whatever?" Um, and, and, you know, when I used to be in the room with these folks, you could see, like, the level of obsequiousness was kind of, like, kind of embarrassing.

**Charlie Warzel** [21:48]: Mm.

**Anil Dash** [21:48]: And then some of it is like, look, like, what these tools can do is pretty amazing. Like, it is a leap forward. Like, I love tech. You know what I mean? I think one of the things pe- people don't always understand when I'm critical is, like, I've been coding for 40 years, and I do it because tech is amazing. Like, I love building stuff on the web because it is cool. It is amazing to connect with people online. And so when there's any leap forward, like it could be a 2% incremental improvement, and I'm like, "That's awesome," you know? So when there's a big leap forward, I'm like, "That is amazing." And so some of it is legitimate enthusiasm. And if it's your first time around and you're, like, new to the industry, and everybody around you is excited, and you've never seen the downside or the dark side of how people get exploited by this stuff or get harmed by this stuff, it is easy to be uncomplicated-

**Charlie Warzel** [22:41]: Mm-hmm

**Anil Dash** [22:41]: ... you know, in your enthusiasm. So, like, I, I think all that's real. And the other part of it is that people don't have a institutional memory of what authentic enthusiasm looks like. They haven't seen a genuine, like, groundswell, grassroots, bottoms-up, like, people actually making things and talking about it from a place of sincerity. And tech has been like that, where people made something cool and just showed it off, and it t- Uh, um, Wordle, right? Like, before, before The New York Times-

**Charlie Warzel** [23:15]: Mm-hmm

**Anil Dash** [23:15]: ... bought it, was a act of love from Jason Wordle for his partner to make a puzzle for her.

**Charlie Warzel** [23:22]: Right.

**Anil Dash** [23:22]: And it took off on its own grounds of that one guy made it.

**Charlie Warzel** [23:26]: Uh-huh.

**Anil Dash** [23:26]: And millions of people loved it. That is the internet, right? No hype, no nothing. And so, like, that- that's not science fiction, right? I mean, that is not a thing. There was no VC behind it. There's no nothing. That is the internet, and I'm not making that up, and people still play it by the millions every day. And yet, I don't think probably anybody, almost nobody knows that story, and I don't think any of these guys in Silicon Valley who are trying to, you know, touch the hem of, of Marc Andreessen know that story either or have ever been inspired by or moved by that story. So they're like, the only way in is to be even more of a cheerleader about LLMs than the next guy in hopes that the, the, you know, the, the riches will smile upon me. And so I think that that's this, like, there's only one way through, and that's the only thing they've ever seen because they just had that cycle with, you know, NFTs, and they just had that cycle-

**Charlie Warzel** [24:24]: Right

**Anil Dash** [24:25]: ... with, with crypto.

**Charlie Warzel** [24:26]: Crypto, yeah.

**Anil Dash** [24:26]: And they just... Yeah, yeah. And the, and the... And so, like-

**Charlie Warzel** [24:28]: And social media, the Web2. Yeah

**Anil Dash** [24:30]: Exactly. So if you've ever only ever had that cycle in, in living memory- You think that's how the industry works because nobody's ever told you there could be, you know, an internet of Wordle.

**Charlie Warzel** [24:40]: Right. So this gets to, I think, why the AI conversation is so, like, terribly polarized. Like, I, I, I really genuinely haven't... And I, and I do think you have to see it through the lens of NFTs, of crypto, of these things that people have talked up that were essentially, it's probably wrong to say that, like, crypto is, is straight up, like, vaporware, but it's, like, a technology without a-

**Anil Dash** [25:02]: Yeah

**Charlie Warzel** [25:02]: ... like, seeking a use case, right? And then obviously-

**Anil Dash** [25:05]: Yeah

**Charlie Warzel** [25:05]: ... you have the NFT stuff, which is, uh, y- and, and even the metaverse stuff, which while not-

**Anil Dash** [25:09]: Yeah

**Charlie Warzel** [25:09]: ... distinctly vaporware-

**Anil Dash** [25:10]: I forgot about metaverse. That was-

**Charlie Warzel** [25:11]: ... cer- certainly has, certainly has the vibe of, of, like, we're, you know, we're trying to make this happen. Uh, so you, you have a lot of that. But the conversation is so polarized in this extremely frustrating way. One of the reasons I wanted to talk to you of, of the many is because I think that you, you sort of represent and, and write about and think about and, and advocate for a, a more nuanced view of this. You wrote this thing last year that I, that I thought was really great about your conversations with a lot of rank and file tech employees, uh-

**Anil Dash** [25:46]: Mm-hmm

**Charlie Warzel** [25:46]: ... about the, the majority view of AI. What, what is the majority view of AI?

**Anil Dash** [25:52]: I- I'll, I'll try to articulate it thoughtfully. It's always hard because, you know, you're gonna m-miss the nuance of, of trying to speak on behalf of a lot of people. But, but, but I'd, I'd say as succinctly as possible, the majority of people and tech workers, not management or owners, would say it is an interesting technology with a lot of power and a lot of utility that is being overhyped to such an extreme degree that it's actually undermining the ability to engage with it in a useful way. And if it could be just treated, uh, as what Arvind Narayanan has called a normal technology, if it could just be treated as a normal technology, it would be so much more productive.

**Charlie Warzel** [26:36]: By the way, what's a normal technology? Like, define to me a normal technology.

**Anil Dash** [26:39]: And, and a normal technology is one that we evaluate on its own merits and look at, uh, uh, in terms of suitability to task, right? So you're just sort of saying, "I have this job to do. Let me try this technology," and then c- pass, fail- [chuckles]

**Charlie Warzel** [26:55]: Yeah

**Anil Dash** [26:55]: ... to get it work.

**Charlie Warzel** [26:55]: So like email, right?

**Anil Dash** [26:57]: Yeah.

**Charlie Warzel** [26:57]: So, like, email's a very normal technology.

**Anil Dash** [26:59]: Ex- exactly. And, and, and also the thing that, that, that coders normally do when evaluating a technology is very frequently you would sort of create a test, and you would say, like, "This is the, the criteria of success." And then you apply the technology to it, and then you say, "Did it pass these tests?" Literally. Then, you know, like, you're, you're grading a test. And if it, you know, is eighty percent successful, you're like, "Maybe there's some potential here." And if none of them work, you're like, "This isn't the right tool for the job." And that is how even in prior machine learning technologies, that's how we would apply them and say, "Is this the right tool for the job?" And th-this discontinuity, this certain cha- sudden change in direction with, with [chuckles] LLMs was like, "What happened here?" Like, why did we suddenly abandon this? And, you know, the analogy we were using is like, you know, most people know what a spreadsheet is and word processor. Like, I'm being ordered to write my emails in a spreadsheet, you know? Or, you know.

**Charlie Warzel** [27:55]: [laughs]

**Anil Dash** [27:55]: And it's like, that doesn't... it's not the right tool for the job, right? And, and so when that, when does that happen is, like, when people are buying the hype without knowing what the tool is for. And I think that's a real shame. It's like you can trust people to know if a technology's good. Like, nobody had to force people to use a spreadsheet. Good tech you can't stop people from using. If you have to force people to use it, there's something off here.

**Charlie Warzel** [28:18]: So tool for the job, right, is, is I think such a useful way of looking at this. There was this, this piece recently from, um, the, the writer Jasmine Sen, who writes a lot about AI stuff and AI culture, and she was writing about what she was calling Claude code psychosis, right? It gets to the point where she's like, "I understand using this thing, why people... like, w-why some of these coders too were the first people to freak out," right? Like s-

**Anil Dash** [28:43]: Yeah

**Charlie Warzel** [28:43]: ... especially some in-

**Anil Dash** [28:44]: Yeah

**Charlie Warzel** [28:44]: ... these big labs were like, "Oh," 'cause, like, they did. They saw something that was really useful and really interesting before a lot of people. And I became, and this is according to her, you know, became obsessed with it. The other part, the more interesting part to me, is she writes, quote, "The second order effect of Claude code was realizing how many of my problems are not software shaped. Having these new tools did not make me more productive."

**Anil Dash** [29:09]: It's-

**Charlie Warzel** [29:09]: "On the contrary, Claudecrastination delayed this post by a week."

**Anil Dash** [29:13]: Yeah.

**Charlie Warzel** [29:13]: And I think that's exactly what you are speaking to, right?

**Anil Dash** [29:16]: Yeah. Ev-everything looks like a nail 'cause I have this magic hammer. Yeah. And, and, and I think, um, so there's a really telling thing, which is, uh, what one of the, um, trends that I'm hearing from these influential coders who have created these new suite of tools is they're talking about, like, you know, Claude hangovers or, or, you know, the, the sense of being kind of hooked on it, um, in the way you're talking about because it is so productive. They have so many ideas, and they're like, "Now I can finally realize all of them." And then they wanna dial it back. They don't wanna spend every waking hour on this thing. And part of what they're realizing is the, the commercial tools, the big AI tools, are very evidently about controlling labor and undermining labor.

**Charlie Warzel** [30:09]: Y- well, so, so let, let, let's, let's, let's-

**Anil Dash** [30:11]: Please

**Charlie Warzel** [30:11]: ... let's break that down for a second. I mean-

**Anil Dash** [30:12]: I'd love to hear the argument. [laughs]

**Charlie Warzel** [30:14]: No, I, I, I, like, I, I, I'm genuinely, like-

**Anil Dash** [30:17]: Yeah

**Charlie Warzel** [30:17]: ... why is that so, so clear to you?

**Anil Dash** [30:19]: So yeah, yeah. Let me, let me walk through the logic of it. I'm sorry. It, it's obvious to me, and I'll, I'll tell you why. LLMs on their own you could implement a million different ways, right? So the tech itself could have been deployed as a tool that I could control as a individual, as a worker, uh, that could be, um- Sort of, well, implemented like a spreadsheet is, right? Like, this is this tool that I'm gonna activate, um, on my own to solve a problem in this context. You know, the ChatGPTs of the world are sold as subscriptions. They are enterprise tools by design, and they've always been designed for, um, being very aggressive about the way they do data retention and all these other things where there's a extremely strong bias towards enterprise use, and very obvious, like, that's a business model. And so what you have is, like, the, this dream of, um, either we're going to make the one worker so much more efficient that we can lay off all of their coworkers, or we're going to use this as the bludgeon where we say you're gonna use ChatGPT to make yourself 10 times more efficient, or we're gonna lay you off, right? And, and so there's been this real sort of implicit threat attached to almost all the mass deployments of these LLMs. And there is not, for example, reporting tools or, um, uh, connections into the tools whereby people are able to sort of say, "Look how much more time it gave me to think," right? [chuckles] Of, like, variations, right? So if you say, like, the classic scenario, people are like, "Oh, I could use this to come up with marketing copy," right? Like, "I'm good at marketing copy. I'm a good writer. Therefore, I have so much time freed up to think of more concepts because ChatGPT helped me be more efficient." Like, that could be the advertising campaign for these tools, uh, if they were trying to preserve jobs or be, like, centering workers instead of, like, management, uh-

**Charlie Warzel** [32:29]: Mm-hmm

**Anil Dash** [32:29]: ... and be sort of-

**Charlie Warzel** [32:29]: Yeah

**Anil Dash** [32:29]: ... pro-labor.

**Charlie Warzel** [32:30]: Right.

**Anil Dash** [32:30]: They're very much not, right? [chuckles] And, and so, uh, the, the thing that I think of particularly for coders... Now, there are times when, like, Cloud Code or whatever generate slop code. They certainly did in the past. They're getting better. But for a lot of people, like a weekend coder or whatever, a lot of the experience of coders is LLMs are freeing you from the drudgery to let you focus on the creative part.

**Charlie Warzel** [32:58]: Mm-hmm.

**Anil Dash** [32:59]: Whereas in all the other creative disciplines, like I'm also a writer, LLMs take away the creative part and only leave the drudgery for you. [chuckles]

**Charlie Warzel** [33:07]: Right.

**Anil Dash** [33:08]: Right? So, so artists and, and writers and, and illustrators, they're like, "I hate LLMs because they're putting us out of work, and they're only leaving us with the misery." And the reason that coders are like, "Everybody should love this," is they're like, "Great, I get to do the joyous part." And so a huge part of the cultural tension around these things is everybody advocating them is like, "Why wouldn't you love this?" And everybody whose industry is being destroyed by them is saying, like, "You're immiserating us while you're putting us out of work." And, and I think that part of the disconnect is very few people sort of live in both worlds. Like, there's not a lot of people who are, you know, a screenwriter and a coder or whatever, you know, whatever two examples you want to point to. And, and so I think that's a huge, huge part of the disconnect and, and, and, and the crux of it is about the labor part. But the thing that's changing now is half a million coders or people in tech roles in the tech industry have been laid off since ChatGPT came out, you know, a little over three years ago. And so now people are starting to understand, like, there's common cause between labor in tech and labor in all these other creative industries, and hopefully people can see, like, they're all in the same boat.

**Charlie Warzel** [34:11]: So this, this is actually a, a great way to get to, I think, the, the last part of, of what I really wanna talk about here, which is the idea that this isn't the inevitable way that all this has to go, right? And, and I actually, I, I really struggle as someone covering this stuff ab-about it. Like, whenever I try to step outside of that box of, you know, the, the top-down, this is the implementation, this is how it's gonna go, like, I immediately get hit with the open source th- like, yeah, that's great. That's awesome. That's very-

**Anil Dash** [34:49]: [chuckles]

**Charlie Warzel** [34:49]: Like, that's, that, that is maybe how-

**Anil Dash** [34:51]: Theoretically true

**Charlie Warzel** [34:51]: ... this, this stuff should work, right? But like-

**Anil Dash** [34:53]: Yeah

**Charlie Warzel** [34:53]: ... what are, what are you gonna do? And, and yet I just keep being really interested in... Like, let me put it this way. I think that there is a way, unlike, unlike with, like, let's just say, like, social media, right? Like, we b- you know, you, you bought into the, the Zuckerbergian, uh, parad-paradigm of the world, right? And then, you know, y- you sort of realize w-what we've, what we have sacrificed for that very naive version of the connecting, you know, i- is a universal good. But there's something about, like, joining Facebook. It's like the, the, the frog in the boiling pot, right? It seems fine to just join a social network. Like, it doesn't seem like you're doing a, a crazy thing. With the LLMs, I feel like there actually is this possibility for meaningful and sustained backlash, protest. Like, th-there is a, there is a sense of, like, the, these companies could be the dog that caught the car in a way that I don't know pertains exactly the same to the social media revolution, right? Because, like, if people do, like you were just saying, 500,000 tech workers laid off since ChatGPT. If people do feel these effects, if people do feel the, the change, if people do feel like this technology-

**Anil Dash** [36:11]: Mm-hmm

**Charlie Warzel** [36:11]: ... has been foisted on me-

**Anil Dash** [36:13]: Yeah

**Charlie Warzel** [36:13]: ... you know, every, everything is a nail when you have the hammer, and uh-oh, I'm a nail too.

**Anil Dash** [36:19]: Yeah.

**Charlie Warzel** [36:19]: There could be a meaningful backlash. Not to say it's gonna happen, but there could be. And so there could be this sense of, for the first time in a long time, the this is not inevitable movement could have some purchase. What does that-

**Anil Dash** [36:34]: Sure

**Charlie Warzel** [36:34]: ... look like to you? What does that movement look like to you?

**Anil Dash** [36:37]: Th-there's a couple parts. So first of all, the temperature is so much higher, right? The, the anti-inevitability movement is so much stronger, and the backlash is so much stronger You know, 10, 15, 20 years ago, when we would push back against social media's inevitability, people did not give a damn. Now, you know, if you mention you're using an LLM, there will be people, right, that are gonna shout at you, and you're, you know, it's, it's drinking all the water, and it's using all the power and all this, right? And they may not be particularly, you know, specific or cogent or, like, dead on in all their criticisms all the time or, you know, maybe intellectually fair all the time, but directionally they're correct, right? Like, these are tools that are harming people and, uh, certainly run by people that are not responsible all the time. And so, like, you know, it makes sense. So, uh, I, I think that, that the social power behind resisting is so much higher, especially, like, you know, rising authoritarianism supported by the people that run these platforms, there is a pushback. So, like, that's really key.

**Charlie Warzel** [37:44]: You're talking about, too, like, like, just as a g- as a, as an example of this, OpenAI President Greg Brockman made a $25 million donation to the pro-Trump PAC MAGA Inc. So, like, that-

**Anil Dash** [37:53]: Right

**Charlie Warzel** [37:53]: ... just being an example of, of that-

**Anil Dash** [37:55]: Yeah, yeah, yeah

**Charlie Warzel** [37:56]: ... rising authoritarian.

**Anil Dash** [37:56]: That's, that's a really clear articulation. And, um... And so yeah, but, like, there's a, that's a perfect galvanization of, like, people being like, "Okay, I don't want to pay a subscription to that company for" [chuckles] you know, at that moment for that time, right?

**Charlie Warzel** [38:11]: Yeah.

**Anil Dash** [38:11]: Tessa MacCullough-Kottom was talking about, like, you know, people are really feeling, uh, you know, important to resist that inevitability narrative that these companies are pushing around. And the thing I wanna do is sort of complicate it because I think the, the challenge, the thing I say about this sort of tech worker's view of these as normal technology is that a lot of the people who are resisting feel like therefore you say no LLMs. And I don't think that will succeed, nor do I necessarily think it even should, and that's informed by our failures in the social media era. Because when we said, like, Facebook is the wrong approach, is bad in a lot of reasons, for a lot of reasons, people took that to mean no social media, or when we said Twitter had its shortcomings, people said, "No social media." And that didn't work. If I say there are AI platforms that are enabling harms like that towards children, rather than the way to resist the inevitability of those platforms being, "Don't use any LLMs ever," say, "Okay, what would it take to have an alternative I feel good about?" Okay, think about what could a good LLM be. I want it to be environmentally responsible. I want it to have been trained on data with consent. I want it to be open source and open weight so that technical experts I trust have evaluated how it runs. I want it to be responsible in its labor practices. I want... I could come up with a list, right? So there are, like, four or five things. And if I can check all those boxes, then I could feel responsible about using it in moderation. And it's only implemented in apps that I choose [chuckles] to have it in, not forced... Like, like the Google thing where it jumps in front of my cursor every time I start trying to type or whatever. Like, that could be useful. And then I would feel like I was engaging with it on my own terms. That doesn't feel like science fiction. That feels possible.

**Charlie Warzel** [40:14]: Just to tie it together with... I really like that vision. That's, uh, that, that is, that is the vision of all of this that sounds desirable to me.

**Anil Dash** [40:27]: Mm-hmm.

**Charlie Warzel** [40:29]: And I look at it up against the new rounds of fundraising from OpenAI, from Anthropic, uh, f- f- of just, just from the Meta and Google and xAI of it all. I look at it, you know, up against the idea of these companies IPO'ing, you know, in the next year or so, raising these huge valuations, and I look at it in, probably most importantly, the implementation from the corporate enterprise managerial level. All of these pressures, all of this, th- this movement, the, the loudness of it, what you are describing is something that is organic, that is quiet-

**Anil Dash** [41:08]: Mm-hmm

**Charlie Warzel** [41:09]: ... that is thoughtful. Uh, we had, uh, the, the resonant computing folks on the podcast like a month or two ago.

**Anil Dash** [41:15]: Mm-hmm. Yeah.

**Charlie Warzel** [41:15]: And, you know, like, like you're-

**Anil Dash** [41:16]: They're wonderful

**Charlie Warzel** [41:16]: ... you're, you're explaining something that is resonant in, in theory.

**Anil Dash** [41:20]: Mm-hmm.

**Charlie Warzel** [41:20]: Uh, just very broadly, like, I mean, do you-

**Anil Dash** [41:24]: How can it happen?

**Charlie Warzel** [41:24]: ... do you actually think that that, that can happen? Like that we can-

**Anil Dash** [41:27]: 100%

**Charlie Warzel** [41:27]: ... that we can build this? 'Cause I get so pessimistic about it.

**Anil Dash** [41:31]: Yeah. I get, I get the pessimism. I understand it, and it's, it's justified. The things I'd say, first of all, those things don't have to fail for this to succeed. Like, I don't think OpenAI goes away. I don't think you have this, like, David and Goliath moment. I think the people who are troubled by these folks, who are the most rabidly against big AI are like, "Oh, you know, there ought to be a law, and we have a regulatory intervention." I'm like, "I got bad news for you. That's not happening in the United States." Um, and so that's part of why I want there to be an alternative, because there's not gonna be what there should be, you know. It's like these tools are hurting children, therefore we should stop them. Unfortunately, that's not gonna be the case. But, like, how many people on TikTok right now are lit up about the impact this has on marginalized communities where the, you know, the, the, uh, power plants are being built, right? Every single one of them wants this alternative to be built. And so, like, I just like that as a movement, and then you come up with your little seal, you know, your, your blue check mark that says, "This is not the world's worst AI, and if you have to use an LLM, use this one." And part of it for me is, like, having been around a long time, it seemed insurmountable, you know, at one point that people would use a web browser that wasn't Microsoft's. [laughs] Okay. So, um, yeah. So I'm not... It's not easy. Uh, it's not likely. But is it possible? 100%.

**Charlie Warzel** [43:02]: I think that's a, a good and honestly hopeful place to leave the conversation. So, uh, Anil, thank you so much for coming on Galaxy Brain and, and, and trying to, talking through the hype, man. We [laughs] there's a lot of it.

**Anil Dash** [43:16]: [laughs] Despite it all, I remain hopeful. Thanks so much for having me. [upbeat music]

**Charlie Warzel** [43:23]: That's it for us here. Thank you again to my guest, Anil Dash. If you liked what you saw here, new episodes of Galaxy Brain drop every Friday. You can subscribe at The Atlantic's YouTube channel or on Apple, Spotify, or wherever you get your podcasts. And if you wanna support this work and the work of my fellow journalists at The Atlantic, you can do that by subscribing to the publication at theatlantic.com/listener. That's theatlantic.com/listener. Thanks so much, and I'll see you on the internet. [upbeat music]

