---
title: "Complex Algorithmic Law"
person: peter-salib
section: by
type: essay
year: 2022
date: 2022-03-09
venue: "University of Chicago Law Review Online"
authors: "Peter N. Salib"
source_url: https://lawreview.uchicago.edu/online-archive/complex-algorithmic-law
retrieved: 2026-08-13
content: full-text
notes: "Written for the symposium on Ben-Shahar & Porat, Personalized Law. Also SSRN abstract 4008507."
---

# Complex Algorithmic Law

## Full text

Complex Algorithmic Law

March 09, 2022

Peter N. Salib

Peter N. Salib is an Assistant Professor of Law at the University of Houston Law Center and an Associated Faculty Member at the Hobby School of Public Affairs. Before coming to the University of Houston, Peter was a Climenko Fellow and Lecturer on Law at Harvard Law School.

Peter would like to thank the other symposium participants for their insightful comments on this Essay. He would also like to thank the editors of the University of Chicago Law Review for their excellent work on the piece.

Share

- 

Share The University of Chicago Law Review | Complex Algorithmic Law on Facebook

- 

Share The University of Chicago Law Review | Complex Algorithmic Law on Twitter

- 

Share The University of Chicago Law Review | Complex Algorithmic Law on Email

- 

Share The University of Chicago Law Review | Complex Algorithmic Law on LinkedIn

Download this publication

A Part of the series

Personalized Law: Different Rules for Different People

TABLE OF CONTENTS

TABLE OF CONTENTS

Professors Omri Ben-Shahar and Ariel Porat’s book, Personalized Law: Different Rules for Different People, is, to state the obvious, about the personalization of law. Less obviously, though, the book is not mostly about technology. True, it is full of wonderful—and I think prescient—science-fictional vignettes imagining a world where many human actions are governed by personalized microrules. And true, Professors Ben-Shahar and Porat write throughout that it is “algorithms”—not people—that will mine vast troves of data, make predictions about individuals’ preferences and behavior, and use those predictions to issue personalized commands. Nevertheless, Ben-Shahar and Porat remain mostly agnostic about what they mean by “algorithms”—the core technology needed to implement personalized law.

This technical agnosticism is a wise choice, given the goal of the book. The authors are lawyers prophesying jurisprudential revolution. They are not technologists prognosticating about the future of statistical inference. The book’s main arguments are thus about things like the efficiency, fairness, and justice of personalizing legal rules. Those arguments are mostly future proof. They will hold up even as underlying technical possibilities evolve. And the technical possibilities are evolving—at a blinding rate.

But for other challenges relating to governance by algorithm, the technical details will matter. This Essay identifies three such challenges, all closely related. These problems will all arise if personalized law is powered by the newest generation of cutting-edge artificial intelligence algorithms.

Perhaps I should say when personalized law is powered by such algorithms. These algorithms—with names like “deep neural network,” “random forest,” and “gradient boosting machine”—are the future. They are much more capable than older statistical models. Their ability to synthesize vast amounts of data, uncover new relationships between input factors, and make accurate predictions about people’s preferences, aptitudes, and behaviors represents a quantum leap forward from older-fashioned approaches.

Such cutting-edge algorithms’ raw power means that it will be extraordinarily tempting to use them for legal personalization. They are already being used for almost everything else. Moreover, such algorithms’ use for personalizing law should be tempting. As Ben-Shahar and Porat show, personalized law’s value lies in its precision. The more accurately a legal rule can reflect an individual’s ability to take care, need for protection, or appetite for privacy, the more welfare it can produce and the fairer its commands will be. Thus, a failure to implement the most advanced—and most accurate—algorithms for personalizing law would leave enormous amounts of unrealized value on the table.

These cutting-edge algorithms—which I will call “complex algorithms”—are quite different from their forebears, at least along one dimension. All predictive algorithms are subject to an accuracy–interpretability trade-off. And complex algorithms, as I will use the term, are just those that have traded away lots of interpretability in exchange for lots of accuracy. In other words, such algorithms do an extraordinarily good job at answering the questions we ask of them. But they do so via inferences that are, at first approximation, incomprehensible to human minds. For this reason, complex algorithms are sometimes described as “black boxes.”

Complex algorithms’ inscrutability gives rise to the three problems discussed here. These problems are general. They arise for many potential uses of complex algorithms—not just their use in personalizing law. But we are lawyers, and this is a symposium on Personalized Law, so this Essay targets its analysis accordingly.

The first problem is algorithmic discrimination. Much ink has already been spilled on that subject, including in Personalized Law. But as will be shown, neither the existing critiques nor the proposed solutions—including the technical solution that Ben-Shahar and Porat advocate—apply straightforwardly to complex algorithms.

The second problem is algorithmic misalignment with human goals. Algorithmic discrimination is, in fact, one concrete instance of misalignment: we do not want our algorithms to discriminate, yet they do. And they do so because the tasks to which we set them are not perfectly aligned to our true policy objectives. As discussed below, algorithmic discrimination is a relatively simple example of an alignment problem. Complex algorithms can be even more misaligned, and their misalignment can be much harder to detect.

The third and final problem is one of “intellectual debt.” As algorithms become more complex, they will begin to uncover empirical relations and scientific facts that humans do not or cannot understand. This means that it will become increasingly—perhaps impossibly—difficult to tell whether algorithms are misbehaving or instead behaving properly according to some valid principle that only the algorithm comprehends.

Having explained these three problems for algorithmic law, this Essay closes by arguing that they should be the focus of significant legal scholarship in the coming years. In some instances, these problems will be distinctly legal, such that legal academics are uniquely well-suited to solving them. And insofar as these problems are much bigger than the law—and they are much bigger—they are the kindof problem that legal rules have sometimes helped overcome.

I. Ordinary and Complex Algorithms

This Essay’s division between ordinary and complex algorithms is a rough one. In reality, there is no bright line. Instead, all algorithms sit on a continuum between highly interpretable and highly noninterpretable. The hallmark of an interpretable algorithm or statistical model is that the relationship between the inputs it considers and the answers it gives is easy to understand. Usually, this means that there are relatively few inputs, which are combined according to some known mathematical function to produce outputs. Imagine, for example, an ordinary-least-squares regression model that uses points, assists, rebounds, blocks, and steals to predict NBA salaries.

A complex, noninterpretable algorithm, by contrast, might consider many more inputs than an interpretable algorithm. Or it might combine inputs into radically nonlinear functions, making it difficult to map inputs onto outputs. Or it might do both. Here, imagine an NBA salary predictor that analyzes dozens of features of each player’s physiology, performance, and history, chops up those features in semirandom ways, recombines them into new features, weights those recombinations, chops them up again, recombines again, and then uses the resulting combinations to generate a prediction. That is, more or less, a neural network—and not a very complicated one.

The basic problem here is that as algorithms go from being simple to complex, they become harder and harder to understand. Sure, a data scientist can pop open the hood of a neural network and see what is connected to what. But as the combinations multiply, understanding the radically nonlinear function they represent becomes impossible. Even when looking at all the machine’s parts—connected and operating—one cannot really say how it works. 

This is the fundamental difference between complex and noncomplex algorithms. And it is the difference that generates all the difficulties discussed below.

II. Three Challenges for Complex Algorithmic Law

A. Algorithmic Discrimination

Algorithms discriminate. This is not because computers have their own racial, gender, or other biases. Nor is it usually because algorithms’ creators intend discriminatory results. Instead, algorithms discriminate because, consciously or subconsciously, humans discriminate. Algorithms are trained on large datasets, and they are designed to uncover relationships in that data. For example, a crime-prediction algorithm might be trained to uncover relationships between arrestees’ criminal history, age, education, income, and their eventual arrests. But if arrests are the proxy the algorithm uses for crime, and if human police discriminatorily overarrest Black citizens, then the algorithm’s predictions will replicate that bias.

One way of fixing this problem would be to avoid using biased data when training algorithms. This is easier said than done. Ideally, a crime-prediction algorithm would be trained using data reflecting all crimes anyone committed. But we never have that data. Many crimes go unreported or undetected, leaving no data trail. Reporting and detection, however, are human activities, and thus subject to human bias. All data, at bottom, is collected by humans—either through painstaking manual processes like criminal investigations or via automated processes that humans set up. Thus, no dataset is completely immune from potential bias. 

Perhaps, then, there is a technical fix. One fix that will not work, as Ben-Shahar and Porat point out, is scrubbing legally sensitive information like race, gender, or religion from the algorithm’s training data. Even traditional, interpretable algorithms are very clever. They find unexpected ways to optimize themselves, modeling even hidden relationships in the data. Thus, if race is a (discriminatory) cause of arrests in a dataset, and race data is hidden from the algorithm, the algorithm will use proxies for race—like zip code—to predict arrest. This approach again produces discriminatory results. In fact, discrimination often gets worse when sensitive information is hidden from an algorithm because such obfuscation also reduces the algorithm’s accuracy.

There is a better technical fix for algorithmic discrimination, which Ben-Shahar and Porat endorse: algorithms can be trained using allthe available data—including sensitive data like race, gender, or religion. So trained, an algorithm will learn that humans favor certain groups over others and will follow suit. It will favor those same groups by the same amount. But when the time comes to put such an algorithm to work—say, assessing new arrestees’ likelihood of committing a crime—it can be fooled. The algorithm can be told that everyone is a member of the most favored group. A Black arrestee, for example, would have all his actual data fed to the algorithm, with the exception that his race would be listed as “white.” Then, instead of penalizing him on the basis of his race, the algorithm would treat him as if he were a member of the favored group.

This is an elegant solution. And it works perfectly well for simple, highly interpretable algorithms.

But complex algorithms are a different story. As discussed above, complex algorithms work by connecting inputs to outputs in complicated, nonintuitive ways. A neural network combines and recombines its input features over and over again, with each recombination giving different weights to different inputs. Thus, the final set of synthetic features that determines the algorithm’s output does not remotely resemble the set of input features.

As a result, there is simply no guarantee that an algorithm trained on data produced by racist cops will give much weight to race per se. On the contrary, it may ignore race data entirely, instead paying lots of attention to complex combinations of racial correlates like zip code, education, and income. These combinations may operate as reconstructed racial features—such that they capture the police’s racism. In fact, the algorithm might more accurately capture racism using such recombinant features rather than by using race per se. If the police’s racial prejudice intersects in complicated ways with their other biases—around gender, income, or education—the recombinant features might track those interactions with maximal fidelity. Alternatively, an algorithm’s reliance on racial proxies, rather than race per se, could be the result of random chance. 

Either way, the result is that, for complex algorithms, Ben-Shahar and Porat’s elegant technical fix for algorithmic discrimination will not work. When it comes time to predict criminal activity by new arrestees, it may make no difference to tell a complex algorithm that everyone is white. The algorithm may not care about the race input. Instead, it may be optimized to guess everyone’s race using other non-racial data. Moreover, given the black-box nature of complex algorithms’ decision functions, there may be no way to see that it is making such guesses—much less how. Without knowing either of those things, it will be impossible to reliably trick such a model into treating everyone as white.

It is worth noting that these difficulties arise for all kinds of complex algorithms, not just fancy neural networks. Even large regression models can suffer from significant multicollinearity. In short, when input features are correlated with one another, the weight that the model assigns to each individual input becomes less meaningful. Then, in a large regression-based crime-prediction algorithm, the weight assigned to the race input would not capture actual race-based mistreatment. Nor would fooling the algorithm into thinking everyone was white adequately remedy the mistreatment.

B. The Alignment Problem

The problem of algorithmic discrimination can be understood as just one instantiation of a broader challenge for governance by algorithm: misalignment. Consider that, while humans wantless incarceration and lower crime, we only have data on incarceration and arrests. We can only train algorithms on the data we have, so we train them to predict arrests. Yet arrests are not crimes, nor are they an unbiased proxy for crimes. Thus, an algorithm that tries to predict arrests is predicting the wrong thing from the perspective of optimal policy. The result is discrimination. Because the algorithm’s goal is not quite aligned with the humans’, a policy based on its predictions would overincarcerate Black people and underincarcerate white people.

Algorithmic discrimination is a predictable variety of misalignment, at least in the realm of crime and policing. Everyone knows that arrests are not crimes. And most know that arrests can be a racially biased proxy for crimes. We can therefore foresee the possibility of discrimination in this area and implement governance by algorithm with our eyes open.

But alignment problems can arise anywhere. And many will be much more complicated and thus much harder to detect. The arrest-prediction algorithm contemplated above is simple. It predicts just one outcome and makes no legal recommendations based on that prediction. Instead, humans must decide how to translate arrest predictions into incarceration and other crime-reducing policy decisions.

Ben-Shahar and Porat’s vision of a personalized-law future is far more ambitious. In their introductory fable of David and Abigail, they walk readers through a world where legal algorithms operate as policy empiricists—trying out novel legal rules, observing the results, and updating subsequent directives accordingly.

Here, algorithms learn via feedback loops. They make a prediction, issue a command, see whether that command helped achieve their goal, and update their future predictions and commands based on those outcomes. This approach, called “reinforcement learning,” is attractive because it allows algorithms to experiment, potentially discovering solutions that humans would never have anticipated. But when reinforcement learning is in the picture, strange and surprising misalignments arise.

Consider the real-world example of an algorithm that was supposed to learn how to drive a robot around a curvy track. The algorithm’s options and incentives were simple. It could move only forward, left, or right, and it was rewarded for any action that did not take the robot off the track. Thus, the algorithm’s creators expected that it would learn to navigate forward around the entire course. Instead, the algorithm learned that certain combinations of left- and right-turn commands would cause the robot to zig-zag backwards. Having mastered this technique, it spent all its time moving back and forth on the straightest part of the track. This served the algorithm’s goals of moving a lot while staying on the track. The problem was that those goals, unexpectedly, did not end up aligning with the humans’.

Personalized legal algorithms could easily exhibit the same kind of behavior. Take Ben-Shahar and Porat’s example of a hypothetical estate-planning algorithm. That algorithm would create and update a basic will for both members of a married couple. These settings would be mere defaults. The humans could change them, but the point of the algorithm is to help them avoid the hassle.

In Ben-Shahar and Porat’s example, the husband and wife have different preferences. The husband wishes to leave his entire estate to his wife, and the wife wants to leave some of hers to her husband and some to their children. In the book, the algorithm minimizes decision costs by implementing those differing preferences into the couple’s respective default wills.

Imagine, however, a cleverer algorithm. Suppose that the algorithm is rewarded for minimizing changes to its defaults. This incentive seems plausibly aligned with the humans’ purposes. Again, the whole point of algorithmic intervention here is to generate defaults that individuals will like and thus keep.

Suppose the algorithm learns that when people see that their spouses have different preferences than they do, they often encourage their spouses to switch. Perhaps our fictional husband does not want his children to be spoiled by an early inheritance. Perhaps our wife believes that children have as much right to parental property as spouses do. Each wants the other to abide by their own preference for the sake of the children.

To head off changes to its defaults that would occur when couples disagree, the algorithm might do one of two things. First, it might try to predict who would win each disagreement and set both defaults accordingly. Suppose that this is hard. Then the algorithm might opt for deceit: when it notices the husband logging in to check his default, it shows him a will reflecting his own preferences. But if it notices that the wife is about to check her husband’s default, it quickly changes his default to reflect her preferences. And back and forth—and vice-versa. Then, each spouse thinks that the other agrees with them, and neither encourages the other to switch.

Essentially any personalized law algorithm could optimize itself for deception. Imagine an algorithm designed to set default retirement savings. Perhaps it notices that people like it when their retirement saving balances are high and when their bank account balances are high. So whenever it sees someone logging in to check retirement balances, it instantly transfers a chunk of money into those accounts. And when it sees that person logging in to check banking balances, it transfers the cash back.

The point here is not just that this kind of misalignment is stranger than the algorithmic discrimination described above. It is that the misalignment may be harder—or, in some cases, impossible—to detect. Algorithms can, and already do, learn to mislead those they are supposed to be serving for the purpose of maximizing their own rewards. True, the above-postulated deceptions might be readily detected. Husbands and wives will probably discuss their estate plans at some point. Then, the algorithm’s trick will be exposed. But there is no guarantee that all algorithmic misalignment will be easy to discover and fix. Indeed, as discussed below, there are reasons to think that much will not.

C. Intellectual Debt

As already discussed, complex algorithms’ decision functions can be baffling. Because of this, it will often be difficult to understand the underlying causal mechanisms driving personalized law algorithms’ choices.

Imagine, for example, a crime-risk algorithm whose predictions end up turning significantly on what a person ate the previous day, whether they were a side or stomach sleeper, and the person’s latitude. Has this algorithm discovered some previously unknown hormonal aggression response triggered by certain foods, influenced by overnight digestion, and catalyzed by exposure to sunlight? Is it operating on some other, even more esoteric, causal principle? Or has it indexed on random variations in its training data? It is exceedingly difficult to say with certainty.

Here, we see the problem of intellectual debt. In the future, many complex algorithms will work very well, even though the principles on which they work remain unknown to us. The algorithms will, in some sense, “know” more about the world than we do. This means that, insofar as such algorithms have made genuine discoveries—perhaps of hormonal aggression mechanisms—humans will not share in the benefits of increased knowledge.

It also means that we will not be able to easily tell whether algorithms are working well or whether they are misbehaving. Consider again our retirement-defaults algorithm that has learned to regularly move money between various investment accounts. Is it behaving this way to deceive its users? Or is it instead moving money around pursuant to a previously-unknown strategy for minimizing financial risk and maximizing returns? If algorithmic risk-minimization or deceit-maximization strategies were guaranteed to be comprehensible by humans, we could probably decide. But the truth is that the algorithm could be doing either, just according to principles that we do not understand.

Thus, the intellectual debt problem exacerbates the alignment problem. It is one thing to observe that we do not understand exactly how complex algorithms achieve their goals. It is yet another to observe that, because of this, we often will not even be able to say whether they are pursuing the right goals at all.

III. A Research Agenda for the Coming Decade

Suppose that the world envisioned in Personalized Law really is—as Ben-Shahar and Porat convincingly argue—our future. Suppose that algorithms really will supplant legislators, executive officials, judges, and attorneys as the primary lawgivers for ordinary citizens. If that is right, then the problems explored in this Essay ought to be among the very most important topics of legal research in the coming decade.

Algorithmic discrimination, of course, has already drawn significant scholarly attention. But as we have seen, the kinds of discrimination already being studied are just one comparatively simple instantiation of the much broader problem of alignment. We presently lack general-use solutions for alignment problems. We lack even the frameworks needed to begin generating solutions. The twin challenges of black-box decision functions and intellectual debt frustrate traditional notions of oversight.

Artificial intelligence researchers are already working on these problems. Legal academics should, too. For one thing, as Personalized Law attests, many instantiations of the problems will be fundamentally legal in nature. Those may, in turn, invite uniquely legal solutions.

Moreover, legal scholars may have insight to offer everyone, including those outside the world of law, about problems of AI alignment. In the end, misalignment is just a variation on the classic principal–agent problem. Humans are the principals, and we need ways to make sure our agents—the algorithms—do what we would want. Entire fields of law are devoted to coming up with creative and effective strategies by which principals and their agents can get along. Thus, lawyers and legal scholars who have spent their careers thinking about human agency problems may be well-suited to inventing solutions for our robot helpers (overlords?) too.
