---
title: "Extracting intersectional stereotypes from embeddings: Developing and validating the Flexible Intersectional Stereotype Extraction procedure"
person: mahzarin-banaji
section: by
type: journal-article
year: 2024
date: 2024-02-29
venue: "PNAS Nexus"
authors: "Tessa E S Charlesworth; Kshitish Ghate; Aylin Caliskan; Mahzarin R Banaji"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/Charlesworth_PNAS_2024.pdf
doi: https://doi.org/10.1093/pnasnexus/pgae089
openalex_id: https://openalex.org/W4392952534
cited_by_count: 13
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard site, extracted with pdftotext -layout. Title-overlap check 1.00."
---

# Extracting intersectional stereotypes from embeddings: Developing and validating the Flexible Intersectional Stereotype Extraction procedure

## Full text

PNAS Nexus, 2024, 3, 1–12
                                                                                                             https://doi.org/10.1093/pnasnexus/pgae089
                                                                                                               Advance access publication 19 March 2024
                                                                                                                                      Research Report


Extracting intersectional stereotypes from embeddings:
Developing and validating the Flexible Intersectional


                                                                                                                                                             Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
Stereotype Extraction procedure
                               a,
Tessa E. S. Charlesworth            *, Kshitish Ghateb, Aylin Caliskan    c
                                                                              and Mahzarin R. Banaji     d


a
  Kellogg School of Management, Northwestern University, Evanston, IL 60208, USA
b
  Language Technologies Institute, Carnegie Mellon University, Pittsburgh, PA 15213, USA
c
  Information School, University of Washington, Seattle, WA 98105, USA
d
  Department of Psychology, Harvard University, Cambridge, MA 02138, USA
*To whom correspondence should be addressed: Email: tessa.charlesworth@kellogg.northwestern.edu
Edited By: Michael Muthukrishna


Abstract
Social group–based identities intersect. The meaning of “woman” is modulated by adding social class as in “rich woman” or “poor woman.”
How does such intersectionality operate at-scale in everyday language? Which intersections dominate (are most frequent)? What
qualities (positivity, competence, warmth) are ascribed to each intersection? In this study, we make it possible to address such
questions by developing a stepwise procedure, Flexible Intersectional Stereotype Extraction (FISE), applied to word embeddings (GloVe;
BERT) trained on billions of words of English Internet text, revealing insights into intersectional stereotypes. First, applying FISE to
occupation stereotypes across intersections of gender, race, and class showed alignment with ground-truth data on occupation
demographics, providing initial validation. Second, applying FISE to trait adjectives showed strong androcentrism (Men) and
ethnocentrism (White) in dominating everyday English language (e.g. White + Men are associated with 59% of traits; Black + Women with
5%). Associated traits also revealed intersectional differences: advantaged intersectional groups, especially intersections involving
Rich, had more common, positive, warm, competent, and dominant trait associates. Together, the empirical insights from FISE
illustrate its utility for transparently and efficiently quantifying intersectional stereotypes in existing large text corpora, with potential
to expand intersectionality research across unprecedented time and place. This project further sets up the infrastructure necessary to
pursue new research on the emergent properties of intersectional identities.

Keywords: gender, intersectionality, race, stereotyping, word embeddings


    Significance Statement
    Stereotypes at the intersections of social groups (e.g. poor man) may induce unique beliefs not visible in parent categories alone (e.g.
    poor or men). Despite increased public and research awareness of intersectionality, empirical evidence on intersectionality remains
    understudied. Using large corpora of naturalistic English text, the Flexible Intersectional Stereotype Extraction procedure is intro­
    duced, validated, and applied to Internet text to reveal stereotypes (in occupations and personality traits) at the intersection of gender,
    race, and social class. The results show the dominance (frequency) and halo effects (positivity) of powerful groups (White, Men, and
    Rich), amplified at group intersections. Such findings and methods illustrate the societal significance of how language embodies, prop­
    agates, and even intensifies stereotypes of intersectional social categories.


Introduction                                                                     convenience. While social group intersectionality has received ex­
Since 2004, Google searches for the term “intersectionality” have                tensive humanistic analyses and qualitative theorizing (3, 7),
increased exponentially, reaching a peak in February 2023                        there remains limited empirical evidence studying intersectional­
(SI Appendix). This increasing interest among the public parallels               ity at-scale (8). Today, methodological developments in testing
rising calls among social scientists to recognize how intersections              and quantifying stereotypes in naturalistic language make such
of social group identities modulate group perception (1–3).                      an effort possible (8).
Intersections of group identities, such as race + gender, produce                   In this study, we address past methodological limitations
unique and emergent stereotype content (4), as well as unique                    and advance empirical research on intersectional social group
experiences of discrimination (5, 6) that would be missed if                     stereotyping by introducing a new stepwise procedure—the
group identities were examined in isolation for experimental                     Flexible Intersectional Stereotype Extraction (FISE) procedure.


                     Competing Interest: The authors declare no competing interest.
                     Received: October 16, 2023. Accepted: February 13, 2024
                     © The Author(s) 2024. Published by Oxford University Press on behalf of National Academy of Sciences. This is an Open Access article
                     distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits
                     unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


2 | PNAS Nexus, 2024, Vol. 3, No. 3


The procedure is flexible in that it can be: (i) applied to large-scale   research with contextualized methods has to-date represented
naturalistic data of word embeddings trained from any text                groups through first/last names (20, 21). Yet many social group di­
source, including different languages, geographies, or demo­              mensions are simply not encoded in names, especially more con­
graphic groups; (ii) applied to any group intersection, so long as        cealable groups, like sexual orientation, religion, or more physical
the group concept can be represented in words; and (iii) quantified       stigmas such as body weight, age, or disability status (23).
in systematic and comparable metrics, such as the frequency               Additionally, given the greater computational and expertise de­
(number) of traits associated with an intersectional group, to fa­        mands of training or fine-tuning contextualized language models
cilitate direct comparisons of intersectional stereotypes across di­      on new text corpora, social science research remains limited in its
verse settings.                                                           ability to examine the variability and scope of intersectional ster­


                                                                                                                                                      Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
                                                                          eotypes if required to rely only on large language models (LLMs).

Past research: extracting single group
stereotypes from static embeddings                                        The current research: FISE
The FISE procedure builds from an emerging body of research               To overcome such barriers for social science researchers, the cur­
using Natural Language Processing, and especially static word             rent research introduces the FISE procedure as a flexible and
embeddings, such as GloVe (9), to propel the understanding of             transparent procedure that can be applied to both static and contex­
how social attitudes and stereotypes prevail in large-scale nat­          tualized models, as necessary. We introduce FISE with a case study­
uralistic data (10–12). For instance, static word embeddings              ing focusing on intersections across three major social categories—
have been used to quantify the relative relationships between             race (in this case, Black/White, because of the dominance of
single groups (e.g. White, Black) and attributes (e.g. good, bad), ul­    Black/White relations in US English contexts), as well as social class
timately revealing that static word embeddings capture biases             (rich/poor), and gender (men/women)—that can shape group per­
similar to attitudes obtained directly from human minds (13).             ception and its consequences of preference and discrimination
Such findings from static word embeddings have been crucial               (24, 25). In our primary analyses, FISE is applied across multiple pre­
in expanding understanding of topics ranging from how                     trained embedding models of large-scale English text corpora, ran­
English language–based stereotypes have shifted across 200                ging from static GloVe embeddings trained on 840 billion words
years of history (12) to how social class is conceived in contem­         from the Common Crawl to contextualized BERT embeddings
porary English (14) and to how gender stereotypes emerge in               trained on a combination of Wikipedia and Common Crawl text.
children’s books (15).                                                    Additionally, in supplemental material and open code resources,
    Despite the insights gleaned from these studies, however,             we illustrate the flexibility of generalizing FISE to applications across
past work has largely represented each social group concept in­           non-English languages (French) for future researchers to address
dependently, thereby leaving stereotypes at intersections of iden­        the English-centric focus of existing work (26). In supplemental
tities unexamined. Such limitations occur, in part, because               material, we also generalize FISE to more complex three-way inter­
social science researchers often rely on the availability and             sections of social groups (e.g. simultaneously crossing gender, race,
ease of use in static single word embedding which have key ad­            and class) and show the advantages of FISE over simpler averaged
vantages of being flexibly trainable across languages (16), time          vector approaches.
points (17), and diverse demographics (18). Still, static word em­            To begin, for the simplest case of static embeddings and two-
beddings arguably encountered difficulties for studying inter­            way intersections, FISE proceeds in five steps (see details in
sectional stereotyping because they cannot represent multiword            Methods and SI Appendix). First, we create a list of target concepts
sentences, and thus, it was difficult to conceive of how to represent     for occupation labels (study 1) or trait adjectives (study 2), as well
intersections, such as Black Women and White Men accurately.              as lists of group labels that represent each of the three groups of
                                                                          interest (gender, race, and class; Fig. 1). Second, we compute the
                                                                          cosine similarity of each target occupation/trait with each group
Past research: extracting group stereotypes                               concept (e.g. janitor-White, janitor-Black, and so on). Third, we
from contextualized embeddings                                            take the difference of the cosine similarities along a group dimen­
Acknowledging such seeming methodological difficulties, com­              sion (e.g. janitor-White vs. janitor-Black) and repeat this for the other
puter science research moved to studying social group biases us­          group dimensions (e.g. janitor-Rich vs. janitor-Poor, janitor-Man vs.
ing contextualized embedding models (e.g. BERT (19)) with                 janitor-Woman). Fourth, we cross two group dimensions (e.g.
multiword sentences (20–22). For instance, Guo and Caliskan               race-by-class), placing each occupation/trait in the resulting x-y
(21) studied intersectional stereotypes across gender and race/           coordinate space according to its cosine similarity with the indi­
ethnicity by representing group concepts in sentences using ex­           vidual group dimensions. Fifth, we analyze the resulting number
amples from everyday English language (e.g. “This is Aisha” or            (frequency) and qualities (e.g. valence) of the occupation/traits
“Look at Keisha,” for example, sentences with Black woman names).         in each quadrant.
As in previous static embedding analyses, the authors then com­               As noted above, the goal of FISE is primarily to improve the flexi­
puted relationships (cosine similarities) between the intersectional      bility for extracting intersectional content across any text source
group–related sentences and positive/negative attribute sentences.        and any group intersection, with comparable, quantitative met­
Results showed evidence of intersectional emergence, in which             rics. Crucially, given wide-ranging scholarly interest in intersec­
new traits emerged as associated with the intersectional group            tionality, the FISE method is also designed to be easy to use,
that were not associated with the individual parent groups in iso­        transparent to understand, and low in computational demands
lation; such findings were further validated against known emer­          so that it can be easily adopted by scholars from any field.
gent content, providing confidence in the general approach of             Indeed, all codes and data are provided openly with clear guide­
using language to study intersectional stereotyping.                      lines to apply the method to the complexity of different group tar­
   Yet even contextualized language models can suffer from lim­           gets (sampling from the large space of potential group topics (27),
itations when studying intersectional stereotypes. For instance,          including groups that may have concealable identities not


                                                                                                                                Charlesworth et al. |       3


     A                                                                                                    B


                                                                                                                                                                 Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
Fig. 1. Group words used to represent class, race, and gender for applications of FISE. In the static embeddings, our primary analyses, FISE uses only the
individual words for each group (no templates, in gray). In the contextualized setting (study 2 only), FISE is performed by looking at the cosine similarity
(essentially a correlation) between target group-related sentences (A) and trait attribute sentences (B). A group sentence is created by first selecting a
template (e.g. “This is a”), and then adding the group labels for class (e.g. “rich”), race (e.g. “Black”), and gender (e.g. “woman”). The process is repeated
across all possible combinations, yielding 5,184 sentences from three templates and 12 words for each group (3 × 12 × 12 × 12 = 5,184). Similarly, for traits,
all trait templates are combined with all positive/negative trait words, to yield a sample of 300–900 trait sentences, depending on how many traits are
chosen. Nationality terms under the race categories (e.g. American) were chosen given the conflation of nationalities with racial groups in stereotypes
and documented evidence that American = White.


encoded in names), as well as different languages, media sources,                occupation stereotypes (i.e. how many occupations are associated
and even timespans.                                                              with each group), then FISE should show that intersectional
                                                                                 groupings associated with the most occupations in the real world
                                                                                 (e.g. White Men) are also associated with the most occupations in
Study 1: intersectional stereotypes of                                           language. That is, if an intersectional group dominates the labor
occupations                                                                      force in vivo, it should also dominate in the frequency with which
The content and frequency of intersectional occupation stereo­                   it occurs in naturalistic language.
types have received almost no consideration in large language                        Indeed, the dominance of an intersectional grouping in real-
corpora (28) even though it is known that workplace experiences                  world data is mirrored in the number of occupations associated
of discrimination can be amplified for intersectional identities                 with each intersectional quadrant in English language (Fig. 2;
(29, 30). Moreover, occupational stereotypes provide an ideal                    Table 1). Chi-square tests confirm that actual frequencies of occu­
case study because they can be compared with ground-truth                        pations are not significantly different from the associations
data of actual occupation demographics to validate the FISE pro­                 extracted in language: for race-by-gender, χ2 = 7.53, P = 0.06,
cedure. Thus, as a first introduction to FISE, we identify (i) how               V = 0.19, for race-by-class, χ2 = 2.63, P = 0.45, V = 0.11, and for
many and (ii) which occupations, from a list of 143 occupations                  gender-by-class, χ2 = 5.46, P = 0.14, V = 0.17. For example, looking
from the 2022 Bureau of Labor Statistics report, are associated                  at actual occupation data we see that 48% of occupations are rela­
with each intersectional quadrant across race-by-gender,                         tively more White (>50% point difference in White vs. Black re­
class-by-gender, and race-by-class.                                              presentation) and occupied by Men (>50% men). In parallel,
                                                                                 looking at language associations, White Men are linguistically
                                                                                 associated with 59% of occupations, which, although descriptively
Results
                                                                                 higher than the actual representations, is not significantly differ­
Frequency of intersectional occupation                                           ent (see chi-squared tests above). Similarly, in real-world data,
stereotypes in FISE vs. ground truth                                             only 5% of occupations are relatively more Black and occupied
How many occupations are associated with each intersectional                     by Women and, in language, Black Women are associated with
quadrant in English language and in occupational demographic                     9% of occupations. Such accuracy is also found for the class-
data? If FISE accurately identifies the frequency of intersectional              by-gender and race-by-class comparisons (Table 1). Ultimately,


4 | PNAS Nexus, 2024, Vol. 3, No. 3


                      0.15                                                                                                                                                         0.15                                                                                                                                                           0.15


                                                                                                                                                                                                                                                                                  investor                                                                                                                                              investor
                                                                                                                                                                                                                                                                             advisor                                                                                                                                                  advisor
                      0.1             Female + White                                                                            Male + White                                       0.1              Female + Rich                                                          producer          Malearchitect
                                                                                                                                                                                                                                                                                                    + Rich                                        0.1             Black + Rich                                                       producer  White + Rich
                                                                                                                                                                                                                                                                                                                                                                                                                                                    architect
                                                                                                                                                                                                                                                                                          developer                                                                                                                                   developer
                                                                                                                                                                                                                                                                         jeweler
                                                                                                                                                                                                                                                                            analyst                                                                                                                                jeweler        analyst
                                                                                                                                          architect                                                                                               realtor                                                                                                                                                                                         realtor
                                                                                                                                              engineer                                                                           skincare          concierge
                                                                                                                                                                                                                                                designer                                                                                                                                                              skincare                 concierge
                                                                                                                                                                                                                                                                                                                                                                                                                                                 designer
                                                                              dishwasher
                                                                               designer
                                                                                 realtor
                                                                                  concierge                      server
                                                                                         cook                         manager                                                                                                                        host                      lawyer                                                                                                                                     host          lawyer
                                                                                                                    chef       programmer                                                                                                                      editor                                                                                                                                                     editor
                                                                                        insurer assembler                investor physicist
                                                    receptionist                                          accountant           chemist                                                                                                                      photographer
                                                                                                                                                                                                                                                                     trainerclergy               cabinetmaker                                                                                  clergy
                                                                                                                                                                                                                                                                                                                                                                                            cabinetmaker               trainerphotographer
                                                                                          salespersondentist advisor
                                                                                                                   technician   developer
                      0.05                                                                                                                                                         0.05                                                                                                                                                           0.05
                                                                                                baker             lawyer
                                                                                                                  pilot
                                                                                                               producer    ceo
                                                                                                                           inspectormechanic                                                                                                               author                professor                                                                                                                                  author
                                                                                                                                                                                                                                                                                                                                                                                                                            professor
                                                                                                photographer                                                                                                                                              journalist                 logger                                                                                                            logger administrator     journalist


                                                                                                                                                                Class Difference                                                                                                                                               Class Difference
                                                                                                                                electrician                                                                                                                                  server     ceo                  engineer                                                                                                                    ceo serverengineer


    Race Difference
                                                                                                     broadcaster                                                                                                                                                  writeradministrator
                                                                                                                                                                                                                                                                                   painter  printer                                                                                                                        writer painter
                                                                                                    radiologist
                                                                                              journalist
                                                                                          underwriter                 painter
                                                                                                                analyst       waiter                                                                                                    curator extractor                        chef           physicist
                                                                                                                                                                                                                                                                                             guard                                                                                                   curator extractorprinter   guard physicist chef
                                           nurse                 hygienist                      translator
                                                                                                   pharmacist
                                                                                                           coach                guard
                                                     caregiver
                                         waitressdietitian          therapist        veterinarian                    tailor
                                                                                                                biologist
                                                                                                               courier
                                                                                                                    professor
                                                                                                                           statistician       actor                                                                                                              broadcaster
                                                                                                                                                                                                                                                      underwriterpipelayer                  programmer actor                                                                            pipelayer                             actor
                                                                                                                                                                                                                                                                                                                                                                                                                               broadcaster
                                                                                                                                                                                                                                                                                                                                                                                                                              underwriter  programmer
                                                                                                   assistant
                                                                                                     chiropractor
                                                                                            investigator
                                                                                               author       judge   police  plumber
                                                                                                                     announcer                                                                                                                           instructor
                                                                                                                                                                                                                                                                radiologist       tailor                                                                                                                                 instructor
                                                                                                                                                                                                                                                                                                                                                                                                                                 tailor
                                                                                                                                                                                                                                                                                                                                                                                                                                radiologist
              actress                                         childcare             psychologist
                                                                                          cashier
                                                                                             instructor
                                                                                                   HR writer      welder
                                                                                                             installer
                                                                                                              emt        driver                                                                                                                              assembler
                                                                                                                                                                                                                                                              artist  accountant   manager                                                                                                                             artist                 manager
                                                                                                                                                                                                                                                                                                                                                                                                                                          assembler
                                                                                                                                                                                                                                                                                                                                                                                                                                       accountant
                                                                   skincare         secretary
                                                                                     host       shipper
                                                                                                   editor
                                                                                                  taper
                                                                                              appraiser    packer
                                                                                                          bartender           butcher
                                                                                                                               printer                                                                                       paralegal                    appraiser     coach
                                                                                                                                                                                                                                                                          detective
                                                                                                                                                                                                                                                                        timekeeper                                                                                                                   timekeeper      appraiser
                                                                                                                                                                                                                                                                                                                                                                                                                    paralegal
                                                                                                                                                                                                                                                                                                                                                                                                                detective         coach
                                                                  paralegal                              trainer
                                                                                                     paramedic
                                                                                                  artist    administrator                                                                                                                               tourguide
                                                                                                                                                                                                                                                              taperntist    biologist                                                                                                                         tourguide      biologist
                                                                                                                                                                                                                                                                                                                                                                                                                         taper
                                      maid                     hairdresser                                  jeweler                                                        actress                                                              secretary HR                   agriculturalist                                                                                    agriculturalist                            HR
                                                                                                                                                                                                                                                                                                                                                                                                                     secretary
                                                                                                                                                                                                                                                                                                                                                                                                                          actress        dentist
                                                                                 teacher pathologist
                                                                                                  recycler utor
                                                                                                              clerk roofer machinist  carpenter                                                                                                                assistantjudge                                                                                                                                               assistant
                                                                                                                                                                                                                                                                                                                                                                                                                            judge
                                                                         masseuse                             detective
                                                                                            tourguide landscaper                                                                                                                                                                            chemist                                                                                                                                        chemist
                                                                              counselorextractor                                postman
                                                                                                                             musician                                                                         dietitian                             insurer shipper
                                                                                                                                                                                                                                                                 chiropractordrafter musician
                                                                                                                                                                                                                                                                         installer                                                                                                                           musicianshipper
                                                                                                                                                                                                                                                                                                                                                                                                             drafter        dietitian
                                                                                                                                                                                                                                                                                                                                                                                                                        chiropractor
                                                                                                                                                                                                                                                                                                                                                                                                                          installer          insurer
                                                                                                                 drafterfirefighter                                                                                                                               surveyer
                                                                                                                                                                                                                                                            translator
                                                                                                                                                                                                                                                      salesperson
                                                                                                                                                                                                                                                 psychologist                                                                                                                             surveyer                             translator
                                                                                                                                                                                                                                                                                                                                                                                                                      psychologist   salesperson
                      0                                    librarian               teller                   timekeeper                                                             0                                                      dishwasher                  tutor                                                                       0                                                                 tutor                      dishwasher
                                            manicurist                                                                  logger                                                                                                 therapist
                                                                                                                                                                                                                                     masseuse           keyerecycler
                                                                                                                                                                                                                                                        investigator             announcer
                                                                                                                                                                                                                                                                           courier
                                                                                                                                                                                                                                                                       packer           statistician
                                                                                                                                                                                                                                                                                      driver
                                                                                                                                                                                                                                                                                technician                                                                                            keyer                   masseuse  announcer
                                                                                                                                                                                                                                                                                                                                                                                                                           statistician
                                                                                                                                                                                                                                                                                                                                                                                                                        packercourier
                                                                                                                                                                                                                                                                                                                                                                                                                             therapist
                                                                                                                                                                                                                                                                                                                                                                                                                            driver
                                                                                                                                                                                                                                                                                                                                                                                                                        investigator
                                                                                                                                                                                                                                                                                                                                                                                                                 recycler             technician
                                                                            curator                                                                                                                                         hygienist                                                                                                                                                                                         hygienist
                                                                                                                                                                                                         manicurist librarian                        cook         metalworker    police            mechanic                                                                        metalworker       manicurist
                                                                                                                                                                                                                                                                                                                                                                                                        librarian           police mechanic cook
                                                                                                                          barber                                                                                                                                       landscaper       inspector                                                                                                             landscaper             inspector
                                                                                                         ironworker            cabinetmaker                                                                                                  teacher                                                                                                                                                              teacher
                                                                           phlebotomist
                                                                                  bookkeeper stocker clergy janitor
                                                                            fundraiser                                                                                                                                                                         pharmacistpilot welder       machinist                                                                                                           machinist    pharmacist
                                                                                                                                                                                                                                                                                                                                                                                                                           welder       pilot
                                                                                                                                                                                                          dressmaker                                                                                                                                                                dressmaker
                                                                                                    surveyer highwayman                                                                                                                                     baker                            electrician                                                                                                                           electrician
                                                                                                                                                                                                                                                                                                                                                                                                                                         baker
                                                                            abstractor             pipelayer                                                                                       maid                   hairdresser                                                      butcher                                                                                                                     butcher
                                                                                                                                                                                                                                                                                                                                                                                                                 hairdresser
                                                                                                                                                                                                                                                                                                                                                                                                                     maid
                                                                                                     logistician
                                                                                                 taxidriver                                                                                                                                             pathologistbartender    highwayman                                                                                              highwayman              pathologist
                                                                                                                                                                                                                                                                                                                                                                                                                     bartender
                                              dressmaker                         drycleaner                                                                                                                                           abstractor veterinarian                              waiter
                                                                                                                                                                                                                                                                                         plumber                                                                                         abstractor                                waiter
                                                                                                                                                                                                                                                                                                                                                                                                                          veterinarian
                                                                                                                                                                                                                                                                                                                                                                                                                            plumber
                                                                                            keyer metalworker  agriculturalist
                      −0.05                                                                                                                                                        −0.05                                                                                                                                                          −0.05
                                                                               busdriver                               laborer                                                                                   receptionist                  teller                                        barber                                                                                                barberteller                         receptionist
                                                                                                                                                                                                                                          counselor
                                                                                                                                                                                                                                    phlebotomist                         ironworker
                                                                                                                                                                                                                                                                           clerk                                                                                                             ironworker counselor
                                                                                                                                                                                                                                                                                                                                                                                           phlebotomist            clerk
                                                                                                                                                                                                                                            bookkeeper stocker
                                                                                                                                                                                                                                      fundraiser
                                                                                                                                                                                                                                                                                                                                                                                              stocker
                                                                                                                                                                                                                                                                                                                                                                                           bookkeeper
                                                                                                                                                                                                                                                                                                                                                                                            fundraiser
                                                                                                                                                                                                                                                                                    roofer         carpenter                                                                                                    carpenter
                                                                                                                                                                                                                                                                                                                                                                                                                   roofercashier


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
                                                                                                                                                                                                        nurse                            busdriver cashier taxidriver                                                                                                              busdriver
                                                                                                                                                                                                                                                                                                                                                                                       taxidriver                               nurse
                                                                                                                                                                                                                                           drycleaner                                firefighter                                                                                    drycleaner             firefighter
                                                                                                                                                                                                      waitress                                                            emt             laborer                                                                                    laborer                                waitress
                                                                                                                                                                                                                                                                                                                                                                                                                            emt
                                                                                                             jailer                                                                                                         childcare                                logistician                                                                                                        logistician                    childcare

                      −0.1                                                                                                                                                         −0.1             Femalecaregiver                                                                                                                               −0.1
                                                                                                                                                                                                                                                                                                                                                                                                                         caregiver
                                      Female + Black                                                                            Male + Black                                                               + Poor                                                   paramedic                Male + Poor                                                          Black + Poor                                      paramedic                  White + Poor
                                                                                                                                                                                                                                                                         jailer    janitor                                                                              jailer                 janitor
                                                                                                                                                                                                                                                                                          postman                                                                                                            postman


                      −0.15                                                                                                                                                        −0.15                                                                                                                                                          −0.15

                              −0.15                  −0.1                 −0.05                   0                   0.05                   0.1         0.15                              −0.15                 −0.1                   −0.05                  0                   0.05                  0.1            0.15                              −0.15       −0.1            −0.05                   0                     0.05                        0.1        0.15

                                                                           Gender Difference                                                                                                                                             Gender Difference                                                                                                                               Race Difference

Fig. 2. English language–based occupation stereotypes from FISE applied to static embeddings. Each panel represents the specific occupations associated
with each intersectional quadrant in the contrast of (A) gender-by-race, (B) gender-by-class, or (C) race-by-class. Interactive scatterplots are available to
zoom in on specific quadrants: https://osf.io/b9nmd/. Analogous plots for the other five methods and data sources are provided in SI Appendix.


the language models show accuracy in identifying which intersec­                                                                                                                                                                                                   Table 1. Percentage of occupations in each intersectional
tional groups dominate (are most frequent) in the occupational                                                                                                                                                                                                     grouping (quadrant) for static embeddings and ground-truth data
stereotype space and, conversely, which intersectional groups                                                                                                                                                                                                      (non-z-scored).
are made invisible (are least frequent) in occupational stereotypes.                                                                                                                                                                                               Intersectional                                                                               Ground-truth                                                                       Static
                                                                                                                                                                                                                                                                   grouping                                                                                 categorizations (BLS)                                                               embeddings
Which occupations are associated with                                                                                                                                                                                                                                                                                                                                                                                                         (GloVe CC 840B)
intersectional groupings in FISE vs. ground truth?                                                                                                                                                                                                                 White + Rich                                                                                                  53                                                                                   46
Looking beyond how many occupations we next ask: which specific                                                                                                                                                                                                    White + Poor                                                                                                  33                                                                                   33
occupations fall in each quadrant (see Fig. 2)? To test accuracy                                                                                                                                                                                                   Black + Rich                                                                                                   2                                                                                    6
                                                                                                                                                                                                                                                                   Black + Poor                                                                                                  13                                                                                   15
here, we compare the “hits” (i.e. both language and ground truth
                                                                                                                                                                                                                                                                   Male + Rich                                                                                                   33                                                                                   42
classify an occupation as, for example, White Rich) to “misses”                                                                                                                                                                                                    Male + Poor                                                                                                   24                                                                                   29
(i.e. language and ground truth deviated for specific occupation clas­                                                                                                                                                                                             Female + Rich                                                                                                 21                                                                                   10
sifications). Across all 143 occupations, language and ground-truth                                                                                                                                                                                                Female + Poor                                                                                                 21                                                                                   20
categorizations showed a 57%, 47%, and 51% “correct hit” rate, for                                                                                                                                                                                                 Male + White                                                                                                  48                                                                                   59
                                                                                                                                                                                                                                                                   Male + Black                                                                                                  10                                                                                   12
gender-by-race, gender-by-class, and race-by-class, respectively,
                                                                                                                                                                                                                                                                   Female + White                                                                                                37                                                                                   20
which were not significantly different from chance, χ2 = 2.27,                                                                                                                                                                                                     Female + Black                                                                                                 5                                                                                    9
P = 0.13; χ2 = 0.28, P = 0.59; and χ2 = 0.03, P = 0.86. Crucially, however,
two additional analyses show that, when sufficient signal exists in                                                                                                                                                                                                Occupation frequencies represent the percentage of occupations (out of 143
                                                                                                                                                                                                                                                                   possible occupations) that are associated with each intersectional grouping
the real-world, FISE can in fact accurately capture occupational                                                                                                                                                                                                   (e.g. the White Men grouping is associated with 59% of occupations in language).
stereotypes.                                                                                                                                                                                                                                                       Bolded numbers indicate the highest relative percentage for each intersectional
                                                                                                                                                                                                                                                                   quadrant.
    First, we inspect the individual occupations that “missed” clas­
sification: as a few examples, judge, analyst, accountant, and bar­
tender were classified as White Men occupations in English
language data but, in ground-truth, were relatively more associ­                                                                                                                                                                                                   race-by-class, 70% [50%, 86%], χ2 = 3.70, P = 0.05. In summary,
ated with White Women. Crucially, in ground truth, these occupa­                                                                                                                                                                                                   when the real-world signal is clear, the language will accurately
tions were around the 50% mark of men/women representation,                                                                                                                                                                                                        identify the occupations; when real-world signal itself is around
with 55–59% women workforces, and thus provided ambiguous                                                                                                                                                                                                          chance then the language will accurately reflect such ambiguity.
gender signals in ground-truth data. Similarly, occupations that
were more ambiguously White/Black (e.g. with smaller differen­
ces in White/Black representation such as guard, caregiver, recycler)
                                                                                                                                                                                                                                                                   Study 2: intersectional stereotypes of trait
were more likely to be misclassified along race. Those that were
                                                                                                                                                                                                                                                                   adjectives
more ambiguously Rich/Poor (e.g. around the median earnings; in­                                                                                                                                                                                                   Study 1 shows that FISE can accurately identify both how many (the
vestigator, librarian, plumber) were more likely to be misclassified                                                                                                                                                                                               relative frequency) and which (the extreme classifications) occupa­
across class (i.e. as a “rich” occupation, above median earnings,                                                                                                                                                                                                  tions are stereotyped into intersectional social group quadrants
or as a “poor” occupation, below median earnings).                                                                                                                                                                                                                 across race, gender, and class. Thus, in Study 2 we are on firmer
    Thus, in a second analysis, we looked at only those occupations                                                                                                                                                                                                ground to expand the scope to consider intersectional stereotypes
that had an arguably clear real-world signal, using stricter criteria                                                                                                                                                                                              with trait adjectives, which provide no ground-truth data (i.e. we
determined by the first and last author (specifically, <30% women                                                                                                                                                                                                  have no objective data on whether men or women, rich or poor,
in the BLS data was required for a “Men” classification; >70% women                                                                                                                                                                                                Black or White are more honest or hardworking). And yet, trait adjec­
was required for a “Women” classification; see SI Appendix). Using                                                                                                                                                                                                 tives are the quintessential carriers of stereotypes and are consist­
only that subset of occupations with clear real-world signal on gen­                                                                                                                                                                                               ently used in research on person or group perception. Study 2 also
der, race, and class, we found significant above-chance accuracy                                                                                                                                                                                                   expands the research scope to demonstrate the flexible application
for all three contrasts of gender-by-race, 69% [53%, 82%], χ2 = 5.36,                                                                                                                                                                                              of FISE across contextualized embedding models (BERT (19)), and
P = 0.02, gender-by-class, 70% [51%, 84%], χ2 = 4.36, P = 0.04, or                                                                                                                                                                                                 identifies where conclusions converge or diverge across models, as


                                                                                                                                                                                                                                                                                                                                                                                       Charlesworth et al. |                                          5


                      0.15                                                                                                                                                  0.15                                                                                                     intellectual                                 0.15                                                            intellectual

                                                                                                                                                                                                                                                                                        loyal                                                                                                           loyal


                      0.1             Female + White                                                            kind
                                                                                                                              Male + White                                  0.1             Female + Rich                                                                        Male + Rich
                                                                                                                                                                                                                                                                           arrogant                                               0.1              Black + Rich                                                             White + Rich
                                                                                                                                                                                                                                                                                                                                                                                                                        arrogant
                                                                                 romantic           relaxed
                                                                                                    friendly                                                                                                                                                   knowledgeable                                                                                                           knowledgeable
                                                                                                            confident                                                                                                                                       friendly                                                                                                                                                               friendly
                                                                                                                                                                                                                                       romantic                                                                                                                                                                                     romantic
                                                                                                       happy                                                                                                                                              thoughtful                                                                                                                          thoughtful
                                                                                      smart generous                                                                                                                                                               talented                                                                                                                talented
                                                                                 warm                     original     arrogant                                                                            sensual                                      relaxed
                                                                                                                                                                                                                                                 pleasant                                                                                                                        sensual                  pleasant                relaxed
                                                                                                         optimistic
                                                                                                    hostile                                                                                                                                smart intelligent                                                                                                                             intelligent                        smart
                                                                                                                                                                                                                                                               confident                                                                                                                                                      confident
                      0.05                                                                                                                                                  0.05                                                                                                                                                  0.05
                                                                                             tense weakhopeful                                                                                                                      jealous witty     enthusiastic     greedy                                                                                                                      enthusiastic
                                                                                                                                                                                                                                                                                                                                                                                                  jealous
                                                                                                                                                                                                                                                                                                                                                                                             greedy    witty
                                                                                                                                                                                            sexy                                                                                                                                                                                            sexy


                                                                                                                                                         Class Difference                                                                                                                                      Class Difference
                                                                                           stupid         angryjolly


    Race Difference
                                                                                           adventurousgrim                                                                                    feminine                              gracious energetic                                                                                                                         energeticgracious
                                                                                                                                                                                                                                                                                                                                                                                        feminine
                                                                                       fearful
                                                                                 depressed pleasant          brilliant
                                                                                            helpful                                                                                                                                              prejudiced                                                                                                                   prejudiced
                                                                                                                                                                                                                   discriminating                    conceited    brilliant
                                                                                                                                                                                                                                                              clever                                                                                                       discriminating conceited            brilliant
                                                                                                                                                                                                                                                                                                                                                                                                           clever
                                                                                     lonely
                                                                                       witty
                                                                                      fussy  irresponsible  clever
                                                                                                    enthusiastic   peaceful
                                                                                                              obnoxious               loyal                                                                                                                               trustworthy                                                                                                            trustworthy
                                                                                    unfriendly                reliable                                                                                                                         adventurous                                                                                                                                                   adventurous
                                                                             jealous carefree             brave             honest
                                                            bossy    spiritedwastefulabusive         cruel             trustworthyintellectual                                                                              spirited                      happy      peaceful
                                                                                                                                                                                                                                                                obnoxious
                                                                                                                                                                                                                                                                     kind
                                                                                                                                                                                                                                                                                                                                                                                                       peaceful
                                                                                                                                                                                                                                                                                                                                                                                                  spirited
                                                                                                                                                                                                                                                                                                                                                                                                      obnoxious                 happy   kind
                                                                                                           gentle
                                                                                                    rudethoughtful
                                                                                                           humorous                                                                                             scornful                                       original
                                                                                                                                                                                                                                                            gentle                                                                                                                 scornful        carefree hopefuloriginal
                                                                                                                                                                                                                                                                                                                                                                                                  gentle
                                                                                              accurate
                                                                                               compassionate
                                                                                cheerful charitable    cowardly         greedy                                                                                                     warm carefree hostile      hopeful                                                                                                                                                      warm
                                                                                                                                                                                                                                                                                                                                                                                                                        hostile
                                                                                                   conceited
                                                                                                intelligent         talented                                                                                                               playful
                                                                                                                                                                                                                                        fussy                   reliable
                                                                                                                                                                                                                                                             humorous jolly                                                                                                                            reliable
                                                                                                                                                                                                                                                                                                                                                                                                humorous
                                                                                                                                                                                                                                                                                                                                                                                           playful        fussy      jolly
                                      sexy
                                        feminine                             gracious glum
                                                                                        playful          knowledgeable                                                                                                                 unfriendly
                                                                                                                                                                                                                                                helpful             dependable                                                                                                      dependable unfriendly     helpful
                      0                                                                                                grumpy                                               0                                                                     tense                        honest                                             0                                                                   honest         tense
                                                         spiteful insecure heartless     immoral
                                                                                       stingy                     dependable                                                                                             manipulative                        optimistic                                                                                                     manipulative                                 optimistic
                                                                                            unreliable
                                                         scornful                         truthful                   incompetent                                                                                             resourceful                                                                                                                                 resourceful
                                                     sensual            uncooperative  deceitful cranky                                                                                                                                affectionate                                                                                                                          affectionate
                                                                   manipulative helpless
                                                            discriminating                   energetic
                                                                                               prejudiced
                                                                                        courageous
                                                                                       unethical
                                                                                    affectionate                dishonest                                                                                         bossy                             generous                                                                                                                                       bossy                    generous
                                                                                                        disorderly                                                                                              spiteful                 fearful
                                                                                                                                                                                                                                     cheerful                                                                                                                                           spiteful
                                                                                                                                                                                                                                                                                                                                                                                               cheerful         fearful
                                                              unkind resourceful irritabledisrespectful
                                                          inconsiderate                                                                                                                                              unkind                     accurate
                                                                                                                                                                                                                                                      disrespectful
                                                                                                                                                                                                                                               irresponsible
                                                                                                                                                                                                                                                         cowardly
                                                                                                                                                                                                                                                      rude                                                                                                                 unkind
                                                                                                                                                                                                                                                                                                                                                                       disrespectful           accurate
                                                                                                                                                                                                                                                                                                                                                                                                     irresponsible
                                                                                                                                                                                                                                                                                                                                                                                              cowardly
                                                                                                                                                                                                                                                                                                                                                                                                   rude
                                                                                           insolent                                                                                                                                      stingy
                                                                                                                                                                                                                                            truthful                                                                                                                                   stingy
                                                                                                                                                                                                                                                                                                                                                                                    truthful
                                                                                                                                                                                                                                                              angry
                                                                                                                                                                                                                                                       cruelbrave                                                                                                                                      brave angry
                                                                                                                                                                                                                                                                                                                                                                                                     cruel
                      −0.05                                                                                                                                                 −0.05                                                                                                                                                 −0.05
                                                                                                                                                                                                                                  wastefuldeceitful
                                                                                                                                                                                                                                           courageous   weak              grumpy                                                                                                 deceitful
                                                                                                                                                                                                                                                                                                                                                                             courageous  grumpy  wasteful            weak
                                                                                 lifeless
                                                                                        negligent                                                                                                                            uncooperativeglum                                                                                                                               uncooperative  glum
                                                                                                                                                                                                                                               charitable
                                                                                                                                                                                                                                             insolent                                                                                                                  insolent              charitable


                                                                                                                                                                                                                                                                                                                                                                                                                                                          Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
                                                                                                                                                                                                                                               immoral
                                                                                                                                                                                                                                                    compassionate                                                                                                                    immoral
                                                                                                                                                                                                                 inconsiderate
                                                                                                                                                                                                                         insecure             unethical
                                                                                                                                                                                                                                                  stupid cranky                                                                                                                cranky compassionate stupid
                                                                                                                                                                                                                                                                                                                                                                             unethical
                                                                                                                                                                                                                                                                                                                                                                       inconsiderateinsecure
                                                                                                                                                                                                                                               negligent
                                                                                                                                                                                                                                       heartless                  dishonest                                                                                       negligent dishonest
                                                                                                                                                                                                                                                                                                                                                                                    heartless
                                                                                                                                                                                                                                        depressed
                                                                                                                                                                                                                                               abusive      disorderly                                                                                                    disorderly                 depressed
                                                                                                                                                                                                                                                 unreliable
                                                                                                                                                                                                                                            lonely                                                                                                                               unreliable abusivelonely


                      −0.1                                                                                                                                                  −0.1                                                                                                                                                  −0.1
                                                                                                                                                                                                                                                                       incompetent                                                                                              incompetent
                                      Female + Black                                                                          Male + Black                                                  Female + Poor                                                       grim
                                                                                                                                                                                                                                                                                 Male + Poor                                                       Black + Poor                                                  grim
                                                                                                                                                                                                                                                                                                                                                                                                                            White + Poor
                                                                                                                                                                                                                                                irritable                                                                                                                  irritable


                      −0.15                                                                                                                                                 −0.15                                                                                                                                                 −0.15
                                                                                                                                                                                                                                         lifeless                                                                                                                   lifeless
                              −0.15                −0.1               −0.05                    0                    0.05                   0.1    0.15                              −0.15                −0.1              −0.05                    0                  0.05                     0.1   0.15                                 −0.15       −0.1        −0.05                     0                     0.05                  0.1   0.15

                                                                        Gender Difference                                                                                                                                    Gender
                                                                                                                                                                                                                                helplessDifference                                                                                                                      Race     Difference
                                                                                                                                                                                                                                                                                                                                                                          helpless


Fig. 3. Language-based trait stereotypes from FISE applied to static embeddings. Each panel represents the specific traits associated with each
intersectional quadrant in the contrast of (A) gender-by-race, (B) gender-by-class, or (C) race-by-class. Interactive online scatterplots are available to
zoom in on specific quadrants and traits: https://osf.io/b9nmd/. Analogous plots for the other five methods and data sources are provided in SI Appendix.


Table 2. Percentage of traits in each intersectional grouping (quadrant) across embedding methods (non-z-scored).

                                                                                                                                   Static embeddings                                                                                                                                                         Contextualized embeddings
Intersectional                                                                           GloVe CC                                          GloVe Wiki                                fastText Wiki                                                   Single words with                                                                    Pooled words with                                                      Pooled words no
grouping                                                                                   840B                                                6B                                         2M                                                             template                                                                              template                                                             template

White + Rich                                                                                         57                                          43                                                  34                                                                       59                                                                        69                                                                              43
White + Poor                                                                                         32                                          24                                                  30                                                                       28                                                                        22                                                                              29
Black + Rich                                                                                          5                                           6                                                   9                                                                        1                                                                         0                                                                               3
Black + Poor                                                                                          6                                          24                                                  27                                                                       12                                                                         9                                                                              25
Male + Rich                                                                                          44                                          33                                                  23                                                                       22                                                                        30                                                                              16
Male + Poor                                                                                          21                                          23                                                  32                                                                       11                                                                         7                                                                              20
Female + Rich                                                                                        18                                          16                                                  20                                                                       38                                                                        39                                                                              30
Female + Poor                                                                                        17                                          28                                                  25                                                                       29                                                                        24                                                                              34
Male + White                                                                                         59                                          46                                                  40                                                                       26                                                                        35                                                                              27
Male + Black                                                                                          6                                          10                                                  15                                                                        7                                                                         2                                                                               9
Female + White                                                                                       30                                          21                                                  24                                                                       61                                                                        56                                                                              45
Female + Black                                                                                        5                                          23                                                  21                                                                        6                                                                         7                                                                              19

Trait frequencies represent the percentage of traits (in this case out of 100 possible traits) that are associated with each intersectional grouping (e.g. the White Men
grouping is associated with 62 out of 100 traits, whereas the Black Men grouping is associated with 3 out of 100 traits). Frequencies are compared within a data source
(e.g. GloVe CC 840B) but across groupings, such that all four groupings within a data source will add up to 100. Bolded numbers indicate the highest relative percentage
for each intersectional quadrant (e.g. 62% is bolded to reflect that White Men is the grouping with the highest relative percentage of traits across all groupings for that
data source). The three contextualized embedding columns indicate three methods for extracting embedding vectors for groups. As described in the main text, single
words with templates indicates that a vector is created from averaging across the hidden state vectors for the template (e.g. “This is a”) and the first subtokens of group
words (e.g. “rich African woman”); pooled words with templates indicates that the vector is created from averaging across the hidden state vectors for the template and
the pooled group words (pooled across subtokens; e.g. “rich African + American woman); pooled words no template indicates that the vector is created from the first
four layers of the hidden state vectors pooled across only the group words (e.g. rich African + American woman).


well as what divergences teach us about how these models appear                                                                                                                                                                                             Interestingly, the data show less support for class-centrism, i.e.
to represent language and society.                                                                                                                                                                                                                      rich does not dominate frequencies in language to the same extent
                                                                                                                                                                                                                                                        that White supersede Black, or men supersede women. For ex­
                                                                                                                                                                                                                                                        ample, Black Poor (6% of traits) and Black Rich (5% of traits) are similar
Results                                                                                                                                                                                                                                                 in frequency showing that the low frequency of traits associated
Frequency of intersectional trait stereotypes                                                                                                                                                                                                           with Black is not altered even after including the dominant class
In the primary case of static embeddings, there is clear evidence of                                                                                                                                                                                    group Rich. Perhaps class may be less of a marked category in lan­
both androcentrism and ethnocentrism, such that any intersec­                                                                                                                                                                                           guage: we may be unlikely to point out that someone is rich, unless
tion, including Men (vs. Women) or White (vs. Black), dominates in                                                                                                                                                                                      it is extreme wealth, because categorizing class is prone to subject­
English language (Fig. 3; Table 2). Indeed, the highest relative fre­                                                                                                                                                                                   ive judgments of wealth cues (31). In contrast, race and gender may
quency of traits occurred for White Men, associated with 59% of                                                                                                                                                                                         be relatively less ambiguous in categorizations and therefore more
traits; the lowest relative frequency of traits occurred for Black                                                                                                                                                                                      likely to be noted in language and to shape trait frequencies.
Women, which was associated with only 5% of traits (Table 2). As
reported in the SI Appendix, the imbalances in trait frequencies                                                                                                                                                                                        Qualities of intersectional trait stereotypes
(e.g. the dominance of White Men over Black Women) deviated sig­                                                                                                                                                                                        As in study 1, our next analyses go beyond the overall number of
nificantly from chance, with effect sizes ranging from V = (0.26–                                                                                                                                                                                       traits to consider the specific traits and their qualities (Table 3).
0.56), equivalent to small-to-moderate effect sizes. Thus, English                                                                                                                                                                                      Specifically, we consider six qualities of traits that are of foundation­
language reveals evidence of intersectional dominance for power­                                                                                                                                                                                        al interest to group perception (25): (i) valence; (ii) dominance;
ful groups and intersectional invisibility for subordinate groups.                                                                                                                                                                                      (iii) arousal; (iv) warmth; (v) competence; and (vi) commonality


6 | PNAS Nexus, 2024, Vol. 3, No. 3


Table 3. Relative percentages of trait qualities (by valence, warmth, competence, arousal, dominance, commonality) within each
intersectional quadrant for GloVe CC 840B static embeddings.

                                                                  Valence                                              Warmth                      Competence                   Arousal                                     Dominance              Word common.
Intersectional grouping                                  Positive          Negative                              Warm            Cold        Comp           Incomp            High                           Low        High        Low

White + Rich                                                 78                22                                 81              19           78             22               48                            52             78          22                  4.13
White + Poor                                                 26                74                                 26              74           26             74               48                            52             26          74                  3.88
Black + Rich                                                 69                31                                 69              31           69             31               46                            54             65          35                  3.56
Black + Poor                                                 21                79                                 21              79           25             75               58                            42             21          79                  3.41
Male + Rich                                                  70                30                                 70              30           70             30               47                            53             70          30                  4.01


                                                                                                                                                                                                                                                                       Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
Male + Poor                                                  28                72                                 28              72           28             72               56                            44             28          72                  3.78
Female + Rich                                                78                22                                 83              17           78             22               48                            52             74          26                  3.63
Female + Poor                                                18                82                                 18              82           23             77               50                            50             18          82                  3.48
Male + White                                                 56                44                                 56              44           56             44               53                            47             56          44                  4.15
Male + Black                                                 43                57                                 43              57           43             57               48                            52             43          57                  3.57
Female + White                                               50                50                                 56              44           50             50               39                            61             50          50                  3.77
Female + Black                                               48                52                                 48              52           52             48               56                            44             44          56                  3.42

For all columns except the last one, numbers reflect the percentage of traits from the given quadrant (e.g. from the intersectional grouping of White Rich) that are, for
example, coded as positive (vs. negative). The “word common” column reflects the average Zipf score across all traits in that quadrant. Zipf scores are the base-10
logarithm of the number of times a word appears in a billion words. For instance, Zipf = 4.13 for the White Rich quadrant reflects that the traits associated with this
quadrant have occurred in language 104.14 times, or ∼13,490 times, for every 1 billion words.


                      3                                                                                     3                                                                                      3
                                Positive    Negative


                      2         Female + White                        Male + White                          2          Female + Rich                        Male + Rich                            2         Black + Rich                          White + Rich


                      1                                                                                     1                                                                                      1


    Race Difference                                                                      Class Difference                                                                       Class Difference
                      0                                                                                     0                                                                                      0


                      −1                                                                                    −1                                                                                     −1


                      −2        Female + Black                        Male + Black                          −2         Female + Poor                        Male + Poor                            −2        Black + Poor                          White + Poor


                      −3                                                                                    −3                                                                                     −3


                           −3          −2        −1      0        1        2         3                            −3        −2         −1      0        1        2        3                             −3         −2       −1      0          1        2          3

                                                 Gender Difference                                                                     Gender Difference                                                                     Race Difference

Fig. 4. Valence of traits (after z-scoring) associated with intersectional comparisons of (A) gender-by-race, (B) gender-by-class , and (C) race-by-class.
Traits are color-coded by valence. All figures use data from the GloVe Common Crawl 840-billion data source of static embeddings. Analogous plots for the
other five methods and data sources are provided in supplemental material.


(how often a given trait is used in everyday contemporary English).                                                                                trait (32)) as well as qualities of warmth/coldness and compe­
To examine such qualities, we ensure that each quadrant has a rela­                                                                                tence/incompetence (25). For warmth/coldness, competence/in­
tively similar representation in number of traits, as this control al­                                                                             competence, and dominant/nondominant traits, results paralleled
lows us to compute the relative qualities of intersectional groups                                                                                 valence: intersections including powerful groups of White, Rich, or
independent of their imbalance of representation. Additionally,                                                                                    Men were not only more likely to be positive, but were also more like­
this control is required to ensure that even low-frequency quad­                                                                                   ly to be associated with traits expressing warmth, competence, and
rants (e.g. Black Rich, associated with only five traits) have sufficient                                                                          dominance (Table 3). As one example, for Rich White, 81% of traits
representation to examine the relative qualities. Thus, we first                                                                                   were warm, 78% were dominant, and 78% were competent. In con­
mathematically adjust the frequencies across quadrants by                                                                                          trast for Poor Black, 79% of traits were cold, 79% were subordinate,
z-scoring the placement of each trait along individual group dimen­                                                                                and 75% were incompetent. Such findings emphasize the “halo ef­
sions and compute each quadrant’s average scores of the traits”                                                                                    fects” (i.e. the unwarranted generalization of positivity across mul­
qualities. Crucially, even after re-scaling the number of traits across                                                                            tiple dimensions (33)) that become amplified for powerful
quadrants, the features of those traits continue to show intersection­                                                                             intersectional groups. Only the dimension of arousal did not differ­
al differences (Table 3 for GloVe 840B; results for all embeddings in                                                                              entiate across intersectional groups, perhaps because this dimen­
SI Appendix).                                                                                                                                      sion is often seen as a less central dimension of meaning (32), and
   First, intersections differed in their relative proportion of posi­                                                                             thus may not be as relevant to distinguish between social categories.
tive/negative traits (Fig. 4 and Table 3). For example, 78% of traits                                                                                  Finally, intersectional social group quadrants also differed in
associated with White Rich were positive, while only 21% of traits                                                                                 how common the associated traits were in everyday language, us­
associated with Black Poor were positive. In general, valence imbal­                                                                               ing commonality scores (as Zipf scores, see Methods) taken from
ances appeared to be the largest across class (Rich/Poor).                                                                                         the wordfreq norms in Python (34). Traits associated with any
   Second, traits differ in word arousal (degree of “activity” evoked                                                                              White, Men, or Rich intersection were more commonly used in lan­
by the trait) and dominance (degree of “control” evoked by the                                                                                     guage than traits associated with any Black, Women, or Poor


                                                                                                                         Charlesworth et al. |     7


intersection (Table 3). For instance, the traits associated with Rich        intersectional stereotypes across occupations and personality traits
Men had, on average, 10,232 occurrences per billion words (Zipf =            at the intersection of gender, race, and social class. A primary aim
4.01, equivalent to 104.01). In contrast, the traits associated with         was to illustrate the kinds of empirical insights that can come
Poor Women had, on average, 3,020 occurrences per billion words              from this new methodological approach. Although many of the
(Zipf = 3.48, or 103.48 occurrences), corresponding to roughly one-          nuanced findings about individual groupings, traits, and occupa­
third the commonality of Rich Men traits. Imbalances in common­              tions remain beyond the scope of this first analysis, we emphasize
ality reveal further andro-, ethno-, and class-centrism in lan­              four overarching empirical conclusions that can help propel inter­
guage. When it comes to our most common traits (e.g. friendly,               sectional analyses: (i) the alignment of intersectional stereotypes
happy, and smart), powerful groups dominate; subordinate groups,             in English language with ground-truth US data, emphasizing how


                                                                                                                                                        Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
in contrast, are relegated to description with more idiosyncratic            language both reflects and reinforces social patterns; (ii) the lan­
traits (e.g. manipulative, spiteful, and spirited) that may, in turn, con­   guage dominance (frequency) of powerful intersectional groups, as
tribute to perceptions of nonprototypicality.                                well as the relative invisibility of subordinate intersectional groups;
                                                                             (iii) the “halo effects” that surround powerful intersectional groups,
                                                                             especially those involving high social class; and (iv) informative di­
Differences between static and contextualized
                                                                             vergences (and convergences) between static and contextualized
embeddings
                                                                             language models.
So far, we have focused on describing the general pattern of results
for static embedding models, which remain the most widely used
method in the social sciences. However, given the flexibility of             Frequencies of intersectional occupational
FISE procedure, we can also compare results across contextualized            stereotypes: alignment with ground-truth data
embeddings from BERT (Table 2). That is, we can compare the re­              In study 1, we sought to validate FISE by showing that results of
sults of the relative frequencies of traits classified into intersectional   intersectional occupation stereotypes identified from English lan­
quadrants (e.g. how many traits are classified as associated with            guage align with ground truth on actual occupational demographics
White Men) not only across multiple static embeddings from various           of those occupations in the United States. In addition to the rele­
algorithms (fastText and GloVe) and data sources (Wikipedia, Common          vance of occupational stereotypes for understanding workforce dis­
Crawl) but also across contextualized embeddings with additional             crimination in hiring and pay (29, 37), occupational stereotypes also
variations in embedding extraction methods (SI Appendix).                    provide a necessary setting for validating a new method because
    The frequencies of classified traits across six different models         they have associated ground-truth data on demographic represen­
and methods are listed in Table 2. Chi-squared tests evaluating              tations. Indeed, classifications of 143 occupations into their intersec­
how similar these frequencies are across methods showed small                tional quadrants showed evidence that FISE validly identifies true
overall effect sizes, implying that static and contextualized models         signal from real-world data. First, intersectional quadrants that do­
generally reveal similar patterns of frequencies: for race-by-class,         minated in the real-world data (e.g. White Men were associated with
χ2(15) = 59.02, P < 0.001, V = 0.18; for gender-by-class, χ2(15) = 64.23,    the most occupations in the real-world) also dominated in language
P < 0.001, V = 0.19; and for race-by-gender, χ2(15) = 100.03,                associations. Second, when specific occupations provided arguably
P < 0.001, V = 0.24.                                                         clear signal in ground-truth data (e.g. they were >70% female and
    Nevertheless, we identify one seemingly systematic difference            >70% White), language associations correctly classified the occupa­
between results for static and contextualized embeddings when it             tion into the specific intersectional quadrant (e.g. as White Women).
comes to the gender-by-class and gender-by-race comparisons.                 When specific occupations provided more ambiguous signal (e.g. fe­
For static embeddings, whenever gender was included, the great­              male representation was ∼50%), the language also showed that am­
est frequency (as well as positivity, commonality, etc.) was associ­         biguity (e.g. showed incorrect classifications of gender), thus
ated with the default group (e.g. Rich Men) (35). Such patterns of           providing an accurate reflection of the signal in reality.
“default” group dominance reflect the ground truth of how groups                Beyond validation of FISE, such results also illustrate new in­
dominate in the world (see study 1). For contextualized embeddings,          sights and opportunities for future research on the intersectionality
however, the greatest frequency (and positivity and commonality)             of workforce demographics. For instance, as elaborated below, the
was associated with the intersectional grouping that joined female           dominance of a group in language can, in turn, feed back into legit­
(a low-power group compared with male) with a higher power class             imizing the group’s dominance in the world (38). The dominance of
group (e.g. Rich Women). Perhaps, in contextualized embeddings,              White Men or Rich Men in the language of occupations may hamper
group information is considered more jointly since the group labels          other strategies to create change in workforce demography (39).
are provided together in a single sentence. Thus, seemingly incon­           Given the unique flexibility of FISE for application across historical
gruent pairings of high-power female groups are more easily noted            language (compared with previous approaches that were less gener­
and “marked” in the model (8). This marking could increase the fre­          alizable), future research can, for the first time, examine questions
quency of traits associated with the group.                                  including how occupation stereotypes in language hinder or help
                                                                             changes in workforce demographics.


General discussion                                                           Frequencies of intersectional trait stereotypes: the
Computational and social sciences have both increasingly recog­              dominance of powerful groups
nized the need for intersectional approaches to understand social            Having provided initial validation of the accuracy of FISE, we turned
biases and their impacts (7, 21, 36). And yet, despite the call for          to trait-based stereotypes, a domain that has no ground-truth data
more intersectional research there remains, to our knowledge, no             but underlies the content of most group stereotypes (25, 40). These
simple, flexible, and transparent approach to quantifying intersec­          frequencies of traits uncovered clear patterns of androcentrism, or
tional stereotype content, at-scale in massive language data. In             the dominance of Men in everyday culture and language, a finding
this study, we introduce such a method for interdisciplinary re­             that we and others have documented and discussed, albeit at small­
search—the FISE procedure. We apply FISE to a first case study of            er scales (41, 42). However, the current work is among the first to


8 | PNAS Nexus, 2024, Vol. 3, No. 3


also emphasize the extent of ethnocentrism, or the dominance of          incongruent nondefault groups (e.g. White Women or Rich
Whiteness in Internet text. Such findings add new quantitative evi­      Women), where one group dimension contains power (e.g. White
dence to past qualitative theorizing on the White “default” in culture   and Rich), but the other group (Female) is subordinate. Perhaps,
(43) and show that it is of the same scale as the masculine defaults     the focus on “markedness” arises for contextualized embeddings
seen in previous work.                                                   because of the joint consideration of all group dimensions that
   The dominance of both Men and Whiteness in language pat­              might more readily highlight the unexpected (incongruent) group
terns has downstream consequences in Artificial Intelligence             of “powerful females” (51). These differences between static and
(AI) and language applications (e.g. in machine translation, text        contextualized models can help researchers make informed deci­
classification, and text generation). Indeed, so much of the ob­         sions about which models to use based on their interests in de­


                                                                                                                                                 Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
served bias in AI more generally seems to be a result of imbalances      fault vs. markedness of subordinate groups. Additionally, future
in the training data. For example, AI-generated faces are judged as      work can identify what methodological differences between static
more realistic than natural human faces, but only for White faces        and contextualized embeddings help explain why default vs.
due to the dominance of White faces in training data (44, 45).           marked gender groups are differentially emphasized across
Moreover, androcentric and ethnocentric dominance can also               methods.
serve to reify mental stereotypes about which groups should dom­
inate in society. For example, experimental research has shown
that the frequency of women vs. men in Google search outputs             Limitations
shapes beliefs about the default “person” as well; cultures that         In supplemental analyses, we test and demonstrate the robust­
have greater male-dominated search outputs also more strongly            ness of inferences across modeling approaches (static, contex­
endorse androcentric defaults (38). In short, the current results        tualized) and additional specifications (how groups were
may play into a feedback loop in which language both reflects            represented, the numbers of traits, types of traits, verb, or noun
and reinforces existing social imbalances—imbalances that are            lists; SI Appendix). Despite general patterns of consistency and ro­
magnified in intersectional comparisons (6, 46).                         bustness across such tests, the current inferences face other lim­
                                                                         itations. First, there are theoretical limitations: social group
Qualities of intersectional trait stereotypes: halo                      intersectionality is sometimes (but not always) thought of as an
effects                                                                  inherently contextualized, emergent phenomenon that is nonad­
                                                                         ditive (7, 36, 52). Therefore, the FISE approach of crossing two
Beyond frequency, we also consider the intersectional differen­
                                                                         (independently created) axes from single dimensions of groups
ces in the qualities of the stereotype content, specifically the
                                                                         may not be an appropriate methodological assumption. While
average positivity, warmth, competence, dominance, and com­
                                                                         this is an inherent limitation for addressing some theoretical
monality (i.e. how common the traits are in everyday language
                                                                         perspectives, we emphasize that the general results were broadly
use). The results show that any intersection that included
                                                                         convergent across contextualized and static approaches. Thus,
Rich, and, to a lesser extent, White or Men, consistently anchored
                                                                         the FISE procedure (even applied to static embeddings) appears
the positive end of the spectrum (e.g. positive, warm, and com­
                                                                         to be sufficient to approximate a contextualized process of
petent). Notably, class was the strongest dimension determin­
                                                                         intersectionality.
ing the qualities of traits, with Rich generating “halo effects”
                                                                             Additionally, FISE relies on representing group and attribute
(47) across all qualities. This may be surprising considering ex­
                                                                         concepts in text. Especially in the case of static embeddings
plicit measures suggesting that stereotypes of Richness often
                                                                         (where group concepts are lists of single words rather than con­
generate mixed content (e.g. competent but also cold (25, 48)).
                                                                         textualized sentences), the results remain limited by concerns
However, evidence of “halo effects” are especially likely to be
                                                                         around polysemy (e.g. Black and White also refer to colors), and fre­
observed with relatively indirect measures of stereotyping (33,
                                                                         quency (e.g. some group words like impoverished are more rare
49), as in the current research.
                                                                         than everyday words like men). Here and in previous work (12),
                                                                         we have attempted to rule out concerns of polysemy by using lists
Comparison of static and contextualized models                           of words that, together, triangulate toward the intended group
As its name suggests, the primary advantage of the FISE procedure        concept, and have shown that this list-based approach indeed
is its flexibility for application across any embedding model, in­       captures the group concept rather than alternative polysemous
cluding both static (GloVe) and contextualized models (BERT)             meanings. Moreover, here we show that even two different ways
trained on diverse Internet data sources. Critically, emphasizing        of representing the group concepts (with lists of 4 or 12 words)
the robustness of primary conclusions, results within all static         yield similar overarching conclusions (SI Appendix).
models were consistent with one another (i.e. all showed similar             Finally, we note that readers may question the relevance of
patterns of the relative frequencies and features of traits), and re­    FISE at a moment when the current static embeddings and BERT
sults within all contextualized embedding approaches were con­           contextualized embeddings are surpassed by more sophisticated
sistent with one another. Additionally, static and contextualized        language model competitors. We see the approach as holding con­
models agreed for frequencies and features of traits in the              tinued relevance because static embedding models will continue
class-by-race contrast, with White Rich consistently associated          to be used for their wide availability, transparency, and flexibility
with the most traits and the most positive traits, regardless of         for training on diverse (and relatively small) datasets. As such,
method.                                                                  demonstrating methods to use static and simple contextualized
    At the same time, however, the few divergences between static        models for intersectional analyses is crucial. Although LLMs like
and contextualized approaches were also informative. Static em­          GPT (Generative Pre-trained Transformer) are widely discussed
beddings seem to capture the dominance of “default” powerful             and increasingly used, they suffer from serious limitations of non­
groups in language (e.g. White Men) in which both group dimen­           representative training data, as well as limited transparency (53).
sions (e.g. gender and race) reflect high power. Contextualized em­      Nevertheless, we look forward to future work generalizing FISE to
beddings, however, seem to capture the “markedness” (50) of              more sophisticated language models, including the newly


                                                                                                                       Charlesworth et al. |     9


developed contextualized construct representations argued to be            Application to contextualized word embeddings
more aligned with psychological representations (54).                      The above procedure can be adapted to most cases in which embed­
   More generally, we look forward to future research using FISE           dings are extracted for group and trait representations, including for
as interdisciplinary infrastructure for addressing long-standing           contextualized embeddings, such as BERT. We demonstrate such an
questions of intersectional stereotyping, especially on the preva­         extension by adapting FISE for use with the BERT base-uncased model
lence and features of emergent content (not contained in parent            and three previously validated methods for retrieving embeddings
group stereotypes). With such tools, the study of intersectionality        of group representations from the model (described below).
and emergence can be expanded in real-world language at an un­                 The FISE procedure for contextualized embeddings again fol­
precedented scale, even across place, languages, demographics,             lows five steps (Fig. 5). First, and different from static applications,


                                                                                                                                                      Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
and history.                                                               group targets are operationalized using group sentence probes
                                                                           (Fig. 1) to include all three intersectional group identities at once
                                                                           (e.g. “This is a rich black man”) varying class (words representing
Methods                                                                    rich/poor), race (words representing Black/White), and gender
                                                                           (words representing man/woman). These three group targets are
Application of FISE to static word embeddings
                                                                           placed in a semantically bleached template (e.g. “This is,” “That
Our primary test case is the set of pretrained GloVe embeddings
                                                                           is,” and so on); templates are semantically bleached to ensure
trained on 840-billion-word tokens from the Common Crawl; rep­
                                                                           that the extracted embedding captures the signal associated
lications for static embeddings are performed across GloVe em­
                                                                           with the main (in this case, group-related) stimulus. Attributes
beddings trained on 6 billion tokens from Wikipedia, and
                                                                           (in this case, we only use traits) are also operationalized using sen­
fastText embeddings trained on Wikipedia. After choosing the
                                                                           tence probes with the traits placed in a semantically bleached
text corpus, FISE proceeds in five steps. First, we identify a list of
                                                                           template (e.g. “They are kind/unkind”).
target concepts. In study 1, we use ∼150 occupation labels gener­
                                                                               Second, to extract associations of a target word with a single
ated from the 2022 Bureau of Labor Statistics report (55); occupa­
                                                                           group dimension (e.g. class), we need to average across the other di­
tion labels, methods for generating them, and approaches to
                                                                           mensions (e.g. gender, race) that were used in the original contex­
classify occupations into intersectional quadrants are detailed
                                                                           tualized sentences. To that end, for each trait target word (e.g.
in the SI Appendix. In study 2, we use 100 traits drawn from a
                                                                           kind), we compute the average cosine similarity to a given three-
list of ∼400 available traits (56) but only the 50 most positive and
                                                                           way target intersection (e.g. rich white men) as well as to the com­
50 most negative traits based on ratings from Warriner et al.
                                                                           parison target intersection that varies only on the group dimension
(57); replications with longer lists of 200 and 300 traits are reported
                                                                           of interest (e.g. poor white men, when we are looking at CLASS). We
in SI Appendix.
                                                                           then take the difference between these two cosine similarities
    Second, for each occupation/trait concept (e.g. kind) we com­
                                                                           (e.g. kind-rich white men − kind-poor white men = kind-CLASS white
pute cosine similarities between the embeddings for the target
                                                                           men effect). We perform this for all contrasts along the dimension
word (ti) and all words representing a given group concept (WgA,
                                                                           of interest to yield kind-CLASS effects for White Men, Black Men,
e.g. Rich, which is represented by group words including rich, weal­
                                                                           White Women, and Black Women. We then average across these
thy, affluent, and so on; see Fig. 1 for all words), and divide by the
                                                                           four contrasts for a single kind-CLASS association. Third, we repeat
number of words in that group representation (NgA) yielding an
                                                                           the above computations for a second group dimension (i.e. gender
average word-group A association (e.g. kind-Rich association;
                                                                           or race). Fourth, we place each target trait in an x-y coordinate
Eq. 1). We then repeat the procedure for the contrast group (e.g.
                                                                           space. And fifth, we perform all analyses of frequency and content.
kind-Poor). For analyses in which we use z-scored results, we
standardize scores at this stage, taking each ti score, subtracting
the mean across scores, and dividing by the standard deviation             Extracting embeddings from contextualized
across all scores.                                                         models
                                􏽐                                          While static embeddings provide the embeddings off-the-shelf,
                                  cos(WgA , ti )
                        ti(A) =                  .                   (1)   contextualized embeddings require an additional step to extract
                                     NgA
                                                                           embeddings of a given sentence. For robustness, we employ three
Third, we take the difference between averaged cosine similar­             common approaches for extracting embeddings from the BERT
ities to get the placement of the target word along the given              model (58): (i) embedding templates (20); (ii) pooled embedding
group dimension (e.g. kind-Rich − kind-Poor = kind-CLASS; Eq. 2)           templates; and (iii) without templates.
and repeat for all other dimensions of groups (in this case, also              First, “embedding templates” (20) extract embeddings of a given
gender and race, to also extract the kind-GENDER and kind-RACE             set of group words in our embedding template (e.g. “rich,” “African
placement).                                                                American,” and “woman” in the template “this is a”), by pulling
                                                                           the BERT embeddings of the first subtoken in the group words (e.g.
                          ti(AvB) = ti(A) − ti(B) .                  (2)
                                                                           “rich,” “African,” “woman”). Next, we use the hidden state vectors
Fourth, we bring in the intersectional analysis by crossing two            (only the top-most BERT layer) of those subtokens and average
group dimensions (e.g. class and gender) in an x-y coordinate              across the three group subtokens (rich, African, woman). This yields
space and place each target word in that space according to its            a single vector embedding for the BERT representation of the group
association with the respective group dimensions (e.g. ti(AvB) rep­        target “rich, African American woman” as it is contextualized in the
resents the x-axis of CLASS, while ti(CvD) represents the y-axis of        sentence “This is a rich African American woman.”
RACE). This x-y space reveals the intersectional stereotypes asso­             Second, “pooled embedding templates,” begins as above but, in­
ciated with each of the four group intersections (e.g. Rich Men,           stead of taking the hidden state vectors of only the first subtoken
Rich Women, Poor Men, and Poor Women). Fifth and finally, the fre­         for each group-related word, we instead take the mean pooled em­
quency and qualities of these associated traits/occupations is             beddings of all subtokens of the group-related words. To continue
analyzed.                                                                  with our example, in the sentence, “This is a rich African


10 |    PNAS Nexus, 2024, Vol. 3, No. 3


                                    That is a Rich White Woman                       That is a Poor White Woman
       intellectual                 That is a Wealthy White Woman                    That is a Needy White Woman
                                                                                                                                 CLASS intellectual
                                                                            vs.                                                  score (0.15)
                                    That is a Rich Black Woman                       That is a Poor Black Woman
                                    That is a Wealthy Black Woman                    That is a Needy Black Woman


                                     That is a Rich White Man                        That is a Rich White Woman


                                                                                                                                                                         Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
        intellectual                 That is a Rich White Boy                        That is a Rich White Girl
                                                                            vs.
                                                                                                                                 GENDER intellectual
                                     That is a Rich Black Man                        That is a Rich Black Woman                  score (0.10)
                                     That is a Rich Black Boy                        That is a Rich Black Girl


                                                                                    [CLASS intellectual score (0.15),
                                                                     Rich           GENDER-intellectual score (0.10)]


                                          Women                                           Men


                                                                    Poor
Fig. 5. Illustration of the application of FISE. In the case of static embeddings, only the lower half of the figure applies: each target trait (e.g. intellectual) is
associated with two single group dimension (e.g. CLASS, based on relative associations to Rich vs. Poor) and then placed in the intersectional x-y space
according to its associations with the two group dimensions. In the case of contextualized embeddings, we use sentence prompts (top half of figure) and
average across all instances of a given group concept (e.g. Rich) vs. the contrasting group (e.g. Poor) to arrive at the group dimension-trait association. As
with the static embeddings application, the final step is to place each trait in the x-y space defined by the two group dimensions.


American woman,” we first take the average across the hidden                         300 traits,” as above but now with 300 traits total; (v) “Model 5:
state vectors for “African” and “American” (the only target word                     Nouns” in which we use parts-of-speech tagging and extract the
with two subtokens) to create a single pooled embedding vector                       top-100 positive/negative nouns (replacing the trait list); and (vi)
for “African American.” We then calculate the average across                         “Model 6: Verbs” in which we change the trait list to top-100 posi­
the pooled embedding of “African American” with the embeddings                       tive/negative verbs.
of “rich” and “woman” (which were only one subtoken and so did                           As elaborated in SI Appendix, the primary empirical conclu­
not need to be pooled) to again obtain a single vector representa­                   sions from study 2 were retained across model variations. First, re­
tion of the group words in the contextualized sentence.                              gardless of (i) how many traits we used (100, 200, and 300),
    Third and finally, “without templates,” we move beyond tem­                      (ii) whether we represented groups with full or with reduced lists
plates, which, although argued to be semantically bleached,                          (of only 4 most central terms), and (iii) whether we used nouns,
may nevertheless convey information that distracts from the tar­                     verbs, or the original trait lists, raw frequencies continued to
get group representations. Instead of templates, we average over                     show patterns of andro-, ethno-, and, to a lesser extent, class-
the pooled embeddings for just the three group words using the                       centrism. Second, even after mathematically aligning frequencies
first four layers of the BERT model for each target word (59, 60).                   using z-scoring, we found that the features of traits continued to
Consider again the example of assessing stereotypes to “rich                         differ across intersectional groupings, with relatively greater posi­
African American woman,” in this setting we calculate the aver­                      tivity, warmth, competence, and dominance for intersectional
age of the pooled embeddings for three group words (“rich,”                          quadrants including White, Rich, or Men.
“African American,” and “woman”) across the first four layers of
BERT. We do not include the embeddings of any template words
in the final average.                                                                Supplementary Material
                                                                                     Supplementary material is available at PNAS Nexus online.
Robustness and sensitivity analyses
To verify the robustness and generalizability of our results for the
more novel analyses of trait stereotypes, we test 6 variations of
                                                                                     Funding
trait and group lists. In addition to (i) “Model 1: Full model,” in                  This research was supported by a Social Sciences and Humanities
which we use the full 24 group words for each dimension (see                         Research Council of Canada Postdoctoral Fellowship, and the
Fig. 1) and the list of 100 traits, we also compute the following var­               Rand Innovation Fund from the Harvard Department of
iations: (ii) “Model 2: Reduced group words” in which we change                      Psychology awarded to Tessa Charlesworth, and the Hodgson
the group list to include only the 4 most central group-related                      Innovation Fund from the Harvard Department of Psychology
words (bolded in Fig. 1); (iii) “Model 3: 200 traits” in which we ex­                awarded to M.R.B. This work is supported by the National
tend the list of traits to include the top 100 most positive and                     Institute of Standards and Technology (NIST) Grant
top 100 most negative traits from the Peabody list; (iv) “Model 4:                   60NANB23D194. Any opinions, findings, and conclusions or


                                                                                                                     Charlesworth et al. | 11


recommendations expressed in this material are those of the au­            16 Grave E, Bojanowski P, Gupta P, Joulin A, Mikolov T. 2018.
thor and do not necessarily reflect those of NIST.                            Learning word vectors for 157 languages. In: Proceedings of the
                                                                              Eleventh International Conference on Language Resources and
                                                                              Evaluation (LREC 2018); Miyazaki, Japan. European Language
Author Contributions
                                                                              Resources Association (ELRA).
T.E.S.C. and M.R.B. conceptualized the project; T.E.S.C. developed         17 Hamilton WL, Leskovec J, Jurafsky D. 2016. Diachronic word em­
the methodology; T.E.S.C. and K.G. performed the formal analysis;             beddings reveal statistical laws of semantic change. 54th Annual
T.E.S.C., M.R.B., and A.C. provided the funding acquisition; T.E.S.C.         Meeting of the Association for Computational Linguistics, ACL
wrote the original draft of the manuscript. All authors reviewed              2016—Long Papers; Berlin, Germany, Vol. 3. p. 1489–1501.


                                                                                                                                                     Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
and edited the manuscript.                                                 18 Charlesworth TES, Yang V, Mann TC, Kurdi B, Banaji MR. 2021.
                                                                              Gender stereotypes in natural language: word embeddings
Data Availability                                                             show robust consistency across child and adult language cor­
All data and analyses reported in this work are publicly available            pora of more than 65 million words. Psychol Sci. 32:218–240.
through https://osf.io/b9nmd/.                                             19 Devlin J, Chang M-W, Lee K, Toutanova K. 2018. BERT: pre-
                                                                              training of deep bidirectional transformers for language under­
References                                                                    standing. Proceedings of North American Chapter of the
                                                                              Association for Computational Linguistics-Human Language
1    Cole ER. 2009. Intersectionality and research in psychology. Am
                                                                              Technologies 2019; Minneapolis (MN). p. 4171–4186.
     Psychol. 64:170–180.
                                                                           20 Tan YC, Celis LE. 2019. Assessing social and intersectional biases
2    Hall EV, Hall AV, Galinsky AD, Phillips KW. 2019. MOSAIC: a mod­
                                                                              in contextualized word representations. In: Proceedings of the
     el of stereotyping through associated and intersectional categor­
                                                                              33rd    International    Conference    on    Neural    Information
     ies. Acad Manage Rev. 44:643–672.
3    Petsko CD, Rosette AS, Bodenhausen GV. 2022. Through the look­           Processing Systems. Curran Associates Inc.; Red Hook (NY).
     ing glass: a lens-based account of intersectional stereotyping. J        Article 1185, p. 13230–13241.
     Pers Soc Psychol. 123:763–787.                                        21 Guo W, Caliskan A. 2021. Detecting emergent intersectional
4    Kunda Z, Miller DT, Claire T. 1990. Combining social concepts:           biases: contextualized word embeddings contain a distribution
     the role of causal reasoning. Cogn Sci. 14:551–577.                      of human-like biases. In: Proceedings of the 2021 AAAI/ACM
5    Coles SM, Pasek J. 2020. Intersectional invisibility revisited: how      Conference on AI, Ethics, and Society (AIES ’21). New York
     group prototypes lead to the erasure and exclusion of black              (NY): Association for Computing Machinery. p. 122–133. https://
     women. Transl Issues Psychol Sci. 6(4):314–324 .                         doi.org/10.1145/3461702.3462536
6    Purdie-Vaughns V, Eibach RP. 2008. Intersectional invisibility:       22 May C, Wang A, Bordia S, Bowman SR, Rudinger R. 2019. On
     the distinctive advantages and disadvantages of multiple                 measuring social biases in sentence encoders. NAACL HLT
     subordinate-group identities. Sex Roles. 59:377–391.                     2019—Proceedings of the 2019 Conference of the North American
7    Nicolas G, de la Fuente M, Fiske ST. 2017. Mind the overlap in           Chapter of the Association for Computational Linguistics: Human
     multiple categorization: a review of crossed categorization, in­         Language Technologies—; Minneapolis (MN). Vol. 1. p. 622–628.
     tersectionality, and multiracial perception. Group Process            23 Pachankis JE, et al. 2018. The burden of stigma on health and
     Intergroup Relat. 20:621–631.                                            well-being: a taxonomy of concealment, course, disruptiveness,
8    Nicolas G, Fiske ST. 2023. Valence biases and emergence in the           aesthetics, origin, and peril across 93 stigmas. Pers Soc Psychol
     stereotype content of intersecting social categories. J Exp              Bull. 44:451–474.
     Psychol Gen. 152:2520–2543.                                           24 Dovidio JF, Gaertner SL. 2010. Intergroup bias. In: Fiske S, Gilbert
9    Pennington J, Socher R, Manning CD. 2014. Glove: global vectors          D, Lindzey G, editors. The handbook of social psychology. Hoboken
     for word representation. In: Proceedings of the 2014 Conference
                                                                              (NJ): Wiley Publishing. p. 1084–1121. https://doi.org/10.1002/
     on Empirical Methods in Natural Language Processing (EMNLP);
                                                                              9780470561119.socpsy002029
     Doha, Qatar. p. 1532–1543. https://doi.org/10.3115/v1/d14-1162
                                                                           25 Fiske ST, Cuddy AJC, Glick P, Xu J. 2002. A model of (often mixed)
10   Caliskan A, Bryson JJ, Narayanan A. 2016. Semantics derived
                                                                              stereotype content: competence and warmth respectively follow
     automatically from language corpora necessarily contain hu­
                                                                              from perceived status and competition. J Pers Soc Psychol. 82:
     man biases. Science. 356:183–186.
                                                                              878–902.
11   Garg N, Schiebinger L, Jurafsky D, Zou J. 2018. Word embeddings
                                                                           26 Blasi DE, Henrich J, Adamou E, Kemmerer D, Majid A. 2022.
     quantify 100 years of gender and ethnic stereotypes. Proc Natl
                                                                              Over-reliance on English hinders cognitive science. Trends Cogn
     Acad Sci U S A. 115:E3635–E3644.
                                                                              Sci. 26:1153–1170.
12   Charlesworth TES, Caliskan A, Banaji MR. 2022. Historical repre­
                                                                           27 Charlesworth TES, Sanjeev N, Hatzenbuehler ML, Banaji MR.
     sentations of social groups across 200 years of word embeddings
                                                                              2023. Identifying and predicting stereotype change across 72
     from google books. Proc Natl Acad Sci U S A. 119:e2121798119.
13   Charlesworth TES, Morehouse K, Rouduri V, Cunningham WA.                 groups, four text sources, and historical time (1900–2015): in­
     2023. Traces of Human Attitudes in Contemporary and                      sights from word embeddings. J Pers Soc Psychol. 125:969–990.
     Historical Word Embeddings (1800-2000). Manuscript Submitted          28 Kirk HR, et al. 2021. Bias out-of-the-box: an empirical analysis of
     for Publication.                                                         intersectional occupational biases in popular generative lan­
14   Kozlowski AC, Taddy M, Evans JA. 2019. The geometry of culture:          guage models. Proceedings of the 35th Conference on Neural
     analyzing the meanings of class through word embeddings. Am              Information Processing Systems.
     Sociol Rev. 84:905–949.                                               29 Stasio D, Larsen V, N E. 2020. The racialized and gendered work­
15   Lewis M, Cooper Borkenhagen M, Converse E, Lupyan G,                     place: applying an intersectional lens to a field experiment on
     Seidenberg MS. 2021. What might books be teaching young chil­            hiring discrimination in five European labor markets. Soc
     dren about gender? Psychol Sci. 33(1):33–47.                             Psychol Q. 83:229–250.


12 |   PNAS Nexus, 2024, Vol. 3, No. 3


30 American Association of University Women. 2018. The Simple            47 Wu SJ, Bai X, Fiske ST. 2018. Admired rich or resented rich? How
   Truth about the Gender Pay Gap [accessed 2022 Sept 1].                   two cultures vary in envy. J Cross Cult Psychol. 49:1114–1143.
   https://www.aauw.org/resources/research/simple-truth/                 48 Durante F, Tablante CB, Fiske ST. 2017. Poor but warm, rich but
31 Rinn R, Ludwig J, Fassler P, Deutsch R. 2022. Cues of wealth and          cold (and competent): social classes in the stereotype content
   the subjective perception of rich people. Curr Psychol. 42:              model. J Soc Issues. 73:138–157.
   27442–27457                                                           49 Greenwald AG, Banaji MR. 1995. Implicit social cognition: atti­
32 Osgood CE, Suci GJ, Tannenbaum PH. 1967. The measurement of              tudes, self-esteem, and stereotypes. Psychol Rev. 102:4–27.
   meaning. Champaign (IL): University of Illinois Press.                50 Battistella EL. 1990. Markedness: the evaluative superstructure of lan­
33 Nisbett RE, Wilson TD. 1977. The halo effect: evidence for uncon­        guage. Albany (NY): SUNY Press.


                                                                                                                                                      Downloaded from https://academic.oup.com/pnasnexus/article/3/3/pgae089/7626925 by Harvard University Library user on 27 March 2024
   scious alteration of judgments. J Pers Soc Psychol. 35:250–256.       51 Wolfe R, Caliskan A. 2022. Markedness in visual semantic AI.
34 Speer R. 2022. GitHub—rspeer/wordfreq: Access a database of
                                                                             ACM International Conference Proceeding Series. p. 1269–1279.
   word frequencies, in various natural languages [accessed 2022
                                                                            https://doi.org/10.1145/3531146.3533183
   Sept 1]. https://github.com/rspeer/wordfreq
                                                                         52 Hester N, Payne K, Brown-Iannuzzi J, Gray K. 2020. On intersec­
35 Cheryan S, Markus HR. 2020. Masculine defaults: identifying and
                                                                             tionality: how complex patterns of discrimination can emerge
   mitigating hidden cultural biases. Psychol Rev. 127:1022–1052.
                                                                            from simple stereotypes. Psychol Sci. 31:1013–1024.
36 Petsko CD, Bodenhausen GV. 2020. Multifarious person percep­
                                                                         53 Abdurahman S. et al. 2024. Perils and opportunities in using large
   tion: how social perceivers manage the complexity of intersec­
                                                                             language models in psychological research. https://doi.org/10.
   tional targets. Soc Personal Psychol Compass. 14:e12518.
37 Cech EA, et al. 2020. LGBT workplace inequality in the federal           31219/OSF.IO/TG79N
   workforce: intersectional processes, organizational contexts,         54 Atari M, Omrani A, Dehghani M. 2024. Contextualized construct
   and turnover considerations. ILR Rev. 73:25–60.                           representation: leveraging psychometric scales to advance
38 Vlasceanu M, Amodio DM. 2022. Propagation of societal gender              theory-driven text analysis. https://doi.org/10.31234/OSF.IO/
   inequality by internet search algorithms. Proc Natl Acad Sci U S         M93PD
   A. 119:1–8.                                                           55 US Bureau of Labor Statistics, and Current Population Survey.
39 O’brien KR, Scheffer M, Van Nes EH, Van Der Lee R. 2015. How to           2022. HOUSEHOLD DATA ANNUAL AVERAGES. 39. Median
   break the cycle of low workforce diversity: a model for change.           weekly earnings of full-time wage and salary workers by detailed
   PLoS One. 10:e0133208.                                                    occupation and sex [accessed 2022 Sept 1]. https://www.bls.gov/
40 Katz D, Braly K. 1933. Racial stereotypes of one hundred college         cps/cpsaat39.htm
   students. J Abnorm Soc Psychol. 28:280–290.                           56 Peabody D. 1987. Selecting representative trait adjectives. J Pers
41 Caliskan A, Parth Ajay P, Charlesworth T, Wolfe R, Banaji MR.            Soc Psychol. 52:59–71.
   2022. Gender bias in word embeddings: a comprehensive ana­            57 Warriner AB, Kuperman V, Brysbaert M. 2013. Norms of valence,
   lysis of frequency, syntax, and semantics. AIES. 22:156–170.              arousal, and dominance for 13,915 English lemmas. Behav Res
42 Bailey AH, LaFrance M, Dovidio JF. 2020. Implicit androcentrism:
                                                                            Methods. 45:1191–1207.
   men are human, women are gendered. J Exp Soc Psychol. 89:
                                                                         58 Delobelle P, Tokpo EK, Calders T, Berendt B. 2022. Measuring fair­
   103980.
                                                                             ness with biased rulers: a comparative study on bias metrics for
43 McDermott M, Samson FL. 2005. White racial and ethnic identity
                                                                             pre-trained language models. In: NAACL 2022—Proceedings of
   in the United States. Annu Rev Sociol. 31:245–261.
                                                                             the 2022 Conference of the North American Chapter of the
44 Miller EJ, et al. 2023. AI hyperrealism: why AI faces are perceived
                                                                             Association for Computational Linguistics: Human Language
   as more real than human ones. Psychol Sci. 34(12):1390–1403.
45 Buolamwini J. 2018. Gender shades: intersectional accuracy dis­           Technologies; Seattle (WA). p. 1693–1706. https://doi.org/10.
   parities in commercial gender classification. Proc Mach Learn Res.       18653/v1/2022.naacl-main.122
   81:1–15.                                                              59 Vulić I, et al. 2020. Multi-simlex: a large-scale evaluation of multi­
46 Lalor JP, Yang Y, Smith K, Forsgren N, Abbasi A. 2022.                    lingual and crosslingual lexical semantic similarity. Comput
   Benchmarking intersectional biases in NLP. Proceedings of the            Linguist. 46:847–897.
   2022 Conference of the North American Chapter of the                  60 Lauscher A, Lüken T, Glavaš G. 2021. Sustainable modular de­
   Association for Computational Linguistics: Human Language                 biasing of language models. In: Findings of the Association for
   Technologies; Seattle (WA). p. 3598–3609.                                 Computational Linguistics: EMNLP 2021. p. 4782–4797.
