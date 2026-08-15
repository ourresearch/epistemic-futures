---
title: "[berkman] Stephen Wolfram – WolframAlpha.com"
person: david-weinberger
section: by
type: blog-post
year: 2009
date: 2009-04-28
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2009/04/28/berkman-stephen-wolfram-wolframalphacom/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [berkman] Stephen Wolfram – WolframAlpha.com

## Full text

Stephen Wolfram is giving at talk at Harvard/Berkman about his WolframAlpha site, which will launch in May. Aim: “Find a way to make computable the systematic knowledge we’ve accumulated.” The two big projects he’s worked on have made this possible. Mathematica (he’s worked on it for 23 yrs) makes it possible to do complex math and symbolic language manipulation. A New Kind of Science (NKS) has made it possible that it’s possible to understand much about the world computationally, often with very simple rules. So, WA uses NKS principles and the Mathematica engine. He says he’s in this project for the long term.

NOTE: Live-blogging.Posted without re-reading

Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

You type in a question and you get back in answers. You can type in math and get back plots, etc. Type in “gdp france” and get back the answer, a graph of the history of the shows histogram of GDP.

“GDP of france / italy”: The GDP of France divided by the GDP of Italy

“internet users in europe” shows histogram, list of highest and lowers, etc.

“Weather in Lexington, MA” “Weather lexington,ma 11/17/92” “Weather lexington, MA moscow” shows comparison of weather and location.

“5 miles/sec” returns useful conversions and comparisons.

“$17/hr” converts to per week, per month, etc., plus conversion to other currencies.

“4000 words” gives a list of typical typing speeds, the length in characters, etc.

“333 gm gold” gives the mass, the commodity price, the heat capacity, etc.

“H2S04” gives an illustration of the molecule, as well as the expected info about mass, etc.

“Caffeine mol wt/ water” gives a result of moelcular weights divided.

“decane 2 atm 50 C” shows what decane is like at two atmospheres and at 50 C, e.g., phase, density, boiling point, etc.

“LDL 180”: Where your cholesterol level is against the rest of the population.

“life expctancy male age 40 italy”: distribution of survival curve, history of that life expectancy over time. Add “1933” and adds specificity.

“5’8″ 160 lbs”: Where in the distribution of body mass index

“ATTGTATACTAA”: Where that sequence matches the human genome

“MSFT”: Real time Microsoft quote and other financial performance info. “MSFT sun” assumes that “sun” refers to stock info about Sun Microsystems.

“ARM 20 yr mortgage”: payment of monthly tables, etc. Let’s you input the loan amount.

“D# minor”: Musical notation, plays the D# minor scale

“red + yellow”: Color swatch, html notation

“www.apple.com”: Info about Apple, history of page views

“lawyers”: Number employed, average wage

“France fish production”: How many metric tons produced, pounds per second, which is 1/5 the rate trash is produced in NYC

“france fish production vs. poland”: charts and diagrams

“2 c orange juice”: nutritional info

“2 c orange juice + 1 slice cheddar cheese”: nutritional label

“a__a__n”: English words that match

“alan turing kurt godel”: Table of info about them

“weather princeton, day when kurt godel died”: the answer

“uncle’s uncle’s grandson’s grandson”: family tree, probabiilty of those two sharing genetic material

“5th largest country in europe”

“gdp vs. railway length in europe”:

“hurricane andrew”: Data, map

“andrew”: Popularity of the name, diagrammed.

“president of brazil in 1922”

“tide NYC 11/5/2015”

“ten flips 4 heads”: probability

“3,7,15,31,63…”: Figures out and plots next in the sequence and possible generating function

“4,1 knot”: diagram of knot

“next total solar eclipse chicago”: Next one visible in Chicago

“ISS”: International Space Station info and map

It lets you select alternatives in case of ambiguities.

“We’re trying to compute things.” We have tools that let us find things. But when you have a particular question, it’s unlikely that you’ll find that specific answer written down. WA therefore tries to compute answers. “The objective is to reach expert level knowledge across a very wide range of domains.”

Four big pieces to WA:

1. Data curation. WA has trillions of people of curated data. It gets it from free data or licensed data. Partially human partially automated system cleans it up and tries to correlate it. “A lot can be done automatically…At some point, you need a human domain expert in the middle of it.” There are people inside the company and a network of others who do the curation.

2. The algorithms. Take equations, etc., from all over. “There are finite numbers of methods that have been discovered in the history of science.” There are 5-6 millions lines of Mathematica code at work.

3. Linguistic analysis to understand the inputs. “There’s no manual, no documentation. You get to interact it with just how you think about things.” They’re doing the opposite of natural language processing which usually tries to understand millions of pages. WA’s problem is mapping a relatively small set of short human inputs to what the system knows about. NKS helps with this. It turns out that ambiguity is not nearly as big a problem as we thought.

4. Automated presentation. What do yo show people so they can cognitively grasp it? “Algorithmic presentation technology … tries to pick out what is important.” Mathematica has worked on “computational aesthetics” for years.

He says that have at least a reasonable start on about 90% of the shelves in a typical reference library.

Q: (andy orem) What do you do about the inconsistencies of data? We don’t know how inconsistent it was and what algorithms you used.

A: We give source info. “We’re trying to create an authoritative source for data.” We know about ranges of values; we’ll make that information available. “But by the time you have a lot of footnotes on a number, there’s not a lot you can do with that number.” “We do try to give footnotes.”

Q: How do you keep current?

A: Lots of people want to make their data available. We hope to make a streamlined, formalized way for people to contribute the data. We want to curate it so we can stand by it.

Q: [me] Openness? Of API, of metadata, of contributions of interesting comparisons, etc.

A: We’ll do a variety of levels of API. First: presentation level: put output on their pages. Second, XML-level so people can mash it up. Third level: individual results from the databases and from the computations. [He shows a first draft of the api] You can get as the symbolic expressions that Mathematica is based on. We hope to have a personalizable version. Metadata: When we open up our data repository mechanisms so people can contribute, some of our ontology will be exposed.

How about in areas where people disagree? If a new universe model comes out from Stanford, does someone at WolframAlpha have to say yes and put it in?

A: Yes

Q: How many people?

A: It’s been 150 for a long time. Now it’s 250. It’s probably going to be a thousand people.

Q: Who is this for?

A: It’s for expert knowledge for anyone who needs it.

Q: Business model?

A: The site will be free. Corporate sponsors will put ads on the side. We’re trying to figure out how to ingest vendor info when it’s relevant, and how to present it on the site. There will also be a professional version for people who are doing a lot of computation, want to put in their own data…

Q: Can you define the medical and population databases to get the total mass of people in England.

A: We could integrate those databases, but we don’t have that now. We’re working on “splat pages” you get when it doesn’t work. It should tell you what it does know.

Q: What happens when there is no answer, e.g., 55th largest state in the US?

A: It says it doesn’t know.

Q: [eszter] For some data, there are agreed-upon sources. For some there aren’t. How do you choose sources?

A: That’s a key problem in doing data curation. “How do we do it? We try to do the best job we can.” Use experts. Assess. Compare. [This is a bigger issue than Wolfram apparently thinks where data models are political. E.g., Eszter Hargittai, who is sitting next to me, points out “How many Internet users are there?” is a highly controversial question.] We give info about what our sources are.

Q: Technologically, where do you want to focus in the future?

A: All 4 areas need to be pushed forward.

Q: How does this compare to the Semantic Web?

A: Had the Web already had been semantically tagged, this product would have been far far easier, although keep in mind that much of the data in WA comes from private databases. We have a sophisticated ontology. We didn’t create the ontology top-down. It’s mostly bottom-up. We have domains. We have ontologies for them. We merge them together. “I hope as we expose some of our data repository methods, it will make it easier to do some Semantic Web kind of things. People will be able to line data up.”

Q: When can we look at the formal specifications of these ontologies? When can we inject our own?

A: It’s all represented in clean Mathematica code. Knitting new knowledge into the system is tricky because our UI is natural language, which is messy. E.g., “There’s a chap who goes by the name Fifty Cent.” You have to be careful.

Q: What reference source tells you if Palestine exists…?

A: In cases like this, we say “Assuming Case A or B.” There are holes in the data. I’m hoping people will be motivated to fill them in. Then there’s the question of the extent to which we can build expert communities. We don’t know the best way to do this. Lots of interesting ideas.

How about pop culture?

A: Pop culture info is much shallower computationally. (“Britney Spears” just gets her name, birthdate, and birthplace. No music, no photos, nothing about her genre, etc.) (“Meaning of life” does answer “42”)

Q: Compare with CYC? (A common sense reasoning system)

A: CYC deals with human reasoning. That’s not the best method for figuring out physics, etc. “We can do the non-human parts of reasoning really well.”

Q: [couldn’t hear the question]

A: The best way to debug it is not necessarily to inspect the code but to inspect the results. People reading code is less efficient than automated systems.

Q: Will it be integrated into Mathematica?

A: A future version will let you type WA data into Mathematica.

Q: How much work do you have to do on the NLP sound? Your searches used a special lexicon…

A: We don’t know. We have a daily splat call to see what types of queries have failed. We’re pretty good at removing linguistic fluff. People drop the fluff pretty quickly after they’ve been using WA for a while.

Q: (free software foundation) How does this change the landscape for open access? There’s info in commercial journals…

A: When there’s a proprietary database, the challenge is making the right deals. People will not be able to take out of our system all the data that we put into it. We have yet to learn all of the issues that will come up.

Q: Privacy?

A: We’re dealing with public data. We could do people search, but, personally, I don’t want to.

Q: What would you think of a more Wikipedia-like model? Do you worry about a competitor making a wiki data that is completely open and grows faster?

A: That’d be great. Making WA is hard. It’s not just a matter of shoveling data in. Wikipedia is fantastic and I use it all the time, but it’s gone in particular directions. When you’re looking for systematic data there, even if people put in systematic data — e.g., 300 pages about chemicals — over the course of time, the data gets dirty. You can’t compute from it.

Q: How about if Google starts presenting your results in response to queries?

A: We’re looking for synergies But we’re generating these on the fly; it won’t get indexed.

canadian pharmacy viagra | cialis online

Q: I wonder how universities will find a place for this.

A: Very interesting question. Generating hard data is hard and useful, although universities often prefer higher levels of synthesis and opinion. [Loose paraphrase!] Leibniz had this nailed: Take any human argument and find a way to mechanically compute it. [Tags: wolfram wolframapha search expertise google metadata libraries ]
