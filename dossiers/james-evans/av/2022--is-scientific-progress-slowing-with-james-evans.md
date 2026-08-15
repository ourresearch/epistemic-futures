---
title: "Is scientific progress slowing? with James Evans"
person: james-evans
section: by
type: talk-transcript
year: 2022
venue: "(Apple Podcasts, id1368737097)"
source_url: https://podcasts.apple.com/us/podcast/is-scientific-progress-slowing-with-james-evans/id1368737097?i=1000555819493
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 29
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Is scientific progress slowing? with James Evans

*Speakers (inferred):* speaker_0=Host, speaker_1=James Evans

## Transcript
**Host** [00:00]: [upbeat music] How can nonprofits drive social change in Chicago and beyond? Join business and nonprofit leaders on April 29th for the On Board conference from Chicago Booth's Rustandy Center for Social Sector Innovation. Gain insights from Obama Foundation CEO Valerie Jarrett on strengthening community engagement and building partnerships. Connect with experts in the social sector and discover how Chicago organizations are creating cultures of innovation and tackling pressing issues. Register at chicagobooth.edu/onboard. If you like Big Brains, there's another science podcast you should check out. PNAS Science Sessions from the Proceedings of the National Academy of Sciences features short, in-depth conversations with the world's top scientific researchers. In less time than it takes to drink a cup of coffee, you can learn about advances such as aquaculture techniques for coral reef restoration. Listen and subscribe to Science Sessions to hear more about their coral reef series on iTunes, Spotify, Google Play, Stitcher, or wherever you get your podcasts. [upbeat music] Climate change, viral pandemics, global poverty. The solutions to our greatest challenges call for scientific innovation.

**James Evans** [01:18]: The stakes are high. The vast majority of productivity improvements come from improvements in science and technology.

**Host** [01:26]: But when it comes to progress, science has a problem with a confusing paradox at its center. [upbeat music] Despite a dramatic increase in scientists and scientific papers, new ideas, innovative discoveries, and disruptive progress are actually slowing down.

**James Evans** [01:43]: We look at all fields, and in all these fields, as the number of papers goes up, as the growth of the fields goes up, the, the number of new ideas that enter the canon exponentially declines.

**Host** [01:55]: That's James Evans, a professor of computational social science and the director of the Knowledge Lab at the University of Chicago, where they use massive data sets, I'm talking millions and millions of scientific papers, findings, patents, discoveries, combined with machine learning techniques, to study the science of how science does science.

**James Evans** [02:13]: We believe that things will get better if I invest enough money with the expectation that there will be some magical discovery that takes place in science, technology, or entrepreneurship that is gonna allow us to do better. This is one of the reasons why I am deeply interested in kind of understanding this in a very nuts and bolts way so that we can think about how to engineer this at a societal level.

**Host** [02:38]: Think of science, the system of science, as a brain. Each field of science is in a different region and each scientist a different cell producing and communicating across its surface. Evans studies how this brain as a whole thinks and how to make it think differently. His lab has shown that this system has gotten so efficient that it's losing its ability to innovate. In fact, it's stalled to such a degree they can actually model what this brain will think before it does.

**James Evans** [03:05]: One of the things that's interesting is in these models, we, we can predict with some reasonable accuracy not only what's gonna be discovered, but who's gonna discover it.

**Host** [03:13]: At the Knowledge Lab, they've mapped out our system of science over and over again, almost like taking MRIs on its brain. And Evans says they've discovered ways to reorganize it such that it will generate a greater number of new ideas. And with our global crises worsening by the day, the stakes of scientific progress have never been higher.

**James Evans** [03:32]: I think that we have some, a handle on some, some things that, uh, measurably look very promising for, for science, but they're hard. They're hard things. None of them are cheap things.

**Host** [03:41]: From the University of Chicago Podcast Network, this is Big Brains, a podcast about the pioneering research and the pivotal breakthroughs that are reshaping our world. On this episode, the science of science. I'm your host, Paul Rand. [upbeat music] You know, being in charge of something called the Knowledge Lab sounds like a pretty, uh, amazing responsibility to be in charge of knowledge. How, how did, how did you find yourself in such a position?

**James Evans** [04:08]: [laughs] Well, you know, we were studying how knowledge was made, uh, where ideas came from. We were exploring how one could make ideas better, which is to say to serve our purposes more. And we're in a new knowledge intensive and data intensive age where we can look at knowledge in completely different ways than we could before, uh, which require, you know, entirely new embedding and other kinds of encoding possibilities, both generatively and analytically.

**Host** [04:38]: Imagine you wanted to understand the underlying dynamics that shape the roughly two million papers that are published each year. What are the invisible forces pushing those studies to be done rather than others? How would you do it? No single person has time to read all of those papers, much less analyze them, drawing connections and forming correlations to understand the mechanics of knowledge creation. But now, with machine learning and algorithms that can hold all that data at once, that's suddenly possible.

**James Evans** [05:06]: Right? So we can both understand how it is that knowledge is being produced, but we can also produce or generate knowledge based on these models in new ways. And so that model just felt like we needed a, a place, you know, that brings together people from the full space of imaginaries and techniques across the scientific and technical world to study and analyze and improve the way in which we invest the $100 billion that we s- invest in knowledge every year. This, and this is where the kind of the idea of Knowledge Lab came from, was that if you look at places, you know, intelligent institutions like the NIH or, uh, the National Science Foundation-

**Host** [05:41]: Sure

**James Evans** [05:41]: ... they're investing, you know, billions of dollars in science every year, and you were to ask, uh, someone at any of those institutions, "Well, what do you fund?" You know? They couldn't provide an answer to that question because there's no portfolio. There's a bunch of individual program officers who are responding to a bunch of individual scientists who do their thing, typically scientists who had productivity in the past, who are basically defining the direction for the future, and it's just a... I, it, it's not a way to build, you know, integrated strategy for success.

**Host** [06:11]: If what we want out of science is new ideas and innovations, we may be building the wrong system. In a recent study, his team designed a model using 1.8 billion citations from about 90 million academic papers, and when they combed through the data, they uncovered a few answers to one of science's most concerning questions: Why, in a time of maximum scientific output, is progress and innovation slowing down? The first answer to how this increase has slowed progress is obvious, but not intuitive before you hear it.

**James Evans** [06:44]: As fields become enormously flooded with ideas and papers, it becomes much more difficult for ideas to disseminate or filter in because they, they have this limited attention span.

**Host** [06:54]: With millions of papers every year, it's like information overload. Fields and communities end up focusing on the ideas that merely expand on well-established research, while more innovative and disruptive ideas get lost in the shuffle.

**James Evans** [07:08]: Just to speak to one another, they have to agree on e- enough things, and if they're all growing, then we're collectively agreeing on fewer things as being foundational.

**Host** [07:16]: Another explanation is both simple and troubling. Our current fields of science are just simply running out of things to discover.

**James Evans** [07:23]: In the same way that Wikipedia, you know, the first year of Wikipedia, you could go to Africa, and there's no Africa, and you could kind of click the button and type in-

**Host** [07:32]: Right

**James Evans** [07:32]: ... there were so many open questions. And so now we're in a different place. Like, it's hard to find a page that's not covered in Wikipedia.

**Host** [07:39]: Right.

**James Evans** [07:39]: There, there are diminishing marginal returns to fields and theories, which is to say, you know, a field, a discipline, is a collection of problems and methods, and each discipline is a hypothesis that, like, that these problems will best be solved by these methods. Once the low-hanging fruits have been plucked, then we have to climb higher on those trees of knowledge, or we have to transit to other trees. [laughs] You know?

**Host** [08:07]: Okay.

**James Evans** [08:08]: Other combinations of problems and methods that, that weren't basically conceived of, formalized, taught, et cetera, inside our current disciplines.

**Host** [08:18]: And while possible, Evans thinks there's a more systemic problem going on, the professionalization of science.

**James Evans** [08:24]: In this new age, there are, I would say, a deviation of incentives for science as a whole to maximize discovery and for scientists as persons to increase their productivity, their visibility, their ability to be promoted, promoted, their ability to survive in the scientific world.

**Host** [08:44]: As scientist, researcher, professor have become viable careers, employed positions in those fields have become more competitive.

**James Evans** [08:51]: Which is to say that individual scientists benefit their careers by staying close to the pack, by maximizing productivity, uh, by making inter- incremental advances. They maximize the likelihood that they're gonna be cited, which is the currency, one of the major currencies of the scientific realm, and all those things are critical for promotion, advance, and survival in, in science. And so the result of all those individuals who are engaging in that way, rather than, "We've got these m- you know, millions of researchers that could cover this enormous space," they're actually clumped together in very narrow pockets around the space because that's the best thing for them to do. Scientists, to demonstrate success, try to hedge their bets. How do they hedge their bets? They do what, like, movie production studios do. I mean, if they're try... If a movie production studio is trying to decide whether they should invest in the next, like, Slumdog Millionaire, like, just a, an independent script, could be amazing, or Transformers 9, they're gonna go with Transformers 9. I mean, they- they're gonna get the same, they're gonna get Transformers 8 receipts minus epsilon.

**Host** [09:56]: Mm-hmm.

**James Evans** [09:56]: Uh, [laughs] you know, like, they're assured to get them in the same way big teams bet on yesterday's ideas. They follow up on-

**Host** [10:03]: Wow, that's a-

**James Evans** [10:03]: ... yesterday's science papers. They hedge their bets. And so sometimes this requires us to be not behaving like the pack animals that we are, which is to say clustering around the last bis- biggest, best win. It means that sometimes we need to, like, explore across this landscape, and that's hard. That's hard. It's hard in science to survive, um, if you explore that landscape, for example, without tenure. Uh, and once you have tenure-

**Host** [10:30]: That's a-

**James Evans** [10:30]: ... it's very, it's very difficult to, you know, to, to do anything other than the, what you've done. If scientists are, like, following, you know, one investigation leads to another, their history predicts their future investigations, their future interests, um, regardless, in this case, of whether or not those things that, those paths not taken are scientifically or technologically efficacious or promising.

**Host** [10:53]: This problem has gotten so extreme that Evans' team can even build algorithms and AIs that can predict scientific discoveries before they even happen.

**James Evans** [11:02]: We were looking at what, uh, materials had valuable energy-related properties, medical properties, et cetera. So we're, we're predicting drugs that would be valuable against disease-related genes. We were predicting thermoelectric, ferroelectric, other kinds of energy-related properties. If we basically build a kind of a knowledge manifold, all of all the, the prior discoveries that are made, we can do a great job of, uh, predicting what materials will be discovered to have these properties in the future. And, uh, one of the things that was interesting is we, we looked at this for all these different disease and drug and other categories, and by incorporating the people, by basically incorporating where the people were sitting across this space, we could dramatically improve by more than 100% our prediction of what would be discovered in the next period.

**Host** [11:50]: They even looked at this in the context of discoveries around COVID.

**James Evans** [11:53]: In the context of COVID. So we were predicting basically what were those, um, medicines and vaccines that would either prevent or be associated with COVID, useful COVID therapies. Now, this is an area where, you know, it became a problem a couple of years ago, and then there was an enormous flood of people coming in-

**Host** [12:10]: Right, right

**James Evans** [12:10]: ... to try to solve this problem. And it turns out by incorporating the distribution of, of scientists, right, at a prior period, even before we begin this wave of discovery, we can improve our prediction of the things that will be discovered by 400%. But when we incorporate people into those predictions of COVID, where there's a ton of people who, who, you know, moved into the space, I thought we would have less purchase because new people would bring their, their different expertise, and they'd be coming at this problem from all different angles. But exactly the opposite is the case. Because everybody came in so quickly, everybody relied on the few pathways-

**Host** [12:51]: Hmm. I see

**James Evans** [12:51]: ... that were available at the very beginning with the very few pe- everything was completely path dependent. That path dependency was locked in like a crystal. Um, so very few investigations went outside what people already had supposed, right, and had been investigating at the very beginning of the crisis.

**Host** [13:08]: There's another aspect to this that ties into something we've talked about a lot on this show, the replication crisis.

**James Evans** [13:14]: Yeah, so one of the things that we've been looking at is in addition to, you know, how fast can science explore the space of opportunities, and to what degree can it explore and discover new things, also how robust is the knowledge that it produces itself, you know, beyond the, the kind of fragile context of your particular experiment. And, uh, and this has been in the context of, I would say, really a 15 to 20 year concern about the degree to which scientific findings in top scientific venues, uh, replicate, and, and the discovery that many of them don't replicate at the level that we expected that they might.

**Host** [13:49]: And the replication crisis has unveiled to us the knowledge we're producing isn't as robust as we would hope. Many papers that for decades were thought to be foundational are turning out to not replicate. By modeling hundreds of thousands of papers, Evans' team can start to identify what conditions lead to more replicable results.

**James Evans** [14:12]: And one of the things that we find in a series of projects, I mean, we've looked at this in the context of randomized clinical trials in medicine, we've looked at this in the context of, you know, gene-gene interactions, you know, hundreds of thousands of papers looking at perturbagens or chemicals and disease related genes, and we model all these aspects. You know, team size, the likelihood that, that groups are working together, that they're independent, they're using different approaches or methods. And we find time and time again deeply replicated is when you bet all your chips on one set of teams or a community that's dense, you know, where the authors and the centers are all interspersed, it dramatically decreases the likelihood that those funding, that, that those findings will replicate outside the fragile cluster of that team. And you can see just a linear and massive linear increase just when you add independent communities to the study of this, uh, of this phenomena. It, it just linearly increases the likelihood that they're gonna replicate in the future, and that they're gonna be able to spin off insights into things like the clinic.

**Host** [15:16]: So teams that are separated from those dense clusters of professionalized researchers focused on that longstanding canon of that field actually make discoveries that are more replicable and more robust, which is really what we hope for from our system of scientific discovery, more innovation that's robust and replicable. And Evans has some ideas of how to reorganize our system to get us there, one of which is really out of the box, literally. Those ideas after the break. Big Brains is supported by the University of Chicago Graham School. Are you a lifelong learner with an insatiable curiosity? Join us at Graham and access more than 50 open enrollment courses every quarter in literature, history, religion, science, and more. We open the doors of UChicago to learners everywhere. Expand your mind and advance your leadership. Online and in person offerings are available. Learn more at graham.uchicago.edu/bigbrains. There's an underlying theme you may have noticed to all of Evans' work.

**James Evans** [16:25]: Well, I think one is, is diversity.

**Host** [16:28]: And when Evans says diversity, he doesn't just mean diversity of identity, although that is part of it, but diversity in every sense of the word. All of the Knowledge Lab's models point to diversity being a major driver of innovation.

**James Evans** [16:40]: W- we have a, a paper that will be coming out very soon, but it's, it's, uh, it's on the archive. We, we look at, at surprising discoveries. So we basically build a model of expectation that kind of predicts new configurations of things that will show up in next year's papers and patents, and then we identify those that are the least likely, the most improbable to show up under that most probable model. And then we, we find that these actually are surprising to the people. I mean, people, scientists who annotate these papers say, "This is really controversial. This is really a surprising discovery." The question is, where do these come from? The majority of these things come from, or the most predicted ones come from where a, a group of people from one discipline or background travels over to another space, right, and publishes something in a journal solving a problem that no one like them has looked at before. No one in that space has seen someone like them before. So these are low probability bets. I mean, these are the things that succeed where the vast majority of such hypotheses fail.

**Host** [17:38]: Physicists think differently than biologists, who think differently than chemists, and usually each wants to invest their time and energy building a knowledge and a reputation in their respective fields. But it's when they take a bet bringing their knowledge to a completely foreign space, creating a diversity of expertise, that we actually get better results.

**James Evans** [17:58]: This is a bet that this, you know, like very distant method is gonna help solve this problem. And I would say this is an opportunity. This is something that we didn't have even 100 years ago. Because of the density of science and the diversity of fields, now we're in a place where when you can't solve your problem, typically it ends up becoming solved, um, not by looking harder at nature, but by Basically transferring, uh, insights and theories that came from completely disconnected-

**Host** [18:27]: Okay

**James Evans** [18:27]: ... other place in the scientific enterprise. So this is-- I think of it as another aspect of diversity.

**Host** [18:33]: There's another project that Evans did at the Knowledge Lab to investigate the power of diversity to generate more robust results, but it took them outside of the sciences and into the realm of politics.

**James Evans** [18:43]: We're not just interested in science and technology, but also civic knowledge.

**Host** [18:47]: Mm-hmm.

**James Evans** [18:47]: I mean, what do people believe about the world? How does that impact their actions that they take in the context of public health crises and even, you know, following and creating laws, right? That are, that are useful, and conventions.

**Host** [19:00]: Evans wanted to know if diversity of political opinion would lead to better knowledge creation. So to find answers, they turned to Wikipedia.

**James Evans** [19:08]: So one of the things that we explored in the context of Wikipedia was do diversities, in this case political diversity, the different exposures to knowledge that, uh, different political positions would have, would make stronger, more robust pages that were perceived as higher quality by independent evaluators?

**Host** [19:26]: Basically, are Wikipedia pages that were written by both right-wing and left-wing people more accurate than pages written by just one side or the other?

**James Evans** [19:35]: And that was exactly the case, and we showed that when that's controllable, the conversations between people with these diverse knowledge exposures do, uh, end up producing more even-handed, thorough, deep, clear, you know, knowledge products in this context.

**Host** [19:51]: In a world in which politics seem to be ripping our country apart, the results of this paper beg the question, could harnessing the power of diversity underlying political polarization actually be useful?

**James Evans** [20:02]: One of the critical things now is for us not just to think about these issues in the context of science and, and technological advance, but also in the context of civic knowledge more broadly. I mean, our governments are inventions and, you know, we're all engaged in the project and the collective action of kind of supporting and breaking down and kind of building anew these kinds of institutions. And so I really feel like for, um, understanding knowledge more broadly, we need to, to think of these things in similar ways and really, you know, try to explore and support, I would say, the science of democracy. You know, the science of, you know, these kinds of social inventions, which are so critical for continuing support and, uh, sustaining of, of technological and scientific advance. These are even more critical, right? The, the... If, if they're not present, you know, they're the things that fund other classes of discovery, and they operate in, in similar ways. And so it's, you know, critical to understand, you know, how all these things fit together. That's what's gonna support the long-term, uh, ability to bet, you know, on science and technology.

**Host** [21:10]: Evans wants to take the power of diversity beyond just independent versus concentrated teams or taking bets on field-mixing studies. Way beyond. He says if we really wanna supercharge our ability to make new discoveries, we may need to create whole new intelligences, intelligence that are so diverse, they don't even think like us.

**James Evans** [21:29]: Well, I think there are a couple of frames of, of AI. I would say the classic framing of, of artificial intelligence in 1955, you know, when it was the basis of a conference at Dartmouth, and, uh, the idea was that we're gonna try to create intelligences in the kind of the Alan Turing model, like following the imitation game idea, you know? That we're gonna try to create intelligences that can think creatively like humans think creatively, that can solve problems like humans solve problems, that we're really gonna create artificial humanoid and human intelligences. And I think, you know, we're in a different place today, uh, for, I would say, competing, including competing against nature or for creating something that's fundamentally complementary to human intelligence and capacity. We, we might wanna do something that may be close to the opposite of that, which is to say, to understand how it is that humans individually and collectively think, and then build alien [laughs] intelligences, alternative or complementary intelligences that can maximize our capacities by doing things that we can't do.

**Host** [22:32]: Give me an example what a, of a opposite of human intelligence could operate like and how it would work.

**James Evans** [22:38]: I have one example that we've recently engaged in that, that works, you know? So I mentioned how we were improving our predictions. So one of the things we, we thought at that point, so if we just follow where scientists are gonna go in the next period, we can dramatically improve our prediction of future scientific discoveries. But it becomes a little less thrilling when you realize that you're predicting that because you're predicting the activity that inertial scientists are gonna make in the next five or 10 years. I mean, you're basically scooping scientists, and it's not, it's neither an ethical, in some ways, or an efficient use of computational intelligence. So we thought, well, what if we actually tried to avoid scientists in this space? So if we actually tried to identify potential discoveries that are equally scientifically promising but are not likely to be discovered just because the distribution of people are not sitting there to make those inferences.

**Host** [23:32]: Okay.

**James Evans** [23:32]: Uh, so it's kind of like it's, it's imagine the world is as it is, except we just, we bet on different disciplines. And so if we build a set of predictions from that and then we, we took these first principles simulations of these properties, which are used in the sciences, in material science, in genetic medicine, to predict the efficacy, for example, of these things, and we look at the discoveries that are made by these alien intelligences, they end up being much more likely even than discoveries that are made, uh, and published in the scientific literature.

**Host** [24:03]: Much more likely to be successful?

**James Evans** [24:05]: Uh, much more likely to be successful as, as gauged by these first principle simulations of these properties. So which I would say is a conservative standard. I mean, that's based by scientists in these fields. So I think that, you know, even based on existing theories, these things that are discovered by aliens that are very unlikely to be discovered by any particular person because there's no person who sits there to make the-

**Host** [24:27]: I see. Okay

**James Evans** [24:27]: ... the inference, are more likely, and the reason they're more likely is because of, again, diminishing marginal returns, you know, to, to theory. These are things that if they would be discovered, the things that, that we discover through this method are are not discoverable for, you know, for years and sometimes decades after because the whole system of science has to reconfigure and educate people who sit in those boundaries for anyone to be able to discover that, that possibility. So I mean, we're certainly exploring and promoting this, and I think we're also interested in the idea of looking at fundamental human limit- limitations of capacity.

**Host** [25:11]: Out of all of these concerns, there's one that Evans says is the most fundamental to holding us back from creating a system focused on innovation. Just as it's fundamental to each of our individual brains, the brain of our system of science suffers from it, too: the fear of failure.

**James Evans** [25:26]: We need to invest in failure. So I think this is a deeply challenging issue, is that so for, you know, places like the National Science Foundation or the National Institutes of Health, they don't want some senator or congressperson, you know, looking, digging up grants, coming up with seemingly ridiculous, uh, and, and ultimately failed approaches that got funding from the federal government. But we know from our research that these failures are tightly and highly correlated with dramatic success.

**Host** [25:56]: But that failure is antithetical to the professionalization of science. Failure means jeopardizing your tenure track or making your research institution look bad, or having to justify a failed project to funders.

**James Evans** [26:08]: Those are people's careers. Those are institutions' reputations, right? Those are big funding institutions' habits. And so breaking these down is, is a challenge. One of the things that we see is that institutions defend their- themselves. You know, once you have a success, that in some ways decreases the likelihood of another dramatic success because it-

**Host** [26:28]: Mm-hmm

**James Evans** [26:29]: ... it has the potential to destroy all the capacity that was in the prior thing. This is this idea-

**Host** [26:33]: Yeah

**James Evans** [26:33]: ... of creative destruction. So this is the challenge, is to build basically a, a kind of a scien- you know, a technoscientific, um, environment where we're surfing that boundary between order and chaos, where we're basically undertaking, uh, and willing to undertake future potential failures, and with the not only the willingness but the expectation that successes, dramatic successes are going to, to deconstruct the value of prior successes.

**Host** [27:01]: So the... If, if you were gonna get to... Is it that you have to get to the funders more than anyone else to get them to ask for something different than what they're currently funding and what they're currently being pitched? Is that the crux of this?

**James Evans** [27:14]: I think that the funders are, are a critical place to, to be, and the reason is exactly as you suggest. I mean, right now if the incentive is, you know, for people to survive to do really incremental and conservative science, that's what we're gonna produce at a large scale unless the funders, who are really, you know, driving in many areas, not all areas, but in mar- many areas of science, um, advance, then, you know, they're gonna have to make commitments. And, uh-

**Host** [27:42]: Yeah

**James Evans** [27:42]: ... and those commitments are gonna have to be, you know, rather than just funding the marginal discovery in this big institute, we're gonna have to fund another approach, uh, that's independent of that. We're gonna have to fund people that don't come from that network of highly previously successful persons. Uh, all these bets, uh, are going to, uh, are gonna entail failure. A- and so, um, so I think really part of it's a public education campaign, not just to funders but to society. Society has to understand that if we want to fund innovation, we, we have to fund failures, that, that, that the- these things go hand in hand. Failures are not a sign of failure as an institution. I think that's probably one of the biggest challenges.

**Host** [28:30]: Have you ever wondered what goes on inside a black hole, or why time only moves in one direction, or what is really so weird about quantum mechanics? Well, you should listen to Why This Universe? On this podcast, you'll hear about the strangest and most interesting ideas in physics broken down by physicists Dan Hooper and Shalma Wegsman. If you want to learn about our universe from the quantum to the cosmic, you won't want to miss Why This Universe?, part of the University of Chicago Podcast Network.

**speaker_2** [29:04]: Big Brains is a production of the University of Chicago Podcast Network. If you like what you heard, please leave us a rating and a review. The show is hosted by Paul M. Rand and produced by me, Matt Hodapp, and Leah Ceasrine. Thanks for listening. [outro music]

