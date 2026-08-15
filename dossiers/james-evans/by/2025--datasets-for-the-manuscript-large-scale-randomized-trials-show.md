---
title: "Datasets for the manuscript \"Large-scale randomized trials show no evidence of gender bias in evaluating scientific abstracts\""
person: james-evans
section: by
type: report
year: 2025
date: 2025-01-01
venue: "Zenodo (CERN European Organization for Nuclear Research)"
authors: "Ferreira Sousa, Sandro, Aiello, Luca, Chen, Zhilong, Evans, James, Sinatra, Roberta"
source_url: https://doi.org/10.5281/zenodo.17579132
openalex_id: https://openalex.org/W7104875833
retrieved: 2026-08-13
content: abstract-only
notes: ""
---

# Datasets for the manuscript "Large-scale randomized trials show no evidence of gender bias in evaluating scientific abstracts"

## Abstract (only openly available portion)

Data for the manuscript “Large-scale randomized trials show no evidence of gender bias in evaluating scientific abstracts” The code to produce and process these files can be obtained in the Github repository github.com/BiasExplained/gender-trial-paper List of files keywords_analysis.zip: Contains the post-processed keywords after BERT. Format: See Document_Format.md in the compressed folder for details. sciofsci_pilot_June-19-2023_00.49.csv: Contains the responses from the soft launch pilot for the questions of likelihood to cite and estimated gender. Format: ResponseId: Response random unique ID estimated_gender: Gender selected by participants for the question about what gender the author of the abstract was egroup: Treatment condition [TFemale, TMale, Control] cite_likelyhood: Text of the 6-point Likert scale choice for the question about the likelihood to cite the paper cite_likelyhood_num: Numeric transformation of the 6-point Likert scale sign: Text of aggregated liker scale answers [Unlikely, Likely] sign_num: Numeric value for the sign text [-1, 1] doi_list.txt: List containing the DOI of publications considered in the experiment after enrighment with Web Of Science data. abstracts.zip: Contains json files with the abstracts and parameters used to generate them. Format: iter: parameter id with the format {temperature}_{presence}_{frequency} keywords: keyword pairs used to prompt the model prompt: prompt used (see paper Supplementary Information for details) raw: model output text temperature: temperature parameter presence: presence parameter frequency: frequency parameter title: title text extracted from the model raw output abstract: abstract text extracted from the model raw output MTurk_batch_4951026_results.csv CSV file containing the results from the MTurk human annotation of abstracts generated on an earlier version of the GPT model (see an explanation of the results in the Paper’s Supplementary Information for details). sciofsci_double-effect_-_Live_April_15,_2024_07.14_anonymised.csv: Contains the responses from the main trial launch for all questions. See file for all fields included and the preprocessing_results.py script available in the github repository for more details.
