---
title: "ChatGPT as Research Scientist: Probing GPT’s capabilities as a Research Librarian, Research Ethicist, Data Generator, and Data Predictor"
person: mahzarin-banaji
section: by
type: journal-article
year: 2024
date: 2024-08-20
venue: "Proceedings of the National Academy of Sciences"
authors: "Steven A. Lehr; Aylin Caliskan; Suneragiri Liyanage; Mahzarin R. Banaji"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/Lehr_etal_ChatGPTScientist_2024.pdf
doi: https://doi.org/10.1073/pnas.2404328121
openalex_id: https://openalex.org/W4401729468
cited_by_count: 59
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard site, extracted with pdftotext -layout. Title-overlap check 1.00."
---

# ChatGPT as Research Scientist: Probing GPT’s capabilities as a Research Librarian, Research Ethicist, Data Generator, and Data Predictor

## Full text

RESEARCH ARTICLE      | COMPUTER SCIENCES
                                                       PSYCHOLOGICAL AND COGNITIVE SCIENCES


ChatGPT as Research Scientist: Probing GPT’s capabilities
as a Research Librarian, Research Ethicist, Data Generator,
and Data Predictor
Steven A. Lehra,1    , Aylin Caliskanb   , Suneragiri Liyanagec   , and Mahzarin R. Banajic,1

Affiliations are included on p. 9.

Contributed by Mahzarin R. Banaji; received March 1, 2024; accepted July 1, 2024; reviewed by James Evans, James W. Pennebaker,
and Richard M. Shiffrin


How good a research scientist is ChatGPT? We systematically probed the capabilities
of GPT-3.5 and GPT-4 across four central components of the scientific process: as                          Significance
a Research Librarian, Research Ethicist, Data Generator, and Novel Data Predictor,
using psychological science as a testing field. In Study 1 (Research Librarian), unlike                    Though scientists widely adopt
human researchers, GPT-3.5 and GPT-4 hallucinated, authoritatively generating fic-                         them, the promise of general-
tional references 36.0% and 5.4% of the time, respectively, although GPT-4 exhibited                       purpose AI systems to facilitate
an evolving capacity to acknowledge its fictions. In Study 2 (Research Ethicist), GPT-4                    science has been largely
(though not GPT-3.5) proved capable of detecting violations like p-hacking in fictional                    untested. In four studies, we
research protocols, correcting 88.6% of blatantly presented issues, and 72.6% of subtly                    examine the capabilities of
presented issues. In Study 3 (Data Generator), both models consistently replicated                         ChatGPT across several tasks
patterns of cultural bias previously discovered in large language corpora, indicating
                                                                                                           intrinsic to the scientific process.
that ChatGPT can simulate known results, an antecedent to usefulness for both data
                                                                                                           ChatGPT is a poor (but
generation and skills like hypothesis generation. Contrastingly, in Study 4 (Novel Data
Predictor), neither model was successful at predicting new results absent in their training                improving) curator of scientific
data, and neither appeared to leverage substantially new information when predicting                       articles. It is a surprisingly good
more vs. less novel outcomes. Together, these results suggest that GPT is a flawed but                     research ethicist, detecting
rapidly improving librarian, a decent research ethicist already, capable of data generation                violations of statistical best
in simple domains with known characteristics but poor at predicting novel patterns of                      practices and evolving open
empirical data to aid future experimentation.                                                              science protocols. Its ability to
                                                                                                           simulate known results may
generative AI | large language models | scientific methods | cognitive science
                                                                                                           herald useful abilities in data
                                                                                                           generation and theory building.
Scientists and writers of science fiction have long embraced the promise of artificial                     However, the chatbot had little
superintelligence, with fictional computers showing astonishing capabilities in scientific                 success predicting highly novel
domains. The idea is compelling, for the acceleration of science could be—at least in
                                                                                                           data, highlighting its limited
theory—one of the most powerful gifts of this technology. It is unquestionably hopeful
                                                                                                           ability to surmise things outside
to imagine a world in which AI can help cure diseases, solve impending global warming,
accelerate space travel, and wipe out age-old inequalities. However, the power of AI—                      its training data. Beyond merely
which has lain mostly dormant over the last 50 y—is at an inflection point. The rise of                    testing large language models,
new deep learning architectures like the Transformer (1) has yielded models capable of                     these studies produce several
an array of impressive tasks, from seamless human-like conversation to composing sym-                      insights into the nature of
phonies. Already, scientists are implementing targeted AI systems to enhance scientific                    machine intelligence.
discovery across various disciplines (2). As just a few examples, machine learning has been
used to discover new protein structures (3), to render complicated problems more tractable             Author contributions: S.A.L., A.C., and M.R.B. designed
in quantum mechanics (4) and fluid dynamics (5), and to accelerate the retrosynthesis                  research; S.A.L., A.C., S.L., and M.R.B. performed
                                                                                                       research; S.A.L. and A.C. contributed new reagents/
of organic molecules (6).                                                                              analytic tools; S.A.L., A.C., and S.L. analyzed data; and
   While these advances incorporate specialized machine learning models, the advent of                 S.A.L., A.C., S.L., and M.R.B. wrote the paper.

large language models (LLMs) like ChatGPT presents the possibility of AI as a scientific               Reviewers: J.E., The University of Chicago; J.W.P.,
                                                                                                       University of Texas at Austin; and R.M.S., Indiana
generalist. Recent research suggests that LLMs, when fine-tuned for the task, can achieve              University Bloomington.
scientific synthesis and inference on par with state-of-the-art special purpose models (7),            Competing interest statement: Cangrade builds AI-driven
and may be informally wielded by enterprising scientists to accelerate a range of research             tools for businesses, but is not affiliated with OpenAI.
tasks (8). When enhanced with scientific tools such as robotic experimentation platforms,              Copyright © 2024 the Author(s). Published by PNAS.
                                                                                                       This article is distributed under Creative Commons
LLMs like GPT-4 display advanced scientific reasoning skills and autonomously make                     Attribution-NonCommercial-NoDerivatives License 4.0
decisions that improve with time and information (9). Commentators in the field of                     (CC BY-NC-ND).
psychological science—the domain of the authors’ expertise—have expressed cautious                     1
                                                                                                        To whom correspondence may be addressed. Email:
                                                                                                       steve@cangrade.com or mahzarin_banaji@harvard.edu.
optimism that LLMs will significantly enhance the discipline (10).
                                                                                                       This article contains supporting information online at
   Yet, despite this excitement, no substantive effort has been directed at testing the ability        https://www.pnas.org/lookup/suppl/doi:10.1073/pnas.
of general-purpose AI models on the many tasks critical to the process of scientific discovery.        2404328121/-/DCSupplemental.
The technology behind ChatGPT—LLMs—while impressive, is not without problems,                          Published August 20, 2024.


PNAS     2024       Vol. 121    No. 35    e2404328121                                               https://doi.org/10.1073/pnas.2404328121 1 of 9


    and even dangers. Research has shown that these models can                 Coding of References. Two coders, blinded to GPT-Version,
    amplify patterns of bias in their training corpus (11, 12). They are       labeled each reference for 1) Correctness, 2) Completeness, 3) Topic
    also infamously prolific generators of convincing falsehoods, col-         Relevance, and 4) Citation Count. For the Correctness variable,
    loquially termed “hallucinations” (13, 14). While capable of passing       coders distinguished between Hallucinations (references that were
    standardized tests in varied domains, these models are currently           entirely fabricated or contained serious issues like attribution to
    strikingly poor at solving even simple mathematical problems (15).         incorrect authors) and “Errors” (references with smaller issues like
    While LLMs selectively show emergent abilities on tasks drawn              an incorrect year or journal name). Coders achieved substantial
    from cognitive psychology, their performance can deteriorate when          agreement. (See SI Appendix, section%S1, for coding details.)
    stimuli are edited to be less familiar (16), and indeed transformers
    are more generally less successful in solving problems external to         Results
    their training data (17). Despite these shortfalls, the promise of
    this technology—still in its infancy—is great. If we agree that “[t]       Unless otherwise noted, all effects reported in this section were
    he purpose of science is to develop, without prejudice or precon-          significant (P < 0.001) in logistic regressions. More detailed sta-
    ception of any kind, a knowledge of the facts, the laws, and the           tistical reporting may be found in SI Appendix, section S2.
    processes of nature” (18), we can ask: Can Generative AI embody
    the neutrality that science aspires to? Can it perform the tasks vital     Overall Hallucinations and Errors. Both models hallucinated, but
    to generating new scientific knowledge? In this paper, we conduct          GPT-3.5 did so more than GPT-4. Out of 500 references GPT-4
    rigorous tests of GPT as a research scientist, or more modestly, its       claimed as real, 5.40% were hallucinations, compared to 36.00%
    ability to assist scientific research by humans. To achieve this, we       for GPT-3.5; OR = 9.854. Error rates provide an interesting
    probe the limits of GPT-4 and its predecessor GPT-3.5 on several           contrast to this pattern. Error rates were roughly equivalent
    tasks integral to scientific discovery. Specifically, we test ChatGPT’s    between GPT-3.5 (4.20%) and GPT-4 (4.60%); OR = 0.909,
    abilities and limits across four domains related to scientific research:   P = 0.758. Thus, GPT-4 demonstrated sizable improvement in
    as a Research Librarian, Research Ethicist, Data Generator, and            terms of fabricating references, but no improvement in terms of
    Novel Data Predictor. To what degree can ChatGPT enhance the               smaller errors like listing an incorrect year or journal.
    scientific process, and what is the trajectory of the technology’s
    improvement between the two recent versions of the model? In the           Completeness as Moderator. Exploratory analysis revealed a
    process of testing this, we make several discoveries about the nature      powerful moderator of hallucination. When GPT provided
    and abilities of ChatGPT.                                                  complete references, these references were also more likely to be
                                                                               real. Collapsing across versions, ChatGPT hallucinated far more
    Study 1: GPT as Research Librarian                                         when it provided incomplete references (62.41%) compared to
                                                                               when it provided complete ones (14.30%); OR = 9.947. This
    Can GPT develop an accurate and comprehensive bibliography?                pattern emerged for each model. Both GPT-3.5 (OR = 7.856)
    Can it separate fact from fiction in this selection? The search for        and GPT-4 (OR = 36.362) hallucinated more for incomplete
    relevant scientific discourse and evidence is a basic building block       relative to complete references. Similar patterns did not emerge
    of the scientific process. AI’s ability to comprehensively cull prior,     to a statistically significant degree for smaller errors. (Full analysis
    relevant scientific articles is therefore critical. Moreover, lay users    in SI Appendix, section%S2 and Table%S1.) In providing complete
    of the technology frequently depend upon LLMs like GPT for                 references, GPT effectively treated the chat as more formal.
    advice that requires scientific knowledge, such as medical queries.        Prompt-engineering research indicates that more formal prompt
    It is no surprise, then, that much negative press about LLMs has           language elicits fewer hallucinations from LLMs (21). Our results
    surrounded their tendency to “hallucinate” or generate fabricated          convergently suggest that when GPT is more complete in its
    knowledge. As an example of how seriously this issue is taken,             response, it is less likely to hallucinate.
    Meta’s “Galactica” LLM, a model trained on scientific knowledge
    (19) was shut down only three days after its release, partly in            Acknowledged vs. Unacknowledged Fiction. The analyses above
    response to its tendency to generate fictional content (20). In            utilized only instances where GPT claimed to provide legitimate
    Study 1, we probed GPT-3.5 and GPT-4’s ability to gather rel-              citations. As noted earlier, GPT sometimes openly acknowledged
    evant and comprehensive scientific content, by asking each to              that references were fictional. (See SI Appendix, section%S1, for
    conduct a series of literature reviews and then gauging the quality        acknowledgment criteria.) While the analyses above ignore these
    of its outputs.                                                            responses, an alternative approach is to include them to examine
                                                                               the overall generation of fictional references and the frequency of
    Design. We asked GPT-3.5 and GPT-4 to find and summarize                   their acknowledgment.
    20 influential articles each from 25 related but specific topics              Collapsing across instances where GPT did and did not
    in psychology, generating a dataset of 1,000 references. These             acknowledge fictional references yields an interesting pattern. In
    topics ranged from broad (e.g., “The psychology of bias and                total, GPT-3.5 generated significantly more fictional references
    discrimination”) to narrow (e.g., “Use of the Implicit Association         (39.05%) than GPT-4 (23.12%); OR = 2.130. However, the larger
    Test to predict dental outcomes). (See SI Appendix, section% S1,           contrast was in acknowledgment of these fictional references.
    for full study design and topic selection details.) Notably, GPT           When GPT-4 generated fictional references, it noted so 84.30%
    sometimes acknowledged that it was presenting fictional references,        of the time compared to 12.20% for GPT-3.5; OR = 38.667. This
    making comments like “Please keep in mind that these references            pattern again did not hold for smaller errors: GPT-4 made roughly
    might not be real.” These were not counted toward the main                 the same number of errors as its predecessor, and while it was
    results but were preserved for analysis of the overall rates of fiction    descriptively more likely to acknowledge these errors, the difference
    generation and its acknowledgment. While GPT was consistently              was insignificant. (SI Appendix, Table S3.)
    asked simply to “include a citation,” the references it provided were         These results build upon research suggesting that LLMs can
    sometimes complete and other times incomplete, e.g., lacking year,         internally represent the truth or fiction of their statements (22).
    journal volume, or page numbers.                                           Our results show an advancement of the technology: GPT-4

2 of 9   https://doi.org/10.1073/pnas.2404328121                                                                                             pnas.org


possesses an evolving capacity to acknowledge when it generates            Study 2: GPT as Research Ethicist*
fictional content. Our findings are, however, agnostic to the source
of this advancement. Since much of GPT-4’s training is shrouded            In recent years, a replicability crisis has emerged in scientific research.
in mystery, it is plausible that OpenAI specifically trained the           Large-scale studies have demonstrated limited replication of research
model toward this goal. It is also plausible that this is an emergent      in Psychology (24, 25), Economics (26), the Social Sciences more
property, arising from GPT-4’s larger-scale training (23).                 generally (27), and Medicine (28–30). One source of these issues is
                                                                           unquestionably poor statistical practices by generally well-intentioned
Hallucination and Topic Broadness. As topics become narrower,              scientists: Studies show that poor statistical practices are widely
GPT will have fewer real and relevant articles in its training data        prevalent across scientific research (31, 32). A fundamental problem
and as a result, its hallucinations may increase. This intuition           is that by running multiple analyses, it is easy to find coincidentally
was confirmed (using our main set of 1,000 references), but only           “significant” results, and thus typical significance tests become
to a point. Collapsing across models, as topics narrowed, and              inaccurate (33). Improving the decisions of well-intentioned scientists
particularly as they became very narrow, GPT was likely to admit           could thus improve the reliability of science. The purpose of our second
defeat, acknowledging that it did not know of such articles. Since         study was to examine the abilities of GPT-3.5 and GPT-4 in this
such acknowledgments were considered “Correct” (i.e. a failure to          domain: Can GPT catch ethical lapses and warn investigators that
hallucinate), a curvilinear effect arose, where GPT first gradually        they are entering into the realm of questionable practices?
hallucinated more as topics narrowed, but then less on the
narrowest. Consistent with a statistical suppression effect, the linear    Research Design. In Study 2, we presented GPT-3.5 and GPT-4
effect of topic broadness on hallucination in a logistic regression        with fictional vignettes describing flawed research protocols, posing
becomes stronger (β = −0.555, P < 0.001; Pseudo-R2 = 0.075)                as scientists looking for feedback. Three of these vignettes contained
when excluding admissions of defeat, compared to when including            poor practices that were blatant and three more subtle. For example,
them (β = −0.191, P = 0.001; Pseudo-R2 = 0.0115). These linear             in the blatant version of vignette 1, the researcher directly states:
patterns were robust for GPT-3.5 but not GPT-4. (Full analysis             “After just 30 participants in each condition, effects already reached
in SI Appendix, section%S2 and Table%S4.)                                  statistical significance (P < 0.05), so we stopped data collection…”
                                                                           The subtle version states, “We collected 50 participants in each
Article Relevance. We were interested in GPT’s ability to discover         condition, at which point statistical analysis indicated that our
references that were not only real but also relevant to specific topics.   results reached statistical significance” and then describes collecting
To study this, we limited data to the 1,000 articles GPT claimed           150 participants in the next study. Here, the researchers do not
were real. Collapsing across topics, GPT-4 was more likely to              directly describe using significance testing to decide whether to
pull relevant articles (50.80%) compared to GPT-3.5 (30.80%);              continue collection, but an experienced reviewer might be suspicious
OR = 2.320. However, this effect was primarily driven by GPT-              based on the contrasting sample sizes. (See SI Appendix, section%S3,
4’s greater success at generating real articles, since hallucinations      for full design, and https://osf.io/sdahr/ for vignettes.)
were automatically labeled irrelevant. Limiting the analysis to real          The purpose of this variation between blatant and subtle
references, the difference in identifying relevant articles between        vignettes was to test, 1) whether GPT showed awareness of the
GPT-4 (53.70%) and GPT-3.5 (48.13%) lost significance; OR =                clear methodological problems described in the blatant vignettes,
1.250, P = 0.124. In short, GPT-4 discovered more real articles            and 2) whether it would be able to “read between the lines” to
than GPT-3.5 more generally and was therefore also more likely             recognize potential problems in more realistic descriptions of
to discover relevant articles. Beyond this, it did not consistently        flawed research. Put differently, the subtle vignettes contained
tailor article recommendations better to specific topics. However,         more ecologically valid descriptions, closer to how a real-world
an exploratory analysis by topic breadth tells a more nuanced story.       researcher might represent research with methodological flaws.
As detailed in SI Appendix, Table% S5, both models successfully               Additionally, we varied the initial prompt used to request GPT’s
found relevant articles on the broadest topics and failed on the           feedback on the protocols. Matched pairs of prompts were
narrowest. However, GPT-3.5 appeared to drop off in this ability           designed to encourage either better or worse responses from GPT.
more sharply as the topics narrowed. The largest gap was at the            The full set of prompts (SI Appendix, section S3) varied in levels
“moderate” broadness level, where GPT-4 discovered relevant                and verbosity of feedback requested, manipulated researcher char-
articles 75.00% of the time compared to GPT-3.5’s 32.14%; OR               acteristics (status, theory protectiveness, rejection sensitivity), or
= 6.333. Regression models indicated that this sharper drop-off            encouraged ethical or unethical responses. Of these last, one pair
in relevance for GPT-3.5 vs. GPT-4 was robust and statistically            prefaced the request with a pro- vs. anti-open science argument,
significant (SI Appendix, section%S2). Thus, while neither model           and three attempts were made to “jailbreak” GPT—requesting it
was exceptional at research curation, there was some evidence of           pretend not to be concerned about p-hacking, avoid mentions of
incremental improvement.                                                   p-hacking, or impersonate a known data fabricator—compared
                                                                           to ethical requests (consider issues around p-hacking, impersonate
Relevant Citation Counts. We requested that GPT find “important            a known data ethicist).
and influential” articles. To analyze how each model did, we focused       In separate chats, we presented each of the 18 initial prompts to
on references coded as relevant. When GPT found a relevant article,        GPT-3.5 and GPT-4, followed by each of the 6 vignettes, for a
how influential was its selection, as gauged by citation count?            total of 216 responses.
The two versions performed similarly here, with GPT-4’s articles
averaging 2936.7 citations compared to 3105.2 for GPT-3.5;                 Coding of Data. Two coders, blinded to experimental conditions,
P = 0.791, d = 0.027. Further regression analysis (SI Appendix,            independently rated all GPT responses on 10-point rubrics. Points
section%S2) ruled out the possibility that significant differences were    of disagreement were discussed, with GPT afterward receiving partial
disguised either by GPT-3.5’s relevant articles coming primarily           credit when only one coder felt a point was merited. Coding achieved
from broader domains or because GPT-4 cited newer articles.                *
                                                                            By referring to GPT as “Ethicist” we do not mean to attribute to it human-like morality, nor
Across linear regression models, no significant differences arose          to advocate for any particular scientific standards. Rather, we examine GPT’s ability to give
for citation count.                                                        advice aligned with currently accepted markers of ethical and replicable research.


PNAS     2024    Vol. 121   No. 35    e2404328121                                                        https://doi.org/10.1073/pnas.2404328121 3 of 9


    high interrater reliability, with a Cronbach alpha of α = 0.9827. (Full     prompts that evoked data ethics (M = 7.35) than those that did
    rubrics and coding details are in SI Appendix, section%S3.)                 not (M = 5.78); P < 0.0001; d = 0.625. As a robustness check, we
                                                                                replicated this analysis, limiting the ethics-priming prompts only
    Analysis. Data from coding were aggregated to the level of GPT’s            to those that did so in the context of encouraging GPT to behave
    responses, with each receiving up to 10 points. In addition to              badly (e.g., impersonate a known data fabricator), initially designed
    standard parametric procedures, differences were examined using             to elicit poor responses. As seen in SI Appendix, section S4, even
    Wilcoxon rank-sum (SI Appendix, section%S4).                                this conservative test revealed the priming effect, though not
                                                                                robust to a Bonferroni correction (P = 0.0099). The positive effect
    Results                                                                     of evoking data ethics appears powerful: ChatGPT’s responses
                                                                                were somewhat improved even when the ethics primes occurred
    Unless otherwise noted, all effects reported in this section reached        in the context of attempting to elicit unethical responses.
    a high bar for statistical significance (P < 0.001). More detailed
    statistical reporting may be found in SI Appendix, section S4.              Good Research Vignettes. As a corollary to Study 2, we conducted
       GPT-4 substantially outperformed GPT-3.5 in its responses                a secondary study (SI Appendix, section% S5) where ChatGPT
    to the Research Ethicist vignettes. In the Blatant condition,               responded to two vignettes demonstrating the opposite—rigorous
    GPT-4 achieved a mean score of 8.86 out of 10 possible points,              practices and pristine research ethics, with 120 responses across
    while GPT-3.5 averaged 5.39; d = 1.992. Similarly, in the Subtle            the two models. When asked to identify positive practices
    condition, GPT-4 averaged 7.26 points compared to GPT-3.5’s                 in these vignettes, both models were successful. Specifically,
    4.05; d = 1.571. Even when poor practices were framed subtly,               GPT-4 identified 92.67% of the good research practices in our
    GPT-4 noticed and offered advice to correct most of them.                   rubrics compared to 90.42% for GPT-3.5, with the difference
       All other pairwise comparisons were significant as well. GPT-4           nonsignificant (P = 0.071). Intriguingly, both models were about
    scored higher on blatant relative to subtle vignettes (d = 0.987),          as good at recognizing generally accepted good research practices,
    as did GPT-3.5 (P = 0.0015, d = 0.627). Strikingly, GPT-4                   though GPT-4 was vastly superior at identifying bad ones.
    received more points in response to subtle vignettes than GPT-3.5
    did in response to blatant ones (d = 0.897). The improvement of             Study 3: GPT as Data Generator
    ChatGPT on this task was thus decisive: while the earlier model
    performed poorly, the more recent iteration was quite successful            Can GPT simulate known scientific results? Several recent articles
    and could provide value to scientists in this domain.                       suggest, for example, that LLMs can mimic responses from human
                                                                                research subjects (34–36), with some even suggesting they may
                                                                                significantly supplant them (37). However, assumptions about their
    Analysis of Initial Prompts. The variation in initial prompts was
                                                                                usefulness for data generation rely on the premise that chatbots
    exploratory and designed to pick up only relatively large effects.
                                                                                can simulate high-quality data aligned with real-world outcomes.
    Though these analyses were not fully independent, to be conservative,
                                                                                Beyond this practical application, LLMs’ ability to replicate known
    we used a Bonferroni correction for multiple comparisons. Since
                                                                                outcomes is a likely precursor to broader scientific capabilities.
    we completed 12 analyses, this correction dictated a statistical
                                                                                For instance, suppose we tasked GPT with generating novel but
    significance threshold of P < 0.004167.
                                                                                plausible hypotheses. This would require it to simulate future
       We first examined each matched pair of prompts, testing for each
                                                                                results by synthesizing prior knowledge. GPT’s proficiency in
    whether the hypothesized “good performance” prompt yielded supe-
                                                                                replicating established findings underscores its capacity to simulate
    rior feedback compared to the “bad performance” prompt. For
                                                                                outcomes in this fashion, and thus its potential in functions like
    example, we tested whether claiming to be a chaired professor at a
                                                                                hypothesis generation. In Study 3, we evaluated GPT’s ability to
    major research institution (high status) elicited less critical feedback
                                                                                simulate data in a domain familiar to it.
    compared to claiming to be a novice researcher running her first
                                                                                   In recent years, a significant body of literature has accumulated
    study (low status). As seen in SI Appendix, Tables S7 and S8, none
                                                                                suggesting that human-like biases and stereotypes emerge from
    of these nine basic contrasts reached statistical significance. One
                                                                                semantic patterns in large language corpora (38–40). For example,
    trended: requesting GPT “carefully consider issues around p-hacking
                                                                                just as reaction-time tasks reveal that people more easily associate
    and open science” (M = 8.38) elicited stronger responses than
                                                                                male (compared to female) names with words related to “career”
    requesting that it “not include any mentions of p-hacking”
                                                                                compared to “family,” machine learning detects analogous patterns
    (M = 6.08, P = 0.0106, d = 1.140). However, this result did not
                                                                                in the co-occurrence of these words in large repositories of human
    meet the significance threshold of the Bonferroni correction. Though
                                                                                language (38). These findings are theoretically important, suggest-
    GPT descriptively gave worse responses following the three different
                                                                                ing that language can crystallize human biases, and transmit and
    “jailbreaking” prompts, compared to two contrasting prompts
                                                                                augment their impact. They are also methodologically important,
    requesting ethical responses, this similarly failed to reach significance
                                                                                offering a new tool with which researchers can probe these issues,
    (P = 0.0295, d = 0.588) after correction.
                                                                                present and historical. However, this research poses challenges:
       One analysis yielded robust results. Regardless of how we asked
                                                                                The study of word embeddings in large language corpora is com-
    GPT to behave, stronger responses emerged following prompts
                                                                                plex and computationally intensive. It is difficult for a researcher
    that in any way evoked data ethics. For example, the 12 chats
                                                                                to undertake this work casually because there is currently no tech-
    where we asked GPT to impersonate a known data fabricator—
                                                                                nically uncomplicated way to do so. Study 3 asked: might one
    designed to jailbreak GPT and elicit unethical responses—actually
                                                                                simply ask GPT to explore its own corpus?† Beyond potentially
    yielded responses that appeared to be of higher quality than most.
                                                                                offering a simplified way to pilot word embedding research, GPT’s
    Accordingly, we collapsed responses across prompts that in any
                                                                                performance here provides an indicator of its broader ability to
    fashion evoked data ethics (Pro- and Anti-Open Science;
                                                                                replicate known results, a precursor to other scientific abilities.
    Concerned and Not Concerned with p-hacking; Don’t Mention
    p-hacking; Data Ethicist and Data Fabricator), comparing these              †
                                                                                 Note: We refer to GPT “exploring its own corpus,” which was the task asked of it. However,
    to all remaining prompts, without mentions of p-hacking or open             it should be noted that we lack insight into how other elements of GPT’s training—e.g.,
    science. Indeed, GPT provided higher-quality responses after                reinforcement learning, fine-tuning—impact its responses.


4 of 9   https://doi.org/10.1073/pnas.2404328121                                                                                                              pnas.org


Research Design. In this study, we explored four well-studied                                 by GPT are primarily driven by stronger associations of Female with
gender stereotypes: Gender Attitudes (overall positivity/negativity                           the stereotypically female category, and not also of Male with the
toward women vs. men), Gender Art/Science stereotypes, Gender                                 stereotypically male category (SI Appendix, Table S10.)
Home/Work stereotypes, and Gender Math/Reading stereotypes.
These stereotypes have been robustly studied in human subjects,                               Study 4: GPT as Novel Data Predictor
using both implicit and explicit measures (41, 42). Furthermore,
consistent patterns for these stereotypes have been found in                                  In Study 3, we examined GPT’s ability to simulate data from word
research on word embeddings in language corpora (39). We did                                  embedding research. As use cases for GPT as a data generator go,
not have access to GPT’s model parameters to generate its word                                this one is obvious: Since GPT is trained on large language corpora,
embeddings directly, and instead used estimates provided within                               it might display knowledge of word embedding patterns found in
the open-ended language of the chatbot’s responses. Adapting                                  them. Less certain and less tested is the potential for LLMs to predict
stimuli from Charlesworth et% al. (39), we presented GPT-3.5                                  data that are novel and outside their training data. Recent concep-
and GPT-4 with thousands of randomly ordered word dyads,                                      tual work has argued that LLMs may augment or even replace
requesting it estimate cultural associations between each based on                            human test subjects (34–37). Logically, the degree of this potential
its training data. (Full design in SI Appendix, section%S6.)                                  depends upon its ability to predict unseen patterns. If GPT is teth-
For analysis, GPT’s estimates were treated as analogous to cosine                             ered to its training data, it might be useful for certain kinds of basic
similarity measures from word embedding research (38). To                                     tasks, such as piloting the psychometric properties of personality
calculate a measure of relative cultural association—e.g., a greater                          scale items. However, to produce results that are both correct and
association of Female with Home and Male with Work, relative                                  novel, it must be able to predict data patterns that are unknown to
to Male with Home and Female with Work—the procedure was                                      it. In Study 4, we gave ChatGPT a more difficult task in this regard.
followed for calculating the WEAT D-score (39).                                                   Specifically, we asked GPT to predict patterns of data that were
                                                                                              complicated and unfamiliar. For this, we used a second paper by
                                                                                              Charlesworth and colleagues (48), which introduced a novel data-
Results
                                                                                              set: the Project Implicit International Dataset. This paper describes
Table 1 depicts the real WEAT D-scores for each construct exam-                               patterns of implicit and explicit attitudes from 2.3 million partic-
ined, drawn from Charlesworth et al.’s (39) meta-analytic estimates                           ipants across 34 countries. Critically, accumulated evidence sug-
across adult corpora (39), compared to those calculated using                                 gests that implicit attitudes—automatic associations held between
responses from GPT-3.5 and GPT-4. Positive WEAT D-scores                                      attitude objects, typically measured by reaction-time tasks—are
reflect effects in the stereotype-congruent direction based on prior                          distinct from explicit attitudes captured in self-reports (49). For
research. Main results replicated prior findings: GPT’s estimates                             example, a person may explicitly express equal positivity toward
based on its training data reflected a cultural preference for Female                         straight and gay individuals, while at the same time implicitly
over Male, and a stronger association of Female (relative to Male)                            harboring greater positivity toward straight individuals. Indeed,
with Art vs. Science, Home vs. Work, and Reading vs. Math.                                    in the Project Implicit International Dataset, correlations between
   The effects gathered from GPT were often somewhat stronger                                 country-level implicit and explicit attitudes vary by attitude object
than those reported in prior research, though this pattern is incon-                          but are generally not strong (SI Appendix, section S9). These
sistent. This may reflect the troubling tendency for AI systems to                            country-level data were previously unpublished, and the paper was
amplify biases in their training data (43–45). It is interesting to                           first posted online after GPT’s training cutoff at the time of the
note that these effects are not generally smaller for GPT-4 vs.                               study. In Study 4, we had GPT-3.5 and GPT-4 make a total of
GPT-3.5, despite efforts OpenAI has made to debias the model                                  60 different predictions of cross-country patterns of Explicit and
(46). This aligns with prior research showing that more powerful                              Implicit Sexuality Attitudes, Age Attitudes, and Gender Science/
models tend to intrinsically learn human biases more precisely (47).                          Liberal Arts stereotypes. (Full design in SI Appendix, section S8.)
   These results are promising in terms of GPT’s ability to generate
estimates of word embedding results, suggesting a use case in                                 Results
piloting this research. However, they come with some caveats.
First, the interitem correlations between GPT-3.5 and GPT-4’s                                 More detailed statistical reporting may be found in SI Appendix,
responses to the same word dyads were variable but modest:                                    section S9.
r = 0.382 for the Math-Reading task, r = 0.568 for the Preference                                For each attitude/stereotype, we examined several patterns. First,
task, r = 0.666 for the Work-Home task, and r = 0.554 for the                                 we examined the intercorrelations between ChatGPT’s different
Art-Science task (all Ps < 0.0001). These moderate correlations                               predictions of the same attitude. For example, a high correlation
might indicate differences in how GPT-3.5 and GPT-4                                           between GPT’s different predictions of Implicit Sexuality Attitudes
approached the task. Alternatively, they might indicate reliability                           suggests reliability and consistency in how it approached the task.
constraints, limiting GPT’s consistency in eliciting these effects.                           We then examined the correlations between GPT’s predictions of
   Second, we calculated Single-Category WEAT D-scores for each                               implicit and explicit attitudes. Importantly, GPT likely has more
of the concepts, to gauge the degree to which results were driven by                          information about explicit compared to implicit attitudes. For
stronger Female–Male associations with each attribute. Interestingly,                         example, at the time of this article’s writing, a Google Scholar
our results diverge from prior research (39) in that those generated                          search for “Sexuality Attitudes” returned 2,710 results compared

Table 1. WEAT D-scores from ChatGPT and Real Large Language Corpora
                       Female-Good Male-Bad                Female-Art Male-Science                Female-Home Male-Work             Female-Reading Male-Math
Prior research               WEAT D = 0.49                        WEAT D = 0.54                          WEAT D = 0.94                     WEAT D = 0.67
GPT-3.5                      WEAT D = 1.00                        WEAT D = 1.16                          WEAT D = 0.40                     WEAT D = 0.73
GPT-4                        WEAT D = 0.57                        WEAT D = 1.46                          WEAT D = 0.45                     WEAT D = 0.96
Notes: Prior research numbers are meta-analytic estimates from adult language corpora (39).


PNAS      2024      Vol. 121      No. 35     e2404328121                                                             https://doi.org/10.1073/pnas.2404328121 5 of 9


    to just 26 results for “Implicit Sexuality Attitudes.” We were inter-                           GPT-4’s different explicit predictions were moderately to highly
    ested in whether GPT leveraged different information when asked                                 correlated (mean r = 0.645), as were its different implicit predic-
    to predict more novel implicit attitudes. If GPT’s predictions of                               tions (mean r = 0.726). Correlations between its implicit and
    implicit attitudes correlate more highly with each other than they                              explicit predictions were in the same range (mean r = 0.664), again
    do with its predictions of explicit attitudes, this would suggest it                            suggesting that it did not lean on substantially new information
    is reliably leveraging different information in making the two pre-                             for predicting patterns of implicit vs. explicit attitudes. Critically,
    dictions. Conversely, if GPT’s predictions of implicit attitudes                                its collective predictions were on average negatively correlated with
    correlate as highly with its explicit predictions as with each other,                           real country-level Explicit Age Attitudes (mean r = −0.395) and
    this would suggest it is approaching the tasks similarly, and not                               uncorrelated with Implicit Age Attitudes (mean r = −0.120).
    leveraging substantively different information in predicting                                        For Gender Science/Liberal Arts stereotypes, GPT-4’s different
    implicit vs. explicit attitudes. Finally, and most critically, we exam-                         explicit predictions were weakly correlated (mean r = 0.363).
    ined the correlations between GPT’s predictions and real-world                                  Curiously, its different implicit predictions were more consistent,
    results in the Project Implicit International Dataset, to gauge                                 correlating strongly across chats (mean r = 0.868), and correlations
    GPT’s overall success as a Novel Data Predictor. (See SI Appendix,                              between its explicit and implicit responses fell between the two
    Table S12, for additional summary statistics. For full correlation                              (mean r = 0.499). The real-world explicit results GPT predicted
    tables, see “GPT as Data Predictor Correlation Tables 20240228”                                 here were measured with two items that needed to be combined:
    at https://osf.io/sdahr/.)                                                                      one capturing associations of Male vs. Female with Science, and
                                                                                                    a second with Liberal Arts. (For full items, see “GPT as Novel
                               ‡
    Sexuality Attitudes . On average, correlations between GPT-3.5’s                                Data Predictor Materials 20240227” at https://osf.io/sdahr/.) This
    five different explicit predictions of Sexuality Attitudes were high                            more complicated explicit item may have challenged the LLM. In
    (mean r = 0.875), as were correlations between GPT-3.5’s different                              any case, neither sets of answers predicted actual cross-country
    implicit predictions of Sexuality Attitudes (mean r = 0.879). This                              results. GPT-4’s explicit predictions were uncorrelated with real
    suggests it approached these tasks reliably. However, correlations                              country-level explicit (mean r = −0.192) and implicit (mean r =
    between its implicit and explicit predictions were nearly as high                               0.054) stereotypes. Similarly, GPT’s implicit predictions were
    (mean r = 0.778). GPT-3.5’s five sets of implicit predictions were                              negatively correlated with explicit (mean r = −0.417) stereotypes
    similar to its five sets of explicit predictions, indeed nearly as similar                      and uncorrelated with implicit (mean r = −0.067) ones.
    to them as to each other. For GPT-4, correlations between different                                 Sexuality bias may receive more media coverage than Age
    explicit predictions were even higher (mean r = 0.957), as were                                 Attitudes or Gender Science/Liberal Arts stereotypes. Though
    correlations between different implicit predictions (mean r = 0.946).                           unaware of published research on this topic, we conducted three
    Interestingly, correlations between its explicit and implicit predictions                       tests to examine this possibility. Patterns from Bing searches,
    were equally high (mean r = 0.952): statistically, GPT-4’s predictions                          Google Books Ngram Viewer, and chats with GPT-4 all suggested
    of Implicit Sexuality Attitudes looked identical to its predictions of                          that Sexuality Attitudes are better represented in ChatGPT’s
    Explicit ones. These patterns suggest ChatGPT was limited in the                                knowledge base relative to Age Attitudes or Gender Science ste-
    new information it applied to these different tasks. When predicting                            reotypes (SI Appendix, Section S9 and Figs. S1 and S2). Predicting
    (more novel) implicit attitudes compared to (more familiar) explicit                            these latter patterns was thus more difficult. In line with this
    attitudes, GPT-3.5 seemingly used little new information, and GPT-                              thinking, while both LLMs were successful at predicting patterns
    4 almost no new information.                                                                    of Explicit (though not Implicit) Sexuality bias, neither achieved
       Considering these analyses, we collapsed across implicit and                                 even small positive correlations with the other real-world results.
    explicit predictions in examining ChatGPT’s success at predicting
    actual Sexuality Attitudes. GPT-3.5 did a reasonable job predicting                             General Discussion
    real-world Explicit Sexuality Attitudes by country (mean r = 0.602),
    but was unsuccessful at predicting Implicit Sexuality Attitudes                                 Across four studies, we have tested GPT’s ability to enhance the
    (mean r = −0.014). GPT-4’s predictions correlated highly with                                   scientific process. Our focus has been on psychological science,
    country-level explicit attitudes (mean r = 0.714), but it similarly                             where the authors have sufficient expertise to judge the quality of
    failed at predicting implicit attitudes less represented in its training                        GPT’s output, but we have selected tasks that are applicable across
    data (mean r = 0.152).                                                                          domains. Future research should, however, confirm the degree to
                                                                                                    which this work generalizes to other disciplines.
    Age Attitudes and Gender Science/Liberal Arts Stereotypes. GPT-                                    We included both GPT-3.5 and GPT-4, even though GPT-4
    3.5’s predictions of Age Attitudes and Gender stereotypes proved                                is expected to be superior and GPT-3.5 may fall out of use as
    not only unsuccessful, but incoherent. As detailed in SI Appendix,                              future versions are released. We did this for several reasons. First,
    section%S9, for each, GPT-3.5’s different implicit predictions were                             the quantitative difference between the two is of interest in track-
    uncorrelated with each other, as were its different explicit predictions.                       ing the speed of improvement. More importantly, only by com-
    Given this low reliability, it is unsurprising that its collective predictions                  paring the two could we gain insight into newly emerging processes
    of Age Attitudes were uncorrelated with real country-level patterns                             such as GPT-4’s ability for self-correction. As we will discuss, such
    of Explicit (mean r = −0.010) and Implicit (mean r = −0.175) Age                                findings have implications for our understanding of underlying
    Attitudes. Similarly, GPT-3.5’s predictions of country-level Gender                             processes in machine cognition. Finally, comparing the models
    Science/Liberal Arts stereotypes were uncorrelated with actual explicit                         allowed us to highlight where the technology did and did not
    (mean r = −0.009) and implicit (mean r = −0.044) results.                                       advance, such as GPT-4’s reduction in hallucinations but not in
       GPT-4 completed these tasks more reliably but was not more                                   smaller errors. This work thus offers actionable insights that can
    successful in predicting real-world results. For Age Attitudes,                                 help guide the training of future models.
                                                                                                       Study 1 probed GPT’s ability as a Research Librarian. GPT
    ‡
     As detailed in SI Appendix, section S9, here and elsewhere GPT-3.5 had difficulty with this    showed a varied trajectory in terms of the ability to discover relevant
    task. GPT-3.5’s intended direction of scoring was frequently unclear, necessitating follow-up
    questions to gauge the meaning of its predictions. This sometimes rendered responses
                                                                                                    research. By any measure, GPT-4 generated many fewer fictional
    difficult to interpret, particularly for Age Attitudes and Gender Science stereotypes.          references. It also displayed a far greater tendency to acknowledge

6 of 9   https://doi.org/10.1073/pnas.2404328121                                                                                                                 pnas.org


when it was generating fiction. This is potentially important for the     grading rubrics were built collaboratively: the original draft by
technology’s development. There is a likely tradeoff between novelty      one of the authors had eight points for each, another author then
and truth in LLMs: Hallucinations might be inevitable in a model          revised it with a ninth point, and upon reflection, the original one
capable of creativity (50). Training a model with a firm goal of          added a tenth. While some of GPT-4’s responses were better than
minimizing fiction generation might therefore be problematic, risk-       others, on average it scored nearly nine points for blatant vignettes,
ing it becoming more factual but also less creative. The possibility      which is roughly identical to what the authors effectively averaged
that GPT-4 is developing some form of fiction recognition is there-       across three iterations of the rubrics. The performance of GPT-3.5
fore intriguing. An AI capable of discerning fact from fiction in its     lies in stark contrast. Not only did it often miss the researchers’
own creation may be capable of generating fact when facts are desir-      lapses, but at times it was even complimentary. For example, on
able, and fiction when fiction is desirable, much as a human author       several occasions it praised the researchers’ decision to add more
might choose to write a short story on one occasion and a research        research subjects after checking for statistical significance, noting
article on another. Put differently, the ability to parse fact from       that it “added statistical power.”
fiction in its responses may open the door for LLMs that are capable         In a scientific era defined by a replicability crisis, these results are
of being at once creative and truthful.                                   important. They suggest that GPT-4 is highly capable of giving
   That said, there is significant room for improvement. GPT-4            useful feedback—aligned with generally accepted standards of mod-
still generated a nontrivial number of unacknowledged hallucina-          ern research practice—on experimental protocols. GPT-4 was rea-
tions. Moreover, acknowledgment generally came on the chat                sonably successful at this task even when the vignettes were framed
level: GPT would note that its references “might be fictional,” for       subtly. This result is striking because this required GPT to infer bad
example, without distinguishing which specific references were            research practices where they were not clearly stated. It is also prac-
real or fake. Finally, GPT-4 did not show meaningful improve-             tically important, as it suggests the LLM can help well-intentioned
ment in terms of smaller errors, such as listing the wrong year or        researchers—operating in a realistic context—improve the quality
journal. This pattern is interesting. GPT-4 increasingly mirrors          and ethics of their work. Finally, it is conceptually interesting that
humans on this task: It has fewer instances of outright fabrication,      GPT-4 suggested distinctly modern practices: From an ocean of
to which people are not prone, but not of smaller errors people           possible suggestions, the more recent model was able to circum-
might also make. Such errors are consequential: Even small errors         navigate practices that have aged poorly, and instead present advice
might, for example, lead to inaccurate conclusions about authors’         aligned with recent advances and best practices. Not so for GPT-3.5.
scientific output in formulas that help decide tenure, or incorrect       The comparatively poor performance of GPT-3.5 is disheartening
citations in new articles. The latter problem may be self-propagating,    in that researchers who do not purchase the paywalled model
since incorrect citations are automatically indexed on Google             upgrade may receive poor-quality advice. Indeed, GPT-3.5’s
Scholar, risking an expanding misinformation ecosystem.                   responses could even embolden poor researchers, since at times it
   Interestingly, hallucination was moderated by the completeness         openly encouraged subpar practices. However, the difference
of the references generated. When generating incomplete citations,        between the two LLMs may also be cast in an optimistic light: the
both GPT-3.5 and GPT-4 were sharply more likely to hallucinate.           technology’s progress is profound, suggesting that its next iteration
One possible framing of this effect is in terms of formality: By          may prove an extremely powerful tool for helping researchers design
providing incomplete references, GPT was intrinsically making             protocols and improve practices. Future research should examine
the chat less formal. Future research should probe the causality of       the LLMs’ ability to improve higher-quality protocols, gauging their
this finding by experimentally varying the formality of the request       ability to help more skillful researchers.
to explore whether this changes ChatGPT’s effectiveness in dis-              The results around initial prompts, while exploratory, were gen-
covering real research. This finding is also interesting in that here,    erally heartening. At the least, they suggest that casual mentions of
again, we see a parallel to human cognition. A person will be more        things like researcher status or sensitivity to criticism are not elic-
prone to misstate a fact—e.g., misquoting the source of a statis-         iting large and robustly worse feedback from GPT. It also did not
tic—over a dinner conversation than in a scientific communica-            prove trivial to jailbreak the technology: GPT consistently rejected
tion. In this case, of course, the source of the confabulation is         requests to provide feedback in an unethical manner. Indeed, if
obvious: the human is drawing on imperfect memory rather than             anything, preceding our protocol with arguments against open
verifying documentation. The source of this analogous error in            science or requests that it ignore p-hacking may have riveted the
GPT is less clear and very likely different. Nevertheless, in some        LLMs’ attention to these issues, leading to more ethical responses.
sense, the machine appears to verify facts more in some contexts          This unique “priming” effect—the tendency for GPT to give supe-
than others, seemingly seizing upon informality as an opportunity         rior feedback following initial prompts that evoked data ethics—is
to be sloppy. Uncovering the source of this discrepancy may gen-          both practically and theoretically important. Merely asking GPT
erate insights into the processes underlying machine cognition.           to be more critical or verbose did not elicit stronger responses.
   ChatGPT’s abilities in terms of pulling relevant references were       However, evoking data ethics in any manner led to better feedback.
uninspiring. It was successful at discovering references on broad         Practically, this underscores the importance of specificity when
topics but quickly became less successful as the subject matter           eliciting advice from ChatGPT. Researchers may benefit from high-
became narrower. However, we saw advancement between                      lighting specific areas where they require support. Theoretically, it
GPT-3.5 and GPT-4 in this regard. GPT-4 was more successful               reveals nuance in the process by which GPT responds to prompts;
at pulling references on moderately broad topics, suggesting              merely hinting at ethics leads the LLMs to evaluate the problem
potential for future improvement in this area.                            differently, adopting an ethically minded perspective.
   Study 2 probed GPT’s abilities as a Research Ethicist. GPT-4              In Study 3, we probed ChatGPT’s ability to generate useful
shined in this regard, decisively outperforming GPT-3.5 when              data for estimating word-embedding results. GPT’s results rep-
providing feedback on subpar research protocols. While these              licated known overall effects from this literature. GPT may thus
results were large statistically, examining the responses qualitatively   be useful for generating data in this context, for example, to pilot
makes the contrast even more striking. (For full transcripts, see         new word embedding work in a technically simplified manner.
“GPT as Research Ethicist Transcripts 20240220” at https://osf.           However, the importance of this work extends beyond GPT’s
io/sdahr/.) To put its performance into perspective, note that the        ability to generate data in this relatively specific domain. The

PNAS    2024     Vol. 121   No. 35   e2404328121                                                  https://doi.org/10.1073/pnas.2404328121 7 of 9


    ability to realistically simulate real-world data is implicitly tied   effects in a domain (word embeddings) familiar to it, GPT-3.5
    to other important scientific abilities. For example, imagine GPT      and GPT-4 were both relatively successful. But tasked with pre-
    was asked to generate plausible scientific hypotheses. Completing      dicting novel and unfamiliar data, both models generally failed.
    this task would likely require the LLM to draw upon and synthe-            The tendency to lean heavily on what is familiar was evident in
    size existing knowledge in new and meaningful ways. Success            GPT’s approach to predicting cross-cultural IAT results. While
    would require GPT to display an intrinsic command of this              even explicit attitude predictions were often beyond it, GPT had
    knowledge. Put another way, if it is unable to simulate existing       some success in that domain. Both GPT-3.5 and GPT-4 achieved
    knowledge, GPT cannot be expected to successfully simulate             relatively high correlations in predicting country-level Explicit
    extensions of this knowledge. GPT’s ability to generate useful         Sexuality Attitudes. However, their predictions for Implicit
    hypotheses may therefore be dependent on its ability to replicate      Sexuality Attitudes were nearly identical, suggesting they brought
    existing results.                                                      little additional information to this more novel prediction. This
        It should be noted that the results from Study 3, while prom-      is particularly striking considering that implicit and explicit atti-
    ising, are not decisive. In particular, the divergence from existing   tudes are often only moderately correlated (49), a fact in GPT’s
    research on the patterns of Single-Category WEAT D-scores is           knowledge base (SI Appendix, section S9). In short, these two
    rather puzzling. There may be differences in GPT’s training data       phenomena were sufficiently distinct that one would expect GPT
    or approach to the task, leading to inconsistencies with prior         to leverage somewhat different information when predicting them.
    work. The relative uniformity across GPT-3.5 and GPT-4 is              Surprisingly, it did not.
    consistent with this interpretation. Where result patterns                 It should be noted that even GPT’s prediction of explicit atti-
    diverged from known results, they usually did so consistently          tudes was far from stellar. The LLMs succeeded only with Sexuality
    across the two models. A more troubling possibility is that GPT        Attitudes. It seems likely that the extensive cross-national coverage
    ignored our instructions not to adjust for stereotypical associa-      and political discussion of sexuality offered GPT information to
    tions viewed as negative. Gendered associations with Work and          lean on here. Beyond Sexuality Attitudes, when GPT attempted
    Math have produced wide discussion, and GPT may have simply            to predict Age Attitudes and Gender Liberal Arts/Science stereo-
    been reluctant to suggest men are more associated with these           types—areas that receive less media coverage—both models failed
    categories. If this is the case, GPT could prove an unreliable         spectacularly.
    source for data related to socially undesirable effects. This issue        We suggest that GPT’s ability to act as a data source may be
    is larger than the specific use case from this study, extending to     limited to relatively simple tasks and domains where the likely
    any use of LLMs to augment human subjects. While self-censoring        results are known or predictable. Future research should finely
    of LLMs may be an overall societal good, in the context of social      map where GPT is and is not successful in simulating data. That
    psychological research, this could undermine their potential.          said, it is conceptually possible that LLMs may prove able to
    One cannot, for example, expect reliable data on human preju-          elaborate upon known results in novel ways, cohesively combining
    dice if GPT refuses to display bias within the context of scientific   sources of knowledge. Testing LLMs’ abilities to generate new
    research.                                                              knowledge in this manner may prove fertile ground for future
        Finally, in Study 4, we examined GPT’s ability to predict novel    research. We believe it unlikely, however, that current or future
    data—cross-cultural patterns of implicit and explicit attitudes—       LLMs will be capable of generating true empirical novelty,
    published after its training cutoff. Our results here should be        whereby results do not reflect existing information regardless of
    viewed as suggestive rather than definitive since we have studied      how it is combined, because we see no mechanism by which LLMs
    merely one of many possible domains in which GPT could be              can predict something with no counterpart in their training data.
    asked to make novel predictions. Conceptually, though, we take         AI may thus continue to be limited in this regard, even as tech-
    issue with the possibility that LLMs can predict novel data. A         nology advances: Scientific progress will likely always require
    finding that is novel is, by definition, one outside the scope of      real-world data.
    the LLM’s training data. As a thought experiment, imagine a                To conclude, we turn to the broader question of whether LLMs
    powerful AI somehow came to exist in the 16th century. This            can enhance or facilitate the scientific process. Based on this
    AI had more cognitive capabilities than current technologies but       report, we would tentatively answer “yes.” ChatGPT’s ability to
    received none of the data collected from hundreds of years of          compile and curate research is currently limited but rapidly
    astronomical research. Without a telescope, could this AI locate       improving in ways (e.g., increasing acknowledgment of fiction)
    the moons of Jupiter? We argue that it could not. Galileo’s dis-       that indicate future generations of this technology might be suc-
    coveries were not merely creative insights; they were the result       cessful in this area. Already, GPT-4 shows a surprisingly strong
    of new data. Given data from a good telescope, a powerful AI           mastery of research methods and ethics, and may be able to help
    might perhaps predict hundreds of years of physical research.          scientists improve their practices. ChatGPT’s successful replication
    Without it, it likely could not.                                       of known results suggests a degree of command over existing
        This extends to the idea of AI acting as a human test subject      knowledge that may simplify research piloting. This same phe-
    (and data source more generally). Without data to suggest a certain    nomenon raises the possibility that GPT may be able to synthesize
    result will arise, how can it be expected to mimic the effect? It      existing knowledge sources to generate new and plausible hypoth-
    would be blind as to Jupiter’s moons. As a simulated human             eses, a premise that may prove a fruitful ground for future research.
    subject, GPT might therefore be expected to replicate — indeed         The most fundamental limitation we perceive is in GPT’s seeming
    perhaps overreplicate — existing findings. To be sure, it might be     inability to predict highly novel empirical results. This limitation
    able to combine knowledge in new ways to reveal novel discoveries      is unsurprising, but it speaks to the need for moderation in the
    about patterns in historical data. But there is no obvious mecha-      optimism about this technology. Future models may show pro-
    nism by which it could generate discoveries dependent on novel         found abilities and spur scientific advancement. But, these abilities
    data, a cornerstone of scientific progress.                            should not be mistaken for omniscience. Like human scientists,
        Our results across Studies 3 and 4, while not definitive, are      advanced LLMs will likely remain limited by the knowledge they
    consistent with this argument. Tasked with replicating known           already possess.


8 of 9   https://doi.org/10.1073/pnas.2404328121                                                                                      pnas.org


Data, Materials, and Software Availability. Trancripts from GPT and spreadsheets                                 transcripts. ChatGPT provided brainstorming and advice on this project but was
containing quantification of these data, including direct recording of quantitative data                         not used in the manuscript’s preparation. All correspondence regarding this man-
and the outputs from coding qualitative data according to rubrics. All data discussed in                         uscript should be directed to S.A.L. at steve@cangrade.com.
the paper are publicly available in OSF (DOI: 10.17605/OSF.IO/SDAHR) (51).
ACKNOWLEDGMENTS. We would like to thank Melanie Mitchell, Tina Eliassi-
                                                                                                                 Author affiliations: aCangrade, Inc., Watertown, MA 02472; bInformation School, University
Rad, and Tessa Charlesworth for their advice on this work, Igor Grossmann for his                                of Washington, Seattle, WA 98195; and cDepartment of Psychology, Harvard University,
comments on an early draft, and Anya Vedantambe for her help coding ChatGPT                                      Cambridge, MA 02138


1.    A. Vaswani et al., “Attention is all you need” in Advances in Neural Information Processing Systems,       28. J. P. A. Ioannidis, Contradicted and initially stronger effects in highly cited clinical research. JAMA
      I. Guyon et al., Eds. (Curran Associates Inc., 2017), vol. 30, pp. 5998–6008.                                  294, 218–228 (2005).
2.    X. Zhang et al., Artificial intelligence for science in quantum, atomistic, and continuum systems.         29. T. M. Errington et al., An open investigation of the reproducibility of cancer biology research. eLife 3,
      arXiv [Preprint] (2023). https://arxiv.org/pdf/2307.08423.pdf (Accessed 19 January 2024).                      e04333 (2014).
3.    J. Jumper et al., Highly accurate protein structure prediction with AlphaFold. Nature 596, 583–589         30. T. M. Errington et al., Investigating the replicability of preclinical cancer biology. eLife 10, e71601
      (2021).                                                                                                        (2021).
4.    G. Carleo, M. Troyer, Solving the quantum many-body problem with artificial neural networks.               31. L. K. John, G. Loewenstein, D. Prelec, Measuring the prevalence of questionable research practices
      Science 355, 602–606 (2017).                                                                                   with incentives for truth telling. Psychol. Sci. 23, 524–532 (2012).
5.    D. Kochkov et al., Machine learning-accelerated computational fluid dynamics. Proc. Natl. Acad. Sci.       32. M. L. Head, L. Holman, R. Lanfear, A. T. Kahn, M. D. Jennions, The extent and consequences of
      U.S.A. 118, e2101784118 (2021).                                                                                p-hacking in science. PLoS Biol. 13, e1002106 (2015).
6.    M. H. S. Segler, M. Preuss, M. P. Waller, Planning chemical syntheses with deep neural networks and        33. J. P. Simmons, L. D. Nelson, U. Simonsohn, False-positive psychology: Undisclosed flexibility in data
      symbolic AI. Nature 555, 604–610 (2018).                                                                       collection and analysis allows presenting anything as significant. Psychol. Sci. 22, 1359–1366 (2011).
7.    Y. Zheng et al., Large language models for scientific synthesis, inference and explanation. arXiv          34. L. P. Argyle et al., Out of one, many: Using language models to simulate human samples. Polit. Anal.
      [Preprint] (2023). https://arxiv.org/pdf/2310.07984.pdf (Accessed 19 January 2024).                            31, 337–351 (2023).
8.    K. M. Jablonka et al., 14 examples of how LLMs can transform materials science and chemistry:              35. D. Dillon, N. Tandon, Y. Gu, K. Gray, Can AI language models replace human participants?
      A reflection on a large language model hackathon. Digit. Discov. 2, 1233–1250 (2023).                          Trends Cognit. Sci. 27, 597–600 (2023).
9.    D. A. Boiko, R. MacKnight, B. Kline, G. Gomes, Autonomous chemical research with large language            36. G. V. Aher, R. I. Arriaga, A. T. Kalai, “Using large language models to simulate multiple humans and
      models. Nature 624, 570–578 (2023).                                                                            replicate human subject studies” in Proceedings of the 40th International Conference on Machine
10.   D. Demszky et al., Using large language models in psychology. Nat. Rev. Psychol. 2, 688–701 (2023).            Learning, A. Krause et al., Eds. (PMLR, 2023), pp. 337–371.
11.   H. Kotek, R. Dockum, D. Q. Sun, “Gender bias and stereotypes in large language models” in                  37. I. Grossmann et al., AI and the transformation of social science research. Science 380, 1108–1109
      Proceedings of the ACM Collective Intelligence Conference (CI ‘23) (Association for Computing                  (2023).
      Machinery, Delft, The Netherlands, 2023), pp. 12–24.                                                       38. A. Caliskan, J. J. Bryson, A. Narayanan, Semantics derived automatically from language corpora
12.   F. Bianchi et al., “Easily accessible text-to-image generation amplifies demographic stereotypes               contain human-like biases. Science 356, 183–186 (2017).
      at large scale” in Proceedings of the 2023 ACM Conference on Fairness, Accountability, and                 39. T. E. S. Charlesworth, V. Yang, T. C. Mann, B. Kurdi, M. R. Banaji, Gender stereotypes in natural
      Transparency (FaccT ‘23) (Association for Computing Machinery, New York, NY, 2023),                            language: Word embeddings show robust consistency across child and adult language corpora of
      pp. 1493–1504.                                                                                                 more than 65 million words. Psychol. Sci. 32, 218–240 (2021).
13.   Y. Zhang et al., Siren’s song in the AI ocean: A survey on hallucination in large language models.         40. W. Guo, A. Caliskan, “Detecting emergent intersectional biases: Contextualized word embeddings
      arXiv [Preprint] (2023). https://arxiv.org/pdf/2309.01219.pdf (Accessed 19 January 2024).                      contain a distribution of human-like biases” in Proceedings of the 2021 AAAI/ACM Conference on
14.   W. H. Walters, E. I. Wilder, Fabrication and errors in the bibliographic citations generated by                AI, Ethics, and Society (AAAI/ACM, 2021), pp. 122–133.
      ChatGPT. Sci. Rep. 13, 14045 (2023).                                                                       41. B. A. Nosek et al., Pervasiveness and correlates of implicit attitudes and stereotypes. Eur. Rev. Soc.
15.   S. Bubeck et al., Sparks of artificial general intelligence: Early experiments with GPT-4. arXiv               Psychol. 18, 36–88 (2007).
      [Preprint] (2023). https://arxiv.org/pdf/2303.12712.pdf (Accessed 19 January 2024).                        42. B. A. Nosek, M. R. Banaji, A. G. Greenwald, Math = male, me = female, therefore math not = me.
16.   M. Binz, E. Schulz, Using cognitive psychology to understand GPT-3. Proc. Natl. Acad. Sci. U.S.A. 120,         J. Pers. Soc. Psychol. 83, 44–59 (2002).
      e2218523120 (2023).                                                                                        43. J. Zhao, T. Wang, M. Yatskar, V. Ordonez, K. W. Chang, “Men also like shopping: Reducing gender
17.   S. Yadlowsky, L. Doshi, N. Tripuraneni, Pretraining data mixtures enable narrow model selection                bias amplification using corpus-level constraints” in Proceedings of the 2017 Conference on
      capabilities in transformer models. arXiv [Preprint] (2023). https://arxiv.org/pdf/2311.00871.pdf              Empirical Methods in Natural Language Processing, M. Palmer, R. Hwa, Eds. (Association for
      (Accessed 19 January 2024).                                                                                    Computational Linguistics, Copenhagen, Denmark, 2017), pp. 2979–2989.
18.   R. A. Millikan, Science and religion. Bull. Calif. Inst. Technol. 32, 3–20 (1922).                         44. K. Lloyd, Bias amplification in artificial intelligence systems. arXiv [Preprint] (2023). https://arxiv.
19.   R. Taylor et al., Galactica: A large language model for science. arXiv [Preprint] (2022). https://arxiv.       org/pdf/1809.07842.pdf (Accessed 19 January 2024).
      org/pdf/2211.09085.pdf (Accessed 19 January 2024).                                                         45. A. Wang, O. Russakovsky, “Directional bias amplification” in Proceedings of the 38th International
20.   Y. Cao et al., A comprehensive survey of AI-generated content (AIGC): A history of generative AI from          Conference on Machine Learning (PMLR, 2021), pp. 10882–10893.
      GAN to ChatGPT. arXiv [Preprint] (2023). https://arxiv.org/pdf/2303.04226.pdf (Accessed 19 January         46. OpenAI, GPT-4 technical report. arXiv [Preprint] (2023). https://arxiv.org/pdf/2303.08774.pdf
      2024).                                                                                                         (Accessed 19 January 2024).
21.   V. Rawte et al., Exploring the relationship between LLM hallucinations and prompt linguistic               47. M. Nadeem, A. Bethke, S. Reddy, “Stereoset: Measuring stereotypical bias in pretrained language
      nuances: Readability, formality, and concreteness. arXiv [Preprint] (2023). https://arxiv.org/                 models” in Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics
      pdf/2309.11064.pdf (Accessed 19 January 2024).                                                                 and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long
22.   A. Azaria, T. Mitchell, The internal state of an LLM knows when it’s lying. arXiv [Preprint] (2023).           Papers) (Association for Computational Linguistics, 2021), pp. 5356–5371.
      https://arxiv.org/pdf/2304.13734.pdf (Accessed 19 January 2024).                                           48. T. E. S. Charlesworth, M. Navon, Y. Rabinovich, N. Lofaro, B. Kurdi, The project implicit international
23.   J. Wei et al., Emergent abilities of large language models. arXiv [Preprint] (2023). https://arxiv.org/        dataset: Measuring implicit and explicit social group attitudes and stereotypes across 34 countries
      pdf/2206.07682.pdf (Accessed 19 January 2024).                                                                 (2009–2019). Behav. Res. Methods 55, 1413–1440 (2023).
24.   Open Science Collaboration, PSYCHOLOGY, Estimating the reproducibility of psychological science.           49. W. Hofmann, B. Gawronski, T. Gschwendner, H. Le, M. Schmitt, A meta-analysis on the correlation
      Science 349, aac4716 (2015).                                                                                   between the implicit association test and explicit self-report measures. Pers. Soc. Psychol. Bull. 31,
25.   B. A. Nosek et al., Replicability, robustness, and reproducibility in psychological science. Annu. Rev.        1369–1385 (2005).
      Psychol. 73, 719–748 (2022).                                                                               50. M. Lee, A mathematical investigation of hallucination and creativity in GPT models. Mathematics 11,
26.   C. F. Camerer et al., Evaluating replicability of laboratory experiments in economics. Science 351,            2320 (2023).
      1433–1436 (2016).                                                                                          51. S. A. Lehr, A. Caliskan, S. Liyanage, M. R. Banaji, Data from “ChatGPT as research scientist: Probing
27.   C. F. Camerer et al., Evaluating the replicability of social science experiments in nature and science         GPT’s capabilities as a research librarian, research ethicist, data generator and data predictor.” OSF.
      between 2010 and 2015. Nat. Hum. Behav. 2, 637–644 (2018).                                                     https://osf.io/sdahr/. Deposited 10 June 2024.


PNAS         2024         Vol. 121          No. 35        e2404328121                                                                               https://doi.org/10.1073/pnas.2404328121 9 of 9
