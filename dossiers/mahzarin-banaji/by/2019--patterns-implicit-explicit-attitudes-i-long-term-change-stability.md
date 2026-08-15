---
title: "Patterns of Implicit and Explicit Attitudes: I. Long-Term Change and Stability From 2007 to 2016"
person: mahzarin-banaji
section: by
type: journal-article
year: 2019
date: 2019-01-03
venue: "Psychological Science"
authors: "Tessa E. S. Charlesworth; Mahzarin R. Banaji"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/2019_Charlesworth_PS.pdf
doi: https://doi.org/10.1177/0956797618813087
openalex_id: https://openalex.org/W2904897888
cited_by_count: 475
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard site, extracted with pdftotext -layout. Title-overlap check 0.73."
---

# Patterns of Implicit and Explicit Attitudes: I. Long-Term Change and Stability From 2007 to 2016

## Full text

813087
research-article2019
                       PSSXXX10.1177/0956797618813087Charlesworth, BanajiPatterns of Attitude Change


                                                                                                                                                                           ASSOCIATION FOR
                                Research Article                                                                                                            PSYCHOLOGICAL SCIENCE
                                                                                                                                                            Psychological Science

                                Patterns of Implicit and Explicit                                                                                           2019, Vol. 30(2) 174­–192
                                                                                                                                                            © The Author(s) 2019
                                                                                                                                                            Article reuse guidelines:
                                Attitudes: I. Long-Term Change and                                                                                          sagepub.com/journals-permissions
                                                                                                                                                            DOI:    10.1177/0956797618813087
                                                                                                                                                            https://doi.org/10.1177/0956797618813087

                                Stability From 2007 to 2016                                                                                                 www.psychologicalscience.org/PS


                                Tessa E. S. Charlesworth                                               and Mahzarin R. Banaji
                                Department of Psychology, Harvard University


                                Abstract
                                Using 4.4 million tests of implicit and explicit attitudes measured continuously from an Internet population of U.S.
                                respondents over 13 years, we conducted the first comparative analysis using time-series models to examine patterns
                                of long-term change in six social-group attitudes: sexual orientation, race, skin tone, age, disability, and body weight.
                                Even within just a decade, all explicit responses showed change toward attitude neutrality. Parallel implicit responses
                                also showed change toward neutrality for sexual orientation, race, and skin-tone attitudes but revealed stability over
                                time for age and disability attitudes and change away from neutrality for body-weight attitudes. These data provide
                                previously unavailable evidence for long-term implicit attitude change and stability across multiple social groups; the
                                data can be used to generate and test theoretical predictions as well as construct forecasts of future attitudes.

                                Keywords
                                implicit attitude change, implicit association test, long-term change, time-series analysis, open data, open materials

                                Received 2/9/18; Revision accepted 8/27/18


                                The structure of the human brain has remained                                           measures), and low perceived societal priority (resulting
                                unchanged over thousands of years, but the products                                     in low discussion and elaboration).
                                of the human brain—thoughts (beliefs) and feelings                                         Recently, attention has turned to the conditions for
                                (attitudes)—are continually changing. Even within the                                   implicit attitude change. Initially hypothesized to be
                                relatively short history of the United States, examples                                 largely immutable (Bargh, 1999), implicit attitudes have
                                of change on societally significant attitudes are easily                                since revealed short-term malleability following targeted
                                found. For instance, from Puritan America through the                                   interventions (Dasgupta, 2013; Lai et al., 2014). Yet the
                                19th century, same-sex relations were punishable by                                     question of long-term implicit attitude change remains.
                                death; today, same-sex marriage is legal across the United                              With some exceptions (Devine, Forscher, Austin, & Cox,
                                States. In 1958, only 4% of White Americans approved of                                 2012; Gawronski, Morrison, Phills, & Galdi, 2017; McNulty,
                                Black–White marriages; today, 87% of White Americans                                    Baker, & Olson, 2014; McNulty, Olson, Jones, & Acosta,
                                approve (Newport, 2013).                                                                2017), attempts to demonstrate long-term implicit atti-
                                   The study of attitudes and attitude change is so fun-                                tude change have been unsuccessful (Lai et al., 2016)
                                damental to social psychology that every Handbook of                                    or failed to replicate (Forscher, Mitamura, Dix, Cox, &
                                Social Psychology since 1935 has included at least one                                  Devine, 2017). Moreover, investigations have largely
                                chapter on the topic (Banaji & Heiphetz, 2010). As a                                    focused on measuring single attitudes within an indi-
                                result, much is known about the conditions that induce                                  vidual; comparisons of long-term implicit attitude change
                                change in explicit, self-reported attitudes (Albarracin &
                                Vargas, 2010). Specifically, theories of attitude strength
                                and change (Petty & Krosnick, 1995) predict that resis-
                                                                                                                        Corresponding Author:
                                tance to explicit attitude change will cooccur with fea-                                Tessa E. S. Charlesworth, Harvard University, Department of
                                tures such as high overall bias, strong intra-attitudinal                               Psychology, William James Hall, 33 Kirkland St., Cambridge, MA 02138
                                linkages (indicated by high correlations among attitude                                 E-mail: tet371@g.harvard.edu


Patterns of Attitude Change                                                                                         175

across multiple attitudes at the population level remain     overcomes past limitations of almost exclusive study of
unexplored.                                                  Black–White racial attitudes and provides information on
                                                             generalizability of change. Differences in rates of change
                                                             across attitudes can also help rule out alternative expla-
Advantages of the Approach
                                                             nations that would equally affect all attitudes, such as
This project examines the possibility of long-term           increasing awareness or test practice. Furthermore, com-
implicit attitude change using data from the Project         parisons across attitudes can test predictions regarding
Implicit demonstration website (http://implicit.harvard      features of implicit attitudes that cooccur with change.
.edu), which has collected two decades of continuous         This project examines predictions from explicit attitude
data from volunteers worldwide, yielding more than 20        theories (Petty & Krosnick, 1995) that implicit attitude
million tests across 14 attitudes/stereotypes. We used a     stability will cooccur with higher bias, higher implicit–
subset of these data involving 4 million tests that were     explicit correlations, and lower perceived societal prior-
collected continuously for 10 years across six social-       ity (indicated by lower frequency of online searches).
group attitudes (sexuality, race, skin tone, age, disabil-      Finally, this project introduces analytic improvements
ity, body weight), measured at the population level and      over previous studies using the same database (Sawyer
analyzed with time-series models. This approach can          & Gampa, 2018; Schmidt & Axt, 2016; Schmidt & Nosek,
newly address whether, and if so how, long-term change       2010; Westgate, Riskind, & Nosek, 2015). Past studies
emerges in explicit and implicit attitudes.                  relied on linear multiple regressions—a model class
    Previous studies of attitude change have used within-    that assumes linearity and independence of observa-
persons repeated measures designs, ensuring strong           tions (i.e., no autocorrelations)—applied to data that
internal validity but typically involving small samples,     violate both assumptions, thus opening the possibility
measurement of single attitude categories, and two dis-      of spurious conclusions about change. Furthermore,
crete measures obtained within a brief period of time.       multiple regression is not designed to produce forecasts,
An alternative approach, following social-survey meth-       an unnecessary limitation given theoretical and practical
ods, measures attitudes from different respondents           interest in predicting attitude trends. The current project
across time, enabling large amounts of data to be col-       employs autoregressive-integrated-moving-average
lected continuously over years without concern for           (ARIMA) time-series models (Cryer & Chan, 2008) to
participant fatigue or practice effects. In giving up tra-   address these concerns. There is growing appreciation
ditional within-persons measurement, we gain a singu-        that psychological data will benefit from adopting pre-
lar opportunity to observe population-level change with      dictive machine-learning analyses (Yarkoni & Westfall,
continuous measurement across a decade.                      2017), particularly when researchers are investigating
    Recently, such a population-level focus has been         the mechanics of cultural change (Varnum & Grossmann,
used to predict consequential outcomes (e.g., racial         2017).
disparities in lethal force; Hehman, Flake, & Calanchini,
2017) as well as to reconsider the theoretical nature of
implicit attitudes and their capacity for change (Payne,     Method
Vuletich, & Lundberg, 2017). Indeed, under this new
perspective, population-level implicit attitudes are
                                                             Data source
argued to be relatively more stable than individual-level    Data, including respondents’ zip codes, were retrieved
attitudes because of greater stability in a culture than     from the Project Implicit demonstration website (https://
in an individual’s daily experiences. Moreover, it should    implicit.harvard.edu/). Cleaned data used in the present
be preceded by situational change, including demo-           study (without zip codes) are publicly available at
graphic, legislative, or explicit attitude change.           https://osf.io/px8h3/; raw data (without zip codes), as
    However, explicit-preceding-implicit attitude change     well as further details about the website and test materi-
is just one possible implicit–explicit relationship that     als, are publicly available at https://osf.io/t4bnj/. All
has been documented in individual-level attitudes            respondents were visitors to the Project Implicit website
(Gawronski & Bodenhausen, 2006). Other patterns,             who provided informed consent and selected an implicit
including implicit-preceding-explicit, bidirectional, and    association test (IAT) from among the following: sexual-
unrelated change, may emerge and may differ across           ity, race, skin tone, age, disability, and body weight.
attitude targets. These data offer the first opportunity     For all tests, the demographic questions, explicit mea-
to empirically examine patterns of implicit–explicit         sures, and IAT were presented to respondents in ran-
change at the population level.                              dom order. Data inclusion began January 1, 2004, and
    Additionally, this project compared change across        ended December 31, 2016, for a total of 13 years. The
social-group attitudes of sexuality, race, skin tone, age,   fully available data from 2004 through 2016 were used
disability, and body weight. Including six attitudes         for analyses of means and correlations. However,


176                                                                                                  Charlesworth, Banaji

because of changes in the recording of explicit attitudes       respondents per month (see Table S2 in the Supplemen-
and demographics prior to 2007, only data collected             tal Material).
after January 1, 2007, were available for the time-series          Overall, the sample had a mean age of 27.46 years
models.                                                         (SD = 11.91); 65.88% identified as female, 72.24% identi-
   Body-weight and skin-tone IATs included missing              fied as White, 10.53% identified as Black or African
data because no demographics or primary measures                American, 0.74% identified as American Indian, 5.09%
(IATs, explicit measures) were collected in particular          identified as Asian, 1.88% identified as Black/White
months. Missing monthly averages for these tests were           biracial, 4.85% identified as other biracial, and 4.99%
imputed using seasonal decomposition with linear                identified as other or unknown; and 91.26% reported
interpolation (see Section 8 in the Supplemental Mate-          having completed a high school education or higher
rial available online). Additionally, stimuli for the body-     and 86.26% reported having completed a college educa-
weight IAT changed from face images to body-figure              tion or higher. In addition, 45.98% identified as slightly,
silhouettes in April 2010, resulting in two subsets of          moderately, or strongly liberal; 25.77% as slightly, mod-
data (figure-stimuli test and face-stimuli test). Thus, data    erately, or strongly conservative; and 28.25% as politi-
from both the recent figure-stimuli test (April                 cally neutral. Table S3 in the Supplemental Material
2010–December 2016) and the early face-stimuli test             provides test-specific demographic distributions.
(March 2004–October 2011) are reported to account for
the loss of early data in the figure-stimuli test.
   Scores on the IAT were computed using the revised
                                                                Materials
scoring algorithm (Greenwald, Nosek, & Banaji, 2003).           IAT. The IAT (Greenwald, McGhee, & Schwartz, 1998)
Respondents whose scores fell outside of the conditions         is a computerized task comparing reaction times to cate-
specified in the scoring algorithm did not have a com-          gorize paired concepts (in this case, social groups, e.g.,
plete IAT D score and were therefore excluded from              young vs. elderly) and attributes (in this case, valence
analyses. Restricting the analyses to only complete IAT         categories, e.g., good vs. bad). To sample the test, visit
D scores resulted in an average retention of 92% of the         https://implicit.harvard.edu/implicit/takeatest.html.
complete sessions across tests. The sample was further          Respondents were presented with target stimuli (e.g.,
restricted to include only respondents from the United          images of young and old faces, as well as good words,
States to increase shared cultural understanding of atti-       such as joyful and friend, and bad words, such as evil
tude categories. Finally, the sample was restricted to          and poison), which were categorized into one of four
include only respondents with complete explicit                 groups (e.g., young, old, good, or bad). Average response
measures and demographic information on age, gender,            latencies in correct categorizations were compared across
race/ethnicity, political ideology, education, and              two paired blocks in which participants categorized con-
attitude-specific variables of sexuality, weight, and dis-      cepts and attributes with the same response keys. For
ability status. After these additional restrictions, an aver-   illustration, in the age IAT, response latencies are com-
age of 62% of complete sessions remained across tests           pared across blocks in which (a) young + good have the
(for test-specific retentions, see Table S1 in the Supple-      same key and old + bad have the same key and (b)
mental Material). Supplemental analyses indicated that          young + bad and old + good have the same keys. Faster
means and correlations (see Table S5.1 in the Supple-           responses in the paired blocks are assumed to reflect a
mental Material), as well as patterns of change over            stronger association between those paired concepts and
time (see Table S5.2 in the Supplemental Material),             attributes. In all tests, positive IAT D scores indicate a
were consistent for data without any exclusions (beyond         relative preference for the typically preferred group (in
having a complete IAT score), indicating that the               this example, young people). All IATs on the Project
excluded participants do not substantively alter the            Implicit demo website use a standard seven-block format
conclusions.                                                    as described by Greenwald and colleagues (2003), with
                                                                the order of the two paired blocks randomized across
                                                                respondents.
Sample demographics
Across all attitudes, a total final sample of 4,393,362         Explicit preference. Explicit attitudes before 2007 were
completed tests was obtained after retaining the maxi-          assessed on a 5-point Likert-type scale from −2 to 2, with
mum possible number of completed tests from U.S.                higher scores indicating bias in favor of the typically pre-
respondents between 2004 and 2016. The unprecedented            ferred group (e.g., “I strongly prefer young people to old
size of this sample and continuous measurement ensures          people”) and lower scores indicating the reverse bias
that the aggregated estimates for each month are derived        (e.g., “I strongly prefer old people to young people”).
from reliably large samples with a median of 3,760              Explicit attitudes from 2007 onward were assessed on a


Patterns of Attitude Change                                                                                                  177

7-point Likert-type scale ranging from −3 to 3, with higher       variation across time, resulting in poor model fit.
and lower scores reflecting the same preferences as               Indeed, the median R2 from multiple regressions with
above. In both cases, the midpoint of 0 represented equal         predictors analogous to those of previous studies (i.e.,
liking of both groups.                                            time, demographic covariates, and time-by-covariate
                                                                  interactions; see Schmidt & Axt, 2016; Schmidt & Nosek,
Demographic variables. Respondents indicated their                2010; Westgate et al., 2015) was .065 (see Section 13 in
age, sex, education, political ideology, and ethnicity/race.      the Supplemental Material), implying that very little
For some tests, additional attitude-specific covariates           variance is accounted for when using these typical
were included: self-reported weight (for body-weight              methods of analysis. ARIMA models account for non-
attitudes), self-reported sexual orientation (for sexuality       linearity by continuously updating their predictions on
attitudes), and self-reported disability status (for disability   the basis of previous values and are therefore able to
attitudes).                                                       capture evolving nonlinear trends in the data.
                                                                     Third, unlike regression models, ARIMA models can
                                                                  use information about nonlinearity and autocorrelation
Results                                                           structures to provide optimal forecasts. In this case,
                                                                  they are designed to suggest upper and lower bounds
Analytic strategy
                                                                  of 95% confidence intervals (CIs) of attitude change into
Advantages of ARIMA models for analyzing change                   the future, that is, the time it will take for a specific atti-
over time. Data were analyzed using ARIMA time-series             tude to reach neutrality or double in intensity. Forecasts
models (Cryer & Chan, 2008; for an accessible introduc-           provide intuitive estimates, akin to effect sizes with
tion to time series in psychology, see Jebb, Tay, Wang, &         standard regression models, that are more easily inter-
Huang, 2015). We first provide a justification for using          preted than the ARIMA parameters alone. The inclusion
ARIMA models and then describe how the models are                 of forecasts also aligns with recent calls to motivate
implemented; additional details are provided in the Sup-          psychology toward a predictive science, thereby
plemental Material.                                               improving scientific and applied understanding of the
   ARIMA models offer several advantages over the                 generalizability of trends into the future ( Jebb et al.,
multiple regression strategies used in previous exami-            2015; Varnum & Grossmann, 2017; Yarkoni & Westfall,
nations of Project Implicit data over time. First, and            2017). Additionally, the current forecasts can be used
most fundamentally, measures over time are generally              to directly assess the impact of social events on the
subject to significant autocorrelations (or serial depen-         patterns of attitude change. Because Project Implicit
dence), meaning that the value measured at time t is              data have the unique feature of being continuously
dependent on, and highly correlated with, the value               updated, researchers can compare predictions gener-
immediately before it. In other words, measures close             ated by ARIMA models with future observed trajectories
in time are more related to each other than measures              to quantitatively test whether social or political events
far in time. Indeed, in the current data, the median cor-         substantively altered the patterns of attitudes outside
relation (r) between monthly averages at month t and              of the provided CIs. At the least, these predictions are
month t – 1 was .67, implying large and significant               worth offering as a way of testing the viability of time-
temporal dependence in the data. The presence of tem-             series models to account for attitude change.
poral dependencies in the data violates the assumption
of independence in standard regression frameworks,                Specifying and implementing ARIMA models. Time-
leading to inefficient or biased model estimates. Indeed,         series data are characterized, first, by differences in val-
Varnum and Grossmann (2017) provided an instructive               ues at two time points; for example, the magnitude of an
summary of cases in which the failure to account for              attitude measured on Saturday is different from the mag-
autocorrelations has led to spurious conclusions. Time-           nitude of an attitude measured on Sunday. Second, time
series models such as ARIMA are explicitly designed to            series are characterized by the aforementioned autocor-
accommodate the autocorrelated nature of time-series              relations; for example, attitudes measured on Saturday
data and therefore address concerns raised by previous            and Sunday are more similar to each other than attitudes
analytic strategies.                                              measured on Saturday and Wednesday. Third, time series
   Second, visual inspection of the Project Implicit data         are characterized by lagged forecast errors; for example,
shows that changes in implicit and explicit attitudes are         the random errors in predicting attitudes on Saturday and
characterized by substantial variability, seasonality (i.e.,      Sunday are more similar to each other than the random
systematic within-year variability), and most impor-              errors in predicting attitudes on Saturday and Wednesday.
tantly, nonlinearity. Thus, attempting to fit a single lin-       ARIMA models describe these three features of time-series
ear slope captures very little of the true nonlinear              data using three parameters (p, d, q): d specifies the


178                                                                                                   Charlesworth, Banaji

number of differencing parameters necessary to explain          criterion (AIC, a relative measure of model parsimony),
the differences between values, p specifies the number of       as well as tests to ensure that the data are stationary
autoregressive parameters used to explain the autocorre-        (i.e., have been adequately differenced by the d param-
lations in the data, and q specifies the number of moving-      eter). Thus, all reported ARIMA models were entirely
average parameters used to explain the lagged forecast          data driven.
errors.
    For example, to predict preferences on Sunday from          Reporting and interpreting ARIMA forecasts. Mindful
preferences earlier in the week, the differencing (d)           of the limits of any forecast, we offer three considerations
parameter would first be applied to ensure that the             in interpreting the results. First, in most cases, attitudes
mean and variance across the week were stable, leaving          have shown a high degree of variability over time, visually
only the daily fluctuations (i.e., “peaks and valleys”).        manifesting in peaks and valleys. ARIMA models incorpo-
These remaining daily variations would then be mod-             rate this variability and provide 95% CIs for their forecasts
eled by a combination of autoregressive (p) and moving-         that include stability, change toward attitude neutrality,
average (q) parameters. Autoregressive parameters               and change away from attitude neutrality. Although all
would be used to model the consistent correlations              directions of future change are therefore possible, we
between, for example, Sunday and Saturday (if p = 1)            draw attention to the direction of the forecast nearest in
or Sunday and Friday (if p = 2). Moving-average param-          time. For instance, we describe an attitude as forecast to
eters would be used to model the similarity in the              move toward attitude neutrality if one bound of the fore-
random noise (i.e., error) in, for example, Sunday and          cast CI passes neutrality before the other bound of the CI
Saturday (if q = 1) or Sunday and Friday (if q = 2).            passes double the initial attitude level. Neutrality and dou-
    These three parameters are first used to explain the        bling are used as standards of change because they repre-
nonseasonal component of the time-series data (i.e.,            sent the same absolute value of change from the first
the trends over the full time span investigated) but can        measurement, but in opposite directions.
also be extended to explain the systematic within-                  Second, we provide a supplemental internal analysis
calendar-year variations, or seasonality, using seasonal        based on past data to allow greater confidence in the
ARIMA models (formally, SARIMA models). The same                application of time-series models to offer predictions
three parameters (p, d, q) are used to explain the sea-         of future attitudes using the Project Implicit data set
sonality component of the time-series data, with the            (see Section 12 in the Supplemental Material). To assess
same definitions as above. Finally, when time-series            forecast accuracy for ARIMA models, we evaluated how
data include a clear and consistent slope over time,            well forecasts built from the first 8 years of data pre-
ARIMA models can include a drift parameter, which is            dicted the observed data of the last 2 years. Accuracy
analogous to a slope estimate in regression.                    statistics (i.e., mean square error and mean percentage
    Thus, the final ARIMA models can include seven              error) indicated that the ARIMA model approach had
parameters, (p, d, q) (p, d, q) + drift, with the first three   appropriate out-of-sample forecast accuracy when
values specifying the order of nonseasonal parameters,          applied to implicit and explicit attitude change, thereby
the second three values specifying the order of seasonal        reinforcing confidence in the method and the results
parameters, and the inclusion of drift specifying any           of forecasts into the future.
consistent slope. The order of the d parameter can be               Third, the predictions offered are the best estimates
informative in revealing whether the time series is             based on currently available data of past trends. Thus,
already stable (when d = 0) or is changing over time            if data in the future change course because of unex-
(when d ≠ 0). The order of the autoregressive (p) and           pected shocks in the social or political climate, the
moving-average (q) parameters can reveal how many               predicted estimates would also be expected to system-
lags backward are necessary to predict the current mea-         atically change in response. Notably, by offering these
surement at time t. However, the order and values of            predictions, we gain the unique opportunity to quan-
autoregressive and moving-average parameters are gen-           titatively assess the impact of future social events in
erally not intuitively interpretable; we therefore focus on     substantively altering the trajectories of implicit and
interpretation of the ARIMA model forecasts (see below).        explicit attitudes.
    In this article, ARIMA models were estimated using
the automated algorithm implemented in the forecast             Addressing sample changes over time. Observed
package in the R programming environment (Hyndman               change may be an artifact of changes in the demographic
& Khandakar, 2008; R Core Team, 2017). The algorithm            composition of the sample over time. That is, observed atti-
explores the model space stepwise and chooses the               tude change toward neutrality could come not from true
best-fitting combination of nonseasonal, seasonal, and          attitude change but from increasing numbers of female,
drift parameters, given the model’s Akaike information          liberal, young, non-White, or less-educated respondents,


Patterns of Attitude Change                                                                                            179

all of whom have been documented to have lower implicit        employed the same weighting procedures as above but
bias (Nosek et al., 2007). Correlations between time (month)   weighted to the demographics of the 2007–2016 U.S. cen-
and each of these demographic variables indicate that,         sus. These procedures ensured that weighted monthly
since 2007, the Project Implicit sample has become more        averages approximated the demographics in the U.S.
liberal (see Table S4.1 in the Supplemental Material), which   population. Descriptions of overall patterns of change for
could create spurious movement toward neutrality across        census-weighted data largely replicated the results from
all attitudes. However, the sample has simultaneously          within-sample weighted data, thus supporting the gener-
become less female, less young, more White, and more           alizability of our findings (see Section 7 in the Supple-
educated (see Table S4.1), each of which could push the        mental Material). However, the discrepancies between
data away from neutrality over time. Evidently, it is neces-   the sample and population demographics meant that,
sary to separate out these spurious causes of change and       despite having stable weights, the census weighting was
identify the unique effect of time beyond changes to sam-      unable to converge. The results from census-weighted
ple demographics.                                              samples are therefore provided for illustration and should
    To control for sampling changes, we calculated             be interpreted with caution.
weights for all participants on the demographic vari-             An additional argument for generalizability comes
ables of age, race, gender, education, and political ori-      from convergent evidence in patterns of explicit attitude
entation. Each individual participant was given a weight       change using representative probability samples that
corresponding to his or her representativeness of the          are not considered to be affected by self-selection. Pat-
demographic frequencies from 2007 through 2016. For            terns of explicit attitude change observed in the present
example, in the race IAT, the gender frequencies across        data are consistent with the patterns of change observed
the whole time span (2007–2016) were 61% female and            in many other surveys, including the rate and direction
39% male, but in 2007, the gender frequencies were             of change in beliefs about gay rights and race relations
63% female and 37% male. In the analysis, the data in          (e.g., General Social Survey, 2017).
2007 would therefore be weighted such that women                  Furthermore, a new study has revealed concordance
were “down-weighted” (given weights less than 1,               between the magnitudes of implicit associations in the
because the data for female participants in 2007 were          Project Implicit data and the magnitudes of linguistic
overrepresented by 2 percentage points relative to the         associations in natural human language using the larg-
frequencies for the whole time span), whereas men              est linguistic corpus of representative communication
would be “up-weighted” (given weights greater than 1).         on the Internet, with more than 840 billion word tokens
These weighting procedures were performed for all              (Caliskan-Islam, Bryson, & Narayanan, 2016). Such con-
demographic variables (not only for gender).                   sistency between, for example, the IAT magnitude of
    With the weighting values for each participant, we         the elderly + bad/young + good association from Project
computed weighted monthly means for each attitude              Implicit and the magnitude of association of elderly +
test, fitting the ARIMA models to the univariate time          bad/young + good in Internet text provides confidence
series of weighted monthly means. Weighting according          that the present database does not reflect the attitudes
to the sample demographics across the whole time span          of a narrowly self-selected group. Finally, the increas-
controls for changes in sample demographics between            ingly wide usage of the Project Implicit website by
2007 and 2016, thereby reducing the likelihood that any        institutions such as schools, governmental agencies,
observed changes toward neutrality were due to                 nonprofits, and for-profit corporations for organization-
increased participation from less-biased demographic           wide education has further reduced concern about self-
groups and any observed changes away from neutrality           selection and sample unrepresentativeness.
were due to increased participation from more-biased
demographic groups (for further details, see Section 6         Addressing repeat test takers and regression to the
in the Supplemental Material).                                 mean. As the popularity of the Project Implicit website
                                                               has increased over time, new respondents are added
Addressing sample unrepresentativeness. The use                daily, but previous respondents have also returned to take
of web-based data raises the concern of whether observed       additional tests. The initially extreme attitudes of novel
attitude change can be generalized from the Project            test takers may gradually regress to the mean as they
Implicit sample to U.S. society. Sample demographics of        become experienced with the IAT. Thus, observed change
race and education (based on high school attainment)           toward neutrality could arise from increasing numbers of
approximated the population values for the United States,      repeat test takers who are regressing to a more neutral
but the sample was younger, more liberal, and more             attitude, rather than to genuine population attitude change.
female than the U.S. population (U.S. Census Bureau,           We addressed this concern by repeating the ARIMA mod-
2016). To account for these demographic differences, we        els on the subset of data from respondents who reported


180                                                                                                   Charlesworth, Banaji

having never taken an IAT before. Descriptions of overall      that can further disambiguate age, cohort, and period
patterns of change for these novel test takers were con-       effects with univariate time-series data.
sistent with the patterns of change in the whole sample           In addition to investigations across generational
(see Section 11 in the Supplemental Material), implying        cohorts, we examined patterns of change in demo-
that the cause of change cannot be attributed to repeat        graphic subgroups to address questions of generaliz-
test takers and regression to the mean.                        ability across the disadvantaged and advantaged groups
                                                               for each attitude test. To maintain the focus on illumi-
Addressing change across generational cohorts                  nating overall patterns of change, we examined only
and demographic groups. Observed change toward                 directly relevant demographic subgroups for each atti-
neutrality could be due to (a) changes to the age of the       tude (e.g., respondent racial group for race and skin-
sample, in which the average age of the sample decreases       tone attitudes). Research currently in preparation
and younger respondents have lower bias; (b) cohort            explores the full complexity of change by demographic
replacement, in which older generations are replaced by        subgroups and geographic location.
younger generations who have lower bias; or (c) period            For both relevant demographic subgroups and gen-
effects, in which external social or political forces affect   erational cohorts, separate ARIMA models were fit to
all ages and cohorts in a society (Winship & Harding,          each subgroup; comparisons are reported for both past
2008). These three factors (age, cohort, period) are lin-      patterns of change (percentage change statistics) and
early dependent, such that a period effect is equivalent to    future patterns of change from ARIMA model forecasts.
the combination of an age and cohort effect. For exam-         Full models by relevant subgroups and cohorts are
ple, the extent of influence from external social forces       reported below for implicit attitudes and in Tables S9
(e.g., experiences in wartime) is entirely determined by       and S10 in the Supplemental Material for explicit
the year in which one was born (e.g., 1935 vs. 1995) and       attitudes.
the age at which one was measured (e.g., 10 years old vs.
30 years old). Thus, these three causes of change cannot       Addressing the relationship between explicit and
be isolated from one another with the present data, a          implicit attitude change. The cross-temporal relation-
problem known as the identification problem. Neverthe-         ship between implicit and explicit attitude change in
less, we emphasize that changes to the age of the sample       individual-level attitudes is a topic of substantial theoreti-
(i.e., age effects) are unlikely to account for the observed   cal interest (Gawronski & Bodenhausen, 2006; Rydell &
change because of the within-sample weighting proce-           McConnell, 2006). The present data can be used to extend
dures described above, which ensure that the average age       this discussion to long-term population-level attitude
of the sample remains consistent across the investigated       change. Specifically, we examined whether long-term
time span.                                                     implicit attitude change predicts explicit attitude change,
    To begin to examine the influence of cohort and            or vice versa. This can be addressed by Granger causality
period effects, we examined differences in patterns of         models, which have been used in psychology to examine
change across four generational cohorts, defined by            causes of cultural change (Grossmann & Varnum, 2015).
birth years: baby boomers (1945–1963), Generation X            Granger models of predictive causality examine whether
(1964–1975), millennials (1976–1995), and Generation           the change in one variable (e.g., explicit attitudes) provides
Z (1996–2009). Data from earlier generations (“the             significantly more explanatory value about the change in a
silent generation”) were not sufficient for monthly anal-      second variable (e.g., implicit attitudes), beyond using only
yses (fewer than 100 observations per month). Addi-            the previous values of that second variable. In other words,
tionally, data from Generation Z were included only            does knowing past values of both explicit and implicit atti-
after 2011, at which point monthly frequencies were            tudes tell us significantly more about the patterns of implicit
sufficient.                                                    attitudes than merely knowing the past values of implicit
    To the extent that attitude change is observed only        attitudes alone?
in younger generational cohorts, we can conclude that              The present study used Granger models to (a) pre-
there is a cohort-by-period interaction, in which the          dict implicit attitudes from explicit attitudes at lags of
social forces causing change (e.g., media campaigns or         1 month and 6 months and (b) predict explicit attitudes
federal legislation) are predominantly affecting younger       from implicit attitudes at lags of 1 month and 6 months.
cohorts. In contrast, to the extent that attitude change       If only one direction of prediction is significant (e.g.,
is observed across all generational cohorts, we can            only implicit to explicit), then one can conclude that
conclude that the likely source of change is a period          change likely follows in that direction (e.g., implicit
effect, in which the causes of change are widespread           attitude change precedes explicit attitude change). If
and affect respondents regardless of their age or cohort.      both directions of prediction are significant, then it is
Future research would benefit from modeling strategies         more likely that an exogenous third variable is causing


Patterns of Attitude Change                                                                                                               181

change in both implicit and explicit attitudes. Finally,                      an artifact of any one search term comparison. Google
if neither direction is significant, then implicit change                     searches have previously been validated as unobtrusive
tells us little about explicit change, and vice versa; in                     measures of social attitudes (Stephens-Davidowitz,
this case, implicit and explicit attitudes may be chang-                      2014) and may be interpreted as proxies for the relative
ing for dissociable and independent reasons.                                  level of societal priority of an attitude.
                                                                                 Comparing the relative rates of group-related searches,
Addressing change as a function of societal priority                          we found that searches for “racism” were always more
of the attitude. At different points in history, particular                   common than any other “-ism” term and that searches
social issues have received societal priority. For instance,                  for “anti-gay” and “gay rights” were always more com-
during the American Civil War, the issue of slavery was of                    mon than any other “anti-” or “rights” term, respectively
utmost social and political interest; during women’s suf-                     (see Table S16 in the Supplemental Material). Out of a
frage, women’s right to vote became the focus of debate.                      possible value of 100 (reflecting peak popularity),
In the United States today, race and sexuality attitudes                      sexuality-related terms averaged a popularity of 18.53,
appear to be societally prioritized (e.g., through the Black                  race-related terms averaged 18.16, disability-related
Lives Matter movement or legislation about same-sex mar-                      terms averaged 2.43, and neither age-related nor body-
riage) and therefore are more frequently discussed than                       weight-related terms reached a score of 1. Thus, to the
other attitudes, such as age or disability. Societal priority                 extent that societal priority and cultural-level frequency
corresponds to more frequent and repeated exposure to                         of discussion cooccur with relative rates of long-term
debate or counterarguments that may, in turn, induce                          implicit attitude change, it would be expected that race/
greater attitude change (Petty & Krosnick, 1995).                             skin-tone and sexuality attitudes will change faster than
   To determine whether change is indeed occurring                            age, disability, or body-weight attitudes.
faster on these prioritized attitudes, we examined the
relative frequency of Google searches from January                            Implicit and explicit attitude means
2007 to December 2016 for three prejudice- and
activism-related terms for each attitude—age: “ageism,”
                                                                              and correlations
“anti-old,” “elder rights”; disability: “ableism,” “anti-                     All explicit and implicit attitudes showed significant
disabled,” “disability rights”; race and skin tone: “rac-                     preferences for the typically preferred group (i.e., pro-
ism,” “anti-Black,” “Black rights”; sexual orientation:                       straight, pro-White, pro-light skin, pro-young, pro-
“homophobia”, “anti-gay,” “gay rights”; and body weight:                      abled, and pro-thin; see Table 1). The strongest implicit
“sizeism,” “anti-fat,” “fat acceptance.” Three commonly                       preferences were observed for disability, body-weight,
used terms were included for each social-group attitude                       and age attitudes, with relatively weaker implicit prefer-
to ensure that the relative rates of searches were not                        ences observed for race, skin-tone, and sexuality


 Table 1. Means and Correlations for Six Implicit and Explicit Social-Group Attitudes

                                                                                                                    Correlation between
                                                                                                                    explicit and implicit
                                               Implicit attitudes                         Explicit attitudes              attitudes

 Attitude                   N        M (SD)       95% CI          t       d     M (SD)      95% CI          t   d    r   95% CI       t
 Sexuality                692,425      0.29     [0.29, 0.29] 495.24 0.60         0.54     [0.54, 0.54] 354.92 0.43 .42 [.41, .42] 381.61
                                      (0.48)                                    (1.27)
 Race                   1,851,445      0.32     [0.32, 0.32] 972.40 0.71         0.32     [0.32, 0.32] 385.05 0.28 .32 [.32, .32] 459.66
                                      (0.44)                                    (1.13)
 Skin tone                488,330      0.31     [0.31, 0.31] 510.57 0.73         0.28     [0.28, 0.29] 197.60 0.28 .21 [.21, .22] 153.34
                                      (0.43)                                    (1.00)
 Age                      588,230      0.44     [0.44, 0.44] 857.74 1.12         0.50     [0.50, 0.51] 314.24 0.41 .12 [.12, .13]   96.20
                                      (0.39)                                    (1.23)
 Disability               191,499      0.49     [0.49, 0.49] 493.63 1.13         0.49     [0.48, 0.49] 221.55 0.51 .14 [.14, .15]   63.17
                                      (0.44)                                    (0.96)
 Body weight              275,321      0.48     [0.48, 0.48] 609.65 1.16         0.92     [0.92, 0.93] 448.56 0.85 .22 [.22, .23] 119.88
   (figure stimuli)                   (0.41)                                    (1.08)
 Body weight              306,112      0.40     [0.40, 0.40] 525.19 0.95         1.05     [1.05, 1.05] 508.80 0.92 .19 [.19, .19] 107.41
   (face stimuli)                     (0.42)                                    (1.14)

 Note: All means and correlations are significantly different from zero (p < .001). CI = confidence interval.


182                                                                                                  Charlesworth, Banaji

attitudes. Similarly, strong explicit preferences were         ARIMA forecasts were predicted to pass neutrality by Jan-
observed for disability, body-weight, and age attitudes,       uary 2025 and September 2045, respectively.
although strong preferences also emerged for explicit             The correlation between implicit and explicit atti-
sexuality attitudes; relatively weaker explicit prefer-        tudes did not change substantively over time (decreased
ences were observed for race and skin-tone attitudes.          by ~3%). Granger causality models were inconclusive
Thus, if higher overall bias cooccurs with slower              and revealed significant relationships in both directions,
change, in line with the aforementioned predictions            suggesting that an exogenous third variable may be
from attitude strength (Petty & Krosnick, 1995), then          causing simultaneous change in both implicit and
implicit age, disability, and body-weight attitudes            explicit sexuality attitudes.
should reveal slower change than implicit race, skin-             All respondents, regardless of sexual orientation,
tone, and sexuality attitudes. The relevance of differ-        showed consistent past and future movement toward
ences in overall bias to rates of long-term change is          implicit pro-gay preference. Additionally, all cohorts
discussed below.                                               changed toward attitude neutrality. This suggests that
   Significant positive correlations between implicit and      change in implicit sexuality attitudes may be caused by
explicit attitudes were observed for all six attitudes,        period effects. That is, the likely causes of changes in
with the strongest correlations for sexuality and race         sexuality attitude are widespread shifts in the sociocul-
attitudes and the weakest correlations for disability and      tural climate that affect all ages, generational cohorts,
age attitudes. The relevance of differences in correla-        and demographics. Such findings extend the conclu-
tion strength to rates of attitude change is discussed         sions from representative social surveys on change in
below. Notably, means and correlations for all attitudes       explicit sexuality attitudes, which document movement
closely replicated the results from previous large-scale       toward neutrality across all birth cohorts (Rosenfeld,
analyses (Nosek et al., 2007), providing convergent evi-       2017).
dence for the present sample.
                                                               Race attitudes. Over the past decade, explicit race atti-
                                                               tudes have moved toward neutrality by approximately
Patterns of change                                             37%. Implicit race attitudes have moved in the same
For each attitude, the reporting of results answered five      direction but at a slower rate than explicit attitudes
questions. First, how fast have explicit attitudes changed     (changing toward neutrality by 17%), with a larger differ-
over the past decade (see Table 2 and Fig. 1)? Rate of         ence in rate of change than seen for sexuality attitudes.
past change is indexed by the percentage change from           The pattern of change in implicit race attitudes revealed
the first to last months of the decomposed time-series         nonlinearity, with stability in early years followed by
trend, removing seasonality and noise. Second, how             notable change since approximately 2012. The lower
fast have implicit attitudes changed (by percentage            bound of the 95% CI of the ARIMA forecasts was pre-
change) and are they predicted to change in the future         dicted to pass attitude neutrality in August 2073, which is
(see Table 2 and Fig. 1)? Predictions were derived from        approximately half the time for the upper bound to reach
the number of months for the bounds of the 95% CIs             double the level of initial bias.
of ARIMA forecasts of implicit attitudes to pass neutral-          Notably, the implicit–explicit correlation for race atti-
ity or double from the first month’s value. Third, has         tudes decreased by approximately 18% over the past
the correlation between implicit and explicit attitudes        decade, in contrast to the stability observed in implicit–
changed over time (see Table 2)? Fourth, does implicit         explicit correlations for all other attitudes. The decrease
attitude change precede or follow explicit attitude            in implicit–explicit correlations implies that, over time,
change, as indexed by Granger causality models (see            the people holding strong implicit race attitudes are
Table 3)? Fifth, does implicit attitude change generalize      less likely to be the same people who hold strong
across generational cohorts (see Table 4) and across           explicit race attitudes (and, conversely, those holding
relevant demographic groups (see Table 5)?                     weak implicit race attitudes are less likely to be those
                                                               holding weak explicit race attitudes). In other words,
Sexuality attitudes. Explicit sexuality attitudes revealed     implicit and explicit race attitudes show reduced cor-
the largest overall change of any explicit attitude, moving    respondence over time, perhaps because of changing
toward neutrality by approximately 49% since 2007.             social desirability for this particular attitude.
Implicit sexuality attitudes also showed the most substan-         Granger models reveal that implicit attitude change sig-
tial overall change of all implicit attitudes, moving in the   nificantly predicted explicit change at lags of both 1 and
same direction but at a slower rate than explicit attitudes    6 months, whereas the reverse direction (explicit to
(changing toward neutrality by 33%). For implicit atti-        implicit) was not significant, suggesting that change in race
tudes, the lower and upper bounds of the 95% CI of the         attitudes likely flows from implicit to explicit attitudes.


                               Implicit Sexuality Attitudes                                       Implicit Race Attitudes                                            Implicit Skin-Tone Attitudes
                    0.40                                                             0.40                                                              0.40
                                                                                                                      double:                                                                      double:
                    0.35                                                             0.35                             107 yrs, 1 mos                   0.35                                        >150 yrs
                                                     neutral:
                    0.30                             29 yrs, 9 mos                   0.30                                                              0.30

                    0.25                                                             0.25                                                              0.25
                                                                                                                                                                                             neutral:
      IAT D Score                                                      IAT D Score                                                       IAT D Score
                    0.20                                                             0.20                             neutral:                         0.20
                                                                                                                                                                                             138 yrs, 7 mos
                                                                                                                      57 yrs, 8 mos
                    0.15                                                             0.15                                                              0.15
                                                    neutral:
                    0.10                            9 yrs                            0.10                                                              0.10
                           2008 2010 2012 2014 2016 2018 2020                               2008 2010 2012 2014 2016 2018 2020                                2008 2010 2012 2014 2016 2018 2020


                                 Implicit Age Attitudes                                         Implicit Disability Attitudes                                    Implicit Body-Weight Attitudes
                    0.60                                                           0.60                                     double:                  0.60
                                                                                                                            >150 yrs
                    0.55                                                           0.55                                                              0.55
                                                                                                                                                                                              not changing
                    0.50                               double:                     0.50                                                              0.50
                                                       >150 yrs
                    0.45                                                           0.45                                                              0.45
                                                                                                                         neutral:
                                                                                                                         >150 yrs
      IAT D Score                                                    IAT D Score                                                       IAT D Score
                    0.40                                                           0.40                                                              0.40
                                                       neutral:
                    0.35                               >150 yrs                    0.35                                                              0.35                  Face Stimuli
                                                                                                                                                                           Figure Stimuli
                    0.30                                                           0.30                                                              0.30
                           2008 2010 2012 2014 2016 2018 2020                               2008 2010 2012 2014 2016 2018 2020                                2005         2010             2015          2020
                                                                                                                                                                          Fig. 1. (continued on next page)


183


184                                          Explicit Sexuality Attitudes                                                   Explicit Race Attitudes                                                   Explicit Skin-Tone Attitudes
                                   0.8                                                                          0.8                                                                          0.8
                                                                    double:
                                   0.6                              42 yrs, 9 mos                               0.6                                                                          0.6


                                   0.4                                                                          0.4                              neutral:                                    0.4                             double:
                                                                                                                                                 21 yrs, 6 mos                                                               23 yrs, 8 mos

      Explicit-Preference Score    0.2                                              Explicit-Preference Score   0.2                                              Explicit-Preference Score   0.2

                                                                     neutral:
                                   0.0                                                                          0.0                               neutral:                                   0.0                            neutral:
                                                                     5 yrs, 6 mos
                                                                                                                                                  1 yr, 11 mos                                                              2 yrs, 7 mos
                                         2008 2010 2012 2014 2016 2018 2020                                           2008 2010 2012 2014 2016 2018 2020                                           2008 2010 2012 2014 2016 2018 2020


                                               Explicit Age Attitudes                                                     Explicit Disability Attitudes                                              Explicit Body-Weight Attitudes
                                   0.8                                                                          0.8
                                                                                                                                                                                             1.2
                                                                    double:
                                   0.6                              26 yrs, 1 mos                               0.6                             neutral:
                                                                                                                                                                                                                            double:
                                                                                                                                                30 yrs, 11 mos
                                                                                                                                                                                             1.0                            67 yrs, 6 mos
                                   0.4                                                                          0.4

                                                                                                                                                neutral:                                     0.8
                                   0.2                                                                          0.2                             17 yrs, 6 mos
                                                                    neutral
       Explicit-Preference Score                                                    Explicit-Preference Score                                                    Explicit-Preference Score
                                                                    8 yrs, 5 mos:
                                   0.0                                                                          0.0                                                                          0.6                            neutral:
                                                                                                                                                                                                                            34 yrs, 3 mos

                                         2008 2010 2012 2014 2016 2018 2020                                           2008 2010 2012 2014 2016 2018 2020                                           2008 2010 2012 2014 2016 2018 2020

        Fig. 1. Change and predicted change in implicit and explicit attitudes from 2007 to 2020: observed monthly weighted averages (2007–2016) of implicit association test (IAT)
        D scores (implicit attitudes; top two rows) and explicit-preference scores (explicit attitudes; bottom two rows), as well as forecasts of the autoregressive-integrated-moving-
        average (ARIMA) model (2017–2020). Solid black lines indicate decomposed trends of observed data (removing seasonality and noise), solid light-gray lines indicate the
        weighted monthly means from observed data, dotted black lines within the light-gray areas indicate the means of the ARIMA forecasts, light-gray areas indicate 80% confidence
        intervals (CIs), and dark-gray areas indicate 95% CIs of the ARIMA forecasts. Reported months to double indicate the number of months for the bound of the 95% CI to pass
        twice the level of initial bias; reported months to neutral indicate the number of months for the bound of the 95% CI to reach attitude neutrality. Implicit body-weight attitudes
        include data from both the face-stimuli test (dotted line and light-gray forecasts) and the figure-stimuli test (solid line and dark forecasts). Implicit age, disability, and body
        weight are on the same y-axis dimensions, whereas implicit race, skin tone, and sexuality are on the same y-axis dimensions. Explicit body-weight attitudes have different
        y-axis dimensions from all other explicit attitudes.


      Table 2. Patterns of Change in Six Implicit and Explicit Social-Group Attitudes and Implicit–Explicit Correlations From 2007 to 2016

                                                                                                                                                                      Correlation between explicit and
                                                   Implicit attitudes                                                  Explicit attitudes                                      implicit attitudes

                           Starting   Ending Percentage change             ARIMA model          Starting Ending Percentage change              ARIMA model
                             raw       raw    in decomposed                  parameters           raw     raw    in decomposed                   parameters                                     Percentage
      Attitude              valuea    valuea    trend valuesb            (p, d, q) (p, d, q)c    valuea valuea     trend valuesb             (p, d, q) (p, d, q)c    Starting ra   Ending ra    change in r
      Sexuality              0.33       0.17            −33.46           (0, 1, 2) (2, 0, 0)     0.67       0.35            −48.59            (0, 1, 2) (2, 0, 0)       .45           .43          −2.78
                                                                               + drift
      Race                   0.33       0.30            −16.81           (1, 1, 1) (2, 0, 0)     0.30       0.17            −36.74            (0, 1, 1) (2, 0, 2)       .35           .29         −18.20
                                                                                                                                                     + drift
      Skin tone              0.33       0.29            −14.59                (0, 1, 1)          0.30       0.15            −21.04            (0, 1, 3) (1, 0, 1)       .22           .25            0.82
      Age                    0.45       0.42             −5.36           (0, 1, 2) (2, 0, 0)     0.52       0.40            −33.65            (0, 1, 2) (2, 0, 0)       .14           .12            1.84
      Disability             0.51       0.52             −1.66                (0, 1, 2)          0.64       0.44            −23.97            (1, 1, 1) (2, 0, 0)       .16           .19           −0.63
                                                                                                                                                     + drift
      Body weight            0.48d      0.48               4.67               (1, 0, 0)          0.90e      0.80e           −14.81e           (0, 1, 2) (2, 0, 0)e      .24f          .21g           9.15
        (figure stimuli)
      Body weight            0.30d      0.41d            40.10           (0, 1, 1) (1, 0, 0)
        (face stimuli)
      a
       Unless otherwise noted, starting values are from January 2007 and ending values are from December 2016. Starting and ending values are from the implicit association test (IAT; D scores) and 7-point
      explicit-preference scales. bPercentage change is between the first and last values of the decomposed time-series trend (removing seasonality and noise). Negative values indicate change toward
      neutrality (i.e., decreasing prejudice); positive values indicate change away from neutrality (i.e., increasing prejudice). cThe first three parameters of the autoregressive-integrated-moving-average
      (ARIMA) model are nonseasonal, and the second three values are seasonal; drift is also included. In each set of parameters, d specifies the number of differencing parameters necessary to explain
      the differences between values, p specifies the number of autoregressive parameters used to explain the autocorrelations in the data, and q specifies the number of moving-average parameters
      used to explain the lagged forecast errors. dImplicit body-weight attitudes were measured in two tests: Figure stimuli were used from April 2010 to December 2016, and face stimuli were used from
      May 2004 to October 2011. eExplicit body-weight attitudes are from the combined data across the two tests, since explicit attitudes were not affected by the change in IAT stimuli. Thus, explicit
      body-weight attitudes are from January 2007 to December 2016, as with all other attitudes. fThe starting implicit–explicit correlation for body-weight attitudes is from January 2007 and is therefore
      the correlation between explicit attitudes and implicit attitudes measured with the face-stimuli test. gThe ending implicit–explicit correlation for body-weight attitudes is from December 2016 and is
      therefore the correlation between explicit attitudes and implicit attitudes measured with the figure-stimuli test.


185


186                                                                                                         Charlesworth, Banaji

      Table 3. Results From Granger Tests of Predictive Causality on Implicit and Explicit Attitudes (With Trends)

                                          Implicit precedes     Implicit precedes     Explicit precedes    Explicit precedes
                                               explicit              explicit              implicit             implicit
      Attitude                               (1 month)            (6 months)             (1 month)           (6 months)
      Sexuality                           F(1, 117) = 0.35      F(6, 107) = 3.18**    F(1, 117) = 4.21*    F(6, 107) = 2.24*
      Race                                F(1, 117) = 11.33**   F(6, 107) = 3.58**    F(1, 117) = 0.35     F(6, 107) = 0.78
      Skin tone                           F(1, 117) = 0.41      F(6, 107) = 5.16***   F(1, 117) = 1.91     F(6, 107) = 0.47
      Age                                 F(1, 117) = 9.94**    F(6, 107) = 2.71*     F(1, 117) = 0.14     F(6, 107) = 5.85***
      Disability                          F(1, 117) = 0.47      F(6, 107) = 1.99      F(1, 117) = 1.30     F(6, 107) = 0.49
      Body weight (figure stimuli)         F(1, 78) = 0.20       F(6, 68) = 0.71       F(1, 78) = 1.29      F(6, 68) = 0.82
      Body weight (face stimuli)           F(1, 55) = 0.12       F(6, 45) = 0.34       F(1, 55) = 0.79      F(6, 45) = 0.077

      *p < .05. **p < .01. ***p < .001.


   Respondents of all racial groups (except Blacks/                    strongly in millennials and Generation Zers, with rela-
African Americans) moved toward implicit attitude                      tive stability (and even slight change away from neutral-
neutrality; Black/African American respondents, how-                   ity) in baby boomers and Generation Xers. As with race
ever, had stable implicit pro-Black preferences over the               attitudes, these generational patterns imply that the
past decade and were forecast to remain stable. Change                 observed change toward neutrality could be attributed
toward neutrality was largest in millennials, with rela-               to a cohort-by-period interaction wherein the causes
tive stability predicted for baby boomers and Genera-                  of change are largely focused on the attitudes of
tion Xers (as indicated by the absence of a differencing               younger generations.
parameter in the ARIMA models). Because millennials
are changing faster than older generational cohorts, the               Age attitudes. Explicit age attitudes changed linearly
observed change in implicit race attitudes may be driven               toward attitude neutrality by approximately 34%. In con-
by a cohort-by-period interaction, in which the social                 trast, implicit age attitudes revealed only slight change
forces driving attitude change are predominantly affect-               toward attitude neutrality over the past decade (changing
ing younger cohorts.                                                   by approximately 5%), moving in a parallel direction but
                                                                       at a slower rate than explicit attitudes. Indeed, age atti-
Skin-tone attitudes. Explicit skin-tone attitudes have                 tudes revealed the largest difference between rates of
changed toward attitude neutrality by 21%, slower than                 explicit and implicit change for any attitude. The upper
sexuality and race attitudes. Implicit skin-tone attitudes             and lower 95% CIs of ARIMA forecasts for implicit attitudes
revealed nonlinear change in the same direction but at a               were not predicted to pass attitude neutrality or doubling
slower rate than explicit attitudes (changing by ~15%).                within the next 150 years. Given the inherent uncertainty
The ARIMA forecasts for implicit skin-tone attitudes also              in forecasting over such long periods, forecasts beyond
indicate slower change than for implicit sexuality or race             150 years are best interpreted as attitude stability.
attitudes, with the lower bound of the 95% CI predicted                   The implicit–explicit correlation for age attitudes also
to pass neutrality in July 2154 and the upper bound not                revealed stability over the past decade (increasing by
predicted to pass doubling within the next 150 years.                  less than 2%). Granger models were inconclusive
    The implicit–explicit correlation for skin-tone atti-              regarding the direction of change, with significance in
tudes remained stable over the past decade, unlike the                 both directions, suggesting that an exogenous third
implicit–explicit correlation for race attitudes. Granger              variable may be causing the variability in both implicit
models indicated that implicit attitudes at a lag of 6                 and explicit attitudes. Finally, the stability in implicit
months significantly predicted explicit attitudes, whereas             attitudes was observed across all age groups and gen-
the reverse direction was not significant. Thus, as with               erational cohorts, with even the oldest cohorts and most
race attitudes, this suggests that the direction of attitude           elderly respondents showing stable implicit pro-young
change may flow from implicit to explicit attitudes.                   preferences.
    Change toward implicit attitude neutrality was most
notable among Black American respondents, whereas                      Disability attitudes. Explicit disability attitudes changed
relative stability was observed among both White Amer-                 toward neutrality by approximately 24%. However, no
ican and Asian American respondents. Change toward                     change was observed in implicit disability attitudes (chang-
neutrality in implicit attitudes was also observed most                ing by approximately 2%), and visual inspection shows


Patterns of Attitude Change                                                                                                            187

            Table 4. Cohort Differences in Change for Six Implicit Social-Group Attitudes From 2007 to 2016

                                                                                           Percentage
                                                              Starting      Ending         change in           ARIMA model
            Attitude and generational                           raw          raw         decomposed              parameters
            cohort                                 N           valuea       valuea       trend valuesb        (p, d, q) (p, d, q)c
            Sexuality
              Baby boomers                      41,203         0.28          0.21           −11.27                (0, 1, 1)
              Generation Xers                   65,168         0.30          0.21           −12.57                (0, 1, 1)
              Millennials                      400,882         0.34          0.16           −31.57           (1, 1, 1) (2, 0, 0)
              Generation Zers                  113,525         0.25d         0.26           −21.18           (1, 1, 3) (1, 0, 0)
            Race
              Baby boomers                     145,673         0.33          0.33            −1.47                (0, 0, 4)
              Generation Xers                  206,923         0.29          0.28           −13.83                (0, 0, 2)
              Millennials                      950,145         0.34          0.29           −19.98           (1, 1, 1) (1, 0, 1)
              Generation Zers                  173,932         0.29d         0.31            −5.62                (0, 1, 1)
            Skin tone
              Baby boomers                      36,963         0.35          0.42             4.20                 (0, 0, 2)
              Generation Xers                   63,897         0.32          0.35             3.10                 (3, 0, 1)
              Millennials                      259,142         0.32          0.27           −12.40                 (2, 1, 3)
              Generation Zers                   47,556         0.33d         0.26           −14.12                 (0, 1, 2)
            Age
              Baby boomers                      41,056         0.46          0.45              1.24               (0, 0, 2)
              Generation Xers                   45,845         0.46          0.45             −4.63               (2, 1, 1)
              Millennials                      289,760         0.45          0.43             −3.92          (0, 1, 2) (2, 0, 0)
              Generation Zers                   63,236         0.38d         0.41             10.59               (0, 1, 1)
            Disability
              Baby boomers                      17,783         0.59          0.73              9.18                (0, 1, 1)
              Generation Xers                   22,291         0.50          0.57             12.40                (0, 1, 3)
              Millennials                      107,650         0.50          0.49              0.67                (0, 0, 0)
              Generation Zers                   20,018         0.42d         0.47             27.55                (0, 0, 1)
            Body weight (figure stimuli)
              Baby boomers                      18,075         0.50e         0.53              4.34               (2, 1, 1)
              Generation Xers                   27,375         0.55e         0.51              7.69               (1, 0, 0)
              Millennials                      173,166         0.46e         0.47              6.50          (1, 0, 0) (1, 0, 2)
              Generation Zers                   55,820         0.35d         0.48             23.15               (4, 1, 0)
            Body weight (face stimuli)
              Baby boomers                      30,353         0.27f         0.41g            60.91           (0, 1, 1) + drift
              Generation Xers                   41,757         0.31f         0.45g            47.40           (0, 1, 4) + drift
              Millennials                      230,267         0.31f         0.42g            38.13           (0, 1, 1) + drift

            Note: Baby boomers were born between 1945 and 1963, Generation Xers were born between 1964 and 1975,
            millennials were born between 1976 and 1994, and Generation Zers were born between 1995 and 2009.
            a
              Unless otherwise noted, starting values are from January 2007 and ending values are from December 2016. Starting
            and ending values are from the implicit association test (D scores) and 7-point explicit-preference scales. bPercentage
            change is between first and last values of the decomposed time-series trend (removing seasonality and noise).
            c
              The first three parameters of the autoregressive-integrated-moving-average (ARIMA) model are nonseasonal, and
            the second three values are seasonal; drift is also included. In each set of parameters, d specifies the number of
            differencing parameters necessary to explain the differences between values, p specifies the number of autoregressive
            parameters used to explain the autocorrelations in the data, and q specifies the number of moving-average parameters
            used to explain the lagged forecast errors. dGeneration Z starting values were from January 2011 to ensure adequate
            sample size for each month. Generation Z body-weight (face-stimuli) values are not available because of the end date
            of the test. eBody-weight (figure-stimuli) tests started in April 2010. fBody-weight (face-stimuli) tests started in May
            2004. gBody-weight (face-stimuli) tests ended in October 2011.


stability with a slight curvilinear trend of less neutral atti-           divergence, relative to sexuality and race attitudes. Neither
tudes before approximately 2013 and slightly more neutral                 the upper nor lower bounds of the 95% CIs of ARIMA
attitudes since 2013. As with age attitudes, rates of change              forecasts for implicit disability attitudes were predicted to
for implicit and explicit disability attitudes show a large               pass neutrality or doubling within the next 150 years.


188                                                                                                                     Charlesworth, Banaji

      Table 5. Relevant Demographic Differences in Change for Six Implicit Social-Group Attitudes From 2007
      to 2016

                                                                                            Percentage
                                                             Starting      Ending           change in               ARIMA model
      Attitude and demographic                                 raw          raw           decomposed                  parameters
      group                                     N             valuea       valuea         trend valuesb           (p, d, q) (p, d, q)c
      Sexuality
        Straight                              489,783         0.43          0.27             −24.91           (0, 1, 1) (2, 0, 0) + drift
        Gay/lesbian                            62,927        −0.15         −0.27             −80.73                (2, 1, 3) + drift
      Race
        White American                      1,059,974         0.40          0.36             −15.27                    (0, 1, 2)
        Black American                        181,157        −0.089         0.0093            −3.61               (0, 0, 1) (1, 0, 0)
        Asian American                         73,051         0.32          0.31             −14.83                    (0, 1, 1)
      Skin tone
        White American                        250,159         0.40          0.36             −11.45                    (0, 1, 1)
        Black American                         74,991         0.095         0.10             −40.17                    (0, 1, 3)
        Asian American                         20,973         0.30          0.27             −10.07                    (0, 0, 1)
      Age
        10–25 years                           283,749         0.44          0.42              −6.54               (0, 1, 1) (2, 0, 0)
        25–35 years                            68,692         0.49          0.39              −6.79               (0, 1, 1) (1, 0, 0)
        35–45 years                            38,889         0.45          0.47              −3.17                    (0, 0, 0)
        45–55 years                            31,945         0.45          0.43              −1.76               (0, 1, 1) (1, 0, 1)
        55+ years                              19,466         0.47          0.44              +2.53                    (0, 0, 0)
      Disability
        Disabled                               24,127         0.42          0.43              −9.08                    (0, 1, 2)
        Not disabled                          144,546         0.53          0.54              −0.69                    (1, 1, 1)
      Body weight (figure stimuli)
        Overweight                             98,532         0.42d         0.44              +5.17               (1, 0, 0) (2, 0, 0)
        Average weight                        112,663         0.52d         0.52              +4.87                    (3, 0, 0)
        Underweight                            24,184         0.50d         0.50              +3.20               (3, 0, 0) (1, 1, 1)
      Body weight (face stimuli)
        Overweight                            122,551         0.26e         0.38f            +48.25                (0, 1, 1) + drift
        Average weight                        135,468         0.34e         0.46f            +41.19                (0, 1, 1) + drift
        Underweight                            28,186         0.29e         0.43f            +26.47                    (3, 1, 0)
      a
       Unless otherwise noted, starting values are from January 2007 and ending values are from December 2016. Starting and ending
      values are from the implicit association test (D scores) and 7-point explicit-preference scales. bPercentage change is between first
      and last values of the decomposed time-series trend (removing seasonality and noise from the data). cThe first three parameters
      of the autoregressive-integrated-moving-average (ARIMA) model are nonseasonal, and the second three values are seasonal; drift
      is also included. In each set of parameters, d specifies the number of differencing parameters necessary to explain the differences
      between values, p specifies the number of autoregressive parameters used to explain the autocorrelations in the data, and q
      specifies the number of moving-average parameters used to explain the lagged forecast errors. dBody-weight (figure-stimuli) tests
      started in April 2010. eBody-weight (face-stimuli) tests started in May 2004. fBody-weight (face-stimuli) tests ended in October 2011.


   The implicit–explicit correlation for disability atti-                  all explicit attitudes, moving by approximately 15% over
tudes revealed stability, with change of less than 1%                      the past decade. Moreover, whereas all other implicit and
over the past decade. Granger models revealed no sig-                      explicit attitudes revealed trends toward neutrality, albeit
nificant prediction in either direction of implicit or                     at varying rates, implicit body-weight attitudes revealed
explicit change, implying that implicit and explicit atti-                 movement away from neutrality over time, with slight
tudes are likely affected by dissociable processes.                        changes in the figure-stimuli test (increasing by 5%) and
Finally, stability in implicit disability attitudes was                    large changes in the face-stimuli test (increasing by 40%).
observed for all respondents, regardless of disability                         In line with the small percentage change in the
status or generational cohort.                                             figure-stimuli test, the ARIMA model for the figure-stim-
                                                                           uli test implied stability of implicit body-weight atti-
Body-weight attitudes. Explicit body-weight attitudes                      tudes, with neither bound of the CIs predicted to pass
showed the slowest change toward attitude neutrality of                    neutrality or doubling. However, for the face-stimuli test,


Patterns of Attitude Change                                                                                           189

the best-fitting ARIMA model predicted change away             demographics, in contrast to the direction of all other
from neutrality, with the upper bound of the 95% CI            implicit and explicit attitudes.
predicted to pass double the level of initial bias by June
2018, approximately 25 years before the lower bound
                                                               General Discussion
would pass neutrality. Crucially, the recent data from
the figure-stimuli test were included within the fore-         Evidence for long-term change in population-level
casted CIs of the face-stimuli test, suggesting that even      implicit attitudes counters the assumption that implicit
the most recent stable data from the figure-stimuli test       attitudes, being less conscious and controllable than
may still conform to a long-term pattern of change away        explicit attitudes, are necessarily immutable (Bargh,
from neutrality.                                               1999). Instead, clear evidence of change across three
   As with most other attitudes, implicit–explicit cor-        attitudes suggests that implicit attitudes can be gradu-
relations for body-weight attitudes did not change over        ally and durably changed at the population level, in the
the past decade. Additionally, Granger causality models        direction of decreasing prejudice. This result comple-
indicated no significant prediction of change in either        ments the currently limited evidence of long-term
direction, implying that implicit and explicit body-           individual-level implicit attitude change (e.g., Gawronski
weight attitudes are changing independently.                   et al., 2017).
   For the figure-stimuli test, stability was observed            Notably, uncovering long-term attitude change
across all respondents regardless of self-reported             requires statistical models that account for autocorrela-
weight. Additionally, this stability was observed across       tions and nonlinearity. This article offers the first exam-
baby boomers, Generation Xers, and millennials; Gen-           ple of applying time-series (ARIMA) models to the study
eration Zers revealed more substantial change away             of implicit attitudes and the Project Implicit data, and
from neutrality than other generations, suggesting that        the results challenge findings from linear multiple
the slight change away from neutrality may be attribut-        regressions. Past conclusions of stability in implicit race
able to a cohort-by-period interaction focused on the          attitudes (Schmidt & Axt, 2016; Schmidt & Nosek, 2010)
youngest cohort. For the face-stimuli test, movement           may result from fitting single linear slopes to nonlinear
away from neutrality was observed across all respon-           trends, thereby underestimating recent change. As in
dents, regardless of self-reported weight or generational      other areas of psychology, research on attitude change
cohort. This suggests that the early pattern of change         would benefit from embracing time-series models
away from neutrality could be attributed to a wide-            (Varnum & Grossmann, 2017).
spread period effect that changed the body-weight atti-
tudes of all respondents in the years before 2010.             Variability in rate and direction
Summary of results. Even within just a decade, all
                                                               of change
explicit attitudes revealed change toward neutrality,          Cross-attitude variability in the rate and direction of
implying that conscious and self-reported prejudice has        change warrants discussion. Examining overarching
decreased over time across attitudes. Crucially, long-term     features that cooccur with changing attitudes reveals
change was also observed across multiple implicit atti-        that, relative to stable attitudes (age, disability, body
tudes, with trends toward neutrality for sexuality, race,      weight), changing attitudes (race, skin tone, sexuality)
and skin-tone attitudes. Forecasts indicated vastly differ-    have lower overall bias, higher implicit–explicit correla-
ent rates of change among these three attitudes: Implicit      tions, and higher perceived societal priority (indexed
sexuality attitudes were predicted to pass attitude neu-       by Google searches). That lower overall bias and higher
trality as early as 9 years from 2016, whereas implicit        societal priority cooccur with faster change is predicted
skin-tone attitudes were predicted to take as long as 138      from theories of attitude strength (Petty & Krosnick,
years. Moreover, the notable change in implicit sexuality      1995), newly showing that such predictions extend to
attitudes was observed across all generations and demo-        implicit attitudes. However, that high implicit–explicit
graphic groups, whereas change in implicit race and            correlations correspond to faster change is, at first,
skin-tone attitudes was observed most strongly in millen-      unexpected: Under attitude-strength perspectives, high
nials and revealed demographic differences across racial       correlations are interpreted to reflect strong intra-
groups.                                                        attitudinal structure, which should correspond to slower
    Implicit disability and age attitudes revealed stability   change. An alternative interpretation, however, is that
over time, regardless of generational cohort or demo-          high implicit–explicit correlations reflect attitudes that
graphics. Implicit body-weight attitudes, on both face-        are frequently discussed (Nosek, 2007). From this per-
stimuli and figure-stimuli tests, revealed trends away         spective, both implicit–explicit correlations and Google
from neutrality over time across all generations and           search prevalence imply that frequency of discussion


190                                                                                              Charlesworth, Banaji

is a consequential determinant of long-term change in        researchers modeling implicit–explicit change would
implicit attitudes.                                          benefit from considering how the attitude target moder-
   Whereas three theoretical explanations are offered        ates processes of change.
for cross-attitude differences in rates of change, numer-
ous additional distinctions could be drawn. For instance,    Variability in change across
rapid change in sexuality attitudes may arise from the
unique concealability of sexual orientation (Pachankis
                                                             generations and demographics
et al., 2018), enabling positive contact before the stigma   Most implicit attitudes showed generalizable trends
is revealed. In contrast, unique trends away from neu-       across generational cohorts and across target and non-
trality in implicit body-weight attitudes may arise from     target demographic groups, despite the expectation that
factors such as an increasing focus on health and the        in-group preferences should dominate motivations to
obesity epidemic, the increasing numbers of overweight       change (Tajfel, 1982). Indeed, implicit sexuality atti-
individuals in the United States, and the perceived con-     tudes showed change across all cohorts and sexualities,
trollability of the stigma. Furthermore, we note that age,   newly suggesting that widespread and rapid attitude
disability, and body-weight attitudes involve a per-         change is not limited to self-report (Rosenfeld, 2017).
ceived but measurable decline of the body and may            Nevertheless, implicit race and skin-tone attitudes
therefore be seen to have an objective basis. In contrast,   revealed idiosyncratic differences by racial group,
race, skin-tone, and sexuality attitudes are not rooted      implying differential exposure to the causes of change,
in objective evidence but have emerged for arbitrary         perhaps due to greater segregation by race than by
and historic reasons (e.g., Sidanius & Pratto, 1999).        other demographics (e.g., age, sexuality). Additionally,
Such differences in perceived objectivity may contribute     race and skin-tone attitudes showed the fastest change
to the relative stability of age, disability, and body-      among millennials, suggesting that causes of change
weight attitudes.                                            are predominantly affecting young generations.

Variability in the implicit–explicit                         Sample generalizability and source
relationship over time                                       of change
Implicit and explicit change between two out of six          Two limitations for interpretation are raised by the use
attitudes (disability and body weight) showed no sig-        of cross-sectional web-based data. First, can the
nificant relationship, supporting dual-process predic-       observed change be generalized from this sample to
tions of dissociable implicit and explicit change (Rydell    U.S. society? The present sample is neither random nor
& McConnell, 2006). However, a relationship was found        representative, yet the results may be cautiously gen-
between implicit and explicit change in four attitudes,      eralized for at least four reasons, elaborated in the
although the direction was conclusive only for race and      Method section: (a) Weighting data to U.S. census
skin-tone attitudes. The presence of implicit–explicit       demographics did not substantively alter descriptions
associations speaks against complete dissociation, sug-      of change, (b) similar change in explicit attitudes is
gesting that the results may be better interpreted           observed in representative social surveys (General
through frameworks allowing for interactive implicit–        Social Survey, 2017), (c) similar magnitudes of implicit
explicit change (e.g., the associative-propositional-        attitudes are documented in natural representative
evaluation, or APE, model; Gawronski & Bodenhausen,          human language (Caliskan-Islam et al., 2016), and (d)
2006).                                                       the sample size and diversity offer improvement over
   Specifically, the current results imply that implicit     small samples in much of psychology and poor response
attitude change precedes explicit attitude change for        rates in probability samples.
race and skin-tone attitudes (corresponding to APE              The second potential limitation concerns the cause
Case 1), whereas exogenous influences likely cause           of change. Potential artifactual causes, including regres-
change in both implicit and explicit sexuality attitudes     sion to the mean and increased representation of cer-
(APE Case 6). In contrast, explicit age, disability, and     tain demographics, are shown not to account for the
body-weight attitude change may be negated before            observed change. Additionally, although strategies to
affecting implicit attitudes (APE Case 3). Although exist-   identify an independent age, period, or cohort effect
ing theories can inform these insights into the processes    remain beyond the scope of this article (Winship &
of attitude change, their predictions are derived from       Harding, 2008), initial explorations generally suggest
short-term individual-level data; processes of long-term     cohort-by-period interactions in long-term population-
population-level change may require theoretical revi-        level attitude change. Moreover, comparisons across
sions. Moreover, given variability across attitudes,         attitudes provide insight into features that cooccur with,


Patterns of Attitude Change                                                                                                        191

and may cause, implicit attitude change: low overall                 This article has received the badges for Open Data and
bias, high implicit–explicit correlation, and high societal          Open Materials. More information about the Open Practices
priority. Addressing these limitations provides confi-               badges can be found at http://www.psychologicalscience.org/
dence in the project’s contribution for generating and               publications/badges.
testing novel predictions about the patterns of long-
term population-level implicit and explicit attitude                 References
change.                                                              Albarracin, D., & Vargas, P. (2010). Attitudes and persua-
                                                                         sion: From biology to social responses to persuasive
Action Editor                                                            intent. In S. T. Fiske, D. T. Gilbert, & G. Lindzey (Eds.),
                                                                         Handbook of social psychology (Vol. 1, 5th ed., pp. 394–
James K. McNulty served as action editor for this article.
                                                                         427). Hoboken, NJ: John Wiley & Sons.
                                                                     Banaji, M. R., & Heiphetz, L. (2010). Attitudes. In S. T. Fiske,
Author Contributions                                                     D. T. Gilbert, & G. Lindzey (Eds.), Handbook of social
Both authors developed the study concept, drafted the manu-              psychology (Vol. 1, 5th ed., pp. 353–393). Hoboken, NJ:
script, and interpreted the data. T. E. S. Charlesworth analyzed         John Wiley & Sons.
the data under the supervision of M. R. Banaji. Both authors         Bargh, J. A. (1999). The cognitive monster: The case against
approved the final manuscript for submission.                            the controllability of automatic stereotype effects. In S.
                                                                         Chaiken & Y. Trope (Eds.), Dual-process theories in social
ORCID iD                                                                 psychology (pp. 361–382). New York, NY: Guilford Press.
                                                                     Caliskan-Islam, A., Bryson, J. J., & Narayanan, A. (2016).
Tessa E. S. Charlesworth          https://orcid.org/0000-0001-
                                                                         Semantics derived automatically from language corpora
5048-3088
                                                                         necessarily contain human biases. Science, 356, 183–186.
                                                                         doi:10.1126/science.aal4230
Acknowledgments                                                      Cryer, J. D., & Chan, K.-S. (2008). Time series analysis: With
We thank Patrick Mair for statistical guidance and Anthony               applications in R (2nd ed.). New York, NY: Springer-
Greenwald, Calvin Lai, Benedek Kurdi, Steven Pinker, Erin                Verlag. doi:10.1007/978-0-387-75959-3
Westgate, and Christopher Winship for their comments on              Dasgupta, N. (2013). Implicit attitudes and beliefs adapt to
the manuscript.                                                          situations: A decade of research on the malleability of
                                                                         implicit prejudice, stereotypes, and the self-concept. In
Declaration of Conflicting Interests                                     P. Devine & A. Plant (Eds.), Advances in experimental
                                                                         social psychology (Vol. 47, pp. 233–279). San Diego, CA:
The author(s) declared that there were no conflicts of interest          Academic Press. doi:10.1016/B978-0-12-407236-7.00005-X
with respect to the authorship or the publication of this            Devine, P. G., Forscher, P. S., Austin, A. J., & Cox, W. T. L.
article.                                                                 (2012). Long-term reduction in implicit race bias: A preju-
                                                                         dice habit-breaking intervention. Journal of Experimental
Funding                                                                  Social Psychology, 48, 1267–1278. doi:10.1016/j.jesp
This research was supported by Harvard University’s Dean’s               .2012.06.003
Competitive Fund for Promising Scholarship awarded to                Forscher, P. S., Mitamura, C., Dix, E. L., Cox, W. T. L., & Devine,
M. R. Banaji.                                                            P. G. (2017). Breaking the prejudice habit: Mechanisms,
                                                                         timecourse, and longevity. Journal of Experimental Social
                                                                         Psychology, 72, 133–146. doi:10.1016/j.jesp.2017.04.009
Supplemental Material
                                                                     Gawronski, B., & Bodenhausen, G. V. (2006). Associative
Additional supporting information can be found at http://                and propositional processes in evaluation: An integra-
journals.sagepub.com/doi/suppl/10.1177/0956797618813087                  tive review of implicit and explicit attitude change.
                                                                         Psychological Bulletin, 132, 692–731. doi:10.1037/0033-
Open Practices                                                           2909.132.5.692
                                                                     Gawronski, B., Morrison, M., Phills, C. E., & Galdi, S. (2017).
                                                                         Temporal stability of implicit and explicit measures: A
                                                                         longitudinal analysis. Personality and Social Psychology
Deidentified and cleaned data for this study, along with data-           Bulletin, 43, 300–312. doi:10.1177/0146167216684131
analysis scripts, have been made publicly available via the          General Social Survey. (2017). GSS data explorer: Key trends.
Open Science Framework and can be accessed at https://osf                Retrieved from https://gssdataexplorer.norc.org/trends
.io/px8h3/. The raw deidentified data and the materials from         Greenwald, A. G., McGhee, D. E., & Schwartz, J. L. K. (1998).
the Project Implicit demonstration website database are                  Measuring individual differences in implicit cognition: The
archived at https://osf.io/t4bnj/. The design and analysis plans         implicit association test. Journal of Personality and Social
for this study were not formally preregistered. The complete             Psychology, 74, 1464–1480. doi:10.1037/0022-3514.74.6.1464
Open Practices Disclosure for this article can be found at http://   Greenwald, A. G., Nosek, B. A., & Banaji, M. R. (2003).
journals.sagepub.com/doi/suppl/10.1177/0956797618813087.                 Understanding and using the implicit association test: I.


192                                                                                                            Charlesworth, Banaji

     An improved scoring algorithm. Journal of Personality            Payne, B. K., Vuletich, H. A., & Lundberg, K. B. (2017). The
     and Social Psychology, 85, 197–216. doi:10.1037/0022-                bias of crowds: How implicit bias bridges personal and
     3514.85.2.197                                                        systemic prejudice. Psychological Inquiry, 28, 233–248.
Grossmann, I., & Varnum, M. E. W. (2015). Social structure,               doi:10.1080/1047840X.2017.1335568
     infectious diseases, disasters, secularism, and cultural         Petty, R. E., & Krosnick, J. A. (Eds.). (1995). Attitude strength:
     change in America. Psychological Science, 26, 311–324.               Antecedents and consequences. Mahwah, NJ: Erlbaum.
     doi:10.1177/0956797614563765                                     R Core Team. (2017). R: A language and environment for
Hehman, E., Flake, J. K., & Calanchini, J. (2017). Disproportionate       statistical computing. Vienna, Austria: R Foundation for
     use of lethal force in policing is associated with regional          Statistical Computing.
     racial biases of residents. Social Psychological & Personality   Rosenfeld, M. J. (2017). Moving a mountain: The extraor-
     Science, 9, 393–401. doi:10.1177/1948550617711229                    dinary trajectory of same-sex marriage approval in the
Hyndman, R. J., & Khandakar, Y. (2008). Automatic time                    United States. Socius, 3. doi:10.1177/2378023117727658
     series forecasting: The forecast package for R. Journal of       Rydell, R. J., & McConnell, A. R. (2006). Understanding
     Statistical Software, 27(3). doi:10.18637/jss.v027.i03               implicit and explicit attitude change: A systems of reason-
Jebb, A. T., Tay, L., Wang, W., & Huang, Q. (2015). Time                  ing analysis. Journal of Personality and Social Psychology,
     series analysis for psychological research: Examining and            91, 995–1008. doi:10.1037/0022-3514.91.6.995
     forecasting change. Frontiers in Psychology, 6, Article 727.     Sawyer, J., & Gampa, A. (2018). Implicit and explicit racial
     doi:10.3389/fpsyg.2015.00727                                         attitudes changed during Black Lives Matter. Personality
Lai, C. K., Marini, M., Lehr, S. A., Cerruti, C., Shin, J. E. L.,         and Social Psychology Bulletin, 44, 1039–1059. doi:
     Joy-Gaba, J. A., . . . Nosek, B. A. (2014). Reducing implicit        10.1177/0146167218757454
     racial preferences: I. A comparative investigation of            Schmidt, K., & Axt, J. R. (2016). Implicit and explicit attitudes
     17 interventions. Journal of Experimental Psychology:                toward African Americans and Barack Obama did not
     General, 143, 1765–1785. doi:10.1037/a0036260                        substantively change during Obama’s presidency. Social
Lai, C. K., Skinner, A. L., Cooley, E., Murrar, S., Brauer, M.,           Cognition, 34, 559–588. doi:10.1521/soco.2016.34.6.559
     Devos, T., . . . Nosek, B. A. (2016). Reducing implicit          Schmidt, K., & Nosek, B. A. (2010). Implicit (and explicit)
     racial preferences: II. Intervention effectiveness across            racial attitudes barely changed during Barack Obama’s
     time. Journal of Experimental Psychology: General, 145,              presidential campaign and early presidency. Journal
     1001–1016. doi:10.1037/xge0000179                                    of Experimental Social Psychology, 46, 308–314. doi:
McNulty, J. K., Baker, L. R., & Olson, M. A. (2014). Implicit             10.1016/j.jesp.2009.12.003
     self-evaluations predict changes in implicit partner eval-       Sidanius, J., & Pratto, F. (1999). Social dominance: An inter-
     uations. Psychological Science, 25, 1649–1657. doi:10                group theory of social hierarchy and oppression. New York,
     .1177/0956797614537833                                               NY: Cambridge University Press. doi:10.2307/2655372
McNulty, J. K., Olson, M. A., Jones, R. E., & Acosta, L. M.           Stephens-Davidowitz, S. (2014). The cost of racial animus on
     (2017). Automatic associations between one’s partner and             a Black candidate: Evidence using Google search data.
     one’s affect as the proximal mechanism of change in                  Journal of Public Economics, 118, 26–40. doi:10.1016/j
     relationship satisfaction: Evidence from evaluative con-             .jpubeco.2014.04.010
     ditioning. Psychological Science, 28, 1031–1040. doi:10          Tajfel, H. (Ed.). (1982). Social identity and intergroup rela-
     .1177/0956797617702014                                               tions. Cambridge, England: Cambridge University Press.
Newport, F. (2013, July 25). In U.S., 87% approve of Black-           U.S. Census Bureau. (2016). QuickFacts: UNITED STATES.
     White marriage, vs. 4% in 1958. Gallup. Retrieved from               Retrieved from https://www.census.gov/quickfacts/table/
     http://www.gallup.com/poll/163697/approve-marriage-                  PST045216/00
     blacks-whites.aspx                                               Varnum, M. E. W., & Grossmann, I. (2017). Cultural change:
Nosek, B. A. (2007). Implicit–explicit relations. Current                 The how and the why. Perspectives on Psychological
     Directions in Psychological Science, 16, 65–69. doi:10               Science, 12, 956–972. doi:10.1177/1745691617699971
     .1111/j.1467-8721.2007.00477.x                                   Westgate, E. C., Riskind, R. G., & Nosek, B. A. (2015). Implicit
Nosek, B. A., Smyth, F. L., Hansen, J. J., Devos, T., Lindner,            preferences for straight people over lesbian women and
     N. M., Ranganath, K. A., . . . Banaji, M. R. (2007).                 gay men weakened from 2006 to 2013. Collabra, 1(1),
     Pervasiveness and correlates of implicit attitudes and               Article 1. doi:10.1525/collabra.18
     stereotypes. European Review of Social Psychology, 18,           Winship, C., & Harding, D. J. (2008). A mechanism-based
     36–88. doi:10.1080/10463280701489053                                 approach to the identification of age–period–cohort
Pachankis, J. E., Hatzenbuehler, M. L., Wang, K., Burton, C. L.,          models. Sociological Methods & Research, 36, 362–401.
     Crawford, F. W., Phelan, J. C., & Link, B. G. (2018). The            doi:10.1177/0049124107310635
     burden of stigma on health and well-being: A taxonomy of         Yarkoni, T., & Westfall, J. (2017). Choosing prediction over
     concealment, course, disruptiveness, aesthetics, origin, and         explanation in psychology: Lessons from machine learn-
     peril across 93 stigmas. Personality and Social Psychology           ing. Perspectives on Psychological Science, 12, 1100–1122.
     Bulletin, 44, 451–474. doi:10.1177/0146167217741313                  doi:10.1177/1745691617693393
