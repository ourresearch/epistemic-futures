---
title: "Abolition by Algorithm"
person: peter-salib
section: by
type: journal-article
year: 2025
venue: "Michigan Law Review (vol. 123, no. 5)"
authors: "Peter N. Salib"
source_url: https://repository.law.umich.edu/cgi/viewcontent.cgi?article=14138&context=mlr
retrieved: 2026-08-13
content: full-text
notes: "Full text extracted with pdftotext from the University of Michigan Law School repository copy. SSRN abstract 4736099."
---

# Abolition by Algorithm

## Full text

Michigan Law Review
Volume 123

Issue 5

2025

Abolition by Algorithm
Peter N. Salib
The University of Houston Law Center, psalib@central.uh.edu

Follow this and additional works at: https://repository.law.umich.edu/mlr
Part of the Artificial Intelligence and Robotics Commons, Law and Society Commons, and the Law
Enforcement and Corrections Commons

Recommended Citation
Peter N. Salib, Abolition by Algorithm, 123 MICH. L. REV. 800 (2025).
Available at: https://repository.law.umich.edu/mlr/vol123/iss5/2

https://doi.org/10.36644/mlr.123.5.abolition
This Article is brought to you for free and open access by the Michigan Law Review at University of Michigan Law
School Scholarship Repository. It has been accepted for inclusion in Michigan Law Review by an authorized editor
of University of Michigan Law School Scholarship Repository. For more information, please contact
mlaw.repository@umich.edu.

ABOLITION BY ALGORITHM
Peter N. Salib
TABLE OF CONTENTS
INTRODUCTION ........................................................................................................................ 801
I. ......... PRISON AND POLICE ABOLITIONISM .................................................................808
A. A Convincing Diagnosis ...............................................................................809
B. Bitter Medicine...............................................................................................813
1. On Policing ............................................................................................815
2. On Prison ...............................................................................................816
II. ....... ALGORITHMIC ABOLITIONISM ............................................................................818
A. Prisons...............................................................................................................821
B. Police ................................................................................................................. 827
C. How to Design an Algorithmic Abolitionist Policy...............................832
III. .... ALGORITHMIC ABOLITIONISM UPENDS THE BIAS DEBATE .........................836
A. Comparative Bias ..........................................................................................837
B. Bias, Levels, and Distribution.....................................................................842
1. Bias-Impact: A New, Levels-Linked, Measure of Fairness.....843
2. Trans-theoretic Tradeoffs Between Levels and
Distribution ...........................................................................................847
3. How Real Policies Fare ......................................................................849
C. Structural Inequality ....................................................................................851
IV. ...... REMARKS ON OTHER NORMATIVE QUESTIONS ..............................................855
A. The Political Economy of the Carceral State .........................................856
B. Humane Replacements for Police .............................................................857
C. Constitutional Constraints..........................................................................860
D. Privacy and Surveillance .............................................................................864
CONCLUSION ............................................................................................................................ 866

799

800

Michigan Law Review

[Vol. 123:799

ABOLITION BY ALGORITHM
Peter N. Salib*
In one sense, America’s newest abolitionist movement—advocating the elimination of policing and prison—has been a success. Following the 2020 Black
Lives Matter protests, a small group of self-described radicals convinced a wide
swath of ordinary liberals to accept a sweeping claim: Mere reforms cannot
meaningfully reduce prison and policing’s serious harms. Only elimination can.
On the other hand, abolitionists have failed to secure lasting policy change. The
difficulty is crime. In 2021, following a nationwide uptick in homicides, liberal
support for abolitionist proposals collapsed. Despite being newly “abolition curious,” left-leaning voters consistently rejected concrete abolitionist policies.
Faced with the difficult choice between reducing prison and policing and controlling serious crime, voters consistently chose the latter.
This Article presents and analyzes a policy approach designed to accomplish
both goals simultaneously: “Algorithmic Abolitionism.” Under Algorithmic
Abolitionism, powerful machine learning algorithms would allocate policing
and incarceration. They would maximally abolish both, up to the point at
which crime would otherwise begin to rise. Results could be impressive. The best
evidence evaluating modern machine learning models suggests that Algorithmic Abolitionist policies could: eliminate at least 40% of Terry stops, with highend estimates above 80%; free a similar share of incarcerated persons; eradicate most traffic stops; and potentially remove police patrols from at least half
of city blocks—all without increasing crime.
Beyond these practical effects, Algorithmic Abolitionist thinking generates new
and important normative insights in the debate over algorithmic discrimination. In short, in an Algorithmic Abolitionist world, traditional frameworks for
understanding and measuring such discrimination fall apart. Traditional
frameworks sometimes rate Algorithmic Abolitionist policies as unfair, even
when those policies massively reduce the number of people mistreated because
of their race. And they rate other policies as fair, even when those policies would
cause far more discriminatory harm. To overcome these problems, this Article
introduces a new framework for understanding—and a new quantitative tool
for measuring—algorithmic discrimination: “bias-impact.” It then explores the
complex array of normative trade-offs that bias-impact analyses reveal. As the
* Assistant Professor of Law, The University of Houston Law Center; Law and Policy
Advisor, Center for AI Safety. Thanks to Nicholas Almendares, Omri Ben-Shahar, Joseph
Blocher, Jacob Bronsther, Kiel Brennan-Marquez, Seth Chandler, Ryan Copus, Nikolas Guggenberger, William Hubbard, Orin Kerr, Guha Krishnamurthi, David Kwok, Jonathan Masur, Alex
Platt, Nicholson Price, Daniel Rauch, James Tierney, Justin Vanderschuren, Carleen Zubrzycki,
and the participants in the University of Chicago International Junior Scholars Conference; the
University of Michigan Junior Scholars Conference, The Emory AI Scholars Roundtable, and
the University of Houston Law Center Works in Progress Workshop. Special thanks to Madeline
McCune and Nathan Halaney for exceptional research assistance.

March 2025]

Abolition by Algorithm

801

Article shows, bias-impact analysis will be vital not just in the criminal enforcement context, but in the wide range of settings—healthcare, finance, employment—where Algorithmic Abolitionist designs are possible.

INTRODUCTION
In many ways, prison and police abolitionism has been a surprising success. Amidst the 2020 Black Lives Matter protests, a small group of self-described radicals convinced a wide swath of mainstream liberals to accept a
series of insurgent propositions: (1) Prison and policing are extremely harmful—more so than is ordinarily assumed, and especially for members of marginalized racial groups; (2) mere reforms cannot meaningfully redress those
serious harms; (3) thus, the only way to make a serious difference is to substantially eliminate police and prisons.
The abolitionist movement struck an immediate chord. By June 2020, just
a month after George Floyd’s murder, 41% of Democrats supported defunding the police, compared with 19% who supported increased funding. 1 Proponents of police and prison abolition were published in national newspapers
and elite academic journals. 2 Progressive lawmakers with national profiles, including Alexandria Ocasio-Cortez and Ilhan Omar, endorsed the abolitionist
argument for reduction over reform. 3 Both New York and San Francisco
planned large cuts to police budgets. 4 And the city council of Minneapolis,
where police killed Floyd, unanimously pledged to disband its police force entirely 5

1. Kim Parker & Kiley Hurst, Growing Share of Americans Say They Want More Spending
on Police in Their Area, PEW RSCH. CTR. (Oct. 26, 2021), https://www.pewresearch.org/shortreads/2021/10/26/growing-share-of-americans-say-they-want-more-spending-on-police-intheir-area [perma.cc/V8G8-VPBC].
2. See, e.g., Mariame Kaba, Opinion, Yes, We Mean Literally Abolish the Police, N.Y. TIMES
(June 12, 2020), https://www.nytimes.com/2020/06/12/opinion/sunday/floyd-abolish-defundpolice.html [perma.cc/B8LQ-KLCS]; Dorothy E. Roberts, Abolition Constitutionalism, 133
HARV. L. REV. 1 (2019).
3. See, e.g., Gino Spocchia, ‘An Indefensible System’: AOC Leads Calls to Abolish Police
After Daunte Wright Killing, INDEPENDENT (Apr. 14, 2021), https://www.the-independent.com/news/world/americas/us-politics/aoc-abolish-police-daunte-wright-b1831282.html
[perma.cc/DX8J-3YSG]; Ilhan Omar Defends Idea of Dismantling Minneapolis Police Department, AXIOS (June 14, 2020), https://www.axios.com/2020/06/14/ilhan-omar-minneapolis-police-department [perma.cc/W4EM-3YXT].
4. See Benjamin Schneider, Is San Francisco Re-Funding the Police?, SF WEEKLY (June
16,
2021),
https://www.sfweekly.com/news/is-san-francisco-re-funding-the-police
[perma.cc/V69W-HT3P]; Dana Rubinstein & Jeffery C. Mays, Nearly $1 Billion Is Shifted from
Police in Budget That Pleases No One, N.Y. TIMES (Aug. 10, 2020), https://www.nytimes.com/2020/06/30/nyregion/nypd-budget.html [perma.cc/SF2N-KWHZ].
5. Tommy Beer, Minneapolis City Council Unanimously Votes to Replace Police with
Community-Led Model, FORBES (June 29, 2021), https://www.forbes.com/sites/tommybeer/2020/06/12/minneapolis-city-council-unanimously-votes-to-replace-police-with-community-led-model/ [perma.cc/BE3G-Q894].

802

Michigan Law Review

[Vol. 123:799

But seen another way, abolitionism has failed. Despite having cultivated a
bloc of “abolition curious” left-leaning voters, it has produced little, if any, durable policy change.
The problem is crime. 2021 saw a modest nationwide uptick in homicides,
which received significant political attention. 6 Support for concrete abolitionist policies collapsed. Only 25% of Democrats supported defunding the police,
and 3% supported increased funding. 7 Cities that had cut their police budgets
re-funded them at even higher levels than before. 8 Minneapolis never got
around to disbanding its force. 9 As it turns out, even “abolition curious” voters
fear that, whatever the ills of prison and policing, their indiscriminate elimination would do more harm than good. 10 The empirical evidence suggests
they are right. 11
Nevertheless, abolitionists have manifested an important political opportunity: If there were a policy approach that could abolish significant amounts
of prison and policing without increasing serious crime, voters would support
it. Or at least, major blocs of voters in Democrat-leaning cities might. The
problem is that, so far, no such policy approach appears to exist.
This Article introduces such an approach: “Algorithmic Abolitionism.”
These policies are, in one meaningful sense, abolitionist. Algorithmic Abolitionism’s primary purpose is to radically and immediately reduce, not reform,
policing and incarceration—and thereby radically reduce their harms. Algorithmic Abolitionist policies are thus not principally designed to reduce crime
below current levels. However, unlike untargeted abolitionist practices, for example, “defund the police,” Algorithmic Abolitionist policies would accomplish their reductions without increasing crime.
This Article proceeds in four parts. Part I describes the rise—and stall—of
prison and police abolitionism. It begins by arguing that abolitionists are correct about their core empirical and normative claims. A substantial empirical
literature documents the serious harms of being caught up in the American
criminal enforcement system. 12 These harms, from unemployment to family

6. Rachel Treisman, Many Midterm Races Focus on Rising Crime. Here’s What the Data
Does and Doesn’t Show, NPR (Oct. 28, 2022), https://www.npr.org/2022/10/27/1131825858/uscrime-data-midterm-elections [perma.cc/XS5C-FS5T].
7. Parker & Hurst, supra note 1.
8. Grace Manthey, Frank Esposito & Amanda Hernandez, Despite ‘Defunding’ Claims,
Police Funding Has Increased in Many US Cities, ABC NEWS (Oct. 16, 2022)
https://abcnews.go.com/US/defunding-claims-police-funding-increased-uscities/story?id=91511971 [perma.cc/ZBJ2-SDEQ]; see also, e.g., Schneider, supra note 4.
9. Ernesto Londoño, How ‘Defund the Police’ Failed, N.Y. TIMES (June 16, 2023),
https://www.nytimes.com/2023/06/16/us/defund-police-minneapolis.html [perma.cc/CV57EJ97].
10. See, e.g., Matthew Yglesias, Defund Police Is a Bad Idea, Not a Bad Slogan, SLOW
BORING (Dec. 7, 2020) https://www.slowboring.com/p/defund-police-is-a-bad-idea-not-a
[perma.cc/423D-H7BX].
11. See infra Section I.B.
12. See infra Section I.A.

March 2025]

Abolition by Algorithm

803

destruction to early death, are so fundamentally tied to prison and policing as
to be mostly irremediable via reform. Major reductions are possible only via
less policing and incarceration. But, as Part I shows, voters also acted reasonably in rejecting untargeted police and prison abolition as harmful on net. This
is because another robust empirical literature shows even moderate acrossthe-board cuts to prison and policing substantially increase serious crime. 13
The sweeping cuts proposed by abolitionists would likely have increased it
even more. Poor and non-white Americans, the very groups abolitionism seeks
to help, would have suffered the most. 14
Part II introduces Algorithmic Abolitionism as a solution to this impasse;
it offers a comprehensive suite of Algorithmic Abolitionist policies, spanning
the entire criminal enforcement system, to abolish large shares of prison and
policing without increasing serious crime. Here is one concrete example: For
over a decade, computer algorithms have predicted whether a given arrestee
or convicted person will likely engage in further crime if not incapacitated.15
Such predictions could be leveraged into Algorithmic Abolitionist incarceration policies. The state could start with the lowest-risk individuals—the ones
almost certain not to commit additional crimes. It could release as many people as possible, climbing the risk gradient up to the limit at which crime rates
would begin to increase. This policy maximally reduces the harm of incarceration—by literally abolishing a portion of it—while retaining its present
crime-controlling effect.
The extent of abolition depends on how accurately the operative algorithm can sort high-risk individuals from low-risk ones. The crime prediction
algorithms of the past probably lacked much abolitionist potential. But the last
decade has seen a revolution in machine learning, including major advances
in computer vision, natural language processing, and more. 16 Likewise, today’s
best crime prediction algorithms have significant abolitionist potential. Highquality empirical evidence suggests that one algorithm published in 2018
could be used to reduce pretrial incarceration by as much as 41.9%, with a
bare-minimum reduction of 18.5%. 17 Similar evidence suggests that an even

13. See infra Section I.B.1; see also Erich Piza & Vijay F. Chillar, The Effect of Police Layoffs
on Crime: A Natural Experiment Involving New Jersey’s Two Largest Cities, 4 JUST. EVAL. J. 163
(2020).
14. See generally Jeffery T. Ulmer, Casey T. Harris & Darrell Steffensmeier, Racial and
Ethnic Disparities in Structural Disadvantage and Crime: White, Black, and Hispanic Comparisons, 93 SOC. SCI. Q. 799 (2012).
15. The controversial COMPAS model is an early example. See Julia Angwin, Jeff Larson,
Surya Mattu & Lauren Kirchner, Machine Bias, PRO PUBLICA (May 23, 2016),
https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
[perma.cc/5HYN-9KVX].
16. See Erik Brynjolfsson & Andrew McAfee, What’s Driving the Machine Learning Explosion?, HARV. BUS. REV., Jul. 18, 2017, https://hbr.org/2017/07/whats-driving-the-machine-learning-explosion [perma.cc/S4W3-J3W6].
17. See infra Section II.A; Jon Kleinberg et al., Human Decisions and Machine Predictions,
133 Q.J. ECON. 237 (2018).

804

Michigan Law Review

[Vol. 123:799

newer algorithm—published just last year—would facilitate releasing as many
as 80%, and at least 50%, of parole-eligible prisoners. 18 There are reasons to
think that this result could generalize to the prison population as a whole. 19
Using just these algorithms, then, Algorithmic Abolitionist policies might free
millions of Americans per decade who would otherwise be incarcerated—all
without generating an increase in crime.
Algorithmic Abolitionism has significant implications beyond incarceration. Point estimates from high-quality academic evaluations of the best existing algorithms suggest that such polices could: cut police street stops by up to
88% (and at least 42%) without affecting rates of dangerous contraband recovery; eliminate the police presence from 50% or more of urban blocks without increasing criminal victimization; and eliminate nearly all traffic stops, a
major source of police violence, 20 while detecting as many traffic violations as
status-quo procedures. 21 They could literally abolish much or most of the police, but without the downsides of indiscriminate policies like “defund.”
All of this is feasible today. In fact, many jurisdictions already use algorithms to some extent in directing criminal enforcement. 22 However, none
have achieved the levels of abolition just described. Part II argues that this is
because those jurisdictions have uniformly implemented the wrong policies
and probably used the wrong algorithms. Part II closes by enumerating a few
key principles for designing Algorithmic Abolitionist policies. It shows that the
main deficiencies in existing plans could be remedied with a stroke of the legislative pen.
The Article’s second half turns to normative considerations. On top of its
important practical effects, Algorithmic Abolitionist thinking opens new normative terrain. In particular, Algorithmic Abolitionism invites a significant rethinking of well-worn debates over algorithmic discrimination—which Part
III takes up.

18. See infra Section II.A; Hannah S. Laqueur & Ryan W. Copus, An Algorithmic Assessment of Parole Decisions, 40 J. QUANTITATIVE CRIMINOLOGY 151 (2022). Note that, the net reduction in incarceration achieved by releasing 80% of parole-eligible prisoners depends on the
status quo release rate. This varies dramatically by state. Appendix: Discretionary Parole Grant
Rates by State, 2019-2022, PRISON POL’Y INITIATIVE (Oct. 18, 2023), https://www.prisonpolicy.org/data/parolerates_2019_2022.html [perma.cc/4UPF-Q8NE]. In New York, for most of the
period examined in the study, the status quo release rate was 20%. Laqueur & Copus, supra, at
153.
19. See infra Section II.A, laying out these reasons, along with counterarguments.
20. Orion Rummler, Over Half of Police-Involved Killings in 2020 Began After Non-Violent
Incidents, AXIOS (Apr. 12, 2021), https://www.axios.com/2021/04/12/police-killings-2020-nonviolent-incidents [perma.cc/7NB2-PC7W] (finding about 10% of killings in 2020 arose from
traffic stops). For a discussion of the reasoning behind these figures, see supra notes 187–188
and accompanying text.
21. See infra Section II.B; see generally G. O. Mohler et al., Randomized Controlled Field
Trials of Predictive Policing, 110 J. AM. STAT. ASS’N 1399 (2015).
22. See How Many Jurisdictions Use Each Tool?, MAPPING PRETRIAL INJUSTICE,
https://pretrialrisk.com/national-landscape/how-many-jurisdictions-use-each-tool
[perma.cc/AN2L-7WHL].

March 2025]

Abolition by Algorithm

805

Historically, progressives, including prison and police abolitionists, have
opposed the use of algorithmic technology in criminal enforcement with near
unanimity, principally citing fears of racial injustice. 23 The literature on algorithmic discrimination has grown dense and thorny. Experts offer competing
theories—and thus quantitative measures—of fairness. Worse, an impossibility theorem has emerged: For essentially all algorithms, becoming perfectly
fair according to one theory mathematically entails discriminating according
to the others. 24
Yet algorithmic decisionmaking is ascendant, in both criminal justice and
elsewhere. This Article therefore asks whether algorithmic policies can be designed which not only avoid perennial racial justice critiques but actively promote equitable outcomes.
Part III begins by arguing that Algorithmic Abolitionist policies sidestep
the impossibility theorem. Such policies would generally reduce—even if not
eliminate—bias according to multiple theories of fairness simultaneously.
This, the Part argues, should be sufficient reason to favor Algorithmic Abolitionist policies over alternatives.
Part III also introduces three entirely new arguments into the literature
on algorithmic fairness. Each argument arises from the main thing that makes
Algorithmic Abolitionist policies unique: their ability to radically reduce levels
of carceral harm. By contrast, traditional accounts—and metrics—of algorithmic fairness are concerned with distributions of harm. Part III shows that these
distribution-focused frameworks often break down when applied to levels-reducing policies. A new evaluative approach is needed.
To see why, consider the following thought experiment: Imagine a country where one million citizens are locked away in prisons and jails. 25 Imagine
that 33% of them are Black, despite Black citizens composing only 12% of the
hypothetical nation’s population. 26 In this country, according to a simple theory of fairness, 27 Black citizens are locked up at nearly three times the fair
rate. 28 But imagine that, in this country, a hypothetical Algorithmic Abolitionist sentencing policy could be implemented. Under it, crime would remain
constant, but the number of incarcerated citizens would fall from one million
to 100,000. Suppose, however, that, of those 100,000, 40,000 would be Black.

23. See infra note 208.
24. See Deborah Hellman, Measuring Algorithmic Fairness, 106 VA. L. REV. 811, 834-36
(2020).
25. In the United States, Black citizens comprise 37% of the prison population. Prison
Pol’y Initiative, Race and Ethnic Disparities, https://prisonpolicy.org/research/race_and_ethnicity [perma.cc/V8SN-25AX].
26. These proportions mirror America’s. John Gramlich, Black Imprisonment Rate in the
U.S. Has Fallen by a Third Since 2006, PEW RSCH. CTR. (May 6, 2020), https://www.pewresearch.org/fact-tank/2020/05/06/share-of-black-white-hispanic-americans-in-prison-2018-vs2006 [perma.cc/E39H-LZBP].
27. Analogous examples can be constructed for all major extant theories of fairness. Competing theories of fairness are discussed infra Section III.A.
28. See Gramlich, supra note 26.

806

Michigan Law Review

[Vol. 123:799

Standard, distribution-focused frameworks for measuring algorithmic
fairness would score the Algorithmic Abolitionist policy much worse than the
status quo. After all, the new policy would increase the Black share of incarceration from 33% to 40%.
Part III’s first new normative argument is that the standard approach is
missing something crucial. 29 True, the hypothetical policy worsens incarceration’s racial distribution in the hypothetical nation. But counterintuitively, and
much more importantly, the policy drastically reduces the number of people
mistreated because of their race. Here are the numbers: Under the status quo,
about 210,000 more Black citizens are locked up in our imaginary nation than
the fair rate would dictate. 30 That is, 210,000 people are discriminatorily imprisoned because of the color of their skin. But under the hypothetical Algorithmic Abolitionist policy, the number of people imprisoned because of race
would fall to 28,000—a reduction of 87%. 31
This is a generalizable failure of the standard approach to algorithmic fairness. It occurs whenever traditional, distribution-focused tools are employed
to evaluate a policy that radically reduces the level of a harmful outcome. In
such cases, traditional tools miss what matters most: the discriminatory injuries borne by actual human beings.
Formalizing these insights, Part III introduces a new quantitative tool for
measuring algorithmic fairness: “bias-impact.” Bias-impact measures the percentage reduction in the number of people who suffer discrimination—harmful outcomes unfairly imposed because of their race. It is a flexible tool. Biasimpact can be used to measure algorithmic discrimination under all major
theories of algorithmic fairness. Moreover, as Part III shows, no matter one’s
preferred theory, the actual Algorithmic Abolitionist policies proposed herein
would significantly reduce unfairness, measured using bias-impact.
Moving on, Part III introduces a second novel argument into the literature on algorithmic fairness. It concedes that, in addition to individual discriminatory injuries (captured by bias-impact), pure distributional fairness
(captured by traditional tools) carries some normative weight. The question
becomes how to trade off distributional improvements against other benefits—like reductions in the number of people suffering discrimination or in
the total number of people imprisoned and policed.
Part III proposes a new, strict framework for evaluating such tradeoffs.
The framework is both demanding and highly solicitous toward distributional
justice. So solicitous, the Part argues, that almost any proponent of pure distributional fairness ought to endorse the framework’s recommendations. 32
The framework centers on a rule dubbed the “Super Difference Principle,”

29. See infra Section III.B.1.
30. We have assumed for now that “fair” means proportionate to population share. So,
the number of unfair Black Americans imprisoned = 1M • (33% - 12%) = 210,000.
31. Calculation: 100,000 • (40% - 12%) = 28,000.
32. The argument is not that any normative theory should treat conformity to the framework as necessary, just that conformity is sufficient for approval.

March 2025]

Abolition by Algorithm

807

which borrows both prioritarian and Rawlsian distributional constraints—
and then supercharges them. The Super Difference principle demands that a
policy: (1) have, among practicable alternative policies, the highest “floor” of
outcomes for the worst off and (2) deliver the largest total benefit to the group
that, under the status quo, was the most disadvantaged. Part III shows that
Algorithmic Abolitionist policies would almost inevitably satisfy the Super
Difference Principle. This is again because Algorithmic Abolitionism radically
reduces bad outcomes, delivering the biggest benefits to those who, under the
status quo, would suffer the most.
Part III’s third novel argument about algorithmic fairness refocuses the
debate over structural inequality through the lens of Algorithmic Abolitionism. 33 Structural inequality, it is often argued, arises when modest initial inequalities compound over time. But, Part III argues, existing accounts of that
compounding are incomplete. They lack a model of differential growth: why,
for some racial groups, but not others, policing begets ever more policing. Part
III supplies such a model. It proposes that carceral harm, like a virus, has a
reproduction rate. 34 One arrest may cause, on average, one more arrest, more
than one, or less than one. If one group’s reproduction rate for arrests is above
one, while another’s reproduction rate is below one, arrests among the former,
but not the latter, group will compound. Part III gives reasons to think that
ambient levels of prison and policing drive their reproduction rates. If so, then
Algorithmic Abolitionist policies would, by substantially reducing those levels,
push reproduction rates downward for all groups. Doing so, they would promote long-run structural equality, not inequality, in prison and policing.
Finally, Part IV offers brief treatments of several other normative concerns. Why the brevity? Because there is less to say. Algorithmic Abolitionist
thinking, as just described, offers many new insights into debates over algorithmic discrimination. It offers some insights, but less decisive ones, elsewhere. Part IV describes how Algorithmic Abolitionism fits into conversations
about alternatives to policing; the political economy of crime; constitutional
constraints; and privacy and surveillance. Two themes recur throughout the
Part. First, unlike other policy approaches, Algorithmic Abolitionism is positive-sum. It offers the possibility of simultaneous wins to groups whose goals
are usually in conflict with one another. Algorithmic Abolitionist policies
could, for example, reduce both crime and punishment for crime. Second, Algorithmic Abolitionism’s reduction in levels of prison and policing would, unlike other algorithmic enforcement policies, reduce the total amount of harm
from invasions of privacy, constitutional violations, and more.

33. See infra Section III.C.
34. Nithya C. Achaiah, Sindhu B. Subbarajasetty & Rajesh M. Shetty, R0 and Re of COVID19: Can We Predict When the Pandemic Outbreak Will be Contained?, 24 INDIAN J. CRITICAL
CARE MED. 1125, 1125 (2020).

808

Michigan Law Review
I.

[Vol. 123:799

PRISON AND POLICE ABOLITIONISM

The American movement to abolish police and prisons feels new. And it
is, at least, newly prominent. Beginning in the mid-2010s, a series of police
killings—mostly of unarmed Black men—brought the high costs of policing
into public light. Each killing amplified the ever-growing wave of public protest against police violence. 35 Then, in 2020, George Floyd was murdered by
Derek Chauvin in Minneapolis. 36 The ensuing protests were nationwide and
massive. Polling suggests that tens of millions of Americans attended the rallies that summer, which would make them the largest in American history. 37
Atop this groundswell of public anti-policing sentiment, abolitionist ideas
broke through into the liberal and progressive mainstream. Most prominently,
activists across the nation called on governments to “defund,” “disband,” or
“abolish” the police. 38 No longer were these calls sequestered to the radical
fringes. Rather, prominent non-abolitionist-identifying liberals adopted them
nationwide. “Defund” proposals were published in the nation’s paper of record 39 and endorsed by sitting congresspeople. 40 And in June of 2020, a substantial plurality of Democratic-identifying voters supported such policies. 41
In Minneapolis, where Floyd was murdered, the city council unanimously
voted to disband the entire police department and replace it completely with
a to-be-defined “community-led public safety system.”42 Other major cities
pledged to substantially cut police funding. 43
In truth, the prison and police abolitionist movement long predates 2020.
Foundational thinkers Angela Davis, Ruth Wilson Gilmore, and Rose Braz
launched Critical Resistance 44—an organization devoted to “eliminat[ing] the

35. Keeanga-Yamahtta Taylor, The Emerging Movement for Police and Prison Abolition,
NEW YORKER (May 7, 2021) https://www.newyorker.com/news/our-columnists/the-emergingmovement-for-police-and-prison-abolition [perma.cc/QB4A-27MM].
36. Derrick Bryson Taylor, George Floyd Protests: A Timeline, N.Y. TIMES (Nov. 5, 2021),
https://www.nytimes.com/article/george-floyd-protests-timeline.html
[perma.cc/9FAH5MQY].
37. Larry Buchanan, Quoctrung Bui, & Jugal K. Patel, Black Lives Matter May Be the Largest Movement in U.S. History, N.Y. TIMES (July 3, 2020), https://www.nytimes.com/interactive/2020/07/03/us/george-floyd-protests-crowd-size.html [perma.cc/CTS2-8JCW].
38. See Kaba, supra note 2; Josiah Bates, How Are Activists Managing Dissension Within
the ‘Defund the Police’ Movement?, TIME (Feb. 23, 2021), https://time.com/5936408/defundthe-police-definition-movement [perma.cc/5D5R-LPVL].
39. Id.
40. See, e.g., AXIOS, supra note 3; Spocchia, supra note 3.
41. Parker & Hurst, supra note 1.
42. Beer, supra note 5.
43. Schneider, supra note 4; Rubinstein & Mays, supra note 4.
44. Honoring Rose Braz, CR Co-Founder and Abolitionist Leader, CRITICAL RESISTANCE
(June 22, 2017), https://criticalresistance.org/6125-2 [perma.cc/V5WB-RHD2]; The Economy of
Incarceration: Ruth Wilson Gilmore, CRITICAL RESISTANCE (May 26, 2015), https://criticalresistance.org/in-the-news/the-economy-of-incarceration-ruth-wilson-gilmore [perma.cc/Y4BXZ48Z].

March 2025]

Abolition by Algorithm

809

prison industrial complex”—in 1997. 45 Davis published her book, Are Prisons
Obsolete?, in 2003. 46 And Critical Resistance launched its newspaper, The Abolitionist, in 2005. 47 Allegra McLeod’s Prison Abolition and Grounded Justice introduced the “first sustained discussion” of prison abolition into the law
review literature in 2015. 48 A deluge of articles soon followed. 49 Thus, abolitionism is a diverse, multigenerational movement, encompassing thinkers
who both agree and disagree on many points. This Article’s recounting of the
movement is necessarily cursory.
The Article engages with prison and police abolitionism in terms familiar
from its recent breakthrough into mainstream discourse. Whatever their other
disagreements, in 2020, abolitionists succeeded in convincing a wide swath of
mainstream liberals of two core beliefs: First, prison and policing are inherently harmful, such that mere reform cannot adequately address their evils.
Second, consequentially, in order to reduce harm from prison and policing,
both should be mostly or completely abolished.
A. A Convincing Diagnosis
Abolitionists are correct about the problem. Prison and policing are inherently harmful, and no amount of reform can eliminate the relevant harms.
Certainly, high-profile tragedies like the police killings of unarmed Black men
are part of the problem—and perhaps emblematic of it. But they are just the
tip of the proverbial iceberg. As abolitionists rightly contend, even in the bestcase scenario—if the system were working as intended without overt corruption, conscious racism, or evil intent—policing and imprisonment would be
extraordinarily costly. 50
Many of these costs are, in fact, the point. Punishment, including imprisonment, is intentionally harmful. It is designed to impose costs on social bad
actors. Imprisoned persons are separated from their families and friends,
made to live under poor conditions, and restricted in their physical movement
and activities precisely because these things harm them. Policing, too, is costly
on its face. In the ordinary course of detecting and preventing crime, police
must stop, search, seize, and arrest citizens. Even if unaccompanied by violence—actual or threatened—these impositions of state power over individual

45. History, CRITICAL RESISTANCE, https://criticalresistance.org/mission-vision/history
[perma.cc/M5QS-RMKF].
46. ANGELA Y. DAVIS, ARE PRISONS OBSOLETE? (2003).
47. About, THE ABOLITIONIST, https://abolitionistpaper.wordpress.com/about-2
[perma.cc/P7FA-VANT].
48. Allegra M. McLeod, Prison Abolition and Grounded Justice, 62 UCLA L. REV. 1156,
1161 (2015).
49. See, e.g., India Thusi, Policing is Not a Good, 110 GEO. L.J. ONLINE (2022); Thomas
Ward Frampton, The Dangerous Few: Taking Seriously Prison Abolition and its Skeptics, 135
HARV. L. REV. 2013 (2022); Amna A. Akbar, An Abolitionist Horizon for (Police) Reform, 108 CAL.
L. REV. 1781 (2020); Roberts, supra note 2.
50. See McLeod, supra note 48, at 1205.

810

Michigan Law Review

[Vol. 123:799

liberty are damaging. It is the reason the Fourth Amendment exists—to place
limits on the amount of damage the police can do when fighting crime. 51
These observations are not unique to abolitionism. Liberal thinkers since
Bentham have classed punishment as an evil “in itself.” 52 Under Benthamite
Utilitarianism—and derivative consequentialist theories—such evil is permitted only to the extent necessary to prevent even greater harms from crime. 53
But, as abolitionists emphasize, the heavy costs of prison and policing go
far beyond the baked-in harms necessary to achieve deterrence. Prisons, for
example, are not actually sterile sites of moderate isolation, constrained freedom, and modest living—secure enough to incapacitate and bad enough to
deter, but no more. They are instead sites, as McLeod puts it, of “intense brutality, violence, and dehumanization.” 54 Currently, tens of thousands of imprisoned people are locked in solitary confinement, caged in small cells, and
completely isolated for twenty-three or twenty-four hours per day. 55
Again, the abolitionists are not alone in raising such concerns. A bevy of
quantitative social science research shows that the costs of policing and prison
go well beyond the intended ones. The empirics show that the costs of an encounter with the criminal justice system can redound for a lifetime, or beyond.
First, there are the economic consequences. Contact with the criminal justice
system seriously impairs one’s ability to find a job and earn a living. 56 This
effect worsens—in both severity and persistence—as the contact grows. 57 This
is true even for those to whom the presumption of innocence applies. Being
held in jail pretrial—even briefly before charges are dropped or an acquittal is
entered—can be economically disastrous. 58 Employers need not and do not

51. U.S. CONST. amend. IV (protecting the right to be “secure . . . against unreasonable
searches and seizures”).
52. JEREMY BENTHAM, THE RATIONALE OF PUNISHMENT 23 (1830).
53. Id.; see Brad Hooker, Consequentialism, in THE ROUTLEDGE COMPANION TO ETHICS
444, 444 (John Skorupski ed., 2010) (defining consequentialist theories).
54. McLeod, supra note 48, at 1173 (citing COMM’N ON SAFETY & ABUSE IN AMERICA’S
PRISONS, CONFRONTING CONFINEMENT 52 (2006)).
55. Id. at 1174; SOLITARY WATCH & UNLOCK THE BOX, CALCULATING TORTURE 4 (2023),
https://solitarywatch.org/wp-content/uploads/2023/05/Calculating-Torture-Report-May2023-R2.pdf [perma.cc/7YPA-QQSB] (finding that “prisons and jails across the U.S. reported
locking more than 122,000 people in solitary confinement for 22 or more hours on a given day
in 2019”).
56. Michael Mueller-Smith, The Criminal and Labor Market Impacts of Incarceration 3
(Univ. Mich. Working Paper, 2015), https://sites.lsa.umich.edu/mgms/wp-content/uploads/sites/283/2015/09/incar.pdf [perma.cc/462B-2RSV]; see also Elizabeth Berger & Kent S.
Scheidegger, Sentence Length and Recidivism: A Review of the Research, 35 FED. SENT’G REP. 59,
68 (2022) (arguing that the effects of incarceration on recidivism are complex and more research
is needed).
57. Mueller-Smith, supra note 56, at 3.
58. See generally Will Dobbie, Jacob Goldin & Crystal S. Yang, The Effects of Pretrial Detention on Conviction, Future Crime, and Employment: Evidence from Randomly Assigned Judges,
108 AM. ECON. REV. 201 (2018).

March 2025]

Abolition by Algorithm

811

hold jobs open during such periods of incarceration. Worse, since incarcerated people are disproportionately poor, losing a job can tip off a spiral of economic hardship—high-interest loans, unpaid debts, eviction, and more. Other
economic costs of the criminal justice system are imposed directly. Criminal
defendants are legally obligated to pay certain fees arising from their cases—
sometimes including tens of thousands of dollars in “room and board” for
their prison stays. 59 If these bills go unpaid, perhaps due to lack of employment, the penalty is often additional fines and fees. 60
Criminal punishment also destroys relationships. Even after incarceration
ends, couples with an incarcerated member are more likely to divorce. 61 The
children of incarcerated people are thus more likely to live in a single-parent
household both during and after incarceration. 62 Beyond family, incarcerated
persons generally have fewer strong social connections than the population at
large. 63
The criminal justice system can also kill you, even long after your last encounter with it. Former prisoners have substantially worse health outcomes
than other groups. 64 They are more likely to die early. 65 The effects can stretch
beyond the grave. The children of incarcerated persons have worse life outcomes than those of similarly situated nonincarcerated persons. 66
Finally, incarceration is criminogenic—that is, it causes crime. Quasi-randomized studies show that, beyond some minimum, each marginal month
spent imprisoned increases the expected number of crimes a person will commit over their lifetime. 67 This paradoxical result is discussed in greater detail
below, 68 but the intuition is easy enough to grasp: If being imprisoned destroys
your earning power, saddles you with unpayable debt, weakens your social
network, and worsens your health, it might for those same reasons drive you
59. Chandra Bozelko & Ryan Lo, You’ve Served Your Time. Now Here’s Your Bill,
HUFFINGTON POST (Sept. 16, 2018), https://www.huffpost.com/entry/opinion-prison-strike-labor-criminal-justice_n_5b9bf1a1e4b013b0977a7d74 [perma.cc/963K-M28H].
60. Id.
61. Sonja E. Siennick, Eric A. Stewart & Jeremy Staff, Explaining the Association Between
Incarceration and Divorce, 52 CRIMINOLOGY 371, 371 (2014).
62. Id. at 374. Of course, depending on the prior family relationship, this may or may not
count as a cost.
63. Jennifer C. Kao et al., Associations Between Past Trauma, Current Social Support, and
Loneliness in Incarcerated Populations, 2 HEALTH & JUST. 1, 1–2, no. 7, 2014.
64. Michael Massoglia & Brianna Remster, Linkages Between Incarceration and Health,
134 PUB. HEALTH REPS. 94, 95 (2019) (collecting evidence); but see Samuel Norris, Matthew
Pecenco & Jeffrey Weaver, The Effect of Incarceration on Mortality (Jan. 28, 2022) (unpublished
manuscript), https://ssrn.com/abstract=3644719 [perma.cc/VT33-M3GL] for one study finding
the opposite.
65. Massoglia & Remster, supra note 64, at 95.
66. See generally Will Dobbie et al., The Intergenerational Effects of Parental Incarceration
(Nat’l Bureau of Econ. Rsch., Working Paper No. 24186, 2018), http://www.nber.org/papers/w24186 [perma.cc/V5PU-SGMH].
67. See generally Mueller-Smith, supra note 56.
68. See infra Section I.B.

812

Michigan Law Review

[Vol. 123:799

to commit more crimes. This induces a vicious cycle—prison causes harm,
which causes more crime, which causes more prison, and so on.
As abolitionists regularly emphasize, these costs are not evenly distributed. At every juncture—search, seizure, arrest, jail, charging, trial, sentencing,
and parole—the harms of prison and policing are disproportionately imposed
on already-disadvantaged groups. Black men bear the brunt. 69 But so do other
people of color, the poor, sexual minorities, and other marginalized communities. 70 Yet again, quantitative social science supports the abolitionist diagnosis. Robust empirical evidence shows that these racial and other social
disparities cannot be fully explained by differences in base rates of crime commission between groups. Rather, discrimination is at work across the criminal
justice system. 71
Thus, the abolitionists are clearly right about something: Prison and policing are extremely costly, both because that is their point and because of their
many downstream, legally unintended consequences. None of that is seriously
contestable.
But abolitionists go even further, arguing that these costs are so deeply
entrenched in policing and prison that no amount of reform could satisfactorily ameliorate them. Framed a certain way, this claim is contestable. For example, as with other kinds of violence, a large proportion of police violence
and other misconduct is committed by a small proportion of officers. 72 Yet,
due to special protections written into law and police union contracts, those
officers are almost never fired or disciplined. 73 Thus, violent police encounters
might be reduced simply by making police officers subject to ordinary mechanisms of legal and professional accountability. 74 Reforms might also improve

69. See generally Gramlich, supra note 26 (prisons); Sharad Goel, Justin M. Rao & Ravi
Shroff, Precinct or Prejudice? Understanding Racial Disparities in New York City’s Stop-and-Frisk
Policy, 10 ANNALS OF APPLIED STAT. 365 (2016) (policing).
70. See generally Gramlich, supra note 26 (showing elevated levels of Hispanic incarceration); Ilan H. Meyer et al., Incarceration Rates and Traits of Sexual Minorities in the United States:
National Inmate Survey 2011−12, 107 AM. J. PUB. HEALTH 267 (showing elevated levels for sexual
minorities); VIRGINIA EUBANKS, AUTOMATING INEQUALITY: HOW HIGH-TECH TOOLS PROFILE,
POLICE, AND PUNISH THE POOR (2018).
71. See, e.g., Goel, Rao & Shroff, supra note 69, at 375 (policing). See generally Crystal S.
Yang, Free at Last? Judicial Discretion and Racial Disparities in Federal Sentencing, 44 J. LEGAL
STUD. 75 (2015) (prison).
72. Samuel Walker, Geoffrey P. Alpert & Dennis J. Kenney, Early Warning Systems: Responding to the Problem Police Officer, NAT’L INST. JUST. RSCH. BRIEF, July 2001, at 1.
73. Mike Riggs, Why Firing a Bad Cop is Damn Near Impossible, REASON (Oct. 19, 2012),
https://reason.com/2012/10/19/how-special-rights-for-law-enforcement-m[perma.cc/B9YD999Q]; Matthew Yglesias, Fixing the Police Will Take More Funding, Not Less, SLOW BORING (Jan.
25,
2021),
https://www.slowboring.com/p/fixing-the-police-will-take-more?s=r
[perma.cc/LNA7-HLJT].
74. Yglesias, supra note 73. But see Aaron Chalfin & Jacob Kaplan, How Many Complaints
Against Police Officers Can Be Abated by Incapacitating a Few “Bad Apples”?, 20 CRIMINOLOGY &
PUB. POL. 351, 351 (estimating that replacing the 10% of officers most likely to commit misconduct would reduce misconduct by only 4% to 6%).

March 2025]

Abolition by Algorithm

813

racial unfairness in policing. Evidence from some cities suggests that Black
and Hispanic officers are less biased in making stops and arrests or using
force. 75 And these officers initiate fewer stops and arrests with force than their
white counterparts. 76 Thus, reforms that diversify police departments, too,
could make a difference.
But framed another way, the abolitionist claim that reform cannot meaningfully address the serious harms of prison and policing is obviously true. As
just discussed, the problems with policing and prison are not limited to excesses of the system. Much of what is bad about prison and policing is inherent
in both—a feature, not a bug. And that which is not inherent is exceedingly
unlikely to be completely—or even mostly—fixed via reform. For example, it
is unlikely that reforms to incarceration could prevent the downward economic spirals that so often result from even short periods of confinement.
Most jobs cannot be done remotely from a prison cell, even if employers were
willing. And employers are not willing. Moreover, the hiring stigma against
individuals who have had contact with the criminal justice system remains intense. 77 It is not clear that it can be reduced via policy. Previous attempts have
backfired. 78 The same goes for family, interpersonal, and intergenerational
consequences. As long as the criminal enforcement system continues to involve taking people out of their families and communities and placing them
in new criminogenic communities, there will be serious social effects.
The best version of the abolitionist argument is thus not that reforms can
do nothing to blunt these effects. It is that they cannot do enough. They fall far
short of a cure. Both logic and empirical investigation show the abolitionists
have all of this correct.
B. Bitter Medicine
If the lion’s share of prison and police’s costs cannot be redressed by reform, a different solution suggests itself: abolish prisons and police. That is
exactly what abolitionists now demand. This position is perhaps exemplified
by the movement’s most successful policy campaign to date, “defund the police.” Almost immediately after George Floyd’s murder, a nationwide chorus
of activists called for police departments to be literally and immediately eliminated—either in whole or in large part.79
As already noted, these proposals were supported by a plurality of Democrat-identifying Americans—the majority party in most major cities with large
75. See generally Bocar A. Ba, Dean Knox, Jonathan Mummolo & Roman Rivera, The Role
of Officer Race and Gender in Police-Civilian Interactions in Chicago, 371 SCI. 696 (2021).
76. Id.
77. Amanda Agan & Sonja B. Starr, The Effect of Criminal Records on Access to Employment, 107 AM. ECON. REV. 560 (2017).
78. See generally Jennifer L. Doleac & Benjamin Hansen, The Unintended Consequences
of “Ban the Box”: Statistical Discrimination and Employment Outcomes When Criminal Histories
are Hidden, 38 J. LAB. ECON. 321 (2020).
79. See, e.g., Kaba, supra note 2.

814

Michigan Law Review

[Vol. 123:799

police forces. Those cities took their voters’ preferences seriously. As already
noted, Minneapolis’s city council almost immediately pledged to “dismantl[e]” the city’s police department. 80 And other cities, to a lesser degree,
followed suit. San Francisco’s mayor promised to cut police funding by $120
million—approximately 14% of the projected budget. 81 New York likewise
pledged to cut its policing budget by $1 billion, or about 17%. 82 Political figures, media outlets, and academics lent their support to the cause. Ilhan
Omar—whose congressional district encompasses much of Minneapolis—
said of the city’s “defund” plan that “you can’t really reform a department that
is rotten to the root.” 83 Alexandria Ocasio-Cortez wrote that policing is “an
indefensible system” and that “reform measures do not ultimately solve what
is a systemic problem.”84 The New York Times ran an opinion piece headlined,
Yes, We Mean Literally Abolish the Police. 85 In it, activist Mariame Kaba advocated—as an intermediate abolitionist goal—immediately halving police
budgets and officer counts. 86 In an essay in the Georgetown Law Journal
Online, India Thusi contends that the demand to defund the police “deserves
serious scholarly engagement.” 87
Then, abolitionists lost their momentum. Their early policy successes in
places like Minneapolis, New York, and San Francisco proved illusory. The
reason, it seems, was crime. In 2021, the United States saw a modest—but nontrivial—nationwide uptick in homicide, widely discussed in the runup to the
midterm elections. 88 Public support for policies like “defund the police” collapsed, even among Democrats. 89 Neither New York nor San Francisco made
the promised deep cuts to police budgets. 90 And Minneapolis quietly shelved
its plan to disband its police force. 91

80. Jason Slotkin & Adrian Florido, Minneapolis City Council Members Announce Intent
to ‘Dismantle’ Police Department, NPR (June 7, 2020, 6:13 PM), https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/06/07/871727567/crowd-cries-shame-afterminneapolis-mayor-answers-no-to-defunding-police [perma.cc/EG5A-7CJT].
81. See Schneider, supra note 4.
82. Rubinstein & Mays, supra note 4.
83. AXIOS, supra note 3.
84. Spocchia, supra note 3.
85. Kaba, supra note 2.
86. Id.
87. Thusi, supra note 49. Note, however, that some prison and police abolitionists prefer
a more incremental approach, enacting abolition only once the root causes of crime are eliminated. See, e.g., McLeod, supra note 48, at 1161; Roberts, supra note 2, at 43–48; DAVIS, supra
note 46, at 105–13. This has the obvious downside that eradicating racism, misogyny, joblessness, homelessness, addiction, and more is a very long-term project.
88. See Treisman, supra note 6.
89. Parker & Hurst, supra note 1.
90. Schneider, supra note 4; Rubinstein & Mays, supra note 4; Manthey, Esposito, & Hernandez, supra note 8.
91. Londoño, supra note 9.

March 2025]

Abolition by Algorithm

815

Abolitionists, it seems, managed to convince left-leaning voters of the diagnosis. But when it came time to administer the cure, it proved too bitter to
swallow. Plausibly, the nationwide increase in homicides reminded ordinary
citizens that prison and policing, while extraordinarily costly, are there to try
to prevent the even larger costs of serious crime. Perhaps, they reasoned, that
for all of their ills, prison and policing were a necessary evil; even moderate
across-the-board cuts would do more harm than good, including for the
groups policing and prison burden most.
This is all correct, too, as another robust body of empirical findings shows.
Serious crime disproportionately affects low-income people, people of color,
and members of sexual and gender minority groups. 92 Such crimes cause
grievous injury or death to their victims. They also have economic effects, significantly reducing victims’ earnings, increasing their reliance on public benefits, and reducing their health. 93
Moreover, prison and policing are vital tools for controlling crime. Even
modest-across-the board cuts cause significant increases in serious crime. A
handful of decades-old, empirically unsophisticated studies once suggested
otherwise. 94 And, occasionally, some abolitionists will repeat those old
claims. 95 But since the 1980s, a raft of studies with much better causal identification strategies have shown that, for better or worse, the old view was wrong.
Here is a necessarily incomplete survey.
1.

On Policing

A clever 2005 study uses exogenous variation in the terror alert level—
which in turn caused variation in the level of policing in Washington, D.C.—
to measure the effect of policing on crime. 96 The study finds significant effects:

92. See Andrew R. Flores, Bianca D. M. Wilson, Lynn L. Langton & Ilan H. Meyer, Violent
Victimization at the Intersections of Sexual Orientation, Gender Identity, and Race: National
Crime Victimization Survey, 2017–2019, PLOS ONE (2023), https://doi.org/10.1371/journal.pone.0281641; Benoît De Courson & Daniel Nettle, Why Do Inequality and Deprivation Produce High Crime and Low Trust?, 11 SCI. REPS. 1937 (2021); See generally Ulmer, Harris &
Steffensmeier et al., supra note 14.
93. Anna Bindler & Nadine Ketel, Scaring or Scarring? Labor Market Effects of Criminal
Victimization, 40 J. LAB. ECON. 939, 939 (2022).
94. For a survey, see Samuel Cameron, The Economics of Crime Deterrence: A Survey of
Theory and Evidence, 41 KYKLOS 301, 323 (1988).
95. E.g., Alec Karakatsanis, Policing, Mass Imprisonment, and the Failure of American Lawyers, 128 HARV. L. REV. F. 253, 260–61 (2015) (arguing that there is “no evidence that [policing
and prison] work”).
96. Jonathan Klick & Alexander Tabarrok, Using Terror Alert Levels to Estimate the Effect
of Police on Crime, 48 J.L. & ECON. 267 (2005).

816

Michigan Law Review

[Vol. 123:799

a 6.6% citywide reduction in crime on “high” alert days, compared with “elevated” alert days. 97 The reduction was over twice as high—15%—on the National Mall, where police presence likely increased the most during periods of
high terrorism alert. 98
The crime-preventing effects of policing are not limited to minor, qualityof-life crimes. Policing prevents murder. A study published in 2022 leverages
variation in the timing of federal block grants to measure the effect of police
on homicides. 99 It finds that hiring ten to seventeen police officers saves, on
average, one life per year that would otherwise end by homicide. 100 The percapita effect is significantly larger for Black victims. 101 A similar study from
2019 compares cities that barely qualified for federal policing subsidies with
those that barely failed to qualify. 102 It finds similar results. 103 Hiring ten additional officers prevented approximately one murder, five rapes, and twenty
robberies annually. 104
A 2016 paper investigates what happened when New York directed surges
of police officers into high-crime areas. 105 It finds that the surges caused an
11% reduction in all violent felonies, including a 12% reduction in assaults
and a 15% reduction in robberies. 106 Major property crimes fell, too—and by
even larger amounts. Overall, property felonies went down by 26%, and burglary fell by 46%. 107
2.

On Prison

Punishment—and incarceration in particular—prevents crime at the societal level. In 2011, California was forced by a federal court to reform its corrections code and enact a “very large and relatively sudden decline in
incarceration rates.” 108 A 2016 study relied on county-level variation in preand post-reform incarceration rates to estimate the change’s effect on crime. 109

97. Id. at 271.
98. Id. at 273.
99. Aaron Chalfin, Benjamin Hansen, Emily K. Welsburst & Morgan C. Williams, Jr., Police Force Size and Civilian Race, 4 AM. ECON. REV. 139, 141 (2022).
100. Id. at 146.
101. Id.
102. Steven Mello, More COPS, Less Crime, 172 J. PUB. ECON. 174, 175 (2019).
103. See id. at 175.
104. See id. at 185.
105. John MacDonald, Jeffrey Fagan & Amanda Geller, The Effects of Local Police Surges
on Crime and Arrests in New York City, PLOS ONE (June 16, 2016), https://doi.org/10.1371/journal.pone.0157223.
106. See id. at 7 tbl.1 (percent reduction = 1 – e (Model 1 impact figure).
107. See id.
108. Magnus Lofstrom & Steven Raphael, Incarceration and Crime: Evidence from California’s Public Safety Realignment Reform, 664 ANNALS AM. ACAD. POL. & SOC. SCI., Mar. 2016 at
197, 200.
109. Id. at 202–04.

March 2025]

Abolition by Algorithm

817

It finds that each additional release generated as many as 0.04 violent crimes
each month for every 100,000 California residents. 110 An earlier, similar
study—likewise estimating the effects of broad decarceration forced by litigation—finds similar jurisdiction-wide results. 111
Studies quantifying incarceration’s individual-level, rather than societylevel, effects often find net reductions in crime. One recent study leveraging
Ohio’s random assignment of defendants to judges—who vary in their average
harshness in sentencing—finds a modest net reduction in crime from incapacitation. 112 Another study from 2021 uses a sudden change in North Carolina’s
sentencing guidelines to estimate the dose-response effect of incarceration. 113
That is, it quantifies how much each marginal year of incarceration reduces
the incarcerated person’s likelihood of being reincarcerated in the future. 114
The study finds a large crime-reducing effect from the first year of incarceration—44% less incarceration over the next three years—with effects diminishing for each additional year. 115
This finding is consistent with the small number of studies finding that
incarceration is, on net, criminogenic as to the incarcerated individuals. 116
These do not suggest that prison lacks any incapacitative or specific deterrent
effect. Rather, it just suggests that those effects diminish as sentences grow
longer and can thus, under certain conditions, be overtaken by criminogenic
effects. 117 More importantly, none of this contradicts the claim that incarceration decreases crime at the level of society—as opposed to at the level of individual incarcerated persons. Even if it increased crime for those actually
incarcerated, this relatively small crime-producing effect could be swamped
by the general deterrent effect on everyone else. And that is exactly what the
studies—discussed above— 118of prison’s total societal effect find.

110. Id. at 211 tbls.4 & 21. Note that this estimate is sensitive to changes in the statistical
controls, with some approaches showing a positive but statistically nonsignificant effect of release violent crime. Estimates of decarceration’s positive effect on property crimes are more consistent across methods.
111. See Steven D. Levitt, The Effect of Prison Population Size on Crime Rates: Evidence from
Prison Overcrowding Litigation, 111 Q.J. ECON. 319, 345 (1996) (finding one prisoner release associated with fifteen additional crimes).
112. Samuel Norris, Matthew Pecenco & Jeffrey Weaver, The Effects of Parental and Sibling
Incarceration: Evidence from Ohio, 111 AM. ECON. REV. 2926, 2927, 2944 (2021).
113. Evan K. Rose & Yotam Shem-Tov, How Does Incarceration Affect Reoffending? Estimating the Dose-Response Function, 129 J. POL. ECON. 3302 (2021).
114. See id. at 3302, 3345 fig.A.
115. Id. at 3302, 3341.
116. See, e.g., Mueller-Smith, supra note 56, at 1, 20. But see Rose & Shem-Tov, supra note
113.
117. Mueller-Smith, supra note 56, at 20.
118. Norris, Pecenco, & Weaver, supra note 112, at 2946; Rose & Yotam Shem-Tov, supra
note 113, at 3302.

818

Michigan Law Review

[Vol. 123:799

Hence, the turn among ordinary liberals against abolitionist policies was
reasonable, assuming that they cared about both the harms from prison and
policing and the harms from serious crime. The turn can be understood as a
rejection of policies that would reduce one set of important harms only by
increasing another. Voters may simply have determined that abolitionist proposals’ costs would, on balance, outweigh their benefits.
This suggests that ordinary liberals’ turn against prison and police abolitionism might well be limited to rejecting just the particular policies on offer—
not the ideology wholesale. There is good reason to believe that abolitionists’
normative arguments retain their full force. Nothing about the 2021 homicide
spike undermines the arguments for policing and imprisonment’s heavy costs,
nor their incurability via reform. Thus, it stands to reason, the voters who supported abolitionists in 2020 might support them again, if only there were a
way to substantially reduce prison and policing without increasing crime.
II.

ALGORITHMIC ABOLITIONISM

Algorithmic Abolition offers such a solution. It is a way to maximally act
on prison and police abolitionists’ forceful normative critique while responding to concerns about serious crime harbored by even “abolition curious” liberal voters. Algorithmic Abolitionism is abolitionism in that it radically
reduces carceral harm by elimination, not reform. But unlike previous abolitionist proposals, Algorithmic Abolitionism would accomplish its elimination
without allowing crime to increase.
To be clear, Algorithmic Abolition is not total abolition. The approach
would not eliminate all prison and policing on its own. It is thus perhaps best
described as what Amna A. Akbar has dubbed a “non-reformist reform,” the
kind of important intermediate step toward fundamental transformation that
radicals should embrace. 119 In particular, Algorithmic Abolitionism would satisfy Akbar’s key criterion of helping to shift the “balance of power” away from
carceral authorities. 120 Likewise, Algorithmic Abolitionist policies could directly achieve the goals of prominent abolitionists like Mariame Kaba, reducing various kinds of policing by well over her target of 50%. 121
Algorithmic Abolitionism has become possible only recently—in the last
five to seven years. Algorithms, however, have been used in criminal enforcement for much longer than that. The infamous 122 COMPAS tool, for example,
has been used by local governments to make bail decisions since at least
2008. 123 Other actuarial—and thus algorithmic, in a sense—approaches to risk

119. See Amna A. Akbar, Non-Reformist Reforms and Struggles over Life, Death, and Democracy, 132 YALE L.J. 2497 (2023).
120. Id. at 2568.
121. Kaba, supra note 2; see infra Section II.B.
122. See Angwin, et al., supra note 15.
123. THOMAS BLOMBERG ET AL., CTR. FOR CRIMINOLOGY AND PUB. POL’Y RSCH.,
VALIDATION OF THE COMPAS RISK ASSESSMENT CLASSIFICATION INSTRUMENT 15 (2010).

March 2025]

Abolition by Algorithm

819

scoring were first used for the same purpose in the 1960s. 124 But there is little
reason to think that these earlier algorithms could accomplish the feats of
decarceration and de-policing described herein. 125
For algorithms to unlock significant abolitionist potential, modern machine learning was required. The world is currently in the midst of a “Machine
Learning Explosion.” 126 The explosion was triggered by a confluence of related
technological factors: breakthroughs in algorithmic design, massive increases
in data, and ever more processing power. 127 Over the past twenty years, each
of these preconditions for rapid algorithmic advancement has improved by at
least one order of magnitude and as many as three. 128
The result has been a blinding proliferation of algorithmic accomplishments. Modern machine learning algorithms power large language models,
like GPT-4, that can perform a range of text-based tasks from coding to passing the bar exam. 129 They safely pilot the autonomous taxis currently carrying
riders across San Francisco. 130 They can generate creative, beautiful, and completely unique images in any artistic style, based on simple natural-language
prompts. 131
Modern machine learning techniques were perhaps first brought to bear
on criminal enforcement by Jon Kleinberg, Himabindu Lakkaraju, Jure Leskovec, Jens Ludwig, and Sendhil Mullainathan, through their algorithm published in a 2018 paper. 132 Their algorithm’s goal—like many algorithms before
124. Christopher T. Lowenkamp, Richard Lemke & Edward Latessa, The Development and
Validation of a Pretrial Screening Tool, 72 FED. PROB., Dec. 2008, https://www.uscourts.gov/federal-probation-journal/2008/12/development-and-validation-pretrial-screening-tool
[https://perma.cc/7P3G-2MDF].
125. It is possible that the COMPAS tool, if put to abolitionist purposes, might be able to
achieve significant decarceral effects. But this is difficult to know. COMPAS’s exact formula is a
trade secret, held closely by its private owners. Frank Pasquale, Secret Algorithms Threaten the
Rule of Law, MIT TECH. REV. (June 1, 2017), https://www.technologyreview.com/2017/06/01/151447/secret-algorithms-threaten-the-rule-of-law
[perma.cc/RR7V-RE8T]. Thus, there are to my knowledge no studies simulating its potential
abolitionist effects. Even so, COMPAS’s primary risk scoring tool used basic statistical methods
such as linear regression, logistic regression, and survival analysis, not one of the more advanced
algorithms associated with modern machine learning. Cynthia Rudin, Caroline Wang, & Beau
Coker, The Age of Secrecy and Unfairness in Recidivism Prediction, HARV. DATA SCI. REV., Winter
2020, at 5, https://doi.org/10.1162/99608f92.6ed64b30 [https://perma.cc/X55J-EMUB].
126. Brynjolfsson & McAfee, supra note 16, at 12.
127. Id.
128. See id.
129. OpenAI, GPT-4 TECHNICAL REPORT 5–6 (2023), https://arxiv.org/pdf/2303.08774v6
[perma.cc/DTQ7-FJJL].
130. Andrew Myers, How AI Is Making Autonomous Vehicles Safer, STANFORD UNIV.
HUMAN-CENTERED ARTIFICIAL INTELLIGENCE (Mar. 7, 2022), https://hai.stanford.edu/news/how-ai-making-autonomous-vehicles-safer [perma.cc/ZGK3-5JKJ].
131. See generally ADITYA RAMESH ET AL., OPENAI, HIERARCHICAL TEXT-CONDITIONAL
IMAGE GENERATION WITH CLIP LATENTS (2021).
132. Jon Kleinberg et al., Human Decisions and Machine Predictions, 133 Q.J. ECON. 237
(2018).

820

Michigan Law Review

[Vol. 123:799

it—was to determine which defendants would be likely to commit crimes if
not incarcerated while awaiting trial. 133 As with other applications of next-generation machine learning to difficult problems, the result was a quantum leap
forward. As discussed in detail below, their algorithm performed remarkably
better than the status quo. 134 Today, high-quality, peer-reviewed empirical evidence shows that, by using algorithms to make various decisions about prison
and policing, dramatic reductions—on the order of 40%, 80%, or more, depending on the context—are possible.
This Part lays out—for the first time 135—a comprehensive vision of how
algorithms could begin abolishing police and prisons. It goes beyond narrow
discussions of, for example, pretrial risk assessment, considering algorithms’
potential across the whole range of criminal enforcement functions. The Part
is quantitative. Relying on the best available empirical evidence, it shows both
that prison and policing could be dramatically reduced using algorithms
and—for each function—attempts to estimate by how much. Law review literature has started to absorb some of the operative evidence—especially the
Kleinberg et al. algorithm—but much of this evidence is too new to have been
properly incorporated. 136
This Part goes beyond merely collecting existing evidence. It represents
the first attempt to think systematically about how modern predictive algorithms could be implemented to maximum abolitionist effect. As the Part describes, many jurisdictions have already begun to experiment with the use of
algorithms in policing and incarceration. But nowhere have those algorithms
yet produced the dramatic reductions in either institution described here. This
Part explains why. Doing so, the Part lays down a set of key principles for the
successful design and implementation of Algorithmic Abolitionist policies.

133. Id. at 239.
134. Id. at 241.
135. The detailed Algorithmic Abolitionist proposals here are novel. But this is not the first
Article to argue that algorithms could help to reduce incarceration. The legal scholar who has
done the most to advance these arguments is probably Christopher Slobogin. His book-length
treatment of algorithms in criminal justice, JUST ALGORITHMS: USING SCIENCE TO REDUCE
INCARCERATION AND INFORM A JURISPRUDENCE OF RISK (2021), is excellent. The proposals there
differ in important ways from Algorithmic Abolitionism: First, and most importantly, it is not
abolitionist at all. Slobogin’s goal is not to maximally eliminate prison and policing. Instead, Slobogin relies on a limiting retributivist theory, under which justice requires some minimum punishment for crime. Second, and perhaps because of this theoretical difference, Slobogin’s book is
not focused on attempting to quantify, as this Article does, how much prison algorithms could
help to eliminate. Third, Slobogin’s proposal is limited to incarceration, while Algorithmic Abolitionism spans other areas of criminal enforcement. Finally, because Slobogin’s proposal is not
abolitionist, it does not directly raise the novel normative arguments discussed in Part III. Slobogin has recently expanded the arguments from his book in an excellent essay, The Minimalist
Alternative to Abolitionism: Focusing on the Non-Dangerous Many, 77 VAND. L. REV. 531 (2024).
That does include interesting estimates, distinct from those here, about the amount by which
algorithms could help to reduce incarceration. Id. at 548.
136. Aziz Z. Huq, A Right to a Human Decision, 106 VA. L. REV. 611, 639 (2020).

March 2025]

Abolition by Algorithm

821

A. Prisons
Of the policies proposed in this Article, the one that has come closest to
having been tried is the Algorithmic Abolition of prisons. In recent years,
many jurisdictions have incorporated algorithmically generated risk scores
into their pretrial incarceration decisions. 137 And a few states have incorporated them into sentencing post-conviction. 138 Section II.C returns to these
experiments to suggest that none of them has, in fact, been either truly abolitionist or truly algorithmic.
Let us first explore how much decarceration would be possible under a
genuine Algorithmic Abolitionist regime. Begin with pretrial incarceration:
Here, the Algorithmic Abolitionist goal is to eliminate as much jailing as possible without increasing either of two bad outcomes. First, if released, certain
defendants might flee the jurisdiction and thus avoid responsibility for crimes
already committed. 139 Second, if released, certain defendants might commit
further crimes. 140 If algorithms could predict who will jump bail or commit
crimes with greater accuracy than status-quo decisionmakers—judges—then
much needless incarceration could be avoided.
Indeed, algorithms vastly outperform humans. Consider again the aforementioned algorithm—a gradient boosted decision tree—trained by Kleinberg et al. 141 This algorithm was designed, in the first instance, to predict
failure to appear. 142 But Kleinberg et al. show that their algorithm would perform even better if asked to predict freestanding crimes. 143
The algorithm’s predictions—and incarceration decisions—were compared in a simulation against the actual decisions judges made. The algorithm
came out far ahead. The 1% of defendants that the algorithm identified as having the highest risk were rearrested 62.7% of the time. 144 Yet judges released
nearly half of those individuals. 145 The judges who did so were not simply being lenient. The strictest subset of judges jailed more people—but an essentially random collection from across the risk spectrum. 146 These judges were
not meaningfully better at predicting and detaining the individuals most likely
to commit crimes upon release.
What kind of Algorithmic Abolitionist policy could be implemented using
such predictions—and to what effect? Suppose high-performing algorithms,

137. MAPPING PRETRIAL INJUSTICE, supra note 22.
138. Angwin et al., supra note 15.
139. Kleinberg et al., supra note 132, at 245. In many jurisdictions this is itself a crime. See,
e.g., N.Y. Penal Law, § 215.58 (McKinney 2024).
140. Kleinberg et al., supra note 132, at 245.
141. See generally id.
142. Id. at 239.
143. Id. at 275.
144. Id. at 240.
145. Id.
146. Id.

822

Michigan Law Review

[Vol. 123:799

rather than low-performing judges, imposed pretrial incarceration only on
those individuals most likely to commit crimes if released. What risk level
would be sufficient to justify incarceration? Here, we can appeal to the definition of Algorithmic Abolition outlined above: Algorithmic Abolitionism seeks
to eliminate as much incarceration as possible without increasing crime. Thus,
the crime-risk cut score would be set at the status quo rate of recidivism. Anyone under that score would be released and, thus, crime would be held constant.
What impact would such a policy have? Kleinberg et al. tell us. They performed exactly this simulation—ranking pretrial defendants from riskiest to
least risky and release as many as possible without increasing observed crime.
The result: pretrial incarceration could be reduced by as much as “41.9% with
no increase in crime rates.” 147 Hence, if algorithmic, risk-based incarceration
decisions completely replaced judges, the American level of pretrial incarceration would be permanently reduced by roughly 185,000 people annually. 148
In the first decade alone, millions of prison years would be avoided. And the
resulting predicted increase in crime—from bail jumping to misdemeanors to
murder—would be zero.
Some might worry that these New York-based results would not generalize to the rest of the country. On the contrary, the Kleinberg et al. pretrial risk
algorithm also works on a national dataset, to similar effect. 149
Others might worry that the massive effect reported above is overstated as
a best-case scenario. True, a reduction of over 40% is the high end of the reported range. But the low-end estimate is still unprecedented: an 18.5% reduction in incarceration—a total of 82,000 people. 150 Importantly, this low-end
estimate is conservative in the extreme. It assumes that every single person in
the dataset that New York judges incarcerated—and whose actual post-release
behavior was thus unobservable—would have committed crimes if released. 151
Given the extremely high rate at which judges incorrectly released high-risk
defendants, it seems extraordinarily unlikely that their error rate incarcerating
people could have been anywhere near zero. Thus, the optimistic scenario is
much more likely than the pessimistic one, and even the pessimistic one would
constitute remarkable abolition.
Pretrial detention is, of course, only half the story of incarceration. Or
more precisely, it is a bit less than a quarter of the story. In the United States,
about 400,000 people are currently jailed awaiting trial. But 1.9 million in total

147. Id. at 238.
148. See Wendy Sawyer & Peter Wagner, Mass Incarceration: The Whole Pie 2024, PRISON
POL’Y INITIATIVE (Mar. 14, 2024), https://www.prisonpolicy.org/reports/pie2024.html
[perma.cc/4GN3-TUBX].
149. Kleinberg et al., supra note 132, at 241.
150. Id.
151. Id.

March 2025]

Abolition by Algorithm

823

are incarcerated. 152 The difference—about 1.5 million people—are imprisoned
because they were convicted of a crime.
How could an Algorithmic Abolitionist approach transform post-conviction incarceration? The approach here is roughly the same. As with pre-conviction incarceration, post-conviction imprisonment would be eliminated to
the maximum extent possible without causing crime—and especially serious
crime—to increase.
Evidence suggests that, as with pretrial incarceration, algorithms could be
used to abolish large proportions of post-conviction imprisonment. In an article in the Journal of Quantitative Criminology, Hannah S. Laqueur and Ryan
W. Copus report the performance of a Super Learner ensemble algorithm
trained to make parole decisions. 153 Their approach to simulating the algorithm’s ability to outperform judges was broadly similar to that of Kleinberg
et al. 154 Their data likewise comes from New York state. 155
Their results are even more striking: The public officials currently tasked
with deciding incarceration are, once again, extremely bad at it, at least if the
goal is minimizing crime. The crime-risk distribution—including violent
crime—of the people New York parole boards release is very similar to those
they send back to prison. 156 That is the result one would expect if parole decisions were made by coin flip. Thus, many people with a high probability of
committing violent crimes are being released; 157 many more with almost no
risk of harming anyone are being locked up. 158
How much imprisonment could be eliminated under an Algorithmic
Abolitionist regime? In the period observed, New York parole boards granted
parole to just 20% of people eligible for it. 159 They thus denied 80% of petitions.
Algorithmic decision-making would have inverted those numbers. That is, the
algorithm could have released 80% of people up for parole—again, with no
increase in crime. 160 On net, then, algorithms would have increased release
among parole-eligible individuals by 60% without any tradeoff in serious
crime.

152. Sawyer & Wagner, supra note 148.
153. Laqueur & Copus, supra note 18.
154. The main differences in the simulation designs lie in their identification strategies for
checking algorithmic performance against the unobserved outcome of true crime risk for those
denied release. See Kleinberg, supra note 132, at 239; Laqueur & Copus, supra note 18, at 151.
Laqueur and Copus exploit variation in parole rehearings and exogenous prisoner releases.
Laqueur & Copus, supra note 18, at 154–55. Both studies find the effect of unobserved outcomes
minimal. Kleinberg, supra note 132, at 270; Laqueur & Copus, supra note 18, at 166.
155. Laqueur & Copus, supra note 18, at 151.
156. Id. at 164 fig.4.
157. Id.
158. Id.
159. Id. at 159.
160. Id. at 170. Laqueur and Copus train their algorithm to predict violent crime. Id. at 155.
This is both because violent crime is more important than nonviolent crime and because higherquality data on violent crime results in the most accurate crime prediction. See id. at 155–56.

824

Michigan Law Review

[Vol. 123:799

As with Kleinberg et al., Laqueur and Copus also report a highly conservative worst-case scenario. Even assuming that unobserved crimes for unreleased defendants would have been twice as high as estimated, the Laqueur–
Copus algorithm could still release about 50% of defendants. 161 This would
have more than doubled the number parole boards freed. 162
Parole-eligible individuals, of course, constitute only a subset of the total
imprisoned population. Most criminal defendants must serve a substantial period of incarceration—often years—before they first become eligible for parole. 163 Thus, an Algorithmic Abolitionist policy that implemented the
Laqueur–Copus algorithm only for parole eligible defendants, and only on the
current parole eligibility schedule, would reduce incarceration. But it would
fall short of reducing total incarceration by 60 or 80%. Many people would
languish in prison while they awaited their first chance to be released by the
algorithm.
Better, then, to institute Algorithmic Abolitionist sentencing from the getgo. Rather than waiting for months or years, an optimal Algorithmic Abolitionist policy would release low-risk offenders as soon as possible—immediately following conviction.
If a Laqueur-Copus style algorithm performed similarly at sentencing as
it does for parole, the abolitionist effect would be impressive. Incarceration
would be reduced by a full 80% as everyone deemed low risk by the algorithm
was immediately released.164 But is such comparable performance at sentencing likely? At this stage, lacking direct empirical evidence on the question, it is
hard to say for certain.
But here are some arguments, based on what we do know, suggesting that
Algorithmic Abolitionism at sentencing might look similar to Algorithmic
Abolitionism at parole. Recall first that incarceration has a criminogenic effect,
which, as sentences lengthen, can outpace its initial crime-reducing effect. 165
Shifting algorithmic release from parole to the moment of sentencing avoids
years of potential criminogenesis. This means that average crime risk among
those algorithmically assessed at sentencing would be lower than those assessed by Laqueur and Copus at parole. The result would be an even greater
expected rate of release than Laqueur and Copus report.
Some may object that this is flawed reasoning. True, shifting algorithmic
release from the moment of parole to the moment of conviction does avoid
prison’s criminogenic effects for the released individuals. But it also eliminates
161.
162.
163.

Id. at 170–72.
Id.
People’s Campaign for Parole Just., Key Facts on Parole Justice in New York, JUST.
ROADMAP,
https://justiceroadmapny.org/wp-content/uploads/2021/12/PCPJKeyFactsDetailed1.pdf [perma.cc/7P9K-S43V].
164. The reduction in incarceration here is 80%, rather than the 60% reported for parole,
because parole boards were already releasing 20% of eligible incarcerated persons. But at initial
sentencing, those 20% would otherwise be sent to jail, increasing the algorithm’s net effect as
compared with the status quo.
165. See supra note 116 and accompanying text.

March 2025]

Abolition by Algorithm

825

prison’s crime-reducing effects for those individuals—especially those strongest effects at the beginning of the sentence. 166 Thus, one might argue, the shift
in timing would increase average crime risk in the target population and therefore reduce the rate of release.
This is not quite right. Not everyone has the same risk of committing future crimes. And the Algorithmic Abolitionist sentencing algorithm would release only those individuals it judged to have little or no risk of committing
future crimes. Incarceration, by and large, could not possibly reduce those individuals’ risk of committing future crimes. Most would have no risk to reduce.
Thus, for them, incarceration would be purely criminogenic, and the abovedescribed argument for the shift to release at sentencing holds.
Indeed, algorithms could reap a double-bonus from heterogeneity. Even
among individuals with nontrivial crime risk, incarceration’s crime-reducing
effect may be highly heterogenous. 167 Strong specific deterrent effects from incarceration might either be correlated with high crime risk or otherwise predictable by algorithms. If so, a sentencing algorithm like Laqueur and Copus’s
could release even more people without increasing crime. It would accomplish
this by focusing incarceration on those for whom it would have an unusually
large crime-reducing effect. All of these factors suggest that a Laqueur-Copus
style algorithm, applied to sentencing, could enable release rates similar to the
80% it would release at parole—and perhaps more.
There are, however, other countervailing factors worth considering. Not
all incarcerated persons in New York are eligible for parole. 168 The population
on which the Laqueur-Copus algorithm was evaluated might therefore be fundamentally different from the full incarcerated population. But because New
York only instituted determinate sentencing in the late 1990s and 2000s, many
non-parole-eligible incarcerated persons in fact committed the exact same
crimes as parole eligible ones. 169 And even after the change, a full 40% of New
York state prisoners are serving parole-eligible sentences. 170 This shift in sentencing law also suggests that parole-eligible incarcerated persons in New
York might be older on average than non-parole-eligible ones. The crime-reducing effects of age are well documented. 171 On the other hand, the same legal
shifts suggest that people eligible for parole have been incarcerated substantially longer than those not eligible. Thus, the crime-reducing effects of ageing
are countervailed to at least some extent by the above-discussed criminogenic
effects of long sentences. The best way to see how all of these effects net out in

166. See supra notes 113–115 and accompanying text.
167. See Rose & Shem-Tov, supra note 113, at 3304.
168. See, e.g., N.Y. PENAL LAW § 70.02(2)(a) (McKinney 2009) (covering class B and C violent felonies).
169. N.Y. STATE PERMANENT COMM’N ON SENT’G, A PROPOSAL FOR “FULLY
DETERMINATE” SENTENCING FOR NEW YORK STATE 3–4 (2014).
170. People’s Campaign for Parole Just., supra note 163.
171. Steven D. Levitt, The Limited Role of Changing Age Structure in Explaining Aggregate
Crime Rates, 37 CRIMINOLOGY 581, 583 (1999).

826

Michigan Law Review

[Vol. 123:799

Algorithmic Abolitionist sentencing is to try it. Even a small-scale experiment
would be highly informative.
Here is another important question about Algorithmic Abolitionist sentencing: What effect would it have on general, as opposed to specific, deterrence? Under the incarceration policies contemplated here, large proportions
of people convicted of crimes would never see jail time. Even if algorithmic
precision in the allocation of incarceration kept crime from rising among the
convicted, what about everyone else? As discussed above, incarceration appears to have an important general deterrent effect that goes well beyond those
individuals actually caught and sentenced. 172 The literature thus shows that, if
incarceration is indiscriminately reduced, its deterrent effect is likewise reduced, and crime increases. 173 Would the huge reductions in total punishment
wrought by Algorithmic Abolitionism, thus, massively reduce general deterrence and increase crime?
Not necessarily. Algorithmic Abolitionism is not like indiscriminate abolitionism. While it does reduce incarceration dramatically, it does not do so
uniformly. The reductions come from releasing the large share of low-risk defendants who, under the status quo, are imprisoned. But the status quo also
frees many among the comparatively small set of individuals who will predictably commit further crimes. Under Algorithmic Abolitionism, they would be
incarcerated. Thus, for this latter group, the switch to Algorithmic Abolitionist
policy increases, rather than decreases expected punishment. Moreover, individuals performing a reflective cost-benefit analysis of their potential crimes
seem much more likely to fall into the latter category than the former. If this
is right, and potential defendants realize it, then Algorithmic Abolitionism
would, at a first cut, increase, not decrease general deterrence.
What about in equilibrium? Consider the rational potential crime committer at the margin. Suppose the relevant algorithm would score him as low
risk, and he knows this. Such knowledge, it should be noted, could be quite
hard to obtain, given the “black box” nature of many machine-learning algorithms. 174 But if the marginal individual could predict his low risk score, this
would decrease the punishment he expected from crime. Then, if rational and
inclined to crime, he would commit more crimes.
But we are not yet in equilibrium. Algorithms need not be static. If the
initial version of an algorithm induced some marginal individuals to commit
more crimes, some of them would be caught. Then, their data could be used
to further train the algorithm, such that similar marginal individuals would no
longer be scored low risk. If they knew this, they would then expect more punishment and revert to a lower level of crime commission. This would then produce more data on which to update the algorithm. And so on until an
equilibrium was reached. Formal microeconomic models of the expected

172. See supra notes 108–112 and accompanying text.
173. See supra notes 108–112 and accompanying text.
174. See Jenna Burrell, How the Machine ‘Thinks’: Understanding Opacity in Machine
Learning Algorithms, BIG DATA & SOC’Y, Jan.–June 2016, at 1, 4–9.

March 2025]

Abolition by Algorithm

827

equilibria for various Algorithmic Abolitionist policies would be useful, but
they are beyond the scope of this Article.
Here is one more factor favoring the idea that Algorithmic Abolitionism
would maintain, rather than reduce, general deterrence. Some evidence suggests that dedicated crime-committers overestimate new technology’s ability
to single them out for increased punishment. For example, economists of
crime have found that the general deterrent effect of DNA databases is larger
than pure rational-actor models would predict. 175 Potential offenders may believe that DNA technology is even better at solving crimes than it really is. The
same effect could hold for committed bad actors’ estimate of algorithms’ ability to single them out.
Algorithmic Abolition could also maintain general deterrence by shifting
criminal policy toward detection, rather than punishment. Robust criminological evidence shows that increasing the certainty of apprehension for a
crime is a much stronger deterrent than increasing the severity of punishment. 176 Thus, if Algorithmic Abolitionism’s large reductions in incarceration
tended to increase crime, this could be offset by modest increases in apprehension. Such increases in apprehension rates could be achieved using the Algorithmic Abolitionist policing policies described below. 177 And because—as
also described below—Algorithmic Abolitionism can, as a baseline, eliminate
such huge shares of policing, modest deviations from that baseline would
blunt the overall abolitionist effect only moderately.
B. Police
The previous Section described Algorithmic Abolitionism’s potential as
applied to incarceration. This Section turns to policing. It estimates the potential effect of Algorithmic Abolitionist policies for three major police functions:
traffic enforcement, street stops, and patrols. These functions are selected for
two reasons. First, they constitute the vast majority of the public’s unwanted
interactions with the police and, thus, the majority of potential harm from disruptive and violent policing. 178 In 2015, 10.8% of Americans over age sixteen
reported having an interaction with the police that they did not request. 179
8.6% reported that the type of unsolicited interaction was a traffic stop where
they were the driver, and another 2.4% reported a traffic stop where they were
the passenger. A full 1% of Americans reported being stopped by the police on

175. Anne Sofie Tegner Anker, Jennifer L. Doleac & Rasmus Landersø, The Effects of DNA
Databases on the Deterrence and Detection of Offenders, 13 AM. ECON. J. 194, 196 (2021).
176. See generally Daniel S. Nagin, 23 Deterrent Effects of the Certainty and Severity of Punishment in DETERRENCE, CHOICE, AND CRIME: CONTEMPORARY PERSPECTIVES 157 (Daniel S.
Nagin, Francis T. Cullen & Cheryl Lero Jonson eds., 2018) (collecting evidence).
177. See infra Section II.B.
178. See ELIZABETH DAVIS, ANTHONY WHYDE & LYNN LANGTON, U.S. DEP’T OF JUST.,
CONTACTS BETWEEN THE POLICE AND PUBLIC, 2015, at 1 fig.1, 16 tbl.18 (2018).
179. Id. at 1 fig.1.

828

Michigan Law Review

[Vol. 123:799

the street. 180 These interactions arose from police patrols, not, for example,
from the execution of preexisting warrants. 181 By contrast, just 1.1% of Americans reported any other type of unwanted police interaction. 182 That comprises arrests—including those with a warrant—that did not start with traffic
or street stops. 183 The second reason for focusing on these police functions is
that, as with incarceration, algorithms already exist that can allocate them
much more efficiently than humans. Significant abolition is thus possible using existing technology.
Begin with street stops. Algorithmic Abolitionist policies could, plausibly,
eliminate the vast majority of them. In 2016, Sharad Goel, Justin M. Rao, and
Ravi Shroff developed an algorithm, trained on data from real New York street
stops, to identify individuals likely to be carrying illegal weapons. 184 As with
other crime prediction tasks, human assessments here are extremely inaccurate. In New York, between 2011-12, 43% of stops made by police had less than
1% probability of revealing an illegal weapon. 185
Thus, as with other risk estimation tasks, superior algorithmic performance could enable significant amounts of abolition. Within the set of actually
made New York stops, the Goel et al. algorithm identified a subset of just 6%
stops from which the majority of weapons could have been predictably recovered. 186 This suggests that, if applied population-wide—to both those people
whom the New York police actually stopped, and those who it did not—an
algorithm-based policy might have reduced stops by 88% while recovering the
same number of weapons. 187 At a bare minimum, the Goel et al. results suggest
180. Id. Note that subcategories do not necessarily sum to higher-level categories since
some individuals reported multiple police interactions.
181. Id.
182. Id.
183. Id.
184. Goel, Rao & Shroff, supra note 69.
185. Id. at 387.
186. Id. at 382.
187. Id. at 371–74. This figure assumes that there were a similar number of algorithmically
identifiable high-risk individuals among those not searched by NYPD as among those who were
searched by them. That assumption would be false if either (1) police officers were substantially
better than random at estimating risk when determining who to stop (2) they had thus already
stopped a very large share of the New Yorkers whom the algorithm would rate as similarly high
risk to the riskiest 6% of New Yorkers actually stopped. But as to (1), the data from actually
executed stops suggests that police are not particularly good estimating risk. More likely, like
judges, their decisions are closer to random, with respect to risk. As for (2), only 1% of the general
population are stopped by police in a given year, suggesting that many individuals whom the
algorithm would score high-risk were not stopped. DAVIS, WHYDE & LANGDON, supra note 178,
at 1. Thus, the operative assumptions seem plausible. Assume conservatively, however, that outof-sample weapons turned out to be twice as hard to find as in-sample. That is, assume that the
6% of non-stopped New Yorkers whom the algorithm rated as riskiest turned out to possess only
half as many weapons as the 6% of stopped New Yorkers whom the algorithm rated as riskiest.
This would still imply the possibility of abolishing 82% of stops, since the police would have to
stop twice as many people from the non-stopped pool than from the stopped pool to achieve
status-quo recovery. If out-of-sample detection were three times as hard, the figure is 76%.

March 2025]

Abolition by Algorithm

829

that roughly 42% of stops could be abolished without meaningfully reducing
weapons recovery. 188 Even better, implementing this Algorithmic Abolitionist
policy would not require officers to fire up a computer application before making every stop-and-frisk decision. Instead, the Goel et al. algorithm reveals a
set of simple observational heuristics that nearly replicate its performance and
can be easily deployed in the field. 189
Algorithmic Abolitionist policymaking could reduce traffic stops even
more. Much of this abolition could be accomplished without advanced algorithms. According to a recent nationwide survey of police, speeding is by far
the most common reason for traffic stops. 190 Many jurisdictions already employ speed cameras in certain locations that automatically detect speeding and
send citations to the car’s registered owner. 191 The Algorithmic Abolitionist
version of this existing policy is to implement speed cameras broadly enough
that human enforcement is no longer necessary—and then to ban it. This
might sound expensive. But, on the contrary, robotic traffic enforcers are
much cheaper than human ones. 192
The automation of other traffic enforcement functions would require algorithmic technology, but nothing novel. The next most common reason reported by police for stopping vehicles is equipment violations. 193 Algorithms
are already highly effective at correctly identifying the content of images of all
kinds, 194 and they could be fine-tuned to identify the whole range of visually
identifiable automotive equipment violations presently detectible by human
police. Examples—including an algorithm that detects illegal window tints—

188. Goel, Rao & Shroff, supra note 69, at 367. The paper reports that the New York police
could have conducted 58% of their actually conducted stops while still recovering 90% of weapons. This implies a straightforward 42% reduction in stops without making any assumptions
about the large pool of New Yorkers who were not actually stopped. That approach would have
reduced contraband recovery by 10%. But it is fairly conservative to estimate that, by applying
the algorithm to both actually stopped and non-stopped New Yorkers, the 42% reduction could
have been achieved with a 0% reduction in recovery. To achieve this, the algorithm would need
to improve police efficiency in determining whom to stop by only a modest 11% (1/0.9). Id.
189. See id. at 383–87.
190. Nancy Perry, Police Research: 1,000 Cops Address Non-Compliance During Traffic
Stops, POLICE1 (June 29, 2021, 2:14 PM), https://www.police1.com/traffic-patrol/articles/police-research-1000-cops-address-non-compliance-during-traffic-stopsC3mPToqhCR2O4Dxu/#form-success-message [perma.cc/GWC3-B6YX].
191. E.g., Automated Speed Enforcement Frequently Asked Questions, CITY OF CHI.,
https://www.chicago.gov/city/en/depts/cdot/supp_info/children_s_safetyzoneporgramautomaticspeedenforcement/automated_speed_enforcementfrequentlyaskedquestions.html
[perma.cc/TBT5-HVH9].
192. See generally Shukai Li, Boshen Jiao, Zafar Zafari & Peter Muennig, Optimising the
Cost-Effectiveness of Speed Limit Enforcement Cameras, 25 INJ. PREVENTION 273 (2019).
193. Perry, supra note 190.
194. See generally, e.g., Maxime Vidal et al., Perspectives on Individual Animal Identification
from Biology and Computer Vision, 61 INTEGRATED & COMPAR. BIOLOGY 900 (2021) (describing
algorithms that identify individual animals).

830

Michigan Law Review

[Vol. 123:799

already exist. 195 Other enforcement actions currently carried out via live police
stops could be automated, too. Various algorithmic approaches already exist
for detecting moving violations, including dangerous and impaired driving. 196
Indeed, if anything, algorithmic traffic enforcement might threaten to replace more than 100% of current traffic stops. Automated systems, after all,
would detect all violations in their vicinity, not, as under the status quo, just
those that occur in sight of a police officer. Likewise, automated systems might
enforce violations strictly—citing everyone driving over the speed limit, rather
than just those driving, say, more than ten-ish miles per hour over it. Insofar
as this is a problem, solutions are available: Even if automated systems could
cite many more traffic offenders than under the status quo, they need not. No
rule of law requires that all detected violations result in a citation; even police
often give warnings. With automated systems, enforcement could be set at desired levels in any number of ways. Systems might issue warnings to occasional
violators, with citations accruing only to repeat offenders. Systems could be
turned on and off at random, mimicking the presence or lack of enforcing officers at different times of day. Or they could be left on at all times, with the
decision to cite or not determined probabilistically, to similar effect. All of
these would likely be fairer than the status quo, wherein non-random, albeit
inconsistent, enforcement affects racial and socioeconomic groups differentially.
What about policies that would not merely reduce unnecessary police
stops, but eliminate unnecessary police presence entirely? How much Algorithmic Abolitionism could be possible for police patrols, broadly construed?
There are two potential crime-controlling effects of patrols. The first is general
deterrence. Empirical evidence shows that mere police presence—even with
no citizen interactions—in areas that would otherwise experience crime has a
significant deterrent effect. 197 Such presence reduces crime on net; it is not
merely displaced to other geographic areas. 198 Patrols’ second crime-controlling effect is the incapacitation that results when police avert a crime in progress. For both effects, physical police presence in a given area has value only
insofar as that area would otherwise experience high crime risk. In areas where
crime is unlikely to occur, the disruptions, intimidation, and violence police
encounters can cause constitute needless harm.

195. See generally Ganesan Kaliyaperumal, IoT-Enabled Vision System for Detection of Tint
Level, in INTERNET OF THINGS 1 (B.K. Tripathy & J. Anuradha eds., 2017).
196. See generally, e.g., ZhenLong Li, HaoXin Wang, YaoWei Zhang & XiaoHua Zhao, Random Forest-Based Feature Selection and Detection Method for Drunk Driving Recognition, INT’L
J. DISTRIBUTED SENSOR NETWORKS, Feb. 2020, at 1; Jair Ferreira Júnior et al., Driver Behavior
Profiling: An Investigation with Different Smartphone Sensors and Machine Learning, PLOS ONE
(Apr. 10, 2017), https://doi.org/10.1371/journal.pone.0174959.
197. See generally Rob. T. Guerette & Kate J. Bowers, Assessing the Extent of Crime Displacement and Diffusion of Benefits: A Review of Situational Crime Prevention Evaluations, 47
CRIMINOLOGY 1331 (2009) (reviewing the evidence).
198. See id. (showing that displacement occurs in only a small percentage of cases, and
where it does occur the net effect is still crime reduction).

March 2025]

Abolition by Algorithm

831

As with individual crime risk, humans are bad at predicting spatio-temporal crime risk. An Algorithmic Abolitionist approach can do better, directing
police patrols to only that subset of places and times where they are truly
needed. The approach here is the same as with Algorithmic Abolitionist incarceration policies: Begin with the lowest-risk places and eliminate police patrols up to the point at which crime would begin to rise.
How good are algorithms at predicting when and where crime will occur?
In a 2015 randomized trial, researchers pitted an adapted earthquake prediction algorithm against the top human crime forecasters in the Los Angeles, CA
and Kent, England police departments. 199 Even when compared with human
forecasters using hotspot data and qualitative criminal intelligence, the algorithm did about twice as well. 200 Other, newer, and more complex, machinelearning models might do even better. A deep neural network published in
2017 was trained to predict incidents of 31 types of crime in Chicago down to
a spatial resolution of just a few feet. 201 It achieved almost 85% accuracy. 202
How much abolition of police patrols can be achieved using modern machine learning? It is difficult to say with the same precision as was possible for
Algorithmic Abolitionist incarceration policies. Unlike with incarceration, no
available empirical evaluations specifically simulate the minimum amount of
police patrols necessary to maintain status-quo crime rates. Nevertheless,
plausible estimates of patrol reduction can be extrapolated from related empirical findings. These estimates are, however, necessarily more speculative
than those based on studies attempting to measure algorithms’ abolitionist
potential directly.
Algorithms’ potential for abolishing police patrols depends on the status
quo distribution of policing: What percent of a given city’s neighborhoods are
patrolled on a given day? And what percent of crimes are captured by those
patrols? The more algorithms can successfully predict the same number of
crimes in a more limited geographic—or temporal—range, the more abolition
is possible.
In the randomized trial in Los Angeles and Kent, the algorithm was about
twice as good as the best human forecasters at identifying hotspots with unusually high levels of crime. It could capture twice as many crimes using
hotspots covering the same percentage of the city. 203 This finding—that algorithms are roughly twice as good as humans at predicting geographic crime

199. See generally Mohler et al., supra note 21.
200. Id. at 1404.
201. See Hyeon-Woo Kang & Hang-Bong Kang, Prediction of Crime Occurrence from
Multi-Modal Data Using Deep Learning, PLOS ONE (Apr. 24, 2017), https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0176244&type=printable
[perma.cc/GNM7-SNF3].
202. Id. at 14 (area under curve = .8333).
203. Mohler et al., supra note 21, at 1405 tbl.2.

832

Michigan Law Review

[Vol. 123:799

risk—is consistent with recent findings from Chicago. 204 Using that estimate,
then, one could design an Algorithmic Abolitionist policy expected to eliminate 50% of risk-targeted police patrols while maintaining the status quo deterrent effect. A simple version would be to dispatch patrols randomly to half
of the geographies the algorithm selected.
This estimate of a 50% reduction in police patrols is not the maximum. It
focuses just on the number of patrols that could be eliminated which would
otherwise have been deployed to high risk hotspots. However, in many urban
neighborhoods, police presence is not primarily allocated on the basis of
risk. 205 Substantially more abolition should therefore be possible when one includes the many geographies where police are not currently trying to patrol
according to risk-based need.
To get a rough of the total abolitionist potential, however, further speculative assumptions are necessary. Suppose optimistically that, under the status
quo, police patrols in the average city are present in the immediate vicinity of
30% of crimes when they happen. And suppose that to do this, police are daily
deployed to neighborhoods covering 60% of the city’s geography. Studies using data from Baton Rouge and Chicago suggest that algorithmically directed
patrols could achieve the same crime coverage while deploying to only about
5% and 10% of the city, respectively. 206 An Algorithmic Abolitionist policy using these algorithms could—under these assumptions—eliminate between
83% and 92% of a given city’s police patrols with no increase in crime.
C. How to Design an Algorithmic Abolitionist Policy
The idea that algorithms might inform the administration of criminal justice is not novel. Many jurisdictions already use at least some algorithms resembling those described above. 207 Pretrial incarceration is a common
application. Over 60% of the U.S. population now lives in a jurisdiction that

204. That implementation suffered from significant uptake problems. Some districts were
“simply not following the playbook” and “ignoring the [algorithm’s] recommendations.” Max
Kapustin, Terrence Neumann & Jens Ludwig, Policing and Management 38 (Nat’l Bureau of
Econ. Rsch., Working Paper No. 29851, 2022), https://www.nber.org/papers/w29851
[perma.cc/5FHZ-Q9WA]. However, in the district and during the period where they were paid
the most heed, algorithmic predictions helped to “reduce[] the rate of shooting victimization by
62%.” Id. at 29. These reductions were roughly twice as large as the average reduction amongst
the districts. Id. at 56–57 tabls.4 & 5.
205. See, e.g., id. at 18 (mapping the neighborhoods where Chicago implemented its riskoriented Strategic Decision Support Centers).
206. Yujie Hu, Fahui Weng, Cecile Guin & Haojie Zhu, A Spatio-Temporal Kernel Density
Estimation Framework for Predictive Crime Hotspot Mapping and Evaluation, APPLIED
GEOGRAPHY, OCT. 2018, at 89, 95; MOHAMMAD AL BONI & MATTHEW S. GERBER, PREDICTING
CRIME WITH ROUTINE ACTIVITY PATTERNS INFERRED FROM SOCIAL MEDIA 1236 (2016).
207. Carolene Haskins, Dozens of Cities Have Secretly Experimented with Predictive Policing Software, VICE (Feb. 6, 2019), https://www.vice.com/en/article/dozens-of-cities-have-secretly-experimented-with-predictive-policing-software [perma.cc/6QEG-8YD5].

March 2025]

Abolition by Algorithm

833

uses some kind of risk assessment tool in the pretrial incarceration process. 208
Yet despite this, the dramatic abolitionist results described above have not
emerged anywhere. Why not?
The answer is that no existing algorithmic policy can rightly be called Algorithmic Abolitionism. Each suffers from at least one of three important
flaws. Each flaw is straightforwardly remediable. This Section describes these
common failures and, based on them, articulates a set of principles for designing Algorithmic Abolitionist policies.
The first widespread problem is that no existing algorithmic criminal justice policy is abolitionist. Put simply, none are designed around the core Algorithmic Abolitionist goal: reducing as much prison and policing as possible
without increasing crime. Consider Virginia, a rare state that adopted risk
scores for sentencing with the explicit goal of reducing incarceration—rather
than, for example, reducing crime. 209 Yet even in this most propitious of circumstances, the legislature set a goal of reducing imprisonment by just 25%. 210
This is a substantial figure, and a laudable goal, but it falls far short of the abolitionist frontier.
Here, then, is the first lesson: Algorithms will not achieve dramatic abolition by accident. Polices must be built for that purpose from the ground up.
The details of policy design—the cut score at which a prisoner is released, the
risk score at which a neighborhood is patrolled—determine the results. For
Algorithmic Abolitionism to be achieved, these must be calibrated for maximal
elimination, rather than around lesser goals.
The second widespread defect is likewise one of policy design. Virginia’s
algorithmic sentencing law set a goal of reducing incarceration by 25%. 211 But
it did not achieve even that. Indeed, a recent analysis shows that the policy
generated “no net change in the incarceration rate or length of sentence[s].” 212
The same was true in Kentucky following its adoption of risk scoring for pretrial detention. As with Virginia, despite an explicit legislative goal of lowering
incarceration, the policy “led to only a trivial increase in pretrial release.” 213
The problem was not with the algorithms. Rather, it was that even in these
facially algorithmic policies, algorithms were given very little role to play. In
both states, judges were allowed to simply ignore algorithmic recommendations. In Virginia, for example, judges were shown both a given defendant’s
risk score and an indication of whether it was low enough for the algorithm to

208.

VALID.

MAPPING PRETRIAL INJUSTICE, supra note 22.ERROR! HYPERLINK REFERENCE NOT

209. See Megan T. Stevenson & Jennifer L. Doleac, Algorithmic Risk Assessment in the
Hands of Humans at 7 (Apr. 21, 2021), https://ssrn.com/abstract=3489440 [perma.cc/WSU8R47U] (prepublication manuscript).
210. Id.
211. Id.
212. Id. at 19.
213. Megan Stevenson, Assessing Risk Assessment in Action, 103 MINN. L. REV. 303, 308
(2018).

834

Michigan Law Review

[Vol. 123:799

recommend release. 214 But judges could decline to follow the algorithmic recommendation without consequence. 215 And decline they did. Judges either ignored algorithmic risk-based recommendations entirely or deviated from
them so as to increase incarceration. 216
Thus, the second lesson for designing Algorithmic Abolitionist policies:
Algorithmic decisions must have bite. What this means may vary by context.
In the context of police patrolling, for example, algorithmic direction of patrol
patterns should be mandatory just like patrol orders given by ranking human
officers. In the domain of sentencing, there are various options for giving algorithmic determinations bite.
Here are three possibilities, ordered from least bite to most. First, judicial
deviations from algorithmic sentencing decisions could be made costly. In federal criminal cases, for example, judges who deviate from the U.S. Sentencing
Guidelines range must explain why in writing—and do so on penalty of reversal. 217 This approach appears to be relatively effective at disincentivizing deviation. Even after United States v. Booker 218 made Guidelines recommendations
discretionary—constrained only by the written explanation requirement—deviations did not rise much. 219 Judges who wished to depart from algorithmic
sentencing determinations could likewise be required to bear the burden of
producing a written explanation.
Second, a prediction requirement could be added to the written explanation requirement. If judges believe they are better at estimating who will and
will not commit crimes than machine-learning algorithms, they could be
forced to put their money where their mouths are, supplying their own probabilities. Then, their aggregate accuracy could—as with algorithms—be assessed against real-world results. The judges could be either praised for their
superior wisdom or held accountable for their hubris.
Finally, algorithmic determinations could be the final word—not subject
to judicial override for any reason. For optimal results, courts should only impose this approach after public experiences with the more flexible approach
convince citizens that judicial discretion, on net, does more harm than good.
This policy design, of course, raises serious concerns about errors—the harmless defendant whom the machine sentences to years of imprisonment. But

214. Stevenson & Doleac, supra note 209, at 7–8.
215. Id. at 7–9. Only if a judge imposed a sentence outside the sentencing guidelines range
were they required to produce a written justification.
216. Stevenson & Doleac, supra note 209, at 20–22; Stevenson, supra note 213, at 369–71.
217. Federal Sentencing Guidelines, CORNELL L. SCH. LEGAL INFO. INST.,
https://www.law.cornell.edu/wex/federal_sentencing_guidelines [perma.cc/7FCU-UFCQ].
218. United States v. Booker, 543 U.S. 220 (2005).
219. U.S. SENT’G COMM’N, FEDERAL SENTENCING: THE BASICS 7 (2020),
https://www.ussc.gov/sites/default/files/pdf/research-and-publications/research-publications/2020/202009_fed-sentencing-basics.pdf [perma.cc/5T3A-VNK8].

March 2025]

Abolition by Algorithm

835

such errors are also rampant under the current system. 220 And as just described, allowing humans to override algorithms increases, not reduces,
them. 221 Thus, at some point it may be worth considering whether keeping
humans in the loop actually serves humanity.
Returning to algorithmic policy design, the final widespread flaw—or at
least potential flaw—in existing policies is technical. Where algorithms are already used in criminal enforcement, they are rarely the best available algorithms. As mentioned above, the COMPAS tool, for example, is now almost a
decade and a half old. 222 Yet it is the primary algorithm used for pretrial risk
assessment in at least eleven counties with a combined population of over 4.3
million people. 223 As already discussed, in recent years, algorithmic capabilities have exploded across essentially every application. Most of the high-performing algorithms described herein use techniques popularized during that
period. 224 If older, widely used algorithms cannot predict crime risk with the
same accuracy as these newer ones, then they cannot be used to abolish as
much policing or prison.
Hence, the final lesson for designing Algorithmic Abolitionist policy: Use
the best available technology, with a plan to update as technology improves.
Note that this maxim will not inevitably imply discarding more traditional statistical models in favor of newfangled machine-learning approaches. For some
questions—and some datasets—traditional approaches work as well as the
newer ones. 225 The point, however, is to test. Older algorithms should be pitted
against new approaches, and the best performer should be adopted into public
use. Great feats of abolition can now be achieved using modern techniques.
There is no reason for policymakers to settle for less.
Existing experiments in algorithmically driven policing, as opposed to incarceration, have likewise, not dramatically reduced policing. But the reasons
are now familiar. First, and most importantly, reducing policing was not these
policies’ aim. Algorithmic policing experiments have instead generally sought
to reduce crime. 226 On this metric, algorithmic policing has perhaps seen more
success than algorithmic sentencing. Two recent empirical evaluations of Chicago’s predictive policing program—from RAND and the University of Chicago Crime Lab—show that it did meaningfully reduce crime. 227 But those
220. Yang, supra note 71, at 77.
221. Stevenson & Doleac, supra note 209, at 22.
222. THOMAS BLOMBERG ET AL., supra note 123.
223. MAPPING PRETRIAL INJUSTICE, supra note 22.
224. See, e.g., Laqueur & Copus, supra note 18, at 156; Kleinberg et al., supra note 132, at
239; Goel, Rao & Shroff, supra note 69, at 391.
225. See Stevenson & Doleac, supra note 209, at 7–8, 11 (finding no difference in performance between a logistic regression and a random forest model for predicting recidivism in Virginia).
226. See, e.g., JOHN S. HOLLYWOOD, KENNETH N. MCKAY, DULANI WOODS & DENIS
AGNIEL, REAL-TIME CRIME CENTERS IN CHICAGO: EVALUATION OF THE CHICAGO POLICE
DEPARTMENT’S STRATEGIC DECISION SUPPORT CENTERS, at xi (2019).
227. Id. at 50–52; Kapustin, Neumann & Ludwig, supra note 204, at 7–8.

836

Michigan Law Review

[Vol. 123:799

evaluations also show that actual crime reduction fell far short of the algorithmic tools’ potential. 228 The primary culprit was again policy design, not algorithms’ predictive power. 229 Algorithmic determinations again lacked bite, so
that many Chicago precincts were simply “not following the playbook” and
“ignoring [the algorithm’s] recommendations.” 230
III. ALGORITHMIC ABOLITIONISM UPENDS THE BIAS DEBATE
Despite algorithms’ considerable abolitionist potential, and despite
prison and police abolitionists’ success in spreading their argument for elimination over reform, both progressives and abolitionists have vigorously opposed the use of algorithms in criminal justice. 231 In the past, they were
perhaps right to do so. Their most common objections—to algorithmic bias
and structural racial inequality—have been genuine concerns. Moreover, until
now, the potential abolitionist upside of algorithms has not been widely understood.
But Algorithmic Abolitionism presents a new normative landscape. Even
if racial-equality objections to previous uses of algorithms in criminal enforcement had merit, they lose their force as applied to Algorithmic Abolitionism.
This is in part because such objections have, as a general matter, weakened as
algorithmic design has improved. But it is also because an Algorithmic Abolitionist approach changes the normative terrain.
To that end, this Part outlines four normative arguments favoring the use
of algorithms, despite longstanding objections based on racial justice. Three
228. See Kapustin, Neumann & Ludwig, supra note 204, at 38 (finding that many districts
were “not following the playbook” by “ignoring the [algorithm’s] recommendations”);
HOLLYWOOD ET AL., supra note 226, at 35 (describing Chicago’s geospatial prediction algorithm
as “not discussed that frequently”).
229. See HOLLYWOOD ET AL., supra note 226, at 17–49; Kapustin, Neumann & Ludwig,
supra note 204, at 33–38.
230. Kapustin, Neumann & Ludwig, supra note 204, at 38; see also Andrew Guthrie Ferguson, Surveillance and the Tyrant Test, 110 GEO. L.J. 205, 220–30 (2021) (providing additional
context on the Chicago program, as well as a critique of a similar program in Los Angeles).
231. See, e.g., Roberts, supra note 2, at 27–29; Akbar, supra note 49, at 1809–11; Kelly Hannah-Moffat & Kelly Struthers Montford, Unpacking Sentencing Algorithms: Risk, Racial Accountability and Data Harms, in PREDICTIVE SENTENCING: NORMATIVE AND EMPIRICAL
PERSPECTIVES 175, 187–90 (Jan W. de Keijser, Julian V. Roberts & Jesper Ryberg eds., 2019);
Malkia Amala Cyril, Black America’s State of Surveillance, PROGRESSIVE MAG. (Mar. 30, 2015,
12:17
PM),
https://progressive.org/magazine/black-america-s-state-surveillance-cyril
[perma.cc/39XM-7AVY]; Will Douglas Heaven, Predictive Policing Algorithms Are Racist. They
Need to Be Dismantled., MIT TECH. REV. (July 17, 2020), https://www.technologyreview.com/2020/07/17/1005396/predictive-policing-algorithms-racist-dismantled-machine-learning-bias-criminal-justice [perma.cc/XTE6-6YNX]; Insha Rahman, Undoing the Bail
Myth: Pretrial Reforms to End Mass Incarceration, 46 FORDHAM URB. L.J. 845, 864–65 (2019);
see also Open Statement, Twenty-Seven Researchers, Technical Flaws of Pretrial Risk Assessments
Raise
Grave
Concerns
(July
17,
2019),
https://dam-prod.media.mit.edu/x/2019/07/16/TechnicalFlawsOfPretrial_ML%20site.pdf [perma.cc/CD23-BSTR]
(open statement signed by twenty-seven researchers opposing the use of pretrial risk scoring
algorithms).

March 2025]

Abolition by Algorithm

837

of them—the latter three—are novel contributions to the literature. The first
argument is comparative. To the extent algorithms are biased, they are much
less so than the best available alternative: human decisionmakers. This point
has been made before, 232 but the Part shows how strong it is as applied to the
state-of-the-art algorithms discussed herein.
The remaining three arguments are new. Algorithmic Abolitionist thinking is necessary to reveal them. The arguments arise when one considers the
racial justice impact of policies that dramatically reduce levels of harmful outcomes—like being policed or incarcerated. Traditional thinking about algorithmic bias, by contrast, has been concerned almost exclusively with ensuring
equal distributions of harm.
The first of these three novel arguments shows, counterintuitively, how
concerns about racial distributions of harm and concerns about total harm
from discrimination diverge. A levels-reducing policy can dramatically reduce
the number of people being discriminated against, while maintaining or even
worsening traditional distributional measures of fairness. To capture this insight, overlooked in existing accounts of algorithmic discrimination, the Part
introduces a new, quantitative metric of algorithmic fairness.
The Part’s second new normative argument is about tradeoffs. It begins
by endorsing the assignment of at least some normative weight to pure distributional, as opposed to absolute, measures of justice. This raises the question
of how to trade distributional benefits against absolute goods—like reducing
harm from discrimination or reducing total incarceration. Pure cost-benefit
analysis, the Part argues, cannot satisfy the progressive critics of algorithms
who prioritize distributional concerns. The Part therefore proposes a new
framework for evaluating such trade-offs—one that stacks the deck in favor of
distributional values. It then shows why the tradeoffs implied by Algorithmic
Abolitionist policies would almost inevitably pass even such a stringent test.
The Part’s third novel normative argument relates to structural inequality.
Structural inequality is sometimes argued to be the cumulative result of bias
over time. But the Part argues that bias is not the sole—or even primary—
driver of structural inequality stemming from criminal enforcement. Rather,
levels are. Thus, the key to breaking cycles of structural inequality is reducing
levels of harm—the main effect of an Algorithmic Abolitionist approach.
A. Comparative Bias
Arguments about racial bias dominate the debate over algorithms’ use in
criminal enforcement.233 But they are also common in broader academic 234

232. See, e.g., Orly Lobel, The Law of AI for Good, 75 FLA. L. REV. 1073, 1083–84 (2023).
233. Id. at 1084.
234. For an archive of dozens of such studies, see Scholarship, FAIRNESS, ACCOUNTABILITY,
& TRANSPARENCY IN MACH. LEARNING, https://www.fatml.org/resources/relevant-scholarship
[perma.cc/PF8K-7ZR8]. For an in-depth academic treatment that refreshingly breaks the standard mold, see generally ORLY LOBEL, THE EQUALITY MACHINE (2022).

838

Michigan Law Review

[Vol. 123:799

and popular 235 debates about algorithms’ many uses. In the context of criminal
enforcement, the dialectic inevitably runs as follows: First, a jurisdiction introduces some algorithmic tool into its criminal justice apparatus, promising
greater efficiencies, improved fairness, and sometimes less policing or incarceration. 236 Following introduction of the tool, high-profile academics or media organizations argue that the tool must not be used, because it is biased—
i.e., that it treats one group (usually white Americans) better than another
group (usually Black Americans). 237 Then the algorithm’s creators rejoin that
their model is, in fact not biased, so long as “bias” is correctly understood. 238
Here, the debate explodes, but it is dominated by second-order arguments,
built atop the initial ones: What is the right understanding of bias? Is it possible, even in theory, to produce an algorithm that would qualify as perfectly
unbiased?
This Section does not seek to relitigate those well-worn disputes. Rather,
it argues that, at least as applied to Algorithmic Abolitionist policies, they miss
what matters most. For any use of algorithms—including Algorithmic Abolitionism—the policy-relevant question is not, “is this algorithm racially just?”
It is instead, “is this algorithm more or less racially just than the alternatives?”
The former, widely debated, question turns out to be a difficult one. The latter
often turns out to be easy.
Determining whether an algorithm is racially biased, full stop, is less tractable than it sounds. There are many dimensions along which algorithms
could be equal or unequal, and the answer thus depends on what one means
by “biased.” Three popular measures of bias cover much of the available conceptual ground. First, there is “predictive parity.” Here, an algorithm is unbiased if a given risk score implies the same set of expected outcomes for
members of different racial groups. 239 That is, if an algorithm labels some individuals, say, “highly likely” to commit a crime, the actual rate of crime commission is the same for the Black subgroup as for the white one. 240
Some argue that predictive parity does not do enough to promote equality. Even when an algorithm has achieved it, different groups may experience

235. See, e.g., Joan Palmiter Bajorek, Voice Recognition Still Has Significant Race and Gender
Biases, HARV. BUS. REV. (May 10, 2019), https://hbr.org/2019/05/voice-recognition-still-has-significant-race-and-gender-biases [perma.cc/BA3N-3VY8]; Emmanuel Martinez & Lauren Kirchner, The Secret Bias Hidden in Mortgage-Approval Algorithms, MARKUP (Aug. 25, 2021, 6:50 PM),
https://themarkup.org/denied/2021/08/25/the-secret-bias-hidden-in-mortgage-approval-algorithms [perma.cc/595D-U7CA].
236. See Angwin et al., supra note 15.
237. See, e.g., id.
238. WILLIAM DIETERICH, CHRISTINA MENDOZA & TIM BRENNAN, COMPAS RISK
SCALES: DEMONSTRATING ACCURACY EQUITY AND PREDICTIVE PARITY (2016).
239. Hellman, supra note 24, at 820–34.
240. As Hellman explains, it is sensible to treat this measure and another measure, dubbed
“equal predictive value,” which incorporates both true positive rate and true negative rates, as
addressing the same normative issues. Id. at 826.

March 2025]

Abolition by Algorithm

839

different kinds of errors at different rates. 241 Different kinds of errors can have
different costs. 242 Incorrectly classifying someone as low risk—and thus releasing them—imposes little cost on the released person.243 Conversely, incorrectly classifying someone as high risk—and thus incarcerating them—is very
costly to them. 244 Thus, some bias-oriented critics of algorithms argue that
fairness means achieving not just predictive parity, but rather “error-rate” parity. Under this theory, an algorithm is unbiased if members of different racial
groups are subjected to costly errors—for example, unnecessary incarceration—at the same rate. 245
These two conceptions of fairness—predictive parity and error-rate parity—are not only different; they are in direct tension. For most populations, it
is mathematically impossible to achieve both simultaneously. The only exception is the exceedingly rare circumstance in which the two populations have
identical underlying distributions of actual crime. 246
Some theorists go further yet, arguing that algorithmic fairness means
equalizing outcomes. Under this conception, an incarceration algorithm is racially unbiased only if it recommends imprisonment at the same rate for all
racial subgroups. 247 Then, the racial composition of the incarcerated population will mirror the racial composition of the total population. This, too, is
almost always impossible to accomplish simultaneously with either of the
other two versions of fairness. 248
Thus, critics are right. Essentially all algorithms are biased, if “biased”
means “unable to achieve parity under all three conceptions.” For essentially
any real-world crime-risk algorithm, the achievement is mathematically impossible. And even if one agreed to evaluate algorithmic fairness using just one
of the conceptions, the dispute over which one mattered most would remain. 249

241. Id. at 834–46.
242. Id.
243. There are of course costs to future crime victims, but those are generally ignored when
evaluating an algorithm’s fairness. Richard A. Berk, Artificial Intelligence, Predictive Policing, and
Risk Assessment for Law Enforcement, 4 ANN. REV. CRIMINOLOGY 209, 225 (2021).
244. See supra Section I.A.
245. Hellman, supra note 24, at 835–39. To understand the difference between this and
predictive parity, consider that, for any two populations with different rates of actual crime, different proportions of the population will be categorized as high risk. This means that despite
equal error rates, conditional on being so categorized, the risks of being incorrectly labeled as
high risk will be unequal. See id. at 839–40.
246. Id. at 823. Hellman’s explanation of why is wonderfully clear. Those interested should
see id. at 820–23.
247. Nima Kordzadeh & Maryam Ghasemaghaei, Algorithmic Bias: Review, Synthesis, and
Future Research Directions, 31 EUROPEAN J. INFO. SYS. 388, 395 (2022).
248. Id. at 396. Technically, an algorithm could achieve predictive parity and public policy
could set different cut points for incarceration for different groups—generating equal outcomes.
But this is a distinction without a difference.
249. Hellman, supra note 24, at 820–46.

840

Michigan Law Review

[Vol. 123:799

But maybe the question of whether an algorithm is biased is the wrong
one. We could instead ask how much bias a given algorithm displayed—and
compared to what? Shifting the inquiry in this way—from absolutist to comparative—causes the impossibilities just described to melt away. Although an
algorithm cannot be perfectly unbiased according to multiple theories simultaneously, it is perfectly possible for one to improve according to multiple theories simultaneously.
And algorithms do improve, a lot, compared with the alternative. In criminal enforcement, that alternative is human decision making. Humans are extraordinarily biased. Algorithms regularly perform much better, no matter
how one conceives of fairness.
Here is why. Consider a straightforward model in which Black defendants
are unjustly incarcerated at higher rates than white defendants. Suppose that
human judges believe that all defendants’ risk of crime is higher than it actually is and incarcerate them according to that (mistaken) assumption. This
produces suboptimally high levels of incarceration, but it does not induce a
racial disparity. However, if the upward skew of human risk assessments is
uniformly even bigger for Black defendants than for white ones, the posited
unjust disparity results. 250
Now consider the effects of an Algorithmic Abolitionist incarceration policy on this model. Suppose the algorithm is, unlike humans, very good at identifying individuals who will commit crimes. Imagine that, among those it
predicts will commit them, 99 percent do—irrespective of racial group. Likewise for its predictions of who will not commit crimes. The algorithm has
achieved predictive parity—perfect fairness according to one of the three accounts.
Having achieved predictive parity, this algorithm cannot also be perfectly
fair according to either of the other conceptions of bias. But it can improve
things—perhaps a lot—according to both of them. The human judges’ uniformly stronger bias against Black defendants than against white defendants
implies serious unfairness in the distribution of errors. Black defendants are
much more likely than white ones to be erroneously imprisoned. By eliminating the additional human-induced penalty for Black defendants, the well-calibrated algorithm would necessarily reduce—if not eliminate—this disparity.
The quantum of improvement is proportional to the quantum of irrational
human discrimination that existed in the first place.
Likewise for the “equal outcomes” theory of fairness. The human judges’
overestimates of risk were uniformly larger for Black defendants than white
ones. Thus, the algorithm’s elimination of human-induced error necessarily
brings the rates of Black and white incarceration closer together. Here again,

250. This model simulates straightforward stereotype-based discrimination, in which human decision makers incorrectly believe that members of one racial group are worse along some
dimension than members of another group.

March 2025]

Abolition by Algorithm

841

the quantum of algorithmic improvement is inversely related to the quantum
of human discrimination. 251
The key insight here is that improved accuracy can often be a powerful
driver of fairness. It should be no surprise, then, that the accuracy-improving
algorithms powering Algorithmic Abolitionism would reduce bias as compared with the human alternative. And they would often do so according to
multiple theories of bias simultaneously. The Laqueur–Copus algorithm, for
example, could be used to eliminate present racial disparities in incarceration
rates entirely, even while radically reducing total incarceration rates. 252 This
would constitute perfect fairness under an equal outcomes conception.
Though Laqueur and Copus do not report further equality metrics, their algorithm would likely make improvements under other theories of fairness, too.
Laqueur and Copus report that achieving equality of outcome requires almost
no tradeoff in terms of either the total reduction in incarceration or the resulting rates of crime. 253 This is at least consistent with improvements under both
the predictive-parity theory and the equal-errors theory. Thus, the Laqueur–
Copus algorithm might well improve fairness under all three conceptions simultaneously. 254 The Kleinberg et al. pretrial detention algorithm shows similar
results. 255 So too for Goel et al. They identify especially large errors in police
risk assessments of nonwhite community members, which their algorithm reduces. 256 So, by shifting from an absolutist perspective to a comparative one,
we see that algorithms can make big improvements, no matter which theory
of fairness one prefers.
This is a convenient shift. But is it normatively desirable? Bias is pernicious. Why should we accept a system that is biased at all, even if less so than
the human alternative?
It might be better to ask why the comparative perspective shouldn’t supplant the absolutist one in the debate over algorithmic bias. The absolutist perspective has never been a useful tool for evaluating social policy, including as
it relates to racial justice. Every great historical victory for civil rights, racial
equality, and antidiscrimination has been a comparative one. None have been
absolute—or even close to it. Emancipation did not end racial subordination

251. This is true assuming that incarceration scales linearly with risk. Assume as much for
purposes of this simple model. In a more complex scenario, inframarginality problems or nonlinear scaling could either reduce or magnify the algorithm’s fairness-promoting effect.
252. Laqueur & Copus, supra note 18, at 173.
253. Id.
254. Because judges in New York do not explicitly assign crime-risk probabilities to defendants, it is not possible to know for certain whether the algorithm improves, say, predictive
parity. We simply do not have the comparator. The same point holds for the other algorithms
discussed above. Nevertheless, assuming judges care at all about crime risk when sentencing,
these algorithms’ results are consistent with the hypothetical human/algorithm comparison described above.
255. Kleinberg et al., supra note 132, at 276–78.
256. Goel, Rao & Shroff, supra note 69, at 367.

842

Michigan Law Review

[Vol. 123:799

in economic, social, or political life. The Civil Rights Act did not end discrimination. Affirmative action did not end unequal access to education or employment. But all of these were serious improvements over the alternatives, and
worth implementing for that reason. Algorithmic policies should be judged no
differently.
B. Bias, Levels, and Distribution
As just described, Algorithmic Abolitionist policies are likely to reduce
bias, according to one or more major theories, compared with the alternative.
But this is not a logical guarantee. It is in principle possible that some Algorithmic Abolitionist policies could leave bias unchanged according to some
theories. Or, in the worst case, they might exacerbate it according to some.
Should such policies be automatically rejected? This Section argues that they
usually should not—at least not if they are genuinely Algorithmic Abolitionist.
The reasons have to do with levels. Even if an Algorithmic Abolitionist
policy made the distribution of incarceration or policing more racially unfair,
that would not be all it did. Algorithmic Abolitionist policies also substantially
reduce the levels of policing or incarceration at which they are targeted.
Such reductions in levels give rise to new and important normative arguments—some of them surprising. This Subsection explains two, and the next
Subsection adds a third. Each argument is designed to appeal to a different set
of normative priorities.
For the sake of clarity, parsimony, and easy math, the arguments are made
first using a thought experiment. After the thought experiment has made the
arguments’ structure clear, the real-world Algorithmic Abolitionist policies described above are reintroduced and evaluated. The results, it will be argued,
are the same.
Here is the thought experiment: Imagine a country that imprisons 1 million of its residents. 257 Suppose 1 in 3 are Black (a disadvantaged group in the
country) even though only 12% of the nation’s population is Black. 258 Under
the “equal outcomes” conception of bias, Black citizens are therefore incarcerated at nearly three times the fair rate. White citizens, by contrast, constitute
just 30% of the prison population—half of their share of the general population. 259 Now imagine a hypothetical Algorithmic Abolitionist sentencing policy that would, without increasing crime, reduce the standing number of
incarcerated citizens from one million to just 100,000. Suppose, however, that
under the policy, 40,000 of the 100,000 would be Black, and 30,000 would be
white.

257.
258.
259.

In the U.S., the figure is 1.9 million. Sawyer & Wagner, supra note 148.
This and the following demographic figures mirror the U.S. Gramlich, supra note 26.
Id.

March 2025]

Abolition by Algorithm

843

Here, then, is a policy that significantly increases bias—by 10 percentage
points 260—as evaluated using a traditional “equal outcomes” metric. That is,
the share of incarcerated people who are white remains the same. But the share
of incarcerated people who are Black increases—both as compared with
whites and as compared with the share of the total population that is Black.
For good measure, suppose that the policy would make bias worse by a similar
amount according to the other theories—predictive parity and error-rate parity—as well.
1.

Bias-Impact: A New, Levels-Linked, Measure of Fairness

Begin narrowly—with racial justice alone. Ignore all other considerations
of potential normative import, including the total reduction in incarceration.
Does our hypothetical policy make the imaginary country better or worse, just
from the perspective of racial justice? According to traditional metrics of algorithmic bias, the answer is worse—by 10 percentage points. But the traditional
metrics miss something crucial. They focus on “bias,” in the most literal
sense—racial differences in the distribution of a set of costly outcomes. But
they ignore the size of the set. They ignore the most important costs traditionally associated with discrimination—the harm individual people suffer when
subject to a bad outcome because of one’s race. These two desiderata can vary
independently. Thus, a policy can simultaneously increase the bias, as measured using existing tools, while also radically reducing the discriminatory
harm suffered by individual people.
The thought experiment’s hypothetical policy does exactly that. True,
within the set of those incarcerated, the policy substantially increases the percentage who are Black, worsening distributional bias. But because of the policy’s reduction in levels, the category of “incarcerated persons” now contains
many fewer people. As a result, not only are many fewer Black people incarcerated under the new policy than under the status quo, but many fewer Black
people are incarcerated unfairly because of their race.
Here are the numbers: Under the status quo, something like 210,000
Black citizens of our imaginary country are unfairly incarcerated each year,
according to the “equal outcomes” conception of bias. 261 This, again, is not
total Black incarceration. It is just discriminatory incarceration—the excess beyond what the fair rate would dictate. By contrast, under the hypothetical abolitionist policy—which is more biased, according to traditional measures—the

260. In the status quo, Black citizens are overrepresented by 18 percentage points (30%12%). Under the Algorithmic Abolitionist policy, they are overrepresented by 28 points (40%12).
261. Calculation of number of Black individuals incarcerated in excess of the fair number:
Status quo prison population • (Black share of prison population–Black share of total US pop.) =
1.9M • (33% - 12% = 399,000. See Sawyer & Wagner, supra note 148; Gramlich, supra note 26. I
use equal outcomes here for simplicity of illustration. But the point holds for the other conceptions of bias, too.

844

Michigan Law Review

[Vol. 123:799

number of Black Americans unfairly incarcerated nevertheless falls dramatically. Just 28,000 Black individuals are incarcerated above the figure the fair
rate would dictate. 262 That is, nearly 200,000 fewer Black Americans suffer
from racially discriminatory incarceration each year. The total harm from discriminatory incarceration falls by 87%. One might formalize these observations by saying that, although incarceration has become more racially skewed,
the discriminatory impact—the number of people treated wrongfully—has
radically decreased.
To capture this insight and encourage its application elsewhere, I propose
a new, general-purpose quantitative measure of algorithmic fairness: “biasimpact.” Bias-impact is importantly distinct from extant measures like equal
outcomes, predictive parity, and error-rate parity. It measures how a new policy changes the amount of discriminatory harm suffered by members of a disadvantaged group. It therefore shifts the focus away from the thing that every
existing measure of algorithmic fairness treats as central: imbalances in the
distribution of harmful outcomes. Such distributional imbalances are not categorically irrelevant to bias-impact. Reducing them can be one route to reducing discriminatory harm. But, as our hypothetical policy illustrates, biasimpact can also be reduced by reducing the total societal level of the harmful
outcome. Locking many fewer people up implies locking many fewer people
up unfairly.
Formally, the bias-impact of a proposed policy can be quantified using the
following equation: B = ((𝐴𝐴1 − 𝐹𝐹1) − (𝐴𝐴2 − 𝐹𝐹2))/((𝐴𝐴1 − 𝐹𝐹1)). 263 B is biasimpact: the amount (expressed as a percentage) that a new policy reduces the
number of people unfairly subjected to a harmful outcome. A1 and A2 are the
number of people in the disadvantaged group (Black citizens, in our example)
actually subjected to the harmful outcome under the status quo and the new
policy, respectively. F1 and F2 are the number of people with the protected
characteristic who would be subjected to the costly outcome if each respective
policy were fair. Note that both the A and F terms are themselves functions.
Each must be defined according to one’s preferred theory of algorithmic fairness. Under the equal outcomes conception, A is equal to the total number of
people in the disadvantaged group times the incarceration rate for that subpopulation. F is equal to the number of people in the disadvantaged group
times the incarceration rate of the whole population. Under the predictive parity conception of fairness, by contrast, A and F would be defined in terms of
each policy’s positive predictive value for different subpopulations. 264 For error-type parity, they would be defined in terms of sub-populations’ risks of
false positives. 265

262. Calculation: New prison population under hypothetical policy • (Black share of new
prison population–Black share of total US population) = 100,000 • (40%-12%) = 28,000.
263. Special thanks to Seth Chandler for thinking through this formalization with me.
264. See Hellman, supra note 24, at 820–23.
265. See id. at 822–23, 827. The discussion above skims over a further question of how to
define the “fair” rate under each theory. For “equal outcomes,” I have assumed the fair rate is the

March 2025]

Abolition by Algorithm

845

Algorithmic abolitionist policies bear a special relationship to bias-impact: they reduce it almost mechanically. The whole idea of algorithmic abolitionism is to reduce levels of harm using more accurate decision tools.
Reducing the level of policing and prison means reducing the number of people unfairly policed or incarcerated—a bias-impact reduction under the equal
outcomes conception. And accomplishing that reduction in levels via improved accuracy means reducing errors—both total and false positives—and
thus reducing bias-impact under the other conceptions. This relationship
holds so long as the Algorithmic Abolitionist policy makes meaningful improvements in levels and accuracy for members of all racial groups.
Buy why should reductions in bias-impact trump increases in bias as
measured using existing tools? Perhaps bias-impact is a poor measure of what
we really care about. Maybe it is even a deceptive one. Skeptics may argue that
bias-impact hides a kind of bait-and-switch, shifting the fairness debate to another topic entirely. After all, the existing measures of algorithmic fairness described above are all denominated in distributions, not absolute amounts of
harm. Perhaps there is a reason for that. Perhaps the wrongfulness of invidious
bias just is about distributions, not about the individual harms stemming from
biased decisions.
This objection gets things mostly backward. Consider a paradigmatic example of wrongful discrimination: the child excluded from a high-quality, majority-white school because she is Black. 266 Surely her exclusion is wrong, first
and foremost, because of how it affects her, not because of how it affects some
distribution. She is barred from receiving a quality education and, moreover,
has suffered a serious dignitary harm. These are bad outcomes regardless of
how her exclusion affects the distribution of Black and white students in the
school. Indeed, suppose the girl’s exclusion somehow increased Black representation at the school. Perhaps her case triggers white flight, leaving a majority-minority school behind. This would have no bearing at all on the
wrongfulness of her treatment. Thus, as sophisticated proponents of traditional fairness measures recognize, 267 bias’s fundamental unit of normative
analysis is its effect on people. We care foremost about the material harm of
the costly outcome and about the moral harm of its being imposed because of
race. These are exactly what bias-impact quantifies.
This is not to say that distributional measures of fairness are always normatively irrelevant. Often, they are relevant, but only for instrumental reasons.
A skewed distribution can be good evidence that many individuals are suffering the kinds of harms just described. 268 But as bias-impact shows, unskewing

average rate of incarceration for the entire population. But other conceptions of fairness are possible, and each can be plugged into the bias-impact equation.
266. See Brown v. Board of Educ. of Topeka, 347 U.S. 483, 487–88 (1954).
267. See, e.g., Hellman, supra note 24, at 835–37.
268. See id. (noting the ratio between the rates of false positives and false negatives, the
Error Ratio Parity, can demonstrate material and moral harms of bias algorithms in the contexts
of airport security and crime convictions).

846

Michigan Law Review

[Vol. 123:799

the distribution is not necessarily the only—or even best—way to eliminate
those harms.
Skewed distributions are also normatively relevant if they generate additional harmful discriminatory acts. For example, unfair distributions of policing and incarceration might lead to inaccurate stereotypes about certain
groups’ criminality. This could generate, for example, additional discriminatory exclusions from employment. Alternatively, unfair distributions of training and mentoring might lead to “statistical discrimination.” There, faced with
two apparently identical candidates of different racial groups, an employer
might assume that the member of the disadvantaged group has fewer unobservable skills. 269 Statistical discrimination is especially pernicious because it
can be actuarily sound—though unjust. The skewed distribution of training
and mentoring might actually have changed the disadvantaged group’s average levels of unobservable skills.
But here again, making distributions fairer is not the only way to solve the
problem. Reducing bias-impact may work just as well. For a stereotype or statistical discrimination to take hold, the outcome in question must be sufficiently common to be worth taking note of. Lightning is more likely to hit
taller objects than shorter ones. 270 Yet there is no stereotype that walking next
to a tall friend in a thunderstorm is a risky proposition. Nor does it seem likely
that life insurance companies statistically discriminate against the tall to account for their increased risk of death by lightning strike. The rarity of the
outcome makes its skewed distribution irrelevant. This is an extreme example
of a low probability event. But it illustrates how reductions in bias-impact
could, just like distributional improvements, mitigate the harms of stereotyping and statistical discrimination.
There may also be reasons to care about unfair distributions intrinsically,
rather than instrumentally. One such reason might be the expressive power of
the law. 271 A skewed distribution—in policing, incarceration, or elsewhere—
disfavoring historically oppressed groups communicates whom society values.
Figuring out what, exactly, law expresses may often be complicated. For example, if the skewed distribution was imposed as part of an Algorithmic Abolitionist policy intentionally designed to reduce bias-impact, the message is
ambiguous. Nevertheless, the point stands. In some situations, there will be
reasons to assign freestanding normative value to fair distributions, as traditional algorithmic fairness measures do.
Thus, bias-impact captures the great majority of what matters most about
bias better than traditional distributional measures. It captures the harms
from discrimination to the real people who actually experience them. It also
captures much of what has historically mattered about fair distributions, since

269. M. Bertrand & E. Duflo, Field Experiments on Discrimination, in 1 HANDBOOK OF
ECONOMIC FIELD EXPERIMENTS 310 (Abhijit Vinayak Banerjee & Esther Duflo eds., 2017).
270. Severe
Weather
101,
NOAA
NAT’L
SEVERE
STORMS
LAB’Y,
https://www.nssl.noaa.gov/education/svrwx101/lightning/faq [perma.cc/MQ9U-DMWP].
271. See generally RICHARD H. MCADAMS, THE EXPRESSIVE POWERS OF LAW (2017).

March 2025]

Abolition by Algorithm

847

distributional metrics were—in a pre-Algorithmic Abolitionist world—good
proxies for individual discriminatory harm. Only in those limited contexts
where fair distributions matter, qua fair distributions, might a tension arise
between reducing bias-impact and improving traditional measures of algorithmic fairness. “Might” is important here. Usually, as already discussed, Algorithmic Abolitionist policies will improve according to both metrics
simultaneously. But when they do not, it will be necessary to make trade-offs
between reductions in bias-impact and improvements in distributional fairness. The next Section addresses how best to navigate such tradeoffs.
2.

Trans-Theoretic Tradeoffs Between Levels and Distribution

Even now, some bias-wary progressives may remain unconvinced. Perhaps, despite the arguments above, they reject bias-impact as the sole measure
of fairness because they significantly value pure distributional fairness, irrespective of how it affects individual people. Then, an Algorithmic Abolitionist
policy that worsened things according to a traditional measure of bias might
be objectionable on fairness grounds, regardless of its bias-impact.
But even this would not be reason to object to the policy, full stop. Fairness
is not the only thing that matters. And Algorithmic Abolitionist policies are
not mostly about fairness. Instead, they are about massively reducing carceral
harm by eliminating large shares of policing and prison.
Here, we widen the scope of the normative inquiry to consider desiderata
beyond racial justice alone. The question now is whether and when a policy’s
total benefits might be sufficiently large to overcome some worsening of distributional fairness. The possibility that algorithmically driven policies could
present such tradeoffs is not new. 272 But in contrast with the existing literature,
this Section eschews pure cost-benefit-analysis. Instead, it fashions a test under which trade-offs should be deemed acceptable even to individuals placing
a very high premium on pure distributional justice.
Suppose one holds a mixed normative theory that assigns value both to
the magnitude of a policy’s net benefits and to who gets them—that is, to distribution. Prioritarianism is one example of such a theory. Prioritarians insist
that, in any analysis of a policy’s costs and benefits, greater weight must be
assigned to those who were worse off under the status quo. 273 Rawls’s Difference Principle is another example. It is even stricter—a kind of prioritarianplus rule. It assigns lexical priority to the wellbeing of the worst-off members
of society. 274 The Difference Principle holds that an increase in distributional
unfairness is justified only if accomplished via whatever policy sets the highest
“floor” of outcomes for the worst-off individuals. 275

272. See, e.g., Matthew Adam Bruckner, The Promise and Perils of Algorithmic Lenders’ Use
of Big Data, 93 CHI.-KENT L. REV. 3, 17–31 (2018).
273. See Derek Parfit, Equality or Priority, Lindley Lecture, Univ. of Kans. at 19–20 (1995).
274. See JOHN RAWLS, A THEORY OF JUSTICE 75 (1971).
275. See id. at 78–79.

848

Michigan Law Review

[Vol. 123:799

But one could go stricter, still, fashioning a test for policy trade-offs that
stacked the deck even more strongly in favor of distributional justice. One
could insist, though no mainstream normative theory requires it, 276 on a “Super Difference Principle.” Under it, the ordinary Difference Principle must be
satisfied. The inequality-increasing policy must have a higher floor of outcomes than alternatives. But that is not enough. Under the Super Difference
Principle, the group that was the worst off under the status quo must get the
biggest benefit from the new policy. This is a kind of hyper-prioritarianism,
wherein the needs of those at the bottom of the distribution are given as much
weight as necessary to outweigh all other groups’. The Super Difference Principle is so demanding that it may often be impossible, as a practical matter, to
satisfy. This will be the case if the policy that most raises the floor on bad outcomes may give somewhat larger benefits to groups other than those most disadvantaged ex ante. 277
Nonetheless, Algorithmic Abolitionist policies would almost always satisfy all of these constraints, up to and including the Super Difference Principle.
Our thought experiment again illustrates why. Under the status quo, Black citizens are so overrepresented in the imaginary country’s prison population
that, despite being a minority group, they outnumber incarcerated white citizens. 278 Thus, the hypothetical Algorithmic Abolitionist policy would free
thousands more Black people than white ones.
The story is the same—indeed, starker—viewed from the perspective of
the risk of incarceration faced by different groups. Assume our imaginary
country has roughly the population of the United States. Then, under the status quo, 0.92% of the country’s Black population is incarcerated at any given
time. 279 By contrast, only 0.17% of the white population is incarcerated—
about five times fewer. 280 But the hypothetical Algorithmic Abolitionist policy
would bring Black incarceration risk down by 0.81 percentage points. 281 This
is a much greater benefit than for white citizens, for whom risk would go down
by only 0.15 percentage points. 282 The absolute benefit to Black citizens, in
terms of reduced risk of incarceration, would thus be over five times greater
than that to whites.

276. Of which the author is aware.
277. Note however that, in theory, transfers from better-off groups to worse-off ones could
remedy this problem.
278. John Gramlich, The Gap Between the Number of Blacks and Whites in Prison is Shrinking,
PEW RSCH. CTR.
(Apr.
30,
2019),
https://www.pewresearch.org/facttank/2019/04/30/shrinking-gap-between-number-of-blacks-and-whites-in-prison
[perma.cc/T8DY-2PGV].
279. (1M • 0.33) / (300M • 0.12) = 0.92%.
280. (1M • 0.3) / (300M • 0.6) = 0.17%.
281. 0.92% - ((100K • .04) / (300M • 0.12).
282. 0.17% - ((100K • 0.3) / (300M • 0.6).

Abolition by Algorithm

March 2025]

849

The hypothetical sentencing policy is thus prioritarian. The needs of the
worst-off group under the status quo—Black Americans—get special attention. It complies with the ordinary version of the Difference Principle. 283 As
compared with the status quo, the worst-off group sees both its total incarceration and its per-capita risk of incarceration decline. Nor, as argued below,
could any feasible alternative policy raise the floor on incarceration risk
more. 284 The sentencing policy even satisfies the Super Difference Principle.
Black Americans see a larger reduction in incarceration—both total and per
capita—than any other group.
These are nearly mechanical results of abolitionist—including Algorithmic Abolitionist—policies. Dramatically reducing the system’s burdens across
the board automatically raises the floor for bad outcomes, and in doing so
gives special priority to the worst off. And so long as the reductions are relatively evenly distributed the largest benefits will accrue to those whom the status quo harmed most disproportionately. 285 Anyone holding a plausible theory
that assigns value both to total net benefits and to their fair distribution should
be satisfied. 286
3.

How Real Policies Fare

The previous Subsections used a thought experiment, with easy math, to
demonstrate in principle how an Algorithmic Abolitionist thinking upends
traditional debates over algorithmic fairness. They showed that even a policy
that worsens racial bias according to traditional measures may nevertheless
decrease it according to an alternative, richer measure. And they showed that
any lingering concerns about fairness could be outweighed by non-distributional benefits, even when the weighing is severely constrained.
But this Article is not about thought experiments. It is about real Algorithmic Abolitionist policies that could be implemented using existing technology.
The thought experiment was useful because it showed that these results all
flow from a single source: large reductions in levels of carceral harm. The
question, then, is whether the actual policies discussed herein reduce levels
enough to make them normatively comparable to the hypothetical one.
283. See RAWLS, supra note 274, at 75.
284. See infra Section IV.0.
285. As with bias-impact, one can construct examples to the contrary. But this requires
designing a policy that—probably intentionally—dramatically reduces incarceration only for
white, not Black, Americans.
286. Of course, some moral theories, like pure deontology, reject the idea of weighing
goods against ills, no matter how constrained the trade-offs. See IMMANUEL KANT, GROUNDING
FOR THE METAPHYSICS OF MORALS; WITH, ON A SUPPOSED RIGHT TO LIE BECAUSE
PHILANTHROPIC CONCERNS 63–65 (3d ed. 1993). This view is of course in some tension with
real-world observation that sometimes, all available courses of action would appear to imply
some violation of a right or duty. As relevant here: the duty to ensure distributional fairness may
conflict with the duty to reduce harm from discrimination. This Article does not attempt to resolve that deep puzzle, leaving it to more capable deontologists. See generally, e.g., Christine M.
Korsgaard, The Right to Lie: Kant on Dealing with Evil, 15 PHIL. & PUB. AFFS. 325 (1986).

850

Michigan Law Review

[Vol. 123:799

None of the actual policies advocated herein could, like the hypothetical
one, singlehandedly bring the American prison population down to 100,000.
Nevertheless, some of them are very nearly as ambitious as the hypothetical
one, at least within their own domains. Algorithmic Abolitionism for Terry
stops could eliminate, at the high end, nearly 90% of them. 287 And Algorithmic
Abolitionism for traffic enforcement could replace an arbitrarily large proportion of traffic stops. 288 Thus, even if these policies had no impact on bias, as
quantified using traditional metrics, they could reduce bias-impact 90% or
more. And even if bias in street stops doubled, as measured using existing metrics, bias-impact would still be reduced by about 80%. 289
Likewise, non-fairness related benefits could be huge. Each year, these Algorithmic Abolitionist policies might spare tens of millions of Americans from
unwanted—and often dangerous—traffic stops. That is hundreds of millions
in the policy’s first decade. 290 Over 2.5 million people could be reprieved from
invasive and intimidating street stops. 291 As with the hypothetical policy, the
benefits from these reductions would flow disproportionately to Black and
Hispanic Americans, who make up more than 80% of stops under the status
quo. 292 Improved accuracy in determining who to stop would skew benefits in
further favor of Black and Hispanic Americans. 293 That is because human decisionmakers systematically overrate these groups’ likelihood of carrying a
weapon, as compared with whites. 294 These improvements satisfy all of the
above-discussed constraints on tradeoffs, including the Super Difference Principle.

287. See supra Section II.0.
288. See supra Part II.
289. Goel et al., report a status quo gap in predictive parity. Street stops of white individuals
result in the recovery of contraband 3.8% of the time, as compared with 2.5% for similarly situated Black individuals. Goel, Rao & Shroff supra note 69, at 379. Thus, the police unfairly stopped
52% more Black individuals than white ones to recover the same number of guns (0.038 / 0.025%
= 1.52). That is, 52 of every 152, or 34 of every 100 stops of Black individuals could be attributed
to bias, as compared with the baseline of predictive parity. Suppose, then, that an Algorithmic
Abolitionist policy doubled the gap predictive accuracy, producing a 3.8% true positive rate for
white individuals and a 1.2% rate for Black individuals, or about 69 out of 100 Black stops attributable to bias. (34 – 0.1 • (69))/34 = 0.797.
290. A rough calculation: % of Americans over 16 years of age reporting unwanted traffic
stops annually (see DAVIS, WHYDE & LANGDON, supra note 178, at 1, fig. 1) • % of Americans over
18 years of age (over-16 data not readily available) • U.S. population = 27.9M stops per year under
the status quo. See Quick Facts, U.S. CENSUS BUREAU, https://www.census.gov/quickfacts/fact/table/US/PST045221 [perma.cc/WKP6-MQV6]. If these were reduced by even half,
over 135M stops would be eliminated per decade.
291. Same calculation as id., but using % of Americans over 16 reporting unwanted street
stops = 2.62M.
292. Goel, Rao & Schroff, supra note 69, at 366.
293. Id. at 382.
294. See id. at 379–81.

Abolition by Algorithm

March 2025]

851

The same goes for Algorithmic Abolitionist decarceration policies. Here,
the magnitude of abolition is somewhat smaller. As discussed above, the highest-end estimate, given some assumptions, is that existing algorithms could be
used to eliminate 80% of incarceration. 295 At the risk of becoming repetitive,
an 80% reduction in incarceration with no change in bias, would reduce biasimpact—the number of people discriminatorily incarcerated—by 80%. Pessimism about the capabilities of Algorithmic Abolitionist policies does not
change the picture much. Even if a policy doubled the strength of bias—an
implausible figure—bias-impact impact would still be reduced by about
60%. 296 Likewise, even if only 40% of incarceration could be eliminated—the
low-end estimate—and bias was held constant, bias-impact would fall 40%. 297
And for the reasons discussed above in relation to the model policy,
broad-based reductions in incarceration satisfy even an extremely strict fairness constraint on tradeoffs, like the Super Difference Principle. Black Americans are so systematically disadvantaged by status-quo policies that any broadbased reduction in incarceration benefits them more than any other group.
Thus, actual Algorithmic Abolitionist policies are not so different from the
policy in our thought experiment. Analysis of the hypothetical policy simply
made clear that policies implementing sufficiently large reductions in levels
upend traditional distribution-focused objections. And though the estimates
are wide as to how much policing and imprisonment the Algorithmic Abolitionist policy discussed here would eliminate, even the low-end figures are
quite large.
C. Structural Inequality
Perhaps the real justice-oriented objection to algorithms is not to bias in
predictions or outcomes, per se, but rather to the long-run effects of those initial inequalities. Abolitionist and progressive opponents of algorithms regularly charge that such tools “exacerbate” inequality and “reenforce” certain
“structures” of disadvantage. 298 This is a version of the algorithmic bias argument, but extended through time. And it is true—disadvantage can breed further disadvantage. 299 Incarceration reduces one’s ability to legally earn a living,

295.
296.

See supra Section II.0.

𝑝𝑝𝑝𝑝𝑝𝑝. (0.33 −0.12) −0.2 • 𝑝𝑝𝑝𝑝𝑝𝑝.(0.12 + 2 (0.33 −0.12) −0.12)
= 0.6
𝑝𝑝𝑝𝑝𝑝𝑝. (0.33 − 0.12)

Here, consistent with the equal outcomes conception of bias, “doubling” the bias means doubling the excess percent of the prison population that is Black, compared with the Black share of
the total population. For input figures, see supra notes 30–31. For the basic bias-impact equation,
see supra note 263 and accompanying text.
(𝑝𝑝𝑝𝑝𝑝𝑝. (0.33 − 0.12) − 0.6 (𝑝𝑝𝑝𝑝𝑝𝑝. (0.33 − 0.12))
297.
= 0.4
𝑝𝑝𝑝𝑝𝑝𝑝. (0.33 − 0.12)

298. See, e.g., Akbar, supra note 49, at 1809–10 n.123; Jessica M. Eaglin, Predictive Analytics’
Punishment Mismatch, 14 I/S 87, 103 (2017); EUBANKS, supra note 70, at 7, 190 (2018).
299. See Deborah Hellman, Big Data and Compounding Injustice, J. MORAL. PHIL. (forthcoming) (manuscript at 4–8), https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3840175
[https://perma.cc/VR2S-ES4V].

852

Michigan Law Review

[Vol. 123:799

which in turn increases the probability that one will resort in the future to
illegal alternatives, producing more incarceration, and so on. 300 Such cycles of
amplification could possibly result in group disparities at the societal level.
Algorithmic Abolitionism again has a distinctive response to such concerns—one not available in the existing literature on algorithmic fairness. This
is again because Algorithmic Abolitionist policies are, first and foremost, designed to reduce levels of penal harm. And yet again, reducing levels has unexpected and normatively relevant implications.
The crucial question here is how modest initial disadvantages imposed by
the criminal justice system might cyclically reenforce themselves into large
disadvantages for entire social or racial communities. Such compound harm
does not always occur. If it did, then every group affected at all by the criminal
justice system—i.e., every group in American life—would have already experienced a similar upward spiral. Rates of arrest, charging, conviction, and incarceration would then be very high—and roughly equally so—for all groups. But
they are not. On the contrary, Hispanic Americans are incarcerated at rates
over two and a half times higher than whites, and Black Americans are incarcerated at a rate over five times higher than whites. 301 Thus, the “structural
inequality” critique of algorithms depends on a model under which initial
harms compound for some groups, but not others.
Here is a simple, plausible, model on which such differential compounding could occur. Suppose that harmful interactions with the criminal justice
system have some rate of reproduction. The COVID-19 pandemic has made
this “R0” concept familiar. 302 An R0 of 1 means that a given harmful incident—
in our case, a street stop, arrest, prosecution, term of incarceration, etc.—will,
in expectation, cause one additional interaction of roughly equal harm. In that
case, total harm will remain level, with each instance reproducing itself, but
no more. As R0 rises above 1, the total number of instances begins to grow—
perhaps exponentially. 303 But as it drops below 1, the total number decays in
the same way. 304
What could modulate the R0 of interactions with the criminal justice system, such that some, but not all, groups might experience runaway feedback
loops? Differences in the ambient levels of criminal enforcement endured by
different groups probably play a role. There are many plausible mechanisms
by which such levels could influence R0 rates. Consider, for example, the direct
300. See supra Section I.0.
301. See Gramlich, supra note 26.
302. See generally Achaiah, Subbarajasetty & Shetty, supra note 34.
303. See id. at 1125–26. The growth curve of viral infection is exponential in shape. The
curve for carceral harm might or might not be. This does not matter to the argument. What
matters is that for R0 > 1, it slopes upward, and for R0<1, it slopes downward. Jeffrey K Aronson,
Jon Brassey & Kamal R Mahtani, “When Will It Be Over?” An Introduction to Viral Reproduction
Numbers, R0 and Re, CTR. EVIDENCE-BASED MED. (Apr. 14, 2020), https://www.cebm.net/wpcontent/uploads/2020/04/%E2%80%9CWhen-will-it-be-over_%E2%80%9D_-An-introduction-to-viral-reproduction-numbers-1.pdf [perma.cc/PQH4-L89C].
304. Id.

March 2025]

Abolition by Algorithm

853

effect of an arrest on the arrestee’s employment prospects. If a given individual
is arrested once and briefly detained, there is some probability that they can
retain their job. Perhaps they can use sick days to cover the absence, or perhaps
their employer will extend some lenience for a one-time occurrence. But if—
due to higher ambient levels of enforcement—an individual is arrested twice
in relatively quick succession, the odds of remaining employed may decrease
dramatically. Then, a job-loss/arrest spiral may result.
There are other plausible mechanisms by which levels could influence R0,
as well. As discussed above, longer-term incarceration may be criminogenic
for those exposed to it. 305 This is partly because of peer effects. Spending lots
of time with people who commit crimes may make you more likely to commit
them. 306 Such peer effects matter outside of prison, too. 307 A young person
whose friends have mostly been arrested for crimes will be more likely to be
arrested than a young person with just one such friend. 308 Here, because connections within social networks grow exponentially, linear increases in ambient enforcement will quickly push R0 upward.
Critics of algorithms in criminal enforcement raise another possible
mechanism: High initial levels of enforcement in neighborhoods of color lead
to the detection of a higher proportion of crimes there than elsewhere. 309 This
generates a false perception of the neighborhoods as dangerous, which may be
used to justify unusually large police responses to additional reported crimes.
Those larger responses push the share of detected crimes up even further, and
so on.
Observe that all of these mechanisms by which R0 is modulated are, first
and foremost, functions of levels of policing and imprisonment, not of disparities in them. This means that, for certain groups, but not others, to experience
spirals of carceral harms, disparities are necessary. But they are not sufficient.

305. See supra Section I.0.
306. See generally, e.g., M. Keith Chen & Jesse M. Shapiro, Do Harsher Prison Conditions
Reduce Recidivism? A Discontinuity-Based Approach, 9 AM. L. & ECON. REV. 1 (2007); Patrick
Bayer, Randi Hjalmarsson & David Pozen, Building Criminal Capital Behind Bars: Peer Effects
in Juvenile Corrections, 124 Q.J. ECON. 105 (2009).
307. See, e.g., Erkmen Giray Aslim, Yijia Lu, & Murat C. Mungan, Inmate Assistance Programs: Toward a Less Punitive and More Effective Criminal Justice System, 75 ALA. L. REV. 863,
885 (2023) (describing cases in which an ex-inmate recidivates and is likely to motivate others in
his network to perform crimes).
308. Dana L. Haynie, Friendship Networks and Delinquency: The Relative Nature of Peer
Delinquency, 18 J. QUANTITATIVE CRIMINOLOGY 99, 121 (2002).
309. See, e.g., Open Statement, supra note 231. Algorithmic Abolitionism aside, there is
something puzzling about this argument. There are only so many crimes to detect in the world.
Thus, if neighborhoods of color are over-policed, turning policing decisions over to algorithms
seems likely to equalize, rather than exacerbate, inequality. This is because a marginal increase
in policing in an over-policed neighborhood will detect fewer marginal crimes than the same
increase in an under-policed neighborhood. If algorithms are continuously trained on the results
of their prior recommendations, they should identify under-policing and correct it.

854

Michigan Law Review

[Vol. 123:799

To see why, observe that, for any two groups with an R0 of less than one,
the long-run result is convergence, not divergence. In both populations, carceral interactions decay and run to zero. 310 This is true even if there are major
disparities in how the two groups are policed or incarcerated. Since levels drive
R0, disparities in the ambient level of enforcement only matter to the long-run
trend when they push one—and only one—group’s R0 above one. If not—if
both R0s are either above or below one—the long-run result is equality.
Here is an example to make the point concrete. Consider again the employment-linked mechanism for modulating R0. Suppose that initial enforcement levels are such that members of Black communities are arrested, on
average, one time over the course of their holding a given job, and members
of white communities are arrested on average 0.5 times. This is a huge disparity in enforcement. But supposing that it takes at least two arrests to lose a
job—thus generating more crime, and then more arrests—the R0 in both communities is below one. Then, assuming prior arrests are the only thing that
generates additional crime and future arrests, arrest rates in both communities
would run to the minimum. Under this model, it is levels, not disparities, that
primarily drive long-run social outcomes.
Now we can see why Algorithmic Abolitionist policies could turn the
standard “structural inequality” critique of algorithms on its head. Again, the
point of Algorithmic Abolitionism is to use algorithms to significantly reduce
levels of prison and policing. If, as discussed above, levels of criminal enforcement are what generate (or not) structural inequality, then Algorithmic Abolitionist policies are not likely to exacerbate it. On the contrary, Algorithmic
Abolitionism could be a powerful force for eliminating structural inequality.
Algorithmic Abolitionist policies would help push the R0 of prison and policing in vulnerable communities below one. This could, in turn, “crush the
curve” of spiraling disadvantage and promote long run racial equality. 311
Of course, there is no guarantee that Algorithmic Abolitionism would, on
its own, cure America’s racial or other structural injustices. Indeed, one must
ask why, under the above-described account of inequality’s genesis, ambient
levels of policing and prison are unequal in the first place. Racism, of course,
is a major part of the answer. For centuries, race-based disadvantage—including in criminal enforcement—was written explicitly into the law. 312 And even
though most such laws have now been overturned, racially discriminatory decision making continues to pervade society. 313 Thus, even under Algorithmic

310. Or to whatever minimum asymptote exogenous forces set. It is possible that the asymptote is different for different groups, due to, for example, discrimination.
311. Harvey V. Fineberg, Ten Weeks to Crush the Curve, 382 NEW ENGLAND J. MED. e37(1),
e37(1) (2020).
312. See, e.g., Irene E. Williams, The Operation of the Fugitive Slave Law in Western Pennsylvania, from 1850 to 1860, 4 W. PA. HIST. MAG. 150 (1921).
313. See Peter N. Salib, Big Data Affirmative Action, 117 NW. U. L. REV. 821, 828–31 (2022)
(collecting sources).

March 2025]

Abolition by Algorithm

855

Abolitionism, such baked-in factors would continue to push levels of policing
and prison upward for members of racial minority groups.
The point, however, is that if high levels of policing and prison are what
drive structural inequality, then policy approaches that reduce those levels will
help fight it. Algorithmic Abolitionism is such a policy approach. Even if it is
not a panacea, it is likely to be a force in the right direction. At a minimum,
Algorithmic Abolitionist policies would help to “slow the spread” 314 of structural inequality. This would buy time for additional interventions—education,
healthcare, housing, and other creative solutions 315—to be brought to bear.
Algorithms could be a powerful tool here, too. They could, for example, help
to identify the people who would benefit the most from additional help. 316
IV. REMARKS ON OTHER NORMATIVE QUESTIONS
The previous Part had much to say about one important and longstanding
normative objection to algorithms—discrimination. It had much to say there
because Algorithmic Abolitionist thinking offers several genuinely new insights into the problem of algorithmic bias. It also had much to say there because the possibility of racial injustice is perhaps the most common reason for
opposition to algorithms, both in criminal justice and elsewhere.317 The hope,
therefore, is that Part III represents a comprehensive response to the most important normative concerns about Algorithmic Abolitionism.
There are, of course, other longstanding normative concerns about algorithms, some of which apply to Algorithmic Abolitionist policy. This Part
raises several, but treats them much more briefly, and thus less satisfyingly,
than Part III treated the bias-related objections. That is in part because one
Article can only do so much. But it is also in part because Algorithmic Abolitionist thinking introduces fewer genuinely novel arguments into these other
debates. The Part thus seeks principally to situate Algorithmic Abolitionism
within each normative debate, allowing the principal debaters to compare it
to the alternatives.
There are, however, a few unique Algorithmic Abolitionist insights here,
too. The first has to do, again, with levels. For certain normative concerns—
like privacy and surveillance—Algorithmic Abolitionist policies could greatly
reduce total levels of costly interventions. Such reductions might produce
large net normative improvements, even if the remaining interventions increased their intensity. The second Algorithmic Abolitionism-specific insight
explored here is positive-sum bargaining. Algorithmic Abolitionist policies are

314. Slow the Spread of Covid-19, CTRS. FOR DISEASE CONTROL & PREVENTION (July 8,
2020) https://stacks.cdc.gov/view/cdc/90440/cdc_90440_DS1.pdf [perma.cc/FRK4-8EEZ].
315. See, e.g., Salib, supra note 313.
316. See generally, e.g., Sara B. Heller, Benjamin Jakubowski, Zubin Jelveh & Max Kapustin,
Machine Learning Can Predict Shooting Victimization Well Enough to Help Prevent It (Nat’l Bureau of Econ. Rsch., Working Paper No. 30170, 2024), https://doi.org/10.3386/w30170.
317. See Scholarship, supra note 234 (collecting dozens of examples of studies that oppose
algorithms because of racial injustice).

856

Michigan Law Review

[Vol. 123:799

nearly unique among criminal justice reforms in that they could be used to
simultaneously reduce both crime and policing and prison. This could allow
for agreements between political factions that are usually bitterly divided.
These themes will recur throughout the Part.
A. The Political Economy of the Carceral State
The core idea of Algorithmic Abolitionism is that algorithms should be
used to maximally reduce prison and policing without increasing crime. But
despite abolitionists’ success at convincing many liberal voters of the value of
that goal, not everyone agrees. Some would prefer to use algorithms in the opposite way, to further reduce crime while holding prison and policing constant—or even increasing them. 318 Insofar as this “tough-on-crime” sentiment
is a powerful political force, perhaps algorithms in policing should be vigilantly opposed, irrespective of their abolitionist potential. The worry is that, if
they are not opposed, they will inevitably be coopted for pro-carceral, rather
than anticarceral, purposes.
Certainly, the desire to reduce crime is a powerful political force. And often for good reason. Crime is extremely harmful, with the harm falling disproportionately on the poor and communities of color. 319 There are also, of
course, bad reasons to support increased crime-prevention efforts—for example if one was motivated by racial animus to impose more harms from policing
on these same communities. But even for those who prioritize reducing carceral harm over reducing crime, the threat of tough-on-crime politics should
not be sufficient reason to uniformly oppose algorithms in criminal enforcement. At least not when Algorithmic Abolitionism is an option.
The reason is that, unlike almost any other criminal justice reform policy,
Algorithmic Abolitionism can improve on both fronts simultaneously.
Laqueur and Copus provide a useful illustration. Recall their estimate that,
holding crime constant, their algorithm could be used to release as many as
80% of parole-eligible prisoners without increasing crime. 320 They also give an
estimate of the inverse: the amount of crime their improved risk assessments
could eliminate without increasing incarceration. Under the status quo, 33%
of parolees were rearrested within three years. 321 An algorithmically driven

318. Kleinberg et al., supra note 132, at 241.
319. See, e.g., Christopher Lewis & Adaner Usmani, The Injustice of Under-Policing in America, AM. J.L. & EQUAL., SEPT. 2022, AT 85, 102. 85, 102 (2022).
320. Laqueur & Copus, supra note 18, at 170. Again, in New York, where their data was
drawn from, this would imply a 60-point reduction in incarceration during the study period,
since 20% of parole-eligible prisoners were already being released. In a jurisdiction granting parole at much lower rates, the total reduction would approach the full 80 points, and in a jurisdiction granting more parole, it would be lower.
321. Id.

March 2025]

Abolition by Algorithm

857

policy could reduce that figure to as few as 10%, a nearly 70% reduction in
crime. 322
This, then, represents the “deal space.” Both groups could agree to some
large, but sub-maximal policy that made both sides better off simultaneously.
Suppose, lacking the political power to act unilaterally, abolitionists had to
agree to an Algorithmic Abolitionist policy that reduced incarceration by
“only” 60, 50, or 30%. Any of these would still be huge, even by the heady
standards of abolitionist goals circa 2020. 323 And suppose, given those reductions in incarceration, crime among those released was reduced by “only” 40,
30, or 20%. 324 This would have a massive impact, on the order of the unprecedented nationwide reductions in violent crime that occurred in the 1990s. 325
Thus, endorsing algorithms for use in Algorithmic Abolitionist policies
does not necessarily risk their co-option for use in pro-carceral policies. Much
more likely, a deal could be struck that would simultaneously reduce the harm
from crime, prison, and policing. Moreover, in the large urban jurisdictions
most likely to implement algorithmic policies, the deal would likely favor abolitionist preferences. As described above, Democratic voters appear open to
abolitionist arguments for reducing prison and policing. They do not want to
see crime go up; but there is little evidence of an appetite to drive it down at
all costs. 326
B. Humane Replacements for Police
The political argument for Algorithmic Abolitionism posits that there is
pent up demand among left-leaning voters for policies that could significantly
reduce prison and policing without increasing crime. That is, abolitionists succeeded in convincing the voters about the goal, but their concrete proposals
were insufficiently attentive to the voters’ fears. This theory would be falsified
if previous abolitionist proposals would in fact have avoided increases in crime
but lost popularity anyway. Many abolitionists might argue exactly that. Often,
their proposals called not just for eliminating policing and prison, but for replacing them with more humane alternatives.
If such alternatives existed, they might be normatively preferable even to
Algorithmic Abolitionism. After all, Algorithmic Abolitionism still relies on the
costly tools of policing and prison to control crime. It simply eliminates their
excess use. But if other, more humane, tools could control crime just as well,
then they might be used to reduce carceral harm even more.
322. Id. Note that the proportional reductions possible are similar if the analysis is limited
to violent crime.
323. See Kaba, supra note 2 (advocating a 50% reduction in policing).
324. These are just example figures; the exact deals possible would depend on the shape of
the risk distribution for parole-eligible incarcerated people.
325. See Steven D. Levitt, Understanding Why Crime Fell in the 1990s: Four Factors that
Explain the Decline and Six that Do Not, J. ECON. PERSPS., Winter 2004, at 163.
326. See Parker & Hurst, supra note 1 (recording plurality support among Democrats in
both 2020 and 2021 for holding police funding steady).

858

Michigan Law Review

[Vol. 123:799

For better or worse, however, the existing empirical evidence does not
suggest that abolitionists’ proposed alternatives could replace very much
prison and policing. Many of them have independent merits. And all of them
would benefit from additional high-quality causal research. But, today, none
seems likely to credibly rival the abolitionist potential of an algorithmic approach, at least not without increasing crime.
Here are a few of the most popular proposals, along with brief summaries
of the evidence, as it stands.
Replacing police with mental health workers: 327 Eugene, Oregon has had
such a program—called CAHOOTS—since 1989. 328 Despite its maturity,
CAHOOTS workers respond to only 17% of 911 calls. 329 Of those, 75% are
welfare checks, requests to provide transportation, or non-emergency service
requests from the public. 330 Less than 2% of calls to which CAHOOTS is dispatched involve an identifiable report of a crime, and even those are simple
trespass. 331 Thus, CAHOOTS almost never responds on its own to the kinds
of adversarial calls most likely to escalate into violence. CAHOOTS may be
effective within its domain, but that domain is quite small. 332
Violence Interrupters: Violence interruption 333 is an intervention where
members work to “dissuade specific individuals and neighborhood residents
in general from engaging in violence.” 334 At the height of the “defund” movement, the approach was widely endorsed, even by non-abolitionists like New
York Mayor Bill de Blasio and President Joe Biden. 335 Dozens of cities have
already deployed this approach. 336 But the best empirical evidence so far does
not show any clear crime controlling effect. A 2015 review of the empirical
literature on violence interruption finds that the “evidence in support of

327. See, e.g., INDIA THUSI, BEYOND POLICING 10 (2020).
328. CAHOOTS stands for “Crisis Assistance Helping Out On The Streets.” Id.
329. See What is CAHOOTS?, WHITE BIRD CLINIC (Oct. 29, 2020),
https://whitebirdclinic.org/what-is-cahoots [perma.cc/9VM6-VHAQ].
330. See EUGENE POLICE DEP’T CRIME ANALYSIS UNIT, CAHOOTS PROGRAM ANALYSIS
(2020).
331. Id. (showing “Criminal Trespass” calls at 1.39%).
332. THUSI, supra note 327, at 10.
333. See, e.g., McLeod, supra note 48, at 1227–28; Roberts, supra note 2, at 47 & n.274;
THUSI, supra note 327, at 9; Philip V. McHarris & Thenjiwe McHarris, No More Money for the
Police, N.Y. TIMES (May 30, 2020), https://www.nytimes.com/2020/05/30/opinion/georgefloyd-police-funding.html [perma.cc/Q4PX-PKKS].
334. THUSI, supra note 327, at 9.
335. Jon Schuppe, Biden Wants to Give Anti-Violence Groups $5 Billion. Here’s How It Could
Be Spent, NBC NEWS (Apr. 14, 2021, 5:00 AM), https://www.nbcnews.com/news/usnews/biden-wants-give-anti-violence-groups-5-billion-here-s-n1263990
[perma.cc/KU3HP6YY].
336. CHARLES BRANAS ET AL., REDUCING VIOLENCE WITHOUT POLICE: A REVIEW OF
RESEARCH EVIDENCE 9 (2021).

March 2025]

Abolition by Algorithm

859

the . . . model to date is mixed at best.” 337 In the most favorable studies it had
zero measured effect on crime at nearly half of deployment sites. 338 The effects
were even smaller on gun injuries and deaths. 339 And since no studies so far
are randomized or even quasi-randomized, they cannot “clearly disentangle
the results from national and regional trends in violent crime.” 340
Restorative Justice: “Restorative justice” practices are a proposed alternative to punishment via imprisonment. There, where wrongdoers are invited to
“encounter” those whom they have wronged and try to “repair” those
wrongs. 341 Again, the empirical results are mixed at best. One high-quality,
randomized trial found no statistically significant effect of a restorative program on future commissions of domestic violence. 342 A recent review the literature likewise finds modest, at most, effects. 343
Decriminalization: As discussed above, untargeted, across-the-board reductions in prison would cause crime to go up. But maybe some crimes should
not be criminalized, or at least should not carry the penalty of incarceration,
in the first place. 344 Could large amounts of prison be eliminated simply by
updating our view about what is and isn’t worthy of punishment? Possibly, but
there is little low-hanging fruit in the current system. Simple drug possession
seems a likely place to start.345 But only 3.8% of Americans in state prisons
were convicted of drug possession as their most serious offense. 346 Likewise

337. Jeffrey A. Butts, Caterina Gouvis Roman, Lindsay Bostwick & Jeremy R. Porter, Cure
Violence: A Public Health Model to Reduce Gun Violence, 36 ANN. REV. PUB. HEALTH 39, 47
(2015); see also BRANAS ET AL., supra note 336, at 9 (describing the evidence on the approach as
“promising but mixed”).
338. Wesley G. Skogan, Susan M. Hartnett, Natalie Bump & Jill Dubois, Evaluation of
CeaseFire-Chicago, DEP’T OF JUST. (2008) https://www.ojp.gov/pdffiles1/nij/grants/227181.pdf
[perma.cc/Z9EG-6TTG].
339. Id. at tbl.7-9–tbl.7-10.
340. JEFFREY A. BUTTS WITH, LINDSAY BOTSWICK & JEREMY PORTER, JOHN JAY COLL.,
DENORMALIZING VIOLENCE: EVALUATION FRAMEWORK FOR A PUBLIC HEALTH MODEL OF
VIOLENCE PREVENTION 22 (2014).
341. See, e.g., McLeod, supra note 48, at 1227; Amna A. Akbar, Toward a Radical Imagination of Law, 93 N.Y.U. L. REV. 405, 431 (2018); THUSI, supra note 327, at 9.
342. Linda G. Mills, Briana Barocas & Barak Ariel, The Next Generation of Court-Mandated
Domestic Violence Treatment: A Comparison Study of Batterer Intervention and Restorative Justice
Programs, 9 J. EXPERIMENTAL CRIMINOLOGY 65, 65 (2013).
343. Jennifer L. Doleac, Encouraging Desistance from Crime, 61 J. ECON. LITERATURE 383,
413 (2023) (reporting that just one other study found reductions in crime, and then for just one
group of offenders, “but results were preliminary and did not include the full sample of participants”).
344. McLeod, supra note 48, at 1226.
345. Ryan Bort, Elisabeth Garber-Paul & Andrew Ward, The United States of Weed,
ROLLING STONE (Apr. 22, 2021), https://www.rollingstone.com/feature/cannabis-legalizationstates-map-831885 [perma.cc/XH79-TSH7].
346. E. ANN CARSON, U.S. DEP’T OF JUST., PRISONERS IN 2020 – STATISTICAL TABLES 28
tbl.14 (2021). Federal figures for simple possession are not available. Nevertheless, as the report
shows, states incarcerate far more people than the federal government. Id. at 7 tbl.2. And there is

860

Michigan Law Review

[Vol. 123:799

for sex work and other “quality of life” crimes. Only 6.2% of state prisoners’
most serious offenses were, “vice,” “decency,” or similar offenses. 347 The vast
majority of incarcerated persons in the U.S. are thus imprisoned for what are
commonly considered serious crimes—violent crimes (58.2%), 348 felony property offenses (15.3%), 349 and major drug crimes like trafficking (10.2%). 350
These seem like the kind of crimes about which even abolitionism-curious
voters continue to worry a great deal.
Thus, abolition via decriminalization would require freeing people who
have committed serious crimes and are likely to do so again. Ben Grunwald
has recently published the best analysis of this approach. 351 Grunwald evaluates various alternative programs for eliminating 25, 50, or 75% of incarceration. 352 One thing remains constant across all strategies analyzed: each would
increase crime, including serious crime, albeit to varying degrees. 353 Algorithmic Abolitionism is favorable, then, because decriminalization does not seem
like an alternative strategy that could satisfy voters’ twin aims of abolishing
incarceration without increasing crime.
C. Constitutional Constraints
Algorithmic Abolitionism raises multiple constitutional questions. Many
of these are well-canvassed in the existing literature on algorithms. What follows are a few brief thoughts on how Algorithmic Abolitionism, in particular,
fits into these extensive debates.
The first possible constitutional speedbump is Due Process. In 2016, the
Supreme Court of Wisconsin upheld the state’s use of the COMPAS tool in
criminal sentencing. 354 The defendant argued that, because that algorithm relied on statistical, rather than individual, data, its use violated his Due Process
right to an individualized sentence. 355 The Court disagreed, holding that algorithmic risk scoring was a way of arriving at accurate individualized determinations of relevant factors, including future crime risk. 356 Nevertheless, the
Court thought that, for sentences to be sufficiently constitutionally individualized, judges needed to be able to “disregard risk scores that are inconsistent
little reason to think that there are proportionally more federal prosecutions for simple possession than in the states. Indeed, commonsense notions of federal prosecutors handling fewer, but
more serious, crimes suggests the opposite.
347. Id. at 28 tbl. 14.
348. Id.
349. Id.
350. Id.
351. See generally Ben Grunwald, Toward an Optimal Decarceration Strategy, 33 STAN. L.
& POL’Y REV. 1 (2022).
352. Id. at 7.
353. Id. at 58.
354. State v. Loomis, 881 N.W.2d 749 (Wis. 2016).
355. Id. at 764.
356. Id. at 765, 767.

March 2025]

Abolition by Algorithm

861

with other factors.” 357 It thus suggested that, if Wisconsin stripped its judges
of discretion to ignore algorithmic recommendation, then that would violate
the Due Process Clause. 358
As described above, Algorithmic Abolitionist policies would need to give
algorithmic recommendations bite. Sometimes, but not always, this might
mean making them mandatory. The Wisconsin Supreme Court’s decision
casts doubt on the constitutionality of taking humans out of the loop entirely.
But it does not call less aggressive approaches into question. Moreover, this is
just one state supreme court decision, and there are good reasons to think that
it is wrong. Aziz Huq’s article-length argument that there is no constitutional
right to a human decision is the best treatment of the topic. 359 At most, Huq
contends, there might be a constitutional right to a well-calibrated algorithmic
decision. 360
In lieu of a full recapitulation of the arguments, here are a few quick highlights. The Wisconsin Supreme Court argued that, to satisfy Due Process, humans need to be able to step in and override algorithmic decisions they
deemed erroneous, given “other factors.” But the sophisticated machine-learning algorithms that would power Algorithmic Abolitionist policies already ignore “other” irrelevant factors, on a case-by-case basis. Unlike, say, an olderfashioned regression model, they do not assign the same weight to each fact
under every circumstance. Rather, their complex decision procedures are
highly context sensitive to interactions among all of the available information.
Moreover, humans regularly allow such “other” irrelevant factors—race, charisma, attractiveness, and more—to drive their decisions. It therefore seems
likely that keeping humans in the loop would sometimes worsen things, even
by the Wisconsin Supreme Court’s own lights.
Another potential constitutional hurdle for Algorithmic Abolitionism
comes from the line of U.S. Supreme Court cases that invalidated the mandatory U.S. Sentencing Guidelines. In United States v. Booker, the Supreme Court
held that the Sixth Amendment forbade mandatory increases to sentences “beyond the prescribed statutory maximum” based on facts found by a judge, not
a jury. 361 This dictate might again conflict with mandatory algorithmic sentencing—though not with other approaches to giving Algorithmic Abolitionism bite.
Moreover, even mandatory algorithmic sentences might be compatible
with Booker, if carefully designed. First, Booker forbids only upward mandatory departures based on facts not found by a jury. An Algorithmic Abolitionist
sentencing scheme could thus avoid the Booker problem by structuring itself

357. Id. at 764–65.
358. Id. at 774.
359. See generally Huq, supra note 136.
360. Id. at 619.
361. United States v. Booker, 543 U.S. 220, 227–29 (2005) (quoting United States v. Booker,
375 F.3d 508 (7th Cir. 2004)).

862

Michigan Law Review

[Vol. 123:799

around downward departures. The legislature might set a high default sentence for each crime and then mandate downward departures—up to and including no incarceration—for defendants with low recidivism risk. The Booker
Court itself suggested that such a scheme would be constitutional. It declined
to impose the scheme as a remedy in that case only because the Court thought
it incompatible with legislative intent. 362 A legislatively enacted Algorithmic
Abolitionist program would, obviously, not face that problem.
Moreover, Booker permits even upward sentence adjustments based on a
defendant’s criminal history. 363 The Kleinberg et al. algorithm, for example,
uses criminal history to make its predictions. 364 Other demographic information, like sex, number of dependents, or marital status, are matters of public
record and will thus generally be easy to prove beyond a reasonable doubt,
insofar as the defendant disputes them. Indeed, defendants could simply be
asked to admit such facts, since admissions also raise no Sixth Amendment
issue. 365 Such demographic admissions could be made a precondition of eligibility for an algorithmic downward variance described above. Essentially all
defendants would oblige, since there would be large potential benefits and no
downsides.
The prior constitutional questions were mostly relevant to Algorithmic
Abolitionist sentencing policies. What would the Constitution say about Algorithmic Abolitionist policing? The most obvious question here is whether the
Fourth Amendment would prohibit algorithmically directed searches and seizures. Street stops—whether initiated on the basis of human intuition or algorithmic prediction—may be constitutionally carried out only on the basis of
reasonable suspicion. 366 Insofar as reasonable suspicion is a measure of probability, the result is straightforward. Empirical analyses suggest that the vast
majority of such searches—initiated by humans—have a vanishingly small
probability of turning up any contraband. 367 Under Algorithmic Abolitionism,
the probabilities triggering a search would be much, much higher. 368 Thus, if
any non-trivial share of human-initiated searches are rightly upheld as constitutional, Algorithmic Abolitionist searches are, a fortiori, legal too.
Both Kiel Brennan-Marquez and Emily Berman have argued that Fourth
Amendment tests for reasonableness ought not rely on probability alone.369
362. Id. at 266. It is worth noting that the upward/downward characterization is basically
a distinction without a difference. But so was the remedy the Booker Court actually imposed:
Granting judges, rather than Congress, discretion to adjust sentences based on judge-found facts.
Id. at 245–46.
363. Id. at 227–28.
364. Kleinberg et al., supra note 132, at 239, 252.
365. Booker, 543 U.S. at 228.
366. Terry v. Ohio, 392 U.S. 1, 27 (1968).
367. See supra Section II.0.
368. See supra Section II.0.
369. See Kiel Brennan-Marquez, “Plausible Cause”: Explanatory Standards in the Age of
Powerful Machines, 70 VAND. L. REV. 1249, 1250 (2017); Emily Berman, A Government of Laws
and Not of Machines, 98 B.U. L. REV. 1277 (2018).

March 2025]

Abolition by Algorithm

863

They should instead require, they argue, a plausible explanatory narrative.
Brennan-Marquez argues that positive law is ambiguous on this point—plausibly endorsing a probabilities-only view. 370 But he contends that normative
considerations like antidiscrimination, fair notice, and oversight cut against
that reading and in favor of a more holistic one. 371
Much is correct in this account. But here are a few points in defense of
Algorithmic Abolitionist policing—if not of all policing algorithms. First, Algorithmic Abolitionism brings even more normative considerations into the
mix. Algorithmic Abolitionist policing would greatly reduce the burdens of
policing, especially for those who currently suffer them the most. These serious benefits must be weighed against the putative normative costs BrennanMarquez identifies. 372 Second, it is not even clear there is a normative tradeoff
at issue here. Brennan-Marquez’s enumerated values might be well-served by
certain well-designed Algorithmic Abolitionist policing policies. For example,
in making street stop recommendations, the Goel et al. algorithm assigns significant weight to factors—the presence of a suspicious object, the sight of
criminal activity—that look like explanatory reasons. 373 This directly serves the
value of fair notice. Antidiscrimination values are served when—as described
above—algorithms reduce bias as compared with the human status quo. Finally, algorithmic designers can be subjected to democratic oversight just as
police officers and their bosses can. The former is arguably easier. Algorithmic
training data and design strategies can be audited for compliance with best
practices, allowing detection of and consequences for gross deviations. By contrast, if a police officer lies to fabricate reasonable suspicion, that misbehavior
is comparatively difficult to detect, prove, and punish.
Finally, a note on Equal Protection. As noted above, it is possible—though
unlikely—that some Algorithmic Abolitionist policies could worsen bias in
prison or policing, as measured using existing tools. Such statistical disparities
would not be sufficient to raise an Equal Protection claim. For better or worse,
proving an Equal Protection violation requires proving that a government policy was enacted with discriminatory intent. 374 And if the policy was enacted
with the intent of reducing incarceration, including for vulnerable racial
groups, that would not qualify.
If the algorithm powering such a policy used race among its many input
variables, strict scrutiny would apply. 375 Then, the algorithm would have to
serve a compelling interest and be narrowly tailored to that interest. Here is
one way in which it might. First, excluding race as an input variable can often
have the unexpected effect of increasing algorithmic bias against minority

370.
371.
372.
373.
374.
375.

See Brennan-Marquez, supra note 369, at 1263–64.
See id. at 1276–97.
Id.
See Goel, Rao & Schroff, supra note 69, at 384.
Washington v. Davis, 426 U.S. 229, 239 (1976).
Parents Involved in Cmty. Schs. v. Seattle Sch. Dist. No. 1, 551 U.S. 701 (2007).

864

Michigan Law Review

[Vol. 123:799

groups. 376 Thus, including race might be the only way to serve the compelling
interest of avoiding discrimination. 377 And in situations where including race
did not improve accuracy and thereby reduce unfair disparities, it could
simply be dropped from the model.
D. Privacy and Surveillance
The literature on law, technology, privacy, and government surveillance
is massive. As with the prior thorny normative issues, this Section does not
seek to resolve higher-order debates. It does, however, situate Algorithmic
Abolitionism within them. It suggests that, as compared with other potential
uses of algorithms in public policy, the privacy and surveillance concerns here
are less dire.
Facial recognition technology powered by machine learning is, for example, now being used by the Chinese government. The goal appears to be building a surveillance system to track and log all citizens’ public movements at all
times. 378 Alternatively, machine learning can be used to infer private facts, even
when their subjects actively try to conceal them. 379 Consider, e.g., ad-serve algorithms that infer a woman’s pregnancy even before she has told her own
family. 380
These two worrisome examples illustrate the two ways in which machine
learning can help increase surveillance and reduce privacy. They can automate
the collection of data that, while public in some sense, could not previously be
aggregated at scale. They can also use data—including the data they help to
aggregate—to discover further, private facts that could not previously be discovered.
How do algorithmic abolitionist policies fit into these twin concerns?
Begin with data collection. Nearly all of the algorithms described above would
operate only on data that the government already routinely collects. Indeed,
that is why they exist in the first place. To train algorithms, you need existing
data. The algorithms discussed above consisted of public administrative records. Sentencing algorithms rely on the ordinary contents of a criminal record: sentence, arrest history, offense, age, and the like. 381 And the algorithm
for Terry stops uses exactly the same variables that police currently record as
their reasons for making stops today. 382

376. Talia B. Gillis, The Input Fallacy, 106 MINN. L. REV. 1175, 1229 (2022).
377. Cf. Salib, supra note 313, at 821.
378. Alfred Ng, How China Uses Facial Recognition to Control Human Behavior, CNET
(Aug. 11, 2020, 5:00 AM), https://www.cnet.com/news/politics/in-china-facial-recognitionpublic-shaming-and-control-go-hand-in-hand [perma.cc/2XRC-CQJQ].
379. Alicia Solow-Niederman, Information Privacy and the Inference Economy, 117 NW. U.
L. REV. 357 (2022).
380. Id. at 379.
381. Laqueur & Copus, supra note 18, at 156.
382. Goel, Rao & Schroff, supra note 69, at 383.

March 2025]

Abolition by Algorithm

865

Thus, these algorithms do not surveil at all, in the sense of automating the
collection of new raw data. But they do make inferences about facts, like
whether a person is likely to commit a crime or a geographic area is likely to
suffer from elevated crime. These facts might be considered private, in the
sense that the individuals they are about would prefer them to remain unknown. But this is unlike an algorithm’s exposure of an early stage pregnancy.
The reason is that our law does not usually treat facts about future crimes
as private. Consider, for example, the structure of the Fourth Amendment, a
privacy-protecting constitutional rule. 383 The Fourth Amendment protects the
privacy of “persons, houses, papers, and effects,” except if there is “probable
cause” to think that violating that privacy will reveal facts about a crime. 384 The
fact about the crime is not only non-private, but law affirmatively abrogates
some legitimate privacy interests to reveal it.
The exception to all of this, at least potentially, is Algorithmic Abolitionist
traffic enforcement. That policy relies on a new network of algorithmically enabled cameras. How does this compare, for example, to China’s facial recognition network? It is entirely up to us. Traffic enforcement cameras would not
need facial recognition and certainly would not need to track everyone’s location at all times. They would not need to make any record of their feeds at all,
saving only those brief snippets on which citations would be based. This would
entail some surveillance. But arguably less than the traffic officer on the side
of the road, who observes and can remember anything he sees during his shift,
not just the violations.
Perhaps merely building the camera network would inevitably lead to its
use in mass surveillance. After all, ubiquitous location tracking would surely,
for example, help to increase America’s shockingly low murder clearance
rate. 385 Such uses might be tempting. But they are not inevitable—or even necessarily constitutional. In 2018, the Supreme Court held that the Fourth
Amendment forbade law enforcement to use cell phone geolocation data as
such an on-demand location tracking system. 386 This holding does not guarantee a surveillance-minimalist implementation of Algorithmic Abolitionist
traffic enforcement. But it cuts against the possibility of a surveillance-maximalist approach.
Finally, it is important to emphasize that abolishing prison and police also
means abolishing status quo surveillance and privacy invasions. Prisoners are
subject to round-the-clock surveillance, with no privacy, and much of what
police do imposes the same costs. Significantly reducing both would be a huge
victory for privacy and civil liberties. True, Algorithmic Abolitionism might
intensify surveillance for some individuals—for example, habitual carriers of

383.
384.
385.

U.S. CONST. amend. IV.
Id.
Derek Thompson, Six Reasons the Murder Clearance Rate Is at an All-Time Low,
ATLANTIC (July 7, 2022), https://www.theatlantic.com/newsletters/archive/2022/07/policemurder-clearance-rate/661500 [perma.cc/4QD4-H644].
386. See Carpenter v. United States, 138 S. Ct. 2206, 2217 (2018).

866

Michigan Law Review

[Vol. 123:799

illegal weapons. But because of Algorithmic Abolition’s reductions in levels,
the net result would be to lift the burden of surveillance from many more people. Likewise, insofar as law enforcement would also wish to use these technologies to reduce crime somewhat, there is ample space for a positive-sum
deal.
CONCLUSION
This Article has proposed Algorithmic Abolitionism as a solution to an
extremely difficult problem. Really, it is two problems—the evils of crime and
the evils of policing and prison. The recent rise of prison and police abolitionism has made the latter problem more publicly salient than ever before. But it
has not made the dilemma more tractable. Until now, most available approaches have been distinctly unappetizing: One could—it seemed—either
eliminate police and prison and accept high costs from increased crime or instead preserve police and prison and accept the high costs that come with
them. Algorithmic Abolitionism is a third, more appealing, approach. It is a
way to radically reduce the high costs of prison and policing without generating additional costs from serious crime. Algorithmic Abolitionism is possible
today. And its normative risks are small, as compared with the upside. Thus,
this Article contends, we should all be Algorithmic Abolitionists.
