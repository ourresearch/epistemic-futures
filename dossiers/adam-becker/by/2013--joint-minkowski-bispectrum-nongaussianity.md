---
title: "Joint Minkowski functionals and bispectrum constraints on non-Gaussianity in the cosmic microwave background"
person: adam-becker
section: by
type: journal-article
year: 2013
date: 2013-08-15
venue: "Physical review. D. Particles, fields, gravitation, and cosmology/Physical review. D. Particles and fields"
authors: "Wenjuan Fang, Adam Becker, Dragan Huterer, Eugene A. Lim"
source_url: https://doi.org/10.1103/physrevd.88.041302
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W1916076194; full text from arXiv preprint https://arxiv.org/abs/1303.4381 (pdftotext); may differ from published version. oa_status=green; cited_by=10."
---

# Joint Minkowski functionals and bispectrum constraints on non-Gaussianity in the cosmic microwave background

## Full text

### Abstract (from OpenAlex metadata)

Two of the most commonly used tools to constrain the primordial non-Gaussianity are the bispectrum and the Minkowski functionals of cosmic microwave background temperature anisotropies. These two measures of non-Gaussianity in principle provide distinct (though correlated) information, but in the past constraints from them have only been loosely compared and not statistically combined. In this work we evaluate, for the first time, the covariance matrix between the local non-Gaussianity coefficient ${f}_{\mathrm{NL}}$ estimated through the bispectrum and Minkowski functionals. We find that the estimators are positively correlated, with correlation coefficient $r\ensuremath{\simeq}0.3$. Using the WMAP7 data to combine the two measures and accounting for the point-source systematics, we find the combined constraint ${f}_{\mathrm{NL}}=37\ifmmode\pm\else\textpm\fi{}28$, which has a $\ensuremath{\sim}20%$ smaller error than either of the individual constraints.

### Full text (arXiv preprint version, pdftotext extraction)

Joint Minkowski Functionals and Bispectrum Constraints on Non-Gaussianity in the
CMB
Wenjuan Fang∗
Department of Astronomy, University of Illinois at Urbana-Champaign, 1002 W. Green St, Urbana, IL 61801 and
Department of Physics, University of Michigan, 450 Church St, Ann Arbor, MI 48109-1040

Adam Becker† and Dragan Huterer‡
Department of Physics, University of Michigan, 450 Church St, Ann Arbor, MI 48109-1040

arXiv:1303.4381v3 [astro-ph.CO] 25 Mar 2015

Eugene A. Lim§
Theoretical Particle Physics and Cosmology Group, Physics Department,
Kings College London, Strand, London WC2R 2LS, United Kingdom and
Centre for Theoretical Cosmology, Department of Applied Mathematics and Theoretical Physics,
University of Cambridge, Wilberforce Road, Cambridge CB3 0WA, United Kingdom
(Dated: March 6, 2022)
Two of the most commonly used tools to constrain the primordial non-Gaussianity are the bispectrum and the Minkowski functionals of CMB temperature anisotropies. These two measures of
non-Gaussianity in principle provide distinct (though correlated) information, but in the past constraints from them have only been loosely compared and not statistically combined. In this work
we evaluate, for the first time, the covariance matrix between the local non-Gaussianity coefficient
fNL estimated through the bispectrum and Minkowski functionals. We find that the estimators
are positively correlated, with correlation coefficient r ≃ 0.3. Using the WMAP7 data to combine
the two measures and accounting for the point-source systematics, we find the combined constraint
fNL = 37 ± 28, which has a ∼ 20% smaller error than either of the individual constraints.

I.

INTRODUCTION

Detection of any departures from Gaussianity in the
distribution of primordial fluctuations would give important information about inflation. Primordial nonGaussianity (henceforth NG) imprints signatures on the
cosmic microwave background (CMB) and large-scale
structure, and these cosmological probes can in turn provide excellent constraints on primordial NG and thus inflationary models; for reviews, see [1–4].
Two of the principal statistics on the CMB used to
constrain NG are the bispectrum (harmonic transform
of the three-point correlation function) of the CMB temperature fluctuations, and Minkowski functionals (henceforth MF) which roughly measure the connectedness or
morphology of the CMB field. In the “local” model of
NG, the primordial curvature perturbation Φ(x) has a
quadratic term correction: Φ = ΦG + fNL (Φ2G − hΦ2G i),
where ΦG is an auxiliary Gaussian field [5]. Recent constraints obtained on the non-linear coupling constant fNL
using the WMAP data are fNL = 37 ± 20 from the bispectrum analysis [6] (see also [7, 8]), and fNL = 20 ± 42
from the MF analysis [9].
Since MF are morphological statistics, they probe NG
both in configuration space and to all orders of the statistics of the temperature anisotropy field. This means

∗ wjfang@illinois.edu
† beckeram@umich.edu
‡ huterer@umich.edu
§ eugene.a.lim@gmail.com

that they sample the anisotropy map differently from the
usual bispectrum (and higher order polyspectra) measurements, albeit in a suboptimal way – this fact is crucial as joint constraints will in principle yield different
constraints. Furthermore, unlike the bispectrum estimators which require a template (i.e. k-space configuration
with a free amplitude) such as the local, equilateral or
orthogonal type, MF are in principle template-free, although in practice one can construct a template-based
MF estimator as we have done in this paper.
In principle, the MF are sensitive to the weighted sum
of the bispectrum coefficients (out to the smallest scale
measured) [10], so the MF would naively be expected to
contain only a subset of the same information as the bispectrum. In reality, however, this idealized expectation is
not borne out: the bispectrum and the MF partially complement each other, and their information is not 100%
correlated. One reason for this is the fact that the optimal bispectrum estimators [11, 12] are computationally challenging to implement for current high-precision
CMB experiments [8, 13], and they are anyway only optimal for the case of vanishing non-Gaussianity [14, 15].
Moreover, the bispectrum and MF are sensitive to different astrophysical and analysis-related systematics, given
that they are defined in the harmonic and real space respectively. Hence, combining the constraints obtained
by current fast though sub-optimal bispectrum estimators with those from the MF, as we do in this paper,
provides an alternative to improving the “optimality” of
these estimators, and makes the combined constraints
both stronger and more robust.
Hence an obvious question is how correlated are the MF

2
and the bispectrum estimators, and consequently what is
the combined constraint on NG from them. This is the
question that we address in this paper – we will show
that the correlation between the two estimators, while
nonzero, is far from maximal. Having calculated that, we
compute the joint estimate of NG from both statistics.

II.

MINKOWSKI FUNCTIONALS
METHODOLOGY

The three Minkowski functionals Vi (i = 0, 1, 2) describe morphological properties of the hot and cold spots
in the CMB temperature map. The morphology of the
map, and thus the MF, are studied by specifying a temperature threshold ν ≡ (∆T /T )/σ0 in the map, where
σ0 is the rms of the fractional temperature fluctuation
∆T /T , hereafter simply denoted as f . Specifically, V0
is the area fraction of the regions above the temperature threshold, V1 is their boundary length, and V2 is
the geodesic curvature integrated along their boundary,
which in a compact S2 space is related to the Euler characteristic χ by χ = V2 + V0 /2π [16]. The MF can be
expressed as integrals of functions of the anisotropy field
and its derivatives over the compact space of the CMB
sky. For explicit expressions see e.g. [10, 16]; we shall
adopt these operationally convenient forms to calculate
the MF for a given map.
If the temperature fluctuations are Gaussian, the ensemble averages of the Minkowski functionals have analytic expressions that are completely specified by the
two-point statistics (variance) of the fluctuations, σ02 and
σ12 (≡ h|∇f |2 i) [17]. On the other hand, when the fluctuations are weakly non-Gaussian and the cumulants hf n ic
(where “c” stands for the connected part) satisfy the hierarchical ordering hf n ic ∼ σ02n−2 , one can obtain an
order-by-order expansion in powers of σ0 for the average of the Minkowski functionals [18, 19]. In this letter, we consider the first order in the hierarchical nonGaussian expansion, which in addition to σ0 and σ1 depends on the three-point statistics (skewness) of the field:
S ≡ hf 3 i, SI ≡ hf 2 ∇2 f i, SII ≡ 2h|∇f |2 ∇2 f i. The two
variance and the three skewness parameters can be calculated from theory by integrating over the power spectrum and bispectrum of the CMB field, respectively; for
explicit expressions, see [9, 10]. In the special case of the
local-type primordial non-Gaussianity, S, SI , SII are all
linearly proportional to fNL .
In this Letter, we use the co-added V+W band data
from the WMAP seven-year results [20] to obtain our
constraints on fNL . The V and W bands are chosen
for they are the most foreground-free. For this purpose,
we generate 1000 simulations of the WMAP data following the procedure given in Appendix A of [21]. The
only difference (aside from using the WMAP7 cosmological model) is that we used a uniform weighting for the
maps, rather than the slightly more complicated weighting given there, since it only gives a marginal improve-

ment in estimating fNL . Each of our simulated map is
the sum of three components: 1) the Gaussian CMB realizations (the “signal”) based on the CMB power spectrum calculated assuming the best-fit WMAP seven-year
cosmology including the effect of beam smearing, 2) instrumental noise modeled
√ as the Poisson process with the
rms noise per pixel σ/ Nobs , where σ is the rms noise per
observation and Nobs is the number of observations per
pixel, and 3) unresolved point sources modeled as the
Poisson realizations from assuming a single population
of sources with a fixed frequency-independent flux whose
flux strength and number density roughly reproduce the
source power spectrum and bispectrum measured from
the WMAP Q band. The latter two components are
modeled to closely match the systematics expected in the
V+W co-added map. We then mask both the WMAP
data and our simulated maps by using the KQ75 mask.
To make predictions for the ensemble average of the
Minkowski functionals when various observational effects
are present, we should also include these effects in the
calculations of the two variance parameters and three
skewness parameters. Each of these parameters has contributions from the noise part – instrumental noise and
point sources, in addition to the beam-smeared CMB signal part. The noise and signal contributions add up directly since the CMB signal and noise are uncorrelated.
We estimate these noise contributions from our simulations: we calculate the variance and skewness parameters
for each simulated map, and take their average over the
1000 samples; we then subtract off the signal contributions which are known to us for these Gaussian CMB
simulations.
Before we proceed to the fitting procedure and obtain
our Minkowski functional constraints on fNL , we address
the “residual problem” in our numerical evaluation of
the Minkowski functionals. Previous work [22] found
that, even for a set of Gaussian CMB simulations without noise, the averages of the MF calculated for each
map are different from their values expected from theory. As shown in [23], these residuals are generated by
the discrete binning of the MF in the threshold ν, and for
weakly non-Gaussian maps can be calculated analytically
and then subtracted order by order in σ0 . In this work,
we instead follow [22] and calculate the residuals from
our simulations as the difference of the sample-averaged
means of the MF and their theoretically expected means.
These residuals are then subtracted from the measured
Minkowski functionals. We use the same residuals to account for those for the non-Gaussian case: for a weakly
non-Gaussian field, the differences are at the order of σ0 .
Before we calculate the Minkowski functionals for each
map, we smooth the map at several different angular
scales. This allows us to extract additional information
from the map and tighten the constraints on fNL . Specifically, we use a Gaussian window function, and smooth
each map at five different scales with the Full Width Half
Maximum (FWHM) θ set at θ = 100 , 200 , 400 , 800 , 1000 .
Pixels within a distance of θ away from the boundary of

3
the KQ75 mask are removed to avoid contamination from
the masked regions that may be introduced due to the
smoothing. Ideally, one may want to smooth the maps at
infinitely many scales and extract the constraint on fNL
by integrating over them. Clearly, this cannot be done in
reality. The five smoothing scales we choose range from
roughly the resolution of the WMAP V+W band data
to the scale at which only ∼ 40% of the map remains
for analysis. (Note, the larger the smoothing scale, the
bigger the area to be removed to avoid contamination.)
Combining the results at the five smoothing scales allows
us to recover most of the available information. For each
smoothed map, we calculate its three Minkowski functionals at 15 temperature thresholds from ν = −3.5 to
3.5 with equal bin size of ∆ν = 0.5.
To obtain the constraints on fNL , we perform a χ2
analysis, which compares theoretical predictions at a
given fNL to the measurements, and is calculated as
X
 −1  obs

Viobs − Vith (fNL ) Cij
Vj − Vjth (fNL ) ,
χ2 =

Minkowski
Functionals

(1)
where i and j run over all combinations of the 15 thresholds, three orders, and five smoothing scales for the
measured Minkowski functionals. Here Viobs are the
“observed” numerically evaluated Minkowski functionals,
Vith are the theoretically expected averages for the MF
(which are functions of fNL ), and C is the covariance matrix for (Vi , Vj ) which we calculate from our simulations
as
Cij = h(Vi − hVi i) (Vj − hVj i)isim ,

(2)

where the angular brackets denote averaging over the
1000 simulated maps. We then obtain our best-fit value
MF
of fNL , henceforth fNL
, by minimizing the χ2 .
MF
is unbiased, we
To check that our estimator for fNL
first apply it to the 1000 simulated maps either for the
MF measurements at each smoothing scale or their combined results. We find that the average of the best-fit
values accurately reproduces the theoretical input in our
simulation, i.e., fNL = 0. Next, we test our estimator on
publicly available non-Gaussian CMB maps generated
with the local-type NG [24], and we again find negligible
bias (1% or less of the true fNL ) in our estimator.
Finally, we apply our estimator on the co-added V+W
band data from the WMAP. In Table I, we show the
MF
constraints on fNL
from smoothing the map at each of
the five angular scales, and the joint constraint from all
scales combined, which we quote as our final MF conMF
straint: fNL
= 29 ± 33. This constraint is consistent
with that found by Hikage & Matsubara [9], although we
improve upon their analysis in a couple of ways: 1) we
remove the residuals in the numerically evaluated MFs
using the method from [22], as opposed to the residual
removal based on the work in [23] which, we found, causes
MF
biases in the estimated fNL
by ∼ 10. and 2) we carefully
include point sources in our simulated WMAP maps.

fNL

10
20
40
80
100
all

71 ±96
−21 ± 52
−2 ± 49
40 ±73
−16±92
29 ± 33

bispectrum

46 ± 35

MF + bisp

37 ±28

TABLE I. Constraints on fNL from the CMB Minkowski functionals, bispectrum, and their combination. The analyses use
the WMAP 7-year V+W co-added map. θ is the FWHM of
the Gaussian beam used to smooth the map for the Minkowski
functional analysis.

III.

i,j

θ(0 )

BISPECTRUM METHODOLOGY

MF
obtained, we next deWith the MF estimator of fNL
bisp
velop fNL – the estimator from bispectrum. The observed CMB bispectrum is given by
!
X
`1 `2 `3
B `1 `2 `3 =
a`1 m1 a`2 m2 a`3 m3 , (3)
m1 m2 m3
m1 m2 m3

where the matrix is the Wigner-3j symbol, and a`m is
the spherical harmonic transform of the temperature
anisotropy map. In the local-type NG model, B`1 `2 `3
is linearly proportional to fNL .
We follow the prescription that uses the KSW [25] esbisp
timator to calculate fNL
from CMB maps (see also [26]
for the exact implementation that we use). In brief, the
KSW is a cubic (in the temperature field) estimator of
non-Gaussianity; it is nearly minimum-variance and computationally fast, and can straightforwardly deal with
partial sky coverage and inhomogeneous noise. The first
ingredient in using KSW is to calculate the Fisher matrix F corresponding to fNL ; for this we need the theoretical bispectrum B`theory
which can be calculated with
1 `2 `3
the help of transfer functions from CAMB [27]. Furthermore, KSW requires filtered maps A(n̂, r) and B(n̂, r)
from which the skewness S of the field can be calculated;
these filtered maps can be computed using HEALPix (by
way of HealPy) to perform the forwards and backwards
spherical harmonic transforms that are necessary in their
computation. Given the skewness and the Fisher matrix,
the KSW estimator for fNL is
bisp
fNL
=

S
.
F

(4)

To account for the masking of the CMB sky, we make
the substitution S → Scut = S/fsky + Slinear [28]. Slinear

4
is an addition to skewness and is calibrated to account
for partial-sky observations
Z
Z

1
2
2
r dr d2 n̂ A(n̂, r)hBsim
(n̂, r)iMC
Slinear = −
fsky
+2B(n̂, r)hAsim (n̂, r)Bsim (n̂, r)iMC ] .
(5)
The subscripted filtered maps Asim and Bsim are created from Python-produced Gaussian Monte Carlo realizations of the cut CMB sky; the brackets hiMC indicate
an average over 300 of the maps. The simulated maps
were produced as outlined earlier when we discussed the
MF.
Applying the bispectrum/KSW estimator to the coadded V+W band data of the WMAP, we obtain the
bisp
constraint on the local NG to be fNL
= 46 ± 35. The
error we obtained is larger than that from Ref. [20] using
the same data because we have used a bispectrum estimator that is less optimal but much more convenient to
evaluate.

IV.

COMBINED ANALYSIS

In addition to obtaining the constraints on fNL separately from the MF and bispectrum analyses, we would
like to combine them to extract a more stringent and
robust result. To make the problem tractable, we opt
to consistently combine the estimators of fNL from these
two analyses, rather than attempting to find the covariance between the observables, i.e. the MF and bispectrum themselves. It is a reasonably good assumption that
the two estimators of fNL satisfy a bivariate Gaussian
distribution, especially near the peak of the distribution
(see Figure 1 below). Let us organize the two estimators
bisp
MF
, fNL
], and let C be the
into a row-vector fNL ≡ [fNL
2 × 2 covariance matrix for them. Assuming the underlying true value of fNL is f¯NL , we can write down the
following joint-distribution for the two fNL estimators


1
L ∝ |C|−1/2 exp − (fNL − f̄NL )C−1 (fNL − f̄NL )T ,
2
(6)
where f̄NL = [f¯NL , f¯NL ] ≡ f¯NL I. Given a measurement
of fNL , a best estimate for f¯NL can be obtained by maximizing L. Assuming that the covariance matrix does
not depend on f¯NL , we find the following expressions for
the best estimate and variance of f¯NL from the combined
analysis
I C−1 fNL T
f¯NL =
,
I C−1 IT

σf2¯NL =

1
I C−1 IT

.

(7)

bisp
MF
At the same time, by evaluating both fNL
and fNL
for the 1000 simulated WMAP maps, we numerically obtain their joint distribution, as shown in Figure 1. From
this distribution, we can deduce their correlation. We

bisp
MF
FIG. 1. Joint-distribution of fNL
and fNL
from 1000 simulations of the WMAP data including point sources and instrumental noise. We find a correlation coefficient of r = 0.32 ±
MF
estimates are obtained from the combination
0.03. The fNL
of smoothing the maps at θ(FWHM) = 100 , 200 , 400 , 800 , 1000 .
The contours show the 68% and 95% confidence regions of
bisp
MF
, fNL
) with its
the bivariate Gaussian distribution for (fNL
covariance matrix derived from the simulations.

find that the two estimators of fNL are positively correlated, with a correlation coefficient of r = 0.32 ± 0.03.
We are using the MF constraints from combining the
five smoothing scales, as these are the final interesting
MF constraints. However, we also find positive correbisp
lations between fNL
and the MF constraints obtained
at each individual smoothing scale: specifically, r varies
from 0.46 to 0.2 when θ increases from 100 to 1000 .
The covariances√or off-diagonal elements of C are then
C12 = C21 = r C11 C22 ; recall that we already found
the variances to be C11 = 332 and C22 = 352 . We find
the bivariate Gaussian distribution with the derived covariance matrix C gives a good description of the joint
bisp
MF
distribution of (fNL
, fNL
) for the simulated maps: the
68%, 95% contours enclose roughly the same percentages
(±1%) as in the simulated maps, and the orientation of
the two distributions agree, see Figure 1.
Using the numerically derived covariance matrix C,
bisp
MF
together with our best-fits for fNL
and fNL
, we find
through Eq. (7) the combined constraint to be
MF+bisp
f¯NL ≡ fNL
= 37 ± 28,

(8)

which has a ∼ 20% improvement in the error with respect
to the individual constraints.

5
V.

CONCLUSIONS

We evaluated, for the first time, the full covariance
matrix for the Minkowski functional estimator of the
MF
local-type primordial non-Gaussianity fNL
and the bisbisp
pectrum estimator fNL . We found the correlation coefficient r = 0.32 ± 0.03, and used it to combine the
constraints from the MF and bispectrum (and their respective variances) to obtain the constraint in Eq. (8).
Combining these two estimators hence provides an alternative to improving their “optimality” and leads to
combined constraints that are both stronger and more
robust. Our work can be extended by using more optimal estimators, e.g. the bispectrum estimator described
in [12] whose calculation is numerically very challenging,
and by applying to the Planck data, which we leave for
future work.
One convenient feature of this work is that, by combining the constraints at the level of MF and bispectrum
estimators, we make the problem tractable: an obvious
first approach could be to calculate the covariance be-

[1] E. Komatsu, Class. Quant. Grav. 27, 124010 (2010).
[2] N. Bartolo, E. Komatsu, S. Matarrese, and A. Riotto,
Phys. Rept. 402, 103 (2004).
[3] M. Liguori, E. Sefusatti, J. Fergusson, and E. Shellard,
Adv.Astron. 2010, 980523 (2010).
[4] A. P. Yadav and B. D. Wandelt, Adv.Astron. 2010,
565248 (2010).
[5] E. Komatsu and D. N. Spergel, Phys. Rev. D 63, 063002
(2001).
[6] C. L. Bennett et al., arXiv:1212.5225 (2012).
[7] A. P. Yadav and B. D. Wandelt, Phys.Rev.Lett. 100,
181301 (2008).
[8] K. M. Smith, L. Senatore, and M. Zaldarriaga, JCAP
0909, 006 (2009).
[9] C. Hikage and T. Matsubara, Mon. Not. R. Astron. Soc.
425, 2187 (2012).
[10] C. Hikage, E. Komatsu, and T. Matsubara, Astrophys.
J. 653, 11 (2006).
[11] D. Babich, Phys. Rev. D72, 043003 (2005).
[12] P. Creminelli, A. Nicolis, L. Senatore, M. Tegmark, and
M. Zaldarriaga, JCAP 0605, 004 (2006).
[13] P. Ade et al. (Planck Collaboration), arXiv:1303.5084
(2013).
[14] P. Creminelli, L. Senatore, and M. Zaldarriaga, JCAP
0703, 019 (2007).
[15] M. Liguori, A. Yadav, F. K. Hansen, E. Komatsu,
S. Matarrese, et al., Phys.Rev. D76, 105016 (2007).

tween the observed bispectrum and MF themselves, but
this is extremely complicated, given that the MF and
bispectrum are functions of many scales and/or thresholds. Combining the different estimators numerically,
as we have done here for the case of local NG, can in
principle be rather straightforwardly extended to other
types of NG and other cosmological probes. This type of
approach is therefore likely to become more widespread
with new and better data.

ACKNOWLEDGEMENTS

We thank Licia Verde for useful comments. We acknowledge the use of the publicly available CAMB [27]
and HEALPix [29] packages. WF is supported by NASA
grant NNX12AC99G. WF, AB and DH have been supported by the DOE and NSF at the University of Michigan. WF and DH thank the Aspen Center for Physics,
which is supported by the NSF Grant No. 1066293, for
the hospitality in the summer of 2012.

[16] J. Schmalzing and K. M. Gorski, Mon. Not. R. Astron. Soc. 297, 355 (1998).
[17] H. Tomita, Progress of Theoretical Physics 76, 952
(1986).
[18] T. Matsubara, Astrophys. J. 584, 1 (2003).
[19] T. Matsubara, Phys. Rev. D 81, 083505 (2010).
[20] E. Komatsu et al., Astrophys. J. Suppl. 192, 18 (2011).
[21] E. Komatsu et al., Astrophys. J. Suppl. 180, 330 (2009).
[22] C. Hikage et al., Mon. Not. R. Astron. Soc. 389, 1439
(2008).
[23] E. A. Lim and D. Simon, J. Cosmol. Astropart. Phys. 1,
048 (2012).
[24] F. Elsner and B. D. Wandelt, Astrophys. J. Supp. 184,
264 (2009).
[25] E. Komatsu, D. N. Spergel, and B. D. Wandelt, Astrophys.J. 634, 14 (2005).
[26] A. Becker and D. Huterer, Phys.Rev.Lett. 109, 121302
(2012).
[27] A. Lewis, A. Challinor, and A. Lasenby, Astrophys.J.
538, 473 (2000).
[28] A. P. S. Yadav, E. Komatsu, B. D. Wandelt, M. Liguori,
F. K. Hansen, and S. Matarrese, Astrophys. J. 678, 578
(2008).
[29] K. Gorski, E. Hivon, A. Banday, B. Wandelt, F. Hansen,
et al., Astrophys.J. 622, 759 (2005).
