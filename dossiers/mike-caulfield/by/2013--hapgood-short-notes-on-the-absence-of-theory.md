---
title: "Short Notes on the Absence of Theory"
person: mike-caulfield
section: by
type: blog-post
year: 2013
date: 2013-12-10
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2013/12/10/short-notes-on-the-absence-of-theory/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Short Notes on the Absence of Theory

## Full text

[Martin Weller](<http://nogoodreason.typepad.co.uk/no_good_reason/2013/12/the-iceland-of-dallas.html>), [Stephen Downes](<http://www.downes.ca/archive/13/12_09_news_OLDaily.htm>), and [Matt Crosslin](<http://www.edugeekjournal.com/2013/12/09/give-me-an-m-give-me-a-c-blah-blah-blah-to-all-pthis-theory/>) have been kicking around the “post-theory” critique of MRI ’13 that came up in a discussion Jim Groom and I had Thursday night in the middle of a bar in the middle of a hotel in the middle of an ice storm. 

I thought I might just add a bit of context and my two cents. 

First, the conversation came up because Jim was quite nicely (and genuinely) asking an edX data analyst what Big Data was. The answer that analyst gave was that Big Data was data that was big. That’s actually technically correct — the original term was meant to refer to data that was big enough in terabytes/petabytes that it could not be processed through traditional means. If your data was big enough that you were using [Hadoop](<http://en.wikipedia.org/wiki/Apache_Hadoop>), it was Big Data. 

Because I’m generally a person that can’t keep my mouth shut, I interjected that while that was true from a technical standpoint, it didn’t really get at the cultural significance of the Big Data _movement_ , which was captured in Chris Andersen’s “[End of Theory](<http://www.wired.com/science/discoveries/magazine/16-07/pb_theory>)” article back in 2008. Here’s a sample:

> Google’s founding philosophy is that we don’t know why this page is better than that one: If the statistics of incoming links say it is, that’s good enough. No semantic or causal analysis is required. That’s why Google can translate languages without actually “knowing” them (given equal corpus data, Google can translate Klingon into Farsi as easily as it can translate French into German). And why it can match ads to content without any knowledge or assumptions about the ads or the content.  
>    
>  …  
>  Petabytes allow us to say: “Correlation is enough.” We can stop looking for models. We can analyze the data without hypotheses about what it might show. We can throw the numbers into the biggest computing clusters the world has ever seen and let statistical algorithms find patterns where science cannot. 

While my analogy-prone brain sees parallels here to Searle’s [Chinese Room problem](<http://plato.stanford.edu/entries/chinese-room/>), it’s probably more correct to see this as behaviorism writ large: where Skinner wanted us to see the mind as a black box determined by inputs and outputs, Big Data asks us to see entire classes of people as sets of statistical probabilities, and the process of research becomes the iterative manipulation of inputs to achieve desired outputs. And the same issues emerge: Chomsky’s “destruction” of behaviorism in his [1959 takedown](<http://www.chomsky.info/articles/1967----.htm>) of B. F. Skinner’s _Verbal Behavior_ is generally overstated, but certain passages in that work seem a relevant critique of the “end of theory”; for instance, where Chomsky criticizes Skinner’s notion of reference: “The assertion (115) that so far as the speaker is concerned, the relation of reference is ‘simply the probability that the speaker will emit a response of a given form in the presence of a stimulus having specified properties’ is surely incorrect if we take the words presence, stimulus, and probability in their literal sense.”

Of course, in the past 50 years we’ve seen this Chomsky-Skinner drama played out anew in linguistics. While Chomsky’s transformational grammar underpinned efforts at computer translation for many years, Google’s translational approach, which sees language as nothing more than a set of probabilities (words are “known” to be the same in two different languages if they have the same probability of occurring in a context), is quickly outstripping the traditional methods. In fact, for a certain class of tasks it becomes increasingly obvious that correlation *is* enough. Google’s translation engine has little to no theory of language, yet adequately serves for a person who needs a quick translation of a web page. And that somewhat atheoretical nature of the engine is in fact its strength — Google’s approach needs only a robust set of web pages from any language to generate the correlations needed to start translating.

So this debate is not really new, and there’s certainly a place for this sort of radical pragmatism. Chomsky’s focus on a system of mental rules that form a universal grammar may have enlarged human knowledge, but it’s turning out to be a really inefficient way to train computers to understand language. Gains in understanding underlying models are not always the shortest route to efficacy.

But such approaches come with a down side as well. Morozov deals with this extensively in his book _To Save Everything, Click Here_ , and in his [WSJ review of the book _Big Data_](<http://online.wsj.com/news/articles/SB10001424127887324178904578342234223307970>). After noting that Big Data is very useful in situations where you don’t care what the cause is (Amazon cares not a whit *why* people who buy [german chocolate](<http://www.amazon.com/Bakers-German-Chocolate-4-Ounce-Bars/dp/B000W7V7PI/ref=sr_1_1?s=grocery&ie=UTF8&qid=1386656716&sr=1-1&keywords=german+chocolate>) also buy cake pans as long as they get to the checkout buying both), where you do care about cause things are a bit different:

> Take obesity. It’s one thing for policy makers to attack the problem knowing that people who walk tend to be more fit. It’s quite another to investigate why so few people walk. A policy maker satisfied with correlations might tackle obesity by giving everyone a pedometer or a smartphone with an app to help them track physical activity—never mind that there is nowhere to walk, except for the mall and the highway. A policy maker concerned with causality might invest in pavements and public spaces that would make walking possible. Substituting the “why” with the “what” doesn’t just give us the same solutions faster—often it gives us different, potentially inferior solutions.

A hardline proponent of a Big Data approach might object to Morozov that you just need more nuanced and informed correlations. But assuming you had no theory about of ultimate causes, how would you even conceive of the possibility? (This is similar to what Michael Feldstein was getting at in his piece about the [inadequacy of Big Data for education](<http://mfeldstein.com/why-big-data-mostly-cant-help-improve-teaching/>)). A person who does not have a model of what is happening is unlikely to know where to look for inconsistencies. And Big Data is, by definition, big. Theory is your roadmap.

This is why at the workshop on analytics at the conference, I insisted on the “grokability” of analytics-produced guidance to the people who would use it to help students. In a way it comes down to the empowerment of the practitioner (and of the student). If I’m told I have a 50% chance of dropping out based on my “rt-score” of 2145.7, that’s one thing. But the interpretation of what to *do* about that number should depend heavily on what the inputs into it were. Was it prior GPA that pumped that score so high, or socioeconomic status? And the reason those variables are treated differently is that we have models and theories about socioeconomic status and GPA that help us understand its significance as a predictor.

Ultimately, like so many in the field, I’m actually very excited about the promise of data (though I would argue that it is actually “small data” — data that can live in a single spreadsheet — that paired with local use has the greatest potential). Still, if we are to enter this world we have to understand the trade-offs we engage in. Most of the theory-bound could certainly use a better understanding of how powerful a tool statistics can be in overcoming our own theoretical predispositions. It’s useful to understand that theory is not the only tool in the toolbox. But it’s equally true that the new breed of data scientist needs to be far more acquainted with the theories and assumptions that animate the sets of data in front of them. At the very least, they have to understand what theory is good for, why it matters, and why it is not always sufficient to tweak inputs and outputs.
