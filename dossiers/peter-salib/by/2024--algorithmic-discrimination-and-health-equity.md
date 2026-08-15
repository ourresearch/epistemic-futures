---
title: "Algorithmic discrimination and health equity"
person: peter-salib
section: by
type: book-chapter
year: 2024
venue: "Research Handbook on Health, AI and the Law (I. Glenn Cohen & Barry Solaiman, eds.), Edward Elgar Publishing, ch. 6"
authors: "Jessica L. Roberts & Peter Salib"
source_url: https://www.elgaronline.com/edcollchap-oa/book/9781802205657/ch06.xml
retrieved: 2026-08-13
content: full-text
notes: "Open-access chapter (CC BY-NC-ND 4.0), not closed as the previous pass recorded — Elgar serves it under the /edcollchap-oa/ path with a matching /downloadpdf/edcollchap-oa/.../ch06.pdf. Resolves the pending item listed under DOI 10.4337/9781802205657.00013 (duplicate OpenAlex record: 10.4337/9781800888548.00012). Text via pdftotext; Elgar's repeated per-page open-access watermark block was stripped."
---

# Algorithmic discrimination and health equity

## Full text

PART II
THE LEGAL CONSIDERATIONS
OF AI IN HEALTH

6.

Algorithmic discrimination and health equity
Jessica L. Roberts and Peter Salib

1.

INTRODUCTION

American healthcare is notoriously expensive,1 difficult to access2 and discriminatory.3 Thankfully, technology could reduce those costs and improve accessibility.4 Yet,
algorithm-based innovations – both in healthcare and beyond – also have the potential to
discriminate. If that discrimination mirrors social inequalities, health algorithms could replicate or even worsen existing health disparities.5 Examples of health disparities include poor
relative health,6 higher rates of disease,7 worse health outcomes,8 greater difficulty accessing

1
Roosa Tikkanen and Melinda K Abrams, ‘U.S. Health Care from a Global Perspective, 2019:
Higher Spending, Worse Outcomes?’ (The Commonwealth Fund, 30 January 2020) <https://​www​
.commonwealthfund​.org/​publications/​issue​-briefs/​2020/​jan/​us​-health​-care​-global​-perspective​
-2019> accessed 30 April 2024.
2
CDC, ‘Access to Health Care’ (Centers for Disease Control and Prevention, 18 August
2023) <https://​www​.cdc​.gov/​nchs/​fastats/​access​-to​-health​-care​.htm> accessed 30 April 2024.
3
Brandon M Togioka, Derick Duvivier and Emily Young, Diversity and Discrimination in
Healthcare (StatPearls Publishing 2023).
4
Dorey Scheimer, Meghna Chakrabarti and Tim Skoog, ‘Smarter Health: How AI is
Transforming Health Care’ (WBUR, 27 May 2022) <https://​www​.wbur​.org/​onpoint/​2022/​05/​27/​
smarter​-health​-how​-ai​-is​-transforming​-health​-care> accessed 30 April 2024.
5
The United States Department of Health and Human Services (HHS) defines a health disparity as ‘a particular type of health difference that is closely linked with social, economic, and/or
environmental disadvantage’. Office of Disease Prevention and Health Promotion, ‘Health Equity
in Healthy People 2030’ (Healthy People 2030) <https://​health​.gov/​healthypeople/​priority​-areas/​
health​-equity​-healthy​-people​-2030> accessed 30 April 2024.
6
See eg, Sofia Carratala and Connor Maxwell, ‘Health Disparities by Race and Ethnicity’
(Center for American Progress, 7 May 2020) <https://​www​.americanprogress​.org/​issues/​race/​
reports/​2020/​05/​07/​484742/​health​-disparities​-race​-ethnicity/​> accessed 30 April 2024; Lisa
I Iezzoni, ‘Eliminating Health and Health Care Disparities Among the Growing Population of
People with Disabilities’ (2011) 30 Health Affairs 1947; Hudaisa Hafeez and others, ‘Health Care
Disparities Among Lesbian, Gay, Bisexual, and Transgender Youth: A Literature Review’ (2017)
9(4) Cur eus 1.
7
See eg, Carratala and Maxwell (n 6); Robin Warshaw, ‘Health Disparities Affect Millions in
Rural U.S. Communities’ (AAMC, 31 October 2017) <https://​www​.aamc​.org/​news​-insights/​health​
-disparities​-affect​-millions​-rural​-us​-communities> accessed 30 April 2024; Hafeez and others (n
6).
8
See eg, Carratala and Maxwell (n 6); Warshaw (n 7); Norma Alicea-Alvarez and others,
‘Impacting Health Disparities in Urban Communities: Preparing Future Healthcare Providers for
“Neighborhood-Engaged Care” through a Community Engagement Course Intervention’ (2016) 93
Journal of Urban Health 732.

93

94

Research handbook on health, AI and the law

care,9 lower rates of health insurance10 and discrimination.11 The underlying reasons for
health disparities are complex and multifaceted, including a combination of biological, social,
environmental and behavioural factors.12 When algorithms discriminate, it threatens to worsen
these already problematic inequalities.
Unfortunately, in the United States, existing healthcare antidiscrimination laws will do
little to combat algorithmic discrimination. While federal law requires providers to offer
non-discriminatory healthcare, these obligations may not extend to developers who create
health technology. And even if they did, many of those laws do not reach unintentional discrimination, which algorithmic discrimination almost always is.13 Antidiscrimination law may
not then be a promising tool for reform in this area. We therefore propose a variety of policy
solutions to allow all Americans to benefit from health artificial intelligence (AI) and other
tools. And although we focus on the American healthcare and legal systems, we hope that our
recommendations will be useful in other jurisdictions facing similar challenges.
After this introduction, this chapter explores the potential health impacts of discriminatory
algorithms, with a focus on health disparities populations, in two sections. Section 2 describes
the possible sources of algorithmic bias and demonstrates how those technologies could create
or exacerbate health disparities. Section 3 turns to our novel policy solutions for addressing
algorithmic discrimination in healthcare.

2.

ALGORITHMIC DISCRIMINATION IN HEALTHCARE

When algorithms discriminate, it is not because they hold conscious invidious attitudes
toward members of disadvantaged groups. It is rather because of choices made by their human
creators. Certainly, if a person wanted to create an intentionally discriminatory algorithm,
they could. However, algorithmic discrimination is usually the result of human error. These
errors can take at least two forms: flawed algorithmic design and issues with the algorithm’s
training data.14 In this section, we explore four distinct but related sources of algorithmic
discrimination and consider their effect on healthcare access and delivery: (1) discrimination
from design; (2) discrimination from biased inputs; (3) discrimination from data deficits; and
(4) ‘discrimination’ from actuarially sound disparate impacts. The first is the result of poorly
9

See eg, UPMC, ‘What Are LGBTQIA+ Health Care Disparities’ (UPMC Health Beat, 27
January 2021) <https://​share​.upmc​.com/​2021/​01/​lgbtq​-health​-care​-disparities/​> accessed 30 April
2024; Iezzoni (n 6); Warshaw (n 7); Alicea-Alvarez and others (n 8); Jennifer Kates and others,
‘Health and Access to Care and Coverage for Lesbian, Gay, Bisexual, and Transgender (LGBT)
Individuals in the U.S.’ (KFF, 3 May 2018) <https://​www​.kff​.org/​report​-section/​health​-and​-access​
-to​-care​-and​-coverage​-lgbt​-individuals​-in​-the​-us​-health​-challenges/​> accessed 30 April 2024.
10 See eg, Carratala and Maxwell (n 6).
11 See eg, UPMC (n 9); René Bowser, ‘Racial Bias in Medical Treatment’ (2001) 105 Dickinson
Law Review 365; Lisa I Iezzoni and others, ‘Physicians’ Perceptions of People with Disability and
their Health Care’ (2021) 40 Health Affairs 297.
12 Office of Disease Prevention and Health Promotion (n 5).
13 See section 2.1 of this chapter.
14 Other authors have also distinguished these two broad categories of algorithmic bias. See
Ziad Obermeyer and others, ‘Algorithmic Bias Playbook’ (Centre for Applied AI at Chicago Booth
2021) 2.

Algorithmic discrimination and health equity 95
chosen proxies at the algorithm’s design stage. The second and third occur because of issues
related to the data used to train the algorithm. The fourth is, in fact, more a problem of biased
policies than biased algorithms.
2.1

Discrimination from Design

Health technologies created with the best of intentions can still inadvertently discriminate
because of flaws in their design. Those flaws can be the result of oversight if a human developer accidentally leaves something out.
But even carefully designed algorithms can have their shortcomings. One important category of design error is goal misspecification. Designing algorithms that predict or identify
requires reliable measures of the variables to be predicted. Often, such variables cannot be
measured directly, so developers must use proxies. Selecting a poor proxy at the design stage
can lead to misalignment between the goal of the algorithm and the results that it generates.
These mismatches can cause what one set of authors calls ‘label choice bias’15 – a disconnect
between what the algorithm should predict and what it actually predicts. In the context of
healthcare, selecting the wrong set of proxies may impact already vulnerable populations.16
Consider this example. Certain health systems, given their limited resources, rely on algorithms to identify patients who will benefit the most from extra healthcare.17 One such widely
used algorithm sought to identify and help patients with complex healthcare needs. But need
is difficult to observe directly, so the algorithm was designed to predict healthcare costs as
a proxy for healthcare need.18
However, many historically disadvantaged populations experience significant barriers
to accessing and paying for healthcare. The result is that those populations spend less on
healthcare, despite their equal or greater relative need. Thus, even if the algorithm predicts
healthcare costs perfectly, its use of cost as a proxy for health will incorrectly conclude that
disadvantaged patients are healthier than they actually are. Because of this incorrectly projected need, the health systems will, in turn, decline to offer more healthcare, even when those
patients could substantially benefit.
The authors of a 2019 study appearing in Science examined the racial impacts of one of
these algorithms.19 They found that using costs to approximate need reduced the number of
Black patients identified as requiring additional care by more than half.20 Thus, Black patients
– who already experience barriers to access, lower levels of relative health, and poorer health
outcomes – were systemically denied beneficial, additional care. These kinds of misalign-

15

ibid.
ibid; see also Jenna Wiens, W Nicholson Price II and Michael W Sjoding, ‘Diagnosing Bias
in Data-Driven Algorithms for Healthcare’ (2020) 26 Nature Medicine 25.
17 Ziad Obermeyer and others, ‘Dissecting Racial Bias in an Algorithm Used to Manage the
Health of Populations’ (2019) 366 Science 447, 447.
18 ibid 453.
19 ibid 447.
20 ibid.
16

96

Research handbook on health, AI and the law

ments, if far-reaching enough, could have a population-level impact, resulting in less access to
care relative to other patients with heightened medical needs.21
To remedy this error, the authors suggest reformulating the algorithm to no longer rely on
cost as a proxy for need.22 Instead, they used an index variable combining cost predictions with
health predictions.23 Their approach generated an 84 per cent decrease in the algorithm’s racial
bias.24 This result may not be typical, but such research can help guide other developers as they
attempt to avoid racially disparate outcomes.25
Goal misspecification can be understood as one species of the broader ‘alignment problem’
in AI.26 Humans want algorithms to help them make certain complex inferences, like health
assessments. But algorithms do not natively know what ‘health’ is. They instead need to be
taught. Algorithms learn by example, and the training examples must be clearly defined in
computer-readable data. Training a health-assessment algorithm thus requires many examples
of humans – or, really, data about humans – each labelled numerically according to relative
health.
‘Health’, however, is a nuanced and multidimensional concept. It is extremely difficult to
translate precisely into numerical, machine-digestible metrics. If any reader doubts this, we
challenge them to try to do it – even without numbers. Try to define a list of necessary and
sufficient conditions that captures all healthy people and excludes all unhealthy people. By
comparison, cost of care is easy to define and write as a number. Just drop the dollar sign!
The problem is that a health-scoring algorithm taught to conceive of health only in terms of
cost is highly misaligned. It gives substantially different results than the ones its creators really
want. And it does this because it was trained to identify a characteristic substantially different
from the ones humans really care about.
Algorithms are not the only ones susceptible to alignment problems. Humans are, too.
When speaking about human misalignment, we often talk in terms of ‘perverse incentives’
or ‘agency costs’.27 Indeed, one can easily imagine a hypothetical scenario in which human,
rather than machine, misalignment might produce exactly the bad algorithm just discussed.

21 It is possible that less access to care could also reduce relative health. However, the extent to
which an algorithm affects a health disparity is very context specific. For example, it is possible that
an algorithmic misalignment could be neutral towards disadvantaged groups, or even benefit them.
For example, it could have turned out that Black patients had on average higher costs of care than
white ones. This might happen if Black patients historically had much less access to preventative,
but not emergency or other high-stakes, care. Then, the health algorithm that distributed care to the
highest healthcare spenders would disproportionately benefit Black patients.
22 Obermeyer and others, ‘Dissecting Racial Bias in an Algorithm Used to Manage the Health
of Populations’ (n 17) 452–53.
23 ibid 453.
24 ibid.
25 ibid.
26 Peter N Salib, ‘Complex Algorithmic Law’ (The University of Chicago Law Review Online
Archive, 9 March 2022) <https://​lawreviewblog​.uchicago​.edu/​2022/​03/​09/​bp​-salib/​> accessed 30
April 2024.
27 Kathleen M Eisenhardt, ‘Agency Theory: An Assessment and Review’ (1989) 14 Academy
of Management Review 57, 57.

Algorithmic discrimination and health equity 97
Imagine a hospital that is struggling to achieve profitability.28 The hospital’s incentive for
profit may misalign with society’s goal of making people healthier. Suppose that the hospital’s
per-patient profitability declines as the patient’s total bill rises – perhaps because payors are
more likely to contest unusually large invoices. Here, the profit-maximising strategy involves
the early identification of those patients who would eventually receive expensive care and
the provision of preventative treatment to head off that eventuality. Hospital administrators
in this situation might – unlike those in the Science study – intentionally design an algorithm
that predicted future costs rather than future need for care. If they did, the reason would be
misaligned incentives.
Here is another observation about misalignment – both human and algorithmic. Even when
suboptimal, misalignment is not necessarily disastrous. Profit-motivated healthcare businesses
can produce lifesaving treatments. Likewise, the cost-focused algorithm in Science may, in
fact, have made people healthier, in that it directed additional care to some patients who needed
it. It may even have constituted a Pareto improvement over the status quo – making some
people healthier and no one less healthy than they previously were.29 But like a health-scoring
algorithm trained on health cost data, the humans’ incentives are not optimised for health, full
stop. They are instead optimised for health plus other financial goals.
Thus, discrimination rooted in algorithmic design is both foreign and familiar. The key
insight is that algorithms pursue only the goals that we set for them. If the goal is defined
imperfectly, errors result – and sometimes fall most heavily on already disadvantaged groups.
Properly specified goals can radically mitigate, if not eliminate, such problems. But to get
properly specified algorithmic goals, one first needs properly specified human ones.
2.2

Discrimination from Biased Inputs

Even algorithms with well-specified goals can discriminate when they rely on biased input
data. Training data must include information that algorithms can use to generate their outputs.
For an algorithm trying to calculate relative health, such data might include patient charts,
or information such as occupation and geography – all factors that correlate with a person’s
health. Biased inputs could be particularly harmful for health disparities populations who face
both stigma and social inequality.
Here, algorithms might learn to discriminate if the input data – as recorded by humans –
reflects human discrimination. Consider an algorithm trained to predict the presence of some
disease. Suppose that patient pain level was among the input features on which the algorithm
was trained, since pain is a symptom of the disease. Imagine the training dataset’s pain data
was drawn from patient charts labelled with doctors’ assessments of pain. Research shows
that doctors significantly underestimate the pain of women and people of colour, as compared
with white males with the same conditions who self-report the same levels of pain.30 If pain
28

For non-profit health systems, ‘profitability’ can be understood as revenues in excess of
costs, which allow the system to invest in additional care. See L Allen Dobson Jr, ‘Beware the
Trend of For-Profit Medicine’ (2021) 98(11) Medical Economics Journal 6, 6.
29 See Jules Coleman, ‘Review: The Normative Basis of Economic Analysis: A Critical Review
of Richard Posner’s The Economics of Justice’ (1982) 34 Stanford Law Review 1105, 1106–07.
30 Consumer Reports, ‘Is Bias Keeping Female, Minority Patients from Getting Proper Care for
their Pain?’ (The Washington Post, 29 July 2019) <https://​www​.washingtonpost​.com/​health/​is​-bias​

98

Research handbook on health, AI and the law

is a significant predictor of the target disease, an algorithm using such data may transpose
some of the doctors’ bias into its predictions. In other words, the algorithm has baked in the
pre-existing biases of physicians. As a result, the algorithm might fail to detect the disease in
women and people of colour more often, in part because of a downward bias in their recorded
pain. The algorithm would diagnose those individuals at lower rates and they would receive
less treatment, leading to worse health outcomes and lowering their relative health. This negative feedback loop could have compounding effects, making such individuals ineligible for
other care – for example, a transplant – requiring some minimum level of pre-treatment health.
The result is what one set of authors calls an ‘exclusion cycle’.31
Based on this example, it might seem that the algorithmic predictions would be just as
biased as the input data.32 But not necessarily. If the training data contained other reasonably
strong predictors of the disease, a sufficiently sophisticated algorithm might do the opposite.
It might learn that recorded pain was a strong disease predictor for only some of the patients
(for example, white men). It might thus adjust its decision function to ignore recorded pain for
women and people of colour and instead rely on other disease predictors for them. The algorithm might even combine weak disease predictors into a strong synthetic predictor, deployed
only for patients marked as female or non-white. The result might then be an algorithm that
de-biased itself and produced highly accurate results for all groups.33
Bias of this kind, when it exists, can be mitigated by ensuring that the variable of interest
– here, pain – recorded in the training data is accurate. Objective measures that do not rely on
human judgement could better avoid perpetuating bias. For example, researchers are investigating blood biomarkers for pain severity.34 If an algorithm relied on biomarkers in lieu of
physician assessments, it would not replicate the doctors’ biases. And algorithms themselves
could identify currently unknown objective indicators, such as a study that used machine
learning to demonstrate that traditional radiographic measures overlook certain factors that
contribute to knee pain in underserved populations.35 Yet, when clear, objective criteria
are unavailable, developers may still want to consider assessments that do not come from
physicians. Self-reports might, in some contexts, be more reliable than doctor assessments.36
Additionally, some algorithms might draw their input data from more than one source, say
by combining self-reports and doctor assessments. However, there is always the question
of whether each additional source increases or decreases accuracy. If self-reports are very

-keeping​-female​-minority​-patients​-from​-getting​-proper​-care​-for​-their​-pain/​2019/​07/​26/​9d1b3a78​
-a810​-11e9​-9214​-246e594de5d5​_story​.html> accessed 30 April 2024.
31 Ana Bracic, Shawneequa L Callier and W Nicholson Price II, ‘Exclusions Cycles:
Reinforcing Disparities in Medicine’ (2022) 377 Science 1158.
32 If this were the case, that would raise the question of harm. An algorithm that is equally
discriminatory as a human physician but more efficient might still represent an improvement over
the status quo.
33 Talia B Gillis and Jann L Spiess, ‘Big Data and Discrimination’ (2019) 86 University of
Chicago Law Review 459, 471–73.
34 Janice A Sabin, ‘Tackling Implicit Bias in Health Care’ (2022) 387 New England Journal of
Medicine 105.
35 Emma Pierson and others, ‘An Algorithmic Approach to Reducing Unexplained Pain
Disparities in Underserved Populations’ (2021) 27 Nature Medicine 136.
36 Of course, patients would need to engage in honest reporting.

Algorithmic discrimination and health equity 99
accurate and doctors less so, then diversification will reduce accuracy, on average. The policy
question is then: how can we enable algorithms to generate non-discriminatory outputs?
2.3

Discrimination from Data Deficits

Structural inequality can also bias algorithms through data deficits. Unfortunately, many
health disparity populations are also underrepresented in biomedical research.37 The National
Institutes of Health (NIH) has identified several currently underrepresented populations,
including Black, Hispanic and Indigenous people; individuals with mental and physical disabilities; and people from disadvantaged backgrounds.38 NIH defines people with disadvantaged backgrounds as individuals who meet two or more of the following criteria: were or are
homeless; were or are in the foster care system; qualify for certain federal income-based benefits; have no parents or legal guardians with a bachelor’s degree; or grew up in either a rural
area or a designated low-income and health professional shortage area.39 Yet, this correlation
is more than a mere coincidence. The failure to study diverse populations contributes to health
disparities by undermining the quality of care that these populations receive.40
The lack of representative data can result in algorithmic discrimination of another kind.
Algorithms trained on unrepresentative data may give accurate results only for those groups
for which sufficient data exists. For everyone else, the algorithm may simply be useless or
even harmful.
Polygenic risk scores, or PRS, offer an example of this phenomenon. A PRS is a number
that summarises a person’s estimated risk of a particular health outcome based on their genetics.41 PRS are based on statistical models, much like the algorithms already discussed. Like
those algorithms, they make their predictions by mining large sets of training data to uncover
statistical predictors of the target outcome. Here, the training data consists of genomic data
labelled as to whether those people experienced the relevant health outcome.42
However, PRS are unreliable for certain populations because of deficits in the training data.
Specifically, almost 80 per cent of the individuals included in the most common PRS training
datasets are of European descent.43 This percentage is significantly higher than the 61 per cent
37 W Nicholson Price II, ‘Medical AI and Contextual Bias’ (2019) 33 Harvard Journal of Law
& Technology 65, 107–10.
38 ‘Notice of NIH’s Interest in Diversity’ (National Institute of Health, 22 November 2019)
<https://​grants​.nih​.gov/​grants/​guide/​notice​-files/​NOT​-OD​-20​-031​.html> accessed 30 April 2024.
39 ibid.
40 Ashwarya Sharma and Latha Palaniappan, ‘Improving Diversity in Medical Research’ (2021)
7(74) Nature Reviews Disease Primers 1.
41 ‘Polygenic Risk Scores’ (National Human Genome Research Institute, 11 August 2020)
<https://​www​.genome​.gov/​Health/​Genomics​-and​-Medicine/​Polygenic​-risk​-scores> accessed 30
April 2024.
42 ‘Genome-Wide Association Studies Fact Sheet’ (National Human Genome Research
Institute, 17 August 2020) <https://​www​.genome​.gov/​about​-genomics/​fact​-sheets/​Genome​-Wide​
-Association​-Studies​-Fact​-Sheet> accessed 30 April 2024; ‘What are Genome-Wide Association
Studies?’ (MedlinePlus) <https://​medlineplus​.gov/​genetics/​understanding/​genomicresearch/​
gwastudies/​> accessed 30 April 2024.
43 Giorgio Sirugo, Scott M Williams and Sarah A Tishkoff, ‘The Missing Diversity in Human
Genetic Studies’ (2019) 177 Cell 25, 27–28; Alicia R Martin and others, ‘Clinical Use of Current
Polygenic Risk Scores May Exacerbate Health Disparities’ (2019) 51 Nature Genetics 584, 584.

100

Research handbook on health, AI and the law

of Americans who identify as white, and radically higher than the 16 per cent of the total global
population who are of European ancestry.44
The predictive value of the PRS generated from such homogenous training data is greatly
reduced for non-European populations.45 One study found that the accuracy of calculations
based on European data were significantly lower for other ancestral populations, decreasing
reliability by factors of 1.6 for people of Hispanic American and South Asian descent, 2.0 for
people of East Asian descent and a whopping 4.5 for people of African descent.46 If declines in
reliability are big enough, PRS may fail to provide any actionable information to members of
unrepresented groups. Unfortunately, this possibility is not merely conjecture. Three genetic
testing companies – Colour Genomics, Ambry Genetics and Myriad Genetics – sparked
controversy in 2018 when they rolled out products that only worked reliably for people of
European descent.47
It is worth noting that underrepresentation has been a longstanding problem for biomedical
research and dates back long before the integration of AI. And these deficits can matter a great
deal. Health conditions might progress differently in certain groups for both social and biological reasons. During the COVID-19 pandemic, people with intellectual and developmental
disabilities were as much as six times more likely to die from COVID-19 than individuals
without those disabilities.48 And Asian Americans tend to develop diabetes mellitus at lower
body weights than white Americans.49 Failing to study diverse populations might miss these
nuances in health risk. These failures can, in turn, affect the information that doctors use
to diagnose and treat their patients, leading to a reduction in the relative quality of care for
people in underrepresented populations. Algorithms create yet another opportunity for biased
healthcare. When algorithms base their assessments on unrepresentative health data, those
technologies will generate inaccurate results and recommendations, potentially lowering the
quality of care.
Here, the best solution is to collect more data on the underrepresented groups. The challenge, however, is that such data collection can be costly. Thus, the second-order policy question is how to design regulatory regimes that produce the most – and most broadly accessible
– health-promoting tools in the long run.
2.4

‘Discrimination’ from Actuarially Sound Disparate Impacts

Finally, algorithms sometimes generate accurate predictions that nevertheless appear biased
because the outcome in question occurs more frequently in a disadvantaged group. Consider an

44

Martin and others (n 43).
ibid 587.
46 ibid 586.
47 Antonio Regalado, ‘White-People-Only DNA Tests Show How Unequal Science Has
Become’ (MIT Technology Review, 18 October 2018) <https://​www​.technologyreview​.com/​2018/​
10/​18/​1980/​white​-people​-only​-dna​-tests​-show​-how​-unequal​-science​-has​-become/​> accessed 30
April 2024.
48 ‘Disability, Health Equity & COVID-19’ (National Institute for Health Care Management
Foundation, 14 Oct ober 2021) <ht t ps://​nihcm​.or g/​publ icat ions/​disabil it y​-heal t h​-equit y> accessed
30 April 2024.
49 Sharma and Palaniappan (n 40) 2.
45

Algorithmic discrimination and health equity 101
algorithm that calculates the chances that a patient will miss an appointment and double-books
the provider based on that likelihood to improve efficiency.50 Even if the algorithm does not
specifically take health disparity categories such as race into account, the algorithm may more
often flag members of one racial group as more likely to miss appointments than members of
other groups. That might be because individuals in those populations are more likely to miss
appointments – due to social and structural barriers such as a lack of transportation.51
This leads to a perverse set of outcomes. The algorithm’s double-booking of already disadvantaged patients’ appointments could reduce their quality of care by increasing wait times
and decreasing their time with the doctor.52 Thus, the presence of health disparities in the first
place opens the door for actuarially sound – yet nonetheless problematic – predictions. And
here again, inequality can compound.53 Having a negative experience with a rushed physician
might increase the likelihood of future no-shows.54 If performed at the population level, this
effort to improve efficiency could systematically harm already disadvantaged groups.55
It might be tempting to label this set of outcomes as ‘algorithmic discrimination’. But that
is not quite right. The problem here is not with the algorithm per se. Its predictions are accurate. The problem is instead with human systems, and it is twofold. First, structural inequality
within those systems generates barriers that lead to missed appointments, which the algorithm
merely identifies. Second, humans choose how to use the algorithm’s predictions, and they
often choose poorly. Double-booking predicted no-shows is only one way to deal with the
issue. Alternatively, providers could use the same algorithmic no-show predictions to offer
support and reminders to those patients, thereby improving their chances of showing up to
appointments.56 And even if they continued with the double-booking practice, they could mitigate the disparate burdens. When predicted no-shows showed up, they could commit to see
them first at their originally scheduled time. These alternative policies rely on exactly the same
algorithmic predictions as the problematic one, but they generate less worrisome results. Here

50

Michele Samorani and others, ‘Overbooked and Overlooked: Machine Learning and Racial
Bias in Medical Appointment Scheduling’ (2021) 24 Manufacturing & Service Operations
Management 2825.
51 American Hospital Association, ‘Social Determinants of Health Series: Transportation and
the Role of Hospitals’ (2017) Health Research & Education Trust 1, 4–9.
52 Samorani and others (n 50).
53 For a non-algorithmic discussion of how this reification process works in health insurance,
see Valarie K Blake, ‘Ensuring an Underclass: Stigma in Insurance’ (2020) 41 Cardozo Law
Review 1441.
54 Rebecca C Winokur and Tanuj K Gupta, ‘Algorithm Bias’ (American College of Healthcare
Executives, October 2020) <https://​www​.ache​.org/​blog/​2020/​the​-impact​-of​-gender​-and​-racial​-bias​
-on​-an​-algorithm> accessed 30 April 2024.
55 Of course, this will also depend on the specifics of the situation. If the algorithm is highly
accurate at predicting no shows, very few patients will be unexpectedly bumped. Moreover, there
will be increased supply, which could then create more scheduled slots. That supply increase could
actually make it easier for certain disadvantaged patients to access care.
56 Office of Disease Prevention and Health Promotion (n 5); for another take on how to reduce
racial unfairness in algorithmic medical scheduling, see Robert Shanklin and others, ‘Ethical
Redress of Racial Inequities in AI: Lessons from Decoupling Machine Learning from Optimization
in Medical Appointment Scheduling’ (2022) 35 Philosophy & Technology 1.

102

Research handbook on health, AI and the law

the policy solution for combatting inequality lies not in regulating what or how the algorithm
predicts but rather in how humans use those predictions.

3.

ENSURING NON-DISCRIMINATORY HEALTH AI

Section 2 laid out some of the health-related dangers of biased algorithms. However,
algorithm-based health technologies could have real, meaningful benefits. We should not,
therefore, completely discount these promising new innovations. Instead, we should take
steps now to ensure that the integration of algorithms and AI into healthcare is both just and
equitable.
At least in theory, Americans have legal rights to non-discriminatory healthcare. However,
the current law does not adequately address algorithmic discrimination. Thus, we need to
adopt creative policy solutions to ensure all Americans can benefit from the potential of new
health technologies.
3.1

Failure of Traditional Antidiscrimination Protections

Several federal antidiscrimination statutes apply to healthcare. Those laws prohibit covered
healthcare providers from discriminating based on race,57 sex,58 disability59 and age.60 And
some of those provisions, such as Section 1557, clearly apply to technology.61 However, the
extent to which they will adequately address the kinds of algorithmic discrimination discussed
in this chapter is unclear.
While current protections cover both individual and institutional healthcare providers, they
may not likewise extend to the entities that develop health AI. Some healthcare antidiscrimination statutes only reach federally funded entities.62 These provisions apply to a significant
number of healthcare providers because of Medicare and Medicaid,63 yet many providers do
not develop their own algorithms or health AI.64 And although third-party developers could be
57

42 USC §§ 18116(a), 2000(d) (United States).
ibid §§ 18116(a), 12112(a).
59 29 USC § 794; 42 USC §§ 12103, 18116(a) (United States).
60 29 USC § 623; 42 USC § 18116(a) (United States).
61 Section 1557’s regulations state that its protections extend to ‘information and communication technology’, which includes technologies that might rely on AI, such as software, websites and
applications. 45 CFR § 92.104(c) (United States).
62 See eg, 45 CFR § 92.2 (United States). The exception is Titles II and III of the Americans
with Disabilities Act (ADA) that apply to state and local government entities and public accommodations, respectively.
63 Office for Civil Rights, ‘Guidance to Federal Financial Assistance Recipients Regarding
Title VI and the Protection Against National Origin Discrimination Affecting Limited English
Proficient Persons – Summary’ (US Department of Health & Human Services, 26 July 2013)
<https://​www​.hhs​.gov/​civil​-rights/​for​-providers/​laws​-regulations​-guidance/​guidance​-federal​
-financial​-assistance​-title​-vi/​index​.html> accessed 30 April 2024.
64 For example, a provider may outsource certain kinds of testing. See eg, ‘MyRisk with
RiskScore’ (Myriad Genetics) <https://​myriad​.com/​myrisk/​riskscore/​> accessed 30 April 2024
(a third-party provider of PRS); however, some providers do develop their own technology. See W
58

Algorithmic discrimination and health equity 103
subject to product liability suits,65 they do not usually accept federal funding and, therefore, do
not have the accompanying antidiscrimination obligations. Without those requirements, they
may not prioritise equity over other concerns such as accuracy, affordability or efficiency.66
The result is that healthcare providers who want to offer algorithm-based services to their
patients may not have equitable options to choose from.67 Unfortunately, this situation could
put healthcare providers in the difficult position of deciding between offering potentially discriminatory technology or no technology at all.
Yet, even assuming that healthcare antidiscrimination laws would cover the developers of
health technology, those protections might still fall short. Remember that most algorithmic
discrimination is unintentional. Misalignment problems occur because of problematic proxies
and not a desire to discriminate. Likewise, when an algorithm uses biased or incomplete
training data, it is probably because – as in the case of PRS – that information is what is available, not because of discriminatory intent. Yet, many of the provisions that currently apply
to healthcare do not cover disparate impact discrimination.68 They would thus not extend to
much discriminatory health technology. And finally, some healthcare antidiscrimination laws
may in fact permit actuarially sound discrimination.69
To overcome these difficulties, Sharona Hoffman and Andy Podgurski have proposed
amending the current statutes to explicitly cover disparate impacts.70 We are pessimistic about
the prospects for this approach. First, the political economy is difficult. In recent years, the
courts have arguably contracted rather than expanded the scope of disparate impact liability

Nicholson Price II, Rachel E Sachs and Rebecca S Eisenberg, ‘New Innovation Models in Medical
AI’ (2022) 99 Washington University Law Review 1121, 1127–40, cataloguing development of AI
by nontraditional innovators including health systems.
65 Barbara J Evans and Frank Pasquale have recently argued that certain biased algorithms
subject to FDA regulation may give rise to product liability suits. See Barbara J Evans and Frank
Pasquale, ‘Product Liability Suits for FDA-Regulated AI/ML Software’ in I Glenn Cohen and
others (eds), The Future of Medical Device Regulation: Innovation and Protection (CUP 2021) 93.
66 For parallel arguments regarding the lack of accessible health tech for patients with disabilities, see Jessica L Roberts and Tiffany C Penner, ‘Innovating Accessible Health Care’ (2023)
University of Houston Law Center No. 2023-W-1 <https://​ssrn​.com/​abstract​=​4311277> accessed
30 April 2024.
67 ibid. While providers may have legal obligations to provide non-discriminatory healthcare,
those obligations have not translated into a perceived demand by developers to ensure that their tech
equally benefits all patients.
68 Title VI and the Age Discrimination Act do not cover disparate impact, and the extent to
which Section 1557 and the Rehabilitation Act cover it are up for debate. Alexander v Sandoval 532
US 275, 291–93 (2001); see Rumble v Fairview Health Services 2015 WL 1997415 (MN District
Court 2015); see CVS Pharmacy, Inc. v Doe 982 F 3d 1204 (US Court of Appeals 9th Cir 2020),
cert granted, 141 S.Ct. 2882 (2021), cert dismissed. (United States).
69 See Govind Persad, ‘Disability Law and the Case for Evidence-Based Triage in a Pandemic’
(2020) 130 Yale Law Journal Forum 26.
70 Sharona Hoffman and Andy Podgurski, ‘Artificial Intelligence and Discrimination in
Healthcare’ (2020) 19 Yale Journal of Health Policy, Law, and Ethics 1, 34–36.

104

Research handbook on health, AI and the law

under statutes where it is currently recognised.71 And thus far, Congress has done nothing to
push back.
Second, even under robust disparate impact approaches, a defendant may escape liability by
demonstrating that the offending policy was needed to serve a legitimate purpose. Under Title
VII, for example, a defendant may escape liability by demonstrating that the policy creating
the disparity was a ‘business necessity’.72 While this may sound like a high bar to clear, it is
not – especially in the context of AI. To constitute a business necessity, the disparity-inducing
program need only ‘be predictive of or significantly correlated with important elements of
[business function] which comprise or are relevant to the job or jobs for which [the program is]
being evaluated’.73 Title VI, which prohibits discrimination in certain healthcare settings, has
a similar defence.74 All of the potentially biased algorithmic design choices discussed above
retain at least a predictive correlation with the algorithm’s intended function. All such correlations are imperfect, and some are biased. But choosing, for example, training data uncorrelated
with the algorithm’s legitimate function would produce an algorithm completely useless to its
creator. Thus, essentially all algorithms challenged via a traditional disparate impact approach
could escape liability.75
3.2

Policy Solutions

What, then, can be done to prevent algorithmic discrimination from becoming pervasive in
healthcare? We offer three alternative regulatory solutions. Each solution is tailored to one
or more of the four distinct varieties of algorithmic discrimination discussed above: (1) discrimination from design; (2) discrimination from biased inputs; (3) discrimination from data
deficits; and (4) ‘discrimination’ from actuarially sound disparate impacts.
3.2.1
Big data affirmative action
Our first solution, big data affirmative action, can address both discrimination from design and
discrimination from biased inputs. Begin with discrimination that results from misalignment
between human and algorithmic goals. Consider again the example of an algorithm intended to
diagnose or predict a particular disease. To accomplish that task, the algorithm must be trained
using data from many patients, who have been labelled as having the disease or lacking it.
Presence or absence of a disease may at first seem directly observable, such that misalignment
is unlikely. Unfortunately, the reality is far more complex. Some diseases can be observed
more or less directly, as with cancer biopsies.76 For conditions where relatively direct obser-

71

See Texas Department of Housing & Community Affairs v Inclusive Communities Project,
Inc. 576 US 519 (2015); Wal-Mart Stores, Inc. v Dukes 564 US 338 (2011) (United States).
72 42 USC § 2000e-2(k)(1)(A)(i).
73 Albemarle Paper Co. v Moody 422 US 405, 431 (1975) (United States).
74 Larry P. v Riles 793 F 2d 969, 983 (US Court of Appeals 9th Cir 1984) (no liability if defendant can show a ‘legitimate discriminatory reason’ for the challenged policy) (United States).
75 Anya ER Prince and Daniel Schwarcz, ‘Proxy Discrimination in the Age of Artificial
Intelligence and Big Data’ (2020) 105 Iowa Law Review 1257, 1305 (explaining that ‘disparate
impact liability (as it is currently constructed) is simply not capable of effectively policing against
proxy discrimination by AIs’).
76 Of course, even biopsies are not perfect predictors of disease.

Algorithmic discrimination and health equity 105
vation is possible, using those reliable observations in the training data minimises the risk of
misalignment. Of course, if only certain patients have access to biopsies, that inequality could
create a data deficit problem,77 but that is a separate issue from misalignment.
But for other diseases – including many psychological disorders – nothing approaching
direct observation is currently available. Then, training data will have to rely on less reliable
proxies for actual disease. For psychological disorders, that proxy will often be a doctor’s
judgement regarding the presence or absence of a condition. The result can be a mismatch
between actual disease and recorded disease diagnoses. And indeed, non-white Americans
are systematically under-diagnosed, for example, with depression and anxiety.78 This type of
misalignment functions similarly to the second source of algorithmic discrimination: biased
input data. Recall the pain levels example discussed above. The problems resulting from goal
misspecification and from biased data both flow from mismatches between the information
available to the algorithm and the truth about the variables of interest.
We suggest that, here, more algorithms can address both variations of algorithmic discrimination. As one of us has argued elsewhere, a second algorithm could correct bias by adjusting
the first’s decisions.79 To achieve this, the correction algorithm is trained not to predict disease
but to measure discriminatory error in the first algorithm’s predictions. This is generally
accomplished using interpretable statistical models such as regression analyses, rather than
cutting-edge machine learning models. Once a correction algorithm has quantified the bias
in the first algorithm’s outputs, the former can be used to automatically correct the latter’s
errors.80
Corrective algorithms of this kind amount to a form of automated affirmative action.81 This
means that they can be implemented as a matter of policy by private institutions – including
health tech companies, hospitals, industry groups – without the need for government action.82
As long as the corrective algorithm is well calibrated to correcting only actual discrimination
that would otherwise be caused by the decision algorithm, such private remediation of inequality is legally allowed.83

77

Not all patients with cancer will be biopsied, and the choice is not random. Instead, it will be
patients who have better access to healthcare whose health records will include a biopsy result in
the first instance.
78 Blue Cross Blue Shield Association, ‘Racial Disparities in Diagnosis and Treatment of Major
Depression’ (Blue Cross Blue Shield Association, The Health of America Report 2022).
79 Peter N Salib, ‘Big Data Affirmative Action’ (2022) 117 Northwestern University Law
Review 821.
80 ibid. This approach is distinct from attempts to explain uninterpretable AI decisions by
imposing an interpretable model on top of an uninterpretable one. See Boris Babic and others,
‘Beware Explanations from AI in Healthcare: The Benefits of Explainable Artificial Intelligence
Are Not What They Appear’ (2021) 373 Science 284. Big Data Affirmative Action models do not
offer an explanation of the uninterpretable model’s decision procedure. Rather, they offer a rough
estimate just of the influence of one invidious factor – and correct it.
81 ibid.
82 ibid.
83 ibid.

106

Research handbook on health, AI and the law

3.2.2
Increasing data to address data deficits
We can now move to data deficits. Recall that PRS are not reliable for people of non-European
descent because of Eurocentric training data. Beyond PRS, unrepresentative research populations also cause differential drug efficacy by race, gender and socioeconomic class.84
Moreover, such differences are often under-studied.85 The regulatory solution is, therefore,
facially straightforward: researchers must collect more and more representative data.
When and how should such requirements be imposed? We posit that a primary cause of data
disparities is cost. Consider that white Americans access healthcare at higher rates.86 There are
thus fewer opportunities for healthcare providers to obtain samples from patients of colour or
to recruit them for research. Moreover, members of racial minority groups – including Black
Americans – may be less trusting of medical professionals.87 And, of course, they have good
reason not to trust. American medical history reveals an array of horrifying episodes in which
medical researchers experimented on Black subjects without their consent, often with tragic
results.88
Given these realities, the incentives for private companies developing health technologies
are clear. Collect comparatively cheap data from individuals of European descent to create
accurate tools for that large market. Other groups can wait, maybe indefinitely. And while
some companies sell directly to consumers, the failure to create products that benefit diverse
populations represents more than just a lost share of the market. Providers may integrate these
unequal technologies into clinical care, and other entities – such as the government – may be
interested in the data.89
Well-designed regulations could push biotech companies to undertake the necessary
costs to ensure that everyone can use their products. We propose the following framework.
Companies and researchers should continue to innovate. In cases where diverse training data
is not available and obtaining adequately representative data would generate a significant
delay, the product could go to market as soon as it was sufficiently useful for enough people
to create demand. But then the clock should start ticking. For any product that works for one
population, the manufacturer should have limited time to collect the necessary data to make
the tool work – and work well – for other populations, especially disadvantaged ones. If the
manufacturer fails to achieve this outcome within the required period, a serious penalty, such
84

Donna H Odierna and Lisa A Bero, ‘Systematic Reviews Reveal Unrepresentative Evidence
for the Development of Drug Formularies for Poor and Nonwhite Populations’ (2009) 62 Journal
of Clinical Epidemiology 1268.
85 ibid.
86 David C Radley and others, ‘Achieving Racial and Ethnic Equity in U.S. Health Care:
A Scorecard of State Performance’ (The Commonwealth Fund, 18 November 2021) <https://​doi​
.org/​10​.26099/​ggmq​-mm33> accessed 30 April 2024.
87 See Kayte Spector-Bagdady and others, ‘Respecting Autonomy and Enabling Diversity: The
Effect of Eligibility and Enrollment on Research Data Demographics’ (2021) 40 Health Affairs
1892.
88 Office of Science, ‘The Syphilis Study at Tuskegee Timeline’ (Centers for Disease Control
and Prevention, 5 December 2022) <https://​www​.cdc​.gov/​tuskegee/​timeline​.htm> accessed 30
April 2024.
89 On integrating such technologies into clinical care, see Stacey Pereira and others, ‘Psychiatric
Polygenic Risk Scores: Child and Adolescent Psychiatrists’ Knowledge, Attitudes, and Experiences’
(2022) 189 American Journal of Medical Genetics 293.

Algorithmic discrimination and health equity 107
as pulling the product from the market, would be imposed. This is just a high-level sketch
of a policy. It leaves important questions unresolved, including how to define the relevant
populations, how to measure equal effectiveness, how to set the time limit for achieving such
equal effectiveness across products, who should enforce the policy and whether a defence of
impossibility or extreme impracticability should be available.
This approach has several virtues. First and foremost, it allows useful products to go to
market as soon as they are available. This aspect has intrinsic value, but also instrumental,
equity-promoting value. An alternative regulatory scheme might demand universal effectiveness before any product could be sold at all. Yet, imposing that restriction could substantially
increase the start-up capital – and thus financial risk – needed to develop new health technologies. The result would be fewer innovations for everyone – including vulnerable populations
who are often most at risk.
By contrast, allowing products to go to market immediately generates a mechanism by
which all the best products rapidly become available. High-value technologies could quickly
generate the free cash flow needed to fund research on underrepresented populations. The
products that turned out to have little market value would quickly die off, being unable to generate the revenues necessary to expand their availability within the allotted time. No great loss.
We acknowledge that this approach initially appears unfair to members of unrepresented
groups – at least during the regulatory expansion window. During that period, new technologies would be made available to some people but not others. Consider, however, that
a regime demanding universal availability before initial approval would, at a minimum, delay
the availability of tools for everyone while the necessary samples were collected. Thus, this
approach would be unlikely to result in earlier access for underrepresented groups. Indeed,
access would likely be slower under that approach. Under it, funds needed to collect missing
data would often have to be sought from outside funders rather than flowing directly from the
company’s own revenue.
Our approach is, of course, not the only one that could increase data representativeness
without stunting innovation. W. Nicholson Price has proposed, for example, that governments
could invest directly in such data collection and make it available for the public good.90 Such
public investment would be a welcome compliment to the private incentive structure we
propose.
One unique feature of our approach is that the individuals who benefit from early availability would pay a kind of ‘privilege tax’ in exchange. They would pay higher prices for
the initial product so that developers could cover the costs of collecting additional data from
underrepresented populations. Those additional costs would not merely be used to expand the
availability of the technology that would have existed anyway. As discussed, the availability
of free cash flows from early market entry would, in effect, be funding the creation of products
that, under the alternative regulatory framework, would not have existed at all. The result
would be a set of monetary transfers from highly represented to underrepresented groups,
mitigating concerns about unfairness.
Our approach has another advantage over alternatives for overcoming data deficits: flexibility. Other scholars of fairness in health technology sometimes favour command-and-control
rules for promoting equity. Hoffman and Podgursky, for example, suggest that plans for

90

Price II (n 37).

108

Research handbook on health, AI and the law

data collection and algorithmic design be subject to review by committees of stakeholders.91
Community input of that kind might sometimes be useful in overcoming the hurdles to collecting representative data. But sometimes, it might not. In some contexts, stakeholder review
means more veto points and bigger holdout problems. It is hard to know in advance which contests are which. Our approach places the burden of equal access on the companies who wish
to profit from algorithmic predictions. They must provide universal access to their products by
any means necessary, or else go extinct.
Finally, our suggested regulatory approach has the advantage of feasibility. Proof of concept
already exists. Following the backlash to its ‘Europeans-only’ rollout of its breast cancer PRS,
Myriad Genetics partnered with researchers at the Cleveland Clinic to expand access.92 Myriad
re-calibrated the test on data from 275,000 additional women – presumably including many
from previously underrepresented ancestry groups.93 The test is now available to ‘any and all
interested women’.94 If Myriad could parlay the initial success of a valuable, but limited-use,
PRS into a valuable PRS for all, others could too.
Our approach might also benefit drug development. Consider the rush to develop COVID-19
vaccines at the beginning of the pandemic. Getting a drug to market quickly was a matter of
public health. However, clinical trials require participants. During its effort to obtain swift
FDA approval, Moderna garnered criticism for failing to recruit diverse participants for its
clinical trials.95 Our proposal would balance the interest in timely access to drugs with a need
for greater representation in clinical trials. Here again, regulators could require manufacturers
of drugs approved for general sale using data from unrepresentative clinical trials to ensure
that their drugs are effective for diverse populations. These regulations could require drug
manufacturers to gather data, within a given timeline, showing the effectiveness of their drug
in other populations. If that research demonstrates a lack of efficacy for certain groups, drug
manufacturers could be required to take reasonably available steps to rectify the disparity.96 Of
course, drug development raises different legal, ethical and social issues than other technologies. Thus, regulators may only want to apply this approach to drug development in situations
where time is of the essence. Importantly, we do not intend our approach to create a perverse
incentive for drug manufacturers to bypass the issue of diversity in clinical trials, go to market
and then attempt to fix the issue in post. However, drugs with unrepresentative clinical trials
91

Hoffman and Podgurski (n 70).
Myriad Genetics, ‘Myriad Genetics Expands Access to Genetic Testing with Launch of
First Polygenic Breast Cancer Risk Assessment Score Validated for Women of All Ancestries’
(GlobeNewswire, 2 August 2021) <https://​www​.globenewswire​.com/​en/​news​-release/​2021/​08/​
02/​2272709/​15459/​en/​Myriad​-Genetics​-Expands​-Access​-to​-Genetic​-Testing​-with​-Launch​-of​
-First​-Polygenic​-Breast​-Cancer​-Risk​-Assessment​-Score​-Validated​-for​-Women​-of​-All​-Ancestries​
.html> accessed 30 April 2024.
93 ibid.
94 ibid.
95 Megan Cerullo, ‘Moderna Vaccine Trial Lacks Black, Latinx and Indigenous Participants’
(CBS News, 25 August 2020) <https://​www​.cbsnews​.com/​news/​covid​-vaccine​-moderna​-trial​
-lacking​-black​-latino​-asian​-native​-volunteers/​> accessed 30 April 2024.
96 What counts as reasonable will vary by context. Drug makers could certainly explore alternate dosing or treatment regimens. But it is not clear that they could, for example, discover new
drugs guaranteed to work for all groups. Thus, demanding that they do on penalty of having the old
drugs pulled from the market would quite likely result in fewer drugs for everyone, not more.
92

Algorithmic discrimination and health equity 109
regularly go to market as it is. Our proposal would, therefore, require more, not less, of drug
manufacturers in many contexts.
3.2.3
Regulating harmful, but actuarially sound, discrimination
This leads us to the final kind of algorithmic discrimination: the potential ill effects of
accurate, though unequal, algorithmic results. Again, we do not view this as a concern about
algorithmic discrimination at all. Rather, if discrimination is going on, it is at the level of individual or collective human decisions. Remember the algorithm used to predict likely no-shows
and double-book those patients. That algorithm had the unfortunate effect of double-booking
disproportionately more patients of colour, leading to a disparate impact. However, as we note
above, double-booking is only one way to use predictions of likely no-shows. Alternatively,
the algorithm could be told to send reminders to those individuals. In cases of actuarially sound
discrimination, the problem is not correct predictions of the algorithm but rather the socially
problematic use of those predictions by humans. Thus, accurate yet disparate algorithmic predictions only cause trouble if they are used to the disadvantaged group’s detriment.
In some cases, that use would constitute intentional disparate treatment by a human and
be actionable as discrimination. For example, the law likely already offers some protection against discrimination based on PRS in certain situations.97 The Genetic Information
Nondiscrimination Act (GINA) prohibits discrimination based on genetic information in
health insurance and in employment. Assuming GINA applies, health insurers could not use
PRS in underwriting or rating decisions. However, GINA does not cover a wide range of
potentially discriminatory conduct. For example, genetic discrimination in education, lending,
housing, and (most important to this chapter) healthcare is still legally permissible in most
states.98 Moreover, GINA confines its protections to statutorily defined genetic information,
leaving discrimination based on other kinds of health data unregulated.99 Thus, increased antidiscrimination protections for PRS and other kinds of sensitive health data might be necessary.
There will be hard policy questions to answer here about what constitutes bad discrimination and what constitutes good personalisation in healthcare. For example, a doctor’s denial
of treatment based on an algorithmic prediction might sometimes (counterintuitively) be
the latter. This outcome could occur if an algorithm made a high-certainty individualised
prediction that a proposed treatment would not help the patient and would have serious side
effects. Similarly, one could make the argument that GINA’s prohibition on actuarially sound
differentiation in insurance premiums generates inefficient cross-subsidies between insured
parties. In both cases, it is up to lawmakers to decide what trade-offs to make in regulating
how humans use algorithms.

97

Genetic Information Nondiscrimination Act of 2008, 122 Stat. 881, 885, 890, 898, 901, 906
(defining the term ‘genetic information’) (United States). While not traditional genetic tests, this
definition may well extend to PRS.
98 The major exception is California, which has a very broad genetic discrimination law. The
California Genetic Information Nondiscrimination Act of 2011, SB 559, Reg Sess, 2011 Cal Stat.
99 See, generally, Elizabeth Weeks and Jessica L Roberts, Healthism: Health-Status
Discrimination and the Law (CUP 2018).

110

4.

Research handbook on health, AI and the law

CONCLUSION

Technology has many potential advantages for improving healthcare. But any integration
of algorithms and AI must ensure that it does not inadvertently lead to discrimination. Left
untouched, algorithmic discrimination could harm patients, including those who already experience health disparities. Here, we have considered the potential for algorithmic discrimination
in healthcare and have offered some possible solutions.
Importantly, as we have illustrated, there are no one-size-fits-all answers. Multiple distinct
problems are routinely discussed under the single heading of ‘algorithmic discrimination’.
These different problems have different sources, and they raise different threats of harm.
Regulatory solutions must be attentive to these differences or risk making things worse. Our
hope is that these examples will serve as a starting point – not an end point – for regulators
thinking about algorithmic discrimination in healthcare more generally.
