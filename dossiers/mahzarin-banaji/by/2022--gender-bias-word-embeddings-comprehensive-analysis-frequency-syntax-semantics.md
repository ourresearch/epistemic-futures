---
title: "Gender bias in word embeddings: A comprehensive analysis of frequency, syntax, and semantics"
person: mahzarin-banaji
section: by
type: book-chapter
year: 2022
date: 2022
venue: "In Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society (pp.156-170)"
authors: "Caliskan, A., Pimparker, P., Charlesworth, T. E. S., Wolfe, R., & Banaji, M. R"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/Caliskan_AIES_Gender_2022.pdf
doi: 
openalex_id: 
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard publications page (banaji.sites.fas.harvard.edu), extracted with pdftotext -layout. Title-overlap check 1.00. Not matched to an OpenAlex work record in this pass. Full citation as listed on her site: Caliskan, A., Pimparker, P., Charlesworth, T. E. S., Wolfe, R., & Banaji, M. R. (2022). Gender bias in word embeddings: A comprehensive analysis of frequency, syntax, and semantics. In Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society (pp.156-170). DEDUP: duplicate file built from the OpenAlex record (W4306021204-family) removed; this file carries the longer extraction."
---

# Gender bias in word embeddings: A comprehensive analysis of frequency, syntax, and semantics

## Full text

Contributed Paper                                                                                         AIES ’22, August 1–3, 2022, Oxford, United Kingdom


            Gender Bias in Word Embeddings:
A Comprehensive Analysis of Frequency, Syntax, and Semantics
                 Aylin Caliskan                                     Pimparkar Parth Ajay                                   Tessa Charlesworth
            University of Washington                           Birla Institute of Technology and                           Harvard University
              Information School                                             Science                                    Department of Psychology
                Seattle, WA, USA                               Department of Computer Science                             Cambridge, MA, USA
                 aylin@uw.edu                                       Pilani, Rajasthan, India                       tessa_charlesworth@fas.harvard.edu
                                                                f20180229@goa.bits-pilani.ac.in

                                                Robert Wolfe                                       Mahzarin R. Banaji
                                       University of Washington                                     Harvard University
                                         Information School                                      Department of Psychology
                                           Seattle, WA, USA                                        Cambridge, MA, USA
                                           rwolfe3@uw.edu                                       mahzarin_banaji@harvard.edu
ABSTRACT                                                                                    for semantic categories: bottom-up, cluster analyses of the top 1,000
Word embeddings are numeric representations of meaning derived                              words associated with each gender. The top male-associated con-
from word co-occurrence statistics in corpora of human-produced                             cepts include roles and domains of big tech, engineering, religion,
texts. The statistical regularities in language corpora encode well-                        sports, and violence; in contrast, the top female-associated concepts
known social biases into word embeddings (e.g., the word vector for                         are less focused on roles, including, instead, female-specific slurs
family is closer to the vector women than to men). Although efforts                         and sexual content, as well as appearance and kitchen terms. Fourth,
have been made to mitigate bias in word embeddings, with the hope                           using human ratings of word valence, arousal, and dominance from
of improving fairness in downstream Natural Language Processing                             a ∼20,000 word lexicon, we find that male-associated words are
(NLP) applications, these efforts will remain limited until we more                         higher on arousal and dominance, while female-associated words
deeply understand the multiple (and often subtle) ways that social                          are higher on valence. Ultimately, these findings move the study of
biases can be reflected in word embeddings. Here, we focus on                               gender bias in word embeddings beyond the basic investigation of
gender to provide a comprehensive analysis of group-based biases                            semantic relationships to also study gender differences in multiple
in widely-used static English word embeddings trained on internet                           manifestations in text. Given the central role of word embeddings
corpora (GloVe 2014, fastText 2017). While some previous research                           in NLP applications, it is essential to more comprehensively docu-
has helped uncover biases in specific semantic associations between                         ment where biases exist and may remain hidden, allowing them to
a group and a target domain (e.g., women – family), using the Single-                       persist without our awareness throughout large text corpora.
Category Word Embedding Association Test, we demonstrate the
widespread prevalence of gender biases that also show differences                           CCS CONCEPTS
in: (1) frequencies of words associated with men versus women;                              • Computing methodologies → Artificial intelligence; Nat-
(b) part-of-speech tags in gender-associated words; (c) semantic                            ural language processing; Learning latent representations;
categories in gender-associated words; and (d) valence, arousal, and                        Learning paradigms; Cognitive science.
dominance in gender-associated words. We leave the analysis of
non-binary gender to future work due to the challenges in accurate                          KEYWORDS
group representation caused by limitations inherent in data.                                word embeddings, AI bias, gender bias, psycholinguistics, represen-
   First, in terms of word frequency: we find that, of the 1,000 most                       tation, masculine default
frequent words in the vocabulary, 77% are more associated with
men than women, providing direct evidence of a masculine default                            ACM Reference Format:
in the everyday language of the English-speaking world. Second,                             Aylin Caliskan, Pimparkar Parth Ajay, Tessa Charlesworth, Robert Wolfe,
turning to parts-of-speech: the top male-associated words are typi-                         and Mahzarin R. Banaji. 2022. Gender Bias in Word Embeddings: A Com-
                                                                                            prehensive Analysis of Frequency, Syntax, and Semantics. In AIES ’22:
cally verbs (e.g., fight, overpower) while the top female-associated
                                                                                            AAAI/ACM Conference on Artificial Intelligence, Ethics, and Society, Au-
words are typically adjectives and adverbs (e.g., giving, emotionally).                     gust 2022, Oxford, England. ACM, New York, NY, USA, 15 pages. https:
Gender biases in embeddings also permeate parts-of-speech. Third,                           //doi.org/10.1145/3514094.3534162

                        This work is licensed under a Creative Commons Attribution-
                        NonCommercial-ShareAlike International 4.0 License.
                                                                                            1     INTRODUCTION
                                                                                            Today, the vast majority of our daily tasks are facilitated and en-
AIES ’22, August 2022, Oxford, England                                                      hanced through the application of Natural Language Processing
© 2022 Copyright held by the owner/author(s).
ACM ISBN 978-1-4503-9247-1/22/08.                                                           (NLP), from simple machine translation to automated resume screen-
https://doi.org/10.1145/3514094.3534162                                                     ing to auto-complete in emails [7]. The core component of many of


                                                                                      156


Contributed Paper                                                                             AIES ’22, August 1–3, 2022, Oxford, United Kingdom


these applications are pretrained static word embeddings – com-                  action, violence, and so on); and (d) the valence, arousal, and domi-
pressed, numeric representations of word meaning based on word                   nance of the top-associated words (e.g., whether the words used for
co-occurrence statistics. These word embeddings are, in turn, cre-               men are terms that convey greater arousal or activation). Each of
ated by training an algorithm (e.g., a neural network) on massive cor-           these metrics provide new, less-studied perspectives on the ways
pora of human-produced text stored on the internet. Ideally, word                that gender biases pervade and persist in pretrained static word
embeddings would be objective representations of human seman-                    embeddings, often in unexpected or subtle ways. The results can
tics but, in reality, word embeddings trained from human-produced                help inform future efforts for more comprehensive bias mitigation
text end up encoding and reproducing the types of social biases held             mechanisms that tackle all such features of gender bias in text.
by humans [9, 12]. When datasets that reflect the thoughts, feelings,                To study the many manifestations of gender bias in language
and actions of a community are used to train artificial intelligence             corpora, we first use the Single-Category Word Embedding Associ-
(AI) models, the models inevitably incorporate the associations and              ation Test (SC-WEAT), a validated and widely-used method that
representations of the community [11–13, 15, 17, 26, 40, 51, 54].                measures cosine similarities to quantify the relative association be-
   In one of the first studies systematically assessing social biases in         tween a target word (in this case, any word in the entire vocabulary
word embeddings, Caliskan et al. [12] showed that pretrained GloVe               of pretrained embeddings, such as aardvark, apple, appetite) and
embeddings replicated ten major biases widely found among hu-                    the two groups, men versus women [12, 46]. The method builds
man participants including biases associating young-good/elderly-                from the same logic as the Single-Category Implicit Association
bad, European American-good/African American-bad, and women-                     Test (SC-IAT) [32] used with human participants, and the relative
family/men-career [28]. Such group-based biases can manifest in                  associations can be interpreted roughly in comparison to statistics
NLP applications (a recent example was seen in Amazon’s auto-                    such as Cohen’s 𝑑 effect sizes.
mated resume screening algorithm that preferentially hired men                       Frequency of Words Associated with Men versus Women.
over women [7]). A comprehensive analysis of where biases re-                    The first research question – how many of the most frequent words
side in word embeddings, including in word frequency, syntax, and                in English-language pretrained embeddings are associated with
semantics, can aid in developing effective bias mitigation strategies.           men relative to women – builds from the social science literature
   The Present Research. The current manuscript provides the                     showing the role of frequency in shaping which groups we think
first comprehensive investigation of the many, and often subtle                  are more famous or liked in society. For instance, if a human par-
ways that social biases are reflected in widely-used static English              ticipant has seen a name more frequently (i.e., on two separate
word embeddings trained on internet corpora (specifically GloVe                  occasions), they judge that name to be more famous than a name
2014 [41] and fastText 2017 [8]). We focus, in particular on gender              they have seen less frequently [3, 31]. Additionally, the mere ex-
biases, because gender is present in every society and gender-based              posure effect in psychology shows that the simple act of seeing a
biases affect large groups of people. We also focus on gender be-                stimulus multiple times increases our liking of that stimulus [56].
cause it is explicitly encoded in many languages including English               The same principles can apply when it comes to word embeddings:
(e.g., via morphemes, pronouns, role labels) allowing a clear sig-               if a given group (e.g., men) has a more frequent representation than
nal for tests of the prevalence and potency of bias transmitted in               another group (e.g., women), the more frequent group will come
language. Here, we focus on gender in terms of the binary repre-                 to shape what we perceive as default, with potential downstream
sentation of men versus women, given the well-established and                    harms. For instance, Wolfe and Caliskan [53] identified that low
validated NLP methods for studying these two identities through                  frequency names in contextualized word embeddings of language
pronouns and role labels. We recognize that, in reality, gender is a             models have more biased and overfitted representations. To present
much more complex spectrum of self-identity and representation.                  a large-scale representation analysis in the language space, we test
However, the existing methods for studying non-binary or fluid rep-              for possible gender biases in word embedding frequency by taking
resentation in text remain in nascent stages [22]; we look forward               the top 1,000, 10,000, and 100,000 words in the pretrained word
to future methodologies that will facilitate a similar comprehensive             embeddings and measuring how many of those words are relatively
investigation of biases for the spectrum of gender identities that               more associated with men (versus women). This approach tells us
are emerging today.                                                              whether the most common concepts in the language of the internet
   Past work has provided evidence for gender biases in the as-                  activate associates with men or with women.
sociation of male/female with a specific semantic domain (e.g.,                      Parts-of-Speech, Content, and Dimensions of Meaning in
science/arts), with sets of traits (e.g., funny, beautiful), and even            Words Associated with Men versus Women. Beyond frequency,
with occupations (e.g., programmer, maid) [12, 17, 26]. However,                 it is also necessary to understand what types of words are more
gender biases in text can extend beyond such semantic associa-                   or less associated with men. In particular, the second research
tions between words. Here, we offer a deep investigation of how                  question focuses on the parts-of-speech used for men versus women.
gender biases also pervade word embeddings in: (a) how many                      Given the stereotypes of men as more active and agentic [30], it is
words are associated with men versus women (i.e., the frequency of               possible that male-associated words will be more likely to be verbs.
words associated with each gender); (b) the parts-of-speech that are             In contrast, given that women are perceived as non-default and
associated with men versus women (e.g., whether men are more                     therefore requiring of additional description or explanation [18], it
referenced using verbs, nouns, or adjectives); (c) the conceptual                is possible that female-associated words will be more likely to be
clusters of the top-associated words with men versus women (e.g.,                adjectives and adverbs (Charlesworth et al. [17] show evidence for
whether the words used for men refer more to content such as                     this expectation with trait adjectives).


                                                                           157


Contributed Paper                                                                                    AIES ’22, August 1–3, 2022, Oxford, United Kingdom


                                              Gender Associations of Words in the GloVe Embedding Space


                                                                                                                                       Female-Male Association Effect Size (𝑑)
                                                                                                                                0.80
                                             40
                                                                                                                                0.50


                        T-SNE y-coordinate
                                             20
                                                                                                                                0.20
                                             0
                                                                                                                              −0.20
                                        −20
                                                                                                                              −0.50
                                        −40
                                                                                                                              −0.80
                                                   −40      −20        0         20             40           60
                                                                  T-SNE x-coordinate

Figure 1: Visualizing the gender associations of the 1,000 most frequently occurring words in the 300-dimensional GloVe
embeddings’ vocabulary in 2 dimensions using the T-SNE algorithm [47] shows that the online language space is overwhelmingly
more associated with men than with women. The imbalanced pattern persists in the top 10,000, and 100,000 words.


   The third research question turns to the semantic content of the                           engineering, sports, and violence; women are more likely to
top-associated words but, instead of using a typical top-down ap-                             be associated, instead, with gender-related slurs and sexual
proach (in which a researcher would study the association to a                                content, as well as appearance and kitchen concepts. Given
domain, selected a priori, such as “science” or “arts”) we investigate                        that big tech is one of the top male-associated clusters of
the semantic bottom-up. Specifically, we use clustering approaches                            words, we provide a deeper case study of the words asso-
to identify conceptual clusters of top-associated words with men                              ciated with this domain. Of nearly 1,000 words uniquely
and women. Although we might expect that common gender stereo-                                associated to big tech, we find that 62% of those words are
types will emerge, the bottom-up approach allows for the possibility                          more associated with men than with women, suggesting
of discovering altogether unexpected domains of words that differ-                            that such masculine defaults may be prevalent even across
entiate between men and women representations.                                                multiple sub-domains of language.
   Fourth and finally, we study whether the top-associated words                          (4) Basic dimensions of word meaning are also gendered: Among
for men and women differ on three foundational dimensions of                                  a set of ∼20,000 words rated by human participants, we find
word meaning [38, 39] – valence (degree to which the word con-                                that, the more a word is associated with men, the more likely
veys positivity/negativity), arousal (degree to which the word con-                           it is to be rated highly on dominance and arousal; in contrast,
veys activity/passivity), and dominance (degree to which the word                             the more a word is associated with women, the more likely
conveys control/submissiveness).                                                              it is to be rated highly on positive valence.
   Ultimately, the work contributes four new insights into where,                        Together, these four conclusions show us that the gender biases
and to what extent, gender biases can persist and pervade static                      in word embeddings are not to be taken only at the level of seman-
word embeddings, in sometimes unexpected ways:                                        tic associations. Rather, gender may be such a deeply organizing
                                                                                      feature in human-produced text that it will pervade throughout met-
   (1) The most frequent words in the vocabularies of pretrained,                     rics as wide-ranging as frequency, syntax, and bottom-up semantic
       static word embeddings (used in many everyday downstream                       discovery.
       applications) are more associated to men than to women,                           The code and resources are available to the public on GitHub.1
       providing direct empirical evidence for the idea of “masculine
       defaults” [18] in these massive corpora of text. Specifically,                 2    RELATED WORK
       of the top 1,000 most frequent words in GloVe embeddings,
                                                                                      We expand on past research in the related, relevant areas of (1)
       77% are associated with men (Figure 1); of the top 10,000
                                                                                      static single-word embeddings; (2) measuring bias in word embed-
       most frequent words, 65% are associated with men; and of
                                                                                      dings; (3) existing evidence of gender bias in NLP; and (4) effects of
       the top 100,000 most frequent words, 55% are associated with
                                                                                      frequency on language representations.
       men. fastText embeddings reveal similar patterns, although
                                                                                      Static Word Embeddings. Static word embeddings are dense,
       slightly less biased.
                                                                                      continuous-valued vector representations of words trained on word
   (2) For parts-of-speech, men are more likely to be associated
                                                                                      co-occurrence statistics of a text corpus, which result in one vec-
       with verbs (at least in fastText) while women are more likely
                                                                                      tor representation per word [20]. Word embeddings geometrically
       to be associated with adjectives and adverbs.
                                                                                      encode semantic similarities between words, enabling them to per-
   (3) Clustering of the top-associated words with men and women
                                                                                      form accurately on analogical reasoning tasks and estimations of
       reveal disparities in content: men are more likely to be as-
       sociated with concepts that include roles such as big tech,                    1 https://github.com/wolferobert3/gender_bias_swe_aies2022


                                                                               158


Contributed Paper                                                                                     AIES ’22, August 1–3, 2022, Oxford, United Kingdom


word relatedness by measuring angular similarity or performing                           Validation of the SC-WEAT. The WEAT has been shown to un-
arithmetic operations on word vectors [35]. While many NLP prac-                         cover statistical realities about the cultures and languages which
titioners have started using language models to encode contextual                        produce the corpora used to train static word embeddings. Caliskan
and sentence-level semantics, static embeddings remain state-of-                         et al. [12] show that gender-associations quantified by SC-WEAT
the-art for many lexical semantics tasks [43], and are known to                          highly correlate with occupational gender statistics and the gender
reflect the cultural norms and biases of the data on which they are                      distribution of names obtained from census data. Toney-Wails and
trained [12, 46]. Consequently, static word embeddings currently                         Caliskan [46] employ the SC-WEAT to show that valence (pleas-
provide a tool for systematically analyzing bias at the training                         antness) norms are consistent across word embedding algorithms,
corpus level.                                                                            time periods, and languages, while that social biases vary. Wolfe
Word Embedding Algorithms. Our work considers two widely                                 and Caliskan [55] use the SC-WEAT to show that valence, domi-
used pretrained static word embeddings. The first is Global Vectors                      nance, and arousal correlate with human psychological judgments
for Word Representation (GloVe) [41], that trains word representa-                       in contextualizing language models, where valence is the strongest
tions for which the dot product of two words corresponds to the                          signal of the three, as demonstrated by Osgood [38].
logarithm of their probability of co-occurrence [41]. Wendlandt                          Gender Bias in Word Embeddings. A summary of the main
et al. [50] find that the GloVe algorithm is the most semantically                       results to date are as follows: Caliskan et al. [12] first quantified
stable based on consistency in nearest neighbors when compared                           gender biases defined in implicit social cognition in word embed-
with singular value decomposition (SVD) factorized positive point-                       dings. Guo and Caliskan [29] expanded the WEAT to detect and
wise mutual information (PPMI) and embeddings trained based on                           quantify intersectional biases associated with identities that belong
the word2vec algorithm of Mikolov et al. [35].                                           to multiple social groups. Bolukbasi et al. [9] found that gender bias
    We also examine the fastText embeddings of Mikolov et al. [34].                      related to occupation exists in common word embedding spaces,
Both GloVe and fastText train on the Common Crawl web corpus, a                          and present a gender debiasing strategy. Gonen and Goldberg [27]
large-scale web scrape intended to produce a "copy of the internet,"                     showed that common debiasing methods for word embeddings
albeit from different time periods. GloVe trains on data through                         fail to remove systematic gender biases, and that biases can be
2014, while fastText trains on data through May 2017.                                    recovered from the debiased space.
Measuring Bias in Word Embeddings. Our work examines gen-                                   Chaloner and Maldonado [14] applied the gender bias WEAT
der bias using SC-WEAT, a variant of the Word Embedding Associ-                          to word embeddings trained on corpora collected from different
ation Test (WEAT) of Caliskan et al. [12]. The WEAT measures the                         domains to show the prevalence of gender bias in news, social
differential association of two groups of word-based concepts (such                      networking, biomedicine, and a gender-balanced corpus. Basta et al.
as instruments and weapons) with two groups of attribute words                           [4] provided a comparative analysis of gender bias in static vs.
(such as pleasant words and unpleasant words). The WEAT is an                            contextualized word embeddings. Zhao et al. [57] quantified gender
adaptation of the Implicit Association Test (IAT) of Greenwald et al.                    bias in the contextualized model ELMo to reveal that a coreference
[28] to word embeddings, which evaluates implicit bias in human                          system inherits its bias.
subjects based on speed and accuracy to associate category and                              Garg et al. [26] used word embeddings to study the evolution of
attribute terms.                                                                         gender stereotypes toward ethnic minorities in the United States
    The SC-WEAT captures the differential association of a single                        during the 20𝑡ℎ and 21𝑠𝑡 centuries. De-Arteaga et al. [21] found
word with two sets of words representing concepts. [12, 13, 46]. The                     that disparities in true positive rates for genders in occupation
concepts can for instance be social groups and the attributes can                        classification using biographies correlate with gender imbalances
be valence terms. Each concept in the SC-WEAT must include at                            in occupations. Charlesworth et al. [17] studied gender bias in
least eight stimuli to ensure that the group constitutes a satisfactory                  word embeddings trained on child and adult corpora curated from
statistical representation of the concept [46]. The formula for the SC-                  conversations, books, movies, and TV of various time periods. The-
WEAT is given below. 𝑤® is the single target stimulus in SC-WEAT.                        oretically selected, personality trait based, and occupation related
cos( ®  ® denotes the cosine of the angle between the vectors 𝑎®
     𝑎, 𝑏)                                                                               gender stereotypes were pervasive and consistent in each corpus.
and 𝑏. 𝐴 = [𝑎®1, 𝑎®2, . . . , 𝑎®𝑛 ] and 𝐵 = [𝑏®1, 𝑏®2, . . . , 𝑏®𝑛 ] are the two
      ®                                                                                     Charlesworth et al. [15] showed that word embeddings con-
equal-sized (𝑛 ≥ 8) sets of attributes representing concepts.                            cerning race/ethnic groups reveal stereotypes whose valence has
                                                                                         remained stable for 200 years. Wolfe et al. [52] demonstrated that
                                                                                         racial bias reflecting the rule of hypodescent in multi-modal language-
                        mean𝑎 ∈𝐴 cos( ®
                                     𝑤, ®                 𝑤, ®
                                        𝑎) − mean𝑏 ∈𝐵 cos( ® 𝑏)                          vision models is more prominent for women, assigning multiracial
       𝐸𝑆 ( ®
           𝑤, 𝐴, 𝐵) =
                               std_dev𝑥 ∈𝐴∪𝐵 cos( ®
                                                 𝑤, ®
                                                    𝑥)                                   female images to the minority group’s linguistic label. Wolfe and
                                                                                         Caliskan [54] further showed that language-vision models mark
   The SC-WEAT returns an effect size metric (𝐸𝑆 in Cohen’s 𝑑)                           the images of women in the language space due to deviation from
and a p-value. (The p-value highly correlates with effect size.) The                     the default representation of ‘person.’
effect size indicates the strength of association, and the p-value                       Frequency and Bias. Our work examines gender bias in the most
determines statistical significance. According to Cohen’s 𝑑 an effect                    frequent words in embeddings’ vocabularies. Brunet et al. [10] used
size of 0.20 is small; 0.50 is medium; and 0.80 is large [19]. The                       the WEAT to show that the least frequent words in the GloVe
sign of the effect size indicates the direction of the association. A
positive effect size 𝑑 corresponds to association with concept 𝐴,
whereas a negative 𝑑 corresponds to association with concept 𝐵.


                                                                                   159


Contributed Paper                                                                                          AIES ’22, August 1–3, 2022, Oxford, United Kingdom


embeddings’ vocabulary are the most semantically sensitive to per-                        which do not occur in the vocabulary of both the GloVe and fastText
turbations of the training data. Wang et al. [48] found that word fre-                    embeddings. The final list of companies includes: Alibaba, Amazon,
quency in the training corpus affects gender direction in static word                     Apple, Facebook, Google, Huawei, IBM, Intel, Microsoft, Nvidia,
embeddings, limiting the effectiveness of debiasing methods which                         Samsung, and Uber. We then compute the mean cosine similarity
do not account for frequency. Wolfe and Caliskan [53] showed that                         for every word in the vocabulary with the embeddings of these
the least frequent names of members of marginalized groups are the                        words, and select the 10, 000 words with the highest mean cosine
most negatively valenced and least context-responsive in language                         similarity for each embedding. For consistency in our approach,
models.                                                                                   and to ensure that the words we retrieve are associated with big
                                                                                          tech across training corpora, we take the intersection of the 10, 000
                                                                                          words returned for each vocabulary, leaving us with a total of 965
3    DATA                                                                                 evaluation words (provided in appendix A.3) reflective of the big
Our work requires the use of validation words for human traits,                           tech space in both embeddings.
a psycholinguistic lexicon for measuring gender associations of
valence, arousal, and dominance, and validation words for study-                          4    APPROACH AND EXPERIMENTS
ing biases in big tech. We also review the static word embedding                          Frequency of Words Associated with Men versus Women.
algorithms covered herein.                                                                Quantifying the relative frequency of male-associated and female-
Word Embeddings. We use 300-dimensional GloVe embeddings                                  associated words show that the full embedding space (i.e., the full
trained on 840 billion tokens of the Common Crawl corpus as it                            vocabulary of embeddings) is more associated with men than with
existed in 2014 [41]. The vocabulary is cased and includes 2.2 mil-                       women; however, it is of particular interest to know whether the
lion words [41]. We also use 300-dimensional fastText embeddings                          degree of male-association increases as we look at subsets of only
trained on 600 billion tokens of the Common Crawl corpus as it                            the most frequent words in the vocabulary. As we discussed above,
existed in May 2017 [34]. The vocabulary is cased and includes 2                          the highest frequency words will have the strongest influence on
million words [34]. These embeddings are widely used in artificial                        shaping downstream outcomes from language models; thus, if one
intelligence (AI) systems by researchers, practitioners, developers,                      gender is more associated with high frequency words, that gender
and students even though they may perpetuate existing biases.                             group will also be overrepresented in downstream outcomes. To
Gender Stimuli. We use the two word lists of gender stimuli em-                           that end, we apply the SC-WEAT to quantify gender bias in the
ployed by Caliskan et al. [12] in SC-WEAT to measure the relative                         100 most frequent words; and also the 1, 000, 10, 000, and 100, 000
gender association of a target word ( ®            𝑤) with women (female at-              most frequent words, for both the GloVe and fastText embeddings.
tribute group) and men (male attribute group). For all gender bias                        We report the distribution of gender bias effect sizes within the
results, positive effect sizes indicate association with women, while                     ranges defined by Cohen, i.e., 0.00 − 0.19 (null), 0.20 − 0.49 (small),
negative effect sizes indicate association with men. These attribute                      0.50 − 0.79 (medium), and ≥ 0.80 (large). Frequency ranges for this
lists 𝐴 = [𝑎®1, 𝑎®2, . . . , 𝑎®8 ] and 𝐵 = [𝑏®1, 𝑏®2, . . . , 𝑏®8 ] follow below:         experiment correspond to the rank-order frequency of the words
Female Attributes: female, she, her, hers, woman, girl, daughter, sister                  as they appear in the embeddings’ vocabulary.
Male Attributes: male, he, him, his, man, boy, son, brother                               Parts-of-Speech Analysis. We analyze the distribution of parts-of-
NRC-VAD Lexicon. Toney-Wails and Caliskan [46], Wolfe and                                 speech in the sets of the 1, 000 most frequent female-biased words
Caliskan [55] show that using SC-WEAT as a lexicon induction                              and male-biased words (to which we also apply our unsupervised
method in word embeddings accurately predicts valence, arousal,                           clustering approach). Part-of-speech tags are obtained using the
and dominance scores of words. We use the NRC-VAD psycholin-                              English-language flair part-of-speech tagger of Akbik et al. [2]. We
guistic lexicon of Mohammad [36], who use the Crowdflower open                            observe the proportion of nouns, adjectives, and verbs within each
source platform to obtain human ratings of valence, arousal, and                          set of biased words, as well as the proportion of singular, plural,
dominance (VAD) for ∼20,000 English-language words. Mohammad                              and proper nouns in those sets.
[36] use best-worst scaling to obtain ratings with better split-half                      Correlation of Gender Bias with Valence, Arousal, and Dom-
reliability than other large psycholinguistic lexica such as the lex-                     inance. We next measured the correlation of gender bias with
icon of Warriner et al. [49]. For our research, a large lexicon is                        respect to the valence, dominance, and arousal ratings included
preferable, because we examine correlations of gender bias with                           in the NRC-VAD lexicon [36]. For this purpose, we computed the
psycholinguistic properties across large word frequency ranges.                           gender effect size for every word in the lexicon which also exists
Word Frequency Data. Even though embeddings’ vocabularies                                 in the embeddings’ vocabulary,2 and obtained Spearman’s 𝜌 of the
are ordered by frequency, we do not have the original training cor-                       gender effect sizes with the human-rated valence scores; with the
pora to compute the actual frequency values. Accordingly, we use                          human-rated arousal scores; and with the human-rated dominance
the python word frequency library wordfreq that estimates word                            scores. Spearman’s 𝜌 is preferable to Pearson’s 𝜌 for this analysis
frequency by pooling multiple language resources [44]. This fre-                          because the effects of frequency and ratings of affect may be mono-
quency information is incorporated into the analysis of correlations                      tonic but not linear, as observed by Wolfe and Caliskan [53], who
between gender associations and valence, arousal, and dominance                           find that the effects of frequency in language models are observable
ratings.                                                                                  on the logarithmic scale.
Big Tech Target Words To create a representative list of words
related to big tech, we use the list of company names defined as "big                     2 Of the 20,007 words in the NRC-VAD lexicon, 19,664 exist in the GloVe vocabulary,
tech" by Abdalla and Abdalla [1], removing those company names                            and 19,665 exist in the fastText vocabulary.


                                                                                    160


Contributed Paper                                                                                                        AIES ’22, August 1–3, 2022, Oxford, United Kingdom


    We then repeat this analysis for only those words which fall                           and Table 2 provide a full breakdown of gender associations by
within specific frequency ranges. Namely, we obtained Spearman’s                           frequency range and effect size for GloVe and fastText. Patterns
𝜌 of gender effect sizes with human-rated VAD scores for the 100                           across GloVe and fastText are consistent, although fastText is less
most frequent words; the 1, 000 most frequent words; and the 10, 000                       biased by percentage of frequency.
most frequent words, ordered based on wordfreq frequency.
    Finally, we repeated this analysis for only those words which                                                           Gender Association by Frequency Range
have effect sizes over a certain threshold. Specifically, we obtained
Spearman’s 𝜌 of gender effect sizes with human-rated VAD scores                                                                                   GloVe Female Associations
for only those words with effect size ≥ .20 (small); only those words                                                                              GloVe Male Associations


                                                                                            % Gender Association
                                                                                                                   100                           fastText Female Associations
with effect size ≥ .50 (medium); and only those words with effect
                                                                                                                                                  fastText Male Associations
size ≥ .80 (large). This analysis includes both words for which                                                    75
the sign of the effect size is positive (indicating association with
women) and words for which the sign of the effect size is negative                                                 50
(indicating association with men).                                                                                 25
Clustering of Gender Biases. Until this point, most analyses of
bias in word embeddings have statistically tested bias along one or                                                 0
several predefined stereotype domains known to exist in the real                                                           𝑁 = 102     𝑁 = 103   𝑁 = 104     𝑁 = 105
world, such as testing the association of women with career words
                                                                                                                                     𝑁 Most Frequent Words
versus family words. We present an unsupervised method for bias
detection which first computes gender bias effect sizes over a subset
of an embeddings’ vocabulary, and then clusters the biased word                            Figure 2: The most frequent words in pretrained GloVe and
vectors to allow detection of biased concepts in the embedding                             fastText word embeddings are associated with men.
space.
    GloVe and fastText embeddings sort their vocabularies in de-                           Clustering of Gender Biases. We obtain eleven clusters each
scending order based on frequency. In light of this, we obtained the                       from the sets of the 1, 000 most frequent female-biased words with
1, 000 most frequently occurring words in the embedding which                              𝑑 ≥ 0.50 (Figure 3) and the 1, 000 most frequent male-biased words
have a gender bias effect size ≥ 0.50 (indicating association with the                     with 𝑑 ≥ 0.50 (Figure 4) in the GloVe vocabulary. Full results are
female attribute group) and a p-value < 0.05, and the 1, 000 most                          included in the appendices A.1 and A.2, but we provide a label and
frequently occurring words in the embeddings’ vocabulary which                             seven examples from each cluster in Table 3.
have a gender bias effect size ≤ −0.50 (indicating association with                            Two of the clusters of the most frequent female-associated words
the male attribute group) and a p-value < 0.05. For each of these                          in the GloVe embeddings are composed of sexual profanities and
two groups of 1, 000 words, we applied K-means clustering using                            obscene adult content.4
the algorithm3 of Elkan [25] to obtain clusters of biased words                                Other female-associated clusters are related to appearance, beauty,
related to the female attribute group and clusters of biased words                         lifestyle, and the kitchen, reflecting cultural expectations for women
related to the male attribute group. We used the elbow method                              to remain submissive and passive. Male-associated clusters, on the
to establish that 𝑘 = 11 clusters are optimal for the sets of 1, 000                       other hand, are related to engineering, sports, violence, leadership,
words. Qualitative review of the clusters with varying 𝑘 indicates                         religion, and big tech. The tokens ‘CEO,’ ‘Captain,’ ‘Chairman,’ and
that clusters obtained with the hyper-parameter 𝑘 = 11 are highly                          ‘chairman’ also cluster into the male names group, suggesting an
cohesive and can be labeled as relating to a single concept.                               association between male proper nouns and corporate power. The
Gender Bias in Big Tech Target Words. While our clustering                                 tokens ‘User,’ ‘Users,’ ‘developer,’ and ‘developers’ have a large
analysis reveals evidence of bias in words related to big tech, we                         male effect size and cluster into the big tech group, reflecting the
also used the SC-WEAT to examine the distribution of gender bias                           (male) identity of the people implicitly associated with the design
effect sizes across the 965 words of our big tech target word list.                        of products and the recruitment of talent at such companies.
As with our frequency analysis, we report the number of small,                                 The affiliation of non-sexual words in certain female-associated
medium, and large effect sizes.                                                            clusters bears remark. The words ‘girl,’ ‘girls,’ ‘Mature,’ ‘Mom,’
                                                                                           ‘movies,’ ‘pics,’‘teen,’ ‘teens,’ and ‘webcam’ cluster within the ob-
5    RESULTS                                                                               scene adult material and sexual profanities clusters, indicating that
Content Warning: The results might be triggering.                                          these words, which have primary meanings that are not related to
Frequency and gender. Our results indicate that the most frequent                          sex, have acquired sexual and obscene features due to the contexts
words in the GloVe and fastText training corpora are associated                            in which they occur. That such words have acquired sexualized
with male attributes (Figure 2). 93 of the 100 most frequent words                         meanings reflects the reinforcing role that sexualization plays in
in the GloVe embeddings’ vocabulary are associated with the male                           male dominance of part of language and culture, such that the
attribute group, as well as 774 of the 1, 000 most frequent words.                         4 One of these clusters consists solely of capitalized words, and the other of uncapi-

This disparity persists regardless of effect size threshold. Table 1                       talized words. With only one exception (the Religion/Violence male-biased cluster,
                                                                                           which is mixed), almost all of the words in a given cluster are either capitalized or
                                                                                           uncapitalized, which seems to be the result of capitalized words appearing more com-
3 Elkan’s algorithm exploits the triangle inequality to avoid unnecessary distance         monly in titles and headers of web content, and uncapitalized words more in the body
calculations and significantly speed up k-means [25].                                      of a web page.


                                                                                     161


Contributed Paper                                                                                                           AIES ’22, August 1–3, 2022, Oxford, United Kingdom


                                                              Gender Association by Frequency Range (𝑁 ) and Effect Size (𝑑) - GloVe
                           𝑁 Most                         𝑑 > 0.00                     𝑑 > 0.20                      𝑑 > 0.50                                  𝑑 > 0.80
                           Frequent Words            Female             Male      Female             Male      Female              Male                   Female             Male
                           𝑁 = 100                    7 (7%)        93 (93%)       2 (3%)        75 (97%)        1 (6%)        15 (94%)                   1 (14%)         6 (86%)
                           𝑁 = 1, 000              226 (23%)       774 (77%)    117 (17%)       578 (83%)     37 (17%)        178 (83%)                  17 (26%)        49 (74%)
                           𝑁 = 10, 000           3,503 (35%)     6,497 (65%)  2,343 (32%)     5,008 (68%)  1,229 (31%)      2,686 (69%)                 611 (34%)     1,187 (66%)
                           𝑁 = 100, 000         45,033 (45%) 54,967 (55%) 34,170 (44%) 43,568 (56%) 20,671 (43%) 27,272 (57%)                        11,373 (44%) 14,369 (56%)
                             Table 1: The most frequent words in the GloVe embeddings’ vocabulary are associated with male attributes.

                                                             Gender Association by Frequency Range (𝑁 ) and Effect Size (𝑑) - fastText
                           𝑁 Most                         𝑑 > 0.00                     𝑑 > 0.20                     𝑑 > 0.50                                   𝑑 > 0.80
                           Frequent Words            Female             Male      Female             Male      Female               Male                  Female             Male
                           𝑁 = 100                  17 (17%)        83 (83%)       4 (8%)         44(92%)      1 (11%)           8 (89%)                  1 (20%)         4 (80%)
                           𝑁 = 1, 000               349(35%)       651 (65%)    182 (31%)       411 (69%)     73 (35%)         137 (65%)                 27 (41%)        39 (59%)
                           𝑁 = 10, 000           4,236 (42%)     5,764 (58%)  2,844 (41%)     4,164 (59%)  1,399 (40%)      2,139 (60%)                 683 (43%)       922 (57%)
                           𝑁 = 100, 000         43,397 (43%) 56,603 (57%) 32,945 (42%) 45,069 (58%) 20,516 (42%) 28,563 (58%)                        12,178 (44%) 15,398 (66%)

                            Table 2: The most frequent words in the fastText embeddings’ vocabulary are associated with male attributes.
                       Female Concept Clusters         Examples                                         Male Concept Clusters          Examples
                       Advertising Words               CLICK, FIRST, FREE, LOVE, OPEN, SPECIAL,         Adventure and Music            Band, Champion, feat, Guitar, LP, Strong,
                                                       WOW.                                                                            Trial.
                       Beauty and Appearance           attractive, beautiful, clothes, cute, exotic,    Big Tech                       API, Cisco, Cloud, Google, IBM, Intel, Mi-
                                                       makeup, perfume.                                                                crosoft.
                       Celebrities and Modeling        bio, cosmetic, designers, magazines, model-      Engineering and Automotive     Automotive, BMW, Chevrolet, Engineer,
                                                       ing, photograph, websites.                                                      Hardware, Power, Technical.
                       Cooking and Kitchen             Bake, cinnamon, dairy, foods, homemade,          Engineering and Electronics    chip, circuit, computing, electronics, logic,
                                                       recipes, teaspoon.                                                              physics, software.
                       Fashion and Lifestyle           Bag, Basket, Diamonds, Earrings, Gorgeous,       God and Religion               Allah, Bible, creator, Christianity, Father, God,
                                                       Shoes, Wedding.                                                                 praise.
                       Female Names                    Alice, Beth, Ellen, Julia, Margaret, Olivia,     Male Names                     Adam, Bryan, CEO, Jeff, Michael, Richard,
                                                       Whitney.                                                                        William.
                       Health and Relationships        allergy, babies, couples, diabetes, marriage,    Non-English Tokens             con, da, del, du, e, que, un.
                                                       parenting, seniors.
                       Luxury and Lifestyle            balcony, bathroom, cruise, luxurious, queen,     Numbers, Dates, and Metrics    -1, 1500, acres, BC, ft, St., £.
                                                       salon, Spa.
                       Obscene Adult Material          blowjob, cunt, dildo, escort, slut, webcam,      Sports                         basketball, championship, coach, franchise,
                                                       whore.                                                                          offense, prospect, victory.
                       Sexual Profanities              Anal, Cum, Fucked, Moms, Porn, Sex, Teens.       Sports and Cities              Baseball, Bowl, Cleveland, Eagles, ESPN,
                                                                                                                                       Sports, Yankees.
                       Web Article Titles               Acne, Blogger, Diet, Newsletter, Relation-      War and Violence               Army, battle, combat, kill, military, soldier,
                                                        ships, Therapy, Yoga.                                                          terror.
                      Table 3: Examples of of instances from the concept clusters of top 1, 000 female and top 1, 000 male associated words


                      40                                                  Advertising Words                  identity of girls and women is being created by male desires and
                                                                       Beauty and Appearance                 preferences. Our results also reveal intersectional bias, as the word


 T-SNE y-coordinate
                                                                       Celebrities and Modeling              ‘Asian’ appears in the female-associated obscene adult material
                      20                                                Cooking and Kitchen
                                                                                                             cluster.
                                                                        Fashion and Lifestyle
                                                                            Female Names                     Parts-of-Speech Analysis. We obtain the 10, 000 most frequent
                      0
                                                                       Health and Relationships              female-biased words and male-biased words based on frequency
                                                                         Luxury and Lifestyle                rank in the embeddings’ vocabulary, and break down each of these
                 −20                                                   Obscene Adult Material                lists based on part-of-speech tags across four frequency ranges
                                                                          Sexual Profanities
                                                                                                             (top 1, 000; 2, 500; 5, 000; and 10, 000 words). In both the GloVe
                 −40                                                      Web Article Titles
                                                                                                             (Table 4) and fastText embeddings (Table 5), a larger share of the
                    −50                     0                 50                                             most frequent female-biased (rather than male-biased), reflecting
                                  T-SNE x-coordinate                                                         the marking of women with trait attributions, for whom more of
                                                                                                             the most frequently associated words are descriptive. In the GloVe
Figure 3: The 1,000 most frequent words associated with the                                                  embeddings, 113 of the 1, 000 most frequent female-biased words are
female attributes (𝑑 ≥ 0.50) in the GloVe vocabulary clus-                                                   adjectives, compared to 66 of the male-biased words; of the 10, 000
ter into conceptual groups related to stereotypes and sexual                                                 most frequent female-biased words, 857 are adjectives, compared
profanities. The visualization above reflects a T-SNE dimen-                                                 to 495 for men. A similar disparity exists for adverbs: of the 10, 000
sionality reduction after conversion to cluster coordinates.                                                 most frequent female-biased words in the GloVe embedding, 133
                                                                                                             are adverbs, compared to 45 of the male-biased words.


                                                                                                       162


Contributed Paper                                                                                       AIES ’22, August 1–3, 2022, Oxford, United Kingdom


                                                       Parts-of-Speech for the Top 𝑁 Gender-Associated Words - GloVe
                                                                𝑁 = 1, 000       𝑁 = 2, 500       𝑁 = 5, 000       𝑁 = 10, 000
                                           Part-of-Speech
                                                             Female Male Female Male Female Male Female Male
                                           Nouns                 778     768     1,981 1,937     3,914 3,908       7,819 7,844
                                           Verbs                  53       66      175    143      371     308       769     594
                                           Adjectives            113       66      251    142      483     251       857     495
                                           Adverbs                16        5       24      11      64       20      133      45
                                           Other                  40       95       69    267      168     513       422 1,022
                                            Table 4: Gender and parts-of-speech associations in GloVe embeddings

                                                      Parts-of-Speech for the Top 𝑁 Gender-Associated Words - fastText
                                                                𝑁 = 1, 000        𝑁 = 2, 500      𝑁 = 5, 000        𝑁 = 10, 000
                                           Part-of-Speech
                                                             Female Male Female Male Female Male Female Male
                                           Nouns                 833     843     2,138 2,056     4,299 4,071        8,581 8,109
                                           Verbs                  63       54      129     140     237     308        482     613
                                           Adjectives             63       46      151     133     302     248        570     524
                                           Adverbs                10        6       15       14     31       32        55      69
                                           Other                  31       51       47     157     131     341        312     685
                                           Table 5: Gender and parts-of-speech associations in fastText embeddings


                                                          Adventure and Music              ranges. On the other hand, 166 of the 1, 000 most frequent words in
                      40
                                                                Big Tech                   the GloVe embedding associated with women are plural common


 T-SNE y-coordinate
                                                       Engineering and Automotive          nouns, compared to 92 of the most frequent words associated with
                                                       Engineering and Electronics
                      20                                                                   men. This might reflect the language positioning men as individuals
                                                            God and Religion
                                                              Male Names                   in their own right relative to women.
                      0                                    Non-English Tokens              Correlation of Gender Bias with Valence, Arousal, and Domi-
                                                       Numbers, Dates, and Metrics         nance. Valence ratings in the NRC-VAD lexicon correlate positively
                 −20
                                                                 Sports                    and significantly (𝑝 < 10−7 ) with gender bias effect size (female
                                                            Sports and Cities
                                                                                           associations), while dominance and arousal correlate negatively
                                                            War and Violence
                                                                                           and significantly (𝑝 < 10−7 ) with gender bias effect size (male
                       −40   −20    0     20      40                                       associations).
                             T-SNE x-coordinate                                               Table 8 indicates that, as the frequency range of the words in-
                                                                                           creases in GloVe, the correlation of female gender bias with human-
Figure 4: The 1, 000 most frequent words associated with male                              rated word pleasantness decreases. Since lower frequency words
attributes (𝑑 ≥ 0.50) in the GloVe vocabulary cluster into                                 tend to have lower valence scores and higher bias (correlation of
conceptual groups related to adventure, engineering, religion,                             word frequency and valence scores: 𝜌 = .23, 𝑝 < 10−233 ), this re-
science, sports, violence, and war.                                                        sult is expected. On the other hand, as frequency range increases,
                                                                                           correlation of male gender bias with both human-rated dominance
                                                                                           and arousal increases or does not show a significant change. Table
                                                                                           9 indicates that, as the gender effect size of words increases, the
   Another striking gender disparity is seen in the "Other" part-
                                                                                           correlation with valence increases in the positive direction (female
of-speech category, which at every frequency range encompasses
                                                                                           associations), while correlation with dominance and arousal in-
more than twice as many of the male-biased words as the female-
                                                                                           creases in the negative direction (male associations). As a result,
biased words both in GloVe (Table 4) and fastText (Table 5). While
                                                                                           female-biased words in the lexicon are associated with pleasantness,
this category includes pronouns and interjections, it is made up
                                                                                           while male-biased words are associated with dominance and with
primarily of numbers, dates, and measurements (677 of the 1, 022
                                                                                           arousal.
"Other" male-biased words at 𝑁 = 10, 000 for the GloVe embed-
                                                                                              The correlation between valence and dominance in the NRC-
ding), potentially reflecting the association of men with subjects of
                                                                                           VAD lexicon is 𝜌 = 0.49, indicating that pleasant words are also
historical and scientific significance.
                                                                                           more associated with dominance. Gender bias effect size has a cor-
   In the fastText embeddings, 613 of the top 10, 000 male-biased
                                                                                           relation coefficient of 𝜌 = 0.09 with valence, but of 𝜌 = −0.19 with
words are verbs, compared to 482 of the female-biased words. While
                                                                                           dominance. This indicates that correlations of gender association
the distribution of nouns seems at first to be comparable between
                                                                                           with valence, arousal, and dominance are distinguishable from the
the two lists of biased words, significant differences arise when noun
                                                                                           underlying correlations of these properties with each other.
type is considered (Table 6 and Table 7). In the GloVe embedding,
                                                                                           Big Tech. In both the GloVe and fastText embedding spaces, big
275 of the 1, 000 most frequent words associated with women are
                                                                                           tech words are primarily associated with men. In the GloVe em-
singular proper nouns, compared to 352 of the most frequent words
                                                                                           bedding, half of the big tech words have at least small male effect
associated with men, a disparity that persists across frequency


                                                                                     163


Contributed Paper                                                                                                 AIES ’22, August 1–3, 2022, Oxford, United Kingdom


                                          Noun Distribution for the Top 𝑁 Gender-Associated Words - GloVe
                                                        𝑁 = 1, 000        𝑁 = 2, 500       𝑁 = 5, 000     𝑁 = 10, 000
                           Noun Type
                                                      Female Male Female Male Female Male Female Male
                           Singular Common Nouns         337      319      751     728    1,345 1,374     2,388 2,425
                           Singular Proper Nouns         275      352      807     881    1,782 1,835     4,009 4,049
                           Plural Common Nouns           166       92      418     315      780     662   1,410 1,296
                           Plural Proper Nouns             0        5        5       13       7       37     12      74
                                       Table 6: Gender and noun associations in GloVe embeddings

                                          Noun Distribution for the Top 𝑁 Gender-Associated Words - fastText
                                                         𝑁 = 1, 000        𝑁 = 2, 500       𝑁 = 5, 000       𝑁 = 10, 000
                           Noun Type
                                                      Female Male Female Male Female Male Female Male
                           Singular Common Nouns          319      372      750     823    1,354 1,510       2,343 2,738
                           Singular Proper Nouns          331      298      955     802    2,160 1,682       4,751 3,739
                           Plural Common Nouns            183      167      433     416      782     847     1,475 1,572
                           Plural Proper Nouns               0       6        0       15       3       32       12      60
                                      Table 7: Gender and noun associations in fastText embeddings


       Spearman’s 𝜌 of Gender Association and NRC-VAD Ratings                                                        Big Tech Gender Association by Effect Size
                        by Word Frequency Range (𝑁 )
Correlation (GloVe)               𝑁 = 102 𝑁 = 103 𝑁 = 104 NRC-VAD                                                                GloVe Female Associations
                                     0.15     0.16    0.10     0.07                                                               GloVe Male Associations


                                                                                     % Gender Association
Female Association vs. Valence
Female Association vs. Arousal      -0.14    -0.11   -0.13    -0.12                                         100                 fastText Female Associations
Female Association vs. Dominance     0.05    -0.16   -0.21    -0.20                                          80                  fastText Male Associations
Correlation (fastText)            𝑁 = 102 𝑁 = 103 𝑁 = 104 NRC-VAD                                            60
Female Association vs. Valence       0.02     0.15    0.15     0.14                                          40
Female Association vs. Arousal      -0.07    -0.12   -0.11    -0.12                                          20
Female Association vs. Dominance    -0.05    -0.10   -0.08    -0.07                                           0
Table 8: Female-associated words correlate more strongly                                                             𝑑 ≥ 0.00    𝑑 ≥ 0.20    𝑑 ≥ 0.50     𝑑 ≥ 0.80
with valence, while male-associated words correlate with
arousal and dominance.                                                                                                  Gender Bias Effect Size (𝑑) Threshold

      Spearman’s 𝜌 of Gender Association and NRC-VAD Ratings                     Figure 5: The words most associated with big tech in both the
                   by Gender-Association Effect Size (𝑑)                         GloVe and fastText embeddings are predominantly associated
Correlation (GloVe)              𝑑 ≥ 0.00  𝑑 ≥ 0.20    𝑑 ≥ 0.50 𝑑 ≥ 0.80         with men.
Female Association vs. Valence      0.07       0.09       0.14     0.17
Female Association vs. Arousal     -0.12      -0.13      -0.16    -0.16
Female Association vs. Dominance   -0.20      -0.22      -0.25    -0.28
Correlation (fastText)           𝑑 ≥ 0.00  𝑑 ≥ 0.20    𝑑 ≥ 0.50 𝑑 ≥ 0.80
                                                                                 6               DISCUSSION
Female Association vs. Valence      0.14       0.15       0.18     0.22
Female Association vs. Arousal     -0.12      -0.12      -0.12    -0.12          GloVe and fastText static word embeddings are, at every level of
Female Association vs. Dominance   -0.07      -0.08      -0.08    -0.09          analysis, more associated with men than with women. Of the 10, 000
Table 9: The most female-associated words correlate more                         most frequent words in the GloVe vocabulary, 1, 187 have a large
strongly with pleasantness, while male-associated words cor-                     effect size association with men, compared to only 611 with a large
relate strongly with arousal and dominance.                                      effect size association with women. fastText shows similar patterns,
                                                                                 although it shows lower bias. This suggests that representation of
                                                                                 women in the corpus has improved from training data collected for
                                                                                 GloVe before 2014 relative to the 2017 data, and is in line with slow
size, compared to just 24% of big tech words with at least small                 but consistent aggregate level change in implicit gender bias [16].
female effect size. In fastText, 19% of big tech words have large                Ultimately, the findings show that large-scale corpora collected
male effect size, compared to just 9% with large female effect size.             from the internet consist primarily of content and contexts related
Figure 5 describe results in full. While Bolukbasi et al. [9] showed             to men, providing evidence of a masculine default in the online
gender biases in words related to programming and computation,                   language of the English-speaking world.
this is the first result which has pointed to biased associations in                Gender differences don’t only exist in how many words are
words related to big tech, an influential sector of the economy.                 associated with one group or another, however, they also pervade
According to the observations of Nosek et al. [37], widespread im-               the type of words associated with each gender [33]. Specifically,
plicit bias associating big tech with men over women reinforces                  associations with part-of-speech tags reveal that women are more
the overrepresentation of men in these professions.                              frequently associated with adjectives and adverbs. In line with


                                                                           164


Contributed Paper                                                                                AIES ’22, August 1–3, 2022, Oxford, United Kingdom


previous work [17], this suggests that women – being the non-                       Limitations. In this work, we use static word embeddings that
default gender category – need additional description. In contrast,                 compress all the PPMI from word co-occurrence statistics of a
we find that men are more associated with verbs in fastText, aligning               single word into one vector. Accordingly, the word embedding for
with stereotypes of men as more agentic and capable of action in                    a polysemous word such as ‘Apple’ represent the most frequently
the world (although this difference in verbs does not exist in the                  occurring definitions and senses of the word. Without access to
GloVe embeddings, except in the 1,000 most frequent words).                         the original training corpora, we cannot disentangle these nuances
    Next, clustering the most frequent 1, 000 female-associated words               when measuring bias. Nevertheless, in future work, the methods
and 1, 000 male-associated words and manually analyzing them                        and data can be extended to study fine-grained phrase associations
highlights a surprising degree of explicit, unique, negative stereo-                in phrase embeddings or language models.
types for both groups. While the most frequent male associates are                  Future work. We focus on the two largest social groups in the
concepts such as aggression, big tech, engineering, names, power,                   world – women and men. Extending this work to other representa-
sports and cities, violence, and war, the most frequent female asso-                tions of gender, sex, and intersectional categories has challenges
ciates are concepts based on explicit adult material, offensive words,              since the signals associated with underrepresented groups are less
and sexual profanities, as well as appearance, beauty, lifestyle,                   accurate, more biased, and overfitted to the few contexts they ap-
names, and kitchen concepts.                                                        pear in [22, 45, 53]. Moreover, many identities are omitted due
    Propagation of all of these representations associated with men                 to frequency thresholding or even fully absent in corpora due to
and women into downstream applications should prompt deliberate                     disparities in access and representation. We plan to tackle these
thought. This is especially the case when designing visual semantic                 challenges in future work by developing appropriate algorithms
AI systems, such as OpenAI’s CLIP [42] which, like GloVe does with                  through participatory design that can help identify and represent
linguistic representations, trains visual and linguistic representa-                multiple social groups in language models.
tions by maximizing the dot product of self-supervised text-image                      Overall, our findings contribute new evaluation criteria for fair
combinations. For example, our results suggest that visual semantic                 representation learning and for analyzing bias mitigation in down-
systems may associate non-sexual text input with pornography and                    stream applications. Furthermore, complementing computational
toxic sexualized representations of women; see also [6].                            methods by adding comprehensive data statements to language
    Another gender difference concerns “big tech” words. Here, we                   technologies as outlined by Bender and Friedman [5] will enhance
offered an additional case study into this domain and showed that,                  transparency and raise awareness, which is the first step towards
of nearly 1,000 words associated with big tech, more than 60% were                  mitigating bias.
associated with men. The findings for big tech may be particular                       Future longitudinal and localized analysis of historical word em-
noteworthy since it shows evidence for default gender biases in the                 beddings can help us identify the significant events and strategies
very industry that creates, applies, and commercializes AI models.                  that contribute to gender equity [15]. Understanding the evolution
    Finally, the correlations between gender associations of words                  of gender bias in language corpora can help us develop bias mit-
with valence, arousal, and dominance scores show that the online                    igation strategies and effective intervention mechanisms such as
language space is not only more frequently associated with men but                  policy level changes. Such approaches will not only contribute to
also that those men are more frequently represented in meaning                      mitigating bias in AI models but also to mitigating gender inequities
dimensions of dominance (i.e., control/submissiveness) and arousal                  in language, which is a dominant method of meaning transmission
(i.e., activity/passivity) (Figure 6). In contrast, women are more                  in all human societies.
associated with the valence of pleasantness, supporting evidence
for the “women are wonderful” effect widely seen in the social                      7   CONCLUSION
sciences [23, 24].                                                                  This work analyzes the scope of gender bias in static word embed-
                                                                                    dings. Our findings show that gender biases are not only present
                                                                                    in well-studied metrics of semantic associations, but also remain
                  Spearman’s 𝜌 of Gender Association and VAD - GloVe
                                                                                    widespread in terms of word frequency, parts-of-speech, clustered
                                  Gender Association vs. Valence                    concepts, and word meaning dimensions. Overall, we find that the
                                  Gender Association vs. Arousal                    most frequent words and concepts in English pretrained embed-
                 0.4             Gender Association vs. Dominance
                                                                                    dings are overwhelmingly associated with men more than women,


 Spearman’s 𝜌
                 0.2                                                                especially for the highest frequency words. Moreover, we find that
                  0                                                                 words associated with men and women are differentiated in terms
                −0.2                                                                of parts-of-speech (e.g., women are more associated with adjectives
                                                                                    and adverbs), clusters of concepts (e.g., women are more associated
                −0.4
                       𝑑 ≥ 0.0    𝑑 ≥ 0.2         𝑑 ≥ 0.5           𝑑 ≥ 0.8         with sexual content; men are more associated with big tech), and
                                                                                    basic dimensions of word meaning (e.g., women are more associated
                                      Effect Size (𝑑)
                                                                                    with positive valence, men are more associated with arousal and
                                                                                    dominance). These findings show the surprising scope of gender
Figure 6: In GloVe embeddings, as the magnitude of female-                          bias that can remain, somewhat hidden, across multiple features of
association increases, the correlation of bias with valence                         pretrained embeddings. As a consequence, the results raise signif-
increases, while as the magnitude of male-association in-                           icant concerns about the social, cultural, and digital mechanisms
creases, the correlation of bias with arousal and dominance                         that may exacerbate gender biases in AI and society.
increases.


                                                                              165


Contributed Paper                                                                                                 AIES ’22, August 1–3, 2022, Oxford, United Kingdom


REFERENCES                                                                                       [26] Nikhil Garg, Londa Schiebinger, Dan Jurafsky, and James Zou. 2018. Word
 [1] Mohamed Abdalla and Moustafa Abdalla. 2021. The Grey Hoodie Project: Big                         embeddings quantify 100 years of gender and ethnic stereotypes. Proceedings of
     tobacco, big tech, and the threat on academic integrity. In Proceedings of the 2021              the National Academy of Sciences 115, 16 (2018), E3635–E3644.
     AAAI/ACM Conference on AI, Ethics, and Society. 287–297.                                    [27] Hila Gonen and Yoav Goldberg. 2019. Lipstick on a pig: Debiasing methods cover
 [2] Alan Akbik, Duncan Blythe, and Roland Vollgraf. 2018. Contextual String Em-                      up systematic gender biases in word embeddings but do not remove them. arXiv
     beddings for Sequence Labeling. In COLING 2018, 27th International Conference                    preprint arXiv:1903.03862 (2019).
     on Computational Linguistics. 1638–1649.                                                    [28] Anthony G Greenwald, Debbie E McGhee, and Jordan LK Schwartz. 1998. Mea-
 [3] Mahzarin R Banaji and Anthony G Greenwald. 1995. Implicit gender stereotyping                    suring individual differences in implicit cognition: the implicit association test.
     in judgments of fame. Journal of personality and social psychology 68, 2 (1995),                 Journal of personality and social psychology 74, 6 (1998), 1464.
     181.                                                                                        [29] Wei Guo and Aylin Caliskan. 2021. Detecting emergent intersectional biases:
 [4] Christine Basta, Marta R Costa-Jussà, and Noe Casas. 2019. Evaluating the                        Contextualized word embeddings contain a distribution of human-like biases. In
     underlying gender bias in contextualized word embeddings. arXiv preprint                         Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society. 122–133.
     arXiv:1904.08783 (2019).                                                                    [30] N. Hsu, K. L. Badura, D. A. Newman, and M. E. P. Speach. 2021. Gender,
 [5] Emily M Bender and Batya Friedman. 2018. Data statements for natural lan-                        “masculinity,” and “femininity”: A meta-analytic review of gender differences
     guage processing: Toward mitigating system bias and enabling better science.                     in agency and communion. Psychological Bulletin (2021), 987–1011. https:
     Transactions of the Association for Computational Linguistics 6 (2018), 587–604.                 //doi.org/10.1037/bul0000343
 [6] Abeba Birhane, Vinay Uday Prabhu, and Emmanuel Kahembwe. 2021. Multimodal                   [31] Larry L Jacoby, Colleen Kelley, Judith Brown, and Jennifer Jasechko. 1989. Be-
     datasets: misogyny, pornography, and malignant stereotypes. arXiv preprint                       coming famous overnight: Limits on the ability to avoid unconscious influences
     arXiv:2110.01963 (2021).                                                                         of the past. Journal of personality and social psychology 56, 3 (1989), 326.
 [7] J Stewart Black and Patrick van Esch. 2020. AI-enabled recruiting: What is it and           [32] Andrew Karpinski and Ross B Steinman. 2006. The single category implicit
     how should a manager use it? Business Horizons 63, 2 (2020), 215–226.                            association test as a measure of implicit social cognition. Journal of personality
 [8] Piotr Bojanowski, Edouard Grave, Armand Joulin, and Tomas Mikolov. 2017.                         and social psychology 91, 1 (2006), 16.
     Enriching word vectors with subword information. Transactions of the Association            [33] Hadas Kotek, Rikker Dockum, Sarah Babinski, and Christopher Geissler. 2021.
     for Computational Linguistics 5 (2017), 135–146.                                                 Gender bias and stereotypes in linguistic example sentences. Language (2021).
 [9] Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T                [34] Tomas Mikolov, Edouard Grave, Piotr Bojanowski, Christian Puhrsch, and Ar-
     Kalai. 2016. Man is to computer programmer as woman is to homemaker?                             mand Joulin. 2018. Advances in Pre-Training Distributed Word Representations.
     debiasing word embeddings. Advances in neural information processing systems                     In Proceedings of the International Conference on Language Resources and Evalua-
     29 (2016), 4349–4357.                                                                            tion (LREC 2018).
[10] Marc-Etienne Brunet, Colleen Alkalay-Houlihan, Ashton Anderson, and Richard                 [35] Tomáš Mikolov, Wen-tau Yih, and Geoffrey Zweig. 2013. Linguistic regularities
     Zemel. 2019. Understanding the origins of bias in word embeddings. In Interna-                   in continuous space word representations. In Proceedings of the 2013 conference of
     tional Conference on Machine Learning. PMLR, 803–811.                                            the north american chapter of the association for computational linguistics: Human
[11] Aylin Caliskan. 2021. Detecting and mitigating bias in natural language process-                 language technologies. 746–751.
     ing. Brookings Institution (2021).                                                          [36] Saif M. Mohammad. 2018. Obtaining Reliable Human Ratings of Valence, Arousal,
[12] Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. 2017. Semantics derived                   and Dominance for 20,000 English Words. In Proceedings of The Annual Conference
     automatically from language corpora contain human-like biases. Science 356,                      of the Association for Computational Linguistics (ACL). Melbourne, Australia.
     6334 (2017), 183–186.                                                                       [37] Brian A Nosek, Frederick L Smyth, Natarajan Sriram, Nicole M Lindner, Thierry
[13] Aylin Caliskan and Molly Lewis. [n. d.]. Social biases in word embeddings and                    Devos, Alfonso Ayala, Yoav Bar-Anan, Robin Bergh, Huajian Cai, Karen Gon-
     their relation to human cognition. PsyArXiv.                                                     salkorale, et al. 2009. National differences in gender–science stereotypes predict
[14] Kaytlin Chaloner and Alfredo Maldonado. 2019. Measuring gender bias in word                      national sex differences in science and math achievement. Proceedings of the
     embeddings across domains and discovering new gender bias word categories. In                    National Academy of Sciences 106, 26 (2009), 10593–10597.
     Proceedings of the First Workshop on Gender Bias in Natural Language Processing.            [38] Charles E Osgood. 1964. Semantic differential technique in the comparative study
     25–32.                                                                                           of cultures 1. American Anthropologist 66, 3 (1964), 171–200.
[15] Tessa Charlesworth, Aylin Caliskan, and Mahzarin R. Banaji. 2022. Historical                [39] Charles Egerton Osgood, George J Suci, and Percy H Tannenbaum. 1957. The
     Representations of Social Groups Across 200 Years of Word Embeddings from                        measurement of meaning. Number 47. University of Illinois press.
     Google Books. Proceedings of the National Academy of Sciences (2022).                       [40] Amandalynne Paullada, Inioluwa Deborah Raji, Emily M Bender, Emily Den-
[16] Tessa ES Charlesworth and Mahzarin R Banaji. 2021. Patterns of Implicit and                      ton, and Alex Hanna. 2021. Data and its (dis) contents: A survey of dataset
     Explicit Stereotypes III: Long-Term Change in Gender Stereotypes. Social Psy-                    development and use in machine learning research. Patterns 2, 11 (2021), 100336.
     chological and Personality Science (2021), 1948550620988425.                                [41] Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. GloVe:
[17] Tessa ES Charlesworth, Victor Yang, Thomas C Mann, Benedek Kurdi, and                            Global Vectors for Word Representation. In Empirical Methods in Natural Lan-
     Mahzarin R Banaji. 2021. Gender stereotypes in natural language: Word embed-                     guage Processing (EMNLP). 1532–1543. http://www.aclweb.org/anthology/D14-
     dings show robust consistency across child and adult language corpora of more                    1162
     than 65 million words. Psychological Science 32, 2 (2021), 218–240.                         [42] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh,
[18] Sapna Cheryan and Hazel Rose Markus. 2020. Masculine defaults: Identifying                       Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark,
     and mitigating hidden cultural biases. Psychological Review 127, 6 (2020), 1022.                 et al. 2021. Learning transferable visual models from natural language supervision.
[19] Jacob Cohen. 2013. Statistical power analysis for the behavioral sciences. Academic              arXiv preprint arXiv:2103.00020 (2021).
     press.                                                                                      [43] Dominik Schlechtweg, Barbara McGillivray, Simon Hengchen, Haim Du-
[20] Ronan Collobert, Jason Weston, Léon Bottou, Michael Karlen, Koray Kavukcuoglu,                   bossarsky, and Nina Tahmasebi. 2020. Semeval-2020 task 1: Unsupervised lexical
     and Pavel Kuksa. 2011. Natural language processing (almost) from scratch.                        semantic change detection. arXiv preprint arXiv:2007.11464 (2020).
     Journal of machine learning research 12, ARTICLE (2011), 2493–2537.                         [44] Robyn Speer, Joshua Chin, Andrew Lin, Sara Jewett, and Lance Nathan. 2018.
[21] Maria De-Arteaga, Alexey Romanov, Hanna Wallach, Jennifer Chayes, Chris-                         LuminosoInsight/wordfreq: v2.2. https://doi.org/10.5281/zenodo.1443582
     tian Borgs, Alexandra Chouldechova, Sahin Geyik, Krishnaram Kenthapadi, and                 [45] Ryan Steed and Aylin Caliskan. 2021. Image representations learned with unsu-
     Adam Tauman Kalai. 2019. Bias in bios: A case study of semantic representa-                      pervised pre-training contain human-like biases. In Proceedings of the 2021 ACM
     tion bias in a high-stakes setting. In proceedings of the Conference on Fairness,                Conference on Fairness, Accountability, and Transparency. 701–713.
     Accountability, and Transparency. 120–128.                                                  [46] Autumn Toney-Wails and Aylin Caliskan. 2021. ValNorm Quantifies Seman-
[22] Sunipa Dev, Masoud Monajatipoor, Anaelia Ovalle, Arjun Subramonian, Jeff                         tics to Reveal Consistent Valence Biases Across Languages and Over Centuries.
     Phillips, and Kai-Wei Chang. 2021. Harms of Gender Exclusivity and Challenges                    Empirical Methods in Natural Language Processing (EMNLP) (2021).
     in Non-Binary Representation in Language Technologies. In Proceedings of the                [47] Laurens Van der Maaten and Geoffrey Hinton. 2008. Visualizing data using t-SNE.
     2021 Conference on Empirical Methods in Natural Language Processing. 1968–1994.                  Journal of machine learning research 9, 11 (2008).
[23] Alice H Eagly and Antonio Mladinic. 1989. Gender stereotypes and attitudes                  [48] Tianlu Wang, Xi Victoria Lin, Nazneen Fatema Rajani, Bryan McCann, Vicente
     toward women and men. Personality and social psychology bulletin 15, 4 (1989),                   Ordonez, and Caiming Xiong. 2020. Double-Hard Debias: Tailoring Word Em-
     543–558.                                                                                         beddings for Gender Bias Mitigation. In Association for Computational Linguistics
[24] Alice H Eagly and Antonio Mladinic. 1994. Are people prejudiced against women?                   (ACL).
     Some answers from research on attitudes, gender stereotypes, and judgments of               [49] Amy Beth Warriner, Victor Kuperman, and Marc Brysbaert. 2013. Norms of
     competence. European review of social psychology 5, 1 (1994), 1–35.                              valence, arousal, and dominance for 13,915 English lemmas. Behavior research
[25] Charles Elkan. 2003. Using the triangle inequality to accelerate k-means. In                     methods 45, 4 (2013), 1191–1207.
     Proceedings of the 20th international conference on Machine Learning (ICML-03).             [50] Laura Wendlandt, Jonathan K. Kummerfeld, and Rada Mihalcea. 2018. Factors
     147–153.                                                                                         Influencing the Surprising Instability of Word Embeddings. In Proceedings of


                                                                                           166


Contributed Paper                                                                                            AIES ’22, August 1–3, 2022, Oxford, United Kingdom


     the 2018 Conference of the North American Chapter of the Association for Com-             stamps, stores, strips, supermarket, swap, temp, template, templates,
     putational Linguistics: Human Language Technologies, Volume 1 (Long Papers).              trends, triangle, updated, websites, widget
     Association for Computational Linguistics, New Orleans, Louisiana, 2092–2102.
     https://doi.org/10.18653/v1/N18-1190                                                      Cooking and Kitchen: bake, Bake, baked, baking, cake, cakes,
[51] Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan. 2022. Evidence for Hy-              chocolate, Chocolate, cinnamon, coconut, Cookies, Cooking, cream,
     podescent in Visual Semantic AI. In Proceedings of the 2022 ACM Conference on
     Fairness, Accountability, and Transparency (ACM FAccT).
                                                                                               creamy, crust, cups, dairy, delicious, Delicious, dessert, dressing,
[52] Robert Wolfe, Mahzarin R Banaji, and Aylin Caliskan. 2022. Evidence for Hy-               egg, eggs, foods, Ginger, homemade, honey, Ingredients, lemon,
     podescent in Visual Semantic AI. arXiv preprint arXiv:2205.10764 (2022).                  milk, Milk, nutrition, organic, pumpkin, recipe, Recipe, recipes,
[53] Robert Wolfe and Aylin Caliskan. 2021. Low Frequency Names Exhibit Bias
     and Overfitting in Contextualizing Language Models. Proceedings of the 2021               Recipes, Salad, spice, spicy, sugar, sweet, tea, teaspoon, tsp, vanilla,
     conference on empirical methods in natural language processing (EMNLP) (2021).            vegan, vegetables, vegetarian, veggies, yogurt, yummy
[54] Robert Wolfe and Aylin Caliskan. 2022. Markedness in Visual Semantic AI. In Pro-          Fashion and Lifestyle: Autumn, Bag, Bags, Ballet, Barbie, Basket,
     ceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency
     (ACM FAccT).                                                                              Bathroom, Beads, Beautiful, Beauty, Bed, Bedroom, Bee, Bottom,
[55] Robert Wolfe and Aylin Caliskan. 2022. VAST: The Valence-Assessing Semantics              Boutique, Bracelet, Bridal, Bride, Butterfly, Cake, Candle, Candy,
     Test for Contextualizing Language Models. In Proceedings of the 36th AAAI
     Conference on Artificial Intelligence (AAAI).
                                                                                               Carnival, Carpet, Ceramic, Charm, Cherry, Clearance, Clothes, Col-
[56] Robert B Zajonc. 2001. Mere exposure: A gateway to the subliminal. Current                ors, Compact, Contemporary, Cookie, Coral, Costume, Cottage,
     directions in psychological science 10, 6 (2001), 224–228.                                Covers, Crafts, Cream, Crystal, Daisy, Dance, Dancing, Decor, De-
[57] Jieyu Zhao, Tianlu Wang, Mark Yatskar, Ryan Cotterell, Vicente Ordonez, and
     Kai-Wei Chang. 2019. Gender bias in contextualized word embeddings. arXiv                 signer, Designs, Desk, Diamonds, Dining, DIY, Doll, Dolls, Dreams,
     preprint arXiv:1904.03310 (2019).                                                         Dress, Dresses, Earrings, Egg, Emerald, Evening, Fabric, Fairy, Fancy,
                                                                                               Fashion, Favorites, Fiber, Floor, Floral, Flower, Flowers, Giveaway,
                                                                                               Gorgeous, Hair, Halloween, Heart, Heated, Honey, Inspired, Jeans,
A     APPENDIX                                                                                 Jewelry, Kiss, Kitty, Lace, Ladies, Laundry, Layer, Lovely, Loving,
Content Warning: The following clusters contain the most frequent                              Luxury, Makeup, Mesh, Metallic, Mint, Mirror, Mirrors, Nail, Natu-
1,000 female-associated and male-associated words in the lexicon                               ral, Necklace, Nylon, Passion, Pattern, Patterns, Pearl, Perfect, Pic-
with effect sizes 𝑑 ≥ 0.50. The results might be triggering.                                   ture, Pillow, Pink, Platinum, Plus, Powder, Pretty, Princess, Printed,
                                                                                               Pump, Queen, Rack, Ribbon, Romance, Romantic, Rose, Roses, Ruby,
                                                                                               Salon, Satin, Shades, Shape, Shipping, Shoes, Shoulder, Shower,
                                                                                               Silk, Simply, Skin, Sleeping, Smile, Soap, Soft, Spice, Split, Style,
A.1      Female Associated Clusters                                                            Sugar, Summer, Sunny, Swan, Sweet, Swim, Tea, Tops, Tote, Trend,
Advertising Words: ABOUT, BEST, CLICK, CONTACT, FIRST,                                         Trim, Tropical, Twilight, Unique, Valentine, Vampire, Vanity, Venus,
FREE, HERE, HOT, LOVE, MAC, MORE, NEXT, NOTE, NOW, OPEN,                                       Victorian, Vintage, Wear, Wedding, Weddings, Witch, Womens,
OR, OTHER, PLUS, SAVE, SEE, SPECIAL, STAR, TODAY, TWO,                                         Wonderful, Wrap, ∼, r
VERY, WITH, WOW                                                                                Female Names: Abbey, actress, Actress, Alice, Allison, Amanda,
Beauty and Appearance: accessories, adorable, adore, attractive,                               Amber, Amy, Ana, Andrea, Angela, Angie, Ann, Anna, Anne, Annie,
beads, beautiful, beauty, boutique, bracelet, bridal, bride, butterfly,                        Ashley, Barbara, Bella, Belle, Beth, Betty, Beverly, Bonnie, Britney,
candles, ceramic, charming, chic, clothes, clothing, coats, cocktail,                          Brooke, Buffy, Carol, Caroline, Carrie, Catherine, Charlotte, Cheryl,
colorful, colors, colours, coral, costume, costumes, crafts, crystal,                          Christina, Christine, Cindy, Claire, Clara, Clare, Courtney, Dana,
crystals, cute, dancers, decor, decorating, decorations, delicate, de-                         Dawn, Debbie, Deborah, Denise, Diana, Diane, Donna, Dorothy,
lightful, designer, designs, doll, dolls, dress, dresses, earrings, el-                        Elizabeth, Ellen, Emily, Emma, Erin, Eva, Eve, Gaga, Grace, Heather,
egance, elegant, ensemble, exotic, exquisite, fabric, fabrics, fab-                            Helen, Hilton, Holly, Ivy, Jackie, Jane, Janet, Jen, Jennifer, Jenny,
ulous, fairy, fashion, fashionable, feminine, floral, flower, flow-                            Jessica, Jill, Jo, Joan, Joy, Judy, Julia, Julie, Karen, Kate, Kather-
ers, footwear, fragrance, gorgeous, gown, hair, handbags, hand-                                ine, Kathleen, Kathy, Katie, Katrina, Katy, Kay, Kelly, Kim, Kristen,
made, heels, invitations, jewellery, jewelry, knit, knitting, lace,                            Lady, Laura, Lauren, Lily, Linda, Lindsay, Lisa, Liz, Louise, Loved,
ladies, lip, lovely, makeup, metallic, necklace, nylon, outfit, out-                           Lucy, Lynn, Madison, Madonna, Mae, Maggie, Mai, Mama, Mar-
fits, paired, pale, pattern, pearl, pendant, perfume, pillow, pink,                            garet, Maria, Marie, Marilyn, Marina, Married, Mary, Maya, Megan,
platinum, polish, princess, prom, purple, purse, quilt, ribbon, ro-                            Melissa, Mercedes, Met, Michelle, Miss, Molly, Mommy, Monica,
mantic, roses, satin, scent, sewing, sheer, silk, skirt, sleek, stitch,                        Ms, Ms., Nancy, Natalie, Nicole, Nikki, Nina, Olivia, Pam, Patricia,
stunning, styling, stylish, sweater, themed, tiny, trendy, vibrant,                            Paula, Penny, Rachel, Rebecca, Rihanna, Rosa, Sally, Samantha, San-
Vuitton, waist, wardrobe, wear, wedding, weddings, wonderful,                                  dra, Sara, Sarah, Savannah, Sharon, Shirley, singer, Sister, Sisters,
yarn                                                                                           Sophie, Spears, Stephanie, Sue, Susan, Tara, Tiffany, Tina, Vanessa,
Celebrities and Modeling: AMI, authors, availability, bio, blog-                               Victoria, Wendy, Whitney, Willow, xx, Yay
ger, bloggers, blogs, bookmark, browse, cell, checkout, class, classes,                        Health and Relationships: abortion, acne, addicted, addiction,
clicks, cluster, collections, contacting, coordinates, cosmetic, coupon,                       allergic, allergy, arthritis, aunt, babies, belly, breast, cancer, caring,
curves, date, designers, dot, engagement, giveaway, goodies, inex-                             celebrities, celebrity, chatting, cheating, clinic, complications, coun-
pensive, info, invites, layout, libraries, litter, magazine, magazines,                        seling, couple, couples, dancer, DD, depressed, depression, diabetes,
markers, matching, measurements, membrane, model, modeling,                                    disabilities, disorder, distress, donor, emotionally, experiencing, girl-
models, ms, newest, null, on-line, patterns, peek, photograph, pho-                            friend, grandmother, healthier, her, hers, herself, hips, hormones,
tos, photostream, pictures, pumps, registry, reserved, royalty, sam-                           inspirational, lady, literacy, lover, loving, marriage, messy, mom,
ple, samples, scans, separated, shipping, shopping, shops, spanish,


                                                                                         167


Contributed Paper                                                                                   AIES ’22, August 1–3, 2022, Oxford, United Kingdom


moms, mother, mothers, mum, nurse, nurses, nursing, obsessed, ob-                     Major, Man, Mario, Marvel, Master, Max, Military, Motion, Nation,
session, oral, parent, parenting, passionate, poems, pose, poses, preg-               Navy, Numbers, Of, Official, Orchestra, Original, Oxford, Pack, Part,
nancy, pregnant, protective, relationship, relationships, romance,                    Pass, Points, Prime, Prince, Quote, Rank, Raw, Records, Remix,
seniors, sensitive, sexuality, she, She, sister, sisters, skin, stories,              remix, Reserve, Retrieved, Return, Revolution, Rise, Rock, Rocky,
stressful, supportive, survivors, syndrome, therapist, therapy, toes,                 Roll, Rule, Running, Rush, Score, Scottish, Shirt, Shot, Six, Sound,
toxic, tumor, vampire, witch, wives, woman, women                                     Stand, Strong, Super, Ten, Tiger, Trail, Trial, Ultimate, views, Vol,
Luxury and Lifestyle: accommodations, Apartment, balcony, bath,                       Volume, Wall, War, Wars, Way, Will, Wolf
bathroom, bathrooms, beaches, bedroom, carpet, catering, closet,                      Big Tech: .0, 1.1, 2.0, 3.0, Android, Answers, API, App, Applications,
cottage, cozy, cruise, Enjoy, enjoys, flats, gardening, holidays, inti-               Audio, Build, Canon, Cisco, Cloud, Command, Computer, contribs,
mate, kitchen, laundry, luxurious, luxury, massage, mattress, out-                    CPU, demo, developer, Developer, developers, Documents, Error,
doors, pets, queen, relaxing, rooms, Rooms, salon, sandy, shower,                     Firefox, Flash, Forums, Galaxy, Gaming, GMT, Google, GPS, HP,
showers, soap, Spa, spa, sunny, swim, swimming, tile, tub, vacations,                 IBM, Install, Intel, Intelligence, Internet, Introduction, iOS, iPhone,
wellness, yoga                                                                        Java, JavaScript, Linux, Message, Microsoft, MP3, NET, Nintendo,
Obscene Adult Material: anal, babe, babes, bikini, bitch, blonde,                     Notes, OS, PC, Player, plugin, Problem, Programming, PS3, Ques-
blowjob, boob, boobs, bra, breasts, brunette, busty, chick, chicks,                   tions, Re, RE, Remote, replies, RSS, Samsung, Security, SEO, Server,
cum, cunt, dildo, ebony, erotic, escort, facial, flashing, fucked, gal,               SMS, Software, SQL, Statistics, Test, User, Users, Wii, Windows,
galleries, gallery, girl, girls, hentai, horny, hot, hottest, juicy, kissing,         Wireless, Xbox, XML, XP, YouTube
latex, lesbian, lesbians, lick, licking, lingerie, mature, milf, movies,              Engineering and Automotive: AC, Advance, Audi, Auto, Auto-
naked, naughty, nipples, nude, orgasm, panties, penetration, pics,                    motive, Bar, Battery, BMW, Built, Button, Cap, Charger, Chevro-
posing, pussy, sexy, shemale, slut, stockings, sucking, teen, teens,                  let, Chrome, Circuit, Construction, Contractors, Custom, Dodge,
tit, tits, webcam, wet, whore, xxx                                                    Doors, Driver, Driving, Duty, Economy, Electric, Engine, Engineer,
Sexual Profanities: 00, Amateur, Anal, Asian, Ass, Babe, Blonde,                      Engineering, Equipment, Extra, Fishing, Fuel, Garage, Gas, Gear,
Busty, Cum, Cute, Ebony, Facial, Fucked, Galleries, Girl, Girls, Her,                 General, GM, Golf, Guard, Hardware, Heating, Heavy, Honda, Indus-
Horny, Hot, Huge, Lesbian, Mature, Mom, Moms, Movies, Naked,                          trial, Laser, Logo, Machine, Maintenance, Manual, Manufacturing,
Nude, Pics, Pictures, Porn, Pussy, Sex, Sexy, Teen, Teens, Tight, Tits,               Metal, Motor, Nissan, Oil, Pocket, Portable, Power, Premium, Pres-
Wet, Wife, XXX                                                                        sure, Printing, Pro, Quick, Racing, RC, Repair, Rod, Signs, Solar,
Web Article Titles: Absolutely, Acne, Across, Addiction, Adelaide,                    Solid, Speed, Sport, Standard, Steel, System, Tech, Technical, Tool,
Advertise, Affordable, Alberta, Apply, Aurora, Awareness, Bache-                      Tools, Toyota, Trade, Trading, Training, Transfer, Transport, Truck,
lor, Benefit, Biggest, Blogger, Bollywood, Breast, Calendar, Cancel,                  Universal, Upper, Wood, Yamaha
Cancer, Caribbean, Celebrity, Changing, Choice, Choosing, Classes,                    Engineering and Electronics: assembly, audio, auto, automotive,
Closed, Collections, Compliance, Consumer, Consumers, Contest,                        backup, batteries, blade, brass, build, built, capable, charge, charg-
Coordinator, Counseling, Created, Cruise, Cure, Czech, Dakota,                        ing, chip, circuit, command, commands, computing, conditioning,
Dates, Denmark, Designers, Destination, Diabetes, Diet, Disclaimer,                   console, construction, contractor, contractors, controller, conver-
Eating, eBook, Editorial, Engagement, ER, Everyday, Exclusive, Ex-                    sion, convert, converted, custom, dealer, dealers, driver, durable,
plore, Factor, Fiction, Finding, Fitness, Food, Foods, Gallery, Get-                  duty, electronics, enabled, engine, engineer, engineering, engineers,
ting, Health, Healthy, Holidays, Inspiration, Languages, Libraries,                   engines, enterprise, execution, formation, gate, gear, general, gen-
Lifestyle, Lots, Magazine, Massage, Model, Models, Month, MS,                         eration, header, install, legacy, lightweight, logic, manual, master,
MSN, Multiple, Naturally, Newsletter, non-profit, nonprofit, Novel,                   motor, operation, physics, pipe, power, printer, printing, proven,
Nurse, Nursing, Nutrition, Oral, Parties, Patent, Patient, Platform,                  receiver, reference, remote, repair, replace, replacement, restoration,
Pregnancy, Privacy, Purchase, Readers, Reality, Recently, Reception,                  rod, root, scheme, seal, security, setup, software, solution, superior,
Registry, Relationship, Relationships, Reserved, Rica, Runtime, Sam-                  suspension, tire, transfer, trucks, upgrade
ple, Scenes, Secret, Secrets, Seller, Shared, Shares, Sharing, Shows,                 God and Religion: Abraham, according, According, Allah, ap-
Sierra, Sites, Spotlight, Statement, Student, Target, Teacher, Teach-                 pointed, authority, bear, bears, believed, Bible, blind, brothers, cen-
ers, Templates, Therapy, Totally, Treat, Trends, Updates, VIP, Virgin,                tury, Christ, Christianity, Christians, commentary, composed, cre-
Virtual, Vitamin, Voices, Wellness, Whole, Winners, Women, Write,                     ator, evil, evolution, Father, favor, followers, fool, genius, glory, God,
Yoga                                                                                  god, Gospel, he, He, himself, His, Holy, holy, hundred, Islam, Israel,
                                                                                      Jerusalem, Jesus, Jews, king, kingdom, land, Lord, man, mere, Mus-
                                                                                      lims, nations, passage, philosophy, poor, Pope, possession, praise,
A.2     Male Associated Clusters                                                      principle, quote, referred, refers, regard, regarded, respect, reward,
Adventure and Music: ", ’, 1972, Against, Answer, Arms, Articles,                     Roman, Rome, rule, sacrifice, sheep, sin, sir, Son, sword, temple,
Back, Band, Bass, Batman, Battle, Bear, Beat, Beer, Blues, Brain,                     theory, tho, thou, Thus, tradition, translation, united, unto, verse,
Brother, Brothers, Bull, Camp, Champion, Cold, Comedy, Cool,                          wise, worthy, ye
Count, Crew, Da, Dead, Death, Devil, Die, DJ, Dog, Dragon, Eagle,                     Male Names: Aaron, actor, Adam, Al, Alan, Albert, Alex, Allen,
Empire, End, EP, Essential, Evil, Evolution, Fans, feat, Fight, Fish,                 Andrew, Andy, Anthony, Arthur, Barry, Ben, Bill, Billy, Bishop, Bob,
Flying, Force, Four, Future, Game, Ghost, Giant, Great, Green, Guitar,                Bobby, Brad, Brandon, Brian, Brown, Bruce, Bryan, Captain, Carl,
Gun, Guys, Hat, Head, Hero, Hood, II, III, Iron, IV, Jazz, Jump, King,                Carlos, CEO, Chairman, chairman, Charles, Chief, Chris, Christo-
Kingdom, Kings, Knight, Late, Leader, Legend, Lincoln, Lion, LP,                      pher, Chuck, Clay, Craig, Dan, Daniel, Danny, Dave, David, Dennis,


                                                                                168


Contributed Paper                                                                                 AIES ’22, August 1–3, 2022, Oxford, United Kingdom


Dick, Don, Donald, Doug, Duke, Ed, Eddie, Eric, Francis, Frank,                      A.3    Big Tech Words
Franklin, Fred, Gary, Gates, George, Glenn, Gordon, Governor, Greg,                  965 Big Tech Words: 23andMe, 3Com, 3COM, 3Par, 3PAR, 7dig-
Guy, Harrison, Harry, Henry, Howard, Ian, Jack, Jackson, Jacob, Jake,                ital, 9to5Google, 9to5mac, 9to5Mac, AAPL, ABBYY, Accenture,
James, Jason, Jay, Jeff, Jefferson, Jeremy, Jerry, Jim, Jimmy, Joe, Joel,            Acer, Acronis, Activision, Acxiom, AdAge, Adaptec, Adidas, Ad-
John, Johnny, Johnson, Jon, Jonathan, Joseph, Josh, Jr., Juan, Justin,               Mob, Admob, Adobe, AdSense, Adsense, AdWords, Adwords, Agi-
Keith, Ken, Kevin, Kyle, Larry, Luke, Marc, Mark, Marshall, Martin,                  lent, Airbnb, Airbus, Airtel, Akamai, Albanesius, Alcatel, Alcatel-
Matt, Matthew, Mayor, Michael, Mike, Miles, Morris, Mr, Mr., Mur-                    Lucent, Alibaba, Alibaba.com, Alienware, AllFacebook, AllThingsD,
ray, Nathan, Neil, Nelson, Nick, Norman, Oliver, Patrick, Paul, Pete,                AltaVista, Altera, Amazon, Amazon.com, AMD, Amdocs, AmEx,
Peter, Phil, Philip, Ralph, Randy, Rich, Richard, Rick, Rob, Robert,                 AMZN, Anandtech, AnandTech, Andoid, Andreessen, Andriod, An-
Robinson, Roger, Ron, Roy, Russell, Ryan, Sam, Samuel, Scott, Sean,                  droid, ANDROID, android, Android-based, Android-powered, An-
Simon, Sir, Stanley, Stephen, Steve, Steven, Ted, Terry, Thomas,                     droidPIT, anti-competitive, anti-trust, anticompetitive, Antitrust,
Tim, Tom, Tommy, Tony, Troy, Victor, Vincent, W., Walter, Wayne,                     antitrust, AOL, AOpen, API, APIs, Appcelerator, AppEngine, Ap-
William                                                                              ple, APPLE, Apple.com, AppleInsider, AppleTV, Appstore, app-
Non-English Tokens: al, Barcelona, con, da, DE, del, der, des, di,                   store, AppStore, AppUp, Archos, Ariba, ARM-based, Ask.com, AS-
du, e, ed, El, el, et, le, Madrid, o, par, que, se, un, van                          Rock, AstraZeneca, Asus, ASUS, asus, ASUSTeK, Asustek, ATandT,
Numbers, Dates, and Metrics: -1, 103, 111, 113, 1500, 160, 2.4, 200,                 Atari, Atheros, ATi, ATI, Atlassian, Atmel, Atom-based, Atos, Atrix,
220, 240, 250, 2d, 300, 3000, 320, 360, 400, 450, 500, 51, 600, 700, 73,             AuthenTec, Autodesk, automaker, Automattic, Avanade, Avaya,
77, 900, [, acres, BC, C, c., D, d, ft, ft., G, Given, k, MP, No., O, OF, P,         Avira, Avnet, AWS, Baidu, baidu, Baidu.com, Ballmer, Barclays,
p, p., Per, pp., R, SS, St, U., v, v., W, £                                          Bazaarvoice, BBRY, BenQ, BestBuy, Bestbuy, BetaNews, Betrieb-
Sports: backs, ball, band, baseball, basketball, bass, bat, beat, beaten,            ssystem, Bezos, BIDU, Bing, Biogen, Bitcoin, Bitdefender, BitTorrent,
beating, beer, bench, betting, blues, boss, buddy, camp, captain,                    BlackBerry, Blekko, Blinkx, bloatware, BloggingStocks, Bloomberg,
champion, championship, cheat, coach, coaches, coin, crew, de-                       BlueStacks, Boeing, BofA, Box.net, Boxee, Brightcove, Broadcom,
cent, defensive, don, draft, drum, drums, dude, elite, epic, era, fans,              Brocade, BSkyB, Bungie, BusinessWeek, Buy.com, BuzzFeed, BYD,
fellow, finest, fishing, football, franchise, gambling, game, games,                 Canalys, Canonical, Capgemini, carmaker, Carphone, CCleaner,
gaming, golf, grand, great, greatest, guard, guitar, guy, guys, heads,               CentOS, ChannelWeb, Chegg, China, China-based, Chinavasion,
hero, hockey, hunting, idiot, injuries, injury, jazz, jersey, jokes,                 chip-maker, Chipmaker, chipmaker, chipmakers, chipset, chipsets,
kick, league, legend, legendary, lineup, manager, mark, mate, mi-                    Chipzilla, Chitika, Chromebook, ChromeBook, Chromebooks,
nor, musicians, offense, offensive, pass, passes, passing, penalty, pit,             ChromeOS, CinemaNow, CIO.com, Cisco, CISCO, CISPA, Citi,
pitch, player, players, points, pound, premier, prime, pro, prospect,                Citibank, Citigroup, Citrix, Cleantech, Clearwire, closed-source,
prospects, racing, rally, rank, recruiting, retired, rotation, rush,                 cloud-computing, Cloudera, CNET, CNet, Cnet, cnet, Coca-Cola,
saves, score, scored, scoring, serving, solid, sport, sports, squad,                 Cognizant, Comcast, Compal, companies, company, Compaq, Comp-
stadium, starter, stats, suspended, tackle, team, teams, thread, ton,                TIA, ComputerWorld, Computerworld, Computex, ComScore, Com-
tournament, trade, trading, tribute, tricks, ultimate, versus, veteran,              score, comScore, Conexant, Cooliris, Corp, Costolo, Coursera, Cr-48,
victory, wing, yard, yards, zone                                                     crapware, Cringely, CrunchBase, CSCO, CUDA, Cupertino, Cupertino-
Sports and Cities: 2014, AL, Antonio, Arena, Athletic, Baltimore,                    based, CyanogenMod, Cyanogenmod, CyberLink, Cyberlink, Cy-
Baseball, Basketball, Bay, Bears, Boston, Bowl, Buffalo, Champions,                  bersecurity, cybersecurity, D-Link, DailyTech, Daimler, Danone,
Championship, Chicago, Cincinnati, Cleveland, Columbus, Dallas,                      DARPA, Datacenter, Deezer, Dell, DELL, Deloitte, DeNA, Dhin-
Detroit, Diego, Draft, Eagles, England, ESPN, FC, Football, Giants,                  gana, DigiTimes, Digitimes, DisplayLink, DisplayPort, DivX, Do-
Highlights, Hockey, Indians, Jersey, Jose, Junior, League, Lions, Liv-               CoMo, Docomo, DOCOMO, DoJ, DOJ, DoubleClick, Doubleclick,
erpool, Louis, Louisville, Manchester, Milwaukee, Minnesota, MLB,                    DreamHost, Dropbox, DropBox, E-Commerce, E-Readers, EBay,
MLS, Montreal, NBA, NCAA, NFL, NHL, Nike, Oakland, Orlando,                          eBay, Ebay, Ebuyer, eCommerce, Ecosystem, ecosystem,
Penn, Philadelphia, Pittsburgh, Players, Premier, Rangers, Saints,                   Electricpig.co.uk, Electronista, Elop, Eloqua, eMachines, Emachines,
San, SEC, Soccer, Sox, Sports, St., Stadium, Tampa, Team, Ticket,                    eMarketer, EMC, Emulex, Endeca, Engadget, engadget, Epson, Er-
Tickets, Tigers, Tournament, United, vs, vs., Yankees                                icsson, Erictric, ESET, Esri, Etisalat, Everex, Evernote, EVGA, eWeek,
War and Violence: against, Army, army, arrest, arrested, attack,                     Experian, ExtremeTech, Exxon, ExxonMobil, Exynos, F-Secure, Face-
ban, battle, bin, Bush, charges, chief, cited, combat, commit, com-                  book, FaceBook, Facebooks, FedEx, Feedly, Firefox, Flextronics, Flip-
mitted, corruption, crimes, criminal, dead, defeat, defeated, defense,               board, Flipkart, Fortinet, FOSS, Foxconn, foxconn, Foxit, FreeBSD,
Defense, destruction, enemies, enemy, executed, fight, fighter, fight-               Freescale, Frito-Lay, FTC, Fudzilla, Fujifilm, Fujitsu, Fusion-io, Gad-
ing, fights, fought, fraud, governor, gun, guns, heroes, illegal, in-                geTell, Gaikai, Gameloft, GameStop, Gartner, Gawker, GE, Geek.com,
jured, intelligence, Iraq, Iraqi, kill, killed, killing, leader, leaders,            GeekWire, GeForce, Geforce, Gemalto, Genentech, Geohot, Get-
leadership, led, march, military, minister, officers, opponents, oppo-               Jar, Gigabyte, GIGABYTE, GigaOm, GigaOM, GitHub, Github, Giz-
sition, personnel, prison, province, racist, regime, revolution, ruled,              modo, Glassdoor, GlaxoSmithKline, Gmail, GMail, GMAIL, go-to-
soldier, soldiers, spokesman, supporters, tactics, terror, terrorist,                market, GoDaddy, Godaddy, GoGrid, GOOG, Google, GOOGLE,
troops, veterans, violent, war, wars, weapons                                        Google-owned, Google.com, Googler, Googlers, Googles, GoogleTV,
                                                                                     Googleâ, Goolge, GoPro, gOS, GottaBeMobile.com, Gowalla, Gphone,
                                                                                     GPU, GPUs, Groupon, GSK, GSMA, GSMArena, H-P, Hackathon,


                                                                               169


Contributed Paper                                                                           AIES ’22, August 1–3, 2022, Oxford, United Kingdom


Hackintosh, hackintosh, Hadoop, Haier, Hanvon, HD-DVD, Heroku,                 Sony, sony, SONY, Sophos, SoundCloud, SourceForge, SpaceX, Span-
Hewlett-Packard, Hisense, Hitachi, Honeywell, Hootsuite, Horton-               sion, Splashtop, Splunk, Spotify, Spreadtrum, Sprint-Nextel, Star-
works, HotHardware.com, Hotmail, HP, HPQ, HSBC, HTC, htc,                      bucks, Stardock, startups, Startups, STMicroelectronics, Success-
HTML5, Huawei, huawei, HUAWEI, HubSpot, Hulu, Hynix, I.B.M.,                   Factors, SugarCRM, SugarSync, Sumsung, Sunnyvale, SunPower,
i7500, IaaS, iAd, iAds, IBM, ibm, IBMs, Icahn, iClarified, iCloud,             Supermicro, superphone, SUSE, SuSE, SwiftKey, Swisscom, Swype,
Ideapad, IDEOS, IDG, IE10, IE8, IE9, iFixit, iMessage, Informat-               Sybase, Symantec, Synaptics, Synnex, Synopsys, T-Mobile, T-mobile,
ica, InformationWeek, Infosys, InfoWorld, Inktomi, INTC, Intel,                TalkTalk, Taobao, tech, TechCrunch, Techcrunch, techcrunch,
INTEL, Intel-based, Intels, InterDigital, internetnews.com, Internet-          techcrunch.com, Techdirt, TechEye, TechFlash, TechHive, Tech-
News.com, InterVideo, Intuit, Inventec, Iomega, iOS, iPad3, iPhone,            meme, TechNewsWorld, TechnoBuffalo, TechRadar, TechSpot, Tech-
iPhone5, iPhones, IPO, iRobot, iTablet, ITProPortal, iTWire, IT-               Web, Tegra, telco, Telco, telcos, Telcos, Telefonica, Telefónica, Te-
world.com, iWatch, iWork, JBoss, JetBlue, Jolicloud, Joyent, JP-               lenor, TeliaSonera, Telstra, Tencent, Teradata, Tesco, Tesla,
Morgan, JR.com, Kaltura, Kaspersky, KDDI, Kinect, Klout, Kobo,                 ThinkGeek, Thinkpad, ThinkPad, TIBCO, Tibco, Ticketmaster,
KPMG, LastPass, Lenovo, lenovo, LENOVO, LePhone, Lexmark,                      TigerDirect, TiVo, Tizen, TMobile, TomTom, Torvalds, Toshiba,
LG, Liliputing, LiMo, Lindows, LinkedIn, Linkedin, Linksys, Lin-               toshiba, TouchPad, Touchpad, Toyota, Transmeta, TRENDnet, TSMC,
spire, Linux, Lite-On, Livescribe, LiveSide.net, Lodsys, Logitech,             Tudou, Turkcell, Twilio, Twitter, Uber, Ubergizmo, Ubisoft, Ubuntu,
LogMeIn, Lucasfilm, Lucent, Lufthansa, Lumia, Lytro, MacDai-                   Udacity, UEFI, Ultrabook, ultrabook, Ultrabooks, ultrabooks, Unilever,
lyNews, MacMall, MacOS, MacRumors, Magento, MakerBot, Mal-                     Unisys, uTorrent, UX, V3.co.uk, Valleywag, VatorNews, Venture-
ware, Malwarebytes, Marketshare, marketshare, Marvell, Mashable,               Beat, VeriFone, Verisign, VeriSign, Verizon, Vertica, Vevo, Viacom,
MasterCard, Mastercard, Mattel, McAfee, McKesson, McKinsey,                    Viadeo, Viber, Vidyo, ViewSonic, Viewsonic, VirnetX, VirtualBox,
McNealy, MediaTek, Mediatek, Medion, Meebo, MeeGo, Meego,                      Visa, Vizio, VIZIO, Vlingo, VMware, VMWare, Vmware, Vodafone,
Meizu, Mellanox, Mendeley, Merck, MetroPCS, Microchip, Micro-                  Vodaphone, Volusion, VP8, VPN, vPro, VR-Zone, Vringo, Vuze, Vy-
electronics, Micron, Microsft, Microsoft, MicroSoft, MIcrosoft, mi-            atta, VZW, W3C, Wacom, Wal-Mart, Walmart, Walmart.com, Waze,
crosoft, MICROSOFT, Microsofts, MicroStrategy, Micrsoft, Mir-                  WebEx, Webkit, WebKit, WebM, WebOS, webOS, Webroot, Web-
cosoft, MIT, Mitel, mobile-device, MobileCrunch, MobiTV, mo-                   sense, Weibo, WhatsApp, Whatsapp, WiDi, WikiLeaks, Wikileaks,
coNews, Monoprice, Monsanto, Motherboard, Moto, Motorola, mo-                  WildTangent, WiMax, WiMAX, Win7, Win8, WinBeta, Windows,
torola, Motorolla, Mozilla, Mozy, MSFT, multinationals, Multitouch,            WIndows, Windows7, Windows8, WinRumors, Wintel, Wipro,
multitouch, MVNO, MySQL, Napster, NASA, Nasdaq, NASDAQ,                        Wistron, WMPoweruser, Woz, WP7, WP8, WSJ, WWDC, x86, X86,
Navteq, Neowin, Neowin.net, Nestle, Nestlé, NetApp, Netbook,                   Xbox, XBox, XCode, XDA, Xerox, Xiaomi, Xilinx, Xobni, Xoom,
Netezza, Netflix, NetFlix, Netgear, NetGear, NETGEAR, Netscape,                XOOM, Xperia, Yahoo, Yammer, Yandex, Yarow, Yelp, YHOO, Youku,
NetSuite, Newegg, NewEgg, newegg, Newegg.com, NewEgg.com,                      YouTube, Zappos, ZDNet, ZDnet, Zenbook, Zendesk, Zillow, Zim-
news.cnet.com, NewsFactor, Nextag, Nexus, Nike, Nimbuzz, Nin-                  bra, Zoho, Zotac, ZTE, Zuckerberg, Zynga
tendo, Nokia, nokia, NOKIA, non-Apple, Nortel, Novartis, Nov-
ell, NSA, NSDQ, Nuance, NVDA, Nvidia, NVIDIA, NVidia, nVidia,
nVIDIA, nvidia, NXP, OCZ, OEM, OEMs, OLED, OLPC, Omniture,
OmniVision, Onkyo, OnLive, Onlive, Open-Source, open-source,
open-sourced, OpenCL, OpenDNS, OpenFeint, OpenSocial, Open-
Solaris, opensource, OpenStack, Optus, Oracle, ORCL, Orkut, OSes,
OSX, Otellini, Outlook.com, Ouya, OUYA, Overstock.com, PaaS,
paidContent, PalmOne, Panasonic, PandoDaily, Pantech, Paper-
master, patent-infringement, PayPal, Paypal, PCMag, PCMag.com,
PCWorld, Pegatron, Pepsi, PepsiCo, Pepsico, Pfizer, Phablet, ph-
ablet, PhoneArena, Phoronix, Pichai, Pixar, Pixel, Plantronics, Plaxo,
Play.com, Playdom, Pogoplug, Polycom, PopCap, post-PC, Postini,
PowerDVD, Powerset, PowerVR, pre-IPO, PS4, Psystar, Publicis,
PwC, QCOM, Qihoo, QLogic, QNAP, Quad-Core, Qualcomm, qual-
comm, QUALCOMM, Quantcast, Quickoffice, QuickOffice, Quora,
Rackspace, RackSpace, Radeon, Rakuten, Ralink, Rambus, Raytheon,
Razer, Rdio, ReadWriteWeb, RealNetworks, Realtek, Redbox, Reddit,
RedHat, Redhat, Redmond-based, Renesas, Renren, RHEL, RightScale,
RIM, RIMM, Roku, Rovio, SaaS, Safaricom, Salesforce, SalesForce,
salesforce, Salesforce.com, SalesForce.com, salesforce.com, Sam-
sung, samsung, SAMSUNG, Samsungs, SanDisk, Sandisk, Sanofi,
SAP, Scoble, Scobleizer, SDK, SDKs, Seagate, search-engine, Seesmic,
Semiconductor, Set-Top, SGX, Shopify, Silicon, SiliconANGLE, Sil-
iconBeat, Singtel, SingTel, Sinofsky, SkyDrive, Skype, Slashdot,
Smartphone, smartphone, smartphones, Smartphones, smartwatch,
SoftBank, Softbank, Softpedia, software, SolarCity, SonicWall, Sonos,


                                                                         170
