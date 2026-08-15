---
title: "UIBert: Learning Generic Multimodal Representations for UI Understanding"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2021
date: 2021-08-01
venue: ""
authors: "Chongyang Bai, Xiaoxue Zang, Ying Xu, Srinivas Sunkara, Abhinav Rastogi, Jindong Chen, Blaise Agüera y Arcas"
source_url: https://doi.org/10.24963/ijcai.2021/235
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W3191804539, W3183631962 (type: conference-paper). Full text from the OpenAlex Content API (grobid_xml)."
---

# UIBert: Learning Generic Multimodal Representations for UI Understanding

## Full text

### Abstract (from OpenAlex metadata)

To improve the accessibility of smart devices and to simplify their usage, building models which understand user interfaces (UIs) and assist users to complete their tasks is critical. However, unique challenges are proposed by UI-specific characteristics, such as how to effectively leverage multimodal UI features that involve image, text, and structural metadata and how to achieve good performance when high-quality labeled data is unavailable. To address such challenges we introduce UIBert, a transformer-based joint image-text model trained through novel pre-training tasks on large-scale unlabeled UI data to learn generic feature representations for a UI and its components. Our key intuition is that the heterogeneous features in a UI are self-aligned, i.e., the image and text features of UI components, are predictive of each other. We propose five pretraining tasks utilizing this self-alignment among different features of a UI component and across various components in the same UI. We evaluate our method on nine real-world downstream UI tasks where UIBert outperforms strong multimodal baselines by up to 9.26% accuracy.

---

## Abstract

To improve the accessibility of smart devices and to simplify their usage, building models which understand user interfaces (UIs) and assist users to complete their tasks is critical. However, unique challenges are proposed by UI-specific characteristics, such as how to effectively leverage multimodal UI features that involve image, text, and structural metadata and how to achieve good performance when high-quality labeled data is unavailable. To address such challenges we introduce UIBert, a transformer-based joint image-text model trained through novel pre-training tasks on large-scale unlabeled UI data to learn generic feature representations for a UI and its components. Our key intuition is that the heterogeneous features in a UI are selfaligned, i.e., the image and text features of UI components, are predictive of each other. We propose five pretraining tasks utilizing this self-alignment among different features of a UI component and across various components in the same UI. We evaluate our method on nine real-world downstream UI tasks where UIBert outperforms strong multimodal baselines by up to 9.26% accuracy.

To improve the accessibility of smart devices and to simplify their usage, building models which understand user interfaces (UIs) and assist users to complete their tasks is critical. However, unique challenges are proposed by UI-specific characteristics, such as how to effectively leverage multimodal UI features that involve image, text, and structural metadata and how to achieve good performance when high-quality labeled data is unavailable. To address such challenges we introduce UIBert, a transformer-based joint image-text model trained through novel pre-training tasks on large-scale unlabeled UI data to learn generic feature representations for a UI and its components. Our key intuition is that the heterogeneous features in a UI are selfaligned, i.e., the image and text features of UI components, are predictive of each other. We propose five pretraining tasks utilizing this self-alignment among different features of a UI component and across various components in the same UI. We evaluate our method on nine real-world downstream UI tasks where UIBert outperforms strong multimodal baselines by up to 9.26% accuracy.

As an increasing number of people rely on smart devices to complete their daily tasks, user interface (UI) -the tangible media through which human interacts with the various applications, plays an important role in creating a pleasant user interaction experience. Recently, many UI related tasks have been proposed to improve device accessibilities and assist device operations. For instance, [Li et al., 2020b] studied how to ground natural language commands (e.g. "play next song") to executable actions in UIs, which enables voice control of devices for visual or situational (e.g. driving) impaired users. [Huang et al., 2019] proposed generating UI descrptions which is useful for screen readers like Talkback 1 . Some other tasks aim to help UI designers learn best design practices, e.g. retrieving similar UIs [Huang et al., 2019] or UI elements [He et al., 2020] . All of the above tasks require a comprehensive understanding of the UI, which proposes unique challenges. The first is how to effectively leverage cross-modal knowledge. UI consists of heterogeneous information (Fig. 1 ) such as images, natural language (e.g. texts on the UI), and structural metadata (e.g. Android view hierarchy in mobile apps and Document Object Model in webpages). Especially, the metadata contains rich information about UI layouts and potentially functionality of UI elements that are invisible to the users, yet also suffering from noise [Li et al., 2020b] . Previous work usually utilized single-modality data, e.g. only image, to solve the tasks [Liu et al., 2018; Chen et al., 2020] . How to effectively leverage cross-modal knowledge and diminish the affect of noise for general UI understanding remains an open question. Second, high-quality task-specific UI data is expensive to achieve as it requires complicated setups of app/web crawlers and time-consuming human labeling work [Li et al., 2020c; Swearngin and Li, 2019] , which inevitably slows the model development cycle. When large-scale data is unavailable, it's non-trivial to overcome overfitting and achieve satisfying performance.

Inspired by the recent success of self-supervised learning like BERT [Devlin et al., 2018] and its multimodal variants [Su et al., 2019; Li et al., 2020a] , [He et al., 2020] explored building generic feature representations for UI from unlabelled data that can be applied to various UI related tasks.

Their promising results open up a new-emerging research direction and leave ample space of exploration. As a concurrent work, we also propose a novel transformer-based multimodal approach UIBert (Fig. 2 ) that generates contextual UI representations for solving the aforementioned challenges. But different from He et al. that leverages temporal connectivity of UIs in a UI sequence connected by user actions, we utilize the inter-connectivity between heterogeneous features on a single UI. Specifically, our key intuition is that heterogeneous features on a UI are predicative of each other. For example, in Fig. 1 that presents a UI with its multimodal features, the texts on the UI ("Healthy hollywood", "Restaurants for families"), the carousel images about food and menu, and the content description of Node 2 in the view hierarchy ("Menu picture") are all semantically related and indicate the theme of this UI. Based on it, we design five novel pretraining tasks to leverage the alignment between various UI features. We experimentally show that our approach outperforms the prior work on all the downstream evaluation tasks. Overall, our contributions are:

• We propose UIBert with five novel pretraining tasks, utilizing the image-text correspondence to learn contextual UI embeddings from unlabeled data.

• We evaluate UIBert on nine downstream tasks of five categories, including zero-shot evaluations. UIBert outperforms strong baselines in all tasks. Qualitative evaluations also proves its effectiveness.

• We release two new datasets extended from Rico [Deka et al., 2017] for two tasks: similar UI component retrieval and referring expression component retrieval. Different machine learning models have been proposed to understand UI. For example, [Li et al., 2020b] leveraged Transformer to map natural language commands to executable actions in a UI. [Li et al., 2020c; Chen et al., 2020] used Transformer to generate textual descriptions for UI elements. There were also attempts using convolutional neural networks to retrieve similar UIs for design mining [Deka et al., 2017; Liu et al., 2018; Huang et al., 2019] . Past work generally built task-specific models and required substantial labeled data. In contrast, we focus on learning general knowledge of UI that is applicable for various tasks and leverage large-scale unlabeled data. ActionBert [He et al., 2020] is the most relevant work to us. They proposed training a Transformer that takes the multimodal features generated by separate image and text encoders through well-designed pre-training tasks.

The main difference is that they leveraged the temporal connections between UIs in a UI sequence to design their pretraining tasks while we focus on the self-alignment among different multimodal features in a single UI. Additionally, ActionBert freezes the image and text encoders during pretraining, whereas we use trainable lightweight encoders such as Albert [Lan et al., 2019] and EfficientNet [Tan and Le, 2019] . This enables representation of domain-specific knowledge within encoder parameters.

In this section, we introduce the Android view hierarchy which is one of our model inputs, and summarize the original BERT model from which UIBert is inspired.

View hierarchy. View hierarchy is a tree representation of the UI elements created by Android developers 3 . Each node describes certain attributes (e.g. bounding box positions, functions) of a UI element -the basic building block of UI. An example of a view hierarchy tree can be found on the right of Fig. 1 . Text records the visible text of textual elements on the screen; Content description and Resource-id sometimes contain useful information about the functionality (e.g. navigation, share) which are usually invisible to users. Class name is the categorical Android API class name defined by developers, and Bounds denotes the element's bounding box location on the screen. Note that except for Class name and Bounds, the other fields can be empty. Although view hierarchy is informative, it is noisy [Li et al., 2020b] and is not completely standardized that different view hierarchies can lead to the same screen layout. Therefore, it alone is insufficient to provide a whole image of the UI.

BERT. BERT is a Transformer [Vaswani et al., 2017]

We introduce the details of UIBert starting with its multimodal inputs, then the entire architecture, followed by our proposing pretraining tasks, and lastly qualitative evaluations of the pretrained embeddings.

Given a UI image with its view hierarchy, we first obtain three types of UI components: images (IMG), OCR texts (OCR), and view hierarchy nodes (VH) as shown in Fig. 1 . Below illustrates their definitions and the individual component features we extract, which will be used in the next subsection:

VH components. VH components are leaf nodes 4 of a view hierarchy tree. For each leaf node, we encode the content of its textual fields - The final input to the Transformer is constructed by summing all the above three embeddings, and UIBert generates the final UI embeddings U ∈ R n×d by:

where T, P, C ∈ R n×d and n is the sequence length.

We design five novel pre-training tasks. The first two aim to learn the alignment between UI components of different types (e.g. VH and IMG) by creating unaligned fake UIs and training the model to distinguish them from real ones. The last three are inspired by the MLM task in BERT: for each UI, we choose a single type (IMG, OCR or VH), randomly mask 15% of the UI components of that type , and infer their content from the unmasked ones. Our pretraining dataset consists of 537k pairs of UI screenshots and their view hierarchies obtained using the Firebase Robo app crawler [Firebase, 2020] . We use Adam [Kingma and Ba, 2014] with learning rate 1e-5, β 1 = 0.9, β 2 = 0.999, =1e-7 and batch size 128 on 16 TPUs for 350k steps. The five tasks are defined below. Task 1: Real UI Prediction (RUI). Given an original UI-A, we create a fake version of it, A', by replacing 15% of its UI components with components from UI-B, which is randomly selected from UIs in the same batch. For each UI, initially the type of components to replace is randomly chosen (IMG, OCR or VH). An example is shown in Fig. 3 , where two IMG components in UI-A are replaced by two IMG components from UI-B to yield the fake UI-A'. Note that in this case, we do not change the VH and OCR inputs to the Transformer as we try to make the task harder by having only small difference between the original and fake UI. The RUI task predicts whether a UI is real or not by minimizing the crossentropy (CE) objective:

where y is the binary label for UI x (y = 1 if x is real), and ŷ = Sigmoid(F C(U CLS )) is the prediction probability. U CLS corresponds to the output embedding of CLS token (Fig. 2 ), and F C is a fully connected layer.

Task 2: Real Component Prediction (RCP). We further predict for every fake UI, whether a UI component aligns with the rest or not. In UI-A' of Fig. 3 , only the two IMG components that are switched from UI-B are fake, whereas all OCR and VH components and the rest of IMG components are real.

Intuitively, the content of a fake component not align with the rest of the components and the model needs to learn from the context to make the correct prediction. The objective of RCP is the sum of the weighted cross-entropy loss over all UI components in a fake UI:

where y i is the label of the i th component, and ŷi is the prediction made by a linear layer connected to the UI embedding U i . The weight λ is multiplied to the loss for fake components to address the label imbalance. We use λ = 2 in our case.

Task 3: Masked Image Prediction (MIP). We randomly mask 15% of the IMG inputs by replacing its content embeddings with 0s and its type feature with MASK. This task aims to infer the masked IMG inputs from its surrounding inputs for each real UI. Prior work on multimodal pretraining also designed similar tasks, but most of them try to predict either the object class (e.g. tree, sky, car) [Li et al., 2020a] or the object features [Su et al., 2019] of the masked image patches, which are obtained by a pre-trained object detector. However, such methods highly rely on the accuracy of the pretrained object detector and is unsuitable for our case, as there is no existing object detector specifically trained with UI data to detect all the generic UI components. Thus, we try to predict the masked IMG inputs in a contrastive learning manner (Fig. 2 ): given the content embedding of the original IMG component (positive) with the content embeddings of some negative distracting IMG components sampled from the same UI, the output embedding of the masked positive is expected to be closest to its content embedding in terms of their cosine similarity scores. Formally, let M IMG be the set of masked IMG indices in a real UI. We employ the softmax version of Noise Contrastive Estimation (NCE) loss [Jozefowicz et al., 2016] as the objective:

(5) where N (i) is the set of negative IMG components for i. In practice, we use the k closest IMGs to the masked component i in the image as the negative components. Task 4: Masked OCR Generation (MOG). When masking OCR inputs, as each OCR component is a sequence of words, we frame the prediction of the masked OCR as a generation problem -a 1-layer GRU decoder [Chung et al., 2014] takes the UI embedding of the masked OCR component as input to generate the original OCR texts. We use a simple decoder as our goal is to learn powerful UI embeddings. Since it can be hard to generate the whole sequence from scratch, we mask tokens of a masked OCR component with probability of 15% (e.g. only "Restaurants" is masked in the OCR component "Restaurants for families" in Fig. 2 ). Denote t i = (t i,1 , . . . t i,ni ) as the WordPiece [Wu et al., 2016] tokens of OCR component i where t i,j , ∀j is the one-hot encoding of the jth token, and ti = GRU (U i ) = ( ti,1 , . . . ti,ni ) as the predicted probability of the generated tokens, the MOG objective is framed as the sum of multi-class cross-entropy losses between the masked tokens and generated ones:

where M OCR denotes the set of (compomnent id, token id) pairs of the masked OCRs.

Task 5: Masked VH Generation (MVG). For VH components, we observe that Resource-id is usually short that contains only two to three tokens and Text field overlaps with OCR texts. Hence, we only mask the Content description and Class name. For each masked VH component, we generate its Content description using the same GRU decoder as for the MOG task, and predict the Class name label by a fully connected layer with a softmax activation. Formally,  where M VH is the set of masked VH components, c i is the one-hot encoding of the Class name label of VH component i, ĉi = Softmax(F C(U i )) is the predicted probability vector, t i,j , ti,j represent the original and predicted content description tokens following the same definition as the OCR tokens.

In practice, content descriptions of UI components can be used by screen reading tools to hints for people with vision impairments, yet prior work shows that more than 66% buttons are missing content description [Chen et al., 2020] . We show in Sec. 4.4 that UIBert pre-trained with the MVG task can generate meaningful descriptions and has great potential to assist screen readers.

Overall, the pretraining loss objective for a UI is

where 1 {.} is the indicator function.

To verify the effectiveness of our pretraining tasks, we visualize the UI embeddings of a pre-trained UIBert, and showcase the generated content descriptions without any fine-tuning.

Embedding visualization. We use t-SNE [Maaten and Hinton, 2008] to visualize U CLS of the UIs that belong to the top-5 common app types and the embeddings of UI components of the top-5 common icon types in Rico [Deka et al., 2017] , which is a public mobile design dataset containing 72k unique UI screenshots with view hierarchies crawled across 9.7k mobile apps. We observe that embeddings of the same app types or icon types are grouped together, suggesting that UIBert captures meaningful UI-level and component-level features.

Content description generation. We generate content descriptions for the synchronized UIs in the public RicoSCA dataset [Li et al., 2020b] (details in Sec. 5.4). We mask all the content descriptions in the input and generate them following the same settings in the MVG task. As shown in examples of Fig. 5 , most of the generated descriptions are correct. Some are incorrect but reasonable (case 5). Overall, 70% of the generated content descriptions are the same as the ground truth.

As UIBert is designed to learn generic contextual UI representations transferable to various UI understanding tasks, we also conduct experiments to evaluate its performance on downstream tasks. We choose nine practical downstream tasks across five categories, including two zero-shot tasks.

Our finetuning approach introduces minimal task-specific parameters and finetunes all the parameters end-to-end. For each finetuning task, we train the model for 200k steps with dropout rate of 0.1, and use the same optimizer configuration and batch size as that in pretraining. In the following, we first describe the baselines to compare with, then the details of each downstream task including definition, datasets, experimental setups and results.

We consider two baseline encoding mechanisms for the downstream tasks: EfficientNet+Albert and ActionBert. The first one uses EfficientNet-B0 [Tan and Le, 2019] and Albert [Lan et al., 2019] to encode the image and text components of the UI separately. The obtained embeddings are then concatenated and fed into the same prediction head as used in UIBert for downstream tasks. As there is no attention across the two modalities, it serves as an ablation evaluation for the Transformer blocks used in UIBert which facilitate this cross-modal attention. The second baseline, ActionBert [He et al., 2020] 5 , is a recently proposed UI representation model, pretrained with user interaction traces.

In this task, given an anchor UI with an anchor component as query and a seacrh UI with a set of candidate components, the goal is to select the closest candidate to the anchor component in terms of the functionality (Fig. 6 (a)). Models for this task can assist UI designers to find best design practices. For example, upon creating a new UI, the designer can refine any component by retrieving similar ones from a UI database. One dataset for this task is extended from Rico [Deka et al., 2017] which serves as a database of mobile app UIs. It consists of 1M anchor-search UI component pairs annotated  To adapt UIBert to this task, the anchor UI and search UI are fed into UIBert separately to get the output embeddings, then the dot products between embeddings of anchor component and candidate components are used as similarity scores to select the most similar candidate to the anchor. We finetune UIBert using the multi-class cross entropy loss on the similarity scores. Since no additional model parameters are needed, the task is also evaluated in a zero-shot manner by directly using the pretrained model. To adapt the Efficient-Net+Albert baseline, we use the OCR text on each anchor and search component as the text features that are into Albert.

Overall, prediction accuracy of all methods on the four task variations are reported in Tab. 1. We observe that UIBert outperforms both baselines on all cases by 0.85%-9.26%, especially by a large margin on the zero-shot tasks.

Given a referring expression and a UI image, the goal of this task is to retrieve the component that the expression refers to from a set of UI components detected on the screen (Fig. 6(b) ). This task has a practical use for voice-control systems [Wichers et al., 2018] in Rico as well. The referring expressions are collected by crowdsourcing. On average, the model is required to choose from 20 UI component candidates for each expression. The train, dev, and test sets respectively contain 16.9k, 2.1k and 1.8k UI componenets with their referring expressions.

To apply UIBert to this task, we treat the referring expression as an OCR component and UI component candidates as IMG components that UIBert takes as input. Dot products of the output embedding of the expression and the output embeddings of the candidate components are computed as their similarity scores to select the referred candidate. The prediction results are shown in Tab. 2. UIBert achieves the best accuracy 90.81%, which outperforms ActionBert by 2.43%.

View hierarchies can be noisy when they are unsynchronized with screenshots ( [Li et al., 2020b] ). This task takes the UI screen with its VH as input and outputs whether the VH matches the screen. It can serve as an important preprocessing step to filter out the problematic UIs. We use the RicoSCA ( [Li et al., 2020b] ) that have 25k synchronized and 47k unsynchronized UIs and split them into train, dev, and test sets by a ratio of 8:1:1.

We use the UI embedding of the CLS component followed by a one-layer projection to predict whether the image and view hierarchy of an UI are synced. Tab. 2 shows that UIBert outperforms the baseline and achieves 79.07% accuracy and 77.06% macro-F1.

This task aims to predict the type of an app (e.g. music, finance) of a UI. We use all the 72k unique UIs in Rico across a total of 27 app types and split them in the ratio of 8:1:1 for train, dev, and test. This task can help filter the malicious apps that have incorrect app types.

For this task, we also use a one-layer projection layer to project the UIBert embeddings to one of the app types. We experiment using the output of CLS component and a concatenation of the embeddings of all the UI components. The preliminary experiments show that the latter yields better results. As shown in Tab. 2, UIBert outperforms the Efficient-Net+Albert baseline by 4.50% accuracy and 4.72% Macro-F1, showing the gain from the attention mechanisms of the Transformer block and from pretraining.

This task aims to identify the types of icons (e.g. menu, backward, search), which is useful for applications like screen readers. We use Rico data with human-labelled icon types for every VH leaf node in two levels of granularity: 32 and 77 classes [He et al., 2020] . To predict the types of an icon component, we concatenate the UI embeddings of the icon's corresponding IMG and VH components and feed them into a fully connected layer. As shown Tab. 3, UIBert consistently outperforms baselines in both accuracy and F1 score.

We propose UIBert, a transformer-based model to learn multimodal UI representations via novel pretraining tasks. The model is evaluated on nine UI related downstream tasks and achieves the best performance across all. Visualization of UI embeddings and content descriptions generated by the pretrained model further demonstrated the efficacy of our approach. We hope our work facilitates the model towards generic UI understanding.

Figure 1: Heterogeneous features in a UI.

Figure 2: UIBert overview. It takes Fig 1 as the input. Content, type, and positional embeddings are computed and summed as the input to the Transformer. The output UI embeddings U , is used for pre-training and downstream tasks. Note that we randomly choose one type of components (IMG, OCR, or VH) to mask in pretraining but to save space, the figure shows the case when we mask all three types in one UI.

Figure 3: Fake UI generation. 15% of the components in UI-A are randomly chosen (red boxes) and replaced by the same amount of random components in UI B (yellow boxes) to get A'.

Figure 4: Zero-shot embedding visualization of UIs of top-5 common apps and UI components of top-5 common icon types using t-SNE. Best viewed in color.

Figure 5: Examples of the generated content descriptions by a pretrained UIBert (correct in blue and incorrect in red).

Figure 6: a) An example of similar UI component retrieval. b) An example of referring expression component retrieval.

2

2 https://github.com/google-research-datasets/uibert 2 Related Work

based language representation model, which takes as input a sequence of word piece tokens pre-pended with a special [CLS] token. BERT defines two pretraining tasks: Masked language model (MLM) that learns the word-level embeddings by inferring randomly masked tokens from the unmasked ones, and next sentence prediction (NSP) that learns the sentence-

level[CLS]embedding by predicting if two input sentences are consecutive. Inspired by it, UIBert adapts MLM to three and NSP to two novel pretraining tasks to learn generic and contextualized UI representations.

[MLKit, 2020]2019] components are image patches cropped from the UI based on the bounding boxes denoted in the VH components.We use EfficientNet[Tan and Le, 2019]of which the last layer is replaced by spatial average pooling to get the component feature of each IMG component.OCR Components.OCR components are texts detected by a pretrained OCR model[MLKit, 2020]on the UI image, which is in most cases complementary with the content in the VH components.We generate its component features using the same Albert model as is used for encoding the VH components.Type embedding. To distinguish input components of diverse types, we introduce six type tokens: IMG, OCR, VH, CLS, SEP, and MASK. MASK is a special type used for pretraining which is discussed in the next subsection. A one-hot encoding followed by linear projection is used to get the type embedding, T i ∈ R d , for the i th component in the sequence where d is the dimension size that is 512 in our case.

[Lan et al., 2019]ription, Resource-id, and Class name that are described in Section 3 into feature vectors.As a preprocessing step, we normalize the content of Class name by heuristics to one of the 22 classes (e.g.TEXT VIEW, IMAGE VIEW, CHECK BOX, SWITCH) and split content of resource-id by underscores and camel cases.Normalized Class name is then encoded as a one-hot embedding, while the content of other fields are respectively fed into a pretrained Albert[Lan et al., 2019]to obtain their sentencelevel embeddings.All the obtained embeddings are concatenated as the final component feature of the VH component.Positional embedding.We encode the location feature of each component using its bounding box, which consists of normalized top-left, bottom-right point coordinates, width, height, and area of the bounding box.Similar to type embeddings, a linear layer is used to project the location feature to the positional embedding, P i ∈ R d , for the i th component (P i = 0 for CLS and SEP).Content embedding. We linearly project the extracted component features (Sec. 4.1) to the content embedding C i ∈ R d , for every i th input with type(i) ∈ {IMG, OCR, VH} and use 0s for the inputs of other types.

Prediction accuracy (%) on four variations of the similar UI component retrieval task. On average, the model chooses one from 10 and 35 candidates in the Rico and web data respectively. via crowd-sourcing and programmatic rules. We use 900k pairs for training, 32k pairs for dev, and 32k pairs for test. On average, each search UI has 10 candidate components for the model to choose from. Another dataset for this task includes 65k anchor-search web UI pairs. search web UI has 35 components on average. Note that as view hierarchies are unavailable in web UIs, there is no VH component input to UIBert during finetuning.

. Our dataset of this task is based on UIs Prediction results on three downstream tasks (from left to right): image-VH sync prediction, app type classification, and referring expression component retrieval. F1 denotes Macro-F1.

Prediction results on two icon classification tasks.

Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence

https://developer.android.com/reference/android/view/View Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21)

Other nodes are discarded as they usually describe a collection of UI elements.

We use ActionBertBASE due to its comparable size to UIBert. Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21)

App type cls results are different from that reported in[He et  al., 2020], which only used a subset (43.5k out of

72k) of Rico data.

The authors thank Maria Wang, Gabriel Schubiner, Lijuan Liu, and Nevan Wichers for their guidance and help on dataset creation and processing; James Stout and Pranav Khaitan for advice, guidance and encouragement; all the anonymous reviewers for reviewing the manuscript and providing valuable feedback.
