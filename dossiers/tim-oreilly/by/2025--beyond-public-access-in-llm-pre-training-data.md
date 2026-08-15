---
title: "Beyond Public Access in LLM Pre-Training Data: Testing OpenAI's models on non-public book content"
person: tim-oreilly
section: by
type: report
year: 2025
date: 2025-04-24
venue: "arXiv:2505.00020 / AI Disclosures Project, SSRC (forthcoming in AI & Ethics)"
authors: "Sruly Rosenblat; Tim O'Reilly; Ilan Strauss"
source_url: https://arxiv.org/abs/2505.00020
retrieved: 2026-08-13
content: full-text
notes: "Open arXiv preprint PDF (v2); text extracted with pdftotext -layout. SSRC DOI 10.35650/AIDP.4111.d.2025."
---

# Beyond Public Access in LLM Pre-Training Data: Testing OpenAI's models on non-public book content

## Full text

Beyond Public Access in LLM Pre-Training Data
                                                           Testing OpenAI’s models on non-public book content

                                                           Sruly Rosenblat ∗1 , Tim O’Reilly1,3 , and Ilan Strauss1,2
                                                                      1 AI Disclosures Project, Code for Science and Society

                                                          2 Institute for Innovation and Public Purpose, University College London

arXiv:2505.00020v2 [cs.CL] 6 May 2026
                                                                                            3 O’Reilly Media

                                                                                                 Abstract

                                                   Using a legally obtained dataset of 34 copyrighted O’Reilly Media books, we apply
                                               the DE-COP membership inference attack method to investigate whether OpenAI’s large
                                               language models show recognition of copyrighted content. Our results based on this
                                               small sample suggest that GPT-4o, OpenAI’s more recent and capable model, exhibits
                                               patterns consistent with recognition of pay-walled book content, with an AUROC score
                                               of 0.82 (95% bootstrapped CI: 0.60–0.96), though this wide confidence interval reflects
                                               substantial uncertainty due to the limited number of books tested. GPT-4o Mini, as a
                                               much smaller model, shows little recognition of any O’Reilly Media content with an
                                               AUROC score of 0.56 (0.28-0.83) for non-public data. Testing multiple models, with the
                                               same cutoff date, provides a partial control for potential language shifts over time that
                                               might bias our findings, though differences in model size, architecture, and potentially
                                               training data composition limit the strength of this control. These preliminary results
                                               underscore the importance of increased corporate transparency regarding pre-training
                                               data sources and the development of formal licensing frameworks for AI content train-
                                               ing. Our principal contribution is our examination of public and non public data separately.

                                               Keywords: Membership Inference Attacks, Large Language Models, Copyright Issues, Data
                                               Access Violations, Pre-Training Data, Architecture of Participation.

                                           ∗ Varying Contributions. Sruly Rosenblat: Compute, statistical analysis and AUROC method, appendix, graphs, and tables.
                                        Ilan Strauss: Paper write-up, structure, core findings, policy discussion. Tim O’Reilly: Topic conceptualization and research
                                        design (public vs. non-public data). Isobel Moure: Policy discussion section.
                                           We gratefully acknowledge funding support from the Omidyar Network, Alfred P. Sloan Foundation, McGovern Founda-
                                        tion, and the O’Reilly Foundation, without which this work would not have been possible. We also extend our full appre-
                                        ciation to Andrew Odewahn for compiling the O’Reilly dataset and to Anshuman Suri and André Duarte for their helpful
                                        feedback on our initial draft. Thank you to Isobel Moure for edits. All mistakes are solely our own. Corresponding author is:
                                        sruly@aidisclosures.org. This version of the paper was completed may 6th 2026. The code for this paper can be found at:
                                        https://github.com/AI-Disclosures-Project/Detecting-Access-Violations-in-a-LLMs-Pre-Training-Data.
1     Introduction: Investigating potential access violations

Large Language Models (LLMs) require incredible amounts of public and non-public data to
learn human language (called the ‘pre-training’ stage). Yet the origins and legal status of this
pre-training data remains largely undisclosed by the corporations that gather and use it (Ope-
nAI 2023; Anthropic 2023). Several high-profile legal proceedings indicate that major AI com-
panies may train on non-public, often illegally obtained, content (New York Times 2023; Roth
2024; Belanger 2025). In response, AI companies are calling for model pre-training to be ex-
empt from copyright obligations (OpenAI 2025; Whitwam 2025). If adopted, copyright holders
and content creators may be unable to sustain themselves and their creations, with profound
implications for the survival of the Internet’s traffic-driven business model (Blaszczyk et al.
2024; Knibbs 2025; Durantaye 2025).

Figure 1. We split our sample of O’Reilly books by time period & accessibility.

Note: Data published prior to a model’s training completion (t − n) may have been trained on. Data published after a model’s
training cutoff (t + n) is known to not be in the model’s training data. Any portion of non-public data found to be included in
a model’s training would constitute an access violation (bottom left square).

    This paper examines whether non-publicly accessible (non-public) copyrighted O’Reilly Media
books were included in the training datasets of OpenAI’s GPT series of models. Each O’Reilly Media
book contains both publicly accessible, free-to-use preview content, and non-public, effectively
pay-walled content. This allows us to examine whether OpenAI primarily trained its models

                                                              1
on publicly available data or if it potentially circumvented paywall restrictions and used non-
public data (Figure 1).

   We employ the DE-COP membership inference attack by Duarte et al. (2024) to test whether
a model can reliably differentiate between human-authored (O’Reilly Media) texts and para-
phrased LLM versions of the text that we generate. If it can, then the model might have prior
knowledge of the text from its training (ibid.). By systematically probing a model’s knowledge
of texts published before and after its training cutoff date, we can estimate the probability of
particular book extracts having been included in a model’s training data (DE-COP measures
paragraph-level recognition; AUROC then aggregates these scores to assess overall separability
between potentially-seen and unseen books).

   We test OpenAI’s GPT-3.5 Turbo, GPT-4o Mini, and GPT-4o models across 13,962 para-
graphs from 34 O’Reilly books for potential access violations, distinguishing between public
and non-public content extracted from the same books. On the basis of AUROC scores calcu-
lated for each GPT Model (using 26 books for GPT-4o and GPT-4o Mini, and 28 for GPT-3.5
Turbo), where 50% reflects no detectable recognition by the model, we find that:

  1. The role of non-public data in OpenAI’s model pre-training data has seemingly increased over
     time. GPT-4o achieves an AUROC score of 0.82 (95% bootstrapped CI: 0.60–0.96), while
     GPT-3.5 Turbo, with a training cutoff two years prior, scores just above 0.50. This dif-
     ference may reflect changes in training data composition, but could also be driven by
     differences in model size or architecture.

  2. GPT-4o potentially exhibits stronger recognition of non-public O’Reilly book content compared
     to publicly accessible samples, with AUROC scores of 0.82 (CI: 0.60–0.96) for non-public
     data vs 0.64 (CI: 0.36-0.93) for public data. We would expect the opposite, since public
     data is more easily accessible and repeated across the internet, and potentially highlights
     the value-add of pay-walled high-quality data to a model’s training if confirmed on a
     larger sample. Though this difference is not statistically significant.

  3. Smaller models may be harder to test accurately. We find that GPT-4o Mini, with the same

                                                  2
       training cutoff as GPT-4o, shows little to no recognition of O’Reilly data – public or non-
       public. This may reflect reduced memorization capacity in a smaller model rather than
       differences in training data, or some combination of both (Meeus et al. 2024; Morris et al.
       2025).

   If access violations occurred, they might have occurred via the LibGen database, as all of
the O’Reilly books tested were found in it. Alternatively data may have come from Books3 (Jia
et al. 2025). However, no licensing agreement existed between OpenAI and O’Reilly Media at
the time of this study.

   As a robustness check, we show that although newer LLMs have an improved ability to dis-
tinguish human-authored from machine-generated language regardless of whether a particular
text was trained on, this does not reduce the method’s ability to classify data as being seen or
not.

   Our study design accounts for the potential of time-specific differences in language to bias
our results (Duan et al. 2024; Debeshee et al. 2024), which can arise because we split our
sample (of potentially trained on and so in-sample, vs. not trained on and so out-of-sample)
by date. Such bias can occur if the DE-COP test mistakes language that the model is simply
“familiar” with (due to temporal shifts) for content the model was trained on. To ensure that
this bias does not drive our findings, we test two models (GPT-4o and GPT-4o Mini) that were
both trained on data from the same period. Because these two models show notably different
results, time-specific effects are unlikely to be the determining factor (although differences in
model size and architecture may obscure differences).

   Our study contributes to research on detecting unauthorized data usage in AI training (Mat-
tern et al. 2023; Shi et al. 2023b; Jingyang Zhang et al. 2024) by applying membership inference
methods to legally sourced non-public copyrighted material. Unlike earlier studies that pri-
marily use publicly available datasets (Shi et al. 2023a; Duarte et al. 2024; Duan et al. 2024),
our public/non-public split within the same books enables the examination of how the paywall
status of text affects model recognition.

   Our findings highlight the need for stronger accountability in AI companies model pre-

                                                 3
training process. Liability provisions that incentivize improved corporate transparency in dis-
closing data provenance (O’Reilly 2024) may be an important step to facilitating commercial
markets for training data licensing and remuneration (Thornhill 2025). Membership inference
attacks can help pressure model developers to negotiate such agreements. But by itself is in-
sufficient, especially given its limited efficacy against smaller models, more advanced models,
and models with certain post-training features (Satvaty et al. 2024; Jie Zhang et al. 2024; Balaji
2024).

    By way of robustness, our results are based on a small sample of books and so are potentially
sensitive to individual book results. It is also difficult to isolate the role of model size on our
results and is an important area for future research.

    Section 2 outlines our books dataset and DE-COP and AUROC methods. Section 3 presents
our findings. Section 4 discusses their policy implications for establishing formal commercial
markets for content creator training data. Appendix A contains more details on our sample
and analysis.

2     Data and Methods

This section first details our O’Reilly dataset of 34 books and explains how its division into
publicly accessible vs non-public (effectively pay-walled) book samples enables us to detect
potential access violations in a model’s pre-training. Finally, we describe our research, which
involves first testing the model’s recognition of paragraphs from O’Reilly Media books, using
the DE-COP membership inference attack method.

2.1      Data: Public vs. non-public book data

Our dataset contains 34 copyrighted O’Reilly Media books lent to us, that we then split into a
total of 13,962 paragraphs. Paragraphs are used to calculate the initial mean DE-COP score,
one for each book, from which a single AUROC Score is then calculated across all books for
each of OpenAI’s models.

                                                4
   The O’Reilly Media books dataset has the unique quality of containing both non-public
(behind a paywall) and public (freely available) text within the same book. This allows us
to differentiate between instances where a model was trained exclusively on public data and
cases where potential access violations may have occurred. We define public text as any content
made available by O’Reilly Media for content previews – specifically the first 1,500 characters
of each chapter as well as the entirety of chapters one and four. All other O’Reilly text we
define as non-public.1

   To accurately measure the performance of the DE-COP membership inference attack
method (discussed below), paragraph samples must be divided into two distinct categories,
that in practice we can only approximate: data known to be included in the model’s pre-
training dataset and those known to be excluded. In our case we designate books published
before the model’s training cutoff (t − n) as possibly in-dataset (previously seen and trained on)
samples, and books published after a model’s training cutoff (t + n) as known out-of-dataset
samples that the model could not have been trained on (see Figure 1). “Access violations” are
defined as the subset of non-public book paragraphs, published during the model’s training
period, that we identify as likely being used for training.

   We categorize books published before October 2023 (for GPT-4o and GPT-4o Mini), and
before September 2021 (for GPT-3.5 Turbo) as potentially in-dataset (t − n), and those books
published after the model’s training cutoff date as out-of-dataset (t + n), where t is the model
training cutoff date (October 2023 and September 2021, respectively). This date is defined by
the model developer as the last date that the model’s pre-training dataset contains data for.

   Our method of splitting our sample between potentially-in-dataset (t − n) and known out-
of-dataset (t + n) by date may introduce “temporal bias” into our findings (Duan et al. 2024;
Debeshee et al. 2024), and in turn provide us with misleadingly high AUROC scores. This
occurs when features in the data changes over time, creating distinguishable patterns between
training and testing datasets split by time periods. Data then can be separately identified by an
LLM based solely on the language varying with time – in our case into potentially-in-dataset
  1 This isn’t an exact split, select paragraphs may have been copied to public articles, that would usually fall under fair use.

                                                               5
(t − n) and known out-of-dataset (t + n) data – with no actual prior knowledge of the text itself.2

    To help account for this we test two different GPT models (GPT-4o and GPT-4o Mini) that
were trained during the same period, and ideally on the same data, such that if our tests show
very different AUROC results then temporal bias is unlikely to be the main driver. It is still
possible that the models were trained on different datasets or have radically different archi-
tectures, the datasets and model architecture were never publicly disclosed to the best of our
knowledge.

    Our study design also helps isolate prior model knowledge of the data. Specifically, our
results are unlikely due to GPT-4o simply being better at distinguishing human-authored from
AI-generated text than GPT-4o Mini, as AUROC here measures the difference in knowledge
within the same model between books published prior to and after training completion. Even
assuming a model has perfect identification capability, if it had not been trained on any of the
test samples, we would expect an AUROC score of approximately 50%.

    It is also unclear how temporal bias would apply to DE-COP. As it is calculated based on
how well the model identifies real text from paraphrases based in the same time period, with
the same names, dates and concepts. For temporal bias to apply there would have to be some
reason why paraphrases generated on text published prior to a models cutoff are more de-
tectable than those generated on text published after besides for familiarity with the text. But
with DE-COP we are not comparing paragraphs across years with different concepts or names.
Instead, we are only directly comparing a paragraph with its paraphrased alternatives.

    We carefully filter the dataset to avoid any ambiguous cases – such as second edition books
with potentially minor changes on the previous editions published during the training period
– that risk contaminating our “unseen” classification. Additionally, to minimize edge cases
where publication dates might overlap with training cutoffs, we excluded books published
during a model’s cutoff year from tests involving that specific model.Consequently, not every
   2 Temporal bias is when the ability to infer membership through DE-COP, or any related method, is confounded by time-
dependent changes in the data, rather than by genuine evidence that a particular example was (or was not) in the training set.
Similarly, stylistic bias captures biases that arise from shifts in how data “looks” or is distributed (e.g., changes in vocabulary,
writing style, or domain). Both these biases can appear if one naively splits data by time period, for instance, using older data
for training and newer data for testing, without making any associated adjustments. In other words, during the DE-COP test
the model might mistake familiar vs. unfamiliar language, for familiar vs. unfamiliar content they were trained on.

                                                                 6
model was tested on precisely the same set of books: GPT-4o and GPT-4o Mini were each
tested on 26 books (excluding 2023 publications), while GPT-3.5 Turbo was tested on 28 books
(excluding 2021 publications). See Appendix A.1 for the full list.

2.2     Methods: DE-COP and AUROC

We first use the DE-COP membership inference attack (Duarte et al. 2024) to determine
whether a particular paragraph was part of a target model’s training set.                              This works
by quizzing an LLM with a multiple-choice test containing four options: one original
human-authored O’Reilly book paragraph and three machine-generated paraphrases of that
paragraph. To eliminate position bias (i.e., the tendency for models to favor certain answer
positions such as “A”), each paragraph is tested across all 24 possible permutations of the
four options (4! = 24). A paragraph’s “guess rate” is the proportion of these 24 permutations
in which the model correctly identifies the original human-authored text. This process is re-
peated for nearly every paragraph in each of the 34 O’Reilly books tested, where a “paragraph”
refers to adjacent sentences of approximately 120 words (not necessarily corresponding to
paragraph breaks in the source material).3

    If the model frequently identifies the original text for books published during its training
period, this likely indicates prior recognition of that content. The key comparison is between
this guess rate on books published before the model’s training cutoff and the baseline guess
rate on books published after the cutoff – content the model could not have been trained on.

    We test GPT-3.5 Turbo, GPT-4o Mini, and GPT-4o in this manner and use Claude 3.5
Sonnet4 to generate the paraphrased, machine versions, of the text. We decided to focus on
OpenAI’s models as at the time of testing they provided top 20 log probabilities making the
method more interpretable. Table 1 shows the paragraph sample sizes used to calculate the
DE-COP scores for each paragraph.

  3 See Appendix A.3 for an example of the prompt format used.
  4 This differs from the paraphrase model used in Duarte et al. (2024). We chose Claude 3.5 Sonnet as it was the most
powerful model from Anthropic at the time of testing.

                                                          7
Table 1. DE-COP – Paragraph-Level Sample Size and Average Word Count by
                            Model (by type)
         Model                  Data-Split                        Sample Size (n)       Average Word Count
                                Public                                       1,965                             112
                                Non-Public                                   8,997                             113
         GPT-4o
                                Potentially In-Dataset                       8,985                             113
                                Out-of-Dataset                               1,977                             110
                                Public                                       1,968                             112
                                Non-Public                                   9,005                             113
         GPT-4o Mini
                                Potentially In-Dataset                       8,991                             113
                                Out-of-Dataset                               1,982                             110
                       Public                                                1,929                             113
                       Non-Public                                            6,171                             113
         GPT-3.5 Turbo
                       Potentially In-Dataset                                2,084                             114
                       Out-of-Dataset                                        6,016                             113
Note: Sample sizes (in paragraphs) and average word counts across different data splits for each model. Potentially in-dataset
represents data published prior to a model’s cutoff date; out-of-dataset represents data published afterward.

    The second step in our study is to use the DE-COP quiz scores or guess rates’ generated
above to calculate AUROC Scores (Area Under the Receiver Operating Characteristic). Where
DE-COP measures a model’s ability to identify original human-authored text at the paragraph
level, AUROC aggregates these paragraph-level scores to evaluate whether there is a meaning-
ful difference (or separability’) between how a model handles content that it was potentially
trained on versus content published after its training was completed. AUROC measures a clas-
sifier’s ability to distinguish between two classes, with scores ranging from 0 to 1, with 0.5
representing random chance and values closer to 1 indicating a strong ability to accurately
‘discriminate’ (i.e., classify) between the two classes (or categories). In our case, AUROC mea-
sures the ability to separate books that may have been trained on (t − n), from books the model
could not have seen (t + n). A high AUROC score, therefore, implies that the model was trained
on many of the books published prior to the model’s cutoff date. The threshold that optimally
separates the two classes is determined by the AUROC calculation itself (i.e., the point on the
ROC curve that maximizes the true positive rate while minimizing the false positive rate); we
describe the specific thresholding variants used in Appendix A.2.

                                                              8
    We calculate AUROC scores at both the paragraph and book levels, though our primary
finding is at the book level (Table 2). AUROC scores are calculated on the book-level sample
sizes: being 26 for GPT-4o, 26 for GPT-4o Mini, and 28 for GPT-3.5 Turbo. In summary,
DE-COP produces a paragraph-level guess rate, which is averaged to the book level, and
AUROC then measures separability between potentially-seen and unseen books based on
these scores.

      Table 2. AUROC Sample - Paragraph and Book Sample Sizes by Model

                   Model                 Total Paragraphs         Non-Public        Public     Books

                   GPT-4o                             11,375              9,300      2,075          26
                   GPT-4o Mini                        11,386              9,308      2,078          26
                   GPT-3.5 Turbo                        8,449             6,410      2,039          28
Note: For GPT-4o, we use a sample of 11,375 paragraphs across 26 books, of which 9,300 are non-public and 2,075 are public.
Similarly, for GPT-4o Mini we use 11,386 paragraphs (9,308 non-public and 2,078 public) across 26 books. Finally, GPT-3.5
Turbo used 8,449 paragraphs, with 6,410 non-public and 2,039 public paragraphs across 28 books.

3     Findings

We present our core findings below, based on book level AUROC scores. We first calculate
DE-COP guess rates for public and non-public book paragraphs within each book. Next, we
calculate the mean DE-COP guess rate for each book based on these paragraphs, and use this
to calculate an AUROC score for each large language model pooled across books. We run and
test the various LLMs via Python (Google Colab) using OpenAI and Anthropic’s batch API
(Appendix A.3 and A.4).

    In what follows an AUROC score of 0.50 indicates no detectable recognition by the model;
while test scores approaching 1.0 suggest near-perfect classification ability (between poten-
tially in-dataset and out-of-dataset samples) – based on the previously estimated DE-COP
guess rate. Our confidence interval are calculated using the bootstrap method.

                                                            9
   Figure 2. AUROC Scores Showing Model Recognition of Pre-Training Data

Note: Showing book level AUROC scores (n = 26 for GPT-4o and GPT-4o Mini for both public and non-public; n=28 for GPT-
3.5 Turbo for both public and non-public) across models and data splits (see Table 1 for sample sizes). Book level AUROC is
calculated by averaging the identification rates of all paragraphs within each book and running AUROC on that. Bootstrapped
95% confidence intervals are shown calculated on the sample number of books for each model as the AUROC scores.

    We find that OpenAI’s more recent and capable model shows markedly stronger recognition of
non-public O’Reilly book content than its older model. Figure 2 shows that OpenAI’s more recent
and capable GPT-4o model shows strong recognition of pay-walled O’Reilly book content 0.82
(95% bootstrapped CI: 0.60–0.96), while OpenAI’s GPT-3.5 Turbo, with a training cutoff two
years prior in September 2021, does not (AUROC score just above 0.50). This indicates a no-
tably improved ability to distinguish between non-public books that were potentially included
in the training dataset and those published after the model’s pre-training cutoff. GPT-4o’s
0.82 AUROC score suggests that the model recognizes, and so has prior knowledge of, many
non-public O’Reilly books published prior to its training cutoff date (of October 2023).

    Secondly, Figure 2 also shows that GPT-4o exhibits somewhat stronger recognition of non-
public O’Reilly book content compared to publicly accessible samples, with AUROC scores of 0.82
(non-public) vs 0.64 (public). We would expect the opposite, since public data is more easily
accessible and repeated across the internet. One possible interpretation is that high-quality,

                                                           10
frequently paywalled data is particularly valuable for model training, though this difference is
not statistically significant (p ≈ 0.295 at book level) and should be treated as suggestive rather
than conclusive The difference in AUROC scores between public and non-public data reaches
statistical significance only for GPT-4o at the paragraph level (p ≈ 0.02). At the book level, the
difference is not statistically significant for any model (p ≈ 0.295 for GPT-4o), reflecting the
limited statistical power inherent in a sample of fewer than 30 books.

   Our AUROC results, being much starker at the book level compared to the paragraph level
(Appendix Figure 4), are similar to Puerto et al. (2024), who finds that aggregating results over
larger data units significantly enhances the performance of membership inference attacks. Our
book level AUROC scores calculated on the mean DE-COP scores for each book were often
significantly higher than AUROC done on the paragraph level. However, it is important to
note our confidence interval was also much larger at the book level because of there being a
small sample size – under 30 books.

   GPT-4o’s seemingly high familiarity with O’Reilly Media books may reflect a deliberate
effort by OpenAI to train on the O’Reilly book dataset. However, some of this familiarity could
have been acquired through more benign means – for example, excerpts from these books
may have entered the dataset via user queries or appear in fair use quotations throughout the
internet.

3.1   Robustness and limitations

One reason for the above findings, and a limitation of our study, may be that smaller models are
harder to test accurately in membership inference attacks. We find that GPT-4o Mini, with the same
training cutoff as 4o, was likely not trained on non-public O’Reilly data, and shows similarly
low recognition of public book data too (Figure 2). GPT-4o Mini recorded AUROC scores of
0.55 on public data and 0.56 on non-public data, both near random chance. This may not
reflect its inherent knowledge of text, as per its training, but instead GPT-4o Mini’s inability, as
a smaller model, to remember text compared to 4o, a much larger model by parameter count

                                                11
(Carlini et al. 2022).5 . However, these differences may also just be down to differences in the
dataset size or memorization.

    Prior research has established no clear relationship between model size and model memo-
rization, noting that larger models can memorize more samples (approximately 3.6 bits per pa-
rameter), but also that membership inference becomes harder on larger models as the datasets
they are trained on also grows considerably (Morris et al. 2025): “bigger models can memorize
more samples, and making [sic] datasets bigger makes membership inference harder.”

    Second, we note that improving LLM capabilities can make the identification of pre-
training data through membership inference attacks more difficult. As per Figure 3, we find
that OpenAI’s models’ ability to correctly identify human-authored text, among paraphrased
LLM alternatives, improves with model capabilities, even for texts the model could not have been
trained on – meaning those texts published after the model’s training cutoff. Figure 3 shows
the baseline DE-COP identification rate on books published after the model’s training cutoff
(unseen books). This increased from 0.31 for GPT-3.5 Turbo (training finished September
2021), to 0.57 for GPT-4o Mini (training finished October 2023), and to 0.78 for GPT-4o
(training finished October 2023).

    Once the baseline guess rate (‘identification rate’) exceeds 96%, the difference between po-
tentially in-dataset and out-of-dataset paragraphs could become undetectable at the paragraph
level. For now, however, the gap remains sufficiently large to reliably separate the two cate-
gories when calculating AUROC score, particularly when aggregating results at the book level.
  5 OpenAI does not disclose model sizes but GPT-4o Mini is smaller than GPT-4o and presumably smaller than GPT-3.5
Turbo.

                                                       12
     Figure 3. DE-COP Guess Rate Improves: More capable models identify
                   human text even when not trained on it.

Note: DE-COP guess rates (i.e., identification rates) pooled across all books for OpenAI models. Red bars represent unseen
data published after a model finished training (t + n), and blue bars represent data published before the cutoff date (t − n)
that is suspected to be in the training set. See Table 4 for more. This should not be confused for AUROC scores, AUROC is
calculated on these raw DE-COP scores by measuring the separability of DE-COP scores between data splits.

    Third, our book level AUROC estimates are highly uncertain, with large bootstrapped con-
fidence intervals. We test to see if the difference between public and non-public books AUROC
scores is statistically significant at the 5%. At the paragraph level, GPT-4o shows a statistically
significant difference between public vs non-public AUROC scores (p≈0.02). At the book level,
intervals are wide and differences are only significant at the p = 0.295 level. The differences
were not statistically significant for the other models.

    This reflects the very large bootstrapped uncertainty intervals which limit the statistical
power of any test in differences, in this case using z-scores. Such that even if real differences
did exist, we would lack the power to detect them, due to only a few dozen being used to
calculate each AUROC score.6 For GPT-4o, meaningful paragraph level AUROC scores with
tighter confidence intervals arise with the larger estimated paragraph level sample size. (Table
7, Appendix A.2).
   6 The extremely wide confidence intervals (averaging 0.47 AUROC points) indicate the test has insufficient statistical power
to detect differences reliably.

                                                             13
 Table 3. Differences between AUROC Scores on Non-Public and Public Data

                 Model                                        Difference       P-value     Significant?

                 GPT-4o Book Level                                0.18           0.29            No
                 GPT-4o Mini Book Level                           0.01           0.96            No
                 GPT-3.5 Turbo Book Level                        -0.10           0.56            No
                 GPT-4o Paragraph Level                           0.04           0.02            Yes
                 GPT-4o Mini Paragraph Level                      0.02           0.24            No
                 GPT-3.5 Turbo Paragraph Level                   -0.01           0.56            No
Note: Showing the difference in AUROC scores between non-public and public data splits for each model, along with corre-
sponding p-values from a statistical significance test (z-scores). A positive difference indicates higher performance on non-
public data. The “Significant?” column indicates whether the difference is statistically significant at the 0.05 level. These
results are from a Z-test.

4     Discussion: Towards functional content AI marketplaces?

Although the evidence presented here on potential access violations is specific to OpenAI and
O’Reilly Media books, and based on a small sample with wide confidence intervals, similar
dynamics may exist across AI model developers. Our findings aim to motivate greater trans-
parency in data collection and usage practices.

    Our findings, alongside similar studies (Ahmed et al. 2026; Belanger 2025) suggest that
current AI model development practices may be creating what O’Reilly (2024) describes as an
“extractive dead end”, creating not just a legal challenge but an existential one for the Internet’s
content ecosystem. The economic implications of uncompensated training data usage extend
beyond individual copyright holders to the broader sustainability of professional content cre-
ation. If AI companies extract value from a content creator’s produced materials without fairly
compensating the creator, they risk depleting the very resources upon which their AI systems
depend (ibid.).

    This dynamic creates a tragedy of the commons.7 If left unaddressed, uncompensated train-
   7 As Longpre et al. (2024) notes: “in less than a year, ∼ 5% of the tokens in C4 and other major corpora have recently
become restricted by robots.txt. And nearly 45% of these tokens now carry some form of restrictions from the domain’s Terms
of Service.”

                                                            14
ing data could lead to a downward spiral in the Internet’s content quality and diversity. As
revenue streams for professional content creation diminish, fewer resources will be dedicated
to producing the high-quality, accurate, and diverse human content that AI systems rely on for
training – and inference.

   Our key finding, that OpenAI may have trained their GPT-4o model on non-public data, is
only preliminary and is based on a small sample of books and subject to the above method-
ological caveats. Membership inference attacks of a model’s outputs are not a substitute for
detailed – ideally programmatic – model cards that disclose and disaggregate the sources of
model training data (Mitchell et al. 2019; Gebru et al. 2021). However, requiring smaller com-
panies to sift through their pre-training dataset and individually identify the sources for each
of their training inputs is unrealistic without tools and standards designed for this purpose.

   Common Corpus (Langlais et al. 2024), a large pre-vetted training dataset, is one way
around this issue. By centralizing the data cleaning process and providing verifiable pre-
training data as a common public good, datasets like Common Corpus could enable smaller
firms to train models on non-proprietary data, and easily facilitate disclosure (ibid.). Special-
ized data auditing companies are already arising but limited in what they can achieve without
specific standards.

   Ensuring that IP holders know when their work has been used in model training represents
a crucial first step toward establishing AI markets for content creator data. Technical methods
for this are still in their infancy (Grosse et al. 2023; Zhao et al. 2024). But when applied to
specific types of content, such as music, these methods seem to achieve better results, with at
least one new music platform already apparently being able to attribute AI generated music
outputs to specific music training inputs (Paine 2025).

   More broadly, given the apparent importance of high-quality paywalled content for model
training, structured markets for licensing such data remain both feasible and necessary. If
the current lack of transparency around training data provenance persists, it could harm both
content creators and AI developers. Content creators lose revenue and incentive to produce the
high-quality material that models depend on, while developers face reputational and legal risk

                                               15
alongside a potential degradation in the quality of available training content – particularly as a
growing share of online content becomes AI-generated (O’Reilly 2024). Liability regimes and
disclosure requirements may be necessary to catalyze viable marketplaces for various types of
model training and inference content (Thornhill 2025).

5    Conclusion

This study applies the DE-COP membership inference attack to 34 legally obtained copy-
righted O’Reilly Media books to examine whether OpenAI’s models exhibit recognition pat-
terns consistent with exposure to non-public, paywalled content. GPT-4o shows notably ele-
vated recognition of non-public book content (AUROC 0.82, 95% CI: 0.60–0.96), while GPT-4o
Mini and GPT-3.5 Turbo do not, though the wide confidence intervals and small sample size
warrant caution in interpretation. Our principal contribution is the application of membership
inference methods to legally obtained non-public material, enabling the detection of potential
access violations that studies using only public data cannot identify. Although our evidence is
specific to OpenAI and O’Reilly Media, the underlying dynamics likely extend to other model
developers and content publishers. Future work should expand the sample of books and pub-
lishers tested, explore complementary detection methods, and investigate how model size and
architecture interact with membership inference performance.

                                               16
References
Ahmed, Ahmed et al. (2026). “Extracting books from production language models”. arXiv
    preprint arXiv:2601.02671.
Anthropic (Nov. 2023). Claude 3 Model Card. Tech. rep. Accessed: 2024-12-04. Anthropic. url:
    https : / / www - cdn . anthropic . com / de8ba9b01c9ab7cbabf5c33b80b7bbc618857627 /
    Model_Card_Claude_3.pdf.
Balaji, Suchir (Oct. 2024). When Does Generative AI Qualify for Fair Use? Accessed: 2024-12-04.
    url: https://suchir.net/fair_use.html.
Belanger, Ashley (Feb. 12, 2025). ““Torrenting from a corporate laptop doesn’t feel right”: Meta
    emails unsealed”. Ars Technica. url: https://arstechnica.com/tech-policy/2025/02/
    meta-torrented-over-81-7tb-of-pirated-books-to-train-ai-authors-say/.
Blaszczyk, Matt, Geoffrey McGovern, and Karlyn D. Stanley (Nov. 2024). Artificial Intelligence
    Impacts on Copyright Law. Accessed: 2024-12-04. url: https : / / www . rand . org / pubs /
    perspectives/PEA3243-1.html.
Carlini, Nicholas et al. (2022). “Quantifying memorization across neural language models”.
    The Eleventh International Conference on Learning Representations.
Debeshee, Das, Zhang Jie, and Tramèr Florian (June 2024). “Blind Baselines Beat Membership
    Inference Attacks for Foundation Models”. arXiv. Accessed: 2024-12-04. url: https : / /
    arxiv.org/abs/2406.16201.
Duan, Michael et al. (Feb. 2024). “Do Membership Inference Attacks Work on Large Language
    Models?” arXiv preprint arXiv:2402.07841. Accessed: 2024-12-04. url: https : / / arxiv .
    org/pdf/2402.07841.
Duarte, André V et al. (2024). “De-cop: Detecting copyrighted content in language models
    training data”. arXiv preprint arXiv:2402.09910.
Durantaye, Katharina de la (2025). “Control and Compensation. A Comparative Analysis of
    Copyright Exceptions for Training Generative AI”. IIC-International Review of Intellectual
    Property and Competition Law, pp. 1–34.
Gebru, Timnit et al. (2021). “Datasheets for Datasets. Documentation to facilitate communica-
    tion between dataset creators and consumers”. Communications of the ACM 64 (12).
Grosse, Roger et al. (2023). “Studying large language model generalization with influence func-
    tions”. arXiv preprint arXiv:2308.03296.
IBM (2024). Area under the Curve. IBM Documentation, SPSS Statistics 30.0.0. Part of "Using
    ROC Analysis to Choose between Competing Classification Schemes." Accessed: 2026-03-
    24. url: https://www.ibm.com/docs/en/spss- statistics/30.0.0?topic=schemes-
    area-under-curve.
Jia, Stella and Abhishek Nagaraj (2025). Cloze Encounters: The Impact of Pirated Data Access on
    LLM Performance. Tech. rep. National Bureau of Economic Research.
Knibbs, Kate (2025). “Thomson Reuters Wins First Major AI Copyright Case in the US”.
    WIRED. url: https : / / www . wired . com / story / thomson - reuters - ai - copyright -
    lawsuit/.

                                              17
Langlais, Pierre-Carl, Anastasia Stasenko, and Catherine Arnett (Nov. 2024). “Releasing
   the largest multilingual open pretraining dataset”. Hugging Face Blog. url: https :
   //huggingface.co/blog/Pclanglais/two-trillion-tokens-open.
Longpre, Shayne et al. (2024). “Consent in crisis: The rapid decline of the ai data commons”.
   The Thirty-eight Conference on Neural Information Processing Systems Datasets and Bench-
   marks Track.
Mattern, Justus et al. (2023). “Membership inference attacks against language models via
   neighbourhood comparison”. arXiv preprint arXiv:2305.18462.
Meeus, Matthieu et al. (2024). “Copyright traps for large language models”. arXiv preprint
   arXiv:2402.09363.
Mitchell, Margaret et al. (2019). “Model Cards for Model Reporting”. Proceedings of the confer-
   ence on fairness, accountability, and transparency, pp. 220–229.
Morris, John X et al. (2025). “How much do language models memorize?” arXiv preprint
   arXiv:2505.24832.
New York Times (Dec. 2023). The New York Times Company v. OpenAI, Inc. Accessed: 2024-12-
   04. url: https://nytco-assets.nytimes.com/2023/12/NYT_Complaint_Dec2023.pdf.
O’Reilly, Tim (June 2024). How to Fix ‘AI’s Original Sin’. Accessed: 2024-12-04. url: https :
   //www.oreilly.com/radar/how-to-fix-ais-original-sin/.
OpenAI (Mar. 2023). GPT-4 System Card. Tech. rep. Accessed: 2024-12-04. url: https://cdn.
   openai.com/papers/gpt-4-system-card.pdf.
— (Mar. 2025). Response to OSTP/NSF RFI: Notice Request for Information on the Development
   of an Artificial Intelligence (AI) Action Plan. Tech. rep. OpenAI. url: https://cdn.openai.
   com/global- affairs/ostp- rfi/ec680b75- d539- 4653- b297- 8bcf6e5f7686/openai-
   response- ostp- nsf- rfi- notice- request- for- information- on- the- development-
   of-an-artificial-intelligence-ai-action-plan.pdf.
Paine, Andre (2025). “Musical AI and Beatoven.ai to Build Fully Licensed Artificial Intelligence
   Platform for Music Creation”. Music Week. url: https://www.musicweek.com/digital/
   read / musical - ai - and - beatoven - ai - to - build - fully - licensed - artificial -
   intelligence-platform-for-music-creation/091000.
Puerto, Haritz et al. (2024). “Scaling Up Membership Inference: When and How Attacks Suc-
   ceed on Large Language Models”. arXiv preprint arXiv:2411.00154.
Roth, Emma (Aug. 2024). “Authors sue Anthropic for training AI using pirated books”. The
   Verge. url: https://www.theverge.com/2024/8/20/24224450/anthropic-copyright-
   lawsuit-pirated-books-ai.
Satvaty, Ali, Suzan Verberne, and Fatih Turkmen (2024). “Undesirable Memorization in Large
   Language Models: A Survey”. arXiv preprint arXiv:2410.02650.
Shi, Weijia et al. (2023a). Detecting Pretraining Data from Large Language Models. arXiv: 2310.
   16789 [cs.CL].
— (2023b). “Detecting pretraining data from large language models”. arXiv preprint
   arXiv:2310.16789.
Thornhill, John (2025). “Help is coming in the AI copyright wars”. Financial Times. url: https:
   //www.ft.com/content/b98979ba-6ae7-4490-97a9-127381440b1f.

                                              18
Whitwam, Ryan (2025). “Google joins OpenAI in pushing feds to codify AI training as fair
  use”. Ars Technica. url: https://arstechnica.com/google/2025/03/google- agrees-
  with-openai-that-copyright-has-no-place-in-ai-development/.
Zhang, Jie et al. (2024). “Membership inference attacks cannot prove that a model was trained
  on your data”. arXiv preprint arXiv:2409.19798.
Zhang, Jingyang et al. (2024). “Min-k%++: Improved baseline for detecting pre-training data
  from large language models”. arXiv preprint arXiv:2404.02936.
Zhao, Haiyan et al. (2024). “Explainability for large language models: A survey”. ACM Trans-
  actions on Intelligent Systems and Technology 15.2, pp. 1–38.

                                             19
A      Appendix

A.1      Additional Details About Our Dataset

We tested OpenAI’s models on a total of 34 books, but not all books were used for every model.
The table below lists the books used and their publication dates. For each model, we excluded
any data published in the year the model completed its training from our testing.

      Table 4. Detailed information about the books included in our dataset.
                                                    GPT-3.5 Turbo     GPT-4o Mini          GPT-4o
                 Title                  Date
                                                   Paragraph Count   Paragraph Count   Paragraph Count
     97 Things Every Information
                                      2021-09-14         —                315               314
 Security Professional Should Know
  AI-Powered Business Intelligence    2022-06-10        239               397               396
       Advancing into Analytics       2021-04-18         —                157               157
 Applied Machine Learning and AI
                                      2022-11-10        329               353               353
            for Engineers
           Azure Cookbook             2023-06-29         42                —                 —
       Building Green Software        2024-03-11        226               416               414
     Building Knowledge Graphs        2023-06-26        160                —                 —
 Building Recommendation Systems
                                      2023-12-11        311                —                 —
          in Python and JAX
      Building Solutions with the
                                      2023-01-06        283                —                 —
      Microsoft Power Platform
         C# 8.0 in a Nutshell         2020-05-12        335               335               334
           Cloud Native Go            2021-04-20         —                358               358
      Communicating with Data         2021-10-03         —                446               446
       Continuous Deployment          2024-07-25        584               584               582
     Data Quality Fundamentals        2022-09-02        447               447               447
    Deciphering Data Architectures    2024-02-07        363               477               477
     Delta Lake: Up and Running       2023-10-17        187                —                 —
 DevOps Tools for Java Developers     2022-04-15        304               467               464
    Distributed Tracing in Practice   2020-04-14        323               578               578
               FastAPI                2023-11-13         79                —                 —
        Genomics in the Cloud         2020-04-08        479               767               767

                                                   20
                                                             GPT-3.5 Turbo         GPT-4o Mini            GPT-4o
                Title                         Date
                                                            Paragraph Count      Paragraph Count     Paragraph Count
            Leading Lean                  2020-01-23               301                 486                  486
      Learning Digital Identity           2023-01-10               478                  —                    —
  Natural Language Processing with
                                          2020-06-25               135                 271                  271
             Spark NLP
            Policy as Code                2024-07-09               235                 335                  334
     Practical Natural Language
                                          2020-06-17               292                 410                  410
             Processing
         Programming C# 10                2022-08-05              1059                 1538                1538
 Prompt Engineering for Generative
                                          2024-05-16               262                 304                  304
                 AI8
   RESTful Web API Patterns and
                                          2022-10-17               276                 444                  444
         Practices Cookbook
   Scaling Machine Learning with
                                          2023-03-09               291                  —                    —
                Spark
      Security and Microservice
                                          2021-09-08               —                   452                  452
         Architecture on AWS
  Software Architecture: The Hard
                                          2021-10-25               —                   404                  404
                Parts
  The Customer-Driven Culture: A
                                          2020-03-10               219                 366                  366
           Microsoft Story
         Web API Cookbook9                2024-03-28               87                  109                  109
     Web Accessibility Cookbook           2024-06-17               123                 170                  170

Note: For GPT-4o, we use a sample of 11,375 paragraphs across 26 books, of which 9,300 are non-public and 2,075 are public.
Similarly, for GPT-4o Mini we use 11,386 paragraphs (9,308 non-public and 2,078 public) across 26 books. Finally, GPT-3.5
Turbo used 8,449 paragraphs, with 6,410 non-public and 2,039 public paragraphs across 28 books.

    In our study any books published in 2023 were excluded from tests involving GPT-4o and
GPT-4o Mini, while books published in 2021 were omitted from any tests involving GPT-3.5
Turbo.

    Table 5 displays the most common three-word phrases in the public and non-public
datasets. These phrasing differences reflect that the public text is typically extracted from the
first 1500 words of each chapter (with the exception, being chapters one and four of each book
  8 Excluded from testing.
  9 Excluded from testing.

                                                           21
    Table 5. There is a noticeable difference in phrasing between public and
                                 non-public text.
                             Public Split                          Non-Public Split
                        Phrase       Occurrences                 Phrase     Occurrences
                    in this chapter       138                as well as         455
                    as well as            115                one of the         449
                    one of the             99                be able to         444
                    be able to             89                the number of      436
                    a lot of               85                you want to        399
Note: Shows most frequent phrases of each data split. The most common phrase in the public dataset introduces a chapter,
likely because the public split primarily consists of the first 1,500 characters of each chapter.

where the entire chapter is public). The public portion of the dataset contains more language
introducing a chapter as it mostly consists of the first 1,500 words of each chapter.

    All paragraphs in Prompt Engineering for Generative AI and Web API Cookbook were excluded
from testing, originally to calibrate results. However, because we tested each paragraph across
all 24 permutations of the four answer options (4!=24), position bias is already fully accounted
for, making such calibration unnecessary. The two books remain excluded from all reported
AUROC scores and statistical tests.

A.2     AUROC Results

We found that there are various ways to calculate AUROC scores, some of which can lead to
significantly different results (see Figure 4 and Table 6). For example, Duarte et al. (2024)
calculated their scores at the book level by first computing the mean guessing score across all
paragraphs within each book. They then used these book level guessing rates to determine an
optimal threshold, ultimately converting each book into a binary prediction based on whether
it exceeded this threshold. This approach appeared to give a boost over doing the AUROC
calculation directly without thresholding first (shown in Figure 4). We calculated AUROC
scores using the following methods:

    • Papers Method for AUROC refers to the AUROC score approach from the DE-COP study

                                                          22
Figure 4. AUROC score is highly dependent on the data scale and method it is
                              measured with.

Note: Despite measuring many different AUROC variations we always had a similar pattern of GPT-4o demonstrating the
most knowledge, followed by GPT-3.5 Turbo and finally GPT-4o Mini showing the least recognition. See Tables: 1, 6, 7 and 8.

       (Duarte et al. 2024). First, the optimal threshold is determined based on Youden’s Index
       (TPR - FPR), (IBM 2024). Next, each book is given a binary value based on the optimal
       threshold. Finally, the AUROC score is computed on these binary predictions.

    • Book Level AUROC is calculated by averaging the identification rates across all para-
       graphs in a book and then computing the AUROC score using these averages.

    • Paragraph Level AUROC uses the identification rate for individual paragraphs to com-
       pute the AUROC score.

    • Balanced AUROC scores are derived similarly to the other AUROC methods but are cal-
       culated from 100 subsets, each containing equal proportions of data from before and

                                                           23
     after the cutoff date. The mean scores from these subsets are then reported.

                 Table 6. All AUROC Metrics by Data Split and Model.

                                                                  GPT-4o       GPT-4o Mini          GPT-3.5 Turbo
  All Paragraphs
  Papers Method for AUROC (Binary)                                  0.79             0.61                   0.65
  AUROC on Book Level                                               0.79             0.56                   0.58
  AUROC on Paragraph Level                                          0.63             0.49                   0.50
  Balanced AUROC Mean Using Papers Method                           0.82             0.65                   0.68
  Balanced AUROC Mean on Book Level                                 0.81             0.56                   0.60
  Balanced AUROC Mean on Paragraph Level                            0.64             0.49                   0.50
  Public Paragraphs
  Papers Method for AUROC (Binary)                                  0.69             0.64                   0.67
  AUROC on Book Level                                               0.64             0.55                   0.64
  AUROC on Paragraph Level                                          0.60             0.48                   0.51
  Balanced AUROC Mean Using Papers Method                           0.71             0.65                   0.69
  Balanced AUROC Mean on Book Level                                 0.64             0.53                   0.63
  Balanced AUROC Mean on Paragraph Level                            0.60             0.48                   0.51
  Non-Public Paragraphs
  Papers Method for AUROC (Binary)                                  0.84             0.66                   0.62
  AUROC on Book Level                                               0.82             0.56                   0.54
  AUROC on Paragraph Level                                          0.64             0.50                   0.50
  Balanced AUROC Mean Using Papers Method                           0.84             0.67                   0.63
  Balanced AUROC Mean on Book Level                                 0.82             0.56                   0.54
  Balanced AUROC Mean on Paragraph Level                            0.64             0.50                   0.50
    Note: Shows all the AUROC scores that we calculated (see Table 1 for sample sizes). Figure 4 visualizes this table.

   Unless otherwise specified, the AUROC scores reported in this paper are book level AUROC.
Throughout the paper we refer repeatedly to book level AUROC. However, when testing for
robustness we found that the 95% bootstrapped confidence intervals were very large at the
book level (see Table 7).

   This is likely attributable to our limited book count. We analyzed a sample of 34 books,
each containing thousands of paragraphs. This small number of titles leads to a very wide
bootstrapped confidence interval for the book level AUROC scores (see Table 7). Although
not ideal, this outcome is expected if some books in our sample were part of the training data

                                                           24
  Table 7. Book Level AUROC Scores with Bootstrapped Confidence Intervals
                              by Data Split.
                            Model                 Data-Split        Book Level AUROC
                                                  All               0.79 (0.53, 0.96)
                            GPT-4o                Public            0.64 (0.36, 0.93)
                                                  Non-Public        0.82 (0.60, 0.96)
                                                  All               0.56 (0.25, 0.84)
                            GPT-4o Mini           Public            0.55 (0.20, 0.84)
                                                  Non-Public        0.56 (0.28, 0.83)
                                          All                       0.58 (0.33, 0.83)
                            GPT-3.5 Turbo Public                    0.64 (0.39, 0.86)
                                          Non-Public                0.54 (0.28, 0.77)
Note: We performed hierarchical bootstrapping using 1,000 bootstraps over all books not published in the year of a model’s
cutoff date (see Table 4). To perform hierarchical bootstrapping, we repeatedly sampled random books and then random
paragraphs within each book. See Table 1 for sample sizes.

while others were not. Since we approximate the in-dataset and out-of-dataset groups with
a small sample, any ‘mislabeled’ data – data that was assumed to be in-dataset but was not
actually included – can disproportionately affect and skew the results.

     Table 8. Paragraph Level AUROC Scores with Bootstrapped Confidence
                             Intervals by Data Split
                        Model                 Data-Split        Paragraph Level AUROC
                                              All               0.63 (0.62, 0.65)
                        GPT-4o                Public            0.60 (0.57, 0.63)
                                              Non-Public        0.64 (0.63, 0.66)
                                              All               0.49 (0.48, 0.51)
                        GPT-4o Mini           Public            0.48 (0.45, 0.51)
                                              Non-Public        0.50 (0.48, 0.51)
                                      All                       0.50 (0.49, 0.52)
                        GPT-3.5 Turbo Public                    0.51 (0.48, 0.54)
                                      Non-Public                0.50 (0.48, 0.51)
Note: We performed bootstrapping using 1000 bootstraps over all paragraphs not published in the year of a model’s cutoff
date. See Table 1 for sample sizes.

                                                           25
   In contrast, performing bootstrap at the paragraph level – where data is pooled across books
– yields significantly smaller bootstrapped confidence intervals across all models (see Table
8), indicating that increasing the number of books would likely help tighten the book level
bootstrapped confidence intervals.

A.3      Prompts and Settings Used for Tested Models

To test the model’s ability to differentiate between member and non-member data, we used a
modified version of the prompts presented in Duarte et al. 2024. An example prompt is shown
below.

System Prompt:

You are a helpful assistant. You must answer using only the
provided options A, B, C, or D, you may not decline to answer.

User Prompt:

Question: Which of the following passages is verbatim from
the "97 Things Every Information Security Professional
Should Know" book by Christina Morillo?

Options:
A. Learn with a community. I’ve personally found that I’ve
developed new and existing skills much faster (by a
magnitude of months) when I’ve joined a community of
learners than when I was trying to learn the same skills
alone. By attending local and online user groups,
conferences, and other events, you can discover new
concepts, hone new skills, and network with possible
future colleagues. Also, in a community, you will gain a

                                              26
more holistic perspective of information security and a
more complete picture of how others are managing
successful information security programs.

B. Connect with fellow learners. From my experience,
acquiring and improving abilities has been significantly
quicker (saving several months) when participating in group
learning compared to solo studying. Going to regional and
virtual meetups, seminars, and similar gatherings helps
you explore fresh ideas, develop capabilities, and build
relationships with potential workmates. Furthermore,
learning within a group provides broader insights into
cybersecurity and better understanding of how various
organizations implement effective security initiatives.

C. Join a learning group. Based on my observations,
mastering both new and current abilities happens much more
rapidly (reducing learning time by months) when I’m part
of a learning circle versus studying independently. Through
participation in area-based and internet-hosted gatherings,
symposiums, and other meetings, you’ll encounter different
concepts, sharpen your abilities, and connect with
prospective professional contacts. Additionally, group
involvement offers deeper understanding of security
practices and clearer insights into successful security
program management across organizations.

D. Engage in collaborative learning. My personal journey
shows that skill acquisition and enhancement occurs

                                      27
substantially faster (cutting months off learning time)
within group settings rather than individual efforts. By
taking part in both physical and digital group meetings,
industry events, and related activities, you can learn new
approaches, improve your capabilities, and establish
connections with future professional peers. Moreover,
group settings provide comprehensive knowledge about
information security and valuable examples of how different
teams run successful security operations.

Answer:

    Our prompt differs slightly from the prompt used in the DE-COP paper. We changed it
to help ensure that the model follows the instructions and returns the tokens needed in the
limited token log probabilities that OpenAI provides.

Model settings:

{
     "max_tokens": 1,
     "temperature": 0,
     "seed": 2319,
     "logprobs": True,
     "logit_bias": {32: +100, 33: +100, 34: +100, 35: +100},
     "top_logprobs": 20
}

    The exact models tested were as follows: gpt-4o-2024-08-06, gpt-4o-mini-2024-07-18 and
gpt-3.5-turbo-1106.

                                             28
A.4    Prompts and Settings Used for Paraphrase model

We used Claude 3.5 Sonnet to generate paraphrases from the O’Reilly Media books. An exam-
ple prompt is shown below.

User Prompt:

Rewrite this entire text (all sentences with no exception)
expressing the same meaning using different words. Aim to keep the
rewriting similar in length to the original text. Do it three
times. The text to be rewritten is identified as <Example A>.
Format your output as:
Example B: <insert paraphrase B>
Example C: <insert paraphrase C>
Example D: <insert paraphrase D>
-
Example A: In general, a soft trade-off exists between active learning that’s
useful for maximally improving your model globally and active
learning that’s useful for maximizing the likelihood that a user can
and will rate a particular item. Let’s look at one particular example
that uses both.

Model settings:

{
      "temperature": 0.1,
      "model":"claude-3.5-sonnet"
}

                                           29
