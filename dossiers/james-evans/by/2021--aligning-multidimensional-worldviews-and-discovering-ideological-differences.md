---
title: "Aligning Multidimensional Worldviews and Discovering Ideological Differences"
person: james-evans
section: by
type: journal-article
year: 2021
date: 2021-01-01
venue: "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing"
authors: "Jeremiah Milbauer, Adarsh Mathew, James Evans"
source_url: https://doi.org/10.18653/v1/2021.emnlp-main.396
openalex_id: https://openalex.org/W3214697366
retrieved: 2026-08-13
content: full-text
notes: "full text via the OpenAlex Content API (content.openalex.org)"
---

# Aligning Multidimensional Worldviews and Discovering Ideological Differences

## Full text

## Abstract

The Internet is home to thousands of communities, each with their own unique worldview and associated ideological differences.With new communities constantly emerging and serving as ideological birthplaces, battlegrounds, and bunkers, it is critical to develop a framework for understanding worldviews and ideological distinction.Most existing work, however, takes a predetermined view based on political polarization: the "right vs. left" dichotomy of U.S. politics.In reality, both political polarization -and worldviews more broadly -transcend one-dimensional difference, and deserve a more complete analysis.Extending the ability of word embedding models to capture the semantic and cultural characteristics of their training corpora, we propose a novel method for discovering the multifaceted ideological and worldview characteristics of communities.Using over 1B comments collected from the largest communities on Reddit.comrepresenting 40% of Reddit activity, we demonstrate the efficacy of this approach to uncover complex ideological differences across multiple axes of polarization.

"The limits of my language mean the limits of my world"

Tractatus Logico-Philosophicus, 1921, Ludwig Wittgenstein Media choice, social networking platforms, and collaborative filtering on the internet have enabled individuals to enter "echo chambers" that reflect shared worldviews (Sunstein, 2018;Mutz, 2006;Bishop, 2009).The internet also publicly reveals these communities and their communication for analysts of language, culture and interaction at unprecedented scale.Despite the abundance of such data, however, analysis of worldviews and ideological difference has been dominated by considerations of "polarization" (Boxell et al., 2017;Bail Figure 1: By training the model to align "candidate", "politics", and "corrupt," a hypothesis alignment f ("trump"|C 1 ) ≈ f ("clinton"|C 2 ) emerges.et al., 2018), which impoverishes the comparison of ideologies by reducing them to pairs separated along a singular dimension.

Here, we draw inspiration from the approach of interpretive anthropology and the focus of cognitive anthropology to represent, investigate and compare worldviews from community discourse.In the Interpretation of Cultures, Geertz rendered culture as "a system of inherited conceptions expressed in symbolic forms by means of which men communicate, perpetuate, and develop their knowledge about and attitudes toward life" (Geertz et al., 1973).Combined with cognitive anthropology's concern with how implicit knowledge changes the way people perceive and relate to the world (d'Andrade, 1995), this motivates assessment of worldviews through modern pre-trained natural language models that render words (Mikolov et al., 2013b;Pennington et al., 2014) and phrases (Devlin et al., 2019;Radford et al., 2019) in relation to one another as a function of their proximity in discourse.When pre-trained on the discourse of distinctive communities, these models have begun to enable a highly resolved evaluation of expressed worldviews -symbol systems that reveal shared patterns of attention and association (Kang and Evans, 2020).

Based in the premise that the language a community uses carries markers of the culture of that community (Webson et al., 2020), recent work has demonstrated the ability of trained embedding models to uncover cultural values (Garg et al., 2018;Xie et al., 2019;Kozlowski et al., 2019).However, these models are limited by requiring significant researcher input to query the model for insights.Recent work has also demonstrated the potential to embed communities themselves Waller and Anderson (2021), but has not extended to the level of a word-level understanding of community worldview.

We instead model community language as a specific instance of an ideological dialect (or, an "ideolect") 1 .Using a similar approach to Khud-aBukhsh et al. ( 2021), which identified single-axis polarized political "languages" on YouTube, we introduce a new method for unsupervised cultural analysis based on multilingual embedding alignment.Our method provides high-accuracy alignment, is the first to analyze multiple facets of ideological polarization, and readily enables analysis in a large multi-community setting -which we demonstrate by identifying multiple axes of ideological differences on Reddit.

As an additional contribution, we publish a Github repository with all the code necessary to replicate this work and apply our methods in new settings. 2This repository also includes tables of results that were too long to reasonably include in this paper.

In this section, we summarize previous approaches to the analysis of cultural values through word embedding models.

1 This is not to be confused with the linguist's notion of an "idiolect", language quirks unique to a person but understood by others, or Wittgenstein's notion of a language uniquely understandable by a single person.Our notion of "ideolect" draws on both: a language shared by an ideological group, which necessarily contains the private worldview of that group and may not be naively decipherable to those outside.

2 https://github.com/jmilbauer/worldview-ideology

Early work on cultural analysis through word embeddings observed that the cultural values of a community or society are embedded within the text produced by that community or society, and are discoverable by word embedding (Garg et al., 2018).These values can then be queried by measuring the distance between wordpairs.

Measuring stereotypes By pre-selecting a set of "entity" words, and "value" words, researchers can measure how attitudes towards the selected entities differ over time, or across communities.This approach works by training an embedding model on a text corpus, and then computing the similarity between each query word and each value word.Garg et al. (2018) use this approach, with occupations comprising the entities and gender or ethnic categories as the values.Each pair thus represents the strength of a particular cultural value or stereotype.However, this approach is limited in that it is only able to discover the specific stereotypes queried by the researchers; it is unable to discover cultural values on its own.Axes of polarization Another approach to unsupervised cultural analysis is introduced by Kozlowski et al. (2019).In this method, two words representing the opposite poles of a particular cultural value (such as "rich" and "poor") are selected.Entity words, such as the names of different sports, are then projected to an axis drawn between the polar words.

Although such models have the capacity to render worldviews as high dimensional spaces, research typically compares representations only selectively in terms of a modest set of keywords queried and compared between models.In these cases, the keywords are typically manually selected according to a predetermined notion of which words may exhibit polarization, and compared with words that are pre-selected to encode cultural values, essentially producing a cultural relatedness score for a given (Entity,Value) pair in some corpus:

This method can then be used to identify differences between corpora:

Xie et al. ( 2019) make progress on this issue by introducing the use of the Moral Foundations Dictionary (Graham et al., 2009) to approximate moral categories.Using a trained embedding model, they assign each word to its nearest cluster of Moral Foundations Words, and measure differences in terms of a word's movement between clusters across distinct corpora.This approach has two key advantages: it does not presuppose the relevant cultural values (the Moral Foundations Dictionary is designed to be comprehensive), and it allows the moral categories to be specific to each corpus's embedding.

With this approach, we are now able to evaluate the relevance of each word to the moral differences between communities C 1 , C 2 , as:

This set of scored words thus represents the cultural differences between two communities.However, it too is limited in expressivity by the reliance on the Moral Foundations Dictionary's list of moral categories.

Rather than rely on the previous query-value paradigm, we achieve fully unsupervised cultural analysis through the use of multilingual embedding alignment.We explicitly model corpus-specific ideological dialects using techniques designed for multilingual word embedding alignment, to learn a translation function F from each embedding to the joint space.Then, for any two corpora, each word has an alignment score:

This ultimately yields a similar set of scores to the Moral-Foundations approach:

with two important benefits: our model requires no moral supervision, and can discover more than just moral differences.By contrasting semantic models per se, we automatically discover ideological differences in a multi-community corpus.

Additionally, for a given word w 1 in C 1 , we can compute a the nearest image w 2 in C 2 , such that

This represents the hypothesis of a conceptual substitution between communities, yielding a highresolution comparison of the worldviews, ideologies, and cultural differences between two communities, without any supervision.Figure 1 illustrates this idea in the context of a conservative political community (bottom panel, in red) and a liberal one (top panel, in blue).Worldviews are seen anchored by the words "corrupt", "politics", and "candidate", and an alignment between the semantics of "clinton" and "trump" emerges.

Reddit serves as the primary source of data for this project.The platform is structured as a collection of peer-driven communities called "subreddits," ostensibly self-regulated by norms decided upon by members of the subreddit and enforced by moderators.All users are anonymous, can be a part of multiple subreddits, and are free to create their own.As such, user comments serve as a rich source of conversation and discourse across varied interests and topics, organized into communities of self-selected individuals.

The structure of Reddit lends itself to a community-focused analysis of language, with the site's use of self-enforced boundaries allowing us to observe discourse across groups without having to define the notion of a group ourselves.Instead, we rely on every user's own choice about where they wish to engage, and where to post their comments.This multi-community setting has been exploited in the past by researchers, with Tan and Lee (2015) exploring the contours of multi-community engagement and the widening of interests via a user's exploration of different subreddits over time.Rajadesingan et al. (2020) explore the norms of interaction dictated and enforced by multiple "toxic" subreddits, showcasing how self-selection and preentry learning play a key role in sustaining these norms.Kumar et al. (2018) explicitly study negative mobilizations between different subreddits as conflict, finding that they tend to occur between communities that are highly similar in content.

We use data from Reddit for the period 2016-2019, and select 32 subreddits from the largest communities to study, representing between 30 and 40% of the site's monthly activity.We rely on the Reddit dumps ingested by Pushshift as described in Baumgartner et al. (2020) activity across all of Reddit for each month.Given the delay in ingesting activity across all subreddits, some comments and users can be deleted before ingestion occurs.Additionally, users are given the opportunity to have their data not ingested by submitting an opt-out request.Although the Pushshift dataset includes the users' usernames, we scrub all information aside from the actual text of the post before even any pre-processing occurs.When discussing a specific community, we refer to it as "r/[community name]," as is customary on Reddit.Table 1 contains information about the size of our dataset after preprocessing.

We conceive of the alignment procedure as a matching of "conceptual anchors," designed to align the worldview of two communities.If two communities, C a and C b , have identical worldviews, we expect that structural relations between words will be preserved across the community boundary.However, if they have different worldviews, we would expect that the words central to that conflict would not align well, even when anchoring words are well-aligned.

On notation For a community called a, we typically use C a to indicate the "language" of the community, V a for its vocabulary, A to represent an embedding matrix trained on C a , and A i to represent the word embedding of a word w i in C a .

In order to align and compare community-specific models, we turn to the literature on multilingual word embeddings.Broadly speaking, these works aim to learn a single embedding space in which synonymous words in different languages have the same embedding.Approaches to this problem vary, but typically either rely on training with parallel corpora in multiple languages, or aligning embeddings with the help of a multilingual lexicon.In our case, all data collected from different Reddit communities is in English -so we automatically have a complete parallel lexicon.As such, we choose to use the lexicon approach to align our different "ideolects."Furthermore, this approach allows our work to be immediately useful to computational social scientists currently using out-of-the-box word embedding algorithms for cultural analysis.

Most common is the bilingual case; given two languages, L a and L b , we use a bilingual lexicon to learn two transformation functions: f a→c and f b→c , such that for every word i ∈ L a and every word j ∈ L b , f a→c (Emb(i)) = f b→c (Emb(j)).In this bilingual case, it is possible to set c to b, and essentially learn a single transformation from one space to the other.In the multilingual case, one can learn a latent space into which all languages are projected, chose one language as the target for all the other languages' transformations, or learn direct pairwise bilingual transformations.

In this work, we adapt approaches (Ammar et al., 2016;Mikolov et al., 2013a) developed for multilingual alignment to the cultural analysis use-case.

After aligning worldviews with this approach, we then evaluate multiple dimensions of ideological difference by computing misalignment scores across different topics.

We treat the posted comments of each community, in each year, as its own corpus.For each community-corpus in the dataset, we tokenize each of the comments posted in the community (without stemming or lemmatization), remove formatting tokens, reduce hyperlinks to just their surface forms, and make all characters lower case.We then run a basic phrase detection algorithm (Mikolov et al., 2013b), implemented in Gensim (Rehurek and Sojka, 2011), to detect common bigrams in each community.

We begin by training a word embedding model for each independent community.Here, we use Gensim's implementation of the Skip-gram model (Mikolov et al., 2013b).We train embeddings in both 100 and 300 dimensions; the following experiments were conducted with 100-dimensional embeddings.Given that the data is from a longtailed forum community on the Internet, we use a maximum vocabulary of 30,000 words.In order to promote the stability of the embedding for each community-corpus, we over-sample sentences from smaller communities.

In order to train an alignment between two embedding spaces, we must first construct a "bilingual" lexicon to anchor the alignment.All text in our corpora a in English, so we can easily construct an lexicon of size N = |V |, using the entire shared vocabulary of two trained embeddings as the anchoring words.However, it should be noted that the goal of our embedding alignment should not be maximum accuracy.We intend to use the trained alignment as a tool for cultural analysis by exploring the misaligned words; so we should not attempt to achieve a perfect map.

We experiment with three distinct approaches to construct the bilingual lexicon.The first approach uses the entire shared vocabulary to anchor the alignment.The second approach uses a large set of stopwords -the most frequent 5000 words across the combined corpora.The third approach uses a smaller set of stopwords -1000.

In order to identify topic areas within which to measure misalignment, we implement a topic assignment procedure, inspired by the success of a simple embedding-based approach for Twitter data in Demszky et al. (2019).We learn word clusters using an embedding model trained on the union of the communities, with the scikit-learn (Pedregosa et al., 2011) implementation of KMeans++ (Arthur and Vassilvitskii, 2006).We then treat each word cluster as a topic.

To validate these topics, we compute the core topics for each community by assigning each comment a topic label, and calculating the association of each topic with each community.For each topic t and community C:

Using these scores, we rank the topics of each community.Table 2 includes examples of some top topics for r/gaming, r/politics, and r/askmenpopular groups that discuss gaming, politics, and mens' issues respectively.

Figure 4 in the Appendix includes a full comparison of topics similarities across communities.An interesting observation from this validation is that communities for which we hypothesize a strong ideological disagreement (such as r/politics and r/the_donald), there is a strong similarity in topic distribution.

Once anchoring words have been selected (either by using all words, stop words, or non-salient topic words), we can train an alignment between embedding spaces.We choose to treat alignment as a linear transformation, T a→b ∈ R d×d from one d-dimensional vector space A to another, B, so A • T a→b = B.This allows the learned transformation to be both compositional and invertible:

A These properties are important when creating multilingual embeddings, especially for lowresource languages.When there is no bilingual lexicon for a pair {L a , → L b }, we can still learn transformations between them by passing through a high-resource {L c like English:

In our case, because the linear transformation is an isomorphism, we also think of our work as an extension of the idea of analogies in Mikolov et al. (2013b), but at the community level.

This compositionality also allows us to reduce the number of alignments to train, which is useful when performing experiments at scale.For a set of N communities, describing the entire set requires N 2 alignments.By relying on compositionality, we need only train N transformations: one for each community and the high-resource community.In our dataset, r/AskReddit is the highest resource community, and thus the most appropriate analog to English in the multilingual setting.

We consider three techniques for alignment: MultiCCA, developed by Ammar et al. (2016), a linear equation solver, and an SVD-based approach described in Smith et al. (2017).We experiment using each of these approaches to select linear projections, different anchoring set size.In each case, we begin with two word embedding models trained on different community corpora, C a and C b , each with their own vocabulary V a and V b .We then construct the set of potential anchoring words, D a,b ⊂ V a,b , where

Our first anchoring strategy uses all words in D a,b , our second strategy uses only the 1000 most frequent words (D a,b 1000 ), and our third strategy uses the 5000 most frequent words (D a,b 5000 ).We then construct two training matrices: A and B , where

We then train the alignment using A and B , then evaluate.

Acc@1 Acc@5 Acc@10 ALL ∼30k 0.6937 0.8335 0.8709 SW 1000 0.6583 0.8037 0.8450 5000 0.6934 0.8306 0.8679 Mode N Acc@1 Acc@5 Acc@10 ALL ∼30k 0.7284 0.8591 0.8924 SW 1000 0.6234 0.7735 0.8174 5000 0.6984 0.8352 0.8718 Mode N Acc@1 Acc@5 Acc@10 ALL ∼30k 0.4980 0.6462 0.7091 SW 1000 0.4798 0.6434 0.6991 5000 0.5203 0.6841 0.7374 MultiCCA For communities C a and C b , Multi-CCA seeks to learn two projections to latent space C: T a→c and T b→c , in order to maximize the correlation of A • T a→c and B • T b→c .From these projections, we then recover the projection of interest T a→b :

We implement this approach using scikit-learn's cross_decomposition.CCA module.(Pedregosa et al., 2011) Linear Equation Solver For A and B, the linear equation solver aims to learn T a→b by solving the equation: A • T a→b = B. We use NumPy's Leastsquares linear equation solver, linalg.lstsq.(Harris et al., 2020) Singular Value Decomposition This method is employed by KhudaBukhsh et al. ( 2021) (albeit with many fewer anchoring words), and is described in Smith et al. (2017).Alignment is trained directly between community pairs, rather than between each community and a shared space.For this method, the projection is learned by solving U ΣV T = A T B, setting T a→b = U V T .We use NumPy's linalg.svd.(Harris et al., 2020) Evaluation For each pair of communities C a and C b , and each word w i ∈ V a , V b , we translate w i from C a to C b .Each w i has an embedding A i learned from C a , an embedding B i learned from C b , and an image B i under alignment, where B i = A i T a→b .We then find the N nearest-neighbors of B i in V b , using cosine similarity.Acc@N is the proportion of N -nearest-neighbor sets that contain w i .Tables 3,4, and 5 contain the results of this evaluation for the year 2016, macro-averaged over each projection learned.Other years are included in the appendix.

As might have been anticipated, the anchoring method that uses all available words is the most accurate.We also notice a trend of decreasing accuracy from 2016 to 2019, despite the increase in dataset size and therefore embedding stability.This suggests growing semantic differences between Reddit communities over time.For future experiments and evaluation, we use the 5000anchor MultiCCA approach, which we found to empirically provide alignment accuracy without exposing the model to all of the data.

Unsupervised cultural analysis of this kind is an extremely recent development in the literature.However, previous methods can be adapted to provide a baseline for comparison.For the following comparisons, we select for analysis two communities with both a high degree of moral polarization, and a known axis of polarization: r/politics and r/the_donald.These communities are highly politically polarized.We perform the comparison with data from the year 2017.

We initially perform a comparison with an approach described by Xie et al. ( 2019), which identifies changes in moral semantics across corpora.We use the technique to generate a set of misaligned words by identifying words that move from a positive to a negative moral category (and vice versa) between communities.We then rank the words by degree of movement.This method retrieves political words (defined as words falling into political topic clusters) with a 0.2247 MAP.

For both our method and the method described by KhudaBukhsh et al. ( 2021), we follow the procedure for anchoring and training an alignment.For KhudaBukhsh et al. (2021), this means using SVD with NLTK stopwords (Bird et al., 2009).We then sort the misaligned wordpairs by degree of alignment, and classify a wordpair as political if either of the misaligned words is in one of the political clusters.KhudaBukhsh et al. ( 2021) achieves 0.3076 MAP; our method achieves 0.3318 MAP.

In this section, we use our method to perform a number of sociolinguistic explorations.

We begin by using the learned projection/alignment to identify "misaligned" words in a political context.

We say that a word is "aligned" when the nearest image of a word w i from C 1 is itself:

And "misaligned" when it is not:

We anticipate the words that will ultimately misalign are either words with low quality embeddings (owing to low frequency in the corpus) or words with very polarized meanings across communities.

Our first experiment, analyzing two politically misaligned corpora, is a typical area of inquiry.(KhudaBukhsh et al., 2021;Xie et al., 2019;Webson et al., 2020) We select r/politics (C a ), a generalpurpose political discussion board with a strong liberal tendency, and r/the_donald (C b ), a Trumpsupporting and aggressively conservative community well known as a breeding grounds for conspiracy theories, including PizzaGate (Kang, 2016).We begin by finding the vocabulary of shared words between r/politics and r/the_donald, and use our alignment algorithm to "translate" each word from r/politics to r/the_donald.Using MultiCCA, and r/askreddit (C c ) as the "high-resource" language, the translation is formulated as:

Using this matrix transformation, we project all shared words from C a to C b .We also repeat this process in reverse.

Querying this model for political words, we find a number of interesting misalignments, including the words which directly define the known axis of polarization: "democrat" and "republican."Table 6 contains a sample of misalignments from r/politics to r/the_donald.This demonstrates the ability of our method to identify the nature of polarization between two communities without any presuppositions about the communities.

While the approach described in section 5.1 is able to identify misaligned words and "translate" across the cultural boundary, we also consider another procedure: using the trained embedding alignments to identify the antonyms that describe an axis of semantic reflection between two communities.We use a predetermined set of antonym pairs from Miller (1995), and identify all instances where a word w in C a maps to its antonym in C b .

We apply this approach to the community pair of r/askwomen and r/askmen, forums that discuss womens' and mens' issues, respectively.Table 7 contains top identified antonyms pairs.Although the list is not exhaustive, we see that the antonym approach quickly identifies the gender axis between the two communities.A weakness of this approach is that many words, such as names and other proper nouns, may not be included in a predetermined set of antonyms.

There may exist two distinct communities of speakers that have similar worldviews and conceptual structures, but do not talk about the same things.A good example of this are the two communities 7: Words in r/askwomen that align to their antonym when projected to r/askmen.Degree of alignment measured in cosine similarity.

r/dota2 and r/leagueoflegends.Both of these communities are discussion boards centered around a "MOBA" (Multiplayer Online Battle Arena) video game, and both video games share a great deal of similarity.However, r/dota2 players and r/leagueoflegends players often see each other as rivals or enemies.By using our alignment technique, we demonstrate a use-case for bridging the conceptual gap between two similar communities and finding conceptual homomorphisms.By aligning the embeddings of two communities C a and C b , we can project words that are in V a , but not V b , from A to B, learning a semantic representation for an out-of-vocabulary word unknown to C b .This projection yields C b 's equivalent of C a 's unique word.This is similar to unsupervised translation.

We then use the projection learned between r/leagueoflegends and r/dota2 to estimate the nearest word within the r/dota2 space for a small set of query words unique to r/leagueoflegends.Table 8 contains some examples of the projections, and Figure 2 provides an additional illustration of the success of the technique in identifying crosscommunity semantic analogs.

Finally, we perform a large-scale analysis across all top Reddit communities.Using the topic clusters described in section 4.5, we compute the number of misalignments for each topic cluster.

We are then able to produce pairwise misalignment scores for each pair of communities with respect to each topic cluster, uncovering the multidimensional ideological misalignment across Reddit.These comparisons are numerous; we include two here.Figure 3 demonstrates the degree of misalignment with respect to two political subcategories, corresponding to "Economics" and "Authority".

ing to play League of Legends; "opgg" is a website used for tracking stats in League of Legends, and "dotabuff" is used by Dota2 players; "Riot Games" and "Valve" are the creators of League of Legends and Dota 2 respectively; "rito" and "volvo" are both joking nicknames for the respective game creators; "Aatrox" and "Bloodseeker" are both blood-themed fighters.

Despite low KL-divergence in topic distributions for political communities, as shown in Figure 4, they demonstrate strong misalignment on the "Economics" topic.The difference demonstrates our method's ability to resolve specific types of polarization across specific ideological categories, as opposed to previous work that treats political polarization as a single-dimensional problem.Additional topic misalignments are included in 5.While significant, an analysis of Reddit communities is only a fraction of what this approach is capable of.Unlike previous methods that rely on calculating all pairwise alignments, the compositional nature of the MutliCCA approach we propose only requires learning the alignment between each community's ideological dialect and a central high-resource community.As such, the training time scales linearly with the number of communities analyzed, which makes the study of the potentially large number of ideological communities much more tractable.

In this paper we have demonstrated a novel technique for unsupervised cultural analysis by building upon existing work treating word embeddings as tools to explore worldview, as well as work on multilingual embedding alignment.We have shown that our formulation is flexible, and able to operate effectively in a complex multi-community setting.

We have also demonstrated a number of useful applications of the worldview discovery procedure, from the automatic identification of axes of polarization, to the identification of out-of-vocabulary words with similar semantics, to the large-scale analysis of an online social community with multiple dimensions of ideological polarization.

A key application of this method is in unsupervised cultural analysis, which would allow researchers to explore culture at scale, without using a manual value-querying process that imputes their own beliefs and values into the process.Such advancements may also enable more sophisticated explorations of Internet conflict.With a highdimensional estimate of ideology for a user and their body of comments, research on Internet conflict can extend beyond high-temperature "confrontation" alone.This would enable analysts to identify and respect "legitimate" conflict-conflict that emerges not from trolling or a clash of moods and personalities (Cheng et al., 2017), but a clash of underlying worldviews.

We believe our method also extends well to the study of academia itself, i.e. the science of science.An unsupervised method to identify terms that translate well into adjacent scientific fields/approaches would make cross-and interdisciplinary studies easier, providing a ready lexicon of ideas which best relate to what you already know.It could also allow us to examine how ideas fare when they are imported into fields adjacent or distant to their point of origin.Even more broadly, our approach could be used to generalize search that takes into account different perspectives onand different phrasings for-similar underlying concepts and issues.

We recognize the significant impact that modern natural language processing technology can have on society, and the potential for its abuse.This paper lays the groundwork for a large-scale unsupervised approach to the analysis of culture, which could ultimately lead to technologies capable of effectively forecasting conflict and radicalization in online speech.In the wrong hands, that might inspire information operations that could have a chilling effect on online speech.But we are optimistic about the future of this approach to cultural (mis)alignment.As demonstrated, it can be used to identify not only disagreement, but where there is undiscovered potential for agreement.We began this paper with a quote: "The limits of my language are the limits of my world."We hope that by building on this technique to reveal both similarities and differences in community worldviews, we can someday expand the limits of everyone's worldview by facilitating mutual understanding, finding ways to resolve ideological tension, and make new knowledge easier to transmit and receive.

Figure 2: These are not the same!The character on the left, "Aatrox" from League of Legends, projects to the character on the right, "Bloodseeker" from Dota 2.

Figure 3: Misalignment frequency within the "Economics" cluster (top), and the "Authority" cluster (bottom).Color corresponds to the relative intensity of misalignment, and the white squares outline political communities.

Figure 5: Community misalignment with respect to Government cluster (top left), Conflict cluster (top right), sex cluster (bottom left), religion cluster (bottom right).

, which we accessed in January of 2020.These dumps contain comment Number of comments, tokens, and gigabytes in the dataset

r/gaming Rank 1 doom, halo, zelda, ... Rank 2 os, hulu, apple, ... Rank 3 graphics, 480, nvidia, ... r/politics Rank 3 states, president, ...

Randomly sampled words from top topics for a small selection of subreddits.Topics consisting primarily of administrative and moderation messages are omitted.

Performance of Least-squares alignments for the year 2016, measuring alignment to the shared space.

Performance of MultiCCA alignments for the year 2016, measuring alignment to the shared space.

Performance of SVD alignments for the year 2016, measuring pairwise alignment.

33 For readers unfamiliar with the games League of Legends or Dota 2; "/r/summonerschool" is a community for learn-

Selected words from r/leagueoflegends and their nearest image in r/dota2.Alignment is measured in cosine similarity.

We would like to thank members of Knowledge Lab, University of Chicago for helpful comments and suggestions.This work is funded in part by DARPA via grants RA-19-01 and HR00111820006 and AFOSR via grant FA9550-19-1-0354.

Linear Equation solver MultiCCA Year Mode N Acc@1 Acc@5 Acc@10 Acc@1 Acc@5 Acc@10 2016 Acc@1 Acc@5 Acc@10 Acc@1 Acc@5 Acc@10 ALL ∼30k 0.4980 0.6462 0.7091 0.5064 0.6683 0.7221 SW 1000 0.4789 0.6434 0.6991 0.4562 0.6130 0.6680 5000 0.5203 0.6841 0.7374 0.4948 0.6531 0.7063 2018 2019 Mode N Acc@1 Acc@5 Acc@10 Acc@1 Acc@5 Acc@10 ALL ∼30k 0.
