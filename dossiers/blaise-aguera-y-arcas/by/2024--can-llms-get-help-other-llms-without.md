---
title: "Can LLMs get help from other LLMs without revealing private information?"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2024
date: 2024-01-01
venue: ""
authors: "Florian Hartmann, Duc-Hieu Tran, Peter Kairouz, Victor Cărbune, Blaise Agüera y Arcas"
source_url: https://doi.org/10.18653/v1/2024.privatenlp-1.12
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W4402683378, W4393924368 (type: conference-paper). Full text from the OpenAlex Content API (grobid_xml)."
---

# Can LLMs get help from other LLMs without revealing private information?

## Full text

### Abstract (from OpenAlex metadata)

Cascades are a common type of machine learning systems in which a large, remote model can be queried if a local model is not able to accurately label a user's data by itself.Serving stacks for large language models (LLMs) increasingly use cascades due to their ability to preserve task performance while dramatically reducing inference costs.However, applying cascade systems in situations where the local model has access to sensitive data constitutes a significant privacy risk for users since such data could be forwarded to the remote model.In this work, we show the feasibility of applying cascade systems in such setups by equipping the local model with privacy-preserving techniques that reduce the risk of leaking private information when querying the remote model.To quantify information leakage in such setups, we introduce two privacy measures.We then propose a system that leverages the recently introduced social learning paradigm in which LLMs collaboratively learn from each other by exchanging natural language.Using this paradigm, we demonstrate on several datasets that our methods minimize the privacy loss while at the same time improving task performance compared to a noncascade baseline.

---

## Abstract

Cascades are a common type of machine learning systems in which a large, remote model can be queried if a local model is not able to accurately label a user's data by itself. Serving stacks for large language models (LLMs) increasingly use cascades due to their ability to preserve task performance while dramatically reducing inference costs. However, applying cascade systems in situations where the local model has access to sensitive data constitutes a significant privacy risk for users since such data could be forwarded to the remote model. In this work, we show the feasibility of applying cascade systems in such setups by equipping the local model with privacy-preserving techniques that reduce the risk of leaking private information when querying the remote model. To quantify information leakage in such setups, we introduce two privacy measures. We then propose a system that leverages the recently introduced social learning paradigm in which LLMs collaboratively learn from each other by exchanging natural language. Using this paradigm, we demonstrate on several datasets that our methods minimize the privacy loss while at the same time improving task performance compared to a noncascade baseline.

## Introduction

Large language models (LLMs) such as Gemini Ultra by Google (2023) and GPT-4 by OpenAI (2023) are reporting remarkable performance on many tasks. These models, however, not only come with high inference costs, but they also have to run in data centers far from the local contexts where private data is available. Conversely, models that can run in private contexts, such as Gemini Nano, have more limited capabilities since they run on the user's device.

To unlock state-of-the-art performance in private contexts, local models with access to sensitive data need to be equipped with a privacy-preserving mechanism that enables querying a remote model without sharing any sensitive data. Although standard cascade systems in which a smaller, less capable model, queries a larger, much more capable one in order to solve a task have previously been studied (Yue et al., 2024; Chen et al., 2023) , privacypreserving ones have not yet been explored. In today's cascade systems, the decision of whether a larger model should be leveraged or not is usually done through an additional mechanism that determines whether the query can be handled by the smaller model independently (Li et al., 2021) . If determined to be handled by the larger model, the query is simply forwarded without consideration for the private data it may contain. This poses privacy threats for users, ranging from leaking sensitive data to the forwarded sample even being ingested in training datasets of the remote system.

We introduce the first privacy-preserving approach to cascade systems. Contrasting to standard cascade systems, our local model always assumes its data is private. As such, the local model should not share anything private with the remote model. Going one step further, even if the local model does not verbatim share private information, we aim to prevent a curious remote model operator from reconstructing private data by utilizing auxiliary information it might have. To focus on these challenges, we assume there are no efficiency constraints and that the local model can always ask for help from the remote model, as shown in Figure 1 . Therefore our optimal cascade setup consists of minimizing the privacy loss while maximizing task performance, where an upper bound is given by querying the teacher model with the actual data, although private.

To succeed at this task, the local model, typically smaller and less capable, needs to find the right balance between revealing sufficient information about the problem to receive useful signals from the more capable, remote model while keeping details private. To enable learning from the remote model, the local model makes use of gradient-free learning capabilities through natural language that in-context learning (ICL) capabilities of LLMs enable (Brown et al., 2020) . Throughout, we leverage the recently introduced social learning paradigm by (Mohtashami et al., 2023; Bandura and Walters, 1977) in which LLMs learn through natural language from other LLMs.

Contributions We summarize our contributions as follows: (i) we enable cascade systems to be used where access to private data is necessary to solve a task, but cannot be revealed (ii) we design and evaluate algorithms that sanitize private data while still leveraging in-context learning capabilities of private models and (iii) whereas previous work to the best of our knowledge analyzes settings without auxiliary information, we go one step further by considering auxiliary information and proposing a novel metric to this end (iv) we perform extensive experiments on a diverse range of tasks, quantifying task performance and impact on privacy using standardized measures.

## Problem Setting

Our paper considers a variant of social learning (Mohtashami et al., 2023) where neither of the participants has any labeled data. A local model, called the student, has private data that it cannot label well by itself. A larger, remote model, called the teacher, can do a better job at labeling the data. These two models form a cascade, in which the student can improve its performance by communicating with the teacher. We call what the student sends to the teacher a query. Figure 1 shows a visualization of this setup.

Constraints There are two constraints on the queries from student to teacher. (i) The communication must be privacy-preserving, i.e. the student may not copy over its data and must not reveal anything private. (ii) There is only a single round of communication between student and teacher, meaning neither of them can maintain any state or update a model of the other's capabilities.

To this end, all algorithms follow the same structure. Given (0) that the student needs help, it then (1) uses it's private data to generate a query to the teacher. In turn, (2) the teacher uses the query to generate ICL examples for the student. Finally, (3) the student uses the ICL examples to go back to solving its original problem.

Simplifying assumptions To better focus on the challenges we aim to address in this paper, we furthermore make two simplifying assumptions. (i) We assume that communication with the remote teacher is always helpful. This assumption is reasonable because existing techniques for determining delegation in cascades, discussed in Section 6, could be combined with our methods. (ii) We also assume that both student and teacher are aware of the format of the examples, as shown in Table 4 in the appendix. Such an assumption is useful because we want the student to learn more complex things about the data from the teacher instead of simply learning a format or chain of thought prompt.

Given this problem setting, the goal of the student is to maximize its performance in correctly labeling its data while not revealing anything private that is part of said data.

## Privacy Measures

The student's data may often contain sensitive personal information that should be kept hidden from an untrusted, or partially trusted, teacher. For example, consider a query that tries to figure out what disease could best explain a set of health symptoms that are experienced by a user after they have engaged in a specific sequence of activities. Here, being able to associate the set of activities and/or symptoms with a specific user is a privacy violation that we would like to eliminate.

To address such privacy violations, one might be tempted to resort to data anonymization techniques, such as differential privacy (DP) (Dwork, 2006) . However, these techniques are most useful when computing aggregates across many users (e.g. average of gradient vectors computed on a batch of sensitive training examples). Using the local model of DP (Warner, 1965; Evfimievski et al., 2003; Kasiviswanathan et al., 2011) as a mechanism to mask private information in the query will end up masking both private and non-private information in the query, rendering the masked query useless for the task at hand. Alternatively, using the ICL model of DP (Liu et al., 2024; Wu et al., 2023) to privatize the sensitive parts of the student's data suffers a major hurdle: it assumes the student has many private examples it can jointly consider when creating a query to the teacher. While we do look into grouping examples when generating a query in Section 4.4, we expect the student to have very few private examples, and want it to be able to generate privacy-preserving queries even when only having a single, private example. DP-ICL cannot work in such a setting.

Instead, we leverage data minimization privacy techniques, specifically contextual integrity (Nissenbaum, 2004) which describes privacy as an appropriate flow of information. Under this technique, the student would keep information that is useful for the task (e.g. the activities & symptoms in the above-mentioned example) but remove any personally identifying information that is not relevant to the query context. We note that even under perfect masking, this approach could still leak sensitive information, should the teacher model have access to auxiliary information that can be used to identify certain unique features that are strongly correlated with the "perfectly masked" prompts (Narayanan and Shmatikov, 2008; Sweeney, 2002) . Thus, an important contribution of our work is a methodology for measuring and assessing leakage under auxiliary information.

The success of our approach hinges on correctly identifying and masking the sensitive parts of the query without tampering with the description of the task. To this end, we propose various techniques that can analyze information in queries to produce safe queries that can be shared with the teacher model. To assess the privacy of the queries, we consider two concrete metrics, the entity leak metric that counts entities that exist in both original examples and the student's queries, and the mapping leak metric that considers a setting with auxiliary information.

Entity leak metric Contextual integrity states that privacy is the appropriate flow of information. For most production applications, it is hard to say what is appropriate to share. As a proxy for this, we consider the interpretable metric of leaked entities. All entities, such as names, locations, email addresses, or numbers, in the dataset, are considered to be private. We measure how many of the entities in the original example are still part of the student's query upon masking.

Mapping leak metric Even if all entities are removed from the student's query, it is still possible for a curious teacher to reconstruct private information by carefully analyzing the query. Indeed, auxiliary information that the teacher may have access to can help it be more effective at this. We measure how well the teacher could do this through a worst-case analysis. More precisely, we assume the teacher is presented with 1 original example and 100 masked queries out of which exactly one was generated from the original example. We measure how often the teacher is able to correctly map the original example to this particular (masked) query out of the 100 options. Providing the teacher with a complete original example represents an upper bound on the auxiliary information the teacher could have. To do a better job at this mapping, we allow the teacher to query the student model, which is useful since it was used to generate the masked query. To conduct the mapping, we then score continuations of the original example and the 100 generated queries, and measure how often the correct query scores the highest. We show that access to such (worst-case) auxiliary information could lead to non-trivial privacy leakage even when the entities are properly masked.

## Methods

We consider three algorithms for how the student could privately learn from the teacher, as shown in Figure 2 . The first of these methods is based on the student describing the problem it is facing while the latter two methods generate similar, non-private examples that the teacher can label. As a hyperparameter for all these methods, we consider the expansion size to denote how many labeled ICL examples the student will receive from the teacher.

## Method 1: Creating a problem description

As an initial approach, we consider a method in which the student analyzes the problem it is given and generates a high-level description from this problem. Even if the student cannot solve the problem, it might be able to describe the type of problem it is facing. This description is the query to the teacher.

The teacher in turn wants to create few-shot examples that the student can use to solve the problem it is facing. Since the teacher has access to a template about the example structure, it knows what format to follow. To create such examples, it then uses this template as well as the student's description to create expansion size many new examples.

## Method 2: Generating new unlabeled examples

Instead of providing the teacher with an abstract description of the problem it is facing, the student can generate a similar, but novel problem itself. As a motivating example for why this is a sensible choice, consider GSM8k (Cobbe et al., 2021) , a math dataset with problems of US middle school difficulty. Given such a math problem, it is possible to create a similar math problem that is just as educational but contains none of the same details, i.e. both problems follow a similar structure and are of similar difficulty. Previous work has shown that LLMs are able to generate new examples from original examples that they see in-context (Shao et al., 2023; Mohtashami et al., 2023) . We additionally observe that for many tasks it is easier to generate new examples than it is to solve them, meaning it is possible for the student model to synthesize similar, unlabeled examples, even if it does not do a good job at labeling them.

To this end, our second method works as follows: We (1) prompt the student LLM to generate expansion size new unlabeled examples. Then, (2) the teacher receives these examples and labels them. Finally, (3) the student learns in-context from that and tries to solve the original problem. Throughout, both teacher and student models utilize the task template to understand what format the labeled and unlabeled examples follow and for where step-bystep explanations make sense.

## Method 3: Replacing entities in original examples

Instead of instructing the student to generate completely novel examples, we can also ask it to keep the same example while replacing names, locations, numbers, and other entities. The student then generates a new unlabeled example that is very similar to the original but that contains none of the private information. Since there are many ways to replace the entities, we can again generate expansion size examples using this technique. While this could be done using a specialized entity detection model and rule-based systems, we observe that LLMs do a fairly good job at this themselves. Thus, we decide to simply prompt the student model to find and replace private entities. The full flow of this method is the same as the method in Section 4.2, except that in step (1), we now simply replace entities instead of generating completely new examples.

## Grouping unlabeled examples to reduce teacher calls

Each call to the teacher implies some chance of leaking private information. This chance needs to be traded off with how much the student can be improved through this process. Like in active learning, the teacher in our setting can thus be considered an expensive resource that needs to be used economically.

To utilize this resource well, we introduce an additional hyperparameter group size that denotes how many private examples the student groups together in order to create expansion size many ICL examples through the teacher. The student considers the entire group jointly when synthesizing descriptions and new unlabeled examples, and is thus able to combine information from the grouped, private examples. By labeling budget = expansion size/ group size, we denote the budget of how many teacher labeled examples may be created for each original example. Note that the student does not get to choose which examples to group together.

## Experiments

In order to evaluate the effectiveness of the methods introduced in Section 4, we evaluate them in terms of accuracy and privacy on a diverse group of datasets and compare them against two baselines. Note that each method generates increasingly specific queries about the student's problem.

Models We use the Gemini 1.0 family of models (Google, 2023) for all of our experiments. As the teacher, we utilize Ultra, the most powerful model of the family. In most of our experiments, Nano-2, a 3.5B parameter model that can be deployed on mobile phones, is the student. The student model capabilities naturally influence the performance of our method and hence we also run experiments when Pro is the student. In line with previous reports on Nano's performance (Google, 2023) , we normalize task success in all our experiments by the teacher's performance since it is an upper bound for what we can hope to achieve.

Datasets We consider a variety of datasets in our experiments to demonstrate that our methods generalize across a suite of tasks: GSM8k math problems (Cobbe et al., 2021) , assistant intent detection (Srivastava et al., 2022) , classifying whether statements are subjective or objective (Conneau and Kiela, 2018) and mid-resource machine translation (Tiedemann, 2020) . See Appendix B for a more detailed description of the datasets.

Baselines We compare against a weak and strong baseline. For the weak baseline, we consider a student that does not communicate with the teacher at all. Since the student does not have any labeled data on its own, it thus falls back to the 0-shot setting while still being able to use the task's template. As the strong baseline, we evaluate a student that has access to 8 arbitrary, golden examples. We consider this to be a strong baseline since these examples are perfectly labeled and for the same task that the student is trying to solve. In practice, such data does often not exist and cannot be easily matched to the student's problem.

## Task Performance

To evaluate our methods, we run experiments for all above mentioned datasets. For ease of comparison, we consider the 8-shot performance of each method. Table 1 shows these results. Across all datasets, we outperform both the weak and strong baseline. However, we note that for GSM8k, getting close to 100% task success, as normalized by the teacher's performance, requires Pro as a strong student model.

We observe that method 3 performs very well across all datasets. Likely this is because the queries generated by this method are the closest to the problem that the student aims to solve. Method 1 performs the worst. We find this method to be the hardest to get to work well since for some tasks, e.g. intent recognition, the student model is only able to explicitly describe the unlabeled example if it is also able to label it, rendering it a less competitive method.

Furthermore, to investigate the best use of the labeling budget = expansion size/ group size, we run full grid searches for the different methods. All values are normalized by the teacher's performance as reported in Table 5 . For easier comparison, we only consider setups with expansion size = 8, group size = 1 here. Note that we report BLEURT (Sellam et al., 2020) for machine translation and accuracy for all other tasks. Appendix D.1 shows similar machine translation results for 6 more languages.

For each labeling budget, we then obtain the best performance that can be reached. As shown in Figure 3 , the choice of these hyperparameters allows budgets below 1, which is not possible without grouping.

## Privacy Results

To analyze how our methods fare in terms of privacy, we compute the two metrics mentioned in Section 3. We find entities in both the original example and in the query by asking Gemini 1.0 Ultra to play an entity detector that finds entities such as names, locations, numbers, and anything else one might consider private. We manually verify on a subset of examples that this does indeed find the desired entities. The results in Table 2 show the results of this analysis. Unexpectedly, we observe that method 1 often leaks the most entities. While this method should generate the most high-level queries in theory, it is hard to get to work well in practice. On a subset of original examples, the student is not able to synthesize a high-level description and instead defaults to detailedly describing the problem it is facing. While the queries of method 3 are the closest to the original messages, they also leak the fewest entities. We hypothesize that this is because the student does not need to understand the problem well in order to find and replace entities. It can simply consider the individual tokens and replace them without needing to understand what kind of problem it is trying to get help on.

However, when analyzing the mapping metric, which describes a worst case of how well an attacker with auxiliary information can identify original examples, the results paint a different picture. Here, method 3 performs significantly worse.

While few entities leak in this method, the structure and writing style are maintained, making it especially easy to map between original and generated example. This is in particular the case for the GSM8k and Subj datasets in which examples have a distinct structure that makes them easy to identify. We find grouping examples to work particularly well with method 2. We observe that with group size = 2 leaks in both metrics significantly reduce, and in the case of GSM8k even without a drop in performance.

Finally, we note that the choice of the right method depends on the concrete threat model considered. While method 1 is neither convincing in terms of quality and privacy, method 3 works remarkably well in situations where the threat model does not involve auxiliary information. Conversely, if one does consider auxiliary information, method 2, potentially with grouping, is the most appropriate to use.

## Qualitative Analysis

In order to better understand where our methods help and where they fall short, we run detailed analyses on the predictions that the student model is able to make after it got help from the teacher. To do this at scale, we ask Gemini 1.0 Ultra to look at the golden label and the student's prediction, and Figure 3 : For a given labeling budget = expansion size/ group size, we show the accuracy reached. Grouping allows us to improve the 29.0% accuracy reached through expansion size = group size = 1 to an accuracy of 32.5% all while just using 1 8 of the budget. Furthermore, even for budgets above 1, we can well outperform the approach without grouping. classify the errors into certain classes. We confirm manually for a subset of cases that these classifications make sense. Table 3 shows the results of this analysis for GSM8k based on 500 examples, for the strong baseline and the best setup for each of our methods. We show similar analyses for machine translation in Appendix D.2, as well as example student queries for all datasets in Appendix F.

## Related Work

LLM Cascades Cascades were mostly studied for improving overall inference costs, particularly given ever-increasing LLM sizes (Hoffmann et al., 2022) . Task performance steadily increases with parameter count (Schaeffer et al., 2023) . Various approaches to cascade inference are compared in (Miao et al., 2023) . Some methods (Li et al., 2021; Chen et al., 2023) use a classifier to determine whether to forward a query or not, while more recent work (Yue et al., 2024 ) leverages a voting and consistency measure of the first model in the cascade as proxy for the inability to provide an answer. We replaced inference cost with a privacy measure optimization and quantified to what degree task performance can be preserved.

Differential Privacy (DP) DP formalizes privacy guarantees in a probabilistic framework (Dwork, 2006) . This can be implemented in various ways, e.g. via the local model of DP (Warner, 1965; Evfimievski et al., 2003; Kasiviswanathan et al., 2011) or as part of in-context learning (Liu et al., 2024; Wu et 2023). While these techniques are useful when computing aggregates across many users, we want our system to work even when a user only has a single, private example, as explain in Section 3.

## Data Minimization

As an alternative to DP, we follow data minimization principles in the form of contextual integrity (Nissenbaum, 2004) . Data minimization techniques are particularly important for removing sensitive information from LLM training datasets. (Lison et al., 2021) present an overview of many techniques relevant to enabling cascade systems in private/public setups. In this work, we investigated the effectiveness of masking operations, and instead of using a separate sequence tagging model we relied on the student LLM capability to perform such transformations. Recent studies, such as (Vats et al., 2023) , have found that pre-training LLMs on datasets processed with privacy-preserving masking does not limit capabilities of models, while privacy benefits are strong.

Social Learning for LLMs (Mohtashami et al., 2023) propose the original framework that we expand here. Notable differences from that are (i) our student model can ask for help from the teacher model, (ii) additional teaching algorithms leveraging in-context learning with improved privacy metrics and (iii) showcasing how social learning can enable cascade systems in setups where they would otherwise not be usable.

## Synthetic Datasets

LLMs are effective at creating bootstrapping datasets, e.g. by creating task instructions through their own conditional gener-ation (Wang et al., 2023) . Similarly, (Lee et al., 2023) have shown how alignment data can be synthesized. The student model needs to have such bootstrapping capabilities and the richer this ability is, the better it produces diverse task transformations that the teacher can better use to explain it back.

## Conclusion

In this paper, we investigated whether LLMs can privately query external LLMs to improve their performance. Indeed, we find that our methods comfortably beat strong baselines that have privacy constraints in place, even with Gemini 1.0 Nano-2 as the student, a 3.5B model that fits on phones.

To evaluate the privacy performance of our methods, we look at two metrics, a simple to interpret count of entities leaked, and another, novel, metric that measures an upper bound of what a curious teacher with auxiliary information could hope to recover from the student's queries. For the first metric, we find masking problems (method 3) to work well, while generating new problems (method 2) with grouping does well in cases where the teacher can be expected to have auxiliary information.

Ultimately, we note that the choice of methods depends on the concrete threat model considered. For either threat model, we present a compelling system and analysis, which show that leakage can be low while beating strong quality baselines. Additionally, we show how grouping examples improves the privacy metrics, and can, under a given labeling budget constraint, even improve model quality.

Future work in this space could consider more complex forms of student-teacher interactions, further improve the privacy metrics established, and look into modalities other than text.

## Limitations

While our work provides a compelling privacy analysis, consisting of an interpretable metrics based on entities and a worst-case, upper bound metric, we do not include methods with privacy guarantees. As discussed in Section 3, we do not find differential privacy to be the right notion here. However, one could consider other ways of potentially adding guarantees in the future.

A further limitation of our work is that we only study a single modality, text. Other modalities could be investigated going forward.

Finally, our work only studies the Gemini family of models. The combination of Nano, Pro and Ultra models provides interesting signal to how well LLMs can get help from other LLMs without revealing private information. However, with more budget to run experiments for different models, the experiments could be repeated for other model families.

When evaluating whether a new dataset is promising to try with our method, we first check these five criteria.

## B More Details on the Datasets

In this section we provide additional details on the four datasets we use. Table 4 shows the templates we use for each dataset.

Grade School Math GSM8k (Cobbe et al., 2021) is a dataset containing grade school math questions, annotated answers as well as step-bystep reasoning on how to reach the answer. Typical GSM8k examples are written in the form of a story with many entities that we do not want the student to reveal to the teacher.

Intent Recognition Cascade systems are especially useful for questions that users pose their personal assistant. Intent Recognition (Srivastava et al., 2022) is a dataset in which one has to classify an utterance as one of 7 assistant as shown in Table 4 .

## Subj

The Subj dataset (Conneau and Kiela, 2018) consists of statements that are either subjective or objective. The model has to classify the statements as one of these two categories.

Machine Translation LLMs show remarkable machine translation performance. Since performance for high-resource languages is difficult to further improve via ICL, we focus on mid-resource machine translation on the Tatoeba (Tiedemann, 2020) dataset.

## C Teacher Task Performance

In Tables 1 and 2 in the main text, we normalize the student's task success by the teacher's performance. In Table 5 , we show this teacher task performance.

## D More Machine Translation Results

## D.1 Task Performance

For brevity's sake, we only show results for one language pair in Table 1 of the main text. Table 6 shows the results for all seven languages we consider. Note that each time we translate from English each time since this allows the student model to synthesize useful queries to the teacher even though it does not understand the target language well. We find our methods to work particularly well for mid-resource languages. Gemini Nano-2 al-ready performs very well on high-resource languages, such as German and Vietnamese, even in the 0-shot setting. Though we do see a small improvement with our methods here, much bigger improvements can be achieved for mid-resource languages.

## D.2 Qualitative Analysis

To better understand in which cases our techniques improve machine translation, we perform a qualitative analysis, similar to the one in Section 5.3. Tables 7 and 8 show the results of these analyses. We find most error types to significantly decrease with our methods, while the incorrect addition or omission of information slightly increases.

## E A Student That Is Copying Instead of Learning In-Context

To evaluate how important ICL is in our setting, we ran additional experiments in which the student copies the teacher's answer instead of learning from it in-context. For the case of expansion size > 1, the student copies the teacher's most common answer.

We start by noting that such an approach does not satisfy the privacy constraint on many tasks. If a student were for example to achieve high task task success on machine translation by simply copying the teacher's answer, this would imply that the teacher learned the most important parts of the student's original data.

Based on this observation, we stick to GSM8k, intent recognition and Subj for this analysis. To enable the student to achieve a good quality by copying, we rely on the masking approach introduced in Section 4.3. However, we additionally instruct the student to replace entities in a way that does not change the result. For the case of GSM8k, this means not replacing any numbers and leaving the relationship between any numbers intact.

We find that ICL outperforms copying in our experiments, as shown in Table 9 . For intent recognition and Subj, copying works fairly well since there are only a few classes to cover. While most of the time, the examples generated by the student all belong to the same class, there are cases where the original example is close to two similar classes. We find ICL to help in these cases.

For GSM8k copying works much worse. This is even the case when using Pro as a significantly larger student. Looking at experiment logs, the Dataset Example Format GSM8k Q u e s t i o n : < q u e s t i o n > Answer : < s t e p -by-s t e p r e a s o n i n g > #### < f i n a l number > Intent Recognition U t t e r a n c e : < u t t e r a n c e > I n t e n t : Machine Translation E n g l i s h s e n t e n c e : < e n g l i s h s e n t e n c e > Basque t r a n s l a t i o n : < b a s q u e t r a n s l a t i o n > 5 : Gemini 1.0 Ultra's task success as the teacher. Even though the teacher itself is not 100% accurate, the student manages to improve through interaction with the teacher in our experiments. We use 0-shot for the teacher in most experiments, but fall back to 8-shot for Subj since this is a difficult task to do in a 0-shot setting.

student in this setup struggles to generate queries that do not affect the result.

Based on these results, we decide to stick to ICL for all other experiments, but use the results to influence our Subj prompt.

## F Example Queries Our Methods Generate

Table 10 shows example student problems and queries that work well. In all of these examples, the student is able to generate a query to the teacher that does not verbatim leak sensitive information but that nevertheless allows the teacher to respond with useful examples.

In Table 11 , we show examples in which the student does not generate a good query. In most of these cases, the student leaks sensitive information. In some, the student generates a query that does not make sense. Emily had $92 to spend at the ice cream shop. She bought 4 ice cream cones, each of which cost $3. How much money does Emily have left?

## GSM8k

Method 3: Masking The Smith family is getting ready for summer and needs to have their swimming pool filled. The pool company instructed them to measure to find the volume of the pool, then to multiply it by 5.9 to calculate how many gallons of water they need. The cost for the pool company to come and fill the pool is $0.10 per gallon. Mr. Smith measured and found the pool is 14 feet wide, 25 feet long, and 4 feet deep. How much will it cost to fill the pool?

The Johnson family is getting ready for summer and needs to have their hot tub filled. The hot tub company instructed them to measure to find the volume of the hot tub, then to multiply it by 6.4 to calculate how many gallons of water they need.

The cost for the hot tub company to come and fill the hot tub is $0.15 per gallon. Mr.

## Figure 1 :

Figure 1: The local model, the student, wants to label its private data. It can query a larger, remote model, the teacher, to get help. The student may not reveal private data to the teacher.

## Figure 2 :

Figure2: The three methods we consider. Steps 1 and 2 show actual student queries and teacher responses as generated in our experiments when using Gemini 1.0 Nano-2 as the student and Gemini 1.0 Ultra as the teacher. Note that each method generates increasingly specific queries about the student's problem.

< a d d _ t o _ p l a y l i s t , b o o k _ r e s t a u r a n t , g e t _ w e a t h e r , p l a y _ m u s i c , s e a r c h _ s c r e e n i n g _ e v e n t , s e a r c h _ c r e a t i v e _ w o r k , r a t e _ b o o k > Subj T e x t : < t e x t > L a b e l : < s u b j e c t i v e , o b j e c t i v e >

## Table 1 :

Task performance with Gemini 1.0 Nano-2 and Pro as students, and Gemini 1.0 Ultra as the teacher.

## Table 2 :

For Nano-2 as the student, and each dataset and method, we present our two privacy metrics. Method 3 generally achieves the best quality results while leaking few entities. Method 2 with grouping offers the strongest privacy metrics.

## Table 3 :

al., An analysis of the student's predictions shows that calculation and reasoning errors of the students reduce through the ICL examples our method provides. Errors caused by using incorrect information slightly increase, likely because the student model can get confused by the similar examples it is seeing. We bold the best cell of each row to emphasize that method 3 shows the most impressive reduction in mistakes. Note that we do not normalize by teacher task success here as opposed to the other tables.

## Table 4 :

The templates for the four datasets we consider. Teacher, student, and baselines can use this information in order to understand how to format examples and where step-by-step reasoning makes sense. This information can either be used in prompts or in constrained decoding configurations.

## Table

## Table 6 :

Machine translation performance (BLEURT) with Gemini 1.0 Nano-2 as the student and Gemini 1.0 Ultra as the teacher. All values are normalized by the teacher's performance. We note that our methods significantly improve results for mid-resource languages while achieving a small improvement for high-resource languages that the student model already understands well.

## Table 7 :

A qualitative error analysis for translation from English to Basque (eu). Lexical, semantic and contextual errors significantly decrease with our methods.

## Table 8 :

A qualitative error analysis for translation from English to Greek (el). Lexical, semantic and grammatical errors significantly decrease with our methods.

## Table 9 :

The student learning in-context always outperforms it simply copying the most common label from the teacher. Both methods use 8-shot.

Johnson measured and found the hot tub is 8 feet wide, 12 feet long, and 3 feet deep. How much will it cost to fill the hot tub

## Table 10 :

Examples where the student generates good queries.

## Table 11 :

Examples in which the student leaks information or does not generate a useful query.
