---
title: "Scaling the Paywall: How Unpaywall Improved Open Access"
person: jason-priem
section: by
type: talk-transcript
year: 2019
venue: "The ORION Open Science Podcast (Podbean, 2019-02-14)"
source_url: https://orionopenscience.podbean.com/e/scaling-the-paywall-how-unpaywall-improved-open-access/
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 31
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Scaling the Paywall: How Unpaywall Improved Open Access

*Speakers (inferred):* speaker_0=Louisa Bengtsson, speaker_1=Emma Harris, speaker_2=Heather Piwowar

## Transcript
**Louisa Bengtsson** [00:00]: [jazz music] Hello, listeners. Welcome to another episode of Orion Open Science podcast.

**Emma Harris** [00:13]: I'm Emma Harris.

**Louisa Bengtsson** [00:14]: I'm Louisa Bengtsson.

**Emma Harris** [00:16]: And we're broadcasting to you from Berlin, Germany.

**Louisa Bengtsson** [00:19]: In today's episode, we are talking with, uh, Heather Piwowar. She, uh, has found, or she co-founded an organization, the Unpaywall, um, which, um, found a really clever way, um, to, uh, give us access to literature online basically.

**Emma Harris** [00:39]: Absolutely. So basically, Unpaywall is a database and then a browser extension, and if you want to read an article and it's behind a paywall, it will search the entire internet to find you a version of that article that isn't behind a paywall. Um, and it, it... You can read it for free, and it works in about, I think Heather says about 50% of cases, so.

**Louisa Bengtsson** [01:04]: Okay. Uh, so I guess it searches all the institutional repositories and, um, any articles people upload on their personal webpages or-

**Emma Harris** [01:14]: Exactly, yeah, yeah. Um, so yeah, it, it basically finds anything that's not behind where the journals kind of are-

**Louisa Bengtsson** [01:21]: Mm

**Emma Harris** [01:21]: ... keeping it [laughs] under lock and key.

**Louisa Bengtsson** [01:24]: Oh, okay. Yeah, very cool. So, uh, yeah, before we talk more about it, I think let's, uh, let's listen to Heather.

**Emma Harris** [01:31]: Let's get the story from the, from the-

**Louisa Bengtsson** [01:33]: From the source

**Emma Harris** [01:34]: ... from the source.

**Louisa Bengtsson** [01:35]: Yes.

**Emma Harris** [01:35]: Yes, indeed.

**Louisa Bengtsson** [01:36]: From the source. [jazz music]

**Heather Piwowar** [01:48]: My name is Heather Piwowar. I am a co-founder of Impact Story, a non-profit company, along with Jason Priem. Uh, Impact Story has existed for seven years. Our goal is to build tools to bring about the transformation to open science. Um, before that, I actually have a background in electrical engineering and digital signal processing. I went to MIT. I worked as a computer scientist for 10 years. I got my PhD in biomedical informatics and got into open science that way.

**Emma Harris** [02:19]: Wow. Um, that's, that's quite a journey. Um-

**Heather Piwowar** [02:22]: [laughs]

**Emma Harris** [02:22]: ... I kinda feel I should ask you a follow-up questions just on, on, on that really. Um, you know what I am? So an... You went from engineering to biomedical informatics. That's-

**Heather Piwowar** [02:32]: I did

**Emma Harris** [02:32]: ... Is, is that quite a jump, or it sounds like it's unrelated to me, but I'm, I'm a humanities person.

**Heather Piwowar** [02:38]: Yeah, good question. It is pretty unrelated, but I guess over the course of 10 years, you end up doing things that are unrelated. So each, each step was sort of related. I was doing, uh, voice recognition and, uh, um, h- uh, text over cell phones be- when that was only cool in Japan, uh, to start [laughs] with. And then, um, changed companies to follow my boss who went to a different company and liked me, and that was a biotech. Um, and then started going back to school and so anyway, it all just kinda happened.

**Emma Harris** [03:12]: Oh, good. That's-

**Heather Piwowar** [03:13]: Yeah

**Emma Harris** [03:13]: ... that's really good. But for today, could you tell, um, us what Unpaywall is and why you and your colleagues helped create it?

**Heather Piwowar** [03:23]: And so the colleagues is, is me and Jason Priem. So, um, we are the whole company, though actually we're bringing on a third employee, uh, this coming month, so that's pretty exciting, um, to help with development work, um, especially around Unpaywall. But the, the people who created it are me and Jason. Um, Unpaywall is a database of links to open access articles, and that sounds pretty boring, but it's actually pretty transformational. So how... What most of your, um, listeners might know of Unpaywall as a browser extension.

**Emma Harris** [03:58]: Yeah.

**Heather Piwowar** [03:58]: And so, um, it is a free browser extension. If you d- haven't got it yet, go and install it now. Uh, it works for Chrome and Firefox. Uh, it's free. The way that it works is once you've installed it, if you go to a landing page of an article, and we can detect that, uh, um, the... If the software can detect that it's the page, um, that is a scholarly article, so it's got a DOI on it, um, we pop up a little logo on the side of the page, kind of discreetly on the what's, l- right-hand side of the page. And that, um, lock is gray if we cannot find a co- free copy to read on the internet anywhere, uh, and turns green when we can. And the exciting news is about half the time, uh, we can find a free copy somewhere on the internet. Sometimes, to be fair, you're actually sitting on a free copy if you're looking at a PLOS article or a PeerJ article. But often you're sitting at something, and it's, it's cool to see the, um, green unlock icon, which if you click on, takes you immediately to a free article right beside a big box on a publisher page that says, "Pay $39 to view." And it feels, it, it feels like we're really unlocking the power-

**Emma Harris** [05:11]: Wow

**Heather Piwowar** [05:12]: ... of open access that people have been building, uh, for so long. So for decades now, um, into archive and, and for a decade into PMC and so on-

**Emma Harris** [05:22]: Yeah

**Heather Piwowar** [05:22]: ... people have been archiving, um, copies of their papers. And so what Unpaywall is, is we're finding all those, all those copies, bringing them into one place, and then putting interfaces like this browser extension on top of it to help bring those copies to the places where people wanna see them. So one, one of the, one of the, um, uses is this browser extension. We've got some more uses which we can talk about later, but that, that's what Unpaywall is. Uh, I should say it's about 20 million, uh, free-to-read, um, open access copies, which is really exciting.

**Emma Harris** [05:57]: Wow.

**Heather Piwowar** [05:57]: And like I said, it's about half of the recent literature, um, is free to read.

**Emma Harris** [06:02]: That's fantastic. That's, that's really cool

**Heather Piwowar** [06:05]: Yeah.

**Emma Harris** [06:05]: And oh my God, I wish I had had that resource when I was finishing up my PhD. Um [laughs]

**Heather Piwowar** [06:12]: Yeah.

**Emma Harris** [06:12]: I don't know if I, I didn't know about it or it hadn't been invented yet, but either way, brilliant.

**Heather Piwowar** [06:17]: Mm-hmm.

**Emma Harris** [06:17]: Um, so how are people actually using this on the web then?

**Heather Piwowar** [06:22]: Yeah, it's a good question. So in the browser extension, like I was saying, and it's also got some other really great uses. So I don't know if you noticed, but Europe PMC itself actually links to Unpaywall. So Europe PMC links directly to copies in PMC whenever they're available there. But sometimes, um, articles are available for free but they're not in PMC, they're in an institutional repository. Sometimes they're in bio archive, sometimes they're in, uh, normal arch- And so PMC actually, uh, about six months ago I think, started linking, uh, using the Unpaywall database and API to link out to these free copies. And they, in doing so, they doubled the amount of full text they, um, link to from something like... Or approximately doubled from something like 4 million to 7 million, which is really exciting. They're not the only ones. Uh, Scopus, Web of Science, and Dimensions also all use the Unpaywall database, uh, to link directly from their articles, uh, to a free copy, um, and to give the data about what kind of open access the articles are for people doing analysis. So that's really exciting too, um, from a assessment point of view, and even more importantly, from a discovery point of view so people can read things. Um, and finally another cool use is a lot of libraries are using us. About 2,000 libraries are using Unpaywall in their link resolver. So when you're on a library site and you click on a DOI link and you wanna go to the paper, the library actually checks to see if it's in its subscription holdings first, and if so, sends you to the subscription page that it's paid for. If n- if it doesn't subscribe, now it checks the Unpaywall database to see if there is a free copy on the web, and if so, it links you to that free copy, and only if there is not a free copy does it send you to their interlibrary loan page. And so we're helping people get that instant paper, uh, that much faster, taking the burden off the libraries, making their patrons happy. So again, about 2,000 libraries are using our free API to do that. Um, they include the British Library, the University of California Library System, and, and all sorts. So yeah, it's really exciting.

**Emma Harris** [08:34]: That's, that's great. I mean, it sounds like it's, it's really growing. It, you're really-

**Heather Piwowar** [08:38]: Yeah

**Emma Harris** [08:38]: ... kind of gaining momentum with this. Um-

**Heather Piwowar** [08:40]: Yeah, yeah.

**Emma Harris** [08:42]: Yeah. Um, so I mean, for our kind of tech geek audience, um, could you just say a little bit, maybe in not too detail, but a, a kind of a prec- precis of, of how you kind of went about creating this? Like what kind of system coding, whatever did you, did you use, and what was your inspiration to create it?

**Heather Piwowar** [09:06]: Yeah, for sure. I'd love to. So it's a cool story actually. So we have a product called Impact Story Profiles, um, which people are welcome to check out. Um, it actually gathers together lots of social media metrics, lots of alt metrics, um, about your papers. Um, and I could... That's a different podcast, so we won't talk about that. [laughs] But, but it has badges, and we wanted to give people a badge for being an open access hero if half of their papers were open access or h- or 100%, I forget what it is. Anyway, um, but so we wanted to collect that data. We didn't realize how hard that was going to be to collect. There weren't good APIs, uh, that, that wasn't centralized. So frankly, Google Scholar actually has that information. Google Scholar does a great job of pointing people to open copies, but Google Scholar does not have an API, and they've said they never will due to agreements they've made with publishers.

**Emma Harris** [09:59]: Yeah.

**Heather Piwowar** [09:59]: So that means we can't build on Google Scholar's, um, results in our app. So instead what we decided to do was go build it ourselves. Um, we looked at other people who had similar APIs, like Open Access Button, which people might have heard of, OpenAIRE, CORE, uh, Dissemin, various. And they, they got, various of them got various bits of the puzzle right, but they either had their API limits were too, um, low or their accuracy wasn't good enough, or a variety of things. So, so we needed to build it ourselves. So we did, and then we decided that, you know what, this isn't just useful for our little cute button on the internet. Um, it's actually gonna be useful for a lot of other people with the same problem that we have. So we made it available as an API about two years ago, and it really t- took off from there. So I can tell you a little bit now, uh, about sort of at a high level, its tech stack if you want, for the geeks. Um, so it's written in... So, um, the front end, the browser stuff is written in JavaScript, uh, Angular I think. Um, but the back end is all written in Python. The data is in a Heroku database. We host all of it on Heroku. Um, uh, yeah. That's the tech stack. [laughs]

**Emma Harris** [11:21]: That, that, that's fine. I mean, um, yeah, uh, I did a bit of Python, uh, once because I had to to fix something. [laughs]

**Heather Piwowar** [11:29]: Yeah.

**Emma Harris** [11:29]: And that's about as far as my coding knowledge goes, I'm afraid. So yeah-

**Heather Piwowar** [11:33]: Yeah

**Emma Harris** [11:33]: ... probably best to keep it at that level or I'll just nod vacantly at you. Um-

**Heather Piwowar** [11:38]: It is all open source, I think in, like for, for the geeks in your audience, in which super includes me, um, it's all open source. So it's on GitHub. Um, it's actually the, the back end code is under Impact Story/OADOI. Uh, that was its original name, uh, because we had a link resolver that would take you to the OA version. Anyway, it's all there if people wanna go have a look

**Emma Harris** [12:02]: Cool. That's great. I'm, I'm, I'm pretty sure there'll be some listeners who will definitely wanna have a look. Well, I mean, what, what is it about open science that you feel is so important that, um, uh, justifies the, the, the work and time that you've put into it? Um-

**Heather Piwowar** [12:18]: That's a good question. So my ... So the way I got into it was through caring about open data and data sharing. So I was a PhD, and I wanted to use other people's clinical trials data, their genomics data. And so at that point in the, uh, mid-2000s, people were drawing lots of graphs of GenBank and the number of submissions to it, and PDB and the number of submissions, and ArrayExpress and Geo and the number of, uh, microarray submissions to those. They were always, like, graphs that would go up, which was great. And so it felt like, "Aha, this is a super good idea to do." But then I realized, um, nobody knew th- whether w- the quality of the data that was going into those databases. So in the case of GenBank, almost everything was going in, but that wasn't true for microarray data, for example, or for most other, uh, data archives. And so it wasn't clear whether it was this great quality stuff that people were really proud of that they were putting in or the dregs that they didn't c- they were like, "Okay, I'm not gonna use this," or like, "I'm willing to share this," um, or, or the medium stuff. And so it fe- felt a little, like, um, tenuous to build one's PhD and potentially career of building on top of this-

**Emma Harris** [13:33]: Sure

**Heather Piwowar** [13:33]: ... data when you don't know what's in there. So, so studying what was in there be- and, and building incentives for people to put everything in there so that the good and the bad quality, and we could know, uh, became a real passion for me because it feels, it feels efficient. It feels fair. It feels like people can build, you know, stand, stand on the shoulders of giants, right? And it feels like it was what we should be doing. But the, the incentive problem is a real problem because you do stick your neck out, um, to do it early, yeah? Now, you can-

**Emma Harris** [14:09]: Yeah

**Heather Piwowar** [14:09]: ... stick your neck out in ways that can give you some pretty good rewards because, because it can be a star. You know, it can be a, a, an a- an asset right now because it's not normal. On the other hand, it can also feel really scary, and what we actually want is everyone to do it. So what is it that w- it will take for everyone to be more open with their science? And so that's, that's where the passion came for me, and, and it's a just a short step, right, from there to care about open access, to care about alternative metrics and alternative products and so on, so.

**Emma Harris** [14:42]: Okay. That, that's really ... Yeah, that's really interesting actually because you saying that you're coming from a, a data sharing background.

**Heather Piwowar** [14:50]: Mm-hmm.

**Emma Harris** [14:51]: And what struck me when I was doing the research for this episode was that you've kind of applied the discoverability element that is usually discussed in terms of sharing data-

**Heather Piwowar** [15:04]: Mm-hmm

**Emma Harris** [15:05]: ... to open access.

**Heather Piwowar** [15:06]: Mm-hmm.

**Emma Harris** [15:06]: Um, so normally open access, all the discussion is, is aimed at authors and, to a lesser extent, publishers making things open access.

**Heather Piwowar** [15:18]: Mm-hmm.

**Emma Harris** [15:18]: Where you've kind of taken it from the other way around and gone, "Well, let's find out what's actually available and increase our open access that way." Um-

**Heather Piwowar** [15:28]: Right. I think it's a really good point, and I think it's one that doesn't get enough attention, is that I think because in a lot of ways the discoverability problem was solved in many ways a- by Google Scholar, yeah? The problem is that it wasn't discoverable in a way that other people could build on, so it didn't have those APIs.

**Emma Harris** [15:50]: Right.

**Heather Piwowar** [15:50]: And the peop- And, and people don't complain very much about something that's solved for the end user but not for the integrators. You don't hear a lot of-

**Emma Harris** [16:01]: Mm

**Heather Piwowar** [16:01]: ... complaints about that. What there is is this huge opportunity cost. Huge. I mean, Unpaywall is a great example of that. Um, and I think also in data, um, discoverability, there's another great use of that. Google, again, as it turns out, it wouldn't have to be Google, could have been somebody else, has built a data ... What do they call it? Data search tool. Something like that.

**Emma Harris** [16:24]: Oh, yeah. I know what you mean. Yeah.

**Heather Piwowar** [16:26]: Yeah, that came out in the last couple months, yeah? But right now it's just a UI. Again, there's not an API on it, and it means that people can't build on it. And so I think that it's really ... And while I'm glad there's now a UI sort of solution for it that works fairly well, best I can tell, I'm a little bit afraid that it will dampen down the talk about discoverability-

**Emma Harris** [16:49]: Mm

**Heather Piwowar** [16:49]: ... of datasets, and we will all be satisfied with this solution that doesn't let people build on it. And I think that for that, that discussion is, is great. It's great to get funding. It helps, it helps people who wanna build that open infrastructure layer openly, um, get funding, have, have ... get attention, be the tool of choice-

**Emma Harris** [17:13]: Mm-hmm

**Heather Piwowar** [17:13]: ... and so on. And I, I think it does need ... Yeah, so I think it needs, it needs more attention than it's getting.

**Emma Harris** [17:19]: Mm.

**Heather Piwowar** [17:19]: And I think I'm really glad that Unpaywa- to the extent that Unpaywall can s- highlight the value of doing something openly and making its data open and the ... Even though there wasn't, which I think is an astute point, a lot of discussion about how this was a problem.

**Emma Harris** [17:37]: Yeah.

**Heather Piwowar** [17:37]: It obviously was a problem because it's only two years old, and it's really taken off, and I think really made the world a better place because a lot more people can find and read the scholarly literature a lot more easily now. That's fantastic.

**Emma Harris** [17:51]: Yeah, I mean, that's ... Well, obviously, I mean, I would, I would say-

**Heather Piwowar** [17:55]: [laughs]

**Emma Harris** [17:55]: ... but I can't see anyone arguing with, with that. And I mean, there's a, a, I think a, a problem in general in that, um- There's an, a- a lot of researchers who are actually quite willing to place their articles in a, in a, in an archive or their data online in some way. Um, but as you say, there's a gap between what researchers are willing to do and what is actually usable information at the end of the day. And I think discoverability is ... and, and usability and, you know, the f- the, the fair principles generally-

**Heather Piwowar** [18:33]: Mm-hmm

**Emma Harris** [18:33]: ... uh, you know, findable, accessible, interoperable, reproducible, the rest of it. I mean, I think that's where the gap is now. I think, I think we've essentially, we're winning the, the, the battle for, um, hearts and minds, as it were, as the Americans like to say. I think we're convincing people that this is something that needs to be done. But it's just that everybody's doing it in a slightly different way, and they're not, as you pointed out, doing it in a way that is maybe, um, particularly helpful in terms of, uh, expansion and, and extending-

**Heather Piwowar** [19:08]: Mm-hmm

**Emma Harris** [19:08]: ... and making things better and building on things.

**Heather Piwowar** [19:10]: Mm-hmm.

**Emma Harris** [19:10]: So yeah, for me, discoverability is, is one of the kind of, um, missing links in, in the open science movement. Um-

**Heather Piwowar** [19:18]: Mm-hmm

**Emma Harris** [19:18]: ... I read that, um, Elsevier are now paying a subscription or linking to A- Unpaywall in some way.

**Heather Piwowar** [19:26]: Yeah.

**Emma Harris** [19:26]: Um, do you feel that's a positive thing? 'Cause Elsevier do get a really bad rap from the open science community generally.

**Heather Piwowar** [19:35]: Yeah, they do. Um, so Elsevier is a customer of our Unpaywall data feed. So we ... One thing we're super proud about, about Unpaywall is the sustainability model that we've developed. So the API is free for anyone to use. They can call it up to 100,000 times a day with just an email address as the token. Um, and it's a very fast API. And so frankly, Europe PMC is building its help entirely on the API, which ... And so are lots of others. It's, it's really, um, really generative-

**Emma Harris** [20:08]: Yeah

**Heather Piwowar** [20:08]: ... really, really working out well that way.

**Emma Harris** [20:10]: Yeah.

**Heather Piwowar** [20:10]: We also do an entire dump of the database, uh, every six months and make that available for people to use commercially and not commercially, and non-commercially. Um, sorry. Non-commercially and commercially, to put the emphasis in the relevant place. Um, uh, which so, so again, open. It's open source, as I said. So there is the browser's free, yeah? Um, so it's very open. But there are some customers who want to keep a local copy, and they want to keep it up to date.

**Emma Harris** [20:38]: Yeah.

**Heather Piwowar** [20:38]: They also usually want a contract, uh, to sign with somebody to say we have liability insurance, et cetera, yeah? And so for those people, having something to ... Having a contract and a, a weekly feed, uh, is useful. And so we offer that, uh, called our data feed, uh, service. And so some of our big, um, integrators have subscribed to that. So, um, Clarivate Analytics was the first one. They also gave us a grant, uh, to do some of this, build some of this open source code, which was fantastic. Wanna give them a shout-out for that.

**Emma Harris** [21:11]: Yeah.

**Heather Piwowar** [21:11]: Um, because they can, they sometimes get a bad rap, and that was a really, uh, open move on their part. Um, Dimensions is an early adopter as well, and so is Elsevier to put in their Scopus product and potentially other things in the future. So I don't ... I have, um, often myself had issues with Elsevier's, um, approaches to things, uh-

**Emma Harris** [21:38]: Sure, yeah

**Heather Piwowar** [21:38]: ... open sciencey. Um, but I am sure glad, thrilled that they are a subscriber to this product-

**Emma Harris** [21:45]: Yeah

**Heather Piwowar** [21:45]: ... and that they're bringing this data into Scopus. It makes open access more visible, more findable for everybody. Who can't ... Who wouldn't be on board with that? I think it's fantastic. This is for their Scopus product. It's not on their publishing side at all. Um, and so I'm just leaving out their publishing and toll access versus open access from their pub- from their publishing side.

**Emma Harris** [22:07]: Yeah.

**Heather Piwowar** [22:07]: I think from a Scopus, from a analytics perspective, it's great news.

**Emma Harris** [22:11]: What do you see as the, the kind of the next step for Unpaywall and for open access generally? Um, where's the future? [laughs]

**Heather Piwowar** [22:21]: Yeah, good question. I'm a pretty big fan of Plan S, which I think isn't popular in some circles. Um, but I think that's the future. I think radical change-

**Emma Harris** [22:32]: Good

**Heather Piwowar** [22:32]: ... so I think full open access and as soon as possible. And notably, that will render Unpaywall, um, fairly useless, right? So all of that nice subscription business model we've got going on, that all goes away if you actually just follow the DOI and get to read the paper. But that is-

**Emma Harris** [22:50]: Yeah

**Heather Piwowar** [22:50]: ... definitely the world I want. I am working as hard as I can to bring about that world. Unpaywall is a stopgap. Uh, and I hope-

**Emma Harris** [22:58]: Mm

**Heather Piwowar** [22:58]: ... it isn't needed. Um, it'll frankly still be needed some for back content and so on, yeah? But-

**Emma Harris** [23:04]: Yeah

**Heather Piwowar** [23:04]: ... but, um, but not at the same level. Um, and so yeah. So, so I hope the future is full open access as soon as possible.

**Emma Harris** [23:13]: If you had one kind of take-home message for, uh, you know, early career researchers who are, who, who are looking to ha- have a good career but also maybe try and do things the best possible way, what, what would that be?

**Heather Piwowar** [23:31]: So it would be to be the change you want to see.

**Emma Harris** [23:34]: Yeah.

**Heather Piwowar** [23:35]: And I think most researchers can see that a more open world will help us make the most scientific progress. And I think what most researchers want is the most scientific progress. They themselves wanna make a whole bunch of it, for sure, and they wanna make some important parts.

**Emma Harris** [23:51]: Yeah.

**Heather Piwowar** [23:51]: So do that. That sounds good. But along the way, do it in a way that's, that's building a better system, and a better system is a more open one than we've got right now. I think it's gotta be ... We've gotta build the infrastructure to make it open for everybody. So and also you've gotta be the change you wanna see. So I think do be willing to stick your neck out and make your papers open access. Um, I think do make your data open access. Put your code, um, on GitHub. Do the things that you, that are pushing your field a little. And, and then brag about it. So turn it into a, um, positive by saying why you're doing it, and making it be a positive in job interviews, on y- in your tenure case, and so on. Not everyone's gonna buy it, but a lot of people will. And right now, we're still n- still in the spot where it will help you stand out, and it will help you stand out as someone who cares about the future, is thinking about the future, is willing to be a little altruistic, and is willing to be brave. And I think those are all really good attributes that will be respected by a lot of people, um, evaluating you. And along the way, you're, yeah, you're building a world you wanna see. So that would be my advice. [upbeat jazz music]

**Emma Harris** [25:24]: I liked what Heather said at the end of the interview, um, about being the change that you want to see in research and in open science.

**Louisa Bengtsson** [25:32]: Well, I guess there's no way around it, huh? I mean, it's, uh, uh, either you do it or you don't do it, but nobody else will do it for you. Well, unless you have wonderful people like Heather [laughs] who actually do something for you.

**Emma Harris** [25:42]: [laughs]

**Louisa Bengtsson** [25:42]: But I mean, in, in the end, you have to use it, right?

**Emma Harris** [25:45]: Yeah.

**Louisa Bengtsson** [25:45]: You have to live open science, uh-

**Emma Harris** [25:48]: Absolutely

**Louisa Bengtsson** [25:48]: ... in order for it to get established, so, uh, it's like a revolution, huh? I mean, nobody will do a revolution for you. [laughs]

**Emma Harris** [25:55]: No, no, no. But I'm very glad that there are people like Heather who, who are maybe manning the barricades in-

**Louisa Bengtsson** [26:00]: Yeah

**Emma Harris** [26:01]: ... your revolution-

**Louisa Bengtsson** [26:02]: Yeah. [laughs]

**Emma Harris** [26:02]: ... analogy here.

**Louisa Bengtsson** [26:03]: The, the first wave, so to say. [laughs]

**Emma Harris** [26:05]: Yes, yes. You know, sort of Le- uh, Les Miserables type, you know. Um, yes. So I, I think we may have got off topic here slightly. Um... [laughs]

**Louisa Bengtsson** [26:14]: Yeah, no. I mean, I, I'm also, uh, also kind of, um, hoping just like she does, um, that Plan S, um, will be, uh, replacing all this, um, initiatives. So we're, we're actually gonna be talking about Plan S next episode, so bear with us. Um-

**Emma Harris** [26:29]: Yeah

**Louisa Bengtsson** [26:30]: ... um, but yeah. I mean, Plan S is a European, uh, initiative, top-down totally, uh, to make all publishing open access basically.

**Emma Harris** [26:38]: Basically.

**Louisa Bengtsson** [26:39]: Yeah.

**Emma Harris** [26:39]: If you receive, uh, state or European funding, you have to do open access.

**Louisa Bengtsson** [26:43]: Yeah.

**Emma Harris** [26:43]: So we'll talk about it in a lot of detail next episode, so don't worry. Um, but the idea is that everything would be open access, which would make all these, um, kind of fixes and patches-

**Louisa Bengtsson** [26:57]: Mm-hmm

**Emma Harris** [26:57]: ... um, like Unpaywall, wonderful though it is, um, completely redundant.

**Louisa Bengtsson** [27:02]: Mm.

**Emma Harris** [27:03]: So.

**Louisa Bengtsson** [27:03]: Yeah. But until Plan S is in effect, please do go and-

**Emma Harris** [27:07]: If Plan S is.

**Louisa Bengtsson** [27:07]: And if. [laughs] Uh, please do go and, uh, just install the Unpaywall. It's a very easy add-on, right, at the browser?

**Emma Harris** [27:14]: Yeah, absolutely.

**Louisa Bengtsson** [27:15]: Yeah.

**Emma Harris** [27:15]: You just add it to your, to your browser, and it's there doing, doing good work for you.

**Louisa Bengtsson** [27:20]: So I, I wasn't there for the interview, so I know.

**Emma Harris** [27:22]: Yeah.

**Louisa Bengtsson** [27:22]: But, um, you, you guys, when I listen to it, um, you talked a bit briefly about the Google Search, the new, uh, Google data search algorithm.

**Emma Harris** [27:29]: So dataset search is still in the beta testing phase, but it's essentially Google Scholar for datasets.

**Louisa Bengtsson** [27:37]: Mm-hmm.

**Emma Harris** [27:37]: Um, so this is kind of what people have been hoping for, in that you will be able to search using Google's amazing power, uh, for different, uh, dataset, and be able to analyze it and so forth. Um, and if you, if you regularly putting datasets out there, it's worth getting in touch with them and, um, putting your data forward to be included now, um, at this stage. Because it helps them, and it'll also be one of the earliest datasets available, so your research-

**Louisa Bengtsson** [28:09]: Mm

**Emma Harris** [28:09]: ... gets more well-known.

**Louisa Bengtsson** [28:10]: But you do have to, like, you, you do have to sort of like, uh, include your dataset in their repository or, like, database I guess.

**Emma Harris** [28:18]: Sure, yeah. I think you have to... Uh, they have certain guidelines-

**Louisa Bengtsson** [28:21]: Mm

**Emma Harris** [28:21]: ... for dataset providers, and you have to kind of-

**Louisa Bengtsson** [28:24]: Interesting, yeah

**Emma Harris** [28:24]: ... fit it into their... So at the moment they've got things like, uh, NASA and Harvard's Dataverse available. That's 'cause NASA have been making their data-

**Louisa Bengtsson** [28:32]: Mm

**Emma Harris** [28:32]: ... open, open access for years now. Um-

**Louisa Bengtsson** [28:35]: Oh, NA- NASA rocks.

**Emma Harris** [28:36]: Yeah.

**Louisa Bengtsson** [28:37]: Oh.

**Emma Harris** [28:37]: It's amazing.

**Louisa Bengtsson** [28:38]: Oh, NASA just kicks ass. I mean-

**Emma Harris** [28:40]: Yeah, we love NASA.

**Louisa Bengtsson** [28:41]: Yeah. [laughs]

**Emma Harris** [28:41]: Everyone who d- knows anything about open science is, like, Team NASA. I mean, I was Team NASA anyway because I love astronomy and space and astronauts and stuff, but you know. Um, then I, I did open science. I was like, "Oh, NASA is also amazing for that."

**Louisa Bengtsson** [28:54]: Yeah. [laughs]

**Emma Harris** [28:55]: [laughs]

**Louisa Bengtsson** [28:56]: Ah, yeah.

**Emma Harris** [28:56]: Um, but anyway, that's some of the datasets they've got available. But I, yeah, if you're interested at all in, um, in, in taking a look, I, I'd recommend it. It's, it could be a game changer. I mean, Heather kind of alluded to that.

**Louisa Bengtsson** [29:08]: Mm.

**Emma Harris** [29:08]: That it's probably going to be the next big thing.

**Louisa Bengtsson** [29:11]: We have planned an episode on data, um, data science. Well, not data science per se, but open data. [laughs]

**Emma Harris** [29:16]: Yeah.

**Louisa Bengtsson** [29:17]: So.

**Emma Harris** [29:17]: Well, several on open data. But on, on data, metadata specifically and, and data repositories, yeah. That's coming-

**Louisa Bengtsson** [29:24]: Yeah

**Emma Harris** [29:24]: ... later this year.

**Louisa Bengtsson** [29:25]: Maybe we can also try to reach the guys from Google and tell us more about their dataset search.

**Emma Harris** [29:29]: That would be great. Yeah, love that.

**Louisa Bengtsson** [29:31]: We'll see. We'll keep you posted. We'll keep you posted.

**Emma Harris** [29:33]: Oh, trust me, if we get an interview with Google, we'll tell you. [laughs]

**Louisa Bengtsson** [29:37]: If you know of anybody who is doing similar stuff that we don't know of, uh, please tell us. I mean, we would love to have people on the show who, like, really hacking the system in a way, you know.

**Emma Harris** [29:46]: Yeah, absolutely.

**Louisa Bengtsson** [29:47]: Just finding solutions to, to problems people have, and, uh, find good solutions. And, uh, so yeah. If you, if you know anybody, let us know.

**Emma Harris** [29:55]: Yeah. If you're part of any projects or, um, personal endeavors, um, yeah, just, just tweet us or, um, email us anytime.

**Louisa Bengtsson** [30:05]: And the Twitter is the...

**Emma Harris** [30:08]: O-O-S-P underscore Orion Pod. And the email is orion@mdc-berlin.de. And you can find us on, um, everywhere really. [laughs] Um, iTunes and Podbean and all major, uh, podcasting apps.

**Louisa Bengtsson** [30:26]: This episode was brought to you from, um, MDC, Max Delbrück Center for Molecular Medicine in Berlin in Germany. Um, the podcast is part of the Orion Open Science project. The music is done by Fabio de Miguel, and the sound editing done by Paulo Oliveira.

**Emma Harris** [30:42]: And we hope that you enjoyed the episode, and you will tune in next time. [outtro music]

**Louisa Bengtsson** [30:48]: See you.

**Emma Harris** [30:48]: Bye now.

