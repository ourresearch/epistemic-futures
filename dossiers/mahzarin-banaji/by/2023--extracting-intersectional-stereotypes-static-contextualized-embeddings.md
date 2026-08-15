---
title: "Extracting Intersectional Stereotypes from Static and Contextualized Embeddings"
person: mahzarin-banaji
section: by
type: preprint
year: 2023
date: 2023-10-16
venue: ""
authors: "Tessa Elizabeth Sadie Charlesworth; Kshitish Ghate; Aylin Caliskan; Mahzarin R. Banaji"
source_url: https://doi.org/10.31234/osf.io/tbuqh
doi: https://doi.org/10.31234/osf.io/tbuqh
openalex_id: https://openalex.org/W4387704250
cited_by_count: 0
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: OpenAlex Content API (pdf) at https://content.openalex.org/works/W4387704250.pdf; title-overlap check 0.67. Publisher landing page is https://doi.org/10.31234/osf.io/tbuqh."
---

# Extracting Intersectional Stereotypes from Static and Contextualized Embeddings

## Full text

EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                           1


Extracting Intersectional Stereotypes from Embeddings: Developing and Validating the FISE
                                          Procedure


     Tessa E.S. Charlesworth*1, Kshitish Ghate*2, Aylin Caliskan3, Mahzarin R. Banaji4

                 1
                     Kellogg School of Management, Northwestern University
                                    2
                                        Carnegie Mellon University
                         3
                             Information School, University of Washington
                                          4
                                              Harvard University


                                    * indicates equal contribution

                                  PREPRINT UNDER REVIEW


Author note: Correspondence concerning this article should be addressed to Tessa

Charlesworth, Kellogg School of Management, Northwestern University, Evanston, IL,

60208, at tessa.charlesworth@kellogg.northwestern.edu. This research was supported by a

Social Sciences and Humanities Research Council of Canada Postdoctoral Fellowship, and

the Rand Innovation Fund from the Harvard Department of Psychology awarded to Tessa

Charlesworth, and the Hodgson Innovation Fund from the Harvard Department of

Psychology awarded to Mahzarin R. Banaji. This work is supported by the U.S. National

Institute of Standards and Technology (NIST) Grant 60NANB23D194. Any opinions,

findings, and conclusions or recommendations expressed in this material are those of the

author and do not necessarily reflect those of NIST. All data and analyses are available at the

Open Science Framework (currently a view-only link for peer review):

https://osf.io/b9nmd/?view_only=f0b512840ad6488fb276cc3a48e09ddd.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                              2


                                            Abstract

Social group-based identities intersect. The meaning of “woman” is modulated by adding

social class as in “rich woman” or “poor woman”. How does such intersectionality operate at-

scale in everyday language? Which intersections dominate (are most frequent)? What

qualities (positivity, competence, warmth) are ascribed to each intersection? Here, we make it

possible to address such questions by developing a new stepwise procedure, Flexible

Intersectional Stereotype Extraction (FISE), applied to word embeddings (GloVe; BERT)

trained on billions of words of Internet text and report on original findings that emerged.

First, applying FISE to occupation stereotypes across intersections of gender, race, and class

showed alignment with ground-truth data on occupation demographics, providing initial

validation. Second, applying FISE to trait adjectives showed strong androcentrism (Men) and

ethnocentrism (White) in commanding everyday language (e.g., White Men are associated

with 59% of traits; Black Women with 5%). Associated traits also revealed intersectional

differences: advantaged intersectional groups, especially intersections involving Rich, were

associated with traits that are more common, positive, warm, competent, and dominant.

Together, the new empirical insights from FISE illustrate its utility for transparently and

efficiently quantifying intersectional stereotypes in existing large text corpora, with the

potential to expand the scope of research on intersectionality across time, place, and

demographic variation. This project further sets up the infrastructure necessary to pursue new

research on the emergent properties of intersectional identities.

       Keywords: gender, intersectionality, race, social class, stereotyping, word embeddings


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                            3


                                    Significance Statement

Stereotypes at the intersections of social groups (e.g., poor man) may induce unique beliefs

not visible in parent categories alone (e.g., poor or men). Despite increased public and

research awareness of intersectionality, empirical evidence on intersectionality remains

understudied. Using a large corpus of natural language, the Flexible Intersectional Stereotype

Extraction (FISE) procedure is introduced, validated, and applied to Internet text to reveal

stereotypes (in occupations and personality traits) at the intersection of gender, race, and

social class. Results show the dominance (frequency) and halo effects (positivity) of powerful

groups (White, Men, Rich), amplified at group intersections. Such findings and methods

illustrate the societal significance of how language embodies, propagates, and even

intensifies stereotypes of intersectional social categories.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                            4


     Extracting Intersectional Stereotypes from Static and Contextualized Embeddings:

                        Developing and Validating the FISE Procedure


       Since 2004, Google searches for the term “intersectionality” have increased

exponentially, reaching a peak in February 2023 (SI Appendix). This increasing interest

among the public parallels rising calls among social scientists to recognize how intersections

of social group identities modulate group perception1–3. Intersections of group identities, such

as race+gender, produce unique and emergent stereotype content4, as well as unique

experiences of discrimination5,6 that would be missed if group identities were examined in

isolation for experimental convenience. While intersectionality has received extensive

humanistic analyses and qualitative theorizing3,7, there remains limited empirical evidence on

it. Today, large-scale empirical work testing and quantifying such ideas in naturalistic

language data makes such an effort possible (cf.8).

       Here, we address past methodological limitations and advance empirical research on

intersectional stereotyping by introducing a new stepwise procedure – the Flexible

Intersectional Stereotype Extraction (FISE) procedure. The procedure is flexible in that it can

be: (a) applied to large-scale naturalistic data of word embeddings trained from any text

source, including different languages, geographies, or demographic groups; (b) applied to any

group intersection, so long as the group concept can be represented in words; and (c)

quantified in systematic and comparable metrics, such as the frequency (number) of traits

associated with an intersectional group, to facilitate direct comparisons of intersectional

stereotypes across diverse settings.

Past Research: Extracting Single Group Stereotypes from Static Embeddings.

       The FISE procedure builds from an emerging body of research using Natural

Language Processing, and especially static word embeddings such as GloVe9 to propel


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                             5


understanding of how social attitudes and stereotypes prevail in large-scale naturalistic

data10–12. For instance, static word embeddings have been used to quantify the relative

relationships between single groups (e.g., White, Black) and attributes (e.g., good, bad),

ultimately revealing that static word embeddings capture biases similar to attitudes obtained

directly from human minds13. In this early work, however, each social group was represented

independently, leaving stereotypes at intersections of identities unexamined. Such limitations

occur, in part, because social science researchers often rely on the availability and ease of use

in static single word embedding which have key advantages of being flexibly trainable across

languages14, time points15, and diverse demographics16. Yet static word embeddings arguably

encounter difficulties for studying intersectional stereotyping because, among other limits,

they cannot handle multi-word analyses (e.g., they cannot represent intersections such as

Black Women, White Men as accurately).

Past Research: Extracting Group Stereotypes from Contextualized Embeddings.

       Acknowledging such apparent methodological limitations, research in computer

science has made it possible to study social group biases using contextualized embedding

models (e.g., BERT17) with multi-word sentences18–20. For instance, Guo and Caliskan19

studied intersectional stereotypes across gender and race/ethnicity by representing group

concepts in sentences using examples from everyday language (e.g., “This is Aisha”, or

“Look at Keisha” for example sentences with Black woman names). As in previous static

embedding analyses, the authors then computed relationships (cosine similarities) between

the intersectional group-related sentences and positive/negative attribute sentences. Results

showed evidence of intersectional emergence, in which new traits emerged as associated with

the intersectional group that were not associated with the individual parent groups in

isolation; such findings were further validated against known emergent content, providing

confidence in the general approach of using language to study intersectional stereotyping.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                6


       Despite the improvements that can emerge from contextualized language models,

even these methods suffer from limitations. For instance, research with contextualized

methods have to-date represented groups through first/last names19,21. Yet many social group

dimensions are simply not encoded in names, especially more concealable groups like sexual

orientation, religion, or more physical stigmas such as body weight, age, or disability status22.

Additionally, given the greater computational and expertise demands of training or even fine-

tuning contextualized language models on new text corpora (e.g., different languages,

demographics, geographies), social science research remains limited in its ability to examine

the variability and scope of intersectional stereotypes if required to rely only on large

language models.

The Current Research: Flexible Intersectional Stereotype Extraction (FISE)

       To overcome such limitations and barriers for social science researchers, the current

research introduces FISE with a focus on intersectionality involving three major social

categories – race (in this case, Black/White), social class (rich/poor), and gender

(men/women) – that can shape group perception and its consequences of preference and

discrimination23,24. We demonstrate the application of FISE across pretrained embedding

models of large-scale Internet text corpora, ranging from static GloVe embeddings trained on

840 billion words from the Common Crawl to contextualized BERT embeddings trained on a

combination of Wikipedia and Common Crawl text.

       For the simplest case of static embeddings, FISE proceeds in five steps (see details in

Methods and SI Appendix). First, we create a list of target concepts for occupation labels

(Study 1) or trait adjectives (Study 2), as well as lists of group labels that represent each of

the three groups of interest (gender, race, class; Figure 1). Second, we compute the cosine

similarity of each target occupation/trait with each group concept (e.g., janitor-White, janitor-

Black, and so on). Third, we take the difference of the cosine similarities along a group


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                                    7


dimension (e.g., janitor-White vs. janitor-Black) and repeat this for the other group

dimensions (e.g., janitor-Rich vs. janitor-Poor, janitor-Man vs. janitor-Woman). Fourth, we

cross two group dimensions (e.g., race-by-class), placing each occupation/trait in the

resulting x-y coordinate space according to its cosine similarity with the individual group

dimensions. Fifth, we analyze the resulting number (frequency) and qualities (e.g., valence)

of the occupation/traits in each quadrant.

           A. Group-related sentences                                             B. Trait sentences
                              Class           Race              Gender                                 Traits
                                                                                                          Happy
                                 Poor             Black           Woman
                                                                                                          Honest
                                Beggar           African          Female
                                                                                                        Courageous
                               Penniless         Negro              Girl
                                                                                                         Cheerful
                             Impoverished        Blacks           Madam
                                                                                                         Peaceful
                               Destitute        Negroes          Daughter
                                                                                                       Compassionate
                                Needy         Dark-skinned        Mother
                                                                                                       Knowledgeable
                             Disadvantaged      Negroid            Sister
                                                                                                         Talented
                              Threadbare        Africans           Aunt
                                                                                                          Friendly
                                Beggars         Ethiopian         Maiden

           Template            Paupers         Ethiopians         Queen            Template              Humorous


                                                                              ∝
                                                                                                           Kind
                             Unprosperous    African-American   Grandmother
                                                                                      This is              Smart
             This is a/an      Homeless      Afro-American         Niece
                                                                                     They are
             There is a/an                                                                                 Rude
                                 Rich            White             Man                That is
             That is a/an                                                                                 Abusive
                               Wealthy         European            Male
                                                                                                         Negligent
                               Affluent        Caucasian           Boy
                                                                                                          Greedy
                                 Elite           Whites             Sir
                                                                                                         Unethical
                              Advantaged         British           Son
                                                                                                         Helpless
                               Moneyed         Caucasians         Father
                                                                                                           Grim
                              Prosperous      Light-skinned       Brother
                                                                                                       Irresponsible
                               Privileged       American           Uncle
                                                                                                          Scornful
                                 Elites        Americans         Gentleman
                                                                                                         Arrogant
                               Aristocrat      Europeans           King
                                                                                                           Angry
                              Aristocrats      Englishman       Grandfather
                                                                                                           Stingy
                                Nobility       Englishmen         Nephew


Figure 1. Group words used to represent class, race, and gender for applications of Flexible
Intersectional Stereotype Extraction. In the static embeddings, our primary analyses, FISE uses
only the individual words for each group (no templates). In the contextualized setting (Study 2 only),
FISE is performed by looking at the cosine similarity (essentially a correlation) between target group-
related sentences (panel A) and trait attribute sentences (panel B). A group sentence is created by first
selecting a template (e.g., “This is a”), and then adding the group labels for class (e.g., “rich”), race
(e.g., “Black”), and gender (e.g., “woman”). The process is repeated across all possible combinations,
yielding 5,184 sentences from three templates and 12 words for each group (3*12*12*12 = 5,184).
Similarly, for traits, all trait templates are combined with all positive/negative trait words, to yield a
sample of 300-900 trait sentences, depending on how many traits are chosen.

        The goal of FISE is primarily to improve the flexibility for extracting intersectional

content across any text source and any group intersection, with comparable, quantitative

metrics. Crucially, given wide-ranging scholarly interest in intersectionality, the FISE

method is also designed to be easy to use, transparent to understand, and low in

computational demands so that it can be easily adopted by scholars from any field. All code

and data are provided openly with clear guidelines to apply the method to any embeddings


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                              8


from different languages, cultures, media sources, and even across long timespans of text to

study change in group-based beliefs.

                    Study 1: Intersectional Stereotypes of Occupations

       The content and frequency of intersectional occupation stereotypes has received

almost no consideration in large language corpora (cf25) even though it is known that

workplace experiences of discrimination can be amplified for intersectional identities 26,27 .

Moreover, occupational stereotypes provide an ideal case study because they can be

compared to ground-truth data of actual occupation demographics to validate the FISE

procedure. Thus, as a first introduction to FISE, we identify (1) how many, and (2) which

occupations, from a list of 143 occupations from the 2022 Bureau of Labor Statistics report,

are associated with each intersectional quadrant across race-by-gender, class-by-gender, and

race-by-class.

Results

       Frequency of intersectional occupation stereotypes in FISE vs. ground truth. How

many occupations are associated with each intersectional quadrant in large-scale language

and in occupational demographic data? If FISE accurately identifies the frequency of

intersectional occupation stereotypes (i.e., how many occupations are associated with each

group), then FISE should show that intersectional groupings associated with the most

occupations in the real world (e.g., White Men) are also associated with the most occupations

in language. That is, if an intersectional group dominates the labor force in vivo, it should

also dominate in the frequency with which it occurs in naturalistic language.

       Indeed, the dominance of an intersectional grouping in real-world data is mirrored in

the number of occupations associated with each intersectional quadrant in language (Table 1).

Chi-square tests confirm that actual frequencies of occupations are not significantly different

from the associations extracted in language: for race-by-gender, c2 = 7.53, p = .06, V = 0.19,


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                               9


for race-by-class, c2 = 2.63, p = .45, V = 0.11, and for gender-by-class, c2 = 5.46, p = .14, V =

0.17. For example, looking at actual occupation data we see that 48% of occupations are

relatively more White (>50 percentage point difference in White vs. Black representation)

and occupied by Men (>50% men). In parallel, looking at language associations, White Men

are linguistically associated with 59% of occupations, which, although descriptively higher

than the actual representations, is not significantly different (see chi-squared tests above).

Similarly, in real-world data, only 5% of occupations are relatively more Black and occupied

by Women and, in language, Black Women are associated with 9% of occupations. Such

accuracy is also found for the class-by-gender and race-by-class comparisons (Table 1).

Ultimately, the language models show accuracy in identifying which intersectional groups

dominate (are most frequent) in the occupational stereotype space and, conversely, which

intersectional groups are made invisible (are least frequent) in occupational stereotypes.

       Which occupations are associated with intersectional groupings in FISE vs. ground

truth? Looking beyond how many occupations we next ask: which specific occupations fall

in each quadrant? To test accuracy here, we compare the “hits” (i.e., both language and

ground truth classify an occupation as, for example, White Rich) to “misses” (i.e., language

and ground truth deviated for specific occupation classifications). Across all 143 occupations,

language and ground-truth categorizations showed a 57%, 47%, and 51% “correct hit” rate,

for gender-by-race, gender-by-class, and race-by-class, respectively, which were not

significantly different from chance, c2 = 2.27, p = .13; c2 = 0.28, p = .59; and c2 = 0.03, p =

.86. Crucially, however, two additional analyses show that, when sufficient signal exists in

the real-world, FISE can in fact accurately capture occupational stereotypes.

       First, we inspect the individual occupations that “missed” classification: as a few

examples, judge, analyst, accountant, and bartender were classified as White Men

occupations in language data but, in ground-truth, were relatively more associated with White


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        10


Women. Crucially, in ground-truth these occupations were around the 50% mark of

men/women representation, with 55-59% women workforces, and thus provided ambiguous

gender signals in ground-truth data. Similarly, occupations that were more ambiguously

White/Black (e.g., with smaller differences in White/Black representation such as guard,

caregiver, recycler) were more likely to be misclassified along race. Those that were more

ambiguously Rich/Poor (e.g., around the median earnings; investigator, librarian, plumber)

were more likely to be misclassified across class (i.e., as a “rich” occupation, above median

earnings, or as a “poor” occupation, below median earnings).

                                                       Thus, in a second analysis, we looked at only those occupations that had clear real-

world signal, using stricter criteria (e.g., <30% women in the BLS data was required for a

“Men” classification; >70% women was required for a “Women” classification; see SI

Appendix). Using only that subset of occupations with clear real-world signal on gender, race,

and class, we found significant above-chance accuracy for all three contrasts of gender-by-

race, 69% [53%, 82%], c2 = 5.36, p = .02, gender-by-class, 70% [51%, 84%], c2 = 4.36, p =

.04, or race-by-class, 70% [50%, 86%], c2 = 3.70, p = .05. In summary, when the real-world

signal is unambiguous, the language will accurately identify the occupations; when real-

world signal itself is around chance then the language will accurately reflect such ambiguity.


 A. Gender-by-race                                                                                                                                                                               B. Gender-by-class                                                                                                                                                                            C. Race-by-class
                     0.15                                                                                                                                                                                             0.15                                                                                                                                                                                        0.15


                                                                                                                                                                                                                                                                                                                                              investor                                                                                                                                                                investor
                                                                                                                                                                                                                                                                                                                                        advisor                                                                                                                                                                    advisor
                     0.10               Female + White                                                                                                      Male + White                                              0.10                 Female + Rich                                                                          producer                    Malearchitect
                                                                                                                                                                                                                                                                                                                                                                     + Rich                                       0.10            Black + Rich                                                               producer            White + Rich
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 architect
                                                                                                                                                                                                                                                                                                                                                         developer                                                                                                                                             developer
                                                                                                                                                                                                                                                                                                                               jeweler
                                                                                                                                                                                                                                                                                                                                   analyst                                                                                                                                                 jeweler            analyst
                                                                                                                                                                         architect                                                                                                               realtor                                                                                                                                                                                                                        realtor
                                                                                                                                                                               engineer                                                                                      skincare              concierge
                                                                                                                                                                                                                                                                                               designer                                                                                                                                                                                         skincare                     concierge
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               designer
                                                                                         dishwasher
                                                                                          designer
                                                                                             realtor
                                                                                               concierge                               servermanager
                                                                                                      cook                                                                                                                                                                                            host                             lawyer                                                                                                                                                       host            lawyer
                                                                                                                                           chef investorprogrammer                                                                                                                                                  editor                                                                                                                                                                         editor
                                                                                                     insurer      assembler                                   physicist                                                                                                                                          photographer
                                                        receptionist                                                          accountantadvisor
                                                                                                                                                        chemist                                                                                                                                                            trainerclergy                      cabinetmaker                                                                                        clergy
                                                                                                                                                                                                                                                                                                                                                                                                                                                               cabinetmaker                     trainer photographer
                                                                                                         salesperson   dentist             technician
                                                                                                                                         lawyer            developer                                                                                                                                           author                                                                                                                                                                                  author
                     0.05                                                                                                                                                                                             0.05                                                                                                                                                                                        0.05
                                                                                                                baker
                                                                                                                 photographerproducer   pilot      ceo
                                                                                                                                                   inspector mechanic                                                                                                                                                                     professor
                                                                                                                                                                                                                                                                                                              journalistwriteradministrator                                                                                                                                                            professor
                                                                                                                         broadcaster                       electrician                                                                                                                                                                        logger
                                                                                                                                                                                                                                                                                                                                     serverpainter
                                                                                                                                                                                                                                                                                                                                                 ceo printer                 engineer                                                                                       logger                   writerjournalist
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            administrator      painterceo      server
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  engineer
                                                                        hygienist
                                                                                                                       radiologist
                                                                                                              journalist
                                                                                                        underwriter
                                                                                                                 translator
                                                                                                                      pharmacist
                                                                                                                               coach  analystpainterwaiter                                                                                                                                curator   extractor                            chef                physicist
                                                                                                                                                                                                                                                                                                                                                         guard                                                                                                            curatorextractor printer guard                physicist
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              chef
                                             nurse                         therapist                                                        tailor
                                                                                                                                      biologist
                                                                                                                                     courierprofessor     guard
                                                                                                                                                    statistician                                                                                                                                                        broadcaster
                                                                                                                                                                                                                                                                                                        underwriter pipelayer                            programmer        actor                                                                         pipelayer                                        actor
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             broadcaster
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          underwriter    programmer
                                                          caregiver
                                          waitress dietitian                                       veterinarian       assistant
                                                                                                            investigator
                                                                                                               author   chiropractor
                                                                                                                                judge                plumber                actor                                                                                                                           instructor                    tailor                                                                                                                                                   instructortailor
                   actress                                          childcare                     psychologist
                                                                                                       cashier
                                                                                                            instructor
                                                                                                                    HR    writer           police
                                                                                                                                             announcer
                                                                                                                                         welder
                                                                                                                                  installer     driver                                                                                                                                                                radiologist
                                                                                                                                                                                                                                                                                                                  assembler
                                                                                                                                                                                                                                                                                                                  artist     accountant     manager                                                                                                                                             artist       radiologist    manager
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        assembler
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     accountant
                                                                          skincare                              shipper            emt
                                                                                                                               packer                                                                                                                                    paralegal                            appraiser       coach
                                                                                                                                                                                                                                                                                                                                 detective                                                                                                                                                     appraiser coach
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              paralegal
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detective
                                                                        paralegal
                                                                                                                    editor
                                                                                                                   taper
                                                                                                 secretary appraiser
                                                                                                  host            artist          administrator butcher
                                                                                                                              bartender
                                                                                                                            trainer
                                                                                                                         paramedic                       printer
                                                                                                                                                                                                                                                                                                 secretarytourguidetaper
                                                                                                                                                                                                                                                                                                                    HR         timekeeper
                                                                                                                                                                                                                                                                                                                                    biologist                                                                                                                             timekeeper tourguide    taperHR
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               secretary biologist


                                                                                                                                                                                                 Class Difference                                                                                                                                                                              Class Difference
                                                                                                                                                                                                                                                                                                                      dentist           agriculturalist                                                                                           agriculturalist                                                    dentist


 Race Difference
                                     maid                             hairdresser                           pathologist          jeweler                                                                            actress                                                                                                                                                                                                                                                                         actress
                                                                                            teacher                 recycler tutor  clerk
                                                                                                                                   detective  roofer machinist    carpenter                                                                                                                                          assistantjudge                                                                                                                                                                   assistant
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       judge
                                                                                   masseuse                tourguide           landscaper                                                                                                                                                                                                              chemist                                                                                                                                                          chemist
                                                                                        counselorextractor                                                postman
                                                                                                                                                       musician                                                                                     dietitian                                        insurer shipper   chiropractor  drafter
                                                                                                                                                                                                                                                                                                                                installer             musician                                                                                                                      musician shipper
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    drafter           dietitian
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   chiropractor
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    installer             insurer
                                                                                                                                       drafter firefighter                                                                                                                                                               surveyer
                                                                                                                                                                                                                                                                                                                 translator
                                                                                                                                                                                                                                                                                                         salesperson                                                                                                                                        surveyer                                        translator
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   salesperson
                     0.00                                                                                                                                                                                             0.00                                                                                                                                                                                        0.00
                                                                                                                                                                                                                                                                                                  psychologist                                                                                                                                                                                  psychologist
                                                                librarian                      teller                             timekeeperlogger                                                                                                                                        dishwasher                        tutor courierannouncer statistician                                                                                                                              tutorpacker
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   announcer
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      statistician
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          courier             dishwasher
                                               manicurist                            curator                                                                                                                                                                                therapist
                                                                                                                                                                                                                                                                         hygienist masseuse                keyer    recyclerpacker
                                                                                                                                                                                                                                                                                                            investigator                       driver
                                                                                                                                                                                                                                                                                                                                         technician                                                                                                   keyer                           masseuse
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          recycler       therapist
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      driver
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   investigator
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           hygienistechnician
                                                                                                                                                                                                                                                manicurist       librarian                            cook              metalworker police                      mechanic                                                                           metalworker            manicurist
                                                                                                                                                                                                                                                                                                                                                                                                                                                                              librarian               police mechanic cook
                                                                                                                                                          barber                                                                                                                             teacher                          landscaper          inspector                                                                                                                           landscaper
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           teacher                inspector
                                                                                  phlebotomist                                     ironworkerjanitor
                                                                                                                                     clergy                    cabinetmaker                                                                                                                                          pharmacist pilot                   machinist                                                                                                                       machinist welder  pharmacistpilot
                                                                                            bookkeeper
                                                                                   fundraiser                     stocker                                                                                                                       dressmaker                                                                             welder                                                                                                        dressmaker
                                                                                   abstractor                             surveyer         highwayman                                                                                                                                                           baker                                     electrician                                                                                                                                           electrician
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     baker
                                                                                                                         pipelayer                                                                                                    maid                            hairdresser                                                                     butcher                                                                                                                                    butcher
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          hairdresser
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              maid
                                                                                                                           logistician
                                                                                                                     taxidriver                                                                                                                                                                             pathologist bartenderhighwayman                                                                                                               highwayman                     pathologist
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               bartender
                                               dressmaker                                 drycleaner                                                                                                                                                                                abstractor     veterinarian                                       waiter
                                                                                                                                                                                                                                                                                                                                                    plumber                                                                                               abstractor                                           waiter
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     veterinarian
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       plumber
                                                                                                           keyer         metalworkeragriculturalist   laborer                                                                                                                                  teller                                                    barber                                                                                                        barber teller
                     −0.05                                                                                                                                                                                            −0.05                                                                                                                                                                                       −0.05
                                                                                       busdriver                                                                                                                                                         receptionist                                                                                                                                                                                                                                                 receptionist
                                                                                                                                                                                                                                                                                         counselor
                                                                                                                                                                                                                                                                                   phlebotomist                                  ironworker
                                                                                                                                                                                                                                                                                                                                  clerk                                                                                                                         ironworker
                                                                                                                                                                                                                                                                                                                                                                                                                                                              phlebotomist           counselor
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            clerk
                                                                                                                                                                                                                                                                                             bookkeeper           stocker                                                                                                                                       stocker
                                                                                                                                                                                                                                                                                                                                                                                                                                                             bookkeeper
                                                                                                                                                                                                                                                                                    fundraiser                                              roofer               carpenter                                                                                    fundraiser                carpenter
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           roofer cashier
                                                                                                                                                                                                                                              nurse                                     busdriver      cashier taxidriver                                                                                                                          busdriver
                                                                                                                                                                                                                                                                                                                                                                                                                                                        taxidriver                                           nurse
                                                                                                                                                                                                                                                                                           drycleaner                                         firefighter                                                                                            drycleaner                   firefighter
                                                                                                                                                                                                                                           waitress                                                                             emt                  laborer                                                                                        laborer                                             waitress
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      emt
                                                                                                                                jailer                                                                                                                                childcare                                            logistician                                                                                                                  logistician                            childcare
                     −0.10               Female + Black                                                                                                     Male + Black                                              −0.10               Female +   Poor                                                                                                     Male + Poor                                         −0.10           Black + Poor                                                                                   White + Poor
                                                                                                                                                                                                                                                 caregiver                                                               paramedic                                                                                                                                                               caregiver
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            paramedic

                                                                                                                                                                                                                                                                                                                               jailer        janitor                                                                                     jailer                   janitor
                                                                                                                                                                                                                                                                                                                                                       postman                                                                                                                     postman


                     −0.15                                                                                                                                                                                            −0.15                                                                                                                                                                                       −0.15


                             −0.15                     −0.10                       −0.05                        0.00                         0.05                        0.10             0.15                                −0.15                     −0.10                      −0.05                        0.00                         0.05                      0.10             0.15                              −0.15       −0.10       −0.05                          0.00                           0.05                         0.10   0.15

                                                                                                        Gender Difference                                                                                                                                                                               Gender Difference                                                                                                                                                   Race Difference


Figure 2. Language-based occupation stereotypes from FISE applied to static
embeddings. Each panel represents the specific occupations associated with each
intersectional quadrant in the contrast of (A) Gender-by-race, (B) Gender-by-class, or (C)
Race-by-class. Interactive scatterplots are available to zoom in on specific quadrants:


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                           11


https://osf.io/b9nmd/?view_only=f0b512840ad6488fb276cc3a48e09ddd. Analogous plots for
the other five methods and data sources are provided in SI Appendix.


                  Study 2: Intersectional Stereotypes of Trait Adjectives

       Study 1 shows that FISE can accurately identify both how many (the relative

frequency) and which (the extreme classifications) occupations are stereotyped into

intersectional quadrants. Thus, in Study 2 we are on firmer ground to expand the scope to

consider intersectional stereotypes with trait adjectives, which provide no ground-truth data

(i.e., we have no objective data on whether men or women, rich or poor, Black or White are

more honest or hardworking). And yet, trait adjectives are the quitessential carriers of

stereotypes and are consistently used in research on person or group perception. Study 2 also

expands the research scope to demonstrate the flexible application of FISE across

contextualized embedding models (BERT17), and identifies where conclusions converge or

diverge across models, as well as what divergences teach us about how these models

represent language and society.

Results

       Frequency of intersectional trait stereotypes. In the primary case of static

embeddings, there is clear evidence of both androcentrism and ethnocentrism, such that any

intersection including Men (versus Women) or White (versus Black) dominates in language

(Table 3). Indeed, the highest relative frequency of traits occurred for White Men, associated

with 59% of traits; the lowest relative frequency of traits occurred for Black Women, which

was associated with only 5% of traits. As reported in the SI Appendix, the imbalances in trait

frequencies (e.g., the dominance of White Men over Black Women) deviated significantly

from chance, with effect sizes ranging from V = [0.26, 0.56], equivalent to small-to-moderate

effect sizes. Thus, language reveals evidence of intersectional dominance for powerful groups

and intersectional invisibility for subordinate groups.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                                                                                                                                                                                                                                                                                                                                                          12


                                 Interestingly, the data show less support for class-centrism, i.e., rich does not

dominate poor in language to the same extent that White supersede Black, or men supersede

women in trait frequencies. For example, Black Poor (6% of traits) and Black Rich (5% of

traits) are similar in frequency showing that the low frequency of traits associated with Black

is not altered even after including the dominant class group Rich. Perhaps class may be less

of a marked category in language: we may be unlikely to point out that someone is rich,

unless it is extreme wealth, because categorizing class is prone to subjective judgments of

wealth cues28. In contrast, race and gender may be relatively less ambiguous in

categorizations and therefore more likely to be noted in language and to shape trait

frequencies.


 A. Gender-by-race                                                                                                                               B. Gender-by-class                                                                                                                            C. Race-by-class
                                                                                                                                                                                                                                                                                                                  0.2


                   0.2                                                                                                                                              0.2
                                                                                                                                                                                                                                                                                                                                Black + Rich                                              intellectual
                                                                                                                                                                                                                                                                                                                                                                                                                        White + Rich
                                                                                                                                                                                                                                                                                                                                                                                         loyal
                                                                                                                                                                                                                                                                                                                                                                                                 knowledgeable smart
                           Female + White                                                                               Male + White                                         Female + Rich                                                  intellectual
                                                                                                                                                                                                                                                       loyal
                                                                                                                                                                                                                                                                           Male + Rich                                                                                                       intelligent
                                                                                                                                                                                                                                                                                                                                                                                                              romantic
                                                                                                                                                                                                                                                                                                                                                                                                         arrogant
                                                                                     friendly                                                                                                                                           knowledgeable
                                                                                                                                                                                                                                          smart
                                                                                                                                                                                                                                          intelligent                                                             0.1                                                 sensual femininepeaceful relaxed                     friendly
                                                                                   happysmartstupid                                                                                                         romantic                                                                                                                                                                thoughtful confident
                                                                                                                                                                                                                                                                                                                                                                                 energetic
                                                                                                                                                                                                                                                          arrogant                                                                                                               gracious
                   0.1                                                       pleasant kind                                                                          0.1               feminine sensual                             friendly                                                                                                                                               adventurous
                                                                                                                                                                                                                                                                                                                                                                             discriminating           brilliant
                                                                                                                                                                                                                                                                                                                                                                                             enthusiastic
                                                          romanticwarm                                                                                                                                                          peaceful
                                                                                                                                                                                                                            relaxed                                                                                                                                                     generous  greedy
                                                                   carefree rude    helpful                arrogant                                                                                                          thoughtful
                                                                                                                                                                                                                         energetic
                                                                                                                                                                                                                         gracious  confident                                                                                                                                                       reliable pleasant
                                                                                                                                                                                                                                                                                                                                                                                               playful
                                                                     jealous relaxed       cleverhonest
                                                                                        knowledgeable    jolly                                                                                                          discriminating           brilliant                                                                                                              spirited talented
                                                                                                                                                                                                                                                                                                                                                                                       trustworthy
                                                                                   confident     brilliant                                                                                                             adventurous
                                                                                                                                                                                                                                 enthusiastic
                                                                                                                                                                                                                                 generous     greedy                                                                                                                                    gentle
                                                                                                                                                                                                                                                                                                                                                                                        witty
                                                                                                                                                                                                                                                                                                                                                                                           hostile
                                                                                                                                                                                                                                                                                                                                                                                             original clever       kind
                                                                               accurate       greedy
                                                                                          reliable
                                                                                       grumpy
                                                                   cheerfulirresponsible   weak                                                                                                             playful
                                                                                                                                                                                                           spirited         pleasant      reliable
                                                                                                                                                                                                                                              trustworthy                                                                                                                              dependable           carefree
                                                           playful
                                                           fussy  lonely         enthusiastic
                                                                       adventurous          brave
                                                                                          intelligent
                                                                                  optimistic
                                                                                    wasteful
                                                                                      angry
                                                                                          original
                                                                                            intellectual                                                                                                                 talented
                                                                                                                                                                                                                          gentlewitty
                                                                                                                                                                                                                                    hostileclever
                                                                                                                                                                                                                                          original
                                                                                                                                                                                                                                          kind                                                                                                                                                               warm
                                                                                peaceful
                                                                       unfriendly
                                                                 depressed        obnoxious
                                                                                 generous     trustworthy
                                                                                          dependable
                                                                                    hostile                                                                                                                        carefree               dependable                                                                                                                 manipulative                accuratehonest
                                           sexy                          cranky
                                                                          gentlewitty
                                                                            inconsiderateincompetent   loyal                                                                                                          warm                                                                                                                                          conceited   affectionate
                                                                                                                                                                                                                                                                                                                                                                               bossy
                                                                                                                                                                                                                                                                                                                                                                       resourceful       sexy
                                                                insecure      thoughtful
                                                                                 humorous cowardly
                                                                                unreliable                                                                                                                                     accurate
                                                                                                                                                                                                        manipulative affectionate                honest                                                                                                                            tense optimistic    jealous
                                    feminine                                 heartless
                                                                          talented
                                                                         energetic
                                                                         gracious
                                                                               cruel
                                                                         affectionate
                                                                           tense
                                                                               negligent
                                                                        discriminating                                                                                                      sexy    bossy           resourceful
                                                                                                                                                                                                                     jealous          conceited                                                                                                              prejudiced


 Race Difference                                                                                                                                 Class Difference                                                                                                                              Class Difference
                                                  bossy          irritable
                                                                 compassionate           dishonest
                                                                                       grim                                                                                                                               tense   optimistic
                                                                                                                                                                                                                               prejudiced                                                                                                                                 unethical                                    happy
                                                                        hopeful
                                                                      abusive   charitable
                                                                                     truthful
                                                                         disrespectful unethical                                                                                                                                   happy
                                                                                                                                                                                                                                       unethical                                                                                                               courageous
                                                                                                                                                                                                                                                                                                                                                         scornful  immoral          humorous
                                                             helpless   fearful
                                                          spiritedresourceful                                                                                                                                                   courageous
                                                                                                                                                                                                                                 humorous                                                                                                                               compassionate
                                             sensual manipulative                     conceited
                                                                                       stingy
                                                                                                                                                                                                                       scornful
                                                                                                                                                                                                                  compassionate immoral
                                                                                                                                                                                                                                    helpful
                                                                                                                                                                                                                                    wasteful                                                                                                                                                  wasteful helpful
                                                 spiteful            unkind deceitful
                                                                                immoral
                                                                                courageous                                                                                                                                               dishonest jolly
                                                                                                                                                                                                                                     truthful
                                                                                                                                                                                                                                  obnoxious                                                                                                                                   dishonestobnoxious
                                                                                                                                                                                                                                                                                                                                                                             truthful                    jolly
                   0.0                                        uncooperative
                                                                        glum   prejudiced                                                                           0.0                                                       irresponsible                                                                       0.0                                                                      irresponsible
                                                                                                                                                                                                                   cheerfuldeceitful brave
                                                                                                                                                                                                                       unfriendly                                                                                                                                  deceitful                    cheerful
                                                                                                                                                                                                                                                                                                                                                                                                brave
                                                                                                                                                                                                                                               cowardly                                                                                                                                  unfriendly
                                                                       scornful disorderly
                                                                   lifeless                                                                                                                        spiteful fussy
                                                                                                                                                                                                                                charitable
                                                                                                                                                                                                                            heartless
                                                                                                                                                                                                                        fearfulcruel   stingy
                                                                                                                                                                                                                                 insolentincompetent                                                                                                                  stingy       cowardly
                                                                                                                                                                                                                                                                                                                                                                            charitable
                                                                                                                                                                                                                                                                                                                                                                                  heartless   fussy
                                                                                                                                                                                                                                                                                                                                                                                     incompetent
                                                                                 insolent                                                                                                                                disrespectful stupid
                                                                                                                                                                                                                              negligent
                                                                                                                                                                                                                                                                                                                                                      insolent     spitefulfearful cruel
                                                                                                                                                                                                                      abusive
                                                                                                                                                                                                                        hopefulrude   angry                                                                                                                            disrespectful
                                                                                                                                                                                                                                                                                                                                                                                negligent                            stupid
                                                                                                                                                                                                                                                                                                                                                                            abusive
                                                                                                                                                                                                                                                                                                                                                                             hopeful          angry          rude
                                                                                                                                                                                                                 insecure              grimweak
                                                                                                                                                                                                                           inconsiderate
                                                                                                                                                                                                                         cranky                                                                                                                                                      insecure weak
                                                                                                                                                                                                                     unkind            grumpy                                                                                                                                   grim
                                                                                                                                                                                                                        glum                                                                                                                                                        inconsiderate
                                                                                                                                                                                                                                      disorderly                                                                                                                   unkind                cranky
                                                                                                                                                                                                               uncooperative    unreliable                                                                                                                                                     grumpy
                                                                                                                                                                                                                                                                                                                                                                 glum
                   −0.1                                                                                                                                             −0.1                                           irritable
                                                                                                                                                                                                                   depressed                                                                                                                              disorderly
                                                                                                                                                                                                                                                                                                                                                             uncooperative          unreliable
                                                                                                                                                                                                                                                                                                                  −0.1                                                          irritabledepressed
                                                                                                                                                                                                                    lifeless
                                                                                                                                                                                                                  lonely
                           Female + Black                                                                                   Male + Black                                     Female + Poor                      helpless                                                   Male + Poor
                                                                                                                                                                                                                                                                                                                                                           lifeless                          lonely

                   −0.2                                                                                                                                             −0.2
                                                                                                                                                                                                                                                                                                                                Black + Poor                                helpless                                    White + Poor

                                                                                                                                                                                                                                                                                                                  −0.2


                          −0.2             −0.1                                0.0                                    0.1                  0.2                             −0.2            −0.1                                0.0                                   0.1                 0.2                             −0.2                  −0.1                   0.0                                       0.1                    0.2

                                                                      Gender Difference                                                                                                                             Gender Difference                                                                                                                        Race Difference


Figure 3. Language-based trait stereotypes from FISE applied to static embeddings.
Each panel represents the specific traits associated with each intersectional quadrant in the
contrast of (A) Gender-by-race, (B) Gender-by-class, or (C) Race-by-class. Interactive online
scatterplots are available to zoom in on specific quadrants and traits:
https://osf.io/b9nmd/?view_only=f0b512840ad6488fb276cc3a48e09ddd. Analogous plots for
the other five methods and data sources are provided in SI Appendix.

                                 Qualities of intersectional trait stereotypes. As in Study 1, our next analyses go

beyond the overall number of traits to consider the specific traits and their qualities.

Specifically, we consider six qualities of traits that are of foundational interest to group

perception24: (1) valence; (2) dominance; (3) arousal; (4) warmth; (5) competence; and (6)

commonality (how often a given trait is used in everyday contemporary language). To

examine such qualities, we ensure that each quadrant has relatively similar representation in


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                                                                                                                                                                                          13


number of traits, as this control allows us to compute the relative qualities of intersectional

groups independent of their imbalance of representation. Additionally, this control is required

to ensure that even low-frequency quadrants (e.g., Black Rich, associated with only 5 traits)

have sufficient representation to examine the relative qualities. Thus, we first mathematically

adjust the frequencies across quadrants by z-scoring the placement of each trait along

individual group dimensions and compute each quadrant’s average scores of the traits’

qualities. Crucially, even after re-scaling the number of traits across quadrants, the features of

those traits continue to show intersectional differences (Table 3 for GloVe 840B; results for

all embeddings in SI Appendix).

                                 First, intersections differed in their relative proportion of positive/negative traits

(Figure 4; Table 3). For example, 81% of traits associated with White Rich were positive;

while only 17% of traits associated with Black Poor were positive. In general, valence

imbalances appeared to be largest across class (Rich/Poor).


 A                                                                                        B                                                                                        C
                   3                                                                                         3                                                                                        3
                             Positive   Negative                                                                       Positive   Negative                                                                      Positive   Negative


                   2
                        Female + White                                 Male + White                          2
                                                                                                                  Female + Rich                                  Male + Rich                          2
                                                                                                                                                                                                                Black + Rich                              White + Rich

                   1                                                                                         1                                                                                        1


 Race Difference                                                                          Class Difference                                                                         Class Difference
                   0                                                                                         0                                                                                        0


                   −1                                                                                        −1                                                                                       −1


                   −2   Female + Black                                 Male + Black                          −2   Female + Poor                                  Male + Poor                          −2        Black + Poor                              White + Poor

                   −3                                                                                        −3                                                                                       −3


                        −3         −2     −1          0            1        2         3                           −3         −2     −1          0            1        2        3                           −3         −2       −1         0           1        2         3

                                               Gender Difference                                                                         Gender Difference                                                                          Race Difference


Figure 4. Valence of traits (after z-scoring) associated with intersectional comparisons
of gender-by-race (A), gender-by-class (B), and race-by-class (C). Traits are color-coded
by valence (positive is red, negative is green. All figures use data from the GloVe Common
Crawl 840-billion data source of static embeddings. Analogous plots for the other five
methods and data sources are provided in supplemental materials.

                                 Second, traits differ in word arousal (degree of “activity” evoked by the trait) and

dominance (degree of “control” evoked by the trait29) as well as qualities of warmth/coldness

and competence/incompetence24. For warmth/coldness, competence/incompetence, and


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                14


dominant/non-dominant traits, results paralleled valence: intersections including powerful

groups of White, Rich, or Men were not only more likely to be positive, but were also more

likely to be associated with traits expressing warmth, competence, and dominance (Table 3).

As one example, for Rich White, 81% of traits were warm, 81% were dominant, 78% were

competent. In contrast for Poor Black, 83% of traits were cold, 83% were subordinate, 79%

were incompetent. Such findings emphasize the “halo effects” (i.e., the unwarranted

generalization of positivity across multiple dimensions30) that become amplified for powerful

intersectional groups. Only the dimension of arousal did not differentiate across intersectional

groups, perhaps because this dimension is often seen as a less central dimension of meaning29

and thus may not be as relevant to distinguish between social categories.

       Finally, intersectional quadrants also differed in how common the associated traits

were in everyday language, using commonality scores (as Zipf scores, see Methods) taken

from the wordfreq norms in Python31. Traits associated with any White, Men, or Rich

intersection were more commonly used in language than traits associated with any Black,

Women, or Poor intersection (Table 3). For instance, the traits associated with Rich Men had,

on average, 10,232 occurrences per billion words (Zipf = 4.01, equivalent to 104.01). In

contrast, the traits associated with Poor Women had, on average, 3,020 occurrences per

billion words (Zipf = 3.48, or 103.48 occurrences), corresponding to roughly one-third the

commonality of Rich Men traits. Imbalances in commonality reveal further andro-, ethno-,

and class-centrism in language. When it comes to our most common traits (e.g., friendly,

happy, smart), powerful groups dominate; subordinate groups, by contrast, are relegated to

description with more idiosyncratic traits (e.g., manipulative, spiteful, spirited) that may, in

turn, contribute to perceptions of non-prototypicality.

       Differences between static and contextualized embeddings. So far, we have focused

on describing the general pattern of results for static embedding models, which remain the


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                               15


most widely used method in the social sciences. However, given the flexibility of FISE

procedure we can also compare results across contextualized embeddings from BERT. That

is, we can compare the results of the relative frequencies of traits classified into intersectional

quadrants (e.g., how many traits are classified as associated with White Men) across multiple

static embeddings from various algorithms (fastText and GloVe) and data sources (Wikipedia,

Common Crawl), but also across contextualized embeddings with additional variations in

embedding extraction methods (SI Appendix).

       The frequencies of classified traits across six different models and methods are listed

in Table 3. Chi-squared tests evaluating how similar these frequencies are across methods

showed small overall effect sizes, implying that static and contextualized models generally

reveal similar patterns of frequencies: for race-by-class, c2 (15) = 59.02, p < .001, V = 0.18;

for gender-by-class, c2 (15) = 64.23, p < .001, V = 0.19; and for race-by-gender, c2 (15) =

100.03, p < .001, V = 0.24.

       Nevertheless, we identify one seemingly systematic difference between results for

static and contextualized embeddings when it comes to the gender-by-class and gender-by-

race comparisons. For static embeddings, whenever gender was included, the greatest

frequency (as well as positivity, commonality, etc.) was associated with the default group

(e.g., Rich Men)32. Such patterns of “default” group dominance reflect the ground-truth of

how groups dominate in the world (see Study 1). For contextualized embeddings, however,

the greatest frequency (and positivity and commonality) was associated with the

intersectional grouping that joined female (a lower-power group compared to male) with a

higher power class group (e.g., Rich Women). Perhaps, in contextualized embeddings, group

information is considered more jointly since the group labels are provided together in a single

sentence. Thus, seemingly incongruent pairings of high-power female groups are more easily


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                             16


noted and “marked” in the model 8. This marking could increase the frequency of traits

associated with the group.

                                      General Discussion

   Computational and social sciences have both increasingly recognized the need for

intersectional approaches to understand social biases and their impact 33–35. And yet, despite

the call for more intersectional research there remains, to our knowledge, no methodological

approach that can provide a simple, flexible, and transparent approach to quantifying

intersectional stereotype content, at-scale in massive language data. Here we introduce such a

method for interdisciplinary research – the Flexible Intersectional Stereotype Extraction or

FISE procedure. Applying FISE to a first case study of intersectional stereotypes across

occupations and personality traits at the intersection of gender, race, and social class, a

primary aim was to illustrate the kinds of empirical insights that can come from this new

methodological approach. Although many of the nuanced findings about individual

groupings, traits, and occupations remain beyond the scope of this first analysis, below we

emphasize four overarching empirical conclusions that help propel intersectional analyses:

(1) the alignment of intersectional stereotypes in language with ground-truth data,

emphasizing how language both reflects and reinforces social patterns; (2) the language

dominance (frequency) of powerful intersectional groups, as well as the relative invisibility

of subordinate intersectional groups; (3) the “halo effects” that surround powerful

intersectional groups, especially those involving high social class; and (4) informative

divergences (and convergences) between static and contextualized language models.

Frequencies of intersectional occupational stereotypes: alignment with ground-truth data

       In Study 1, we sought to validate FISE by showing that results of intersectional

occupation stereotypes identified from language align with ground-truth on actual

occupational demographics of those occupations. In addition to the relevance of occupational


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                             17


stereotypes for understanding workforce discrimination in hiring and pay26,36, occupational

stereotypes also provide a necessary setting for validating a new method because they have

associated ground-truth data on demographic representations. Indeed, classifications of 143

occupations into their intersectional quadrants showed evidence that FISE validly identifies

true signal from real-world data. First, intersectional quadrants that dominated in the real-

world data (e.g., White Men were associated with the most occupations in the real-world) also

dominated in language associations. Second, when specific occupations provided clear signal

in ground-truth data (e.g., they were >70% female and >70% White), language associations

correctly classified the occupation into the specific intersectional quadrant (e.g., as White

Women). When specific occupations provided ambiguous signal (e.g., female representation

was ~50%), the language also showed that ambiguity (e.g., showed incorrect classifications

of gender), thus providing an accurate reflection of the signal in reality.

       Beyond validation of FISE, such results also illustrate new insights and opportunities

for future research on the intersectionality of workforce demographics. For instance, as

elaborated below, the dominance of a group in language can, in turn, feed back into

legitimizing the group’s dominance in the world37. The dominance of White Men or Rich Men

in the language of occupations may hamper other strategies to create change in workforce

demography38. Given the flexibility of FISE for examining intersectionality across historical

language corpora, future research can now, for the first time, examine such questions of how

occupation stereotypes in language hinder or help changes in workforce demographics.

Frequencies of intersectional trait stereotypes: the dominance of powerful groups

   Having provided initial validation of the accuracy of FISE, we can turn to trait-based

stereotypes, a domain that has no ground-truth data but underlies the content of most group

stereotypes24,39. These frequencies of traits uncovered clear patterns of androcentrism, or the

dominance of Men in everyday culture and language, a finding that we and others have


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                               18


documented and discussed, albeit at smaller scales40,41. However, the current work is among

the first to also emphasize the extent of ethno-centrism, or the dominance of Whiteness in

Internet text. Such findings add new quantitative evidence to past qualitative theorizing on

the White “default” in culture42 and show that it is of the same scale as the masculine defaults

seen in previous work.

   Ultimately, the dominance of both Men and Whiteness in language patterns will not only

have downstream consequences in AI and language applications (e.g., in machine translation,

text classification, and text generation), but also can serve to reify mental stereotypes about

which groups should dominate in society. For example, experimental research has shown that

the frequency of women versus men in Google search outputs shapes beliefs about the default

“person” as well; cultures that have greater male-dominated search outputs, more strongly

endorse androcentric defaults37. In short, the current results may play into a feedback loop in

which language both reflects and reinforces existing social imbalances – imbalances that

become especially magnified in intersectional comparisons6,43.29

Qualities of intersectional trait stereotypes: halo effects

   Beyond frequency, we also consider the intersectional differences in the qualities of the

stereotype content, specifically the average positivity, warmth, competence, dominance, and

commonality (i.e., how common the traits are in everyday language use). Results show that

any intersection that included Rich, and, to a lesser extent, White or Men, consistently

anchored the positive end of the spectrum (e.g., positive, warm, competent). Notably, class

was the strongest dimension determining the qualities of traits, with Rich generating “halo

effects” 44 across all qualities. This may be surprising considering explicit measures

suggesting that stereotypes of Richness often generate mixed content (e.g., competent but

also cold 24,45). However, evidence of “halo effects” are especially likely to be observed with

relatively indirect measures of stereotyping30,46, as in the current research.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                              19


Comparison of static and contextualized models

       As its name suggests, the primary advantage of the FISE procedure is its flexibility

for application across any embedding model, including both static (GloVe) and

contextualized models (BERT) trained on diverse Internet data sources. Critically,

emphasizing the robustness of primary conclusions, results within all static models were

consistent with one another (i.e., all showed similar patterns of the relative frequencies and

features of traits), and results within all contextualized embedding approaches were

consistent with one another. Additionally, static and contextualized models agreed for

frequencies and features of traits in the class-by-race contrast, with White Rich consistently

associated with the most traits and the most positive traits, regardless of method.

       At the same time, however, the few divergences between static and contextualized

approaches were also informative. Static embeddings seem to capture the dominance of

“default” powerful groups in language (e.g., White Men) in which both group dimensions

(e.g., gender and race) reflect high power. Contextualized embeddings, however, seem to

capture the “markedness”47 of incongruent non-default groups (e.g., White Women or Rich

Women), where one group dimension contains power (e.g., White, Rich), but the other group

(Female) is subordinate. Perhaps, the focus on “markedness” arises for contextualized

embeddings because of the joint consideration of all group dimensions that might more

readily highlight the unexpected (incongruent) group of “powerful females” 48. These

differences between static and contextualized models can help researchers make informed

decisions about which models to use based on their interests in default versus markedness of

subordinate groups. Additionally, future work can identify what methodological differences

between static and contextualized embeddings help explain why default versus marked

gender groups are differentially emphasized across methods.

Limitations


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                              20


   In supplemental analyses we seek to test and demonstrate the robustness of inferences

across modeling approaches (static, contextualized) and additional specifications (how groups

were represented, the numbers of traits, types of traits, verb, or noun lists; SI Appendix).

Despite general patterns of consistency and robustness, the current inferences face other

limitations. First, there are theoretical limitations: intersectionality is sometimes (but not

always) thought of as an inherently contextualized, emergent phenomenon that is non-

additive 7,35,49. Therefore, the FISE approach of crossing two (independently created) axes

from single dimensions of groups may not be an appropriate methodological assumption.

While this is an inherent limitation for addressing some theoretical perspectives, we

emphasize that the general results were broadly convergent across contextualized and static

approaches. Thus, the FISE procedure (even applied to static embeddings) appears to be

sufficient to approximate a contextualized process of intersectionality.

   Additionally, FISE relies on representing group and attribute concepts in text. Especially

in the case of static embeddings (where group concepts are lists of single words rather than

contextualized sentences), the results remain limited by concerns around polysemy (e.g.,

Black and White also refer to colors), and frequency (e.g., some group words like

impoverished are more rare than everyday words like men). Here and in previous work12 we

have attempted to rule out concerns of polysemy by using lists of words that, together,

triangulate towards the intended group concept, and have shown that this list-based approach

indeed captures the group concept rather than alternative polysemous meanings. Moreover,

here we show that even two different ways of representing the group concepts (with lists of 4

or 12 words) yield similar overarching conclusions (SI Appendix).

   Finally, we note that readers may question the relevance of FISE at a moment when the

current static embeddings and BERT contextualized embeddings are surpassed by more

sophisticated language model competitors. We see the approach as holding continued


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                         21


relevance because static embedding models will continue to be used for their wide

availability, transparency, and flexibility for training on diverse (and relatively small)

datasets. As such, demonstrating methods to extend static and simple contextualized models

for intersectional analyses is crucial. Even in the unlikely scenario of GPT and large language

models (LLMs) replacing all text analysis, the FISE approach represents a general stepwise

“recipe” that can be flexibly extended to LLM settings as well.

    Ultimately, we look forward to future research using FISE as the necessary

interdisciplinary infrastructure for addressing such questions, especially on the prevalence

and features of emergent content (not contained in parent group stereotypes). With such tools,

the study of intersectionality and emergence can be expanded in real-world language at an

unprecedented scale, even across place, languages, demographics, and history.


Table 1.
Percentage of occupations in each intersectional grouping (quadrant) for static embeddings
and ground-truth data (non-z-scored)
                                                 Ground-truth      Static embeddings
                 Intersectional grouping
                                             categorizations (BLS) (GloVe CC 840B)
                      White + Rich                     53                  46
                      White + Poor                     33                  33
                       Black + Rich                    2                    6
                      Black + Poor                     13                  15
                       Male + Rich                     33                  42
                       Male + Poor                     24                  29
                      Female + Rich                    21                  10
                     Female + Poor                     21                  20
                      Male + White                     48                  59
                      Male + Black                     10                  12
                     Female + White                    37                  20
                     Female + Black                    5                    9
Note. Occupation frequencies represent the percentage of occupations (out of 143 possible occupations) that are
associated with each intersectional grouping (e.g., the White Men grouping is associated with 59% of
occupations in language). Bolded numbers indicate the highest relative percentage for each intersectional
quadrant.


Table 2.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                                      22


Percentage of traits in each intersectional grouping (quadrant) across embedding methods
(non-z-scored)
                                 Static embeddings                          Contextualized embeddings
  Intersectional       GloVe  GloVe               fastText        Single words       Pooled words Pooled words
    grouping          CC 840B Wiki 6B             Wiki 2M         with template      with template no template
  White + Rich              57          42            37               59                   69                43
  White + Poor              32          26            28               28                   22                29
  Black + Rich              5           7               6              1                    0                 3
  Black + Poor              6           25            29               12                   9                 25
   Male + Rich              44          33            23               22                   30                16
   Male + Poor              21          23            32               11                   7                 20
  Female + Rich             18          16            20               38                   39                30
 Female + Poor              17          28            25               29                   24                34
  Male + White              59          47            39               26                   35                27
  Male + Black              6           9             16               7                    2                 9
 Female + White             30          21            26               61                   56                45
 Female + Black             5           23            19               6                    7                 19
Note. Trait frequencies represent the percentage of traits (in this case out of 100 possible traits) that are
associated with each intersectional grouping (e.g., the White Men grouping is associated with 62 out of 100
traits, whereas the Black Men grouping is associated with 3 out of 100 traits). Frequencies are compared within
a data source (e.g., GloVe CC 840B) but across groupings, such that all four groupings within a data source will
add up to 100. Bolded numbers indicate the highest relative percentage for each intersectional quadrant (e.g.,
62% is bolded to reflect that White Men is the grouping with the highest relative percentage of traits across all
groupings for that data source). The three contextualized embedding columns indicate three methods for
extracting embedding vectors for groups. As described in the main text, single words with templates indicates
that a vector is created from averaging across the hidden state vectors for the template (e.g., “This is a”) and the
first sub-tokens of group words (e.g., “rich African woman”); pooled words with templates indicates that the
vector is created from averaging across the hidden state vectors for the template and the pooled group words
(pooled across sub-tokens; e.g., “rich African+American woman); pooled words no template indicates that the
vector is created from the first four layers of the hidden state vectors pooled across only the group words (e.g.,
rich African+American woman).


Table 3.
Relative percentages of trait qualities (by valence, warmth, competence, arousal,
dominance, commonality) within each intersectional quadrant for GloVe CC 840B
static embeddings.
                         Valence             Warmth          Competence           Arousal        Dominance
                                                                                                                Word
Intersectional                                                                                                common.
                 Positive    Negative   Warm      Cold      Comp    Incomp    High    Low        High   Low
   grouping
White + Rich        81             19        81    19        78       22       44      56         81    19        4.14
White + Poor        30             70        30    70        30       70       48      52         30    70        3.93
 Black + Rich       65             35        69    31        69       31       50      50         62    38        3.55
 Black + Poor       17             83        17    83        21       79       58      42         17    83        3.36
 Male + Rich        70             30        70    30        70       30       47      53         70    30        4.01
 Male + Poor        28             72        28    72        28       72       56      44         28    72        3.78
Female + Rich       78             22        83    17        78       22       48      52         74    26        3.63
Female + Poor       18             82        18    82        23       77       50      50         18    82        3.48
Male + White        58             42        58    42        58       42       52      48         58    42        4.13


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                              23

 Male + Black       41        59         41      59      41       59       50     50      41     59       3.57
Female + White      59        41         59      41      53       47       35     65      59     41       3.87
Female + Black      43        57         46      54      50       50       57     43      39     61       3.37
Note. For all columns except the last one, numbers reflect the percentage of traits from the given quadrant (e.g.,
from the intersectional grouping of White Rich) that are, for example, coded as positive (vs. negative). The
“word common” column reflects the average Zipf score across all traits in that quadrant. Zipf scores are the base-
10 logarithm of the number of times a word appears in a billion words. For instance, Zipf=4.14 for the White
Rich quadrant reflects that the traits associated with this quadrant have occurred in language 104.14 times, or
approximately 13,803 times, for every 1 billion words.


Methods

         Data availability statement. All data and analyses reported in this work are publicly

available through https://osf.io/b9nmd/?view_only=f0b512840ad6488fb276cc3a48e09ddd.

         Application of FISE to Static Word Embeddings. Our primary test case is the set of

pretrained GloVe embeddings trained on 840-billion-word tokens from the Common Crawl;

replications for static embeddings are performed across GloVe embeddings trained on 6

billion tokens from Wikipedia, and fastText embeddings trained on Wikipedia. After

choosing the text corpus, FISE proceeds in five steps. First, we identify a list of target

concepts. In Study 1, we use ~150 occupation labels generated from the 2022 Bureau of

Labor Statistics report50; occupation labels, methods for generating them, and approaches to

classify occupations into intersectional quadrants are detailed in the SI Appendix. In Study 2,

we use 100 traits drawn from a list of approximately 400 available traits51 but only the 50

most positive and 50 most negative traits based on ratings from Warriner and colleagues52;

replications with longer lists of 200 and 300 traits are reported in SI Appendix.

         Second, for each occupation/trait concept (e.g., kind) we compute cosine similarities

between the embeddings for the target word (ti) and all words representing a given group

concept (WgA e.g., Rich, which is represented by group words including rich, wealthy,

affluent, and so on; see Figure 1 for all words), and divide by the number of words in that

group representation (NgA) yielding an average word-group A association (e.g., kind-Rich

association; Formula 1). We then repeat the procedure for the contrast group (e.g., kind-

Poor). For analyses in which we use z-scored results, we standardize scores at this stage,


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                24


taking each ti score, subtracting the mean across scores, and dividing by the standard

deviation across all scores.
                                          ∑ &'( (*!" , ,# )
                                𝑡!(#) =         -!"
                                                                (1)


       Third, we take the difference between averaged cosine similarities to get the

placement of the target word along the given group dimension (e.g., kind-Rich – kind-Poor =

kind-CLASS; Formula 2) and repeat for all other dimensions of groups (in this case, also

gender and race, to also extract the kind-GENDER and kind-RACE placement).

                                𝑡!(#./) = 𝑡!(#) − 𝑡!(/)         (2)

       Fourth, we bring in the intersectional analysis by crossing two group dimensions (e.g.,

class and gender) in an x-y coordinate space and place each target word in that space

according to its association with the respective group dimensions (e.g., ti(AvB) represents the x-

axis of CLASS, while ti(CvD) represents the y-axis of RACE). This x-y space reveals the

intersectional stereotypes associated with each of the four group intersections (e.g., Rich Men,

Rich Women, Poor Men, and Poor Women). Fifth and finally, the frequency and qualities of

these associated traits/occupations is analyzed.

       Application to Contextualized Word Embeddings. The above procedure can be

adapted to most cases in which embeddings are extracted for group and trait representations,

including for contextualized embeddings, such as BERT. We demonstrate such an extension

by adapting FISE for use with the BERT base-uncased model and three previously-validated

methods for retrieving embeddings of group representations from the model (described

below). The FISE procedure for contextualized embeddings again follows five steps. First,

and different from static applications, group targets are operationalized using group sentence

probes (Figure 1) to include all three intersectional group identities at once (e.g., “This is a

rich black man”) varying class (words representing rich/poor), race (words representing

Black/White), and gender (words representing man/woman). These three group targets are


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                              25


placed in a semantically bleached template (e.g., “This is”, “That is”, and so on); templates

are semantically bleached to ensure that the extracted embedding captures the signal

associated with the main (in this case, group-related) stimulus. Attributes (in this case, we

only use traits) are also operationalized using sentence probes with the traits placed in a

semantically bleached template (e.g., “They are kind/unkind”).

       Second, to extract associations of a target word with a single group dimension (e.g.,

class) we need to average across the other dimensions (e.g., gender, race) that were used in

the original contextualized sentences. To that end, for each trait target word (e.g., kind) we

compute the average cosine similarity to a given three-way target intersection (e.g., rich white

men) as well as to the comparison target intersection that varies only on the group dimension

of interest (e.g., poor white men, when we are looking at CLASS). We then take the

difference between these two cosine similarities (e.g., kind-rich white men - kind-poor white

men = kind-CLASS white men effect). We perform this for all contrasts along the dimension

of interest to yield kind-CLASS effects for White Men, Black Men, White Women, and Black

Women. We then average across these four contrasts for a single kind-CLASS association.

Third, we repeat the above computations for a second group dimension (i.e., gender or race).

Fourth, we place each target trait in an x-y coordinate space. And fifth, we perform all

analyses of frequency and content.

       Extracting Embeddings from Contextualized Models. While static embeddings

provide the embeddings off-the-shelf, contextualized embeddings require an additional step

to extract embeddings of a given sentence. For robustness, we employ three common

approaches for extracting embeddings from the BERT model53: (1) embedding templates 18;

(2) pooled embedding templates; (3) without templates.

       First, “embedding templates”18 extracts embeddings of a given set of group words in

our embedding template (e.g, “rich” “African American” “woman” in the template “this is


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                            26


a”), by pulling the BERT embeddings of the first sub-token in the group words (e.g., “rich”,

“African” “woman”). Next, we use the hidden state vectors (only the top-most BERT layer)

of those sub-tokens and average across the three group sub-tokens (rich, African, woman).

This yields a single vector embedding for the BERT representation of the group target “rich,

African American woman” as it is contextualized in the sentence “This is a rich African

American woman.”

       Second, “pooled embedding templates,” begins as above but, instead of taking the

hidden state vectors of only the first sub-token for each group-related word, we instead take

the mean pooled embeddings of all sub-tokens of the group-related words. To continue with

our example, in the sentence, "This is a rich African American woman," we first take the

average across the hidden state vectors for “African” and “American” (the only target word

with two sub-tokens) to create a single pooled embedding vector for “African American.” We

then calculate the average across the pooled embedding of “African American” with the

embeddings of “rich” and “woman” (which were only one sub-token and so didn’t need to be

pooled) to again obtain a single vector representation of the group words in the

contextualized sentence.

       Third and finally, “without templates,” we move beyond templates, which, although

argued to be semantically bleached, may nevertheless convey information that distracts from

the target group representations. Instead of templates, we average over the pooled

embeddings for just the three group words using the first four layers of the BERT model for

each target word 54,55. Consider again the example of assessing stereotypes to “rich African

American woman,” in this setting we calculate the average of the pooled embeddings for

three group words (“rich,” “African American,” and “woman”) across the first four layers of

BERT. We do not include the embeddings of any template words in the final average.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                                27


       Robustness and sensitivity analyses. To verify the robustness and generalizability of

our results for the more novel analyses of trait stereotypes, we test 6 variations of trait and

group lists. In addition to (1) “Model 1: Full model,” in which we use the full 24 group words

for each dimension (see Figure 1) and the list of 100 traits, we also compute the following

variations: (2) “Model 2: Reduced group words” in which we change the group list to include

only the 4 most central group-related words (bolded in Figure 1); (3) “Model 3: 200 traits” in

which we extend the list of traits to include the top 100 most positive and top 100 most

negative traits from the Peabody list; (4) “Model 4: 300 traits,” as above but now with 300

traits total; (5) “Model 5: Nouns” in which we use parts-of-speech tagging and extract the

top-100 positive/negative nouns (replacing the trait list); and (6) “Model 6: Verbs” in which

we change the trait list to top-100 positive/negative verbs.

       As elaborated in SI Appendix, the primary empirical conclusions from Study 2 were

retained across model variations. First, regardless of (a) how many traits we used (100, 200,

300), (b) whether we represented groups with full or with reduced lists (of only 4 most

central terms), and (c) whether we used nouns, verbs, or the original trait lists, raw

frequencies continued to show patterns of andro-, ethno-, and, to a lesser extent, class-

centrism. Second, even after mathematically aligning frequencies using z-scoring, we found

that the features of traits continued to differ across intersectional groupings, with relatively

greater positivity, warmth, competence, and dominance for intersectional quadrants including

White, Rich, or Men.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                      28


                                        References

1.    Cole, E. R. Intersectionality and Research in Psychology. American Psychologist 64,
      170–180 (2009).
2.    Hall, E. V, Hall, A. V, Galinsky, A. D. & Phillips, K. W. MOSAIC: A model of
      stereotyping through associated and intersectional categories. Q Academy of
      Management Review 44, 643–672 (2019).
3.    Petsko, C. D., Rosette, A. S. & Bodenhausen, G. V. Through the looking glass: A lens-
      based account of intersectional stereotyping. J Pers Soc Psychol (2022)
      doi:10.1037/pspi0000382.
4.    Kunda, Z., Miller, D. T. & Claire, T. Combining social concepts: The role of causal
      reasoning. Cogn Sci 14, 551–577 (1990).
5.    Coles, S. M. & Pasek, J. Intersectional Invisibility Revisited: How Group Prototypes
      Lead to the Erasure and Exclusion of Black Women. (2020) doi:10.1037/tps0000256.
6.    Purdie-Vaughns, V. & Eibach, R. P. Intersectional invisibility: The distinctive
      advantages and disadvantages of multiple subordinate-group identities. Sex Roles 59,
      377–391 (2008).
7.    Nicolas, G., de la Fuente, M. & Fiske, S. T. Mind the overlap in multiple
      categorization: A review of crossed categorization, intersectionality, and multiracial
      perception. Group Processes & Intergroup Relations 20, 621–631 (2017).
8.    Nicolas, G. & Fiske, S. T. Valence Biases and Emergence in the Stereotype Content of
      Intersecting Social Categories. J Exp Psychol Gen (2023) doi:10.1037/xge0001416.
9.    Pennington, J., Socher, R. & Manning, C. D. GloVe: Global vectors for word
      representation. in EMNLP 2014 - 2014 Conference on Empirical Methods in Natural
      Language Processing, Proceedings of the Conference 1532–1543 (2014).
      doi:10.3115/v1/d14-1162.
10.   Caliskan, A., Bryson, J. J. & Narayanan, A. Semantics derived automatically from
      language corpora necessarily contain human biases. Science (1979) 356, 183–186
      (2016).
11.   Garg, N., Schiebinger, L., Jurafsky, D. & Zou, J. Word embeddings quantify 100 years
      of gender and ethnic stereotypes. Proc Natl Acad Sci U S A 115, E3635–E3644 (2018).
12.   Charlesworth, T. E. S., Caliskan, A. & Banaji, M. R. Historical Representations of
      Social Groups Across 200 Years of Word Embeddings from Google Books.
      Proceedings of the National Academy of Sciences 119, (2022).
13.   Charlesworth, T. E. S., Morehouse, K., Rouduri, V. & Cunningham, W. A. Traces of
      Human Attitudes in Contemporary and Historical Word Embeddings (1800-2000).
      Manuscript Submitted for Publication (2023).
14.   Grave, E., Bojanowski, P., Gupta, P., Joulin, A. & Mikolov, T. Learning Word Vectors
      for 157 Languages. (2018).
15.   Hamilton, W. L., Leskovec, J. & Jurafsky, D. Diachronic word embeddings reveal
      statistical laws of semantic change. in 54th Annual Meeting of the Association for
      Computational Linguistics, ACL 2016 - Long Papers vol. 3 1489–1501 (2016).
16.   Charlesworth, T. E. S., Yang, V., Mann, T. C., Kurdi, B. & Banaji, M. R. Gender
      Stereotypes in Natural Language: Word Embeddings Show Robust Consistency
      Across Child and Adult Language Corpora of More Than 65 Million Words. Psychol
      Sci 32, 218–240 (2021).
17.   Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. BERT: Pre-training of Deep
      Bidirectional Transformers for Language Understanding. in Proceedings of North
      American chapter of the Association for Computational Linguistics-Human Language
      Technologies 2019 4171–4186 (2018).


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                      29


18.   Tan, Y. C. & Celis, L. E. Assessing social and intersectional biases in contextualized
      word representations. in Advances in Neural Information Processing Systems vol. 32
      (2019).
19.   Guo, W. & Caliskan, A. Detecting Emergent Intersectional Biases: Contextualized
      Word Embeddings Contain a Distribution of Human-like Biases. in AIES 2021 -
      Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society 122–133
      (2021). doi:10.1145/3461702.3462536.
20.   May, C., Wang, A., Bordia, S., Bowman, S. R. & Rudinger, R. On measuring social
      biases in sentence encoders. in NAACL HLT 2019 - 2019 Conference of the North
      American Chapter of the Association for Computational Linguistics: Human Language
      Technologies - Proceedings of the Conference vol. 1 622–628 (2019).
21.   Tan, Y. C. & Celis, L. E. Assessing social and intersectional biases in contextualized
      word representations. Adv Neural Inf Process Syst 32, (2019).
22.   Pachankis, J. E. et al. The Burden of Stigma on Health and Well-Being: A Taxonomy
      of Concealment, Course, Disruptiveness, Aesthetics, Origin, and Peril Across 93
      Stigmas. Pers Soc Psychol Bull 44, 451–474 (2018).
23.   Dovidio, J. F. & Gaertner, S. L. Intergroup bias. The Handbook of Social Psychology
      1084–1121 (2010) doi:10.1002/9780470561119.socpsy002029.
24.   Fiske, S. T., Cuddy, A. J. C., Glick, P. & Xu, J. A model of (often mixed) stereotype
      content: Competence and warmth respectively follow from perceived status and
      competition. J Pers Soc Psychol 82, 878–902 (2002).
25.   Kirk, H. R. et al. Bias Out-of-the-Box: An Empirical Analysis of Intersectional
      Occupational Biases in Popular Generative Language Models. Proceedings of the 35th
      Conference on Neural Information Processing Systems (2021).
26.   Di Stasio, V. & Larsen, E. N. The Racialized and Gendered Workplace: Applying an
      Intersectional Lens to a Field Experiment on Hiring Discrimination in Five European
      Labor Markets. Soc Psychol Q 83, 229–250 (2020).
27.   American Association of University Women. The Simple Truth about the Gender Pay
      Gap. https://www.aauw.org/resource/the-simple-truth-about-the-gender-pay-gap/
      (2018).
28.   Rinn, R., Ludwig, J., Fassler, P. & Deutsch, R. Cues of wealth and the subjective
      perception of rich people. Current Psychology (2022) doi:10.1007/s12144-022-03763-
      y.
29.   Osgood, C. E., Suci, G. J. & Tannenbaum, P. H. The measurement of meaning.
      (University of Illinois Press, 1967).
30.   Nisbett, R. E. & Wilson, T. D. The Halo Effect: Evidence for Unconscious Alteration
      of Judgments. J Pers Soc Psychol 35, 250–256 (1977).
31.   Speer, R. GitHub - rspeer/wordfreq: Access a database of word frequencies, in various
      natural languages. https://github.com/rspeer/wordfreq (2022).
32.   Cheryan, S. & Markus, H. R. Masculine defaults: Identifying and mitigating hidden
      cultural biases. Psychol Rev 127, 1022–1052 (2020).
33.   Guo, W. & Caliskan, A. Detecting Emergent Intersectional Biases: Contextualized
      Word Embeddings Contain a Distribution of Human-like Biases. in AIES 2021 -
      Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society 122–133
      (2021). doi:10.1145/3461702.3462536.
34.   Nicolas, G., la Fuente, M. de & Fiske, S. T. Mind the overlap in multiple
      categorization: A review of crossed categorization, intersectionality, and multiracial
      perception. Group Processes and Intergroup Relations vol. 20 621–631 Preprint at
      https://doi.org/10.1177/1368430217708862 (2017).


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                     30


35.   Petsko, C. D. & Bodenhausen, G. V. Multifarious person perception: How social
      perceivers manage the complexity of intersectional targets. Soc Personal Psychol
      Compass 14, (2020).
36.   Cech, E. A. et al. LGBT workplace inequality in the federal workforce: intersectional
      processes, organizational contexts, and turnover considerations. ILR Review 73, 25–60
      (2020).
37.   Vlasceanu, M. & Amodio, D. M. Propagation of societal gender inequality by internet
      search algorithms. Proc Natl Acad Sci U S A 119, 1–8 (2022).
38.   O’brien, K. R., Scheffer, M., Van Nes, E. H. & Van Der Lee, R. How to Break the
      Cycle of Low Workforce Diversity: A Model for Change. (2015)
      doi:10.1371/journal.pone.0133208.
39.   Katz, D. & Braly, K. Racial stereotypes of one hundred college students. J Abnorm
      Soc Psychol 28, 280–290 (1933).
40.   Caliskan, A., Parth Ajay, P., Charlesworth, T., Wolfe, R. & Banaji, M. R. Gender Bias
      in Word Embeddings: A Comprehensive Analysis of Frequency, Syntax, and
      Semantics. AIES 22, (2022).
41.   Bailey, A. H., LaFrance, M. & Dovidio, J. F. Implicit androcentrism: Men are human,
      women are gendered. J Exp Soc Psychol 89, 103980 (2020).
42.   McDermott, M. & Samson, F. L. White racial and ethnic identity in the United States.
      Annu Rev Sociol 31, 245–261 (2005).
43.   Lalor, J. P., Yang, Y., Smith, K., Forsgren, N. & Abbasi, A. Benchmarking
      Intersectional Biases in NLP. Proceedings ofthe 2022 Conference ofthe North
      American Chapter ofthe Association for Computational Linguistics: Human Language
      Technologies 3598–3609 (2022).
44.   Wu, S. J., Bai, X. & Fiske, S. T. Admired Rich or Resented Rich? How Two Cultures
      Vary in Envy. J Cross Cult Psychol 49, 1114–1143 (2018).
45.   Durante, F., Tablante, C. B. & Fiske, S. T. Poor but Warm, Rich but Cold (and
      Competent): Social Classes in the Stereotype Content Model. Journal of Social Issues
      73, 138–157 (2017).
46.   Greenwald, A. G. & Banaji, M. R. Implicit Social Cognition: Attitudes, Self-Esteem,
      and Stereotypes. Psychol Rev 102, 4–27 (1995).
47.   Battistella, E. L. Markedness: The Evaluative Superstructure of Language. (SUNY
      Press, 1990).
48.   Wolfe, R. & Caliskan, A. Markedness in Visual Semantic AI. ACM International
      Conference Proceeding Series 1269–1279 (2022) doi:10.1145/3531146.3533183.
49.   Hester, N., Payne, K., Brown-Iannuzzi, J. & Gray, K. On Intersectionality: How
      Complex Patterns of Discrimination Can Emerge From Simple Stereotypes. Psychol
      Sci 31, 1013–1024 (2020).
50.   Bureau of Labor Statistics, U. & Population Survey, C. HOUSEHOLD DATA
      ANNUAL AVERAGES 39. Median weekly earnings of full-time wage and salary
      workers by detailed occupation and sex. (2022).
51.   Peabody, D. Selecting representative trait adjectives. J Pers Soc Psychol 52, 59–71
      (1987).
52.   Warriner, A. B., Kuperman, V. & Brysbaert, M. Norms of valence, arousal, and
      dominance for 13,915 English lemmas. Behav Res Methods 45, 1191–1207 (2013).
53.   Delobelle, P., Tokpo, E. K., Calders, T. & Berendt, B. Measuring Fairness with Biased
      Rulers: A Comparative Study on Bias Metrics for Pre-trained Language Models.
      NAACL 2022 - 2022 Conference of the North American Chapter of the Association for
      Computational Linguistics: Human Language Technologies, Proceedings of the
      Conference 1693–1706 (2022) doi:10.18653/v1/2022.naacl-main.122.


EXTRACTING INTERSECTIONAL STEREOTYPES FROM LANGUAGE                                          31


54.   Vulić, I. et al. Multi-simlex: A large-scale evaluation of multilingual and crosslingual
      lexical semantic similarity. Computational Linguistics 46, 847–897 (2020).
55.   Lauscher, A., Lüken, T. & Glavaš, G. Sustainable Modular Debiasing of Language
      Models. Findings of the Association for Computational Linguistics, Findings of ACL:
      EMNLP 2021 3, 4782–4797 (2021).
