---
title: "[liveblog] Doaa Abu-Elyounes on \"Bail or Jail? Judicial vs. Algorithmic decision making\""
person: david-weinberger
section: by
type: blog-post
year: 2017
date: 2017-12-02
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2017/12/02/liveblog-doaa-abu-elyounes-on-bail-or-jail-judicial-vs-algorithmic-decision-making/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog] Doaa Abu-Elyounes on "Bail or Jail? Judicial vs. Algorithmic decision making"

## Full text

I’m at a weekly AI talk put on by Harvard’s Berkman Klein Center for Internet & Society and the MIT Media Lab. Doaa Abu-Elyounes is giving a talk called “Bail or Jail? Judicial vs. Algorithmic decision making”.

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

Doaa tells us that this talk is a work in progress.

We’ve all heard now about AI-based algorithms that are being used to do risk assessments in pretrial bail decisions. She thinks this is a good place to start using algorithms, although it’s not easy.

The pre-trial stage is supposed to be very short. The court has to determine if the defendant, presumed innocent, will be released on bail or jailed. The sole considerations are supposed to be whether the def is likely to harm someone else or flee. Preventive detention has many efffects, mostly negative for the defendant.

(The US is a world leader in pre-trial detainees. Yay?)

Risk assessment tools have been used for more than 50 years. Actuarial tools have shown greater predictive power than clinical judgment, and can eliminate some of the discretionary powers of judges. Use of these tools have long been controversy What type of factors to include in the power? Is the use of demographic factors to make predictions fair to individuals?

Existing tools use regression analysis. Now machine learning can learn from much more data. Mechanical predictions [= machine learning] are more accurate than statistical predictions, but may not be explicable.

We think humans can explain their decisions and we want machines to be able to as well. But look at movie reviews. Humans can tell if a review is positive. We can teach which words are positive or negative, getting 60% accuracy. Or we can have a human label the reviews as positive or negative and let the machine figure out what the factor are — via machine leaning — in which case we get 80% accuracy but may lose explicability.

With pretrial situations, what is the automated task is that the machine should be performing?

There’s a tension between accuracy and fairness. Computer scientists are trying to quantify these questions What does a fair algorithm look like? John Kleinberg and colleagues did a study of this [this one?]. Their algorithms reduced violent crime by 25% with no change in jailing rates, without increasing racial disparities. In short, the algorithm seems to have done a more accurate job with less bias.

Doaa lists four assessment tools she will be looking at: the Pretrial Risk Assessment [this one?], the Public Safety Assessment, the Virginia Pretrial Risk assessment Instrument and the Colorado Pretrial Assessment Tool.

Doaa goes through questions that should be asked of these tools, beginning with: Which factors are considered in each? [She dives into the details for all four tools. I can’t capture it. Sorry.]

What are the sources of data? (3 out of 4 rely on interviews and databases.)

What is the quality of the data? “This is the biggest problem jurisdictions are dealing with when using such a tool.” “Criminal justice data is notoriously poor.” And, of course, if a machine learning system is trained on discriminatory data, its conclusions are likely to reflect those biases.

The tools neeed to be periodically validated using data from its own district’s population. Local data matters.

There should be separate scores for flight risk and public safety All but the PSA provide only a single score. This is important because there are separate remedies for the two concerns. E.g., you might want to lock up someone who is a risk to public safety, but take away the passport of someone who is a flight risk.

Finally, the systems should discriminate among reasons for flight risk. E.g., because the defendant can’t afford the cost of making it to court or because she’s fleeing?

Conclusion: Pretrial is the front door of the criminal justice system and affects what happens thereafter. Risk assessment tools should not replace judges, but they bring benefits. They should be used, and should be made as transparent as possible. There are trade offs. The tool will not eliminate all bias but might help reduce it.

Q&A

Q: Do the algorithms recognize the different situations of different defendants?

A: Systems do recognize this, but not in sophisticated ways. That’s why it’s important to understand why a defendant might be at risk of missing a court date. Maybe we could provide poor defendants with a Metro card.

Q: Could machine learning be used to help us be more specific in the types of harm? What legal theories might we drawn on to help with this?

A: [The discussion got too detailed for me to follow. Sorry.]

Q: There are different definitions of recidivism. What do we do when there’s a mismatch between the machines and the court?

A: Some states give different weights to different factors based on how long ago the prior crimes were committed. I haven’t seen any difference in considering how far ahead the risk of a possible next crime is.

Q: [me] While I’m very sympathetic to allowing machine learning to be used without always requiring that the output be explicable, when it comes to the justice system, do we need explanations so not only is justice done, but we can have trust that it’s being done?

A: If we can say which factors are going into a decision — and it’s not a lot of them — if the accuracy rate is much higher than manual systems, then maybe we can give up on always being able to explain exactly how it came to its decisions. Remember, pre-trial procedures are short and there’s usually not a lot of explaining going on anyway. It’s unlikely that defendants are going to argue over the factors used.

Q: [me] Yes, but what about the defendant who feels that she’s being treated differently than some other person and wants to know why?

A: Judges generally don’t explain how they came to their decisions anyway. The law sets some general rules, and the comparisons between individuals is generally within the framework of those rules. The rules don’t promise to produce perfectly comparable results. In fact, you probably can’t easily find two people with such similar circumstances. There are no identical cases.

Q: Machine learning, multilevel regression level, and human decision making all weigh data and produce an outcome. But ML has little human interaction, statistical analysis has some, and the human decision is all human. Yet all are in fact algorithmic: the judge looks at a bond schedule to set bail. Predictability as fairness is exacerbated by the human decisions since the human cannot explain her model.

Q: Did you find any logic about why jurisdictions picked which tool? Any clear process for this?

A: It’s hard to get that information about the procurement process. Usually they use consultants and experts. There’s no study I know of that looks at this.

Q: In NZ, the main tool used for risk assessment for domestic violence is a Canadian tool called ODARA. Do tools work across jurisdictions? How do you reconcile data sets that might be quite different?

A: I’m not against using the same system across jurisdictions — it’s very expensive to develop one from scratch — but they need to be validated. The federal tool has not been, as far as I know. (It was created in 2009.) Some tools do better at this than others.

Q: What advice would you give to a jurisdiction that might want to procure one? What choices did the tools make in terms of what they’re optimized for? Also: What about COMPAS?

A: (I didn’t talk about COMPAS because it’s notorious and not often used in pre-trial, although it started out as a pre-trial tool.) The trade off seems to be between accuracy and fairness. Policy makers should define more strictly where the line should be drawn.

Q: Who builds these products?

A: Three out of the four were built in house.

Q: PSA was developed by a consultant hired by the Arnold Foundation. (She’s from Luminosity.) She has helped develop a number of the tools.

Q: Why did you decide to research this? What’s next?

A: I started here because pre-trial is the beginning of the process. I’m interested in the fairness question, among other things.

Q: To what extent are the 100+ factors that the Colorado tool considers available publicly? Is their rationale for excluding factors public? Because they’re proxies for race? Because they’re hard to get? Or because back then 100+ seemed like too many? And what’s the overlap in factors between the existing systems and the system Kleinberg used?

A: Interviewing defendants takes time, so 100 factors can be too much. Kleinberg only looked at three factors. Another tool relied on six factors.

Q: Should we require private companies to reveal their algorithms?

A: There are various models. One is to create an FDA for algorithms. I’m not sure I support that model. I think private companies need to expose at least to the govt the factors that they’re including. Others would say I’m too optimistic about the government.

Q: In China we don’t have the pre-trial part, but there’s an article saying that they can make the sentencing more fair by distinguishing among crimes. Also, in China the system is more uniform so the data can be aggregated and the system can be made more accurate.

A: Yes, states are different because they have different laws. Exchanging data between states is not very common and may not even be possible.
