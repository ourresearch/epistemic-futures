---
title: "[liveblog][ai] Ben Green: The Limits of \"Fair\" Algorithms"
person: david-weinberger
section: by
type: blog-post
year: 2018
date: 2018-04-27
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2018/04/27/liveblogai-ben-green-the-limits-of-fair-algorithms/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog][ai] Ben Green: The Limits of "Fair" Algorithms

## Full text

Ben Green is giving a ThursdAI talk on “The Limits, Perils, and Challenges of ‘Fair’ Algorithms for Criminal Justice Reform.”

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

In 2016, the COMPAS algorithm

became a household name (in some households) when ProPublica showed that it predicted that black men were twice as likely as white men to jump bail. People justifiably got worried that algorithms can be highly biased. At the same time, we think that algorithms may be smarter than humans, Ben says. These have been the poles of the discussion. Optimists think that we can limit the bias to take advantage of the added smartness.

There have been movements to go toward risk assessments for bail, rather than using money bail. E.g., Rand Paul and Kamala Harris have introduced the Pretrial Integrity and Safety Act of 2017. There have also been movements to use scores only to reduce risk assessments, not to increase them.

But are we asking the right questions? Yes, the criminal justice system would be better if judges could make more accurate and unbiased predictions, but it’s not clear that machine learning can do this. So, two questions: 1. Is ML an appropriate tool for this. 2. Is implementing MK algorithms an effective strategy for criminal justice reform?

#1 Is ML and appropriate tool to help judges make more accurate and unbiased predictions?

ML relies on data about the world. This can produce tunnel vision by causing us to focus on particular variables that we have quantified, and ignore others. E.g., when it comes to sentencing, a judge balances deterrence, rehabilitation, retribution, and incapacitating a criminal. COMPAS predicts recidivism, but none of the other factors. This emphasizes incapacitation as the goal of sentencing. This might be good or bad, but the ML has shifted the balance of factors, framing the decision without policy review or public discussion.

Q: Is this for sentencing or bail? Because incapacitation is a more important goal in sentencing than in bail.

A: This is about sentencing. I’ll be referring to both.

Data is always about the past, Ben continues. ML finds statistical correlations among inputs and outputs. It applies those correlations to the new inputs. This assumes that those correlations will hold in the future; it assumes that the future will look like the past. But if we’re trying reform the judicial system, we don’t want the future to look like the past. ML can thus entrench historical discrimination.

Arguments about the fairness of COMPAS are often based on competing mathematical definitions of fairness. But we could also think about the scope of what we couint as fair. ML tries to make a very specific decision: among a population, who recidivates? If you take a step back and consider the broader context of the data and the people, you would recognize that blacks recidivate at a higher rate than whites because of policing practices, economic factors, racism, etc. Without these considerations, you’re throwing away the context and accepting the current correlations as the ground truth. Even if we were to change the base data, the algorithm wouldn’t make the change, unless you retrain it.

Q: Who retrains the data?

A: It depends on the contract the court system has.

Algorithms are not themselves a natural outcome of the world. Subjective decisions go into making them: which data to input, choosing what to predict, etc. The algorithms are brought into court as if they were facts. Their subjectivity is out of the frame. A human expert would be subject to cross examination. We should be thinking of algorithms that way. Cross examination might include asking how accurate the system is for the particular group the defendant is in, etc.

Q: These tools are used in setting bail or a sentence, i.e., before or after a trial. There may not be a venue for cross examination.

In the Loomis case, an expert witness testified that the algorithm was misused. That’s not exactly what I’m suggesting; they couldn’t get to all of it because of the trade secrecy of the algorithms.

Back to the framing question. If you can make the individual decision points fair we sometimes think we’ve made the system fair. But technocratic solutions tend to sanitize rather than alter. You’re conceding the overall framework of the system, overlooking more meaningful changes. E.g., in NY, 71% of voters support ending pre-trial jail for misdemeanors and non-violent felonies. Maybe we should consider that. Or, consider that cutting food stamps has been shown to increases recidivism. Or perhaps we should be reconsidering the wisdom of preventative detention, which was only introduced in the 1980s. Focusing on the tech de-focuses on these sorts of reforms.

Also, technocratic reforms are subject to political capture. E.g., NJ replaced money bail with a risk assessment tool. After some of the people released committed crimes, they changed the tool so that certain crimes were removed from bail. What is an acceptable risk level? How to set the number? Once it’s set, how is it changed?

Q: [me] So, is your idea that these ML tools drive out meaningful change, so we ought not to use them?

A: Roughly, yes.

[Much interesting discussion which I have not captured. E.g., Algorithms can take away the political impetus to restore bail as simply a method to prevent flight. But sentencing software is different, and better algorithms might help, especially if the algorithms are recommending sentences but not imposing them. And much more.]

2. Do algorithms actually help?

How do judges use algorithms to make a decision? Even if the algorithm were perfect, would it improve the decisions judges make? We don’t have much of an empirical answer.

Ben was talking to Jeremy Heffner at Hunch Lab. They make predictive policing software and are well aware of the problem of bias. (“If theres any bias in the system it’s because of the crime data. That’s what we’re trying to address.” — Heffner) But all of the suggestions they give to police officers are called “missions,” which is in the military/jeopardy frame.

People are bad at incorporating quantitative data into decisions. And they filter info through their biases. E.g., the “ban the box” campaign to remove the tick box about criminal backgrounds on job applications actually increased racial discrimination because employers assumed the white applicants were less likely to have arrest records. (Agan and Starr 2016) Also, people have been shown to interpret police camera footage according to their own prior opinions about the police. (sommers 2016)

Evidence from Kentucky (Stevenson 2018): after mandatory risk assessments for bail only made a small increase in pretrial release, and these changes eroded over time as judges returned to their previous habits.

So, we need to be asking the empirical question of how judges actual use these decisions. And should judges incorporate these predictions into their decisions?

Ben’s been looking at the first question:L how do judges use algorithmic predictions? He’s running experiments on Mechanical Turk showing people profiles of defendants — a couple of sentences about the crime, race, previous record arrest record. The Turkers have to give a prediction of recidivism. Ben knows which ones actually recidivated. Some are also given a recommendation based on an algorithmic assessment. That risk score might be the actual one, random, or biased; the Turkers don’t know that about the score.

Q: It might be different if you gave this test to judges.

A: Yes, that’s a limitation.

Q: You ought to give some a percentage of something unrelated, e.g., it will rain, just to see if the number is anchoring people.

A: Good idea

Q: [me] Suppose you find that the Turkers’ assessment of risk is more racially biased than the algorithm…

A: Could be.

[More discussion until we ran out of time. Very interesting.]
