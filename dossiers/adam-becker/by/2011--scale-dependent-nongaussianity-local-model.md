---
title: "Scale-dependent non-Gaussianity as a generalization of the local model"
person: adam-becker
section: by
type: journal-article
year: 2011
date: 2011-01-11
venue: "Journal of Cosmology and Astroparticle Physics"
authors: "Adam Becker, Dragan Huterer, Kenji Kadota"
source_url: https://doi.org/10.1088/1475-7516/2011/01/006
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W2005440443; full text from arXiv preprint https://arxiv.org/abs/1009.4189 (pdftotext); may differ from published version. oa_status=bronze; cited_by=43."
---

# Scale-dependent non-Gaussianity as a generalization of the local model

## Full text

### Abstract (from OpenAlex metadata)

We generalize the local model of primordial non-Gaussianity by promoting the parameter f NL to a general scale-dependent function f NL ( k ). We calculate the resulting bispectrum and the effect on the bias of dark matter halos, and thus the extent to which f NL ( k ) can be measured from the large-scale structure observations. By calculating the principal components of f NL ( k ), we identify scales where this form of non-Gaussianity is best constrained and estimate the overlap with previously studied local and equilateral non-Gaussian models.

### Full text (arXiv preprint version, pdftotext extraction)

Preprint typeset in JHEP style - HYPER VERSION

arXiv:1009.4189v3 [astro-ph.CO] 15 Jan 2011

Scale-Dependent Non-Gaussianity as a Generalization
of the Local Model

Adam Becker, Dragan Huterer, Kenji Kadota
Department of Physics and Michigan Center for Theoretical Physics
University of Michigan, 450 Church Street, Ann Arbor, MI 48109

Abstract: We generalize the local model of primordial non-Gaussianity by promoting the
parameter fNL to a general scale-dependent function fNL (k). We calculate the resulting
bispectrum and the effect on the bias of dark matter halos, and thus the extent to which
fNL (k) can be measured from the large-scale structure observations. By calculating the
principal components of fNL (k), we identify scales where this form of non-Gaussianity is
best constrained and estimate the overlap with previously studied local and equilateral
non-Gaussian models.
Keywords: Cosmology.

Contents
1. Introduction

1

2. Scale dependent non-Gaussianity

2

3. Non-Gaussianity and Bias
3.1 The effect of a non-vanishing bispectrum on bias
3.2 From the bispectrum to bias
3.2.1 Constant fNL
3.2.2 Scale-dependent fNL

3
3
5
5
6

4. Forecasted measurements of the scale-dependent nongaussianity
4.1 Fisher Matrix Analysis

7
7

5. Projection and Principal Components
5.1 Constraining other fNL (k) models
5.2 Principal components and relation to local and equilateral models

9
9
11

6. Conclusions

14

7. Acknowledgements

15

A. Calculating the error on an arbitrary parametrized fNL (k)

15

B. Principal Components of fNL (k)

16

C. Generalized local ansatz does not recover the equilateral case

17

1. Introduction
Primordial non-Gaussianity provides cosmology one of the precious few connections between primordial physics and the present-day universe. Standard inflationary theory, with
a single slowly rolling scalar field, predicts that the spatial distribution of structures in
the universe today is very nearly Gaussian random (e.g. [1, 2, 3, 4, 5]; for excellent recent
reviews, see [6, 7]). Departures from Gaussianity, barring contamination from systematic
errors or late-time non-Gaussianity due to secondary processes, would be a violation of this
standard inflationary assumption. Constraining or detecting primordial non-Gaussianity
is therefore an important basic test of the standard cosmological model.
Most of the study of non-Gaussianity in the literature to date has been carried out
assuming the magnitude of departure from Gaussianity is scale-independent (e.g. [8, 9, 10]).

–1–

However, the assumption that fNL is constant for a wide range of scales could be an oversimplification, since the primordial cosmic perturbations were presumably produced from
the time-dependent dynamics in the early universe. In particular, single-field inflationary
models with interactions, along with most multi-field models, generically produce scaledependent non-Gaussianity. It is therefore not surprising that scale-dependence of nonGaussianity has been discussed in the community in recent years [11, 12, 13, 14, 15, 16,
17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]. Notably, the parameterization of the
scale-dependent non-Gaussianity in our analysis is applicable to the curvaton [30, 31, 32,
33, 34] and the modulated reheating scenarios [35, 36], which are of great interest for their
potentially observable scale-dependent non-Gaussianity1 .
Motivated by such inflationary models that predict detectable scale-dependent nonGaussianity, as well as a desire to have an easily usable basis for studying those models,
we present a novel scale-dependent ansatz for primordial non-Gaussianity: we promote the
parameter fNL to a free function of wavenumber fNL (k). We define our model (Sec. 2),
predict clustering bias of dark matter halos in our model (Sec. 3), obtain an upper bound
on the accuracy with which these new parameters could be measured with a future largescale structure survey (Sec. 4), and compare our model with other parameterizations of
non-Gaussianity in the literature (Sec. 5).

2. Scale dependent non-Gaussianity
The most commonly discussed model of non-Gaussianity, often referred to as the local
model, is defined via [8]
Φ(x) = φG (x) + fNL (φG (x)2 − hφG (x)2 i).

(2.1)

Here, Φ denotes the primordial curvature perturbations (Bardeen’s gauge-invariant potential), φG (x) is a Gaussian random field, and the constant fNL is the non-Gaussianity
parameter. The local model has been much studied, in part because it is the first two
terms of the most general local form of non-Gaussianity [40].
In Fourier space, Eq. (2.1) becomes
Z
Φ(k) = φG (k) + fNL

d3 k 0
φG (k 0 )φG (k − k 0 ).
(2π)3

(2.2)

(Hereafter, we omit the subscript G on the Gaussian distribution when it is clear from
context.) In this paper, we study a model that generalizes Eq. (2.2) – we allow fNL to
vary with k as well, while assuming isotropy and homogeneity (so fNL (k) = fNL (k)). The
1

For instance, when the observed perturbations originate from the single curvaton field, the “running”
(with scale) of the non-Gaussianity parameter is proportional to the third derivative of the curvaton potential, V 000 [37, 38, 39]. Given that this third derivative is not tightly constrained from the observed
power spectrum, it can potentially lead to observable and scale-dependent non-Gaussianity. Therefore,
constraints on the running of non-Gaussianity can be a powerful probe of the origin of the primordial
curvature perturbations.

–2–

gravitational potential in the new model is defined via
Z
d3 k 0
Φ(k) = φ(k) + fNL (k)
φ(k 0 )φ(k − k 0 ).
(2π)3

(2.3)

As mentioned above, this form of non-Gaussianity is expected in curvaton or modulated
reheating scenarios (see e.g. Ref. [37], where this form explicitly appears in the study of
these models).
Note that this new ansatz is not local, which is clear when we transform back into real
space:
Φ(x) = φ + fNL (x) ∗ (φ(x)2 − hφ(x)2 i),
(2.4)
where ∗ represents convolution and x denotes a three-dimensional spatial coordinate. These
primordial perturbations Φ(k) are related to the present-time (z=0) smoothed linear overdensity δR by the Poisson equation:
δR (k) =

2 k 2 T (k)
W̃R (k)Φ(k) ≡ MR (k)Φ(k);
3 H02 Ωm

(2.5)

where T (k) is the matter transfer function, H0 is the Hubble constant, Ωm is the matter
density relative to critical today, and W̃R (k) is the Fourier transform of the top-hat filter
with radius R. The smoothing spatial scale R is related to the smoothing mass scale M
via
4
M = πR3 ρm,0 ,
(2.6)
3
where ρm,0 is the matter energy density today. The choice of mass scale is discussed further
in section 4.1.
The bispectrum in our generalized model becomes
Bφ (k1 , k2 , k3 ) = 2[fNL (k1 )Pφ (k2 )Pφ (k3 ) + perm.],

(2.7)

where Pφ is the power spectrum of potential fluctuations. This reduces to the familiar
expression B(k1 , k2 , k3 ) = 2fNL (Pφ (k1 )Pφ (k2 ) + perm.) when fNL is a constant.
Notice the difference between our ansatz for the scale-dependent fNL (k) (which has
the corresponding bispectrum Eq. (2.7)) and the particular form of scale-dependent nonGaussianity, discussed elsewhere in the literature, which is defined as fNL (k1 , k2 , k3 ) ≡
Bφ (k1 , k2 , k3 )/[2Pφ (k1 )Pφ (k2 ) + perm.] ([25, 27, 26]). The two forms are inequivalent, and
either form can be borne out in realistic inflationary models; however, given that our form
lives in a lower-dimensional k-space, it is easier to simulate it numerically [41] or treat it
with the Fisher matrix analysis, as we do in this paper.

3. Non-Gaussianity and Bias
3.1 The effect of a non-vanishing bispectrum on bias
Dalal et al. [42] found, analytically and numerically, that the bias of dark matter halos
acquires strong scale dependence if fNL 6= 0:
b(k) = b0 + fNL (b0 − 1)δc

–3–

3Ωm H02
.
a g(a)T (k)c2 k 2

(3.1)

Here, b0 is the usual Gaussian bias (on large scales, where it is constant), δc ≈ 1.686
is the collapse threshold, a is the scale factor, Ωm is the matter density relative to the
critical density, H0 is the Hubble constant, k is the wavenumber, T (k) is the transfer
function, and g(a) is the growth suppression factor2 . This result has been confirmed by
other researchers using a variety of methods, including the peak-background split [43, 44,
45, 46], perturbation theory [47, 48, 49], and numerical (N-body) simulations [50, 51, 52].
Astrophysical measurements of the scale dependence of the large-scale bias, using galaxy
and quasar clustering as well as the cross-correlation between the galaxy density and CMB
anisotropy, have recently been used to impose constraints on fNL already comparable to
those from the cosmic microwave background (CMB) anisotropy [45, 43], giving fNL =
28 ± 23 (1σ), with some dependence on the assumptions made in the analysis [45]. In the
future, constraints on fNL are expected to be on the order of a few [42, 53, 54, 55]. The
sensitivity of the large-scale bias to other models of primordial non-Gaussianity has not
yet been investigated much (though see analyses in e.g. [56, 57]).
Following the MLB formula [58, 59], one can express the two point correlation function of dark matter halos, ξh (x1 , x2 ), in terms of certain configurations of the correlation
(N )
functions of the underlying density field, ξR . In the high-threshold limit (ν  1), this
becomes:
ξh (x1 , x2 ) = ξh (x12 )


"
#
N
ν
1
x
,
...,
x
,
x
,
...,
x
(N )
1
1
2
2
 ;(3.2)
= −1 + exp 
ξ
N j!(N − j)! R
j
times
(N
−
j)
times
σ
N =2 j=1 R
∞
−1
X NX

where xij = |xi − xj |, ν = δc /σR represents the peak height, and ξR (n) (r) is the n-point
correlation function of the underlying matter density smoothed with a top-hat filter of
radius R. Keeping the terms up to the three-point correlation function, which would be
reasonable for the observationally allowed range of fNL , the expansion series gives us the
halo correlation function in terms of the field correlation functions:
ξh (x12 ) =

ν 2 (2)
ν 3 (3)
ξ
(x
,
x
)
+
1
2
2 R
3 ξR (x1 , x1 , x2 ).
σR
σR

(3.3)

The Fourier transform of the real-space correlation function – the power spectrum –
is given, to the same expansion order as Eq. (3.3), by
Z
ν2
ν3
d3 q
Ph (k) = 2 PR (k) + 3
BR (k, q, |k − q|) + . . .
(3.4)
(2π)3
σR
σR
The first term on the right-hand side includes the familiar (Gaussian) bias b = ν/σR (in
the high-peak limit for which the MLB formula is valid) for the Gaussian fluctuations. The
effects of non-Gaussianity on the galaxy bias are represented by the second term, including
the bispectrum BR , which vanishes for the Gaussian fluctuations.
2

The usual linear growth D(a), normalized to be equal to a in the matter-dominated epoch, is related
to the suppression factor g(a) via D(a) = ag(a), where g(a) is normalized to be equal to unity deep in the
matter-dominated epoch.

–4–

3.2 From the bispectrum to bias
If we denote the full bias of dark matter halos by b + ∆b, where b represents the bias for
the Gaussian fluctuations and ∆b is the non-Gaussian correction, then


∆b 2
Ph
2
=b 1+
,
(3.5)
PR
b
where Ph and PR are the power spectra of halos and dark matter, respectively. The nonGaussian correction to the linear peak bias to the leading order becomes
Z
1
∆b
ν
d3 q
(k) =
BR (k, q, |k − q|),
(3.6)
b
σR 2PR (k)
(2π)3
where BR is the matter bispectrum on scale R. Hence, the non-Gaussian correction ∆b(k)
can be expressed in terms of the primordial potential fluctuations as ([44]):
Z ∞
Z 1
Bφ (k1 , k2 , k)
1
∆b
δc
2
(k) =
dk
k
M
(k
)
dµMR (k2 )
.
(3.7)
1 1
R 1
2
2
b
D(z) 8π σR MR (k) 0
Pφ (k)
−1
We perform the integration over all triangles. The triangles’ sides are k1 , k2 , and k; the
cosine of the angle opposite k2 is µ, so k22 = k12 + k 2 + 2k1 kµ. MR (k) is the same function
defined in Eq. (2.5), and the time dependence of the critical threshold for collapse is given
as δc (z) = δc /D(z), with δc = 1.686.
3.2.1 Constant fNL
Eq. (3.7) leads to the famous scale-dependent bias formula in the case of a constant fNL .
For this model, the bispectrum is
Bφ (k1 , k2 , k3 ) = 2fNL [Pφ (k1 )Pφ (k2 ) + perm.].

(3.8)

Through Eq. (3.7), this leads to the result


Z
Z
Pφ (k2 )
δc
2fNL
∆b
2
(k) =
dk1 k1 MR (k1 )Pφ (k1 ) dµMR (k2 )
+2
2 M (k)
b
D(z) 8π 2 σR
Pφ (k)
R
≡

2fNL δc F(k)
,
D(z) MR (k)

(3.9)

where
1
F(k) ≡ 2 2
8π σR

Z

dk1 k12 MR (k1 )Pφ (k1 )

Z




Pφ (k2 )
dµMR (k2 )
+2 .
Pφ (k)

(3.10)

Note that there is a factor of 2 in Eq. (3.9) because we can exchange the order of integration
of terms corresponding to k1 and k2 .
Finally, we rewrite Eq. (3.9) by defining
Z
Z
1
2
F1 (k) ≡
dk1 k1 MR (k1 )Pφ (k1 ) dµMR (k2 )Pφ (k2 ) (3.11)
2 M (k)P (k)
8π 2 σR
R
φ
Z
Z
2
2
dk1 k1 MR (k1 )Pφ (k1 ) dµMR (k2 ).
(3.12)
F2 (k) ≡
2 M (k)
8π 2 σR
R

–5–

Then, for constant fNL ,
2fNL δc
∆b
(k) =
[F1 (k) + F2 (k)] ,
b
D(z)

(3.13)

and the derivative with respect to fNL is


∆b
2δc
∂
(k) =
[F1 (k) + F2 (k)] .
∂fNL b
D(z)

(3.14)

3.2.2 Scale-dependent fNL
Now we repeat the analysis of the previous section, but we allow fNL (k) to be an arbitrary function of scale, adopting the ansatz in Eq. (2.3). We still assume homogeneity, so
fNL (~k) = fNL (k). The bispectrum is given by
Bφ (k1 , k2 , k3 ) = 2[fNL (k1 )Pφ (k2 )Pφ (k3 ) + perm.].

(3.15)

Here, the triangle condition always holds, so that (for example) k1 = |k~2 + k~3 |. Following
Eq. (3.7), we get
Z
∆b
2
δc
(k) =
dk1 k12 MR (k1 )Pφ (k1 )
2 M (k)
b
D(z) 8π 2 σR
R


Z
Pφ (k2 )
+ 2fNL (k2 ) .
(3.16)
×
dµMR (k2 ) fNL (k)
Pφ (k)
This looks like Eq. (3.9) – but this time, fNL (k) is a function, not a constant. Thus, to
find the derivative of ∆b/b(k) with respect to the relevant parameters, we must parametrize
fNL (k) in a way that is valid for any general form of fNL (k). We consider the piecewisei in the ith wavenumconstant (in wavenumber) parametrization where fNL (k) is equal to fNL
ber bin:
i
fNL
≡ fNL (ki ).
(3.17)
i is:
The derivative of ∆b/b(k) with respect to these fNL


∂
∆b
δc
2
×
(ki ) =
2
j
2
D(z) 8π σR MR (k)
∂fNL b


δij

1
Pφ (k)
Z

+2
k2 ∈kj

Z

dk1 k12 MR (k1 )Pφ (k1 )

dk1 k12 MR (k1 )Pφ (k1 )

Z

Z
dµMR (k2 )Pφ (k2 )+ (3.18)
#
dµMR (k2 ) ,

where δij is the Kronecker delta function. Note that the last integral over k2 only goes
over the jth wavenumber bin.
This derivative can be rewritten more concisely as


i
∂
∆b
2δc h
j
(k
)
=
δ
F
(k)
+
F
(k)
.
(3.19)
i
ij 1
2
j
b
D(z)
∂fNL
The functions F1 and F2 are defined as in Eqs. (3.11) and (3.12), except that the superscript
in F2j indicates that the integral over k2 is to be executed only over the jth wavenumber
bin.

–6–

4. Forecasted measurements of the scale-dependent nongaussianity
4.1 Fisher Matrix Analysis
j
With an expression for ∂/∂fNL
[(∆b/b)(ki )] in hand (Eq. (3.19)), we can calculate the Fisher
j
information matrix for the parameters fNL
that describe the piecewise-constant fNL (k).
The Fisher matrix, in turn, allows us to forecast the extent to which the scale-dependent
non-Gaussianity could be measured in future galaxy surveys.
We consider measurements of the power spectrum Ph (k) of dark matter halos (galaxies
or clusters, for example) averaged over thin spherical shells in k-space. The variance of
Ph (k) ≡ Ph in each shell is [60]

σP2 h =

2Ph2
Vshell Vsurvey



1 + nPh
nPh

2

(2πPh )2
= 2
k dk Vsurvey



1 + nPh
nPh

2
,

(4.1)

where Vshell = 4πk 2 dk/(2π)3 is the volume of the shell in Fourier space (we are ignoring redshift distortion effects for simplicity here). Therefore, the Fisher matrix for measurements
of Ph (k, z) is [61]
Fij =

X
m

Z kmax
Vm
kmin

∂Ph (k, zm ) ∂Ph (k, zm )

∂pi
∂pj

1
1
Ph (k, zm ) +
n

2

k 2 dk
,
(2π)2

(4.2)

where Vm is the comoving volume of the m-th redshift bin, each redshift bin is centered
on zm , and we have summed over all redshift bins. We adopt kmin = 10−4 h−1 Mpc,
and we choose kmax as a function of z so that σ(π/(2kmax ), z) = 0.5 [62], which leads to
kmax (z = 0) ≈ 0.1h Mpc−1 . Finally, pi are the parameters of interest; in our case, these
i .
are the fNL
We assume a flat universe and a fiducial model of zero non-Gaussianity: fNL (k) =
i . We include six cosmological parameters in our Fisher matrix aside from the
0 = fNL
2
2
i : Hubble’s constant H ; physical dark matter and baryon densities Ω
fNL
0
cdm h and Ωb h ;
equation of state of dark energy w; the log of the scalar amplitude of the matter power
spectrum, log As ; and the spectral index of the matter power spectrum, ns . Fiducial values
of these parameters correspond to their best-fit WMAP7 values [63]. We also added the
forecasted cosmological parameter constraints from the CMB experiment Planck by adding
its Fisher matrix as a prior (W. Hu, private communication). Note that the CMB prior
does not include CMB constraints on non-Gaussianity; the CMB constraints on fNL (k) will
be separately studied in a future work. Finally, in addition to the cosmological parameters
i , we include five Gaussian bias parameters in our Fisher matrix – one b (z)
and the fNL
0
for each redshift bin. The fiducial values of these parameters are set by the relations
b0 (z = 0) = 2.2, and b0 (z) = b0 (z = 0)/D(z).
i , so the derivative
We already have the derivatives of b(k) with respect to each of the fNL
i
of Ph (k) with respect to the fNL is just
∂Ph (k)
∂b(k)
=2
b(k)Pmat (k);
i
i
∂fNL
∂fNL

–7–

(4.3)

Pmat (k) is the ΛCDM matter power spectrum, easily obtained from a numerical code such
as CAMB. Since we only consider information from large scales (k ≤ kmax ≈ 0.1 h Mpc−1 ),
we do not model the small amount of nonlinearity present at the high-k end of these scales.
We assume a future survey covering one-quarter of the sky (about 10,000 square dei
grees) out to z = 1, and find constraints for a set of 20 fNL
uniformly spaced in log k in
−1
−4
the range 10 ≤ k/(h Mpc ) ≤ 1, with a smoothing scale of Msmooth = 1014 M . Fig. 1
shows the resulting unmarginalized (left panel) and marginalized (right panel) constraints
i . For both sets of constraints, we first marginalized over the other
on the parameters fNL
i
cosmological parameters.3 The fNL
have most of their degeneracy among themselves; a
i
plot showing the fully unmarginalized constraints on the fNL
would not look much difi
have support at
ferent than the left panel of Fig. 1. Note that, while some of the fNL
−1
k > kmax (z = 1) ≈ 0.2 h Mpc , we only use information about those (and other) parameters coming from k < kmax . The constraints vary considerably as a function of the
i
k at which these parameters are defined. The best-constrained fNL
corresponds to the
−0.8
−0.6
16 ) = 7.3; for
10
< k < 10
bin, and it has an estimated unmarginalized error of σ(fNL
i , which corresponds to the largest scale (smallest k)
comparison, the worst-constrained fNL
bin, has an unmarginalized error well over one billion.
As expected, the marginalized constraints for the best-constrained parameters are
i
much weaker than the unmarginalized constraints – even the best-measured fNL
has an
2
estimated marginalized error of 6 × 10 . In general, dependence of the constraints on the
value of k is determined by two competing factors: as k increases, there is a larger number
of modes, each with a smaller signal (given by the smaller nongaussian bias ∆b). The
best-constrained k is also affected by the fact that only information out to k = kmax =
0.1h Mpc−1 is assumed from the galaxy survey. In particular, we have checked that if we
unrealistically assume information to be available at all k (instead of at k < kmax ) without
i improve monotonically
modeling the nonlinearities, the unmarginalized constraints on fNL
i
increases with k. To
with increasing k. Therefore, the raw signal-to-noise ratio in fNL
further demonstrate the effect of the choice of kmax (z), we also plotted the errors obtained
with the condition σ(π/(2kmax ), z) = 0.15, which yields kmax (z = 0) ≈ 0.03.
The smoothing mass scale chosen for this analysis (see Eq. (2.5)) has a small but
noticeable effect on the constraints yielded. Figure 2 shows that, in the case of the unmarginalized errors, the k at which non-Gaussianity is best constrained decreases as the
smoothing mass scale increases. (The behavior of the marginalized errors is more comi .) Since the mass scale is
plicated due to correlations in errors between neighboring fNL
proportional to the physical scale (to the third power), this means that best-constrained
k decreases with increasing smoothing scale R, which is exactly what we should expect.
We remind the reader that while a survey filtered at some scale Msmooth contains objects roughly more massive than this scale, in practice the near-exponentially falling mass
function implies that the number density is dominated with M ≃ Msmooth halos.
3

i
Using six cosmological parameters along with five b0 (z) and 20 fNL
led us into some issues with floatingpoint errors and numerical precision. The 31 × 31 Fisher matrix we obtained was rather ill-conditioned and
difficult to invert reliably using 64-bit precision; we were eventually forced to move to 128-bit precision in
order to accurately marginalize over the cosmological parameters.

–8–

1010
109
108
107
106
105
104
103
102
101
0
1010
-4

10-3

10-2

k (h/Mpc)

10-1

kmax(z =0) =0.03 h/Mpc
kmax(z =0) =0.10 h/Mpc

i
Forecasted Error in fNL

kmax(z =0) =0.03 h/Mpc
kmax(z =0) =0.10 h/Mpc

i
Forecasted Error in fNL

1010
109
108
107
106
105
104
103
102
101
0
1010
-4

100

(a) Unmarginalized errors

10-3

10-2

k (h/Mpc)

10-1

100

(b) Marginalized errors

Figure 1: Estimated unmarginalized (left panel) and marginalized (right panel) constraints on
i
piecewise-constant parameters fNL
assuming a future galaxy survey covering one-quarter of the sky
out to z = 1, with average number density of 2×10−4 gal/Mpc3 . For comparison, the green line is the
constraint found for a constant fNL using the same survey assumptions, and the red histograms are
i
the constraints found with a lower kmax (see text for details). While the individual parameters fNL
are poorly constrained as expected, their few best linear combinations – the principal components
– are well measured; see the next section and text for details.

109

109

M =1012 M ¯
M =1014 M ¯
M =1016 M ¯

107
106

108
i
Forecasted Error in fNL

i
Forecasted Error in fNL

108

107
106

105

105

104

104

103

103

102

102

101
100

10-4

101
10-3

10-2

k (h/Mpc)

10-1

0
1010
-4

100

(a) Unmarginalized errors

M =1012 M ¯
M =1014 M ¯
M =1016 M ¯
10-3

10-2

k (h/Mpc)

10-1

100

(b) Marginalized errors

Figure 2: Estimated constraints obtained from future surveys with the same parameters as the
previous figure at different mass smoothing scales Msmooth (labeled as M in the legend). In other
words, these are errors for a survey with halos of M & Msmooth .

5. Projection and Principal Components
5.1 Constraining other fNL (k) models
i , it is quite simple
Once the Fisher matrix F has been obtained for the set of parameters fNL
i that could be obtained from a future galaxy
to find the best possible constraints on the fNL

–9–

redshift survey. By projecting this Fisher matrix into another basis (see Appendix A), it
is also possible to find the constraints on any arbitrary fNL (k) without calculating a new
Fisher matrix from scratch. A trivial example can be found in Appendix A, where we find
that the estimated error on a constant fNL , assuming the same future survey as in the
previous section, is σ(fNL ) = 2.1. (Note that this forecasted constraint is on a par with
the error expected from Planck, where σ(fNL ) ∼ 5.)
For another, scale-dependent example, consider the simple form of non-Gaussianity
analogous to the conventional parameterization of the power spectrum
 nNG
k
∗
fNL (k) = fNL
,
(5.1)
k∗
∗ and n
where k∗ is an arbitrary fixed parameter, leaving fNL
NG as the parameters of interest
∗ and n
in this model. (k∗ is generally chosen to minimize degeneracy between fNL
NG for
−1
the observable of interest. We have set k∗ = 0.165h Mpc , close to the optimal value in
our case; in CMB analysis, the optimal value is lower, around 0.06h Mpc−1 .) The partial
i with respect to these parameters are:
derivatives of our basis of fNL
 nNG
i
∂fNL
k
=
;
(5.2)
∗
∂fNL
k∗
 nNG
 
i
∂fNL
k
k
∗
= fNL
log
.
(5.3)
∂nNG
k∗
k∗
i evenly spaced in log k, we project down to a basis of f ∗ and
Starting in a basis of 20 fNL
NL
nNG in order to forecast constraints on the two new parameters from a survey covering onequarter of the sky out to z = 1. We are using the same limits of integration as in Section
∗ = 50 and n
4.1, along with the fiducial values fNL
NG = 0. The forecasted constraints on
∗
these parameters, marginalized over each other, are σfNL
= 1.7 and σnNG = 0.58. Despite
a superficial similarity between this model and the model used by Sefusatti et al. in [23],
the two models are quite different, and our results cannot be compared. The model used
in [23] is a function of three arguments, k1 , k2 , and k3 :
 nN G
K
∗
fNL (k1 , k2 , k3 ) = fNL
,
(5.4)
k∗

where K = (k1 k2 k3 )1/3 . This leads to a bispectrum of the form found in Eq. (3.8), but
with fNL (k1 , k2 , k3 ) in place of fNL , whereas our bispectrum is of the less-factorizable form
Eq. (2.7).
Another example we consider is the form of non-Gaussianity in which the running on
fNL itself has running; that is, the case in which nNG is a function of k. A simple case of
this would be fNL of the form4
B
fNL (k) = eAk .
(5.5)
i to the parameters A and B,
Projecting the Fisher matrix down from the original basis fNL
with fiducial values of A = log 50 and B = 0, we obtain forecasted constraints of σA = 1.0
and σB = 0.15. (In this case, the survey characteristics and bounds of integration are the
same as in the previous example.)
4

Analogous parameterization for the power spectrum and its motivations are discussed in [64].

– 10 –

Figure 3: The first four principal components of fNL (k). The PCs, e(j) (k), are eigenvectors of
i
the Fisher matrix for the fNL
, and are ordered from the best-measured one (j = 0) to the worstmeasured one (j = 19) for the assumed fiducial survey.

5.2 Principal components and relation to local and equilateral models
We now represent a general function fNL (k) in terms of principal components (PCs). In this
approach, the data determine which particular modes of fNL (k) are best or worst measured.
The PCs also constitute a useful form of data compression, so that one can keep only a
few of the best-measured modes to make inferences about the function fNL (k). Finally, the
PCs will also enable us to measure the degree of similarity between our scale-dependent
ansatz and the local and equilateral forms of non-Gaussianity.
It is rather straightforward to start from the covariance matrix for the piecewise coni and obtain the PCs of f
stant parameters fNL
NL (k). The PCs are weights in wavenumber
with amplitudes that are uncorrelated by construction, and they are ordered from the
best-measured (i = 0) to the worst-measured (i = 19) for the assumed fiducial survey.
The construction of the PCs is described in Appendix B. A few of these PCs of fNL (k)
are shown in Fig. 3. For example, the best-measured PC has most of its weight around
k = 10−0.4 h Mpc−1 , which agrees with sensitivities of piecewise-constant parameters shown
in Fig. 1. The sensitivity is not greatest at the largest value of k (1 h Mpc−1 ) because we
assumed cosmological information from k ≤ kmax = 0.1 h Mpc−1 . We checked that information available at a higher kmax would shift the “sweet spot” of sensitivity to higher
wavenumbers.

– 11 –

Figure 4: RMS error on each principal component, along with the cumulative error.

The error in the best-measured PC is 4.8; however, the error in the next-best measured
PCs are 18.3 and 27.4, and the accuracy rapidly drops off from there. Thus, the first three
or four PCs should be enough for any conceivable application. The error in each PC is
plotted on a logarithmic scale in figure 4, along with the cumulative error σcum , which is
defined as
X 1
1
=
(5.6)
2.
2
σcum
σ
i
i
Each PC e(j) (k) has its own associated bispectrum (see Eq. (2.7)):
B (j) (k1 , k2 , k3 ) = 2[e(j) (k1 )P (k2 )P (k3 ) + e(j) (k3 )P (k1 )P (k2 ) + e(j) (k2 )P (k3 )P (k1 )]. (5.7)
(As always, k1 , k2 , and k3 have a triangle relation: k3 = |k~2 − k~1 |.) We would like to test the
similarity of these bispectra to those that have already been discussed in the literature. We
can do this by using a distance measure between bispectra, defined by ‘cosines’ developed
in [40]. A cosine near unity implies that the two bispectra have very similar shapes, and a
cosine near zero implies the opposite. The cosine is defined as
B1 · B2
cos(B1 , B2 ) = p
,
(B1 · B1 ) (B2 · B2 )
where the inner product between two bispectra, B1 · B2 , is [23]
X B1 (k1 , k2 , k3 )B2 (k1 , k2 , k3 )
B1 · B2 =
.
∆2 B(k1 , k2 , k3 )

(5.8)

(5.9)

k1 ,k2 ,k3

The (Gaussian) variance of the bispectrum is
∆2 B(k1 , k2 , k3 ) =

1
1
P (k1 )P (k2 )P (k3 ) ∼
(k1 k2 k3 )−3 ,
NT
NT

– 12 –

(5.10)

B (0)
B (1)
B (2)
B (3)

Local cosine
0.669
0.040
0.099
0.189

Equilateral cosine
0.074
0.000
0.030
0.037

Table 1: Cosines of the first four principal-component derived bispectra with the local bispectrum
and the equilateral bispectrum. A cosine near unity implies that the two bispectra have very similar
shapes, and a cosine near zero implies the opposite. Note that the zeroth PC, which is by far the
best measured (see Fig. 4), has a much larger overlap with the local model than with the equilateral,
as expected.

where NT is the number of distinct triangular configurations of k1,2,3 , and P (k) ∼ k −3 is
the primordial curvature perturbation power spectrum. (The overall constant is irrelevant,
since it cancels out in Eq. (5.8).)
We first compare our bispectra Eq. (5.7) to the local model with a constant fNL , whose
bispectrum is (see Eqs. (2.1) and (3.8))
Blocal (k1 , k2 , k3 ) ∝

1

1

1

+
+
.
k13 k23 k13 k33 k23 k33

(5.11)

Most of the power of Blocal is in so-called “squeezed” triangles, in which one side is much
smaller than the other two (comparable) sides, k1 << k2 ≈ k3 .
Another form for the bispectrum much discussed in the literature is the “equilateral”
bispectrum
Bequi (k1 , k2 , k3 ) = −

1
1
2
−Blocal (k1 , k2 , k3 )+
+
+permutations. (5.12)
(k2 k1 k3 )2
k1 k22 k33 k3 k12 k23

In contrast with Blocal , most of the power of Bequi is in triangles where k1 ≈ k2 ≈ k3 ; hence
the name “equilateral”.
Table 1 lists the cosines of the first few principal-component derived bispectra with
the local bispectrum and the equilateral bispectrum. The form of Eq. (5.7) suggests that
the PC-derived bispectra B (j) will have more in common with the local bispectrum than
the equilateral one. However, it is initially conceivable that some e(j) (k) might exist which
would yield a bispectrum of the form in Eq. (5.12) when substituted into Eq. (5.7) – but
in Appendix C, we prove that no such function exists. Thus, the only guarantees for the
cosines of the B (j) are that the cosine of B (0) – the bispectrum corresponding to the bestmeasured PC – will be large with the local model, and that none of the B (j) have a very
large cosine with the equilateral model. We expect the former because our model looks
like the local model; we expect the latter because of the proof in Appendix C. Table 1
bears out this expectation. The small cosines with the equilateral form of non-Gaussianity
are also unsurprising because equilateral non-Gaussianity is expected to have a strongly
suppressed signal in the non-Gaussian halo bias [57].

– 13 –

6. Conclusions
In this paper we have suggested a new phenomenological model of primordial nongaussianity by generalizing the local model (parametrized with a constant parameter fNL ) to
a scale-dependent, non-local class of models. There are multiple ways to do this, and our
choice was to write the Newtonian potential as
Φ(x) = φG (x) + fNL (x) ∗ (φG (x)2 − hφG (x)2 i),

(6.1)

where the convolution in real space corresponds to multiplication in k-space, featuring
an arbitrary function fNL (k). Explicit calculations show that such a form of the scale
dependent fNL is borne out in inflationary models [11, 14, 37, 38, 39].
We calculated the bispectrum and bias of dark matter halos in this class of models, following the formalism valid for high peaks [58, 59]. We then specialized in the
piecewise-constant (in wavenumber) parametrization of fNL (k) which, for the case of narrow enough k-bins, recovers any arbitrary function. We used forecasted constraints from
i (see
an intermediate-future galaxy survey to calculate errors on individual parameters fNL
Fig. 1) and briefly studied dependence on the smoothing scale (Fig. 2).
We further calculated the principal components of fNL (k), and thus identified the
best-measured configurations (in wavenumber) of this function (see Fig. 3). While the
sensitivity increases with increasing k, restricting the survey information to scales where
linear perturbation theory is valid imposes a “sweet spot” in sensitivity of k ∼ 0.1h Mpc−1 .
We then calculated the overlap of the best-measured principal components with two familiar classes of non-Gaussian models: local (fNL = const) and equilateral models, using
a cosine measure between the bispectra suggested in [40]. We found the expected result:
the best measured component overlaps much more with the local model (which our model
generalizes) than with the equilateral one.
One immediate utility of our results is an easy adaptation to specific models of nonGaussianity predicted by classes of inflationary models. If one wants to forecast the accuracy with which parameters of a specific model of fNL (k)-style non-Gaussianity will be
measured, neither the halo bias nor the Fisher matrix needs to be calculated from scratch.
Instead, our formalism makes it possible to obtain these forecasts by performing a simple
linear projection to our piecewise-constant model; this procedure is described in Appendix
A and illustrated with a few examples.
In future investigations, it will be interesting to consider specific inflationary models,
projecting down to specific forms for fNL (k). It will also be important to test how well the
observable effects of scale-dependent non-Gaussianity, studied here using the theoretical
ansatz from Eq. (3.2), agree with numerical simulations; the first such investigations, for
select specific forms of fNL (k), are now being done [41]. Finally, it will be interesting to see
how one can optimally select objects in the universe (i.e. their mass) to probe information
about scale-dependence of non-Gaussianity. While in Fig. 2 we showed scaling of the bestdetermined scale of fNL (k) with the smoothing mass scale applied to the density field, a
more complete analysis might use the Halo Occupation Distribution (HOD) approach to
relate the content of dark matter halos to their mass.

– 14 –

7. Acknowledgements
We thank Chris Byrnes and Sarah Shandera for useful discussions, and the anonymous
referee for constructive comments. AB and DH are supported by DOE OJI grant under contract DE-FG02-95ER40899, NSF under contract AST-0807564, and NASA under
contract NNX09AC89G. KK is supported in part by the Michigan Center for Theoretical
Physics. DH and KK would like to thank the Aspen Center for Physics where this project
germinated, and DH also acknowledges the generous hospitality of Centro de Ciencias de
Benasque “Pedro Pascual”.

A. Calculating the error on an arbitrary parametrized fNL (k)
i ≡ f
Projecting the constraints from an old set of parameters fNL
NL (ki ) (i = 1, 2, . . . , N )
to new parameters (which we can call q; j = 1, 2, . . . , M for some M ) is in principle
straightforward. The Fisher matrix in the new parameters, F new , is given by

new
Fi,j
=

N
X
∂pk ∂pl
k,l=1

∂q i ∂q j

Fkl

(A.1)

so that
F new ≡ P T F P,

(A.2)

where Pij = ∂pi /∂q j is the derivative matrix of old parameters with respect to new.
Let us look at a couple of examples. Projecting to the case
fNL (k) = fNL = const

(A.3)

i /df
new is
is particularly easy, since P is the column vector with Pi1 = dfNL
NL = 1. Then Fij
a 1 × 1 matrix that quantifies information on fNL , given by
X
new
F11
=
Fkl .
(A.4)
k,l

p new
The error on fNL is of course given simply by σ(fNL ) = 1/ F11
.
Another example is given by the function
 nNG
k
fNL (k) =
,
k0

(A.5)

with two parameters, k0 and nNG . Then one can show that (labeling k0 ≡ q1 and nNG ≡ q2 ):
 
nNG ki nNG
Pi1 = −
;
(A.6)
k0
k0
   nNG
ki
ki
Pi2 = ln
.
(A.7)
k0
k0
Then, using Eq. (A.2), one can simply obtain the 2 × 2 Fisher matrix in k0 and nNG .

– 15 –

B. Principal Components of fNL (k)
We now show how to decompose the measurement of fNL (k) in principal components,
which are essentially the eigenmodes of the covariance matrix for the aforementioned parameters fNL (ki ). This method has been widely used in cosmology, including applications
to parametrizing and describing dark energy [65, 66]. It allows us to order the best-to-worst
measured weights in wavenumber of the function fNL (k).
i ≡
Let the function fNL (k) be described in terms of piecewise constant parameters fNL
fNL (ki ), where
N
X
fNL (k) =
pi Θi (k).
(B.1)
i=1



Here, Θ(k) ≡ H(k − kilower ) − H(k − kiupper ) is the top-hat function of unit height over
the ith wavenumber bin, and we assume a total of N bins. kilower and kiupper are the
wavenumber bin boundaries, and H is the Heaviside step function. We have effectively
expanded the function around the zero value, though this is not crucial: the left-hand side
fid (k), for any fiducial f fid (k), and the formalism still follows.
could be fNL (k) − fNL
NL
The Fisher matrix F is the inverse covariance matrix in the original piecewise-constant
parameters pi , so that Fij−1 = hpi pj i − hpi ihpj i. We first diagonalize the Fisher matrix F :
F = W T DW,

(B.2)

where D is diagonal and W is some orthogonal matrix. The vector of uncorrelated parameters, q, is related to the vector of original parameters p via
q = W p,

(B.3)

and it is easy to check that the q are uncorrelated; that is, hq qT i = D−1 . The rows of W
are therefore the new parameters.
Thus, to calculate the principal components:
1. Obtain the full Fisher matrix for N parameters pi , plus the cosmological parameters
Ωb h2 , ΩCDM h2 , H0 , w, log As , and ns .
2. Marginalize over the cosmological parameters by inverting this larger Fisher matrix,
taking the N × N submatrix, then inverting back to get the Fisher matrix of the pi ;
we call this Fisher matrix F
3. Diagonalize F as in Eq. (B.2)
4. The rows of W are the principal components. More precisely, qa =
are the PCs.

P

i Wai pi , and qa

Let us now change notation slightly (to agree with the commonly used one, e.g. [65]),
(a)
and define the shape of the a-th principal component in i-th redshift bin as αi , so that

– 16 –

(a)

αi ≡ Wai . Then we can represent the a-th principal component, e(a) (k), in terms of the
original parameters pi as5
N
X (a)
e(a) (k) =
αi pi Θi (k).
(B.4)
i=1

The PCs are obviously uncorrelated, and their eigenvalues λa , so that
N
X

he(a) e(b) i ≡

(a) (b)

αi αj hpi pj i =

i,j=1

δab
.
λa

(B.5)

where, recall, λa ≡ Daa .
Finally, let us calculate the coefficients c(a) in the expansion in principal components
of an arbitrary fNL (k)
N
X
fNL (k) =
ca e(a) (k).
(B.6)
a=1
i
fNL

Let coefficients
describe fNL (k) in our original basis, so that fNL (k) = const ≡
P i
i
i fNL pi Θi (k), with fNL being left arbitrary for now. Then, taking the expectation value
of the product with e(b) , we get
+
* N
! N
X
X
cb
(a)
i
hfNL (k)e(b) i ≡
=
fNL
pi × 
αj p j 
(B.7)
λb
i=1

=

N
X

j=1

(a)

(B.8)

(a)

(B.9)

i
fNL
αj (F −1 )ij ,

i,j=1

so that
ca = λa

N
X

i
fNL
αj (F −1 )ij .

i,j=1
i
For example, in the simplest case of constant fNL (k), where fNL
= const ≡ fNL , the
coefficients of the principal components in the expansion of fNL (k) are
X (a)
ca = λa fNL
αj (F −1 )ij
(for fNL (k) ≡ fNL = const).
(B.10)
ij

C. Generalized local ansatz does not recover the equilateral case
Here, we prove that our ansatz cannot perfectly mimic the equilateral bispectrum for any
choice of fNL (k). The generalized local form of the bispectrum that we considered in this
paper is
Bgener (k1 , k2 , k3 ) = 2[fNL (k1 )P (k2 )P (k3 ) + permutations] ∝
5

This is basically the continuous version of the relation qa =

– 17 –

P

i Wai pi .

fNL (k1 )
+ perm.
k23 k33

(C.1)

The equilateral bispectrum is




2
1
1
+ perm. −
− 3 3 + perm. .
Bequi (k1 , k2 , k3 ) ∝
(k2 k1 k3 )2
k1 k22 k33
k2 k3

(C.2)

The claim is that there is no fNL (k) such that Bgener = Bequi for all k1 , k2 , k3 . To show
this, we define a new function h(k) ≡ fNL (k) + 1. If there is some fNL (k) such that
Bgener = Bequi , then we have:


1
2
h(k1 )
+ perm. ∝
+ perm. −
.
3
3
3
2
(k2 k1 k3 )2
k2 k3
k1 k2 k3
We can go from a proportionality to an equality by defining a new function g(k) that
is simply h(k) with the appropriate constant out in front. Next, multiply both sides by
k13 k23 k33 to get


k13 g(k1 ) + k23 g(k2 ) + k33 g(k3 ) = k1 k22 + k2 k32 + perm. − 2k1 k2 k3 .

(C.3)

Each term on the left-hand side is dependent on only one of k1 , k2 , or k3 . However, every
term on the right-hand side depends on at least two different k; thus, there is no g(k) that
can satisfy this relation.
Alternatively, consider the case where k1 = k2 = k3 = k. Then (C.3) becomes
3k 3 g(k) = 4k 3
which means that
g(k) = 4/3.
This answer is wholly independent of k, so this value of g(k) must be true for all k. But
this solution for g(k) is clearly incorrect in the general case where k1 6= k2 6= k3 ; therefore,
no such g(k) can exist.
While this proves that there is no fNL (k) that yields an exact equality between our
ansatz and the equilateral bispectrum, the question of an approximate equality remains.
Such solutions for fNL (k) certainly exist for narrow ranges of k. For example, fNL (k) =
δ(k−k ∗ ), where δ(k) is the Dirac delta function, yields a bispectrum that is larger for exactly
one equilateral triangle – the triangle where k1,2,3 = k∗ – than it is for any squeezed triangle.
However, no fNL (k) exists that yields a bispectrum which favors equilateral triangles over
squeezed triangles for all k. It is straightforward but tedious to prove this fact, and the
details of the proof are beyond the scope of this paper.

References
[1] J. Maldacena, Non-gaussian features of primordial fluctuations in single field inflationary
models, Journal of High Energy Physics 5 (2003) 13, [arXiv:astro-ph/0210603].
[2] V. Acquaviva, N. Bartolo, S. Matarrese, and A. Riotto, Second-order cosmological
perturbations from inflation, Nucl. Phys. B667 (2003) 119–148, [astro-ph/0209156].

– 18 –

[3] P. Creminelli, On non-gaussianities in single-field inflation, JCAP 10 (2003) 003,
[astro-ph/0306122].
[4] D. H. Lyth and Y. Rodriguez, The inflationary prediction for primordial non- gaussianity,
Phys. Rev. Lett. 95 (2005) 121302, [astro-ph/0504045].
[5] D. Seery and J. E. Lidsey, Primordial non-gaussianities in single field inflation, JCAP 06
(2005) 003, [astro-ph/0503692].
[6] X. Chen, Primordial Non-Gaussianities from Inflation Models, Adv. Astron. 2010 (2010)
638979, [arXiv:1002.1416].
[7] E. Komatsu, Hunting for Primordial Non-Gaussianity in the Cosmic Microwave Background,
Class. Quant. Grav. 27 (2010) 124010, [arXiv:1003.6097].
[8] E. Komatsu and D. N. Spergel, Acoustic signatures in the primary microwave background
bispectrum, Phys. Rev. D 63 (Mar., 2001) 063002, [arXiv:astro-ph/0005036].
[9] L. Verde, L.-M. Wang, A. Heavens, and M. Kamionkowski, Large-scale structure, the cosmic
microwave background, and primordial non-gaussianity, Mon. Not. Roy. Astron. Soc. 313
(2000) L141–L147, [astro-ph/9906301].
[10] R. Scoccimarro, E. Sefusatti, and M. Zaldarriaga, Probing primordial non-gaussianity with
large-scale structure, Phys. Rev. D 69 (2004) 103513, [astro-ph/0312286].
[11] D. Salopek and J. Bond, Nonlinear evolution of long wavelength metric fluctuations in
inflationary models, Phys.Rev. D 42 (1990) 3936–3962.
[12] T. Falk, R. Rangarajan, and M. Srednicki, The angular dependence of the three point
correlation function of the cosmic microwave background radiation as predicted by
inflationary cosmologies, Astrophys. J. 403 (1993) L1, [astro-ph/9208001].
[13] X.-c. Luo and D. N. Schramm, Testing for the gaussian nature of cosmological density
perturbations through the three-point temperature correlation function, Phys. Rev. Lett. 71
(1993) 1124–1127, [astro-ph/9305009].
[14] A. Gangui, F. Lucchin, S. Matarrese, and S. Mollerach, The three point correlation function
of the cosmic microwave background in inflationary models, Astrophys. J. 430 (1994)
447–457, [astro-ph/9312033].
[15] L.-M. Wang and M. Kamionkowski, The cosmic microwave background bispectrum and
inflation, Phys. Rev. D 61 (2000) 063504, [astro-ph/9907431].
[16] N. Bartolo, E. Komatsu, S. Matarrese, and A. Riotto, Non-gaussianity from inflation:
Theory and observations, Phys. Rept. 402 (2004) 103–266, [astro-ph/0406398].
[17] D. Seery and J. E. Lidsey, Primordial non-Gaussianities from multiple-field inflation, JCAP
0509 (2005) 011, [astro-ph/0506056].
[18] X. Chen, Running Non-Gaussianities in DBI Inflation, Phys. Rev. D 72 (2005) 123518,
[astro-ph/0507053].
[19] M. Liguori, F. K. Hansen, E. Komatsu, S. Matarrese, and A. Riotto, Testing primordial
non-Gaussianity in CMB anisotropies, Phys. Rev. D 73 (Feb., 2006) 043505,
[arXiv:astro-ph/0509098].
[20] X. Chen, R. Easther, and E. A. Lim, Large non-Gaussianities in single field inflation, JCAP
06 (2007) 023, [astro-ph/0611645].

– 19 –

[21] M. LoVerde, A. Miller, S. Shandera, and L. Verde, Effects of Scale-Dependent
Non-Gaussianity on Cosmological Structures, JCAP 04 (2008) 014, [arXiv:0711.4126].
[22] X. Chen, R. Easther, and E. A. Lim, Generation and Characterization of Large
Non-Gaussianities in Single Field Inflation, JCAP 04 (2008) 010, [arXiv:0801.3295].
[23] E. Sefusatti, M. Liguori, A. P. S. Yadav, M. G. Jackson, and E. Pajer, Constraining running
non-gaussianity, JCAP 12 (Dec., 2009) 22, [arXiv:0906.0232].
[24] J. Kumar, L. Leblond, and A. Rajaraman, Scale dependent local non-gaussianity from loops,
JCAP 04 (Apr., 2010) 24, [arXiv:0909.2040].
[25] C. T. Byrnes, S. Nurmi, G. Tasinato, and D. Wands, Scale dependence of local fN L , JCAP
02 (Feb., 2010) 34, [arXiv:0911.2780].
[26] C. T. Byrnes and K.-Y. Choi, Review of local non-Gaussianity from multi-field inflation, Adv.
Astron. 2010 (2010) 724525, [arXiv:1002.3110].
[27] D. Wands, Local non-Gaussianity from inflation, Class.Quant.Grav. 27 (2010) 124002,
[arXiv:1004.0818].
[28] A. Riotto and M. S. Sloth, Strongly Scale-dependent Non-Gaussianity, arXiv:1009.3020.
[29] Q.-G. Huang, Scale dependence of fN L in N-flation, arXiv:1009.3326.
[30] S. Mollerach, Isocurvature Baryon Perturbations and Inflation, Phys.Rev. D 42 (1990)
313–325.
[31] A. D. Linde and V. F. Mukhanov, Nongaussian isocurvature perturbations from inflation,
Phys.Rev. D 56 (1997) 535–539, [astro-ph/9610219].
[32] K. Enqvist and M. S. Sloth, Adiabatic CMB perturbations in pre - big bang string cosmology,
Nucl.Phys. B 626 (2002) 395–409, [hep-ph/0109214].
[33] D. H. Lyth and D. Wands, Generating the curvature perturbation without an inflaton, Phys.
Lett. B 524 (2002) 5–14, [hep-ph/0110002].
[34] T. Moroi and T. Takahashi, Effects of cosmological moduli fields on cosmic microwave
background, Phys.Lett. B 522 (2001) 215–221, [hep-ph/0110096].
[35] L. Kofman, Probing string theory with modulated cosmological fluctuations,
astro-ph/0303614.
[36] M. Zaldarriaga, Non-Gaussianities in models with a varying inflaton decay rate, Phys.Rev.
D69 (2004) 043508, [astro-ph/0306006].
[37] C. T. Byrnes, M. Gerstenlauer, S. Nurmi, G. Tasinato, and D. Wands, Scale-dependent
non-Gaussianity probes inflationary physics, JCAP 10 (2010) 004, [arXiv:1007.4277].
[38] C. T. Byrnes, K. Enqvist, and T. Takahashi, Scale-dependence of Non-Gaussianity in the
Curvaton Model, JCAP 09 (2010) 026, [arXiv:1007.5148].
[39] Q.-G. Huang, Negative spectral index of fN L in the axion-type curvaton model, JCAP 11
(2010) 026, [arXiv:1008.2641].
[40] D. Babich, P. Creminelli, and M. Zaldarriaga, The shape of non-gaussianities, JCAP 08
(2004) 009, [astro-ph/0405356].
[41] S. Shandera, N. Dalal, and D. Huterer, A generalized local ansatz and its effect on halo bias,
arXiv:1010.3722.

– 20 –

[42] N. Dalal, O. Dore, D. Huterer, and A. Shirokov, The imprints of primordial non-gaussianities
on large- scale structure: scale dependent bias and abundance of virialized objects, Phys. Rev.
D77 (2008) 123514, [arXiv:0710.4560].
[43] N. Afshordi and A. J. Tolley, Primordial non-gaussianity, statistics of collapsed objects, and
the Integrated Sachs-Wolfe effect, Phys. Rev. D78 (2008) 123507, [arXiv:0806.1046].
[44] S. Matarrese and L. Verde, The effect of primordial non-Gaussianity on halo bias, Astrophys.
J. 677 (2008) L77, [arXiv:0801.4826].
[45] A. Slosar, C. Hirata, U. Seljak, S. Ho, and N. Padmanabhan, Constraints on local primordial
non-Gaussianity from large scale structure, JCAP 08 (2008) 031, [arXiv:0805.3580].
[46] F. Schmidt and M. Kamionkowski, Halo Clustering with Non-Local Non-Gaussianity, Phys.
Rev. D 82 (2010) 103002, [arXiv:1008.0638].
[47] P. McDonald, Primordial non-Gaussianity: large-scale structure signature in the perturbative
bias model, Phys. Rev. D78 (2008) 123519, [arXiv:0806.1061].
[48] A. Taruya, K. Koyama, and T. Matsubara, Signature of primordial non-Gaussianity on the
matter power spectrum, Phys. Rev. D 78 (Dec., 2008) 123534, [arXiv:0808.4085].
[49] T. Giannantonio and C. Porciani, Structure formation from non-Gaussian initial conditions:
multivariate biasing, statistics, and comparison with N- body simulations, Phys. Rev. D81
(2010) 063530, [arXiv:0911.0017].
[50] M. Grossi, K. Dolag, E. Branchini, S. Matarrese, and L. Moscardini, Evolution of Massive
Haloes in non-Gaussian Scenarios, Mon. Not. Roy. Astron. Soc. 382 (July, 2007) 1261,
[arXiv:0707.2516].
[51] V. Desjacques, U. Seljak, and I. T. Iliev, Scale-dependent bias induced by local
non-Gaussianity: a comparison to N-body simulations, MNRAS 396 (June, 2009) 85–96,
[arXiv:0811.2748].
[52] A. Pillepich, C. Porciani, and O. Hahn, Halo mass function and scale-dependent bias from
N-body simulations with non-Gaussian initial conditions, MNRAS 402 (Feb., 2010) 191–206,
[arXiv:0811.4176].
[53] C. Carbone, L. Verde, and S. Matarrese, Non-Gaussian halo bias and future galaxy surveys,
Astrophys. J. 684 (2008) L1–L4, [arXiv:0806.1950].
[54] B. Sartoris et al., The potential of X-ray cluster surveys to constrain primordial
non-Gaussianity, arXiv:1003.0841.
[55] C. Cunha, D. Huterer, and O. Doré, Primordial non-gaussianity from the covariance of
galaxy cluster counts, Phys. Rev. D 82 (Jul, 2010) 023004, [arXiv:1003.2416].
[56] V. Desjacques and U. Seljak, Signature of primordial non-Gaussianity of φ3 -type in the mass
function and bias of dark matter haloes, Phys. Rev. D81 (2010) 023006, [arXiv:0907.2257].
[57] L. Verde and S. Matarrese, Detectability of the effect of Inflationary non- Gaussianity on
halo bias, Astrophys. J. 706 (2009) L91–L95, [arXiv:0909.3224].
[58] B. Grinstein and M. B. Wise, Nongaussian Fluctuations and the Correlations of Galaxies or
Rich Clusters of Galaxies, Astrophys. J. 310 (1986) 19–22.
[59] S. Matarrese, F. Lucchin, and S. A. Bonometto, A path-integral approach to large-scale
matter distribution originated by non-Gaussian fluctuations, Astrophys. J. 310 (Nov., 1986)
L21–L26.

– 21 –

[60] H. A. Feldman, N. Kaiser, and J. A. Peacock, Power spectrum analysis of three-dimensional
redshift surveys, Astrophys. J. 426 (1994) 23–37, [astro-ph/9304022].
[61] M. Tegmark, Measuring cosmological parameters with galaxy surveys, Phys. Rev. Lett. 79
(1997), no. 20 3806–3809, [astro-ph/9706198].
[62] H. Seo and D. J. Eisenstein, Probing Dark Energy with Baryonic Acoustic Oscillations from
Future Large Galaxy Redshift Surveys, Astrophys. J. 598 (Dec., 2003) 720–740,
[arXiv:astro-ph/0307460].
[63] E. Komatsu et al., Seven-Year Wilkinson Microwave Anisotropy Probe (WMAP)
Observations: Cosmological Interpretation, arXiv:1001.4538.
[64] K. Abazajian, K. Kadota, and E. D. Stewart, Parameterizing the power spectrum: Beyond
the truncated Taylor expansion, JCAP 0508 (2005) 008, [astro-ph/0507224].
[65] D. Huterer and G. Starkman, Parameterization of dark-energy properties: A principalcomponent approach, Phys. Rev. Lett. 90 (2003) 031301, [astro-ph/0207517].
[66] A. J. Albrecht et al., Findings of the Joint Dark Energy Mission Figure of Merit Science
Working Group, arXiv:0901.0721.

– 22 –
