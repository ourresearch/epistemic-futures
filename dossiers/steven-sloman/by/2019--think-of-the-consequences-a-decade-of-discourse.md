---
title: "Think of the Consequences: A Decade of Discourse about Same-Sex Marriage"
person: steven-sloman
section: by
type: journal-article
year: 2019
venue: ""
authors: "Babak Hemmatian, Sabina Sloman, Uriel Cohen Priva, Steven A. Sloman"
source_url: https://doi.org/10.31234/osf.io/c7r54
openalex_id: W4234231735
doi: https://doi.org/10.31234/osf.io/c7r54
cited_by_count: 1
retrieved: 2026-08-13
content: full-text
notes: "preprint version; OA: https://doi.org/10.31234/osf.io/c7r54; Full text from the author-deposited OSF/PsyArXiv preprint (osf.io), extracted from the deposited manuscript."
---

# Think of the Consequences: A Decade of Discourse about Same-Sex Marriage

## Abstract (from OpenAlex metadata)

Approaching issues through the lens of non-negotiable values increases the perceived intractability of debate (Baron &amp;amp; Spranca, 1997), while focusing on concrete consequences of policies instead results in the moderation of extreme opinions (Fernbach et al., 2013) and greater likelihood of conflict resolution (Baron &amp;amp; Leshner, 2000). Using comments on the popular social media platform Reddit from January 2006 until September 2017, we show how changes in the framing of same-sex marriage in public discourse relate to changes in public opinion. We use a topic model to show that the contribution of certain protected-values-based topics to the debate (religious arguments and freedom of opinion) increased prior to the emergence of a public consensus in support of same-sex marriage (Gallup, 2017), and declined afterwards. In contrast, discussion of certain consequentialist topics (the impact of politicians’ stance and same-sex marriage as a matter of policy) showed the opposite pattern. Our results reinforce the meaningfulness of protected values and consequentialism as relevant dimensions for describing public discourse and highlight the usefulness of unsupervised machine learning methods in tackling questions about social attitude change.

## Full text

Running Head: THINK OF THE CONSEQUENCES

Please cite as: Hemmatian, B., Sloman, S.J., Cohen Priva, U., & Sloman, S.A. (in press). Think
of the consequences: A decade of discourse about same-sex marriage. Behavior Research
Methods.

© The Psychonomic Society, Inc. 2019. This is a pre-print of an article to be published in
Behavior Research Methods. The final authenticated version will be available online at:
https://doi.org/10.3758/s13428-019-01215-3 upon publication.

THINK OF THE CONSEQUENCES

1

Think of the Consequences: A Decade of Discourse About Same-Sex Marriage

Babak Hemmatian
Brown University
Sabina J. Sloman
Carnegie Mellon University
Uriel Cohen Priva and Steven A. Sloman
Brown University

Author Note
Babak Hemmatian, Department of Cognitive, Linguistic and Psychological Sciences,
Brown University; Sabina J. Sloman, Department of Social and Decision Sciences, Carnegie
Mellon University; Steven A. Sloman, Department of Cognitive, Linguistic and Psychological
Sciences, Brown University; Uriel Cohen Priva, Department of Cognitive, Linguistic and
Psychological Sciences, Brown University.
Earlier versions of results included in this paper were presented at Heterodox Psychology
Workshop held at Chapman University in Orange, CA, USA, in August 2018, and at the 39th
Annual Conference of Society for Judgment and Decision-making in New Orleans, LA, USA in
November 2018.
This publication was made possible through a grant from the Intellectual Humility in
Public Discourse Project at the University of Connecticut and the John Templeton Foundation.

THINK OF THE CONSEQUENCES

2

Correspondence should be addressed to Babak Hemmatian, Department of Cognitive,
Linguistic and Psychological Sciences, Brown University, Providence, RI 02906. Email:
Babak_Hemmatian@Brown.edu. Phone: (401)680-3879.
Word count: 9430 words (excluding title, references, author affiliations and note,
acknowledgments, appendices, figures and figure legends)

THINK OF THE CONSEQUENCES

3

Abstract
Approaching issues through the lens of non-negotiable values increases the perceived
intractability of debate (Baron & Spranca, 1997), while focusing on concrete consequences of
policies instead results in the moderation of extreme opinions (Fernbach et al., 2013) and greater
likelihood of conflict resolution (Baron & Leshner, 2000). Using comments on the popular social
media platform Reddit from January 2006 until September 2017, we show how changes in the
framing of same-sex marriage in public discourse relate to changes in public opinion. We use a
topic model to show that the contribution of certain protected-values-based topics to the debate
(religious arguments and freedom of opinion) increased prior to the emergence of a public
consensus in support of same-sex marriage (Gallup, 2017), and declined afterwards. In contrast,
discussion of certain consequentialist topics (the impact of politicians’ stance and same-sex
marriage as a matter of policy) showed the opposite pattern. Our results reinforce the
meaningfulness of protected values and consequentialism as relevant dimensions for describing
public discourse and highlight the usefulness of unsupervised machine learning methods in
tackling questions about social attitude change.
Keywords: Protected values, consequentialism, Same-sex marriage, Latent Dirichlet
Allocation, Reddit

THINK OF THE CONSEQUENCES

4

Introduction
A good negotiator will acknowledge their opponent’s most basic values, but not try to
change them (Atran, Axelrod, & Davis, 2007). All but the most transactional of us have
protected or sacred values that we regard as non-negotiable (Baron & Spranca, 1997). Protected
values are deontological in Kant’s (1797) sense: They are prescriptions or prohibitions regarding
actions and are not as much affected by the outcomes of those actions. Decisions that do focus on
outcomes (e.g. maximizing expected utility) are sometimes called consequentialist. In this paper,
we review evidence suggesting that consequentialist discourse leads to more intellectual
openness and potential for attitude change than discourse about protected values. We test the
claim by examining the amount of discourse of each type in discussions of an issue as public
opinion about it changed over time. The issue is whether same-sex marriage should be legal.
Protected values are common. Many refuse to consider abortion because they believe that
the act is murder, and they possess a protected value that prohibits murder, regardless of the
consequences of aborting or not aborting. Sometimes protected values conflict with one another.
One might believe that abortion is murder and that a woman has a fundamental right to choose
what happens to her body. People use various strategies to justify violating deeply-held moral
principles (Baron & Leshner, 2000; Tetlock, 2003).
When two sides with incommensurable protected values are debating policy, focusing on
those values is not likely to help achieve conciliation. Indeed, evidence suggests that highlighting
protected values hardens attitudes. Dehghani and colleagues (2009) argued that the Iranian
government managed to obtain support from their citizenry to pursue a nuclear program by
launching a campaign to frame possession of a nuclear industry to be an inalienable right, a
protected value.

THINK OF THE CONSEQUENCES

5

A more promising approach to overcoming policy divides may be to focus on the
consequences of the policy (Baron & Spranca, 1997). Asking people to consider the likely
outcomes of a policy makes them more open to compromise. This type of consequentialist
reasoning is a kind of causal reasoning: it is concerned with the effects of policies, the
probabilities of those effects, and how good or bad they are (a different type of value)1. Tanner,
Medin, and Iliev (2008) have shown this empirically: They probed people’s deontological versus
consequentialist orientations and their protected values and found that protected values tended to
be more aligned with deontological than consequentialist orientation.
One reason that reasoning about protected values makes disputes intractable is that it
simplifies--and often oversimplifies--the issues. Fernbach, Min, and Sloman (2018) found that
the degree to which individuals assume protected values-based over consequentialist orientations
towards a given issue predicts how well they think they understand that issue, as well as how
intractable they consider it and how extreme their opinion is. Inducing a consequentialist
perspective can reveal to people how limited their understanding is. Following Rozenblit and
Keil (2002), Fernbach, Rogers, Fox and Sloman (2013) found that asking people to explain the
mechanism by which a policy would lead to some consequence modulated their own sense of
understanding. It also made them slightly less extreme in their attitude toward the policy. This
adds to the empirical evidence suggesting that when it comes to facilitating open-mindedness
and compromise, consequentialist perspectives trump protected-values perspectives.
This brief review suggests that protected values and consequentialist perspectives are, to
at least some extent, matters of framing. Many people can assume both perspectives on many

1

Of course, any judgment about the downstream effects of a policy is ultimately rooted in some kind of value we
hold about what consequences are more or less desirable. We hold the position prevalent in the literature that the
distinction between rhetoric appealing to the moral principle expressed by a policy itself and rhetoric appealing to
the causal chain of events a policy induces is meaningful in thought and discourse.

THINK OF THE CONSEQUENCES

6

issues. In a period of increasing political polarization across a range of issues (Newport &
Duggan, 2017), these findings suggest an avenue for improving public discourse.
We focus on the issue of same-sex marriage because attitudes toward same-sex marriage
have changed considerably over the past decade, providing a successful example of consensusbuilding. According to the Pew Research Center, 35% of Americans favored same-sex marriage
in 2001, while 62% did in 2017 (Pew Research Center, 2017). The shift in attitudes has licensed
major politicians to come out in support of same-sex marriage in recent years, as Democrats
Hillary Clinton and Barack Obama did in 2012 and 2013, respectively. Republicans like Rob
Portman and Jon Huntsman also changed their public positions in 2013. The issue came to a
head in the United States on June 26, 2015, when the Supreme Court ruled on Obergefell v.
Hodges that the constitution guarantees a right to same-sex marriage.
Shift in discourse. What kind of changes in discourse should we expect in the face of such
opinion change? One possibility is that people on both sides of the issue have well-formed
protected values buttressing their position. In such cases, re-framing the issue in consequentialist
terms should make them more open minded as suggested by the evidence that, relative to
protected-values-based discourse, consequentialist conversation leads people to see the
complexity of issues, to reduce their hubris, to focus on the outcomes of a policy rather than on
their personal opinion, to see the possibility of compromise, and to engage in less polarized
reasoning. When people start with protected values, changes in opinion should be correlated with
shifts towards consequentialist discourse. Specifically, the shift in public attitudes surrounding
same-sex marriage should be accompanied by a shift in public discourse away from talk about
issues related to protected values (like the biblical definition of marriage or the fundamental right

THINK OF THE CONSEQUENCES

7

to marry who one wants) towards talk about concrete consequences and the causal processes that
lead to them (e.g. marital benefits or the welfare of children raised by same-sex parents).
An alternative hypothesis is suggested by a quote from Justice Anthony Kennedy writing
for the majority in the Obergefell v. Hodges case: “No longer may this liberty be denied,” a clear
framing of a pro-same-sex marriage position in terms of protected values. This illustrates that the
shift in attitudes, rather than reflecting a shift from protected-values-based to consequentialist
conversation, could reflect a shift from one kind of protected-values frame to another.
Presumably this would only occur if people’s initial positions were based on protected values
that are amenable to change. Sometimes people do not have protected values that they strongly
adhere to. For instance, they might rely on protected values frames only because they are unable
to generate convincing consequentialist ones (Sloman & Fernbach, 2017). Lakoff (2004) has
argued that changes in opinion are governed by changes between what are essentially different
protected-values frames. To illustrate, the US civil rights movement that led to the Voting Rights
Act of 1965 used arguments in favor of the protected right of all citizens to be able to vote
regardless of race, suggesting that protected-values frames likely increased in frequency in
discussion of this issue up to 1965.2 It is plausible in that case that most people did not hold
intransigent protected values about voting; they probably had not thought much about the issue
until it became politically charged. It is a distinct possibility that the shift in collective attitude
toward same-sex marriage is accompanied by a shift from an anti-same-sex marriage protectedvalues frame (e.g., a religious one) to a pro-same-sex marriage protected-values frame (like
Kennedy’s).
Causal direction. Yet another possibility is that greater prominence of protected-values over
consequentialist discourse is associated with greater consensus, but it is increased consensus that
2

Suggested by Robert Goldstone (personal communication, September 30, 2018).

THINK OF THE CONSEQUENCES

8

triggers such a shift in discourse, rather than the other way around. The empirical work we report
is designed to reveal how discourse about same-sex marriage has changed over the past decade.
While correlational, the method’s focus on temporal trends can provide us with hints about the
causal relations between protected-values-based and consequentialist discourse on one hand, and
changes in public attitude observed in national polls on the other.
Naturally, we do not intend to suggest that the relative amount of consequentialist versus
protected-values discourse is the only factor governing public conversation. For instance, the
Supreme Court decision on same-sex marriage may have had a measurable influence on what
people talked about. Our method fundamentally tracks changes in the themes of discourse and
can reveal such effects.
Methods
Most of the research that has explored the effects of protected-values versus
consequentialist framing has either been performed in an experimental setting (e.g. Tanner et al.,
2008), or using field methods with small samples (e.g. Atran et al., 2007). However, the
increasing popularity over the past decade of social media as a forum for discussion of socially
significant topics coincides with rapid changes in public opinion surrounding same-sex marriage.
This provides an opportunity to examine the prevalence of these framings in the broader
discourse using a much larger and more naturalistic sample. We use a large corpus of
conversations on the popular social media platform Reddit3 to track the evolution of the
discourse surrounding same-sex marriage over the past decade.
Self-touted as “the front page of the internet”, Reddit offers users the opportunity to post
their opinions publicly in specialized forums (called subreddits), where others can upvote or
downvote them, making it more or less likely that other users will see the material. We chose
3

https://www.reddit.com/

THINK OF THE CONSEQUENCES

9

Reddit because it is the fourth most visited website in the United States4 and comments shared on
this platform have been used in the past to uncover the determinants of changes in opinions (Tan,
Niculae, Danescu-Niculescu-Mizil & Lee, 2016). With billions of posts spanning a period of
rapid change in public attitude towards same-sex marriage, presumably changes in the broader
discourse would be reflected in discourse on Reddit. Nevertheless, there is a potential for bias in
our dataset due to factors like the disproportionate representation of young urban males on
Reddit (Duggan & Smith, 2013) and Reddit’s appropriate use policy that may result in deletion
of certain types of messages.
Given the size of our corpus, which includes 603,282 posts, it would be impractical to
manually classify posts as protected-values-based or consequentialist. Supervised machine
learning algorithms provide increasingly refined means of automating such tasks. However,
supervised methods often depend on large annotated datasets that can be difficult to obtain.
Moreover, the selection of data to annotate for the algorithm’s training can itself pose difficulties
and strongly impact the outcome of the algorithm (Bishop, 2006).
We therefore use an unsupervised learning algorithm, which obviates the need for
annotated data, as an initial step to characterize the main dimensions of discourse on Reddit.
Latent Dirichlet Allocation (LDA; Blei, Ng & Jordan, 2003; Hoffman, Blei & Bach, 2010) is a
method for representing the gist of a body of texts (each text called a document). It assumes that
the gist of every document consists of several themes (topics). We use this method to identify the
salient themes of more than ten years of comments related to same-sex marriage and calculate
the relative contribution of each topic to Reddit discourse.
We chose LDA because past research shows that it can provide insights into the semantic
content of natural language that go beyond the level of words, partly due to its hierarchical
4

www.redditinc.com

THINK OF THE CONSEQUENCES

10

nature that allows for disambiguation of different senses of a term given its immediate context
(Griffiths, Steyvers & Tenenbaum, 2007). There is also evidence that this method is capable of
uncovering changes over time in the contribution of generally interpretable topics occurring in
natural text (e.g. Cohen Priva & Austerweil, 2015), including on Reddit (e.g., Thompson,
Wojtowicz & DeDeo, 2018). More important for the purposes of this paper, the same literature
suggests that topic models such as LDA can be used to distinguish between not only specific
content, but also different framings of the same content: Cohen Priva and Austerweil (2015)
show that articles published in the peer-reviewed journal Cognition over the past few decades
became more experimental and less theoretical, even when discussing the same areas of research
such as developmental or moral psychology. It is plausible that if protected values and
consequentialism are important frames for discourse about same-sex marriage, this fact would be
reflected in the topics that LDA provides: Either topics exclusively related to these framings will
be uncovered, or certain topics will reflect consistently more or less protected values-based or
consequentialist framing.
We use ratings from participants blind to LDA’s representation of the corpus to
determine the degree of association between each topic and consequentialist or protected-valuesbased framing. We then track the contributions of these two framings to the corpus over time.5
The aim of unsupervised machine learning methods such as LDA is to provide a
generalized summary of data rather than optimized answers to specific questions. However, to
demonstrate the usefulness of our method for the latter task, we will compare the predictive and
classification performance, as well as the interpretability of a linear model based on LDA’s

5

Python and R code used in this study, as well as the learned models and results of all analyses are openly available
at: https://github.com/BabakHemmatian/Gay_Marriage_Corpus_Study

THINK OF THE CONSEQUENCES

11

topics with that of a similar keyword-based model with many more parameters that does not
benefit from a topic-based representation of text.
Data
Using all comments on Reddit from January 2006 until September 20176, we created a corpus of
comments matching a regular expression containing negatively- or positively-valenced words
and phrases related to same-sex marriage (see Appendix A). Quotes and hierarchical
dependencies between the comments were ignored.
To improve the quality of our topic model, we applied common pre-processing
techniques to the dataset: We coerced all comments in our corpus to lowercase to avoid different
cases of the same word being treated as different words and changed different grammatical forms
of the same words to a uniform lemma (a process called lemmatization). HTML escape codes,
stopwords (common function words that do not distinguish between different contents),
extremely rare words (words that appeared in fewer than five documents) or ubiquitous terms
(words that appeared in 99 percent of the documents), as well as non-alphanumeric characters
were removed from the dataset. We used the lemmatizer and set of stopwords from Natural
Language Toolkit (NLTK; Bird, Loper & Klein, 2009), but retained around twenty words with
possible relevance to protected values or consequentialist framing (see Appendix A). These steps
were meant to reduce noise in representation of the gist of each post. Our corpus contains
603,282 comments (15,711,221 words in total, comprised of 32,925 unique words) with a mean
length of 26 words (median = 20, SD = 24.99).
Figure 1 shows the number of comments in our dataset from each year. Most of the
comments come from later years, even though the percentage of comments on the website that

6

Access provided by http://files.pushshift.io/reddit/comments

THINK OF THE CONSEQUENCES

12

are associated with same-sex marriage has decreased over time, reflecting the growing popularity
of Reddit in recent years (see Appendix A).

Figure 1. Number of posts on Reddit per year that are relevant to same-sex marriage, as determined by our regular expression
(see Appendix A).

Latent Dirichlet Allocation (LDA)
Latent Dirichlet Allocation is a generative hierarchical Bayesian model of discrete data
(Blei et al., 2003). The model is applied to a set of collections of discrete data (a set of
documents composed of a set of words) to recover latent dimensions (topics) that reflect
statistical regularities among the words in each document. The structure of an LDA model lends
itself naturally to recovering generally interpretable recurrent themes in data that is organized
into separable chunks, such as natural language (Griffiths et al., 2007). For our purposes, each
Reddit comment is considered a document.
An LDA model is uniquely characterized by a set of words
hyperparameters

and that determine the granularity of topics. ,

, a set of
and

topics , and

are free parameters.

THINK OF THE CONSEQUENCES

13

LDA models the generative process of each document as follows: First, a multinomial
distribution
word

∈

~ Dirichlet( ) over topic indices { ∶
in the document, a topic index

probability distribution defined by

∈ [1, ]} is defined. To determine each

is drawn from . Finally,

is drawn from the

(Blei et. al., 2003). In short, each document is characterized

as a probability distribution over topics, and each topic is characterized as a probability
distribution over words. The estimated model is a hierarchical probability distribution fit to the
training corpus (word order is ignored).
training. We use a freely-available and open-source implementation of an online
variational Bayes algorithm (Hoffman et. al., 2010) to train an LDA model on our corpus and to
query the resultant model (Řehůřek & Sojka, 2010). The estimation procedure for topics is
beyond the scope of this paper; for more information, see Blei et. al. (2003) and Hoffman et. al.
(2010). Ninety-nine percent of the documents (randomly chosen) were used to train the model
over 1,000 iterations. The rest of the dataset was used as an evaluation set to ensure it had no
more uncertainty than the training set as a means of preventing overfitting (see Appendix C).
choice of hyperparameters. Following Cohen Priva and Austerweil (2015),

and were

set to 0.1, which encourages the model to represent each document as composed of only a few
topics and to assign high probability to only a few words for a certain topic. The lower bound on
per-term topic probability was set to 0.01.
To determine the number of topics that offers the most intuitively interpretable
representation of the corpus, we trained models with up to 100 topics in increments of 25. For
each model, we looked at a combination of quantitative indicators of the model’s predictive
capacity and the qualitative, semantic content of the topics.

THINK OF THE CONSEQUENCES

14

quantitative indicators. We looked at the per-word perplexity of each model and the rate
at which it changes with different values of n for our evaluation set (Zhao et al., 2015). Per-word
perplexity reflects how uncertain the model is on average when predicting each word in a
document given the other words in the document. We also calculated UMass coherence values
for all models (Mimno, Wallach, Talley, Leenders & McCallum, 2011). UMass coherence
measures how much, within the words used to describe a topic, a common word is on average a
good predictor for a less common word. All measures showed a preference for fewer topics (see
Appendix C for values).
semantic content. While per-word perplexity and UMass coherence provide an
approximation to interpretability of topics, they often do not align well with our internal
semantic spaces (the gold standard of coherence; Chang, Boyd-Graber, Gerrish, Wang & Blei,
2009; Stevens, Kegelmeyer, Andrzejewski & Buttler, 2012). We therefore also manually
inspected the 80 words most strongly associated with each topic in every model. We made note
of whether the vast majority of words for each topic intuitively belonged to the same conceptual
category (e.g. “finance” or “religion”), and whether most of them could presumably be used in
making the same kind of appeal for or against same-sex marriage. This revealed topics with n =
25 to mainly consist of mixtures of disparate arguments and framings. We will therefore report
the results with 50 topics because that led to the optimal trade-off between, on one hand, the
interpretability and distinguishability of topics, and on the other, the predictive power of the
model. Similar inspections for n = 45 and n = 55 suggested that our results are stable for similar
numbers of topics and not an artifact of the exact value used (for all the models with various
numbers of topics, the set of most representative words and their probabilities under the relevant

THINK OF THE CONSEQUENCES

topics can be found in the study’s online repository). The choice for

15

topics was made before

the rest of the analysis presented in this paper was conducted.
categorizing topics as consequentialist vs. protected-values-based. To determine
which topics in the learned model are representative of consequentialist or protected-valuesbased discourse, 2000 posts were selected from the corpus that had the greatest impact on Reddit
discourse as proxied by the absolute difference between number of upvotes and downvotes.7 The
difference in the number of upvotes and downvotes in this set ranged from -609 to 10,343, with
an average difference of 543. Eight hundred of the 2,000 posts were chosen from our corpus such
that, to the extent possible, comments most representative of each topic were evenly sampled
(henceforth called impactful posts). A comment’s representativeness of a topic
operationalized as the percentage of words in the comment for which topic

was

is the most

probable topic according to the LDA model. The sampled comments were on average 25 percent
representative of their most likely topic. One topic out of all 50 was not the most likely topic for
any comment in the eventual sample (see Appendix B for the distribution of topic assignments
among the 2,000 comments, as well as the rated subset).
Ratings for the resulting set of 800 posts were gathered from six trained participants (3
men and 3 women) blind to the predictions of the model. The average age in the sample was 34
years (SD = 17, ranging from 21 to 65). All participants were supportive of same-sex marriage.
Participants read instructions for distinguishing between protected-values-based and
consequentialist discourse based on Baron and Spranca (1997). The full text of the instructions
can be found in Appendix B. The full set of impactful comments, their topic estimates and
participant ratings for them can be found in the study’s online repository.
7

Because of “fuzzing” algorithms employed by Reddit to combat the effect of bots on upvotes and downvotes, it is
impossible to recover the absolute number of votes from the freely available data. Only the difference between the
number of upvotes and downvotes can be accurately determined.

THINK OF THE CONSEQUENCES

16

After comprehension check questions, participants were shown comments in randomized
order and first asked to rate whether the attitude expressed in the post is in favor of same-sex
marriage, against it, or whether it is impossible to tell from the content. They then rated the
degree to which the post showed consequentialist or protected-values-based framing of same-sex
marriage on a scale from one (completely protected-values-based) to seven (completely
consequentialist), where four was labeled “neither”. Five participants each rated 120 posts. One
participant rated 360 posts. To determine the reliability of ratings, twenty percent of the posts
were rated by two different raters.
The contribution of different topics to each rated impactful comment was queried from
the LDA model and entered into a linear regression for training sets composed of ninety percent
of the 800 comments. Parameter estimates from the regression were then used to predict ratings
on the remaining ten percent. Predictions were derived after dropping topics from the regression
formula that were not significant predictors of ratings in the training set using a stepwise search.
To ensure robust results despite the small size of our sample, we performed ten ten-fold crossvalidations, testing the model’s performance on 100 different test sets in total: For each ten-fold
cross-validation, we randomly divided the 800 comments into ten mutually-exclusive subsets,
deriving predictions for each subset based on the other nine, and aggregating results across all
ten test subsets. This entire process was then repeated ten times and the results were aggregated
across all ten ten-fold cross-validations.
We chose topics for tracking over time that were significant predictors (p < 0.05) in the
linear model for at least half of the 100 iterations. These topics were classified as protected
values-based or consequentialist based on the sign of their associated parameter estimates
averaged across all iterations.

THINK OF THE CONSEQUENCES

17

To characterize the theme represented by each topic, we randomly chose ten posts from
the set of 25 posts in the corpus that were most representative of each top topic. Examples of
sampled comments and their associated representativeness values can be found in Appendix D.
All sampled comments can be found in the study’s online repository. We examined the
comments for use of similar categories of concepts (e.g. religious dogma), as well as arguments
with appeals similar in form and content (e.g. causal analysis involving changes to the structure
of mainstream families). We also queried the 40 words that had the highest probabilities under
that topic. We then identified words only present in the high probability set of that top topic
(unique top words) or shared with the high probability set of only one other top topic (almost
unique top words). See Appendix D for the resulting sets. We then examined the sets for
properties shared among the vast majority of unique or almost unique top words belonging to
each topic, noting whether they belonged to similar categories of concepts or could be used in
arguments similar in style or content for or against same-sex marriage.
calculating topic contributions. In order to determine the relative popularity of different
topics over time, we calculated the monthly contribution of topic

(for

∈ [1, ]) to the

learned model. Following Cohen Priva and Austerweil (2015), this measure was defined as:
( ) =
where

|

|

∑ ∈

|{

∈ ∶

(
| |

)

}|

(1)

is a word in document d, d is a document represented as an unordered bag of words in

(the set of documents from month m), and topic(

) stands for the most likely topic for

given the prior distribution over topics and the other words present in d. This measure reflects
the percentage of words in a month that are most strongly associated with a certain topic. In

THINK OF THE CONSEQUENCES

18

calculating the norm of documents, only words were counted for which the conditional
probability of at least one topic was more than 0.01.8
Other than tracking the contribution of protected-values-based and consequentialist topics
over time, this measure was used to identify topics that were major contributors to the discourse
even though not consistently associated with either category. The combination of such topics and
topics chosen based on predictive value with respect to ratings of impactful comments comprises
a set that we will henceforth call top topics. We consider only these topics in the results reported
below.
Comparison with a Word-Frequency Model
Topic models such as LDA posit latent variables that make it possible to learn
dependencies in text that may not be uncovered using a non-hierarchical representation of word
meanings (Griffiths et al., 2007). To determine whether the LDA model captures more of the
variance in the human ratings of consequentialist versus protected-values-based reasoning, we
compared the test set prediction performance of the LDA-based regression model with that of a
regression model that used the most discriminative words as predictors, defined according to the
word-frequency model described below.
Hierarchical models of language can also provide more interpretable dimensions of
variation (Griffiths et al., 2007). We therefore also discuss the predictors included in the two
regressions in terms of interpretability.

8

It is possible that for a significant portion of the dataset, similar probabilities were associated with several topics
and by choosing only the most likely topic we lost information with significant impact on the trends. The choice of
hyperparameters discourages this. However, to ensure the robustness of the trends, we used an alternative
calculation where the contribution of a given topic is determined by the normalized sum of probabilities assigned to
the words of a document conditioned on that topic and the document’s context. Using this method, any probability
associated with a topic counts towards its overall contribution. The results did not deviate from what is reported in
the text.

THINK OF THE CONSEQUENCES

19

The word-frequency model uses the conditional probability of each word wij (the
word of the
(P(

comment) in a training set of impactful comments rated as consequentialist

|consequentialist)) or protected values-based (P(

|protected-values-based)). The

informativeness of each word with respect to the distinction between the two frames is defined
as:
(

)=

(
(

|

|

)
)

(2)

where greater values mean stronger association with consequentialist framing. One hundred
training and test sets were produced with ten ten-fold cross-validations using a procedure similar
to that of the LDA predictive model described above. The informativeness values for each word
was summed across all iterations to calculate each word’s overall association with the two
frames of discourse. One hundred words with the highest aggregate values and 100 words with
the lowest aggregate values were chosen as the best word-level predictors (see Appendix C for a
list of these predictors).
A linear regression model was learned for each iteration following the same procedure as
described for LDA, but with these 200 words as potential predictors instead of topic
contributions. Parameter estimates based on each training set were then used to predict ratings of
comments in the associated test set. Performance was averaged across all 100 iterations and
compared with that of LDA.
The presence of the following words was a significant predictor of consequentialist rating
of an impactful comment in more than half of the 100 test sets (in decreasing order of number of
times; numbers range from 100 for “used” to 51 for “barometric”): used, ignored, claim, fiscal,
destroy, effect, zero, morning, kill, forcing, work, aggressive, tried, none, gain, barometric. The
presence of the following words was a significant predictor of protected-values-based rating of

THINK OF THE CONSEQUENCES

20

an impactful comment in more than half of the 100 test sets (in decreasing order of number of
times; numbers range from 97 for “devil” to 65 for “directly”): devil, clear, stupid, believe,
clapped, within, holy, favor, weekend, wanting, becomes, Christian, currently, away, different,
terrible, directly. While some of these words carry connotations associated with the relevant
discourse category (such as “fiscal” for consequentialist or “holy” for protected values), others
are less intuitive indicators of their assigned discourse category (such as “kill” for
consequentialist or “currently” for protected values).
Results
Human Ratings of Impactful Posts
The average rating for the association of comments with protected-values-based and
consequentialist discourse was 4.27 (slightly more consequentialist than not; SD = 2.09). Based
on these ratings, out of 800 impactful posts, 302 (37.8 percent) were categorized as
consequentialist, 237 (29.6 percent) were categorized as protected-values-based, and the
remainder were rated as neither (261 comments, comprising 32.6 percent of the dataset).9
One hundred and sixty comments were rated more than once. To measure the reliability
of ratings, we randomly assigned one of the two ratings for each comment to one of two sets and
calculated the Pearson correlation between the resulting sets. This random assignment was
repeated 100 times. The resulting correlations between different ratings of the same comments
ranged from 0.18 to 0.19. The correlations suggest less agreement among raters than we
anticipated, though they are consistently positive. The difficulty participants had in classifying
posts as consequentialist or protected-values-based is in line with what has been found in other
studies (e.g. Fernbach, Min & Sloman, 2018).

9

To determine classification where more than one rating was available, we classified a comment as “neither” if two
raters provided ratings on the opposite halves of the scale, and otherwise used the mean.

THINK OF THE CONSEQUENCES

21

Of the rated comments, 554 (69 percent) were identified as pro-same-sex marriage, 33 as
clearly against same-sex marriage (4 percent), and the remaining 213 (27 percent) had unclear
ramification for the issue. The strong bias towards pro-same-sex marriage arguments might
reflect the population of Reddit users, moderation and acceptable use rules, or the coincidence of
increased public support for same-sex marriage with the increased popularity of Reddit and is a
limitation of our study. It is also noteworthy that the vast majority of impactful comments had
more upvotes than downvotes, suggesting that Reddit users are more likely to react to content
they approve of. This may have introduced further bias towards opinions in favor of same-sex
marriage in our sample of most impactful comments.
prediction of human ratings using LDA and the word-frequency model. The average
correlation between predictions of a linear regression based on LDA topics and true ratings of
held-out test sets was 0.25 across ten ten-fold cross-validations. Including random intercepts to
account for the rating styles of different raters increased this correlation to 0.4. Average adjusted
R-squared for the former model was 0.13, while the same value for the latter model was 0.34
(see the study’s online repository for the results of all regression analyses).
Comments for which the predicted rating was greater than 4 were considered to be
classified as consequentialist, while predictions of less than 4 were considered protected-valuesbased. The accuracy of these classifications across the 100 tests sets was 0.64. A model that
classified every comment as consequentialist would have an accuracy of 0.56. The wordfrequency model had comparable predictive and classification capability with an average
correlation of 0.37 and classification accuracy of 0.64. Adjusted R-squared averaged across
iterations was 0.27 for the word-frequency model.

THINK OF THE CONSEQUENCES

22

The amount of information contained in human ratings, and the amount thus captured by
topic models, is modest. Our results suggest that the LDA model captures as much information
about human intuitions surrounding consequentialist versus protected-values-based reasoning as
a word-frequency model with four times the number of parameters.
Breakdown of Discourse
See Table 1 for the top five high probability words associated with each of the top topics:
topics that a) were significant predictors of classification of impactful comments in more than
half of all cross-validations, or b) were major contributors to the discourse based on the LDA
model. The probability of words in this this table given the associated top topic ranges from one
to 25 percent (M = 0.035, SD = 0.036). The variability in probabilities partly reflects differences
in breadth among topics. The probability of any word in this table being associated with any
other topic in the model (including non-major topics) is less than 0.056. Only unique highprobability words are shown, because certain words such as “gay” or “marriage” have high
probability under all topics and thus do not capture the topic’s focus. See Appendix D for the full
sets of unique and almost unique high probability words for all mentioned topics. For the 80
words most associated with each of the 50 topics in the model and their probabilities, see
supplemental materials.10
protected-values-based topics. Significant contributions from three topics were
significant predictors of a post being rated as more protected-values-based in all 100 crossvalidations. Inspection of the unique and almost unique high-probability words and the
comments most representatives of these topics revealed the following prominent themes:
religious arguments, freedom of belief, and LGBT rights. The presence of no other topic was a

10

Supplemental materials can be found at:
https://github.com/BabakHemmatian/Gay_Marriage_Corpus_Study/blob/master/Supplemental_Materials.pdf

THINK OF THE CONSEQUENCES

23

significant predictor of protected-values-based reasoning in more than half of the crossvalidations.
consequentialist topics. Significant contributions from five topics were significant
predictors of a post being rated as more consequentialist in more than half of all crossvalidations. Inspection of the most representative words and comments revealed that these topics
covered a greater range of themes than the protected-values-based topics. Topics were most
representative of the following themes: politicians’ stance, children of same-sex parents, samesex marriage as a policy issue, employer attitudes and associated regulations, and cultural and
historical status.
The last two topics had a noticeably broader focus. Their contribution was more
distributed across different posts and their most representative comments were more diverse in
content (see Appendix D and representative comments in the online repository). These two
topics were also highly associated with several words that did not intuitively cohere with the
majority of elements in the same sets. Words such as “evil” and “value” are among the top words
for these two topics. While these words appear to be more associated with protected values,
inspection of the impactful and representative comments shows the main focus to be causal
analysis of cultural and financial trends related to same-sex marriage. This ability to separate
overall association of such terms with a discourse category from their association in a specific
context is one of the benefits of using hierarchical models such as LDA and is absent in simple
keyword-based methods (Griffiths et al., 2007).
major topics rated as neither consequentialist, nor protected-values-based. For each
topic, we calculated the topic’s average monthly contribution to the model, i.e. the fraction of
words in the corpus from a certain month generated by that topic. We then compared that value

THINK OF THE CONSEQUENCES

24

to the contribution that would have been expected if topic contributions were uniformly
distributed at each time point. Two topics were not consistently associated with consequentialist
or protected-values-based discourse but were nevertheless major contributors to the discourse
based on this criterion, contributing on average more than twice the uniform baseline. The
themes represented by these two major contributors were: forcing versus allowing behaviors and
personal anecdotes. The former topic has fewer unique associated words in Table 1, because
words such as “force” and “let” most strongly associated with it are common terms also
associated (albeit less strongly) with other top topics. Similarly, the word “right” had by far the
highest probability under LGBT rights, but was shared as a high-probability word with other
topics due to its many meanings.
Topic

Top five most associated unique words
Protected-values-based topics

Religious arguments

God, Bible, Islam, Jesus, Christianity

Freedom of belief

belief, opinion, others, atheist, respect

LGBT rights

LGBT community*, trans, movement, right, fight

Consequentialist topics
Employer attitude and regulations

job, Sanders, evil, owner, trade

Cultural and historical status

traditional, modern, Tory, value, destroy

Politicians’ stance

anti, supported, changed, pro-gay, politically

Children of same-sex parents

child, parent, divorce, adoption, adopt

Same-sex marriage as a policy issue

political, Left, important, climate, immigration

Neither
Forcing versus allowing behaviors

allowed, legally, fine, anybody

Personal anecdotes

woman, man, lesbian, wife, husband

THINK OF THE CONSEQUENCES

25

Table 1. Top five words that are uniquely associated with each top topic, in decreasing order of probability given that topic. *The
probabilities conditional on the associated topic for “LGBT” and “community” were almost identical, suggesting these words
appeared in conjunction.

Intertemporal Trends
To visualize how the contribution of protected-values-based and consequentialist top
topics to discourse has changed over time, we first combined monthly contribution estimates of
topics associated with the two discourse categories. We then visualized the trends of these
pooled estimates as a function of time using degree two locally-estimated scatterplot smoothing
(LOESS) regressions. We used LOESS to highlight the local perturbations in contributions that
characterize the impact of specific events. While the LDA was trained on the entire dataset,
monthly contributions from 2006 and 2007 were excluded from our regression analyses because
each estimate was based on less than 100 documents. Figure 2 shows the results for the two
discourse categories. The shaded areas represent 95% confidence intervals. Note that the
combination of the two sets of categories accounts for at most about twenty percent of our corpus
at each point in time.

THINK OF THE CONSEQUENCES

26

Figure 2. Points reflect percentage monthly contribution of consequentialist and protected-values-based topics to the trained
LDA model. Each data point is calculated by summing the monthly contribution of all topics subsumed by the relevant discourse
category. The colored lines show the best-fitting locally-estimated scatterplot smoothing (LOESS) function (see text for details).
The shaded areas represent 95% confidence intervals. The vertical line to the left marks the beginning of a steady upward trend
of support for same-sex marriage among a majority of Americans (Gallup, 2017). The vertical line to the right marks the
Supreme Court ruling that legalized same-sex marriage.

Protected-values-based themes rise in prominence until mid-2012, after which they show
a steady decline that predates the Supreme Court ruling in June 2015. The decline begins not
long after the point at which a majority of Americans expressed support for same-sex marriage
(leftmost vertical line), which was followed by a number of prominent politicians expressing

THINK OF THE CONSEQUENCES

27

support for the issue (Gallup, 2017).11 In contrast, the contribution of consequentialist topics
decreases overall until 2010, despite significant monthly variability during this period. One spike
in consequentialist discourse happens around the time of majority support for same-sex marriage,
while a larger spike can be seen in 2016, presumably associated with the United States’
presidential election.
These results are based on the pooled contributions of several topics. To see if our results
generalized to individual topics, we ran a separate regression to predict the logarithmic odds of
each topic ’s contribution,

( | )

, where

(¬ | )

is the total observed text in the corpus on a

given timestep and ¬ is the contribution of all other topics, as a function of time. The model
accounted for 49 percent of the variance in contribution. Consequentialist topics and higher time
indicators were both associated with significantly higher contribution (p < 0.001). The linear and
quadratic interaction between these two predictors was positive and highly significant (p <
0.001). In other words, individual consequentialist topics are on average associated with
increasing contributions over time.
We then visualized the trend of each top topic’s contribution to the LDA model as a
function of time using LOESS regression. Figure 3 shows the results for protected-values-based
topics. Religious arguments and freedom of belief follow each other closely: They rise in
prominence prior to 2013 and see a decrease in importance afterwards. The contribution of
LGBT rights is relatively constant until the Supreme Court ruling and shows a spike in 2016.
To test whether the trends associated with each topic’s contribution over time are
statistically significant, we ran separate cubic regressions with each topic’s contribution as the
11

Gallup first reported that more than 50% of Americans support same-sex marriage in May 2011 (Gallup, 2017).
However, the percentage dropped from 53% to 48% in November of the same year (with a 95% confidence interval
of 4%). Starting in May 2012, all polls showed steadily increasing mean approval rate of 50% or more. Note that
one of the cases that culminated in the Supreme Court ruling to legalize same-sex marriage was also filed in the
same year (DeBoer v. Snyder in January 2012).

THINK OF THE CONSEQUENCES

28

predicted variable and time indicators as the predictors. This analysis showed the linear and
quadratic trends for religious arguments and freedom of belief to be significant (p < 0.05). The
upward linear trend in LGBT rights was also significant (p < 0.05).

Figure 3. Points reflect percentage monthly contribution of individual protected-values-based topics to the trained LDA model.
The colored lines show the best-fitting LOESS function. The shaded areas represent 95% confidence intervals. The black vertical
line to the left marks the beginning of a steady upward trend of support for same-sex marriage among a majority of Americans
(Gallup, 2017). The vertical line to the right marks the Supreme Court ruling that legalized same-sex marriage.

Figure 4 shows the results of LOESS regression for consequentialist topics. The
contribution of politicians’ stance to discourse about same-sex marriage stays relatively constant
prior to 2011 and increases sharply for a period of two years afterwards. We conjecture that this
increase reflects the time when many politicians started to voice their support publicly, including
Barack Obama in May 2012. The second increase in discussions of politicians’ stance starts in

THINK OF THE CONSEQUENCES

29

2014 and might initially relate to a string of highly publicized court cases regarding LGBT rights
that culminated in the Supreme Court decision. The prominence of LGBT issues in presidential
campaigns of 2016 might explain the higher probability of discussion about politicians’ stance in
2016. The contribution of this topic decreases in 2017 but is still higher on average than in 2015.
Discussion of same-sex marriage as a policy issue follows a similar pattern, but with smaller
spikes. Same-sex marriage as a policy issue was also the only topic that did not show any
significant cubic polynomial trend, which may be ill-equipped to represent its seemingly periodic
pattern of contribution. The contribution of discussions about children of same-sex parents
decreases slightly but significantly until 2016, while that of employer attitude and regulations
and cultural and historical status to discourse is stable.

THINK OF THE CONSEQUENCES

30

Figure 4. Points reflect percentage monthly contribution of individual consequentialist topics to the trained LDA model,
separated by color. SSM stands for same-sex marriage. The colored lines show the best-fitting LOESS function. The shaded areas
represent 95% confidence intervals. The black vertical line to the left marks the beginning of a steady upward trend of support
for same-sex marriage among Americans since the first time a Gallup poll showed a majority of Americans are in favor of it
(Gallup, 2017). The vertical line to the right marks the Supreme Court ruling that legalized same-sex marriage.

Figure 5 shows the results of LOESS regression for major topics categorized as neither
protected-values-based, nor consequentialist. Forcing versus allowing behaviors has the highest
average monthly contribution to the model of any topic. It also shows the clearest downward
trend, seemingly unperturbed by major events in this period concerning same-sex marriage. The
significance of this linear trend was confirmed via cubic regression (p < 0.001). In contrast, the
contribution of personal anecdotes to the model increases rapidly in earlier years and more
slowly afterwards. This trend was also highly significant based on cubic regression (p < 0.001).
We conjecture that the latter pattern reflects the increased tendency of individuals to share their
experiences or that of their acquaintances with higher societal acceptance of same-sex
relationships.

THINK OF THE CONSEQUENCES

31

Figure 5. Points reflect percentage monthly contribution of major topics that were categorized as neither protected-values-based
nor consequentialist to the trained LDA model, separated by color. The colored lines show the best-fitting local polynomial
function. The shaded areas represent 95% confidence intervals. The black vertical line to the left marks the beginning of a steady
upward trend of support for same-sex marriage among a majority of Americans (Gallup, 2017). The vertical line to the right
marks the Supreme Court ruling that legalized same-sex marriage.

Individual temporal trends and the most strongly-associated keywords for the 40 topics
not included in Figures 3-5 can be found in supplemental materials. The average contribution of
all those topics to the model did not vary significantly over the timeframe of interest.
Intertemporal Trends of the Word-Frequency Model
Figure 6 shows the fraction of words that the word-frequency model classified as
consequentialist and protected-values-based in each month. This measure shows a relatively
constant advantage for consequentialist discourse throughout the years, which reflects the higher

THINK OF THE CONSEQUENCES

32

base rate of consequentialist comments in the set of impactful comments. Unlike LDA, the word
frequency model is a flat semantic representation that does not posit latent themes, but
effectively averages across more nuanced and temporally variant threads of discourse. This
averaging may reconcile the flatness of the trends in word-based classification with the temporal
variation discussed in the previous sections.

Figure 6. The fraction of words in each month classified as consequentialist or protected-values-based by the word frequency
model (see text for details). The shaded regions indicate the 95% confidence region calculated based on 100 instances of the
word-frequency model, each trained on a different set of comments consisting of 90% of the labeled impactful comments. The
black vertical line to the left marks the beginning of a steady upward trend of support for same-sex marriage among a majority of
Americans (Gallup, 2017). The vertical line to the right marks the Supreme Court ruling that legalized same-sex marriage.

Considerations in Interpretation of Results
prediction and classification accuracy. While reliably above chance, the accuracy of
classification and rating prediction based on both our word-frequency model and the LDA
analysis was slightly below two-thirds. The word-based model might have performed better if it
had a way to represent the hierarchical nature of language. LDA might have performed better if

THINK OF THE CONSEQUENCES

33

it were not an unsupervised method not optimized for providing such a classification, but rather
for offering a summary representation of the corpus. Additionally, much of the information about
discourse content was not present in individual comments as it was carried by other elements of
the discourse context. More recent topic modeling methods that allow for the inclusion of
hierarchical relations between different posts can help extract aspects of the relevant context (e.g.
Matrix Inter-Joint Factorization; Nugroho, Zhong, Yang, Paris & Nepal, 2015). However,
implied inferences that are not referred to directly in the text would escape most common natural
language processing models (Manning, Manning & Schütze, 1999).
coverage of discourse. We recognize that the distinction between consequentialist and
protected-values-based discourse accounted for only about twenty percent of our corpus. While
more robust ratings may increase the fraction considerably, we acknowledge that same-sex
marriage is a complex topic that can be approached from a variety of standpoints, not all of them
characterized by our focal distinction.
data limitation. The quality of an algorithm’s outputs is largely a function of its inputs.
Most of the posts in our dataset belong to more recent years. Therefore, the trained model is
biased in favor of the statistical properties of discourse in those years. In addition, Reddit posts
appear to be strongly biased towards pro-same-sex marriage opinions. According to ratings by
the authors, the rate of positive attitudes among the most representative posts we sampled for the
ten top topics was higher than the reported national average (Gallup, 2017). A similar pattern
was observed for impactful posts rated by participants blind to our hypothesis.
properties of LDA. The distributions representative of top topics partly reflect parameter
choices, such as the number of topics and granularity of topics. Although we based our choice of
parameters on careful analysis of the corpus, there may exist better values. We also note that, due

THINK OF THE CONSEQUENCES

34

to either the strictness of the thresholds that determined inclusion or the nature of discourse on
Reddit, our analysis may have excluded some topics relevant to the debate over same-sex
marriage.
More generally, the inherent shortcomings of LDA may have affected our results. LDA’s
ability to pick up interpretable themes in documents emerges from the correspondence of
interpretability with statistical properties of the “bag-of-words” representations of these
documents. Such representations lose important aspects of language, including sequential
dependencies between words. We urge readers to follow the advice of Blei et al. (2003) and treat
the epistemological claims we make about the top topics with the usual degree of caution.
Similarly, the simplicity of our word-frequency model may have concealed interesting patterns
in the data. For instance, our word-frequency model did not make use of base rates of words.
Discussion
We hypothesized that shifts in public attitudes surrounding same-sex marriage are
accompanied by shifts in public discourse away from protected values and towards
consequentialist rhetoric, and that this shift would be reflected in discourse on Reddit over the
last decade. To address the question, we used LDA to infer the topics underlying posts appearing
on Reddit from January 2006 to September 2017. We categorized major topics into protectedvalues-based, consequentialist, and neither based on human ratings and average contribution to
the model and examined the contribution of each category as well as the individual topics to the
corpus over time. Many of the trends we observed coincided with turning points associated with
the same-sex marriage debate, suggesting discourse on Reddit can track shifts on issues of major
social interest.

THINK OF THE CONSEQUENCES

35

Discussion of the political framing of same-sex marriage (e.g., the impact of politicians’
stance) ebbed and flowed, following election cycles closely. However, the spikes grew larger
over time, showing an overall increase in discussing political ramifications of this issue even
after the Supreme Court ruling in favor of same-sex marriage in 2015. Discussion of two
protected-values-based topics (freedom of belief and religious arguments) increased sharply prior
to majority support. These trends reversed in the latter half of 2012, when several high-profile
court cases related to same-sex marriage were filed, but long before the Supreme Court ruled in
favor of equal marriage. While these topics dominated the overall pattern of consequentialist and
protected-values-based discourse, not every topic in one of these two categories changed in
contribution considerably over during the same period: Among protected values, LGBT rights
gained some limited prominence in 2016 but was otherwise unaffected by the passage of time.
The contribution of children’s welfare to the discussion decreased prior to consistent majority
support in the US for same-sex marriage (Gallup, 2017) and flattened afterwards. Discussion of
other major consequentialist topics was flat during this period.
Other significant contributors to the discourse not reliably associated with either category
were LGBT-themed anecdotes and discussion of forcing or allowing certain behaviors. The
former increased in contribution monotonically, presumably due to increasing acceptance of
LGBT experiences in society at large, while forcing or allowing behaviors consistently decreased
in influence.
Our results are correlational, and do not speak to the causal relation between changes in
discourse and changes in attitudes. They only show that for this one social issue, a relative shift
from a certain type of protected-values-based discourse to a certain consequentialist framing on a
popular online platform coincided with a shift in public attitude in more recent years. A natural

THINK OF THE CONSEQUENCES

36

follow-up to our work would be to track to what extent shifts in protected-values-based and
consequentialist rhetoric trace public attitudes associated with other major social topics (e.g.
marijuana legalization). Regardless, the timing of the shift in discussion of same-sex marriage
hints at a causal relation that is in the opposite direction of what we initially hypothesized. The
data we report suggest that the trajectory of discourse on this important social issue began with a
debate about protected values: Should the issue be framed in relation to protected notions of
marriage or in terms of freedom of opinion and beliefs? Once attitudes began to change, the
discourse changed too. Even though protected values remained major contributors to the
discourse, the debate shifted to be less protected-values-oriented, and the relative concentration
of consequentialist discourse--in particular, the political and policy ramifications of the issue-increased.
That the shift coincided with the development of majority support for same-sex marriage
could have occurred for several reasons. Individuals might have voiced their support for values
they believe are popular. As opinions shift, the tendency to provide arguments for the less
popular viewpoints could decrease. With increased public support, hopes for achieving concrete
outcomes related to same-sex marriage may have been rekindled as well, spurring talk of
political processes, which itself may have impacted attitudes.
Alternatively, people may be likely to rely on the consensus within their communities to
determine their protected values and consequentialist beliefs (Sloman & Fernbach, 2017). There
is strong evidence that people do not reason their way to many of their beliefs, but instead inherit
those beliefs from the groups they affiliate with (including their families, religious and political
communities, etc.; for an early modern discussion see Hardwig, 1985). Majority support for

THINK OF THE CONSEQUENCES

37

same-sex marriage may have signaled a shift in these inherited beliefs, itself inducing further
changes in discourse and attitudes.
So far, we have discussed protected-values-based and consequentialist framing of the
discourse as if they are mutually exclusive. It is possible that protected values and
consequentialist thinking fall on separate discursive dimensions rather than on the same
continuum (cf. Tanner et al., 2008). Relatedly, some of the themes we discovered in our dataset
such as forcing or allowing behaviors and personal anecdotes can and were used to appeal to
both or neither of these dimensions. Without assuming a strict continuum between the two, we
maintain that protected values and consequentialism characterize two important frames of public
discourse.
Public discourse is a rugged and complex landscape. We have presented a survey of
specific dimensions in that landscape which can be helpful for characterizing societal discourse,
with the hope of contributing to an ongoing project of mapping its features more entirely.
However, that not all protected-value-based and consequentialist topics showed clear temporal
trends highlights the fact that discourse about major social topics is impacted by many factors
and not reducible to a binary dimension. Indeed, only about twenty percent of the text in our
corpus was classified along this dimension. A natural follow-up to our work would be to attempt
to identify the other dimensions that characterize online discourse on major social topics.
We have tracked intertemporal trends in high-level themes, but our method does not have
the resolution to allow us to delve into the fine-grained ways in which these themes are invoked.
For example, while we can track discussion of religious arguments over time, we’re unable to
say how often it is invoked sincerely and how often as a straw man. The different ways in which
discussants invoke protected values and consequences could explain or predict different patterns

THINK OF THE CONSEQUENCES

38

of attitude shifts. For example, Atran et al. (2007) argue that acknowledging and making small
concessions to the other side’s protected values is an important and often necessary step in
conflict resolution and the achievement of consensus. Brewer (2003) provides evidence of
changes in protected values accompanying more positive attitudes towards the LGBT
community. While the increase in discussion of LGBT rights in 2016 and 2017 may reflect the
results of such a process, our method may have failed to uncover other examples of similar shifts
in the corpus.
From a methodological perspective, our results highlight how limited annotated data
combined with unsupervised machine learning can help psychologists extract properties of large
corpora that speak to important facets of and hypotheses about individual and social cognition.
Topic modeling of the corpus was independent of our hypothesis and therefore free of biases
introduced by training samples, and our annotated dataset was small comparative to those
commonly used in supervised natural language processing. Given the ubiquity of social media in
modern life, open access to much of this data, and easy access to packages for performing
associated analyses, such methods allow researchers to use much larger and more naturalistic
samples of human discourse to address psychological hypotheses with modest resources.
Even though not optimized to classify consequentialist and protected-values-based
reasoning, LDA’s performance was comparable to a keyword-based approach optimized for that
purpose with many more parameters. The results of LDA were more interpretable with respect to
a couple major dimensions of human discourse. Many of the keywords associated with either
category in the word-frequency model could not be readily associated with specific arguments.
In contrast, LDA topics represented more interpretable clusters of discourse surrounding samesex marriage. This is partly because the hierarchical structure of LDA allowed us to separate the

THINK OF THE CONSEQUENCES

39

association of terms with the two types of reasoning from their association to specific classes of
arguments. For instance, the term “value” was a strong predictor in both models. However, it
was among the 80 words most associated with both the discussion of causal historical processes
categorized by raters as consequentialist, and the freedom of belief topic, rated as predominantly
protected-values-based. The word frequency model simply associated this term with protectedvalues-based reasoning.
LDA also afforded clearer and more fine-grained, argument-specific temporal trends:
While the presence of words associated with consequentialist or protected-values-based human
ratings suggested a constant advantage for consequentialist discourse over time, a more detailed
look at the topics underlying the use of certain words showed the ebb and flow of arguments
over time. These trends corresponded to major social events, suggesting that LDA can be used to
uncover how discourse reacts to influences that unfold over time. Future work could take
advantage of the burgeoning collection of related methods (e.g. Esmaeili et al., 2019) to
characterize the rugged landscape of social discourse.
Acknowledgments
This article greatly benefited from discussion with members of Sloman Lab at Brown
University. We thank Elinor Amit, Linda Covington, David Sherman, Leila Sloman, Semir
Tatlidil, An Vo and Luana Pessanha de Mattos for their help with data gathering.

THINK OF THE CONSEQUENCES

40

References
Atran, S., Axelrod, R., & Davis, R. (2007). Sacred barriers to conflict resolution. Science, 317,
1039-1040.
Baron, J., & Leshner, S. (2000). How serious are expressions of protected values?. Journal of
Experimental Psychology: Applied, 6(3), 183-194.
Baron, J., & Spranca, M. (1997). Protected values. Organizational behavior and human decision
processes, 70(1), 1-16.
Bird, S., Loper. E, & Klein, E. (2009). Natural Language Processing with Python. O’Reilly
Media Inc.
Bishop, C. M. (2006). Pattern recognition and machine learning. Secaucus, NJ, USA: Springerverlag.
Blei, D. M., Ng, A. Y., & Jordan, M. I., (2003). Latent Dirichlet Allocation. Journal of Machine
Learning Research, 3, 993-1022.
Brewer, P. R. (2003), The Shifting Foundations of Public Opinion about Gay Rights. Journal of
Politics, 65, 1208-1220.
Chang, J., Boyd-Graber, J., Gerrish, S., Wang, C. & Blei, D., (2009). Reading tea leaves: How
humans interpret topic models. Advances in Neural Information Processing Systems, 21
(pp. 288-296). Proceedings of Neural Information Processing Systems 2009.
Cohen Priva, U., & Austerweil, J. L. (2015). Analyzing the history of Cognition using topic
models. Cognition, 135, 4-9.
Dehghani, M., Iliev, R., Sachdeva, S., Atran, S., Ginges, J., & Medin, D. (2009). Emerging
sacred values: Iran's nuclear program. Judgment and Decision Making, 4(7), 930-933.

THINK OF THE CONSEQUENCES

41

Duggan, M., & Smith, A. (2013). 6% of online adults are reddit users. Pew Internet & American
Life Project, 3, 1-10.
Esmaeili, B., Huang, H., Wallace, B. C., & van de Meent, J. W. (2019). Structured
Representations for Reviews: Aspect-Based Variational Hidden Factor Models. arXiv
preprint arXiv:1812.05035.
Fellbaum, C. (1998). WordNet: An Electronic Lexical Database. Cambridge, MA: MIT Press.
Fernbach, P. M., Rogers, T., Fox, C., & Sloman, S. A., (2013). Political extremism is supported
by an illusion of understanding. Psychological Science, 24, 939-946.
Fernbach, P. M., Min, L., & Sloman, S. A. (2018). Values-based and consequence-based policy
attitudes. Working paper.
Gallup. (2017). US Support for Gay Marriage Edges to New High. Retrieved from
http://news.gallup.com/poll/210566/support-gay-marriage-edges-new-high.aspx
Griffiths, T. L., Steyvers, M., & Tenenbaum, J. B. (2007). Topics in semantic representation.
Psychological review, 114(2), 211.
Hardwig, J. (1985). Epistemic dependence. Journal of Philosophy, 82(7), 335–349.
Hoffman, M., Bach, F. R., & Blei, D. M. (2010). Online learning for latent dirichlet allocation. In
Advances in Neural Information Processing Systems (pp. 856-864). Proceedings of
Neural Information Processing Systems 2010.
Kant, I. (1797). The metaphysics of morals. Cambridge: Cambridge University Press.
Lakoff, G. (2004). Don't think of an elephant!: Know your values and frame the debate. Chelsea
Green Publishing.
Manning, C. D., Manning, C. D., & Schütze, H. (1999). Foundations of statistical natural
language processing. Cambridge, MA, USA: MIT press.

THINK OF THE CONSEQUENCES

42

Mimno, D., Wallach, H. M., Talley, E., Leenders, M., & McCallum, A. (2011). Optimizing
semantic coherence in topic models. In Proceedings of the conference on empirical
methods in natural language processing (pp. 262-272). Association for Computational
Linguistics.
Newport, F., & Dugan, A. (2017, August) Partisan Differences Growing on a Number of Issues.
Retrieved from https://news.gallup.com/opinion/polling-matters/215210/partisandifferences-growing-number-issues.aspx.
Nugroho, R., Zhong, Y., Yang, J., Paris, C., & Nepal, S. (2015, June). Matrix inter-joint
factorization-a new approach for topic derivation in twitter. In 2015 IEEE International
Congress on Big Data (pp. 79-86). IEEE.
Pew Research Center (2017, June). Changing Attitudes on Gay Marriage. Retrieved from
http://www.pewforum.org/fact-sheet/changing-attitudes-on-gay-marriage/.
Řehůřek, R. & Sojka, P., (2010). Software Framework for Topic Modelling with Large Corpora.
In Proceedings of the LREC 2010 Workshop on New Challenges for NLP Frameworks,
(pp. 45-50). Website: http://is.muni.cz/publication/884893/en.
Rozenblit, L., & Keil, F. (2002). The misunderstood limits of folk science: An illusion of
explanatory depth. Cognitive science, 26(5), 521-562.
Sloman, S., & Fernbach, P. (2017). The Knowledge Illusion: Why We Never Think Alone.
Riverhead Books.
Stevens, K., Kegelmeyer, P., Andrzejewski, D., & Buttler, D. (2012, July). Exploring topic
coherence over many models and many topics. In Proceedings of the 2012 Joint
Conference on Empirical Methods in Natural Language Processing and Computational
Natural Language Learning (pp. 952-961). Association for Computational Linguistics.

THINK OF THE CONSEQUENCES

43

Tan, C., Niculae, V., Danescu-Niculescu-Mizil, C., & Lee, L. (2016, February). Winning
arguments: Interaction dynamics and persuasion strategies in good-faith online
discussions. In Proceedings of the 25th international conference on world wide web (pp.
613-624). International World Wide Web Conferences Steering Committee.
Tanner, C., Medin, D. L., & Iliev, R. (2008). Influence of deontological versus consequentialist
orientations on act choices and framing effects: When principles are more important than
consequences. European Journal of Social Psychology, 38(5), 757-769.
Tetlock, P. E. (2003). Thinking the unthinkable: Sacred values and taboo cognitions. Trends in
Cognitive Sciences, 7(7), 320-324.
Thompson, W.H.W., Wojtowicz, Z., & DeDeo, S. (2018, December). Levy flights of the
collective imagination. Retrieved December 28, 2018, from
https://arxiv.org/abs/1812.04013v1.
Zhao, W., Chen, J. J., Perkins, R., Liu, Z., Ge, W., Ding, Y., & Zou, W. (2015). A heuristic
approach to determine an appropriate number of topics in topic modeling. BMC
bioinformatics, 16(13),S8.

THINK OF THE CONSEQUENCES

44

Appendix A
Corpus Pre-processing
Regular Expression Used to Select Relevant Comments
In creating the Regular expression, WordNet synsets (Fellbaum, 1998) were used to
determine words close in meaning to “gay” and “marriage”. Some of the terms include
homophobic slurs, while some are not taboo. We then removed terms with obvious alternative
meanings (such as “queen”) to reduce the amount of noise, resulting in the following regular
expression:
(^(?=.*gay|.*\\bfag|.*faggot|.*fagot|.*queer|.*\\bhomo|.*LGBT|.*GLBT|.*same.sex|.*lesb
ian|.*\\bdike|.*\\bdyke|.*sodom)(?=.*marry|.*civil union|.*marri).*$)|(^(?=.*marriage
equality|.*equal marriage).*$)
Set of Words Retained from Natural Language Toolkit’s list of Stopwords
potentially protected-values-based. should, shouldn’t, should've, shan’t, need, needn’t,
ought, must, mustn’t
potentially consequentialist. how, can, could, couldn’t, few, more, most, all, any,
against, because, why

THINK OF THE CONSEQUENCES

45

Fraction of posts on Reddit related to Same-sex Marriage

Figure A1. The fraction of all Reddit posts that is relevant to same-sex marriage (vertical axis) as a function of time (horizontal
axis).

THINK OF THE CONSEQUENCES

46

Appendix B
Ratings of Impactful Comments
Distribution of most likely topics among impactful posts
among 2000 most impactful posts. Differences in the number of sampled posts may
reflect differences in popularity, or the base rate of different topics. Topics identified as
protected-values-based by raters have IDs 12 (religious arguments), 48 (freedom of belief) and
49 (LGBT rights); topics identified as consequentialist are marked with IDs 4 (employer attitude
and regulations), 14 (cultural and historical status), 22 (politicians’ stance), 27 (children of
same-sex parents) and 28 (same-sex marriage as a policy issue). The two major topics that did
not belong to either category can be identified by IDs 16 (forcing vs. allowing behaviors) and 33
(personal anecdotes). Topic 38, with the greatest number of sampled comments in the set, had a
focus similar to topic 33.

Figure B1. The relative prominence of the 50 topics in the 2,000 most impactful comments. x-axis: The 50 topic indicators. yaxis: The number of comments for which the topic had the highest contribution.

THINK OF THE CONSEQUENCES

47

among 800 rated impactful posts. IDs are similar to Figure B1.

Figure B2. The relative prominence of the 50 topics in the 800 comments for which human ratings were elicited. x-axis: The 50
topic indicators. y-axis: The number of comments for which the topic had the highest contribution.

instructions for ratings of impactful posts (Emphasis in the original). Thank you for
your participation in this task. We are interested in better understanding the reasons behind
people’s attitudes for and against the legalization of same-sex marriage. On the next several
pages, you will see a sample of comments from the popular social media platform Reddit. Your
task is to read each comment carefully, and then answer two questions: whether the comment is
pro or against same-sex marriage, and why you think the commenter holds the attitude they do.
In particular, we ask you to rate the comment on a scale from “completely protected valuesbased” to “completely consequentialist”. Here’s what we mean:
Protected values-based reasoning invokes values about actions that people think are definitely
permissible or should be avoided, and are generally not open to compromise. For example, some
people believe that marrying someone of the same sex violates a sacred value because marriage

THINK OF THE CONSEQUENCES

48

must be between a man and a woman. Others have a protected value that people have the right to
marry the person they love. Note that while protected values-based arguments may imply belief
in certain concrete consequences (for example, that pursuing true love leads to happiness), a
person engaging in such reasoning is unlikely to change their mind based on the consequences
that result from certain actions. It is the action that is right or wrong regardless of its
consequences.
Consequentialist reasoners hold positions because of the consequences they believe the policy
will lead to. They aim for positive outcomes and want to avoid negative ones. For instance, an
opponent may believe that legalizing same-sex marriage will hurt the development of children
that may be put under the same-sex couple’s care. Proponents of same-sex marriage may believe
that allowing same-sex marriage will allow same-sex couples to have access to better benefits,
which will in turn improve their quality of life. Note that while these reasons may be rooted in
certain values (e.g. the importance of children’s wellbeing), a person holding a consequentialist
attitude would change their mind if they changed their mind about the consequences. For
example, if the opponent was convinced that being raised by same-sex couples does not
negatively impact children’s development, she might change her position.
Note that most arguments are neither completely protected-values-based nor completely
consequentialist.
example of impactful post. “Why would you think that anyone wants to force churches
to marry gay people? I've never heard anyone suggest that - ever.” (From January 2015; 1877
more upvotes than downvotes, 54% representative of forcing vs. allowing behaviors)

THINK OF THE CONSEQUENCES

49

Appendix C
Modeling Procedures and Analysis Results
LDA model
measures of predictiveness. per-word perplexity. Smaller values indicate that the model
is better at predicting unseen words and phrases. Note that per-word perplexity is lower for
evaluation sets with 25 and 50 topics, providing no evidence of overfitting. The performance on
training set that comprises most of the corpus is comparable across different numbers of topics.
Lower bound on per-word perplexity for training set:
25 topics

50 topics

75 topics

100 topics

164.95

178.35

188.54

197.47

Lower bound on per-word perplexity for evaluation set:
25 topics

50 topics

75 topics

100 topics

15.13

64.32

211.51

545.59

Perplexity Change Rate (PCR). This measure was introduced by Zhao et al. (2015) and
shown to outperform simple per-word perplexity in determining optimal number of topics. PCR
is equal to the absolute difference between per-word perplexity of two models, divided by the
absolute difference in the number of topics in each model. This measure also shows preference
for smaller number of topics (lower values are preferable):
25 topics

50 topics

75 topics

100 topics

0.61

5.28

5.89

13.36

UMass coherence. Calculated for the training set. Larger numbers indicate that the words
associated with each topic in that model are more likely to co-occur.
25 topics

50 topics

75 topics

100 topics

THINK OF THE CONSEQUENCES

-2.95

-3.74

50

-4.05

-4.31

robustness of topic contribution calculation. To test for the robustness of the
distribution of topic contributions to random initializations of estimated parameters12, we ran the
topic contribution calculation ten times and calculated the Jensen-Shannon divergence (JSD)13
between the resulting distributions. The pairwise JSD between the distributions from all runs was
effectively 0.
Word-frequency model
most predictive words. In order of decreasing informativeness regarding the
classification task, as defined in the text. Words in italic were significant predictors for the linear
model in more than half of the iterations.
Most consequentialist words. Democratic, voting, third, tried, pay, caused, fear, claim,
effect, aggressive, ring, crime, decision, campus, character, work, blame, favor, registered,
despite, kill, ruling, among, destroy, shift, air, shouldn’t, somebody, built, venue, lower, zero,
girlfriend, fiscal, likely, November, used, little, candidate, rate, adoption, men, benefit, mental,
existing, body, site, Iran, career, constitution, hospital, tomorrow, logic, multiple, arguing,
ignored, unmarried, cock, dollar, overturn, currently, administration, gain, gave, abolish, net,
seek, quickly, using, neutrality, medical, entitled, barometric, ahead, hurricane, agenda,
widespread, legislation, perfectly, homophobe, blue, sub, trade, banned, whose, awkward,
potentially, Fox, certainly, feminist, forcing, none, reform, nominee, appointed, DADT, virginia,
subject, 000, establishment

12

The gensim package’s (Řehůřek & Sojka, 2010) implementation of the algorithm to estimate topic-word
distributions, which we used to estimate each term of the topic contributions (see section “Calculating topic
contributions”), randomly initializes model parameters.
13
We used the naïve calculation of JSD implemented by the THOTH Python package, available at thoth-python.org.

THINK OF THE CONSEQUENCES

51

Most protected-values-based words. clear, evidence, Jesus, terrible, 2012, different, 100,
pray, ethnic, lil, culture, moral, month, directly, looking, opposition, fundamentalist, wearing,
figure, gonna, met, God, felony, repeatable, Zeus, Estonian, trip, music, religion, thinking,
unnatural, within, stupid, board, weird, ask, impose, rally, federally, write, shitty, standing,
weekend, clerk, wanting, debated, licence, technically, faggot, map, ridiculous, knew,
experience, required, Netherlands, pro, sin, xd, hispanic, unit, art, home, fuck, pot, believe,
Christian, personal, away, treated, Catholic, holy, respect, focus, belief, money, brother, clapped,
committing, silly, morning, becomes, discriminate, accepted, opposing, recent, thus, quiet, visit,
defending, burn, southern, sitting, defense, provide, mostly, Francis, Chinese, interviewed,
attacking, devil
log odds of discourse assuming a consequentialist frame based on the wordfrequency model. Figure C1 shows the estimated log odds that the subset of the corpus from
each month was generated by a consequentialist frame. In particular, each point is the sum ( )
over every observed word in month

of the log odds that that word was generated under a

consequentialist frame:
( ) = ∑
where

is the number of comments from month

cardinality of

∑| | (
,

is defined as the number of words in

) (3)

is the

comment from month

, the

and wij is defined as in equation (2). Log

odds are mostly greater than zero, showing consistent advantage of consequentialist discourse
over time (see Figure 6 in the main text).

THINK OF THE CONSEQUENCES

52

Figure C1. The log odds of the observed discourse in each month under the assumption of a persistent consequentialist frame
(see text for details). The blue line tracks the mean and the shaded region indicates the 95% confidence region calculated based
on 100 instances of the word-based model, each trained on a different set of comments consisting of 90% of the expertly-labeled
data. The black vertical line to the left marks the beginning of a steady upward trend of support for same-sex marriage among a
majority of Americans (Gallup, 2017). The vertical line to the right marks the Supreme Court ruling that legalized same-sex
marriage.

THINK OF THE CONSEQUENCES

53

Appendix D
Unique or Almost Unique High Probability Words and Example Comments for Top Topics
Unique high probability words are words among a topic’s list of 40 words with highest
prior probability that were not found in similar lists for other top topics. Almost unique high
probability words were shared with only a single other top topic. The words are ordered based on
probability given the relevant topic. The two sets of high probability words are followed by a
representative post randomly chosen from the set of posts in the corpus most representative of
that topic. Representativeness is operationalized as the percentage of words in the comment for
which the associated top topic is the most probable topic. The full sets of high probability words
for all topics can be found in supplemental materials. The full set of representative comments can
be found in the study’s online repository.
Protected-values-based Topics
religious arguments. Unique. God, Bible, Islam, Jesus, Christianity, else, tell
almost unique. Christian, sin, believe, Muslim, wrong, everyone, anyone
representative post (representativeness = 0.73). I understand that many people interpret
the bible to say that God doesn't approve of gay sex, but when I interpret the bible or any other
book that makes claims about what God does or doesn't like, I always ask myself what is the
reason? If God tells us not to do something, he should have a very good reason for it, like don't
murder, that makes sense because it harms people, so I can believe this command comes from
God, no problem. But what could God possibly see wrong with two people of the same sex, who
love each other, getting married? Who does this harm, you don't believe God gives us arbitrary
rules do you?
freedom of belief. unique. belief, opinion, others, atheist, based, respect

THINK OF THE CONSEQUENCES

54

almost unique. believe, wrong, agree, choice, freedom, personal, moral, Christian,
disagree, person
representative post (representativeness = 0.69). I think religion is based on personal
opinions. If you personally don't like gay marriage, abortion and evolution, that is your choice,
you don't have to get gay married, have an abortion or believe in evolution. When you try to
enforce others to believe what you believe, that is based on your traditional understanding that
people should follow your tradition which they will attribute to religion.
LGBT rights. unique. LGBT community, trans, movement, fight, fighting, plebiscite,
conversion, wing, push, anti-LGBT, denying, activist, ya, deserve, overturning, proud, fire,
liberalism, rainbow
almost unique. equal, support, away
representative post. (representativeness = 0.48). Fundamentally, the right to form
coequal legal relations ought to be available to homosexuals as a matter of Due Process. That is,
we're getting confused about what a right is. A right is not susceptible to plebiscite. If it were, it
would be superfluous qua right. The "people" of California, Arkansas, Florida, etc., can no more
vote on the rights of homosexuals to marry than they can vote on the rights of Jews or Puerto
Ricans, for example, to speak or to associate. The entire point of a right is to protect minorities
from majority tyranny. These ballot measures, as a vehicle to attack an individual right, are
extremely dangerous not only to the rights of homosexuals, but also to all other individual rights.
Consequentialist Topics
politicians’ stance. unique. anti, supported, changed, pro-gay, politically, opposes, mind,
considering, 90’s, pro-choice

THINK OF THE CONSEQUENCES

55

almost unique. support, Hillary, Clinton, Libertarian, position, said, politician, anti-gay,
pretty, actually, campaign, came, Bill
representative post (representativeness = 0.68). Either it was politically expedient for
him to claim not to support gay marriage, or it was politically expedient for him to not support
DOMA. I think his overall posture on gay rights while in office (DOTA, etc) lends support to the
former view.
children of same-sex parents. unique. child, parent, divorce, adoption, adopt, sign,
adult, baby, joke, rate, raise, home, son, raising, worried, parenthood, adopted
almost unique. better
representative post (representativeness = 0.76). Because it affects society in general. We
know an alcoholic abuse parent has an affect on his/her children. We also know that children
who are raised in single parents homes are affected by that. Why wouldn't Gay marriage and the
right for gays to adopt affect a child? And children grow up and they affect society.
same-sex marriage as a matter of policy. unique. political, Left, important, climate,
immigration, economic, major, far
almost unique. issue, social, policy, etc., party, politics, side
representative post (representativeness = 0.68). People apathetic to politics will stay
apathetic to politics. Especially when there's a good chance the issue doesn't make a difference to
them. How will gay marriage affect the average heterosexual either way? There's no good reason
to *not* be apathetic. Personally, I'm straight and I think the current setup of marriage is
inequitable, but most don't.

THINK OF THE CONSEQUENCES

56

employer attitude and regulations. unique. job, Sanders, OP, evil, owner, trade, sell,
employee, SSM, 2009, blow, EU, depending, argued, class, reach, store, donor, realise, career,
category, guilty, lesser, 2003, fly, tolerate, buying, threw, 2011, assault, Rubio, oil
almost unique. protected
representative post (representativeness = 0.27). And it is freedom from consequences if
the government is your employer. Especially if it's political speech. If back in 1950 I said I
support gay marriage and was fired from a government job for supporting gay rights vocally, I
constitutionally could not be fired.
cultural and historical status. unique. traditional, modern, Tory, value, destroy,
Islamic, China, duty, legalisation, Hilary, attack, recognised, dunno, Baptist, cult, nationally,
Adam, unit, century, civilization, wasn’t, badly, Arab, monogamy, designed, household,
aggressive, vague, reached, warrior
representative post (representativeness = 0.32): I don't think gay "marriage" devalues
anyone else's marriage. This isn't a values issue for me. I'm concerned for society and want to
preserve and protect its traditional structure which is based on the nuclear family only. I don't
feel that my marriage isunder attack, but I do feel the society I grew up in is.
Major Topics Categorized as neither Protected-Values-Based, nor Consequentialist
personal anecdotes. unique. woman, man, men, lesbian, wife, husband, male, girl,
female, bi, bisexual, another, always
almost unique. friend, dude, relationship, partner
representative post (representativeness = 0.65). Yeah, I've noticed something similar to
this. I haven't even been in a long-term relationship with a woman, and my situation is much
different (I'm married to a man who allows me to enjoy being with women because he

THINK OF THE CONSEQUENCES

57

understands). I'm incredibly up front about this situation when I'm talking to women that I'm
interested in 'getting to know further' and they always ask "why don't you just tell your husband
you're a lesbian then?" I've gotten that from a couple women and am always slightly irritated by
it. I have to keep saying "it’s not that I don't enjoy sex with my husband, it’s that he's not a
woman, and I like those too."
forcing vs. allowing behaviors. unique. allowed, legally, fine, nobody
almost unique. getting, able, shouldn’t, forced, let, understand, anyone, happy
representative post (representativeness = 0.71). Because it does no impact my life at all.
If two straight people get married it does not affect my life, just as if two gay people go get
married. So who am I to tell two consenting adults they can't do something that will not actually
hurt anyone, but make them very happy.
