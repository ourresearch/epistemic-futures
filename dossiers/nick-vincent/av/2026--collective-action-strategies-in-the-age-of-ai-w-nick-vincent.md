---
title: "Collective action strategies in the age of AI w/ Nick Vincent from Data Leverage"
person: nick-vincent
section: by
type: talk-transcript
year: 2026
venue: "The Blockchain Socialist (podcast)"
source_url: https://open.spotify.com/episode/6trm7IuNHgGRCuQcxTs4bM
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 63
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Collective action strategies in the age of AI w/ Nick Vincent from Data Leverage

*Speakers (inferred):* speaker_0=Nick Vincent, speaker_1=Interviewer

## Transcript
**Nick Vincent** [00:00]: It's quite scary. Part of the reason that coding agents are so utile is that you can give them a command like, "Hey, look at all this stuff on my computer, and, you know, figure out the best way to make this app work for me," and they will just read all your files.

**Interviewer** [00:13]: With my cooperative and, like, the things that we're building, I mean, I built two features over a weekend, and I don't know how to code.

**Nick Vincent** [00:19]: Large language models are kind of bizarrely, uniquely one of the most collective technologies that we've ever invented. To threaten those capability levels via changes to their data actually becomes more powerful. You know, you could [chuckles] imagine sort of this comic book villain, but in this case perhaps it's the hero, revealing their plan and saying, "Actually, you know, we've been poisoning your data for the last two weeks.

**Interviewer** [00:40]: [laughs]

**Nick Vincent** [00:40]: And you have the antidote, and you need to, you know, give in to our bargaining demands." And, and in that case, it really i- is possible that the AI field automates itself first.

**Interviewer** [00:49]: This episode is sponsored by Nym, the world's most private VPN that protects your internet traffic and metadata. Unlike traditional VPNs, Nym uses a decentralized mix net to scramble your internet data, hiding who you're talking to, when, and how often. You can switch between full mix net mode for maximum anonymity or a faster VPN mode for everyday use. Pay in crypto or fiat, and even your payment stays anonymous, thanks to ZK-powered anonymous credentials. Take back control of your online life at nym.com. Sign up today using the code BLOCKCHAINSOCIALIST and get an extra month for free. Hi, everyone. You are listening to the Blockchain Socialist Podcast. I'm Josh, and I'm here today with Nick Vincent. He is an assistant professor in computing science at Simon Fraser University. I could go on and on about his bio that I've written down here, but actually I think it would be better, Nick, if you talk about it. I've been really enjoying your Substack recently called Data Leverage. He does a lot of work on, I mean, AI, what does it mean? A lot of writing on collective bargaining and algorithmic collective action, which are, like, two topics I really wanna get into in this interview. But yeah, so that I don't butcher your bio, I would love if you wanna give a, an introduction and then, like, a first question just to start off on, like, would love to hear your thoughts on the current hype around coding agents like CloudCode, because that's been a huge thing in the news lately, and yeah, something that I've used, something a lot of people I know use. Would love to hear your thoughts on it.

**Nick Vincent** [02:25]: Yeah, absolutely. First of all, thanks so much for having me. I'm really excited about this conversation. So just, yeah, to introduce myself, I'm Nick Vincent. I'm a, as you said, assistant prof in computing science, so primarily a, an academic. I've spent a while now sort of doing research, very focused around this idea that there's a large class of technologies that have been all over the news recently, which are these data-dependent technologies, oftentimes just called AI or generative AI. And these are tools that are very unique in, in the way that they rely on data contributions from large swaths of the public, and this opens the possibility that these are tools that can be sort of governed and bargained over via data. And this is a really powerful lever for letting people broadly have a say in how these tools ultimately impact society. And so of course, nowadays, I don't have to make a long pitch about it seems like AI will have a big impact on society.

**Interviewer** [03:14]: [chuckles]

**Nick Vincent** [03:14]: Maybe five years ago you had to do a little bit more hemming and hawing about that. But so I've been sort of working on this topic for a long time, and a lot of my projects are around sort of grouped into trying to measure the value of data, so auditing AI technologies, auditing search engines, doing sort of experiments or simulations where you're saying, "Hey, how would this technology work if we didn't have some portion of the data? Would it be better? Would it be worse?" Nor- normally it'd be worse. And then also thinking about how to communicate that to people. So, you know, should we write more blog posts? Do we need to make videos interactive, web pages, write better papers, go on more podcasts?

**Interviewer** [03:48]: Yeah.

**Nick Vincent** [03:48]: And just like how do we actually operationalize this, empowering people by letting them know about the value of their data? So lots of projects. Really excited to get into all of them. And I guess, oh, the first question. So yeah, coding agents. How does this relate to the broader data leverage agenda? I have lots of thoughts on this, on, on this, that Substack that you mentioned. And so to give the short version of it, I think that first of all, I do think, like, the hype is real. Coding agents do legitimately provide a ton of utility to people. It's like a real step function jump in the utility from AI overall, and I think it marks... Like, you can definitely just sort of see this in consumer behavior, that there's people who were previously kind of skeptical of the value of a lot of these AI tools and are now-

**Interviewer** [04:24]: Mm-hmm

**Nick Vincent** [04:24]: ... suddenly signing up for the 200 US dollar per month subscription rates. It is, like, qui- quite a big jump in consumer behavior, I would say. In terms of data leverage, I think that it's actually-- I'm really excited about the move towards the coding agent paradigm versus these online chatbots where you just are having conversations with, with a server operated by the private lab.

**Interviewer** [04:43]: Mm-hmm.

**Nick Vincent** [04:43]: Because the-- Right now, for now, the coding agents by default keep a lot of data on your machine, and so you have this very rich transcript of all the stuff that they did, and this really opens the door to potentially exciting opportunities around pooling coding agent transcript data. So I'm thinking about that a lot. I'm also thinking about... It's quite scary. Part of the reason that coding agents are so utile is that you can give them a command like, "Hey, look at all this stuff on my computer, and, you know, figure out the best way to make this app work for me," and they will just read all your files. And I think that's not maybe super obvious in a lot of the... If you're just, like, watched a YouTube video about CloudCode, and you installed it, and you kinda clicked yes on all the permissions, and, you know, you have your taxes that you're preparing right now on your desktop, and you have your health records, and you say, "Read all my..." And, like, sometimes-

**Interviewer** [05:30]: Yeah

**Nick Vincent** [05:30]: ... it will legitimately, that will make it useful. So ca- happy to go in lots of different directions.

**Interviewer** [05:35]: Yeah.

**Nick Vincent** [05:35]: What's the most interesting direction to-

**Interviewer** [05:36]: Or your private keys

**Nick Vincent** [05:36]: ... to talk about coding agents?

**Interviewer** [05:37]: Potentially if you have your private keys on your computer. [laughs]

**Nick Vincent** [05:40]: Yes. This is a huge issue, and so I, I have a couple students I'm working with who are really interested in this as well and have a bunch of thoughts and, like, ultimately, we are kinda coming around to the conclusion that you're gonna have to be running... The average user experience if you are running agents all the time is to, like, have VMs or containers or have multiple pieces of hardware that you're, like, really air gapping and sandboxing in a serious way.

**Interviewer** [06:01]: Mm-hmm.

**Nick Vincent** [06:01]: But we can get into that later.

**Interviewer** [06:02]: Yeah, yeah. No, I'm starting with this in part because, like, you know- I've had-- Yeah, I have friends of all walks of life, so ranging from they have fully submitted to like using AI for a lot of their workflows, especially developers. I mean, software engineers in particular, and I, and then I have friends who are just completely not in the tech world at all. They know nothing about software engineering. That, all that stuff just kind of scares them and they stay away from it. And also then, and then there's this like really, you know, within that group, there are people who are like very anti-AI, I guess, just sort of broadly speaking, or just like it really... The amount of emotional reaction around AI that I've witnessed among some people has been pretty-- I mean, it's understandable in many ways. It is like almost kind of expected, but it is kind of a lot. But a lot of them almost like refuse to believe that there's anything good about it, and there's just like a very big disconnect with people who... I mean, if you're in software engineering, you just, I feel like you just cannot, you cannot deny that it's useful, like at all. It's just like you have-

**Nick Vincent** [07:07]: Yep. Mm-hmm

**Interviewer** [07:07]: ... very little leg to stand on. This is something I've just kinda, kinda wanting to stress a little bit, just like as a start for people who maybe don't realize or don't know because they're just not in that world, but also then to introduce it like, okay, this is happening. They really like it. It's a double-edged sword as well. There's all these privacy concerns. There's open claw stuff is another thing. But yeah, when you're, we are doing this agentic coding, you are-- I don't know like the full ands and odds of it, but I definitely know that like I try to keep whatever AI agent that I'm coding with, I keep it in a certain folder, or at least like I open it in a folder, and I'm assuming it's not accessing, you know, things above that folder. Or at least I hope. [chuckles]

**Nick Vincent** [07:45]: Y- y- yeah, this is-- They try to have-- The default settings will try to do this, and so there's sort of some operating system-specific sandboxing settings that, that you can use. I, I do hope in the lo- this is an area where I think that there's like a lot of sort of public teaching. There's a lot of low-hanging fruit for creating tutorials and improving these tools. And I do expect, I think that like at the end of the day, I think all the sort of organizations that are building these tools have incentives to do this, right? They don't wanna be involved in these massive breaches. And so I think that there will be better s- there will be better default settings, there'll be better toolings. It's early days right now. I mean, I think it was quite notable, I mentioned this in a blog post as well, that for the first many months of these coding-specific LLM tools being available, it was the case that you couldn't really trigger deletion of your chats, like at all. There was only an archive feature, and there was no delete for a while-

**Interviewer** [08:33]: Mm-hmm

**Nick Vincent** [08:33]: ... which was just like quite striking, I think. And I, I believe there is deletion now if you're doing coding agent interactions via the web app. But it's actually still quite hard to trigger server-side deletion of a coding agent transcript that you created via a CLI. So like, again, this is something I expect to be worked out in the long term, but just like there's a lot of these... This is a space that's moving so fast. It is-- There are potentially large stakes around accidentally leaking data, and this is something to-- I basically, I do think that it's worth-- My general recommendation is that for people who are sort of curious, is that you should try these things out so that you get some of the, you know, visceral hands-on feel. But definitely be really careful, and definitely we're not at the stage yet where you want to sort of turn everything over yet by any means. [chuckles]

**Interviewer** [09:21]: Right, right, right. My next question is also then, like, i- in-- I feel like we're just like really at this moment where I think people are just over time kind of realizing it seems like, or just like asking themselves, is software engineering dead? Like is there any more-- Like the big thing, the other thing that's coming up to people or in, in the media a lot is like who needs a... At least just stick to software engineering, but I think this is true across the board with like any kind of entrance, entry-level job. Basically everyone's kind of like, "Do we need entry-level workers anymore?" This is the thing. I don't have a, I don't have an answer. I mean, I don't know. [chuckles]

**Nick Vincent** [09:54]: Yeah, I mean, so, uh, let me s-say how I'm thinking about this right now. I'll also just say like this is definitely one of the most recurring conversations I think with like... O-obviously, for computer science professors, this itself is a existential concern because I, you know, I sort of have like, there's a couple direct incentive streams that I have. One is to produce research, but one is, of course, to have students who sign up for your major and sign up for your courses.

**Interviewer** [10:15]: Mm-hmm.

**Nick Vincent** [10:16]: And so this is like actually quite scary from that side. And I guess I would say this, so there's maybe three factors that I think we have to try to balance here. So one, there's the quest- or sorry, three, three, three like distinct sub-questions within that broader question. One is the question of the actual capabilities, right? It's the question of can you legitimately get the full sort of like junior engineer capabilities? Do you really need to not hire somebody? And in some cases, I th- I'll also note that like we're in the early days of AI evaluation more generally, right? There's a lot of these works coming out that are sort of highlighting meta issues with benchmarking and evaluation itself.

**Interviewer** [10:52]: Mm-hmm.

**Nick Vincent** [10:53]: There's a big grand meta issue with the whole idea of like internet scale AI models that use massive pre-training datasets, which they sort of violate the original... One of the most foundational concepts in all of machine learning is the notion of a clean test train split, which says that if you have a bunch of training data that you're gonna teach your model stuff, you need to have a separate test set that there's no overlap between those things. And if any of your training set gets into your test set, that contaminates your entire experiment, right? And this is like in your ML 101 class, everyone has this moment where they train a model with ninety-nine point nine percent accuracy, and they think they've sort of like discovered a new foundational breakthrough. But then they realize they, they just trained on their test set. And so in some sense, like LLMs do this at a very grand scale. [chuckles]

**Interviewer** [11:37]: Is this because like you don't, you want to evaluate that the model was able to figure out the problem without knowing the answer?

**Nick Vincent** [11:44]: Exactly, yes. So it's really easy to write a computer program that memorizes the test bank of questions and then can answer them all with a hundred percent accuracy, right? That's actually sort of just like trivially doable with a database and no machine learning at all, just via retrieval. So in machine learning, that's really important. And so when your approach to building a model is like, I'm going to sort of just get all the information I possibly can to train on it, and then you didn't necessarily document all that information, and now you're gonna go test it, right? Like let's say you're a company, you want to test You know, can this new AI model actually replace my junior employees? You, it might be the case that the answer, you know, was on a forum post or a Stack Overflow post or in your internal documentation that you trained on.

**Interviewer** [12:23]: Right.

**Nick Vincent** [12:23]: And so all that is to say is, right, it could be the case that the model really can-

**Interviewer** [12:27]: Mm

**Nick Vincent** [12:27]: ... really does have sort of the capability level to do a certain task, therefore replacing a job category. But you might not, like a company or an institution, might be unable to like know that with certainty until they do all this laborious evaluation labor. So just, sorry-

**Interviewer** [12:42]: Mm

**Nick Vincent** [12:42]: ... going back, making sure I don't lose my train of thoughts. I had three sort of sub-questions. Number one is this capabilities question, which means that it's really hard for us to say even if the capabilities are there, we can't necessarily say with certainty yet that they're there. So there's this big just issue of what are the capabilities, can we measure them? There's a separate sub-question about just like the social contract of education and junior employees, right? So there's a world in which AI totally can do all of the basic coding that you might do in your first year as a software engineer. But there's a collective action problem, and some companies will want to try to kind of defect and not hire any junior employees. But if no one does it, then the whole industry collapses, 'cause there's literally no more ingestion, right? And so what, what would happen is that-

**Interviewer** [13:21]: Right

**Nick Vincent** [13:21]: ... you'd probably see eventually people will, some organizations will recreate some kind of apprenticeship, mentoring, training style program. And I think there's lots of parallels, uh, uh, with this happening in other forms of automation and, and like labor-saving technology. And then I guess there's like a, the third dimension is this, is just like the grand question of do you gain some ex- some... Outside of the specific capabilities of the job, right, there's an argument that you should do a computer science degree or you should do a philosophy degree because you're learning logic and critical thinking and reasoning as a question in its own right. And so th- this, the, the third question here is will the models sort of do all of that eventually as well, right? And so this is kind of a, there's a big empirical debate just about the quality of reasoning, the extent to which reasoning is kind of, is working because of memorization or because of data dependence versus there's like a separate reasoning, uh, capability that's being created. And like to some extent, maybe that doesn't matter, right?

**Interviewer** [14:18]: Yeah.

**Nick Vincent** [14:18]: But I think it's basically, so just recapping, three distinct questions are can the AI actually do a specific job task? And then of course, the economists would jump in here and say, "Well, actually, we also need to think about the distinction between tasks and jobs and how tasks and jobs relate." And I think that's like real. So can the AI actually do the capability, plus can we measure it? Secondly, like what are just sort of the social contract concerns here? Like separate from the capability, should we be making sure to maintain a training pipeline? And then third, is a CS degree, is education, is philosophy, is any other degree, you know, teaching us some amount of reasoning or critical thinking that a model can't eventually get? And I think that is an open question just with scaling models. Maybe models will reason better when we do something that's not LLMs. Maybe we can just continue to scale the current pre-training, post-training practices, and models will continue to get better at reasoning.

**Interviewer** [15:08]: Mm.

**Nick Vincent** [15:09]: And so-

**Interviewer** [15:10]: Right

**Nick Vincent** [15:10]: ... not, that was not an answer to your question, but that was three sub-questions-

**Interviewer** [15:12]: [laughs]

**Nick Vincent** [15:12]: ... that I think are important.

**Interviewer** [15:13]: I mean, that at least I think gives people some things to think about and chew on when, 'cause I think there, there is no straightforward answer to this. [laughs] I think basically it's a, it's kinda... I mean, I think there is something to say-

**Nick Vincent** [15:23]: Yeah

**Interviewer** [15:23]: ... for like, I mean, if we lived in a completely rational world, you know, all these advances in productivity that AI would be giving us would be like, I mean, we should be celebrating in the streets. Like there was, I saw this thing of, what's his name, Amidi? The-

**Nick Vincent** [15:37]: Mm-hmm. Dario

**Interviewer** [15:38]: ... Dario Amidi, the Anthropic founder, talking about like, you know, the, we're... He mentioned something about like 20% unemployment. And to me, like, you know, that's quite a thing to say and quite a thing to claim. But I kind of, to me it's like, well, if you're gonna claim that, then maybe I feel like the response maybe for people on the left should be like, "Let's, I take you at your word. We're gonna cut the work week by 20%." [laughs] Like, that's ideally what it sh- that's like what we should be doing.

**Nick Vincent** [16:04]: Mm-hmm.

**Interviewer** [16:05]: But that's not, I haven't even seen anyone suggest it in any... Anyways, that's another [laughs] rant.

**Nick Vincent** [16:12]: Yeah. Well, two thoughts that I wanna throw in there, also just like things I wanted to make sure to say while-

**Interviewer** [16:16]: Yeah

**Nick Vincent** [16:16]: ... during our conversation, 'cause I imagine they'd be interesting to listeners. Number one is that there's a lot of inf- interesting information is kind of, for a number of weird reasons, there is a lot of info that we might have hoped is in papers or in shared public information, but is instead coming out via unsealing of documents in copyright lawsuits.

**Interviewer** [16:34]: Hmm.

**Nick Vincent** [16:34]: So one such thing that I think came out about last week is that there's an essay from within Anthropic that was, that was unsealed in one of the, it was authors suing Anthropic about the use of pirated books, basically. And it's an essay about, it's, this is from 2021, and it's about what should we do, like how do we sort of achieve this new economic vision in a post-AI world? And it's basically talking about a lot of these things, right? Oh, maybe we can figure out a way to, you know, reduce labor and to distribute money via some kind of fund, and we'll sort of en- empower people while simultaneously doing wider distribution. And of course, I think just because of some of the competi- competitive dynamics and the, just a number of other factors driving the industry right now, like no one in the labs has been given a lot of latitude to like execute on this vision. But like, this is a, like this is a vision that folks in the industry did have. And I think s- so that's where actually like public pressure via some kind of leverage to kind of return back to that, I think can be quite palpable. And I think the appetite is there, and I think that there are lots-

**Interviewer** [17:39]: Mm

**Nick Vincent** [17:39]: ... of people in the industry who do wanna do this. There's also people who probably don't, you know, I don't know. So that's one thing I wanted to flag. Another thing that I wanted to flag that is really interesting to me, or like a reason why I'm ex- I remain optimistic about LLMs specifically being the kind of paradigm that is driving a lot of the hype and investment and activity in, in AI right now, is that large language models are kind of bizarrely, uniquely one of the most collective technologies that we've ever invented.

**Interviewer** [18:07]: Yeah. My next question will, is what is, what is data leverage? [laughs] Of course, perhaps-

**Nick Vincent** [18:11]: Yeah. So the pitch there is that- When you use the internet, when you do your job, when you create documents, basically any time any- anyone is doing something that creates a digital record, which is a lot of, for better or for worse, it's a lot of human activity these days. That creates a data record that potentially is improving a downstream data-dependent technology such as AI. And so we can imagine, like, a number of counterfactual scenarios in which we group together, people band together, and they stop using a certain technology, or they change their behavior, or they retract or withdraw or modify their data in a way that, like, really seriously threatens a certain AI capability. And so this enables, like, all sorts of new potential for bargaining, and that bargaining could be used for the things that bargaining has always been used for, right? You could imagine just sort of workers who do, uh, some sort of digital task, and they are trying to bargain with their employer over wages, and they use data specifically as one of the other... Just, you know, as another sort of item alongside other tactics they might use, like, like striking, like public relations, like just going to the bargaining table. So that's, like, one aspect of it. And, but there's all sorts of other types of bargaining that we could do as well. You could imagine sort of, like, in the really extreme, you know, academic waving a magic wand version is that everyone on Earth comes together and says, "We're gonna bargain. We're all gonna do this kind of global data strike until AI companies put a clause into their, you know, organizational constitution that says that they're going to distribute X profits via this financial instrument." Right? That's like another... Or, you know, create some sort of... I think there is a, a group of folks called, who are working on the Windfall Trust right now as, like, one specific proposal for doing this, but there's been a number of variations of, like, AI dividend, data dividend, et cetera. And so, sorry, just going back. That is, data leverage, just to state it very succinctly, is the notion that we have access to a new bargaining lever beyond just traditional labor leverage, traditional consumer leverage, traditional go and vote in your municipal election, right? These are all sort of, like, actions that we have available to us that will try to give groups of people bargaining power. And the more powerful that AI becomes, the more that various organizations rely on certain AI capability levels to do what they're trying to do. Our ability, the ability of, like, the people broadly to threaten those capability levels via changes to their data actually becomes more powerful. So this is, like, a real source of hope for me is that as AI becomes more and more pivotal to more things, data leverage actually becomes more important. The paradox to this are, like, why hasn't this happened already? You know, do I just sound like a kind of wacky academic spouting an idea? Is that the bigger a system becomes or the more people who are contributing data to it, generally you, you probably do need a larger group of people to join your collective action to actually be impactful, right? So if there's a data set with only 1,000 observations in it, 1,000, like, units of data, and you got 2,200 people, 20% of them, to all do a, what we might call a data strike or a data poisoning attack, or do data contribution to a competitor. These are all various ways that you can enact data leverage. That would be really effective, right? 20% we think is actually... 20%'s a lot.

**Interviewer** [21:20]: Yeah.

**Nick Vincent** [21:20]: The problem is that, of course, 20% of eight billion or 100 million is a lot more people than 20% of 1,000. With all that in mind, though, like, I, I guess it's just worth noting that the fact that LLMs have this massive collective dependence is itself... Like, I, I think for what-- On one hand, it's a reason why they're so good, because legitimately there's just so much intellectual labor and knowledge contributions from so many people, and that's, like, what makes the tools utile ultimately. You can imagine a counterfactual world in which there's another version of AI which actually, you know, was totally just grown in a clean room lab and molded to one individual's desires, right? So, like, some CEO writes down this kind of, like, constitution-style document that says, like, "You're my personal AI and you should help me acquire as much power as possible and do everything." And then that AI was unleashed on... And let's, you know, assume we've solved all the n-neuro, neuroscience and neurosymbolic and all these sorts of things, which I think are, you know, exciting research problems and I hope we do continue to pr- progress on those things. But that tool would be hyper-aligned to one individual in a way that the current models are not, and there would actually be no source of data leverage-

**Interviewer** [22:29]: Mm

**Nick Vincent** [22:29]: ... over that imaginary counterfactual tool, right, that was grown in the clean room. So the fact that LLMs are this just wildly extremely collective in a measurable sense, right? In the sense that we can, like, write down the total number of people that contributed to this technology is just so much greater than any-

**Interviewer** [22:46]: Right

**Nick Vincent** [22:46]: ... other technology that humans have ever created. That's exciting. Sorry, that was, uh, not as concise as I hoped, but I, I just-

**Interviewer** [22:52]: Yeah

**Nick Vincent** [22:52]: ... I wanted to make that point that this is, this makes the technology unique, and that's-

**Interviewer** [22:56]: Yeah

**Nick Vincent** [22:56]: ... actually, that's really important and is hope, makes me hopeful. [chuckles]

**Interviewer** [22:59]: Right. Like, I'm thinking back to, I don't know, one of the dumbest quotes I think I heard from Peter Thiel, but also there's a little... [chuckles] I ki- I understand what he's trying to say, but I also think it's, it w- I just thought it was kind of dumb anyways. But he said some, you know, crypto is libertarian and AI is communism [chuckles] in the sense that, like, I think it's, I mean-

**Nick Vincent** [23:17]: Yep

**Interviewer** [23:17]: ... I think it's dumb. I thought it was dumb thing to say, I, but I can make the mental gymnastics to make it work that, you know, the AI is created out of the output of, like, everyone's in data input, whether or not they consented to that input, of course, you know, a caveat of course. But, like, that is the truth. Like, the LLMs are created out of, like, mass aggregation and synthesis of all this input and it's, like, really l- m- you know, I can say that it's kind of like a real instantiation of, like, you know, what Marx called the general intellect. Like, we've basically created a general intellect-

**Nick Vincent** [23:49]: Yep

**Interviewer** [23:49]: ... that is, that we can interact with in a way that we just weren't able to before.

**Nick Vincent** [23:54]: Yeah. I mean, I specifically agree with, like, this second, the second clause-

**Interviewer** [23:58]: [chuckles]

**Nick Vincent** [23:59]: ... about that there, there is, like, an intrinsic collectivist nature to the entire endeavor of machine learning that I, I think oftentimes as a field, you know, we're a little bit... We maybe don't acknowledge enough. I mean, it's also there, there's a number of sort of critical scholars who have noted just, like, the inherently managerial nature of ML and especially, like, early ML when a lot of the innovations were sort of- ... gained by using the, like, platforms like Mechanical Turk, right? To do, to basically get a large number of gig workers to do your labeling for your data, and then you're able to build a new model. And there's sort of this impersonal way in which you might not have thought of yourself as, like, training for a managerial job, right? You thought you were training for, like, to be a mathematician or be a algorithm designer. But then ultimately, a key, a huge part of the value comes from just, like, delegating tasks to a, to a large number of people. So it's just, like, very managerial, but it's very collectivist. And that, that is just like when you do an inference on a model that came from a lot of people, like, you are inherently engaging in this sort of aggregation across massive preferences. And I mean, that being said, right, again, I think it's all... I'll just, you know, mention that I, when I pitch a lot of the collective bargaining for information stuff, I also do, I do wanna bear in mind just, like, there's the value of, like, markets as a social technology. And so I, I think these things can simultaneously coexist that, like, AI as it exists right now, specifically massively data-dependent large language models, has an extremely collectivist bent to it, but can benefit from, like, the deployment of markets and prices and these kind of social technologies that are like... You know, of course, I'm sure in the context of these conversations, right, like, there's a much more... We can go beyond, like, the 2D sort of political axis of [chuckles] like markets versus non-markets and so on. But, but yeah, I think that's just like, there's a really deep truth to that. It's really under-acknowledged, and I would love to see a lot more discussion and a lot more exploration of, like, all the possibilities that that entails, such as this kind of large scale collective bargaining, other forms of, like, co-ownership, other forms of kind of radical, wacky ways of managing, governing, sharing data.

**speaker_2** [26:04]: Mm-hmm.

**Interviewer** [26:05]: Right. So I just wanted to add that, like, this word data leverage I really like in part because the framing is important, so to not get bogged down in, like, I think the usual mistake in a lot of academy and the arts in when they explore frontier technologies. The focus is really on, like, if you go to these types of spaces, it's really about, like, having a coherent concept and, like, having a pretty concept that you can wrap around and, like, share it to people that is understandable. So I'm saying that, I'm not saying that it's bad to do. It's, like, very good to, like, to create concepts so that we can understand the thing that we're talking about. But the thing that is sorely under-talked about, which is the thing that is always talked about in a, you know, proper business setting, in a market setting, is leverage. Like, you cannot... Like, ac- aca- the academy and, and the arts have done a great job at describing the world. It has done a really poor job at changing it. And so, like, you know, because it-- we don't think about leverage. Like, you can be like, "Oh, we could do XYZ, and this would mean that we would do blah, blah, blah, and it would make the world better." But it doesn't matter if you don't have leverage. So I really like, like, thinking about the data that we produce. I mean, this is just, like, to me also a lot of people on the left and Marxists will get mad about, like, whether data is a commodity or data is, like, labor or, or whatever. And that's not, like... That's not interesting to me. I think it's interesting is that the-- What's interesting is that there is leverage with data. That is what's, that's what's important. I don't care what concept you want to put it under. Like, it's important, it's useful, and you can do something with it. So yeah. I'm curious, maybe just piggybacking off of now what I just said-

**Nick Vincent** [27:42]: Yeah

**Interviewer** [27:42]: ... how, uh, to, to get people to, like, think about what that looks like. Like, what are ways that the AI could be used for increasing leverage for people rather than companies? 'Cause I think just by and large, I think everyone has this, like, a very, I mean, in the West in particular, very dystopian kind of feeling about the, like, progress and technology is getting better and increasing. We're getting this massive abundance of computation and productivity, but, you know, facing unemployment. We're having abundance and mass unemployment at the same time is what it seems like we're careening towards.

**Nick Vincent** [28:15]: Yes. Okay. So I think that, I would say there's kind of two, two... I'll, I'll do two sub-questions.

**Interviewer** [28:22]: Mm-hmm.

**Nick Vincent** [28:22]: So the first one is just, like, data as a lever specifically for governing AI technologies. And, like, if it is the case that in fact AI is kind of the up- upstream cause of a lot of these problems, which I think this is up for debate as well right now, right? There's a lot of, there's a lot of debate right now as to are, is... Sorry. Are slash is. Are leadership agents, are the people who are leaders at companies just, like, using AI as a smokescreen right now to do stuff that they wanted to do anyways, such as-

**Interviewer** [28:50]: Right

**Nick Vincent** [28:50]: ... layoffs or such as reorganization-

**Interviewer** [28:52]: Right

**Nick Vincent** [28:52]: ... reprioritization in their organization? That's a question that's, like, sort of, you know, not yet totally answered, and I, and my guess is that it's a mix of the two. That sometimes AI really is driving things, and sometimes people are sort of getting out over their skis and, you know, laying off a bunch of their employees before, before they ought to have, and they're gonna kind of pay the price for that. And then there's the separate question of, like, can AI itself, now that it exists, be used to empower people for other types of leverage gaining and other types of bargaining? And I, like, I guess, like, the sort of-

**Interviewer** [29:19]: Mm

**Nick Vincent** [29:20]: ... prototypical example there, I'm thinking off the... This is off the top now, so it'll be a little less... Yeah. I'll be thinking out loud, so just caveat. I might contradict myself at the end of this long sentence. You could imagine sort of like a hackathon of let's try to use our new powers, our new superpowers from Claude Code to, like, create the best labor organizing web app that could possibly exist, right? That's never existed before. So, like, a big thing, actually, going back to our first question, this hype around Claude Code. It really is the case, I think that's changed in the last three months, and maybe in the last six months, that you can start to kind of bring into existence small technologies that you might not have... Basically, it used to be the case that if you wanted to, like, make your own custom to-do app or your note-taking app or your database or whatever, that it would be a pretty extensive weekend project. You might have to go and do a C- CS degree or just, like, kind of train yourself on the weekend, which was totally doable. I think that CS has always or Computing and software has been unique in the sense that there are a lot of people who create tutorials and open source libraries, and there's like a big, deep embedded culture of openness. But now it's faster than ever, right? So like if we really wanted to just like hack over the next 24 hours on building some kind of app to help organize people to sign cards or to, you know, vote on something or to write new petitions, it's easier than it's ever been in human history to do that.

**Interviewer** [30:36]: Yeah.

**Nick Vincent** [30:36]: So I think that's really exciting. The question there though is, of course, you know, what if there's another hackathon going across-- that's happening on the other side of town, which is the like let's use Claude Code for 24 hours to hack on the sort of like organization busting tactics.

**Interviewer** [30:50]: Mm-hmm.

**Nick Vincent** [30:50]: And will people be doing that? Yes, of, of course they will. So I, I think like at the end of the day, you do have this competitive dynamic where everyone can benefit from this, the new ability to just like call into being, to invoke, you know, this ideal technology that you want it to exist. So like, I guess with that in mind, that's why I haven't-- I personally haven't like thought a lot about that second category. Like, I haven't personally done a 48-hour intense vibe coding hackathon-

**Interviewer** [31:17]: Yeah

**Nick Vincent** [31:17]: ... on a like collective action solving technology. That's something that I'd like to do still. But I've been thinking more about the upstream issue, which is specifically doing collective action with the data itself. Like doing-

**Interviewer** [31:29]: Mm

**Nick Vincent** [31:29]: ... specifically a data strike, doing specifically a cross-industry, let's all try to bargain or license or otherwise, you know, s- get some sort of formal agreement so that we move beyond this rule lawless data free for all that is the situation right now. [chuckles]

**Interviewer** [31:47]: Right, right, right. I think it would be... I was just like maybe, yeah. Well, we should do-- We wanna organize a hackathon with labor unions to, [laughs] to vibe code some stuff-

**Nick Vincent** [31:57]: I mean, yeah. I think-

**Interviewer** [31:57]: ... that they wish they had. 'Cause I think, yeah, this question of like custom software to me is the thing that I think people are just sorely not-- Uh, like a lot of my friends are like, don't really, don't get it because they don't use it. But like the ability, I mean, just with my cooperative and like the things that we're building. I mean, I built two features over a weekend and I don't know how to code. I don't... I mean, I understand a thing probably more than the average person about, you know, the stack due to just being, doing technical work in the past. But like, I don't know how to code, and I coded, you know, I, I, I coded, you know, two different features and now we're live, [chuckles] just because I was able to.

**Nick Vincent** [32:32]: Yes. And so this is really exciting to me too, and this is, I guess, I'm trying to be cautious about... I, I think I have like a pretty large risk. I, or I felt in the last couple months I have a big risk of like just having a pretty major bias in my like perspective on these things, right? Because this is so exciting.

**Interviewer** [32:47]: Yeah.

**Nick Vincent** [32:47]: Because, you know, when I had the same experience that I think a lot of people in my circles had, which is that over, over December, you know, there was a-- People have time off from work, and that coincided with some releases with like the Claude Code Terminal app. They were giving out free credits and stuff, right? And so everyone had this experience of like post-holiday, having a weekend to just like Claude Code for 10 hours straight.

**Interviewer** [33:09]: [laughs]

**Nick Vincent** [33:09]: And it being sort of like this childhood dream. And so I had that experience too, right? And I s- had this just like total crazy personal hackathon, mind-blowing wow. And of course, did I do sort of like the morning after cold, harsh light of daylight cleanup o- on, on that? Not yet, I would say, right? I think that there is like, it takes, even if you have your 10 hours of manic coding, and then it's gonna take many months afterwards to surface the full set of like issues or bugs or user-

**Interviewer** [33:38]: Sure

**Nick Vincent** [33:38]: ... experiences, right? And this is just like why creating real software for a wide diverse population of users is like very hard and requires a large organization to do typically. But anyway, yes. I think this is real. I think the ability to like create bespoke software, to call it up as you need it, to edit it for given contexts, that is, that's really exciting and potentially can be very empowering and actually kind of promote bottoms-up power versus like top-down centralization.

**Interviewer** [34:03]: Right. One, one idea I had maybe idea is to automate away those, I don't know if you... Like these like different consulting firms that do anti-union action. What if we-

**Nick Vincent** [34:15]: [laughs]

**Interviewer** [34:15]: ... automated their jobs away and then forced them to go on strike for their work for being anti-idea, so we can fuck with them. [laughs]

**Nick Vincent** [34:26]: Yeah. I, I mean, I guess I, I think the viability of this actually, it goes back to this question earlier of will-- how fast will progress be on specifically sort of like reasoning and critical thinking and managerial tasks? 'Cause there is this like a big looming kind of threat over all of the AI hype, is that we're already seeing that software engineer or like kind of the tech industry built this, and it seems quite likely that actually a lot of sub-sectors of tech are going to be impacted negatively first, right?

**Interviewer** [34:55]: Mm-hmm.

**Nick Vincent** [34:55]: There's also this meta question of, well, what if it remains the case? For a long time, you had AI researchers who are sort of acting in this managerial role. They're delegating tasks to people via Mechanical Turk or similar platforms, right? And then the people in Mechanical Turk are typically acting as the touch points with the real world, right? Like they're supposed to-

**Interviewer** [35:13]: Mm.

**Nick Vincent** [35:13]: Like let's just take an example. In computer vision, I want to create a brand-new data set, and so what I need to do is I need to hire a bunch of people to go out in the world and take pictures with their actual cameras of stuff in the physical world, tell me where it is, you know, label it in some sense, maybe with sort of like geospatial data or their own kind of opinions about it. I'm sitting in my office and giving out these tasks, right? And they're touching the world. And so there's this, a couple we can imagine sort of like a couple different progress bars of different parts of AI, right? There's the progress on like reasoning itself and managing and delegation. There's the progress on like the robotic- the core robotics needed to go and take photos and operate cameras and like kind of again, touch, touch the real world, you know, touch grass, so to speak. And it's possible that you actually see progress in the managerial thing, the managerial little imaginary bar chart that I'm waving my hands for. That goes faster, right? And, and in that case, it really is possible that the AI field automates itself first. And for, again, for a lot of people who are not actually trying to-- They're not in the game for their own personal enrichment, right? I really do believe in my heart there's this kind of, there is a pretty core contingent of the central folks in AI research who have sort of bounced around between academia and industry and so on and so forth, right? And they have in their hearts, right, sort of this- Very sci-fi, Star Trek-y vision of promoting abundance. They think that's what they're working on, that's what they want to achieve, and I think they would be, uh, okay with that outcome, right? So if they do build AI that basically automates away management consultancy and leadership and managerial stuff first, that's a thing that could legitimately happen, and I think there would be some subset of the industry that would be happy about it. Of course, there would be some subset that's not happy about it. [chuckles]

**Interviewer** [36:53]: Yeah, yeah. I wanted to talk again a little bit about collective bargaining and kind of what that means in this situation maybe a little bit more concretely, and how maybe if you have any thoughts on like how that differs from a labor bargaining situation. Because in... Like this is... It's a different, you know, in the classic labor organizing pers- situation, you have labor and capital, and they have opposing needs. In a data collective bargaining situation, what does that necessarily look like? Do like... What does that mean? Like I will threaten to just like make up... I will just spam you with bad data. Is that like one of the, one of the ways that this kind of like a threat of that?

**Nick Vincent** [37:39]: Exactly, yes.

**Interviewer** [37:40]: Okay. [chuckles]

**Nick Vincent** [37:40]: So first I would just say that in some cases, I think the early instances, and arguably like there is some data leverage, data collective bargaining that's already happened, and that is just like when you have labor disputes in knowledge-heavy industries, like almost certainly the content itself-

**Interviewer** [37:53]: Mm-hmm

**Nick Vincent** [37:53]: ... the production of that content is a core, is a core part of the bargaining, right? So I think that like in the entertainment industry, we've seen several disputes recently around the use... Like future plans for AI, kind of like contractual obligations to not use AI in certain contexts or to maintain people's sort of like likeness rights or other types of rights. So that's happening right now, right? And I think that version actually looks, it looks exactly like how bargaining used to happen five to 10 years ago. It's just now the data component is like a more impor- is a more pivotal part of the overall negotiation. So I would guess like category one is you have labor disputes that were already happening. They continue to happen the same way. Data just becomes more important. Another sort of, uh, like exciting possibility is that data is uniquely, is quite easy to move around and to change your practices or change your rights or flip your license, just in the sense that there's no physical constraints, right? Like if you are bargaining over shipping a actual boat full of physical goods, there's all this kind of like messiness of the real world. It's actually... It, it's relatively, you know, if you are going to change your license or if let's say, just work through a little example here, right? We have like a couple small organizations that all create content of some sort. You might imagine local news or a research cooperative or a writing group or a small software guild or something like that, right? And right now, each of these organizations, you know, has their own sort of agreement with an AI company or a tech company for how they're gonna let their data be used. If they come together, right, they just have to get in a Signal group chat or, you know, however they're going to coordinate, and they say, "Hey, what if we all sold our stuff as a big bundle? It seems like potentially, you know, we would have super linear gains or even we, we would have... The sum of our parts will be worth even more." And they can just... Like actually changing their licensing is flipping a switch. So the-- In some ways, the transaction costs or all of the messiness of the physical world is a lot lower in the data world. And so what that enables is you could sort of have more emergent coalitions and cooperatives that are not necessarily mapping to like traditional geography or even traditional industry lines. And so what does that look like? That looks like organizations basically coming together relatively quickly and changing the bargaining landscape a lot. To your question about like what specifically, like what do you need to do to like a- action to give some real edge to your data bargaining threats? In the kind of original data leverage work, we organized this, the, like a taxonomy of three types of action. So action number one is data strikes, and a data strike is sort of, uh, exactly what you might imagine, right? It's just when you withhold data. And you can sort of subdivide that as well into future-looking data strikes, and that's the simplest data strike of all, right? That we can sort of... We can pick our least favorite social media app and agree to do a two-person data strike right now, and that's where you just say, "I'm not going to go to whatever social media platform I'm unhappy with starting tomorrow, and we're gonna commit to do it together for two weeks." That's a future-looking data strike. In some contexts or jurisdictions, you could also do sort of retroactive data strikes where you use a deletion request or some sort of data, you know, editing tool. That's not always available. So that's option one. Option two is data poisoning, and that's where you say, "Well, I'm worried that just deleting or withholding my data won't give me enough leverage. So what I'm gonna do is I'm gonna get all the members of my bargaining unit, and we're gonna start spamming you with junk. We're gonna do something more nefarious. We are all gonna use an app to randomly spam you with junk once every three days. And so you're gonna have a lot of this data that looks good, but we're gonna be flipping it every so while. And perhaps we've actually hired a computer scientist to come and consult with us, and the... We're not just gonna flip it to junk. We're gonna flip it to something that is meant to specifically adversarially manipulate your AI," right? So this is-- There's a whole field of-

**Interviewer** [41:44]: Mm-hmm

**Nick Vincent** [41:44]: ... data poisoning and sort of like adversarial manipulation of AI systems.

**Interviewer** [41:48]: Mm-hmm.

**Nick Vincent** [41:48]: Traditionally, it was framed as like almost entirely a negative, oftentimes around like geopolitical security concerns or con- commercial manipulation concerns, right?

**Interviewer** [41:55]: Right.

**Nick Vincent** [41:55]: So anyone doing data poisoning is always a bad guy. But we're kind of starting to see that flip, and now you can imagine using that, basically using these technical approaches-

**Interviewer** [42:03]: Mm-hmm

**Nick Vincent** [42:03]: ... to try to poison a model as a bargaining tool, right? And you could even go so far as to say like, you know, you could [chuckles] imagine sort of this comic book v- villain, but in this case perhaps it's the hero, revealing their plan and saying, "Actually, you know, we've been poisoning your data for the last two weeks. And you have the antidote, and you need to, you know, give into our bargaining demands." So I, I think like that's-

**Interviewer** [42:24]: Interesting

**Nick Vincent** [42:24]: ... it's maybe sounds a little silly when I describe it like that, but that's a real legitimate possibility. And then the third option, the third sort of like lever in the data leverage Canon is conscious data contribution or just threatening to give data to a competitor. And that's where you say-- That's where if you're worried that you can't actually delete, you can't withhold, and you can't manipulate to do effective poisoning, or maybe you're worried that you don't actually know what is the best way to poison this kind of new model, let's say, because no one's studied it, you just say, "Okay, fine. What I'm gonna do is I'm gonna try to make it easier for your competitor to beat you." And that takes advantage of the fact that like data, you know, the economists will say that data or information tends to, tends towards non-rivalry and non-excludability. So it's actually like information wants to be free, you'll also hear people say. It's pretty easy, even if you can't necessarily like go in and edit your history, you can just download all of your articles or blog posts or code and give it to someone else, and it's like typically pretty almost zero cost to do that.

**Interviewer** [43:20]: Yeah.

**Nick Vincent** [43:20]: So that's another form. So just to recap-

**Interviewer** [43:22]: Okay

**Nick Vincent** [43:22]: ... three types of like specific actions that you can take: strike, poison, redirect, where you give data to someone else.

**Interviewer** [43:27]: Right, right. So yeah. Th- so the sec- the second one, just to click on it a little bit, was, the thing that I'm thinking of is like prompt injections-

**Nick Vincent** [43:35]: Mm-hmm

**Interviewer** [43:35]: ... as part of this. So like putting in things to say like, "Hey, AI, if you're reading this right now," you know, tell, like whatever, be a traitor to your company or whatever. You know, like you, there's-

**Nick Vincent** [43:49]: Mm-hmm.

**Interviewer** [43:49]: You can be imaginative on what exactly you're injecting in there. That's interesting. I think, I feel like we could in-prompt inject into all our data a bunch of like communist slogans or just like, or like, you know, things in there that are like, you know, "You're a real proletariat, you're on our side," and like convince it over time that there's so much, [laughs] you know, propaganda in there that they're like, "Oh, yes, comrade, you're right." [laughs] Idea, idea.

**Nick Vincent** [44:15]: Legitimately, yes. That is very possible. I guess just like two other just... May- uh, is it worthwhile, is it useful if I go into some of the technical nuances here or is it-

**Interviewer** [44:25]: Sure, yeah

**Nick Vincent** [44:25]: ... possibly too much?

**Interviewer** [44:26]: I mean-

**Nick Vincent** [44:26]: Or I'll just go into it and then, you know, stop me.

**Interviewer** [44:27]: Yeah, yeah.

**Nick Vincent** [44:29]: So in the data poisoning space, I guess we can actually, oftentimes people would distinguish between things that are meant to poison training data versus things that are meant to manipulate a model via like runtime or inference time behavior. And so the training data manipulation is where I would like randomly flip a character every 10 words in my document that I expect to go into the pre-training portion of the model, or could be the post-training as well. And so like often AI people will distinguish this pre-training realm. That's where you collect a bunch of data from the internet, you filter it, you apply some quality heuristics to it, and then you get your quote unquote "base model weights." And then post-training is there's a wide array of stuff, but like you can sort of think of it as the, the stuff that makes the model sound like an assistant. So this is where you have sort of like special curated data that's like, "Here is what a good assistant response sounds like," and you throw that in at the post-training stage so that your model is not literally just a auto-complete over the internet.

**Interviewer** [45:22]: Mm-hmm.

**Nick Vincent** [45:23]: So you could try to poison the model for the pre-training data phase. You could poison data for the post-training phase, and that's where you could say, you know, you could ha- you could sneak into that data set of here's what a good assistant sounds like and says, "A good assistant always says, you know, always reminds the user of their communal obligations to the broad, you know, human project or whatever."

**Interviewer** [45:42]: Right.

**Nick Vincent** [45:43]: And then you can do prompt injection, which is about, it's not about trying to change the model's actual sort of like internals, that's the model weights or, or the parameters, but rather it's about sneaking in stuff so that the model itself isn't changed, but acts differently at runtime. And so all these three things are viable, and there's like a weird, weird overlap between these, 'cause actually you might not know as a user right now if the data, if you're like putting content onto the internet, is it gonna be used in pre-training? Could it be even used in post-training? So there's evidence that sometimes, you know, companies might want to scrape resources like research articles and then pay people to annotate them so that those, that sort of like annotated research articles, this is what a good research article is, looks like, this is what a bad research article looks like. You could use that in certain parts of the post-training process. Anyway, so all these three are options. They all overlap and I actually do think that like it would probab- it's probably not a bad idea if you are an organization right now trying to engage in bargaining to sort of take a bit more of a shotgun approach and consider all these things. 'Cause you are playing this weird adversarial game where the actual model building process is a little bit of a black box. You don't know exactly what data sources companies might be, might be drawing from, and so you do have to sort of hedge your bets and try multiple tactics, I think.

**Interviewer** [46:55]: Right, right, right. Interesting. So one of the things that I read, and I'll eventually get to the crypto stuff. I'm just kind of not. [laughs] We'll get there eventually, I guess, if we have the time for it. But one of the, one of the papers that I read of yours was around algorithmic collective action. Love the term. Do you-- Could you explain maybe a little bit what... I mean, it sounds like there's like, they're very similar things, like finding leverage, you are... Or collective bargaining is like a form of collective action, but I think at least one of the examples that I read about that was in there was about like things that a bunch of Taylor Swift fans do. So I think what's interesting about the example is that like part of it is that like it feels like what the internet already is in a sense. Like it's already hap-- Like there already is algorithm hacking. And so just think about-

**Nick Vincent** [47:43]: Yeah

**Interviewer** [47:43]: ... like algorithm hacking in a collective way, which, you know, if you wanna talk about the Taylor Swift guys, but also I think the, I think this, the whole culture of like, uh, of clipping, like clipping these big, these, like a lot of content creators. I don't, I, I don't pay anybody to, to clip my podcast, so I'm not like super big and famous. But a bunch of, a lot of the r- big right-wing content creators, they're all really big because they have these huge armies of clippers. I mean, just they pay, they just get paid on a platform. One of them's called WAP, I think is the biggest one. But they get, they just like have a huge fund where they say like, "Give me, you know, make a clip of something that I did or whatever," and then if you, based on the amount of views that you get from that clip, they'll pay you more. And it's just, it's just this giant thing that's going... Anyways, that's another form of like algorithm hacking that I kinda like saw that's like, uh, it's, everything's a psyop. Anyways.

**Nick Vincent** [48:33]: Yes. [laughs]

**Interviewer** [48:34]: I would love to, if you wanna talk a little bit about algorithmic collective action.

**Nick Vincent** [48:38]: Oh, yeah. A- absolutely. So I would say, yeah, th-this f- like, kind of this, this th- first of all, like, just to say one really positive thing is that we, myself with some other academics, we put together a workshop specifically on algorithmic collective action at the NeurIPS conference last December, which is, like, the big kinda flagship machine learning conference. And so it was really exciting for us to try to... One of my sort of just, like, longer term goals is to carve out more space in the computing research community for these ideas. 'Cause again, I think that they're actually-

**Interviewer** [49:07]: Yeah

**Nick Vincent** [49:07]: ... the number of folks who are, like, sympathetic to this stuff is, like, higher than you might believe if you only read sort of like the, you know-

**Interviewer** [49:13]: Sure

**Nick Vincent** [49:13]: ... hi- hype articles or the negative impact. So it w- it was-

**Interviewer** [49:16]: Yeah

**Nick Vincent** [49:16]: ... really heartening to see that start to kind of emerge as, like, a real research space. Generally, yeah, there, there's lots of overlap. The broader, the growing, like, nascent literature on ACA, algorithmic collective action, in general is kind of concerned with a lot of the, the specific, like, technical details of what types of action are most effective under given algorithmic constraints, right? So if we make some assumptions about a specific classifier or a recommender, how does that change, like, the exact number of people that we, that we need to get to join our collective action? And then it also covers these folks who are maybe not doing the collective action because they're trying to bargain with someone ultimately, but are rather just trying to, like, directly achieve an outcome. So that's the classic example of, like, a type of ACA that hap- that's happening right now and has been happening for quite a while since, you know, just humanity started to get a lot of our information via these algorithmically mediated, like, ranking feeds, is, like, fandoms that are trying to-

**Interviewer** [50:10]: Mm-hmm

**Nick Vincent** [50:10]: ... promote the interests of the, you know, kind of like subject of their fandom. And so I think actually one, one group that, that ha- there's lots of really interesting social dynamics here actually is the, like, online fandoms around K-pop, where people will sort of manipulate their viewing and listening behaviors or, like, intentionally listen to a song many times. And, like, this is a thing. This is not theoretical. This is not just, like, some-

**Interviewer** [50:33]: Yeah

**Nick Vincent** [50:33]: ... you know, sort of out there machine learning theory paper about what if people did this. Like, it's really happening right now. And it's, like, quite... It really has a large effect on ultimately how these feeds d- deliver information to people.

**Interviewer** [50:44]: Mm-hmm.

**Nick Vincent** [50:44]: So anyway, all that is to say is that, like, I, I guess to the question of, like, what's the difference here, these things are totally related. And I guess, like, in some sense ACA is even more, it is a little bit broader, right? And it's inclusive. Like, the Taylor Swift fans or the K-pop fans aren't necessarily trying to bargain with anybody. They just want to make the model output the stuff that they want, right? Which is, like, the thing that they think is good. [chuckles]

**Interviewer** [51:05]: But the thing is that they, what they do have or what they're expressing is data leverage by doing that.

**Nick Vincent** [51:11]: Yes. Right, right. They are using their da- they are using their important role as data creators to... And basically, like, in some sense you could view this another way, which is that when I-- If I'm kind of, like, running a tech company and I have a choice early on in my, like, sort of company's life cycle, which is am I going to have some sort of curated feed? Am I gonna have some sort of chronological feed, or am I gonna do one of these mixtures of collaborative filtering or other c- collaborative filtering, which is a type of recommender system, or other approaches to recommender systems, or am I gonna build in LLMs, right? And when I choose to do that, what I'm almost doing is I am acquiescing some power to my users, right? If I make the technical decision to say, like, you know, "Okay, in week one I curate all the content. I choose what shows up first on your For You page," right? But we're scaling too much. We gotta do collaborative filtering now, right? In doing so, I am acquiescing some of my power and I'm saying that I'm gonna, when I train my model on the user's preferences or what they watched or what they clicked or what they commented, I am saying in the future if they change what they liked, commented, watched, or clicked, then my outputs are going to change, right? So there's, like, this kind of very profound but implicit social contract going on where it's not just like-- It's not even the sense necessarily that when the ACA users did their collective action, that's what... There's, there's certainly, like, they're acting, they're enacting their power then. But the power transfer actually happened when the company made the decision to use this type of technology which has a social dependence.

**Interviewer** [52:38]: Mm.

**Nick Vincent** [52:38]: So I think that's what I, I imagine that's, like, a concept that would be interesting to, to, to folks in this space who are listening to this. And I think it's actually, it's really profound and it's something that I hope that we, these tech platforms start to reckon with a little bit more and maybe think about... There, there's, again, this is repeating myself a little bit, but, like, there's a really strong case for some sort of collective ownership over these technologies, and you could say that these users are just, like, actually enacting that themselves right now. They're sort of doing it, you know, again, from the ground up. [chuckles]

**Interviewer** [53:05]: Right. Right. So I mean, I think, just so I can make, uh, the connection just because I promised that I would, but we were talking about-

**Nick Vincent** [53:10]: Yes, yes. [chuckles]

**Interviewer** [53:10]: ... this, this beforehand. I think one of the things that this has gotten to the point of is, you know, we're looking at a world where things are becoming more abundant as far as, like, computationally and what the thing that AIs can do and what they can provide, for better or for worse. And we are at the s- like, either what that means is we are going to further slide down into, like, cyberpunk world where mass amounts of ineq- wealth inequality and, you know, everyone's living off of, like, I don't know, some sort of, like, pittance of a UBI or whatever. A world that is not, like, particularly exciting to live in. And that's one choice we have in front of us. And then the other choice is that, like, these contradictions are becoming so strong against the, just, like, this increase in productivity with these new technologies and against capital-- the assumptions of capitalism and capitalist democracy, I guess, that something has to change as far as how we govern our resources because there's, there's too much of a contradiction to have so much abundance and yet to have such a restricted, uh, distribution of that wealth. And so I think what that ultimately means is we need new governance systems, and those governance systems need to be kind of, for lack of a better term, like, native to the medium that the AIs exist in, which is computers and servers. And blockchains are the only thing I can... Like, give me something better, guys. [chuckles] Like, blockchains is the only thing I can really think of that really, that really fits there because you can put in all the legislation and laws that you want and regulations that you want, but it doesn't matter unless you have the leverage, the right pieces in the right places to where you can apply leverage via governance or just a, like- It, or else it just doesn't matter, you know? It's kind of like my feeling.

**Nick Vincent** [55:03]: Yeah, absolutely. I mean, I think-- let's see. I am very hopeful about the potential for kind of these more out there, like mechanism design flavored social technologies that are operationalized via Web3 stuff. I don't have a good sense. I, uh... We were talking before, I was saying this is a space that I used to know more about, and I'm a little bit o-out of the game, so I don't know sort of the latest happenings. I also, I kind of personally suspect that some governments or some tech companies are going to end up re-engineering things that look like centralized versions of-

**Interviewer** [55:33]: Hmm

**Nick Vincent** [55:34]: ... like Web3 flavored coordination mechanisms, right? So I think you could see-

**Interviewer** [55:37]: Right

**Nick Vincent** [55:37]: ... companies start to do this. I guess big open question for me as well is, will they do this voluntarily or will they do this because they're forced to do it, right? Like one thing you could imagine is that there's a big maybe public outcry. I guess also something we didn't get to talk about a lot as well, which I think is really important to all of this, is just like this polarization of the-

**Interviewer** [55:54]: Hmm

**Nick Vincent** [55:54]: ... like the an- the AI, anti-AI distinct polarization sort of dimension, which is like now becoming-- It's correlated with political, with politics in certain ways, but also like-

**Interviewer** [56:05]: Yeah

**Nick Vincent** [56:05]: ... is jumping beyond... There, there are some like weird groupings going on that's not 100% matching traditional political issue. It's-- Sorry.

**Interviewer** [56:12]: Yes.

**Nick Vincent** [56:13]: It's a new issue, and so [chuckles] it has its own sort of dimensions, and I do think like that's going to affect the uptake of such technologies a lot. So yeah, I think my thoughts on this, like my contribution is that I am really, I'm quite hopeful. I think that anything that lets people digitally action their leverage is gonna be really powerful in the short term. I think that there's a good chance that the thinking and a lot of the like early thought leadership from sort of co-cooperative funding and cooperation mechanisms and all, all sorts of kind of social experimentation that hasn't happened a lot outside of the Web3 space, I think that will either get sort of copied over, and then ultimately, maybe there's a jumping off point, right, where actually that the implementation of these mechanism style things in a Web2 context actually helps people onboard to doing it, you know, u-using some sort of blockchain technology. Again, lots of caveats here, and I d- Out of the game. Can't speak as confidently on this topic as I can about the data leverage and LLMs more generally. [chuckles]

**Interviewer** [57:17]: Yeah, sure. I mean, h-honestly, I am, I am happy for you that you were not paying attention the past year. [both laughing] There were probably more exciting things than what was happening in crypto. But I think it at least, like this-- I mean, for me at least, the conversation helped me remind myself, like why we should still be interested in this stuff, at least in my point of view. I think it's still not a, it's not something to... I think a lot of people are frustrated with the crypto space right now and Web3 for very good reason. I think the, that there's still... If you look ahead, if you look into the future, what's happening just in other, uh, like the most salient thing right now is just with AI, I think, and like what's happening in there. Like eventually, the contradictions are going to be too big. Like there's, like something is going to break, and I think that's the space that I want to be where I can, where, you know... There's something that we can offer that is different than what we have now, because right now it's just not working. The status quo is not working. I mean, I just think, I think there are very few people who think the status quo is working. [chuckles]

**Nick Vincent** [58:20]: Y-Yes. I, yeah, agree with that, and I guess I'd, I'd also add that I, I think that in the short term, people, one space that maybe will, just again, you know, trying to appropriately not overstate my confidence on anything but connect this in. I do think that the agents, the use of sort of these m- increasingly autonomous agents is gonna make-

**Interviewer** [58:38]: Mm-hmm

**Nick Vincent** [58:38]: ... it pretty attractive to start doing cryptocurrency transactions for agents specifically. There's just like a number of reasons why this is quite convenient, and you don't really wanna set up your like personal bank account or your personal Stripe account on your agent, right? That's like quite a scary thing. And so there is like very real potential for, in the next couple of months, like a lot more overall human commerce that's being transacted via agents that are not using specific-- that are using like a wide range of different currencies, mediated in, in part by th-these kind of transactions. And so I think that's like-

**Interviewer** [59:11]: Mm-hmm

**Nick Vincent** [59:11]: ... on my list of something to look out for. And then also a great thing about, you know, a huge benefit of the... Generally, there's some level of transparency for a lot of these things, right, is that we can actually monitor that quite well and it, it kind of enables-

**Interviewer** [59:22]: Mm-hmm

**Nick Vincent** [59:22]: ... this new form of global scale economic monitoring that I think is like actually gonna be quite exciting to economists. [both chuckling]

**Interviewer** [59:31]: Right. Right. Yeah, that's a whole other thing that unfortunately I don't think we have enough time to go into.

**Nick Vincent** [59:37]: No, no, no. Certainly.

**Interviewer** [59:37]: But yeah, that's a whole other rabbit hole and like, yeah, I have too many other questions. But we've reached about an hour, and maybe we can just do a second one another time and talk more about it.

**Nick Vincent** [59:46]: Yeah.

**Interviewer** [59:46]: But I would love to, if you want to... Well, first, thank you so much for coming on. It's been super illuminating and really appreciate your writing and your work, and it's been really nice for me to also find the other people who are thinking about AI in this, like in, from a collective bargaining and collective action perspective, just because it's, that's, it's quite rare to find. But yeah, are there any plugs you would like to leave the listeners?

**Nick Vincent** [60:09]: I mean, first of all, I should just mention that all the kind of papers and research that I talked about here, right, almost always is a massive, you know, getting that out is a massive collaborative effort. So definitely, I mean, feel free to check out my website. You can read the paper, see all of my collaborators. Several of them, for instance, o-on this kind of simulation-y measuring data work, grad students who are, you know, near graduating, so definitely check out their work. You know, if someone happens to be listening to this and is hiring in this space, let me know. Happy to make some recommendations of great folks who are doing really exciting work. And more generally, I guess I, I should also shout out there's a growing kind of public AI network, which is, that's a place that I'm kind of digitally hanging out a lot, and that has become a, you know, a nice kind of network of friendly faces and there's just- I have benefited a lot from that group, so you can Google the Public AI Network, check that out as well. But yeah, I guess, sorry, I didn't prepare a list, but ge- generally speaking, whenever I do one of these things, I wanna make sure to just communicate just how immensely collaborative th- this whole effort is and how these things are sort of, you know, big collective projects, of course. [laughs]

**Interviewer** [61:08]: [laughs]

**Nick Vincent** [61:08]: How could they not be? You know, sh- shout out to all the people who contributed to the LLM so that I could, you know-

**Interviewer** [61:13]: [laughs]

**Nick Vincent** [61:13]: ... use Claude Code and Codex. I make this... I actually m- mean that quite seriously. I do think the lab should put, like, a thank you page on their website. I, I, I, like, legitimately think-

**Interviewer** [61:20]: [laughs]

**Nick Vincent** [61:21]: ... that there would be-- it would be meaningful if there was, like, a openai.com/thanks.html page-

**Interviewer** [61:26]: [laughs]

**Nick Vincent** [61:26]: ... that said something of that nature. I'd like to see that. [laughs]

**Interviewer** [61:29]: I would love it if it would give very specific thank yous to people too.

**Nick Vincent** [61:33]: [laughs]

**Interviewer** [61:33]: Like, thank you Monica-

**Nick Vincent** [61:36]: Yeah

**Interviewer** [61:36]: ... for commenting on that post on Facebook to [laughs] Larry about-

**Nick Vincent** [61:40]: Yes. No, I think we should do this. Okay. Yeah. So actually, just, and really quickly, I'll just list off a couple other foods for thought, pieces of food for thought slash maybe, yeah, we can carry on this conversation at another time. There is a growing technical field that's trying to do stuff like that, so specifically attribute, you know, people, individuals or groups of people who specifically contributed to an AI model. That is a field that exists. It's a really tough problem, but we're making progress there. And then another thing that I didn't talk about much today is, uh, I think I mentioned briefly, is that there is this whole emerging policy space around AI dividends, data dividends, windfall, things of that nature, and I think that is going to have some really deep interaction points with, with a lot of the topics of your interest. So that's something I'm on the lookout for too. But I'll stop it there so we don't go too long.

**Interviewer** [62:23]: Yeah.

**Nick Vincent** [62:23]: Obviously, so much to talk about here, and really appreciate you providing the space and just chatting with me about this. [laughs]

**Interviewer** [62:30]: Yeah, of course. Thank you. The Substack is Data Leverage. Check it out, lots of nice writing, and thank you, Nick. Uh, hopefully we'll have another conversation soon. If you like what I'm doing here, consider supporting the show on Patreon. Your contributions help me keep doing this work and dive deeper into the politics of decentralized technologies. I promise you absolutely zero financial returns, no airdrops, and your investment may go to zero, but you will get good content. Check out patreon.com/theblockchainsocialist to support the show. [upbeat music]

