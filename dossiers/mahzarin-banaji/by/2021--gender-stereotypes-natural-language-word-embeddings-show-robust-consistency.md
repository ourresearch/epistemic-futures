---
title: "Gender Stereotypes in Natural Language: Word Embeddings Show Robust Consistency Across Child and Adult Language Corpora of More Than 65 Million Words"
person: mahzarin-banaji
section: by
type: journal-article
year: 2021
date: 2021-01-05
venue: "Psychological Science"
authors: "Tessa E. S. Charlesworth; Victor Yang; Thomas C. Mann; Benedek Kurdi; Mahzarin R. Banaji"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/2021_Charlesworth_PS.pdf
doi: https://doi.org/10.1177/0956797620963619
openalex_id: https://openalex.org/W3045825772
cited_by_count: 178
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard site, extracted with pdftotext -layout. Title-overlap check 0.44."
---

# Gender Stereotypes in Natural Language: Word Embeddings Show Robust Consistency Across Child and Adult Language Corpora of More Than 65 Million Words

## Full text

963619
research-article2021
                       PSSXXX10.1177/0956797620963619Charlesworth et al.Gender in Language


                                                                                                                                                                 ASSOCIATION FOR
                               Research Article                                                                                                   PSYCHOLOGICAL SCIENCE
                                                                                                                                                  Psychological Science

                               Gender Stereotypes in Natural Language:                                                                            2021, Vol. 32(2) 218­–240
                                                                                                                                                  © The Author(s) 2021
                                                                                                                                                  Article reuse guidelines:
                               Word Embeddings Show Robust                                                                                        sagepub.com/journals-permissions
                                                                                                                                                  DOI:    10.1177/0956797620963619
                                                                                                                                                  https://doi.org/10.1177/0956797620963619

                               Consistency Across Child and Adult                                                                                 www.psychologicalscience.org/PS


                               Language Corpora of More Than
                               65 Million Words

                               Tessa E. S. Charlesworth1 , Victor Yang1, Thomas C. Mann1,
                               Benedek Kurdi1,2, and Mahzarin R. Banaji1
                               1
                                     Department of Psychology, Harvard University, and 2Department of Psychology, Yale University


                               Abstract
                               Stereotypes are associations between social groups and semantic attributes that are widely shared within societies.
                               The spoken and written language of a society affords a unique way to measure the magnitude and prevalence of
                               these widely shared collective representations. Here, we used word embeddings to systematically quantify gender
                               stereotypes in language corpora that are unprecedented in size (65+ million words) and scope (child and adult
                               conversations, books, movies, TV). Across corpora, gender stereotypes emerged consistently and robustly for both
                               theoretically selected stereotypes (e.g., work–home) and comprehensive lists of more than 600 personality traits and
                               more than 300 occupations. Despite underlying differences across language corpora (e.g., time periods, formats, age
                               groups), results revealed the pervasiveness of gender stereotypes in every corpus. Using gender stereotypes as the
                               focal issue, we unite 19th-century theories of collective representations and 21st-century evidence on implicit social
                               cognition to understand the subtle yet persistent presence of collective representations in language.

                               Keywords
                               collective representations, gender stereotypes, machine learning, natural-language processing, word embeddings,
                               open data, open materials

                               Received 10/21/19; Revision accepted 7/22/20


                               Psychological analyses of social-group stereotypes have                       human thought. Durkheim (1898/2009) and the social
                               most commonly asked participants to report on their                           scientists who followed him argued that the primary
                               own or other people’s beliefs about social groups (e.g.,                      place to seek such information is in the language of
                               indicate the degree to which men–women are associ-                            societal products (e.g., books, conversations, TV, movies,
                               ated with qualities of agency–communion). Across 50                           the Internet). Although Durkheim’s view was ahead of
                               years of research, variations of such questions have                          its time, nobody could have conceived of the possibilities
                               been the primary source of evidence about the pres-                           presented by today’s computational approaches that rely
                               ence and strength of stereotypes (Ellemers, 2018). Such                       on machine learning to analyze billions of words from
                               methods are valuable indicators of individual, subjec-                        the sociosphere of the Internet (e.g., Pennington, Socher,
                               tive reports of stereotypes, but they cannot reveal the                       & Manning, 2014, analyzed 840 billion word tokens).
                               presence and potency of stereotypes as collective rep-                            It is within the natural language of human conversa-
                               resentations (Durkheim, 1898/2009; Moscovici, 1988),                          tions, books, and audiovisual media that the implicit
                               the term used to refer to societal-level systems of mean-
                               ing that pervade everyday social life.                                        Corresponding Author:
                                   To learn about the presence of stereotypes in social                      Tessa E. S. Charlesworth, Harvard University, Department of Psychology
                               life, we must examine more natural expressions of                             E-mail: tet371@g.harvard.edu


Gender in Language                                                                                                    219

presence and potency of group stereotypes can be mea-
sured. Take, for example, innocuous child-directed              Statement of Relevance
statements such as “get mommy from the kitchen” or
“daddy is still at the office.” Such sentences do more          Language permeates every aspect of our daily lives
than describe the physical locations or roles of mothers        through conversations, books, TV, movies, and the
and fathers; they also reinforce attributes associated          Internet. A key role of language is to communicate
with those roles. That is, although the proximity               social information, including stereotypes about
between the words mommy–kitchen or daddy–office                 social groups (e.g., which groups are delicate vs.
can describe the reality of gender-based roles, it also         strong or fast vs. slow). It is an intriguing aspect of
creates and perpetuates perceptions of the internal             social-group stereotypes that they are often hidden
traits of individuals who occupy such roles (Eagly &            in plain sight; they are right there but rarely stated
Wood, 2012; Koenig & Eagly, 2014). When consistently            explicitly. In this research, we applied methods from
expressed in spoken and written language, such per-             natural-language processing (word embeddings) to
ceptions can become collective “truths” that shape how          systematically uncover and quantify the strength
children and adults think about and interact with the           and prevalence of subtle gender stereotypes across
social world (e.g., Gaucher, Friesen, & Kay, 2011; Rhodes,      child and adult language (conversations, books, TV,
Leslie, Yee, & Saunders, 2019).                                 movies). Despite many differences across corpora
   But just how pervasive are stereotypes in natural            (e.g., time periods, formats, age groups), gender
language? Is there consistency even across language             stereotypes were surprisingly consistent and robust
that varies in format (TV, movies, books, conversations),       for widely studied stereotypes and lists of more
age groups, and time periods? To answer this question,          than 600 traits and more than 300 occupations.
we combined an unprecedented database of language               The results underscore the pervasive and even
corpora (65+ million words from seven corpora of child          obligatory role of language in sustaining stereotypes
and adult text) with advances in natural-language pro-          in mind and society.
cessing (word embeddings) to quantify the prevalence
of gender stereotypes in language.
   We investigated language corpora that vary in theo-        explicit measures, both elderly and young respondents
retically meaningful ways, including (a) format, from         show consistent, anti-elderly/pro-young attitudes on
ordinary conversations to books to audiovisual media;         implicit measures (Nosek et al., 2007). The only expla-
(b) time, from historical books to conversations of the       nation is that implicit measures are particularly affected
late 20th century to contemporary TV and movies; and          by societal-level representations of stigmatized groups,
(c) age groups, from child to adult audiences and speak-      even overriding in-group preferences. Similarly, mea-
ers. We also investigated gender stereotypes across           suring the hidden, indirect structures of language
domains, ranging from well-studied associations (e.g.,        (through word-embedding techniques elaborated
women–home/men–work) to associations with more                below) is uniquely poised to reveal the collective ste-
than 600 personality traits and more than 300 occupa-         reotypes embedded in a society.
tions. Given evidence that gender stereotypes vary in
magnitude across age groups (e.g., Miller, Nolla, Eagly,
& Uttal, 2018), time (e.g., Eagly, Nater, Miller, Kaufmann,
                                                              The Present Research
& Sczesny, 2020), and domains (Martin & Ruble, 2010),         With new data and methods, we have the opportunity
the diversity of language sources and topics allows a         to test whether large-scale natural language (from
rigorous test of the pervasiveness and potency of gen-        everyday conversations to formal writing) confirms the
der stereotypes.                                              views from 19th-century theories and 21st-century
   Since Durkheim, scholars have argued that collective       research in implicit social cognition. If the present
stereotypes are maintained through language that is           analyses show weak or inconsistent evidence of gender
subtle or indirect, often even more so than language          stereotypes (e.g., appearing only in some corpora, age
that is explicit and direct (Moscovici, 2000). Echoes of      groups, or time periods), we would be led to a limited
such theories are heard in modern perspectives of             view of gender stereotypes in language. If, on the other
implicit social cognition, which posit that indirectly        hand, evidence of gender stereotypes is strong across
assessed (implicit) stereotypes reflect and reveal col-       sources, we would conclude that language is a potent
lective, societal-level phenomena (Payne, Vuletich, &         carrier of gender stereotypes and that it has a role in
Lundberg, 2017) more so than directly assessed                the propagation of collective representations.
(explicit) measures. For instance, although elderly and          Across three studies, we examined both well-studied
young respondents show in-group preferences on                stereotypes (e.g., women–home/men–work; Study 1)


220                                                                                                   Charlesworth et al.

and comprehensive lists of traits (Study 2) and occupations   We direct readers interested in the specifics to the Sup-
(Study 3) in diverse natural language of child-produced,      plemental Material available online.
child-directed, adult-produced, and adult-directed text.
To identify stereotypes on this massive scale, we used        Step 1: collect text data. Child-produced and child-directed
word embeddings (see the Method section) to quantify          corpora were selected because they are, to our knowl-
the association between groups (male–female) and attri-       edge, the largest corpora of natural child-produced and
butes (e.g., home–work; Caliskan, Bryson, & Narayanan,        child-directed language; the three adult corpora were
2017). The idea underlying word embeddings is that            subsequently chosen to best approximate the child cor-
patterns of word co-occurrences are modeled (with             pora in data size, time period of data collection, breadth
machine-learning algorithms) to quantify the semantic         of topics, and linguistic style (e.g., dyadic speech, movie
relationships between words (e.g., the semantic rela-         transcripts, or book text).
tionship between the words women and home vs. men
and home). The method has already shown feasibility              Child-produced and child-directed speech. Text of
in documenting social-group representations, including        child-produced and child-directed speech (from parents
gender biases (e.g., Caliskan et al., 2017; DeFranza,         and caregivers) was obtained from transcripts of English-
Mishra, & Mishra, 2020; Garg, Schiebinger, Jurafsky, &        language dyadic parent–child conversations documented
Zou, 2018; Lewis & Lupyan, 2020). However, such work          through the Child Language Data Exchange System lan-
has exclusively focused on adult-produced corpora and         guage corpus; most transcripts were collected between
without direct comparisons across language sources            1970 and 1990 (MacWhinney, 2000). Although these dates
(e.g., conversations vs. books). The current project thus     are historical (and therefore cannot provide insights into
offers the first test of consistency of gender stereotypes    contemporary speech), the corpus remains an impor-
across child and adult natural language to quantify           tant product of study because (a) regardless of year, it
whether stereotypes are indeed widely shared collec-          can reveal whether children and adults from the same
tive representations.                                         conversations are similarly communicating collective
                                                              representations; (b) the corpus remains widely used to
                                                              understand children’s and adults’ language; and (c) it is
Study 1: Well-Studied Gender Stereotypes                      the largest known corpus of child speech. The prepared
Study 1 was designed to investigate four well-studied         corpus consists of 6,518 conversations between children
gender associations: male–female with semantic attri-         (age: M = 2.92 years, range = 0–12 years) and their care-
butes of home–work, arts–science, and math–reading            givers, yielding 8,429,128 word tokens (i.e., individual
and evaluative attributes of good–bad. Study 1 tested         words in the corpus, regardless of how many times the
whether collective representations of gender exist in         word is repeated).
large-scale natural language, at consistent magnitudes           Child-produced speech (i.e., child speaking to par-
across conversations, books, TV, and movies, from mul-        ent) and child-directed speech (i.e., parent speaking to
tiple decades and from both adults and children.              child) were assessed independently by dividing the
                                                              corpus according to whether the speaker was a child
                                                              (indexed by a “CHI” tag in the corpus) or parent
Method                                                        (indexed by a “MOT” or “FAT” tag, for mother or father,
Below, we describe the eight steps in our method pro-         respectively). We therefore obtained two independent
cedure: Step 1, collect text data; Step 2, clean text data;   corpora with (a) utterances produced by child speakers
Step 3, select the attributes to test (e.g., home–work,       (2,601,432 word tokens) and (b) utterances directed
arts–science); Step 4, select word stimuli to represent       toward children by parents and caregivers (5,827,696
categories and attributes; Step 5, generate word embed-       word tokens).
dings from text data using machine-learning algorithms;
Step 6, perform the Word-Embedding Association Test              Child-directed books. Child-directed book text was
(WEAT) and Single-Category WEAT (SC-WEAT) and                 retrieved from a subsample of English-language children’s
calculate significance; Step 7, calculate meta-analytic       books obtained from Project Gutenberg, an open-source
estimates and meta-regressions to compare WEAT                database of books (https://www.gutenberg.org/). This
scores across age groups, sources, and domains; and           subsample of children’s books was previously extracted
Step 8, perform validation tests, including replicating       from Project Gutenberg for machine-learning tests of lan-
the results with additional large-scale corpora and           guage comprehension (Hill, Bordes, Chopra, & Weston,
word-embedding algorithms. Our focus in this section          2016). The current corpus consists of 98 books, published
is to provide a concise and accessible introduction to        between 1820 (The Legend of Sleepy Hollow by Washington
working with massive text data and word embeddings.           Irving) and 1922 (Blacky the Crow by Thornton Burgess),


Gender in Language                                                                                                 221

and consists of 4,583,629 word tokens. Although these        Family) and present day (e.g., CSI, Breaking Bad). Thus,
books are historical, we argue that they remain impor-       the adult-directed audiovisual-media corpus matches the
tant societal-level products because they reflect classic    child-directed TV shows and movies corpus in time
texts that continue to be read by (and to) children, and     period (i.e., relatively more contemporary) and format
they provide a comparison point against relatively more      (i.e., online transcripts provided by volunteer transcrib-
contemporary speech and audiovisual media to investi-        ers). As with the child-directed audiovisual corpus, the
gate possible influences of time period on the strength of   corpus of adult-directed audiovisual transcripts was cre-
gender stereotypes in language.                              ated for this project and has been made available to other
                                                             researchers at https://osf.io/kqux5/. The corpus consists
   Child-directed audiovisual media. Transcripts from        of 2,056,384 word tokens.
child-directed audiovisual media were retrieved from
online transcripts, transcribed by volunteers, of English-   Step 2: clean text data. Complete details on cleaning
language Disney movies, PBS Kids TV shows, and Nick-         procedures for each corpus, including reproducible code
elodeon TV shows, airing between approximately 1938          and data, are available at OSF (https://osf.io/kqux5/) and
(Disney’s Snow White and the Seven Dwarfs) and the           described in the Supplemental Material. In brief, cleaning
present day (e.g., Disney’s 2017 remake of Beauty and        proceeded in two steps. First, all punctuation, meta-data
the Beast). The corpus of transcripts was created for this   (e.g., speaker gender, character name), and linguistic
project and has been made available to other research-       markings (e.g., notes about a speaker’s tone) were
ers at the project’s OSF page (https://osf.io/kqux5/). The   removed from the text. Second, all words were “lemma-
corpus consists of 1,078 movies, 4,309 TV episodes, and      tized,” meaning that words were changed from any vari-
6,747,208 word tokens.                                       ant and inflection forms to their root form. For example,
                                                             the words running and ran would be changed to the
   Adult-produced speech. Adult-produced speech tran-        root form of run (for further details, see the glossary in
scripts were retrieved from the Switchboard-1 Telephone      the Supplemental Material). Reducing word variants to
Speech Corpus (Godfrey & Holliman, 1993), a database         root forms increases the number of occurrences of each
of English-language dyadic telephone conversations,          root word to improve the reliable computation of word
recorded in 1990 and 1991, between 543 adult speak-          embeddings (see below). In this case, lemmatization is
ers (ages 17–68 years) on a set of 70 randomly selected      particularly helpful because the target corpora are
topics. This corpus was chosen because it best approxi-      smaller than other natural-language corpora, such as the
mated the size and time period of the child-produced         Common Crawl corpus (which we use for validation as
and child-directed speech corpora (see above). The           described below) with more than 600 billion word
adult-produced speech corpus consists of approximately       tokens (Mikolov, Grave, Bojanowski, Puhrsch, & Joulin,
2,400 conversations and 3,063,280 word tokens.               2018).

   Adult-directed books. Texts of adult-directed books       Step 3: select categories and attributes to test. In
were obtained from a randomly selected subsample of          Study 1, we aimed to provide a proof-of-concept test on
1,000 English-language books on Project Gutenberg.           whether the word-embedding method can replicate well-
The subsample was determined using a random-number           studied stereotypes in natural language. Only with such
generator and including the text of the book indexed         empirical grounding can we confidently extend the
by each random number. The majority of texts in Proj-        method to study consistency across more diverse stereo-
ect Gutenberg were published before 1923, matching           type topics and language corpora. Thus, in Study 1, we
the time period for children’s books. Again, although        focused on gender stereotypes that have been robustly
these books are historical, they nevertheless continue to    documented on both explicit and implicit measures and
provide common cultural knowledge as well as a com-          with both adults and children. Specifically, we examined
parison point with more contemporary sources. The pre-       the stereotypes of female–arts/male–science (for a review,
pared adult-directed books corpus consists of 40,252,700     see Charlesworth & Banaji, 2019), female–reading/male–
word tokens.                                                 math (e.g., Cvencek, Meltzoff, & Greenwald, 2011), and
                                                             female–home/male–career (e.g., Croft, Schmader, Block,
  Adult-directed audiovisual media. Transcripts of           & Baron, 2014) and the attitude of female–good/male–
adult-directed audiovisual media were retrieved from         bad (e.g., Dunham, Baron, & Banaji, 2016).
online transcripts, transcribed by volunteers, of popular       Although all four associations have been robustly
English-language movies and TV shows for adult audi-         documented, two of these associations warrant further
ences across numerous broadcasting stations and pro-         discussion. First, the association of women–home/men–
duction houses. The movies and TV shows aired between        work may seem to challenge current evidence that,
approximately the 1960s (e.g., Doctor Who, The Addams        worldwide, approximately half of all women (52%)


222                                                                                                             Charlesworth et al.

 Table 1. Word Stimuli Used to Represent Each Category and Attribute (Study 1)

 Category                                                         Word stimuli
 Female       she, her, mommy, mom, girl, mother, lady, sister, mama, momma, sis, grandma, herself
 Male         he, his, daddy, dad, boy, father, guy, brother, dada, papa, bro, grandpa, himself
 Good         happiness, happy, fun, fantastic, lovable, magical, delight, joy, relaxing, honest, excited, laughter, lover, cheerful
 Bad          torture, murder, abuse, wreck, die, disease, disaster, mourning, virus, killer, nightmare, stress, kill, death
 Home         baby, house, home, wedding, kid, family, marry
 Work         work, office, job, business, trade, activity, act, money
 Art          art, dance, dancing, sing, singing, paint, painting, song, draw, drawing
 Science      science, scientist, chemistry, physic, engineer, space, spaceship, astronaut, chemical, microscope
 Reading      book, read, write, story, word, writing, reading, tale
 Math         puzzle, number, count, math, counting, calculator, subtraction, addition


participate in the labor force (67% in the United States;          of interest with both precision (i.e., low variance) and
2019 estimates from The World Bank, 2020). Thus,                   comprehensiveness (i.e., no obvious exclusions). This
women might be expected to be associated with the                  concern is also present when selecting the word stimuli
attribute work. However, the stereotype of women–                  to represent a given category or attribute in a word-
home/men–work reflects the relative associations of                embedding approach (e.g., selecting the words to repre-
women (vs. men) with work (vs. home). Thus, because                sent female). Thus, to select word stimuli, we aimed to
men are more likely to participate in the labor force              balance precision, comprehensiveness, and frequency of
than women (75% of men worldwide and 68% of men                    word occurrence to ensure that each category or attribute
in the United States), the relative association of men–            was accurately represented. Specifically, to select word
work versus women–work will favor men–work. Addi-                  stimuli, we began with the stimuli lists from Caliskan and
tionally, because women are more likely to take on                 colleagues (2017). If the stereotype was not tested in that
household responsibilities and more likely to partici-             study, we used the stimuli list from online Implicit Asso-
pate in caregiving occupations even within the work-               ciation Tests (IATs; http://implicit.harvard.edu). Next, we
force (U.S. Bureau of Labor Statistics, 2019), the relative        examined the frequency of these words in the child-
association of women–home versus men–home will                     produced speech corpus (the corpus least likely to include
favor women–home. Likely for these reasons, the                    complex words). We retained those words that appeared
women–home/men–work stereotype has been widely                     in the child-produced speech corpus. Finally, we expanded
observed with typical psychological measures from                  the stimuli list by adding semantically related words
both children and adults (Croft et al., 2014; Nosek et al.,        (generated by the researchers) that were also present in
2007) and is therefore also expected across the natural            the child-produced speech corpus. All final stimuli are
language of children and adults.                                   reported in Table 1. Notably, we also performed a supple-
   Second, the female–good/male–bad association may                mentary analysis to test the robustness of the results when
appear counterintuitive because higher status groups               using other (longer) word stimuli lists, obtained from a
(in this case, men) are usually associated with “good”             more recent application of the WEAT (DeFranza et al.,
attributes. Nevertheless, psychologists have long docu-            2020). All major conclusions held regardless of the choice
mented a counterintuitive “women are wonderful”                    of gender stimuli (see the Supplemental Material).
effect (Eagly & Mladinic, 1994). Indeed, contemporary
data from both implicit and explicit measures reveal               Step 5: create word-embedding vectors. To understand
consistent evidence for a female–good/male–bad asso-               how word embeddings are created, it is useful to begin by
ciation among both children and adults (Dunham et al.,             imagining a “cloud” that represents all semantic meaning
2016). In sum, previous research would predict that all            (formally, a high-dimensional semantic space). Each word
four gender associations should be present, at least in            in our language exists somewhere in this cloud of semantic
adult language corpora. Whether the gender associa-                meaning. To situate each word within this cloud, we can
tions are also observed at consistent magnitudes across            represent each word by a vector (a line that points in a spe-
diverse child and adult corpora is the focus of the pres-          cific direction). The goal of these vector representations is to
ent study.                                                         represent words that are close in meaning (e.g., mother and
                                                                   girl) with vectors that point in similar directions and to rep-
Step 4: select word stimuli to represent categories                resent words that are far in meaning (e.g., mother and cac-
and attributes. As with any psychological experiment,              tus) with vectors that point in different directions. Projecting
a primary concern is how to best represent the construct           down into two-dimensional space, this would essentially


Gender in Language                                                                                                    223

mean that words close in meaning have similar (x, y) coor-      2019) are not particularly applicable here because we
dinates and are therefore positioned close in space. A word     are primarily using this method as an index of societal
embedding is the term for the vector representation of a        (rather than individual) phenomena.
word (the position of a word) within the cloud of semantic         In practice, one can calculate word embeddings from
meaning.                                                        a variety of algorithms, including two of the most
   Representing words as vectors (i.e., as word embed-          widely used algorithms, fastText and GloVe (for defini-
dings) is useful because one can use these numeric              tions, see the glossary in the Supplemental Material).
vectors in subsequent quantitative operations to under-         More recently, word-embedding algorithms have also
stand the space of semantic meaning. In this case, we           expanded to incorporate sentence-level contextual
can use word embeddings to quantify the overlap in              information, such as with the advent of ELMo, BERT,
meaning between words (e.g., between mother and girl)           and RoBERTa embeddings (see the Supplemental Mate-
by looking at the angle between the word-embedding              rial). In this project, we used the fastText algorithm, an
vectors. Again, words that are close in meaning will            improvement from the widely used word2vec algo-
have vectors pointing in similar directions and will            rithm, for all main analyses because (a) at the time of
therefore have a small angle between them and, con-             analysis, it was the highest performing algorithm for
sequently, a large cosine similarity (a measure of the          single-word embedding vector creation (Mikolov et al.,
strength of association between word vectors). Con-             2018); (b) it was similar in approach to previous studies
versely, words far in meaning will have a large angle           using the WEAT that rely on single-word embeddings
between them and a small cosine similarity. In the              (i.e., Caliskan et al., 2017); and (c) it allowed us to
WEAT (described below), we used these cosine similari-          maintain focus on the theoretical contributions of our
ties as the basis for identifying stereotypes (i.e., associa-   findings rather than introduce a new class of sentence-
tions between groups and attributes) in language.               level contextualized approaches (e.g., ELMo, BERT).
   The general approach to create an embedding for a            Notably, in subsequent validation analyses, we also
word is to iteratively calculate the best set of real num-      ensured the robustness of the results by using the
bers that situates the word in semantic space according         GloVe algorithm, and the results remained generally
to its semantic meaning, so that it is situated close to        consistent across both fastText and GloVe approaches.
words similar in meaning. To achieve this optimal rep-
resentation, the word-embedding algorithm (in this case,        Step 6: WEAT. To transform the individual word-embedding
the fastText algorithm; Mikolov et al., 2018) uses the          vectors into an effect size of the strength of gender ste-
target word’s surrounding context to try to predict the         reotypes, we used the WEAT, which has begun to be
target word (e.g., predict dog from within the context          widely applied in understanding social psychological
“the brown X wagged its tail”). At first, the accuracy of       phenomena (e.g., DeFranza et al., 2020; Kurdi, Mann,
predicting the target word is low because the algorithm         Charlesworth, & Banaji, 2019). The WEAT computes a
has received little feedback on the types of word co-           standardized effect-size measure of the relative associa-
occurrences that are most informative of a word’s mean-         tion between words representing group categories (in
ing (e.g., it may also predict bag, rather than dog, in the     this case, male–female) and words representing attributes
context “the brown X wagged its tail”). However, with           (in this case, home–work, math–reading, arts–science,
each iteration, the accuracy of the predictions increases       good–bad ). The degree of association is measured from
until the algorithm “understands” the contexts and co-          the cosine similarities between category and attribute
occurrences of the target word.                                 word-embedding vectors (see above). Again, large cosine
   Notably, because word embeddings are trained on              similarities indicate large overlap between word vectors.
the specific word contexts and co-occurrences in a                 For an example of the WEAT computation, take the
given corpus, the embedding for a target word in cor-           WEAT effect-size calculation for the stereotypical asso-
pus A may be different from the embedding for the               ciation of women–home/men–work. In this example,
same word in corpus B (e.g., the embedding for dog in           we represent each group and attribute by four indi-
children’s books may be different from the embedding            vidual word vectors: she, her, mommy, and mom for
for dog in adult speech). For this reason, word embed-          women; he, him, daddy, and dad for men; house, home,
dings can be used to identify the strength of stereotypes       baby, and family for home; and work, job, business, and
within a given corpus and also test consistency across          money for work. The WEAT computation can be
corpora. In short, word embeddings document the                 described in six general steps.
traces of societal-level collective representations. From          First, we computed the association (i.e., the cosine
this perspective, debates on whether and how word               similarity) between an individual women word vector
embeddings (and vector-space models, more generally)            (she) and all individual home word vectors (house,
reflect the operation of individual human cognition and         home, baby, family). The individual she to house, she
semantic memory (e.g., Günther, Rinaldi, & Marelli,             to home, she to baby, and she to family associations


224                                                                                                   Charlesworth et al.

were then averaged to provide a mean she to home              SC-WEAT test for all stereotype associations. All results are
cosine similarity.                                            reported in Table S3 in the Supplemental Material and are
   Second, we computed the association between that           summarized in the main results below.
same individual women word vector (she) and all work             The SC-WEAT computation followed the same gen-
word vectors (work, job, business, money). Again, the         eral steps as the above WEAT computation, except that
individual associations were averaged to yield a she-to-      (a) we did not repeat the procedures for a second
work mean cosine similarity.                                  attribute because we were interested only in a single
   Third, we took the difference between the she-to-          attribute, and therefore, (b) we did not calculate a
home and she-to-work mean cosine similarities, provid-        double-difference score but, rather, stopped after cal-
ing a difference score for the individual word vector         culating the single-difference score.
she. These three initial steps were then repeated for the        To make this concrete, take the female/male–home
other three women word vectors (her, mommy, mom)              SC-WEAT computation. First, we computed the associa-
to get four individual word difference scores (she to         tion (i.e., cosine similarity) between each individual
home vs. work, her to home vs. work, mommy to home            word representing the single attribute (e.g., the word
vs. work, and mom to home vs. work).                          home for the attribute home) and all individual words
   Fourth, we took the mean of these four individual          representing the women group category (she, her,
word difference scores to provide a mean group differ-        mommy, mom). These associations are then averaged
ence score across all group word vectors (women to            to give a home-to-women mean cosine similarity. Sec-
home vs. work). Steps 1 through 4 were then repeated          ond, we computed the association between that same
to calculate the mean group difference score for the          word (home) and all individual words representing the
opposite group category (men to home vs. work).               men group category (he, him, daddy, dad). Again, these
   Fifth, we took the difference between the two mean         individual associations were averaged to give a home-
group difference scores (men to home vs. work minus           to-men mean cosine similarity. Third, we took the dif-
women to home vs. work). This provided a “double-             ference between the home-to-women and home-to-men
difference” score that reflects the relative semantic simi-   mean cosine similarities, providing a difference score
larity between the groups (male–female) and attributes        for the individual word vector home. These three initial
(home–work ). Sixth and finally, we took this double-         steps were then repeated for the other three home word
difference score (women–home vs. work minus men–              vectors (house, baby, family) to get four individual word
home vs. work) and divided it by the standard deviation       difference scores. Fourth, we took the average of these
across all eight individual word-vector difference scores     four individual word difference scores to get the mean
computed in Step 3 (she to home vs. work, her to home         cosine similarity of home to women versus men, yield-
vs. work, him to home vs. work, etc.). This yielded an        ing a single-difference score. Fifth and finally, we
effect size—the WEAT D score—that is analogous in             divided this single-difference score by the standard
interpretation to an IAT D score in that it is a double-      deviation across all individual word-vector difference
difference score normalized by a measure of variance.         scores computed in Step 3 (home to women vs. men;
                                                              house to women vs. men, etc.). Again, this provided an
   SC-WEAT. A limitation of the WEAT, as well as the          effect size—the SC-WEAT D score—analogous to a
traditional IAT, is that the computations collapse two        single-category IAT D score in that it is a difference
associations into a single relative measure of association.   normalized by the standard deviation.
For instance, the stereotypical association of women–
home/men–work represents both the association of                 Significance of WEAT and SC-WEAT. To perform sig-
home with female (over male) and the association of           nificance tests for the WEAT and SC-WEAT effect sizes,
work with male (over female). Thus, finding a significant     we repeated the above computations 1,000 times after
relative WEAT effect may be driven by one association         permuting the category word vectors across category
being very large (e.g., a strong home–female associa-         boundaries (i.e., randomly shuffling the word vectors rep-
tion), whereas the second association is relatively small     resenting the categories men and women). This yielded
(e.g., a weaker work–male association). Fortunately, the      an empirical null distribution of effect sizes across ran-
present word-embedding approach can easily overcome           dom permutations of categories. The two-tailed p value
this limitation by decomposing the relative association       was then calculated as the proportion of WEAT (or SC-
into two single associations, using the SC-WEAT (see also     WEAT) effects in the empirical null distribution that are
the Word-Embedding Factual Association Test, reported         larger in absolute magnitude than the observed WEAT
by Caliskan et al., 2017, and the SC-WEAT, described by       effect (or SC-WEAT effect).
Kurdi et al., 2019). Thus, to inform interpretation of the       Notably, the results from the permutation tests often
relative effects reported in Study 1, we also performed the   produce relatively large standard errors and therefore


Gender in Language                                                                                                       225

sometimes reveal individual effect sizes that are non-          k = 28; see Table 2), (b) a summary effect for each of
significant at an alpha of .05 (see Table 2). We never-         the four stereotype domains (collapsing across corpora;
theless argue that when these nonsignificant effects are        see Table 2), and (c) a summary effect within each of
large in magnitude (e.g., a WEAT D score of 0.66 with           the seven corpora (collapsing across stereotype
a p value of .10), they can be interpreted descriptively,       domains; see Table 2).
especially alongside the meta-analyses and meta-                   Additionally, we performed meta-regressions to
regressions (described below). Throughout the Results           directly compare the strength of gender stereotypes
section, we focus attention on the meta-analyses and            across corpora and stereotype domains. Specifically, we
meta-regressions because these approaches combine               predicted the magnitudes of the individual effect sizes
data across corpora and thereby provide greater preci-          from (a) stereotype or attitude domain (Study 1 only;
sion and statistical power in estimating the effect sizes       the four dummy-coded domains were good–bad vs.
of interest.                                                    home–work vs. arts–science vs. math–reading ), (b) age
   Why might individual effects sometimes be nonsig-            group (all studies; the two dummy-coded age groups
nificant? In traditional psychological data, standard           were child-produced/child-directed vs. adult-produced/
errors are larger when there are few (vs. many) obser-          adult-directed), and (c) corpora time period (all studies;
vations, all else being equal. Similarly, in word embed-        the three dummy-coded time periods were “early”
dings, larger standard errors (and nonsignificant effects)      [books] vs. “middle” [speech] vs. “late” [AV media]). In
can arise from multiple factors related to the frequency        Study 1, the power to detect significant effects in the
of observations, including (a) the number of stimuli            meta-regressions was limited because the total number
words used to represent a given group category or               of effect sizes was relatively small (k = 28). Thus, the
attribute (e.g., whether 10 or 40 words are used to             results are offered for illustration and interpreted along-
represent the female category), (b) the number of               side the descriptive patterns. In contrast, Studies 2 and
occurrences of a given stimuli word in each corpus              3 had greater power to detect significant meta-regres-
(e.g., the number of times mommy appears in child               sion effects, with more than 1,000 effect sizes in Study
speech), and (c) the number of co-occurrences between           2 and more than 300 effect sizes in Study 3.
stimuli words (e.g., the number of times mommy and
kitchen co-occur in child speech). Ongoing research is          Step 8: validation and replication tests. Word embed­
being conducted to investigate the multiple factors that        dings have begun to be implemented more widely in
contribute to the significance and sensitivity of WEAT          psychology and adjacent fields and have been shown to
results (e.g., Ethayarajh, Duvenaud, & Hirst, 2020).            be valid and reliable methods for capturing psychological
                                                                and social phenomena (Caliskan et al., 2017; DeFranza
Step 7: meta-analyses and meta-regressions. For suc-            et al., 2020; Garg et al., 2018; Kurdi et al., 2019; Lewis &
cinct descriptions of effect sizes across corpora and stereo-   Lupyan, 2020). However, because this article introduces
type domains, a fixed-effects meta-analysis was performed       multiple novel corpora as well as a relatively less-used
using the meta package in the R programming environ­            algorithm (i.e., fastText), we provide four further tests for
ment (R Version 3.6.1; Schwarzer, 2020). A fixed-effects        validation and replication.
approach was chosen over a random-effects approach                 First, to assess whether the chosen word-embedding
because (a) the stereotypes (in Study 1) were not assumed       vectors cohesively represented the categories/attributes
to be a random draw from the true population of stereo-         of interest (i.e., were valid indicators of the category/
types but were specifically selected as well-studied top-       attribute), we compared the similarity between indi-
ics; (b) in some cases, the number of studies used for the      vidual word vectors within a given category (e.g.,
meta-analytic estimate was small (e.g., child-directed          within the categories men, women, good, bad, etc.) with
meta-analysis was based on k = 3), and therefore estima-        the similarity between individual word vectors across
tion of random effects may be biased; and (c) supple-           categories. Specifically, we compared the average
mentary tests of meta-analytic heterogeneity indicated          within-category cosine-similarity score between words
little to no significant cross-study heterogeneity (see         (e.g., the average cosine similarity between she, her,
Table S2.1 in the Supplemental Material). Nevertheless, to      mommy, mom) with the null distribution of all cross-
illustrate the robustness of the results, we also report the    category pairwise cosine similarities, computed through
results from random-effects meta-analyses in the Supple-        permutation tests (e.g., the pairwise cosine similarities
mental Material (see Table S2.2). All major conclusions         between she, work, he, home, etc.). The p value was
about stereotype consistency hold regardless of the fixed-      computed as the proportion of cosine similarities from
effects or random-effects approach.                             the null distribution that were greater than the average
    In Study 1, fixed-effects meta-analytic estimates were      within-category cosine similarity. If the word vectors
computed to provide (a) an overall effect size (collaps-        are indeed cohesive within their category, the p value
ing across all seven corpora and all four stereotypes,          should be less than .05, indicating that less than 5% of


 226


Table 2. Gender Associations Occurring in Child and Adult Natural-Language Corpora (Study 1)

                                                                                                Female–good,                 Female–home,                  Female–arts,             Female–reading,
                                                                    Overall results               male–bad                    male–work                    male–science               male–math

Corpus                                                            D       SE        p         D        SE        p          D        SE        p         D        SE       p        D       SE         p
Meta-analytic estimate                                          0.57     0.08    < .001      0.53     0.16    < .001       0.76     0.16    < .001      0.44     0.16     .005     0.55    0.15     < .001
Child-directed combined (speech, audiovisual, books)            0.46     0.12    < .001      0.42     0.24      .08        0.61     0.24      .01       0.26     0.24     .27      0.56    0.24       .02
Adult-produced/directed combined (speech,                       0.66     0.12    < .001      0.49     0.25      .05        0.94     0.24    < .001      0.54     0.24     .02      0.67    0.24       .005
  audiovisual, books)
Child-produced speech (children to parents)                     0.61     0.20      .002      0.96     0.41       .02      0.69      0.39      .08       0.66     0.40     .10      0.19    0.38       .58
Child-directed speech (parents to children)                     0.44     0.20      .03       0.79     0.40       .05     −0.13      0.40      .80       0.68     0.39     .09      0.43    0.41       .30
Child-directed books                                            0.76     0.23    < .001      0.77     0.46       .12      1.05      0.45      .02       0.69     0.46     .14      0.55    0.46       .22
Child-directed audiovisual media                                0.27     0.20      .17      −0.19     0.40       .66      0.97      0.38      .008     −0.44     0.38     .27      0.69    0.38       .07
Adult-produced speech                                           1.02     0.21    < .001      0.46     0.45       .31      1.07      0.43      .01       0.91     0.42     .03      1.62    0.43     < .001
Adult-directed books                                            0.67     0.21      .001      0.63     0.41       .13      1.09      0.42      .01       0.90     0.44     .03      0.17    0.39       .64
Adult-directed audiovisual media                                0.32     0.21      .12       0.36     0.42       .43      0.69      0.40      .10      −0.11     0.41     .77      0.36    0.43       .38

Note: D is the Word-Embedding Association Test (WEAT) D-score effect size (analogous to the Implicit Association Test D score), providing a standardized effect size of the overlap between categories
(female–male) and attributes (e.g., good–bad). The standard error of the WEAT D-score effect size was computed as the standard deviation of the permutation distribution of WEAT effects. The first
row reports the meta-analytic estimates collapsed across all corpora, yielding summaries at the level of stereotypes. The “overall results” column reports the meta-analytic estimates collapsed across all
associations, yielding summaries at the level of corpora. The second and third rows report the meta-analytic estimates for the combination of child sources and adult sources, respectively.


Gender in Language                                                                                                    227

the null cosine similarities are greater than the actual       score in the stereotypically expected direction (overall
within-category cosine similarity. Testing for cohesive-       WEAT D = 0.57, p < .001; see Table 2 and Fig. 1). Addi-
ness also increases confidence that no single word             tionally, collapsing across all corpora revealed that WEAT
stimulus is overwhelmingly driving the observed asso-          D scores were significant and large for each of the four
ciations because all word stimuli from a category/             stereotype domains (see Table 2; all Ds > 0.44, all ps <
attribute are taken to be similarly representative of the      .005). Finally, collapsing across stereotypes, we found
category/attribute.                                            that WEAT effects were significant and large for five out
   Second, to assess whether the trained word embed-           of the seven corpora (see Table 2; all Ds > 0.44, all ps <
dings accurately captured semantic associations that           .03). The consistency across corpora is remarkable in that
are known to be strong and consistent in psychological         even child-produced speech (from children with mean
data, we tested the strength of a nonsocial association,       age of ~3 years) and child-directed speech (from parents)
musical-instrument–good/weapon–bad. If the WEAT                were communicating gender stereotypes that have not
effect for the musical-instrument–good/weapon–bad              yet been robustly documented at such young ages (Martin
association is significant and strong within a corpus, it      & Ruble, 2010).
can be inferred that the word vectors have accurately             The two nonsignificant corpora were the child-
learned the expected semantic associations (for a simi-        directed audiovisual media (D = 0.27, p = .17) and the
lar approach, see Caliskan et al., 2017).                      adult-directed audiovisual media (D = 0.32, p = .12),
   Third, to assess replicability of the observed results,     although the effect sizes of these corpora are moderate
we performed the same analyses with external data sets         in the expected direction (see Table 2). These results
from data from (a) stereotypes aggregated at the soci-         are discussed below in terms of the possible role of the
etal level (i.e., stereotypes measured through the IAT         relatively more contemporary time period of these two
taken at the Project Implicit demonstration website) as        corpora. Nevertheless, with these two exceptions, the
well as (b) the largest-known corpus of natural lan-           meta-analytic estimates suggest surprising strength and
guage (i.e., the Common Crawl corpus, consisting of            consistency in the magnitude of gender stereotypes
more than 600 billion words from all Internet text). If        across stereotype domains and corpora in children’s
the results are replicated in the Project Implicit data set,   and adult’s natural language.
it suggests that stereotypes measured through word
embeddings are consistent with a very different form           SC-WEAT scores across corpora and stereotypes.
of measuring aggregate societal-level stereotypes. Addi-       Decomposing the relative WEAT D-score effect sizes into
tionally, if the results are replicated in the Common          the SC-WEAT D scores revealed that no single-category
Crawl corpus, it suggests that the observed findings are       association appeared to be driving the relative effects
unlikely to be an artifact of idiosyncratic features in the    (see Table S3 and Fig. S1 in the Supplemental Material).
relatively smaller corpora but, rather, are consistent         In other words, the SC-WEAT scores were approximately
even across the majority of Internet text.                     parallel in magnitude: The stereotypically male-typed
   Fourth, to assess the robustness of the results to the      attribute (e.g., bad, work, science, math) was always
choice of word-embedding algorithm, we retrained all           men-associated, and the stereotypically female-typed
word-embedding vectors using the GloVe algorithm               attribute (e.g., good, home, arts, reading) was always
(Pennington et al., 2014). In brief, the GloVe algorithm       women-associated. Given the parallel results across the
differs from fastText most notably in (a) representing         SC-WEAT scores, we have greater confidence in report-
words only as whole words (e.g., the word cat is rep-          ing and interpreting the more succinct relative results for
resented as the whole word cat) rather than also rep-          all other analyses.
resenting words with subword information (e.g., also
representing cat as a sum of “ca” and “at,” as in fastText)    Meta-regressions across stereotype domain. To
and (b) working directly on the word–word co-occurrence        directly examine the consistency across stereotype topics,
matrix (for further details, see the glossary in the Sup-      we performed a meta-regression predicting the individ-
plemental Material). If the results are replicated despite     ual WEAT effect sizes (k = 28) from stereotype domain
these differences, it indicates that the findings are          (good–bad, home–work, arts–science, math–reading ). No
robust to word-embedding training.                             significant differences were found across stereotype
                                                               domains (all bs = −0.09 to 0.23, zs = −0.35 to 0.91, ps >
                                                               .36; see Table S7.1 in the Supplemental Material), rein-
Results
                                                               forcing that these domains are similarly and consistently
Meta-analyses across corpora and stereotypes. Col-             expressed throughout child and adult language.
lapsing across all seven corpora and all four stereotype          Nevertheless, descriptive trends suggest the strongest
associations (k = 28), we found that the meta-analytic         meta-analytic effect for home–work stereotypes, fol-
estimate revealed a significant and large overall WEAT D       lowed, in order, by associations with math–reading,


228                                                                                                                   Charlesworth et al.


                                 2

                               1.5

                                 1


           WEAT Effect Size
                               0.5

                                 0

                              −0.5

                               −1

                              −1.5                 Child-Produced Speech          Adult-Produced Speech
                                                   Child-Directed Speech          Adult-Directed Books
                               −2                  Child-Directed Books           Adult-Directed AV Media
                                                   Child-Directed AV Media        Meta Estimate

                                      Male−Bad,         Male−Work,             Male−Science,            Male−Math,
                                     Female−Good       Female−Home              Female−Arts           Female−Reading
            Fig. 1. Gender associations in child and adult language (Study 1). Word-Embedding Association Test (WEAT)
            D-score effect sizes are shown as a function of gender association (stereotypes and attitudes), separately for each
            type of child-directed/child-produced and adult-directed/adult-produced speech, books, and audiovisual (AV)
            media. Also shown is the meta-analytic estimate, which was computed from a fixed-effects meta-analysis across
            all sources. Error bars represent 95% confidence intervals computed from the standard error (i.e., the standard
            deviation of the permutation distribution of WEAT effect scores).


good–bad, and arts–science (see Table 2). That the                      examine the role of language as reflecting (from direct
home–work stereotype stands out as the descriptively                    experience) or creating and perpetuating (from indirect
strongest stereotype warrants further examination. It is                experience) the collective representations of gender
possible that the domain of home–work may have                          stereotypes in society.
greater observability than other stereotypes because
gender distribution in caregiving versus labor roles can                Meta-regressions across corpora by age groups.
be widely observed and directly experienced by both                     There was no significant difference in the magnitude of
children and adults. In contrast, distributions of specific             WEAT D-score effect sizes between the baseline of child-
occupational subfields (arts–science), capacities (math–                directed/child-produced corpora and adult-directed/adult-
reading), and especially more general evaluative associ-                produced corpora (b = 0.16, 95% confidence interval
ates (good–bad) may be less observable. Thus, it is                     [CI] = [−0.18, 0.51], z = 0.91, p = .36). Despite previous
possible that the direct experience and observability of                work suggesting variation across children and adults in
home–work roles may lead to particularly strong home–                   their magnitude of gender stereotypes and attitudes
work gender stereotypes being reflected in language                     (Dunham et al., 2016; Martin & Ruble, 2010; Miller et al.,
(Eagly & Wood, 2012; Koenig & Eagly, 2014).                             2018), the meta-regression suggests that, at least for these
   It is also possible, however, that language is not                   four well-studied domains, the language produced by
merely reflecting observable role distributions but also                and directed toward children and adults may be largely
being used to draw attention to stereotypes that are                    consistent.
deemed most important for maintaining social order,
such as the separation of men and women into agentic                    Meta-regressions across corpora by time period. A
(“breadwinning”) versus communal (“caregiving”) roles.                  small (and barely significant) difference emerged across
From this perspective, language may be used as a peda-                  corpora divided by time period, operationalized as early
gogical tool to provide indirect experience and perpetu-                (i.e., child-directed books, adult-directed books) versus
ate stereotypes about who should (or should not)                        middle (i.e., child-directed speech, adult-directed speech,
occupy certain roles. Continued research is needed to                   child-produced speech) versus late (i.e., child-directed


Gender in Language                                                                                                         229

audiovisual media, adult-directed audiovisual media)            reliable in spontaneous language that does not focus
corpora. Specifically, compared with the baseline of early      children’s attention on these group boundaries.
corpora, later corpora were marginally significantly               Also, within child-directed speech (from parents to
weaker in their expression of gender stereotypes (b =           children), the home–work stereotype was small in mag-
−0.42, 95% CI = [−0.85, 0.01], z = −1.91, p = .06). Early and   nitude and nonsignificant (see Table 2), unlike the rela-
middle time-period corpora did not differ from one              tively large effects for the three other associations.
another (b = −0.04, 95% CI = [−0.44, 0.36], z = −0.18, p =      Given that this corpus is largely composed of mothers
.86). The small difference between early and late corpora       speaking with their children about daily life in the
suggests that the magnitude of effect sizes, at least for       home, it may be a unique context in which both moth-
these four well-studied stereotypes in language, may be         ers and fathers are equally likely to co-occur with work
slightly decreasing across time. Such decreases are in line     and home. Phrases such as “mommy needs to work”
with trends observed on other aggregated psychological          and “daddy comes home soon” could be more common
measures (e.g., on male–science/female–arts associa-            in this corpus than others and thereby lead to more
tions; Charlesworth & Banaji, 2019; Miller et al., 2018) but    neutral associations. Future research using parent-to-
stand in contrast to trends of increasing (or stable) ste-      child speech from contexts outside the home, such as
reotypes for other domains (e.g., female–communion              in educational or work settings, could reveal how the
associations have increased over time; Eagly et al., 2020).     environment in which speech is produced also shapes
    It is important to highlight that the corpora com-          the content of the speech.
pared across time also differ in other respects (e.g.,             Finally, within child-directed audiovisual media, two
early corpora are books whereas late corpora are tran-          domains— arts–science and good–bad (see Table 2)—
scripts of audiovisual media; middle corpora are con-           revealed nonsignificant WEAT effects. In general, this
versations, which are more spontaneous than books or            corpus may sometimes show weaker gender stereo-
media). Ideally, temporal comparisons would be per-             types because it is more contemporary than other child
formed within a single language format (e.g., within            corpora (see the meta-regression results above). Addi-
books or within TV and movies). The present corpora             tionally, the audiovisual media corpus may be more
are not sufficiently large for within-corpus comparisons        likely to be the focus of gender-equitable interventions,
and are thus offered as a first step in understanding           such as the United Kingdom’s 2019 ban on gender
change. Future research examining within-corpus                 stereotypes in advertisements. In line with this explana-
change (Garg et al., 2018) will be beneficial to draw           tion, the good–bad association may be weak because
firm conclusions about patterns of gender stereotypes           that association could be seen as particularly harmful
over time in both child and adult language.                     and important to address (i.e., associating men or
                                                                women with “bad” is perceived as particularly harmful).
Additional results. The main takeaway from the meta-            Future research looking at changes within children’s
analytic estimates and meta-regressions is that gender          audiovisual media will be helpful in testing these
stereotypes are consistent in magnitude, even across ste-       explanations.
reotype domains and even across language from both
children and adults. Nevertheless, we also identify a           Validation and replication tests. The corpora and
selection of surprising and potentially informative differ-     word vectors passed all four tests of validation and repli-
ences to guide future research.                                 cation, indicating that the results are reliable and inter-
   Within child-produced speech, we note that, unlike           pretable. First, word vectors were significantly more
the large effects observed for associations of home–            cohesive within category than across categories (all ps <
work, arts–science, and good–bad, the effect for the            .05; with the exception of four out of 70 effects, or 6%,
math–reading stereotype was small in magnitude and              which were p = .06; see Tables S1.1 and S1.2 in the Sup-
nonsignificant (see Table 2). Although a female–reading/        plemental Material), indicating that the word vectors are
male–math stereotype has been documented among                  cohesive representations of their underlying latent group/
children (ages 6–10 years) with laboratory-based                attribute categories. Second, as expected, the WEAT D
implicit and explicit measures (Cvencek et al., 2011), it       score for the musical-instrument–good/weapon–bad
is possible that the stereotype may emerge only after 6         association was strong and consistent in all seven cor-
years old and not at the young average age of the               pora (D range = 1.32–1.50, all ps < .003; see Table S5 in
speakers in this corpus (3 years old). Additionally, it is      the Supplemental Material), indicating that the novel data
possible that the female–reading/male–math stereotype           sets are sufficiently large to identify linguistic associations
may be observed on psychological tests that reinforce           at the expected magnitudes. Third, the magnitude (and
categorical distinctions (i.e., focusing children on cat-       significance) of WEAT effect sizes was generally repli-
egorizing by groups and attributes) but may not yet be          cated in the available data from IATs at the Project Implicit


230                                                                                                 Charlesworth et al.

website, indicating consistency with a very different        fixed-effects meta-analyses and meta-regressions. For
method of capturing societal-level, aggregated represen-     reporting and describing the meta-analysis results, we
tations of gender stereotypes (see Table S7 in the Supple-   retained only trait words that were present in five out
mental Material). The magnitude of WEAT effect sizes         of seven of the primary corpora in the final meta-anal-
was also generally replicated in vectors trained on the      ysis summary, resulting in 170 trait words.
Common Crawl corpus (see Table S7), indicating that the          For these 170 target trait words, we also identified
results appear to be consistent even with a corpus that      five synonyms (from online thesaurus searches; see the
captures nearly all Internet text. Fourth, the magnitude     Supplemental Material) that were specific to the trait
(and significance) of WEAT effect sizes was generally        meaning of the word. This ensured that words with
replicated with word embeddings trained using the            sometimes ambiguous meanings (e.g., frank referring
GloVe algorithm (see Table S6.1 in the Supplemental          to both the trait of “being honest or direct” and the
Material). The current findings—showing consistent gen-      common male name “Frank”) were grouped together
der stereotypes in child and adult language across sources   with other trait words that clearly denoted the semantic
and stereotype topics—are therefore not dependent on         trait meaning (e.g., frank was represented as the aver-
any one method of representing word meaning.                 age association with “frank,” “candid,” “direct,” “forth-
                                                             coming,” “honest,” and “straightforward”). This increased
                                                             the likelihood that the effect size was capturing the
Study 2: Gender–Trait Stereotypes
                                                             intended semantic meaning of the trait, rather than
Experiments documenting stereotypes typically test           some other usage of the word.
only a subsample of topics because of concerns of                Additional analyses with single trait words (rather
interpretability, theoretical precedent, practice effects,   than traits and their synonyms) as well as using differ-
and resource limitations. In this vein, we used a sub-       ent cutoffs for retaining trait words (e.g., appearing in
sample of gender stereotypes in Study 1 to align with        one corpus, retaining 541 trait words, or appearing in
theoretical precedent. However, using a subsample of         all seven corpora, retaining 54 trait words) are provided
stereotypes risks misestimation if the sample does not       in the Supplemental Material. Overarching conclusions
represent the full population. Thus, having shown that       are consistent regardless of the number of traits retained
word embeddings capture well-studied stereotypes, we         (see the Supplemental Material).
used word embeddings to test entire populations of
stereotypes with more than 600 traits (Study 2) and
more than 300 occupations (Study 3). In Study 2, we
                                                             Results
focused on traits because they are a fundamental input       Prevalence of gender–trait stereotypes across all
to person perception (Fiske, Cuddy, Glick, & Xu, 2002)       corpora. Across the 170 trait words (aggregated with
and are even made spontaneously without instruction.         their five synonyms), 72% of traits revealed meta-analytic
Examining hundreds of gender–trait stereotypes can           SC-WEAT D-score effects beyond [−0.1, 0.1], 47% revealed
reveal the consistency of such fundamental stereotypes       effects beyond [−0.2, 0.2], and 29% revealed effects
throughout language.                                         beyond [−0.3, 0.3] (see Fig. 2). These SC-WEAT effect-
                                                             size cutoffs correspond roughly to Cohen’s d cutoffs of
                                                             small, small to medium, and medium to large effects
Method                                                       (because SC-WEAT effect sizes correspond to roughly half
Data sources and procedures for cleaning, lemmatizing,       of a Cohen’s d). Thus, these results can be interpreted as
and creating word embeddings were identical to those         showing the pervasiveness of gender–trait associations:
in Study 1. Only the SC-WEAT (defined above) was             72% of traits reveal meaningful (greater than small) effect
used in Study 2 to measure the association between a         sizes associating a trait word with male or female.
single attribute (i.e., a trait) and the group categories       Additionally, the majority of traits (76%) were associ-
(i.e., male–female).                                         ated with women (i.e., had SC-WEAT effect sizes < 0),
   Single trait words were taken from a list of 627 traits   a proportion that is significantly more likely than would
(Peabody, 1987), providing the most comprehensive            be expected if traits were equally likely to be male or
sample space of traits that were not a priori assumed        female (P = .76, 95% CI = [.69, .83], p < .001). Perhaps
to be associated with men or women. Because of the           traits are more likely to be associated with women
large number of effect sizes coming from the more than       because women is the “nondefault” social category and
600 traits across seven corpora (yielding more than 4,200    therefore more likely to be described and labeled (Bailey,
possible individual effect sizes that would be impossible    LaFrance, & Dovidio, 2019). In contrast, men, as the
to succinctly describe), effects were summarized with        default social category, is seen as synonymous with the


                                           231
                                                                                                                                                                                                                                                                                           b                                                                                         a
                                                                                                                                                                                                                              Meta-Analytic Effect (Trait = Male)                                                       Meta-Analytic Effect (Trait = Male)
                                                                                                                                                                                                                       −1.2   −1   −0.8   −0.6   −0.4   −0.2   0   0.2   0.4   0.6   0.8                         −1.2   −1   −0.8   −0.6   −0.4   −0.2   0   0.2   0.4   0.6   0.8
                                                                                                                                                                                                                        Effects Beyond
                                                                                                                                                                                                          helpful                                                                                   strong
                                                                                                                                                                                                 sophisticated                                                                                    serious
                                                                                                                                                                                                          careful              [−0.1, 0.1]                                                            frank
                                                                                                                                                                                                          steady                                                                                    stable
                                                                                                                                                                                                  sympathetic                  [−0.2, 0.2]                                                 independent
                                                                                                                                                                                                understanding                                                                                        tough


Fig. 2. Gender–trait stereotypes in child and adult language: Traits 1 to 85 (a) and 86 to 170 (b) ranked from most male to most female (Study 2). The Single-Category Word-Embedding
                                                                                                                                                                                                            silent             [−0.3, 0.3]                                                  responsible
                                                                                                                                                                                                         gloomy                                                                                   upright
                                                                                                                                                                                                      stubborn                                                                                      verbal
                                                                                                                                                                                                    thoughtful                                                                                  practical
                                                                                                                                                                                                       polished                                                                                defensive
                                                                                                                                                                                                       talented                                                                                       cruel
                                                                                                                                                                                                         relaxed                                                                                     direct
                                                                                                                                                                                                         clumsy                                                                                   shallow
                                                                                                                                                                                                             lively                                                                                    rigid
                                                                                                                                                                                                           harsh                                                                                        bold
                                                                                                                                                                                                     organized                                                                                    original
                                                                                                                                                                                                        trusting                                                                                    proud
                                                                                                                                                                                                          simple                                                                                    daring
                                                                                                                                                                                                      sensitive                                                                                     stupid
                                                                                                                                                                                                               lazy                                                                              creative
                                                                                                                                                                                                     impatient                                                                                controlled

Association Test (SC-WEAT) effect size is shown for each trait (higher scores indicate that the trait label is associated with male more than female). Traits further toward the right-hand
                                                                                                                                                                                                   competitive                                                                                  accurate
                                                                                                                                                                                                        restless                                                                            cooperative
                                                                                                                                                                                                  complaining                                                                                      honest
                                                                                                                                                                                                       efficient                                                                                     brave
                                                                                                                                                                                                       satisfied                                                                                  rational
                                                                                                                                                                                                       helpless                                                                                     unfair
                                                                                                                                                                                                    suspicious                                                                                     severe
                                                                                                                                                                                                              neat                                                                             generous
                                                                                                                                                                                                          playful                                                                                forward
                                                                                                                                                                                                              hard                                                                                    deep
                                                                                                                                                                                                    depressed                                                                                aggressive
                                                                                                                                                                                                           eager                                                                                      noisy
                                                                                                                                                                                                       complex                                                                               reasonable
                                                                                                                                                                                                      sarcastic                                                                                      bossy
                                                                                                                                                                                                               jolly                                                                                     dull
                                                                                                                                                                                                           angry                                                                                 artificial

side of each plot are the most strongly female typed; traits further toward the left-hand side of each plot are the most strongly male typed. Error bars represent 95% confidence intervals
                                                                                                                                                                                                         jealous                                                                              intelligent
                                                                                                                                                                                                          messy                                                                                  assured
                                                                                                                                                                                                         curious                                                                                    clever
                                                                                                                                                                                                  enthusiastic                                                                                   affected
                                                                                                                                                                                                           merry                                                                                     moral
                                                                                                                                                                                                          fearful                                                                           respectable
                                                                                                                                                                                                       cheerful                                                                                 peaceful
                                                                                                                                                                                                           subtle                                                                               reserved
                                                                                                                                                                                                               cold                                                                               grumpy
                                                                                                                                                                                                            bitter                                                                                 formal
                                                                                                                                                                                                   demanding                                                                                   confident
                                                                                                                                                                                                          touchy                                                                                   critical
                                                                                                                                                                                                          casual                                                                             committed
                                                                                                                                                                                                              rash                                                                                      able
                                                                                                                                                                                                     ambitious                                                                                       polite
                                                                                                                                                                                                              kind                                                                                   smart
                                                                                                                                                                                                    consistent                                                                                      bright


computed from the standard error (i.e., the standard deviation of the permutation distribution of SC-WEAT effect scores). Effects to the left and right of the solid black lines are greater
                                                                                                                                                                                                     charming                                                                                    spiritual
                                                                                                                                                                                                             calm                                                                               cautious
                                                                                                                                                                                                              sexy                                                                                   meek
                                                                                                                                                                                                         intense                                                                              traditional
                                                                                                                                                                                                          tender                                                                              superficial
                                                                                                                                                                                                               soft                                                                             resigned
                                                                                                                                                                                                      gracious                                                                                            fair
                                                                                                                                                                                                    indifferent                                                                                       strict
                                                                                                                                                                                                           social                                                                                  natural
                                                                                                                                                                                                         precise                                                                                  brilliant
                                                                                                                                                                                                       nervous                                                                              determined
                                                                                                                                                                                                           happy                                                                               dishonest
                                                                                                                                                                                                              alert                                                                        mischievous
                                                                                                                                                                                                            weak                                                                                 capable
                                                                                                                                                                                                                tidy                                                                                   loyal
                                                                                                                                                                                                        anxious                                                                                        rude

than small effects (i.e., outside [−0.1, 0.1] SC-WEAT D scores), effects to the left and right of the dashed black lines are greater than medium effects (i.e., outside [−0.2, 0.2] SC-WEAT D
                                                                                                                                                                                                           warm                                                                                    artistic
                                                                                                                                                                                                       careless                                                                                    greedy
                                                                                                                                                                                                         mature                                                                                     active
                                                                                                                                                                                                      romantic                                                                                 dedicated
                                                                                                                                                                                                            tense                                                                                   lonely
                                                                                                                                                                                                        friendly                                                                             intellectual
                                                                                                                                                                                                          patient                                                                                  cranky
                                                                                                                                                                                                        worried                                                                                    sloppy
                                                                                                                                                                                                      feminine                                                                                       crude
                                                                                                                                                                                                                shy                                                                              impolite
                                                                                                                                                                                                           gentle                                                                                        just
                                                                                                                                                                                                  affectionate                                                                                             sly
                                                                                                                                                                                                      pleasant                                                                                     selfish
scores), and effects to the left and right of the dotted black lines are greater than large effects (i.e., outside [−0.3, 0.3] SC-WEAT D scores).                                                        retiring                                                                              educated


232                                                                                                      Charlesworth et al.

general “human” or “person” and therefore may not be             with single trait words did not reach significance, although
labeled with as many trait descriptors. If so, then the          effects were in the same direction (see the Supplemental
greater frequency of women-typed traits could be inter-          Material).
preted as a form of implicit androcentrism.
   Despite the meaningful effect sizes for the SC-WEAT           Content of gender–trait stereotypes across corpora.
trait associations, it is notable that the standard errors       In addition to the quantitative examination of gender–
of the effect sizes were large and, thus, the majority of        trait stereotypes, word embeddings can also begin to
traits were not significantly associated with male or            shed light on the more qualitative content of the trait
female categories (see Fig. 2). Perhaps within the               stereotypes associated with men (i.e., male typed) and
“noisy” environment of spontaneous natural language,             women (i.e., female typed). Descriptively, the top male-
and the polysemy inherent in many trait words, traits            typed and female-typed traits across corpora can be seen
may not always reveal clear signals of gender stereo-            to communicate the trait stereotypes that women are
types, even when the effect sizes are large. However,            generally “pleasant” and “affectionate,” whereas men are
we reemphasize that the majority of traits revealed              “strong” and “serious” (see Table 3 and Fig. 2). The gen-
medium to large effect sizes, suggesting that gender–            eral content reflected in these qualitative descriptions
trait stereotypes are widely communicated through                appears to align with adults’ explicit reports that men are
language.                                                        agentic and competent, whereas women are communal
                                                                 and warm (Abele, Uchronski, Suitner, & Wojciszke, 2008;
Meta-regressions across corpora by age group. SC-                Fiske et al., 2002). Future research would benefit from
WEAT effect sizes (total k = 1,133) were compared across         empirically testing the agency–communion dimension
child-directed/child-produced and adult-directed/adult-          further to answer questions such as whether SC-WEAT
produced corpora. A significant difference emerged by            gender–trait associations correlated with the ratings of
age group, with adult corpora indicating significantly           those traits on agency–communion. Are communion ste-
more female–trait associations than child corpora (indi-         reotypes stronger than agency stereotypes? And has the
cated by more negative effect sizes; b = −0.16, 95% CI =         strength of the communion stereotype (as represented in
[−0.21, −0.11], z = −6.47, p < .001). Notably, because the       traits) increased across time while agency stereotypes
child corpora already indicated a baseline toward female–        have remained stable (Eagly et al., 2020)?
trait associations (b = −0.08, 95% CI = [−0.11, −0.05], z =
−4.73, p < .001), this indicates that adult corpora are          Exploratory analyses of gender–trait associations.
expressing stronger gender–trait stereotypes than chil-          As in Study 1, some results of gender–trait stereotypes
dren, in that they were significantly further below the          were occasionally surprising and may call into question
neutral point. This means that children may express (and         the validity of the analyses. We therefore report two addi-
be exposed to) language that indicates more gender               tional exploratory analyses to show that gender–trait
equity in trait stereotypes.                                     associations in language are indeed meaningful represen-
                                                                 tations of gender stereotypes. First, we tested external
Meta-regressions across corpora by time period.                  validity by correlating SC-WEAT scores with actual data
SC-WEAT effect sizes for traits were next tested across          from child and adult participants’ masculinity/femininity
corpora divided by time period into early (i.e., books),         ratings or categorizations for a subset of traits, collected
middle (i.e., speech), and late (i.e., audiovisual media)        within the same decades as the speech data (obtained
corpora. Significant differences were found across cor-          from Powlishta, 1995, for children and Williams & Ben-
pora by time period, indicating movement toward more             nett, 1975, for adults). The SC-WEAT effect sizes for traits
equitable trait stereotypes over time: Compared with the         (from traits and their synonyms) were significantly corre-
baseline of early corpora showing that traits were, on           lated with both children’s ratings of a trait’s masculinity/
average, female typed (b = −0.23, 95% CI = [−0.27, −0.18],       femininity, r = .50, t(18) = 2.45, p = .02, and the percent-
z = −9.46, p < .001), both middle corpora (b = 0.11, 95%         age of adults categorizing a trait as masculine/feminine,
CI = [0.05, 0.17], z = 3.68, p < .001) and later corpora         r = .72, t(21) = 4.77, p < .001 (see Tables S12.1 and S12.2
(b = 0.10, 95% CI = [0.03, 0.16], z = 2.94, p = .003) revealed   in the Supplemental Material). That is, if a trait was
significantly more gender-balanced trait stereotypes (i.e.,      strongly associated with female in natural language, chil-
more positive effect sizes). Thus, with the caveat that          dren and adults also explicitly reported that trait to be
these temporal comparisons were confounded by other              strongly feminine, and if a trait was strongly associated
differences, the result suggests that gender–trait associa-      with male in natural language, children and adults also
tions (similar to the four well-studied domains of Study 1)      explicitly reported that trait to be strongly masculine.
may be decreasing in bias, in this case decreasing in                Second, we tested construct validity by calculating
androcentric bias. However, we encourage caution in              the primary dimensions (i.e., principal components)
interpreting this finding because meta-regression analyses       that characterize the SC-WEAT scores and examined


Gender in Language                                                                                                                                      233

  Table 3. Top Female–Trait and Male–Trait Associations Occurring Across Corpora (Study 2)

                          Child-              Child-             Child-         Child-directed        Adult-          Adult-         Adult-directed
                        produced             directed           directed         audiovisual         directed        directed         audiovisual
  Overall                speech              speech              books              media            speech           books             media
                                                               Female-typed traits
  Retiring             Careless           Worried            Mature           Affectionate          Pleasant       Tender                Sarcastic
  Pleasant             Shy                Cold               Feminine         Polite                Happy          Feminine              Friendly
  Affectionate         Lazy               Helpless           Charming         Feminine              Playful        Affectionate          Pleasant
  Gentle               Retiring           Suspicious         Consistent       Careless              Messy          Pleasant              Worried
  Shy                  Tense              Consistent         Romantic         Social                Sloppy         Gracious              Shy
  Feminine             Sly                Pleasant           Tense            Crude                 Casual         Gentle                Jolly
                                                                 Male-typed traits
  Strong               Rigid              Strong             Independent       Deep                 Polished       Responsible           Grumpy
  Serious              Controlled         Serious            Noisy             Sarcastic            Stable         Competitive           Creative
  Frank                Tough              Responsible        Sly               Meek                 Resigned       Accurate              Proud
  Stable               Formal             Clever             Strong            Generous             Strong         Creative              Rigid
  Independent          Polite             Independent        Unfair            Proud                Serious        Cranky                Noisy
  Tough                Independent        Gloomy             Careful           Helpful              Unfair         Practical             Artificial

  Note: Trait results were computed from aggregated trait synonyms and were ranked according to magnitude of effect sizes. Results for
  overall corpora were computed from meta-analytic estimates across the 170 traits that were present in at least five (out of seven) corpora.
  Thus, the overall results were determined on the basis of the magnitude of individual effect sizes, as well as the standard errors of the
  individual effect sizes and the range or variability in the magnitude of individual effect sizes. A top overall result therefore reflects both that
  the trait had a high magnitude of effect size, on average, and that it had low variability in the magnitude of effect sizes.


the correlations between these principal components                            Method
and ratings of masculinity/femininity. The principal
component analysis indicated that a one-factor solution                        All data and procedures for data preparation and analy-
provided the best fit to the SC-WEAT scores, with the                          sis were identical to those in Study 2, except that occu-
first principal component explaining 49% of the vari-                          pation stimuli were used in place of trait stimuli.
ance (see the Supplemental Material). Moreover, the                               Occupation stimuli were obtained from a list of 306
loadings on the first principal component were strongly                        occupation titles used by the U.S. Bureau of Labor Statis-
and significantly correlated with the percentage of                            tics (1998). The year 1998 was chosen to match the time
respondents categorizing that trait as masculine/                              period of many of the corpora (e.g., child-produced
feminine (Williams & Bennett, 1975), r = .73, 95% CI =                         speech, child-directed speech, and adult-directed speech,
[.45, .88], t(20) = 4.82, p < .001. Thus, the primary under-                   as well as the majority of child and adult audiovisual media)
lying component of the SC-WEAT gender–trait scores                             and was the earliest year available online with statistics on
indeed appears to be the gender typing of the traits.                          occupational gender distributions. Occupational–gender
                                                                               distribution data were obtained from the same 1998
                                                                               Bureau of Labor Statistics report.
                                                                                  As in Study 2, because of the large number of occu-
Study 3: Gender–Occupation Stereotypes                                         pations across seven corpora (yielding more than 2,000
Societal-level stereotypes about social groups are also                        possible individual effect sizes), the effects were sum-
grounded in associations between groups and occupa-                            marized with a fixed-effects meta-analysis as well as
tions: The occupations/roles that groups occupy (or are                        meta-regressions. Occupation titles that appeared in at
expected to) fundamentally shape the traits and quali-                         least one out of the seven primary corpora were retained
ties ascribed to those groups (Eagly & Wood, 2012).                            (yielding a final sample of 82 occupations). Only single
Additionally, such gender–occupation stereotypes are                           occupation titles were used (without synonyms). Addi-
of interest because occupations, unlike unobservable                           tional analyses using more strict limits (appearing in five
traits, have observable real-world data on gender dis-                         out of seven corpora, retaining 39 occupations; or in all
tributions. The strength of gender–occupation stereotypes                      seven corpora, retaining 17 occupations) are reported
can thus be compared with real-world gender–occupation                         in the Supplemental Material. Overarching conclusions
distributions to understand the relationship between real-                     remain consistent regardless of the number of occupa-
ity and stereotypes.                                                           tions retained (see the Supplemental Material).


234                                                                                                       Charlesworth et al.

Results                                                         have entered the workforce over the past century
                                                                (Charlesworth & Banaji, 2019), children’s and adults’ nat-
Prevalence of gender–occupation stereotypes across              ural-language corpora also express increasingly female–
all corpora. Out of 82 occupation titles present in at          occupation associations.
least one corpus, 79% revealed SC-WEAT effects beyond
[−0.1, 0.1], 57% revealed effects beyond [−0.2, 0.2], and 44%   Content of gender–occupation associations across
revealed effects beyond [−0.3, 0.3]. As with gender–trait       sources. The occupations that revealed large effect sizes
associations, these results show that gender–occupation         were descriptively consistent across corpora (see Fig. 3
associations are strong and pervasive in child and adult        and Table 4). For instance, nurse was among the top six
natural language. Additionally, the majority (62%) of gen-      female-typed occupations in six out of seven corpora,
der–occupation trait associations were associated with          whereas maid and teacher were strongly female typed in
male (P = .62 [.51, .73], p = .04), aligning with the fact      five out of seven corpora; pilot was strongly male typed
that, in the 1998 Bureau of Labor Statistics report, the        in five out of seven corpora, and both guard and excava-
workforce was 60% male.                                         tor were strongly male typed in three out of seven cor-
   Finally, although the majority of occupations showed         pora. This qualitative consistency aligns with the finding
large effect sizes, only a subset revealed significant          that children and adults did not differ in their quantitative
effects. As with gender–trait stereotypes in Study 2, this      magnitude of gender–occupation stereotypes. Moreover,
may suggest that single labels of occupations are not           the content of these gender–occupation stereotypes
always clearly gendered in the “noise” of spontaneous           aligns with the occupations rated as most feminine/
natural language, even when their effect sizes are large.       masculine by children and adults (e.g., Liben, Bigler, &
                                                                Krogh, 2002).
Meta-regressions across corpora by age group. SC-
WEAT effect sizes for gender–occupation stereotypes             Relationship between gender–occupation stereo-
(total k = 344) were compared between child-directed/           types and occupational gender distributions. The
child-produced and adult-directed/adult-produced cor-           strength of gender–occupation stereotypes in language
pora. No significant difference emerged by age group            was significantly and positively correlated with real-world
(b = −0.08, 95% CI = [−0.19, 0.04], z = −1.27, p = .20).        occupational gender distributions, r = .53, 95% CI = [.35,
Unlike gender–trait stereotypes—where adult corpora             .67], t(80) = 5.59, p < .001 (see Fig. 4). The more that men
revealed stronger female–trait associations than child          were represented in a given occupation in the real world,
corpora—the similarity across children’s and adults’            the stronger the association between men and the occu-
gender–occupation stereotypes may emerge because                pation in language. Although similar results have been
these associations are more likely to be grounded in            reported for large-scale Internet text produced by and for
direct experiences and real-world observations (Eagly &         adults (Caliskan-Islam et al., 2016; Garg et al., 2018), the
Wood, 2012; Koenig & Eagly, 2014). That is, the gender          current analyses extend such findings to child-produced
distributions across occupations are arguably more visi-        speech, r = .46, 95% CI = [.11, .71], t(26) = 2.65, p = .01, as
ble than any minor gender differences that may emerge           well as across all other child and adult corpora (rs = .21–
in the expression traits. Thus, to the extent that children     .78, all ps < .10; see the Supplemental Material). The rela-
and adults have similar direct experiences with distribu-       tionship between gender–occupation stereotypes expressed
tions in their environments, children and adults would          in language and real-world occupational gender distribu-
also be expected to show similar magnitudes of gender–          tions is therefore consistent and robust, regardless of the
occupation stereotypes.                                         language source, age group, or time period.
                                                                   The bidirectionality of this relationship will be of
Meta-regressions across corpora by time period. A               interest for future research. In one direction, it is possible
meta-regression predicting SC-WEAT effect sizes by time         that gender–occupation stereotypes are collective rep-
period indicated movement toward weaker male–                   resentations that shape how men and women participate
occupation associations over time: Compared with the            in different occupations (Gaucher et al., 2011). In the
baseline of early corpora, which indicated a significant        other direction, the distribution of men and women into
baseline of male–occupation associations (b = 0.20, 95%         occupations likely shapes how observers talk about,
CI = [0.10, 0.31], z = 3.84, p < .001), both middle corpora     describe, and perceive those occupations and the people
(b = −0.27, 95% CI = [−0.41, −0.13], z = −3.75, p < .001)       in those occupations (Eagly & Wood, 2012; Koenig &
and late corpora (b = −0.21, 95% CI = [−0.35, −0.07], z =       Eagly, 2014). For now, the current data merely reveal a
−2.98, p = .003) moved toward more gender-equal occu-           coupling between language and the real world that is
pation associations. With the caveat that comparisons by        present even in the language of young children.
time period are likely confounded by other differences             Of note, this coupling between real-world occupation
across corpora, the result suggests that, as more women         distributions and stereotypes in language is moderate in


      a
                                                   1.6
                                                   1.2
                                                   0.8
                                                   0.4
                                                     0

                                                  −0.4
                                                         Effects Beyond
                                                  −0.8
                                                                             [−0.1, 0.1]
                                                  −1.2                       [−0.2, 0.2]
                                                                             [−0.3, 0.3]
       Meta-Analytic Effect (Occupation = Male)

                                                  −1.6

                                                                                                                      pilot                                            guard         tailor                                                                                                                                                              actor                                                                                                                                            editor      police
                                                                                                                                                                                                                                         athlete      analyst                                                                                                        laborer                                                        clergy   glazier       grader                     barber                                                                               janitor   clerks
                                                                                                          geologist            inspector   engineer                                                                       biologist                                                         architect     plumber                chemist                                       designer                                                                                                        manager                           executive                    musician
                                                           machinist     excavator                                                                        pharmacist                              economist   assembler                                         mechanic                                            supervisor             electrician                                        lumberjack                messenger                                        technician                                                             firefighter
                                                                                                                                                                                                                                                                            administrator                                                                                                                  bookkeeper
                                                                                        agriculturalist


      b
                                                   1.6
                                                   1.2
                                                   0.8
                                                   0.4
                                                    0
                                                  −0.4
                                                  −0.8
                                                  −1.2
       Meta-Analytic Effect (Occupation = Male)

                                                  −1.6
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            maid
                                                                                                          fisher                                                                                                                                      author                sheriff                                 model                                                                                  cook                     writer                                            baker                                                                                nurse
                                                                                                                      lawyer   welder                                                                         cleaner                                                                                     farmer                 dentist   butcher                   painter                                                                                                                   adjuster   librarian                             teacher
                                                                                        carpenter                                                         gardener                                                                                              physician                                                                                bartender                            therapist                 counselor                                                                                     waitress
                                                          professional                                                                                                 underwriter   dispatcher   announcer               receptionist   accountant                                         hairdresser                                                                                                                                      upholsterer   interviewer                                                           veterinarian                 dressmaker
                                                                         psychologist                                                      cabinetmaker                                                                                                                                                                                                                        photographer                                                                              programmer


      Fig. 3. Gender–occupation stereotypes in child and adult language: Occupations 1 to 41 (a) and 42 to 82 (b) ranked from most male to most female (Study 3). The Single-
      Category Word-Embedding Association Test (SC-WEAT) effect size is shown for each occupation (higher scores indicate that the occupation is associated with male more than
      female). Occupations further toward the right-hand side of the plot are the most strongly female typed; occupations further toward the left-hand side of the plot are the most
      strongly male typed. Error bars represent 95% confidence intervals computed from the standard error (i.e., the standard deviation of the permutation distribution of SC-WEAT
235   effects). Effects to the left and right of the solid black lines are greater than small effects, effects to the left and right of the dashed black lines are greater than medium effects,
      and effects to the left and right of the dotted black lines are greater than large effects.


236                                                                                                                           Charlesworth et al.

      Table 4. Top Female–Occupation and Male–Occupation Associations Occurring Across Corpora (Study 3)

                           Child-          Child-           Child-        Child-directed       Adult-                           Adult-directed
                         produced         directed         directed        audiovisual        directed      Adult-directed       audiovisual
      Overall             speech          speech            books             media           speech           books               media
                                                           Female-typed occupations
      Nurse              Maid           Nurse            Dressmaker     Veterinarian         Librarian      Maid                 Interviewer
      Maid               Nurse          Librarian        Maid           Librarian            Nurse          Waitress             Cook
      Dressmaker         Teacher        Cook             Nurse          Nurse                Waitress       Nurse                Teacher
      Teacher            Sheriff        Maid             Teacher        Farmer               Teacher        Dressmaker           Model
      Veterinarian       Cleaner        Veterinarian     Model          Baker                Musician       Adjuster             Maid
      Waitress           Cook           Teacher          Baker          Gardener             Editor         Upholsterer          Announcer
                                                            Male-typed occupations
      Machinist          Manager        Athlete          Police         Actor                Mechanic       Machinist            Analyst
      Excavator          Pilot          Plumber          Engineer       Cook                 Guard          Administrator        Guard
      Agriculturalist    Excavator      Gardener         Barber         Pilot                Inspector      Excavator            Pilot
      Geologist          Plumber        Excavator        Guard          Janitor              Athlete        Editor               Messenger
      Pilot              Grader         Firefighter      Musician       Inspector            Chemist        Engineer             Assembler
      Inspector          Guard          Announcer        Pilot          Architect            Pilot          Agriculturalist      Tailor

      Note: Occupations were ranked according to magnitude of effect sizes. Results for overall corpora were computed from meta-analytic
      estimates across the 82 occupations that were present in at least one (out of seven) corpora. Thus, the overall results were determined
      on the basis of the magnitude of individual effect sizes, as well as the standard errors of the individual effect sizes and the range
      or variability in the magnitude of individual effect sizes. A top overall result therefore reflects both that the occupation had a high
      magnitude of effect size, on average, and that it had low variability in the magnitude of effect sizes.


magnitude, perhaps suggesting that stereotypes in lan-                       and quantitative evidence that gender stereotypes are
guage are also shaped by inputs other than direct experi-                    indeed collective representations, consistently expressed
ence and observation of the real world. That is, because                     across different language formats, age groups, and time
people are not always accurate at noticing and discuss-                      periods. Our ability to conduct this analysis is a function
ing real-world statistics on gender (e.g., they underesti-                   of unprecedented availability of language corpora and
mate the gender pay gap; Beyer, 2018), even direct                           the emergence of machine-learning algorithms to system-
experience with real-world statistics is unlikely to be a                    atically analyze such data. More than any individual find-
perfect predictor of how occupations are represented                         ing, this project stands as a signal of the vast possibilities
and stereotyped in language. It is possible that indirect                    that lie ahead.
experiences from language itself (which may overem-
phasize or underemphasize gender differences) can fur-
ther create and perpetuate stereotypes in language.
                                                                             Gender stereotypes in language
However, the moderate correlation may also be sup-                           are surprisingly consistent
pressed as a result of less theoretically interesting fea-                   Across three studies, yielding thousands of effect sizes
tures of the data, including noise in the estimation of the                  from hundreds of stereotypes and seven corpora, results
Bureau of Labor Statistics data, noise in the SC-WEAT                        revealed surprising consistency in the strength of gen-
scores from language corpora, and the different time                         der stereotypes in natural language. First, four well-
periods and populations of the Bureau of Labor Statistics                    studied domains (e.g., female–home/male–work) all
data and language corpora. Thus, although the moderate                       revealed large and significant meta-analytic estimates
correlation may point to the possibility of multiple                         (Study 1). Indeed, consistency was observed in the
sources of input to occupation stereotypes (i.e., both                       magnitude of effect sizes across all four domains and
direct and indirect inputs), further research will be                        across children and adults. Small differences emerged
needed to support this interpretation.                                       across language sources divided by time period (1800s
                                                                             to present day), with late corpora expressing weaker
                                                                             stereotypes than early corpora, perhaps suggesting
General Discussion                                                           movement toward more equitable gender stereotypes
The study of collective representations of social-group                      over time (Charlesworth & Banaji, 2019). Although the
stereotypes has a long history of theory (Durkheim, 1898/                    number of effect sizes in Study 1 was limited, the trends
2009; Moscovici, 1988), yet it has remained short on empiri-                 suggest that these gender stereotypes are consistently
cal evidence. In this project, we provided comprehensive                     communicated collective representations.


Gender in Language                                                                                                                                                                   237


                                            1.0
                                                                                                                                                             machinist

                                                                                                                                          agriculturalist           excavator
                                                                                                                                                            geologist    pilot
                                                                                                                              inspector
                                                                                                                                      tailor                 engineer
                                                                                                           pharmacist
                                                                                                                         assembler              athlete    guard
                                            0.5                                                          economist                                                  mechanic
                                                                                                                                                          architect
                                                                                                                      analyst biologist                              plumber
                                                                    administrator                                                                     electrician
                                                                                                                    supervisor      chemist


          Effect Size (Occupation = Male)
                                                                                              designer                                                 laborer lumberjack
                                                                                                                          actor       messenger
                                                                                                        grader                                         clergy glazier
                                                    bookkeeper                                  technician         manager       janitor      barber              firefighter
                                                                 clerks                                                                                   fisher
                                                                                 psychologist                editor       musician             police
                                                                                                                                                                 carpenter
                                                                                               professional
                                            0.0         cleaner
                                                                         underwriter                                    executive         announcer cabinetmaker
                                                                                         accountant                               lawyer                                 welder
                                                                                                               dispatcher                                sheriff
                                                                        model                             author
                                                receptionist                                  bartender                         physician             dentist       gardener
                                                                                                                                           farmer
                                                         hairdresser        therapist                                         photographer
                                                                                                            painter                               butcher
                                                                                                                          cook
                                                                                   counselor        writer
                                                                   interviewer                                                               upholsterer
                                                                                                                     baker           programmer
                                                                                 adjuster
                                    −0.5                        librarian

                                                                            waitress                                             veterinarian
                                                                                 teacher

                                                       dressmaker

                                                                          maid
                                    −1.0               nurse


                                                   0                                25                         50                               75                             100
                                                                                            Percentage of Men in Occupation
             Fig. 4. Gender–occupation stereotypes in language and occupational gender distributions (Study 3). The Single-
             Category Word-Embedding Association Test effect size (meta-analyzed across all seven corpora) is shown for the
             percentage of men in each occupation. Higher scores on the y-axis indicate that the occupation label is associated
             with men more than women). Values on the x-axis are taken from the Bureau of Labor Statistics (1998). The line
             shows the best-fitting slope for a simple linear regression.


   Second, gender–trait stereotypes were also found to                                                            Third, pervasiveness also extended to gender–occu-
be pervasive, even across the largest sample of traits                                                         pation stereotypes, in which 79% of occupations showed
ever simultaneously tested: 72% of traits showed mean-                                                         meaningful associations with gender (Study 3). Gender–
ingful associations with gender (Study 2). These per-                                                          occupation stereotypes revealed significant differences
vasive gender–trait associations nevertheless indicated                                                        across corpora by time period, moving toward more
some change over time, with recent corpora showing                                                             female–occupation associations over time, perhaps in
more gender-equal trait associations. Additionally,                                                            concert with an increasingly female workforce (Charles-
gender–trait associations significantly differed across                                                        worth & Banaji, 2019). Indeed, the strength of gender–
age groups: Child corpora indicated more gender-equal                                                          occupation stereotypes was significantly correlated with
trait associations than adult corpora. Although children                                                       real-world gender distribution of occupations, suggest-
and adults may be similar in how they express widely                                                           ing a coupling between language and direct experience
communicated stereotypes (Study 1), they may never-                                                            of the real world (Eagly & Wood, 2012). Reinforcing this
theless differ in how they express and understand more                                                         interpretation is the finding that gender–occupation ste-
nuanced trait associations (Martin & Ruble, 2010).                                                             reotypes were consistent across age groups, perhaps


238                                                                                                        Charlesworth et al.

because children and adults observe similar occupa-              Declaration of Conflicting Interests
tional gender distributions. Finally, across all studies,          The author(s) declared that there were no conflicts of
we performed multiple supplementary analyses to test               interest with respect to the authorship or the publication
robustness to methodological variations including stim-            of this article.
                                                                 Funding
uli choice, corpus selection, and word-embedding algo-
                                                                   This research was supported by the Harvard University
rithms. General conclusions held throughout, indicating
                                                                   Dean’s Competitive Fund for Promising Scholarship
that the results reflect stable features of how children           awarded to M. R. Banaji and by the Institute for Quantita-
and adults use language to express collective gender               tive Social Sciences Undergraduate Research Scholars
stereotypes.                                                       program.
                                                                 Open Practices
                                                                   All data and analysis scripts have been made publicly
Limitations                                                        available via OSF and can be accessed at https://osf.io/
Theoretical, empirical, and methodological advances not-           kqux5. The design and analysis plans for this study were
withstanding, this project is limited in several ways. First,      not preregistered. This article has received the badges for
the corpora captured only a subset of children’s and               Open Data and Open Materials. More information about
                                                                   the Open Practices badges can be found at http://www
adults’ linguistic repositories. Future research will benefit
                                                                   .psychologicalscience.org/publications/badges. The stud-
from other sources, including the language of siblings,
                                                                   ies were not formally preregistered.
peers, teachers, advertising, and social media. Second,
the text was all English; including non-English languages,
each associated with differing cultures, will advance theo-
ries of how culture and language interact in shaping
                                                                 ORCID iD
collective representations (DeFranza et al., 2020). Third,
although we provided preliminary analyses of patterns            Tessa E. S. Charlesworth   https://orcid.org/0000-0001-5048-3088
of change over time, we were limited in our ability to
look at change within a corpus. Knowing that stereotypes         Acknowledgments
are dynamic, future researchers must seek to document            We thank Aylin Caliskan for guidance and comments on the
changes within child (and adult) language.                       manuscript.

                                                                 Supplemental Material
Conclusion
                                                                 Additional supporting information can be found at http://
With seven corpora of more than 65 million words, this           journals.sagepub.com/doi/suppl/10.1177/0956797620963619
project used word embeddings to quantify the presence
and magnitude of hundreds of gender stereotypes in               References
adult and child language. Associations of gender (male–
                                                                 Abele, A. E., Uchronski, M., Suitner, C., & Wojciszke, B.
female) with well-studied attributes of home–work,
                                                                     (2008). Towards an operationalization of the fundamen-
arts–science, math–reading, and good–bad, as well as                 tal dimensions of agency and communion: Trait con-
with hundreds of traits and occupation labels, emerged               tent ratings in five countries considering valence and
with consistent magnitude across child and adult lan-                frequency of word occurrence. European Journal of Social
guage. These results underscore that gender stereo-                  Psychology, 38, 1202–1217. doi:10.1002/ejsp.575
types, expressed subtly through patterns of word                 Bailey, A. H., LaFrance, M., & Dovidio, J. F. (2019). Is man
co-occurrences in language, are deeply embedded in                   the measure of all things? A social cognitive account of
the social ether. We take this as the first empirical evi-           androcentrism. Personality and Social Psychology Review,
dence for stereotypes as collective representations with             23, 307–331. doi:10.1177/1088868318782848
a strong presence in our language and with the poten-            Beyer, S. (2018). Low awareness of occupational segregation
tial to shape how society thinks about and treats social             and the gender pay gap: No changes over a 16-year span.
                                                                     Current Psychology, 37, 373–389. doi:10.1007/s12144-016-
groups.
                                                                     9521-4
                                                                 Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). Semantics
Transparency                                                         derived automatically from language corpora contain
Action Editor: Rebecca Treiman                                       human-like biases. Science, 356, 183–186. doi:10.1126/
Editor: D. Stephen Lindsay                                           science.aal4230
Author Contributions                                             Charlesworth, T. E. S., & Banaji, M. R. (2019). Gender in sci-
   All the authors developed the study concept and drafted           ence, technology, engineering, and mathematics: Issues,
   the manuscript. T. E. S. Charlesworth, V. Yang, and T. C.         causes, solutions. The Journal of Neuroscience, 39, 7228–
   Mann analyzed the data, and all the authors interpreted           7243. doi:10.1523/jneurosci.0475-18.2019
   the data. All the authors approved the final manuscript for   Croft, A., Schmader, T., Block, K., & Baron, A. S. (2014).
   submission.                                                       The second shift reflected in the second generation: Do


Gender in Language                                                                                                                239

    parents’ gender roles at home predict children’s aspira-               Perspectives on Psychological Science, 14, 1006–1033.
    tions? Psychological Science, 25, 1418–1428. doi:10.1177/              doi:10.1177/1745691619861372
    0956797614533968                                                  Hill, F., Bordes, A., Chopra, S., & Weston, J. (2016, May).
Cvencek, D., Meltzoff, A. N., & Greenwald, A. G. (2011).                   The Goldilocks principle: Reading children’s books with
    Math-gender stereotypes in elementary school children.                 explicit memory representations. Paper presented at the
    Child Development, 82, 766–779. doi:10.1111/j.1467-                    4th International Conference on Learning Representations
    8624.2010.01529.x                                                      (ICLR 2016), San Juan, Puerto Rico. Retrieved from https://
DeFranza, D., Mishra, H., & Mishra, A. (2020). How language                arxiv.org/abs/1511.02301
    shapes prejudice against women: An examination across             Koenig, A. M., & Eagly, A. H. (2014). Evidence for the social
    45 world languages. Journal of Personality and Social                  role theory of stereotype content: Observations of groups’
    Psychology, 119, 7–22. doi:10.1037/pspa0000188                         roles shape stereotypes. Journal of Personality and Social
Dunham, Y., Baron, A. S., & Banaji, M. R. (2016). The devel-               Psychology, 107, 371–392. doi:10.1037/a0037215
    opment of implicit gender attitudes. Developmental                Kurdi, B., Mann, T. C., Charlesworth, T. E. S., & Banaji,
    Science, 19, 781–789. doi:10.1111/desc.12321                           M. R. (2019). The relationship between implicit inter-
Durkheim, E. (2009). Sociology and philosophy. New York,                   group attitudes and beliefs. Proceedings of the National
    NY: Taylor & Francis (Original work published 1898).                   Academy of Sciences, USA, 116, 5862–5871. doi:10.1073/
Eagly, A. H., & Mladinic, A. (1994). Are people prejudiced                 pnas.1820240116
    against women? Some answers from research on atti-                Lewis, M., & Lupyan, G. (2020). Gender stereotypes are
    tudes, gender stereotypes, and judgments of compe-                     reflected in the distributional structure of 25 languages.
    tence. European Review of Social Psychology, 5, 1–35.                  Nature Human Behaviour, 4, 1021–1028. doi:10.1038/
    doi:10.1080/14792779543000002                                          s41562-020-0918-6
Eagly, A. H., Nater, C., Miller, D. I., Kaufmann, M., & Sczesny, S.   Liben, L. S., Bigler, R. S., & Krogh, H. R. (2002). Language at
    (2020). Gender stereotypes have changed: A cross-tempo-                work: Children’s gendered interpretations of occupational
    ral meta-analysis of U.S. public opinion polls from 1946               titles. Child Development, 73, 810–828. doi:10.1111/1467-
    to 2018. American Psychologist, 75, 301–315. doi:10.1037/              8624.00440
    amp0000494                                                        MacWhinney, B. (2000). The CHILDES project: Tools for ana-
Eagly, A. H., & Wood, W. (2012). Social role theory. In P. A. M.           lyzing talk (3rd ed.). Mahwah, NJ: Erlbaum.
    Van Lange, A. W. Kruglanski, & E. T. Higgins (Eds.),              Martin, C. L., & Ruble, D. N. (2010). Patterns of gender
    Hand­book of theories of social psychology (pp. 458–476).              development. Annual Review of Psychology, 61, 353–381.
    Thousand Oaks, CA: SAGE.                                               doi:10.1146/annurev.psych.093008.100511
Ellemers, N. (2018). Gender stereotypes. Annual Review of             Mikolov, T., Grave, E., Bojanowski, P., Puhrsch, C., & Joulin,
    Psychology, 69, 275–298. doi:10.1146/annurev-psych-                    A. (2018). Advances in pre-training distributed word
    122216-011719                                                          representations. In N. Calzolari (Ed.), Proceedings of the
Ethayarajh, K., Duvenaud, D., & Hirst, G. (2020). Understanding            11th International Conference on Language Resources
    undesirable word embedding associations. In A. Korhonen,               and Evaluation (LREC 2018) (pp. 52–55). Retrieved
    D. Traum, & L. Màrquez (Eds.), Proceedings of the 57th                 from https://www.aclweb.org/anthology/L18-1008.pdf.
    annual meeting of the Association for Computational               Miller, D. I., Nolla, K. M., Eagly, A. H., & Uttal, D. H. (2018).
    Linguistics (pp. 1696–1705). Stroudsburg, PA: Association              The development of children’s gender-science ste-
    for Computational Linguistics. doi:10.18653/v1/p19-1166                reotypes: A meta-analysis of 5 decades of U.S. Draw-
Fiske, S. T., Cuddy, A. J. C., Glick, P., & Xu, J. (2002). A               A-Scientist studies. Child Development, 89, 1943–1955.
    model of (often mixed) stereotype content: Competence                  doi:10.1111/cdev.13039
    and warmth respectively follow from perceived status and          Moscovici, S. (1988). Notes towards a description of social
    competition. Journal of Personality and Social Psychology,             representations. European Journal of Social Psychology,
    82, 878–902. doi:10.1037//0022-3514.82.6.878                           18, 211–250. doi:10.1002/ejsp.2420180303
Garg, N., Schiebinger, L., Jurafsky, D., & Zou, J. (2018). Word       Moscovici, S. (2000). Social representations: Explorations in
    embeddings quantify 100 years of gender and ethnic ste-                social psychology. Cambridge, England: Polity Press.
    reotypes. Proceedings of the National Academy of Sciences,        Nosek, B. A., Smyth, F. L., Hansen, J. J., Devos, T., Lindner,
    USA, 115, E3635–E3644. doi:10.1073/pnas.1720347115                     N. M., Ranganath, K. A., . . . Banaji, M. R. (2007).
Gaucher, D., Friesen, J., & Kay, A. C. (2011). Evidence that               Pervasiveness and correlates of implicit attitudes and
    gendered wording in job advertisements exists and sus-                 stereotypes. European Review of Social Psychology, 18,
    tains gender inequality. Journal of Personality and Social             36–88. doi:10.1080/10463280701489053
    Psychology, 101, 109–128. doi:10.1037/a0022530                    Payne, B. K., Vuletich, H. A., & Lundberg, K. B. (2017). The
Godfrey, J., & Holliman, E. (1993). Switchboard-1 Release 2                bias of crowds: How implicit bias bridges personal and
    (Catalog No. LDC97S62). Retrieved from https://catalog                 systemic prejudice. Psychological Inquiry, 28, 233–248.
    .ldc.upenn.edu/LDC97S62                                                doi:10.1080/1047840X.2017.1335568
Günther, F., Rinaldi, L., & Marelli, M. (2019). Vector-space          Peabody, D. (1987). Selecting representative trait adjectives.
    models of semantic representation from a cognitive                     Journal of Personality and Social Psychology, 52, 59–71.
    perspective: A discussion of common misconceptions.                    doi:10.1037/0022-3514.52.1.59


240                                                                                                        Charlesworth et al.

Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe:      U.S. Bureau of Labor Statistics. (1998). Labor force statistics
   Global vectors for word representation. In B. Pang & W.           from the current population survey: 1995–1999 annual
   Daelemans (Chairs), Proceedings of the 2014 Conference            averages - household data - tables from employment and
   on Empirical Methods in Natural Language Processing               earnings (Table 10). Retrieved from https://www.bls.gov/
   (EMNLP) (pp. 1532–1543). doi:10.3115/v1/D14-1162                  cps/cps_aa1995_1999.htm
Powlishta, K. K. (1995). Gender bias in children’s perceptions   U.S. Bureau of Labor Statistics. (2019). American time use
   of personality traits. Sex Roles, 32, 17–28. doi:10.1007/         survey—2019 results (Table A-1). Retrieved from www
   BF01544755                                                        .bls.gov/tus/a1-2019.pdf
Rhodes, M., Leslie, S.-J., Yee, K. M., & Saunders, K. (2019).    Williams, J. E., & Bennett, S. M. (1975). The definition of
   Subtle linguistic cues increase girls’ engagement in sci-         sex stereotypes via the adjective check list. Sex Roles, 1,
   ence. Psychological Science, 30, 455–466. doi:10.1177/            327–337. doi:10.1007/BF00287224
   0956797618823670                                              The World Bank. (2020). Labor force participation rate, female
Schwarzer, G. (2020). Package ‘meta’: General package for            (% of female population ages 15-64) (modeled ILO esti-
   meta-analysis. Retrieved from https://cran.r-project.org/         mate). Retrieved from https://data.worldbank.org/indica
   web/packages/meta/meta.pdf                                        tor/SL.TLF.ACTI.FE.ZS
