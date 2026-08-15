---
title: "Optimization over Explanation: Maximizing the benefits of machine learning without sacrificing its intelligence"
person: david-weinberger
section: by
type: essay
year: 2018
date: 2018-01-28
venue: "Berkman Klein Center Collection (Medium)"
authors: "David Weinberger"
source_url: https://medium.com/berkman-klein-center/optimization-over-explanation-41ecb135763d
retrieved: 2026-08-13
content: full-text
notes: "Berkman Klein Center Collection post on Medium. Retrieved directly; Medium chrome, publication header and follow/clap widgets stripped."
---

# Optimization over Explanation: Maximizing the benefits of machine learning without sacrificing its intelligence

## Full text

## Berkman Klein Center Collection

Insights from the Berkman Klein community about how technology affects our lives (Opinions expressed reflect the beliefs of individual authors and not the Berkman Klein Center as an institution.)

Optimization over Explanation

## Maximizing the benefits of machine learning without sacrificing its intelligence

Note: Wired.com has simultaneously run an op-ed version of this paper.

Imagine your Aunt Ida is in an autonomous vehicle (AV) — a self-driving car — on a city street closed to human-driven vehicles. Imagine a swarm of puppies drops from an overpass, a sinkhole opens up beneath a bus full of mathematical geniuses, or Beethoven (or Tupac) jumps into the street from the left as Mozart (or Biggie) jumps in from the right. Whatever the dilemma, imagine that the least worst option for the network of AVs is to drive the car containing your Aunt Ida into a concrete abutment. Even if the system made the right choice — all other options would have resulted in more deaths — you’d probably want an explanation.

Or consider the cases where machine-learning-based AI has gone wrong. It was bad when Google Photos identified black men as gorillas. It can be devastating when AI recommends that black men be kept in jail longer than white men for no reason other than their race. Not to mention autonomous military weapon systems that could deliver racism in airborne explosives.

To help ameliorate such injustices, the European Parliament’s has issued the General Data Protection Regulation (GDPR) that is often taken to stipulate a “right to explanation” for algorithms that “significantly affect” users.[1] This sounds sensible. In fact, why not simply require all AI systems be able to explain how they came to their conclusions?

The answer is not only that this can be a significant technical challenge[2], but that keeping AI simple enough to be explicable can forestall garnering the full value possible from unhobbled AI. Still, one way or another, we’re going to have to make policy decisions governing the use of AI — particularly machine learning — when it affects us in ways that matter.

One approach is to force AI to be artificially stupid enough that we can understand how it comes up with its conclusion. But here’s another: Accept that we’re not always going to be able to understand our machine’s “thinking.” Instead, use our existing policy-making processes — regulators, legislators, judicial systems, irate citizens, squabbling politicians — to decide what we want these systems optimized for. Measure the results. Fix the systems when they don’t hit their marks. Celebrate and improve them when they do.

We should be able to ask for explanations when we can. But when we can’t, we should keep using the systems so long as they are doing what we want from them.

For, alas, there’s no such thing as a free explanation.[3]

## The problem with explanations

Pretend that your physician tells you that a deep-learning diagnostic system like Mt. Sinai’s Deep Patient has concluded that there is a good chance that you will develop liver cancer in the next five years.

“What makes the computer think that?” you ask.

Your doctor replies that the machine learning system — let’s call it Deep Diagnosis — has been trained on the health records of 700,000 patients, as was Deep Patient. From this data it has found patterns in what may be thousands of factors that have enabled it to accurately predict probabilities of health issues. In your case, it’s predicting with a confidence of 70 percent that you’ll develop liver cancer within the next five years.

“Based on what factors in my health record?”

Your doctor replies: “Deep Diagnosis tracks thousands of factors, including many that seem irrelevant to a diagnosis, and we don’t understand why they add up to a particular probability of liver cancer. A trained physician like me could stare at the print-out of all those variables and their weightings without ever understanding why they led to that result. In fact, these patterns may not be the same for other patients with the same diagnosis. But it turns out that they do indeed predict probable health issues. So, here are your options for treatment, including ignoring the prediction…”

This is very different from what we normally expect from a human giving an explanation. Usually our doctor would explain the model she’s using: liver cancer is caused by this or that, here are the test results for the state of your this or that, and here are the alternatives for lowering your risk.

But machine learning systems don’t have to start out primed with explicit human models of how factors interrelate. Certainly, human assumptions are inevitably smuggled in via our choices about which data to train them on, the biases expressed by that data, the implicit biases of the system’s programmers, the user interface we provide for interacting with the system, the reports we choose to generate, etc. But the system does not have to be told how we think the data it’s fed interrelates. Instead, the system iterates on the data, finding complex, multi-variable probabilistic correlations that become part of the model it builds for itself.

Human-constructed models aim at reducing the variables to a set small enough for our intellects to understand. Machine learning models can construct models that work — for example, they accurately predict the probability of medical conditions — but that cannot be reduced enough for humans to understand or to explain them.

This understandably concerns us. We think of these systems as making decisions, and we want to make sure they make the right moral decisions by doing what we do with humans: we ask for explanations that present the moral principles that were applied and the facts that led to them being applied that way. “Why did you steal the apple?” can be justified and explained by saying “Because it had been stolen from me,” “It was poisoned and I didn’t want anyone else to eat it” or “Because I was hungry and I didn’t have enough money to pay for it.” These explanations work by disputing the primacy of the principle that it’s wrong to steal.

It’s thus natural for us to think about what principles we want to give our AI-based machines, and to puzzle through how they might be applied in particular cases. If you’d like to engage in these thought experiments, spend some time at MoralMachine.mit.edu where you’ll be asked to make the sort of decision familiar from the Trolley Problem: if you had to choose, would you program AVs to run over three nuns or two joggers? Four old people or two sickly middle-aged people? The creators of the site hope to use the crowd’s decisions to provide guidance to AV programmers, but it can also lead to a different conclusion: We cannot settle moral problems — at least not at the level of detail the thinking behind MoralMachines demands of us — by applying principles to cases. The principles are too vague and the cases are too complex. If we instead take a utilitarian, consequentialist approach, trying to assess the aggregated pains and pleasures of taking these various lives, the problem turns out to be still too hard and too uncertain.

So perhaps we should take a different approach to how we’ll settle these issues. Perhaps the “we” should not be the commercial entities that build the AI but the systems we already have in place for making decisions that affect public welfare. Perhaps the decisions should start with broad goals and be refined for exceptions and exemptions the way we refine social policies and laws. Perhaps we should accept that AI systems are going to make decisions based on what they’ve been optimized for, because that’s how and why we build them.[4] Perhaps we should be governing their optimizations.

## Optimization over explanation

1. AI systems ought to be required to declare what they are optimized for.

2. The optimizations of systems that significantly affect the public ought to be decided not by the companies creating those systems but by bodies representing the public’s interests.

3. Optimizations always also need to support critical societal values, such as fairness.

Optimization is a measure of outcomes against goals. A system of AVs is successfully optimized for reducing fatalities if over a statistically reasonable interval the number of fatalities drops. It is optimized for energy savings if the overall energy use of the system — and the larger systems in which it’s embedded — declines. Optimization does not have to specify a precise target in order to succeed; rather the target is the maximum desirable and possible given all of the other desired optimizations, in conjunction with the world’s vicissitudes.

System designers talk about optimization because they recognize that machines are imperfect and are often designed to serve inconsistent goals. Are you going to optimize your car for good mileage, environmental impact, price, acceleration, safety, comfort, scenic views, or prestige? Designing for safety might require a heavier chassis, which will negatively affect acceleration, mileage, and environmental impact. Designing for environmental impact might mean longer travel times. Designers have to create a balance of optimizations, playing with a set of metaphorical sliders that determine how much of a value the system will sacrifice to gain some combination of the other values. As David P. Reed, one of the architects of the Internet, has said, optimizing a system for one value de-optimizes it for others.[5]

While optimizations apply to systems, they may be determined, within limits, by the individual users. For example, the passengers in an AV might want to optimize a trip for scenic value. Moving that “slider” up — someday possibly a slider in a digital control panel — will automatically move some of the others down: the trip is likely to take longer and consume more energy. The limits imposed on the users’ ability to adjust the sliders will be determined by those who are designing the optimization of the system overall: perhaps users will not be allowed to optimize their particular trip in a way that will de-optimize the overall system, even a little, for preserving lives.

There’s more to say about what’s entailed in optimizing AI systems, especially about keeping them fair, but first: why discuss the morality and governance of AI systems in terms of their optimization at all?

First, it focuses the normative discussion on AI as a tool designed to provide benefits we’ve agreed we want, rather than as a set of moral conundrums to be solved by arguing over principles and their application. For example, we are never going to agree as a society if AVs should be programmed to run over two prisoners to save one nun, or if rich people should be allowed to go faster at the expense of the not so rich; if we can’t even agree on Net Neutrality, how are we ever going to agree on Highway Neutrality? But we do have apparatuses of governance that let us decide that, say, a system of AVs should aim at reducing fatalities as a first priority, and at reducing environmental impact as a second. Does this mean an AV should run over the nun? Yes, if we’ve decided to optimize AVs to lower fatalities and her death will save two others, but not because we have at long last figured out the moral algebra of nuns vs. sinners. We can stop talking about the Trolley Problem, at least when it comes to governing this sort of AI system. That by itself should count as a major benefit.

Second, it enables us to evaluate success and failure — and liability — in terms of system properties, rather than case by case. Since governance of these systems will be done at some system layer of society — local, state, national, global — the primary evaluation ought to also be on the benefits at the system level.

Third, it contextualizes the suffering most AI systems are going to cause. For example, Aunt Ida’s family is going to be outraged that her AV drove into the concrete abutment. The family may well want to bring suit against the maker of the AV. But why her car killed specifically her may be inexplicable. There may be too many variables. It may require gathering all the real-time data from all the networked AVs on the road that provided input into the networked AI decision. Some of the data may need to be cloaked for privacy reasons. The ad hoc network that made the decision may have been using real-time data from other systems, including weather information, pedestrian locations, economic impact systems, etc….and some of those systems may be inexplicable black boxes. It may simply not be practical to expect all that data to be preserved so that we can perfectly recreate the state of the system. We well not be able to explain the decision or even verify it.

From the standpoint of morality and legal liability, this seems highly unsatisfactory. On the other hand, in 2016, there were about 40,000 traffic fatalities in the US. Let’s say a few years after AVs have become common, that falls to 5,000 deaths per year. Five thousand deaths per year is a horrible toll, but 35,000 lives saved per year is a glorious good. The moral responsibility of the AV manufacturer and of the network of AVs on the road at the time is not to save Aunt Ida but to achieve the optimizations that we as a society have decided on through our regulatory, legislative, and judicial systems.

Fourth, governing via optimization makes success measurable.

Finally, the concept of optimization has built into it an understanding that perfection is not possible. Optimization is a “best effort.” “AVs killed 5,000 people this year!” does not become a cause for moral outrage but a cheer for a major, humane accomplishment.

Overall, understanding and measuring AI systems in terms of their optimizations gives us a way to govern them that enables us to benefit from them even though they are imperfect and even when we cannot explain their particular outcomes.

## Critical constraints: Hedging optimization

Imagine that AVs are optimized to minimize fatalities, and deaths by car drop from 40,000 to 5,000 per year. Yay!

Now imagine that in an early simulation of the system, people of color are hugely disproportionately represented among those 5,000 dead.

Or imagine that a system designed to cull applicants for Silicon Valley tech jobs is producing high quality sets of people for in-person interviews, but the percentage of women making it through the AI process is even lower than the current dismal percentage of women in tech positions.

A system that achieves the results it’s been optimized for may still fail to meet societal goals. As has been well documented[6], machine learning systems are prone to reproducing or even amplifying the biases reflected in the data the systems used to create their models.

Achieving the stated optimization goals is clearly not enough. AI systems need to be able to provide evidence in the form of quantifiable results that the optimizations are not violating a culture’s broader, deeper values; this is the deontological (principle-based) moment of this utilitarian approach.[7]

We could count these constraints as another sort of optimization. But they deserve their own name and category, for two reasons.

First, “being fair” is not what a system of AVs or a medical diagnostic system is designed to do. Such systems are tools and thus are optimized for a more focused purpose. It’s useful to reserve the term “optimization” for the purposes for which a tool was designed.

Second, optimizations are trade-offs. But these constraints are critical because we will not permit them to be traded off.

So, we’ll call them critical constraints.

Deciding on the critical constraints we’ll demand from AI systems will require difficult moral discussions that express deep conflicts in our culture. For example, a Silicon Valley company resistant to demands for gender equity might say it wants its applicant-culling software to recommend the “best of the best” (as the company defines that), and “Gender balance be damned!” Or it may claim that the company receives relatively few applications from women. Or it may be terribly misguided about what to look for when evaluating potential employees.[8]

We may nevertheless decide as a culture to address the inequity of the tech workforce by enforcing a requirement that tech application-culling systems produce pools at least 50 percent composed of women. Or we might decide that the problem is the inequity in the educational pipeline and thus may want to suspend enforcing a “50 percent female” constraint until the pipeline becomes more gender balanced. Or we may want to insist on a 50 percent rule on the grounds that empirical evidence has shown that otherwise AI application-culling systems will reflect societal biases. Or we might insist that the recommendation pool be 75 percent female to help correct the inequity of the existing workforce. Such decisions undoubtedly will require difficult political and judicial conversations. On the positive side, having to come up with critical parameters for AI can serve a useful forcing function.

Resolving these issues are not AI’s problem, though. It’s our responsibility. Asking what we want AI systems optimized for frames it in a way appropriate for the necessary social discussions and political processes.

## Liability and compensation

There’s an endless series of mistakes AI can — and therefore will — make: misdiagnosing a disease, targeting innocents in military attacks, discriminating based on race and gender, as well as recommending a movie that you don’t much like. There’s a far smaller number of ways in which AI will make these errors, each needing its own set of policy, regulatory, and judicial tools to help prevent and ameliorate them .

1. The wrong optimization: Say an AV system optimized for shortest delivery times routes continuous traffic through a residential section of town, resulting in a degradation of the quality of life. Or it routes high-speed traffic through a shopping district, de-optimizing local and pedestrian traffic, causing a drop in sales. (In this case, we well might want to let localities regulate the local optimizations of the system, just as airplanes have to lessen their noise over some towns.)

The manufacturers of AI systems should not be liable for successfully meeting poorly thought-through optimizations. They should be liable for ignoring local optimizations, just as airlines can be held responsible for violating local noise restrictions on late night arrivals.

2. Faulty execution: Say a home Internet of Things system has been optimized for energy savings, but in some homes it’s resulting in higher monthly expenditures on energy. In this case, the optimization is the preferred one, but the execution of it is faulty due to buggy software, the system having been trained on inappropriate data, a failure to interoperate properly with one or more of the devices, etc.

The optimization is correct but the implementation is flawed. If the AI system is capable of yielding explanations, those explanations need to be presented, and liability assessed. But if the AI is not capable of yielding explanations, product liability and class action processes might apply.

3. Expected harms from a well-optimized, properly functioning system: Say Aunt Ida happens to be one of the 5,000 fatalities in the new national AV system that is optimized first for reducing fatalities. It is operating properly: fatalities have dropped and the system is operating within its critical constraints.

The unfortunate losers in this system should receive no-fault compensation, probably via some form of social insurance.

4. Failure to instill a critical constraint, or to get its constraining power correct: Say an autonomous police drone uses undue force to subdue a criminal, resulting in serious collateral damage to innocent people. The injured innocents might bring suit, arguing that the drone failed to heed the “no harm to innocents” constraint.

If the drone indeed failed to heed that constraint, or if the manufacturers “forgot” to instill it, the manufacturers should be liable.

If the regulations governing police drones do not include such a constraint, then liability would seem to fall on the body that decided on the mix of optimizations and critical constraints. (The question of how a drone recognizes innocents is not a question of governance but a technical question — an important one — about implementation.)

(a) In the cases where systems are not functioning as expected, liability law, including product liability law, can often be invoked. The explanation of the failure need not always be determined.

(b) Where the systems are functioning as expected, and where the expectations assume imperfections, the victims ought to be compensated along the model of no-fault insurance: The families of the 5,000 people killed in car crashes ought to be compensated according to guidelines that try to be as fair as possible.

## Why this way?

This overall approach has several advantages:

First, it lets us benefit from AI systems that have advanced beyond the ability of humans to understand exactly how those systems are working.

Second, it focuses the discussion on the system rather than on individual incidents.

Third, it places the governance of these systems within our human, social framework. Optimizations are always imperfect and entail trade-offs that we need to discuss. Optimizations should always be constrained by social values that we consider paramount. The operations of autonomous systems are autonomous from human control in particular situations but are subordinate to human needs, desires, and rights. (The italicized words indicate places where humanity is requisite and evident.)

Fourth, it does not require us to come up with a new moral framework for dealing with an infrastructure that increasingly uses the most advanced tools our species has ever created. Rather, it treats these inevitable problems as societal questions that are too important to be left unregulated and in the hands of commercial entities. It instead it lets them be settled by existing regulatory bodies, using our existing processes for resolving policy questions, and it uses and extends the existing legal frameworks for assessing liability and schedules of compensation.

This way we don’t have to treat AI as a new form of life that somehow escapes human moral questions. We can treat it as what it is: a tool that should be measured by how much better it is at doing something compared to our old way of doing it: Does it save more lives? Does it improve the environment? Does it give us more leisure? Does it create jobs? Does it make us more social, responsible, caring? Does it accomplish these goals while supporting crucial social values such as fairness?

By treating the governance of AI as a question of optimizations, we can focus the necessary argument about them on what truly matters: What is it that we as a society want from a system, and what are we willing to give up to get it?

## The elements of this process

Use existing public institutions of policy-making to decide on the weighting of interrelated and frequently conflicting optimizations and critical constraints.

Require AI systems to announce those optimizations publicly and clearly, and then hold them to them. This is where the locus of transparency should be. The transparency of algorithms is a tool that has its own uses in special cases.

Measure everything possible. Make those measurements available publicly, or, when necessary, privately to sanctioned, trusted, independent bodies.

Establish no-fault compensation and social insurance for systems where some harmful results cannot be avoided.

In short: Govern the optimizations. Patrol the results.

Thank you to the twenty or so people who commented on an online draft of this paper. Many but not all came from Harvard’s Berkman Klein Center or the MIT Media Lab. Not all agree with this paper’s premises or conclusions. All were helpful.

## END NOTES

(I took the photo. It’s licensed as Creative Commons BY.)

[1] What the GDPR actually stipulates is much harder to parse. See Sandra Wachter, Brent Middelstadt, Luciano Floridi, “Why a Right to Explanation of Automated Decision-Making Does Not Exist in the General Data Protection Regulation”, International Data Privacy Law, Jan. 24, 2017.

[2] There is a great deal of research underway about how explicable, or interpretable, complex Deep Learning systems can be. We know empirically that at least some of them can be understood to some useful degree. See, for example, this explanation of how Google’s DeepDream image maker works. For a fascinating and powerfully argued proposal for enabling explanations of machine learning systems without requiring any alteration of the systems and even without direct inspection of the algorithms used, see” Towards A Rigorous Science of Interpretable Machine Learning” by Finale Doshi-Velez and Been Kim.

[3] Thanks to Stuart Shieber for suggesting a version of this phrase. Also, note that there may be such a thing as a free hunch.

[4] And what they are optimized for will shape their design, including their sensors and controls. Optimization decisions have implications for every stage of devices’ design and production.

[5] In a private conversation. Cited with permission.

[6] For example, see Cathy O’Neil’s Weapons of Math Destruction and Kate Crawford’s “Artificial Intelligence’s White Guy Problem.”

[7] In “Fairness through Awareness,” Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Richard Zemel suggest both a metric for measuring fairness and “an algorithm for maximizing utility subject to the fairness constraint.” “Our framework permits us to formulate the question as an optimization problem that can be solved by a linear program.” Their “similarity metric” allows a way to assess whether an AI system is treating people who are relevantly similar in similar ways.

[8] See John Simons, “What Sephora Knows About Women in Tech That Silicon Valley Doesn’t,” Wall Street Journal, Oct. 9, 2017
