---
title: "Mathematical modelling with Lisa Jardine"
person: kenneth-cukier
section: by
type: talk-transcript
year: 2013
venue: "BBC Radio 4, Start the Week"
source_url: https://podcasts.apple.com/us/podcast/mathematical-modelling-with-lisa-jardine/id131131620?i=1000353663125
retrieved: 2026-08-14
content: full-text
transcription:
  method: asr
  asr_model: elevenlabs-scribe_v2
  diarized: true
  speaker_labels: inferred   # ASR diarization + LLM naming (claude-sonnet-4-6); not ground truth
  duration_min: 45
notes: "PROVENANCE: machine-transcribed from AV via ElevenLabs Scribe v2 (diarized) + LLM speaker-naming pass. Speaker labels are inferred, not authoritative. Layer-2 (mildly lossy) per charter, not camera-raw."
---

# Mathematical modelling with Lisa Jardine

*Speakers (inferred):* speaker_0=Narrator, speaker_1=Unknown, speaker_2=Unknown, speaker_3=Unknown, speaker_4=Lisa Jardine, speaker_5=Kenneth Cukier, speaker_6=Tiffany Jenkins, speaker_7=Marcus du Sautoy, speaker_8=James Weatherall

## Transcript
**Narrator** [00:00]: This BBC podcast is supported by ads outside the UK.

**Unknown** [00:05]: [electronic jingle]

**Unknown** [00:06]: At McAlister's Deli, strangers are just regulars visiting for the first time because the food we serve is food that brings people together. With a huge variety of craveable sandwiches, giant spuds, and handcrafted salads, there's something that everyone will enjoy. Come eat with us and enjoy our famous iced tea on us when you sign up for McAlister's Rewards. McAlister's Deli, taste togetherness. Click the banner now to sign up for McAlister's Rewards. Terms apply. See McAlistersDeli.com for details. Free tea offer conditions apply.

**Narrator** [00:36]: Struggling with addiction? Finding hope can feel impossible.

**Unknown** [00:39]: At Bel Air Recovery Center, we're here to help through personalized treatment plans and a thorough assessment at each stage of recovery. From medically monitored detox to residential care and aftercare support, Bel Air Recovery Center is here for you twenty-four/seven, and we accept most private insurance, including VA and TRICARE. Call eight eight eight two zero one nine two six six or visit BelAirCenter.com. Bel Air Recovery Center, transforming lives with compassion and care.

**Unknown** [01:07]: [electronic jingle]

**Narrator** [01:09]: Thank you for listening to this download of Start the Week, presented by Lisa Jardine.

**Lisa Jardine** [01:14]: Hello. When the English stock market crashed in seventeen twenty, Sir Isaac Newton, who lost twenty thousand pounds, is supposed to have said, "I can calculate the movement of the stars, but not the madness of men." Today, we regard science and mathematics as the key to economic recovery and a proper understanding of how the world works. Was Newton wrong? Or do we risk further calamities like the financial crash of two thousand and eight if we allow mathematical models to decide how financial markets will behave? Should we be worried that companies can mine vast datasets to predict our future behavior or follow our every move? To try to answer some of these questions, I'm joined by Kenneth Cukier, data editor of The Economist, who writes widely on technology, business, and economics. James Wetherall, assistant professor of Logic and the Philosophy of Science at the University of California, Irvine. Tiffany Jenkins, an independent sociologist and cultural commentator, and Marcus du Sautoy, professor of mathematics at the University of Oxford and an eloquent advocate for the power of numbers since his best-selling book, The Music of the Primes. Kenneth Cukier, let's start with you. In your new book, Big Data, the subtitle, one of those long subtitles that allow the search engines to creep over [chuckles] and find all the key terms, um, the subtitle is A Revolution That Will Transform How We Live, Work, and Think. That's quite a big claim. Could you start us off by explaining what we mean by big data?

**Kenneth Cukier** [02:47]: Yeah, absolutely. So we've always had information around, and for most of the time, we've had lots of data as well. But new technologies have allowed us, and new mindsets have allowed us to do new things with it that we weren't able to do in the past. What we're finding is, first, we are able to take more data about something that we've already been collecting in the past, but g-getting not just a lot more data, but vastly more data. Secondly, we're able to take things that had never... had always been informational in a way, but had never been rendered into data form, and we're now starting to put a datafied, quantified element to it. And when these things get married, and we have the new technologies that allow us to parse this information really well, we can do some radically new things.

**Lisa Jardine** [03:30]: Could you-- Okay. C-could we have a simple example of-- No, if I say simple, that's not fair. Could we just have an example, um, of, of how that works? And perhaps you could just say before you give it to us, what sort of orders of magnitude are we talking about, about the increase in data? Just to give us some idea.

**Kenneth Cukier** [03:47]: Oh, yeah. Sure. I mean, one very basic way of thinking about it is that, um, the Library of Alexandria, about five hundred BC or so, uh, was known to contain all of the written heritage of the world. We now have about a couple hundred Library of Alexandrias for every single individual in the world, and that number is, is growing at a preponderant rate, and it's actually increasing as well, the pace with which it increases. Roughly the amount of information in the world doubles about every three or four years. Th- Some statistics look in other directions, but that's the most conservative.

**Lisa Jardine** [04:21]: And companies like Amazon can suck up all that data and, and combine it, and then you've got a-

**Kenneth Cukier** [04:28]: Yeah

**Lisa Jardine** [04:28]: ... vast repository.

**Kenneth Cukier** [04:29]: Let's just look at Amazon as one short example right now. Books-- People have always gone into bookstores, they've browsed, and they've left. They may have looked at six books, they bought one. The bookstore, if they wanted to really match and know their customer, would look at the data on that one single person and learn something about their traits and who they were and what they might be interested in for other books. Amazon can look at not just what you purchase, but what you've only looked at and browsed. They know for how long, they know where you were when you did it at the time. They may know what page you were at before on the web and where you went afterwards. All that information are signals, if you mine it correctly, to give you a profile of the person and sell them more.

**Lisa Jardine** [05:06]: Now, can you give us an example of that data mining which yields some interesting result?

**Kenneth Cukier** [05:11]: Yeah. Sure. What we're finding is that we can reuse data in innovative ways. So one example is Google Flu Trends. Our interaction with Google is basically we put in a search term, we get a response, and it seems, as a consumer, that our interaction with the company is over. But Google collects all of this data and stores it forever. It's in an anonymized or quasi-anonymized form. Nevertheless, what they're able to do is go into the past searches, and they, what they did a few years ago was match searches of the, they get about a bill- a few billion a day, with the correlation of where flu was in America on a regional basis. Now, often, if you think you were to find out, if you were to use Go-Google searches as a proxy for where flu is, we would have to think together in a room what are the terms that would most likely correlate with this. That's not what Google did. What they did is they let the data speak for it its- for itself. They just ran the correlation about a, a list of about 500 million terms on a weekly basis through lots of mathematical models. Happened to be 450 million mathematical models. There you have it. What they were able to find is that they were able to correlate where, in a very strong correlation, where flu outbreaks were going to be at, in quasi real time.

**Lisa Jardine** [06:27]: Because of what people were ordering, because they were ordering flu remedies ahead of time?

**Kenneth Cukier** [06:33]: Well, that's our innate human sense of causation. We want to presume that this is because they're looking for search terms, uh, uh, flu-related terms. And in truth, if you look at the terms, many of them are search-related terms. In the top 100, there was the term college basketball, and the reason why is it's played in the winter, and it, and it happens to correlate with the seasonal outbreak of the winter flu. However, the-- but that was not... Google cut it off after 45 terms, so that was not part of their model, and the reason why is when they put in these other terms, although there was a strong correlation, it lessened the strength of the model.

**Lisa Jardine** [07:08]: Now, you, you, you spoke there about, uh, I'd done the classic human thing of looking for causality, looking for a, a reason why, uh, w-one of the terms that came up in that top 45, um, would correlate with flu. Um, say a little bit more about the way in which this way you are proposing of mining data, uh, these, these big data, um, data sets, uh, is actually doing away with that idea of causality.

**Kenneth Cukier** [07:37]: Well, what we're able to do is when we have many, many variables, we have to give up a degree of understanding in terms of how the world works. We have to let the data speak for itself. We like to see things ourselves as human beings, uh, why a drug may work, why it may not, but the fact is reality is very, very complex, and we often mislead ourselves. That's one reason why we put drugs on the market, and then we have to backpedal and take them off the market. When we trust the data and look at the data, it is a little bit less biased in some respect, not in all respects, but in some respect than we are, and therefore it can find correlations that we simply as human beings can't because we have limited capacity. In a small data universe, the one we lived in up until very recently, we could sort of interact with the world and try to get highly curated data because we didn't have that much of the data. But now that the vast amount of data has expanded, we now have to give it to the machine to do what it does best, and that is parse through it to come up with insights.

**Lisa Jardine** [08:36]: Now, inevitably, you're sounding pretty evangelical there, so I think I'm gonna ask Tiffany, who I'm sure is much more skeptical about this, uh, perhaps to ask you about those, those wonderful correlations that we would never have noticed.

**Tiffany Jenkins** [08:48]: Well, I do think the claims for big data are outlandish and probably wrong. Um, I think there's a number of assumptions at the heart of your book that I would want to question or certainly unpick. The first is that, um, you can measure everything, that more is measurable. The second is that data is the same as knowledge. Now, you talked just now about the Library of Alexandria and compared it to the immense library now that we have of our own selves. What's more important and what's more interesting? Well, probably the Library of Alexandria. More data doesn't mean more knowledge. But I think the central problem I have with your thesis is this idea of letting the data speak for itself. You mention that a lot in the book, and you argue that data is predictive. I think what there is a danger of is a kind of data determinism, a dataism. I think human beings have to interpret and analyze the data, and if it's to have any application, we do have to understand causality.

**Lisa Jardine** [09:41]: Kenneth Cukier, do you want to come back on that?

**Kenneth Cukier** [09:44]: Yeah. Uh, there's a few things there. L-Let me first go into, uh, whether more, uh, gives us everything. If we, we will never absolutely get all of the data. We, we never can, so that's really not the goal. Whether data gives us knowledge, it c- it can if we want it to. So let me give you an example. For years, captains have been in, in, on the high seas were writing their captain's log. They were looking at the winds, and they were looking at the waves. But still, for most of time, people, mariners felt that the winds and the waves were unpredictable, and the oceans were a chaotic and difficult place where it was just random. What a fellow was able to do in the mid 1800s in America was to take all of the captain's logs going back about a century that he could get his hands on and extract the data from it, the temperature of the ocean at the time, the direction of the winds, the, the direction of the waves and the currents, and he was able to spot, if you will, the patterns of the sea that wasn't apparent to any singular person at any time. But when you aggregated all of this data, nature no longer looks so random. We could now wrest it under human control. We could tame it by human hand, not entirely, but just enough so that we could have a safe passage. That is, if you will, an early precursor of big data, and that's simply what we're talking about, that we can extract meaningful insights. Not to-- we don't know why the currents work in the way they do, but if you're trying to get from New York to Rio de Janeiro, and it's the mid 1800s, you'll probably have a safer voyage by listening to the data.

**Tiffany Jenkins** [11:17]: The example you give, you put human control at the center of it in terms of understanding and application, but I think in your book you argue against human judgment, and you point to the demise of expertise.

**Kenneth Cukier** [11:29]: Well, I, I don't see the two things different in the way I've just described it, and the reason why is in the past, there was always a salty dog who would tell you you needed to travel, you know, completely to the east, uh, to get to the south of the equator and then to, to jerk back right, uh, to the west to get to Rio de Janeiro from New York. It happened to be a very difficult passage, mainly because, uh, sailors would throw themselves into the most asinine routes. What we found was a straight shot south was fine, but our human judgment was fallible. We didn't know that. It was based on sort of instinct and intuition or reading tea leaves. But when we just learned to listen to the data, we were able to come up with insights that were more valuable that saved lives.

**Lisa Jardine** [12:09]: Marcus du Sautoy, I actually wonder if you could take us forward because we're, we're, we're going to be moving into another mathema-- application of mathematics. Maybe to sort out for us, uh, what I think is a distinction between, um, the huge datasets and the, um, the sorts of, um, uh, technology you have to use to, to mine them, and the mathematicization, which I think Tiffany, um, was having trouble with, uh, which sounds as if it's going to ovew-overwhelm all human activity but, in fact, does something else.

**Marcus du Sautoy** [12:42]: Well, I mean, I think, uh, one has to come back to what pa-- mathematics is about, which is, um, mathematics is really the search for pattern and structure and order and trying to navigate the world around us. It's how our brain evolved. I mean, we're, we're all essentially mathematicians at heart 'cause that's how we interpret the world around us. And the more information you have, uh, the more you're going to be able to, to, to make that analysis. Now, I think at the moment it's about choosing your battles carefully. I mean-

**Lisa Jardine** [13:07]: Mm.

**Marcus du Sautoy** [13:07]: If you take something like, uh, Nate Silver's, uh, predictions of the American, uh, US election, he seemed like some sort of magician. But no, all he said was that, you know, everyone's taking these polls, why not let-- put all the polls together? You've-- I mean, basically, what's an election? It's just counting number of votes. So if you've already got a huge number of votes, you're going to get much more insight. And so he, he called all, all states correctly. But, um, so I think it's, uh, it-it's about which, which things actually are, are you likely to win on. I mean, one of the things I think, uh, if you take something like the Large Hadron Collider, huge amount of data there. But if you didn't know what you were looking for, and this is, I think, the role of the mathematician in big data, is to be able to, to s-- to, to know where to look sometimes. How do you spot a pattern? And, and often randomness can produce things which look like patterns which aren't real. I mean, a great example is, um, the Bible code. I mean, there you've got a huge amount of data, the Bible, and you say, okay, are there messages hiding inside here?

**Lisa Jardine** [14:03]: Mm.

**Marcus du Sautoy** [14:03]: If you do your statistics badly, you'll come up with correlations between, um, you know, uh, rabbis' deaths, uh, dates of death and their names in the Bible, but that's a, a false correlation. You can find the same in Moby Dick. So, um, so I think, y-you know, it's the, the idea of correlation is very powerful, but it, you know, there are examples where it's misleading.

**Lisa Jardine** [14:21]: And could you, could you maybe just give, maybe this is too much to ask of you, but [laughs] maybe you could, uh-

**Marcus du Sautoy** [14:27]: I'm not even gonna go.

**Lisa Jardine** [14:27]: Because I'm going to move forward to an application of mathematics to systems of human behavior, um, uh, which, um, is tried and tested, as it were. Um, just give us-- I think it's hard for non-mathematicians to have any idea in their head about what it would mean to look for a correlation or to find a correlation or to devise an algorithm that, that, uh, that searched for these, uh, these relationships. And the reason I ask that, um, is that there is a slight sense of pulling rabbits out of hats. And I think the reason that, um, uh, that Tiffany is nervous about— I'm putting words into your mouth. I'm really sorry, Tiffany. Um, uh, uh, nervous about pulling out false correlations is because we don't really have a sense of how the controls are built into the systems.

**Marcus du Sautoy** [15:16]: Well, I mean, yes, mathematics is about producing models in a way to try and understand, um, what, what, what might happen next. I mean, that's what we're ki-kind of all after. We're trying to predict the future from, uh, looking at the past. And of course, um, those models, I mean, the correlation that you might pick out might be, um, not-- You might not have s-- had enough insight into what or a situation, an outlier, which might send things in a completely different direction. So, so it's all m-- I, I mean, actually big data is nothing new. It's how we've done science for, for, for centuries. I mean, we, we look at, um, the data. We try to, to find some connection between it. We do the what, and then we try and do the why. I mean, I think, uh, y-y-you know, the, the idea that we should throw away the why. No, the point is that, um, let's do the what and then try and understand the why because it'll take us somewhere new.

**Lisa Jardine** [16:03]: Okay. That's a perfect moment, I think, for me to move on. Um, now, if you took a poll of the most untrustworthy occupations these days, it would be bankers and economists who were up there with politicians and journalists. But what do we think about physicists? Are the men in white coats above the hurly burly of eco-

**Marcus du Sautoy** [16:22]: They're not in white coats. Uh, that's a real-

**Lisa Jardine** [16:25]: [laughs]

**Marcus du Sautoy** [16:25]: Or, uh, okay, you're, uh, uh, that's a, an image.

**Lisa Jardine** [16:28]: It's, uh-

**Marcus du Sautoy** [16:28]: Yeah, have I seen a white coat?

**Lisa Jardine** [16:29]: That's almost as much, that's almost as much of a trope as the idea that Newton said what I said in my intro.

**Marcus du Sautoy** [16:34]: Okay.

**Lisa Jardine** [16:34]: All right? [laughing] That's, that's the way we do it. Okay? Are the men in white coats or not in white coats, uh, and the women above the hurly burly of economics and politics? Don't they spend their days deep underground in Switzerland searching for the meaning of the universe? Not according to James Weatherall and his book, "The Physics of Finance: Predicting the Unpredictable," which celebrates the achievement of physicists, men of science, in the murky world of Wall Street. And James, you do this, um, in s-- in s-- essentially historically-

**James Weatherall** [17:06]: Mm-hmm.

**Lisa Jardine** [17:06]: Um, and taking us up, um, to the crisis of two thousand and eight. So perhaps you could tell us a little about the history of the way these men not in white coats and some women got into, uh, the, the, um, uh, got into the finance system.

**James Weatherall** [17:21]: Well, sure. Uh, so, so what I, uh, what I do in the book is, is look at, uh, a number of examples of people trained as physicists, trained as, as mathematicians, um, who at some point in, in their careers, uh, decided to, to try, try the, the, the tools of their trade, uh, in a, an entirely new, new domain. Uh, to, to try to apply ideas, methods from physics, from mathematics, uh, to understand financial markets. And, um, the, the really quite re-remarkable contributions that have come, uh, from f-far, far-flung pla-- far-flung places from the point of view of at least of, of mainstream economists and some of the most important ideas behind, uh, uh, modern financial practice really have come from physicists and mathematicians. Of course, not all of the ideas, but, uh, a shocking number of them.

**Lisa Jardine** [18:15]: As it were, physicists and mathema-mathematicians actually go into the, uh, stock market until they... And, and, a-a-and they actually become, um-

**James Weatherall** [18:24]: That's right. So th-there are, uh, sort of two, two separate strands here. O-one is how, sort of a history of ideas, uh, where-- What, what are the debts that modern financial theory, uh, owe to, to physicists and to mathematicians? Um, but then also, uh, how is it that, you know... So, so one thing we heard an awful lot about in, in two thousand and seven and two thousand eight, uh, was the role of quants, so-called quants, these, uh, highly mathematical traders and analysts who-

**Lisa Jardine** [18:51]: Yeah. So just so people understand-

**James Weatherall** [18:53]: Who are changing finance

**Lisa Jardine** [18:53]: ... 'cause we're getting all these things that-

**James Weatherall** [18:55]: Yeah

**Lisa Jardine** [18:55]: ... that we've ne- these are actually people, quants. They're people who-

**James Weatherall** [18:56]: Quants are people, that's right.

**Lisa Jardine** [18:57]: [laughs]

**James Weatherall** [18:58]: Uh, a-and in fact, there are a number of things in my book that, that turn out to be people that you might have not expected to be people. Um, computers, uh, in one chapter turn out to be people. Uh, the army at o-one stage of this ena-enormous data analysis.

**Lisa Jardine** [19:10]: Okay, but let's stick with quants now that we've got the hang of the fact that they are actual people-

**James Weatherall** [19:13]: Yeah, that's right

**Lisa Jardine** [19:14]: ... applying these models in the financial sector.

**James Weatherall** [19:17]: So, so, so, so quants are, are people who, uh, uh, have, have backgrounds in physics and mathematics and engineering. Uh, increasingly, uh, MBAs can be quants as well. Um, but, uh, we heard an awful lot in two thousand and seven and two thousand and eight about the role that they had played in the crisis, and, uh, one thing that became clear was that there were an awful lot of them. There were an awful lot of people working at Wall Street banks who didn't have backgrounds, uh, in, in economics or in banking, had backgrounds in, in science. And so that's a separate, a separate thread from the history of ideas. I talk about both in the book, and they're related to one another, of course. But, uh, uh-

**Lisa Jardine** [19:50]: And that fulfills Tiffany's worst fears, doesn't it? That, that, that, that the, that the men with the models got separ- uh, were men. Men and women with the models got separated from the, um, the human, intensely human area that they were involved with.

**Tiffany Jenkins** [20:05]: I think there's a real danger of naturalizing the economy and applying physics to the economy, and I think what you've done is conflate the financial markets where you can make money with physics, with the economy, which is a social and political project, and that needs to be subject to human intervention. That is really about how we want to run our world, how we want to run the economy. That's something that is debated within society, and it's something that physicists can tell us very little about, and relying on them will certainly not get us out of this financial mess that we're in now.

**Lisa Jardine** [20:34]: Kenneth Cukier.

**Kenneth Cukier** [20:35]: Yeah. Tiffany, would you, would you rather that we not use math to try to understand the economy?

**Tiffany Jenkins** [20:39]: I think we can use it to understand the market and financial markets, but in terms of how we want to run our economy, not really, no. That's a social and political question. And if you think where we are today and why actually financial markets arose, it was really as a result of decline in production in the nineteen seventies. That's where this all came from. What we really need to do is find a way to build growth. Physicists are not going to come up with that.

**Lisa Jardine** [21:03]: Marcus du Sautoy.

**Marcus du Sautoy** [21:04]: But there's a perfect example at the end of, uh, uh, of the book, um, which is where, uh, the US government decide they want to set, um, uh, inflation at a particular value in order to save themselves money. And so they go in and they try and create in this committee, um, a formula. They, they sort of work backwards from the thing they want the answer to be. But actually that's gonna cheat people out of, um, th-e the, the in-inflation rate is related to, um, what your pension is going to be, uh, benefits and things like that. So, uh, if you actually use a mathematical model which was proposed by, uh, Weinstein and Milani, uh, using mathematics which gives you a-actually the, the truth of the situation of what, um, uh, inflation will be, you actually cut through the, the human intervention of politics trying to actually sort of, uh, engineer what they want the answer to be.

**Lisa Jardine** [21:50]: Marcus, you're a true mathematician. You just used the word truth about-

**Marcus du Sautoy** [21:54]: Oh, yes. Well, I'm in truth

**Lisa Jardine** [21:55]: ... your financial, your model.

**Marcus du Sautoy** [21:55]: Absolutely. Oh, gosh, yeah.

**Lisa Jardine** [21:56]: But James, James, I think we have to let James come back in.

**James Weatherall** [21:58]: Well, I just, I just want... There are just two things I wanted to say here. O-o-one is that, uh, as a matter of fact, ph-physicists have had an enormous contribution to just mainstream economics, uh, over the last, you know, hundred and fifty years or so. I mean, so, uh, for instance, the first Nobel laureate in economics, Jan Tinbergen, uh, was trained as a physicist. Um, the second, uh, Nobel laureate or winner of the second Nobel Prize in Economics anyway, uh, Paul Samuelson, was, his first book was, uh, he, he was a student of a student of the great American, uh, mathematical physicist, Willard Gibbs. Uh, and, and he, in his, his first book, uh, uh, started with a quote from Gibbs and, you know, talked throughout about the, the deep influence that, that Gibbsian, uh, thermodynamics had on his theories. And th-there's a long history here-

**Lisa Jardine** [22:45]: But, but, but James, we-

**James Weatherall** [22:46]: ... uh, mainstream economics.

**Lisa Jardine** [22:47]: Yeah. We broke into-- That wasn't quite fair 'cause we broke into your account, and I want you to talk a little bit about, um, uh, where you arrive after, uh, in, in the, towards the end of your book, which is that, that what went wrong in two thousand and eight was not the physicists and their models, but that, but that those who were applying the models were not physicists enough. Could you say something about that?

**James Weatherall** [23:07]: Well, there's actually a bit of an irony here because I think that, that I agree far more with, uh, with Tiffany than, than maybe it, uh, it was seeming. Because I, I, I do think that, uh, what went wrong in two thousand and seven and two thousand eight, and in previous instances as well, nineteen eighty-seven, for instance, the Black Monday crash, uh, had a lot more to do with the misapplication of models than with failures of the models themselves. There, there's, uh, it's very easy when you have a piece of mathematics to, uh, allow yourself... I, I'm a big fan of the truth too, Marcus, but, uh, to allow yourself to think that it, that, that a, a piece of mathematics is the truth and nothing but the truth, the whole truth about whatever matter that you're, you're concerned about, that somehow you have a final theory that's telling you how markets work.

**Marcus du Sautoy** [23:51]: No, I agree.

**James Weatherall** [23:52]: And, and that's not right.

**Marcus du Sautoy** [23:53]: Yeah, I mean, these, uh, equations, like the Black-Scholes equation, tells you what an option... Yeah, I mean, it's, it's a model which says what an option some-something you can buy in the financial market should be worth. But it's only a model, and the models can be wrong, and the mo- and the, the, uh, f- the actual, uh, sort of system can change such that the model was right. So it's a constant, um, thing of updating the model, which is of course what we do in science.

**Lisa Jardine** [24:14]: Now, okay-

**James Weatherall** [24:14]: Right. And in order to do that, you n- you need to have some sort of understanding of, of how you think the model represents the world and how it can fail to represent the world.

**Lisa Jardine** [24:22]: Okay. Now, who around the table wants to give a very quick, um, account of how models now are somewhat self-correcting, and, I mean, uh, how you can, you can iterate in order to, uh Modify your model so that it is, I think it's probably James.

**James Weatherall** [24:39]: Well, I, I don't think they're self-correcting at all. I mean, I, I, uh-

**Lisa Jardine** [24:42]: Well, except I think Ken might say they were. They are.

**James Weatherall** [24:45]: Yeah, I know, but Ken, Ken-

**Lisa Jardine** [24:45]: Okay, well, let James start. We'll let James start, and then I want to have a word from Kenneth because the big data man I think might dis-disagree there.

**James Weatherall** [24:51]: Uh, well, so may-maybe there, there, maybe there's a distinction to be made. I mean, there are different things that can, can, uh, uh, count as, as models. Uh, and but the, the kinds of things that I'm thinking about, um, really aren't self-correcting. They're, they're, uh, they're models that, uh, uh, are based on, you know, strong simplifying assumptions and idealizations about how markets work. Uh, they're, they're great approximations in, in some regimes, but n-n-not all the time. And we really do need-- There really is an important place for the human element to, to interpret models, to interpret market conditions, and, and to make decisions about, uh, when a model is appropriate to use.

**Lisa Jardine** [25:30]: I can see Marcus nodding like crazy, and I know that's partly because he's trained some of these, uh, people who are-

**Marcus du Sautoy** [25:35]: [laughs] Yes, yes, all, all, all my postdocs go off and leave, uh, mathematics and go into, uh, making money.

**Lisa Jardine** [25:40]: Tiffany, just before I ask Kenneth. Yeah.

**Tiffany Jenkins** [25:41]: I j- I just want to come back to something you said, Marcus, which was a dismissal of the American politicians. And I'm all for doing that. I think they made the wrong decisions, but they're the ones who have to make the decision about where to take the economy. They know better about what future they want for American society, and they are elected, whereas mathematicians are not.

**Marcus du Sautoy** [25:57]: Yes, but surely they can make a decision much better based on, um, uh, as much information as possible and as much information which is going to actually, uh, tell you, uh, uh, how things are rather than how you want them to be.

**Tiffany Jenkins** [26:07]: Those models aren't telling them how to create growth.

**Lisa Jardine** [26:10]: But I-

**Tiffany Jenkins** [26:10]: That's what they're avoiding.

**Lisa Jardine** [26:11]: Yeah, I'd like to come back to that. Maybe we could come back to that in a few minutes about the who does it and what are the, uh, some of the, um, ethical and political implications. But if I could, I really would like just a word from Kenneth because, um, uh, you know, it seems to me that what I'm hearing from the, the, the hard mathematical models in the financial sector is different from what you were saying, for instance, about the Google Translation machine.

**Kenneth Cukier** [26:32]: Right. Okay. So, uh, first, as a, as a, as a quip to our conversation about models, a famous mathematician of the twentieth century, George Box, said, "All models are wrong. Some are useful."

**Lisa Jardine** [26:43]: Mm-hmm.

**Kenneth Cukier** [26:43]: Right? So we're never gonna have all of the, um, of all, all of the data. Now, Google Translate is very, uh, uh, Google Translate is very interesting. What we try to do for translation is try to understand what a word means in one language and another, and teach a computer to think like a human being to figure out how that worked. But a shift took place because that wasn't really working very well. It's just hard to do because it's just so myriad. It's a big problem. So instead, what we did is we fed the computer lots of data. We looked at, in this case, uh, the Canadian parliamentary transcripts that are both in French and in English, and it was a real sea change. It became better because now it was just based on probability. It was statistical machine translation. It just looked at the frequency of one word in one language and whether what was the most likely word for the other. So an example in French, you'd have légère, and should that be, um-- or you'd have light in English, and should it be illumination or légère, right? Weight or illumination. That was good, but it wasn't great. We only had a couple million documents. But when Google got into the game a little bit later, they didn't have a million documents. They had trillions of documents. They used the entire global internet. They looked at every document from the EU in all twenty-one languages when it was translated that way. They looked at, in the Google book scanning project, every translation of the book they translated. They looked at all the corporate websites that have very high-quality translations. Dealing with preponderantly more data, orders of magnitude more data, allowed us to give up the benefit of having highly curated, accurate data, and instead, with the messy data, get much better translations, and that was the sea change. It was a pr- branch of artificial intelligence called machine learning, but if you really under- want to understand what it is, it's just probability. It's just math. The computer doesn't have to understand language anymore.

**Lisa Jardine** [28:25]: Yeah, but people, I think the, uh, I think the phrase computer learning sits nicely alongside the other model that James and, and Marcus were, were sort of talking about. So I think that, that takes us to a reasonably good place, although I would have loved-- and maybe we'll have time for you to say a little bit more about messy data, which seems would maybe... Um, so, um, but, um, I'd like to move on and really ask a broader question, which is the question that's circulating around this table already, which is, are we living in an era where science and mathematics is going to be our guide for the answers to the big questions? Um, is it going to be science and mathematics that make the money and predict the future? And is that all that we want out of our knowledge gathering and, uh, sifting and model building? Um, so I think, uh, Tiffany-

**Tiffany Jenkins** [29:12]: Yeah, I think that's a really good question. Um, I've been really struck in recent times by the use of, by politicians of things like evidence. The evidence shows, the evidence base for this is. And in my field where I research, I research the arts and how we value them, there's been a kind of creeping instrumental, um, measurement discourse. So everybody wants to measure everything. So they're bringing in any kind of semblance of maths and science to these areas which previously wouldn't have been interested in them, and I think we have to ask why. I think what's happened is that kind of political questions, social questions, and artistic questions have been kind of made feeble. They're in retreat, and that's why they've embraced this kind of idea, this appearance of certainty. But while science and maths can bring certainty s- to some areas, it can't to the more social and human areas, and that's where it's dangerous. So I, I don't necessarily blame science and maths. I think the geeks finally think that this is their time, and I don't blame them for that.

**Lisa Jardine** [30:07]: [laughs]

**Tiffany Jenkins** [30:07]: But the reason is, is that they're being invited in, and they're being invited into areas where they really have no application.

**Lisa Jardine** [30:13]: Now, I think that's a very, very interesting question. Of course, it takes us beyond. Yes, uh, Kenneth.

**Kenneth Cukier** [30:16]: Yeah. Um, I agreed with all of it except for the very last thing you said, that they're invited into areas where they, quote-unquote, "Have no application." I think they have a great application. I agree that we should be on guard. However, I think that, um, uh, the application is actually quite good as long as it's done in the right way, uh, and not, and we don't divorce our judgment to the data, but that we marry the benefits of using the data with what our rea- sensibility and reasonability tells us.

**Lisa Jardine** [30:42]: I have a suspicion that one of the things that underlies, uh, Tiffany's, um, uh, remarks is that, um, try applying for a humanities grant from a grant-giving body at the moment. Unless you can quantify what you're doing, you don't stand a hope. There are-- Marcus du Sautoy.

**Marcus du Sautoy** [30:56]: Well, I, I think that is a, a real big danger because science has become extremely sort of powerful. It, it's, uh, you know, a lot of governments are realizing that that's gonna be, uh, you know, the secret to boosting the economy and things. But I think that, uh, as a scientist, I, I think we will lose, um, uh, a lot if we don't s- talk to the humanities and the arts, um, uh, i-in a sort of, uh, uh, as a, as a partnership. I mean, I'm doing a lot of projects at the moment. I'm doing a project at the, um, Barbican, uh, looking at one of the big questions of science, which is, uh, what is consciousness? Um, and I think that the point is that, uh, uh, we have certain ways of looking at things, but so does a, an artist. I'm working with James Holden, who's a composer, also a mathematician by training. But, um, but the, it's great because as an artist can ask me new questions about a subject like consciousness that I haven't ever thought about. We get very boxed in, in the way we think about things. And so I think we, we sort of, uh, um, let the The humanities and the arts wither at science cost.

**Tiffany Jenkins** [31:53]: There is a danger with the question of what is consciousness, um, that you locate it solely in the brain. Whereas-

**Marcus du Sautoy** [31:59]: Well, I would do that, actually. [laughs]

**Tiffany Jenkins** [32:01]: Yes. [laughs] That's why I'm saying-

**Marcus du Sautoy** [32:02]: But where would I... Where would you put it?

**Kenneth Cukier** [32:05]: Yeah. [laughs]

**Tiffany Jenkins** [32:05]: Well, I, I think it's a joint enterprise. Obviously, if you didn't have a brain, you wouldn't have consciousness. But at what point in humanity's development did we develop-

**Marcus du Sautoy** [32:12]: Well, that's very interesting, I think-

**Tiffany Jenkins** [32:12]: Did, did we develop a sense of self?

**Marcus du Sautoy** [32:13]: Well, I think this relates to big data a lot.

**Kenneth Cukier** [32:14]: There's a philosopher in the room. I feel like he's stepped in. [laughs]

**Marcus du Sautoy** [32:16]: [laughs]

**Kenneth Cukier** [32:17]: All right.

**Lisa Jardine** [32:17]: Let, let me referee here. Let me referee here.

**Marcus du Sautoy** [32:19]: Yeah.

**Lisa Jardine** [32:19]: Okay. So, um, uh, there was a slightly condescending note, Marcus, that I worried about in your, uh, in your contribution, where you kind of-

**Tiffany Jenkins** [32:26]: Condescending

**Lisa Jardine** [32:26]: ... you let us back in as a kind of, um, frosting and a cherry on the-

**Marcus du Sautoy** [32:30]: No, no.

**Lisa Jardine** [32:31]: Well, that was... So-

**Marcus du Sautoy** [32:32]: Oh

**Lisa Jardine** [32:32]: ... so I just, I just... Z- z- I, I mean, what we are not addressing or haven't addressed yet, and maybe it's, it, it, it runs alongside, I think, Tiffany Jenkins' strong, um, sense that, that the maths and, and, and number is, is drowning out a whole lot of crucial questions. There's a bit of triumphalism about, um, uh, both of, of your books, James Weatherall and, uh, Kenneth Cuvier. I mean, uh, yours in particular, Kenneth, you know, it starts terrifically triumphalist-ly, if that's a word. Um, by the end, you are being more concessive. But could you perhaps say something about the limits that would feed into Tiffany Jenkins' sense that we, we want a dialogue here?

**Kenneth Cukier** [33:14]: Yeah. Um, there's g... there's always been a temptation to lean on the data and let it make decisions for us because the world is a complex place, and the data can help us this way. But done in the wrong way, uh, it's gonna lead us down a lot of, uh, terrible places. We have experience with that. Of course, the Vietnam War in America in some ways is the first war fought over a data point, a statistic, and that was the body count. Uh, McNamara was a professor of statistics at Harvard. Uh, he was part of an elite team at the Pentagon during World War II that helped win World War II by being able to data-ize and inventory all of America's armaments and save money. And, and of course, modern warfare became, uh, uh, uh, about mobilizing resources, and who did it more effectively would win. And, uh, the success was phenomenal. He turned around Ford when he and the whole team went en masse to then America's most ailing company. By the time they got to the Pentagon, he had simply allowed the data and trusted the data to do things that it was never intended to do. In this case, the, the whole point of, of a war of attrition and using the, the data point of body count was atrocious and immoral and disgusting and wrong. Uh, and in fact, the data itself was wrong. So these two things compounded it that it, it was meaningless, and America only learned this much, much later because no one had the common sense to figure that out. And I do fear that in a world of big data, that we're going to multiply that problem manyfold. In today's Metro newspaper, the headline is all about predictive policing, that an algorithm of Big Brother is going to look at... is gonna identify future crimes and arrest people perhaps prior to those crimes being created. I mean, if you knew that the crime was likely there with statistical certainty, it'd be odd if you weren't to intervene with an arrest of some sort. So whether it's an arrest or not, just the police using this technology should frighten us. So I think what we need to do is carve out a place for the human, for the sacred, for the, for, for man's will or human will to intervene in the data as a stopgap measure so that we can learn from it in responsible ways. But we're not beholden to it, that we don't slaughter our judgment on the altar of data.

**Lisa Jardine** [35:19]: Okay. I want Tiffany to come back. There was still, I think, adding... We, we've still got human- humaneness as a bit of an add-on. So-

**Tiffany Jenkins** [35:24]: Yes. You, you kind of bring it in at the end as a kind of spell check almost. And I think it should be much-

**Lisa Jardine** [35:29]: [laughs]

**Tiffany Jenkins** [35:29]: ... much earlier on and far more central. I do think your points in the book about the authoritarian implications of this are very serious and should be taken on board, likewise the implications for privacy.

**Kenneth Cukier** [35:39]: Mm-hmm.

**Tiffany Jenkins** [35:39]: But I think what, what it ends up doing is just being inherently conservative because you follow the data rather than shaping the future, and that's why it's also a very big problem for politicians.

**Marcus du Sautoy** [35:47]: Yeah, I agree with that. I mean, I think that's the why. Uh, you've, you've still got to ask that why question because that can take you somewhere new. I mean-

**Lisa Jardine** [35:52]: Marcus, Marcus du Sautoy, why don't you say a little bit about how you're setting up what I take it is some sort of experiment in, uh, music versus, uh, let's say the, the, the brain math of the nematode worm or the brain math of the human brain.

**Marcus du Sautoy** [36:06]: Yes. Well, I think, you know, consciousness, the question of consciousness is one that we really don't understand. And I think actually it's interesting that, um, what we're looking for is something called the neural correlates of consciousness. So at the moment, we really don't want... know what it is. It's such a m- mystery. So we, we start with Kenneth's kind of, um, idea of, okay, we'll look for correlations. What do I need to take out, uh, uh, and still have consciousness? So you, you can remove the cerebellum at the back of the brain and, and still be conscious. Um, so that's a good start, and I think it sort of, uh, illustrates the idea of big data. But, uh, but eventually, you know, you might actually, uh... I mean, there's a project to, to actually make a sort of artificial brain. If you say where all of the neurons are, all of the connections, the synapses, a- and you, and the, the, the sort of logic map between how those might fire and things, would you actually have something which was conscious? Well, uh, I'm, I'm not sure you would. I mean, that's the kind-

**Lisa Jardine** [36:54]: I think you said the answer would be no.

**Marcus du Sautoy** [36:55]: Pro... Well, uh, uh, no, I think the answer is we don't know. No, I mean, I don't see why you're so, uh, adamant that it's, um-

**Tiffany Jenkins** [37:01]: And in what way are you testing? Okay. So it's provisional-

**Lisa Jardine** [37:02]: Tiffany Jenkins

**Tiffany Jenkins** [37:03]: ... and I take that you're open. But I think if you look at the development of humanity, there are two factors that are really important in terms of the development of consciousness. One is language. At which point does language give us a self-awareness? Would we have it without it? Obviously, we wouldn't have language at the... without the brain, but that's a kind of social communicative thing. Likewise, at different points in soci... uh, different points in history, you've had man more self-aware than others. And I think Harold Bloom makes the argument, and I think it's a bit overstated, that it is with Shakespeare you have the development of inner man.

**Narrator** [37:34]: Okay, so humanity and consciousness is historically constituted or at certain degrees of it is. So I think we have to see man as a social being as well as something that's just made in the head, made inside our brains.

**Lisa Jardine** [37:46]: James Weatherall, let me-- I want just to bring back in that theme of... So your physicists who are running the markets, I mean, they are in team-- they are in tandem with economists who are soft scientists who do have a sense of behavioral psych, who do include these other elements that are going to hopefully tether the models to the more humane side of... Is that wet of me to think that they might do that?

**James Weatherall** [38:12]: Well, there are a few things to say. I mean, one is that it's certainly the case that details of how people actually make decisions are entirely relevant. I mean, markets are, at the end of the day, a bunch of people-

**Lisa Jardine** [38:31]: Yeah

**James Weatherall** [38:31]: ... great apes [laughs] yelling at one another, right? [laughs]

**Lisa Jardine** [38:37]: And defaulting on their mortgages.

**James Weatherall** [38:38]: Yeah, that's right. And so, in fact, one of the striking things that I discovered in the book was that the very, very earliest, I guess actually the second earliest physicist to really come up with the idea that markets can be thought of as a random process, which is absolutely essential to much of modern financial theory, based it on an assumption that he took right out of psychology, something called the Weber-Fechner Law. Now, of course, that was obsolete psychology even in 1958 when he was working on it. But the idea that there's somehow a distinction to be made between the physics and the math and the details of behavioral economics, I think is a mistake. But actually, there's something else I want to say because I want to pick up on a line that Marcus started regarding the role of models in policymaking and in regulation. One of the things that I focus on at the end of the book is how these models can be used as effective tools, I think. Not in setting policy, but as a source of information for the people who have to make decisions about setting policy. And that seems to me to be extraordinarily important. If you want to make informed decisions, you should make them on the basis of all available information. That should include contributions from, as you say, Lisa, the soft sciences, although I think that if there were an economist in the room, she would probably object to that characterization. [laughs]

**Lisa Jardine** [40:12]: She'd probably accept it alongside you mathematizing one of-

**James Weatherall** [40:15]: [laughs]

**Lisa Jardine** [40:16]: Okay, now we've got Kenneth self-correcting or machine learning translation models. We've got Tiffany's Shakespearean language as being somehow unreached by the mathematical models. I want Marcus du Sautoy to bring us, to draw us to a close by saying something because it's music that you actually set side by side with scientific and mathematical models and tools. And could you-- Does that help us at all? Because I think with language we tend to get lost personally. Does it help us at all?

**Marcus du Sautoy** [40:54]: [laughs]

**Lisa Jardine** [40:55]: God, you've got two minutes. [laughs]

**Marcus du Sautoy** [40:58]: My feeling is about choosing your battles carefully. At the moment, there are things that we can use mathematics to really help us with. But maths is actually really easy. It's things like cats which are really difficult. I mean, I don't understand a cat at all. What's going on inside a cat?

**Lisa Jardine** [41:16]: Oh, Marcus, we're supposed to be understanding at the end of this. And now we've got into cats.

**Marcus du Sautoy** [41:18]: No, I think that's the point. The models at the moment are you use them where they're effective and sometimes-- But I don't think we should shy away from these big problems of what the hell is going on inside a cat's head.

**Lisa Jardine** [41:30]: So really, if I maybe presume to round off what we've been saying, we're all excited. I think I'm quite excited by these big data possibilities. I'm quite excited at the idea we might get a few more physicists into the financial houses so they might know what to do with them and all the rest.

**Marcus du Sautoy** [41:50]: Well, I thought they studied physics, but-

**Lisa Jardine** [41:51]: Well, I know, but there's no money in physics, is there?

**Marcus du Sautoy** [41:54]: [laughs] There are jobs in physics that are well paid.

**Lisa Jardine** [41:55]: And it's important, and it's very important, Tiffany's caveat. So we've got all of that excitement, and then we've got the huge world in which this is not all that is going to help us to an understanding of the world. And in a way, it's been three to one, and that's been extremely unfair. But it's probably, as Tiffany has told us, the way that the world is going. That is, for every three spokespeople we will get telling us that it is all to do with quantification and models, there will be only one of us allowed to come in and say, "But what about the heart, the soul?" [laughs] I hope that that is fair enough. So I think it just remains for me to thank all my spirited guests. Tiffany Jenkins, who would have loved to have come in at the end there, and I didn't let her. Her next book, Keeping Their Marbles, will be out in the autumn. Marcus du Sautoy, who's wonderfully presented his own billing of his lecture, a performance lecture on consciousness at the Barbican Center on the second of March. I've already booked. Kenneth Cukier's Big Data will be published next month. And James Owen Weatherall's The Physics of Finance: Predicting the Unpredictable: Can Science Beat the Market? is out now. Next week, Tom Sutcliffe talks persecution with James Lasdun, Mary Beard, John Gray, and Roxana Silbert. But for now, from all of us around this table, who are now going to go away and have a good further conversation about it, I have no doubt. Thank you and goodbye.

**Narrator** [43:28]: There's more information about Start the Week on the program's website. Go to bbc.co.uk, where you'll also find many more Radio 4 programs you can download for free.

**speaker_9** [43:37]: [upbeat music] Ever have that specific craving where only extra melty cheese or a cold glass of milk hits the spot? Yeah, that one. It's a staple for a reason, but it's about more than just the taste. It's the natural energy you get from thirteen essential nutrients, like the protein and calcium your body actually knows what to do with. It's real food from local Midwest dairy farmers who care as much about the land as they do their herd. For nutrition-packed recipes and more, visit usdairy.com. It's your cheat sheet for feeling good. Go see for yourself at usdairy.com.

**speaker_10** [44:10]: [upbeat music] Answer the call to care with Rasmussen University. Whether you're beginning your nursing journey or advancing your credentials, Rasmussen offers programs for entry-level roles to the highest level. You'll gain access to a thriving network of over thirty-one thousand nursing students, alumni, and faculty, and financial aid options for those who qualify. Plus, multiple start dates and entrance exam options mean you can start your way. Start building your future today at rasmussen.edu. [upbeat music]

