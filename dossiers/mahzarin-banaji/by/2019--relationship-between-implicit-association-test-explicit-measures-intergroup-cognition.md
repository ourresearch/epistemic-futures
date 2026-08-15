---
title: "Relationship between the Implicit Association Test and explicit measures of intergroup cognition: Data from the meta-analysis by Kurdi et al. (2018)"
person: mahzarin-banaji
section: by
type: preprint
year: 2019
date: 2019-03-18
venue: ""
authors: "Benedek Kurdi; Mahzarin R. Banaji"
source_url: https://banaji.sites.fas.harvard.edu/research/publications/articles/2019_Kurdi_ICE.pdf
doi: https://doi.org/10.31234/osf.io/vpcx8
openalex_id: https://openalex.org/W4236226561
cited_by_count: 3
retrieved: 2026-08-14
content: full-text
notes: "PROVENANCE: author-hosted PDF on her Harvard site, extracted with pdftotext -layout. Title-overlap check 1.00."
---

# Relationship between the Implicit Association Test and explicit measures of intergroup cognition: Data from the meta-analysis by Kurdi et al. (2018)

## Full text

Running head: THE IAT AND EXPLICIT MEASURES


 Relationship between the Implicit Association Test and explicit measures of intergroup cognition:
                         Data from the meta-analysis by Kurdi et al. (2018)


                              Benedek Kurdi and Mahzarin R. Banaji
                          Harvard University, Cambridge, Massachusetts


                                            Author Note

       Benedek Kurdi and Mahzarin R. Banaji, Department of Psychology, Harvard University.

       All data files and analysis scripts used in this project are available for download from the

Open Science Framework (https://osf.io/k7qx5/).

       Correspondence concerning this report should be addressed to Benedek Kurdi, Department

of Psychology, Harvard University, Cambridge, MA 02138, email: kurdi@g.harvard.edu


Running head: THE IAT AND EXPLICIT MEASURES                                                             2

 Relationship between the Implicit Association Test and explicit measures of intergroup cognition:
                          Data from the meta-analysis by Kurdi et al. (2018)

       In our recent meta-analysis (Kurdi et al., 2018), we reported detailed investigations of the re-

lationship between Implicit Association Tests (IATs; Greenwald, McGhee, & Schwartz, 1998)

measuring attitudes (e.g., White/Asian–good/bad), stereotypes (e.g., White/Asian–dumb/smart), and

identity (e.g., White/Asian–me/not me) and a wide range of criterion measures of intergroup behav-

ior. Although this was not a requirement for inclusion in the meta-analytic database, in addition to

implicit and criterion measures, some studies also reported explicit (self-report) measures of atti-

tudes, stereotypes, and identity.

       To the extent that explicit measures were used in the relevant studies, the dataset forming

the basis of the meta-analysis conducted by Kurdi et al. (2018) and made publicly available on the

Open Science Framework (OSF; https://osf.io/k7qx5/) contains information on implicit–explicit

correlations (IECs) as well as their moderator variables. With the exception of analyses concerning

incremental predictive validity, data on IECs were not analyzed by Kurdi et al. (2018). Unlike in

other investigations (Cameron, Brown-Iannuzzi, & Payne, 2012; Hofmann, Gawronski, Gschwend-

ner, Le, & Schmitt, 2005; Nosek, 2005), the implicit–explicit relationship was not of primary con-

cern to our recent meta-analysis; however, researchers interested in this relationship may still gain

valuable insights from the data generated there.

       As such, the present report includes a meta-analytic measure of effect size, followed by the

results of moderator analyses. Similar to the analyses reported by Kurdi et al. (2018), all analyses

reported here were conducted using correlated effects models (Hedges, Tipton, & Johnson, 2010),

which explicitly account for statistical dependencies among effect sizes extracted from the same

study. Analyses were implemented using the robumeta package (Fisher & Tipton, 2015) in the R


Running head: THE IAT AND EXPLICIT MEASURES                                                               3

statistical computing environment. The raw data and R code are freely available for download from

OSF (https://osf.io/k7qx5/).

                                      Meta-analytic effect size

       The meta-analytic effect size was estimated using an intercept-only correlated effects model

(Hedges et al., 2010) relying on 710 effect sizes extracted from 160 research reports with a com-

bined sample size of 10,218. The meta-analytic average of implicit–explicit correlations (IECs) sig-

nificantly differed from zero and was small in size, r = .12 [.09; .14], t(159) = 8.97, p < .001. The

90-percent prediction interval (Borenstein, Higgins, Hedges, & Rothstein, 2017) around the mean

effect size ranged from rmin = -.12 to rmax = .33, indicating that 90 percent of IECs in the intergroup

domain are expected to fall in the small negative to medium-sized positive range. This result corre-

sponds to a high level of heterogeneity and, as such, we report detailed analyses of the moderators

of the implicit–explicit relationship below.

                                        Moderator variables

       The results of moderator analyses involving six groups of moderator variables (basic study

characteristics, conceptual variables, study-level methodological variables, measure-level methodo-

logical variables, sample characteristics, and publication-related variables) are reported in Table 1,

with brief interpretations provided below.

Basic study characteristics

       The first group of moderators reported by Kurdi et al. (2018) concerned basic characteristics

of the studies, including study setting, target group, and type of behavior. Conceptually, type of be-

havior is independent of the implicit–explicit relationship; as such, here were report analyses in-

volving only study setting and target group. Paralleling the results on implicit–criterion correlations

(ICCs), we found that study setting (real-world, online, or lab) did not significantly moderate im-


Running head: THE IAT AND EXPLICIT MEASURES                                                                4

plicit–explicit correlations (IECs). By contrast and in deviation from the results obtained with ICCs

as the dependent variable, target group category emerged as a significant moderator: IECs were

highest for studies involving sexual orientation, with all other target group categories producing

significantly smaller effects.

Conceptual variables

       Similar to the results obtained with ICCs as the dependent measure, attribute concept (atti-

tude, stereotype, or identity) did not significantly moderate the implicit–explicit relationship. The

variables involving social sensitivity yielded conflicting results: Whereas the regular versions of

these variables produced significant effects, their blind-coded counterparts did not. Specifically, the

regular implicit and explicit social sensitivity variables both positively predicted the size of the im-

plicit–explicit correlation. This result is in conflict with the prevailing theoretical view according to

which implicit–explicit correlations should be especially high when social desirability concerns are

absent (Nosek, 2005). However, it should be noted that the effect size for both variables was small,

with only a difference of rdiff = .09 predicted between the lowest and highest possible values of so-

cial sensitivity. Moreover, the same result was not replicated using the blind-coded versions of the

same variables, thus raising the possibility that awareness of the study outcomes may have contami-

nated coding of the social sensitivity variable.

Study-level methodological variables

       Study-level methodological variables (including whether studies focused on the implicit–

criterion relationship, whether studies used a manipulation, and what kind of manipulation they

used) did not moderate the implicit–explicit relationship. However, it should be noted that the

study-level methodological variables were not primarily designed with the implicit–explicit rela-


Running head: THE IAT AND EXPLICIT MEASURES                                                                5

tionship in mind. A different set of study-level methodological variables specifically conceived to

address the implicit–explicit relationship may very well have impact.

Measure-level methodological variables

       Most measure-level methodological variables investigated also did not emerge as significant

moderators of the implicit–explicit relationship. Notably, (a) the order in which implicit and explicit

measures were administered within a study (implicit first, explicit first, or counterbalanced), (b) at-

tribute polarity (i.e., the extent to which the IAT attributes were polar opposites of each other; e.g.,

smart/dumb vs. smart/weak), and (c) target polarity (i.e., the extent to which the IAT attributes were

polar opposites of each other; e.g., White/Black vs. elderly/Asian) produced no effect. The only var-

iable that significantly moderated the implicit–explicit relationship was implicit scoring method,

with the D algorithm (Greenwald, Nosek, & Banaji, 2003) producing a higher average IEC than the

scoring algorithm originally introduced by Greenwald et al. (1998). This result should not be sur-

prising given that one of the criteria used to evaluate the D algorithm was that the scores produced

should maximize correlation with explicit measures.

Sample characteristics

       Some characteristics of the samples used significantly moderated the magnitude of the im-

plicit–explicit relationship. Specifically, online and real-world samples produced larger effects than

general samples, student samples, and samples preselected on some kind of measure (e.g., scores on

a depression scale). Moreover, the data suggest that implicit–explicit correlations may be lower in

American samples than in samples from outside the United States; however, this result did not reach

conventional levels of statistical significance. Within the same group of variables, type of student

sample (pre-college vs. college) and sample composition (stigmatized, nonstigmatized, or mixed)

did not produce significant effects.


Running head: THE IAT AND EXPLICIT MEASURES                                                                 6

Publication-related variables

       Finally, several publication-related variables significantly moderated the implicit–explicit

relationship. Specifically, (a) journal impact factor, (b) mean IAT experience (measured as mean

number of reports included in the meta-analytic database for the authors of the given report), (c)

first author IAT experience (measured as number of reports included in the meta-analytic database

for the first author of the given report), (d) maximum and (e) mean network centrality of the authors

of the report in a collaboration network emerging from all reports included in the meta-analytic da-

tabase, and (f) IAT originator status each positively predicted the magnitude of the implicit–explicit

correlation. By contrast, year of publication, publication status (published vs. unpublished), and

yearly citation count had no impact. Moreover, IAT experience and network centrality measured for

the last author of each report also did not produce a significant effect.

                                               Summary

       In the present report we provide a brief summary of the relationship between implicit and

explicit measures of social cognition based on the meta-analytic database analyzed in more detail

with respect to the relationship between measures of social cognition and measures of intergroup

behavior by Kurdi et al. (2018). In the present analysis, a statistically significant but small relation-

ship emerged between implicit and parallel explicit measures of attitudes, stereotypes, and identity.

       The implicit–explicit relationship was characterized by high levels of statistical heterogenei-

ty, thus making moderator analyses necessary. Implicit and explicit measures were more highly cor-

related with each other in studies (a) of sexual orientation (relative to other target group categories),

(b) using the improved scoring algorithm (Greenwald et al., 2003) to index IAT performance, (c)

conducted using real-world or online samples (relative to general, student, and preselected samples),


Running head: THE IAT AND EXPLICIT MEASURES                                                                 7

(d) conducted using foreign samples (relative to U.S. samples), and (e) conducted by authors with

higher levels of experience involving the Implicit Association Test.

        Other variables that, based on theoretical or practical considerations, may have been ex-

pected to produce an effect had no impact. Notably, (a) study setting (real-world, online, or lab), (b)

attribute concept (attitude, stereotype, or identity), (c) social sensitivity, (d) order of implicit and

explicit measures (implicit first, explicit first, or counterbalanced), and (e) publication status of the

report (published vs. unpublished) had no significant effect.


Running head: THE IAT AND EXPLICIT MEASURES                                                             8

                                              References

Borenstein, M., Higgins, J. P. T., Hedges, L. V., & Rothstein, H. R. (2017). Basics of meta-analysis:
    I2 is not an absolute measure of heterogeneity. Research Synthesis Methods, 8(1), 5–18.
    http://doi.org/10.1002/jrsm.1230
Cameron, C. D., Brown-Iannuzzi, J. L., & Payne, B. K. (2012). Sequential priming measures of im-
    plicit social cognition: a meta-analysis of associations with behavior and explicit attitudes. Per-
    sonality and Social Psychology Review, 16(4), 330–350.
    http://doi.org/10.1177/1088868312440047
Fisher, Z., & Tipton, E. (2015, March 7). robumeta: An R-package for robust variance estimation in
    meta-analysis. Retrieved from http://arxiv.org/abs/1503.02220
Greenwald, A. G., McGhee, D. E., & Schwartz, J. L. K. (1998). Measuring individual differences in
    implicit cognition: The Implicit Association Test. Journal of Personality and Social Psycholo-
    gy, 74(6), 1464–1480. http://doi.org/10.1037//0022-3514.74.6.1464
Greenwald, A. G., Nosek, B. A., & Banaji, M. R. (2003). Understanding and using the Implicit As-
    sociation Test: I. An improved scoring algorithm. Journal of Personality and Social Psycholo-
    gy, 85(2), 197–216. http://doi.org/10.1037//0022-3514.85.2.197

Hedges, L. V., Tipton, E., & Johnson, M. C. (2010). Robust variance estimation in meta-regression

    with dependent effect size estimates. Research Synthesis Methods, 1(1), 39–65.
    http://doi.org/10.1002/jrsm.5
Hofmann, W., Gawronski, B., Gschwendner, T., Le, H., & Schmitt, M. (2005). A meta-analysis on
    the correlation between the implicit association test and explicit self-report measures. Personal-
    ity and Social Psychology Bulletin, 31(10), 1369–1385.
    http://doi.org/10.1177/0146167205275613
Kurdi, B., Seitchik, A. E., Axt, J. R., Carroll, T. J., Karapetyan, A., Kaushik, N., et al. (2018). Rela-
    tionship between the Implicit Association Test and intergroup behavior: A meta-analysis. Amer-
    ican Psychologist. Advance online publication. http://doi.org/10.1037/amp0000364
Nosek, B. A. (2005). Moderators of the relationship between implicit and explicit evaluation. Jour-
    nal of Experimental Psychology: General, 134(4), 565–584. http://doi.org/10.1037/0096-
    3445.134.4.565


Running head: THE IAT AND EXPLICIT MEASURES                                                                                               9

Table 1. Summary table of univariate meta-regressions predicting implicit–explicit correlations (IECs) on the basis of moderator vari-
ables. Mean = mean of moderator variable, SD = standard deviation of moderator variable, ktotal = total number of effect sizes included
in the model, kind = number of independent effect sizes included in the model, b = unstandardized regression coefficient, CI lower =
lower bound of the 95-percent confidence interval, CI upper = upper bound of the 95-percent confidence interval, DF = degrees of
freedom, t = value of the t statistic, p = p value, τ2 = residual heterogeneity, [B] = blind-coded version of moderator variable. For cate-
gorical predictors (with their levels listed), b coefficients represent condition means, whereas for metric predictors, b coefficients rep-
resent units of change in the dependent variable (IEC) associated with one unit of change in the moderator variable. For categorical
moderators, asterisks in the superscript indicate a significant difference from the first (reference) category at p < .10, p < .05, and p <
.01, respectively.
        Moderator              Mean         SD        ktotal   kind       b       CI lower     CI upper     DF       t         p         τ2
                                                        (1) Basic study characteristics
Study setting
   Real-world                         –          –       68      16      0.180        0.055       0.300      15     3.06       .008      .049
   Online                             –          –      154      25      0.139        0.075       0.202      24     4.46     < .001      .026
   Lab                                –          –      488     119      0.101        0.074       0.127     118     7.53     < .001      .015
Target group category
   Sexuality                          –          –       24      8     0.218        0.150         0.285       7     7.39     < .001      .003
   Race**                             –          –      281     64     0.134        0.088         0.180      63     5.71     < .001      .030
   Ethnicity*                         –          –       78     19     0.129        0.086         0.172      18     6.27     < .001      .001
   Other intergroup***                –          –       55     13     0.093        0.028         0.157      12     3.11       .009      .004
   Gender***                          –          –      165     27     0.087        0.030         0.144      26     3.11       .005      .019
   Other clinical***                  –          –       42     14     0.056       -0.038         0.149      13     1.29       .218      .019
   Eating disorder***                 –          –       65     17     0.053       -0.010         0.115      16     1.78       .093      .006
                                                          (2) Conceptual variables
Concept
   Attitude                          –          –       420     123      0.118         0.087      0.149     122     7.40     < .001      .025
   Stereotype                        –          –       232      45      0.101         0.064      0.138      44     5.46     < .001      .011
   Identity                          –          –        58      12      0.087        -0.005      0.177      11     2.08       .061      .024
Implicit social sensitivity      5.342      1.567       710     160      0.014         0.000      0.028     158     1.98       .049      .020
Implicit social sensitivity
[B]                              4.553      1.707       710     160      0.014        -0.001      0.028     158     1.86       .064      .020
Explicit social sensitivity      5.261      1.621       710     160      0.016         0.001      0.031     158     2.18       .031      .021
Explicit social sensitivity
[B]                              4.985      1.518       710     160      0.003        -0.015      0.020     158     0.30       .761      .021


Running head: THE IAT AND EXPLICIT MEASURES                                                                            10

       Moderator           Mean       SD        ktotal  kind      b        CI lower CI upper     DF    t       p       τ2
                                            (3) Methodological variables: Study-level
Study focus
   Primary without
   moderator                      –        –      261     79      0.136       0.099      0.173    78   7.22   < .001   .019
   Secondary without
   moderator                      –        –       28     10      0.107      -0.027      0.237     9   1.81    .104    .024
   Primary with modera-
   tor                            –        –      161     34      0.102       0.051      0.151    33   4.09   < .001   .019
   Secondary with mod-
   erator                         –        –       22      6      0.088      -0.043      0.216     5   1.73    .145    .005
   Incidental                     –        –      238     31      0.082       0.025      0.139    30   2.92    .007    .039
Manipulation
   No                             –        –      375     89      0.120       0.086      0.153    88   6.96   < .001   .023
   Yes                            –        –      335     72      0.107       0.071      0.143    71   5.89   < .001   .011
Type of manipulation
   Within subjects                –         –      57     27      0.145       0.062      0.226    26   3.58     .001   .017
   Mixed                          –         –      72      9      0.138       0.094      0.182     8   7.09   < .001   .001
   Between subjects               –         –     203     35      0.074       0.037      0.111    34   4.05   < .001   .005
                                           (4) Methodological variables: Measure-level
Type of implicit measure
   IRAP                           –        –        8      4      0.128      -0.052      0.300     3   2.26     .109   .056
   IAT                            –        –      567    138      0.115       0.088      0.143   137   8.21   < .001   .021
   IAT variant                    –        –      135     22      0.112       0.046      0.177    21   3.53     .002   .035
Order of implicit and
explicit measures
   Random                         –        –      177     35      0.152       0.105      0.198    34   6.48   < .001   .024
   Explicit first                 –        –      187     52      0.113       0.063      0.163    51   4.52   < .001   .021
   Implicit first                 –        –      346     73      0.097       0.059      0.134    72   5.11   < .001   .016
Implicit scoring method
   D score                        –        –      452    111      0.132       0.101      0.163   110   8.33   < .001   .019
   Other                          –        –       74     21      0.077       0.015      0.139    20   2.59   < .001   .013
   1998 scoring**                 –        –      146     29      0.063       0.013      0.113    28   2.57   < .001   .013


Running head: THE IAT AND EXPLICIT MEASURES                                                                             11

       Moderator           Mean       SD       ktotal   kind      b       CI lower     CI upper   DF    t       p       τ2
Explicit scoring method
   Difference score              –        –      193     49     0.142         0.096      0.188     48   6.10   < .001   .028
   Relative rating*              –        –      109     22     0.119         0.056      0.181     21   3.93     .001   .017
   Single rating                 –        –      399    109     0.110         0.079      0.142    108   6.91   < .001   .020
Target polarity              2.546    0.732      688    155     0.003        -0.015      0.020    153   1.39     .168   .021
Attribute polarity           2.687    0.533      688    155     0.029        -0.008      0.066    153   1.57     .119   .021
                                                  (5) Sample characteristics
Stigmatized sample
   Only stigmatized               –        –     188     41      0.144        0.082      0.204     40   4.69   < .001   .030
   Mixed                          –        –     130     35      0.112        0.054      0.169     34   3.91   < .001   .026
   Nonstigmatized                 –        –     388    106      0.103        0.074      0.132    105   6.93   < .001   .016
Special sample
   Online                         –        –      72      11     0.180        0.056      0.298     10   3.23     .009   .036
   Real-world                     –        –     135      38     0.153        0.088      0.217     37   4.71   < .001   .028
   General**                      –        –      31      12     0.092        0.028      0.155     11   3.16     .009   .000
   Student**                      –        –     429      96     0.091        0.063      0.119     95   6.33   < .001   .012
   Preselected**                  –        –      39       8     0.070       -0.034      0.173      7   1.59     .156   .018
Student sample
   Undergrad & grad               –        –     440    106      0.089        0.061      0.116    105   6.37   < .001   .013
   Pre-college                    –        –      55      7      0.088        0.016      0.159      6   2.98     .025   .000
Sample country
   Foreign                        –        –     316     59      0.150         0.114     0.185     58   8.34   < .001   .019
   U.S.*                          –        –     394    104      0.099         0.065     0.132    103   5.85   < .001   .021
                                               (6) Publication-related variables
Year                      2010.366    2.503      710    160      0.004        -0.005     0.014    158   0.97    .333    .021
Publication status
  Published                      –        –      644    144      0.120        0.093      0.147    143   8.72   < .001   .021
  Unpublished                    –        –       66     16      0.075        0.002      0.147     15   2.18     .045   .021
Impact factor                2.598    2.567      581    133      0.004        0.000      0.008    131   2.00     .048   .021
Yearly citation count        6.491    6.534      710    160      0.002       -0.000      0.005    158   1.66     .098   .020
IAT experience (mean)        2.127    1.358      710    160      0.023        0.000      0.045    158   2.01     .047   .019
IAT experience (first)       1.987    1.243      710    160      0.022        0.001      0.009    158   3.41     .001   .019


Running head: THE IAT AND EXPLICIT MEASURES                                                                 12

       Moderator        Mean      SD      ktotal   kind    b      CI lower CI upper   DF     t      p       τ2
IAT experience (last)    2.580    2.627     710     160   0.004      -0.012   0.020   158   0.46    .644    .020
Authorship centrality
(max)                   433.486 905.559    710     160    0.000      0.000    0.000   158   2.98    .003    .018
Authorship centrality
(mean)                  156.024 352.151    710     160    0.000      0.000    0.000   158   2.04    .043    .019
Authorship centrality
(last)                  341.691 814.484    710     160    0.000     -0.000    0.000   158   0.85    .400    .020
IAT originators
   Yes                       –       –     118      15    0.210      0.113    0.303    14   4.60   < .001   .034
   No**                      –       –     589     146    0.102      0.077    0.127   145   7.96   < .001   .015
