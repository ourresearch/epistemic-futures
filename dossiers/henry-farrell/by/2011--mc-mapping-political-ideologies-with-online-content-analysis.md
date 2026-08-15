---
title: "Mapping Political Ideologies with Online Content Analysis"
person: henry-farrell
section: by
type: blog-post
year: 2011
date: 2011-03-28
venue: "The Monkey Cage"
authors: "Henry Farrell"
source_url: https://goodauthority.org/news/mapping-political-ideologies-with-online-content-analysis/
retrieved: 2026-08-13
content: full-text
notes: "Post from The Monkey Cage, retrieved from the Good Authority archive (goodauthority.org), which hosts the complete Monkey Cage back catalogue; themonkeycage.org itself is offline. Text spot-verified against Wayback captures of the original themonkeycage.org pages (100% word coverage on 3 checks). Legacy Textile link markup surviving the WordPress migration was converted to markdown links."
---

# Mapping Political Ideologies with Online Content Analysis

## Full text

This paper by Amr Ahmed and Eric Xing seems like the kind of computer science that [political scientists should be interested in](http://www.cs.cmu.edu/~epxing/papers/2010/Ahmed_Xing_EMNLP10.pdf) (PDF).

bq. We can attribute the lexical variations of the word content of a document to three factors … Writer Ideological Belief. A liberal writer might use words like freedom and choice regardless of the topical content of the document. … Topical Content. This constitutes the main source of the lexical variations in a given document. For instance, a document about abortion is more likely to have facts related to abortion, health, marriage and relationships. Topic-Ideology Interaction. When a liberal thinker writes about abortion, his/her abstract beliefs are materialized into a set of concrete opinions and stances, therefore, we might find words like: pro-choice and feminism. On the contrary, a conservative writer might stress issues like pro-life, God and faith.

bq. Given a collection of ideologically-labeled documents, our goal is to develop a computer model that factors the document collection into a representation that reflects the aforementioned three sources of lexical variations. … We introduce a factored topic model that we call multi-view Latent Dirichlet Allocation or mview-LDA for short. Our model views the word content of each document as the result of the interaction between the document’s idealogical and topical dimensions.

bq. We evaluated our model over three datasets: the bitterlemons corpus and a two political blog-data set. …Right Wing News … the Carpetbagger, and Daily Kos … bitterlemons dataset. … our model performs better than the baselines over the three datasets. … it is evident from the figure that the experiment .. which measures each model’s ability to generalize to a totally unseen new blog is a harder task than generalizing to unseen posts form the same blog. However, our model still performs competitively with the SVM baseline. We believe that separating each topic into an ideology-independent part and ideology-specific part is the key behind this performance, as it is expected that the new blogs would still share much of the ideology-independent parts of the topics and hopefully would use similar (but not necessarily all) words from the ideology-specific parts of each topic when addressing this topic.

Via Cosma.
