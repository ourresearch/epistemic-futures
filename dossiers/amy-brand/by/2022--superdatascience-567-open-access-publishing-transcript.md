---
title: "SuperDataScience 567: Open-Access Publishing — with Amy Brand (transcript)"
person: amy-brand
section: by
type: talk-transcript
year: 2022
venue: "SuperDataScience Podcast (host Jon Krohn)"
authors: "Jon Krohn (host); Amy Brand (guest)"
source_url: https://www.superdatascience.com/podcast/open-access-publishing
retrieved: 2026-08-13
content: full-text
notes: "Official podcast transcript published by SuperDataScience. Episode 567; YouTube mirror at https://www.youtube.com/watch?v=OKJwuvBDEdw. Exact episode date not confirmed on the page (episode numbering places it in 2022)."
---

# SuperDataScience 567: Open-Access Publishing — with Amy Brand (transcript)

## Full text

Jon Krohn: 00:00:00

This is episode number 567 with Dr. Amy Brand, the director and publisher of the MIT Press. Today’s episode is brought to you by Monte Carlo, the data observability leaders and by Einblick.ai, the collaborative way to explore data.

Jon Krohn: 00:00:21

Welcome to the SuperDataScience podcast, the most listened to podcast in the data science industry. Each week, we bring you inspiring people and ideas to help you build a successful career in data science. I’m your host, Jon Krohn. Thanks for joining me today, and now let’s make the complex simple.

Jon Krohn: 00:00:52

Welcome back to the SuperDataScience podcast. We’ve got a special episode for you today with the extraordinary and pioneering Dr. Amy Brand. As the director and publisher of the MIT Press, Amy leads one of the world’s largest and most influential university presses. She is co-founder of Knowledge Futures Group, a non-profit that provides technology to empower organizations to build the digital infrastructure required for open access publishing. She created a new open-access business model called Direct to Open and launched MIT Press Kids, the first collaboration between university and children’s publishers. On top of all that, she was the executive producer of Picture A Scientist, an exceptional documentary that was selected to premiere at the prestigious Tribeca Film Festival and was recognized with the 2021 Kavli Science Journalism Award. Prior to the MIT Press, Amy held senior leadership roles at Harvard University and a number of organizations that bridge academia, publishing and industry. She holds a PhD in cognitive science from MIT itself. Today’s episode is well suited to a broad audience, not just data scientists, so you’re in the right place for a fascinating discussion with a brilliant person, whatever your background.

Jon Krohn: 00:02:07

In the episode, Amy details what open access means, why open access papers, books, data, and code are invaluable for data scientists and anyone else doing research and development. She talks about the new metadata standards she developed to resolve issues around accurate attribution of who did what for a given academic publication. She talks about how we can change the STEM fields, that’s science, technology, engineering, and math, to be welcoming to everyone, including historically underrepresented groups. She fills us in on what it’s like to devise and create an award-winning documentary film. All right. You ready for this wonderful mind-expanding episode? Let’s go.

Jon Krohn: 00:02:51

Amy, welcome to the SuperDataScience podcast. I’ve been so excited about getting you on the program. Where in the world are you calling in from?

Amy Brand: 00:02:59

I am calling in from Newton, Massachusetts, not too far from Cambridge.

Jon Krohn: 00:03:05

Nice, and not surprising that you are close to Cambridge, given that you work at MIT Press, which is in Cambridge. I’m sure all listeners are aware of the Massachusetts Institute of Technology, which is one of the world’s foremost universities and it has a great press. So the MIT Press is one of the world’s largest university publishers. It’s behind, in our industry, the Adaptive Computation and Machine Learning Series, which is edited by the absolutely iconic data scientists, Christopher Bishop, Michael I. Jordan and others. It includes books like Ian Goodfellow, Yoshua Bengio and Aaron Courville’s Deep Learning book, which is a Bible for me. It is the book probably that I refer to the most of any, and it’s a great example of an MIT Press book that is freely available as HTML at deeplearningbook.org. We’re going to talk about that freeness again very soon. Other titles in the series are Sutton & Barto’s Reinforcement Learning: An Introduction; Kevin Murphy’s Machine Learning: A Probabilistic Perspective and a couple of dozen other amazing books. So thank you, Amy, for being behind such amazing books for [crosstalk 00:04:22]

Amy Brand: 00:04:21

Thank you. We publish a lot in data science going out into even less machine learning, computational areas, so happy to be here.

Jon Krohn: 00:04:33

Awesome. So what does it mean to be a director and publisher at MIT Press? What does that role involve?

Amy Brand: 00:04:40

I have one of most fun jobs in the world because I just get to live in this world of just amazing ideas and help people see their creative works through to fruition, but day-to-day what it means is running an organization of 100 plus people mainly in the Boston, Cambridge area, but several of them in the UK as well. We publish about 350 books a year across a range of disciplines, 40 journals. I feel sometimes like the orchestra conductor. I’m trying to make it all work smoothly, but I have a fabulous team. We’re a pretty non- hierarchical organization, that’s the director part. The publisher part, which was added to my title about a year ago and I was insistent on it was really important to me because I get to sign all the publishing contracts, so I’m ultimately responsible for making those decisions. Now, of course, I consult widely with my team and others.

Jon Krohn: 00:05:47

So literally every single book that gets published by the MIT Press, your signature is on the contract. You make a final decision?

Amy Brand: 00:05:56

That is correct. Yes.

Jon Krohn: 00:05:57

Wow. That’s cool. I didn’t realize that one person could have so much power.

Amy Brand: 00:06:02

Yeah, it’s somewhat distributed, actually less distributed at MIT than a lot of other university presses where the faculty editorial boards have more power than they do at MIT. It’s more consultative, but that was decided long before I became director.

Jon Krohn: 00:06:22

Cool. Yeah. So publisher for the last year, at least in your title, having that there-

Amy Brand: 00:06:26

Yeah.

Jon Krohn: 00:06:27

… but director for seven years, so you have been leading MIT Press for some time. Something that we alluded to already, when I was talking about the Goodfellow book and it’s being freely available online is that MIT Press publishes a lot of books with open access. So over 12% of books are freely available. Why is open access valuable to data scientists, anybody doing research and development?

Amy Brand: 00:06:55

Well, I think it’s valuable to all scholars and researchers. There’s a special value to people in data science when you think about having that underlying information available to mine and compute over, but our investment in open access goes back literally decades at the MIT Press. For us, it’s an issue of making scholarship as equitably accessible around the world as possible to as many researchers as possible and readers as possible, and also to broadening participation in the whole research enterprise by making this information widely available. Among many other things that I’m involved in relation to the open data, open science, open access spaces, I’m on the board of Creative Commons, which of course is the organization that created-

Jon Krohn: 00:07:52

No kidding? Wow.

Amy Brand: 00:07:52

… and runs the open licenses that we all use when we put our works online.

Jon Krohn: 00:07:59

Wow. I didn’t know that I didn’t catch that in my research before the episode. That’s amazing. It makes so much sense to me that research academic work, which is often publicly-funded, it makes sense to me that it should be available then to the public to read. So there’s been a big shift since I’ve been an academic. It’s now 10 years since I finished my PhD, and it was during my PhD period where not only did we start to digitize works, so it’s crazy to me to think that in my undergrad, especially in the first couple years of my undergrad, I had to physically go to the library-

Amy Brand: 00:08:43

That’s right.

Jon Krohn: 00:08:44

… and photocopy journal articles that I wanted to read later.

Amy Brand: 00:08:48

If you look back at the history of digital information and open access, it really did take off in the scientific journal space. But now today, and certainly in the way in which we publish at the MIT Press, it’s across all disciplines and everything that we publish. But it’s a complicated topic, so you mentioned publicly-funded research should be openly accessible. It’s not that simple. That is a core principle, but often you are talking about the creative works, blood, sweat, and tears of an individual or a lab that has data that it wants to use and leverage in other ways. So these decisions are sometimes individual decisions, not necessarily made on the principle that it should be open. So for us, for example, when we publish open access books, it’s always with the consent of the author, if it’s something that we initiate or because the authors, like in the case of the Deep Learning book, have demanded or expected that the work be made open link, accessible.

Amy Brand: 00:09:56

That was a great example for us because it’s very easy if you look at the business of publishing for us to take, say, scholarly monographs and professional books, which have a relatively specialized limited audience and say we’ll figure out a model in which we can make those openly available. We’ll still sell some in print and a form. But if you look at our textbook program, especially in computer science, AI machine learning, which has been so core to the revenue of the press and the history of the press, it’s a lot harder. But now, a huge percentage of our reference and textbooks in AI and machine learning are openly available. What we saw with Deep Learning, it was the right book at the right time, and it was so tremendously successful in print while it was being made openly available.

Jon Krohn: 00:10:50

Yeah. I think it’s hard to tell because it’s hard to figure out from the data what the causal impact is, but I hypothesize without any real data to back me up that making something publicly available, it increases the reach so much. It allows a book like Deep Learning to have such a broad impact that everybody’s aware of it. You’re like, “Wow, this amazing book is available online,” but you’re are also like, “But a lot of people, despite having access to it online, for me, for a lot of people, having the physical book, I’m able to attend to it a lot better. I’m able to make a lot more progress. I feel like I can understand concepts a lot better as a result of that.” You can step away from the computer and just work through the book, and so for me, the book is then hugely valuable. So I might look at the first few pages online, the first chapter, and then I’m like, “Oh, my goodness. I’ve got to buy this,” and I think that that experience happens for a lot of people.

Amy Brand: 00:11:52

I think that’s true. We see that a lot in open textbooks where we know that students want to have the digital file as well as that print book. Certainly with a book like this, with many books, we’ve done some experiments where it hasn’t worked so well. So for example, when we’ve done a $0 Kindle edition of a book, that really depresses print sales. So we’ve had to find our way to doing this because we believe it’s the right thing to do, and we want to support our authors who want their work to be openly available, but making it sustainable.

Jon Krohn: 00:12:30

That’s cool. That makes a lot of sense, and that explains why it says on deeplearningbook.org, it says there’s something like an FAQ at the bottom that’s like, “Can I get a PDF version?” It’s like, “No, you can’t.”

Amy Brand: 00:12:43

Yeah. [crosstalk 00:12:44] Well.

Jon Krohn: 00:12:46

Yeah.

Amy Brand: 00:12:48

Yeah. We aspire going forward to be able to figure out the model that does allow us have that PDF. We’re still working on it.

Jon Krohn: 00:12:56

Yeah. In terms of a browsing experience on your computer anyway, I think HTML is better. There’s no point in having this idea that information should fit into a small box shape when you can scroll infinitely anyway, so I think that’s great. Going beyond just MIT Press, what tools or technologies are needed to build public digital infrastructure for open access publishing?

Amy Brand: 00:13:30

So that’s a great question. I think it would surprise a lot of people looking from the outside at the publishing industry and seeing all the digital publishing that’s happening to know how consolidated the underlying platforms and technologies are. So in the university press world, for example, there are very few hosting platforms that we choose among. I can remember early on when I had gotten involved in the world of digital publishing, I kept thinking, “Wow, I should go off and just build one of these digital hosting platforms because there’s so much demand.” You look at academic journal publishers, and they’re literally hopping back and forth between two or three, or maybe three or four choices of these platforms; a couple of which by the way, are now owned by private equity, but that’s another conversation.

Amy Brand: 00:14:25

I believe very strongly that this is a space that needs more competition, that needs some open source solutions. One of the things that I’ve been really pleased to have been involved in over the last several years was helping launch an independent non-profit called Knowledge Features, which created, developed and runs open source community publishing technologies for a range of different groups. The MIT Press does a lot of it’s open book publishing on PubHub. It’s the PubHub platform that knowledge features runs several of our journals like the Harvard Data Science Review.

Amy Brand: 00:15:04

But there are other universities, other presses, even governments that use the platform. The way that I think about it is, this isn’t about the way in which we do science publishing or data publishing is absolutely broken, so we have to destroy what we have and create something new, I think about it in terms of multiple levers of change and creating alternatives that work well, and that gradually shift the wheel and the balance of power. When I speak about the balance of power, I’m talking about the power that a lot of these large commercial companies, both publishing companies and technology companies, have over the research publication space.

Jon Krohn: 00:15:45

Cool. Very interesting, and amazing how many different organizations related to open source that you are involved with personally. So the MIT Press itself, in a way, lots of open source involvement, the Creative Commons, and now also to hear about Knowledge Futures, very cool. So we have your thoughts and clearly we know how important it is to have openness in books, in papers. What are your thoughts also on making data and code available where possible?

Amy Brand: 00:16:16

Yeah. Anybody that’s publishing research today thinks about the products of the research process beyond just the textual content. We’re thinking also of, “What is the methodology and what were the protocols in the research and how can that information be shared? What about the data, and certainly, what about the code?” What we all aspire to is having all of this content accessible in ideally standardized ways that protects people’s privacy where it needs to be protected, protects the interests of researchers that for whatever reason might not be in a position to share their data, but that ultimately allows us to accelerate the pace of research and discovery by being able to compute over that data, over that code, et cetera. I feel very, very strongly about that. It’s a somewhat different conversation for a publisher like me though, than it is for a university or a funding agency.

Amy Brand: 00:17:25

I think early on when we became aware of the fact that if we publish a journal article, say a neurochemistry, and we feel like it’s the best policy to make the related data available, it’s not necessarily that we are publishing the data. We are essentially enforcing a policy that says, “For this journal, you have to make your data available, but you’re going to make it available through your university, or potentially through your funding partner, or on some other platform or repository.”

Jon Krohn: 00:17:56

Mm-hmm (affirmative). Mm-hmm (affirmative).

Amy Brand: 00:17:59

So as I see it, this is an issue of governments, and in the U.S. certainly at the federal level to come up with that solution. What is going to be our data commons to accelerate research? If you think about the global situation right now, and the position that the U.S. is in with respect to its preeminence and research now as opposed to several years ago, the ability to capture, preserve, share and ultimately mine research data is a big part of what we want to see going forward.

Jon Krohn: 00:18:34

Right. Right, right. That makes sense. Struggling with broken pipelines, stale dashboards, missing data, you’re not alone. Look no further than Monte Carlo, the leading end-to-end data observable. In the same way that New Relic and Datadog ensure reliable software and keep application downtime at bay, Monte Carlo solves the costly problem of data downtime. As detailed in episode number 499 with the firm’s brilliant CEO Barr Moses, Monte Carlo monitors and alerts for data issues across your data warehouses, lakes, ETL, and business intelligence, reducing data incidents by 90% or more. Start trusting your data with Monte Carlo today, visit www.montecarlodata.com to learn more.

Jon Krohn: 00:19:28

So it’s super cool to me how this openness and yes, we do need to have considerations probably just beyond, there are more complications-

Amy Brand: 00:19:40

Yeah.

Jon Krohn: 00:19:41

… there’s geopolitical complications around how much things can be shared, but generally speaking, geopolitical situations not withstanding, the availability of papers, books, data, code, the more people that have access to it, the more brains there are involved in solving problems, they can have a huge impact on society. So every single person in the world, every single person listening to this podcast in particular has the capacity to make an enormous impact with what they do with their lives. The more information that you have access to, whether for reading or for feeding into your models, the bigger year impact can be.

Amy Brand: 00:20:25

Mm-hmm (affirmative).

Jon Krohn: 00:20:29

It’s taking the long view of decades or centuries, we live at a time today where a lot of people in the world, certainly not everyone in the world, but a lot of people in the world for the first time in histor don’t have to worry about whether they’re going to have enough to eat and don’t have to worry about being murdered in a war. There’s obviously exceptions at this time that we’re recording. We there’s are particularly salient exceptions, but generally speaking, we enjoy this, this abundance that would’ve been unimaginable two generation three generations ago, even, and yeah, science progress has facilitated this, and I’m reiterating the point now, but the more brains that have access to this information [crosstalk 00:21:22]

Amy Brand: 00:21:21

Brains and machines-

Jon Krohn: 00:21:21

Yeah.

Amy Brand: 00:21:21

Right? It’s brains and machines.

Jon Krohn: 00:21:23

Yeah. Right. Right. Right.

Amy Brand: 00:21:25

Yeah. Go ahead.

Jon Krohn: 00:21:26

Yeah. I agree 100%-

Amy Brand: 00:21:28

Yeah.

Jon Krohn: 00:21:30

… but on the point of brains, we want to make sure that all of the brains have the opportunity to participate. So-

Amy Brand: 00:21:37

That is correct.

Jon Krohn: 00:21:39

So science and engineering, historically, women and minorities are underrepresented in these fields. So we can call them the STEM fields, science, technology, engineering, and math, STEM. There’s this under-representation issue, so even if we lived in this world where there weren’t geopolitical issues and we didn’t worry about particular information getting into particular people’s hands, we could have all of this data, all of this information be open access, but if we have this inequity, we’re still not making the most of it-

Amy Brand: 00:22:19

That’s absolutely right.

Jon Krohn: 00:22:20

… because we’re not getting everyone involved.

Amy Brand: 00:22:23

Yeah. I agree wholeheartedly. I think about it in terms of that brain power. I think of about think of what’s lost when don’t have a whole participation of a population in solving certain problems. So this is an issue now, certainly in research, the ability of people in the Global South to participate in research. The way in which how we publish, and I as a publisher, think about this impacts that it’s not just the access to content. What is authorship and who has the right to participate as an author? What are the barriers to that? This is a big issue right now in open access models, and I’d love to come back to that if you want to talk more about it. I think where you were going was around our interest at the press in publishing as many diverse marginalized voices that previously have been underrepresented and how that even changes how we think about the definition of what science is.

Amy Brand: 00:23:32

We’re soon going to be launching a series called Epistemologies of the Global South, which I’m very excited about, but because of my own personal experience as a woman in science, I’d been a grad student at MIT. I was in academia for a while and then I left to go into publishing. I felt like it wasn’t a level playing field for men and women at all. When I decided to come back to MIT in this role as director of the press, one of the things I really wanted to do was to use that privileged position to provide opportunities for women to publish about their STEM work, to create a platform for books that would inspire kids and especially young women and young girls into careers in science and technology. We’ve gone fully in that direction now, both in books that we’re publishing at the MIT Press and in partnership with a children’s publisher as well. It did lead to my thinking of essentially conceiving of this film called Picture A Scientist, and-

Jon Krohn: 00:24:47

Yes.

Amy Brand: 00:24:47

Yeah. Through that, I really wanted to pay homage to these women that I had known, some of whom I had known when I was a grad student at MIT in the ’80s, and that I had heard about through the years of having essentially had gotten the president of MIT to admit in 1999, which seems like it’s not too long ago that women were being discriminated against in the resources they had access to, how they were being compensated in the opportunities that they had access to, size of their labs. That was a real turning point in academia.

Jon Krohn: 00:25:27

All right. So Amy, you’ve talked about how MIT Press is involved in publishing not only books by women and minorities in STEM fields, but also about them and being a leader in that area. Then you also mentioned this film, Picture A Scientist, which is related to that. So not only is your work as director at MIT Press helping to create content for, about, by historically underrepresented books in STEM fields, but on top of that, you’ve been executive producer of this amazing, amazing film, Picture A Scientist. I haven’t finished it yet, but I’ve started it. I’m about halfway through and it is completely absorbing. It is no surprise that it was selected for a 2020 Tribeca Film Festival appearance-

Amy Brand: 00:26:24

Premiere. Yeah.

Jon Krohn: 00:26:25

Premiere is the right word. I don’t know lingo.

Amy Brand: 00:26:25

Yeah. [crosstalk 00:26:27] It was so sad-

Jon Krohn: 00:26:27

It’s available-

Amy Brand: 00:26:33

Right before the pandemic, we were all set to go and then it didn’t happen, but it was selected. Yeah. [crosstalk 00:26:41].

Jon Krohn: 00:26:41

It right in my neighborhood here.

Amy Brand: 00:26:43

Yeah. Okay.

Jon Krohn: 00:26:44

I’m basically in Tribeca here.

Amy Brand: 00:26:45

Oh.

Jon Krohn: 00:26:47

Yeah, I’m a little bit south of Tribeca in the financial district of Manhattan, but the pandemic ruined a lot of things, was there a virtual premiere or something like that?

Amy Brand: 00:27:01

I think there were some for virtual screenings, and of course it was still an honor to have been selected, but certainly the pandemic changed the whole course of how that film was seen by the world, but in some ways for the better, because there were so many screenings on campus and so many good conversations with people.

Jon Krohn: 00:27:21

Right. Yeah. It’s available around the world on Netflix. It’s about 100 minutes long, but if you don’t have access to Netflix, there’s even a 13- minute version called The Uprising that is key excerpts of it. That’s available for free on the MIT YouTube channel. So Amy, how did you get inspired to make this film? I guess you talked about already how you were exposed to these stories being at MIT, this big change in 1999 around the president of the university having to acknowledge the women have smaller labs than men on average, and significantly smaller on average. But having that idea thinking, “Hey, I’m aware of these stories,” and I might have thought if I was running a publishing company, I might have thought I need to make a book about this, but you made a film about it. So how did that end up happening?

Amy Brand: 00:28:27

Yeah, happy to talk about that. I will say, when I was a grad student at MIT in the ’80s, it was really hard to find a woman’s bathroom almost anywhere that you went, and this was a constant source of griping. I became aware of the fact, I guess it was about four or five years ago through the MIT libraries and the archives that there was an effort to collect the papers of many incredibly eminent women at MIT who had been in the ’90s, I think something like the only 16 or 17 tenured women on the faculty of science at MIT, just a very, very small number. I had known some of them when I was a grad student at MIT and the archivist at the library said, “Maybe you want to do a book about this,” and so I agreed to meet with all the women.

Amy Brand: 00:29:22

I remember that meeting clearly-

Jon Krohn: 00:29:25

Oh, wow.

Amy Brand: 00:29:25

… to this day, and it was in the course of that conversation that we thought, “Well, it would be a lot easier for everybody if we just did like we’re doing now, film, audio interviews of everyone to capture their story and we’ll build the book from there.” We were very quickly able to obtain funding for this project to collect all this footage, the American Academy of Arts and Sciences in Cambridge loaned us this incredible space to bring all the women together. Friends of mine who were closer to the film industry connected me to two incredible directors who take most of the credit for the ultimate film that you see, Sharon Shattuck and Ian Chaney. I essentially hired them to come in and do these interviews.

Amy Brand: 00:30:18

We got about 30 hours of interview footage with just an incredible group. I think almost everyone who was still alive, who had been part of this movement at MIT in the ’90s that led to the report on the status of women on the faculty of science at MIT, and led to then president Chuck Vest saying, and it being covered in The New York Times that women were being discriminated against at MIT, all of those people came back. Because the footage we captured was so remarkable and there was just great, I would say, synergy with the filmmakers, we realized that we had not only a book project, but we also had the potential for a documentary film.

Amy Brand: 00:31:04

Ian and Sharon, I was as executive producer, my main function was to help raise money, which I did, for the film while they shaped the broader story that went out beyond MIT to bring in a couple of other just amazing women and their stories from other universities. So that’s really how it came about. The book we did, the book is happening, but it’s not happening at the MIT Press, it’s happening elsewhere, but I’m so excited about it. A number of other book projects resulted from this as well. We just put out a book called Carbon Queen, which is a biography of Millie Dresselhaus, who was among what we call the MIT 16, these remarkable women. It’s the story of her career at MIT.

Jon Krohn: 00:32:08

So incredible to hear that story and having watched half the film, I can confirm that there are stunning, emotionally moving interviews. In everything I’ve seen so far, everybody presents what happened to them so articulately. So clearly you can almost experience alongside them the unpleasantness or the unfairness, the unjustness of historically, and probably still today, a lot of people experience. In fact, I know even from those interviews, definitely still today, that it sounds like, especially if you add multiple of these minorities together, so if you’re not just a woman or not just Black, that if you’re a Black woman, then it’s still today at conferences, at university, in meetings, it’s like there’s lots of small ways that you are made to feel like you are not part of the community, that you’re not, say, a scientist or an engineer.

Amy Brand: 00:33:29

Mm-hmm (affirmative).

Jon Krohn: 00:33:31

So hearing these stories presented so clearly, so articulately it’s been a moving experience for me, and I can’t wait to finish watching the film. Einblick is a faster and more collaborative way to explore your data and build models. It was developed at MIT and showed to reduce time to insight by 30 to 50%. Einblick is based on a novel progressive engine, so no matter the data size, your analysis won’t slow down and Einblick’s novel interface supports the seamless combination of no code operations with Python code. This makes Einblick the go-to data science platform for the entire organization. Sign up for free today at einblick.ai. That’s E-I-N-B-L-I-C-K.ai, E-I-N-B-L-I-C-K.ai.

Amy Brand: 00:34:26

Well, thank you. I do think of it as that metaphor of death by 1,000 cuts, that through the course of whether you’re in the Silicon Valley company or you’re in a science department at Harvard or MIT or elsewhere, the day-to- day experiences of not being included or not being listened to or not being taken seriously, it does continue. Addressing those concerns requires just ongoing vigilance on the part of people who are in a position to make decisions about an individual’s career growth. In the period of time when I wasn’t at MIT, in my professional career I spent some of that time working at Harvard in the Provost’s office specifically on these issues on faculty diversity and equity and career paths for faculty.

Jon Krohn: 00:35:27

Mm-hmm (affirmative). Mm-hmm (affirmative). Yeah. So building on what you’re saying there, I do really encourage people to watch this film to get a sense of this in more detail, but an analogy that the film keeps coming back to is this idea of an iceberg.

Amy Brand: 00:35:42

Yes.

Jon Krohn: 00:35:42

Where above the surface, there are really blatant sexual harassment types of behaviors where actual groping or sexual comments, that kind of thing, these are the kinds of things that it’s like obvious sexual harassment, but that’s the tip of the iceberg. It’s a small amount of the issues that underrepresented people face in STEM fields. It’s really, what’s under the water that has by far the biggest impact. What you just described is like the death by 1,000 cuts, where it’s being left off of an email chain, or your opinion not being listened to in a meeting where that same opinion expressed by a White man is listened to. So it’s the accumulation of all of these kinds of things that it sounds like certainly was a bigger issue at MIT in the ’90s, but no question still happens today, as you say, in academia, as well as in big tech companies, these kinds of I don’t want to say smaller, but more subtle-

Amy Brand: 00:36:54

Mm-hmm (affirmative).

Jon Krohn: 00:36:57

… yeah, more subtle behaviors in a way that maybe to the person who’s saying them or doing them, you might not even be aware that it’s having an impact. I guess it’s that lack of awareness that hopefully, films like this can, can bring up, that if you are a White man, you could be doing and saying things that are having a big impact on people without you realizing it. Beyond just the impact or the content of this film, I’d also love to learn a little bit about what it was making it. You’ve alluded to this a little bit, but what does it mean to be the executive producer of a film? What is that like you’ve talked about getting the film off the ground, but then once you’ve had these interviews, you’ve got the footage, you’ve realized, “Let’s make this a movie,” what happens next?

Amy Brand: 00:37:52

Yeah. So I came into this knowing absolutely nothing about making films, and I would not have known a few years ago what being an executive producer was either. So it came out of my interest in realizing that we could do this because I had fabulous creative partners and wanting to help make it happen, being in a position to help raise the funds to make the film happen. I think it wasn’t until it actually came into signing agreements with the production company that Ian and Sharon were running to make this movie, that executive producer was qualified as an individual who raises a certain amount of money or raises the majority of funding for the film. I think sometimes executive producers are more involved in the creative process. I was very much involved at the outset and have more of a stamp on the film, the short film that you mentioned, The Uprising. Then later, Ian and Sharon went off to realize their creative vision in Picture A Scientist.

Jon Krohn: 00:39:01

Wow.

Amy Brand: 00:39:04

I was in the background saying, “I’m going to raise money to make this happen for you. Please consult with me. I want to make sure that I still love what you’re doing,” but it was really their creative vision.

Jon Krohn: 00:39:17

Wow.

Amy Brand: 00:39:18

I’m doing this again in an entirely different area. I was living in Vermont during the pandemic, and I met a wonderful young filmmaker who’s making a film actually about design build architecture in Vermont, which I’m also very passionate about and have commited to executive produce another film in an entirely different area-

Jon Krohn: 00:39:40

Oh, cool.

Amy Brand: 00:39:40

… because part of it is I love working with young people. I love helping them see their interests and their passions come to fruition.

Jon Krohn: 00:39:52

Amazing. Well, I look forward to checking that out as well. Given how wonderful this film is, I’m sure that will be a success as well. Then you also corrected me on something there. I didn’t know that The Uprising came before Picture A Scientist. So the short 13-minute film that’s available on the MIT YouTube channel, that came first. I had this impression not having watched that shorter film, that it was excerpts or cut together to make-

Amy Brand: 00:40:19

They were developed at the same time-

Jon Krohn: 00:40:21

Oh, okay.

Amy Brand: 00:40:21

… where we had an agreement that there would be a short film that was just about the MIT story where actually not just me, but it was effectively sponsored by the MIT Press which is unusual for a press to do, and that the longer film that was being made, even though I was raising money for, it was financially handled outside of MIT.

Jon Krohn: 00:40:52

Got it. Got it. Got it.

Amy Brand: 00:40:54

It’s confusing. They’re overlapping in many ways.

Jon Krohn: 00:40:57

Right. Right. So they’re two separate projects, but using some of the same media-

Amy Brand: 00:41:02

Exactly.

Jon Krohn: 00:41:03

… and conveying the same idea. Yeah. Yeah.

Amy Brand: 00:41:05

Yeah.

Jon Krohn: 00:41:06

Cool. Well, so a prominent issue in the film, which we’ve already talked about is how what culminates in 1999 and the president of MIT having to acknowledge that women on average have a significantly smaller lab spaces than their equivalent male peers, equivalent at least in terms of title like assistant professor, professor, that kind of thing. So the film discusses the lead up to that a fair bit, and so you were at MIT School of Science at that same timeframe. You mentioned how coming across women’s bathrooms, for example, could be something that’s hard to do. Are there other things that you experienced while you were there?

Amy Brand: 00:41:55

Yeah. I think it was more along the subtle lines. Being very aware of the fact that women were in a minority, there were certainly some fabulous female mentors at MIT, but if you’re coming into a field and you see that you are not as well represented as men, whether consciously or unconsciously, it makes you question your career choices.

Jon Krohn: 00:42:25

Mm-hmm (affirmative).

Amy Brand: 00:42:26

I remember thinking that the women that I knew in the field that I was working in, it seemed to me that they were working so much harder. I remember thinking that it just doesn’t feel like a level playing field.

Jon Krohn: 00:42:48

Right.

Amy Brand: 00:42:50

I often feel that way today. I sometimes tell people the story, I’m running this publishing company. I had the experience about four or five years ago of having to lay someone off, and this was a White male. I had very good reasons for letting him go and I’m his boss, and I go to lay him off and he looks at me and he says, “That is not acceptable.”

Jon Krohn: 00:43:19

Wow.

Amy Brand: 00:43:19

Actually, it is totally acceptable, and that’s an everyday thing. It just was such a wake up call to me because I thought, “Your world view about your privilege and what is due to you versus just a woman walking through the world,” so I know that the same issues come up in all kinds of industries. I do think that there is something about academic science and the way in which we judge excellence and the way in which careers progress, or it’s a particularly sticky problem where there’s a lot of entrenched bias. Part of my interest in this relates to my work in the field of publishing, because I look at what is that record of production and science and how is excellence being assessed? Often it leads to many more opportunities to exclude or marginalize women and other groups. It’s almost like all of the underlying social dynamics get amplified and exacerbated through the systems that we use to do research, create new knowledge, publish it, judge it.

Jon Krohn: 00:44:38

Yeah. Something that I think can make that issue particularly salient in academia, and this is mentioned in the film Picture A Scientist, which is why it’s top of mind for me, is that there are these dependency structures embedded in it. So when you’re doing your PhD, you typically have one PhD supervisor. So if you are a young female PhD student, and you have an older male PhD supervisor who has all of this power over you, if that person wants to abuse that power, they’re in a position where it’s easier to do so. So that was something about academia, in particular, that was brought up-

Amy Brand: 00:45:28

Exactly.

Jon Krohn: 00:45:29

You’re dependent on this person, if you want to then get a postdoc, you’re going to need this person’s letter of reference.

Amy Brand: 00:45:37

Uh-huh (affirmative).

Jon Krohn: 00:45:38

But actually, now that I’m saying that out loud, almost every work relationship is like that, where you’re dependent on one person, like that power dynamic.

Amy Brand: 00:45:45

Yeah. Yes. You want to make sure whether you’re in school, in class with your professors or in any job that you do that you’re thinking about, “How do I make sure that I’m protecting these relationships? I get the best letter of reference that I can?” But it does play out differently in academia because of the networks. We tend to think about, “Okay, you’re in the discipline in biology or computer science,” but think about all the sub-disciplines within that and how small these communities are, these people, they know one another. The leaders might have gone to school together. It does tend to lend itself more to a certain type of cronyism.

Jon Krohn: 00:46:30

Right. Right. Right. That makes a lot of sense. To your point about how it can seem like, say, the women are needing to work a lot harder to be at the same position in academia as a man, there was an interesting part of an interview in the part of Picture A Scientist that I’ve watched so far where a woman of color talks about she ends up investing so much time in every email making sure that she’s getting the tone right because there can be stereotypes against her of being quick to be angry or something. So she has to put all this extra care and she’s like, “What if I add up all of that extra time spent trying to really articulate clearly in an email to make sure that I’m striking the right balance, as opposed to maybe me as a White man, I can just say how I’m feeling and I’m not going to encounter the same resistance or backlash?” So that was an interesting example to me, a specific example of how it can end up being the case that somebody in an underrepresented group can end up having to invest so much more time and getting the same outcome.

Amy Brand: 00:47:50

Yeah. That was the chemist, Rachelle Burke, and it’s also, for me, one of the most salient stories in the film about the amount of time that she invests and how that’s time away from doing the science that she wants to do. That comes through in Nancy Hopkins story as well. There’s this moment in the film where she says, “I didn’t want to be an activist, and all of a sudden I realized that this is what I had to do.” To this day, she’s become a good friend. She talks about that her investing and telling this story and affecting this change through collective social action took away from her science. She’s-

Jon Krohn: 00:48:35

No doubt.

Amy Brand: 00:48:36

… happy about the impact she’s had on the world, but it’s painful for her.

Jon Krohn: 00:48:42

Yep. So what can we do to change STEM so that it’s more welcoming to everyone?

Amy Brand: 00:48:52

It starts at the beginning, I always think in terms of pipeline. In terms of education, it is how do you expose young kids of all ethnicities and genders around the world to STEM careers in a way that makes them attractive and accessible? Certainly, in the workplace, in my workplace and publishing is a very White un-diverse industry, we’re constantly focusing on how do we attract people into publishing? We’ve been working at the press on this issue of making STEM recognizable to kids at a young age through new children’s publishing efforts that we’re doing. We started a partnership with the wonderful Candlewick Press, which are the some of the leading children’s publishers in the country.

Amy Brand: 00:49:50

They happened to be located in Somerville, not far from us with new imprints, MIT Press Kids and MI Teens, that are focused. I would say not just on STEM, I’d say STEAM fields, so bringing in the arts as well, but at the MIT Press itself, we had started publishing graphic novels for adults a few years ago and have now started to do graphic novels for young adults. One of them that I love that came out, I want to say, I think it was, yes, it was last year or earlier this year, it’s called The Curie Society. It’s adventure stories illustrated in comic book style of young women solving complex scientific problems, and has been-

Jon Krohn: 00:50:42

You mean after Marie Curie?

Amy Brand: 00:50:45

Branded after Marie Curie. Next month, we actually have a book coming out called Power On, which is it tells stories of coding for kids that show how empowering it is to be able to actually do computer programming and code. It represents in the book through the illustrations it just a diverse population of kids, and we’re really, really excited about that one as well, because in some of the normal adult publishing we were doing, whether it was graphic novel treatments of complex topics, we had one on The History of Feminism not too long ago, and then we had another one on-

Jon Krohn: 00:51:25

Wow.

Amy Brand: 00:51:26

The Origins of the Universe by the wonderful Clifford Johnson at USC. We were realizing that there was a young adult audience for these books and also for some of our essential knowledge books, which are very short introductions to topics. It started out in science and technology, and now it’s across the range of fields that we publish in. We realized that this was just a natural direction for us to go in, but we also realized that we could do some of these books for young adults, but when it came to truly publishing well for young children, that went beyond our capabilities and our area of expertise. From that came the decision to partner with Candlewick.

Jon Krohn: 00:52:10

Wow. That’s so cool. So I personally love graphic novels of complex topics. So some particular ones that have impacted me in recent years is a book called Logic Comics, which is about Bertrand Russell and logic.

Amy Brand: 00:52:31

Yeah.

Jon Krohn: 00:52:32

So yeah, I learned a ton about philosophy and his really interesting biographical history, both as an academic, as well as an anti-war activist. So that was really cool. It sounds like you’re very familiar with it. Then also-

Amy Brand: 00:52:48

Yeah.

Jon Krohn: 00:52:48

Yuval Noah Harari is my favorite non-fiction author today. I absolutely love his book Sapiens, and now they’re releasing it as graphic novels as well [crosstalk 00:52:59]

Amy Brand: 00:52:59

I actually didn’t know that. I love Sapiens too. I didn’t know it was coming out of graphic novels. That’s very cool.

Jon Krohn: 00:53:05

Yeah. There’s a first volume for sure that’s out now at the time of recording and-

Amy Brand: 00:53:11

That’s neat.

Jon Krohn: 00:53:12

It is. It’s very well done and I could see how that can be appealing to young adults, the Sapiens one in particular. I think it seems to me like there’s elements of it that they’re trying to make it a bit more appealing to that younger audience, but Logic Comics, that is an adult book. I just enjoyed it. We have to spend so much of our day feeling like we’re being serious and reading, you know rigorous things. So it’s really nice to be able to relax and I’m quite a visual person. I created a book called Deep Learning Illustrated.

Amy Brand: 00:53:45

Yeah. Yeah.

Jon Krohn: 00:53:45

I like visual approaches to conveying information and so I love that those graphic novels exist. I can’t wait to check out what MIT Press is releasing, because I didn’t know you were doing that until now.

Amy Brand: 00:53:57

Yeah.

Jon Krohn: 00:53:58

Then going a step further, I love that you have this MIT Press Kids that you’re working with Candlewick on?

Amy Brand: 00:54:06

Candlewick, yeah. We also have in our MIT Press bookstore, which is it was closed for some time during the pandemic and just reopened within the MIT Museum here in Cambridge, a large children’s section now, which it’s just fabulous. It has not only our books, but books of other publishers that are intended to inspire young kids all the way down to those really little chunky books that you give to nine-months-old children into these topics.

Jon Krohn: 00:54:42

Cool. So we got onto talking about this topic, because we were talking about how we can help change STEM so that it’s more welcoming to everyone. So for listeners that have forgotten, that’s how we got that we got here. Yeah, such an incredible example.

Amy Brand: 00:55:00

I guess it’s too easy to talk about, “Oh, we have these big problems in the world,” but look at the world, we do. It’s a world literally on fire and we need all the brain power and compute power to be solving these big problems in the world.

Jon Krohn: 00:55:15

For sure.

Amy Brand: 00:55:18

Certainly, when it comes to data science, that’s the work of a lot of the listeners to this podcast. But in my world, I think about it in terms of how do you shorten the path from idea and discovery to impact on the world? How do you broaden participation in research so that we can bring all that brain capacity around the world, starting at a young age to bear on these issues? Fortunately, as a publisher who has to sustain and run a business, there’s just been an explosion of growth in interest in these topics as well. So-

Jon Krohn: 00:55:57

Wonderful.

Amy Brand: 00:55:57

… when I came back to the press almost seven years ago, we had a very large and successful, and have for many years, publishing program for general readers in art and architecture and design and much less so in STEM topics. Now publishing books for, we like to call them books that honor the complexity of their subject matter, but they are books also for the general reader, just very, very successful. It feels like it’s an opportunity for us as a publisher to actually have an influence on public policy. That’s the way I think about it.

Jon Krohn: 00:56:36

So cool. Yeah. So now that I know that MIT Press is doing all this, it sounds like for me, finding gifts for people, which is perennially a big issue for me. Now all of a sudden, no matter whether they’re nine-months-old or 90-years-old-

Amy Brand: 00:56:52

Yeah.

Jon Krohn: 00:56:52

… I’m going to be able to find a great, super interesting book about a topic that I’m passionate about that could also help open horizons or perceptions of young people, old people to the impact they could be making in the world with science and technology and engineering.

Amy Brand: 00:57:13

You can be sure if-

Jon Krohn: 00:57:13

Very cool.

Amy Brand: 00:57:14

… sure if it’s a book coming from the press, it’s going to be beautifully designed and often beautifully illustrated and packaged, but this isn’t an advertisement though.

Jon Krohn: 00:57:25

No, it’s true. Yeah. There’s been no sponsorship by MIT Press or any-

Amy Brand: 00:57:29

No.

Jon Krohn: 00:57:30

Yeah, anything. This is entirely my personal opinions that are being reflected here. Cool, Amy. So we’ve talked about how things like the MIT Press Kids can be helpful for opening young people’s eyes to opportunities in science and engineering, even if they come from historically underrepresented STEM backgrounds. Going back to an earlier conversation in the conversation, we also talked about how open source can itself be a driver of more quality, because we have more minds that can be involved. There’s fewer barriers to entry. So with that in mind and given your rich expertise in open source, what do you think is the best open source model going forward?

Amy Brand: 00:58:32

Great question. It’s something I think a lot about. What we’re trying to do at the MIT Press is create open access models that don’t perpetuate bias, either in terms of access to the content, but also in terms of ability to participate as an author. Part of what’s happened over the course of the whole open access movement, and it’s a movement that has a lot of very, very driven advocates behind it, is that we’ve reached a place right now in academic publishing where most of the open access that’s happening is happening through pay-to-publish models. So when we talk about an open access journal, typically what’s happening is the author is being asked, or they’re getting money from their university or their grant funder to pay a publisher an exchange for making that work openly available. Okay. So the work ends up open access, but you’ve created a whole host of other inequities in terms of who’s able to participate, inequities across fields because some fields have more grant funding across institutions, because some universities will have those resources and certainly across geographic regions in the world.

Amy Brand: 00:59:46

I love this particular example because it’s a great example of what happens when we reduce ourself to simplistic binary thinking, “Open is good and close as bad, so open at all costs.” In fact, the issues here are very, very complex and you need to think about models that don’t essentially fall prey to this unintended consequence, and that’s what we’ve been trying to do at the MIT Press. For example, our open book model, which we launched this year is a collective institutional subsidy model, which means that if we reach a threshold of institutional support, then we just open up all the books that we published in a particular season, which we did for our scholarly monographs this year.

Jon Krohn: 01:00:40

Wow. Wow.

Amy Brand: 01:00:43

… and we’re not requesting that individual authors pay for that privilege. So that’s an example of the model that I’d really like to see more of, and those of us who work on open access and open data, we’re trying to come up with ways of funding and subsidizing the whole ecosystem to make open possible.

Jon Krohn: 01:01:08

Really innovative. I hadn’t heard of models like that before. I had not thought of the issues inherent in the prevailing open source model today where we rely on the author coming up with money, which of course, I hadn’t thought of how that introduces its own biases. So, all right. Going back to earlier in your career, you did a cognitive science PhD, and at that time it sounds like from conversation that you and I were having just before we started recording that you also considered computer science as an option. So what fascinates you about natural language and about natural language processing?

Amy Brand: 01:01:57

Yeah. So much to this day, we all think about the past that we could have taken, and didn’t take. When I was an undergraduate at Barnard/Columbia, my undergraduate degree was in linguistics. I had always been fascinated, you were talking about philosophy and philosophy of language and logic, just fascinated by imposing formal structure in symbolic systems and that could go in several directions. It could go into linguistics. It could go into the study of mind and language, certainly go into natural language processing. I’d had a minor in computer and thought about that path, so when I came to MIT-

Jon Krohn: 01:02:42

No kidding.

Amy Brand: 01:02:42

When I came to MIT, I was in cognitive science, but largely studying linguistics and had a secondary advisor in computer science, what’s now CSAIL at MIT.

Jon Krohn: 01:02:55

Oh, yeah.

Amy Brand: 01:02:55

I was someone whose focus was on natural language processing and I was interested as my career went on in how brains and machines learn symbolic systems and learn language and ultimately, when in the human development direction. This could only happen at MIT, because my focus was on the formal structure of these systems, and I was working closely with Noam Chomsky, it was-

Jon Krohn: 01:03:33

Wow.

Amy Brand: 01:03:33

It was very much formal modeling of these systems. My dissertation was about this very, very esoteric thing. It’s a tactic theory and how this particular principle is learned by children in English, French, and Spanish. I stayed in academia for a while, but realized that it was these larger philosophical questions kept calling me back. I found my way into publishing. I think I could have been pretty successful as an academic, and I still love to do research and publish. I continue to do that more in the field of scholarly communication and information science, but to me, it’s so closely related to what I was doing before.

Jon Krohn: 01:04:27

Well, I for one, am very grateful that you are doing what you’re doing. No doubt you could have been, if you chosen to focus even more on academics than you have, you could have made an enormous impact, but I love the impact that you are making by disseminating incredible literature and now films as well. On the note of your research, late, research of yours is more about, as you alluded to, authorship in academic research; so topics of credit, collaboration, contribution, attribution, even plagiarism, and you point to classifying contributions and setting standards for role taxonomy. Could you elaborate on why this is important and what are the blockers, if any, to implementing a system like that?

Amy Brand: 01:05:19

Sure. I’ll start just quickly on how this came about. So I mentioned that I had spent some time at Harvard in the Provost office and my job when I was there for about four or five years was to help pull together tenure and promotion cases, and look at people’s record of scholarship and excellence, really, really fascinating work, also closely related to publishing, but it became clear to me that there’s this issue. If you’re preparing your CV or your dossier and you happen to be a researcher where the main record of what you’ve done or achieved is a list of publications, there’s a total mismatch between how that information is conveyed and what actually happened in the research. So you may be familiar with the fact that it’s pretty common practice in the sciences, which are increasingly multi-authored to have the first author, the last author positions, which are the most prominent, be, say the lab head, the person who obtained the funding and to have there be no indication in a long list of authors, like “Who actually was behind this methodology? Who actually did this work?”

Jon Krohn: 01:06:38

Right.

Amy Brand: 01:06:39

“Who actually did the writing of this paper?” The fact that that process is like a two-dimensional way of representing authorship obfuscates all the contribution underneath just struck me as being one of the ways in which the biases that we’ve been talking about through this conversation get perpetuated, and particularly-

Jon Krohn: 01:07:00

Right.

Amy Brand: 01:07:00

… a barrier for young researchers because the culture of a lot of labs, of course it varies from field to field, is graduate students and post-docs might be doing the bulk of the work, but might not be in that most prominent author position. So-

Jon Krohn: 01:07:14

Right.

Amy Brand: 01:07:15

… the way I think about things as a data scientist monkey, I guess, is that, “Let’s create another dimension on which to represent this other signal,” that, “Okay. We don’t have to change anything about the order of author names, but we can have a way of signaling in a machine readable way that this individual contributed to the underlying statistical model or this individual did the bulk of the data analysis or writing or what have you.” While I was still working at Harvard, I pulled together a bunch of people I knew who would get this whole problem space and a bunch of people who probably never thought about things that way into a workshop. This was 2012, I think, that we had this workshop. Just a couple of months ago, or maybe just a couple weeks ago, the National Information Standards Organization announced that this taxonomy is now in a formal technical standard-

Jon Krohn: 01:08:25

Oh, wow.

Amy Brand: 01:08:25

… which is really fun, and it’s-

Jon Krohn: 01:08:27

Congrats.

Amy Brand: 01:08:29

… [crosstalk 01:08:29] again. It’s collaborative work. There’s several people involved, I work most closely with my colleague in the UK, who was Alan, and there were several people involved. Over the years, we’ve seen more and more publishers adopt the standard so that it means that if you’re publishing a paper in SEL, for example, and you’re contributing it, you’re not only going to indicate who the authors are, you’re going to choose from this standardized taxonomy of roles, who did what-

Jon Krohn: 01:08:57

Wow

Amy Brand: 01:08:57

… and it’s adoption is growing. There’s still barriers, because it’s obviously an imperfect taxonomy. There are only 14 roles, and there are many ways to talk about contribution. Of course, the ways in which people contribute to research varies tremendously across the different fields, but it’s a good place to start-

Jon Krohn: 01:09:23

Yeah.

Amy Brand: 01:09:24

My hope is that it continues to grow and it just changes the conversation and enriches the vocabulary that we have to talk about how we’ve contributed to research or contributed to an article.

Jon Krohn: 01:09:36

Very cool. I can see the utility in this. There are a handful of papers from my time when I used to be publishing papers regularly where it does state exactly what I did on the paper. I’m always like, “That seems really helpful.”

Amy Brand: 01:09:48

Mm-hmm (affirmative). Yeah.

Jon Krohn: 01:09:51

It’s nice that I’m being acknowledged for having done the statistical analysis, for example-

Amy Brand: 01:09:55

Yeah.

Jon Krohn: 01:09:56

… and that it’s clear that somebody else actually did all the writing and that I wasn’t really involved in that at all.

Amy Brand: 01:10:02

Yeah.

Jon Krohn: 01:10:03

Yeah. It makes so much sense to be able to have that on paper, so that you’ve done that.

Amy Brand: 01:10:09

Yeah, but the way it was being done in the past, though, was in a free text way.

Jon Krohn: 01:10:15

Oh, totally. Yeah. Yeah. Yeah.

Amy Brand: 01:10:16

So the whole point of standardizing it is, again, to make it machine readable.

Jon Krohn: 01:10:21

Right.

Amy Brand: 01:10:21

Even though this description is qualitative, essentially, it provides a foundation for other quantitative metrics to be created that go beyond the kinds of metrics we use currently.

Jon Krohn: 01:10:34

100%. Yeah.

Amy Brand: 01:10:36

Yeah. I can imagine a whole other career for myself where all I did full time was work on different types of things like this because I’m fascinated by it, but I’m glad to see this come to fruition.

Jon Krohn: 01:10:51

Yeah. Yeah. Super cool, and I look forward to seeing more of that now that it has been approved as a standard.

Amy Brand: 01:10:59

Yeah.

Jon Krohn: 01:10:59

Very cool. All right. So we’ve had an amazing interview and amazing conversation so far. We’re wrapping it up. We’re getting near the end now. So near the end of these episodes, I always ask for a book recommendation. I feel like-

Amy Brand: 01:11:16

Sure.

Jon Krohn: 01:11:17

… with some of my guests that can throw them off guard, they weren’t anticipating it. Some of them haven’t been reading in a while, but now we’ve got somebody who has book after book going under your nose every day.

Amy Brand: 01:11:29

It’s true. If you don’t mind, I’ll provide two. One is-

Jon Krohn: 01:11:35

Please.

Amy Brand: 01:11:36

I absolutely love audio and I especially love it when the writers I love read their own books. So I found my way recently to Ann Patchett’s most recent book of essays, which is called all These Precious Days. I just absolutely love it because this is a woman who’s not only a phenomenal writer, but I listen to her and I think like, “I just wish you were my best friend. She’s the sanest person in the world.” The other thing is she’s just so passionate about books and the written word. She runs her own bookstore in Nashville and tells a lot of stories about that, and so I’ve been recommending this book to my colleagues at the Press.

Amy Brand: 01:12:22

But another book that I’m reading, not an audio, it’s one of our own books that’s called The Future of Work by MIT economist, David Autor. It tries to explain and then provide remediation to the issue that in what we have considered blue collar jobs in the U.S., less specialized jobs, that the U.S. has been falling behind in providing the computational skills and job growth that might be possible. So it’s about applying technology to the workplace in a way that promotes equity and financial growth for a broader range of people. It’s a fabulous book and I’m proud that it’s one that we published.

Jon Krohn: 01:13:14

Brilliant. Those both sound my great recommendations for our listeners. The first one, because they probably enjoy audio format, keeping that they enjoy listening to this podcast. Being able to hear an author read her own work sounds great. Then The Future of Work, this is such a massive opportunity and something that you were talking earlier about how publishing can influence policy. This sounds like a perfect situation for that because we have this huge problem of so many people, millions of people in the United States who are being displaced by change. Some of that is related to AI and automation, and it seems that the data that we’re seeing more and more of, it seems like automation actually increases employment opportunities and that the employment opportunities that people can have are more enjoyable. So the kind of work that gets displaced is laborious, repetitive work that humans don’t really want to be doing anyway.

Amy Brand: 01:14:17

Yeah.

Jon Krohn: 01:14:18

So there’s a huge opportunity, but it only exists if people are being retrained.

Amy Brand: 01:14:24

Right.

Jon Krohn: 01:14:25

If they’re not retrained, then-

Amy Brand: 01:14:27

Exactly.

Jon Krohn: 01:14:27

… not only is that horrible on an individual level to be unable to find employment, but going back to the thing about having more brains involved, it’s bad for our society.

Amy Brand: 01:14:37

Yeah, it is.

Jon Krohn: 01:14:38

Yeah.

Amy Brand: 01:14:39

Yeah.

Jon Krohn: 01:14:40

So really great recommendations. Thank you.

Amy Brand: 01:14:43

Wow.

Jon Krohn: 01:14:43

Well, all right.

Amy Brand: 01:14:44

Thank you. This was so much fun. Thanks.

Jon Krohn: 01:14:47

Yeah, my pleasure, Amy. Clearly, you are a brilliant person with lots of interesting perspectives on a broad range of topics. Is there any particular way that listeners should be connecting with you or following with you to hear your opinions going forward?

Amy Brand: 01:15:03

Well, I’m very easy to reach at MIT. I’m not very big on social media, but occasionally, we’ll tweet about things going on at the MIT Press, but I’m-

Jon Krohn: 01:15:15

There you go.

Amy Brand: 01:15:15

… open to folks reaching out to me over email.

Jon Krohn: 01:15:19

Nice. All right. We’ll be sure to include your Twitter handle-

Amy Brand: 01:15:23

Okay.

Jon Krohn: 01:15:24

… in the show notes. Thank you so much, Amy, for being on the program. Hopefully, we’ll have the opportunity to have you on again in the future.

Amy Brand: 01:15:32

I’d love that. Thanks so much.

Jon Krohn: 01:15:40

What a special episode that was. Dr. Brand is such an inspiring pioneering individual who’s making the world a better place through her relentless creativity, intellect, and drive. In today’s episode, Amy filled us in on what it’s like run the prestigious MIT Press that has brought us so many classic data science and machine learning books, including essential open access books like Goodfellow, et al.’s Deep Learning. She talked about how open access makes scholarly work more impactful on society and makes it more equitable for historically underrepresented groups in STEM. She talked about how competition and open source solutions are needed to facilitate more open access publishing across more organizations, how her award-winning documentary Picture A Scientist grew organically out of interviews with exceptional female scientists, how publishing outstanding STEM books for broader audiences, including for children, can help address the biases that exist against women and minorities in STEM, and how author metadata in standardized tech taxonomies can help authors receive the credit they deserve for the work they’ve done for a given publication.

Jon Krohn: 01:16:40

As always, you can get all the show notes, including the transcript for this episode, the video recording, any materials mentioned on the show, the URLs for Amy’s Twitter profile, as well as my own social media profiles at www.superdatascience.com. 567. That’s www.superdatascience.com/567. If you enjoyed this episode, I’d greatly appreciate it if you left a review on your favorite podcasting app or on the SuperDataScience YouTube channel. I also encourage you to let me know your thoughts on this episode directly by adding me on LinkedIn or Twitter, and then tagging me in a post about it. Your feedback is invaluable for helping us shape future episodes of the program. All right. Thanks to my colleagues at Nebula for supporting me while I create content for you. Thanks, of course, to Ivana Zibert, Mario Pombo, Serg Masís, Sylvia Ogweng and Kirill Eremenko on the SuperDataScience team for managing, editing, researching, summarizing, and producing another inspiring episode for us today. Keep on rocking it out there, folks, and I’m looking forward to enjoying another round of the SuperDataScience podcast with you very soon.
