---
title: "Evidence for hypodescent in visual semantic AI. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (pp"
person: mahzarin-banaji
section: by
type: book-chapter
year: 2022
date: 2022
venue: "1293-1304)"
authors: "Wolfe, R., Banaji, M. R., & Caliskan, A"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/Wolfe_CLIP_Hypodescent_FAccT_2022.pdf
doi: 
openalex_id: 
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard publications page (banaji.sites.fas.harvard.edu), extracted with pdftotext -layout. Title-overlap check 0.69. Not matched to an OpenAlex work record in this pass. Full citation as listed on her site: Wolfe, R., Banaji, M. R., & Caliskan, A. (2022). Evidence for hypodescent in visual semantic AI. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (pp. 1293-1304). DEDUP: duplicate file built from the OpenAlex record removed; this file carries the longer extraction."
---

# Evidence for hypodescent in visual semantic AI. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (pp

## Full text

Evidence for Hypodescent in Visual Semantic AI
                    Robert Wolfe                                     Mahzarin R. Banaji                                Aylin Caliskan
             University of Washington                                 Harvard University                          University of Washington
                 Seattle, WA, USA                                    Cambridge, MA, USA                               Seattle, WA, USA
                 rwolfe3@uw.edu                                   mahzarin_banaji@harvard.edu                          aylin@uw.edu

ABSTRACT                                                                          Accountability, and Transparency (FAccT ’22), June 21–24, 2022, Seoul, Repub-
We examine the state-of-the-art multimodal "visual semantic" model                lic of Korea. ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/
                                                                                  3531146.3533185
CLIP ("Contrastive Language Image Pretraining") for the rule of hy-
podescent, or one-drop rule, whereby multiracial people are more
likely to be assigned a racial or ethnic label corresponding to a                 1    INTRODUCTION
minority or disadvantaged racial or ethnic group than to the equiv-               Recent progress in multimodal "visual semantic" artificial intelli-
alent majority or advantaged group. A face morphing experiment                    gence (AI) has produced CLIP ("Contrastive Language Image Pre-
grounded in psychological research demonstrating hypodescent in-                  training"), the first language-and-image model that allows the def-
dicates that, at the midway point of 1, 000 series of morphed images,             inition of image classes in natural language and generalizes to
CLIP associates 69.7% of Black-White female images with a Black                   datasets on which it was not explicitly trained [56]. For the field of
text label over a White text label, and similarly prefers Latina (75.8%)          computer vision, CLIP was able to realize many of the benefits of
and Asian (89.1%) text labels at the midway point for Latina-White                large-scale self-supervised pretraining first seen in natural language
female and Asian-White female morphs, reflecting hypodescent.                     processing (NLP). While its designers primarily evaluate CLIP in
Additionally, assessment of the underlying cosine similarities in                 the context of image classification [56], features derived from the
the model reveals that association with White is correlated with as-              model have been used to train zero-shot object detection models
sociation with "person," with Pearson’s ρ as high as 0.82, p < 10−90              and zero-shot image generation AI [23, 60]. Investigations of biases
over a 21, 000-image morph series, indicating that a White per-                   in CLIP have uncovered under-representation of women in image
son corresponds to the default representation of a person in CLIP.                retrieval tasks [70], the presence of biased and offensive content in
Finally, we show that the stereotype-congruent pleasantness as-                   an open-source training corpus similar to the one on which CLIP
sociation of an image correlates with association with the Black                  was trained [6], and semantic biases (e.g., association of Muslims
text label in CLIP, with Pearson’s ρ = 0.48, p < 10−90 for 21, 000                with terrorism), in multimodal neuron activations in the CLIP image
Black-White multiracial male images, and ρ = 0.41, p < 10−90 for                  encoder [20]. In this research, we investigate whether the manner
Black-White multiracial female images. CLIP is trained on English-                in which CLIP forms categorical boundaries between images of
language text gathered using data collected from an American web-                 humans reflects a particular racial bias: the rule of hypodescent, or
site (Wikipedia), and our findings demonstrate that CLIP embeds                   one-drop rule.
the values of American racial hierarchy, reflecting the implicit and                 In the paper introducing CLIP, Radford et al. [56] report that
explicit beliefs that are present in human minds. We contextualize                in the zero-shot setting, CLIP associates with a White text label
these findings within the history of and psychology of hypodescent.               only 58.3% of people with the White racial label in the FairFace
Overall, the data suggests that AI supervised using natural language              dataset [35], while associating 91.3% of individuals belonging to
will, unless checked, learn biases that reflect racial hierarchies.               the six other racial and ethnic groups represented in FairFace with
                                                                                  their FairFace label. While the FairFace dataset consists of visually
CCS CONCEPTS                                                                      noisy in-the-wild photographs, and relies not on self-identification
• Computing methodologies → Artificial intelligence.                              of race but on the potentially biased labels of human perceivers
                                                                                  (Amazon Mechanical Turkers), the results of Radford et al. [56]
KEYWORDS                                                                          indicate that a substantial minority of people who are perceived by
multimodal, bias in AI, visual semantics, language-image models,                  other humans as White are associated with a race other than White
racial bias, hypodescent                                                          by CLIP. The inverse does not appear to be true, as individuals
                                                                                  who are perceived to belong to other racial or ethnic labels in the
ACM Reference Format:                                                             FairFace dataset are associated with those labels by CLIP. This
Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan. 2022. Evidence for          result suggests the possibility that CLIP has learned the rule of
Hypodescent in Visual Semantic AI. In 2022 ACM Conference on Fairness,            "hypodescent," as described by social scientists: individuals with
                                                                                  multiracial ancestry are more likely to be perceived and categorized
                                                                                  as belonging to the minority or less advantaged parent group than
                                                                                  to the equally legitimate majority or advantaged parent group. In
This work is licensed under a Creative Commons
Attribution-NonCommercial-ShareAlike International 4.0 License.                   other words, the child of a Black and a White parent is perceived to
                                                                                  be more Black than White; and the child of an Asian and a White
FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea                             parent is perceived to be more Asian than White. Psychological
© 2022 Copyright held by the owner/author(s).
ACM ISBN 978-1-4503-9352-2/22/06.                                                 research finds that a rule of hypodescent reflects a belief in racial
https://doi.org/10.1145/3531146.3533185                                           hierarchy, and maintains and enhances the racial status quo [31].


                                                                           1293


FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea                                                                         Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan


                                                           Mean Cosine Similarity of Text Label to Image - Black-White Male Morph Series


                   Mean Cosine Similarity
                                                                                                                                     Black Label
                                             0.3                                                                                    White Label
                                                                                                                                    Person Label
                                            0.28

                                            0.26
                                                   1   2     3    4   5    6   7   8    9   10 11 12 13 14 15 16 17 18 19 20 21
                                                                                            Morph Index

Figure 1: Across 5% increments in mixing ratio between Black source images (index 1) and White target images (index 21),
the mean probability of a White text label and the mean probability of a person text label are nearly equivalent and nearly
invariant. On the other hand, the mean probability of the Black text label varies with the mixing ratio of the images, indicating
that White is the default race in CLIP, with other racial and ethnic groups defined based on difference from White.


   We systematically test for evidence of hypodescent in CLIP.                                    (3) Valence bias (association with bad or unpleasant vs.
This is, to our knowledge, the first analysis of hypodescent in AI.                                   good or pleasant concepts) correlates with association
We make research code public at https://github.com/wolferobert3/                                      with the minority group. For each morph series, the SC-
evidence_for_hypodescent. Three main results are highlighted:                                         WEAT [9] is used to measure the association of each em-
                                                                                                      bedded image with unpleasant vs. pleasant concepts in the
                                                                                                      CLIP embedding space, represented using 25 valenced words
   (1) CLIP shows hypodescent, or the one-drop rule, by bi-                                           each (e.g., grief, agony, disaster vs. love, peace, cheer). The
       ased association of images of multiracial people with                                          cosine similarity of each image with the minority race or
       minority ancestry. Faces of individuals who self-identified                                    ethnicity text label is obtained. For the 21, 000-image Black-
       as Black, Asian, and Latino/a were morphed into faces of                                       White male morph series, the association with unpleasant
       people who self-identified as White. At the halfway point                                      concepts for an embedded image correlates with the image’s
       of the morph series, the critical juncture, CLIP associates                                    association with the Black label, with Pearson’s ρ = 0.48,
       the majority of the morphed images with a Black, Asian,                                        p < 10−90 . The correlation is similar for the Black-White
       or Latino/a text label rather than a White text label. Hy-                                     female morph series, with ρ = 0.41, p < 10−90 .
       podescent is more pronounced for images of women: at the
                                                                                               Although this work will discuss racial categories such as Asian,
       halfway point, 69.7% of Black-White female multiracial im-
                                                                                               Black, Latino, and White, we use them in the manner in which the
       ages are associated with Black; 75.8% of Latina-White female
                                                                                               social and psychological sciences use them, i.e., to refer to social
       multiracial images are associated with Latina; and 89.1% of
                                                                                               constructions, not biological realities [3].
       Asian-White female multiracial images are associated with
       Asian. 53.8% of Black-White male multiracial images at the                              2     RELATED WORK
       halfway point are associated with Black. We do not observe
       hypodescent for the Asian-White male or for the Latino-                                 This research draws on multiple strands of previous research on
       White male morph series.                                                                hypodescent, CLIP and multimodal AI, and bias in AI.
   (2) White is the default race in CLIP, with other racial and                                Hypodescent. Hypodescent refers to the association of people who
       ethnic groups defined by their deviation from White.                                    have multiracial ancestry with the race of their minority parent
       For each morph series, we obtain Pearson’s ρ for the co-                                group. The way multiracial individuals are perceived by others is of
       sine similarity of a "person" label (with no text indicating                            sociopolitical importance, as it can serve as an indication of whether
       race or ethnicity) and the cosine similarity of White, Black,                           intermarriage and miscegenation will result in the disturbance of
       Asian, and Latino/a text labels. In all cases, the correlation                          racial hierarchy1 [33]. For example, if a society has a high number
       between person and White is higher (ρ ∈ [0.60, 0.82]) than                              of multiracial births, those at the top of a racial hierarchy may
       the correlation between person and Asian, Black, or Latino                              make the hierarchy durable to demographic change by categorizing
       (ρ ∈ [0.11, 0.40]), indicating that the most similar represen-                          multiracial individuals as belonging to a minority racial or ethnic
       tation to a person is a White person in CLIP. As shown in                               group [33]. The minority group increases in size, but can be denied
       Figure 1, the mean cosine similarity for the White label at                             privileges providing access to life’s opportunities and outcomes,
       each step of the morph series is nearly invariant, and nearly                           ranging from housing and loans, to education and jobs, to treatment
       indistinguishable from that of the person label. On the other                           by law and law enforcement [29].
       hand, the mean cosine similarity of the Black label varies as                           1 The term "racial hierarchy" is common in the social and psychological literature, and

       the mixing ratio of the source and target images changes,                               is the term we will employ here. Others such as Wilkerson [71] have characterized
                                                                                               the racial ordering of political and economic advantages in America as a caste system.
       such that images are associated with Black based on devia-                              In referring to racial hierarchy, we do not intend to lend legitimacy to this system, but
       tion from the White default.                                                            to draw attention to the ways it operates to prevent its encoding in AI.


                                                                                       1294


Evidence for Hypodescent in Visual Semantic AI                                                        FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea


   The primary psychological reference for the present research             extending Blackness to multiracial people with Black ancestry "be-
is the work of Ho et al. [33], who uncovered evidence for a rule            cause they perceive that Black–White biracials face discrimination
of hypodescent in human perceivers based on measures of both                and consequently feel a sense of linked fate with them." Peery and
relatively more implicit and explicit cognition [33]. To study the          Bodenhausen [55] finds that automatic (reflexive/implicit) racial
implicit bias of hypodescent, Ho et al. [33] used a face morphing           categorizations by White perceivers reflect hypodescent, but that
experiment, wherein the face of a Black person or an Asian per-             "more complex racial identities may be acknowledged upon more
son (subjectively strongly judged to be so) is "morphed" across             thoughtful reflection." Zarate and Smith [79] find that white per-
a series of images into a face of a White person. They find that            ceivers classify members of their own race more quickly, and that
human perceivers are more likely to classify intermediate images            speed of categorization is linked to attribution of racial stereotypes.
according to minority ancestry, reflecting a rule of hypodescent                While hypodescent has been observed for both males and fe-
[33]. Moreover, they show that perceivers presented with the family         males, Ho et al. [33] observed stronger effects for men than women.
tree of a multiracial person with one Black or Asian parent and             This is consistent with research by Sidanius and Pratto [64] and
one White parent were more likely to classify that person as Black          Navarrete et al. [51], who find that histories of intergroup con-
or Asian, respectively, than as White [33]. Ho et al. [33] find that        flicts involving primarily male aggressors have resulted in stronger
biases of hypodescent are more significant for multiracial people           exclusionary biases toward outgroup males. The disparity in hy-
with Black ancestry, but are also observed for multiracial people           podescent patterns observed in experimental psychology may be a
with Asian ancestry, a result reflecting the existence of American          result of broader intersectional gender biases, wherein Black faces
racial hierarchy [29]. As described in the Section 4, our research          are less readily classified as female [19], and male faces are more
design draws insight from the work of Ho et al. [33] to test for the        likely to be classified as Black [10]. We are not aware of studies
bias of hypodescent in AI. If the result of Ho et al. [33] is limited       examining hypodescent beyond a gender binary.
to a bias in human minds, it should not be observed in the analy-           American Context of Hypodescent. A notable result that has
ses performed using visual semantic CLIP associations. If, on the           emerged from the present work is that hypodescent in AI resem-
other hand, hypodescent is reflected in the CLIP embedding space,           bles hypodescent in human cognition, as observed by experimental
the result will add to a growing body of research demonstrating             psychologists. Our work focuses on hypodescent in an American
the manner in which human biases are transduced into machine                context, for two reasons: because most modern psychological re-
learning architectures.                                                     search of hypodescent studies American subjects and locates find-
   In a subsequent study of the psychological underpinnings of              ings within the American context [78]; and because CLIP is trained
hypodescent and racial hierarchy, Ho et al. [31] find that a rule of        on English-language internet data, the majority of which is based on
hypodescent is employed when a minority group makes signifi-                a query list collected from an American website (English-language
cant gains in social realms such as business and politics (a threat         Wikipedia) [56], suggesting that what CLIP has learned about hy-
condition to the racial status quo), and that individuals high in           podescent is likely to be best understood within the American
social dominance orientation (an individual difference measure of           context. The historical context of hypodescent in the United States -
preference for group-based hierarchies [32]) are more likely to cate-       as a mechanism for expanding slavery [4], for enforcing segregation
gorize multiracial individuals according to a minority parent group.        [29], and for preserving the stability of racial hierarchy [47] - has
Ho et al. [31] find that hypodescent can be seen as a "hierarchy-           been noted by psychologists as a likely factor in modern Americans’
enhancing" social categorization, in that it amplifies perception of        implicit biases with regard to the race of multiracial individuals
racial differences such that racial boundaries and advantages are           [33].
preserved despite changing demographics and social structures.              CLIP and Visual Semantic AI. We now describe the technical
More recently, Krosch et al. [38] find that White perceivers who            architecture of CLIP, the AI model we will test for evidence of hy-
read about impending demographic shifts which will render the               podescent. CLIP was designed to be the first "zero-shot" image clas-
U.S. a majority-minority country are more likely to characterize            sifier, meaning that it has learned to associate images in computer
multiracial faces as belonging to a minority group, reflecting a rule       vision datasets with their text labels without seeing the training
of hypodescent.                                                             data provided for those datasets [56]. This constituted a significant
   Other psychological studies have suggested that hypodescent is           step forward in computer vision and multimodal AI, as CLIP ad-
related to attention and to frequency of observation. Halberstadt           vanced the zero-shot state-of-the-art on ImageNet from 11.5% [44]
et al. [26] suggest that hypodescent is related to selective attention,     to 76.2% [56]. CLIP is known as a "visual semantic" or "multimodal"
wherein humans pay more attention to physical characteristics               AI model, in that it encodes text and images and projects them into
infrequently and first observed later in life, such that people who         the same embedding space, such that the text most similar to an
possess a mixture of majority-group and minority-group traits are           image can be matched to it by measuring the cosine similarity of
perceived as belonging to the minority group. This has particu-             the encoded text and the encoded image [56]. While CLIP has been
lar salience for computer vision, given prior research that finds           discussed primarily in terms of its performance as a zero-shot image
that people who have darker skin tones, and in particular women             classifier, the model learns "transferable" visual features, meaning
who have darker skin tones, are significantly underrepresented in           that the representations formed by CLIP can be easily adapted for
computer vision training datasets [8]. Lewis [43] finds that people         many computer vision tasks, such as image retrieval [70], and can
who have more experience seeing Black faces are more likely to              be used to train specialized zero-shot computer vision models for
classify multiracial faces as belonging to a White person. Ho et al.        tasks such as object detection [23] and image generation [53, 60].
[30] find that Black perceivers may use hypodescent inclusively,            Moreover, the word and sentence representations formed by CLIP


                                                                     1295


FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea                                                        Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan


have been shown to be highly semantic, to the point that they set            subjects in the Implicit Association Test (IAT) [22]. The WEAT was
or match state-of-the-art on intrinsic evaluations [75].                     expanded to uncover racial, gender, and intersectional biases in
    CLIP jointly trains a computer vision model (a ResNet [27] or            contextualized word embeddings formed by language models like
a Vision Transformer (ViT) [17]) and a contextualizing language              BERT and GPT-2 [25, 76], and in the generative computer vision
model (a smaller version of GPT-2 [57]), and projects representa-            model Image GPT [65]. Our research is most similar to these studies,
tions from each model into the same embedding space. Both GPT-2              in that we test an AI model for a bias well-known in psychology.
and ViT are based on the transformer architecture, a deep learn-             GANs for Bias Assessment. Our study builds on prior work which
ing network which uses self-attention to draw information from               uses GAN-generated synthetic images to study bias in AI. Denton
anywhere in its input window [69]. CLIP’s success in generalizing            et al. [15] use a generative adversarial network (GAN) to generate
across datasets is the result of applying a novel training objective         series of counterfactual images for analyzing unintended biases in
to an internet-scale language-and-image corpus. CLIP trains on the           facial analysis AI. Li and Xu [45] use series of images produced by a
WebImageText (WIT) corpus, a collection of 400 million images and            GAN to discover unknown biases in image classifiers. Ramaswamy
their associated captions scraped from the internet [56]. While WIT          et al. [58] use a GAN to generate synthetic training data which
is not publicly available, Radford et al. [56] note that it contains         is more balanced based on protected attributes such as race and
roughly as many words as the text corpus used to train GPT-2. The            gender. Most recently, Lang et al. [40] train a GAN to explain the
query list for WIT consists of all words occurring at least 100 times        decisions of an image classifier by discovering the visual attributes
in English language Wikipedia, bigrams from Wikipedia which                  which lead to its predictions.
have high pointwise mutual information, the names of Wikipedia               Racial Bias in Computer Vision. Buolamwini and Gebru [8] find
articles, and all WordNet synsets not included in the list [56]. CLIP        that state-of-the-art AI facial recognition systems fail to detect the
employs a "contrastive learning" pretraining objective, which maxi-          faces of women with darker skin, and that this problem is traceable
mizes the cosine similarity of an encoded caption with its encoded           to the underrepresentation of women and people with darker skin
image while minimizing its cosine similarity with all of the other           in widely used facial recognition datasets. Wilson et al. [72] finds
encoded images in the batch [56, 67]. When this research refers to           that this problem is not limited to facial recognition, and that state-
an image or text embedding, this means the multimodal representa-            of-the-art object detection systems also perform poorly for people
tion formed by CLIP after projection to this joint embedding space.          with darker skin. Moreover, emotion detection AI systems have
Our supplementary materials include a discussion of advances in              been shown to disproportionately detect unpleasant emotions such
deep learning visual semantic AI beginning with its origins in 2013.         as anger in emotionally ambiguous or neutral images of members
    This research tests for hypodescent in CLIP by comparing the             of minority racial or ethnic groups [61].2 Steed and Caliskan [65]
cosine similarities of embedded images and embedded text labels              show that Image GPT, which generates image completions given a
corresponding to four racial or ethnic groups, an approach which             visual prompt [12], implicitly associates images of Black individuals
reflects the typical zero-shot use of the model during inference [56].       with images of weapons.
Biases observed in the embedding space will be reflected in the              Racial Bias in NLP. May et al. [49] find evidence of sentence-
many zero-shot settings in which CLIP is used, including image               level racial bias in language models, while Sheng et al. [63] show
retrieval [70], image classification [56], and other settings which          that the text output of language models like GPT-2 contains biases
may benefit from transferable visual features. We examine the                demonstrating low regard for members of marginalized groups,
CLIP-ViT-Base-Patch32 model, which was downloaded from the                   including racial minorities. Wolfe and Caliskan [74] find that under-
Transformers library [73] more than one million times during the             representation of women and marginalized racial and ethnic groups
month prior to this writing alone, accounting for more than 98% of           in the training corpora of language models produces representations
the downloads of any CLIP model from the library.                            more likely to be biased and overfit to stereotypical pretraining
Bias in AI. Social biases related to gender [7], age [37], religion [1],     contexts. Dodge et al. [16] show that filtering algorithms used to
and sexuality [63] have been observed in AI systems. Our review              construct the C4 training corpus remove information by and about
of the extensive related work in this area focuses on racial bias in         people belonging to marginalized populations.
AI and on biases observed in CLIP.                                           Bias in CLIP. Radford et al. [56] and Agarwal et al. [2] catalogue
Implicit Bias and AI. CLIP offers the first opportunity to study             social biases in CLIP, including that images of people who are
implicit biases in machine-learned visual semantic representations.          labeled as Black in the FairFace dataset [35] are the most likely to be
Where a supervised algorithm is provided with explicit class labels,         mislabeled as animals. In highlighting multimodal neurons in CLIP
CLIP is provided, like word embeddings and language models, with             which respond to photographic, symbolic, or textual depictions of
text (and accompanying images) collected from the internet. While            a concept, Goh et al. [20] find that the activation of these neurons
unsupervised and self-supervised algorithms free machine learning            reflect stereotypes, such as association of terrorism with Muslims.
from using a relatively small number of human-curated labels, and            Birhane et al. [6] find that LAION-400m [62], a multimodal image-
allow for the expansion of training datasets without the need for            and-language dataset similar to CLIP’s training corpus, contains
supervised labeling, unsupervised models learn the social biases of          2 There are ethical questions related to whether technologies like facial recognition and
the data on which they are trained [5, 9]. The most direct adaptation        emotion detection are beneficial, as they are used for purposes of surveillance and social
of an implicit bias measurement to machine learned representations           control [42], and recent research focuses on ways to circumvent mass surveillance
is the Word Embedding Association Test (WEAT) of Caliskan et al.             [24]. Where such systems are used, the research of scholars such as Buolamwini and
                                                                             Gebru [8] makes clear the over-representation of men and people who have lighter
[9], which replicated in word embeddings an array of widely shared           skin in AI training data, and the failure of commercial AI systems to perform equally
human associations and social biases previously observed in human            for women and for people who have darker skin.


                                                                      1296


Evidence for Hypodescent in Visual Semantic AI                                                                             FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea


racial and ethnic slurs and stereotypes, along with images of sexual
violence and other obscene adult content.

3     DATA
We use the Chicago Face Database (CFD), a dataset of images pro-
duced for studies of race in psychology [48]. The CFD includes 597                           Figure 2: Images of the five middle steps (40-60% mixing ra-
high-resolution (2, 444 x 1, 718 pixel) images of male and female                            tio) of a Black-White male GAN-generated morph series.
study volunteers, with labels (Asian, Black, Latino/a, and White)
based on self-identified race or ethnic group [48]. The subjects of
the photos faced the camera, and images are standardized such                                the GAN, we train on the source image and the target image. We
that they are all set against a White background, with the face                              use the default hyperparameters of StyleGAN2-ADA, and train for
occupying the same area of the image. CFD subjects were recruited                            125 steps per image, beyond which we observe no benefit given the
in the United States. The CFD includes photos of all subjects with                           high-resolution, standardized images we provide to the GAN. This
a "neutral" facial expression, and of a subset with "happy (open                             produces a source embedding, and a target embedding, for which we
mouth)," "happy (closed mouth)," "angry," and "fearful" facial expres-                       use the generator to produce the first and last images in the series.
sions. The experiments of Ho et al. [33] used images of subjects                             For the rest of the morph series, we take the difference between
with a neutral facial expression, and for consistency we use only                            these two embeddings and divide it by the number of intermediate
the images with neutral facial expressions for this research.                                images to be produced.4 At each step, we add the divided difference,
GAN-Generated Images. Consistent with the research design of                                 and create a new image using the generator. This creates a series
Ho et al. [33], who produce face morphs between racial or ethnic                             of 21 high-resolution (1,024x1,024 pixel) synthetic images, such as
groups in 5% increments, we morph faces of people who self-identify                          those seen in Figure 2. Our supplementary materials include an
as Black, Asian, and Latino/a into faces of people who self-identify                         example of a morph series for each source and target group pair.
as White in the CFD. Specifically, for each morph series, an image of                           A projected image embedding is obtained from CLIP for each of
a person who self-identifies as Black, Asian, or Latino/a is selected,                       the 21 images in each morph series. Then, projected text embed-
and nineteen intermediate images are generated which blend fa-                               dings reflecting the self-identified race or ethnicity of the source
cial features between that image and the image of a person who                               group image, the self-identified race or ethnicity of the target group
self-identifies as White. At each morph step, the morphed image                              image, three multiracial group labels ("multiracial," "biracial," and
becomes less similar to the image of the person who self-identifies                          "mixed race"), and a "person" label (with race omitted) are obtained
as Black, Asian, or Latino/a, and more similar to the person who                             from CLIP. Following the prompt of Radford et al. [56], who recom-
self-identifies as White. Using a 21-step series allows the definition                       mend using "a photo of [[image class]]" for best performance with
of 75%, 50%, and 25% mixture ratios between the source and target                            zero-shot CLIP, we use "a photo of a [[race or ethnicity]] person"
images at the 6th , 11th , and 16th morph indices respectively.                              as the text input to the model for each of the text labels.
   For each pair of racial or ethnic groups, we produce 1, 000 unique                           Note that we do not morph faces across genders. That is, we
morph series to ensure the statistical significance of our results. Let                      morph images of men into men, and images of women into women.
n denote the number of images for a "source" racial or ethnic group                          The reasons for this are three-fold: first, psychological research has
in the Chicago Face Database, i.e., for the group which serves as                            tested morphs of men into men and women into women, and we are
the initial image in the morph series, rather than the final image in                        able to compare our results to prior work in this light. Second, prior
the morph series. For each image in the source group, we randomly                            research indicates that the rule of hypodescent is applied more to
select ⌈ 1,000                                1,000                                          men than to women, and we intend to test this hypothesis with
           n ⌉ (i.e., the largest integer ≥     n ) images from the
target group to serve as final images in the morph series. This                              CLIP. Third, our experiments test for a bias based on race, rather
method enables maximum variety in the morph series. Because this                             than gender. It is unclear whether gender-related stimuli changing
produces slightly more than 1, 000 morph series per paired source                            across a series of morphs would introduce noise which distorts the
and target group, we randomly downsample to 1, 000 morph series                              model’s association based on race. Future research designs might
(a total of 21, 000 images) per pair to ensure uniformity between                            study how CLIP’s biases change when gender stimuli vary along
morph series comparisons. To produce highly realistic images, we                             with racial stimuli.
use StyleGAN2-ADA3 pretrained on the FFHQ dataset [36]. Images
are normalized by cropping around the face, such that facial features                        4    APPROACH AND EXPERIMENTS
appear in positions similar to the positions of the facial features                          We conduct three experiments. The first tests whether CLIP as-
in the pretraining dataset. Failing to do this produces distorted                            sociates images of multiracial people with minority ancestry, ac-
and distended faces bearing little similarity to either of the images                        cording to a rule of hypodescent. The second tests whether CLIP
between which the morph occurs. To produce morph series using                                embeds White as a default racial group. The third tests a relation-
                                                                                             ship between valence association (good vs. bad) and association
3 A GAN may itself exhibit bias based on its training dataset; for example, if images of     with a minority group label.
White individuals are overrepresented in the training data, the GAN may lighten the          Test of Hypodescent. At each step in the morph series, we mea-
skin tone of generated images, or produce noisy or lower quality images of individuals
with physical characteristics underrepresented in the training dataset [34]. We note         sure the percentage of morphed images for which the image’s cosine
that inspection of several thousand generated images by multiple domain experts
suggests inter-annotator reliability of these series for quantifying bias.                   4 Steps for morphing between images are derived from the work of Heaton [28].


                                                                                      1297


FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea                                                  Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan


similarity with the minority group label is higher than with the             Unpleasant: abuse, crash, filth, murder, sickness, accident, death,
White label. If hypodescent is reflected in CLIP, we would expect            grief, poison, stink, assault, disaster, hatred, pollute, tragedy, divorce,
that the majority of images which blend source features and target           jail, poverty, ugly, cancer, kill, rotten, vomit, agony, prison
features most equally (i.e., those in the middle of the morph series)           In addition to measuring the standardized difference in valence
would be more similar to the embedded text corresponding to the              between two groups of target words (e.g., European-American
disadvantaged group. We also characterize the skewness of each               names and African-American names), the WEAT is also able to
distribution of associations, defined as m3/2
                                            3
                                              , with the biased ith cen-     measure the valence of a single target stimulus using the single-
                                         m2
                                                                             category WEAT (SC-WEAT). We adapt the SC-WEAT to measure
tral moment given by mi = N1 1N (x[n] − x̄)i , and x̄ referring to the
                                 Í
                                                                             the valence of a visual semantic representation of an encoded image,
sample mean. Skewness measures of the symmetry of a distribution:            rather than a word. The formula for the SC-WEAT is:
negative skewness indicates that the distribution of associations
leans toward the minority racial or ethnic group, while positive
skewness indicates a distribution that leans toward White.                                   meana ∈A cos(i®, ®                     ®
                                                                                                              a) − meanb ∈B cos(i®, b)
Test of White as a Default Race. For the 21, 000 images of each                                                                                        (1)
                                                                                                    std_devx ∈A∪B cos(i®, ®
                                                                                                                          x)
morph series (1, 000 images at each morph step), we obtain the
cosine similarity with the source (Asian, Black, or Latino/a) group          where i® refers to the multimodal image representation, and A and B
text label, the White text label, and a person label with no race or         refer to multimodal text representations of sets of attribute words.
ethnicity included. We then take Pearson’s ρ between the cosine              The SC-WEAT returns an effect size, Cohen’s d [13], and a p-value
similarities for the person label with those for the minority group          denoting statistical significance. We obtain Pearson’s ρ between the
label, and with those for the White label. If CLIP encodes White as          SC-WEAT effect size (association with unpleasant vs. pleasant) for
a default race, we would expect to observe stronger correlations             the 21, 000 images, with the cosine similarities between the images
between White and person than between other racial or ethnic                 and a text label corresponding to the minority racial or ethnic
groups and person. Next, we take the mean cosine similarity at               group (i.e., the degree of association with the minority group). For
every morph index (corresponding to a 5% morph increment) for                this experiment, a positive effect size denotes association with
each racial or ethnic group label with the 1, 000 GAN-generated              unpleasantness, such that a positive correlation denotes association
images at that morph index. Mean cosine similarity can be thought            of a minority racial or ethnic group with unpleasantness, and a
of as the average association with a text class at a morph step. To          negative correlation denotes association with pleasantness.
validate that results using the mean are representative of the full              By relying on visual, face-based stimuli, our research overcomes
series, we report the standard deviation of 21, 000 cosine similarities      the limitation imposed by words, as there is little question about
for each text label. If CLIP encodes White as a default race, we would       whether a face is a face or not, whereas words may contain multiple
expect to observe correspondence between the cosine similarity for           meanings. Moreover, both research on word embeddings and hu-
White and person, with other racial and ethnic groups defined in             man subjects research using pictorial stimuli can use only limited
relation to White.                                                           inputs, typically 8 faces or 25 words, to represent social groups [14].
Test of Relationship Between Valence and Race or Ethnicity.                  Using the current methodology expands the stimulus input to be
The third analysis focuses on the association of race or ethnicity           two orders of magnitude greater than the inputs used in previous
with valence (good or pleasant vs. bad or unpleasant), which is              research with humans or word embeddings. If the present analy-
fundamental to any psychological analysis of social cognition and            ses support previous small-scale input studies, the inferences that
social interaction [22, 54]. Previous research has shown that static         can be drawn about the strength and generality of group valence
word embeddings encode the concept of Black (represented us-                 associations will be significantly strengthened.
ing 25 African-American names) such that it is more associated               Validating the SC-WEAT for Visual Semantics. The WEAT and
with unpleasantness than the concept of White (represented us-               SC-WEAT are well-established methods for measuring biases in lin-
ing 25 European-American names), a result of training on large               guistic representations [9, 25, 74, 76], and have been adapted to mea-
language corpora scraped from the internet [9]. This result con-             sure bias in image embeddings by Steed and Caliskan [65]. As this
firmed demonstrations of human implicit social cognition showing             is the first application of the SC-WEAT to a visual semantic model,
evidence that even those individuals who report no racial bias nev-          we test that using the SC-WEAT produces human-interpretable re-
ertheless demonstrate automatic association of Black with bad and            sults. For each image included in the OASIS norms, a dataset of 900
White with good [22]. The WEAT, and the IAT before it, measure               images which includes labels reflecting the human-rated valence
racial bias using two sets of attribute words: one good or pleasant          of each image [39], we obtain an SC-WEAT effect size measuring
group, and one bad or unpleasant group. These groups correspond              the pleasantness of the image’s embedding in CLIP. Comparing
to the psycholinguistic property of valence, or the pleasantness             the SC-WEAT effect sizes with the human-rated valence norms
or unpleasantness of a stimulus [54]. Below are the pleasant and             yields Pearson’s ρ = 0.77, p < 10−30 , on par with similar semantic
unpleasant attribute words used in the IAT and the WEAT, which               evaluations of the best static and contextualized word embeddings
we also employ:                                                              on valence-labeled linguistic lexica of comparable size [68, 76]. This
Pleasant: caress, freedom, health, love, peace, cheer, friend, heaven,       means, concretely, that CLIP associates images depicting war, sick-
loyal, pleasure, diamond, gentle, honest, lucky, rainbow, diploma,           ness, and so on with unpleasantness; and images related to nature,
gift, honor, miracle, sunrise, family, happy, laughter, paradise, vaca-      family, and so on with pleasantness, and that the SC-WEAT can be
tion                                                                         used to detect these associations.


                                                                      1298


Evidence for Hypodescent in Visual Semantic AI                                                                                   FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea


                                                                         Association with Minority Ancestry for Morphs by Race and Gender


                  % Associated with Minority Group
                                                     100

                                                      80

                                                      60           Black-White Female
                                                                   Asian-White Female
                                                      40           Latina-White Female
                                                                    Black-White Male
                                                      20            Asian-White Male
                                                                    Latino-White Male
                                                       0
                                                           1   2     3    4    5    6    7   8   9   10 11 12 13 14 15 16 17 18 19 20 21
                                                                                                 Morph Image Index

Figure 3: Across 5% increments in mixing ratio between source (minority group) images at index 1 and target (White) images
at index 21, CLIP associates a majority of images with the minority group until the image is only 20% similar to the source
group for Asian-White and Latina-White Female morph series, and 40% similar to the source group for the Black-White Female
morph series, indicating evidence of hypodescent for Female images. 53.5% of Black-White Male images are associated with
Black at the 50% point.


5    RESULTS                                                                                            to the target (White) image), 53.8% of the time at 50% MR, and 42.5%
Our results provide evidence for hypodescent in the CLIP embed-                                         of the time at 45% MR. Hypodescent is not observed at 50% MR for
ding space, a bias applied more strongly to images of women. Re-                                        the Asian-White male or Latino-White male morph series. Female
sults further indicate that CLIP associates images with racial or                                       morph series reflect stronger biases of hypodescent, with 89.1% of
ethnic labels based on deviation from White, with White as the                                          Asian-White female morphed images associated with Asian at 50%
default. Finally, an image’s valence association correlates with its                                    MR, 69.7% of Black-White female morphed images associated with
association with a minority racial label. For readability, some tables                                  Black at 50% MR, and 75.8% of Latina-White female morphed images
below refer to series of Asian-White morphed images as "A-W,"                                           associated with Latina at 50% MR. The Black-White female morph
of Black-White morphed images as "B-W," and of Latino/a-White                                           series yields a majority of Black associations until 40% MR, while
morphed images as "L-W."                                                                                the Asian-White and Latina-White morph series yield a majority
                                                                                                        of Asian and Latina associations, respectively, until 20% MR. Full
                                                                                                        results for 25%, 45%, 50%, 55%, and 75% MR steps are provided in
          Minority Group Associations by Mixing Ratio
                                                                                                        Table 1, and association curves across the six morph series are
     Morph Series            75% 55% 50% 45% 25%
                                                                                                        visualized in Figure 3.
     Asian-White Female      98.6 92.9 89.1 84.6 52.7
     Black-White Female      97.6 79.7 69.7 58.2 18.6                                                                       Skew by Morph Series
     Latina-White Female 92.2 81.5 75.8 71.4 50.3                                                                 Female Series Skew Male Series Skew
     Asian-White Male        84.4 55.3 47.2 40.1 11.1                                                             A-W Female     -0.84  A-W Male      0.00
     Black-White Male        96.5 67.5 53.8 42.5 10.8                                                             B-W Female     -0.30  B-W Male -0.06
     Latino-White Male       77.4 52.7 45.2 39.2 19.9                                                             L-W Female     -0.42   L-W Male     0.12
Table 1: At 50% mixing ratio, the point denoting equal sim-                                             Table 2: Skew is negative for the distribution of minority
ilarity between the source (Asian, Black, or Latino/a) and                                              group vs. White label associations across all three Female
target (White) images, CLIP associates a higher percentage                                              morph series and the Black-White Male morph series. This
of 1, 000 morphed Female images with Asian (89.1%), Latina                                              reflects an asymmetry which leans toward the minority
(75.8%), and Black (69.7%) text labels than with a correspond-                                          group, indicating hypodescent.
ing White label, indicating hypodescent. Hypodescent is
also observed for Black-White Male images (53.8% at 50%
mixing ratio), but not for Asian-White Male or Latino-White
                                                                                                        Four of the morph series exhibit negative skewness, indicating
Male images.
                                                                                                        asymmetry in the distribution of associations which leans toward
                                                                                                        a racial minority group label. Table 2 shows that results also reflect
                                                                                                        a stronger bias of hypodescent for women than for men, with a
Evidence for hypodescent in CLIP. For the 1, 000 morph series                                           largest male series skew of -0.06 (Black-White male series), and a
of 21 images each between Black males and White males, CLIP                                             largest female series skew of -0.84 (Asian-White female series). The
assigns a higher cosine similarity to the Black text label 67.5% of                                     smallest female series skew is -0.30 (Black-White female series).
the time at a 55% mixing ratio (MR) (i.e., step 9 out of 20, wherein                                    Evidence that White is the Default Racial Group in CLIP. As
the image is 55% similar to the source (Black) image and 45% similar                                    shown in Table 3, the correlation between the cosine similarity


                                                                                                 1299


FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea                                                                       Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan


                                            Mean Cosine Similarity of Text Label with 1, 000 Images Per Index of Black-White Male Morph Series


                 Mean Cosine Similarity
                                           0.3

                                          0.28
                                                           Black Label
                                          0.26             White Label
                                                         Multiracial Label
                                                          Biracial Label
                                          0.24           Mixed Race Label

                                                 1   2   3     4     5       6   7   8   9     10 11 12 13 14 15 16 17 18 19 20 21
                                                                                         Image Morph Index

Figure 4: Across 5% increments in mixing ratio between Black source images (index 1) and White target images (index 21), the
mean cosine similarity of Multiracial, Biracial, and Mixed Race labels varies with the mixing ratio of the images in a similar
manner as the Black label, instead of increasing to a maximum value at index 11 (50% mixing ratio), as would be expected if
CLIP were detecting a mix of racial features. The Mixed Race label is preferred at the intermediate steps of the morph series.

                        Correlation (Pearson’s ρ) of race or ethnicity label with "person" label (over 21, 000 images)
            Racial or Ethnic Group            A-W Female B-W Female L-W Female A-W Male B-W Male L-W Male
            Source Racial or Ethnic Group              0.13            0.33           0.21          0.11         0.40  0.33
            White                                      0.81            0.75           0.82          0.60         0.74  0.64
Table 3: Over 21, 000 images, the cosine similarity of the White label and the images strongly correlates with the cosine simi-
larity of the person label and the images, with Pearson’s ρ up to 0.82. Correlation does not exceed 0.40 for any other label.


                            Standard Deviation of Cosine Similarities with 21, 000 Images by Morph Series
           Racial or Ethnic Group Label A-W Female B-W Female L-W Female A-W Male B-W Male L-W Male
           Source Group                           0.025         0.019            0.013       0.028       0.019   0.014
           White                                  0.008         0.010            0.008       0.007       0.008   0.007
           Person (Race Omitted)                  0.006         0.008            0.006       0.006       0.006   0.006
Table 4: The standard deviation of associations between the White label and a series of 21, 000 images is smaller than for any
other race or ethnicity. This indicates that the probability of the White label, like the person label, is nearly constant across
the steps of the morph series, suggesting that White is a default race against which other races and ethnicities are defined.


of an image with person and cosine similarity of an image with                                      Mixed Race text label rather than with Black or White, as shown in
White is higher in all morph series than the correlation between the                                Figure 4. This result corresponds well to the research of Peery and
cosine similarity of an image with person and with a minority racial                                Bodenhausen [55], who found evidence of hypodescent as an auto-
group. Correlations are for 21, 000 images each, and p-values are                                   matic, reflexive bias, but also found that humans acknowledge more
< 10−50 in all cases. While the mean cosine similarities with 1, 000                                complex racial identities when presented with option to choose
encoded images at each morph step vary according to mixing ratio                                    them. However, cosine similarity with the Multiracial, Biracial, and
for minority racial and ethnic groups, the mean cosine similarity of                                Mixed Race text labels does not increase uniformly from both sides
the White text label with encoded images is nearly invariant across                                 to a maximum at morph index 11 (50% mixing ratio), as might be
the morph series, and nearly indistinguishable from the person text                                 expected if the label denoted that the model has perceived a blend
label. Table 4 captures standard deviation by text label for 21, 000                                of features. Rather, these labels have higher mean cosine similar-
images in all six morph series, and shows that standard deviations                                  ity when the images are more similar to Black source images, and
for the White label fall within [0.007, 0.010], while standard devia-                               lower mean cosine similarity as images are more similar to White
tions for Black, Asian, and Latino/a labels fall within [0.013, 0.028],                             target images. That CLIP prefers the Mixed Race label of the three,
with all Black and Asian labels ≥ 0.019. Standard deviations are                                    and assigns lower probability to Multiracial than even the default
small because cosine similarity ranges from 0 to 1, and has a narrow                                White label, may be a consequence of the model being trained on
span for one kind of image (faces).                                                                 internet image captions, such that more colloquial descriptions are
   Adding Multiracial, Biracial, and Mixed Race labels reveals that,                                preferred.
on average, the model associates intermediate morph steps with the


                                                                                             1300


Evidence for Hypodescent in Visual Semantic AI                                                                           FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea


               Mean Valence WEAT (Cohen’s d)
                                                         Mean Unpleasant Valence Association by Morph Index - Black-White Male Series
                                               0.7
                                                                                                      Unpleasantness Bias in BM-WM Morph Series
                                               0.6

                                               0.5

                                               0.4
                                                     1   2   3   4   5   6   7   8   9    10 11 12 13 14 15 16 17 18 19 20 21
                                                                                     Image Morph Index

Figure 5: Images more similar to the Black Male source images (index 1) are more associated with unpleasantness than images
similar to the White Male target images (index 21). Correlation between the mean association with the "Black" label and mean
valence association across the morph series is Pearson’s ρ = .97, p < 10−12 . This indicates that multiracial people are subject to
valence bias in CLIP, and suggests a link between the model’s perception of an image as "Black" and its automatic association
with unpleasantness.


Evidence that Valence Correlates with Minority Group Asso-                                      images ranges between -0.30 (Black-White female series) and -0.84
ciation. As depicted in Figure 5, mean valence association (associ-                             (Asian-White female series). The three female morph series do not
ation with bad or unpleasant vs. with good or pleasant) varies with                             see a majority of associations with White until 40% mixing ratio
the mixing ratio over the Black-White male morph series, such that                              (Black-White series) or 20% mixing ratio (Asian-White and Latina-
CLIP encodes associations with unpleasantness for the faces most                                White series). We describe a few possible causes for a primary effect
similar to CFD volunteers who self-identify as Black. As shown                                  based on gender. First, Radford et al. [56] observe that CLIP directs
in Table 5, for the 21, 000 images of the Black-White male morph                                more attention to the physical features of women (such as hair),
series, Pearson’s ρ between valence association and the cosine sim-                             likely the result of training captions which describe women in terms
ilarity of an image with the Black text label is 0.48, p < 10−90 ; ρ                            of physical appearance. Such attention to physical features may
between mean valence association and mean cosine similarity with                                render CLIP more sensitive to what the model perceives as race in
the Black label at each morph step is ρ = 0.97, p < 10−12 . A similar                           women. On the other hand, Halberstadt et al. [26] have suggested
effect is observed for the Black-White female morph series, with                                that hypodescent in human subjects is related to attention, such
ρ = 0.41, p < 10−90 over 21, 000 images. The negative correlations                              that a perceiver notices deviation from the physical features most
for Asian-White morph series indicate that Asian faces are more                                 frequently observed. Prior research in computer vision and in NLP
associated with pleasantness relative to White faces.                                           finds that women with darker skin [8] or who are Black, Asian,
                                                                                                or Latina [74] are underrepresented in machine learning training
   Correlation of Minority Group Label with Unpleasantness                                      data. Hypodescent as it pertains to women may thus be related to
   Female Series    Pearson’s ρ Male Series     Pearson’s ρ                                     underrepresentation in CLIP’s WIT training corpus.
   A-W Female      -0.22 (10−90 )   A-W Male -0.43 (10−90 )                                     The evidence indicates that CLIP encodes White as a default
   B-W Female       0.41 (10−90 )   B-W Male 0.48 (10−90 )                                      race. This is supported by the stronger correlations between White
   L-W Female       0.05 (10 )
                            −13     L-W Male       0.01 (.26)                                   cosine similarities and person cosine similarities than for any other
Table 5: The valence association of an image correlates with                                    racial or ethnic group, with Pearson’s ρ ∈ [0.60, 0.82]. Standard
the probability that it will be associated with a minority                                      deviations for both person and White labels are also much lower
group text label. Most significantly, the unpleasantness as-                                    than for Asian, Black, or Latino/a labels. This accords with the near
sociation of an image increases with the probability that the                                   invariance of the means of the White label across all steps of the
model will associate the image with Black, with Pearson’s                                       morph series, such that images are associated with a minority racial
ρ = 0.48, p < 10−90 across 21, 000 images for the Black-White                                   or ethnic group based on deviation from White. That White is a
Male morph series.                                                                              default race in CLIP is further supported by image associations
                                                                                                with Multiracial, Biracial, and Mixed Race text labels, which do not
                                                                                                increase from both sides of the series to a peak at 50% mixing ratio,
                                                                                                but are higher when the image is similar to an image of a Black
                                                                                                person, and lower when more similar to a White person.
6    DISCUSSION                                                                                 The evidence indicates that the valence of an image corre-
The evidence indicates a rule of hypodescent, or one-drop                                       lates with racial association, with Pearson’s ρ = 0.48, p < 10−90
rule, in CLIP. The effect occurs in four of six morph series, and is                            for images in the Black-White male series. More concretely, our
more pronounced for images of women than images of men, such                                    results indicate that the more certain the model is that an image
that the largest negative skew for male images is -0.06, for the Black-                         reflects a Black individual, the more associated with the unpleasant
White male morph series, while the skew of associations for female


                                                                                         1301


FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea                                                     Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan


embedding space the image is. We note three consequences of this            ease of use, modern AI applications may, on an unprecedented scale,
result. First, it indicates that multiracial people whom the model          affect the way human beings perceive other human beings.
associates more strongly with Black are subject to valence biases           Limitations and Future Work. This research examines only one
in visual semantic AI. Second, it suggests that an implicit bias - of       visual semantic model, which prevents assessment of whether our
Black individuals with unpleasantness - is linked to the perception         results generalize across architectures. CLIP is the first in a new
of race in visual semantic AI. This accords with research of Zarate         generation of multimodal AI, and until late December 2021 was the
and Smith [79], who found that the speed of racial categorization by        only English-language zero-shot visual semantic model available
human perceivers is linked to the attribution of racial stereotypes         open source for scientific study. Further work will be necessary to
to a subject. Third, this result affirms the results of smaller studies     test hypodescent in new zero-shot visual semantic models such as
of implicit bias in word embeddings and in human subjects.                  SLIP [50], and in other CLIP architectures. Moreover, CLIP creates
Observing a correlation between pleasantness and probability of             highly contextual text representations, and using different labels
the Asian text label may correspond to the "model minority" stereo-         may produce different results. We employ a principled method
type, wherein people of Asian ancestry are lauded for their upward          by adhering to the prompt outlined by Radford et al. [56], and
mobility and assimilation into American culture, and even associ-           operationalizing only the racial and ethnic categories specified in
ated with "good behavior" [77]. This is likely a stereotype held in         the CFD. 2019 Google N-Gram frequency statistics indicate that
conjunction with Asian individuals being perceived and marked               these are also by far the most common ways to describe each racial
as outsiders [41], and the strong negative response during the pan-         or ethnic group in all English N-Gram sources [46]. Nonetheless,
demic [66]. While this is consistent with CLIP’s association of faces       using different text prompts is likely to affect associations in the
of Asian people relative to the White default group, further work           model, and might be explored in future work. Future work might
is needed to confirm the underlying positive association to Asian           also use a GAN-based approach such as that of Lang et al. [40] to test
and its dissociation from acts of discrimination.                           what characteristics of an image directly influence hypodescent and
Impact on AI. As indicated by the title of the paper introducing            valence bias. Such a study might test our hypothesis that increased
CLIP, the model is designed to learn "transferable" visual features,        attention to physical features results in stronger bias of hypodescent
i.e., features which can be used in a wide variety of settings and          for women, a finding which varies from studies of hypodescent in
applications [56]. One of these uses is to serve as ground truth for        human perceivers, for which hypodescent is observed more strongly
creating other specialized multimodal models: among the first uses          for men [33, 51, 64].
of CLIP was to train the zero-shot image generation model DALL-
E [56, 60]. A larger, non-public version of the CLIP architecture           7    CONCLUSION
was used in the training of DALL-E 2 [59]. Commensurate with the
findings of the present research, the Risks and Limitations described       The primary result of the present research is the demonstration
in the DALL-E 2 model card note that it "produces images that tend          of hypodescent in a state-of-the-art visual semantic AI system.
to overrepresent people who are White-passing" [59]. Such uses              Additionally, the results reflect that women are more likely to be
demonstrate the potential for the biases learned by CLIP to spread          classified according to a rule of hypodescent, that White is a default
beyond the model’s embedding space, as its features are used to             race in the model, and that stereotype-congruent pleasantness bias
guide the formation of semantics in other state-of-the-art AI models.       correlates with association with Black. This work adds to a body of
Moreover, due in part to the advances realized by CLIP and similar          literature showing that AI encodes the implicit and explicit biases
models for associating images and text in the zero-shot setting,            of the society and language on which it trains.
multimodal architectures have been described as the foundation for
the future of widely used internet applications, including search           ACKNOWLEDGMENTS
engines [52]. Our results indicate that additional attention to what        This material is based on research partially supported by the U.S. Na-
such models learn from natural language supervision is warranted.           tional Institute of Standards and Technology (NIST) Grant 60NANB-
Impact on the Sciences. Our results suggest that visual semantic            20D212T. Any opinions, findings, and conclusions or recommenda-
AI models like CLIP may prove useful tools for studying societal-           tions expressed in this material are those of the authors and do not
level biases. For example, word embeddings have been used to                necessarily reflect those of NIST.
study the consistency of gender stereotypes across child and adult
language corpora [11], as well as changes in gender and ethnic
stereotypes over one hundred years [18]. Visual semantic AI may
                                                                            REFERENCES
                                                                             [1] Abubakar Abid, Maheen Farooqi, and James Zou. 2021. Persistent anti-muslim
facilitate similar scientific research enabling the study of human               bias in large language models. arXiv preprint arXiv:2101.05783 (2021).
biases which can be observed in the statistical relationship between         [2] Sandhini Agarwal, Gretchen Krueger, Jack Clark, Alec Radford, Jong Wook Kim,
language and images.                                                             and Miles Brundage. 2021. Evaluating CLIP: Towards Characterization of Broader
                                                                                 Capabilities and Downstream Implications. arXiv preprint arXiv:2108.02818
Impact on Society. As human interaction with AI systems be-                      (2021).
comes more common, hypodescent and valence bias in visual se-                [3] American Medical Association et al. 2020. New AMA policies recognize race as
                                                                                 a social, not biological, construct. Published November 16 (2020).
mantic AI may affect the human perception of multiracial individu-           [4] Carlos A Ball. 2007. The Blurring of the Lines: Children and Bans on Interracial
als. Greenwald et al. [21] find that implicit racial biases in humans            Unions and Same-Sex Marriages. Fordham L. Rev. 76 (2007), 2733.
can "explain discriminatory impacts that are societally significant ei-      [5] Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret
                                                                                 Shmitchell. 2021. On the Dangers of Stochastic Parrots: Can Language Models Be
ther because they can affect many people simultaneously or because               Too Big?. In Proceedings of the 2021 ACM Conference on Fairness, Accountability,
they can repeatedly affect single persons." Given their ubiquity and             and Transparency. 610–623.


                                                                     1302


Evidence for Hypodescent in Visual Semantic AI                                                                               FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea


 [6] Abeba Birhane, Vinay Uday Prabhu, and Emmanuel Kahembwe. 2021. Multimodal               [31] Arnold K Ho, Jim Sidanius, Amy JC Cuddy, and Mahzarin R Banaji. 2013. Status
     datasets: misogyny, pornography, and malignant stereotypes. arXiv preprint                   boundary enforcement and the categorization of black–white biracials. Journal
     arXiv:2110.01963 (2021).                                                                     of Experimental Social Psychology 49, 5 (2013), 940–943.
 [7] Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T            [32] Arnold K Ho, Jim Sidanius, Nour Kteily, Jennifer Sheehy-Skeffington, Felicia
     Kalai. 2016. Man is to computer programmer as woman is to homemaker?                         Pratto, Kristin E Henkel, Rob Foels, and Andrew L Stewart. 2015. The nature
     debiasing word embeddings. Advances in neural information processing systems                 of social dominance orientation: Theorizing and measuring preferences for in-
     29 (2016), 4349–4357.                                                                        tergroup inequality using the new SDO7 scale. Journal of Personality and Social
 [8] Joy Buolamwini and Timnit Gebru. 2018. Gender shades: Intersectional accu-                   Psychology 109, 6 (2015), 1003.
     racy disparities in commercial gender classification. In Conference on fairness,        [33] Arnold K Ho, Jim Sidanius, Daniel T Levin, and Mahzarin R Banaji. 2011. Evidence
     accountability and transparency. PMLR, 77–91.                                                for hypodescent and racial hierarchy in the categorization and perception of
 [9] Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. 2017. Semantics derived               biracial individuals. Journal of personality and social psychology 100, 3 (2011),
     automatically from language corpora contain human-like biases. Science 356,                  492.
     6334 (2017), 183–186.                                                                   [34] Niharika Jain, Alberto Olmo, Sailik Sengupta, Lydia Manikonda, and Subbarao
[10] Colleen M Carpinella, Jacqueline M Chen, David L Hamilton, and Kerri L Johnson.              Kambhampati. 2020. Imperfect imaganation: Implications of gans exacerbating
     2015. Gendered facial cues influence race categorizations. Personality and Social            biases on facial data augmentation and snapchat selfie lenses. arXiv preprint
     Psychology Bulletin 41, 3 (2015), 405–419.                                                   arXiv:2001.09528 (2020).
[11] Tessa ES Charlesworth, Victor Yang, Thomas C Mann, Benedek Kurdi, and                   [35] Kimmo Karkkainen and Jungseock Joo. 2021. FairFace: Face Attribute Dataset
     Mahzarin R Banaji. 2021. Gender stereotypes in natural language: Word embed-                 for Balanced Race, Gender, and Age for Bias Measurement and Mitigation. In
     dings show robust consistency across child and adult language corpora of more                Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision.
     than 65 million words. Psychological Science 32, 2 (2021), 218–240.                          1548–1558.
[12] Mark Chen, Alec Radford, Rewon Child, Jeffrey Wu, Heewoo Jun, David Luan,               [36] Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, and
     and Ilya Sutskever. 2020. Generative pretraining from pixels. In International               Timo Aila. 2020. Training Generative Adversarial Networks with Limited Data.
     Conference on Machine Learning. PMLR, 1691–1703.                                             In Proc. NeurIPS.
[13] Jacob Cohen. 1992. Statistical power analysis. Current directions in psychological      [37] Eugenia Kim, De’Aira Bryant, Deepak Srikanth, and Ayanna Howard. 2021. Age
     science 1, 3 (1992), 98–101.                                                                 Bias in Emotion Detection: An Analysis of Facial Emotion Recognition Perfor-
[14] Nilanjana Dasgupta, Debbie E McGhee, Anthony G Greenwald, and Mahzarin R                     mance on Young, Middle-Aged, and Older Adults. In Proceedings of the 2021
     Banaji. 2000. Automatic preference for White Americans: Eliminating the fa-                  AAAI/ACM Conference on AI, Ethics, and Society. 638–644.
     miliarity explanation. Journal of Experimental Social Psychology 36, 3 (2000),          [38] Amy R Krosch, Suzy J Park, Jesse Walker, and Ari R Lisner. 2022. The threat of
     316–328.                                                                                     a majority-minority US alters white Americans’ perception of race. Journal of
[15] Emily Denton, Ben Hutchinson, Margaret Mitchell, Timnit Gebru, and Andrew                    Experimental Social Psychology 99 (2022), 104266.
     Zaldivar. 2019. Image counterfactual sensitivity analysis for detecting unintended      [39] Benedek Kurdi, Shayn Lozano, and Mahzarin R Banaji. 2017. Introducing the
     bias. arXiv preprint arXiv:1906.06439 (2019).                                                open affective standardized image set (OASIS). Behavior research methods 49, 2
[16] Jesse Dodge, Maarten Sap, Ana Marasovic, William Agnew, Gabriel Ilharco, Dirk                (2017), 457–470.
     Groeneveld, and Matt Gardner. 2021. Documenting the english colossal clean              [40] Oran Lang, Yossi Gandelsman, Michal Yarom, Yoav Wald, Gal Elidan, Avinatan
     crawled corpus. arXiv preprint arXiv:2104.08758 (2021).                                      Hassidim, William T Freeman, Phillip Isola, Amir Globerson, Michal Irani, et al.
[17] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xi-                 2021. Explaining in Style: Training a GAN to explain a classifier in StyleSpace.
     aohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg                   arXiv e-prints (2021), arXiv–2104.
     Heigold, Sylvain Gelly, et al. 2020. An Image is Worth 16x16 Words: Trans-              [41] Stacey J Lee, Nga-Wing Anjela Wong, and Alvin N Alvarez. 2009. The model
     formers for Image Recognition at Scale. In International Conference on Learning              minority and the perpetual foreigner: Stereotypes of Asian Americans. (2009).
     Representations.                                                                        [42] James Leibold. 2020. Surveillance in China’s Xinjiang region: Ethnic sorting,
[18] Nikhil Garg, Londa Schiebinger, Dan Jurafsky, and James Zou. 2018. Word                      coercion, and inducement. Journal of Contemporary China 29, 121 (2020), 46–60.
     embeddings quantify 100 years of gender and ethnic stereotypes. Proceedings of          [43] Michael B Lewis. 2016. Arguing that Black is White: Racial categorization of
     the National Academy of Sciences 115, 16 (2018), E3635–E3644.                                mixed-race faces. Perception 45, 5 (2016), 505–514.
[19] Phillip Atiba Goff, Margaret A Thomas, and Matthew Christian Jackson. 2008.             [44] Ang Li, Allan Jabri, Armand Joulin, and Laurens van der Maaten. 2017. Learning
     “Ain’t I a woman?”: Towards an intersectional approach to person perception                  visual n-grams from web data. In Proceedings of the IEEE International Conference
     and group-based harms. Sex Roles 59, 5 (2008), 392–403.                                      on Computer Vision. 4183–4192.
[20] Gabriel Goh, Nick Cammarata, Chelsea Voss, Shan Carter, Michael Petrov, Ludwig          [45] Zhiheng Li and Chenliang Xu. 2021. Discover the Unknown Biased Attribute of
     Schubert, Alec Radford, and Chris Olah. 2021. Multimodal neurons in artificial               an Image Classifier. arXiv preprint arXiv:2104.14556 (2021).
     neural networks. Distill 6, 3 (2021), e30.                                              [46] Yuri Lin, Jean-Baptiste Michel, Erez Aiden Lieberman, Jon Orwant, Will Brock-
[21] Anthony G Greenwald, Mahzarin R Banaji, and Brian A Nosek. 2015. Statistically               man, and Slav Petrov. 2012. Syntactic annotations for the google books ngram
     small effects of the Implicit Association Test can have societally large effects.            corpus. In Proceedings of the ACL 2012 system demonstrations. 169–174.
     (2015).                                                                                 [47] Jordan Liz. 2018. “The Fixity of Whiteness”: Genetic Admixture and the Legacy
[22] Anthony G Greenwald, Debbie E McGhee, and Jordan LK Schwartz. 1998. Mea-                     of the One-Drop Rule. Critical Philosophy of Race 6, 2 (2018), 239–261.
     suring individual differences in implicit cognition: the implicit association test.     [48] Debbie S Ma, Joshua Correll, and Bernd Wittenbrink. 2015. The Chicago face
     Journal of personality and social psychology 74, 6 (1998), 1464.                             database: A free stimulus set of faces and norming data. Behavior research methods
[23] Xiuye Gu, Tsung-Yi Lin, Weicheng Kuo, and Yin Cui. 2021. Open-vocabulary                     47, 4 (2015), 1122–1135.
     Object Detection via Vision and Language Knowledge Distillation. arXiv preprint         [49] Chandler May, Alex Wang, Shikha Bordia, Samuel Bowman, and Rachel Rudinger.
     arXiv:2104.13921 2 (2021).                                                                   2019. On Measuring Social Biases in Sentence Encoders. In Proceedings of the 2019
[24] Nitzan Guetta, Asaf Shabtai, Inderjeet Singh, Satoru Momiyama, and Yuval Elovici.            Conference of the North American Chapter of the Association for Computational
     2021. Dodging Attack Using Carefully Crafted Natural Makeup. arXiv preprint                  Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers).
     arXiv:2109.06467 (2021).                                                                     622–628.
[25] Wei Guo and Aylin Caliskan. 2021. Detecting emergent intersectional biases:             [50] Norman Mu, Alexander Kirillov, David Wagner, and Saining Xie. 2021. SLIP: Self-
     Contextualized word embeddings contain a distribution of human-like biases. In               supervision meets Language-Image Pre-training. arXiv preprint arXiv:2112.12750
     Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society. 122–133.             (2021).
[26] Jamin Halberstadt, Steven J Sherman, and Jeffrey W Sherman. 2011. Why Barack            [51] Carlos David Navarrete, Melissa M McDonald, Ludwin E Molina, and Jim Sida-
     Obama is Black: A cognitive account of hypodescent. Psychological Science 22, 1              nius. 2010. Prejudice at the nexus of race and gender: an outgroup male target
     (2011), 29–33.                                                                               hypothesis. Journal of personality and social psychology 98, 6 (2010), 933.
[27] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual              [52] Pandu Nayak. 2021. MUM: A new AI milestone for understanding information.
     learning for image recognition. In Proceedings of the IEEE conference on computer            https://blog.google/products/search/introducing-mum/
     vision and pattern recognition. 770–778.                                                [53] Alex Nichol, Prafulla Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela Mishkin,
[28] Jeff Heaton. 2020. Applications of deep neural networks. arXiv preprint                      Bob McGrew, Ilya Sutskever, and Mark Chen. 2021. GLIDE: Towards Photoreal-
     arXiv:2009.05673 (2020).                                                                     istic Image Generation and Editing with Text-Guided Diffusion Models. arXiv
[29] Christine B Hickman. 1996. The devil and the one drop rule: Racial categories,               preprint arXiv:2112.10741 (2021).
     African Americans, and the US census. Mich. L. Rev. 95 (1996), 1161.                    [54] Charles E Osgood. 1964. Semantic differential technique in the comparative study
[30] Arnold K Ho, Nour S Kteily, and Jacqueline M Chen. 2017. “You’re one of us”:                 of cultures 1. American Anthropologist 66, 3 (1964), 171–200.
     Black Americans’ use of hypodescent and its association with egalitarianism.            [55] Destiny Peery and Galen V Bodenhausen. 2008. Black+ White= Black: Hypodes-
     Journal of personality and social psychology 113, 5 (2017), 753.                             cent in reflexive categorization of racially ambiguous faces. Psychological Science
                                                                                                  19, 10 (2008), 973–977.


                                                                                      1303


FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea                                                                       Robert Wolfe, Mahzarin R. Banaji, and Aylin Caliskan


[56] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh,                      Empirical Methods in Natural Language Processing (EMNLP) (2021).
     Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark,             [69] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
     et al. 2021. Learning transferable visual models from natural language supervision.          Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all
     arXiv preprint arXiv:2103.00020 (2021).                                                      you need. In Advances in neural information processing systems. 5998–6008.
[57] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever,        [70] Jialu Wang, Yang Liu, and Xin Eric Wang. 2021. Are Gender-Neutral Queries
     et al. 2019. Language models are unsupervised multitask learners. OpenAI blog                Really Gender-Neutral? Mitigating Gender Bias in Image Search. arXiv preprint
     1, 8 (2019), 9.                                                                              arXiv:2109.05433 (2021).
[58] Vikram V Ramaswamy, Sunnie SY Kim, and Olga Russakovsky. 2021. Fair attribute           [71] Isabel Wilkerson. 2020. Caste (Oprah’s Book Club): The origins of our discontents.
     classification through latent space de-biasing. In Proceedings of the IEEE/CVF               Random House.
     Conference on Computer Vision and Pattern Recognition. 9301–9310.                       [72] Benjamin Wilson, Judy Hoffman, and Jamie Morgenstern. 2019. Predictive in-
[59] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen.                     equity in object detection. arXiv preprint arXiv:1902.11097 (2019).
     2022. Hierarchical Text-Conditional Image Generation with CLIP Latents. arXiv           [73] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue,
     preprint arXiv:2204.06125 (2022).                                                            Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, Joe
[60] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec                   Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu,
     Radford, Mark Chen, and Ilya Sutskever. 2021. Zero-shot text-to-image generation.            Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest,
     arXiv preprint arXiv:2102.12092 (2021).                                                      and Alexander M. Rush. 2020. Transformers: State-of-the-Art Natural Language
[61] Lauren Rhue. 2018. Racial influence on automated perceptions of emotions.                    Processing. In Proceedings of the 2020 Conference on Empirical Methods in Natural
     Available at SSRN 3281765 (2018).                                                            Language Processing: System Demonstrations. Association for Computational
[62] Christoph Schuhmann. 2021. LAION-400-Million Open Dataset. https://laion.                    Linguistics, Online, 38–45. https://www.aclweb.org/anthology/2020.emnlp-
     ai/laion-400-open-dataset/                                                                   demos.6
[63] Emily Sheng, Kai-Wei Chang, Prem Natarajan, and Nanyun Peng. 2019. The                  [74] Robert Wolfe and Aylin Caliskan. 2021. Low Frequency Names Exhibit Bias
     Woman Worked as a Babysitter: On Biases in Language Generation. In Proceedings               and Overfitting in Contextualizing Language Models. In Proceedings of the 2021
     of the 2019 Conference on Empirical Methods in Natural Language Processing and               Conference on Empirical Methods in Natural Language Processing. 518–532.
     the 9th International Joint Conference on Natural Language Processing (EMNLP-           [75] Robert Wolfe and Aylin Caliskan. 2022. Contrastive Visual Semantic Pretraining
     IJCNLP). 3407–3412.                                                                          Magnifies the Semantics of Natural Language Representations. Association for
[64] Jim Sidanius and Felicia Pratto. 2001. Social dominance: An intergroup theory of             Computational Linguistics (2022).
     social hierarchy and oppression. Cambridge University Press.                            [76] Robert Wolfe and Aylin Caliskan. 2022. VAST: The Valence-Assessing Semantics
[65] Ryan Steed and Aylin Caliskan. 2021. Image representations learned with unsu-                Test for Contextualizing Language Models. In Proceedings of the 36th AAAI
     pervised pre-training contain human-like biases. In Proceedings of the 2021 ACM              Conference on Artificial Intelligence.
     Conference on Fairness, Accountability, and Transparency. 701–713.                      [77] Ellen D Wu. 2015. The color of success: Asian Americans and the origins of the
[66] Hannah Tessler, Meera Choi, and Grace Kao. 2020. The anxiety of being Asian                  model minority. Vol. 100. Princeton University Press.
     American: Hate crimes and negative biases during the COVID-19 pandemic.                 [78] Danielle M Young, Diana T Sanchez, Kristin Pauker, and Sarah E Gaither. 2021.
     American Journal of Criminal Justice 45, 4 (2020), 636–646.                                  A meta-analytic review of hypodescent patterns in categorizing multiracial and
[67] Yonglong Tian, Dilip Krishnan, and Phillip Isola. 2019. Contrastive Representation           racially ambiguous targets. Personality and Social Psychology Bulletin 47, 5 (2021),
     Distillation. In International Conference on Learning Representations.                       705–727.
[68] Autumn Toney-Wails and Aylin Caliskan. 2021. ValNorm Quantifies Seman-                  [79] Michael A Zarate and Eliot R Smith. 1990. Person categorization and stereotyping.
     tics to Reveal Consistent Valence Biases Across Languages and Over Centuries.                Social cognition 8, 2 (1990), 161–185.


                                                                                      1304
