---
title: "The Cultural Evolution of National Constitutions"
person: david-krakauer
section: by
type: journal-article
year: 2017
date: 2017-11-18
venue: "arXiv (Cornell University)"
authors: "David C. Krakauer et al."
source_url: https://doi.org/10.48550/arxiv.1711.06899
retrieved: 2026-08-13
content: full-text
notes: "OA (green); OpenAlex W2952369845; cited_by 0. Extracted via pypdf from https://arxiv.org/pdf/1711.06899."
---

# The Cultural Evolution of National Constitutions

## Full text

The Cultural Evolution of National Constitutions
Daniel N. Rockmore, 1,2,3,4∗ Chen Fang,1 Nicholas J. Foti, 5
Tom Ginsburg,6 David C. Krakauer 3
1Department of Computer Science, Dartmouth College, Hanover, NH, USA 03755
2Department of Mathematics, Dartmouth College, Hanover, NH, USA 03755
3The Santa Fe Institute, Santa Fe, NM, USA 87501
4The Neukom Institute for Computational Science, Dartmouth College, Hanover, NH, USA 03755
5Department of Statistics, University of Washington, Seattle, WA USA 98195-4322
6University of Chicago Law School, The University of Chicago, Chicago, IL, USA 60637
∗To whom correspondence should be addressed; E-mail: rockmore@math.dartmouth.edu.
November 21, 2017
Abstract
We explore how ideas from infectious disease and genetics can be used to uncover patterns of
cultural inheritance and innovation in a corpus of 591 national constitutions spanning 1789–2008.
Legal “Ideas” are encoded as “topics” - words statistically linked in documents - derived from topic
modeling the corpus of constitutions. Using these topics we derive a diﬀusion network for borrowing
from ancestral constitutions back to the US Constitution of 1789 and reveal that constitutions are
complex cultural recombinants. We ﬁnd systematic variation in patterns of borrowing from ancestral
texts and “biological”-like behavior in patterns of inheritance with the distribution of “oﬀspring”
arising through a bounded preferential-attachment process. This process leads to a small number of
highly innovative (inﬂuential) constitutions some of which have yet to have been identiﬁed as so in the
current literature. Our ﬁndings thus shed new light on the critical nodes of the constitution-making
network. The constitutional network structure reﬂects periods of intense constitution creation, and
systematic patterns of variation in constitutional life-span and temporal inﬂuence.
Introduction
Cultural inheritance involves the diﬀusion of innovations, a process of interest to both biologists (Hart &
Clark, 1997) and social scientists (E. M. Rogers, 1995). In biology inheritance is governed by mechanisms
of genetic transmission, which have been quantiﬁed (Christiansen, 2008). Cultural inheritance takes a
variety of forms which can resemble variants of biological inheritance (Sforza & Feldman, 1981; Richerson
& Boyd, 2006; Mesoudi, Whiten, & Laland, 2006), including cultural selection (D. S. Rogers & Ehrlich,
2007; Pagel, 2013). In cultural domains, complex forms of knowledge are encoded in social norms, legal
principles and scientiﬁc theories (Wimsatt, 1999; Kaiser, 2009) and follow complex forms of transmission
1
arXiv:1711.06899v1  [cs.SI]  18 Nov 2017

that involve the coordinated borrowing and learning of constellations of ideas, producing a diversity of
phylogenetic patterns (Mace & Holden, 2004).
Now that a large body of the cultural record has been digitized (including books ( The Google books
website, n.d.), music ( International Music Score Library Project , n.d.), art ( ARTstor, n.d.), etc.) new
techniques of machine learning are making the quantitative analysis of high-dimensional cultural artifacts
possible. In analogy with the biological sciences, and genetics in particular, this data mining approach to
the analysis of culture is sometimes referred to as “culturomics” (Michel et al., 2010), a term born of the
consideration of the frequency distribution of ann-gram in the Google Books corpus over time (The Google
books N-Gram Viewer , n.d.) as proxy for how memes move in and out of the cultural record. Literature
(and text generally) remains a primary focus of such work (see e.g., (Moretti, 2005; Jockers, 2013; Hughes,
Foti, Krakauer, & Rockmore, 2012)). A fascinating challenge is to supplement these correlation-based
approaches to the understanding of cultural evolution with principled causal mechanisms directed at
discovering fundamental, extra-biological evolutionary processes.
We consider the notion of diﬀusion patterns in the study of cultural inheritance as a means of tracking
the diﬀusion of topics through the documents in a legal text corpus of ﬁve hundred and ninety-one national
constitutions (the full list is given in the Supplementary Materials Table S1). “Topics” has a technical
meaning here (and throughout this paper that is the sense in which the word is used) as probability
distributions over words (positive weights that sum to one) that are the output of topic modeling, which
is a computational and statistical methodology for text analysis that has made great inroads throughout
the humanities (see e.g., (Riddell, 2014)), to the point of reaching an almost “plug-and-play” form (see
e.g., ( Stanford Topic Modeling Toolbox , n.d.)) for easy deployment. A set of topics is “learned” (i.e.,
automatically derived) from the corpus. The various topic distributions highlight (i.e., attach high weight
to) diﬀerent sets of words. In the best cases those words usually suggest a particular theme and associated
labeling of the topic. Texts in the corpus are partitioned into chunks, which are thus represented as varying
weighted mixtures of topics. In this way topics provide a low-dimensional representation of the corpus
in terms of higher level ideas and provide a rigorous operational basis for a meme, to be tested against a
suitable dynamics of inheritance. Although we focus on its use in the analysis of text, the topic modeling
framework is more general and has been used in a number of areas (Blei, 2012).
Given a topic of some signiﬁcance in a work, embodied in a set of semantically correlated legal
concepts, we track its appearance and prevalence in subsequent constitutions within the corpus, as well
as its extinction. While dynamical considerations have been incorporated previously into topic models
(Blei & Laﬀerty, 2006; Wang & McCallum, 2006) this analysis diﬀers in that we account for the diﬀusion
of topics from document to document, and in this way reveal more clearly the patterns of genealogy and
2

the essentially recombinant nature of textual artifacts. These resemble in the parallel domain of invention
the recombinant quality of patents (Youn, Strumsky, Bettencourt, & Lobo, 2015). It is our contention
that while culture is clearly an active in situ feature of human brains (Boyd & Richerson, 1996), it is also
present in material artifacts which aﬀord rich forms of combinatorial manipulation and transmission ex
situ.
The corpus of national constitutions is particularly well-suited to a framing and analysis as a document
corpus composed of units of correlated meaning evolving according to idea diﬀusion and borrowing.
Indeed, scholars have demonstrated that many provisions in constitutions are copied from those of other
countries. For example, through n-gram analysis Ginsburg et al. (Foti, Ginsburg, & Rockmore, 2014)
show that constitutional preambles, which are conceptualized as the most nationally localized part of
constitutions, also speak in a universal idiom and include a good deal of borrowing. Law and Versteeg
(Law & Versteeg, 2011) have shown that rights provisions have spread around the globe. Elkins et al.
(Elkins, Ginsburg, & Melton, 2009; Elkins, Ginsburg, & Simmons, 2013) show that some rights, such
as freedom of expression, have become nearly universal, while others have not. Some even argue that
there is a kind of global script at work, whereby nation-states seek to use constitutions to participate in
global discourses (Go, 2003; Boli-Bennett, 1987; Law, 2005). This evolutionary framing of the creation of
national constitutions draws on broader biological analogies for legal development across time and space
(Watson, 1974). Our use of diﬀusion trees as a framework for the study of this problem (see the Methods
section in the Supplementary Materials for details) can be seen as a novel quantiﬁcation of this biological
analogy.
It is important that we are clear that this integration of topic modeling and diﬀusion networks enables
only a quantitative articulation and tracking of instances of thematic similarity over time. The links we
demonstrate across texts are consistent with a model in which one text inﬂuences another. However,
our approach does not demonstrate the speciﬁc mechanisms by which inﬂuences are transmitted, so we
focus instead on the sequential patterns in which textual material ﬂows across time and space. As we
demonstrate in our Discussion, this enables an analysis enhancing traditional scholarly opinion as regards
the usual notion of “inﬂuence”, while also at times uncovering temporal connections suggesting further
or new investigations.
Results
As mentioned, a topic is a probability distribution over a ﬁxed vocabulary derived from a text corpus. It
thus represents a correlated set of words encoding something like a “meme” or stochastic set of associ-
ations. (Technically, the pre-processing of the texts may result in some elements of the vocabulary set
3

that are not words per se, but instead word stems, often called “tokens”. We will use the more colloquial
term “word” in this paper.) The text corpus is partitioned into documents, sets of roughly contiguous
groupings of 500 words. This is a standard topic modeling document length, short enough to reﬂect
local context and long enough to make sensible the statistical model. In the best case each constitution
would be partitioned into contiguous word-blocks, but processing may remove the odd abbreviation, ti-
tle, etc. besides respecting natural boundaries, such as the end of one constitution and the beginning
of another. In the case of our corpus of constitutions, each constitution generally comprises a subset of
such documents. The model does not take into account word order, just which words occur and in what
frequencies. This is the so-called “bag-of-words” model or representation, which is then encoded as a
probability distribution over the vocabulary (the frequencies are positive and sum to one).
Topic modeling is a methodology for learning topics such that each document (represented as a bag
of words) is represented as a weighted sum (mixture) of topics. In its generative form, the topic model
encodes the creation of each document by ﬁrst choosing a topic according to the mixture of topics that the
document comprises and then choosing a word according to the distribution of that particular topic. In
this respect a constitution can be thought of as a “meme cloud” with the topics encoding the memes. We
use the latent Dirichlet allocation (LDA) topic model (see (Blei, Ng, & Jordan, 2003) for a discussion of
the various parameters that deﬁne the model). LDA is eﬀectively the topic modeling industry standard.
We tested several choices for the number of topics and chose 100 which we then validated (cf. the Methods
section in the Supplementary Materials for details).
The output of the topic model forms the basis for our results. They include (1) the discovery of the
topics that make up the corpus of constitutions, (2) the determination of their ﬂow through time (“in-
formation cascades”), (3) the reconstruction of cultural diﬀusion trees; (4) network analysis of diﬀusion
trees; and (5) discovery of a very biological pattern of inheritance with a highly skewed pattern of cultural
fertility.
Topics
The 100 topics were “hand-labeled” by a constitution expert. Note that “hand-labeling” of topics is
standard. Further elaboration on this can be found in our Discussion. Since generally each constitution
comprises a set of corpus documents we assign an overall constitutional weight for a topic as the average
topic weight over the documents that it comprises. In Table 1 we list the ten topics with largest average
topic weight (over all the constitutions), along with the ten most probable (heavily weighted) words (in
decreasing order) for each topic. 1
1A full list of the topics, in order of average weight, with the weights of the top 20 words can be found at
https://www.math.dartmouth.edu/∼rockmore/topics weight order.txt.
4

Topic name Top 10 words in topic
General rights right rights citizens freedom law
public guaranteed citizen everyone religious
Sovereignty national people sovereignty law rights
state ﬂag language international equal
public order law public cases order one
property laws authority liberty civil
separation of powers congress executive laws power ministers
state secretaries order necessary public
organic law law government president organization national
organic public laws social functioning
socialism people socialist country revolution working
popular citizens system society development
legislative sessions session deputies sessions deputy members
elected ﬁrst vote majority extraordinary
bureaucracy papers years state department necessary
respective individuals departments body power
socialism legislature people organs state supreme work
organ presidium elected decisions committees
Table 1: Most popular topics across entire corpus, and their corresponding top 10 words. A full
list of the topics, in order of average weight, with the weights of the top 20 words can be found at
https://www.math.dartmouth.edu/∼rockmore/topics weight order.txt.
Inﬂuence and clustering
The identiﬁcation of the topics now gives a natural way to represent a constitution as a mixture of
probability distributions. With that, we can compare quantitatively constitutions and get at a quanti-
tative notion of inﬂuence, completely driven by the data of the words. A ﬁrst coarse pass at this is to
create a constitutional “family tree”, where the (unique) immediate ancestor of any given constitution
is simply the constitution closest to it among all earlier constitutions. Given that our constitutions are
now represented as probability distributions (over topics), a natural measure of distance is the Kullback-
Liebler (KL) divergence. Recall that the KL divergence of probability distributions P andQ is deﬁned as
KL(P||Q) = ∑
iP (i) logP (i)
Q(i). KL is inherently non-symmetric. A standard interpretation 2 is the degree
to which a distributionQ approximates another distributionP . So thinking of an earlier constitution as a
potential model for a newly written constitution, the KL divergence of their underlying topic probability
distributions is a natural measure of similarity.
The “KL Constitution Tree” is shown in Figure 1. Note that the ﬁgure is not scaled horizontally for
time. The size and form of the representation presents some diﬃculty for reproducing legibly herein, so
a separate pdf document, readily magniﬁable, can be found online. 3 We also include a detail.
2See e.g., https://en.wikipedia.org/wiki/Kullback-Leibler divergence.
3See https://www.math.dartmouth.edu/∼rockmore/kl-tree.pdf.
5

The KL-tree is a coarse and aggregate articulation of the notion that constitutional ideas ﬂow in
time. It is also purely correlative and local. We should also like to explore global patterns of inﬂuence
and the possibility of causal inﬂuence. We approach this by considering the “ﬂow” of topics through
constitutions and through time. Each instance of a topic ﬂowing appearing in a constitution (above
some ﬁxed threshold) is treated as a “cascade”. We follow standard conventions (Leskovec, McGlohon,
Faloutsos, Glance, & Hurst, 2007) and deﬁne an information cascade as a collection of constitutions
and their timestamps where each topic in the constitution makes up a proportion greater than a robust
threshold value. When two constitutions (nodes) both express a topic above threshold then we consider
this pair as a candidate for information “cascading” from the earlier to the later.
The topic cascades form the underlying data for a mode of inference for how ideas represented by
topics are likely to have propagated through the corpus over time. As stated previously, we view the
observation of a topic (above some threshold) in two constitutions as a quantitative measure indicating
correlation across time. Given the content of the topics and the fact that the constitutions are ordered
chronologically and typically clustered spatially (see the Network Analysis subsection below and Figure
2), shared topics may very well have spread from the earlier to the latter, and hence are at least consistent
with weak causality. In order to learn the most likely propagation structure of the topics (given the data)
we estimate an underlyingdiﬀusion network for the corpus (Gomez-Rodriguez, Leskovec, & Krause, 2012).
A diﬀusion network is a directed graph with nodes corresponding to constitutions and where the edges
satisfy the condition that the source constitution predates the destination constitution. This imposes
weak causal structure on the correlations. Importantly, we do not observe the diﬀusion network, but only
the cascades that are assumed to diﬀuse over it and are consistent with it. In brief, a probabilistic model
describing the consistency of the observed cascades with respect to a ﬁxed diﬀusion network is deﬁned.
The diﬀusion network is that which (approximately) maximizes this probability (Gomez-Rodriguez et al.,
2012).
The presentation of the full diﬀusion tree on our corpus presents some visualization challenges. To
give a sense of what it looks like, Figure S1 shows the entire learned diﬀusion tree on a restricted set of
ninety-nine constitutions. Even this is too dense to be inspected visually for information, but the ﬁgure at
least gives a good sense of the way in which the methodology reiﬁes the phenomena of the idea diﬀusion.
Each of the edges (directed and extending downward) indicate particular topics diﬀusing forward in time
to be taken up by subsequent constitutions. Issues of readability make it impossible to put labels on
the various edges. The optimization algorithm that produces the diﬀusion network only collects a subset
of the topics that appear in a constitution. Some diﬀuse forward, others do not. The “oﬀspring” of a
given constitution thus borrow certain “ideas” of the parents, but others are created afresh, presumably
6

depending on legally appropriate contextual factors.
Network analysis
In order to discern patterns in the diﬀusion tree the diﬀusion network is subjected to a clustering analysis.
This picks out communities of constitutions by methods of community detection and optimal modularity
in which groups of constitutions which share topics – and thereby a directed edge – in an amount above
that expected by chance. Such a community constitutes a cluster (Newman, 2006). Figure 2 displays the
results of a network reconstruction of the full circuit along with two color codings of the network resulting
from the application of two forms of clustering analysis to the network. The network is illustrated using
spring embedding whereby densely connected nodes appear packed together. The network has the form of
a “constitutional caterpillar” with a temporal spine threaded through the network spanning 1789 to 2014
(Figure 2A). This temporal structure is very clear in the clustering coloring. Using community structure
algorithms (Girvan & Newman, 2002) we observe (Figure 2B) three clear constitutional communities,
each of which describes a span of time: epoch 1: from 1789 to 1936; epoch 2: from 1937 to 1967; and
epoch 3: from 1968 to 2014. Using a spectral technique for community detection we can further partition
(Figure 2C) these network data into higher order communities (Newman, 2006). This analysis maintains
the chronological structure and illustrates the way in which clusters that are growing in absolute size
(more constitutions in each) have evolved to encompass roughly decreasing ranges of time.
Each constitution in the diﬀusion tree can be described in terms of its transmission motif – “t-motif” ,
a visualization of the indegree and outdegree for each constitution. A selection of these motifs is shown in
Figure 3 with a full set in Supplementary Materials Figure S2. The motifs demonstrate the variation to
be found in balancing in-bound and out-bound inﬂuence for each constitution. Early constitutions tends
to have few parents (e.g., Canada only has one – the US constitution) whereas subsequent constitutions
vary signiﬁcantly in their ancestry. This variation can be explained thorough a combination of both
time (earlier constitutions present more opportunities for imitation) and how representative, novel and
applicable each constitutions is as a model for imitation.
Models for transmission
We can gain further insights into the patterns of inheritance by studying directly the distributions of
indegree and outdegree across the entire dataset. Figures 4A and 4B represent the pdf (probability density
function) and cdf (cumulative distribution function) for the indegree for all constitutions. Illustrated
in blue is the data and in orange the maximum likelihood parameter estimates for the best ﬁtting
distribution. The indegree distribution is well-captured by a Gaussian distribution with a mean of 8 .8
7

and a standard deviation of 2.9. The estimated distribution does tend to slightly underestimate the mean
but captures the tails very accurately. A straightforward interpretation is one of independent sampling
of possible sources. The outdegree however, is quite diﬀerent. Figures 4C and 4D show the best ﬁtting
Poisson distribution and the outdegree distribution. Whereas the mean is eﬀectively recovered, the tails
of the distribution are poorly ﬁtted; the Poisson underestimates the number of constitutions with few
oﬀspring and overestimates the number of constitutions with many oﬀspring. On the other hand consider
Figures 4E and 4F where we show the best ﬁtting negative binomial distribution to the data. This very
accurately recovers the entire oﬀspring distribution with maximum likelihood parameter estimates for
the two shape parameters of the distribution asr = 2.5 andp =.22) Recall that for a negative binomialr
describes the number of oﬀspring observed before no more oﬀspring are generated and that the probability
of producing an oﬀspring is given by the value of p. We view this as a pure birth process as constitutions
never die – in the sense that they are always available as inspiration for a newly written constitution.
Moreover, the negative binomial distributions are well known to be attractors of the Yule process (Karlin
& Taylor, 1975), also known as “preferential attachment” (van der Hofstad, 2017) . The excellent ﬁt
of outdegree to this distribution has broader implications for connections between oﬀspring number and
longevity. In short, that we witness a small number of constitutions of relatively early constitutions of
enduring inﬂuence. All of this – including the attendant modeling considerations – is considered in some
greater detail in the Discussion below.
Growth and Lifespans
We are able to track the number of new constitutions written over time. We ﬁnd statistical evidence
for three epochs of authorship reﬂecting three distinct rates of growth (Figure 5 inset). These three
growth phases coincide with the three temporal groupings of the transmission graph determined through
spectral clustering. Hence there is an association between the growth rate and the detailed community
structure of the graph. We also ﬁnd signiﬁcant variation in the lifespan of constitutions. The lifespan is
deﬁned as the ﬁrst appearance to the last instance of inﬂuence. There is a strong association between
how early a constitution is written and how long it is observed to live. Unlike biological life spans nearly
all constitutions “die” young (Figure 5).
Discussion
We have searched for regular patterns of transmission in complex cultural artifacts. If there are cultural
analogs to genotypes, and perhaps even phenotypes if we were to consider the broader context of constitu-
tional inﬂuence, we should be able to observe their signatures in a temporally resolved study of evolving
8

documents. Much like organisms that adapt to local environments, constitutions must be adapted to
local cultural and legal conditions to be eﬀective. And as with organisms, a great deal of variability in
constitutions has been documented or inferred as derived from ancestral documents.
Our deeper discussion of the results starts with the labeling of the topics. We had an expert in
constitutional law inspect the learned topics and provide labels for them corresponding to the dominant
theme of the most probable words in each topic. We note that providing labels for the learned topics is
a challenging task due to the lack of ground truth. Assigning labels to topics in our setting is essentially
projecting the learned topics onto one’s conception of constitutional law and (admittedly) depends heavily
on the individual involved contributing both bias and variance to the procedure. We assume that an expert
in the ﬁeld mitigates both of these eﬀects and allows us to study the corpus using the learned topics.
Perhaps given the nature of the topic labeling problem (a general lack of ground truth) there is not
much prior work on solving it. An early line of research examined whether commonly used predictive
measures of topic models correlated with human interpretation of the topics and found that they did
not (Chang, Boyd-Graber, Gerrish, Wang, & Blei, 2009). This previous work also was the ﬁrst to use
human experiments to evaluate the interpretation of learned topics. More recent work has focused on
incorporating knowledge bases of topics (e.g., WordNet) directly into topic models in order to encourage
the model to learn topics that are interpretable by biasing them to look like topics in the knowledge base
(Wood, Tan, Das, W. Wang, & Arnold, 2016). This is an interesting and diﬃcult problem and further
progress on it would enhance the results of this paper.
The motifs (Figures 3) illustrate clearly how constitutions are “cultural recombinants” borrowing
extensively from their ancestors. Constitutions vary in their hybridicity. The motif variations suggest
a constitution taxonomy, of minor, major, idiosyncratic, and innovative depending on where in the
distribution matrix (divided via the median in both dimensions) the indegree and outdegree lie. As an
example of a minor constitution, consider Switzerland 1848. It had no descendants and only two parents
(Liberia 1847 and El Salvador 1843, both of which are probably explained by temporal proximity.) A
major constitution, on the other hand, might be Thailand’s 1932 Constitution, which established a
constitutional monarchy and a European style administrative system: it had 15 parents and 33 oﬀspring,
making it the third most densely networked in the data. Idiosyncratic constitutions include those of
Burkina Faso 1991 and Lesotho 1983, with twelve and nine parents respectively, but only a single oﬀspring
each. Some 20% of texts in the data have a child/parent ratio of 0 .5 or less, indicating more than twice
as many parental relationships as oﬀspring. On the other hand, some 8% of constitutions in the sample
have a child/parent ratio of two or more, indicating relatively high levels ofinnovation. Examples include
Zambia’s 1991 constitution, with 4 parents and 11 oﬀspring, or Micronesia’s constitution of 1990, with 8
9

parents and 24 oﬀspring; in the latter case, it may be that the oﬀspring are in fact those of the United
States 1789, which was a very close model for Micronesian drafters. In general, parent-child relationships
are temporally proximate, and they are often geographically proximate. This reﬂects the more general
ﬁnding in the literature that time and space are powerful determinants of constitutional content. This
diversity highlights an important diﬀerence from biology where species of organisms show far less variation
in the basic mechanics of transmission.
Returning to the highlighted portion of Figure 1 to illustrate the mechanisms at play, consider Egypt’s
1923 Constitution and its relationship with those of its descendants. Examining the top ten topics in each
text, Egypt 1923 shares multiple topics with Albania 1925 (topics act and public oﬃce) and Iraq’s 1925
documents (civil service and monarchy) Burundi (public oﬃce and labor) and one with Yugoslavia 1931
(mandate). No other constitutional dyad feature these combination of topics in the same density. While
the inﬂuence of Egypt’s 1923 Constitution is well known to scholars of the Arab region, it also seems
to share similarities with other documents drafted shortly thereafter in neighboring parts of Europe and
Africa. This illustrates how our method can point scholars to look at new links that conventional analysis
might not identify.
The most fecund constitution in our network is surprising at ﬁrst glance: Paraguay’s 1813 Consti-
tution. It makes sense, however, when one realizes that Latin America is the home to a plurality of
constitutional texts, because it is a region of old nation states and frequent turnover (Elkins et al., 2009).
Paraguay’s was the ﬁrst constitution adopted in Latin America after the Spanish Constitution of Cadiz
of 1812. That document embodied an ill-fated attempt to establish a liberal constitutional monarchy in
Spain, featuring equality under the law and popular sovereignty, and is recognized as a model for the
constitutions of Norway of 1814, Portugal of 1822 and Mexico of 1824. The top topic in this Constitution,
“language of law” consists of generic legal terms that are, of course, widely used in constitutional texts.
So the inﬂuence was more formal than substantive.
Conversely, some canonical constitutions do not indicate the same kind of inﬂuence in our analysis
that conventional analysis would expect. For example, the 1936 Constitution of the Soviet Union is well
known as a major step in the ideological development of communism in that it incorporated many rights
that were never implemented. Yet at the level of ideas, much of this involved borrowing from extant
models, such as the 1931 Republican constitution of Spain. Perhaps unsurprisingly, there was little new
that was in the USSR’s constitution and so it has few children. Similarly, the Weimar Constitution of
1919, which was thought to have embodied social democratic ideas (Venter, 2013), in fact was squarely
within the topical mainstream of its time. With six parents and nine oﬀspring, it is near the medians and
its oldest direct ancestor is only 14 years prior to it. It shares three of its top ten topics (”geography”,
10

”human rights”, and ”education”) with Spains Republican Constitution of 1931, which is regarded as an
important and inﬂuential text. Its last direct descendent is the 1936 Constitution of the Soviet Union,
with which it shares the topic ”social development.” This supports the claim that our method emphasizes
ideological connections across text, because the Weimar Constitution is generally considered to have been
a structural model for France’s 1958 Constitution (Skach, 2006) though ideologically perhaps closer to
that of the USSR.
The notion of “cultural recombination” imports one kind of biological analogy to the evolution of
constitutions. The distributions of the indegree and outdegree support diﬀerent biological analogies.
Consider again the striking result of the ﬁt of the outdegree distribution to the negative binomial and
the indegree to the Gaussian. A principled way to understand these distributions is to derive them from
suitable stochastic processes. The Gaussian distribution arises naturally from the sum of independent
random variables with a well deﬁned mean and variance. Poisson distributions are attractors of the
Galton-Watson process whereas negative binomial distributions are attractors of the Yule process (see
e.g.(Karlin & Taylor, 1975)). Both Poisson and negative binomial oﬀspring distributions are observed
frequently in biological systems. The Galton-Watson process was derived to explain the extinction of
family names. The idea is that at each generation a parent can transmit their name to some number of
0, 1,...,n oﬀspring. Each parent samples the number of oﬀspring independently from the same distri-
bution. Our data support a negative binomial distribution so we shall focus on the Yule process. The
Yule process is also well known as a preferential attachment process (van der Hofstad, 2017) as it can
be derived from an “urn process” in which balls of a given color are sampled in linear proportion to the
number of balls already in each urn. The negative binomial distribution is derived by solving a simple
recurrence equation describing the temporal evolution of a probability distribution of the form,
P′
n(t) =−nλPn(t) + (n− 1)λPn−1(t).
HerePn(t) is the probability of ﬁndingn constitutions at timet. The rate of oﬀspring production in some
intervalδt is parameterized by λ. Hence at a time t a number n of constitutions will decline through the
addition of more oﬀspring proportional to nλPn(t) and increase through the production of oﬀspring by
the classn−1 at a rate (n−1)λPn−1(t). If we establish an initial condition as the number of constitutions
at the start of constitutional history as 1, P0(0) = 1, we ﬁnd that,
Pn(t) = ( n− 1
n−n0
)e−λn0t(1−e−λt)n−n0.
Which takes the form of the negative binomial distribution in which we observe exactly n0 oﬀspring in n
trials with a success probability, p =e−λt. For a formal exposition of preferential attachment dynamics
illustrating the relationship of negative binomials to the special case of power laws see (Ross, 2013).
11

We can test the assumptions of the Yule process by looking directly at the imitation dynamics of
any given constitution. We simply plot the date on which the descendant of a given constitution was
created against the order in which it was created. In Figure 6A we look at the evolution of the ﬁrst
20 constitutions. By far the majority have fewer than 10 oﬀspring and these oﬀspring span a range of
under 50 years. However a few of these constitutions are exceptional. The most remarkable is the 1813
constitution of Paraguay that has provided material for 70 descendant constitutions in a temporal range
extending 200 years. This is followed by the original constitution of the Unites States of America from
1789 that produces 20 descendant constitutions, and over a span of 80 years. The Canadian constitution
of 1791 produces 11 descendants over 150 years. Figure 6B includes the ﬁrst 100 constitutions, 6C the
ﬁrst 200 , and 6D all 591 in the data set. A clear relationship between oﬀspring number and longevity
emerges consistent with preferential attachment in which a small number of constitutions are of dominant
inﬂuence, these appeared early in constitutional history gaining a signiﬁcant foothold, and with the vast
majority of constitutions both short lived and producing less than 10 oﬀspring.
The analysis of cultural recombination through a principled decomposition of textual artifacts suggests
new domains of cultural inheritance. Unlike simple Mendelian systems, or simple learning models with
homogeneous rules, we observe diverse patterns of variation in the way in which nations encode important
moral and legal principles. Moreover we can obtain a principled deﬁnition of a meme – or unit of cultural
transmission – that goes beyond the single “word” and captures highly linked sets of words expressing
a functional, legal category – much the way a gene, composed of linked sets of nucleotides – contributes
to a function. Nations diﬀer in their debt to the past and their original contributions to the future.
This allows us to speak in a rigorous fashion about phylogenetic concepts like analogy and homology
when it comes to a cultural artifact. This has been an area of active research which includes the formal
analysis of cultural and symbolic systems (Sforza & Feldman, 1981; Nowak & Krakauer, 1999; Nowak,
Plotkin, & Krakauer, 1999), experimental approaches to cultural transmission (Henrich & McEalreath,
2003; Mesoudi & Whiten, 2008), and qualitative frameworks of integration (Mesoudi et al., 2006). At
this point in time the status of key phylogenetic concepts applied to culture is in ﬂux (Mace & Holden,
2004), we favor an instrumental approach deﬁning cultural analogy and homology strictly in phylogenetic
terms.
We suggest that the “semantic” interpretation of a given constitution and its practical legal impact is
what we mean by the phenotype. We might expect many diﬀerent genotypes to be neutral in that their
interpretations are equivalent, and that constitutions vary in their “penetrance”, that is their inﬂuence
on cultural practices.
This approach builds on prior research related to concepts such as “citation backbones” (Gualdi,
12

Yeung, & Zhang, 2011) in which citations to prior publications form a tree-like structure from which
novel papers descend, patent backbones in the automobile industry (Lin, chen, & Chen, 2011), skewed
patterns of borrowing in human designed artifacts (Eldredge, 2011), patterns of word borrowing (Nelson-
Sathi et al., 2011) and the evolution of programming languages (Valverde & Sol´ e, 2015).
Reconciling statistical patterns of inﬂuence with potential biases and patterns in thinking and writing
will bring us closer to frameworks that connect methods of mathematical science with objects of psycho-
logical and humanistic interest in the service of new models and theories of cultural transmission and
inﬂuence. The evolution of the law with its rich textual and interpretive traditions provides a nearly ideal
model system.
13

Figure 1: The “family tree” of constitutions. The United States constitution of 1789 is the root and thus
the “Last Universal Common Ancestor Constitution”. Any other constitutions is deemed as having as
its most recent ancestor the closest earlier constitutions where distance is measured as the KL-divergence
of the former to the latter. The size of this tree makes it diﬃcult to render so that the constitution
country and date are legible. A detail of the tree around the Egyptian constitution of 1923 is provided
in the upper inset. Note the fertility of that constitution, as well as the sterility of the constitutions of
Burundi (1962), Morocco (1970), and Albania (1939). The last of these is particularly interesting as we
see a line of descendants issuing forth from the Albania constitution of 1925. The Albanian Constitution
of 1939 was an imposed, fascist document that drew on earlier models, but had little purchase after
World War II. The most frequent topic, “subnational government” is found in such proportions in only
one other, earlier text. So, earlier versions of constitutions can have patterns of transmission that do
not include all of their descendants.A pdf document of this tree, easily magniﬁable, can be found at
https://www.math.dartmouth.edu/∼rockmore/kl-tree.pdf.
14

Figure 2: (A) Spring embedded reconstruction of constitutional diﬀusion network. Nodes correspond to
constitutions and directed edges encode topic borrowing. The blue arrow traces time forward through
the network starting in 1789 and ending in 2014. Time is the dominant factor in explaining the geometric
form of the network. (B) Application of a community detection algorithm to the thresholded diﬀusion tree
reveals three clear epochs of constitutional inheritance. The oldest epoch spans 147 years and contains 175
constitutions generating an average of 1 .2 constitutions per year. The second epoch spans 30 years and
contains 148 constitutions and an average of 4.9 constitutions per year. The third epoch spans 46 years and
contains 267 constitutions and an average of 5.8 constitutions per year. The rate at which constitutions are
being written has increased through time whereas the temporal inﬂuence of constitutions into the future
has contracted. (C) Use of more sensitive optimal modularity methods provides a decomposition of each of
these epochs into a further three epochs. Each induced cluster preserves the largely temporally contiguous
ordering demonstrating that time remains a dominant dimension of variation at the microscopic level.
15

Figure 3: Each constitution in the diﬀusion tree can be described in terms of a transmission motif, which
visualizes the indegree and outdegree for each target constitution. The motifs demonstrate the balance
between in-bound and out-bound inﬂuence for each constitution in terms of a threshold number of topics
that are borrowed. (1) Early constitutions tends to have few parents, e.g., Canada (1791) only has one
(the U.S.(1789) constitution, the leftmost node in Figure 1). Subsequent constitutions vary signiﬁcantly
in their ancestry: (2) Iceland (1874)’s constitution has many parents and many oﬀspring; (3) Bolivia
(1826) constitution has fewer parents and few oﬀspring (4) Venezuela (1830) exhibits many parents and
few oﬀspring; (5) South Korea (1948) has few parents and many oﬀspring; (6) Albania (1976) has several
parents and only one oﬀspring; (7) Montenegro (1992) has no oﬀspring. This variation in parentage and
fertility can be explained thorough a combination of both the time at which they were written and the
tendency to preferentially attach to a small number of highly favored models for imitation.
16

Figure 4: Illustrated in blue are the inferred connectivity data and in orange the maximum likelihood
parameter estimates for the best ﬁtting distributions for constitutional indegree (A,B) and outdegree
(C,D,E,F). The indegree is best approximated by a Gaussian distribution with a mean of 8.8 and a
standard deviation of 2.9. Figures 4C and 4D plot the outdegree distributions and the best ﬁtting
Poisson distribution. Whereas the mean is eﬀectively recovered, the tails of the distribution are poorly
ﬁtted. The Poisson underestimates the number of constitutions with few oﬀspring and overestimates the
number of constitutions with many oﬀspring. In Figure 4E and 4F we show the best ﬁtting negative
binomial distribution to the data. This very accurately recovers the entire oﬀspring distribution with
maximum likelihood parameter estimates for the two shape parameters of the distribution as r = 2.5 and
p =.22.
17

Figure 5: Growth and life span of constitutions. The inset ﬁgure superimposes the n best-ﬁtting piece-
wise linear regressions over the growth rate of constitutions (show in the larger image). We discover that
n = 3 and that these three growth rates correspond to the three epochs uncovered through the community
structure analysis. We also show the life span of constitutions (ﬁrst appearance to last recorded inﬂuence),
with the life-span plotted against the order of appearance of a constitution in the corpus. We clearly see
how the earliest constitutions exert the longest inﬂuence on descendant constitutions – a result strongly
in accord with the ﬁndings supporting a form of preferential attachment rule of inﬂuence.
18

Figure 6: Fecundity and inﬂuence of constitutions. On the x-axis are the number of descendant consti-
tutions arranged in chronological order and on the y-axis the date of their appearance. In Panel A we
plot the ﬁrst 20 constitutions. In Panel B the ﬁrst 100. Panel C the ﬁrst 200. Panel D all 591. Most
constitutions have few descendants and these appear over a relatively short span of time. Constitutions
with many descendants tend to span longer periods of time. Most of the longest-lived constitutions in
terms of inﬂuence/borrowing were written in the ﬁrst of the three epochs of constitutional history (as in
Figure 4A).
19

Supplementary Materials for The Cultural Evolution of National
Constitutions: Supporting Information
Materials and Methods
As explained, our results and methodology depend on the use of topic models (see e.g., (Blei, 2012)) and
diﬀusion networks. Topic models are statistical models to learn the underlying structure of a corpus of
documents. There are many ﬂavors of topic model. We use the Latent Dirichlet Allocation (LDA) (Blei
et al., 2003) probabilistic generative topic model. The underlying topics are represented as latent vari-
ables in a hierarchical Bayesian model. A generative model is assumed to be responsible for the observed
documents and the word distributions of each topic. The topic proportions of each document can be
learned via estimation of the posterior distribution of latent variables conditioned on the observed docu-
ments. The topic representations of the constitutions then form the underlying data for the inference of
the diﬀusion network a la (Gomez-Rodriguez et al., 2012). Some details of this now follow.
Materials
Our basic materials are 591 constitutions in English obtained from the publicly available and accessible
Comparative Constitutions Project website (http://comparativeconstitutionsproject.org/). A complete
list of the constitutions we use is in Table S1.
Methods
Topic modeling
The foundation of our text analysis is the use of a form oftopic modeling on the corpus of 591 constitutions
from which we derive a diﬀusion network for the inferred topics. A topic is a probability distribution over
a ﬁxed vocabulary derived from a text corpus. The corpus is composed of documents, where a document
consists of a set of (possibly non-unique) words from the vocabulary.
We obtained PDF versions of the constitutions from ( The Comparative Constitutions Project , n.d.)
and converted them to text ﬁles. Table S1 provides a list of the constitutions. The documents in the
corpus are contiguous blocks of text extracted from partitioning the constitutional texts. We set a
document length of 500 words and also require that documents respect the borders of constitutions (i.e.,
no document straddles multiple constitutions). If the length of a document is too long then the learned
topics will put similar probability on many words and thus will not capture our intuitive notion of a
topic. If the document length is too short the resulting topics are overﬁt to speciﬁc documents as there
is insuﬃcient data to learn general topics that can be used across the corpus. In addition, the choice of
20

document length depends on the type of structure we are interested in, short document lengths are good
for learning localized topics that are speciﬁc whereas longer document lengths learn smooth topics that
explain large portions of the corpus.
We use a standard methodology for further preprocessing the documents by stemming the documents
using the well known NLTK stemming package (http://www.nltk.org/api/nltk.stem.html), removing En-
glish stopwords as well as words that appear less than 20 times across the entire corpus. We also remove
words that appear in over 90% of the corpus. The resulting vocabulary consists of 3,546 unique terms.
We then computed the number of occurrences of each word in the vocabulary in each document so that
each document is represented by a 3,546 dimensional vector where the ith entry contains the number of
occurrences of token i in the document. This is a bag of words representation. (i.e., that the order of
words does not matter, also referred to as exchangeable) and additionally we assume that the order of
the documents, both within and between constitutions, does not matter.
We then topic model the document corpus using the Latent Dirichlet Allocation (LDA) (Blei et al.,
2003) probabilistic generative topic model. In the topic model a document is viewed as a mixture of
topics where the underlying topics are represented as latent variables in a hierarchical Bayesian model.
A generative model is assumed to be responsible for the observed documents and the word distributions
of each topic. The topic proportions of each document through the posterior distribution of the latent
variables conditioned on the observed documents.
To set notation let our corpus D be deﬁned as a set of N documents,D ={d1,d 2,...,d N}. Let l
denote the document length and break a constitution into multiple documents, respecting constitution
boundaries. A topic is a distribution over a ﬁxed vocabulary V and can thus be represented by a vector
β∈ Rm, βi≥ 0, ∑
iβi = 1, where m is the size of the vocabulary and the ith entry is the probability of
picking word i from this topic. We denote the proportion of document di that is made up of topic i by
θi∈ RK, where K is the number of topics, where θi≥ 0 and ∑
iθi = 1. Given the 𝓁th word in document
i, wi𝓁, let zi𝓁 indicate which topic the token wd𝓁 is drawn. Let Dir(η) denote the Dirichlet distribution
with parameter η and Mult(θi) denote the multinomial distribution over the distribution θi.
The speciﬁc generative process underlying LDA is as follows:
1. Fix K, the number of topics
2. For each topic k, draw βk∼Dir(η)
3. For each document di:
• Choose topic proportions θdi∼Dir(α)
• For each word position wdi𝓁:
21

– Choose a topic indicator zdi𝓁∼Mult(θdi)
– Choose a word wdi𝓁∼Mult(βzdi
)
Note that LDA depends on four parameters, the Dirichlet parameters α,η , the number of topics K
and the document length l = 500. In order to expedite the mixing of the Markov chain and reduce
experiment time, we ﬁx α, η and l, and vary the value of K. Choosing an appropriate number of topics
for a given corpus is a problem of model selection. We carried out 5-fold cross-validation to optimize K.
Speciﬁcally, we split the corpus evenly into 5 folds which are used to deﬁne training and testing sets to
evaluate parameter conﬁgurations. For each conﬁguration of K we hold out one of the folds as a test
set, W test, and use the other four as the training set, W train. We ran the Gibbs sampler for LDA on
the training set for 10, 000 iterations which produced samples from the posterior distribution which were
then used to evaluate the likelihood of the test set, p(W test|K) which measures the generalization ability
of the model. Unfortunately, the computation of the held-out likelihood, p(W test|K) is intractable so
we adopted the Chib-style estimation in (Wallach, Murray, Salakhutdinov, & Mimno, 2009) to eﬃciently
approximate it. The values of K and l that obtain the highest overall held-out likelihood over the ﬁve
folds are chosen for the rest of our analysis. Figure S3 shows the eﬀect of varying K from which we see
the optimal value is K = 100.
Inferring diﬀusion networks
The topics, β1:K, that are learned with LDA represent high level ideas and each constitution Ci can
be represented by the proportion of topics it exhibits, θi (which we described how to compute above).
As demonstrated in experiments, these discovered topics correspond to high level legal aspects, such
as human rights, international agreements, and economic systems. By treating a topic as the unit in
a diﬀusion and tracking the occurrence of each topic at each constitution over time, we can learn an
underlying diﬀusion network by which topics spread through constitutions over time, thus uncovering
the diﬀusion patterns of legal evolution over time.
We follow the method of Rodriguez et al. (Gomez-Rodriguez et al., 2012) for inferring diﬀusion
networks. We deﬁne a cascade c as a set of pairs ( i,ti), indicating that cascade c was observed at
node/constitution i at time t. Each topic, βk, will have an associated cascade, ck, so that ( i,ti)∈ ck
means that topic k has spread to constitution i at time t. To determine if a topic has spread to a
constitution, we set a threshold τ and we say the topic is observed at the nodes/constitutions whose
proportion of this topic are among the top τ percent When a topic does not spread to a constitution,
Cj, we set tj =∞. Note that we do not observe the path by which topics are spreading but only where
topics have spread to at a given time.
22

Having deﬁned cascades, we describe a probabilistic model of how they diﬀuse through constitutions.
Speciﬁcally, we denote the probability that a cascade c is transmitted from node i to node j as Pc(i,j ),
wheretj≥ti, indicating that a constitution can only be inﬂuenced by its predecessors. In our experiment,
we take Pc(i,j ) = e
−(tj −ti )
ˆα , where ˆα is the diﬀusion parameter and ti and tj are the timestamps of
constitutions i and j.
A diﬀusion network G is a directed graph (Cormen, Leiserson, Rivest, & Stein, 2001) where an edge
from nodei to nodej indicates that topics can diﬀuse from constitution i to constitutionj. We note that
any directed graph can be represented as the union of the set of spanning trees (Cormen et al., 2001),
i.e. sub-graphs that connect all of the nodes and that have no cycles. The inference process produces
an optimal network able to accommodate the observed cascades. To get a sense of what the process
produces, see Figure S1 for an inferred diﬀusion network derived from the methodology discussed here
on a subset of 99 constitutions.
First, we deﬁne the probability that a cascade c is consistent with a given tree structure T (where the
edges in T obey the ordering of time stamps) to be the following:
P (c|T )∝
∏
(i,j)∈T
Pc(i,j ) (1)
Notice that Eq.1 assumes that all edges inT are independent but thatPc(i,j ) are conditional probabilities
so that Eq. 1 deﬁnes a Markov process. Notice that Eq. (1) only depends on the edges in the tree as
nodes not observed in a cascade have and inﬁnite time of observation 4.
Using Eq.1 we deﬁne the probability of observing a cascade given an arbitrary diﬀusion network G
as:
P (c|G) =
∑
T∈T (G)
P (c|T )p(T|G) (2)
whereT (G) is the set of all spanning trees of G and we assume p(T|G) = 1/|T (G)| is uniform over all
spanning trees T∈T (G). Lastly, we deﬁne the probability of observing all cascades, C ={ck}K
k=1, one
for each topic, for a given diﬀusion network G as:
P (C|G) =
∏
c∈C
P (c|G). (3)
The goal is then to ﬁnd the maximum likelihood diﬀusion network by maximizing Eq.3 with respect to G
over all possible directed graphs with consistent time stamps (directed edges only emanate from earlier
4In (Gomez-Rodriguez et al., 2012) the probability of a cascade spreading from a given node or dying oﬀ at the node
is modeled with a Bernoulli random variable in order to account for the fact that cascades usually do not reach all nodes
and thus controlling the size of the cascades. However, the probability of spreading and not spreading turns out to be a
constant in the optimization used to infer a diﬀusion network so we ignore it here and it turns out to be computationally
advantageous to control the complexity of the inferred diﬀusion network using a constraint on the number of edges in the
inferred diﬀusion network.
23

constitutions and terminate in later constitutions). Formally, we need to solve the following optimization
problem:
ˆG = argmax|G|≤kP (C|G) (4)
where the constraint, |G|≤ k, indicates that the number of edges in ˆG be less than k. This constraint
provides complexity control since the graph consisting of all edges from a constitution to later constitu-
tions is a trivial solution and because as mentioned above cascades usually only consist of a subset of
constitutions. Optimizing Eq. 4 is NP-hard, however, an eﬃcient greedy algorithm that obtains a near-
optimal solution due to the submodularity of the problem (Gomez-Rodriguez et al., 2012). In addition,
we use a heuristic that stops the algorithm from adding new edges (and thus terminating) when the
objective function in Eq. 4 reaches 80 − 90% of an upper bound derived in (Gomez-Rodriguez et al.,
2012). This allows us to avoid using expensive cross-validation when setting the complexity, k, of the
model.
A key parameter is the threshold τ, which sets the fraction of topics viewed as important at a given
constitution. In order to set τ, we varied τ between 0 to 0.8, and inferred the diﬀusion network for each
of the values. We optimize τ relative to the parameters of the mean in- and out-degrees of all inferred
diﬀusion networks sat each parameter. This can be found in Figure S4. Note the hump shape of the
means in increasing τ, reﬂecting the gradual accumulation of possible paths in increasing τ and then a
tailing oﬀ as the optimization aspect of the diﬀusion network construction begins to winnow edges. After
observing both in- and out-degrees reach peaks at 0 .3, we investigate the robustness around 0 .3. For a
set of thresholds, most densely sampled around 0 .3 we create a vector of in-degrees ordered according
to the year of the constitution and a vector of out-degrees similarly ordered. Then for the in-degrees a
(symmetric) matrix is constructed computing the Pearson correlation of the i,j entry, and similarly for
the out-degrees. Figures S4 and S5 show the heat map of values. The farther away you are from the
diagonal, the farther you are in threshold diﬀerence (most densely sampled near 0.3). The slow roll-oﬀ in
color reﬂects the robustness of the calculation in that region – i.e., the in-degree and out-degree orderings
are not changing much as threshold varies between 0.2 and 0.4. All of this motivates a choice of τ = 0.3.
The ﬁnal diﬀusion tree produces for each constitutions a set of direct descendants and ancestors,
thereby giving rise to the indegree/outdegree “motifs”. A full list of motifs is presented in Figure S2.
The full tree can be found at www.math.dartmouth.edu/ ∼rockmore/FullConstDiﬀNet.pdf. A detail of
the full tree is given in Figure S5.
24

Table S1(a). List of constitutions in our corpus in alphabetical order – Table 1 of 5.
25

Table S1(b). List of constitutions in our corpus in alphabetical order – Table 2 of 5.
26

Table S1(c). List of constitutions in our corpus in alphabetical order – Table 3 of 5.
27

Table S1(d). List of constitutions in our corpus in alphabetical order – Table 4 of 5.
28

Table S1(e). List of constitutions in our corpus in alphabetical order – Table 5 of 5.
29

Figure S1. Learned diﬀusion network on a subset of ninety-nine constitutions.
30

Figure S2. Full set of motifs.
31

Figure S3. Results of 5-fold cross-validation for model selection. The log-likelihood of held-out data is
showed.
SI Figure S4. The mean and standard deviation of the in and out degree of the inferred diﬀusion
networks for the threshold parameter sampled between the values of 0 and 0 .8. The density is non-
monotonic and exhibits a maximum value at around 0.3. Threshold values toward zero yield disconnected
networks and values toward 1 also generate sparse networks. For our analysis we select the threshold (0.3)
that maximizes the density of connections. This is equivalent to maximizing variation through descent.
32

Figure S5. Detail from the full diﬀusion network learned on the topic modeling of 591 constitutions.
The arrows pointing in to a node indicate a topic expressed above some threshold earlier in the space of
constitutions (a source) also being expressed above some threshold at this new point (the target).
33

Figure S6. Indegree heatmap robustness. This illustrates how changes in the diﬀusion threshold have a
negligible impact on the temporal ordering of the indegree. In other words the number of constitutional
parents of any given constitution is very stable with respect to our choice of threshold parameter.
34

Figure S7. Outdegree heatmap robustness. This illustrates how changes in the diﬀusion threshold have a
negligible impact on the temporal ordering of the outdegree. In other words the number of constitutional
parents of any given constitution is very stable with respect to our choice of threshold parameter.
35

References
ARTstor. (n.d.). Retrieved from http://www.artstor.org (Accessed April, 2013)
Blei, D. M. (2012). Probabilistic topic models. Communications of the ACM , 55(4), 77-84.
Blei, D. M., & Laﬀerty, J. D. (2006). Dynamic topic models. In Proceedings of the 23rd interna-
tional conference on machine learning (pp. 113–120). New York, NY, USA: ACM. Retrieved from
http://doi.acm.org/10.1145/1143844.1143859 doi: 10.1145/1143844.1143859
Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning
Research, 3, 993-1022.
Boli-Bennett, J. (1987). Human rights or state expansion? Cross-national deﬁnitions of constitutional
rights, 1870-1970. In G. Thomas, J. Meyer, F. Ramirez, & J. Boli (Eds.), Institutional structure
(pp. 71–91). Sage.
Boyd, R., & Richerson, P. J. (1996). Why culture is common but cultural evolution is rare. Proceedings
of the British Academy , 88, 73-930.
Chang, J., Boyd-Graber, J. L., Gerrish, S., Wang, C., & Blei, D. M. (2009). Reading tea leaves: How
humans interpret topic models. In Nips (Vol. 31, pp. 1–9).
Christiansen, F. B. (2008). Theories of population variation in genes and genomes . Princeton University
Press, Princeton, NJ.
The Comparative Constitutions Project. (n.d.). Retrieved from
http://www.comparativeconstitutionsproject.org (Accessed April, 2013)
Cormen, T., Leiserson, C., Rivest, R., & Stein, C. (2001). Introduction to algorithms . MIT Press,
Cambridge MA.
Eldredge, N. (2011). Paleontology and cornets: Thoughts on material cultural evo-
lution. Evolution: Education and Outreach , 4(3), 364–373. Retrieved from
http://dx.doi.org/10.1007/s12052-011-0356-z doi: 10.1007/s12052-011-0356-z
Elkins, Z., Ginsburg, T., & Melton, J. (2009). The endurance of national constitutions . Cambridge
University Press.
Elkins, Z., Ginsburg, T., & Simmons, B. (2013). Getting to rights: Constitutions and international law.
Harvard International Law Journal , 51, 201–34.
Foti, N., Ginsburg, T., & Rockmore, D. (2014). ‘We the Peoples’: The global origins of constitutional
preambles. George Washington International Law Review, , 46, 101–134.
Girvan, M., & Newman, M. E. (2002, June). Community structure in social and biological net-
works. Proceedings of the National Academy of Sciences , 99(12), 7821–7826. Retrieved from
http://dx.doi.org/10.1073/pnas.122653799
Go, J. (2003, March). A globalizing constitutionalism? Views from the postcolony 1945-2000. Interna-
tional Sociology, 18, 71-95.
Gomez-Rodriguez, M., Leskovec, J., & Krause, A. (2012). Inferring networks of diﬀusion and inﬂuence.
TKDD, 5(4), 21.
The Google books N-Gram Viewer. (n.d.). Retrieved from http://books.google.com/ngrams (Accessed
April, 2013)
The Google books website. (n.d.). Retrieved from http://books.google.com/ (Accessed April, 2013)
Gualdi, S., Yeung, C. H., & Zhang, Y.-C. (2011). Tracing the evolution of physics on the backbone of
citation networks. CoRR, abs/1108.1325.
Hart, D. L., & Clark, A. G. (1997). Principles of population genetics . Sinauer Associates, Inc Publishers,
Mass.
Henrich, J., & McEalreath, R. (2003). The evolution of cultural evolution. Evolutionary Anthropology,
12, 132-135.
Hughes, J. . M., Foti, N. J., Krakauer, D. C., & Rockmore, D. N. (2012). Quantitative patterns of
stylistic inﬂuence in the evolution of literature. Proceedings of the National Academy of Sciences ,
109(20), 7682–7686.
36

International Music Score Library Project. (n.d.). Retrieved from http://imslp.org/ (Accessed July,
2013)
Jockers, M. (2013). Macroanalysis: Digital methods and literary history . University of Illinois Press.
Kaiser, D. I. (2009). Drawing theories apart: The dispersion of feynman diagrams in postwar physics .
University of Chicago Press.
Karlin, S., & Taylor, H. M. (1975). A ﬁrst course in stochastic processes . Academic Press.
Law, D. (2005, Feb.). Generic constitutional law. Minn. L. Rev. , 89, 652.
Law, D., & Versteeg, M. (2011). The evolution and ideology of global constitutionalism. Cal. Law
Review, 99, 1163.
Leskovec, J., McGlohon, M., Faloutsos, C., Glance, N. S., & Hurst, M. (2007). Patterns of cascading
behavior in large blog graphs. In Sdm (p. 551-556).
Lin, Y., chen, J., & Chen, Y. (2011). Backbone of technology evolution in the modern era automobile
industry: an analysis by the patents citation. J Syst Sci Syst Eng , 20, 416-442.
Mace, R., & Holden, C. J. (2004). A phylogenetic approach to cultural evolution. Trends in Ecology and
Evolution, 20, 116-121.
Mesoudi, A., & Whiten, A. (2008). The multiple roles of cultural transmission ex-
periments in understanding human cultural evolution. Philosophical Transactions
of the Royal Society B: Biological Sciences , 363(1509), 3489–3501. Retrieved
from http://rstb.royalsocietypublishing.org/content/363/1509/3489 doi:
10.1098/rstb.2008.0129
Mesoudi, A., Whiten, A., & Laland, K. N. (2006). Towards a uniﬁed science of cultural evolution.
BEHAVIORAL AND BRAIN SCIENCES , 29, 329-383.
Michel, J.-B., Shen, Y. K., Aiden, A. P., Veres, A., Gray, M. K., Team, T. G. B., . . . Aiden, E. L. (2010).
Quantitative analysis of culture using millions of digitized books. Science, 331, 176-182.
Moretti, F. (2005). Graphs, Maps, Trees. Verso Books.
Nelson-Sathi, S., List, J.-M., Geisler, H., Fangerau, H., Gray, R. D., Martin, W., & Dagan,
T. (2011). Networks uncover hidden lexical borrowing in indo-european language evolu-
tion. Proceedings of the Royal Society of London B: Biological Sciences , 278(1713), 1794–
1803. Retrieved from http://rspb.royalsocietypublishing.org/content/278/1713/1794 doi:
10.1098/rspb.2010.1917
Newman, M. (2006). Modularity and community structure in networks. Proceedings of National Academy
of Sciences, USA , 103, 8577-8582.
Nowak, M., & Krakauer, D. (1999). The evolution of language. Proc Natl Acad Sci USA, 96, 8028-8033.
Nowak, M., Plotkin, J., & Krakauer, D. (1999). The evolutionary language game. J. theor . Biol , 200,
147-162.
Pagel, M. D. (2013). Wired for culture. W.W. Norton & Company.
Richerson, P. J., & Boyd, R. (2006). Not by genes alone: How culture transformed human evolution .
University Of Chicago Press.
Riddell, A. (2014). How to Read 22,198 Journal Articles: Studying the History of German Studies with
Topic Models. In M. Erlin & L. Tatlock (Eds.), Distant readings: Topologies of german culture in
the long nineteenth century (pp. 91–114). Rochester, NY, USA: Camden House.
Rogers, D. S., & Ehrlich, P. R. (2007). Natural selection and cultural rates of change. Proceedings of the
National Academy of Sciences , 105, 3416–3420.
Rogers, E. M. (1995). Diﬀusion of innovations . The Free Press, NYC.
Ross, N. (2013). Power laws in preferential attachment graphs and stein’s method for the negative
binomial distribution. Advances in Applied Probability , 45, 876-893.
Sforza, L. L. C., & Feldman, M. W. (1981). Cultural transmission and evolution: A quantitative approach.
Princeton University Press, Princeton, NJ.
Skach, C. (2006). Borrowing constitutional designs. Princeton: Princeton University Press.
37

Stanford Topic Modeling Toolbox.(n.d.). Retrieved from http://nlp.stanford.edu/software/tmt/tmt-0.4/
(Accessed July, 2013)
Valverde, S., & Sol´ e, R. V. (2015). Correction to ’punctuated equilibrium in the large-scale evolution of
programming languages’. Journal of the Royal Society, Interface , 13 117 .
van der Hofstad, R. (2017). Random graphs and complex networks . Cambridge Universty Press, Cam-
bridge, UK.
Venter, F. (2013). Constitutional comparison. Cambridge, MA: Kluwer.
Wallach, H. M., Murray, I., Salakhutdinov, R., & Mimno, D. M. (2009). Evaluation methods for topic
models. In Icml (p. 139).
Wang, X., & McCallum, A. (2006). Topics over time: A non-Markov continuous-time model
of topical trends. In Proceedings of the 12th acm sigkdd international conference on knowl-
edge discovery and data mining (pp. 424–433). New York, NY, USA: ACM. Retrieved from
http://doi.acm.org/10.1145/1150402.1150450 doi: 10.1145/1150402.1150450
Watson, A. (1974). Legal transplants. Cambridge University Press.
Wimsatt, W. C. (1999, April). Genes, memes, and cultural heredity. Biology and Philosophy , 14,
279–310.
Wood, J., Tan, P., Das, A., W. Wang, W., & Arnold, C. (2016). Source-lda: Enhancing probabilistic
topic models using prior knowledge source. Retrieved from https://arxiv.org/abs/1606.00577
Youn, H., Strumsky, D., Bettencourt, L., & Lobo, J. (2015). Invention as a combinatorial process:
evidence from us patents. J. R. Soc. Interface , 12, 106.
38
