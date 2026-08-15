---
title: "Banking’s secret AI middleware: a fall guy"
person: kenneth-cukier
section: by
type: blog-post
year: 2017
date: 2017-09-16
venue: "The Self-Driving Company (Medium)"
authors: "Kenneth Cukier"
source_url: https://medium.com/self-driving-company/bankings-secret-ai-middleware-a-fall-guy-478516a5b4e6
retrieved: 2026-08-13
content: full-text
notes: "His own Medium publication 'the self-driving company'. Full text taken from the publication's RSS feed (content:encoded), which medium.com serves without the Cloudflare block that 403s the HTML pages; images/figures stripped, inline links preserved."
---

# Banking’s secret AI middleware: a fall guy

## Full text

##### Between strategy and trading algos is a man-in-the-middle — to fire

AH, THE BANTER of weekend brunch in West London. Coffee. Eggs. Gourmet smashed avocado on sourdough. And office chit-chat. Here’s what one anonymous banking-tech chap says about his week.

On Tuesday, his team launched a new automated trading system. There are two parts. On one end is a “strategy algorithm”. It slurps up a vast amount of market data in order to tease out the best trades several times a day. On the other end is the “execution algorithm.” It takes the strategy algo’s decisions and efficiently implements those trades continuously throughout the day.

But in between the two algos is a human. The person has to literally cut-and-paste the trade description between the two applications. “Control-C, click new window, control-V.” The manual operation takes just a few seconds of time on a computer.

*Huh?! Why?!*

Yes, it slows things down. Yes, it’s inefficient. Yes, it adds to costs. So why have a human-in-the-loop at all, if the only thing they do is bridge two algos without a wit of thought?

Says my brunch companion: “I intentionally built that in so we’d have someone to fire if things go wrong.”

He says this without irony, deviousness or remorse — as matter-of-factly as the tone with which he orders milky cappuccinos. At the table was a quant-ish fund manager. He laughed knowingly. They fist-pumped.

Chirped the second financier: “Why he gets paid a lot — it’s ‘danger money.’ It’s a short career,” he chortled. “You know you’ll get fired — so you’re compensated for that today!”

The point wasn’t heartless glee at unemployment. Far from it. These guys are more Brainy Smurf with an arm full of math books than Scrooge McDuck re-counting his coins. It was something deeper and sincere. And it speaks volumes about the way AI will get implemented in business and society.

As the first tech-banker put it: “It scares the shit out of everyone when you have an algorithm end-to-end — so you need to have a human around.” The mathy fund manager concurred: “Every now and then you need to throw the controls to manual.”

Just such a problem happened to him recently, he explained. A trader had to buy into a position — forced to spend £9 million as the market was nearing its close. So it was a mad rush to buy. He was forced to do complicated sums in his head while the trader operated the terminal. “Every time he pushed a button a million bucks was spent, but he couldn’t do it fast enough — OK, OK, OK, OK, to all the boxes popping up on the screen to confirm the operations.”

The ability to have manual override was critical, he explained. “We had to pull out all the fuses — Aaaaggghh, it was horrible. What we discovered was that there were quite a few fuses.”

What does this all mean? We tend to think that jobs are going disappear overnight because of the automation that AI promises. Though many jobs will be obliterated, the reality will probably mean lots of jobs still hanging around, with human inefficiency being deliberately built in to the system.

I got a taste of that after a [lecture I gave at Imperial College’s](http://www3.imperial.ac.uk/newsandeventspggrp/imperialcollege/engineering/datascienceinstitute/eventssummary/event_28-7-2017-16-7-45) Data Sciences Institute this week. At the reception following the talk, a woman approached. She runs the AI and automation division of a large British bank. For a given trading operation, it can use machine-learning to automate 80% of the task. But it still needs humans around to handle the “edge-cases” — the tricky ‘exceptions to the rule’, that require a human’s expert judgement. Did I have any advice, she asked, on how to balance the two goals: use algos and people?

This, I explained, sounds a lot like the Japanese just-in-time supply chains — they work beautifully in good times but they fail catastrophically in bad times. The hyper efficiency is a license to print money until an earthquake forces the whole assembly line to stop for want of a basic polymer because the factory holds zero inventory.

The solution, I offered, was to bite the bullet and build some slack into the system. Keep a few humans around. Yes, it’s inefficient and adds to costs. But they’ll handle the handful of cases that the algos can’t do.

However she shook her head, no. Just keeping a few of the best people around isn’t enough, she explained. The problem is that, because they’re no longer deep in the data and making decisions day-in and day-out, they’ve lost their touch on what to look for and don’t perform well enough on those edge cases.

Hers, in effect, was a paean in favor of experience, apprenticeship and tacit knowledge — the value of what the management thinker Peter Drucker called “learning by doing.” Take that away from humans via an algorithm, and skills atrophy. Something special about how companies perform and how workers succeed gets obliterated. The whole system fails to attain its potential.

I noted that some industries already practice this inefficiency in the face of automation. Pilots need to maintain a minimum number of annual flight-hours to keep their skills sharp, so that if they ever need to take the controls, they can — like “Sully on the Hudson” in 2009, when a pilot safely landed on water after the engines failed during takeoff from a bird strike. (The primacy of human judgement is nicely explored in Nicholas Carr’s book “[The Glass Cage](http://www.nicholascarr.com/?page_id=18)” and in a [Harvard Business Review essay](https://hbr.org/2017/03/the-trade-off-every-ai-company-will-face) by Ajay Agrawa, Joshua Gans and Avi Goldfarb from Toronto’s Rotman School of Management.)

An echo of that idea came to me two days later, when I was on a [panel on AI and jobs](http://www.csfi.org/20170914-ai-the-future-economy/) at the Centre for the Study of Financial Innovation in London. John Hawksworth, the chief economist of the consultancy PwC in Britain, noted that some jobs may remain despite their inefficiency. “Having a pilot in the cockpit makes people feel safer, even if is not actually safer.”

I built on the idea in my own remarks. Like pilots, so too doctors. Having a person interact with patients is vital even if it’s an algorithm that makes the diagnoses. The nature of the doctor’s work changes. They need to “translate” the technology to people. But there is still a role. The human will be a “prop” to give patients confidence in the technology, just as today the stethoscope is a prop to give patients confidence in the humans. The instrument is rarely, and the readings can be made by a machine. Yet it remains a ubiquitous accessory. (A hat-tip to the “99% Invisible” [podcast on the stethoscope’s history](http://99percentinvisible.org/episode/the-stethoscope/).)

Where does this leave us? That humans-in-the-loop systems won’t necessarily exist because people are better, or are even needed, but to give the recipients of the algorithms confidence in the system. Second, people may act as the “middleware” to give the builders of the algorithms a fall guy to push out a window if things go wrong. Third, as we plough further into the AI age, we risk losing our sense of ground-truth, of the reality that exists below what the simulacrum of data represents — and losing that is risky.

[Banking’s secret AI middleware: a fall guy](https://medium.com/self-driving-company/bankings-secret-ai-middleware-a-fall-guy-478516a5b4e6) was originally published in [the self-driving company](https://medium.com/self-driving-company) on Medium, where people are continuing the conversation by highlighting and responding to this story.
