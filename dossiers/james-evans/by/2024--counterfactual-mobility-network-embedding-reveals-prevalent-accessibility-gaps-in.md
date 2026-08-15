---
title: "Counterfactual mobility network embedding reveals prevalent accessibility gaps in U.S. cities"
person: james-evans
section: by
type: journal-article
year: 2024
date: 2024-01-09
venue: "Humanities and Social Sciences Communications"
authors: "Yunke Zhang, Fengli Xu, Lin Chen, Yuan Yuan, James Evans, Luis Bettencourt, Yong Li"
source_url: https://doi.org/10.1057/s41599-023-02570-5
openalex_id: https://openalex.org/W4390725622
retrieved: 2026-08-13
content: full-text
notes: "full text via the OpenAlex Content API (content.openalex.org)"
---

# Counterfactual mobility network embedding reveals prevalent accessibility gaps in U.S. cities

## Full text

Supplementary Information for
Counterfactual mobility network embedding reveals
prevalent accessibility gaps in U.S. cities
Yunke Zhang1,+ , Fengli Xu1,+ , Lin Chen2 , Yuan Yuan1 , James Evans3, 4 , Luis
Bettencourt4, 5, 6 , and Yong Li1, *
1 Beijing National Research Center for Information Science and Technology (BNRist), Department of Electronic

Engineering, Tsinghua University, Beijing, People’s Republic of China
2 Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Hong Kong
SAR, People’s Republic of China
3 Department of Sociology, University of Chicago, Chicago, Illinois, USA
4 Santa Fe Institute, Santa Fe, New Mexico, USA
5 Mansueto Institute for Urban Innovation, University of Chicago, Chicago, Illinois, USA
6 Department of Ecology and Evolution, University of Chicago, Chicago, Illinois, USA
* corresponding author: liyong07@tsinghua.edu.cn
+ these authors contributed equally to this work

Supplementary Notes
S1 Implementation Details
S1.1 Counterfactual Random Walk
In each MSA, we construct an urban mobility network comprising nodes that represent POI categories, POIs, neighborhoods,
and demographic features. For every category Q, we sample 200,000 random walks, denoted as Q → Pi → Co → o, to observe
outcomes represented by Co . It is important to note that we are interested in five demographic features. Therefore, for each
demographic feature, we sample an alternative neighborhood Ca along with its corresponding alternative outcome a. In total,
we randomly sample one million pairs of observed-alternative outcomes for each category within each MSA.
S1.2 Network Embedding
In each MSA, we learn an 64-dimensional embedding vector for each of the following entities: four POI categories, all POIs,
all neighborhoods, and all treatment levels of five neighborhood demographic features. We use the Adam optimizer to minimize
the loss function introduced in the Main Text. The spatial threshold σs is set to 2.5 kilometers, and the strength of regularization
is 0.0001 and 0.01 for spatial and demographic feature continuity. During the training, we set the batch size as 10,000 and
trained for 10,000 epochs. The codes are implemented with PyTorch 1.7 and run on a Linux server with NVIDIA RTX 2080 Ti.
Codes for reproducing the CRANE algorithm are available at https://github.com/tsinghua-fib-lab/CRANE.
S1.3 Predictive Analysis
For the within-city prediction task, we conducted a five-fold analysis, repeating the following procedure five times for each
POI category in every MSA. We randomly selected 80% of the neighborhoods as the training set, where we performed
counterfactual random walks and learned network embeddings to obtain embedding vectors for each category and each level of
demographic features. For our Multilayer Perceptron (MLP) regression model, we combined the raw demographic features of
each neighborhood (5 dimensions) with the dot products between their corresponding L(T )’s embedding vectors and all four
category embedding vectors (20 dimensions) as input. The model’s output represents the urban facility accessibility of the
neighborhood. Specifically, we utilized the “MLPRegressor” function from the Python package “scikit-learn”, which includes
two hidden layers with dimensions of 32 and 16, respectively, using the sigmoid activation function. To evaluate the model’s
performance, we tested it on the remaining 20% test set of neighborhoods, calculating the average explained variance as the
performance metric.
For the cross-city prediction task, we performed counterfactual random walks and learned network embeddings on the
entire urban mobility network consisting of all neighborhoods in an MSA. Then we also combined the raw demographic

1

features of each neighborhood with the dot products between their corresponding L(T )’s embedding vectors and all four
category embedding vectors to fit an MLP regression model. Subsequently, during the test stage, we applied the learned
vectors in conjunction with the demographic characteristics of neighborhoods within the Chicago MSA to predict urban facility
accessibility for those specific neighborhoods.

S2 Credibility of Treatment Effects
The goal of PSM is to balance covariates across different treatment levels L(T ). Under this scenario, differences in mobility
patterns can be attributed to differences in L(T ). We report the average relative covariate differences before and after propensity
score matching for each treatment variable across six MSAs in Supplementary Figure S2. The covariate differences are lower
than 2% after PSM, demonstrating the effectiveness of PSM in balancing covariate and deriving debiased causal effects.
Specifically, we define relative covariate differences after matching as the relative disparities in the average values of
covariates between two groups: the high-treatment group, composed of neighborhoods with higher treatment levels in each
matched pair, and the low-treatment group, consisting of neighborhoods with lower treatment levels in each pair. Relative
covariate differences before matching reflect the correlation between treatment and covariates, indicating the relative disparities
in average covariate values between the neighborhoods with the highest and lowest treatment levels.
We observed that propensity score matching (PSM) significantly improved the balance of covariates. Prior to matching,
relative covariate differences could exceed 50%, but following matching, they all decreased to less than 2%, as indicated by
the red vertical line. This substantial reduction in covariate differences demonstrates the effectiveness of PSM in achieving
covariate balance. This, in turn, enhances the reliability of PSM in identifying urban mobility inequalities and analyzing
treatment effects.

S3 Complexity analysis
Here we analyze the time complexity of propensity score matching and the counterfactual random walk to demonstrate the
efficiency of the CRANE method. In an MSA with N census block groups, the PSM approach first fits an ordinal regression
model to estimate propensity scores. The complexity of calculating propensity for all CBG is O(N). Each CBG is then matched
with another CBG with the closest distance defined by propensity score and treatment level, which takes O(N). The matching
procedure takes a complexity of O(N 2 ) in total.
In the counterfactual random walk stage, we randomly sample a POI from the starting category, then sample a CBG that has
visited the sampled POI, and finally sample an alternative CBG that has covariates identical to the sampled CBG. Each step in
the counterfactual random walk is a sampling from a discrete probability distribution. The corresponding time complexity can
be reduced to O(1) if we generate an alias table for each POI category, POI, and covariates combination in advance. In Section
3.2 of the Main Text, we demonstrate that the counterfactual random walk can well approximate PSM with a sample size over
100,000, which is often less than N 2 in big MSAs. Therefore, the counterfactual random walk can efficiently approximate
PSM.

2/6

Supplementary Figures

E

A

B

C

D

F

G

Figure S1. Geographical distribution of neighborhood’s features. A-G Mobility frequency and demographic features at
the neighborhood level in the New York metropolitan statistical area. Colors indicate the quintile of the neighborhood’s
features.

3/6

A

B

D

C

E

Figure S2. Effect of propensity score matching on covariate balance. A-E The relative differences of average confounding
variables on high-dose and low-dose groups for each treatment variable. The propensity score matching method can reduce
relative differences from over 50% to less than 2%.

4/6

Supplementary Tables
Table S1. The correlation between demographic feature and mobility behavior in Los Angeles MSA.

NM2019
∆M
Art%
Sports %
Education %
Health %

Female%

White%

Bachelor%

Income

Disability%

-0.014
-0.033**
-0.001
0.010
0.055***
0.065***

0.160***
0.071***
0.199***
0.410***
0.084***
0.008

0.248***
0.241***
0.417***
0.697***
0.085***
-0.019

0.287***
0.202***
0.337***
0.587***
0.243***
-0.033**

-0.098***
-0.111***
-0.20***
-0.303***
0.007
0.090***

* p < 0.05; ** p < 0.01; *** p < 0.001.

Table S2. The correlation between demographic feature and mobility behavior in Chicago MSA.

NM2019
∆M
Art%
Sports %
Education %
Health %

Female%

White%

Bachelor%

Income

Disability%

0.009
0.046***
-0.017
-0.071***
-0.046***
0.106***

0.152***
-0.058***
0.141***
0.492***
0.330***
-0.115***

0.192***
0.304***
0.399***
0.733***
0.083***
-0.212***

0.262***
0.189***
0.24***
0.687***
0.310***
-0.198***

-0.104***
-0.149***
-0.221***
-0.387***
-0.046***
0.215***

* p < 0.05; ** p < 0.01; *** p < 0.001.

Table S3. The correlation between demographic feature and mobility behavior in Dallas MSA.

NM2019
∆M
Art%
Sports %
Education %
Health %

Female%

White%

Bachelor%

Income

Disability%

-0.002
-0.014
0.001
0.016
0.042**
0.080***

0.231***
0.016
0.115***
0.282***
0.188***
-0.049**

0.284***
0.405***
0.431***
0.654***
0.211***
-0.049**

0.376***
0.354***
0.351***
0.635***
0.366***
-0.073***

-0.136***
-0.254***
-0.19***
-0.325***
-0.012
0.162***

* p < 0.05; ** p < 0.01; *** p < 0.001.

5/6

Table S4. The correlation between demographic feature and mobility behavior in Houston MSA.

NM2019
∆M
Art%
Sports %
Education %
Health %

Female%

White%

Bachelor%

Income

Disability%

0.051**
0.030
0.004
0.036
0.058**
0.116***

0.259***
-0.006
0.044*
0.204***
0.196***
-0.066***

0.260***
0.455***
0.314***
0.753***
0.208***
0.072***

0.336***
0.35***
0.201***
0.686***
0.328***
-0.002

-0.092***
-0.281***
-0.088***
-0.359***
-0.018
0.029

* p < 0.05; ** p < 0.01; *** p < 0.001.

Table S5. The correlation between demographic feature and mobility behavior in Washington DC MSA.

NM2019
∆M
Art%
Sports %
Education %
Health %

Female%

White%

Bachelor%

Income

Disability%

0.019
0.051**
0.015
-0.007
-0.017
0.074***

-0.14***
-0.257***
0.166***
0.445***
0.291***
-0.082***

-0.046**
0.124***
0.397***
0.591***
0.047**
-0.177***

0.042*
0.044**
0.190***
0.579***
0.298***
-0.189***

-0.000
-0.069***
-0.158***
-0.258***
0.035*
0.185***

* p < 0.05; ** p < 0.01; *** p < 0.001.

Table S6. Regression coefficients between each demographic feature and its proximity with POI categories in the embedding
space. Significance levels of regression coefficients are listed.
New York

MSAs
Category
Demographic
Female%
White%
Bachelor%
Income
Disability%

Sports%

Edu%

Health%

Art%

Sports%

Edu%

Health%

Art%

Sports%

Edu%

Health%

0.023
(***)
-0.050
(**)
0.033
(***)
-0.031

0.018
(***)
0.036
(*)
0.031
(*)
0.018

0.030

0.003

0.014

0.005

-0.001

0.000

-0.002

-0.001

0.014

0.021
(*)
-0.027

0.007

0.015

-0.006

-0.005

-0.004

0.000

0.025

-0.011

0.039
(*)
0.011

0.036
(*)
-0.010
0.016

-0.014

0.025
(***)

0.002

0.044
(**)
0.025
(*)
-0.024
(***)

0.041
(*)
0.054
(***)
0.016

-0.006

-0.017

0.024
(**)
0.047
(**)
0.002

0.018
(**)
-0.001

0.001

-0.000

-0.013

0.002

0.001

Female%
White%
Bachelor%
Income
Disability%

0.032
(*)
0.016
(**)

0.001
0.016
(***)

Dallas
Category

Chicago

Art%

MSAs
Demographic

Los Angeles

-0.016

-0.026
(***)

Houston

-0.016

Washington DC

Art%

Sports%

Edu%

Health%

Art%

Sports%

Edu%

Health%

Art%

Sports%

Edu%

Health%

-0.014

0.001

-0.010

0.011

-0.002

0.010

0.005

0.021

0.012

0.019

0.003

0.018

0.018

0.029

-0.003

-0.011

-0.002

0.009

0.021

-0.027

-0.007

0.042
(***)
0.022

0.003

0.004

0.003

-0.002

0.044

-0.004

0.062
(**)
0.011

0.007

0.019

0.015

0.006

-0.004

0.030
(**)
0.006

-0.000

0.011

0.069
(***)
0.041
(*)
-0.009

0.007

0.026
(**)
0.004

0.059
(**)
0.015

0.061
(**)
-0.013

-0.017

0.051
(**)
0.032
(*)
-0.003

0.047
(*)
0.036
(***)
0.034

-0.025

0.008

-0.008

* p < 0.2; ** p < 0.1; *** p < 0.05.

6/6
