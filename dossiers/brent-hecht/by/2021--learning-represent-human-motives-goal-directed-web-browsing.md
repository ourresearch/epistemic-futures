---
title: "Learning to Represent Human Motives for Goal-directed Web Browsing"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2021
date: 2021-09-13
venue: "arXiv (Cornell University)"
authors: "Jyun-Yu Jiang, Chia-Jung Lee, Longqi Yang, Bahareh Sarrafzadeh, Brent Hecht, Jaime Teevan"
source_url: https://doi.org/10.1145/3460231.3474260
fulltext_url: https://content.openalex.org/works/W3187795233.grobid-xml
openalex_id: W3187795233
doi: https://doi.org/10.1145/3460231.3474260
oa_status: gold
cited_by_count: 0
retrieved: 2026-08-13
content: full-text
notes: "Full text retrieved via the OpenAlex Content API (https://content.openalex.org/works/W3187795233.grobid-xml); no binary stored; text extracted from the GROBID TEI rendering hosted at content.openalex.org"
---

# Learning to Represent Human Motives for Goal-directed Web Browsing

## Full text

Learning to Represent Human Motives for Goal-directed Web Browsing

University of California, Los Angeles USA

Amazon Inc. USA

Microsoft USA

Learning to Represent Human Motives for Goal-directed Web Browsing

Motives or goals are recognized in psychology literature as the most fundamental drive that explains and predicts why people do what they do, including when they browse the web.Although providing enormous value, these higher-ordered goals are often unobserved, and little is known about how to leverage such goals to assist people's browsing activities.This paper proposes to take a new approach to address this problem, which is fulfilled through a novel neural framework, Goal-directed Web Browsing (GoWeB).We adopt a psychologically-sound taxonomy of higher-ordered goals and learn to build their representations in a structure-preserving manner.Then we incorporate the resulting representations for enhancing the experiences of common activities people perform on the web.Experiments on large-scale data from Microsoft Edge web browser show that GoWeB significantly outperforms competitive baselines for in-session web page recommendation, re-visitation classification, and goal-based web page grouping.A follow-up analysis further characterizes how the variety of human motives can affect the difference observed in human behavioral patterns.

Constructs such as motives and goals are recognized in the psychology literature as the fundamental forces that guide human behavior.While a variety of interpretations of goals exist, there is consensus that these constructs regulate controlled cognitive processes such as planning and resource allocation, and direct behavioral sequences intended to enact specific performances [10].When people browse the web, which is one important behavior common in modern lives, goals also underlie why they do what they do.For example, they may buy products to work towards their fitness goals, plan trips to stay connected with friends and family, conduct business to pursue career success, or do research or seek health advice in support of their well-being.Understanding peoples' goals not only helps answer the "why" questions about their activities [18,56], but also signifies where the opportunities sit for potential improvements.

Although goals and motives are fundamental to browsing behaviors, they stay unobserved and cannot be easily inferred due to the variety and complexity of activities prevalent on modern web browsers.Moreover, the question of how goals and motives can be utilized to assist browsing remains unanswered.To bridge the gap, we propose to adopt the well-established bodies of psychological theories [5,11,44] regarding human motives to the need for browser-centric activities.For instance, the motive of staying physically healthy may energize a person to consider purchasing a rowing machine or to learn nutritious ingredients via a number of web interactions.As a result, a better understanding of human motives can guide how we might enhance browsing experiences pertaining to people's needs.

Previous research on supporting user goals on the web has primarily sought to understand and categorize a person's intent manifested through search queries.In their seminal studies, Broder [8] and Rose and Levinson [54] classified the goal of a user query into one of three categories: navigational, informational, and transactional.Successive work refined intent categorization by introducing purchase, sell or job search intents [14,36], as well as examined the variability of intents across different users [62].The main objective of research in this field is often to inform and improve the search process [8,9,35,54], and the characteristics of user goals tend to be task-oriented or situation-specific.In contrast to that, we emphasize incorporating the fundamental human goals into the context of web browsing, since they are recognized to be key to the core values in people's lives [5] (e.g.health, well-being, sustainability, and learning).

In this paper, we focus on tackling two research agendas toward our goal-directed vision, namely, how to represent influential human goals 1 and how to leverage the learned representations to provide assistance in browsing sessions.We propose a unified neural framework, Goal-directed Web Browsing (GoWeB), for both objectives laid out in two phases.The first phase concerns human motives.Psychology research has developed decades of knowledge informing which human goals are considered influential through theoretical and empirical evidence.Inspired by the findings, GoWeB uses these goals as the backbone and builds on the top to learn intrinsic goal representations following a distance-based reconstruction objective to retain inherent hierarchical structures 2 .GoWeB further devises a neural goal estimator, which learns to transfer the knowledge entailed in these goal representations to estimating people's motives for visiting web pages.The second phase focuses on enhancing web experiences with what we have learned.Specifically, GoWeB integrates the goal estimator with modern language models [15] to assist three common interactions or needs people have on the web.We consider an in-session web page recommender that recommends web pages to help people advance their goals, a web page re-visitation classifier that predicts if a person will revisit a web page in the future due to recurring or unfinished goals, and a web page grouping method that clusters in-session web pages according to underlying goals.The overall framework is illustrated in Figure 4.

We evaluate GoWeB using anonymized browsing logs obtained from the Microsoft Edge browser.The experimental results show that GoWeB consistently outperforms competitive baselines in all three browser-centric applications, suggesting that capturing fundamental human motives can empirically improve the intelligence of web browsers.To understand the effectiveness, we find that the learned intrinsic goal representations largely preserve the humancurated hierarchical relations.Meanwhile, the goal estimator can effectively predict the goals behind web page visits evaluated based on quantitative and qualitative exercises.Our follow-up analysis further characterizes the browsing patterns when people engage in pursuing different goals.The results suggest that people may explore multiple directions simultaneously when the categories of session's focal goals are broad (e.g., Ethics & Idealism), while they may revisit web resources in shorter intervals for goals concerning social interactions (e.g., Friendship).

Studying goals is an important, long-lasting topic across multiple research disciplines.We examine the different notions of goals that have been investigated in the literature.

Task-oriented Goals in Search and Web Browsing.Prior work has a strong focus on studying search goals as they contribute to a critical segment of web browser usage.The mainstream work in this space follows Broder [8], and Rose and Levinson [54] who classified the goal of user queries into navigational, informational, and/or transactional. Lee et al. [35] identified that 60% of search queries can be associated with informational or navigational goals, and proposed using clicks and anchors to predict those.Caruccio et al. [9] introduced a lightweight taxonomy that added a handful of sub-classes to informational and transactional queries.Casting as a classification problem, they proposed content and behavioral features to predict which class in the taxonomy a query should belong to using data collected from a custom browser extension.For more complex search needs, Jones and Klinkner [26] leveraged human annotations and built predictive models that were trained to segment sequences of user queries into same or different search goals.Among a set of hand-crafted features, they showed that lexical features such as words and characters were identified as the most useful.Similarly, Law and Zhang [32] showed that the ability to decompose a complex search goal into sub-problems (i.e., a set of queries and corresponding search results) can better support a user's information need.

General web browsing behavioral patterns tend to involve higher flexibility and complexity than search.Kumar and Tomkins [31] analyzed large-scale commercial logs and showed that page visits related to search comprise only one-sixth of the log sample.In addition to search, they identified that content consumption (e.g., news, portals, games, verticals, multimedia) comprise about half of online page views, while communication (e.g., email, social networking, forums, blogs, chat) represent about one-third of those.As a result, general web browsing patterns require different types of support.For example, past studies have shown that people are often unable to focus on or return to their goals when using a web browser due to the prevalence of distractions on the web [1,63].Research on Cyberloafing [20,37] and task resumption on the web [19,43,48] have shown that individuals experience difficulty when resuming their main task after external-or self-interruptions [3,13].

Faaborg and Lieberman [18] introduced a program-by-example goal-oriented web browser that allows people to customize how they organize and interact with the web.A person who visits a recipe website, for example, may want to know the nutritional information.By explicitly demonstrating how to complete nutrition extraction once, the system could potentially evoke the same human-specified macros on similar websites.Dix et al. [16] attempted to understand the goals behind user behavior by connecting actions and user-created personal ontology structures.

Higher-ordered Human Goals.Understanding human goals and motives has long been a central area of research in the psychology literature, as the goals of individuals largely direct the behavior in which they engage [29].Earlier attempts in creating goal taxonomies relied on theoretical viewpoints.McDougall [42] presented a list of 13 instincts while Murray [45] articulated 44 variables of personality as forces determining behavior.Chulef et al. [11] took an empirical approach and recruited participants of diverse backgrounds to delve into developing a hierarchical human goal taxonomy based on similarity between goals, providing a concrete and comprehensive structure.More recently, Talevich et al. [60] iterated on the taxonomy derived in [11] with several added classes of human motives.

As our work incorporates long-term goals in browsing sessions to provide goal-directed assistance, we review the classic and stateof-the-art technical methods applicable in the three browser-centric tasks, and conclude with a brief summary comparing previous approaches and ours.

Recommendation.The task of web page recommendation [21] aims to predict the information needs of users and provide them with recommendations to facilitate their navigation.Classic approaches to recommendation relies on mining user-item relationships through collaborative filtering [58] and matrix factorization [23,52].Session-based approaches [61] take into account sessionlevel user actions as a sequential stream of events, based on which recommendations are made to users.In recent years, large-scale deep neural networks [68] have shown top performing effectiveness in recommender systems, including leveraging GRU [24], selfattention blocks [27] and BERT-based architectures [59] for sessionbased recommendation.

Revisitation.Web page revisitation behavior is prevalent on the web.Obendorf et al. [47] suggested that people may revisit web pages to access the same resource again (e.g., for unfinished goals) or may re-access a resource as they expect changed content (e.g., for recurring goals, such as new headlines on a news site).Adar et al. [2] combined quantitative and qualitative approaches and showed that people revisit web pages with varying speed.To help resume previously encountered information, Dontcheva et al. [17] presented a web extension that allows people to extract entities of interest and creates an interactive summary of extracted entities (e.g., hotels that a person considers for a trip).

Grouping.Automatic managing and grouping the vast amount of unorganized web pages can help reduce the cognitive load required when navigating the web.A common strategy is to classify web pages [6,51] by the encapsulated topics; popular class choices include the Open Directory Project, the Yahoo!Directory, categorized URLs from the Wikipedia, etc.To relax the requirement of predefined classes, clustering techniques have been studied to mine related web pages based on semantics or graph partitioning [50].Different from prior studies, we adopt the notion of goals as the basis to associate web pages for web page grouping.

In this work, we incorporate long-term goals to facilitate effective web browsing experiences, including recommendation, revisitation and goal-based grouping, which differ significantly from previous perspectives and approaches.We leverage Poincaré embeddings [46] to derive the goal representations, which are combined with state-of-the-art transformer-based architectures [15] to model users' web session behavior.

This section presents our approach to learning distributed intrinsic goal representations (iGoalRep r д ) for human motives, which are grounded by an expert-curated goal taxonomy in the psychology literature.Moreover, we propose a goal estimator to embed any web page visit p in browsing sessions into the same goal embedding space as r д , and we denote them as visit goal representation (vGoalRep) r p .To learn the goal estimator, we collect and rely on a weak supervision dataset through the associations between related  Root (non-goal)

Taxonomy of Human Goals.We leverage the hierarchical human goal taxonomy curated by Chulef et al. [11] to form the basis of the goal space.Specifically, the taxonomy leaf nodes were curated based on an aggregation of psychology literature [41,45,53,65] and the responses from participants of diverse background, followed by a similarity-based sorting process to create the hierarchy relationship.

The resulting set consists of 135 leaf goal nodes descended from 30 parent categorical nodes.We further introduce a "non-goal" node as the root that covers all the categorical nodes.Conceptually, the root represents prosaic behavior that might not be tied with specific goals; examples could include random distractions on the web or one-time matters.Figure 2 illustrates the final adopted human goal taxonomy consisting of 166 nodes in three layers.Formally, G denotes the set of goals in the goal taxonomy and H denotes the hierarchical structure.

Representation Learning in Hyperbolic Space.To induce the structural bias H , we propose to learn intrinsic goal representations (iGoalRep) in a hyperbolic space.Hyperbolic geometry brings the advantage of learning compact representations that capture both hierarchy and similarity, which, for our case, is desirable as we aim to preserve the hierarchical properties of the goal taxonomy.The center red node indicates the concept of "non-goal," while the blue nodes represent goal categories that cover more specific goals presented as orange nodes.

Concretely, we adopt Poincaré embeddings [46] to derive

.

Subsequent representation learning is then guided by this distance measure where a similar pair of goals should be closer to each other than a remote pair.

Reconstruction Optimization.To start learning, we treat the edges in the goal taxonomy as transitive closure and reconstruct the relationship by minimizing the Poincaré distances between the embeddings of their endpoints.Following prior work [46], we define the loss function L r as:

We adopt RSGD [7], a stochastic Riemannian optimization method, to learn goal embeddings within the Poincaré ball as in [46].To do so, we need to rely on the Riemannian manifold structure of the Poincaré Ball when minimizing L r .Since Euclidean gradient is not directly applicable in hyperbolic space, rescaling gradients depends on the Riemannian metric tensor t x equipped in the Poincaré ball:

x ∈ B d G ; t E denotes the Euclidean metric tensor. 3In practice, we randomly sample 50 negative examples for each positive example.

When a person visits a web page, we aim to predict a visit goal representation (vGoalRep) r p such that r p can best reflect which goals may have driven the visit.To do so, we first build a weak supervision data collection that provide the association information of what the most probable goals are when web pages are being visited.Then, a parameterized goal estimator is introduced to predict r p based on the weak labels according to a multi-class classification objective.

Weak Supervision Data Collection.Inspired by past work [57] that demonstrated search engine queries can contain explicit user objectives (e.g., get rid of belly fat), we first reify every goal in the goal taxonomy with a set of seed queries.For example, we manually generate queries such as "how to be charismatic" and "how to meet new friends" to elicit the high-ordered goal of being likeable, making friends, drawing others near.Then we expand the seed query set with related queries by requesting publicly available Microsoft Bing search API.In total, 300 seed queries and 1,932 related queries represent 165 defined human goals.The last step involves querying the same API using the enlarged query set together with the original goals; we then keep the top 5 returned web pages as the weaklypositive instances for the corresponding goal.For the concept of "non-goal, " i.e., the root of the goal taxonomy, we randomly select 1,000 web page visits from general web browsing logs as "negative examples".Here we denote this data collection as D weak .

Goal Estimator Construction.Next, we aim to devise a goal estimator that can predict vGoalRep r p by projecting each web page p to the same goal embedding space in which r д exists.A web page visit p is commonly characterized by the semantics conveyed via its textual content c p , as well as the website h p where it is hosted (e.g., pages one the same site often demonstrate higher associations).

To build an effective goal estimator, we take as input the two sources of information, p = (h p , c p ), and estimate vGoalRep r p ∈ R d G by:

, where emb G host (h p ) projects the host to a d h -dimensional embedding space; BERT G (•) is a contextualized content encoder, such as BERT [15] and RoBERTa [38]; F G (•) as a fully-connected hidden layer derives ultimate d-dimensional estimated goal embeddings.The output of the goal estimator, r p , can be regarded as a continuous representation of certain underlying motives for visiting a particular web page p.

Multi-class Goal Classification.While the architecture of goal estimator is the same as web page encoder, we learn the parameters using a multi-class goal classification objective guided by D weak .The multi-class classification loss function is defined by categorical cross-entropy [22] as

< l a t e x i t s h a 1 _ b a s e 6 4 = " / c S w d       A final remark to note is that we could derive the most probable goal д p associated with a page p based on the learned r p , by simply calculating the similarity between r p and r д :

When designing GoWeB in Section 4, we choose to incorporate r p rather than д p because a continuous representation can encode more information and reduce sparsity compared to a discrete one.

Based on the goal estimator and visit goal representations introduced in Section 3, we present a unified framework, Goal-directed Web Browsing (GoWeB), to assist common activities that people perform when browsing the web.We first architect a generic neural framework that can encapsulate information incurred in browsing using goal-aware representations.Second, we employ this framework to assist people to advance their goals through in-session recommendation, to pick up their goals through re-visitation prediction, and to focus on certain goals through goal-based clustering.Figure 4 further illustrates an overview of GoWeB.

A web browsing session involves three key actors: individual web pages that a person visits, the sequence of visits in the same session, and the person who performs these visits.To support goal-directed browsing, GoWeB needs to derive representations that effectively incorporate goal awareness for each of these.More concretely, suppose a web browsing session s consists of n web page visits s = {p 1 , . . ., p n } performed by a person u.In the below, we describe the steps to form individual goal-aware visit representation (gVisitRep) as v p i , goal-aware session representation (gSessionRep) as v s , and personal goal representation (pGoalRep) as r u .

Goal-aware Visit Representation (gVisitRep).To represent a web page visit, we consider two types of essential signals, namely the lexical content expressed inside the page as well as the probable goals accounting for the visit.Specifically, we derive content-based embeddings by initializing a separate set of weights using the same encoder architecture described in Section 3.2.For each visit p i , the content embedding w p i ∈ R d V is determined by its underlying content c p i and the host of the page h p i .Formally, we compute content embedding by

), where emb V host (h p ) projects the host to a d h -dimensional embedding space; BERT V (•) is a contextualized language model; F V (•) as a fullyconnected hidden layer derives the final d V -dimensional content embedding.While the content-based embeddings are important, we take a step further to incorporate probable goals for the act of visiting, by concatenating the vGoalRep r p i and the content embedding w p i as x p i = [r p i , w p i ].Thus, visits in the same session s can be denoted as X ∈ R n×d model , where n is the number of pages and

To make page visits sensitive to the session context in which they appear, we propose to apply the multi-head attention mechanism [64] to derive contextualized visit representations.Formally, for each web page visit, the gVisitRep v p i can be computed as:

To represent the overall browsing session, we learn a context vector c i ∈ R 1×d k for each head to dynamically estimate the importance of each visit for a specific application.The gSessionRep v s of the browsing session can then be derived as v s = Concat(head s 1 , . . ., head s k )W Os , where head

As an individual's past goals could be predictive of their future goals or behavior, conventionally it is a common practice to rely on an individual's past browsing activities to derive their personal representation [25].We argue that it is equally important to account for the activities in a currently active session, according to Shah et al. [55] that the activation of a given focal goal tends to result in an inhibition of alternative goals.To implement this idea, GoWeB constructs pGoalRep r u for an individual u by aggregating the current session activities as a query to attend to past activities of the same individual.Suppose {r p i } denotes the vGoalReps for all page visits in a current session; Z u = {p u i } is the set of web pages visited in the past by a user u.We adopt the Luong's attention mechanism [39] to aggregate current session activities as:

, where α i is the weight for r p i ; c s is the context vector to estimates the importance of each visit; F s (•) is a fully-connected hidden layer.The pGoalRep r u is computed by using r s as a query to discover and aggregate past goals related to current session:

where β i is the weight for each historical visit.

To summarize, we have described how to create goal-aware representations for a page visit (v p i ), a browsing session (v s ), and an individual acting in the session (r u ).These representations can, when designed properly, be used for directing people towards their goals while they browse the web.In particular, we consider three opportunities for goal-aware assistance described as follows.

Making progress towards goals when navigating the web can be challenging, which could be due to unfamiliarity with subject matter or other external factors.To address this, GoWeB aims to recommend most goal-related, unseen resources that can help people advance their goals.Concretely, GoWeB formulates an in-session web page recommender.Given n preceding web pages s = {p 1 , • • • p n } visited in a session, GoWeB ranks web pages from a candidate set C according to their likelihood of being visited later in the same session.We follow prior work [12] and cast recommendation as a classification task.Based on the information available in s, we combine the gSessionRep v s and pGoalRep r u as a feature vector.The ranking scores y rec ∈ R |C | of each web page in C can then be calculated as classification logits:

where F hidden (•) is a fully-connected hidden layer; F rec (•) projects the hidden state to the ranking scores of candidate web pages.Finally, the ranked list of recommendations can be generated by retrieving candidates with top ranking scores.

Web page re-visitation is prevalent as people may visit the same resources for unfinished or recurring goals.The ability to forecast potential future re-visitations can be useful for supporting people resuming their goals when predicted correctly.For instance, the predictions can be stored in the browser backend and resurface to users when they start a new session as a reminder.To support this, GoWeB aims to predict whether any of web pages in a current session will be revisited in a future session.For each visit p in the session s, we first construct its feature vector by concatenating the gVisitRep v p and the pGoalRep r u .The probability of the web page being re-visited can then be estimated as:

where F hidden (•) is a fully-connected hidden layer; F rev (•) projects the hidden state to a logit so that the sigmoid function σ ( derive a probabilistic score.We note that for the first and second tasks, GoWeB is trained end-to-end to directly optimize the target objective.

Another common challenge with web browsing is being able to rationalize with goals and focus on subsets of web pages by goals.Considering that people often visit multiple, potentially diverse web pages in a session, this may create high cognitive load when people switch in-between goals.For this, we employ GoWeB to group in-session web pages by goals, such that the resulting groups of pages can be used to categorize ongoing flows and help people concentrate on certain goals of choice.Specifically, we cast this as a clustering task where the vGoalRep r p of each visit p is used as features, based on which subsequent feature-based clustering algorithms can be applied.

This section examines the effect of incorporating high-ordered goals into the context of web browsing.We compare each of the browser-centric tasks with competitive baselines and demonstrate how GoWeB can enhance multiple browsing experiences.

Experimental Datasets.Our main experimental dataset, denoted as D web , consists of web browsing sessions that are used for evaluating the three goal-based applications supported by GoWeB.D web was constructed by randomly sampling the anonymized logs of Microsoft Edge web browser 5 .A session is composed of a sequence of web page visits of a user, where a boundary is found between two consecutive visits that are at least 30 minutes apart.The logs contain records of web pages visits assembled by sessions, where each page comes with a host, a title and a timestamp when the page was visited; the titles are used as the web page content.The data was sampled from June 2020, where the training and test sets were respectively gathered from the periods of June 1st to 23rd and June 24th to 30th.To avoid tail behavior, a web page is discarded if it appears less than 10 times in the sampling period, and short sessions with less than 10 page visits are disregarded as the associated goals are likely to be simpler.In total, our dataset contains web pages originating from 79,695 unique hosts (websites).

We prepare two disjoint test sets to study the effect of incorporating the notion of personal goals.The warm-start sample includes users whose behavior can be found in the training period, while the cold-start sample draws from users new to the system.The statistics of D web used for the experiments are shown in Table 1.For cold-start users, since we do not have access to their past behavior, we exclude the personal goal representations from the framework and denote this variant as GoWeB (NP).Implementation Details.We implement GoWeB and baseline methods with the PyTorch framework [49].The dimensions of goals and hosts (i.e., d G and d h ) are set to 64, while the number of hidden units in fully-connected layers and the dimension of the remaining embeddings are set to 128.The number of attention heads k is set to 8. We use a learning rate of 0.3 for RSGD [7] in the Riemannian optimizer, while a learning rate 10 -5 and (β 1 , β 2 ) = (0.9, 0.999) are used in the Adam optimizer [28] for optimizing the supervised goal-based applications and the goal estimator.For contextualized language modeling (i.e., the BERT functions in Section 4 and 3), we use the pre-trained RoBERTa [38] models provided by Hugging-Face [66].We will open-source our implementation.

Recall that the in-session recommender predicts goal-related web pages that are likely to be visited later in the same session.Specifically, for a session, we take the first half of page visits as observed input information and use the second half as ground-truth to evaluate our model.The ranking candidates of web pages are generated by removing the top 10 popular web pages (e.g., msn.com and google.com)and selecting the top 50,000 frequent web pages 6 from the remaining set.For both test sets, we assert that the ground-truth (i.e., the second half) of every session contains at least one web page from the candidate set.We treat the task as a retrieval problem and evaluate it by conventional metrics, including MRR@10, HR@{1, 5, 10}, and NDCG@{5, 10}.We compare our method with state-of-theart top-K session-based recommenders, including popularity (Pop), BPRMF [52], NCF [23], Caser [61], GRU4Rec [24], SASRec [27], and BERT4Rec [59].We further consider a modern content-based modeling method that incorporates web page semantics using BERT and contextualization.We implement this by reusing the GoWeB neural architecture but with all the goal-awareness removed (i.e.excluding r p and any representations derived based on r p ), which is denoted as SemRec.

Table 2 demonstrates the recommendation performance in two test sets.Among the baseline methods, SemRec performs better than conventional session-based recommenders that disregard web page content.It advocates for the importance of modeling the semantics of web pages, as the open-domain nature of the web can make recommendation more challenging than domain-specific applications (e.g.movies).Without personalization, GoWeB (NP) performs the best and outperforms SemRec by 18.52% and 16.09% in MRR@10 for two test sets.This empirical finding sheds light on the opportunity of modeling human motives and higher-level goals carried by the goal estimator without accessing historical data, since only the in-session page visits are considered.For the warm-start test set where access to past page visits is available, GoWeB can further provide more satisfactory recommendations.Overall, the results suggest that incorporating people's motives can lead to better recommendation in web browsing sessions.

For re-visitation prediction, given a browsing session, the task is formulated as a binary classification problem to predict if each web page visit in the session will be re-visited by the same user in any future session.Similarly, we consider two families of baseline methods.The conventional sequence modeling methods learn an embedding vector for each unique web page without using web page content, including CNN, RNN, SAS [27], BERT [15,38].To account for page content, we likewise build a strong semantic classifier, SemCLS, based on the sequence modeling component embedded in GoWeB without using any goal-related representations.We utilize common binary classification metrics, including F1-score, precision, recall, and accuracy, for evaluation.

Table 3 shows the classification performance of methods in two test sets.Consistent with the results in Table 2, SemCLS that incorporates web page content is the best-performing baseline method.Compared to SemCLS, GoWeB (NP) respectively provides 2.32% and 3.30% gains in F1 scores for the two test sets.Similar to in-session recommender, GoWeB introduces further gains when using the focal goals to attend to past goals.These results indicate that the GoWeB framework can provide goal-aware assistance in supervised ranking and classification tasks.

The objective of the web page grouping task is to create coherent clusters of web pages inside a session in an unsupervised fashion.We treat the goal representations r p derived in GoWeB as features and apply K-means++ algorithm [4] to cluster page visits into different groups.We consider two popular text modeling methods, doc2vec [34] and BERT [15], as the baselines where the corresponding embedding vectors are used for clustering.

To create ground-truth for evaluation, we leverage the outcome of a proprietary hierarchical topical classifier as references that different methods can compare to.The proprietary classifier predicts the topics of web pages according to a 3-layer taxonomy consisting of a root node, 22 category nodes, and 288 leaf nodes.This setup resembles the traditional web page classification task [6,51] where a topical organization of the web was found to be useful.Once we obtain the outcome topics, the number of ground-truth clusters in each session is also determined accordingly.Note that, following previous studies [33,67], our focus is to evaluate the clustering quality using different embedding features.We acknowledge past work on determining the optimal number of clusters [30] as a different research problem.

Table 4 shows the resulting grouping performance on NMI and AMI metrics [40]; here we combine the two test sets together since this is an unsupervised task.BERT, as is powered by a decent pretrained contextualized language model, performs better than doc2vec.Meanwhile, the goal representations generated by goal estimatoroutperforms both baselines, suggesting its efficacy for tackling unsupervised tasks.Figure 5 further shows the percentage of clusters over the number of unique ground-truth topics included in a cluster.An ideal cluster should contain exactly one topic.

The results show that GoWeB tends to derive purer clusters with fewer unique classes compared to baselines.It may suggest that the goal-aware representations are also more topically coherent.

In section 5, we demonstrate empirically the effectiveness of GoWeB when applying to browser applications.Now we turn our attention to deepen our understanding for the effectiveness of the goal estimator, and how the variety of goals may affect the differences observed in people's behavioral patterns.

Effectiveness of Goal Estimator.To uncover the details, we scrutinize the goal estimator as it powers the prediction for goal representations when people make visits to web pages.Recall that the goal estimator is learned with a multi-class objective, where a 136-way classification is carried out to predict among the 135 leaf goals plus a non-goal class.We use 90% of weakly-labeled instances from D weak for training, and evaluate on the remaining 10%.As a result, we achieve 55.27% and 83.01%F1 scores for predicting individual goals and goal categories.Figure 6 depicts the confusion matrix for our goal estimator, where the grid partitions leaf goals into goal categories.We can see that most of the predictions are  We further conduct a lightweight qualitative exercise to analyze the relations between hosts and predicted goals.We first identify top hosts that cover a higher proportion of web pages being predicted closest to each goal category.Two annotators were then asked to judge whether these hosts are topically relevant to the corresponding categories.Table 5 shows the assessment results with 100% agreement from the two annotators.The assessments suggest that the goal estimator can make reasonable predictions in the majority of cases.

Characterization of In-session Goals.To start, we note that people tend to involve in multiple goals in a single session; for example, the average number of goals can be more than 5 for sessions containing 10 page visits.We also find that the increase in the number of goals pursued is sub-linear to the session length; for example, sessions of 60 page visits are associated with fewer than 14 goals on average.Given that people may seek multiple goals in a session, to which degree each goal category could be considered as the session's focal goal? Figure 7a illustrates the percentage of being the only goal in a single session.On one hand, for sessions that contain a Finances goal, about 16% of the times people concentrate solely on this goal category.We conjecture that it might be related to the time-dependent sensitivity required in the process of financial decision making; further studies need to be conducted in the future.On the other hand, we find that more nebulous goals such as Ethics & Idealism are seldom being pursued singularly (i.e., only 3% of the times).The results suggest people behave differently according to the types of goals, and fathoming the underlying objectives is key to providing delightful web browsing experiences.For example, enabling a focus mode on detecting goals that require high concentration, or proactively recommending new resource for more exploratory goals could be new designs to consider.

Characterization of Revisitation Patterns by Goals.People's goals that motivate visits to certain web pages may also have an impact on how these pages are revisited.We analyze temporal cross-session revisitation patterns.A revisit is identified by two consecutive visits of the same web page, where the elapsed time between the former visit and the latter is considered as the duration.Following Adar et al. [2], we group all collected revisitation patterns into 14 unequal-size buckets according to the length of duration.Figure 7b  30 goal categories exhibit similar revisiting patterns.Most of the revisits (37%) occur roughly after a day or within few days, while between 23% to 36% of revisits occur within 7 hours.We observe far less revisiting after a week has passed.This could be due to the limitation of our data being sampled from a month period.

Beyond the distributional similarity at a macro level, we observe distinct patterns in the top 5 goal categories for three revistation duration scales in Table 6.The results suggest that goal categories concerning social interactions (Friendship, Social Recognition, and Marriage), addictability (Entertainment), and timeliness (Appearance) can lead to relatively quicker revisits within hours.It may imply that inter-personal relationships tend to urge people to voluntarily stay up-to-date, potentially due to the desire for intimacy or attractive looks, or the fear of missing out.On the contrary, goal categories (Career development, Self-sufficiency, and Social Qualities) that demand continuous investment associate more frequently with slower revisits.More abstract, higher-ordered goals, such as Order, Receiving from Others and Stability & Safety may result in the slowest revisitation compared to more concrete goals such as Entertainment.This highlights the opportunities for supporting people browsing the web, where an ambient reminder for a potential revisit can reduce the overhead of manual retrieval.

In this paper, we highlight the importance of modeling human motives grounded by the long history of psychology literature.A unified neural framework, GoWeB, is presented to fulfill this vision.We build on the top of existing taxonomy and concertize these goals with structure-preserving representation learning in hyperbolic space, based on which a goal estimator is introduced to tighten the loop of how goals could be employed for enhancing browsing experiences.We showcase the generality of GoWeB and adopt it in three browser-centric applications.On real-world data, GoWeB consistently outperforms competitive baselines for both warm-start and cold-start users, and demonstrates additional gains when using the focal goals to attend to past goals.Our follow-up analysis reveals the effectiveness of the goal estimator via quantitative and qualitative exercises, and characterizes the similarities and differences found in behavioral patterns when people pursue different goals.

Our work brings new perspectives in multiple ways.We present a promising paradigm where we capture the fundamental motives that drive people in their actions and reflect those in digital applications.Broadly speaking, we introduce and transfer the knowledge from psychology findings to modeling browsing sessions on the web, while keeping the framework flexible such that future research could incorporate other types of taxonomies.It is our hope that Percentage 3% 4% 5% 6% 7% 8% 9% 10% 11% 12% 13% 14% 15% 16% these findings can lift the burden of understanding and characterizing complex human goals for ubiquitous web browsing applications.

t e x i t s h a 1 _ b a s e 6 4 = " O x m W d b o R I X L 3 3 D D h r 5 l n P 2 q D c E s = " > A A A C S H i c b V B N S w J B G J 6 1 L 7 M v q 2 O X I Q n s I r t C J H Q R I u p o k R / g i s y O r z o 4 O 7 v M z E q y + G P 6 N U G n O v Y v O h X d m t U 9 p P b A C w / P + / 1 4 I W d K 2 / a H l V l b 3 9 j c y m 7 n d n b 3 9 g / y h 0 c N F U S S Q p 0 G P J A t j y j g T E B d M 8 2 h F U o g v s e h 6 Y 2 u k 3 x z DF K x Q D z q S Q g d n w w E 6 z N K t J G 6 + S u X g t A g m R j g G 6 W Z T z T 0 c I M p p v F t Q L j r 5 h 7 A T F S m a t a C i + N E N + J 5 N 1 + w S / Y M e J U 4 K S m g F L V u / s v t B T T y z S z K i V J t x w 5 1 J y Z S M 8 p h m n M j B S G h I z K A t q G C + K A 6 8 e z J K T 4 z S g / 3 A 2 l C a D x T / 3 b E x F d q 4 n u m 0 j w x V M u 5 R P w v 1 4 5 0 v 9 K J m Q g j D Y L O F / U j j n W A E 8 d w j 0 m g m k 8 M I V Q y c y u m Q y I J N b Y t b v H 8 h R / i p / n p O W O U s 2 z L K m m U S 8 5 F y b 4 v F 6 q V 1 L I s O k G n q I g c d I m q 6 A 7 V U B 1R 9 I x e 0 B t 6 t 1 6 t T + v b + p m X Z q y 0 5 x g t I J P 5 B Y 7 G s v E = < / l a t e x i t > Estimated Visit Goal Representation (vGoalRep) < l a t e x i t s h a 1 _ b a s e 6 4 = " E m d W O a e 0 + 8 0 f 5 m 0 C A w o R 7 i a I Y l U = " > A A A C J n i c b V D L S g M x F M 3 4 r P U 1 6 k r c B I v g q s w U x C 4 L b l x W s A 9 o h 5 J J 7 7 S h S W Z I M m I Z i l 8 j u N I / c S f i z q 9 w b d r O w r Y e C B z O v T f n 3 h M m n G n j e V / O 2 v r G 5 t Z 2 Y a e 4 u 7 d / c O g e H T d 1 nC o K D R r z W L V D o o E z C Q 3 D D I d 2 o o C I k E M r H N 1 M 6 6 0 H U J r F 8 t 6 M E w g E G U g W M U q M l X r u a Z e C N K C Y H O A W h L h O B oC b T D P T c 0 t e 2 Z s B r x I / J y W U o 9 5 z f 7 r 9 m K b C / k c 5 0 b r j e 4 k J M q I M o x w m x W 6 q I S F 0 Z B 0 6 l k o i Q A f Z 7 I Q J v r B K H 0 e x s k 8 a P F P / T m R E a D 0 W o e 0 U x A z 1 c m 0 q / l f r p C a q B h m T S W p A 0 r l R l H J s Y j z N A / e Z A m r 4 2 B J C F b O 7 Y j o k i l A b y q J L K B Z u y B 7 n q x d t U P 5 y L K u k W S n 7 V 2 X v r l K q V f P I C u g M n a N L 5 K N r V E O 3 q I 4 a i K I n 9 I x e 0 Z v z 4 r w 7 H 8 7 n v H X N y W d O 0 A K c 7 1 9 / 9 6 X u < / l a t e x i t > Web Page Visit < l a t e x i t s h a 1 _ b a s e 6 4 = "

Figure 1: Framework for learning intrinsic goal representations (iGoalRep) and training the goal estimator to predict visit goal representations (vGoalRep).

Figure 2: Illustration of the constructed 3-layer goal taxonomy with 166 nodes.

Figure 3: Illustration of learned 2-dimensional Poincaré goal representations with the 3-layer goal taxonomy from[11].The center red node indicates the concept of "non-goal," while the blue nodes represent goal categories that cover more specific goals presented as orange nodes.

be an open Poincaré ball, where || • || indicates the Euclidean norm.In contrast to Euclidean distance, the hyperbolic distance between any two points u, v ∈ B d G is given as:

Figure 3 visualizes the resulting iGoalRep r д with two dimension 4 learned from the goal taxonomy.The results demonstrate that the learned embeddings preserve the desired hierarchical properties and align with the original goal taxonomy curated by human.

a t e x i t > Historical Web Pages < l a t e x i t s h a 1 _ b a s e 6 4 = " N z 9 x p Q W a 5 a c I Q W e l w E v n 6 s c w G b w = " > A A A C L n i c b V B N S 8 M w G E 7 n 1 5 x f V Y 9 e o k P w N N q B 6 H H g Q S / C B P c B W x l p m n Z h a V K S V B x l Z 3 + N 4 E n / i e B B v P o L P J t u P b j N F x I e n u f 9 f P y E U a U d 5 8 M q r a y u r W + U N y t b 2 z u 7 e / b + Q

r z U y I + d 0 P 2 O F u 9 Z I P y F 2 N Z J s 1 q x T + v e H f V c s 3 L I y u C Y 3 A C z o A P L k A N 3 I I 6 a A A M n s A z e A V v z o v z 7 n w 4 n 7 P S g p P 3 H I I 5 O N + / Z 8 q m + Q = = < / l a t e x i t > Goal Estimator < l a t e x i t s h a 1 _ b a s e 6 4 = " O 1 D C O 0 S N q p D P f n 4 l j O b u s

5 y t X r R B e c u x r I J W t e J d V t z b a r l e m 0 d W Q K f o D F 0 g D 1 2 h O r p B D d R E F D 2 h Z / S K 3 p w X 5 9 3 5 d L 5 m 0 j V n P n O C F s r 5 / g U i 5 6 p h < / l a t e x i t > Session Web Page Visits < l a t e x i t s h a 1 _ b a s e 6 4 = " I a b m p l N L o M Z + e N P 0 W G 0 + Z e D u W G U = " > A A A C P 3 i c b V D L S s N A F J 3 4 r P E V d e l m s A h 1 U 5 K C 2 G X B h S 6 r 2 A c 0 p U y m t + 3 Q y S T M T I o l 9 D / 8 G s G V / o J f 4 E 5 c C e 6 c t l n Y 1 g s X D u f c 5 w l i z p R 2 3 X d r b X 1 j c 2 s 7 t 2 P v 7 u 0 f H

H T N y n p O 0 E J Y P 7 9 T F 7 B u < / l a t e x i t > Visit Goal Representation (vGoalRep) < l a t e x i t s h a 1 _ b a s e 6 4 = " J Q l J j V F h m z V v Q T w J P O S i w v m e m w c = " > A A A C R 3 i c b V D L S g M x F M 3 U V 6 2 v U Z d u g k W o C 8 u M I I o r w Y U u q 9 g q d E q 5 k 9 7 W Y C Y z J B m 1 D P 6 L X y O 4 0 q 1 f 4 a 6 4 N J 1 2 Y V s v B A 7 n n N z H C R P B t f G 8 L 6 c w N 7 + w u F R c L q 2 s r q 1 v u J t b D R 2 n i m G d x S J W d y F o F F x i 3 X A j 8 C 5 R C F E o 8 D Z 8 O B / q t 4 + o N I / l j e k n 2 I q g J 3 m X M z C W a r u n A U N p U H H Z o x c x i A N 4 A o W 0 w T U 3 Q V C 6 R t t N W 0 d u t 0 S l l 0 u W 3 2 + 7 Z a / q 5 U V n g T 8 G Z T K u W t s d B J 2 Y p Z F t x w R o 3 f S 9 x L Q y U I Y z g S + l I N W Y A H u A H j Y t l B C h b m X 5 j S 9 0 z z I d 2 o 2 V f d L Q n P 3 7 I 4 N I 6 3 4 U W m c E 5 l 5 P a 0 P y P 6 2 Z m u 5 J K + M y S Q 1 K N h r U T Q U 1 M R 0 G R j t c I T O i b w E w x e 2 u l N 2 D A m Z T m 5 w S R h M 3 Z M + j 1 U s 2 K H 8 6 l l n Q O K z 6 R 1 X v 6 r B 8 d j K O r E h 2 y C 6 p E J 8 c k z N y S W q k T h h 5 J W / k g 3 w 6 7 8 6 3 M 3 B + R t a C M / 6 z T S a q 4 P w C q c m y g w = = < / l a t e x i t > Goal-aware Visit Representation (gVisitRep) < l a t e x i t s h a 1 _ b a s e 6 4 = " y Ko o G t 3 4 G q 2 V k P q G o 7 x y t Q 0 0 p a E = " > A A A C J n i c b V B N S w M x E J 3 1 s 9 a v q i f x E i y C p 7 J b E H u s e N B j B f s B 7 V K y a b Y N T T Z L k h X L U vw 1 g i f 9 J 9 5 E v P k r P J t u e 7 C t D w Y e 7 8 0 w M y + I O d P G d b + c l d W 1 9 Y 3 N 3 F Z + e 2 d 3 b 7 9 wc N j Q M l G E 1 o n k U r U C r C l n E a 0 b Z j h t x Y p i E X D a D I b X E 7 / 5 Q J V m M r o 3 o 5 j 6 A v c j F j K C j Z W 6 h e M O o Z G h i k V 9 d C M x R 1 f G W C H z i m 7 J z Y C W i T c j R Z i h 1 i 3 8 d H q S J M K O E 4 6 1 b n t u b P w U K 8 M I p + N 8 J 9 E 0 x m S I + 7 R t a Y Q F 1 X 6 a v T B G Z 1 b p o V A q W 5 F B m f p 3 I s V C 6 5 E I b K f A Z q A X v Y n 4 n 9 d O T F j x U x b F i f 2 L T B e F C U d G o k k e q M cU J Y a P L M F E M X s r I g O s M L G h z G 8 J x N w P 6 e P 0 9 L w N y l u M Z Z k 0 y i X v o u T e l Y v V y i y y H J z A K Z y D B 5 d Q h V u o Q R 0 I P M E z v M K b 8 + K 8 O x / O 5 7 R 1 x Z n N H M E c n O 9 f O k S m X Q = = < / l a t e x i t > Goal Attention < l a t e x i t s h a 1 _ b a s e 6 4 = " I a b m p l N L o M Z + e N P 0 W G 0 + Z e D u W G U = " > A A A C P 3 i c b V D L S s N A F J 3 4 r P E V d e l m s A h 1 U 5 K C 2 G X B h S 6 r 2 A c 0 p U y m t + 3 Q y S T M T I o l 9 D / 8 G s G V / o J f 4 E 5 c C e 6 c t l n Y 1 g s X D u f c 5 w l i z p R 2 3 X d r b X 1 j c 2 s 7 t 2 P v 7 u 0 f H D p H x 3 U V J Z J C j U Y 8 k s 2 A K O B M Q E 0 z z a E Z S y B h w K E R D K + n e m M E U r F I P O h x D O 2 Q 9 A X r M U q 0 o T p O y a c g N E g m + r j O F N P 4 J i L c 9 + / B j F F G m t X 5 v l 0 Y T Q V D X 3 S c v F t 0 Z 4 F X g Z e B P M q i 2 n G + / W 5 E k 9 B M o 5 w o 1 f L c W L d T I j W j H C a 2 n y i I C R 2 S P r Q M F C Q E 1 U 5 n v 0 3 w u W G 6 u B d J k 0 L j G f u 3 I y W h U u M w M J U h 0 Q O 1 r E 3 J / 7 R W o n v l d s p E n G g Q d L 6 o l 3 C s I z w 1 C n e Z B K r 5 2 A B C J T O 3 Y j o g k l D j 1 u K W I F z 4 I X 2 c n 2 4 b o 7 x l W 1 Z B v V T 0 L o v u X S l f K W e W 5 d A p O k M F 5 K E r V E G 3 q I p q i K I n 9 I x e 0 Z v 1 Y n 1 Y n 9 b X v H T N y n p O 0 E J Y P 7 9 T F 7 B u < / l a t e x i t > Visit Goal Representation (vGoalRep) < l a t e x i t s h a 1 _ b a s e 6 4 = " E / L j 6 / Z 0 C x 4 E s h 8 x m W 8 D U x b p w X 0 = " > A A A C I 3 i c b V D L S s N A F J 3 4 r P U V F d y 4 G S y C q 5 I U R Z c F N y 7 r o w 9 o Q 5 l M b 9 q h k 0 m Y m Y g l 9 m c E V / o n 7 s S N C 3 / D t Z M 2 C 9 t 6 Y O B w 7 u v M 8 W P O l H a c L 2 t p e W V 1 b b 2 w U d z c 2 t 7 Z t f f 2 G y p K J I U 6 j X g k W z 5 R w J m A u m a a Q y u W Q E K f Q 9 M f X m X 1 5 g N I x S J x r 0 c x e C H p C x Y w S r S R u v Z h h 4 L Q I J n o 4 / 4 d q K z x F u K u X X L K z g R 4 k b g 5 K a E c t a 7 9 0 + l F N A n N M s q J U m 3 X i b W X E q k Z 5 T A u d h I F M a F D 0 o e 2 o Y K E o L x 0 4 n + M T 4 z S w 0 E k z R M a T 9 S / E y k J l R q F v u k M i R 6 o + V o m / l d r J z q 4 9 F I m 4 k S D o N N D Q c K x j n A W B u 4 x C V T z k S G E S m a 8 Y j o g k l C T y O w V P 5 z 5 Q / o 4 t V 4 0 Q b n z s S y S R q X s n p e d m 0 q p e p Z H V k B H 6 B i d I h d d o C q 6 R j V U R x Q 9 o W f 0 i t 6 s F + v d + r A + p 6 1 L V j 5 z g G Z g f f 8 C M z C l V A = = < / l a t e x i t > gSessionRep < l a t e x i t s h a 1 _ b a s e 6 4 = " e F F V b d Q V n V x 4 l 6 3 Q H M 7 4 N e 6 5 A B g = " > A A A C Q n i c b V D L S g M x F M 3 4 r P U 1 6 t J N s A h 1 U 2 Y K x S 4 L L n R Z x T 6 g U 0 o m v W 1 D M 8 m Q Z M Q y 9 E v 8 G s G V f o G / 4 E 4 E V y 5 M H w v b e i F w O O f k P k 4 Y c 6 a N 5 7 0 7 a + s b m 1 v b m Z 3 s 7 t 7 + w a

9 L w o M A 3 4 F t p a 0 8 9 Q Z B P p 4 I l r 3 o u D m v 4 E 0 L r w J / D n J o X t W O + x 1 0 J U 0 i 2 4 x y o n X L 9 2 L T T o k y j H I Y Z 4 N E Q 0 z o k P S h Z a E g E e h 2 O j 1 v j M 8 t 0 8 U 9 q e w T B k / Z v z 9 S E m k 9 i k L r j I g Z 6 G V t Q v 6 n t R L T K 7 d T J u L E g K C z Q b 2 E Y y P x J C v c Z Q q o 4 S M L C F X M 7 o r p g C h C b W C L U 8 J o 4 Y b 0 c b Z 6 1 g b l L 8 e y C u r F g l 8 q e L f F X K U 8 j y y D T t E Z y i M f X a I K u k F V V E M U P a F n 9 I r e n B f n w / l 0 v m b W N W f + 5 w Q t l P P z C x d F s d E = < / l a t e x i t > Personal Goal Representation (pGoalRep) < l a t e x i t s h a 1 _ b a s e 6 4 = " r S c a M / H K y Q G f n A W g D 0 o s M D e 5 1 R Q = " > A A A C F X i c b V A 9 S w N B E J 2 L X z F + R S 1 t F o N g F e 5 E 0 T J g Y x n B f G B y h L 3 N X r J k d + / Y 3 Q u G 4 / 6 F Y K X / x E 5 s r f 0 j 1 m 6 S K 0 z i g 4 H H e z P M z A t i z r R x 3 W + n s L a + s b l V 3 C 7 t 7 O 7 t H 5 Q P j 5 o 6 S h S h D R L x S L U D r C l n k j Y M M 5 y 2 Y 0 W x C D h t B a P b q d 8 a U 6 V Z J B / M J K a + w AP J Q k a w s d J j N x D p O O u l O u u V K 2 7 V n Q G t E i 8 n F c h R 7 5 V / u v 2 I J I J K Q z j W u u O 5 s f F T r A w j n G a l b q J p j M k I D 2 j H U o k F 1 X 4 6 u z h D Z 1 b p o z B S t q R B M / X v R I q F 1 h M R 2 E 6 B z V A ve 1 P x P 6 + T m P D G T 5 m M E 0 M l m S 8 K E 4 5 M h K b v o z 5 T l B g + s Q Q T x e y t i A y x w s T Y k B a 2 B G L h h / R p f n r J B u U t x 7 J K m h d V 7 6 r q 3 l 9 W a p d 5 Z E U 4 g V M 4 B w + u o Q Z 3 U I c G E J D w D K / w 5 r w 4 7 8 6 H 8 z l v L T j 5 z D E s w P n 6 B Z Y s o G M = < / l a t e x i t > vs < l a t e x i t s h a 1 _ b a s e 6 4 = " P y / W E U O f L N d 4 C 4 3 r e 7 a z o m k m F 3 0

6 M 1 5 c T 6 c T + c r b c 0 4 0 5 l 9 N A P n + x d A G 6 7 t < / l a t e x i t > Goal-directed Browser Applications < l a t e x i t s h a 1 _ b a s e 6 4 = "

y b B X O b c Q D p o F a P n a A U M 3 c r p j e E U 2 o d W Y v T I n F w g 3 Z 4 2 x 1 3 x k V / r b l L7 i p 1 8 K T W n B Z r z Y b c 8 t K a B 8 d o C M U o l P U R O e o h d q I o m f 0 i t 7 R R + H N K 3 p l b 3 N W 6 h X m m l 2 0 E N 7 e F w B Z u H 0 = < / l a t e x i t > • In-session Web Page Recommender < l a t e x i t s h a 1 _ b a s e 6 4 = " Z G B C + 9 4 g 9 y u n F B G v e i G G e h H 6 T a o = " > A A A C W H i c b V B N S w M x E J 2 u 3 / W r 6 t F L s A h e L L u C 6 F H w I n i p Y q 3 Q l p J N p z W Y Z J d k V q y L P 8 p f I 3 r S P + H Z b F v E q g O B x 5 s 3 m T c v T p V 0 F I a v p W B m d m 5 + Y X G p v L y y u r Z e 2 d i 8 d k l m B T Z E o h J 7 E 3 O H S h p s k C S F N 6 l F r m O F z f j u t O g 3 7 9 E 6 m Z g r G q b Y 0 X x g Z F 8 K T p 7 q V s 7 b M Q 6 k y S W h l o / 4 V C 6 3 C 8 i a G L M6 H y C 7 x P 1 7 6 S S N 9 O x U c e e + x 7 0 Y T e 9 7 t l u p h r V w V O w v i C a g C p O q d y u f 7 V 4 i M o 2 G R P F x K w p T 6 u T c k h T K e 2 l n D l M u 7 r y P l o e G a 3 S d f H T 0 E 9 v 1 T I / 1 E + u f I T Z i f 0 7 k X D s 3 1 L F X a k 6 3 7 n e v I P / r t T L q H 3 d y a d K M 0 I j x o n 6 m G C W s S J D 1 p E V B a u g B F 1 Z 6 r 0 z c c s s F + Z y n t s R 6 6 o b 8 Y W y 9 7 I O

Figure4: Overview of GoWeB.The goal estimator produces goal representations r p , which are then used to derive goalaware visit v p and session v s representations, as well as personal goal representation r u .These representations facilitate goal-directed experiences in browser applications.The details of the goal estimator are described in Section 3.

Figure 5: The percentage of clusters over different numbers of incorporated unique topics.

Figure 7: (a) The percentage of being in a web browsing session with a single goal for each goal category.(b) Percentage of revisits within different duration interval buckets [2] and three duration scales for goal categories.Note that each line represents the statistics of goals in a certain category.

Statistics of web session experimental datasets.

Performance of methods in session-based web page recommendation.Note that cold-start users do not have personalized historical goal embeddings from training data, so GoWeB with personalization is not available for the cold-start testing dataset.GoWeB (NP) denotes the non-personalized version of GoWeB.

Performance of methods in re-visitation classification.Similar to Table2, GoWeB with personalization is N/A for cold-start users.GoWeB (NP) denotes the nonpersonalized version of GoWeB.

Performance of methods in goal-based clustering.

Top 3 hosts whose web pages are more likely to belong to some goal categories.Hosts with (✓) are labeled as relevant websites to the corresponding categories.The goal "Order" means "(Keep Things in) Order."aligned with the diagonal as correct predictions; among other cases, most of the misclassifications are in the same grid block, indicating that errors are bounded within the same goal category.

illustrates the distributions of revisits in different buckets for different goal categories.Interestingly, at a high level, all the Top 5 goal categories with different duration scales in re-visitations.

Unless otherwise mentioned, we use human motives and goals interchangeably in this paper.

For example, in Chulef et al.[11]'s human goal taxonomy, the goals be affectionate and share feelings are both decedents of a parent goal friendship.

We select dim=2 for visualization convenience here; in the actual experiments, dim=64 is used as described in Section

To the best of our knowledge, unfortunately, there is no publicly available user web browsing dataset that is suitable for evaluating our hypothesis and framework, but we will release our implementation to facilitate the community development.

The number was selected in accordance with the prior study[2] that analyzed largescale web data.

Drawn to distraction: A qualitative study of off-task use of educational technology

Computers & Education

Jesper Aagaard. 2015. Drawn to distraction: A qualitative study of off-task use of educational technology. Computers & Education 87 (2015), 90-97.

Large Scale Analysis of Web Revisitation Patterns

Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '08)

Eytan Adar, Jaime Teevan, and Susan T. Dumais. 2008. Large Scale Analysis of Web Revisitation Patterns. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '08). 1197-1206.

Self-interruptions in discretionary multitasking

Computers in Human Behavior

Rachel F Adler and Raquel Benbunan-Fich. 2013. Self-interruptions in discre- tionary multitasking. Computers in Human Behavior 29, 4 (2013), 1441-1449.

k-means++: The advantages of careful seeding

Technical Report

David Arthur and Sergei Vassilvitskii. 2006. k-means++: The advantages of careful seeding. Technical Report. Stanford.

Modelling Long Term Goals

User Modeling, Adaptation, and Personalization

Debjanee Barua, Judy Kay, Bob Kummerfeld, and Cécile" Paris. 2014. Modelling Long Term Goals. In User Modeling, Adaptation, and Personalization. Springer International Publishing, 1-12.

A Comprehensive Study of Features and Algorithms for URL-Based Topic Classification

ACM Trans. Web

E. Baykan, M. Henzinger, L. Marian, and Ingmar Weber. 2011. A Comprehensive Study of Features and Algorithms for URL-Based Topic Classification. ACM Trans. Web 5 (2011), 15:1-15:29.

Stochastic gradient descent on Riemannian manifolds

IEEE Trans. Automat. Control

Silvere Bonnabel. 2013. Stochastic gradient descent on Riemannian manifolds. IEEE Trans. Automat. Control 58, 9 (2013), 2217-2229.

A Taxonomy of Web Search

SIGIR Forum

Andrei Broder. 2002. A Taxonomy of Web Search. SIGIR Forum 36, 2 (2002), 3-10.

Understanding user intent on the web through interaction mining

Journal of Visual Languages & Computing

Special Issue on DMS2015

Loredana Caruccio, Vincenzo Deufemia, and Giuseppe Polese. 2015. Under- standing user intent on the web through interaction mining. Journal of Visual Languages & Computing 31 (2015), 230 -236. Special Issue on DMS2015.

A Hierarchical Taxonomy of Human Goals

Dissertation

Ada S. Chulef. 1993. A Hierarchical Taxonomy of Human Goals. Dissertation (1993).

A Hierarchical Taxonomy of Human Goals

Motivation and Emotion

Ada S. Chulef, S. Read, and D. Walsh. 2001. A Hierarchical Taxonomy of Human Goals. Motivation and Emotion 25 (2001), 191-232.

Deep neural networks for youtube recommendations

Proceedings of the 10th ACM conference on recommender systems

Paul Covington, Jay Adams, and Emre Sargin. 2016. Deep neural networks for youtube recommendations. In Proceedings of the 10th ACM conference on recommender systems. 191-198.

A diary study of task switching and interruptions

Proceedings of the SIGCHI conference on Human factors in computing systems

Mary Czerwinski, Eric Horvitz, and Susan Wilhite. 2004. A diary study of task switching and interruptions. In Proceedings of the SIGCHI conference on Human factors in computing systems. 175-182.

Detecting online commercial intention (OCI)

Proceedings of the 15th international conference on World Wide Web

Honghua Dai, Lingzhi Zhao, Zaiqing Nie, Ji-Rong Wen, Lee Wang, and Ying Li. 2006. Detecting online commercial intention (OCI). In Proceedings of the 15th international conference on World Wide Web. 829-837.

BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies

Long and Short Papers

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 4171-4186.

From the web of data to a world of action

Journal of Web Semantics

Alan Dix, Giorgos Lepouras, Akrivi Katifori, Costas Vassilakis, Tiziana Catarci, Antonella Poggi, Yannis Ioannidis, Miguel Mora, Ilias Daradimos, Nazihah Md Akim, et al. 2010. From the web of data to a world of action. Journal of Web Semantics 8, 4 (2010), 394-408.

Summarizing Personal Web Browsing Sessions

UIST '06)

Mira Dontcheva, Steven M. Drucker, Geraldine Wade, David Salesin, and Michael F. Cohen. 2006. Summarizing Personal Web Browsing Sessions (UIST '06). 115-124.

A goal-oriented web browser

CHI

A. Faaborg and H. Lieberman. 2006. A goal-oriented web browser. In CHI.

What makes interruptions disruptive? A study of length, similarity, and complexity

Psychological research

Tony Gillie and Donald Broadbent. 1989. What makes interruptions disruptive? A study of length, similarity, and complexity. Psychological research 50, 4 (1989), 243-250.

To monitor or not to monitor: Effectiveness of a cyberloafing countermeasure

Information & Management

Jeremy Glassman, Marilyn Prosch, and Benjamin BM Shao. 2015. To monitor or not to monitor: Effectiveness of a cyberloafing countermeasure. Information & Management 52, 2 (2015), 170-182.

Combination of Web page recommender systems

Expert Syst. Appl

Murat Göksedef and Sule Gündüz Ögüdücü. 2010. Combination of Web page recommender systems. Expert Syst. Appl. 37 (2010), 2911-2922.

Deep learning

Ian Goodfellow, Yoshua Bengio, Aaron Courville, and Yoshua Bengio. 2016. Deep learning. Vol. 1. MIT press Cambridge.

Neural Collaborative Filtering

Proceedings of the 26th International Conference on World Wide Web

X. He, Lizi Liao, Hanwang Zhang, L. Nie, Xia Hu, and Tat-Seng Chua. 2017. Neural Collaborative Filtering. Proceedings of the 26th International Conference on World Wide Web (2017).

Sessionbased Recommendations with Recurrent Neural Networks

Balázs Hidasi, Alexandros Karatzoglou, L. Baltrunas, and D. Tikk. 2016. Session- based Recommendations with Recurrent Neural Networks. CoRR abs/1511.06939 (2016).

End-to-End Deep Attentive Personalized Item Retrieval for Online Content-sharing Platforms

Proceedings of The Web Conference

Jyun-Yu Jiang, Tao Wu, Georgios Roumpos, Heng-Tze Cheng, Xinyang Yi, Ed Chi, Harish Ganapathy, Nitin Jindal, Pei Cao, and Wei Wang. 2020. End-to-End Deep Attentive Personalized Item Retrieval for Online Content-sharing Platforms. In Proceedings of The Web Conference 2020. 2870-2877.

Beyond the Session Timeout: Automatic Hierarchical Segmentation of Search Topics in Query Logs

Proceedings of the 17th ACM Conference on Information and Knowledge Management

CIKM '08

Rosie Jones and Kristina Lisa Klinkner. 2008. Beyond the Session Timeout: Auto- matic Hierarchical Segmentation of Search Topics in Query Logs. In Proceedings of the 17th ACM Conference on Information and Knowledge Management (Napa Valley, California, USA) (CIKM '08). 699-708.

Self-Attentive Sequential Recommendation

IEEE International Conference on Data Mining (ICDM)

Wang-Cheng Kang and Julian McAuley. 2018. Self-Attentive Sequential Recom- mendation. 2018 IEEE International Conference on Data Mining (ICDM) (2018), 197-206.

Adam: A method for stochastic optimization

arXiv preprint

Diederik P Kingma and Jimmy Ba. 2014. Adam: A method for stochastic opti- mization. arXiv preprint arXiv:1412.6980 (2014).

The Interview Questionnaire technique: Reliability and validity of a mixed idiographic-nomothetic measure of motivation

Advances in personality assessment

Eric Klinger. 1987. The Interview Questionnaire technique: Reliability and validity of a mixed idiographic-nomothetic measure of motivation. J. N. Butcher & C. D. Spielberger (Eds.), Advances in personality assessment 6 (1987), 31-48.

Review on determining number of Cluster in K-Means Clustering

International Journal

Trupti M Kodinariya and Prashant R Makwana. 2013. Review on determining number of Cluster in K-Means Clustering. International Journal 1, 6 (2013), 90-95.

A Characterization of Online Browsing Behavior

Proceedings of the 19th International Conference on World Wide Web (WWW '10)

Ravi Kumar and Andrew Tomkins. 2010. A Characterization of Online Browsing Behavior. In Proceedings of the 19th International Conference on World Wide Web (WWW '10). 561-570.

Towards Large-Scale Collaborative Planning: Answering High-Level Search Queries Using Human Computation

Proceedings of the Twenty-Fifth AAAI Conference on Artificial Intelligence (AAAI'11)

Edith Law and Haoqi Zhang. 2011. Towards Large-Scale Collaborative Planning: Answering High-Level Search Queries Using Human Computation. In Proceed- ings of the Twenty-Fifth AAAI Conference on Artificial Intelligence (AAAI'11). 1210-1215.

Deep spectral clustering learning

International Conference on Machine Learning

Marc T Law, Raquel Urtasun, and Richard S Zemel. 2017. Deep spectral clustering learning. In International Conference on Machine Learning. 1985-1994.

Distributed representations of sentences and documents

International conference on machine learning

Quoc Le and Tomas Mikolov. 2014. Distributed representations of sentences and documents. In International conference on machine learning. 1188-1196.

Automatic Identification of User Goals in Web Search

Proceedings of the 14th International Conference on World Wide Web (WWW '05)

Uichin Lee, Zhenyu Liu, and Junghoo Cho. 2005. Automatic Identification of User Goals in Web Search. In Proceedings of the 14th International Conference on World Wide Web (WWW '05). 391-400.

Learning query intent from regularized click graphs

Proceedings of the 31st annual international ACM SIGIR conference on Research and development in information retrieval

Xiao Li, Ye-Yi Wang, and Alex Acero. 2008. Learning query intent from regularized click graphs. In Proceedings of the 31st annual international ACM SIGIR conference on Research and development in information retrieval. 339-346.

The IT way of loafing on the job: Cyberloafing, neutralizing and organizational justice

Journal of organizational behavior: the international journal of industrial, occupational and Organizational Psychology and Behavior

Vivien KG Lim. 2002. The IT way of loafing on the job: Cyberloafing, neutralizing and organizational justice. Journal of organizational behavior: the international journal of industrial, occupational and Organizational Psychology and Behavior 23, 5 (2002), 675-694.

Roberta: A robustly optimized bert pretraining approach

arXiv preprint

Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692 (2019).

Effective Approaches to Attention-based Neural Machine Translation

Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing

Minh-Thang Luong, Hieu Pham, and Christopher D Manning. 2015. Effective Approaches to Attention-based Neural Machine Translation. In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing. 1412-1421.

Introduction to information retrieval

Christopher D Manning, Hinrich Schütze, and Prabhakar Raghavan. 2008. Intro- duction to information retrieval. Cambridge university press.

Motivation and personality

2nd ed.

Abraham H. Maslow. 1970. Motivation and personality (2nd ed.). New York: Harper & Row (1970).

The Energies of Men

William McDougall. 1933. The Energies of Men. New York: Scribner's (1933).

The scope and importance of human interruption in human-computer interaction design

Human-Computer Interaction

Daniel C McFarlane and Kara A Latorella. 2002. The scope and importance of human interruption in human-computer interaction design. Human-Computer Interaction 17, 1 (2002), 1-61.

The psychology of goals

Gordon B. Moskowitz and Heidi Grant. 2009. The psychology of goals.

Explorations in personality : a clinical and experimental study of fifty men of college age

H. A. Murray. 1938. Explorations in personality : a clinical and experimental study of fifty men of college age. (1938).

Poincaré Embeddings for Learning Hierarchical Representations

NIPS'17)

Maximilian Nickel and Douwe Kiela. 2017. Poincaré Embeddings for Learning Hierarchical Representations (NIPS'17). 6341-6350.

Web page revisitation revisited: implications of a long-term click-stream study of browser usage

CHI

Hartmut Obendorf, H. Weinreich, E. Herder, and Matthias Mayer. 2007. Web page revisitation revisited: implications of a long-term click-stream study of browser usage. In CHI.

Timespace in the workplace: Dealing with interruptions

Conference companion on Human factors in computing systems

Brid O'Conaill and David Frohlich. 1995. Timespace in the workplace: Dealing with interruptions. In Conference companion on Human factors in computing systems. 262-263.

Pytorch: An imperative style, high-performance deep learning library

Advances in neural information processing systems

Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. 2019. Pytorch: An imperative style, high-performance deep learning library. In Advances in neural information processing systems. 8026-8037.

A Review on Web Pages Clustering Techniques

Dipak Patel and Mukesh Zaveri. 2011. A Review on Web Pages Clustering Techniques.

Web page classification: Features and algorithms

ACM Comput. Surv

Xiaoguang Qi and Brian D. Davison. 2009. Web page classification: Features and algorithms. ACM Comput. Surv. 41 (2009), 12:1-12:31.

BPR: Bayesian Personalized Ranking from Implicit Feedback

Proceedings of the Twenty-Fifth Conference on Uncertainty in Artificial Intelligence (UAI '09)

Steffen Rendle, Christoph Freudenthaler, Zeno Gantner, and Lars Schmidt-Thieme. 2009. BPR: Bayesian Personalized Ranking from Implicit Feedback. In Proceedings of the Twenty-Fifth Conference on Uncertainty in Artificial Intelligence (UAI '09). 452-461.

The nature of human values

Milton Rokeach. 1973. The nature of human values. New York: Free Press (1973).

Understanding User Goals in Web Search

Proceedings of the 13th International Conference on World Wide Web

Daniel E. Rose and Danny Levinson. 2004. Understanding User Goals in Web Search. In Proceedings of the 13th International Conference on World Wide Web (New York, NY, USA) (WWW '04). 13-19.

Forgetting all else: on the antecedents and consequences of goal shielding

Journal of personality and social psychology

James Y Shah, Ron Friedman, and Arie W Kruglanski. 2002. Forgetting all else: on the antecedents and consequences of goal shielding. Journal of personality and social psychology 83, 6 (2002), 1261.

The Why UI: using goal networks to improve user interfaces

Proceedings of the 15th international conference on Intelligent user interfaces

Dustin A Smith and Henry Lieberman. 2010. The Why UI: using goal networks to improve user interfaces. In Proceedings of the 15th international conference on Intelligent user interfaces. 377-380.

Acquiring knowledge about human goals from Search Query Logs

Information Processing & Management

Markus Strohmaier and Mark Kröll. 2012. Acquiring knowledge about human goals from Search Query Logs. Information Processing & Management 48, 1 (2012), 63 -82.

A Survey of Collaborative Filtering Techniques

Xiaoyuan Su and Taghi M. Khoshgoftaar. 2009. A Survey of Collaborative Filtering Techniques. (2009).

BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer

CIKM '19)

Fei Sun, Jun Liu, Jian Wu, Changhua Pei, Xiao Lin, Wenwu Ou, and Peng Jiang. 2019. BERT4Rec: Sequential Recommendation with Bidirectional Encoder Repre- sentations from Transformer (CIKM '19). 1441-1450.

Toward a comprehensive taxonomy of human motives

PLoS ONE

Jennifer Talevich, Stephen J. Read, David A. Walsh, Ravi Iyer, and Gurveen Chopra. 2017. Toward a comprehensive taxonomy of human motives. PLoS ONE 12 (2017).

Personalized Top-N Sequential Recommendation via Convolutional Sequence Embedding

Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining

Jiaxi Tang and Ke Wang. 2018. Personalized Top-N Sequential Recommenda- tion via Convolutional Sequence Embedding. Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining (2018).

To personalize or not to personalize: modeling queries with variation in user intent

Proceedings of the 31st annual international ACM SIGIR conference on Research and development in information retrieval

Jaime Teevan, Susan T Dumais, and Daniel J Liebling. 2008. To personalize or not to personalize: modeling queries with variation in user intent. In Proceedings of the 31st annual international ACM SIGIR conference on Research and development in information retrieval. 163-170.

Overcoming distractions during transitions from break to work using a conversational website-blocking system

Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems

Vincent W-S Tseng, Matthew L Lee, Laurent Denoue, and Daniel Avrahami. 2019. Overcoming distractions during transitions from break to work using a conversational website-blocking system. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. 1-13.

Attention is all you need

NIPS

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In NIPS. 5998-6008.

Categorical goal hierarchies and classification of human motives

Journal of Personality

Frank Wicker, Frank Lambert, Frank Richardson, and Joseph Kahler. 1984. Cate- gorical goal hierarchies and classification of human motives. Journal of Personality 52 (1984), 285 -305.

HuggingFace's Transformers: State-of-the-art Natural Language Processing

ArXiv

Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, et al. 2019. HuggingFace's Transformers: State-of-the-art Natural Language Processing. ArXiv (2019), arXiv-1910.

Deep spectral clustering using dual autoencoder network

Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition

Xu Yang, Cheng Deng, Feng Zheng, Junchi Yan, and Wei Liu. 2019. Deep spectral clustering using dual autoencoder network. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 4066-4075.

Deep Learning Based Recommender System: A Survey and New Perspectives

Shuai Zhang, Lina Yao, Aixin Sun, and Yi Tay. 2019. Deep Learning Based Recommender System: A Survey and New Perspectives. 52, 1 (2019).
