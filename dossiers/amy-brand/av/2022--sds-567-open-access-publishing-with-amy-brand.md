---
title: "SDS 567: Open-Access Publishing — with Amy Brand"
person: amy-brand
section: by
type: talk-transcript
year: 2022
venue: "*SuperDataScience* podcast (host Jon Krohn)"
source_url: https://www.youtube.com/watch?v=OKJwuvBDEdw
retrieved: 2026-08-15
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 76
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# SDS 567: Open-Access Publishing — with Amy Brand

*Speakers (inferred):* speaker_0=Host, speaker_1=Amy Brand

## Transcript
**Host** [00:00]: What can we do to change STEM so that it's more welcoming to everyone?

**Amy Brand** [00:06]: You know, it starts, it starts at the beginning, I always think in terms of pipeline. So in terms of education, it is, you know, how do you expose young kids of all ethnicities and, and genders, um, around the world to, to STEM careers in a way that makes them attractive and accessible? We... We're, we're soon gonna be launching a series, um, called Epistemologies of, of the Global South, which I'm very excited about.

**Host** [00:38]: Amy, welcome to the Super Data Science Podcast. I've been so excited about getting you on the program. Where in the world are you calling in from?

**Amy Brand** [00:47]: I am calling in from Newton, Massachusetts, uh, not too far from Cambridge.

**Host** [00:53]: Nice. And, uh, not surprising that you are close to Cambridge given that you work at MIT Press, which is in Cambridge. So, um, I'm sure all listeners are aware of the Massachusetts Institute of Technology, which is one of the world's foremost universities. Uh, and it has a great press. So the MIT Press is one of the world's largest university publishers. It's behind, in our industry, the Adaptive Computation and Machine Learning series, which is edited by the absolutely iconic data scientists Christopher Bishop, Michael I. Jordan, and others, and it includes books like Ian Goodfellow, Yoshua Bengio, and Aaron Courville's Deep Learning book, which is a bible for me. It is the book probably that I, uh, refer to the most of any. Um, and it's a great example of an MIT Press book that is freely available as, uh, HTML at deeplearningbook.org. We're gonna talk about that freeness [laughs] again very soon. Um, other titles in the series are, uh, Sutton and Barto's Reinforcement Learning: An Introduction, Kevin Murphy's Machine Learning: A Probabilistic Perspective, and a couple of dozen other amazing books. Um, so thank you, Amy, for being behind such amazing books for-

**Amy Brand** [02:08]: Thank you. And yeah, we, we publish a lot in data science, going out into less, even less kind of machine learning computational areas. So happy to be here.

**Host** [02:21]: Awesome. Uh, so what does it mean to be a director and publisher at MIT Press? What does that role involve?

**Amy Brand** [02:28]: I, I have one of the most fun jobs in the world because I just get to live in this world of just amazing ideas and help people see their creative works through to fruition. Um, but you know, day to day, what it means is running an organization of 100-plus people, mainly in, in the Boston/Cambridge area, but, uh, several of them in the UK as well. Uh, we publish about 350 books a year across a range of disciplines, 40 journals. Um, I feel sometimes like the orchestra conductor, you know? I'm-

**Host** [03:03]: [laughs]

**Amy Brand** [03:03]: ... uh, you know, trying to, to, to make it all work smoothly, but I have a fabulous team. We're a pretty non-hierarchical organization. Um, that's the director part. Uh, the publisher part, which was added to my title about a year ago, uh, and I was-

**Host** [03:20]: Mm

**Amy Brand** [03:20]: ... kind of insistent on it, was really important to me because, uh, I get to sign all the publishing contracts, so I'm ultimately responsible-

**Host** [03:29]: Mm

**Amy Brand** [03:29]: ... for, um, making those decisions. Now, of course, I consult widely-

**Host** [03:33]: Ah

**Amy Brand** [03:33]: ... with my team and others.

**Host** [03:35]: So literally every single book that gets published by the MIT Press, your signature is on the contract. You make a final decision.

**Amy Brand** [03:43]: That is correct, yes.

**Host** [03:45]: Wow, that's cool. I didn't realize that one person could have so much power. Um-

**Amy Brand** [03:49]: Yeah, I mean, it's somewhat distributed. Actually, m- less distributed at MIT than a lot of other university presses where the kind of faculty editorial boards are, uh, you know, have more power than they do at MIT. It's more consultative. But you know, that, that was decided long before I became director.

**Host** [04:09]: Cool. Yeah. And so publisher for, uh, the last year, at least in your title, having that there.

**Amy Brand** [04:14]: Yeah.

**Host** [04:14]: But director for seven years. Um, so-

**Amy Brand** [04:17]: Uh-huh

**Host** [04:17]: ... you have been leading MIT Press for some time. Um, so something that we alluded to already when I was talking about the Goodfellow book and its being freely available online is that, uh, MIT Press, uh, publishes a lot of books with open access, so, uh, over 12% of books are freely available. Why is open access valuable to scientists, data scientists, anybody doing research and development?

**Amy Brand** [04:42]: Well, I, I think it's, it's valuable to all scholars and, and researchers. There- there's, um, a special value to people in data science when you think about having that underlying information available to mine and compute over. Um, but you know, our investment in open access goes back literally decades at the MIT Press. Uh, you know, and, and for us it's an, it's an issue of making, uh, scholarship as equitably accessible around the world as possible, um, to as many researchers as possible and readers as possible, and also, um, to broadening participation in the whole research enterprise by making this information widely available. Um, among the many other things that I'm involved in in relation to the open data, open science, open access space is I'm on the board of Creative Commons, which of course is the organization that created-

**Host** [05:39]: No kidding

**Amy Brand** [05:40]: ... and-

**Host** [05:40]: Wow

**Amy Brand** [05:40]: ... yeah, runs, runs the, um, open licenses that we all use when we put our works online.

**Host** [05:47]: Wow.

**Amy Brand** [05:47]: Yeah.

**Host** [05:48]: I didn't know that. That didn't-- I didn't catch that in my research before the episode. That's amazing. And yeah, it, it makes so much sense to me that research, academic work, which is often publicly funded, it makes sense to me ... that it should be available then to the public to read. And so there's been a big shift since I've been an academic. So it's now 10 years since I finished my PhD, and it was during my PhD period where, um, not only [laughs] did we start to digitize works. So it's crazy to me to think that in my undergrad, especially in the first couple years of my undergrad, I had to physically go to the library-

**Amy Brand** [06:31]: That's right

**Host** [06:31]: ... and photocopy journal articles [laughs] that I-

**Amy Brand** [06:33]: Yeah

**Host** [06:34]: ... wanted to read later.

**Amy Brand** [06:35]: Um, if you look back at, at the history of digital information and open access, um, you know, it, it, it really did, uh, take off in, in the scientific journal space. But, but now today, and, and certainly in the way in which we publish at the MIT Press, it's across all disciplines and, and, and everything that we publish. Um, but it's a complicated topic. So you mentioned, okay, publicly funded research should be openly accessible. It's, it's not that simple. I mean, that is a core-

**Host** [07:04]: Mm

**Amy Brand** [07:04]: ... principle, but often you are talking about, um, you know, the creative works, you know, blood, sweat, and tears of an individual or a lab, um, that has data-

**Host** [07:13]: Mm

**Amy Brand** [07:13]: ... that it wants to use and leverage in, in other ways. Um, and so these, these decisions, um, are, are sometimes, you know, individual decisions, not necessarily made on the principle that, that, uh, it should be open. So for us, for example, when we publish open access books, it's always with, um, the consent of the author if it's something that we initiate, or because the authors, like in the case of the Deep Learning book, have demanded or expected that-

**Host** [07:41]: [laughs]

**Amy Brand** [07:41]: ... the work be made openly accessible. And that was a great example for us because, you know, we... It's very easy if you look at the business of publishing for us to take, say, scholarly monographs and professional books which have a relatively specialized limited audience and say, "We'll figure out a model in which we can make those openly available. We'll still sell some in print and digital form." But if you look at, um, you know, our textbook program, especially in computer science, AI, machine learning, which has been so core to the revenue of the press and the history of the press, it was a lot... it's a lot harder. But now, you know, a huge percentage of our, our reference and textbooks in, in AI and machine learning are openly available. And what we saw with the, with, with Deep Learning, um, was just, you know, it was the right book at the right time, and it was so tremendously successful in print while it was being made openly available.

**Host** [08:37]: Yeah, I think it's hard to tell because you can't kind of... You... It's hard to figure out from the data what the causal impact is. But I hypothesize, without any real data to back me up, that making something publicly available, it increases the reach so much. It allows a book like Deep Learning to have such a broad impact that everybody's aware of it. You're like, "Wow, this amazing book is available online." But you're also like, "But a lot of people, despite having access to it online," for me, for a lot of people, having the physical book, I'm able to attend to it a lot better. I'm able to make a lot more progress. I feel like I can understand pr- uh, concepts a lot better as a result of that. Um, you know, you can step away from the computer and just work through the book. Um, and so for me, the book is then hugely valuable. And so I might look at the first few pages online, the first chapter, and then I'm like, "Oh my goodness, I've gotta buy this." And I think that that experience happens for a lot of people.

**Amy Brand** [09:39]: I, I think that's true. Um, we see that a lot in open textbooks where we know that students wanna have the digital file as well as that print book. Um, and, uh, yeah, certainly with a book like li- this, with many books, um, we've done some experiments where it hasn't, uh, worked so well. So for example, when we've done like a $0 Kindle edition of a book-

**Host** [10:02]: Mm. Mm

**Amy Brand** [10:02]: ... um, that really depresses, um, print sales. And so, you know, we've, we've had to kind of find our way to doing this because we believe it's the right thing to do, and we wanna suppor- support our authors who want their works to be openly available, but making it sustainable. Um, so-

**Host** [10:19]: That's cool that-

**Amy Brand** [10:20]: Yeah

**Host** [10:20]: ... that makes a lot of sense, and that explains why it says on deeplearningbook.org-

**Amy Brand** [10:24]: [laughs]

**Host** [10:24]: ... it says, you know, there's something like an FAQ at the bottom that's like, "Can I get a PDF version?" It's like, "No, you can't." [laughs]

**Amy Brand** [10:30]: Yeah.

**Host** [10:31]: Uh-

**Amy Brand** [10:31]: Well, you know, I-

**Host** [10:32]: 'Cause yeah

**Amy Brand** [10:33]: ... I'm in... Yeah. Um, I, I'd love, I'd love to be able... It's-- We aspire going forward to be able to figure out the model that does allow us to have that PDF.

**Host** [10:43]: Yeah.

**Amy Brand** [10:43]: We're still working on it, so.

**Host** [10:46]: No, I mean, in terms of a browsing experience on your computer anyway, I think HTML is better. Like, there's no point in having this idea that information should fit [laughs] into a, into a small box shape-

**Amy Brand** [10:59]: Yeah

**Host** [10:59]: ... uh, when you can scroll infinitely anyway. So, um-

**Amy Brand** [11:03]: Mm

**Host** [11:03]: ... I think that's great. So going beyond just MIT Press, what tools or technologies are needed to build public digital infrastructure, um, for open access publishing?

**Amy Brand** [11:18]: So that, that's a great question. Um, I think it would surprise a lot of people looking from the outside at the publishing industry and, and, and seeing all the digital publishing that's happening to know, um, you know, how consolidated the underlying platforms and technologies are. So in the university press world, for example, there are very few hosting platforms that we choose among. Um, and I can remember early on when I had gotten involved in the world of digital publishing, I, you know, I kept thinking like, "Wow, you know, I should go off and, and just build one of these digital hosting platforms," because there's so much demand, and you look at academic journal publishers, publishers, and they're literally hopping back and forth between two or three or maybe three or four choices of these, these platforms. A couple of which, by the way, are now owned by private equity, but that's another conversation. Um, you know, I, I believe very strongly that this is a space that needs more competition, that needs some open source solutions. Um, one of the things that, um, I've been really pleased to have been involved in over the last several years was helping launch an independent nonprofit called Knowledge Futures, um, which created, developed, and, and, and runs, uh, open source community publishing, um, technologies for a range of, of different groups. And the MIT Press does a lot of its open book publishing on PubPub. It's the PubPub platform that Knowledge Futures runs, um, several of our journals, like the Harvard Data Science Review. Um, and, but there are other universities, other presses, uh, even governments that, that, that use the platform.

**Host** [12:58]: Mm.

**Amy Brand** [12:58]: And the way that I think about it is, you know, this isn't about, um, you know, the way in which we do science publishing or data publishing is absolutely broken, so we have to destroy what we have and create something new. I, I think about it in terms of multiple levers of change and creating al- alternatives that work well, um, and that gradually kind of shift the wheel and the, and the balance of power. Um, and when I speak about the balance of power, I'm talking about the, the power that a l- a lot of these large commercial companies, both publishing companies and technology companies, have over the research publication space.

**Host** [13:33]: Cool. Very interesting, and amazing how many different organizations related to open source that you're involved with personally. So the MIT Press itself, in a way, you know, lots of open source involvement, the Creative Commons, and now also to hear about Knowledge Futures. Very cool. Um, so we have your thoughts, and clearly we know how important it is to have openness, uh, in books, in papers. Um, what are your thoughts also on making data and code available where possible?

**Amy Brand** [14:03]: Yeah. Um, you know, an- anybody that's, that's publishing research today thinks about, um, the products of the research process beyond just the textual, textual content. We're thinking also of what is the methodology and what were the protocols in the research, and how can that information be shared? What about the data? Um, and certainly what about the code? And, you know, what we all aspire to, um, is having all of this content, um, accessible in ideally standardized ways that, uh, protects people's privacy where it needs to be protected, um, protects the interests of, of, you know, researchers that for whatever reason might n- not be in a position to share their data, but that ultimately allows us to accelerate the pace of research and discovery, uh, by being able to compute over that data, you know, over that code, et cetera. So, um, you know, I feel very, very strongly about that. It's, it's an, it's a somewhat different conversation for a publisher like me though than it is for a university or a funding agency. Um, you know, I think early on when we became aware of the fact that if we publish a journal article, um, you know, say in neurochemistry, and we feel like it's the best policy to make the related data available, it's not necessarily that, that we are publishing the data. Um, we are essentially enforcing a policies that says, "You know, for this journal, you have to make your data available, but you're gonna make it available through your university or potentially through, um, you know, your funding partner or on some other platform or repository."

**Host** [15:44]: Mm-hmm.

**Amy Brand** [15:44]: So this is a, this is a much bigger for... You know, as I see it, this is a, um, this is a, an issue of, of governments, you know, and in the US certainly at the federal level to come up with that solution. What is, what is going to be our data commons, um, to accelerate research? And if you think about the global situation right now and, you know, the, the, the position that the US is in with respect to its preeminence in research now as opposed to several years ago, the ability to, um, capture, preserve, share, and ultimately mine research data is, is a big-

**Host** [16:19]: Right

**Amy Brand** [16:19]: ... part of what we wanna see going forward.

**Host** [16:21]: Right, right, right. That makes sense. [upbeat music] Struggling with broken pipelines, stale dashboards, missing data? You're not alone. Look no further than Monte Carlo, the leading end-to-end data observability platform. In the same way that New Relic and Datadog ensure reliable software and keep application downtime at bay, Monte Carlo solves the costly problem of data downtime. As detailed in episode number 499 with the firm's brilliant CEO, Bar Moses, Monte Carlo monitors and alerts for data issues across your data warehouses, lakes, ETL, and business intelligence, reducing data incidents by 90% or more. Start trusting your data with Monte Carlo today. Visit www.montecarłodata.com to learn more. Um, so it's super cool to me how this kind of openness, and yes, you know, we do need to have considerations probably just beyond... Yeah, there, there are more complications, uh, if-

**Amy Brand** [17:29]: Yeah

**Host** [17:29]: ... just geopolitical complications around, uh, how much things can be shared. But generally speaking, um, geopolitical situations notwithstanding, the availability of papers, books, data, code, uh, the more people that have access to it, the more brains there are involved in solving problems that can have a huge impact on society. So every single person in the world, every single person listening to this podcast in particular, um, has the capacity to make an enormous impact with what they do with their lives. And the more information that you have access to, whether for reading or for feeding into your models, the bigger your impact can be. It's, uh- I mean, it's taking the long view of decades or centuries. We live at a time today where there's... where a lot of people in the world, certainly not everyone in the world, but a lot of people in the world for the first time in history don't have to worry about whether they're going to have enough to eat, and don't have to worry about, uh, being murdered in a war. It's, you know, there's obviously exceptions [laughs]

**Amy Brand** [18:42]: Mm-hmm

**Host** [18:42]: ... uh, at this time that we're recording. We- there's- are particularly salient exceptions. But-

**Amy Brand** [18:46]: Mm-hmm

**Host** [18:46]: ... uh, generally speaking, we enjoy this, this abundance that would've been unimaginable, um, two generations ago, three generations ago even. Um, and yeah, science progress has facilitated this, and I- I'm kind of reiterating the point now, but, uh, the, the more brains that are- that have access to information-

**Amy Brand** [19:10]: Brains, brains and machines, right?

**Host** [19:12]: Yeah.

**Amy Brand** [19:12]: It's brains and machines.

**Host** [19:12]: Yeah. Right, right, right.

**Amy Brand** [19:14]: Yeah. Go ahead.

**Host** [19:14]: That is a... Yeah.

**Amy Brand** [19:15]: [laughs]

**Host** [19:16]: I a- I agree [laughs] 100%.

**Amy Brand** [19:18]: Yeah.

**Host** [19:18]: But, uh, but on the point of brains, there's... We wanna make sure that all of the brains have-

**Amy Brand** [19:23]: Yeah

**Host** [19:24]: ... the opportunity to participate. So-

**Amy Brand** [19:26]: That is correct

**Host** [19:28]: ... um, so science and engineering historically, um, women and minorities are underrepresented in, in these fields. Um, so we call- we can call them the STEM fields, science, technology, engineering, and math, STEM. Um, you know, there's this underrepresentation issue where we are not... So even if we lived in this world where there weren't geopolitical issues, and we didn't, we w- didn't worry about particular information getting into particular people's hands, we could have all of this data, all of this information be open access. But if we have this, um, this inequity, we're still not making the most of it, um, because yeah-

**Amy Brand** [20:09]: That's absolutely right

**Host** [20:09]: ... we're not getting everyone involved.

**Amy Brand** [20:11]: Yeah. I, I agree wholeheartedly. You know, I, I, I think about it in terms of that brain power. I think about, you know, think of what's lost when you, you know, don't have a whole participation, you know, of a population in solving certain problems. Um, and so this is an issue now certainly in research, you know, the, the ability of people in the Global South to participate in research, and the way in which how we publish, and I, you know, as a publisher think about this, uh, impacts that. It's not just the access to content. It, it... Who, who... You know, what is authorship, and who has the right to participate as an author? Um, what are the barriers to that? Uh, this is-

**Host** [20:51]: Mm

**Amy Brand** [20:52]: ... a big issue right now, um, in open access models, and I'd, I'd love to come back to, to that if you wanna talk more about it. I think where you were going was, was, uh, um, you know, around our interest at the press in publishing, um, as many diverse, marginalized, uh, voice- voices that, um, previously have been underrepresented, and how that even changes, you know, how we think about the definition of what science is. Um, you know, we... We're, we're soon gonna be launching a series, um, called Epistemologies of, of the Global South, which I'm very excited about. Uh, but, you know, my own... Because of my own personal experience as a woman in science, I'd been a grad student at MIT. I was in academia for a while, and then I left to, to go into publishing. Um, you know, I, I felt like it wasn't a level playing field for, for men and women at all, and when I decided to come back to MIT in this, in this role as director of the press, you know, one of the things I, I really wanted to do was to use that privileged position, um, to provide opportunities for, uh, you know, women to publish, uh, about their, their STEM work, um, to, to create a platform, um, for, um, you know, books that would inspire, uh, kids, and especially young women and young girls into careers in, in, uh, science and technology. We've, we've gone, you know, fully in that direction now, both in books that we're publishing at the M- MIT Press and in partnership with a, with a children's publisher as well. Um, and it did lead to my, um, thinking of, or essentially conceiving of this, this film called Picture a Scientist. Um, and-

**Host** [22:35]: Yes.

**Amy Brand** [22:36]: Yeah. And, and through that, I really wanted to, um, you know, to pay homage to these women that I, that I had known, some of whom I had known when I was a grad student, um, at MIT in the '80s, uh, and that I had heard about, you know, through the years of having essentially gotten the, uh, president of MIT to admit in 1999, which seems like it's not too long ago, uh, that, that women were, were being discriminated against, uh, in the resources they had access to, how they were being compensated, in the opportunities, you know, that they had access to, um, the size of their labs. And that was a real turning point in academia. Yeah.

**Host** [23:16]: All right. So Amy, you've talked about, uh, how MIT Press is involved in publishing not only books by, uh, women and minorities in STEM fields, but also about them, and being a leader in that area. And then you also mentioned, uh, this film, Picture a Scientist, which is kind of related to that. So, um, not only is your work as director at MIT Press, um, helping to, uh, create content for, about, by, uh, historically underrepresented books in STEM fields, but on top of that, you've been executive producer of this amazing film, Picture a Scientist. So I haven't finished it yet, but I've started it. I'm about halfway through, and it is completely absorbing. It is no surprise that it was selected for a 2020, uh, Tribeca Film Festival, um, appearance. [laughs]

**Amy Brand** [24:13]: Premiere.

**Host** [24:13]: Uh-

**Amy Brand** [24:14]: Yeah

**Host** [24:14]: ... premiere is the right word.

**Amy Brand** [24:16]: [laughs]

**Host** [24:16]: I don't know the lingo. Um-

**Amy Brand** [24:19]: It was so sad

**Host** [24:20]: And yeah, it's available

**Amy Brand** [24:20]: It was right, right before the pandemic. We were all set to go, and then, you know, then it didn't happen, but it was selected. [laughs]

**Host** [24:29]: Ah.

**Amy Brand** [24:30]: So, yeah. It's sad but it's like-

**Host** [24:30]: Right in my neighborhood here.

**Amy Brand** [24:31]: Yeah. Okay.

**Host** [24:32]: I'm basically in Tribeca here.

**Amy Brand** [24:34]: Oh.

**Host** [24:34]: And, uh, yeah. I, I'm a little bit south of Tribeca, uh-

**Amy Brand** [24:39]: Cool

**Host** [24:39]: ... in the Financial District of Manhattan, but, uh, yeah. I, yeah, it is... Th- the, the pandemic ruined a lot of things, including, yeah, being able to...

**Amy Brand** [24:46]: Yeah.

**Host** [24:46]: And was it, like, a virtual premiere or something like that?

**Amy Brand** [24:49]: Um, there were some... I think there were some virtual screenings, you know, but, uh... And, and of course, it was still an honor to have been selected, but certainly the, the pandemic changed the whole course of, of how that film was seen by the world. But in some ways, you know, for the better because there were so many screenings on campus and so many good conversations with people, so.

**Host** [25:09]: Right. Yeah, and it's available around the world on Netflix. It's about 100 minutes long, but if you don't have access to Netflix, there's even a 13-minute version called The Uprising that is, um, kind of key excerpts of it, and that's available for free on the MIT YouTube channel. So, um, Amy, h- how did you get inspired to make this film? I guess you kind of... You've, you talked about already how, you know, you were exposed to these stories, you know, being at MIT, um, this big change in 1999 around, uh, the president of the university having to acknowledge that women have smaller labs than men on average, uh, and significantly smaller on average. Um, but, you know, having that idea [laughs] thinking, "Hey, I, you know, I, I'm aware of these stories," and, um, you know, I might have thought... If I was running a publishing company, I might have thought, "I need to make a book about this." But you made a film about it, so, uh, how did that end up happening?

**Amy Brand** [26:15]: Uh, yeah, happy to talk about that. Um, when I was, um... I, I will say when I was a grad student at MIT in the '80s, it was really hard to find a woman's bathroom almost anywhere that you went, and this was, you know, a constant source of griping. But, um-

**Host** [26:29]: Hmm

**Amy Brand** [26:30]: ... I, you know, I became aware of the fact, um, I guess it was about four or five years ago, through the MIT libraries and the archives, that there was an effort to collect the papers of, uh, many, um, incredibly eminent women at MIT who had been, in the '90s, the, I think something like the only 16 or 17 tenured women on the, on the, um, faculty of science at MIT. Just a very, very small number. I had known some of them when I was a grad student at MIT. Um, and the archivist at the library said, you know, "Maybe you wanna do a book about this." Uh, and so I agreed to meet-

**Host** [27:09]: Hmm

**Amy Brand** [27:09]: ... with all the women. I, I remember that, that meeting-

**Host** [27:13]: Oh, wow

**Amy Brand** [27:13]: ... clearly to this day. Um, and it was in the course of that conversation that we, we thought, "Well, it would be a lot easier for, for everybody if we just, um, did, like we're doing now, you know, film audio interviews of everyone to capture their story, and we'll build the book from there." And we were-

**Host** [27:35]: Hmm

**Amy Brand** [27:35]: ... very quickly able to, um, obtain funding for this project to, uh, collect all this footage. The American Academy of Arts and Sciences in Cambridge, uh, loaned us this incredible space to bring all the women together. Um, friends of mine who are closer to the, the film industry connected me to two incredible, uh, directors who take most of the credit for the ultimate film that you see, Sharon Shattuck and Ian Cheney. Um, but I, you know, I h- essentially hired them to come in and, and do these interviews. We got about 30 hours of interview footage with, uh, just, you know, an incredible group. I think almost everyone who had been... who was still alive, who had, uh, you know, been part of this, uh, movement at MIT in the '90s that led to the report on the status of women on the faculty of science at MIT and led to then President Chuck Vest saying, and it being covered in The New York Times, uh, you know, that women were being discriminated against at MIT. All, all those people, you know, came back. Um, and because the footage we captured was so remarkable and, you know, there was just-

**Host** [28:42]: Mm-hmm

**Amy Brand** [28:42]: ... great, I would say, kind of synergy with the filmmakers, um, we realized that we had not only a, a book, um, project, but we, we also-

**Host** [28:51]: Ah

**Amy Brand** [28:51]: ... had the potential for a documentary film. And-

**Host** [28:56]: Mm-hmm

**Amy Brand** [28:56]: ... um, Ian and Sharon, you know, had... I, I was, as executive producer, my main function was, uh, to, um, help raise money, which I did, um, you know, for, for the film, um, while they sort of shaped the broader story that went out beyond MIT to bring in, um, a couple of other just am- uh, amazing women and their stories from other universities. Uh, so, so that's, that's really how it came about. And, and the, the book, um, we did... The book is happening, but it's, it's not happening at the MIT Press. It's happening, uh, you know, elsewhere, but I'm so excited about it. A number of other book projects resulted from this as well. We just put out, um, a book called Carbon Queen, uh, which is a, a biography of, uh, Millie Dresselhaus, who, uh, was, was among the, what we call the MIT 16, these remarkable women. Uh, and it's the story of her career at MIT. Um, so.

**Host** [29:57]: So incredible to hear that story, and having watched half the film-

**Amy Brand** [30:00]: Mm-hmm

**Host** [30:01]: ... I can confirm that there are stunning, um, uh, emotionally moving interviews. Everybody presents... I- in everything I've seen so far, everybody presents what happened to them so articulately, um- And so clearly you can see, you can, you can almost experience alongside them, uh, yeah, the, the unpleasantness or the, the unfairness, the unjustness of, of historically and probably still today a lot of people experience. Um, in fact, I know even from those interviews, definitely still today, um, that it, it sounds like e- especially, um, you know, if you add multiple of these minorities together, so if you're not just a woman or not just Black, that if you're a Black woman, then, you know, it's, it's still today the... At conferences, at university, in meetings, it sounds like there's lots of small ways that you are made to feel like you are not part of the community, that you're not, say, a scientist or an engineer.

**Amy Brand** [31:18]: Mm.

**Host** [31:19]: Um, and yeah, so hearing... Yeah, hearing these stories presented so clearly, so articulately, um, yeah, it really... Yeah, it's, it's been a moving experience for me, and I can't wait to finish watching the film. [upbeat music] Einblick is a faster and more collaborative way to explore your data and build models. It was developed at MIT and showed to reduce time to insight by 30 to 50%. Einblick is based on a novel progressive engine, so no matter the data size, your analysis won't slow down. And Einblick's novel interface supports the seamless combination of no-code operations with Python code. This makes Einblick the go-to data science platform for the entire organization. Sign up for free today at einblick.ai. That's E-I-N-B-L-I-C-K.A-I. E-I-N-B-L-I-C-K.A-I.

**Amy Brand** [32:13]: Well, thank you. Yeah, I do, I do think of it as that, that metaphor of, like, death by a thousand cuts, right? That, you know, through, through the course of whether you're in the Silicon Valley company or you're in, you know, a science department at Harvard or MIT or elsewhere, um, you know, the day-to-day experiences of, of not being included or not being listened to or, or not being taken seriously, and, um, it, it does continue. Uh, and a- addressing those concerns requires just ongoing vigilance, um, you know, on the part of people who are in a position to make decisions about an individual's career growth. Uh, and that, that, you know, in, in the period of time when I, when I wasn't at MIT, um, in my professional career, I spent some of that time working at Harvard, uh, in the Provost office, specifically on these issues, on, on, uh, faculty diversity-

**Host** [33:12]: Mm

**Amy Brand** [33:12]: ... and, and equity and career paths for faculty.

**Host** [33:16]: Mm-hmm, mm-hmm. Yeah, so building on what you're saying there, I, I do really encourage people to watch this film, uh, to get a sense of this in more detail, but an analogy that, um, that the film keeps coming back to is this idea of an iceberg-

**Amy Brand** [33:29]: Yes

**Host** [33:29]: ... where, um, above the surface there are really kind of blatant sexual harassment types of behaviors where, like, like actual, like, groping or, or, you know, sexual comments, that kind of thing. These are the kinds of things that it's like obvious sexual harassment, but that's, like, the tip of the iceberg. It's a small amount of the issues that, um, underrepresented people face in STEM fields. It's really what's under the water that has by far the biggest impact. What you just described is, like, the, the death by a thousand cuts, where it's being left off of an email chain or your opinion not being listened to in a meeting where that same opinion expressed by a white man is listened to. Um, and so it's the accumulation of all of these kinds of things that, um, you know, s- it sounds like certainly was a bigger issue at MIT in the '90s, but no question, um, still happens today, as you say, uh, in academia as well as in, uh, big tech companies. Um, these kinds of, um, I don't wanna say smaller, uh, but, like, more subtle, um-

**Amy Brand** [34:43]: Mm-hmm

**Host** [34:44]: ... yeah, more, more subtle behaviors, uh, in a way that, um, maybe to the person who's, who's saying them or doing them, you, you might not even be aware that it's having an impact. And I guess it's kind of that lack of awareness that hopefully films like this, um, can, can bring up that, you know, you... If you are a white man, you could be going around doing and saying things that are having a big impact on people without you realizing it. So, um, beyond just the impact or the, the content of this film, I'd also love to learn a little bit about, um, what it was like making it. So you've alluded to this a little bit, but what does it mean to be the executive producer of a film? What is that like? Y- you know, you've talked about getting the film kind of off the ground, but then once you've had these interviews, you've got the footage, you've realized, "Let's make this a movie," what happens next?

**Amy Brand** [35:38]: Um, yeah. So I, I came into this knowing absolutely nothing about making films, and I would not have known a few years ago what being an executive producer was either. So it, it, um, you know, it came out of my interest in, in realizing that we could do this because I had fabulous creative partners and wanting to help make it happen, being in a position to, um, help raise the funds to, to make the film happen. And I think it wasn't until it actually came to kind of signing agreements with the production company that, that Ian and Sharon were running to make this movie, that executive producer was qualified as an individual who, you know, raises a certain amount of money or raises the majority of, of funding for the film. Um, I think sometimes executive producers are, are more involved in the creative process. I was very much involved at the outset, and have more of a, kind of a stamp on the film, the short fil- film that you mentioned, The Uprising, and then later Ian and Sharon, um, went off to realize, you know, their creative vision in Picture a Scientist. And, uh, you know, I was in the-

**Host** [36:51]: Oh, yeah

**Amy Brand** [36:51]: ... I was in the background saying, uh, you know, "I'm gonna raise money to make this happen for you. Uh, you know, please consult with me. I wanna make sure that, you know, I still love what you're doing," but it, but it was really their creative vision. And I'm-

**Host** [37:05]: Wow

**Amy Brand** [37:05]: ... I'm doing this again in an entirely different area. I've, um, met this wonderful... I was living in Vermont during the pandemic, and I met a wonderful young filmmaker, uh, who's making a film actually about design build architecture in Vermont, which I'm also very passionate about, and I, um-

**Host** [37:22]: Hmm

**Amy Brand** [37:22]: ... have committed to, uh, executive produce another, another film in an entirely different area-

**Host** [37:27]: Oh, cool

**Amy Brand** [37:27]: ... because part of it is I, I just really, I love working with young people. I love helping them see their interests and their passions come to fruition, so.

**Host** [37:39]: Amazing. Well, I look forward to checking that out as well. Given how, uh, wonderful this film is, I'm sure that that will be a success as well. And then you also, uh, corrected me on something there. Um, I didn't know that The Uprising came before Picture a Scientist, so the short 13-minute film that's available on the MIT YouTube channel, that came first. I had this impression, not having watched that shorter film, that it was kind of like excerpts, like cut together-

**Amy Brand** [38:05]: Well, they were de-

**Host** [38:06]: ... to make-

**Amy Brand** [38:06]: They were developed at the same time-

**Host** [38:08]: Oh, okay

**Amy Brand** [38:08]: ... where we, we had a, um, we had an agreement that there would be a short film that was just about the MIT story where, uh, you know, the... Actually, not just me, but it was, it was effectively sponsored by the MIT Press, which is unusual for a press to do, and that the longer film, um, that was being made would be financially... Even though I was raising money for it, was financially handled outside of MIT. Um-

**Host** [38:39]: Got it, got it, got it

**Amy Brand** [38:40]: ... so they're, they're... It's confusing. They're overlapping in many ways.

**Host** [38:44]: Right, right, so they're two separate projects, but using some of the same media and-

**Amy Brand** [38:49]: Exactly

**Host** [38:50]: ... conveying the same idea. Yeah, yeah.

**Amy Brand** [38:51]: Yeah.

**Host** [38:52]: Um, cool. Well, so a prominent, uh, issue in the film, which we've already talked about, is how, um... Well, what culminates in 1999 in the president of MIT having to acknowledge that women, on average, have significantly smaller, uh, lab spaces than, than their equivalent male peers, um, equivalent at least in terms of, um, a title, um, like assistant professor, professor, that kind of thing. And so, uh, the film discusses the lead-up to that a fair bit. Um, and so you were at MIT School of Science at that same timeframe. Um, you mentioned how coming across-

**Amy Brand** [39:35]: Hmm

**Host** [39:35]: ... women's bathrooms, for example-

**Amy Brand** [39:36]: Mm-hmm

**Host** [39:36]: ... can be something that's hard to do. Are there other things that you experienced while you were there?

**Amy Brand** [39:41]: Um, yeah, and I, I think it was more, you know, along the sort of subtle lines, I mean, being very, you know, aware-

**Host** [39:48]: Right

**Amy Brand** [39:48]: ... of the fact that women were, uh, in a minority. Um, there were certainly some fabulous female mentors at MIT, but you know, if you, if you're coming into a field and you see that you are not as well represented as men, it, whether consciously, unconscious, or unconsciously, um, you know, makes you question your career choices. Um-

**Host** [40:13]: Mm-hmm

**Amy Brand** [40:13]: ... I, I remember, uh, you know, thinking that, um, the, the women that I knew in, in, you know, the field that I was, uh, working in, um, it seemed to me that they were, they were working so much harder. You know? I remember thinking that, that-

**Host** [40:31]: Hmm

**Amy Brand** [40:31]: ... that this... It, it, it just doesn't feel like a level playing field. Um-

**Host** [40:36]: Right

**Amy Brand** [40:37]: ... and I, I often feel that way today. I mean, I sometimes tell people [chuckles] the story, like, okay, so I'm, I'm running this publishing company. I had the experience, um, about four or five years ago of having to, uh, lay someone off, and, uh, and this was a white male. Um, and I, and I had very good reasons for l- for, for letting him go, and I, and I'm his boss, right? And I go to lay him off, and he looks at me, and he says, "That is not acceptable." Like-

**Host** [41:06]: Wow

**Amy Brand** [41:06]: ... actually, it is totally ac- And that, you know, that's an everyday thing, and it just was such a, like a wake-up call to me [chuckles] because I thought, you know, your worldview about your privilege and what is due to you versus, you know, um, just a woman walking through the world, it's... So, and, and I know, you know, that the same issues come up in, in all kinds of, of industries. I do think that there is, um, something about, you know, academic science, and the way in which, um, we judge excellence, and the way in which careers progress, where it's a particularly sticky problem, where there's a lot of entrenched bias. And part of my interest in this relates to my work in the field of publishing because I look at, you know, what is, what is that record of production in science, and, and how is, how is excellence being assessed, right? And often it leads to, you know, many more opportunities to exclude or marginalize women and, and, and other groups. Um, all of... It's almost like all of the underlying social dynamics get amplified and, and exacerbated through the systems that we use to do r- research, you know, create new knowledge, publish it, judge it. Uh, yeah.

**Host** [42:25]: Yeah, something that I think can make that issue particularly salient in academia, um, and this is mentioned in the film, Picture a Scientist, which is why it's top of mind for me- ... is that there are these dependency structures embedded in it. So when you're doing your PhD, you typically have one PhD supervisor. And so if you're a young female PhD student, and you have an older male PhD supervisor who has all of this power over you, it can create, uh... If, if that person wants to abuse that power, they're in a position where it- it's easier to do so. Um, and so yeah, so that was something about academia in particular that, um, that was brought up there.

**Amy Brand** [43:15]: Exactly.

**Host** [43:16]: And kind of you're dependent on this person. If you want to then, you know, get a postdoc, you're gonna need this person's letter of reference. Um-

**Amy Brand** [43:24]: Uh-huh

**Host** [43:25]: ... but actually, now that I'm saying that out loud, almost every work relationship is like that, where you're dependent on one person. [laughs] Like-

**Amy Brand** [43:31]: But the, the-

**Host** [43:31]: ... that kind of power dynamic, yeah.

**Amy Brand** [43:33]: Yeah. I mean, yes. I mean, you, you wanna make sure whether you're, you know, in school, in class with your professors, or in any job that you do that you're thinking about, you know, how do I make sure that I'm protecting these relationships, I get the best letter of reference that I can, but it, it does play out differently in a- academia because of the networks. I mean, we tend to think about, okay, you're in the discipline of biology or computer science, but think about all the sub-disciplines within that and how small these communities are, and these people-

**Host** [44:03]: Right

**Amy Brand** [44:03]: ... you know, they know one another. They might have-

**Host** [44:06]: Right

**Amy Brand** [44:06]: ... you know, the leaders might have gone to school together. Um, it, it, it does tend to be, you know, to lend itself more to a certain type of cronyism.

**Host** [44:16]: Right, right, right. That makes a lot of sense. Um, and yeah, to your point about how it can seem like, say, the women are needing to work a lot harder to be at the same, uh, position, um, in academia as a man, um, there was an interesting part of an interview in the part of, uh, Picture a Scientist that I've watched so far, where, um, a woman of color talks about how she ends up investing so much time in every email, making sure that she's getting the tone right, because-

**Amy Brand** [44:52]: Mm

**Host** [44:52]: ... there's a perception of, like, there can be stereotypes against her of like, you know, being quick to be angry or something. And so she has to put all this extra care, and she's like, "What if I add up all of that extra time spent trying to really articulate clearly in an email to make sure that I'm striking the right balance?" As opposed to, you know, maybe me as a white man, I can just say how I'm feeling, and I'm not gonna encounter the same kind of, um, resistance or, or backlash. Um, and so yeah, so, so that is... That was an interesting example to me, um, a specific example of how it can end up being the case that somebody in an underrepresented group can end up having to invest so much more time in getting the same outcome.

**Amy Brand** [45:37]: Yeah. That, that was, um, the chemist, Rachel Burks, and it's also, for me, one of the most salient stories in the film about the amount of time that she invests and how that's time away from doing the science that, that she wants to do.

**Host** [45:51]: Mm-hmm.

**Amy Brand** [45:52]: And, and that comes through, you know, in, in Nancy Hopkins' story as well. You know, she... There's this, this moment, you know, in the film where she says, "I didn't... You know, I didn't wanna be an activist, and all of a sudden, I realized that this-"

**Host** [46:03]: Right

**Amy Brand** [46:04]: ..."this is what I had to do." And, and to this day, you know, she's become a good friend. Um, she talks about, you know, the, that her investing in telling the story and, and effecting this change through, you know, collective social action took away from her science. And, and, you know, she's-

**Host** [46:22]: No doubt

**Amy Brand** [46:23]: ... happy about the impact she's had on the world, but it's, it's painful for her. Yeah.

**Host** [46:29]: Yep. Um, so what can we do to change STEM so that it's more welcoming to everyone?

**Amy Brand** [46:39]: You know, it starts, it starts at the beginning, I always think, in terms of pipeline. So in terms of education, it is, you know, how do you expose, uh, young kids, um, you know, of all ethnicities and, and genders, um, around the world to, to STEM careers in a way that makes them attractive and accessible. Um, you know, certainly in the workplace, in my workplace, uh, in publishing is a very white, un-diverse industry. We're constantly focusing on how do we attract people into publishing. But in, in, um, you know, we've been working at the press, um, on this issue of making STEM recognizable to kids at a young age through new children's publishing efforts that we're doing. Uh, we started a partnership with, uh, the wonderful Candlewick Press, which is one of the leading children's publishers, uh, in the country, and they happen to be located in Somerville, not far from us, with two new imprints, um, MIT Press Kids and MITeens, um, that are focused, I, I would say not just on STEM, I'd say STEAM, um, fields, so bringing in the arts as well. Um, but at the MIT Press itself, we had started publishing graphic novels for adults, you know, a few years ago and have now started to do-

**Host** [48:03]: Oh

**Amy Brand** [48:03]: ... um, you know, graphic novels for young adults. Uh, one of them that was, that, that I, I love that came out, I want to say it was, I think it was, yes, it was last year, um, or earlier this year, is called The Curie Society, and it's, uh, adventure stories, um, illustrated in kind of comic book style of young women solving complex scientific problems, um, and has been-

**Host** [48:29]: Named after Marie Curie?

**Amy Brand** [48:31]: Mm, named after Marie Curie. And next month, we actually have a, a book coming out called Power On, which is intended to make, um, tells- You know, stories of, of coding, uh, for kids that show how empowering it is to be able to actually do computer programming and code. And it represents-

**Host** [48:51]: Wow

**Amy Brand** [48:51]: ... in the books through the illustrations just like a d- very diverse population of kids, and we're really, really excited about that one as well. Um, so, you know, 'cause we, we... in some of the normal adult publishing we were doing, whether it was, you know, graphic novel treatments of complex topics. We had one on the history of feminism not too long ago, and then we had another one on-

**Host** [49:12]: Wow

**Amy Brand** [49:13]: ... the origins of the universe by the wonderful, uh, Clifford Johnson at USC. Um, you know, there... We were realizing that there was a young adult audience for these books, and also for some of our essential knowledge books, which are very short introductions to topics and, uh, started out in science and technology and, uh, and now it's across the range of fields that we publish in. Uh, we realized that, you know, this was just a natural direction for us to go in. Um, but we also realized that we, we could do, you know, some of these books for young adults, but when it came to publishing, truly publishing well for young children, um, that went beyond, you know, our capabilities and our area of expertise and, and from that came the decision to partner with Candlewick.

**Host** [49:57]: Wow, that's so cool. So I personally love-

**Amy Brand** [50:02]: Yeah

**Host** [50:02]: ... graphic novels of complex topics. So some particular ones that have impacted me, uh, in recent years is a book called Logicomix, which-

**Amy Brand** [50:11]: Yes

**Host** [50:11]: ... is about, um, Bertrand Russell and-

**Amy Brand** [50:14]: Mm

**Host** [50:14]: ... logic. [laughs]

**Amy Brand** [50:16]: Yeah.

**Host** [50:16]: Uh, and so it's called Lo- yeah. So I, yeah, I learned a ton about philosophy and his really interesting biographical history, both as an academic as well as an anti-war activist. Um, so that was really cool. It sounds like you're very familiar with it. Um, and then also-

**Amy Brand** [50:35]: Yeah

**Host** [50:35]: ... uh, Yuval No- Yuval Noah Harari, uh-

**Amy Brand** [50:38]: Yeah

**Host** [50:38]: ... is my favorite nonfiction author today. I absolutely love his book Sapiens, and now they're releasing it-

**Amy Brand** [50:44]: Yeah

**Host** [50:44]: ... as graphic novels as well.

**Amy Brand** [50:46]: I d-

**Host** [50:46]: There's a first volume that's out now

**Amy Brand** [50:46]: I actually didn't know that. I, I love Sapiens too. I didn't know it was coming out as graphic novels. That's very cool.

**Host** [50:52]: Yeah. There's a-

**Amy Brand** [50:53]: Neat

**Host** [50:53]: ... there's a first volume, um, for sure that's out now at the time of recording. And, uh-

**Amy Brand** [50:58]: That's neat

**Host** [50:58]: ... it is, it's very well done. And it... I, I could see how that can be appealing to young adults. Um, the, the Sapiens one in particular, I think it seems to me like there's elements of it that they're trying to make it a bit more appealing to that younger audience. Um, but Logicomix is, that is an adult book. Uh, and I just, I just enjoy it. It's like a nice... You know, we have to spend so much of our day feeling like we're being serious and reading, you know-

**Amy Brand** [51:24]: Yeah

**Host** [51:24]: ... rigorous things, and so it's really nice to be able to relax, and I'm quite a visual person. I created a book called Deep Learning Illustrated.

**Amy Brand** [51:31]: Yeah. Yeah.

**Host** [51:32]: Um, I like visual approaches to conveying information and, um, yeah, so I, I love that those graphic novels exist. I can't wait to check out what MIT Press is releasing, 'cause I didn't know you were doing that until now.

**Amy Brand** [51:44]: Yeah.

**Host** [51:45]: And then going a step further, I love that you have this MIT Press Kids that you're, uh, you know, working with Candle- uh, Candlewick on.

**Amy Brand** [51:53]: Candlewick. Yeah. We also have, um, Can- we have in our MIT Press bookstore, which is, uh, you know, it was closed for some time during the pandemic and just reopened within, um, the MIT Museum here in Cambridge, a large children's section now, um, which is, is, is just fabulous, and it has not only our books, but books of other publishers that are intended to inspire young kids, all the way down to those like really little chunky books that you give to nine-months-old, you know, children, um, into these topics.

**Host** [52:28]: Wow. Cool. And so we got onto talking about this topic-

**Amy Brand** [52:32]: Yeah

**Host** [52:33]: ... because we were talking about how we can help change, uh, STEM so that it's more welcoming to everyone. And so [laughs] for listeners that have forgotten, like that's how we got n- that we got here.

**Amy Brand** [52:44]: Yeah.

**Host** [52:44]: Um, yeah, such an incredible example.

**Amy Brand** [52:47]: I guess it's sort of too easy to talk about, oh, you know, we have these big problems in the world, but look, look at the world. We do. It's a world literally on fire, and we need all the brain power and compute power, uh, to, to be solving these big problems in the world. Um-

**Host** [53:03]: For sure

**Amy Brand** [53:03]: ... and part of, you know... And so certainly when it comes to data science, that's the work of, of a lot of the listeners to this podcast. But in my world, I think about it, you know, in terms of how, how do you shorten the path from, you know, idea and discovery to impact on the world? How do you broaden participation in, um, in research so that we can bring all that brain capacity around the world, starting at a young age, uh, to bear on these issues? Um, you know, fortunately, as a publisher who has to sustain and, and run a business, there's just been ex- an explosion of, of growth, um, in, in interest in, in these topics as well. So-

**Host** [53:43]: Wonderful

**Amy Brand** [53:44]: ... you know, when I came back to the press, um, almost seven years ago, uh, we had a very large and successful, and have for many years, publishing program, um, for general readers in art and architecture and design, uh, much less so in STEM topics. And, and now, you know, publishing books for, uh, we like to call them books that honor the complexity of their subject matter, but they are books also for the general reader. Um, just, you know, very, very successful, and it, and, and it feels like it's an opportunity for us as a publisher to actually have, you know, an influence on public policy. I mean, that's the way I think about it.

**Host** [54:24]: So cool. Yeah. So now that I know that MIT Press is doing all this, it sounds like for me, finding gifts for people, which is perennially a big issue for me, now all of a sudden, no matter whether they're nine months old or 90 years old-

**Amy Brand** [54:39]: Yeah

**Host** [54:39]: ... I'm gonna be able to find a great, super interesting book about a topic that I'm passionate about that could also, um, help open horizons Um, or perceptions of young people, old people, to, uh, the impact they could be making in the world with science and technology, um, and engineering.

**Amy Brand** [54:58]: And you can be-

**Host** [54:59]: Very cool

**Amy Brand** [54:59]: ... be sure if the, you know, sure if it's a book coming from the Press, it's, it's gonna be beautifully designed and often beautifully illustrated and packaged, but this isn't an advertisement, so... [laughs]

**Host** [55:11]: [laughs] No, it's true. Yeah. There's been no sponsorship by MIT Press or any of this-

**Amy Brand** [55:16]: [laughs] No

**Host** [55:16]: ... uh, yeah, anything. This is entirely, uh, yeah, my, uh, personal opinions and, uh-

**Amy Brand** [55:23]: Mm

**Host** [55:23]: ... that are, that are being reflected here. Cool, Amy. So we've talked about how things like the MIT Press Kids can be helpful for, um, opening people's, uh, opening young people's eyes to, uh, to opportunities in science and engineering, even if they come from, um, historically underrepresented STEM backgrounds. Um, but, um, going back to an earlier conversation in the conversation, we also talked about how open source can itself be a driver of, um, of more equality because we have, uh, yeah, more minds that can be involved. Uh-

**Amy Brand** [56:04]: Mm

**Host** [56:04]: ... there's fewer barriers to entry. And so with that in mind, and given your rich, rich expertise in open source, what do you think is the best open source model going forward?

**Amy Brand** [56:19]: Um, great question. It's something I think a lot about. You know, what we're trying to do at the MIT Press is create open access models that don't perpetuate bias, either in terms of access to the content, but also in terms of ability to participate as an author. Uh-

**Host** [56:36]: Mm

**Amy Brand** [56:36]: ... part of what's happened over the course of the whole open access movement, and it's a movement that, um, has a lot of very, very driven advocates, uh, behind it, um, is that we've, we've reached a place right now in academic publishing where most of the open access that's happening is happening through pay-to-publish models. Uh, so when we talk about an open access journal, typically what's happening is the author is being asked, or they're getting money from their university or, or their grant funder to, uh, pay a publisher to, in exchange for making that work openly available. Um, okay, so the work ends up open access, but you've created a whole host of other inequities in terms of who's able to participate. Inequities across fields, because some fields have more grant funding across institutions, 'cause c- some universities will have those resources. Uh, and certainly across geographic regions, um, in, in the world. And you know-

**Host** [57:32]: Mm-hmm

**Amy Brand** [57:32]: ... I, I love this particular example because it's a, it's a great example of what happens when we kind of reduce ourself to simplistic binary thinking. Uh, you know, open is good and closed is bad, so open at all costs. And in fact, the, the, the issues here are very, very, uh, complex, and you need to think about, uh, models that, um, you know, don't essentially fall prey to this kind of unintended consequence, and that's what we've been trying to do at the MIT Press. So for example, our open book model, which we launched this year, is an, a collective institutional subsidy model, which means that if we reach a threshold of institutional support, then we just open up all the books that we publish in a particular season, which we did for our scholarly monographs this year.

**Host** [58:27]: Oh, wow.

**Amy Brand** [58:28]: And you know, um, we're not requesting that individual authors pay for that, for that privilege. Uh, and so that's an example of the kind of model that I'd, I'd really like to see more of. And those of us, um, who work on open access and open data, you know, we're trying to come up with ways of, uh, funding and subsidizing the whole ecosystem to, to, to make open possible.

**Host** [58:55]: Really innovative. I hadn't heard of models like that before, and I had not thought of the issues inherent in the prevailing open source model today, where we rely on the, the author coming up with money-

**Amy Brand** [59:11]: [laughs]

**Host** [59:11]: ... which of course, yeah, I hadn't thought of how that introduces its own biases. Huh. So all right. Going back to earlier in your career, um, you did a cognitive science PhD, and, um, and at that time, it sounds like from conversation that you and I were having just before we started recording, that you also considered computer science as an option. So what fascinates you about natural language [laughs] and about natural language processing?

**Amy Brand** [59:43]: Um, yeah. So, so much to this day, you know, we all think about the paths that we, we could have, could have taken and, and didn't take. When I, when I was an undergraduate at Barnard/Columbia, my, my, um, undergraduate degree was in linguistics and, and I had always been, you know, fascinated. You were talking about, you know, philosophy and philosophy of language and logic, just fascinated by imposing formal structure on symbol, in symbolic systems, you know. And that could go in several directions. It could go into linguistics. It could go into the study of mind and language. Um, certainly go into natural language processing, and I'd had a minor in computer science and thought about that path. So when I came to MIT-

**Host** [60:28]: Mm-hmm

**Amy Brand** [60:29]: ... you know, when I came to MIT, I was in cognitive science, but largely studying linguistics, and had a secondary advisor in, in computer science, what's now CSAIL at MIT. Um, uh-

**Host** [60:44]: Oh, yeah

**Amy Brand** [60:44]: ... you know, someone whose, you know, whose focus was on natural language processing. Um, and, uh, you know, and I, I was Interested as my career went on in, um, how brains and machines, uh, learn symbolic systems and, and learn language and ultimately kind of went in the direct-- the, the human development direction. But because my focus, and, and this could only happen at MIT, right? Because my focus was on the, the formal structure of these systems, and I was working closely with Noam Chomsky, um, you know, it was-

**Host** [61:19]: Wow.

**Amy Brand** [61:19]: ... it was very, it was very much, um, [lip smack] you know, sort of form- formal modeling of these systems and, and my dissertation, you know, is about this very, very esoteric thing in syntactic theory and how this, this particular principle is, is learned by children in English, French, and Spanish. Um, yeah. And, and, you know, I, I stayed in academia for a while, but, um, realized that it was these, these larger kind of philosophical questions kept calling me back, and I found my way into publishing. Um, you know, I, I, I think I could have been pretty successful as an academic. Um, and I still love to do research and publish, and I, and I continue to do that kind of more in, in the field of scholarly communication and information science. But to me, it's so-

**Host** [62:10]: Mm-hmm

**Amy Brand** [62:10]: ... closely related to what I was doing before.

**Host** [62:14]: Well, I, for one, am very grateful that you are doing what you're doing. I mean, yeah, no doubt you, uh, could have been if you'd chosen to focus even more-

**Amy Brand** [62:24]: Yeah

**Host** [62:24]: ... on academics than you have, you could have made an enormous impact, but I love the impact that you are making by, yeah, disseminating incredible literature, um, and now films as well. Um, but on the note of your research, l- later research of yours is more about, as you kind of alluded to, um, authorship in academic research. So topics of credit, collaboration, contribution, attribution, even plagiarism, um, and you point to classifying contributions and setting standards for role taxonomy. Could you elaborate on why this is important, um, and what are the blockers, if any, to implementing a system like that?

**Amy Brand** [63:06]: Um, sure. Just, just-- I'll start just quickly on, on how this came about. So I mentioned that I had spent some time at Harvard in the Provost office, and my, my job when I was there for about four or five years, um, was to help pull together tenure and promotion cases and, and, and look at, uh, people's kind of record of, of scholarship and excellence. Um, really, really fascinating work also closely related to publishing. But it became clear to me that w- there's this issue, like if you, if you're preparing your CV or your dossier, um, and you happen to be a researcher where the main record of what you've done or achieved is a list of publications, um, there's a total mismatch between how that information is conveyed and what actually happened in the research. [chuckles] So, you know-

**Host** [64:00]: Mm-hmm

**Amy Brand** [64:00]: ... you may be familiar with the fact that it's, it's pretty common practice, uh, in the sciences, which are increasingly multi-authored, to have the first author or the last author positions, which are the most prominent, be, say, the lab head-

**Host** [64:14]: Mm-hmm

**Amy Brand** [64:14]: ... the person who obtained-

**Host** [64:15]: Mm-hmm

**Amy Brand** [64:15]: ... um, the funding, um, and to have there be like no indication in a long list of authors, like who actually, you know, was behind this methodology? Who actually did this work?

**Host** [64:25]: Right. Yeah.

**Amy Brand** [64:25]: Who actually did the writing of this paper? Um, and the fact that that, that process, this sort of like two-dimensional way of representing authorship obfuscates all the contribution underneath just, you know, struck me as, as being one of the ways in which the biases that we've been talking about through this conversation get perpetuated and, and-

**Host** [64:47]: Right

**Amy Brand** [64:47]: ... particularly a barrier for young researchers because the culture of a lot of labs, I mean, of course, it varies from field to field, is, you know, graduate students and postdocs might be doing the bulk of the work, but-

**Host** [64:58]: Mm-hmm

**Amy Brand** [64:58]: ... um, might not be in that most prominent author position. So-

**Host** [65:02]: Right

**Amy Brand** [65:02]: ... the way I think about things as a sort of data scientist monk, I guess, is that let's create another dimension on which to represent this other, th- this other, um, signal, right? That, um, okay, you know what? We don't have to change anything about the au- order of author names, but we can have a way of signaling in a machine-readable way that, you know, this individual contributed, um, to the underlying statistical model, or this indivi- individual did the bulk of the, the, um, you know, data analysis or writing or what have you. Um, and so I-- while I was still working at Harvard, I pulled together a bunch of people I knew who would get this whole problem space and a bunch of people who probably never thought about things that way into a workshop. And, you know, this was 2012, I think, that we, we had this workshop. Um, and just a couple of months ago, or maybe just a couple of weeks ago, the National Information Standards Organization announced that this taxonomy, uh, is, is now in a formal technical standard-

**Host** [66:12]: Oh, wow

**Amy Brand** [66:12]: ... um, which is really fun. And, and it's still-

**Host** [66:15]: Congrats

**Amy Brand** [66:15]: ... again, it's, it's collaborative work. There's several people involved. Um, worked most closely with my, my colleague in the UK, Liz Allen. Um, and there were several people involved. But, um, you know, we-- over the years, we've seen more and more publishers adopt this standard so that it means that if you're, you know, publishing a paper in Cell, for example, um-

**Host** [66:35]: Mm-hmm

**Amy Brand** [66:36]: ... and you're contributing it, you're not only gonna indicate who the authors are, you're gonna choose from this standardized taxonomy of roles, um, who did, who did what. Um-

**Host** [66:45]: Wow.

**Amy Brand** [66:45]: And it's, its adoption is growing. You know, there's, there's still, um, barriers because it's obviously an imperfect taxonomy. There are only 14 roles, and there, there are many ways to talk about contribution. And of course- You know, the ways in which people contribute to research varies tremendously across the different-

**Host** [67:06]: Right

**Amy Brand** [67:07]: ... fields, but, but it's a good place to start. And so-

**Host** [67:09]: Yeah

**Amy Brand** [67:09]: ... you know, my, yeah, my hope is that, that it continues to grow and it just changes the conversation and, and enriches the vocabulary that we have to talk about how we've contributed, uh, to research or contributed to an article.

**Host** [67:23]: Very cool. I can see the utility in this. There are a handful of papers from my time when I used to be publishing papers regularly, where it does state exactly what I did on the paper, and I'm always like-

**Amy Brand** [67:34]: Yeah

**Host** [67:34]: ... that seems really helpful. Like-

**Amy Brand** [67:36]: Yeah

**Host** [67:37]: ... uh, it just, you know, it's nice that I'm being acknowledged for having done the statistical analysis, for example. Um-

**Amy Brand** [67:43]: Yeah

**Host** [67:44]: ... and that it's clear that somebody else actually did all the writing and that I wasn't really involved in that at all. Um-

**Amy Brand** [67:50]: Yeah

**Host** [67:51]: ... yeah, it makes so much sense to be able to have that on paper. So yeah, great that you've done that.

**Amy Brand** [67:56]: Yeah.

**Host** [67:56]: Um-

**Amy Brand** [67:56]: But it... the way it was being done in the past though, was in a free text way, right?

**Host** [68:02]: Oh, totally.

**Amy Brand** [68:02]: And so-

**Host** [68:03]: Yeah, yeah, yeah

**Amy Brand** [68:03]: ... yeah, and so the, the whole, the whole point of standardizing it is, is again, to make it machine readable.

**Host** [68:08]: Right.

**Amy Brand** [68:08]: And even though this kind of description is qualitative, essentially, it, it provides a foundation for, um, other quantitative metrics to be created that go beyond the kinds of metrics we use currently. Um-

**Host** [68:22]: 100%, yeah.

**Amy Brand** [68:23]: Yeah. And I, you know, it... I, I can imagine a whole other career for myself where all I did full-time was work on different types of things like this 'cause I'm fascinated by it and, um, but I'm, I'm glad to see this come to fruition.

**Host** [68:38]: Yeah. Yeah. Super cool. I look forward to seeing more of that, uh, now that it has been approved as a, as a standard.

**Amy Brand** [68:46]: Yeah.

**Host** [68:46]: Very cool. All right. So we've had an amazing interview and amazing conversation so far. Uh, we're wrapping it up. We're getting near the end now. And so near the end of these episodes, I always ask for a book recommendation, [laughs] and I feel like-

**Amy Brand** [69:04]: Sure

**Host** [69:04]: ... with some of my guests, that can throw them off guard. They weren't anticipating it. Some of them haven't been reading in a while. But now we've got somebody who has-

**Amy Brand** [69:12]: Yeah

**Host** [69:12]: ... book after book going, yeah, going under your nose every day, so yeah, yeah.

**Amy Brand** [69:16]: It's true. I, I... So I'll, I'll... If, if you don't mind, I'll, I'll provide two. One is, um-

**Host** [69:23]: Please

**Amy Brand** [69:23]: ... I, I, I absolutely love audio, and I-

**Host** [69:27]: Mm

**Amy Brand** [69:27]: ... especially love it when the writers I love read their own books. And so I found my way recently-

**Host** [69:34]: Mm

**Amy Brand** [69:34]: ... to, um, Ann Patchett's, uh, most recent book of es- essays, which is called These Precious Days. And I just absolutely love it because this is a woman who's not only a phenomenal writer, but as... I, I, I listen to her and I think like, "I just wish she were my best friend." She's like the sanest person in the world.

**Host** [69:52]: [laughs]

**Amy Brand** [69:52]: But the, but the other thing is she's, she's just so passionate about books and the, and the written word, and she runs her own bookstore in Nashville, and tells a lot of-

**Host** [70:01]: Wow

**Amy Brand** [70:01]: ... stories about that. Um, and so I've been recommending, you know, this book to, to my colleagues at the press. But another book that I'm reading, not, not on audio, is one of her own books. Um, it's called The Future of Work by MIT economist-

**Host** [70:17]: Mm

**Amy Brand** [70:17]: ... um, David Autor. Um, and it, it, it, it, it tries to explain and then provide kind of remediation to the issue that, you know, in the, the, um, kind of what we consider or have considered like blue collar jobs in the US, less specialized jobs, um, that the US has kind of been falling behind in, um, providing the kind of computational skills and, and, you know, job growth that might be possible. Um, and so it's about applying technology to the workplace in a way that promotes equity, um, and financial growth-

**Host** [70:54]: Wow

**Amy Brand** [70:54]: ... for a broader range of people. And it's, it's a fabulous book and, um, I'm, I'm proud that it's one that we've published.

**Host** [71:01]: Brilliant. Those both sound like great recommendations for our listeners. The first one because they probably enjoy audio format. [laughs]

**Amy Brand** [71:09]: Yeah.

**Host** [71:09]: Given that they enjoy listening to this podcast. Um, so being able to hear an author read her own work sounds great. And then The Future of Work, I mean, this is, this is such a massive opportunity and something that you were talking earlier about how publishing can influence policy, and this sounds like a perfect situation for that because we have this huge problem of so many people, millions of people in the United States, who are being displaced by change, and some of that is related to AI and automation. Um, and it seems the, the, the data that we're seeing more and more of, it seems like it- automation actually increases employment opportunities, and that the employment opportunities that people can have are more enjoyable. So the kind of work that gets displaced is laborious, repetitive work that humans don't really wanna be doing anyway. And so-

**Amy Brand** [72:06]: Yeah

**Host** [72:06]: ... there's a huge opportunity, but it only exists if people are being retrained.

**Amy Brand** [72:11]: Right.

**Host** [72:11]: Um, and if they're not retrained, then-

**Amy Brand** [72:13]: Exactly

**Host** [72:14]: ... not only is that horrible on an individual level to be unable to find employment, but it's also, you know, it's... going back to the thing about having more brains involved, it's bad for our society.

**Amy Brand** [72:24]: Yeah. It is.

**Host** [72:25]: Um, yeah.

**Amy Brand** [72:26]: Yeah.

**Host** [72:27]: So really-

**Amy Brand** [72:28]: Good

**Host** [72:28]: ... great recommendations. Thank you.

**Amy Brand** [72:30]: Yeah.

**Host** [72:30]: All right. So-

**Amy Brand** [72:31]: Thank you. This was so much fun. Thanks.

**Host** [72:34]: Yeah, my pleasure, Amy. And so clearly you are a brilliant person with lots of interesting perspectives on a broad range of topics. Is there any particular way that listeners should be connecting with you or following with you to hear your opinions going forward?

**Amy Brand** [72:49]: Um, well, I'm, I'm very easy to, to reach at MIT. Um, I'm not very big on social media, um, so, but, you know, occasionally will tweet about things going on at the MIT Press, but I'm-

**Host** [73:02]: [laughs] There you go

**Amy Brand** [73:02]: ... open to folks reaching out to me over email.

**Host** [73:06]: Nice. All right. And we'll be sure to include, uh, your Twitter handle, uh-

**Amy Brand** [73:11]: Okay

**Host** [73:11]: ... in the show notes. Thank you so much, Amy, for being on the program. And yeah, hopefully we'll have the opportunity to have you on again in the future.

**Amy Brand** [73:19]: I'd love that. Thanks so much.

**Host** [73:21]: [upbeat music] What a special episode that was. Dr. Brand is such an inspiring, pioneering individual who's making the world a better place through her relentless creativity, intellect, and drive. In today's episode, Amy filled us in on what it's like to run the prestigious MIT Press that has brought us so many classic data science and machine learning books, including essential open access books like Goodfellow et al.'s Deep Learning. She talked about how open access makes scholarly work more impactful on society and makes it more equitable for historically underrepresented groups in STEM. She talked about how competition and open source solutions are needed to facilitate more open access publishing across more organizations, how her award-winning documentary Picture a Scientist grew organically out of interviews with exceptional female scientists, how publishing outstanding STEM books for broader audiences, including for children, can help address the biases that exist against women and minorities in STEM, and how author metadata in standardized taxonomies can help authors receive the credit they deserve for the work they've done for a given publication. As always, you can get all the show notes, including the transcript for this episode, the video recording, any materials mentioned on the show, the URLs for Amy's Twitter profile, as well as my own social media profiles at superdatascience.com/567. That's superdatascience.com/567. If you enjoyed this episode, I'd greatly appreciate it if you left a review on your favorite podcasting app or on the Super Data Science YouTube channel. I also encourage you to let me know your thoughts on this episode directly by adding me on LinkedIn or Twitter and then tagging me in a post about it. Your feedback is invaluable for helping us shape future episodes of the program. All right. Thanks to my colleagues at Nebula for supporting me while I create content for you, and thanks of course to Yvonne Atsiebert, Mario Pombo, Serge Massis, Silvia Ogvang, and Kirill Eremenko on the Super Data Science team for managing, editing, researching, summarizing, and producing another inspiring episode for us today. Keep on rocking it out there, folks, and I'm looking forward to enjoying another round of the Super Data Science Podcast with you very soon. [upbeat music]

