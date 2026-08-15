---
title: "Generative AI To Recognize Response Fabrication in PTSD"
person: james-evans
section: by
type: journal-article
year: 2024
date: 2024-04-23
venue: "Research Square"
authors: "Ishanu Chattopadhyay, Royce Lee, James Evans, Michael Brook, Robert Gibbons"
source_url: https://doi.org/10.21203/rs.3.rs-4289440/v1
openalex_id: https://openalex.org/W4395046525
retrieved: 2026-08-13
content: full-text
notes: "preprint version; full text via the OpenAlex Content API (content.openalex.org)"
---

# Generative AI To Recognize Response Fabrication in PTSD

## Full text

Generative AI To Recognize Response Fabrication in
PTSD
Ishanu Chattopadhyay

University of Chicago https://orcid.org/0000-0001-8339-8162
Royce Lee
University of Chicago
James Evans
University of Chicago and Santa Fe Institute https://orcid.org/0000-0001-9838-0707
Michael Brook
Northwesterm Medicine
Robert Gibbons
University of Chicago

Article
Keywords:
Posted Date: April 23rd, 2024
DOI: https://doi.org/10.21203/rs.3.rs-4289440/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License
Additional Declarations: There is NO Competing Interest.

1

Generative AI To Recognize Response
Fabrication in PTSD
Ishanu Chattopadhyay✶❀✹❀✻⋆ , Royce Lee✷ , James Evans✸❀✹ , Michael Brook✼ , and Robert Gibbons✶❀✹❀✺❀✻
✶ Department of Medicine, University of Chicago, Chicago, IL 60637, USA
✷ Department of Psychiatry, University of Chicago, Chicago, IL 60637, USA
✸ Department of Sociology, University of Chicago, Chicago, IL 60637, USA

✹ Committee on Quantitative Methods in Social, Behavioral, and Health Sciences, University of Chicago,

Chicago, IL 60637, USA

✺ Department of Public Health Sciences, University of Chicago, Chicago, IL 60637, USA
✻ Center for Health Statistics, University of Chicago, Chicago, IL 60637, USA
✼ Feinberg School of Medicine, Northwestern University, Chicago, IL 60611, USA
⋆

To whom correspondence should be addressed: e-mail: ishanu@uchicago.edu.

Abstract: Fabricating symptoms of Post-Traumatic Stress Disorder (PTSD) can hinder accurate clinical
assessments via structured diagnostic interviews 1,2 . Symptom simulation or fabrication is a known
problem 3,4 in PTSD assessments, with diverse motivations including unmet mental health issues, varied
socio-economic factors and the potential for external gain from positive diagnoses. Here we introduce
an artificial intelligence (AI) framework referred to as Algorithm VeRITAS (Vetting Response Integrity
from cross-Talk in Adversarial Surveys), for detecting symptom fabrication in the context of PTSD
diagnosis. In contrast to current approaches to fabrication detection which indirectly assess atypical
symptom presentations, and have limited reliability, VeRITAS infers statistical dependencies inherent in
true response patterns, flagging responses which violate these subtle constraints. With a study sample
of ♥
patients, VeRITAS has an Area Under the Curve (AUC) of ≧ ✿ ✝ ✿ , with sensitivity
❃
, specificity ❃
, and positive likelihood ratio between ✿
✿
. Additionally, VeRITAS is
difficult-to-impossible to beat with coaching or training; we demonstrate that having advanced training
in mental health diagnosis is not helpful in defeating the algorithm. Our tool offers an objective, diseasespecific, fast (average time ≦ min) detection of simulated or feigned PTSD, and on wider adoption,
can potentially help resources and disability concessions reach those genuinely in need, while helping
to maintain integrity of clinical data. Moreover, reliably identifying patients who might be fabricating
symptoms due to unmet mental health needs or socio-economic compulsions can ultimately improve
outcomes in disadvantaged communities.

❂ ✻✺✶
✾✺✪

✵ ✾✺ ✵ ✵✷
✾ ✾ ✶✾ ✼✼

✽✽✪

✹

I NTRODUCTION
Accurate psychiatric diagnosis is a core component of mental health research and practice 5 . It allows for
replicable empirical investigation into the epidemiology of mental disorders, and for ethical and equitable dissemination of evidenced based treatments. Because no reliable biological markers have been identified for most
mental health diseases, diagnosis and measurement of severity of psychiatric disorders rely on self-reported
symptoms, often using standardized questionnaires that ask individuals to rate the frequency and/or severity
of their symptoms 6 . However, as has been extensively documented, symptom rating scales are susceptible
to a number of responder biases including symptom exaggeration and fabrication 1,2,7 . Non-credible symptom
reporting can have varied motivation; when incentivized by secondary gain it is referred to as malingering. Factors
related to unmet health or socio-economic needs may also drive such response patterns. Posttraumatic Stress
Disorder (PTSD) is particularly relevant to the investigation of feigned symptomatology, since in PTSD subjective
stressors coupled similarity in presentation, relative ease of access to information on how to feign symptoms, and
financial incentives related to a positive diagnosis in legal procedures or disability claims incentivizes deception 8 .
Notwithstanding the motivation behind symptom fabrication, there is a need for tools enabling identification of
true PTSD 9 .
Despite the general difficulty in formulating principles to detect fabrication 10 , multiple standardized tests 11,12 ,
validity assessment tools 13 have been proposed, with limited success. These tools typically involve scales
(“lie scales”, some dating back to the Minnesota Multiphasic Personality Inventor (MMPI) 14 ) and assess the
endorsement of “atypical” symptoms (✐✿❡✿, symptoms that are rarely endorsed by individuals with verified genuine
psychopathology) or ask similar or related questions multiple times to verify consistency, and provide only
indirect assessment of symptom fabrication 12,15–17 , are vulnerable to coaching 18 , and can yield unacceptable
false positive rates in individuals with genuinely severe psychopathology 19 .

TABLE 1: Demographic Characteristics and Fabrication Success Rates (PL Dataset)❄ at 94.2% sensitivity
characteristics
Race: Asian
Race: Black
Race: Mixed
Race: Other
Race: White
Sex: Female
Sex: Male
Residence: United Kingdom
Residence: United States
All participants

mean Completion
Time [s]
188.4
329.5
195.8
286.2
186.5
201.5
213.5
213.5
202.9
206.6
❄

mean age
[years]
34.3
38.0
31.4
38.5
42.7
40.5
41.0
43.1
39.4
40.7

no. of
participants
24
33
20
13
220
167
141
110
200
310

fabrication success
rate (%)
8.3
18.2
5.0
0.0
4.1
4.8
7.1
4.5
6.5
5.8

Using ✔✵ ❂ ✶❀ ✗✵ ❂ ✵✿✼✻❀ ✖✵ ❂ ✶✿✸✺.

TABLE 2: Lower Bounds on Performance trade-offs at Different Population Prevalences of PTSD Symptom Fabrication②
prev.
0.15
0.20
0.25
0.30

sensitivity

✵✿✾✸✵✝✵✿✵✶✹
✵✿✾✹✷✝✵✿✵✶✷
✵✿✾✹✽✝✵✿✵✶✷
✵✿✾✺✻✝✵✿✵✶✵

specificity
0.95
0.93
0.91
0.88

ppv

✵✿✼✼✼✝✵✿✵✵✸
✵✿✽✸✶✝✵✿✵✵✷
✵✿✽✻✽✝✵✿✵✵✷
✵✿✽✾✹✝✵✿✵✵✶

npv

✵✿✾✽✼✝✵✿✵✵✷
✵✿✾✽✹✝✵✿✵✵✸
✵✿✾✽✶✝✵✿✵✵✹
✵✿✾✼✾✝✵✿✵✵✹

acc

✵✿✾✹✾✝✵✿✵✵✷
✵✿✾✹✽✝✵✿✵✵✸
✵✿✾✹✼✝✵✿✵✵✸
✵✿✾✹✺✝✵✿✵✵✹

LR+

✶✾✿✼✼✝✵✿✸✹✼
✶✾✿✼✼✝✵✿✸✹✼
✶✾✿✼✼✝✵✿✸✹✼
✾✿✾✽✽✝✵✿✽✾✵

LR-

✵✿✵✼✹✝✵✿✵✶✺
✵✿✵✼✹✝✵✿✵✶✺
✵✿✵✼✹✝✵✿✵✶✺
✵✿✵✼✹✝✵✿✵✶✺

② Abbreviations: Population prevalence (prev.), Positive Predictive Value (ppv), Negative Predictive Value (npv), Accuracy
(acc), Positive Likelihood Ratio (LR+), Negative Likelihood Ratio (LR-). 99% confidence intervals calculated for
♥ ❂ ✸✶✵ ✰ ✵✿✻ ✂ ✸✵✹ ❂ ✹✾✷.

And, by design, current approaches are unlikely to be effective against a fabricator with psychiatric training (See
Table 4). Other strategies with physiological monitoring and linguistic analysis 20–23 cannot be easily adopted in
structured or semi-structured interviews or patient reported outcome (PRO) measurement. Here, we present
an approach based on a generative artificial intelligence (AI) models to flag feigned PTSD symptomology
rapidly, efficiently, and accurately, and one that is remarkably immune to familiarity of the subject with psychiatric
diagnostic criteria.
We illustrate our methodology using symptom-level data for PTSD. Clinically, PTSD is an acquired mental disorder
that can develop following exposure to highly emotionally aversive event(s) and is characterized by a defined
set of symptoms including intrusive reactions, defensive avoidance, negative alterations in mood, cognitions,
and autonomic arousal 5 . In the United States, disability compensation is available for those with mental health
disorders, which while being a crucial resource for the truly afflicted, potentially can drive up fabrication rates 3,4 .
Feigning PTSD to access medical treatment, commit insurance, personal injury and other frauds, or in an attempt
to evade criminal liability and penalties 24–27 is unfortunately not rare, although some of the cited numbers could
be inflated 28 . Because PTSD is a serious mental health condition associated with substance use, mood, anxiety,
personality disorder, increased morbidity, and possibly with increased mortality 29,30 , false diagnoses and fabrication of self-reported symptom severity can cause substantial financial drain 31,32 to healthcare systems, divert
crucial resources from where they are needed 33 , and interfere with study outcomes by introducing inaccuracies
in clinical data 34 . Accurate disambiguation of true and fabricated PTSD is therefore of high importance, especially
since noncredible symptom reporting has been implicated in over over 20% of personal injury cases, as well as
20% of personal injury cases, as well as 20% of compensation-seeking Veterans 3,35–37 . In addition to curbing
financial fraud, the ability to reliably and efficiently detect PTSD symptom fabrication can help disambiguate
noncredible symptom reports and those driven by genuinely severe psychiatric distress from an indequate access
to healthcare 38,39 arising from poverty and other broad-ranging socio-economic factors.
VeRITAS exploits the fact that that both clinician-rated and patient self-reported symptoms have statistical
dependencies arising from the nature of the questions themselves (Fig. 1) and are modulated by the latent trait
or condition we are attempting to measure ❡✿❣✿, PTSD diagnosis and/or severity. We operationalize this principle
without requiring human-understanding of the specific items being administered; thus, making the approach
specific to the disease at hand (PTSD), while being potentially generalizable to other disorders if appropriate
training data are available.
Our key finding is that the subtle cross-dependencies between the symptom items are challenging to mimic onthe-fly, even for individuals with advanced training in psychiatric diagnosis, ❡✿❣✿, forensic psychiatry. In particular,
maintaining the right amount of expected structure in a sequence of responses to a structured diagnostic
interview, measurable via our “complexity” and “surprise” parameters proves is difficult. Thus, we posit that
VeRITAS offers a robust approach for flagging fabricated response sequences, can be trained to target specific
2

Feel emotionally numb due to a
stressful event in the past?
Still enjoy doing many things that
ptsd43 you used to enjoy?
How often have you experienced
memory problems due to a
ptsd119
stressful event in the past?
ptsd19

Structured interview for
PTSD diagnosis

Q-net
Inference

ptsd43

ptsd208
ptsd19

ptsd119

1

2

3

4

Qnet :
generative model
for responses

5

Colors representing responses
(mixed colors represent distributions)

Complexity

response

fabrication condition
Surprise

too simple
or
too
surprising

Fig. 1: Conceptual framework. Using a dataset of responses to a validated structured interview for PTSD diagnoses,
along with clinician-validated diagnoses, we infer a generative model (Q-net) for responses among PTSD patients. In our
framework for detecting fabrication, we flag responses as those which are highly “surprising” (defined as violating inferred
cross-dependencies between individual response items) or are too simple (lacking complexity in the response patterns typical
of true responses). The precise “fabrication condition” shown above is validated from theoretical considerations as well as
field experimental data. In the fragment of the Q-net model shown, the recursive structure may be seen emerging with
each non-leaf node being mapped to its own predictor, ❡✿❣✿, follow the highlighted nodes corresponding to questions (items)
labeled ptsd119, ptsd43 and ptsd19.

disorders, can be administered in less that ✹ minutes on average, and requires no subjective interpretation.

R ESULTS
Participants and Data Sources
Our first dataset (referred to as the VA dataset) comprises ♥ ❂ ✸✵✹ participants recruited at a Veterans Health
Administration facility for an earlier study 40 . Veterans between the ages of 18 and 89 years were recruited
with written informed consent. Once eligibility was determined by the study team, participants completed a
PTSD-symptom questionnaire from the CAT-MH PTSD item bank 40,41 , comprising ✷✶✶ items, including some
items from the PTSD Checklist (PCL-5). Participants were also assessed by licensed doctorate-level mental
health providers using the Clinician-Administered Scale for PTSD for Diagnostic and Statistical Manual of Mental
3

TABLE 3: Demographic characteristics of participating mental health professionals
Area of Expertise
Neuropsychology, Psychology, Neurology
Forensic Psychiatry, Forensic Neuropsychology

16
11

Sex
Male
Female

14
13

Primary Institution of Affliation
Northwestern University
University of Illinois Chicago, NorthShore
University HealthSystem, University of Chicago
Medicine , Rush University Medical Center

21
6

Disorders, Fifth Edition (CAPS-5), which resulted in ✽✻ PTSD diagnoses, and ✷✶✽ participants deemed as not
having PTSD. We used 60% of the data for inferring our generative models, and the rest were used for validation,
including determining the out-of-sample AUC for identifying PTSD vs no-PTSD cases. The possibility of symptom
fabrication was not recorded in this dataset.
Our second dataset (the PL dataset) comprises results from online surveys conducted by a third party vendor
(Prolific) hired by the study team. Referred to here as the Prolific dataset, it comprises ♥ ❂ ✸✶✵ participants
(200 in the US, and 110 in the UK), screened for the absence of past or present mental health diagnoses. The
participants were asked to fake symptoms of PTSD while taking the VeRITAS interview.
Our third dataset (the PS cohort) comprises ♥ ❂ ✷✼ doctorate-level mental health professionals including
psychiatrists, psychologists, and neuropsychologists recruited from academic institutions in the Chicago region
(See Table 3). Eleven (40%) of the professionals described forensic mental health as part of their professional
practice specialization. Akin to the PL participants, professionals were instructed to feign PTSD symptoms when
taking the VeRITAS test with the aim of obtaining a false PTSD diagnosis. The objective in collecting the PS
cohort was to test if advanced knowledge of the relevant mental health diagnostic criteria and norms makes it
easier to “defeat” the detection algorithm.
In total, we considered ♥ ❂ ✻✺✶ participants comprising US Veterans, psychiatrically healthy community individuals from the general population in the US and the UK, and mental health professionals, with broad
representation across sexes, race and ethnicity. Average completion times and detailed demographic composition
of the respondents in the PL dataset are shown in Table 1, and that for the PS cohort are shown in Table 3. Both
the PL and the PS datasets were generated via a “web-app” implementation of the VeRITAS. Unlike the PL
dataset for which identifying respondent information is available to the third-party vendor (but not released to the
study team), for the PS cohort we only collected de-identified responses, and hence, while we knew who were
in the complete set of respondents for the PS cohort, we did not collect information to identify which response
was generated by which individual.

Principle of Characterizing Fabricated Responses
Our first insight behind VeRITAS is that fabricated response sequences necessarily have high average “surprise”,
✐✿❡✿ deviate more on average from the context-specific model predictions of symptom ratings (✐✿❡✿ item responses).
Here context-specificity refers to the dependence of a response to responses to other items, which might be
indicative of behavioral or mental health phenotypes. Our other insight, based on observations, is that attempts
to feign PTSD tends to generate “over-structure” compared to responses from participants with actual PTSD, ✐✿❡✿,
fabrication tends to manifest too much regularity in the response patterns. In other words, mimicked responses
are less “complex”. Here, we understand complexity in the formal sense of Kolmogorov 42 : more complex objects
are less compressible, and perfectly random sequences being not significantly compressible at all. Thus, a
sequence of all 1’s (✐✿❡✿ symptom absence) is very compressible (since, instead of storing individual responses,
one could just remember such responses as “all 1’s”), but a sequence generated from the sequential tosses
of a fair coin is not very compressible, ✐✿❡✿ has less structure. We hypothesize that true response sequences
tends to have maximal randomness, conditional on being constrained by the emergent cross-dependencies.
In other words, true responses should have just the right amount of identifiable structure, and no more. More
structure will make it less random, and less or inappropriate structure will increase surprise. Thus too much,
too little or deviant structures are all indicative of deviant responses, interpreted here as probably fabrication.
It is important to note that these criteria (upper bound on surprise and lower bound in complexity) are based
solely on algorithmic properties of the response sequence, and do not require human understanding of the items
themselves in a natural-language sense. Instead, for each response sequence ①, we compute two quantities:

4

✶✿✷

✔

✶✿✸

✗

✔

✵✿✾

✷

probability

✵✿✺

✵

✵✿✺

✷

(e) Selecting item bank

✶

✶✵ ✷

✖
✗
✔

✷

✖

✶✵ ✸

✶✵ ✹

✔
✗

✖

dx

✤
✶✵✵

(k)

✶✵✶

✶✵✷

sorted items

✤
✖

✶

✗

✗

✔

✶✿✺

✶

✶✿✺

✔

✔

✷

✶

✖

✔

✷

(l)

(m)

(n)

✵✿✾

✶✿✻

✤

✶✿✹

dx

✶✿✷

✖

✶

✗

✗

✔

✵✿✽
✵✿✼
✵✿✽

✶

✖

dx

✵✿✽
✵✿✼

✵

dx

✶
(j)

✵

✵ ✵✿✷ ✵✿✹ ✵✿✻ ✵✿✽ ✶

✤

✷

(i)

control

(h) correlation matrix

✔
✶✿✺

✵✿✺
positive

✶

✶
✶

✵✿✷

fabrication

✶✿✺

✵✿✻

✵✿✹

1-specificity

✷

✵✿✽

✵✿✻

✵

✵✿✻✹ ✵✿✻✻ ✵✿✻✽ ✵✿✼

(g)

✗

VA Dataset

✵

PTSD

(f)

Prolific Dataset

✶✵

✶✿✹

no PTSD

Mental Health Pro.

✷✵

SHAP value

✶✿✶

✶

✵✿✽

✸✵

✶

✶✿✷ ✶✿✹ ✶✿✻

✔

✵✿✽

✗

✖

dx

✤

✵✿✽

✶✿✺

✖

✷

✔

✷✿✺

✵✿✻
✵✿✹
✵✿✷

✔
✶

(o) VeRITAS ROC

✶

sensitivity

✶

(d) class distribution

✶

sensitivity

probability

✺

✵

(c) diagnosis ROC

(b) surprise

✹✵

✶✵
probability

In sample (VA)

(a) complexity

✗

✖

dx

✵

✤

✵

✵✿✷

✵✿✹

✵✿✻

✵✿✽

✶

1-specificity

Fig. 2: Training and performance. a, distribution of the complexity parameter. b, distribution of the surprise parameter.

c, ROC curve for diagnosis of PTSD without consideration of possible fabrication using Q-net models, ✐✿❡✿ using the ✖
parameter as risk. d, Class distribution for setting ✖✵ ❂ ✶✿✸✺. e, distribution of SHAP values of the CAT-PTSD master item
bank, showing the threshold above which the VeRITAS subset is selected. Panels f-n, out-of-sample results for the three
datasets, namely out-of-sample portion of the VA dataset, the PL and the PS datasets. Notably, the different categories
of responses obtained comprise ones that are deemd to not have PTSD without any need to consider fabrication, those
which are diagnosed as having PTSD, and those who are flagged as fabrication. Panels h,k,n show correlation between the
three VeRITAS parameters, and ✤ which is an indicator variable for fabrication flags. dx is the indiator of physician-confirmed
diagnosis (only available for the VA data), or estimated diagnosis using the ✖✵ threshold. Panel o illsutrates the lower envelop
of teh ROC curve for VeRITAS, and 95% confidence bounds.

✔✭①✮ and ✗ ✭①✮, referred to as the complexity and the surprise parameters respectively (See Methods for precise

definitions). Kolmogorov complexity is not computable 42 , and thus we estimate a related computable parameter
(See section on VeRITAS analysis in Methods).
The distributions for ✔❀ ✗❀ ✖ are characterized from the part of the VA data used for training, despite the fact
that this dataset does not have a direct evaluation of the possibility of symptom fabrication. This is possible,
because these quantities are computable from just the response sequences themselves. Concretely, we propose
a response sequence ① should be flagged as an instance of fabrication if for suitably chosen thresholds ✖✵ ❀ ✗✵ ❀ ✔✵ :

✤✭①✮ , ✖✭①✮ ≧ ✖✵

✁❫

✒

✁

✔✭①✮ ≦ ✔✵ ❴ ✗ ✭①✮ ≧ ✗✵

✓
✁

(1)

This may be paraphrased as “a response sequence has high likelihood of being fabricated if it 1) produces a
5

diagnosis of PTSD with high probability, and 2) is either too surprising or too simple.” The decision thresholds are
obtained from theoretical considerations and the VA data (See Methods), which allows us to choose thresholds
as reflecting specificity-sensitivity trade-offs (Fig. 2 a,b).

Integrated Diagnostic Capability
Given a sequence of responses in a diagnostic interview (symptom rating questionnaire), our first task is to
determine if a particular subject should be diagnosed with PTSD, if the possibility of symptom fabrication is
ignored. We call this a “naive diagnosis”. This diagnostic information might be available to VeRITAS externally
(❡✿❣✿ from a physician’s assessment of the patients). However, VeRITAS also has an integrated capability for
naive diagnosis: we identify separate generative models for 1) the diagnosed set of patients in the training set
(▼ ✰ , some of them might be fabricating their responses) and 2) for the patients identified as not having PTSD
(▼ ✵ ). Then given the sequence of responses from a new subject, we estimate if that sequence is more likely
to have been generated by the model for ▼ ✰ vs that for ▼ ✵ . We validate this diagnostic capability using the
training data described above, and we achieve good disambiguation between ▼ ✰ and ▼ ✵ , with out-of-sample
AUC ✿
✝ ✿ (See Fig. 2 c), which is at par or better compared to reported tools, ❡✿❣✿, CAT-PTSD 43 . In the
VeRITAS algorithm, for a given response sequence ①, the naive diagnosis risk score is denoted as ✖ ① , and
referred to as simply the “score” (See Methods). Fig. 2,d shows the class specific distributions estimated for ✖
for the VA data.

✵ ✽✻✼ ✵ ✵✵✽

✭✮

VeRITAS Validation Strategy and Performance
Since the VA data does not indicate presence or absence of possible fabrication, we adopted a non-standard
approach for validating VeRITAS. We assume that the PL participants do not have PTSD (based on their
screening of not having past or present mental health diagnosis, reporting at-most sub-clinical levels of anxiety
severity, and being informed to not take the test if experiencing PTSD symptoms), and that all of them were
attempting to fabricate symptoms as directed. This allows us to measure the false negative rate (or 1 - sensitivity),
as function of the VeRITAS parameters. The success rates of these participants in getting a “diagnosis” at a
average sensitivity of ✿
(using VeRITAS parameters ✔✵
❀ ✗✵
✿ ❀ ✖✵
✿ ) is shown in Table 1. Then
we check how many of the VA participants are flagged as being fabricating their symptoms amongst the ones
with a PTSD diagnosis. To determine a lower bound on performance we can assume all of these subjects are
false positives (which is unlikely, but nevertheless is an upper bound on false positives as function of VeRITAS
parameters). This allows us to construct a lower envelop of the ROC curve, and hence estimate a lower bound
of the AUC for determining fabrication, establishing a minimum AUC of ✿ ✝ ✿ at 95% confidence. High
performance operating points for different values of the population prevalence (prevalence has been reported
to be high between 20 to 30%) 9 , reflecting specificity/sensitivity trade-offs are shown in Table 2. These results
indicate that i fthe population prevalence in 30%, then we can achieve ✿ ✝
sensitivity with
specificity,
along with ✿ ✝ ✿
PPV and ✿ ✝ ✿
NPV, and positive likelihood ratio ✿ ✝ ✿ . For lower population
prevalences, ❡✿❣✿ at
, we can achieve ✿ ✝ ✿
sensitivity with
specificity, along with ✿ ✝ ✿
PPV
and ✿ ✝ ✿
NPV, and positive likelihood ratio ✿ ✝ ✿ . We note that these numbers represent lower
bounds on VeRITAS performance, due to our assuming an upper bound on false positives. The variation of
the complexity and surprise parameters for the VA data, along with a set of decision thresholds, is shown in
Fig. 2 f,g for the VA data, panels i,j for the PL data, and panels ll,m for the PS data. The correlation matrix
between ✔❀ ✗❀ ✖❀ ❞①❀ ✤ (where dx is the variable for clinician diagnosis) for the VA dataset (panel h) shows that the
complexity and the surprise parameters are well-correlated, and the dx and the ✖ parameters are well-correlated,
and the decision to designate as fabrication (✤) is not very well correlated to either of these. This pattern is
closely replicated in the PL and the PS datasets (panels k,n respectively), where the “dx” variable refers to the
predicted diagnosis. The estimated lower envelop for the ROC curve for the VeRITAS algorithm is shown in
panel o.

✾✹ ✷✪

❂✶

❂ ✵ ✼✻

❂ ✶ ✸✺

✵ ✾✺ ✵ ✵✷

✽✾ ✹ ✵ ✶✪
✷✵✪
✾✽ ✹ ✵ ✸✪

✾✼ ✾ ✵ ✹✪
✾✹ ✷ ✶ ✷✪
✶✾ ✼✼ ✵ ✸✺

✾✺ ✻ ✶✪
✾✾ ✵✾
✾✸✪

✽✽✪
✽✸ ✶ ✵ ✷✪

Item Presentation and Response Sequence in Administration
In VeRITAS we present a small random subset of the full item bank to the subjects. Although the models for
cross-dependency are inferred using the complete response sequence to all 211 items available, presenting a
smaller item set makes the test feasible, while also producing a vast number of possible variations. In the version
we validated, 20 items are presented. These are randomly generated from a distribution reflecting the impact
of the items in the inferred models on their ability to disambiguate between responses from diagnosed PTSD
patients and the control group. Impact is measured using standard SHAP analysis (See Methods). SHAP-values
for items are normalized to a probability mass function (pmf) over the top r
items, which is then sampled
to produce the item set. We can select items adaptively similar to CAT-PTSD 40 ; such complications have been
presently avoided. Fig. 2e shows the sorted estimated SHAP values for the items, and shows the threshold of
selection for presentation.

❂ ✷✵

6

Q-net Inference and Cross-talk Modeling
The generative models for response sequences inferred separately from the PTSD-positive and PTSD-negative
patients are referred to as “Q-nets”. Structurally, an Q-net comprises an interdependent collection of local
predictors, each aiming to predict the response to a specific item using as features the responses to ther
items from the item bank. (Fig. 1). Thus, an Q-net comprises almost as many such position-specific predictors
as the length of the response sequence. These individual predictors are implemented as conditional inference
trees 44 , in which nodal splits have a minimum pre-specified significance in differentiating the child nodes. Thus,
each predictor yields an estimated conditional response distribution for each item. The set of items acting as
features in each predictor are automatically identified, e.g., in the fragment of PTSD-positive Q-net (Fig 1), the
predictor for item ptsd119 includes the response to item ptsd19, that for ptsd19 includes item ptsd43, that for
ptsd43 includes ptsd208, which in turn includes ptsd43, revelaing complex possibly cyclic dependencies. Owing
to this recursive expansion, a complete Q-net captures the complexity of the rules guiding the subtle cross-talk
emerging between different items in a survey, and can be trained wihout linguistic understanding of the items
themselves. The Q-nets inferred for ▼ ✰ and ▼ ✵ have 5,852 and 10,301 independent parameters, encoding the
probability distributions on the tree leaves, which were identified automatically in the course of inferring the sets
of conditional inference trees. The overall VeRITAS model, which comprises these Q-nets along with the three
thresholds described before, therefore has 16,156 parameters.

Time-to-completion and Symptom Fabrication
In the PL dataset, the average completion time was 3.4 minutes ([2.9, 3.9], 95% CI). We find that fabrication
flags have no significant correlation with the time to completion. The success rate of defeating VeRITAS is
observed to have a correlation of ✿
✿
❀✿
❀
❈ ■ . Thus, fast responses that might reflect poor quality
survey in general 45–47 might not be effective in detecting fabrication, especially if participants are putting more
thought into how to feign their symptoms.

✵ ✹✽✭❬ ✷✼ ✽✼❪ ✾✺✪ ✮

Performance among Mental Health Professionals
The PS dataset illustrates that advanced training in mental health diagnosis or neuropsychology confers no
significant advantage in defeating the VeRITAS algorithm. Only one participant succeeded in not being flagged,
implying a false negative rate of ✿ . Using the same settings, participants in the PL dataset (drawn from the
general population in the US and the UK as part of Prolific’s cohort), were able to achieve a false negative rate
of ✿ , which is about 56.8% worse compared to the cohort comprising a substantial number of participants
with training in forensic mental health.

✸ ✼✪

✺ ✽✪

Number of Distinct Variations of VeRITAS Implementation

❂ ✷✵

❂ ✹✵
❂✺
❂ ✶✸ ✶✹✻ ✵✻✾ ✹✶✹ ✶✸✽ ✼✾✸ ✾✹✺ ✸✶✷ ✺✵✵

With r
items presented, randomly chosen from the top ◆
shortlisted from the master item bank
(sorted according
to SHAP values, as described before), and each✁ item having ▲
possible responses, we
✁
❀
❀
❀
❀
❀
❀
❀
❀
or
❀
❀
❀
variations of the test, with ▲r ◆r
can have ◆r
approximately ✷✺ possible responses, which is approximately equal to the number of stars in the observable
universe. Thus, it is non-trivial for human subjects to “learn” or “train” to defeat the algorithm.

❂ ✶✸✼ ✽✹✻ ✺✷✽ ✽✷✵
✶✵

Comparison Against State of Art
A well-known tool used to identify fabrication in mental health diagnoses is the Structured Interview of Reported
Symptoms, 2nd Edition (SIRS-2) 11 , which has a reported performance of sensitivity of 0.80, a specificity of 0.975,
and positive and negative predictive powers of more than 0.90 (based on a base rate of 31.8%), takes 30-40
minutes to complete, needs extensive expert interpretation, and is not disease-specific. In contrast, VeRITAS
may be completed in under 4 minutes, can have sensitivity and specificity both above 90%, has PPV over 86%
and NPV over 90% in selected operating points, can be tuned to specific disorders, and may be administered
automatically. The crucial difference in VeRITAS is the near-impossibility of defeating it through coaching, and
its effectiveness in the scenario that the subject has training as a mental health professional. The principles on
which existing tools such as the SIRS-2 are based makes them highly unlikely to be effective if the subject is
familiar with the symptomologies of mental disorders, and the approaches employed to flag fabricated response
sequences.

D ISCUSSION
The VeRITAS algorithm aims to identify symptom fabrication or “simulation” in clinician-rated and patient selfreported evaluations. While our current findings have demonstrated its applicability in assessments for PTSD,
the underlying principles of VeRITAS are broadly applicable for detecting feigned symptoms across other mental

7

health disorders, and more generally, for vetting possibly adversarial responses in structured interviews, even
unrelated to mental health assessments.
The potential negative societal implications and impacts on patient outcomes of being flagged as a possible
malingerer, i.e., engaging in intentional deception for external incentives, necessitate a careful consideration of
the unintended consequences of deploying any tool designed to make such assessments more automated. We
emphasize that while our findings are pertinent to the detection of feigned, faked, or simulated symptoms, they are
intended to be interpreted with nuance as part of a broader clinical assessment, acknowledging the often complex
motivations behind simulated symptoms. Although traditionally, these behaviors might indicate malingering,
an over-zealous application of that construct has frequently led to misunderstandings regarding the nature
of simulated symptoms. Descriptively, simulated symptoms manifest through a response style that impedes
accurate measurement of symptom severity in evaluating a medical syndrome. Simulated symptoms occur in both
factitious disorder and malingering. Factitious disorder is a psychiatric condition involving simulated symptoms
without clear positive incentives for illness, where the individual is unaware of not having a medical disorder,
contrasting with malingering, which is not a diagnostic category in DSM-5-TR but is coded in a special section on
clinical phenomena that are not well understood and/or do not represent a mental illness 5 . The empirical study
of symptom fabrication reveals a complex picture beyond criminally motivated deception, with three subtypes
of fabricated PTSD symptoms identified: manufactured, exaggerated, and misattributed 48 . Motivations behind
fabricated symptoms can range from criminological to pathogenic or adaptational. For instance, in an emergency
department context, a patient with a significant substance use disorder may simulate symptoms as a short-term
strategy perceived to be of adaptive value, though such a strategy ultimately proves maladaptive, undermining
trust between the patient and clinician. Empirical studies in emergency departments show that individuals who
feign psychiatric disorder symptoms are at a higher risk for psychopathology, mortality, and are more likely
to be unhoused or Black/African-American, and more likely to have a substance use disorder than matched
controls 38,49 .
Hence, the challenge of simulated symptoms and inaccurate diagnosis is not merely about detecting fabrication
to deny resources but about preventing potential side effects from inappropriate treatments, such as medication
or involuntary psychiatric hospitalization, and missing opportunities to address the real needs of those feigning
symptoms. Additionally, accurate measurement of PTSD symptom severity guides treatment decisions, and
invalid responses from an individual with true PTSD could lead to harmful treatment escalations.
Nevertheless, irrespective of the underlying motivations, deceptive responses present a significant challenge in
the accurate diagnosis of PTSD. Estimates of the prevalence of feigned symptoms for PTSD in psychiatric and
criminal justice settings range from 8% to 64% 9,50,51 , highlighting the complexity of the issue and underscoring
the need for reliable, rigorous, and principled methods for detecting deception in this context 52 . The prevalence
of deceptive responses, especially when common in certain clinical settings, may indicate broader societal
challenges. Moreover, a high incidence of fabrication burdens healthcare and legal systems, compromising
the integrity of clinical diagnoses and research, potentially leading to resource misallocation and impeding the
treatment of those genuinely suffering from PTSD. Efficient and discreet identification of such behaviors, avoiding
the stigma associated with a “malingering test”, is vital in addressing the complex challenges faced in clinical
practice. Research underscores the financial and clinical importance of accurately diagnosing mental health
conditions, with disability payments and the prevalence of service-connected mental disorders among veterans
illustrating the issue’s complexity. Furthermore, the variability in fabrication prevalence by context emphasizes
the necessity of a nuanced approach to diagnosis and treatment.
Our methodology represents a significant advancement over traditional fabrication detection methods, which
typically depend on domain-specific knowledge 53 and standardized tests developed through extensive research
on both genuine patients and fabricators (Table 4). Traditional methods, including the SIRS 11 (which requires
30-40 minutes and expert assessments), the Structured Inventory of Malingered Symptomology (SIMS) 12 , and
validity scales associated with the Minnesota Multiphasic Personality Inventory-2 13 , have demonstrated accuracy
rates between 85% to 95% depending on the context 54–57 . However, these methods have their limitations,
including the need for significant expertise to develop and administer, vulnerability to clinician bias, and the risk
o false positives and negatives. They may not easily extend to other contexts or disorders, and their effectiveness
can be compromised by coaching or prior knowledge of psychiatric symptomology. Additionally, current practice
lacks effective methods for discreetly flagging likely fabrication. Attempting to make such assessments without
formal tools is problematic since humans generally perform poorly at detecting lies, with accuracy rates often
barely surpassing chance 20 .
In contrast, VeRITAS leverages statistical differences in an individual’s response patterns compared to a set
of baseline responses, aiming to capture the complex, often non-obvious dependencies between interview
questions. The model is a non-parametric generative model that maps inter-question relations and dependencies,
enabling the detection of inconsistencies indicative of fabrication. Future investigations may also be able to train
the algorithm to detect other types of noncredible symptom reporting such as defensive responding (✐✿❡✿, symptom
under-reporting) and careless or random responding.

8

For now, our findings suggest that VeRITAS can achieve high sensitivity and specificity in detecting fabrication,
potentially surpassing or at least comparable to existing state-of-the-art techniques, but with several advantages.
VeRITAS requires less time for administration, does not necessitate domain-specific expertise for interpretation,
and minimizes the risk of bias. Moreover, its design makes it challenging for individuals, even those with advanced
psychiatric training, to defeat the system through coaching or preparation.
However, the impact of VeRITAS in clinical practice must be carefully evaluated, particularly for unintended
ethical implications, especially concerning vulnerable communities where the impact of mental health disorders is
often exacerbated by limited access to healthcare, socio-economic instability, and the stigma surrounding mental
health diagnoses. A non-zero risk of false positives could unjustly exclude vulnerable individuals from receiving
necessary care, and the algorithm’s reliance on statistical patterns may overlook the nuanced expressions of
PTSD symptoms across different cultures, potentially leading to biased assessments. This highlights the importance of incorporating cultural sensitivity into the algorithm’s development and underscores the indispensable
role of human judgment in the diagnostic process 20,52 . Ongoing research and validation in diverse settings are
crucial to refining the algorithm’s application, ensuring it serves as a tool for empowerment rather than exclusion,
particularly for underserved populations.
In conclusion, while symptom fabrication presents a persistent challenge in the accurate diagnosis and treatment
of PTSD, our study offers a promising new direction for detection methods. By employing a sophisticated, datadriven approach that transcends the limitations of traditional methods, VeRITAS provides a powerful tool for
clinicians and researchers. Its adoption could significantly enhance the integrity of PTSD diagnoses, ensuring
that resources are allocated to those genuinely in need and supporting the broader goals of psychiatric care
and research. However, further research and validation across diverse populations and settings are essential to
fully realize its potential and applicability in clinical practice.

M ETHODS
1. D EFINITIONS & N OTATION
Definition 1 (Survey). A survey for the purpose of this work is a structured interview, consisting of a finite
number of questions (items) posed to a set of participants, with these items drawn from a finite item bank, and
whose responses must be one from a pre-specified set fo choices, ❡✿❣✿, the Likert scale, with missing values for
the responses allowed.
Definition 2 (Response vector). A response vector is the set of responses to a survey from a single participant,
typically assuming that not all items are posed, and allows for the possibility that some responses are missing.
A Q-net, as described here, is a model of the response dependency structure for questions (items) posed to
participants in a survey. The Q-net explicitly estimates individual conditional distributions of each item response,
which collectively serve as a model of the full joint distribution of the responses.
Definition 3 (Q-net). Let ❳ ✘ P be an ♥-dimensional discrete random vector supported on a finite set ✝ and
following distribution P , i.e.
♥
❳ ❂ ✭❳✶ ❀ ✿ ✿ ✿ ❀ ❳♥ ✮ ✘ P❀
s✉♣♣✭❳ ✮ ❂ ✝ ❂ ✝✐ with ❥✝❥ ❁ ✶✿
✐❂✶

❨

For ✐ ❂ ✶❀ ✿ ✿ ✿ ❀ ♥, let P✐ ✿❂ P ✭❳✐ ❥ ❳❥ ❂ ①❥ for ❥ , ✐✮ denote the conditional distribution of ❳✐ given the values of
the other components of ❳ . Finally, for each ✐ ❂ ✶❀ ✿ ✿ ✿ ❀ ♥, let ✟P✐ denote an estimate of the distribution P✐ . Then
the set ✟P ✿❂ ❢✟P✐ ❣♥
✐❂✶ is called a Quasinet (Q-net). Identifying the true distribution P as the one describing the
joint statistics of the responses from a survey with ♥ items, we also refer to ✟P as the Q-net for the survey P .
When P is clear from context, we may omit the superscript and simply write ✟ ❂ ❢✟✐ ❣ to denote the Q-net. The
motivation for Definition 3 is that the collection of all estimators ✟ ❂ ❢✟✐ ❣ contained in a Q-net represents the
set of all inferred dependencies from the observed ecosystem. While the definition allows for arbitrary method of
algorithm to construct the estimators ✟✐ , the utility of a Q-net clearly depends primarily on the properties of the
✟✐ . In this study, we aim to minimize the set of a priori assumptions on the overall model structure to allow the
complex dependencies present in P to emerge. To that end, throughout this work all Q-nets are computed using
conditional inference trees 58 (a variant of classification and regression trees) to compute each ✟✐ . In general
each Q-net component ✟✐ is computed independently from the other ✟❥ , which allows a network structure to
emerge amongst these estimators.
An important quantity for an inferred Q-net is the persistence function ✦① .

Definition 4 (Persistence Function). Given a survey P inducing the Q-net ✟P and a response vector ① ❂

9

✭①✶ ❀ ✿ ✿ ✿ ❀ ①♥ ✮, the persistence ✦① of ① in the population modeled by the Q-net:
✦①P ✿❂ Pr✭① ✷ P ✮ ❂

♥
❨

✐❂✶

✟P✐ ✭❳✐ ❂ ①✐ ❥ ❳❥ ❂ ①❥ ❀ ❥ , ✐✮

(2)

The persistence function ✦①P , as the name suggests, is the probability that ① persists, ✐✿❡✿, P r✭① ✦ ①✮ for the
population modeled by the Q-net P , with ✶ ✦①P being the probability that ① is altered by a random perturbation.
We will show that if for two inferred Q-net models P❀ ◗, we have ✦①P ≧ ✦① , then it is more likely that model P
generated ①. This is an important result that justifies the definition of the score parameter in Defn. 6.
◗

The Q-net allows us to rigorously compute bounds on the probability of a spontaneous change from one response
vector to another, induced by spontaneous chance variations. Not all perturbations in a vector are either likely or
contextually meaningful. With an exponentially exploding number of possibilities in which a vector over a large
set of items can vary, it is computationally intractable to directly model all possible dependecies; nevertheless,
we can constrain the possibilities using the patterns we uncover via the Q-net construction. A key piece of this
approach is to design an intrinsic distance (q-distance) between any two response vectors, which is reflective
of this underlying dependency structure.
◗ ❂ ❢✟ ❣ ♥
Definition 5 (q-distance). Let ✟P ❂ ❢✟P✐ ❣♥
✐❂✶ and ✟
✐ ✐❂✶ denote Q-nets on populations P and ◗,
and suppose ① ❂ ✭①✶ ❀ ✿ ✿ ✿ ❀ ①♥ ✮ and ② ❂ ✭②✶ ❀ ✿ ✿ ✿ ❀ ②♥ ✮ are samples of ❳ ✘ P and ❨ ✘ ◗ respectively. Then the
q-distance ✒P❀◗ ✭①❀ ② ✮ between ① and ② is
◗

✒P❀◗ ✭①❀ ②✮ ✿❂

✑✐
❳❤ ✶ ✏
✶ ♥
◗
J ✷ ✟P ✭❳ ❥❳ ❂ ① ❀ ❥ , ✐✮ ❦ ✟ ✭❨ ❥❨ ❂ ② ❀ ❥ , ✐

♥ ✐❂✶

✐

✐

❥

❥

✐

✐

❥

❥

where J denotes the Jensen-Shannon divergence 59 .
For brevity, we may write simply ✒ (dropping the suffixes) if the populations are clear from context. Since the
Jensen-Shannon distance J is a legitimate metric 60 on the set of probability distributions (unlike KL-divergence),
✒ inherits nonnegativity, symmetry, and respects the triangle inequality; it follows that q-distance is a (pseudo)metric on ✝. Note that, being a pseudo-metric implies that we may have ✒✭①❀ ② ✮ ❂ ✵ for ① , ② , i.e. distinct vectors
can induce the same distributions over each index, and thus have zero distance. This is in fact desirable, since
we do not want our distance to be sensitive to changes that are not meaningful. The intuition is that not all
variations are equally important or likely. Moreover, we show in Theorem 1 that the log-likelihood of a vector ①
transitioning to ② scales with ✒✭①❀ ② ✮, allowing us to directly estimate the probability of spontaneous (or sequential)
jumps between abundance profiles.
Theorem 1 (Probability Bound). Given a vector ① of length ♥ from P that transitions to ② from ◗, we have the
following bounds at significance level ☛.
♣✽◆ ✷
♣✽◆ ✷
(3)
✦② ❡ ✶ ☛ ✒✭①❀②✮ ≧ P r✭① ✦ ②✮ ≧ ✦② ❡ ✶ ☛ ✒✭①❀②✮
where ✦② is the persistence of ② (Def. 4), and ✒✭①❀ ② ✮ is the q-distance between ①❀ ② (Def. 5).
Proof. See later in Section 3.



Theorem 1 gives theoretical backing to the claim that samples generated by the Q-net indeed reflect likely
perturbation possibilities from the current state. Thus we can use the Q-net to draw contextually realistic samples
that respect the cross dependencies and reduce surprise (that is, the Q-net-inferred conditional distributions can
be used to generate approximate samples from the population P ).
Remark 1 (Neighborhood Structure). It follows from Th. 1 that we have for some constant ❈ ,

✦ ②✮ ☞☞ ≦ ❈✒✭①❀ ②✮
❧♥ PP rr✭✭①② ✦
②✮ ☞
implying for all response vectors ② within a small neighborhood of ① (small in metric ✒), we have:
P r✭② ✦ ①✮ ✙ P r✭① ✦ ①✮
☞

☞
☞
☞
☞

which reveals an important special structure on local neighborhoods.

10

(4)
(5)

2. V E RITAS A NALYSIS
Definition 6 (Algorithm VeRITAS Parameters). We introduce three parameters referred tro as teh complexity,
surprise and score parameters (✔❀ ✗❀ ✖ respectively) for a given response vector ①:
✶ ❧♥ P r✭① ✦ ①❥▼ ✰ ✮ ❂ ❧♥ ✦①▼ ✰
complexity: ✔ ,
(6)

❥①✏❥

❥

✶

surprise: ✗ , E✐
score: ✖ ,

✰
✟▼
✐ ✭① ✐ ✮ ①✐

❥①❥

✑

(7)
▼✰

❧♥ P r✭① ✦ ①❥▼ ✰ ✮ ❂ ❧♥ ✦①
❧♥ P r✭① ✦ ①❥▼ ✵ ✮ ❧♥ ✦①▼ ✵

(8)

where ▼ ✰ indicates the sub-population exhibiting a particular trait of interest ❡✿❣✿ a mental health disorder such
as PTSD, and ▼ ✵ is the control sub-population where this trait is absent.
Definition 7 (Fabrication Signal). A response vector ① is defined to have the fabrication signal if:

✤✭①✮ , ✖✭①✮ ≧ ✖✵

✁❫

✒

✁

✔✭①✮ ≦ ✔✵ ❴ ✗ ✭①✮ ≧ ✗✵

✓
✁

(9)

The decision thresholds ✔✵ ❀ ✗✵ ❀ ✖✵ are inferred from survey data.
Lemma 1 (Complexity). For a survey with ♥ items, and assuming ▲ to the number of possible responses to each
item, the unconditional probability of a response vector ① occurring among all feasible responses is bounded
above by ✭❡✔ ❂▲✮♥ , where ✔✭①✮ is the complexity parameter for response ①.
Proof. Let ✔✭①✮ ≦ ✔✵ . From Def. 6, we have for a response vector ①,

✶ ❧♥ ✦ ≦ ✔✵ ✮ ✦ ≧ ❡ ♥✔
(10)
①
①
♥
✵
Summing on both sides over all responses ① with ✔✭①✮ ≦ ✔ (assume there are ◆① such sequences), we have:
❳
❳
✶ ≧ ✦① ≧ ❡ ♥✔
(11)
✵

✵

①

①

where the first inequality follows from observing that responses very close to ① in the q-distance metric have
a specific structure, namely ✦① ✙ P r✭② ✦ ①✮ (See Remark 1) and responses further away have smaller jump
probabilities, which then implies:

◆①

❳

①

❡ ♥✔ ≦ ✶ ✮ ◆① ≦ ❡♥✔
✵

✵

The result then follows from noting that the complete set of possible responses has the size ▲♥ .

(12)


Lemma 1 justifies why a low value of ✔ implies the possibility of an un-natural response, because the odds of
generating such a response is remarkably small.
Corollary 1 (Algorithmic Complexity). , The algorithmic complexity of a response ① conditional on the number
of survey items ♥ is at most ✔✭①✮ ✰ ❖✭✶✮.
Proof. This follows from noting that a set of cardinality ▲♠ has a algorithmic complexity of ♠ ✰ ❖✭✶✮, since words
of length ♠ are sufficient to encode the index of any element of the set, and thus can be uniquely identified.
Sinec we can calculate ✔✵ ❂ ✔✭①✮ for any ①, and since the set of all ① for a given value of ✔✵ belongs to a set of
size at most ❡ ♥✔ , the result follows.

✵

Lemma 2 (Surprise). For any response vector ①, we have:
✗ ✭①✮ ≦ ✶ ❡ ✔✭①✮

(13)

Proof. Denoting ✟✐ ✭① ✐ ✮❥①✐ as ❛✐ , we note that ✦① is the geometric mean of the vector of ❛✐ s, while E✐ ✭✟✐ ✭① ✐ ✮❥①✐ ✮
is the arithmetic mean of the same vector, which then completes the proof by noting:
(14)
E✐ ✭✟✐ ✭① ✐ ✮❥①✐ ✮ ≦ ✦①✶❂♥ ✮ ✗ ✭①✮ ≦ ✶ ✦①✶❂♥

✶❂♥

Interpretation on Why the Defined Property Identifies Feigned Symptoms
Lemma 2 indicates that the requirement of an upper bound on the surprise and a lower bound on the complexity
are both aiming to flag responses which are unlikely to appear when the data (responses) are being generated
by the underlying process corresponding to the phenotype of interest (PTSD). When such unlikely responses do
appear appear nevertheless, it is likely that they are not being generated by the correct underlying process. One
can attempt to fake responses that might seem to increase the odds of a positive diagnosis, but the respondant
must replicate the cross-dependencies closely enough (build in enough structure) so that the deviation from
11

the expected responses is limitd (limited surprise requirment). But building in too much structure will reduce the
complexity too much (too much structure reduces complexity, since there are fewer highly structured sequences),
which will then fail the complexity lower bound.
Note that the remaining condition ✖✭①✮ ≧ ✖✵ is a diagnosis criterion for the trait of interest (▼ ✰ ), and may be
replaced with a different condition if available for identifying participants with the ▼ ✰ trait. This particular form
follows from a straightforward Bayesian argument on estimating the posterior.

SHAP Analysis Selection of Item Bank
We present a random subset of r ❂ ✷✵ items from a master subset of items used in CAT-PTSD. The items that
are selected to make this master subset is obtained by ranking the items according to their estimated impact on
model pprediction. One standard approach to estimate impact of features on model outcomes is SHAP (SHapley
Additive exPlanations) analysis 61 , which is a method derived from game theory to explain the output of machine
learning models. It provides a way to measure the contribution of each feature in a given model to the prediction
for each instance. In our scenario, we use the persistence function as the model prediction to compute SHAP
values, ✐✿❡✿, we rank the items based on the degree to which including an item within a subset of items with
non-empty responses moves the value of the persistence function.

3. P ROOF OF T HEOREM 1
Theorem 2 (Probability bound). Given a sequence ① of length ◆ that transitions to a strain ② ✷ ◗, we have the
following bounds at significance level ☛.
♣✽◆ ✷
♣✽◆ ✷
(15)
✦②◗ ❡ ✶ ☛ ✒✭①❀②✮ ≧ P r✭① ✦ ②✮ ≧ ✦②◗ ❡ ✶ ☛ ✒✭①❀②✮

where ✦② is the membership probability of strain ② in the target population ◗ (See Def. ??), and ✒✭①❀ ② ✮ is the
q-distance between ①❀ ② (See Def. 5).
◗

Proof. Using Sanov’s theorem 59 on large deviations, we conclude that the probability of spontaneous jump from
strain ① ✷ P to strain ② ✷ ◗, with the possibility P , ◗, is given by:

P r ✭① ✦ ② ✮ ❂
Writing the factors on the right hand side as:

◆
❨

✟P✐ ✭① ✐ ✮❥②✐

✐❂✶

✟P✐ ✭① ✐ ✮❥②✐ ❂ ✟ ✭② ✐ ✮❥②✐

✥

◗
✐

✁

✟P✐ ✭① ✐ ✮❥②✐
✟◗✐ ✭② ✐ ✮❥②✐

(16)
✦

(17)

we note that ✟P✐ ✭① ✐ ✮, ✟✐ ✭② ✐ ✮ are distributions on the same index ✐, and hence:
◗

❥✟P✐ ✭① ✐ ✮②✐ ✟◗✐ ✭② ✐ ✮②✐ ❥ ≦

❳

②✐

❥✟P✐ ✭① ✐ ✮②✐ ✟◗✐ ✭② ✐ ✮②✐ ❥

✷✝✐

(18)

Using a standard refinement of Pinsker’s inequality 62 , and the relationship of Jensen-Shannon divergence with
total variation, we get:
☞

☞

☞
✟◗✐ ✭② ✐ ✮②✐ ☞☞ ≦ ✶ ♣✽✒
✶
✒✐ ≧ ❥✟P✐ ✭① ✐ ✮②✐ ✟◗✐ ✭② ✐ ✮②✐ ❥✷ ✮ ☞☞☞✶
✐
✽
✟P✐ ✭① ✐ ✮②✐ ☞☞ ❛✵

(19)

where ❛✵ is the smallest non-zero probability value of generating the entry at any index. We will see that this
parameter is related to statistical significance of our bounds. First, we can formulate a lower bound as follows:
✥

✦

✥

❥ ❂ ❳ ❧♦❣ ✟P✐ ✭① ✐ ✮❥②✐
❧♦❣
◗
✟◗✐ ✭② ✐ ✮❥②✐
✐
✐❂✶ ✟✐ ✭② ✐ ✮❥②✐
◆
❨
✟P✐ ✭① ✐ ✮ ②✐

Similarly, the upper bound may be derived as:
✥

✦

✦

≧

❳

✥

✐

✥

❥ ❂ ❳ ❧♦❣ ✟P✐ ✭① ✐ ✮❥②✐
❧♦❣
◗
✟◗✐ ✭② ✐ ✮❥②✐
✐
✐❂✶ ✟✐ ✭② ✐ ✮❥②✐
◆
❨
✟P✐ ✭① ✐ ✮ ②✐

Combining Eqs. 20 and 21, we conclude:

♣✽◆

◗
✶ ✟P✐ ✭② ✐ ✮②✐
✟✐ ✭① ✐ ✮②✐

✦

≦

❳
✐

✦②◗ ❡ ❛✵ ✒ ≧ P r✭① ✦ ②✮ ≧ ✦②◗ ❡

✥

✦

≧

♣ ❳
✽

❛✵

✐

✟◗✐ ✭② ✐ ✮②✐ ✶
✟P✐ ✭① ✐ ✮②✐

♣✽◆

❛✵ ✒

✒✐✶❂✷ ❂

♣

✦

≦

♣

✽◆ ✒

❛✵

✽◆ ✒
❛✵

(20)

(21)

(22)
Now, interpreting ❛✵ as the probability of generating an unlikely event below our desired threshold (✐✿❡✿ a “failure”),
we note that the probability of generating at least one such event is given by ✶ ✭✶ ❛✵ ✮◆ . Hence if ☛ is the
pre-specified significance level, we have for ◆ ❃❃ ✶:
❛✵ ✙ ✭✶ ☛✮❂◆
(23)

12

Hence, we conclude, that at significance level ≧ ☛, we have the bounds:
♣✽◆ ✷
♣✽◆ ✷
✦②◗ ❡ ✶ ☛ ✒ ≧ P r✭① ②✮ ≧ ✦②◗ ❡ ✶ ☛ ✒

✦

(24)


TABLE 4: Summary of malingering/deception detection methods❄ .
Approach/Tool

Description

Noted Accuracy/Performance

Structures Interview of
Reported Symptoms
(SIRS) 11

An interview-based measure with
multiple detection strategies.

sensitivity of 0.80, specificty of
0.975, and positive and
negtaive predictive values
❃ ✵✿✾, takes 30-40 minutes to
administer.

Structured Inventory of
Malingered
Symptomology
(SIMS) 12

A paper-and-pencil screening device for
detecting malingering with a sensitivity
for detecting malingering of 95.6% in a
study with college students.

95.6% sensitivity in a specific
study context.

Minnesota Multiphasic
Personality Inventory-2
(MMPI-2) 13,63

A self-report measure assessing
personality and psychopathology.
Certain validity scales were developed
to uncover malingering.

Not specified, but noted flaws
and potential for false positives.

Millon Clinical Multiaxial
Inventory MCMI-III 64

A self-report scale focusing on
personality disorders.

Minimal clinical utility with low
to zero positive predictive value,
and negative predictive value of
0.63.

Miller Forensic
Assessment of
Symptoms (M-FAST) 65

A brief screening measure for
malingered mental illness in forensic
settings.

AUC 0.754, with poor
sensitivity, and not appropriate
as symptom valdity test.

Human Lie Detectors

Not a specific tool, but the general
method of humans attempting to
discern lies from truth.

People are generally poor lie
detectors 20 .

Arousal-Based
Approaches (like the
Polygraph)

Techniques that rely on physiological
responses.

Criticized for poor validity and
high rate of false positives 66 .

Cognitive Load-Inducing
Approaches such as
“reverse order
interview”

Techniques that view deception as a
cognitive act that generally imposes
greater cognitive load on respondents
than honesty does.

No reliable support in
literature 67

Autobiographical
Implicit Association Test
(aIAT) 55

Designed to determine whether
respondents possess actual
autobiographical memories.

91% accuracy rate in identifying
genuine autobiographical
memories.

Timed Antagonistic
Response Alethiometer
(TARA) 56

A computer-administered, response
time-based method of lie detection.

85% accuracy rate.

Detecting Faked
Identities With
Unexpected Questions
and Mouse
Movements 57

Technique using computer mouse
movements in conjunction with
unexpected questions to uncover faked
identities

95% accuracy rate.

Time-Restricted
Integrity Confirmation
(TRI-Con)

Designed to detect deception by
inducing cognitive load on the individual
being tested, claimed to uncover
different kinds of deception including
malingering.

Up to 89% accuracy rate.

13

Personality Assessment
Inventory (PAI) 68

Activation-DecisionConstruction-Action
Theory (ADCAT)

Four validity scales, 11 clinical scales,
five treatment consideration scales, and
two interpersonal scales, for use in
diverse clinical, forensic, and
employment contexts.

AUC 0.65 with specificity values
0.86 -0.92, but poor sensitivity
0.12 - 0.18

A theory of high-stakes deception.

No specific accuracy rate
mentioned, but this is more of a
theoretical foundation rather
than a specific tool or method.

❄ This list is not exhaustive. Other MMPI-like measures exist that also include measures of noncredible symptoms reporting. There is exten-

sive body of research on symptom validity measures from tools like the MMPI and MCMI, and non-self-report lie detectors like polygraph and
TARA are not directly related to psychiatric symptom malingering.

R EFERENCES
[1] Rogers, R. An overview of malingering and its assessment. Psychiatric Clinics of North America 20, 15–27
(1997).
[2] Rogers, R. E. Clinical assessment of malingering and deception (Guilford Press, 2008).
[3] Frueh, B., Grubaugh, A., Elhai, J. & Buckley, T. Us department of veterans affairs disability policies
for posttraumatic stress disorder: administrative trends and implications for treatment, rehabilitation, and
research. Am J Public Health 97, 2143–5 (2007).
[4] Taylor, S., Frueh, B. C. & Asmundson, G. J. G. Detection and management of malingering in people
presenting for treatment of posttraumatic stress disorder: Methods, obstacles, and recommendations.
Journal of Anxiety Disorders 21, 22–41 (2007).
[5] Association, A. P. et al. Diagnostic and statistical manual of mental disorders. Text revision (2022).
[6] Diagnostic, A. Statistical manual of mental disorders (1994).
[7] Ali, S., Jabeen, S. & Alam, F. Multimodal approach to identifying malingered posttraumatic stress disorder:
A review. Innovations in Clinical Neuroscience 12, 12 (2015).
[8] Sparr, L. F. & Pitman, R. K. Ptsd and the law. Handbook of PTSD: Science and practice 449–468 (2007).
[9] Matto, M., McNiel, D. E. & Binder, R. L. A systematic approach to the detection of false ptsd. The journal
of the American Academy of Psychiatry and the Law 47, 325–334 (2019).
[10] Drob, S. L., Meehan, K. B. & Waxman, S. E. Clinical and conceptual problems in the attribution of
malingering in forensic evaluations. The journal of the American Academy of Psychiatry and the Law
37, 98–106 (2009).
[11] Wong, S. & O’Sullivan, M. The structured interview of reported symptoms (sirs): An overview. Assessment
12, 289–307 (2005).
[12] Smith, G. P. & Burger, G. K. Detection of malingering: validation of the structured inventory of malingered
symptomatology (sims). Journal of the American Academy of Psychiatry and the Law Online 25, 183–189
(1997).
[13] Ben-Porath, Y. S. Interpreting the mmpi-2-rf (U of Minnesota Press, 2012).
[14] Butcher, J. N. Minnesota multiphasic personality inventory. The Corsini Encyclopedia of Psychology 1–3
(2010).
[15] Fox, K. A. & Vincent, J. P. Types of malingering in ptsd: Evidence from a psychological injury paradigm.
Psychological Injury and Law 13, 90–104 (2020).
[16] Ales, F. & Erdodi, L. Detecting negative response bias within the trauma symptom inventory–2 (tsi-2): A
review of the literature. Psychological injury and law 15, 56–63 (2022).
[17] Reeves, C. K., Brown, T. A. & Sellbom, M. An examination of the mmpi-3 validity scales in detecting
overreporting of psychological problems. Psychological Assessment 34, 517 (2022).
[18] Suhr, J. A. & Gunstad, J. Coaching and malingering: A review. Assessment of malingered neuropsychological deficits 287–311 (2007).
[19] Rosen, G. M. et al. Risk of false positives when identifying malingered profiles using the trauma symptom
inventory. Journal of Personality Assessment 86, 329–333 (2006).
[20] Ekman, P. & O’Sullivan, M. Who can catch a liar? American Psychologist 46, 913 (1991).
[21] Mihalcea, R. & Strapparava, C. The lie detector: Explorations in the automatic recognition of deceptive
language. In ACL-IJCNLP 2009 (2009).
[22] Burgoon, J. K., Blair, J. P. & Strom, R. E. Cognitive biases and nonverbal cue availability in detecting
deception. Human Communication Research 34, 572–599 (2008).
[23] Zhou, L., Burgoon, J. K., Nunamaker Jr, J. F. & Twitchell, D. Automating linguistics-based cues for
detecting deception in text-based asynchronous computer-mediated communications. Group Decision and
Negotiation 13, 81–106 (2004).

14

[24] Guriel, J. & Fremouw, W. Assessing malingered posttraumatic stress disorder: A critical review. Clinical
Psychology Review 23, 881–904 (2003).
[25] Salloway, S., Southwick, S. & Sadowsky, M. Opiate withdrawal presenting as posttraumatic stress disorder.
Hospital and Community Psychiatry 41, 666–667 (1990).
[26] Resnick, P. J., West, S. & Payne, J. W. Malingering of posttraumatic disorders. In Rogers, R. (ed.) Clinical
assessment of malingering and deception, 109–127 (Guilford Press, 2008), 3 edn.
[27] Burkett, B. G. & Whitley, G. Stolen valor: How the Vietnam generation was robbed of its heroes and history
(Verity Press, 1998).
[28] Pagel, J. F. Post-Traumatic Stress Disorder: A Guide for Primary Care Clinicians and Therapists (Springer
Nature, 2020).
[29] Goldstein, R. B. et al. The epidemiology of dsm-5 posttraumatic stress disorder in the united states:
results from the national epidemiologic survey on alcohol and related conditions-iii. Social psychiatry and
psychiatric epidemiology 51, 1137–1148 (2016).
[30] Schnurr, P. P., Lunney, C. A., Bovin, M. J. & Marx, B. P. Posttraumatic stress disorder and quality of
life: Extension of findings to veterans of the wars in iraq and afghanistan. Clinical psychology review 29,
727–735 (2009).
[31] LoPiccolo, C., Goodkin, K. & Baldewicz, T. Current issues in the diagnosis and management of malingering.
Ann Med 31, 166–174 (1999).
[32] Oboler, S. Disability evaluations under the department of veterans affairs. In Rondinelli, R. & Katz, R. (eds.)
Impairment Rating and Disability Evaluation, 187–217 (W. B. Saunders, Philadelphia, PA, 2000).
[33] Taylor, S. Clinician’s Guide to Treating PTSD: A Cognitive-Behavioral Approach (Guilford Press, New York,
2006).
[34] Rosen, G. Dsm’s cautionary guideline to rule out malingering can protect the ptsd data base. J Anxiety
Disorders 20, 530–535 (2006).
[35] Marx, B. & Holowka, D. Ptsd disability assessment. PTSD Res Q 22, 1–6 (2011).
[36] Rogers, R., Sewell, K. & Goldstein, A. Explanatory models of malingering: a prototypical analysis. Law &
Hum Behav 18, 543–52 (1994).
[37] Lees-Haley, P. Mmpi-2 base rates for 492 personal injury plaintiffs: implications and challenges for forensic
assessment. J Clin Psychol 53, 745–55 (1997).
[38] Park, L., Costello, S., Li, J., Lee, R. & Jacobson, K. C. Race, health, and socioeconomic disparities
associated with malingering in psychiatric patients at an urban emergency department. General Hospital
Psychiatry 71, 121–127 (2021).
[39] Muntaner, C., Eaton, W. W., Miech, R. & O’campo, P. Socioeconomic position and major mental disorders.
Epidemiologic reviews 26, 53–62 (2004).
[40] Brenner, L. A. et al. Development and validation of computerized adaptive assessment tools for the
measurement of posttraumatic stress disorder among us military veterans. JAMA Network Open 4,
e2115707–e2115707 (2021).
[41] Gibbons, R. D. et al. Development of a computerized adaptive test for depression. Archives of general
psychiatry 69, 1104–1112 (2012).
[42] Li, M., Vitányi, P. et al. An introduction to Kolmogorov complexity and its applications, vol. 3 (Springer,
2008).
[43] Brenner, L. A. et al. Development and validation of computerized adaptive assessment tools for the
measurement of posttraumatic stress disorder among us military veterans. JAMA Network Open 4,
e2115707 (2021). URL https://doi.org/10.1001/jamanetworkopen.2021.15707.
[44] Hothorn, T., Hornik, K. & Zeileis, A. Unbiased recursive partitioning: A conditional inference framework.
JOURNAL OF COMPUTATIONAL AND GRAPHICAL STATISTICS 15, 651–674 (2006).
[45] Tourangeau, R., Rips, L. J. & Rasinski, K. The psychology of survey response (2000).
[46] Malhotra, N. Completion time and response order effects in web surveys. Public opinion quarterly 72,
914–934 (2008).
[47] Callegaro, M., Yang, Y., Bhola, D. S., Dillman, D. A. & Chin, T.-Y. Response latency as an indicator
of optimizing in online questionnaires. Bulletin of Sociological Methodology/Bulletin de Méthodologie
Sociologique 103, 5–25 (2009).
[48] Resnick, P. J. The detection of malingered mental illness. Behavioral Sciences & the Law 2, 21–38 (1984).
[49] Dell, N. A., Carbone, J. T., Holzer, K. J. & Vaughn, M. G. Malingering and comorbid psychopathology:
Evidence from the 2016-2017 nationwide emergency department sample. General Hospital Psychiatry 73,
121–122 (2021).
[50] McDermott, B., Dualan, I. & Scott, C. Malingering in the correctional system: does incentive affect
prevalence? Int’l J L & Psychiatry 36, 287–92 (2013).
[51] Schmidt, T., Krüger, M. & Ullmann, U. Base rate of probable malingering and its indicators in the
assessment of mental disorders-retrospective analysis of a sample of forensic psychological evaluations.
Die Rehabilitation 59, 231–236 (2020).
[52] DePaulo, B. M., Lindsay, J. J., Malone, B. E., Muhlenbruck, L. & Charlton, K. Cues to deception.
Psychological Bulletin 129, 74–118 (2003).

15

[53] Walczyk, J. J., Sewell, N. & DiBenedetto, M. B. A review of approaches to detecting malingering in forensic
contexts and promising cognitive load-inducing lie detection techniques. Frontiers in psychiatry 9, 700
(2018).
[54] Rogers, R. & Correa, A. A. Determinations of malingering: Evolution from case-based methods to detection
strategies. Psychiatry, Psychology and Law 15, 213–223 (2008).
[55] Sartori, G., Agosta, S., Zogmaister, C., Ferrara, S. D. & Castiello, U. How to accurately detect autobiographical events. Psychological science 19, 772–780 (2008).
[56] Gregg, A. P. When vying reveals lying: The timed antagonistic response alethiometer. Applied Cognitive
Psychology: The Official Journal of the Society for Applied Research in Memory and Cognition 21, 621–647
(2007).
[57] Monaro, M., Gamberini, L. & Sartori, G. The detection of faked identity using unexpected questions and
mouse dynamics. PloS one 12, e0177851 (2017).
[58] Sarda-Espinosa, A., Subbiah, S. & Bartz-Beielstein, T. Conditional inference trees for knowledge extraction
from motor health condition data. Engineering Applications of Artificial Intelligence 62, 26–37 (2017).
[59] Cover, T. M. & Thomas, J. A. Elements of Information Theory (Wiley Series in Telecommunications and
Signal Processing) (Wiley-Interscience, New York, NY, USA, 2006).
[60] Fuglede, B. & Topsoe, F. Jensen-shannon divergence and hilbert space embedding. In International
Symposium onInformation Theory, 2004. ISIT 2004. Proceedings., 31 (IEEE, 2004).
[61] Lundberg, S. M. & Lee, S.-I. A unified approach to interpreting model predictions. In Advances in neural
information processing systems (Curran Associates, Inc., 2017).
[62] Fedotov, A. A., Harremoës, P. & Topsoe, F. Refinements of pinsker’s inequality. IEEE Transactions on
Information Theory 49, 1491–1498 (2003).
[63] Glassmire, D. M. et al. Sensitivity and specificity of mmpi-2 neurologic correction factors: Receiver operating
characteristic analysis. Assessment 10, 299–309 (2003).
[64] Schoenberg, M. R., Dorr, D. & Morgan, C. D. The ability of the millon clinical multiaxial inventory–to detect
malingering. Psychological Assessment 15, 198 (2003).
[65] Shura, R. D. et al. The miller forensic assessment of symptoms test (m-fast) in veterans. Psychology &
Neuroscience 16, 167 (2023).
[66] Herbig, F. The ‘psychology’of polygraph’: Engendering differential salience-concerns and caveats. Journal
of Psychological Research 2, 1–10 (2020).
[67] Brimbal, L., Jones, A. M. & Quinby, E. A. Does telling a story in reverse elicit cues to deceit? a replication
and extension of vrij, leal, mann and fisher (2012). Legal and Criminological Psychology (2023).
[68] Gaasedelen, O. J., Whiteside, D. M. & Basso, M. Exploring the sensitivity of the personality assessment
inventory symptom validity tests in detecting response bias in a mixed neuropsychological outpatient sample.
The Clinical Neuropsychologist 31, 844–856 (2017).

DATA , M ATERIALS AND S OFTWARE AVAILABILITY
Software for inferring Q-nets is available as an open-source python package quasinet, and can be installed from
the standard Python code registry. A live implementation of the algorithm is available as https://paraknowledge.
ai/veritas/.

ACKNOWLEDGEMENTS
We extend our appreciation to the PS cohort comprising mental health professionals from around Chicago for
their uncompensated participation, and the Prolific survey participants, who received nominal compensation for
their invaluable contributions to this study.

Funding
This work is funded in part by the Defense Sciences Office of the Defense Advanced Research Projects Agency
(Project No. W911NF2010302). The claims made in this study do not necessarily reflect the position or the
policy of the sponsors, and no official endorsement should be inferred.

Author Contributions
IC originated the idea, performed analysis, provided funding, developed software and wrote the paper. MB, RG,
RL and JE interpreted data and wrote the paper.

Regulatory Approvals
Data collection for the PL and PS cohorts were approved by University of Chicago IRB #IRB24-0310. The third
party platform Prolific adheres to rigorous ethical guidelines and privacy policies, ensuring a diverse and reliable
16

participant pool verified through bank-grade ID checks and continuous quality management, aligning with WCAG
2.1 AA standards for accessibility and inclusivity.

17
