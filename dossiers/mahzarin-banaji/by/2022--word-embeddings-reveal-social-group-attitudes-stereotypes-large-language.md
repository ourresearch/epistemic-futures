---
title: "Word embeddings reveal social group attitudes and stereotypes in large language corpora"
person: mahzarin-banaji
section: by
type: book-chapter
year: 2022
date: 2022
venue: "In M. Dehghani & R. Boyd (Eds.), Handbook of language analysis in psychology (pp. 494-510). New York: Guilford Press"
authors: "Charlesworth, T. E. S., & Banaji, M. R"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/2021_Charlesworth_TAL.pdf
doi: 
openalex_id: 
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard publications page (banaji.sites.fas.harvard.edu), extracted with pdftotext -layout. Title-overlap check 1.00. Not matched to an OpenAlex work record in this pass. Full citation as listed on her site: Charlesworth, T. E. S., & Banaji, M. R. (2022). Word embeddings reveal social group attitudes and stereotypes in large language corpora. In M. Dehghani & R. Boyd (Eds.), Handbook of language analysis in psychology (pp. 494-510). New York: Guilford Press."
---

# Word embeddings reveal social group attitudes and stereotypes in large language corpora

## Full text

ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                        1


 Word embeddings reveal social group attitudes and stereotypes in large language corpora


                        Tessa E.S. Charlesworth & Mahzarin R. Banaji


                        Harvard University, Cambridge, Massachusetts


Accepted for publication in The Atlas of Language (eds. Dehghani, M, & Boyd, R). Final version
                                 of record may differ slightly.


                                         Author Note

The authors declare no competing financial interests. Correspondence concerning this article

should be addressed to Tessa Charlesworth, Department of Psychology, Harvard University,

Cambridge, MA 02138, at tet371@g.harvard.edu. The authors acknowledge funding from the

Harvard Mind Brain Behavior Inter-Faculty Initiative, the Foundations of Human Behavior, and

the Hao Family Inequality in America Support Fund awarded to M. R. Banaji and T. E. S.

Charlesworth.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                              2


Word embeddings reveal social group attitudes and stereotypes in large language corpora

 “There are no social representations without language, just as without them [social
representations] there is no society”
    - Moscovici (2000), p. 159


   Human language is a unique medium through which a society communicates the attitudes

and stereotypes about various social groups, whether gender, race, ethnicity, nationality, class,

age, or more (Beukeboom & Burgers, 2019). Without ever even meeting a member of a social

group, one need only listen to the language of passing conversations, watch a movie, or read a

newspaper to learn how that social group is treated and perceived by society. As a result, our

culture can construct and perpetuate attitudes and stereotypes about social groups – from the

relatively innocuous (e.g., “Canadians love hockey”) to the problematic (e.g., “men are more

brilliant than women”; Storage, Charlesworth, Banaji, & Cimpian, 2020) – even when those

attitudes and stereotypes have little bearing in reality or direct experience. Indeed, it is simply the

widespread and repeated transmission of attitudes and stereotypes that makes them seem

legitimate and true (Ames, 2004; Duguid & Thomas-Hunt, 2015). For this reason, language is

taken to be so central to constructing and maintaining a society’s representations of social groups

that scholars have argued there can be no such representations without language (Durkheim,

1924; Moscovici, 2000). That is, without language, our society would not be able to transmit and

maintain the nuanced social group representations across people, time, and place. When social

scientists set out to study how social groups are represented in society, their research thus

depends on the study of how those groups are represented through language.

   Today, advances in the online availability of massive language corpora (e.g., billions of

words from millions of books), alongside techniques to rapidly analyze such data using natural

language processing (in particular, word embeddings), have yielded exciting new opportunities


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                              3


to study social group representations in language. As we elaborate below, word embeddings look

at the contexts in which words appear (i.e., “the company words keep”; Firth, 1957) to

quantitatively represent the meaning of words and reveal which words are close or far in

meaning. The relative closeness of these word representations can be used to uncover, for

instance, whether words referring to the group female are semantically more similar to words

referring to family or to words referring to career. In this way, word embeddings can provide

snapshots of how social groups (e.g., gender, race, ethnicity, class) are represented as good/bad,

strong/weak, doctor/nurse and so on. Moreover, because word embeddings can be applied to

archived texts from different time periods and cultures, the method can uncover how the social

group representations of today emerged and transformed across time and place.

   In this chapter, we review early findings from the study of social group representations (i.e.,

stereotypes and attitudes) using word embeddings applied to massive natural human language.

Although this research is still young (with the oldest papers published just in 2016), emerging

results suggest surprising consistency and prevalence of group representations across various

topics, language sources, and even across time and cultures. The implication of such widespread

prevalence is that social group attitudes and stereotypes (including problematic ones) can

become perceived as true and legitimate (e.g., Ames, 2004; Duguid & Thomas-Hunt, 2015),

even when they have little bearing in reality. Following this review, we outline open questions

and suggestions for future work.

Social group representations can be hidden in language

   To fully appreciate the contribution of word embeddings we must recognize that, at least

today, when humans communicate attitudes and stereotypes about social groups, they will rarely

do so explicitly and publicly. Explicit phrases attributing negative qualities to groups, such as


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                              4


“elderly people are slow,” or “women are too weak for politics,” are rarely heard out loud in

most public discourse, even though the sentiments may remain (Bergsieker et al., 2012). Indeed,

parents are often surprised when their young children express full-blown stereotypes: when

children publicly spout the belief that “boys are obviously more brilliant than girls,” or that

“Black Americans are less “good” than White Americans” (e.g., Baron & Banaji, 2006; Bian,

Leslie, & Cimpian, 2017; Croft, Schmader, Block, & Baron, 2014), their parents are

understandably bewildered. Recently, a colleague of ours reported that her 4-year old daughter

asked who “this” is, looking at a picture of the late Supreme Court Justice Ruth Bader Ginsburg.

After explaining who RBG was, the child was swift and confident to respond, “No way she could

be a judge!” How could this be, our colleague asked, when nothing her daughter had heard at

home or in daycare would have supported such a gender-stereotyped belief.

   Our answer to the parents’ question “How could this be?” is to explain that such biases are

pervasive. Nobody needs to say anything as direct and explicit as “RBG cannot be a judge” or

that “people who look like RBG cannot be judges”. Instead, adult-child conversations (and

human language, more generally) can contain seemingly innocuous phrases such as “What a

good cook mommy is!” or “Daddy’s office gave him a star for his work!” that provide the

building blocks for the 4-yr old to assert that RBG could never have been a judge. When mommy

co-occurs in similar contexts with cook, and daddy co-occurs in similar contexts with work, the

listener can infer more than just a simple association. That is, patterns of co-occurrences create

an attachment to the idea of women+cook that makes women+work less imaginable. In this way,

language reveals social representations that link groups (women/men) with attributes

(home/work), even without explicit reference. Simply put, social representations “never reveal

themselves clearly… so much are they intricately interwoven with a certain collective memory


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                               5


inscribed in language” (p. 182, Moscovici, 2000). A researcher is therefore required to look

beyond what is said on the surface of language to study the deeper, sometimes hidden, context of

words and meaning.

Using word embeddings to uncover social group representations

   Techniques from natural language processing (NLP) offer many methods to uncover the

representations of social groups that persist in subtle, indirect, and hidden ways in language. One

NLP method that has received increasing attention recently is the method of word embeddings

(Bojanowski et al., 2017; Mikolov et al., 2018; Pennington et al., 2014), an idea that traces its

technical roots to tools such as Latent Semantic Analysis (Deerwester et al., 1990). Here, we

focus on studies using word embeddings to examine the shared semantic meaning between social

groups (e.g., female/male, Black/White, old/young, rich/poor), on the one hand, and various

attributes including general valence (e.g., good/bad), traits (e.g., nurturing/strong, smart/dumb),

occupations (e.g., nurse/surgeon, teacher/principal, lawyer/clerk) and other content (e.g., objects

such as skirt/pants, magazine/newspaper), on the other hand.

   Although the formal methodology behind word embeddings is covered elsewhere (Kennedy

et al., this volume) we provide a high-level understanding of word embeddings to contextualize

our discussion. To begin, imagine a cloud (formally, a high-dimensional vector space) that

characterizes the meanings of all words in a language. The placement of each word in the cloud

is determined by its similarity in meaning to all other words. Words with similar meaning (e.g.,

flower, tree) are located closer to one another in semantic space while words with less similarity

in meaning (e.g., flower, hammer) are placed farther apart. The term “word embedding” refers to

the quantitative vector representation that captures that word’s meaning and places (embeds) the

word within the cloud. A word’s placement is learned by looking at the many and unique


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                                6


contexts in which a word is used. For this reason, word embeddings begin to overcome

limitations of simpler NLP methods that perform direct analyses of text and can provide a more

indirect assessment of the hidden patterns of attributes associated with social group

representations in language.

   To use word embeddings to study the semantic overlap between social groups (e.g., female,

male) and attributes (e.g., skirt, pants, trustworthy, competent, nurse, surgeon), we simply extend

our example of the form flower-tree/hammer by replacing the words with social group terms and

attribute terms (e.g., female-skirt/pants). For instance, if the word female is closer in meaning to

the word skirt than the word pants (because female/skirt occur more frequently in similar

contexts), the word embedding for female will be closer to the embedding for skirt than for

pants. In word embeddings, the strength of such an association can be formalized as the cosine of

the angle between two vectors. A wider angle (small cosine similarity) signals greater semantic

distance, while a narrower angle (larger cosine similarity) signals a relatively closer semantic

connection. In this way, we can quantitatively test any number of relative associations between

groups and attributes to quantify how groups are represented in natural human language.

The first tests of social group representations using word embeddings

       We are fortunate at this time to be able to mention nearly all known investigations of

word embeddings to examine the content of associations that surround social groups. Given the

speed at which new research is appearing, it will soon become difficult to cover the scope of all

existing studies in a single chapter. We welcome this development as it signals the birth of a

method that is proving to be exciting to so many who are interested in social cognition.

       Thus far, researchers applying word embeddings to study how social groups are

represented in language corpora have largely focused on studying stereotypes and attitudes about


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                              7


gender, from early demonstrations (Bolukbasi et al., 2016) to the most recent publications (e.g.,

Charlesworth, Yang, Mann, Kurdi, & Banaji, in press; DeFranza, Mishra, & Mishra, 2020;

Lewis & Lupyan, 2020). Only a small subset of studies has investigated attitudes and stereotypes

towards other groups such race, ethnicity, social class, age, or ability (reviewed below), leaving

many groups and identities unexamined (e.g., body weight, mental health, nationality). This

presents a clear area for further inquiry. Additionally, with few exceptions (e.g., Bolukbasi et al.,

2016; Garg et al., 2018; Xu et al., 2019), the majority of papers have studied social group

representations by applying the Word Embeddings Association Test (WEAT, introduced below;

Caliskan et al., 2016). As a result, much of the current research shares a similar framework: the

authors test for the presence of a specific stereotype that is well-studied in past literature and can

be clearly represented through multiple words (e.g., male/female-math/arts is well-studied and

can be represented by words commonly-used as stimuli for the Implicit Association Test on the

same topic; Nosek, Banaji, & Greenwald, 2002).

       Although much recent work with word embeddings uses the WEAT, we begin our review

of the literature chronologically by discussing one of the first demonstrations that uncovers

social group representations using word embeddings. This first test builds on the geometric

properties of word embeddings (i.e., their representation as vectors), which can be used to

answer simple analogy queries. For instance, when asked “Berlin is to Germany as X is to

France,” the word embedding vector given for X is, accurately, “Paris.” Bolukbasi and

colleagues (2016) noted that this type of “analogy task” could also be used to reveal more

contested and potentially problematic representations of social groups. When queried with “man

is to programmer as woman is to X,” the resulting word embedding answer was the female-

dominated occupation of “homemaker.” Similar gender stereotype analogies emerged across


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                              8


other traits, qualities, and occupations, ranging from the relatively innocuous “he-carpentry/she-

sewing,” and “he-chuckle/she-giggle,” to the pejorative “he-coward/she-whore” (for example

analogies, see Table 1).

Table 1.
Example analogies of gender stereotypes, obtained from Bolukbasi and colleagues (2016)
                                 Man is to…         As woman is to…
                                  Doctor               Midwife
                                 Surgeon                Nurse
                                 Football             Volleyball
                                   Pizza              Cupcakes
                                 Brilliant             Lovely
                                 Grandeur              Beauty
                                 Arrogant            Judgmental
                                 Briefcase            Handbag
                                Carpentry              Sewing
                                 Chuckle                Giggle
                                  Coward                Whore
       What are the societal implications of such revealed associations? A skeptical reader may

retort that the results of such analogies simply describe “what is” in society. After all, due to

persistent divisions in labor, women in many countries, including the United States, remain more

likely to be primary caregivers than men (U.S. Bureau of Labor Statistics, 2019). Thus, the

women-homemaker association may simply be descriptive. However, the same argument cannot

be offered for stereotypes that are clearly not grounded in reality (e.g., he-coward/she-whore, or

men-brilliant/women-beautiful; Storage et al., 2020). In such cases, the broad trends of human

language reveal bias (i.e., an inaccurate or harmful association) of how groups are, in general,

perceived and represented in the culture. Ultimately, when everything we hear and read (through

the Internet, TV, movies, newspapers, or books) communicates such a widespread cultural

stereotype (e.g., that “men are more brilliant”), we may come to see that stereotype as legitimate

and alter our behavior accordingly (e.g., women may select out of jobs described as brilliant;


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                               9


Bian, Leslie, Murphy, & Cimpian, 2018). In this way, it is important to remember that language

not only describes reality, but also helps shape it, with potentially unequal consequences (see

discussion below, and Caliskan & Lewis, this volume).

   Moreover, there is justifiable concern that the biases revealed from word embeddings can

perpetuate biases in downstream applications in machine learning and decision-making. Even a

rather neutral fact-like report (e.g., man-programmer/woman-homemaker) can create problems if

over-used by artificial intelligence and algorithmic systems for decision-making, such as in using

NLP to decide whom to hire or promote. To our knowledge, the current tools of word

embeddings and the WEAT have not yet been applied in such a problematic way. Nevertheless,

it is worth anticipating the potential risks that could arise from relying too heavily on automated

algorithms applied to biased language (e.g., as has been shown in other applications relying on

AI for decision-making; O’Neil, 2017).

Building our knowledge of social group representations with word embeddings

   Several questions are immediately prompted by the initial work of Bolukbasi and colleagues.

First among them: How are other groups (beyond gender) represented in language? And what are

the magnitudes of these other social representations? The analogy task has the benefit of

providing an interpretable, qualitative insight into the content of social group representations, but

it cannot directly compare the relative strength. Furthermore, the question arises as to how the

magnitude of group representations obtained via word embeddings align with the magnitude of

group representations from more traditional psychological tests of attitudes and stereotypes in the

population (i.e., those measured from implicit tests like the Implicit Association Test, as well as

explicit tests like self-report surveys). Are word embeddings capturing similar biases to what is

measured from the mind?


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                                                10


    To answer these questions, Caliskan and colleagues (2016) proposed the Word Embedding

Association Test (WEAT), directly building from the methods of the Implicit Association Test

(IAT), a widely-used test to indirectly measure relatively automatic and hidden attitudes and

stereotypes (Greenwald et al., 1998). The WEAT follows the logic of the IAT in that it measures

the associations between groups (e.g., male/female) and attributes (e.g., home/work). However,

instead of using reaction time to capture the strength of association between a group

(female/male) and an attribute (home/work) in a single respondent’s mind, the WEAT uses

cosine similarities to capture the strength of association between a group and attribute in the

semantic space of human language.

    With the WEAT, Caliskan and colleagues reported a stunning finding: For every bias

reported by IAT researchers on 10 tests of group-attribute association, ranging from African-

American-bad/European-American-good to flower-good/insect-bad, scores on the WEAT

revealed not only the same direction of bias as observed on the IAT but also similar magnitudes

(Table 2, reproduced from Caliskan and colleagues)1. These findings demonstrate, for the first

time, that the language of the Internet (with hundreds of billions of words) encodes the same

strong magnitudes and widespread prevalence of social group biases as those studied with

traditional psychological measures. Among the contributions is the suggestion that measures of

individual minds, such as the IAT, are ultimately revealing the thumbprint of the broader culture

on the mind (Payne et al., 2017).

Table 2.


1
  Interestingly, however, the relative magnitudes of effect sizes did not perfectly align with IAT effect sizes. For
instance, one of the strongest IAT effects is observed for Young people-good/Old people-bad and male-
science/female-arts. The strongest WEAT biases, however, were male-career/female-family and European
American-good/African American-bad, with relatively weaker (although still large) WEAT biases observed for
male-math/female-arts and Young people-pleasant/Old people-unpleasant. Future research could examine more
domains to see how closely WEAT and IAT scores align across a wider sample space of social group topics and
discover whether there are systematic areas that the WEAT over or underestimates relative to the IAT.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                            11


Magnitudes of social group attitudes and stereotypes using the IAT and WEAT, obtained from
Caliskan and colleagues (2016)
        Group                Attribute        IAT result (Cohen’s d)     WEAT result (Cohen’s d)

    Male vs. female       Science vs. arts              1.47                         1.24

    Male vs. female         Math vs. arts               0.82                         1.06

    Male vs. female      Career vs. family              0.72                         1.81

     Young vs. old          Good vs. bad                1.42                         1.21
  European-American
                            Good vs. bad                1.17                         1.41
 vs. African-American
  Mental vs. physical      Temporary vs.
                                                        1.01                         1.38
        disease             permanent


Testing consistency of social group representations using word embeddings

   Following the results of Caliskan and colleagues, the WEAT approach has been extended to

additional corpora and newer embeddings models. For instance, the first papers naturally used

the word embeddings algorithms that first showed feasibility in analyzing massive online text

corpora (of over 8 billion words), such as GloVe (Pennington et al., 2014) and word2vec

(Mikolov, Chen, et al., 2013; Mikolov, Sutskever, et al., 2013). Today, more models have arrived

including a new class of “contextualized” word embeddings, such as BERT (Devlin et al., 2018),

and RoBERTA (Liu et al., 2019), with many more surely on the way (for a review of the

timeline of some NLP approaches, including word embeddings, see Boyd & Schwartz, in press).

Interestingly, even these newer word embeddings approaches generally replicate the data from

the earlier algorithms (Guo & Caliskan, 2020; Kurita et al., 2019), reinforcing the robustness of

the conclusions across various methodological approaches.

   Another research direction prompted by the development of the WEAT has been to

quantitatively compare the strength and prevalence of social group representations across various

language sources or corpora (e.g., child language versus adult language; Charlesworth et al., in


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                                12


press), across cultures (DeFranza et al., 2020; Lewis & Lupyan, 2020), and across time

(Kozlowski et al., 2019). For instance, Charlesworth and colleagues (in press) applied the

WEAT to 7 unique corpora of child and adult conversations, books, and TV/movies to test 4

well-studied gender representations (e.g., male-science/female-arts, male-bad/female-good) as

well as gender associations with 600+ traits and 300+ occupations. Despite the many differences

that would be predicted across age groups, language sources, and time periods, the authors found

remarkable consistency in the prevalence of gender representations. As shown in Figure 1, the

overall strength of stereotypes (meta-analytic estimates across all 7 corpora) consistently

revealed strong effects in the expected directions. Similar conclusions of widespread prevalence

have also been obtained by applying word embeddings to Twitter, Wikipedia, and adult movie

synopses (e.g., Lauscher & Glavas, 2019; Xu et al., 2019).


                                    2


                                   1.5


                                    1


                                   0.5


                     Effect Size
                                    0


                           −0.5


                                   −1


                           −1.5          Child−produced speech    Adult−produced speech
                                         Child−directed speech    Adult−directed books
                                   −2    Child−directed books     Adult−directed media
                                         Child−directed media     Meta Estimate

                                            Male−Bad     Male−Work     Male−Science     Male−Math
                                          Female−Good   Female−Home    Female−Arts    Female−Reading

Figure 1. Gender associations in child and adult language, reproduced from Charlesworth and
colleagues (in press). Y-axis represents Word Embedding Association Test (WEAT) D score
effect size; X-axis represents the four gender associations. Error bars represent 95% confidence
intervals, computed from the standard error (i.e., the standard deviation of the permutation
distribution of WEAT effect scores).


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                              13


   Looking forward, future work can explore consistency across even more diverse corpora of

text including statements from hiring committees, police reviews, or judges’ legal decisions (e.g.,

Ash, Chen, & Ornaghi, 2020). Additionally, testing corpora that have been ostensibly

“debiased”, such as by subtracting out the gender dimension in the word embedding space to

reduce gender bias (e.g., Bolukbasi et al., 2016; Brunet, Alkalay-Houlihan, Anderson, & Zemel,

2019; Manzini, Lim, Tsvetkov, & Black, 2019), could reveal whether some stereotypes are more

or less resistant to existing “debiasing” algorithms in language. For instance, Bolukbasi and

colleagues (2016) suggested that a researcher can discover the gender dimension in word

embeddings by subtracting two gender vectors (e.g., the vector woman – the vector man returns

the gender subspace g). Subsequently, the researcher can correct all vectors in the corpus by

subtracting out this gender dimension (e.g., subtract g from the vectors home, work, science, arts,

pink, blue, etc.) resulting in only the non-gendered semantic content. With this method, the

authors showed that, indeed, many of the aforementioned problematic analogies were reduced or

eliminated. However, it may not be possible to similarly subtract out a group dimension that is

relatively less communicated in language, such as race or sexuality, dimensions that do not have

markings by pronouns (e.g., there is no race equivalent of his/hers) or role terms (e.g., there is no

race equivalent of waiter/waitress). Theoretically, this could provide an interesting insight into

the types of social group dimensions that are most reliant on more subtle, hidden

communications and therefore most resistant to language-based interventions.

   More generally, the finding of consistency across language sources is notable because it

underscores how deeply gender stereotypes are embedded throughout human language and

communication. In this sense, gender stereotypes are truly “collective” shared representations

that are so widespread as to become perceived as societal facts (Durkheim, 1924). Yet because


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                                       14


the majority of studies to date have focused on gender stereotypes (well over two-thirds of the

total number of papers we reviewed), it is far less-known whether the same conclusions of

widespread, consistency would apply to groups of race, class, nationality, age, or more. Most

likely, some group representations will differ in their degree of consistency across language. For

instance, groups that are considered to be “arbitrary,” such as race and ethnicity, may be more

variable than those groups that appear across societies and history, such as gender and age

(Sidanius & Pratto, 1999).

    Notably, two recent papers using word embeddings to examine cross-language differences

suggest that even gender stereotypes may not always or equally be present in natural language

(DeFranza et al., 2020; Lewis & Lupyan, 2020). DeFranza and colleagues (2020) examined the

prevalence of gender attitudes (i.e., male-good/female-bad, assessed with the WEAT) across 45

world languages. The languages were specifically chosen to capture those that use grammatical

gender (e.g., French, Hebrew, German) and those that do not (e.g., English, Hungarian, Chinese).

Briefly, a language with grammatical gender means that it uses gender to label nouns, verbs, or

pronouns (e.g., in French, the noun for “cat” is male and is referenced as “le chat,” whereas the

noun for “earth” is female and is referenced as “la terre”). A language without grammatical

gender, in contrast, does not gender nouns and verbs (e.g., in English, “cat” is simply “the cat”

and “earth” is simply “the earth”).

    Surprisingly, less than half of the 45 languages studied by DeFranza and colleagues revealed

a male-good/female-bad2 association across data from Wikipedia and the Common Crawl. This


2
  Note that the male-good/female-bad association is in contrast to the more common finding among English-
speaking participants that associate women-good/men-bad (not men-good/women-bad). Although counterintuitive,
this widely-studied “wonder are wonderful” effect (Eagly & Mladinic, 1989, 1994) has also recently been
documented using word embeddings with English corpora (Charlesworth et al., in press). Future research is now
poised to explore whether English may be one of the unique languages to reveal the “women are wonderful” effect,
while other languages (especially those encoding grammatical gender) may reveal a “men are wonderful” effect.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                           15


stands in contrast to the conclusion of widespread consistency within only English corpora (see

above) and opens the door to examine what variable may explain which languages do and do not

reveal the male-good/female-bad association. DeFranza and colleagues found that one such

variable is grammatical gender: languages with grammatical gender were more likely to reveal a

male-good/female-bad association. For example, in the Common Crawl, 67% of languages with

grammatical gender revealed significant male-good/female-bad associations, whereas none of the

languages without grammatical gender (including English) revealed such an association. Thus,

structural features of a culture’s language may contribute to the prevalence of gender

associations communicated in that culture.

   Lewis and Lupyan (2020) recently offered a complementary cross-cultural analysis of the

prevalence of the male-career/female-family gender stereotype across 25 world languages. As

with the aforementioned findings, Lewis and Lupyan also observed that some but not all

languages appear to encode the stereotype, suggesting that cultural- or language-level variables

are creating variation in the strength of gender stereotypes. However, Lewis and Lupyan found

no evidence that grammatical gender predicted the strength of the male-career/female-family

stereotype encoded in a language. Whether this discrepancy between the two papers was due to

the sample of languages (25 versus 45) or to the distinction between attitudes (good/bad) and

stereotypes (career/family associations) is unknown at this time. Nevertheless, Lewis and

Lupyan did identify another variable that correlated with the strength of the male-career/female-

family stereotype in word embeddings: the strength of the IAT scores from speakers of that

language. That is, across the 25 languages, the stronger the aggregated IAT scores from speakers

of a language (e.g., the IAT scores from speakers of English, French, Dutch, Polish, etc.), the

stronger the WEAT scores for the gender stereotype in that language (e.g., the WEAT scores for


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                             16


texts in English, French, Dutch, Polish, etc.). This reveals a coupling between language and the

IAT, although leaving open whether the coupling arises because language merely reflects

existing biases and/or actually shapes new biases (Caliskan & Lewis, this volume).

   In addition to such tests of consistency across corpora and cultures, a final line of research

has begun to test the consistency of social group representations across historical time. With the

availability of pre-trained word embeddings from historical text corpora stretching back to the

1800s (Hamilton, Leskovec, & Jurafsky, 2016) researchers are newly equipped to study how

group representations have transformed at timescales that could not have been imagined

previously given constraints of traditional psychological data. For the first time, researchers can

look back to quantitatively compare the attitudes and beliefs of societies from centuries ago to

the attitudes and beliefs of our society today. The almost magical quality is that, without having

access to the minds of 19th and 20th century speakers, we may nevertheless be able to uncover

their implicit attitudes and stereotypes. We can do this because contemporary implicit attitudes

and beliefs obtained with the IAT are shown to correspond to the representations obtained with

word embeddings (Caliskan et al., 2016; Lewis & Lupyan, 2020). We can therefore reasonably

assume that the same correspondence extends back in time, such that the automatic associations

of the 1800s can be captured through historical text from that period.

   Already, a handful of studies have capitalized on this possibility and explored historical

patterns of attitudes and beliefs about race/ethnicity (Garg et al., 2018), gender (Jones et al.,

2020), and social class (Kozlowski et al., 2019). Garg and colleagues (2018) used data from

historical books (the Corpus of Historical American English) from 1900-1990 and the New York

Times Annotated Corpus from 1988-2005 to document the top traits and occupations associated

with gender and racial/ethnic groups (e.g., Chinese, Hispanic, Russian, White). Both gender and


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                                17


racial/ethnic representations shifted in content across time. In 1910, for example, the top

adjective associates with Chinese last names were largely negative, including irresponsible,

envious, barbaric, and aggressive. In 1990, however, positive adjectives emerged, with Chinese

last names now associated with inhibited, passive, dissolute, and haughty.

   For gender stereotypes, the content changed from reflecting women as largely positive and

complacent, with adjectives of charming, placid, delicate, and passionate in the 1910s, to more

mixed content, including more agentic qualities and negative adjectives such as morbid,

physical, and artificial. Similar findings were reported by Jones and colleagues (2020), who

showed that female-family/male-career associations weakened towards neutrality from 1800-

1990. The female stereotype in language thus appears to have moved away from a simple

stereotype of females as charming, warm, and family-oriented, to more mixed representations

that reflect female agency and roles in the workforce.

   Importantly these changes in gender and racial/ethnic representations are not random

fluctuations. Rather, the changes were found to align with meaningful historical events. For

instance, a phase shift (i.e., a point of discontinuity) in the content of gender stereotypes in the

1960s aligned with the rise of the women’s movement in the 1960s (Garg et al., 2018; Jones et

al., 2020). Similarly, multiple phase shifts were noted in the stereotypes about racial groups.

Although stereotypes about Chinese people began as predominantly negative, in the 1960s, the

content of the stereotypes transitioned to the contemporary stereotypic content of Asian

Americans as “passive” but also “haughty” (Zou & Cheryan, 2017), coinciding with the first

major immigration wave from East Asia to America and passage of the Immigration &

Nationality Act in 1965.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                            18


   In the same vein, when there has been little to no substantive societal change (i.e., few

protests, immigrations, etc.), group representations in word embeddings appear to reveal stability

over the long-term. Specifically, the representation of groups defined by social class (e.g.,

“affluent” versus “poor”) have remained largely stable over the past century (Kozlowski, Taddy,

& Evans, 2019), perhaps as a result of the persistent structuring of society according to social

class. That is, although there have been some changes (e.g., the dimension of “education”

became more important to defining social class), the many other dimensions that characterize

class (e.g., morality, employment) did not shift over time. Ultimately, the way society perceives

“poor” is much the same today as it was 100 years ago. In this way, word embeddings can help

us to identify when change happens (or does not happen) in social representations.

   More than any one result, however, these early papers point to the great potential of using

word embeddings to extend the historical reach of research on change in social group

representations, for both implicit (Charlesworth & Banaji, 2019) and explicit measures (e.g.,

Bobo, Charles, Krysan, & Simmons, 2012). Furthermore, by virtue of these longer timespans, the

methods can be used to test the macro-level causes of change. With access to longer historical

periods with archived books, newspapers, government and legal documents, we have access to

data that can cover periods of significant social movements (e.g., women’s movement, Civil

Rights era protests), demographic shifts (e.g., waves of immigration from Europe, Asia, or

Africa), and a plethora of other cultural events (e.g., ecological threats like pandemics, or

introduction of new legislations and policies; Grossman & Varnum, 2015). Mapping out the

trends of historical changes in word embeddings alongside a record of historical events can

provide insights into how macro-level events are interwoven with representations in language.

Interpreting social group representations uncovered with word embeddings


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                            19


       Although word embeddings are increasingly applied throughout the social sciences to

measure group representations, the theoretical interpretations remain open as to what these

findings actually mean within psychology and the social sciences. Debates around the cognitive

plausibility of word embeddings algorithms (i.e., do neural network models approximate the

operations of the brain?) are not our focus here, as they are reviewed elsewhere (Günther et al.,

2019). Instead, here we pose two theoretical questions for the social plausibility and meaning of

group representations uncovered with word embeddings. Specifically, (1) do social group

representations identified in word embeddings capture more implicit or explicit cognitions? And

(2) what, if anything, can be said about the directionality between measures of social biases in

language and measures of social biases in the mind?

       First, perhaps because of the wide adoption of the WEAT (an analogue to the IAT), an

implied assumption in interpreting results from word embeddings tests of social representation is

that they capture automatic, subtle or implicit representations. Indeed, in many ways, because

they are derived from context-based co-occurrences that uncover hidden structures within natural

language, word embeddings appear methodologically analogous to the IAT in providing a

relatively indirect measure of bias. As Bolukbasi and colleagues (2016) write, the biases

“generated from these embeddings spell out the bias implicit in the data on which they were

trained. Hence, word embeddings may serve as a means to extract implicit… associations from a

large text corpus similar to how Implicit Association Tests detect automatic… associations

possessed by people” (p. 3, emphasis added).

       However, a competing perspective is that word embeddings may, at least in part, also

capture explicit representations. The natural language that many word embeddings are trained on

often arise from very deliberate and explicit text (e.g., newspapers, books, TV show transcripts).


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                             20


Thus, the expression of potential social group representations may be controlled by the author or

speaker. Indeed, language itself is often taken to be an explicit measure of cognition – when

participants are asked to provide a verbal self-report of their biases, they are providing an explicit

measure. Similarly, natural language models might be interpreted to reflect explicit measures.

       What might resolve this interpretational ambiguity? Because implicit and explicit

measures are assumed to be differentially susceptible to self-presentation concerns, with implicit

measures less likely to be controlled by self-presentation than explicit measures (Greenwald &

Banaji, 1995, 2017), initial evidence could come from comparing the magnitude of bias across

text sources presumed to activate more versus less self-presentation concerns. For instance,

natural conversations are arguably more spontaneous than written and reviewed materials (e.g.,

books, journal articles, newspapers). Thus, if the word embeddings methods are predominantly

capturing explicit biases that are sensitive to self-presentation concerns, they may be weaker in

books, for example (which are controlled and deliberative, and thus prone to self-presentation),

and stronger in everyday conversations (which are more spontaneous). If, however, word

embeddings are capturing implicit biases they should be equivalent across these text sources.

       Another empirical approach to resolve this question could compare the magnitude of

correlations between (a) bias in word embeddings and bias in explicit measures versus (b) bias in

word embeddings and bias in implicit measures. Both approaches remain open for future

research. With the current evidence, however, it cannot be concluded that word embeddings are

exclusively measures of implicit cognition or cultural representations (or explicit cognition and

representations). In fact, the relationship between implicit and explicit cognition shows that they

are both independent of each other and deeply connected (Cunningham et al., 2001; Nosek &

Smyth, 2007), and thus that both implicit and explicit cognition may be reflected in embeddings.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                            21


       The second question for interpretation is an age-old question on the relationship between

language and thought (Zlatev & Blomberg, 2015; see also Caliskan & Lewis, this volume). In

one direction, it is believed that language itself, whether the structure of the language or the ideas

communicated through that language, fundamentally shape perceptions and biases, a position in

line with a weak form of linguistic relativity (Boroditsky, 2001; Boroditsky et al., 2003;

Casasanto & Boroditsky, 2008). From this perspective, the language of cultural products, as

measured in word embeddings, shape the thoughts and behavior of individuals living in a culture.

The alternative possibility is that language merely reflects existing perceptions and biases present

inside the mind (Pinker, 1994). In this case, group biases in the mind may be acquired through a

combination of linguistic (e.g., explicit teaching and instruction; Charlesworth, Kurdi, & Banaji,

2019) and non-linguistic means (e.g., observing nonverbal behavior; Skinner, Meltzoff, & Olson,

2017; Skinner & Perry, 2019) that, in turn, produce the broader expression of group biases in

language and cultural products.

       In all likelihood, the answer is a complex bidirectional relationship: the language of a

culture shapes individuals’ thought but individuals’ thoughts also influence the language of a

culture. To our knowledge, however, no experiments with word embeddings exist to explore this

relationship. Does increased exposure to biased language (determined based on word

embeddings) lead to increased biased attitudes, stereotypes, or behaviors in an individual or in

society (as might be suggested by findings such as Arendt, 2013; Arendt & Northup, 2015;

Danziger & Ward, 2010)? And/or do increases in biased attitudes, stereotypes, or behaviors lead

to increased production of biased language (determined from word embeddings)? For instance, at

the cultural level, tracking changes over time in attitudes (Charlesworth & Banaji, 2019)

alongside changes over time in the biases uncovered through language (Garg et al., 2018) could


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                            22


identify whether decreases in the attitudes precede decreases in the biases from word

embeddings (or vice versa).

Discovering novel social group representations using word embeddings

       Throughout this chapter we have highlighted numerous future research paths in the social

sciences that can be facilitated by word embeddings, whether examining change in group

representations over unprecedented time scales, identifying variability of such representations

across languages and cultures, or understanding the relationships between biases in language and

the mind. Thus far, however, we have largely constrained our imaginations to examining known

social groups, stereotypes, and attitudes, such as the biases of male-career/female-home. This

approach is typical of much of psychology: the researcher selects, top-down, which topics to test

and which stimuli should represent the categories that are examined. Yet the full potential of a

machine learning method like word embeddings can be realized when we think about bottom-up

discoveries of previously unknown biases, domains, or social groups.

       In essence, the ideal setting for discovering biases is an unsupervised method, without the

interference of a researcher preselecting the number or types of groups or attributes. A first step

was suggested by Swinger and colleagues (2019) who described the process of “unsupervised

bias enumeration” (UBE) using clustering algorithms to identify sets of social groups (i.e.,

clusters based on a list of first names from the Social Security Administration) and sets of

associated attributes (i.e., clusters of the highest frequency non-name words). The UBE

algorithm is able to uncover both well-known and novel associates. For instance, for the cluster

of predominantly Hispanic American names, the top associates in a “food” attribute cluster are

the words [tortillas, salsa, tequila], while an “occupation” cluster reveals [translator, interpreter,

smuggler]. For the cluster of predominantly female names, the “food” cluster reveals [cookbook,


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                              23


baking, baked goods], while an “occupation” cluster reveals [registered nurse, homemaker,

chairwoman]. Importantly, some of these associates (e.g., translator, interpreter) may not have

been identified a priori by researchers; yet discovering such biases may contribute to new

theorizing about how society represents a given social group. That is, we believe that a bottom-

up approach will not only reveal the truth of what a concept is made up of, but can also, by

revealing unpredicted possibilities, provide a new impetus to theory.

       Although the UBE approach shows, in principle, that one can perform a bottom-up

derivation of group and attribute clusters, the algorithm still requires authors to prespecify the

number of group and attribute clusters. New work can aim to develop methods that overcome

even these pre-specification requirements and fully automate the process of bias discovery.

Furthermore, the unsupervised approach will help capture biases towards intersectional groups

with multiple identities (e.g., Black American females, lower-class White Americans) and test

whether these intersectional groups are associated with emergent biases not predicted by either

constituent identity (e.g., by just “White” or “lower-class” alone; Guo & Caliskan, 2020).

Concluding remarks

       Social scientists have long emphasized the central role of language in understanding the

complex ways that society thinks about and perceives various social groups (Durkheim, 1924;

Moscovici, 2000). It is unlikely that these past scholars could have anticipated the opportunities

offered by recent advances in data availability and natural language processing that can be used

to document group representations on an unprecedented scale. As word embeddings have been

increasingly adopted throughout the social sciences, many insights have emerged, including that:

(a) group representations are prevalent and consistent in language across many sources of

language (e.g., books, TV/movies, conversations, Internet); (b) representations nevertheless vary


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                            24


across languages and cultures; and (c) representations can shift meaningfully across time, in

concert with societal changes such as immigration and social protests. The next stage for

researchers is to grapple with what these prevalent and dynamic biases actually mean. Further

research is needed to clarify interpretations regarding the implicit (versus explicit) nature of the

biases uncovered by word embeddings, as well as the relationship between such biases in

language and biases measured from the mind. For now, what stands out more than anything is

the vast potential offered by word embeddings to contribute a new wave of research in the social

sciences documenting how social groups are embedded in the fundamentally human act of

language.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                         25


                                           References

Ames, D. R. (2004). Strategies for social inference: A similarity contingency model of projection

     and stereotyping in attribute prevalence estimates. Journal of Personality and Social

     Psychology, 87(5), 573–585. https://doi.org/10.1037/0022-3514.87.5.573

Arendt, F. (2013). Dose-dependent media priming effects of stereotypic newspaper articles on

     implicit and explicit stereotypes. Journal of Communication, 63(5), 830–851.

     https://doi.org/10.1111/jcom.12056

Arendt, F., & Northup, T. (2015). Effects of long-term exposure to news stereotypes on implicit

     and explicit attitudes. International Journal of Communication, 9(1), 2370–2390.

     http://ijoc.org.

Ash, E., Chen, D. L., & Ornaghi, A. (2020). Stereotypes in High-Stakes Decisions: Evidence

     from U.S. Circuit Courts.

     https://warwick.ac.uk/fac/soc/economics/research/centres/cage/manage/publications/462-

     2020_ornaghi.pdf

Baron, A. S., & Banaji, M. R. (2006). The development of implicit attitudes: Evidence of race

     evaluations from ages 6 and 10 and adulthood. Psychological Science, 17(1), 53–58.

     https://doi.org/10.1111/j.1467-9280.2005.01664.x

Bergsieker, H. B., Leslie, L. M., Constantine, V. S., & Fiske, S. T. (2012). Stereotyping by

     omission: Eliminate the negative, accentuate the positive. Journal of Personality and Social

     Psychology, 102(6), 1214–1238. https://doi.org/10.1037/a0027717

Beukeboom, C. J., & Burgers, C. (2019). How Stereotypes Are Shared Through Language: A

     Review and Introduction of the Social Categories and Stereotypes Communication (SCSC)

     Framework. Review of Communication Research, 7, 1–37.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                        26


     https://doi.org/10.12840/issn.2255-4165.017

Bian, L., Leslie, S.-J., & Cimpian, A. (2017). Gender stereotypes about intellectual ability

     emerge early and influence children’s interests. Science, 355(6323), 389–391.

     https://doi.org/10.1126/science.aah6524

Bian, L., Leslie, S. J., Murphy, M. C., & Cimpian, A. (2018). Messages about brilliance

     undermine women’s interest in educational and professional opportunities. Journal of

     Experimental Social Psychology, 76, 404–420. https://doi.org/10.1016/j.jesp.2017.11.006

Bobo, L. D., Charles, C. Z., Krysan, M., & Simmons, A. D. (2012). The Real Record on Racial

     Attitudes. In P. V. Marsden (Ed.), Social Trends in American Life: Findings from the

     General Social Survey since 1972 (pp. 38–83). Princeton University Press.

Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). Enriching Word Vectors with

     Subword Information. Transactions of the Association for Computational Linguistics, 5,

     135–146. https://doi.org/10.1162/tacl_a_00051

Bolukbasi, T., Chang, K. W., Zou, J., Saligrama, V., & Kalai, A. (2016). Man is to computer

     programmer as woman is to homemaker? Debiasing word embeddings. Advances in Neural

     Information Processing Systems, 4356–4364. http://arxiv.org/abs/1607.06520

Boroditsky, L. (2001). Does Language Shape Thought?: Mandarin and English Speakers’

     Conceptions of Time. Cognitive Psychology, 43(1), 1–22.

     https://doi.org/10.1006/cogp.2001.0748

Boroditsky, L., Schmidt, L. A., & Phillips, W. (2003). Sex, Syntax, and Semantics. In D.

     Gentner & S. Goldin-Meadow (Eds.), Language in Mind: Advances in the Study of

     Language and Thought (pp. 61–80). MIT Press. https://doi.org/10.1353/lan.2006.0068

Boyd, R. L., & Schwartz, H. A. (n.d.). Natural Language Analysis and the Psychology of Verbal


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                           27


     Behavior: The Past, Present, and Future States of the Field. Journal of Language and Social

     Psychology.

Brunet, M. E., Alkalay-Houlihan, C., Anderson, A., & Zemel, R. (2019). Understanding the

     origins of bias in word embeddings. 36th International Conference on Machine Learning,

     ICML 2019, 2019-June, 1275–1294.

Caliskan, A., Bryson, J. J., & Narayanan, A. (2016). Semantics derived automatically from

     language corpora necessarily contain human biases. Science, 356(6334), 183–186.

     https://doi.org/10.1126/science.aal4230

Casasanto, D., & Boroditsky, L. (2008). Time in the mind: Using space to think about time.

     Cognition, 106(2), 579–593. https://doi.org/10.1016/j.cognition.2007.03.004

Charlesworth, T. E. S., & Banaji, M. R. (2019). Patterns of Implicit and Explicit Attitudes: I.

     Long-Term Change and Stability From 2007 to 2016. Psychological Science, 30(2), 174–

     192. https://doi.org/10.1177/0956797618813087

Charlesworth, T. E. S., Kurdi, B., & Banaji, M. R. (2019). Children’s implicit attitude

     acquisition: Evaluative statements succeed, repeated pairings fail. Developmental Science.

     https://doi.org/10.1111/desc.12911

Charlesworth, T. E. S., Yang, V., Mann, T. C., Kurdi, B., & Banaji, M. R. (n.d.). Gender

     Stereotypes in Natural Language: Word embeddings show robust consistency across child

     and adult language corpora of 65+ million words. Psychological Science.

Croft, A., Schmader, T., Block, K., & Baron, A. S. (2014). The Second Shift Reflected in the

     Second Generation: Do Parents’ Gender Roles at Home Predict Children’s Aspirations?

     Psychological Science, 25(7), 1418–1428. https://doi.org/10.1177/0956797614533968

Cunningham, W. A., Preacher, K. J., & Banaji, M. R. (2001). Implicit Attitude Measures:


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                       28


    Consistency, Stability, and Convergent Validity. Psychological Science, 12(2), 163–170.

    https://doi.org/10.1111/1467-9280.00328

Danziger, S., & Ward, R. (2010). Language Changes Implicit Associations Between Ethnic

    Groups and Evaluation in Bilinguals. Psychological Science, 21(6), 799–800.

    https://doi.org/10.1177/0956797610371344

Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990). Indexing

    by Latent Semantic Analysis. Journal of the American Society for Information Science,

    41(6), 391–407. https://doi.org/https://doi.org/10.1002/(SICI)1097-

    4571(199009)41:6<391::AID- ASI1>3.0.CO;2-9

DeFranza, D., Mishra, H., & Mishra, A. (2020). How Language Shapes Prejudice Against

    Women: An Examination Across 45 World Languages. Journal of Personality and Social

    Psychology. https://doi.org/10.1037/pspa0000188

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of Deep

    Bidirectional Transformers for Language Understanding. Proceedings of North American

    Chapter of the Association for Computational Linguistics-Human Language Technologies

    2019, 4171–4186. http://arxiv.org/abs/1810.04805

Duguid, M. M., & Thomas-Hunt, M. C. (2015). Condoning stereotyping? How awareness of

    stereotyping prevalence impacts expression of stereotypes. Journal of Applied Psychology,

    100(2), 343–359. https://doi.org/10.1037/a0037908

Durkheim, E. (1924). Sociologie et philosophie [Sociology and philosophy]. Felix Alcan.

Eagly, A. H., & Mladinic, A. (1989). Gender Stereotypes and Attitudes Toward Women and

    Men. Personality and Social Psychology Bulletin, 15(4), 543–558.

    https://doi.org/10.1177/0146167289154008


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                             29


Eagly, A. H., & Mladinic, A. (1994). Are people prejudiced against women? some answers from

     research on attitudes, gender stereotypes, and judgments of competence. European Review

     of Social Psychology, 5(1), 1–35. https://doi.org/10.1080/14792779543000002

Firth, J. R. (1957). Papers in linguistics, 1934-1951. Oxford University Press.

Garg, N., Schiebinger, L., Jurafsky, D., & Zou, J. (2018). Word embeddings quantify 100 years

     of gender and ethnic stereotypes. Proceedings of the National Academy of Sciences of the

     United States of America, 115(16), E3635–E3644. https://doi.org/10.1073/pnas.1720347115

Greenwald, A. G., & Banaji, M. R. (1995). Implicit Social Cognition: Attitudes, Self-Esteem,

     and Stereotypes. Psychological Review, 102(1), 4–27. https://doi.org/10.1037/0033-

     295X.102.1.4

Greenwald, A. G., & Banaji, M. R. (2017). The implicit revolution: Reconceiving the relation

     between conscious and unconscious. American Psychologist, 72(9), 861–871.

     https://doi.org/10.1037/amp0000238

Greenwald, A. G., McGhee, D. E., & Schwartz, J. L. K. (1998). Measuring individual

     differences in implicit cognition: The implicit association test. Journal of Personality and

     Social Psychology, 74(6), 1464–1480. https://doi.org/10.1037/0022-3514.74.6.1464

Günther, F., Rinaldi, L., & Marelli, M. (2019). Vector-space models of semantic representation

     from a cognitive perspective: A discussion of common misconceptions. Perspectives on

     Psychological Science. https://doi.org/10.1177/1745691619861372

Guo, W., & Caliskan, A. (2020). Detecting Emergent Intersectional Biases: Contextualized

     Word Embeddings Contain a Distribution of Human-like Biases. Arxiv.

     http://arxiv.org/abs/2006.03955

Hamilton, W. L., Leskovec, J., & Jurafsky, D. (2016). Diachronic word embeddings reveal


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                           30


     statistical laws of semantic change. 54th Annual Meeting of the Association for

     Computational Linguistics, ACL 2016 - Long Papers, 3, 1489–1501.

     https://doi.org/10.18653/v1/p16-1141

Jones, J. J., Amin, M. R., Kim, J., & Skiena, S. (2020). Stereotypical gender associations in

     language have decreased over time. Sociological Science, 7, 1–35.

     https://doi.org/10.15195/v7.a1

Kozlowski, A. C., Taddy, M., & Evans, J. A. (2019). The Geometry of Culture: Analyzing the

     Meanings of Class through Word Embeddings. American Sociological Review, 84(5), 905–

     949. https://doi.org/10.1177/0003122419877135

Kurita, K., Vyas, N., Pareek, A., Black, A. W., & Tsvetkov, Y. (2019). Measuring Bias in

     Contextualized Word Representations. 166–172. https://doi.org/10.18653/v1/w19-3823

Lauscher, A., & Glavas, G. (2019). Are We Consistently Biased? Multidimensional Analysis of

     Biases in Distributional Word Vectors. Proceedings of the Eighth Joint Conference on

     Lexical and Computational Semantics, 85–91. https://www.aclweb.org/anthology/S19-1010

Lewis, M., & Lupyan, G. (2020). Gender stereotypes are reflected in the distributional structure

     of 25 languages. Nature Human Behaviour. https://doi.org/10.1038/s41562-020-0918-6

Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M., Zettlemoyer, L.,

     Stoyanov, V., & Allen, P. G. (2019). RoBERTa: A Robustly Optimized BERT Pretraining

     Approach. https://arxiv.org/abs/1907.11692

Manzini, T., Lim, Y. C., Tsvetkov, Y., & Black, A. W. (2019). Black is to Criminal as Caucasian

     is to Police: Detecting and Removing Multiclass Bias in Word Embeddings. Proceedings of

     NAACL-HLT, 615–621.

Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient Estimation of Word


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                           31


     Representations in Vector Space. ArXiv Preprint. http://arxiv.org/abs/1301.3781

Mikolov, T., Grave, E., Bojanowski, P., Puhrsch, C., & Joulin, A. (2018). Advances in Pre-

     Training Distributed Word Representations. Proceedings of the International Conference

     Language Resources and Evaluation. http://arxiv.org/abs/1712.09405

Mikolov, T., Sutskever, I., Chen, K., Corrado, G., & Dean, J. (2013). Distributed Representations

     of Words and Phrases and their Compositionality. ArXiv Preprint.

     http://arxiv.org/abs/1310.4546

Moscovici, S. (2000). Social representations : explorations in social psychology. Polity Press.

Nosek, B. A., Banaji, M. R., & Greenwald, A. G. (2002). Math=Male, Me=Female, Therefore

     Math Does not Equal Me. Journal of Personality and Social Psychology, 83(1), 44–59.

     https://doi.org/10.1037/0022-3514.83.1.44

Nosek, B. A., & Smyth, F. L. (2007). A multitrait-multimethod validation of the implicit

     association test: Implicit and explicit attitudes are related but distinct constructs.

     Experimental Psychology, 54(1), 14–29. https://doi.org/10.1027/1618-3169.54.1.14

O’Neil, C. (2017). Weapons of Math Destruction: How Big Data Increases Inequality and

     Threatens Democracy. Crown Books.

Payne, B. K., Vuletich, H. A., & Lundberg, K. B. (2017). The Bias of Crowds: How Implicit

     Bias Bridges Personal and Systemic Prejudice. Psychological Inquiry, 28(4), 233–248.

     https://doi.org/10.1080/1047840X.2017.1335568

Pennington, J., Socher, R., & Manning, C. (2014). Glove: Global Vectors for Word

     Representation. Proceedings of the 2014 Conference on Empirical Methods in Natural

     Language Processing (EMNLP), 1532–1543. https://doi.org/10.3115/v1/D14-1162

Pinker, S. (1994). The Language Instinct. Harper Perennial Modern.


ATTITUDES AND STEREOTYPES IN EMBEDDINGS                                                         32


Sidanius, J., & Pratto, F. (1999). Social dominance: An intergroup theory of social hierarchy and

    oppression. Cambridge University Press. https://doi.org/10.2307/2655372

Skinner, A. L., Meltzoff, A. N., & Olson, K. R. (2017). “Catching” Social Bias. Psychological

    Science, 28(2), 216–224. https://doi.org/10.1177/0956797616678930

Skinner, A. L., & Perry, S. (2019). Are Attitudes Contagious? Exposure to Biased Nonverbal

    Signals Can Create Novel Social Attitudes. Personality and Social Psychology Bulletin,

    014616721986261. https://doi.org/10.1177/0146167219862616

Storage, D., Charlesworth, T. E. S., Banaji, M. R., & Cimpian, A. (2020). Adults and children

    implicitly associate brilliance with men more than women. Journal of Experimental Social

    Psychology. https://doi.org/10.1016/j.jesp.2020.104020

U.S. Bureau of Labor Statistics. (2019). American time use survey - 2018 results.

    www.bls.gov/tus/data.htm.

Xu, H., Zhang, Z., Wu, L., & Wang, C. J. (2019). The Cinderella complex: Word embeddings

    reveal gender stereotypes in movies and books. PLoS ONE, 14(11).

    https://doi.org/10.1371/journal.pone.0225385

Zlatev, J., & Blomberg, J. (2015). Language may indeed influence thought. Frontiers in

    Psychology, 6(OCT), 31. https://doi.org/10.3389/fpsyg.2015.01631

Zou, L. X., & Cheryan, S. (2017). Two Axes of Subordination: A New Model of Racial Position.

    Journal of Personality and Social Psychology. https://doi.org/10.1037/pspa0000080.supp
