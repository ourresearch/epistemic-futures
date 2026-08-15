---
title: "[liveblog][bkc] Algorithmic fairness"
person: david-weinberger
section: by
type: blog-post
year: 2017
date: 2017-10-10
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2017/10/10/liveblogbkc-algorithmic-fairness/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text. Live-blogged notes taken during another speaker's talk or panel — the summarized content is the speaker's, the framing and commentary are Weinberger's."
---

# [liveblog][bkc] Algorithmic fairness

## Full text

I’m at a special Berkman Klein Center Tuesday lunch, a panel on “Programming the Future of AI: Ethics, Governance, and Justice” with Cynthia Dwork, Christopher L. Griffin, Margo I. Seltzer, and Jonathan L. Zittrain, in a discussion moderated by Chris Bavitz.

NOTE: Live-blogging. Getting things wrong. Missing points. Omitting key information. Introducing artificial choppiness. Over-emphasizing small matters. Paraphrasing badly. Not running a spellpchecker. Mangling other people’s ideas and words. You are warned, people.

They begin with brief intros of their interests:

Chris Griffin: One of the big questions for use of algorithms in the justice system is what: is the alternative? Human decision making has its own issues.

Margo Seltzer: She’s been working on transparent models. She would always prefer to be able to get an index card’s worth of explanation of how a machine learning system has come up with its output.

Cynthia Dwork: What is our definition of fairness, and how might we evaluate the fairness of our machine systems? She says she’s not that big a fan of insisting on explanations.

Jonathan Zittrain: What elements of this ought to be contracted out? Can we avoid the voting machine problem of relying on a vendor we don’t necessarily trust? Also, it may be that expalantions don’t help us that much. Also, we have to be very wary of biases built into the data. Finally, AI might be able to shed light on interventions before problems arise, e.g., city designs that might lower crime rates.

Chris Bavitz: Margo, say more about transparency…

Seltzer: Systems ought to be designed so that if you ask why it came up with that conclusion, it can tell you in a way that you can understand. Not just a data dump.

Bavitz: The legal system generally expects that, but is that hard to do?

Seltzer: It seems that in some cases you can achieve higher accuracy with models that are not explicable. But not always.

Dwork: Yes.

Zittrain: People like Cynthia Rudin have been re-applying techniques from the 1980s but are explainable. But I’ve been thinking about David Weinberger’s recent work [yes, me] that reality may depend on factors that are deeply complex and that don’t reduce down to understandable equations.

Dwork: Yes. But back to Margo. Rule lists have antecedents and probabilities. E.g., you’re trying to classify mushrooms as poisonous or not. There are features you notice: shape of the head, odor, texture, etc. You can generate rules lists that are fairly simple: if the stalk is like this and the smell is like, then it’s likely poisonous. But you can also have “if/else” conditions. The conclusions can be based on very complex dependencies among these factors. So, the question of why something was classified some way can be much more complicated than meets the eye.

Seltzer: I agree. Let’s say you were turned down for the loan. You might not be able to understand the complex of factors, but you might be able to find a factor you can address.

Dwork: Yes, but the question “Is there a cheap and easy path that would lead to a different outcome?” is a very different quesiton than “Why I was classified some particular way?””

Griffin: There’s a multi-level approach to assessing transparency. We can’t expect the public to understand the research by which a model is generated. But how is that translated into scoring mechanisms? What inputs are we using? If you’re assessing risk from 1 to 6, does the decision-maker understand the difference between, say, a 2 and 3?

Zittrain: The data going in often is very reductive. You do an interview with a prisoner who doesn’t really answer so you take a stab at it … but the stabbiness of that data is not itself input. [No, Zittrain did not say “stabbiness”].

Griffin: The data quality issue is widespread. In part this is because the data sets are discrete. It would be useful to abstract ID’s so the data can be aggregated.

Zittrain: Imagine you can design mushrooms. You could design a poisonous one with the slightest variation from edible ones to game the system. A real life example: the tax system. I think I’d rather trust machine learning than a human model that can be more easily gamed.

Bavitz: An interviewer who doesn’t understand the impact of the questions she’s asking might be a feature, not a bug, if you want to get human bias out of the model…

Seltzer: The suspicion around machine algorithms stems from a misplaced belief that humans are fair and unbiased. The combination of a human and a machine, if the human can understand the machine’s model, might result in less biased decisions than either on their own.

Bavitz: One argument for machine learning tools is consistency.

Griffin: The ethos of our system would be lost. We rely on a judicial official to use her or his wisdom, experience, and discretion to make decisions. “Bias could be termed as the inability to perceive with sufficient clarity.” [I missed some of this. Sorry.]

Bavitz: If the data is biased, can the systems be trained out of the bias?

Dwork: Generally, garbage in, garbage out. There are efforts now, but they’re problematic. Maybe you can combine unbiased data with historical data, and use that to learn models that are less biased.

Griffin: We’re looking for continuity in results. With the prisoner system, the judge gets a list of the factors lined up with the prisoner’s history. If the judge wants to look at that background and discard some of the risk factors because they’re so biased, s/he can ignore the machine’s recommendation. There may be some anchoring bias, but I’d argue that that’s a good thing.

Bavitz: How about the private, commercial actors who are providing this software? What if these companies don’t want to make their results interpretable so as not to give away their special sauce?

Dwork: When Facebook is questioned, I like to appeal to the miracle of modern cryptography that lets us prove that secrets have particular properties without decrypting them. This can be applied to algorithms so you can show that one has a particular property without revealing that algorithm itself. There’s a lot of technology out there that can be used to preserve the secrecy of the algorithm, if that were the only problem.

Zittrain: It’d be great to be able to audit a tech while keeping the algorithm secret, but why does the company want to keep it secret? Especially if the results of the model are fed back in, increasing lock-in. I can’t see why we’d want to farm this out to commercial entities. But that hasn’t been on the radar because entrepreneurial companies are arising to do this for municipalities, etc.

Seltzer: First, the secrecy of the model is totally independent from the business model. Second, I’m fine with companies building these models, but it’s concerning if they’re keeping the model secret. Would you take a pill if you had no idea how it worked?

Zittrain: We do that all the time.

Dwork: That’s an example of relying on testing, not transparency.

Griffin: Let’s say we can’t get the companies to reveal the algorithms or the research. The public doesn’t want to know (unless there’s litigation over a particular case) the reasoning behind the decision, but whether it works.

Zittrain: Assume re-arrest rates are influenced by factors that shouldn’t count. The algorithm would reflect that. What can we do about that?

Griffin: The evidence is overwhelming about the disparity in stops by race and ethnicity. The officers are using the wrong proxies for making these decisions. If you had these tools throughout the lifespan of such a case, you might be able to change this. But these are difficult issues.

Seltzer: Every piece of software has bugs. The thought of sw being used in way where I don’t know what it thinks it’s doing or what it’s actually doing gives me a lot of pause.

Q&A

Q: The government keeps rehiring the same contractors who fail at their projects. The US Digital Service insists that contractors develop their sw in public. They fight this. Second, many engineering shops don’t think about the bias in the data. How do we infuse that into companies?

Dwork: I’m teaching it in a new course this semester…

Zittrain: The syllabus is secret. [laughter]

Seltzer: We inject issues of ethics into our every CS course. You have to consider the ethics while you’re designing and building the software. It’s like considering performance and scalability.

Bavitz: At the Ethics and Governance of AI project at the Berkman Klein Center, we’ve been talking about the point of procurement: what do the procurers need to be asking?

Q: The panel has talked about justice, augmenting human decision-making, etc. That makes it sound like we have an idea of some better decision-making process. What is it? How will we know if we’ve achieved it? How will models know if they’re getting it right, especially over time as systems get older?

Dwork: Huge question. Exactly the right question. If we knew who ought to be treated similarly to whom for any particular classification class, everything would become much easier. A lot of AI’s work will be discovering this metric of who is similar to whom, and how similar. It’s going to be an imperfect but improving situation. We’ll be doing the best guess, but as we do more and more research, our idea of what is the best guess will improve.

Zittrain: Cynthia, your work may not always let us see what’s fair, but it does help us see what is unfair. [This is an important point. We may not be able to explain what fairness is exactly, but we can still identify unfairness.] We can’t ask machine learning pattern recognition to come up with a theory of justice. We have to rely on judges, legislators, etc. to do that. But if we ease the work of judges by only presenting the borderline cases, do we run the risk of ossifying the training set on which the judgments by real judges were made? Will the judges become de-skilled? Do you keep some running continuously in artesinal courtrooms…? [laughter]

Griffin: I don’t think that any of these risk assessments can solve any of these optimization problems. That takes a conversation in the public sphere. A jurisdiction has to decide what its tolerance for risk is, what it’s tolerance is for the cost of incarceration, etc. The tool itself won’t get you to that optimized outcome. It will be the interaction of the tool and the decision-makers. That’s what gets optimized over time. (There is some baseline uniformity across jurisdictions.)

Q: Humans are biased. Assume a normal distribution across degrees of bias. AI can help us remove the outliers, but it may rely on biased data.

Dwork: I believe this is the bias problem we discussed.

Q: Wouldn’t be better to train it on artificial data?

Seltzer: Where does that data come from? How do we generate realistic but unbiased data?
