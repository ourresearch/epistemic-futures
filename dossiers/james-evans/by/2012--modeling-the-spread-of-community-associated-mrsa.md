---
title: "Modeling the spread of community-associated MRSA"
person: james-evans
section: by
type: journal-article
year: 2012
date: 2012-12-09
venue: "Winter Simulation Conference"
authors: "Charles M. Macal, Michael North, Nicholson Collier, Vanja Dukić, Diane S. Lauderdale, Michael David, Robert S. Daum, Philip Shumm, James A. Evans, Jocelyn Wilder, Duane T. Wegener"
source_url: https://doi.org/10.5555/2429759.2429855
openalex_id: https://openalex.org/W2104009712
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex duplicates merged: W2104009712 W4251914904; full text extracted from an open-access copy hosted at a repository or publisher OA location (OSTI, Zenodo, ACL Anthology, DSpace, OSF, IEEE, ResearchSquare or similar)"
---

# Modeling the spread of community-associated MRSA

## Full text

Proceedings of the 2012 Winter Simulation Conference
C. Laroque, J. Himmelspach, R. Pasupathy, O. Rose, and A.M. Uhrmacher, eds

MODELING THE SPREAD OF COMMUNITY-ASSOCIATED MRSA

Charles M. Macal
Michael J. North
Nicholson Collier
Argonne National Laboratory
Argonne, IL 60439 USA
and
University of Chicago
Chicago, IL 60637 USA

Diane S. Lauderdale
Michael Z. David
Robert S. Daum
Philip Shumm
James A. Evans
Jocelyn R. Wilder

University of Chicago
Chicago, IL 60637 USA

Vanja M. Dukic

Duane T. Wegener

University of Colorado - Boulder
Boulder, CO 80309 USA

Ohio State University
Columbus, OH 43210 USA

ABSTRACT
Community-associated methicillin-resistant Staphylococcus aureus (CA-MRSA) are strains of the bacterium S. aureus that are responsible for skin and soft tissue, blood, bone, and other infections that can be
life threatening. CA-MRSA strains are resistant to standard antibiotics related to penicillins and have a
high prevalence in the general community, as well as in healthcare facilities. CA-MRSA presents novel
challenges for computational epidemiological modeling compared to other commonly modeled diseases.
CA-MRSA challenges include modeling activities and contact processes of individuals in which direct
skin contact can be an important infection pathway, estimating disease transmission parameters based on
limited data, and representing behavioral responses of individuals to the disease and healthcare interventions. We are developing a fine-grained agent-based model of CA-MRSA for the Chicago metropolitan
area. This paper describes how we are modeling CA-MRSA disease processes based on variants of standard epidemiological models and individual agent-based approaches.
1

INTRODUCTION

Community-associated methicillin-resistant Staphylococcus aureus (CA-MRSA) are strains of the bacterium S. aureus that are responsible for skin and soft tissue, blood, bone, and other infections that can be
life threatening. CA-MRSA strains are resistant to standard antibiotics related to penicillins and have a
high prevalence in the general community, as well as in healthcare facilities. CA-MRSA presents novel
challenges for computational epidemiological modeling compared to other commonly modeled diseases,
such as influenza and smallpox. There have been few epidemiological simulation models focusing on
CA-MRSA until now. This paper describes aspects of modeling CA-MRSA and its spread throughout the
community that have not been previously reported. These include modeling the co-location of individuals
and the nature of contact between individuals that could result in CA-MRSA transmission, individual behavior in response to MRSA infection, and the effects of healthcare interventions on individuals. The
modeling approaches developed here may also apply to other diseases and in other public health contexts.

978-1-4673-4782-2/12/$31.00 ©2012 IEEE

Macal, et al.
This paper is organized as follows. Section 2 provides background on CA-MRSA and epidemiological modeling. Section 3 describes the CA-MRSA modeling problem and our approaches to modeling contact, disease transmission and transition, behavior, and metrics. Section 4 presents conclusions.
2

BACKGROUND

2.1

Community Associated (CA-)MRSA

Staphylococcus aureus is a bacterium first described in 1880 in pus from surgical abscesses. Frequently,
S. aureus lives on the skin, in the nose, throat, and other body surfaces. It has been estimated that up to
30% of the population are “staph carriers,” exhibiting no symptoms unless an active infection is present.
Through the 1950s, S. aureus infections were generally treated with early beta-lactam antibiotics including penicillin. In the early 1960s an antibiotic-resistant form of S. aureus, named MRSA (MethicillinResistant S. aureus) was isolated in the United Kingdom. MRSA was identified in the U.S. in 1968. Initially described in hospitals and facilities, this strain was referred to as “health care-associated” MRSA
(HA-MRSA). HA-MRSA strains had evolved an ability to resist treatment with all beta-lactam antibiotics, requiring treatment with specialized antibiotics. In hospitals, patients with open wounds, invasive devices, and compromised immune systems were at greater risk for contracting this infection. The spread of
bacterial colonies from patient to patient was attributed in part to contacts with hospital staff, which suggests that modeling the nature and frequency of contacts between workers and patients is of central importance in modeling HA-MRSA transmission.
MRSA was identified in the general community outside of the healthcare system in the late 1990s,
and genetically distinct strains came to be called Community-Associated MRSA (CA-MRSA). Simple
CA-MRSA skin infections are often found in people living or working in close quarters where skin contact is more likely, such as in households or as members of sports teams, prison inmates, child care workers, etc. However, individuals with no apparent risk factors have also contracted CA-MRSA. Why some
healthy people develop CA-MRSA skin infections that are treatable, whereas others infected with the
same strain develop severe and potentially deadly infections is the subject of ongoing research.
CA-MRSA infection reports increased dramatically across the U.S. and Europe in the early 1990s,
leading to the recognition that CA-MRSA had reached epidemic proportions. CA-MRSA became the
most frequent cause of skin and soft tissue infections seen in emergency departments in the U.S. throughout the first decade of the 2000s. The frequency of reported deaths from invasive MRSA infections surpassed the number of deaths from HIV-AIDS in the U.S. to become the number one public health crisis in
the country. Lee et al. (2012) estimate that in the U.S., CA-MRSA imposes an annual burden of $478 million to $2.2 billion on third-party payers and $1.4 -13.8 billion on society, depending on the CA-MRSA
definitions and incidences. One of the goals of the CA-MRSA model discussed here is to understand the
factors that might have been responsible for the rapid progress of the epidemic in its early stages.
2.2

Epidemiological Modeling

The differential equation model proposed by Kermack and McKendrick (1927) for modeling infectious
disease spread provides a conceptual framework for modeling CA-MRSA in an agent-based modeling
framework. The SIR model, as it is known, has been widely used to understand and predict the behavior
of many epidemics. A population is divided into three groups, or compartments, which consist of susceptible individuals, denoted by S, infected individuals, denoted by I, and recovered individuals, denoted by
R (thus S-I-R):

Macal, et al.

dS
= SI / N
dt
dI
= SI / N I
dt
dR
=
dt
Initial conditions: S0 = N 1, I 0 = 1, R0 = 0.

(1)

where E is related to both the number of contacts an individual has with other individuals and the likelihood that an infected individual transmits the infection to a susceptible individual upon contact, J is the
rate at which infected individuals recover from an infection, which is taken as 1/(mean duration of the illness), and N is the population size, assumed to be constant. The SIR model is termed a homogeneous
mixing model because of three implicit assumptions: the population is fully mixed in such a way that a
susceptible individual is equally likely to have contact with anyone in the population; all individuals have
the same number of contacts per unit time; and infected individuals transmit the disease to any susceptible
individual with the same probability. Each of these assumptions is relaxed in an agent-based epidemic
model, which, unlike the deterministic system in Equation (1), is also stochastic in nature.
Equation (1) represents the number of susceptible individuals that become infected in the time interval 't. Sterman (2000) and others note that E is a composite of two factors, the number of contacts per individual, Ec, and the probability that the infection is transmitted from an infected individual to a susceptible individual upon contact, Ei, as in E Ec Ei , where only the composite of Ec and Ei appears in Equation
(1). If 'S is the number of susceptibles infected in 't, then

'S = (number of susceptibles, S) u Pr[Susceptible becomes infected in 't].
Decomposing the probability that a susceptible individual becomes infected into its contact and infectivity
components yields the following:

'S = (Number of contacts per individual) u Pr[infection is transmitted from an infected individual to a
susceptible individual upon contact] u S I / N.

where the number of contacts per individual is taken as an average value in the deterministic SIR model.
In an agent-based model of disease transmission, the activities of individuals that lead to contact with
others are explicitly modeled. Disease transmission is context-dependent and modeled as a stochastic process. The processes that give rise to contact and infection, can be treated separately, mechanistically, and
in great detail. There are equivalence relationships between differential equation, system dynamics, and
agent-based models that can inform the epidemic agent-based modeling process (Rahmandad and Sterman 2008, Macal 2010).
2.3

Agent-based Epidemiological Modeling

From a public health perspective, Maglio and Mabry (2011) observe that agent-based modeling applications to public health are relatively new, but see ABM as part of an important “movement in public health
to embrace systems science methodologies and the interdisciplinary study of complex systems.” Some
large-scale agent-based epidemiological models have appeared in the literature with varying degrees of
detail and sophistication. Many of these focus on modeling influenza, such as EpiSimS, a massive simulation of the dynamics of contagious pandemic influenza in an artificial society (Stroud et al. 2007),
GSAM, a global simulation of pandemic influenza (Parker and Epstein 2011), and the urban pandemic in-

Macal, et al.
fluenza model by Aleman et al. (2009). An agent-based approach to modeling infective processes explicitly models the processes of contact, infection, treatment, and recovery.
2.4

Background on Modeling HA-MRSA

Detailed simulation models for HA-MRSA in the healthcare setting include Chamchod and Ruan (2012),
Meng et al. (2010), Barnes et al. (2010), D’Agata et al. (2009), Forrester et al. (2005), Hotchkiss et al.
(2005), Raboud et al. (2005), and Sebille and Valleron (1997). HA-MRSA models are typically probabilistic transmission models or discrete-event simulations that model movements of healthcare workers, contacts with patients, and patient contact with the hospital environment. Facilities are represented in spatial
detail, and time is represented in discrete increments, as in a process or discrete event simulation. This
approach facilitates the fine-grained modeling of individual contacts between patients and healthcare
workers, including the nature of, duration of, and timing of contacts, which is necessary to fully investigate the effects of such contact. In another application, Lee et al. (2011) model HA-MRSA transmission
in a model of a hospital system by modeling patient transfers between facilities.
3

MODELING CA-MRSA

The challenges for modeling CA-MRSA differ from those for modeling HA-MRSA. Instead of modeling
individual facilities or the relationships between facilities, the entire community must be modeled. There
are many open questions about the types of contact between individuals that might result in CA-MRSA
transmission and the importance of individual factors, such as genetic predisposition, demographic characteristics, etc. In addition, some individuals seem to resist colonization and infection, while others appear
to be in a semi-permanent state of colonization. CA-MRSA differs from other diseases such as influenza
in several important ways for modeling; in influenza models, the geographic scope is often national or
global, as mobility patterns could allow infection to spread around the globe within a short time. For CAMRSA, the focus is on the community, and the geographic scope is local or regional, such as a metropolitan area; the effects of new people entering the region are not thought to be large once CA-MRSA has
been established in the community. The asymptomatic colonization state makes the disease interesting in
terms of modeling agent behaviors. Specific aspects of modeling CA-MRSA contact and transmission as
embodied in the CA-MRSA ABM are described in the following sections. The CA-MRSA ABM is being
developed as part of the Models of Infectious Disease Agent Study (MIDAS 2012).
3.1

Contact Through Modeling Agent Activities

The CA-MRSA ABM models people as agents who go through their daily activities at various places in
the metropolitan area, on an hourly basis, and separately for weekdays and weekends. Agents engage in
activities that afford possibilities for disease transition, such as self-infection due to an abrasion or injury,
or transmission, if other agents are present and have close contact. The model includes a synthetic population of agents for the metro area based on U.S. Census and other data (Wheaton et al. 2009). Individual
places across the area are included in the model, with locations denoted by geographic coordinates.
Agents located in the same place and engaged in the same activity at the same time in the simulation possibly have the type of close physical contact with one another that can result in CA-MRSA transmission.
They may transition to different disease states through contact or other possible disease state transition
pathways.
Data are combined from many data sources to model the daily activities of the synthetic agent population. The American Time Use Survey (ATUS) is used to model adult activities. ATUS, available from the
U.S. Department of Labor, measures the amount of time people spend in various activities, such as paid
work, childcare, volunteering, and socializing. The Panel Study of Income Dynamics (PSID) is used to
model children’s activities. PSID, administered by the University of Michigan, is a longitudinal household survey. The ATUS data categorize an extensive number of individual daily activities. For the CAMRSA ABM, ATUS activities are aggregated into a smaller number of categories most relevant to the

Macal, et al.
kinds of contact that might occur for individuals engaged in the activities and the possibilities these activities afford for CA-MRSA disease state transmission and transition. Places and activities relevant to CAMRSA include households, schools, workplaces, hospitals and clinics, jails and prisons, and general living quarters, such as nursing homes, college dorms, gyms, and military barracks. These CA-MRSA specific activities can be modified as new data and studies are reported. Each place and activity type has its
own model for the likelihood of uncolonized individuals becoming colonized or infected when engaged in
that activity.
Agent activities vary by time of year; for example, children are out of school during summer recess
and have different contact patterns. We assume that the time of year is not important in terms of the direct
effect of environmental conditions (temperature, humidity, rainfall, etc.) on CA-MRSA infectivity, since
no data suggests these factors are important for CA-MRSA.
To model individual activities and movements as realistically as possible, assignment algorithms have
been developed to match specific people with specific places and activities. Children agents are matched
to schools, people agents are matched to workplaces, individuals who visit other households are matched
to a set of households they could likely visit, etc. For example, children are matched to the nearest schools
in their neighborhood, based on geographic coordinates of households and schools. Within schools, students are assigned to grade levels based on age, which allows for children to have more contact with the
children in their same classrooms, and less contact with other children in the same school. The matching
is designed to be statistically accurate. Although an agent may not correspond exactly to a specific person
in the population engaged in an activity at a particular time and place, the aggregate of all the agents engaging in all such activities at a particular time is consistent with empirical data at the regional level.
3.2

Modeling Disease Transmission and Disease State Transition

We model the disease transitions between the three disease states for CA-MRSA: colonized (denoted by
C), uncolonized (denoted by U), and infected (denoted by I). The uncolonized state corresponds to the
state S and infected to state I in the SIR model, Equation (1). Colonized is an additional compartment corresponding to an asymptomatic state in which an individual has measurable levels of CA-MRSA but exhibits no symptoms. An individual transitions between pairs of these states and is susceptible to repeated
colonizations and infections. Figure 1 summarizes the CA-MRSA disease states and transitions in the
CA-MRSA ABM.
Various approaches to modeling contact have been used in epidemiological models. Some model disease state transition as a Markov process with probabilistic “memoryless” agent disease state transitions
(Larson 2007). Others model the social contact structure for individuals within households based on family relationships. For example, Marathe et al. (2011) considers synthesized household contact networks for
complete mixing and care-giver types. In care-giver networks, infected individuals have contact only with
caregivers, who in turn have contact with the rest of the household members.
There is incomplete data at this time on the nature of various contacts and specific relationships
among individuals that result in CA-MRSA colonization or infection. So the CA-MRSA ABM uses a hybrid approach to model contact likelihood, based partly on perfect mixing and partly on implied social
network relationships by activity. Disease transition at the individual level is modeled by transition probabilities and event scheduling. The event scheduler is a nondeterministic finite state automaton (FSA) and
discrete event simulation (DES). The FSA models individual disease state transition in the absence of
agent behavioral responses or policy interventions. Effectively, this is a Markov discrete-time state transition model in which agents change disease states and are dynamically compartmentalized based on their
current disease and activity states. The DES is used to model disease state transitions that depend on individual patient behavior and assumed policy interventions, and potentially of physician and healthcare
worker behavior.
The next section describes modeling each disease transmission and transition pathway.

Macal, et al.

Uncolonized

e

~0

1 - (a x PAR x TIP)

a x PAR x TIP

1 - b x AIP - e

Colonized
d
c

Infected

PAR: Place/Activity Risk parameter
TIP: Transmission Intensity Parameter
AIP: Activity Infection Parameter

b x AIP

1-c-d

PAR varies by place/activity
TIP = 1 if U has contact with C
= 2 if U has contact with I
AIP varies by activity type

Figure 1 Disease State Transition Probabilities in CA-MRSA Model
3.2.1 Uncolonized to Colonized
An uncolonized individual may become colonized upon contact with a colonized or infected individual.
The likelihood of an individual becoming colonized is greater when the individual contacts an infected
individual than when contacting a colonized individual. We assume CA-MRSA is only transmitted between individual people; transmission does not occur from animals to people or through contact with inanimate objects (fomites). If ongoing research shows other transmission pathways could be important, the
structure of the CA-MRSA ABM allows them to be readily incorporated.
We define the parameter a as the empirically-estimated transition probability of an uncolonized individual (in disease state U) becoming colonized (transitioning to disease state C) due to contact for one
hour with a colonized individual. (Empirical estimation of all parameters in the model is described in
Section 3.2.6.) Parameter a is the only disease state transition parameter in the CA-MRSA model that is
the result of physical contact between individuals. To reflect a higher probability of becoming colonized
upon contact with an infected individual, we define the Transmission Intensity Parameter (TIP), which
scales the transmission rate. The value of TIP is based on expert judgment of clinical physicians, and is
one of the model parameters designated for sensitivity testing experiments.
The likelihood of transmission also depends on the kind of activity individuals are engaged in that results in contact. For example, activities in which abrasions are more likely as the result of contact, such as
certain sports activities, are more likely to result in colonization of an uncolonized individual by a colonized or infected individual. To account for this activity-related risk, a is adjusted according to the risk
level of the place and activity in which the contact occurs. This scaling factor is denoted as the
Place/Activity Risk parameter (PAR). Equation 2 summarizes the state transition process from the uncolonized to the colonized state.
Pr[Us o C] = TIPs u PAR u a

(2)

where Us is the disease state of the uncolonized individual having contact with an individual in state s H
{C, I}, and TIPs depends on the state of the contacting individual.

Macal, et al.
3.2.2 Colonized to Infected
Colonized individuals may develop infections by infecting themselves as a result of a skin abrasion, cut,
or other injury, represented as parameter b, estimated from empirical data. In the model,
Pr[C o I] = AIP u b
where b is the probability of a colonized individual becoming infected per hour, and AIP (Activity Infection Parameter) is a parameter that reflects the relative likelihood that an activity results in an infection.
An infected individual either clears the infection naturally through self-care or seeks treatment. Upon receiving care, the individual is treated with antibiotics and most likely clears the infection, returning to either a colonized (parameter c below) or uncolonized state (parameter d below). If the infection clears by
itself, we assume it takes several days longer to clear than if it is treated. We assume that an individual
passes through the C state to become infected; direct infection by a colonized or infected individual is not
an important pathway.
3.2.3 Infected to Colonized
We assume an infected individual eventually clears the infection, either through self-care or by receiving
treatment, and returns to either a colonized state or uncolonized state. We characterize the disease state
transition from I to C by a probability as:
Pr[I o C] = c
where c is the probability of an infected individual transitioning to a colonized state per hour after receiving treatment, estimated from empirical data. If the individual does not receive treatment, this probability
is adjusted downward, as described below and represented in Figure 4, corresponding to observed disease
durations for individuals who self-care.
3.2.4 Infected to Uncolonized
We characterize the disease state transition from I to U by the probability :
Pr[I o U] = d
where d is the probability of an infected individual transitioning to an uncolonized state per hour after
seeking treatment, estimated from empirical data. If the individual does not receive treatment, this probability is adjusted downward, corresponding to observed disease durations for individuals who do not seek
treatment.
3.2.5 Colonized to Uncolonized
An individual may spontaneously become uncolonized (i.e., without treatment), as the individual’s own
defenses eliminate the bacteria, or through targeted decolonization treatments. The hourly probability of
the transition is denoted by parameter e, estimated from empirical data:
Pr[C o U] = e.

Macal, et al.
3.2.6 Estimating Disease Transmission and Transition Parameters
Miller et al. (2012) conducted a cross-sectional study of adults and children with skin infections and their
household contacts in Los Angeles and Chicago; it is one of the few sources of detailed data on CAMRSA infection and colonization disease states over time. These data, along with data from studies in the
literature on CA-MRSA infection and colonization, are the basis for estimating disease state transmission
probabilities.
Describing the full process for estimating transmission parameters is beyond the scope of the current
paper. In general, parameter estimates are based on Miller et al. (2012) and a small set of time series data
from the literature. Bootstrap resampling is applied to the household contact data to estimate uncertainty
ranges for the disease state transition parameters a, c, d, and e; data from several studies on CA-MRSA
infection rates are used to estimate the range for parameter b. Figure 2 shows, for example, the resampled
distribution for disease state transitions U o C. Figure 3 shows the estimated ranges for all parameters.

3.7 ‫ ٻ‬10‫ ٻ‬3

2.32 ‫ ٻ‬10‫ ٻ‬3

denotes paramter values assumed for one simulation run

0.10

0.11

0.12

0.13

Figure 2 Bootstrap resampling statistics for
portion of the population transitioning
from U to C state in 90 days based on 660
data points and 200 samples. 95% confidence interval is [0.0796, 0.1308] (used for
estimation of parameter a),

c

‫ٻ‬

b

‫ٻ‬

‫ٻ‬

a ‫ٻ‬

‫ٻ‬

d: 2.98 ‫ ٻ‬10‫ ٻ‬3

c: 3.04 ‫ ٻ‬10‫ ٻ‬4

b: 2.58 ‫ ٻ‬10‫ ٻ‬5

‫ٻ‬

a: 2.59 ‫ ٻ‬10‫ ٻ‬5

‫ٻ‬
Note: Log Scale

4.74 ‫ ٻ‬10‫ ٻ‬4

0.09

‫ٻ‬

1.9 ‫ ٻ‬10‫ ٻ‬4

0.08

d

3.25 ‫ ٻ‬10‫ ٻ‬5

0.02

e: 2.4 ‫ ٻ‬10‫ ٻ‬5

‫ٻ‬

1.92 ‫ ٻ‬10

0.04

e

‫ٻ‬5

0.06

Transmission Transition Parameter

0.08

0.00

2.85 ‫ ٻ‬10‫ ٻ‬4

U ‫ ٻ‬C

6.69 ‫ ٻ‬10‫ ٻ‬5

a

0.10

1.53 ‫ ٻ‬10‫ ٻ‬5
2.31 ‫ ٻ‬10‫ ٻ‬5

3.2.7 Modeling Behaviors and Policy Interventions

Figure 3 Estimated 95% confidence intervals
for all disease state transition parameters
Ferguson (2007) contends that understanding the dynamics of infectious-disease transmission demands a
holistic approach, yet today's models largely ignore how epidemics change individual behavior. Some
models incorporate endogenous behavior of agents who dynamically respond to disease states computed
by the model. Del Valle et al. (2005) use a simplified model of an epidemic outbreak that includes behavioral changes modeled by the permanent transfer of individuals during the outbreak to a less active class;
transfer rates depend on people’s knowledge of the outbreak as measured by the number of identified cases. Epstein et al. (2008) model two interacting compartmentalized contagion processes: one of disease and
one of fear of the disease. Aleman et al. (2009) and Aleman et al. (2011) model the actions of individuals
based on the recognition of a pandemic outbreak; as people realize an outbreak is occurring, they decide
to quarantine themselves, admit themselves to hospitals, etc. Lizon et al. (2010) incorporate patient behaviors and interactions with healthcare workers into their model.

Macal, et al.
We develop a framework for modeling behavior of patients, and potentially of healthcare workers.
Figure 4 shows a scenario in which an individual agent acquires a CA-MRSA infection for the first time.
The behavioral framework shown explicitly represents the infection duration, actions the agent might take
in response to the infection, and a possible public health intervention. An alternative behavioral model
might be invoked for the same agent if infection reoccurs; for example, the next time the agent develops
an infection, they might seek treatment more quickly and receive alternate treatments.

Key:

Household
contacts begin
treatment

Behavioral
branching
Probabilistic
branching
Milestone

Household contacts
decolonized
t4
Household contacts
remain colonized

Pool for
disease state

Infected seeker
to uncolonized
t2

Individual
becomes infected
Infected
seeks
treatment
t1

a
1-a

Infected
self-care

Infected
seeker to
colonized

U

1-q
C

Infected self-care to
uncolonized
t3

7

1-g

q

Infected self-care
to colonized
0

g

14

z
1-z

19

28

Nominal
Timeline (days)

Notes: (1) a, q, g, z are empirically estimated parameters related to the propensity of individuals to exhibit
specific behaviors. (2) t1 is the distribution of time individuals wait before deciding to seek care, t2 is the
time individuals remain infected after seeking care, t3 is the time individuals remain infected after deciding
to self-care, t4 is the delay in starting decolonization treatments for household members after an infected
individual from the household seeks care, under a simulated household decolonization program.

Figure 4 Discrete Event Framework for Modeling Behavior
3.3

Data Logging and Metrics

A deterministic differential equation epidemic model produces the values for the state variables over the
simulation time horizon, which consists of the numbers of individuals in each disease state. A detailed
agent-based model produces data on many more variables in a single simulation run, from agent disease
states to agent interaction outcomes, to agent behavioral responses activities. The stochastic nature of the
simulation also requires many simulation runs to properly characterize uncertainty. Recording all of the
data the model produces is prohibitive due to the overhead of recording and storing the data. A subset of
“indicator variables” consists of summary statistics computed by the model and logged as the simulation
progresses. The indicator variables are initially used for debugging and to determine whether the model is
producing reasonable results; later in the modeling process indicator variables are used for model calibration, verification, and validation. Indicator variables include infected and colonized counts at each time,
new colonizations due to contacts with infected and colonized individuals, dendograms for selected
agents that portray their entire disease state history, and many more.

Macal, et al.
Indicator variables include metrics that correspond to the metrics that public health decision makers
typically use to understand epidemics. One of the key metrics that indicates the severity of an epidemic is
called the basic reproduction ratio, referred to as “R0,” an empirical statistic often calculated from surveillance data in the initial stages of fast-moving epidemics, such as influenza. R0 is defined as “the expected
number of secondary cases produced in a completely susceptible population, by a typical infected individual during its entire period of infectiousness” (Diekmann et al. 1990) and is typically calculated as the
spectral radius of the next generation operator for a differential equation epidemic model. From Equation
(1), R0 (not to be confused with the number of recovered individuals at time zero from Equation (1)) is estimated as ȾȀɀ, which can be seen by assuming the index patient is the only infected at t = 0, and interacts
with a fully susceptible population. When estimated in this way, R0 is a threshold, rather than the average
number of secondary infections and is used to understand whether an epidemic will die out (R0 < 1) or become endemic (R0 > 1). Longini et al. (2005) provides a method for calculating R0 from a stochastic epidemiological model, which also applies to agent-based models, by performing many simulations starting
with a single infected individual entering a wholly susceptible population. For an agent-based model, R0
can also be calculated explicitly, true to its definition as the number of secondary infections per infected
individual per infection episode by logging data on agent colonization/infection (C/I) events and C/I interactions with other agents. This calculation is done in the CA-MRSA ABM.
4

CONCLUSIONS

We are developing a fine-grained agent-based model of community associated CA-MRSA for the Chicago metropolitan area. Time is represented at the hourly level and space is represented at the place and activity level. The model represents the details of contact and disease transmission and transition for individuals as they go through their daily routines and participate in various activities in various places. The
model combines U.S. Census data, samples of individual activity diaries, data from the CA-MRSA literature, clinical data, expert judgments based on clinical experience, and specialized studies. The model provides a detailed picture of general activity patterns of the population, CA-MRSA transmission pathways,
and individuals’ behaviors in response to contracting the disease and public health programs. Using traditional epidemic models as a foundation, several modeling challenges (modeling contact, infectivity, behavior, metrics) are addressed in making the transition to the CA-MRSA ABM, some of which are applicable to other diseases that share CA-MRSA characteristics.
5

ACKNOWLEDGMENTS

This work is supported by the National Institute of General Medical Sciences, Models of Infectious Disease Agent Study (MIDAS), grant number U01GM087729, and the U.S. Department of Energy under
contract number DE-AC02-06CH11357.
REFERENCES
Aleman, D., T. Wibisono, and B. Schwartz. 2009. “Accounting for Individual Behavior and Demographics in Pandemic Disease Modeling.” Proceedings of the 2009 Winter Simulation Conf., edited by M. D. Rossetti, R. R. Hill, B. Johansson, A. Dunkin and R. G. Ingalls, 86-98, Wiley-IEEE
Press.
Aleman, D., T. Wibisono, and B. Schwartz. 2011. “A Non-Homogeneous Mixing Model For Predicting
Pandemic Disease Spread.” Interfaces Special Issue on Humanitarian Applications 41(3):301-315.
Barnes, S., B. Golden, and E. Wasil. 2010. “MRSA Transmission Reduction Using Agent-Based Modeling and Simulation.” INFORMS Journal on Computing 22(4):635-646.
Chamchod F., and S. Ruan. 2012. “Modeling the Spread of Methicillin-Resistant Staphylococcus aureus
in Nursing Homes for Elderly.” PLoS ONE 7(1):e29757.

Macal, et al.
D’Agata, E., G. Webb, M. Horn, R. Moellering, and S. Ruan. 2009. “Modeling the Invasion of Community-Acquired Methicillin-Resistant Staphylococcus aureus into Hospitals.” Clin. Infect. Dis.
48(3):274–284.
Del Valle, S., H. Hethcote, J. M. Hyman, and C. Castillo-Chavez. 2005. “Effects Of Behavioral Changes
In A Smallpox Attack Model.” Mathematical Biosciences. 195(2):228-251.
Diekmann, O., J. A. P. Heesterbeek, and J. A. J. Metz. 1990. “On the Definition and Computation of the
Basic Reproduction Ratio R0 in Models of Infectious Diseases in Heterogeneous Populations.” Journal of Mathematical Biology 28(4):365–382.
Epstein, J., J. Parker, D. Cummings, and R. Hammond. 2008. "Coupled Contagion Dynamics of Fear and
Disease: Mathematical and Computational Explorations." PLoS ONE 3(12):e3955.
Ferguson, N. 2007. “Capturing Human Behavior.” Nature 446:733, April.
Forrester, M., B. Comm, B. Arts, and A. Pettitt. 2005. “Use of Stochastic Epidemic Modeling to Quantify
Transmission Rates of Colonization With MethicillinǦ Resistant Staphylococcus aureus in an Intensive Care Unit.” Infection Control and Hospital Epidemiology 26(7):598-606.
Hotchkiss, J., D. Strike, D. Simonson, A. Broccard, and P. Crooke. 2005. “An Agent-Based and Spatially
Explicit Model of Pathogen Dissemination in the Intensive Care Unit.” Critical Care Medicine
33(1):168-176.
Kermack, W., and A. McKendrick. 1927. "A Contribution to the Mathematical Theory of Epidemics."
Proc. Roy. Soc. Lond. A 115:700-721.
Larson, R. 2007. “Simple Models of Influenza Progression Within a Heterogeneous Population.” Operations Research 55 (3):399–412.
Lee, B., S. McGlone, et al. 2011. "Modeling the Spread of Methicillin-Resistant Staphylococcus aureus
(MRSA) Outbreaks Throughout the Hospitals in Orange County, California." Infection Control and
Hospital 32(6):562-572.
Lee B., A. Singh, M. David, S. Bartsch, R. Slayton, S. Huang, S. Zimmer, M. Potter, C. Macal, D.
Lauderdale, L. Miller, and R. Daum. 2012. “The Economic Burden of Community-Associated Methicillin-Resistant Staphylococcus aureus (CA-MRSA).” Clin. Microbiol. Infect. May 21 [Adv. Epub].
Lizon, N., D. Aleman, and B. Schwartz. 2010. “Incorporating Healthcare Systems in Pandemic Models,”
Proceedings of the 2010 Winter Simulation Conference, edited by B. Johansson, S. Jain, J. MontoyaTorres, J. Hugan, and E. Yucesan, 2230-2236. Baltimore, MD.
Longini, I., A. Nizam, S. Xu, K. Ungchusak, W. Hanshaoworakul, D. Cummings, and M. Halloran. 2005.
“Containing Pandemic Influenza at the Source.” Science 309:1083-1087, Supplement.
Maglio, P. P., and P. L. Mabry. 2011. “Agent-Based Models and Systems Science Approaches to Public
Health.” Am J Prev Med 40(3):392–394, March.
Macal, C. 2010. “To Agent-based Simulation from System Dynamics.” Proceedings of the 2010 Winter
Simulation Conference, edited by B. Johansson, S. Jain, J. Montoya-Torres, J. Hugan, and E. Yücesan, 86-98. Wiley-IEEE Press.
Marathe, A., B. Lewis, J. Chen, and S. Eubank. 2011. “Sensitivity of Household Transmission to Household Contact Structure and Size.” PLoS ONE 6(8):e22461.
Meng Y., R. Davies, K. Hardy, and P. Hawkey. 2010. “The Application of Agent-Based Simulation to the
Modelling of MRSA Transmission in Hospital.” Journal of Simulation 4:60-67.
MIDAS
(Models
of
Infectious
Disease
Agents
Study).
2012.
www.nigms.nih.gov/Research/FeaturedPrograms/MIDAS/.
Miller, L., S. Eells, A. Taylor, M. David, N. Ortiz, D. Zychowski, N. Kumar, D. Cruz, S. Boyle-Vavra,
and R. Daum. 2012. “Staphylococcus aureus Colonization Among Household Contacts of Patients
With Skin Infections: Risk Factors, Strain Discordance, and Complex Ecology.” Clinical Infectious
Diseases 54(11):1523-1535.
Parker J., and J. Epstein. 2011. “A Distributed Platform for Global-scale Agent-based Models of Disease
Transmission.” ACM Trans. Model. Comput. Simul. 22(1) Article 2.
Raboud, J., R. Saskin, A. Simor, M. Loeb, K. Green, D. Low, and A. McGeer. 2005. “Modeling Trans-

Macal, et al.
mission of MethicillinǦ Resistant Staphylococcus aureus Among Patients Admitted to a Hospital.”
Infection Control and Hospital Epidemiology 26(7):607-615.
Rahmandad, H., and J. Sterman. 2008. “Heterogeneity and Network Structure in the Dynamics of Diffusion: Comparing Agent-Based and Differential Equation Models.” Management Sci. 54(5):998–1014.
Sebille V., and A. J. Valleron. 1997. “A Computer Simulation Model for the Spread of Nosocomial Infections Caused by Multidrug-Resistant Pathogens.” Computers and Biomedical Research 30:307-322.
Sterman, J. D., 2000, Business Dynamics: Systems Thinking and Modeling for a Complex World. Boston:
Irwin McGraw-Hill.
Stroud, P., S. Del Valle, S. Sydoriak, J. Riese and S. Mniszewski. 2007. “Spatial Dynamics of Pandemic
Influenza in a Massive Artificial Society.” Journal of Artificial Societies and Social Simulation
10(4)9 http://jasss.soc.surrey.ac.uk/10/4/9.html.
Wheaton, W. D., et al. 2009. Synthesized Population Databases: A US Geospatial Database for AgentBased Models. Publication No. MR-0010-0905, RTI Press: North Carolina.
AUTHOR BIOGRAPHIES
CHARLES M. MACAL, PhD, PE, is a senior system engineer at Argonne National Laboratory and Senior Fellow of the Computation Institute (CI) of the University of Chicago (UC) (macal@anl.gov).
MICHAEL J. NORTH, MBA, PhD, is a software engineer at Argonne and Senior Fellow in the UC-CI
(north@anl.gov).
NICHOLSON COLLIER, PhD, is a software engineer at Argonne (nick.collier@gmail.com).
VANJA M. DUKIC, PhD, is associate professor in the Dept. of Applied Mathematics at the University
of Colorado-Boulder (Vanja.Dukic@colorado.edu).
DIANE S. LAUDERDALE, PhD, is professor of epidemiology in the UC Dept. of Health Studies
(lauderdale@uchicago.edu).
MICHAEL Z. DAVID, MS, MD, PhD, is assistant professor in the UC Depts. of Medicine and Health
Studies (mdavid@medicine.bsd.uchicago.edu).
ROBERT S. DAUM, MD, CM, is professor of pediatrics, microbiology, and molecular medicine in the
UC Dept. of Pediatrics and director of the UC MRSA Research Center (rdaum@bsd.uchicago.edu).
PHILIP SHUMM, MA,
(pschumm@uchicago.edu).

is

senior

biostatistician

in

the

UC

Dept.

of

Health

Studies

JAMES A. EVANS, PhD, is associate professor in the UC Dept. of Sociology (jevans@uchicago.edu).
JOCELYN R. WILDER, MA, is a public health analyst in the UC Dept. of Health Studies
(jwilder@health.bsd.uchicago.edu).
DUANE T. WEGNER, PhD, is professor in the Dept. of Psychology, Ohio State University
(wegener.1@osu.edu).
