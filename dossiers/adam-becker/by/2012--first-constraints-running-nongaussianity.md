---
title: "First Constraints on the Running of Non-Gaussianity"
person: adam-becker
section: by
type: journal-article
year: 2012
date: 2012-09-18
venue: "Physical Review Letters"
authors: "Adam Becker, Dragan Huterer"
source_url: https://doi.org/10.1103/physrevlett.109.121302
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W2029741149; full text from arXiv preprint https://arxiv.org/abs/1207.5788 (pdftotext); may differ from published version. oa_status=green; cited_by=37."
---

# First Constraints on the Running of Non-Gaussianity

## Full text

### Abstract (from OpenAlex metadata)

We use data from the Wilkinson Microwave Anisotropy probe temperature maps to constrain a scale-dependent generalization of the popular "local" model for primordial non-Gaussianity. In the model where the parameter f(NL) is allowed to run with scale k, f(NL)(k) = f*(NL) (k/k(piv))(n)(fNL), we constrain the running to be n(f)(NL) = 0.30(-1.2)(+1.9) at 95% confidence, marginalized over the amplitude f*(NL). The constraints depend somewhat on the prior probabilities assigned to the two parameters. In the near future, constraints from a combination of Planck and large-scale structure surveys are expected to improve this limit by about an order of magnitude and usefully constrain classes of inflationary models.

### Full text (arXiv preprint version, pdftotext extraction)

First constraints on the running of non-Gaussianity
Adam Becker∗ and Dragan Huterer†
Department of Physics, University of Michigan, 450 Church St, Ann Arbor, MI 48109-1040
(Dated: November 27, 2024)

arXiv:1207.5788v1 [astro-ph.CO] 24 Jul 2012

We use data from the WMAP temperature maps to constrain a scale-dependent generalization
of the popular ‘local’ model for primordial non-Gaussianity. In the model where the parameter
∗
fNL is allowed to run with scale k, fNL (k) = fNL
(k/kpiv )nfNL , we constrain the running to be
∗
nfNL = 0.30+1.9
at
95%
confidence,
marginalized
over
the amplitude fNL
. The constraints depend
−1.2
somewhat on the prior probabilities assigned to the two parameters. In the near future, constraints
from a combination of Planck and large-scale structure surveys are expected to improve this limit
by about an order of magnitude and usefully constrain classes of inflationary models.

Introduction. Non-Gaussianity in the distribution of
primordial density fluctuations provides a unique window
into the physics of inflation. The magnitude of primordial
non-Gaussianity and its dependence on scale provide information about the dynamics of scalar field(s), their interactions, and the speed of sound during inflation. Constraints on non-Gaussianity have traditionally come from
the measurements of the three-point correlation function
of the cosmic microwave background (CMB) temperature
anisotropies. Upper limits from COBE [1] have been improved by two orders of magnitude by the WMAP experiment [2]. Moreover, clustering of galaxies and galaxy
clusters has also been identified as a powerful probe of
non-Gaussianity [3], already leading to interesting constraints that are complementary in their information content to the CMB measurements.
So far most attention has been devoted to the “local” model of primordial non-Gaussianity, where the primordial Newtonian potential φ(x) is modified with a
quadratic term: φ = φG + fNL (φ2G − hφ2G i), where φG is
a Gaussian potential [4]. The parameter fNL is currently
constrained to be 32 ± 21 by WMAP ([2]; see also [5, 6])
and 28 ± 23 by the large-scale structure [7–9]. Several
other non-Gaussian models have been constrained as well
(e.g. [10, 11]). However, the ‘running’ with physical scale
of these models, which may carry important information
about the number of inflationary fields and their interactions [12–22], has not yet been constrained with current
data (except for a very rough estimate of the angularmultipole dependence of fNL [11] and implicit constraints
on a braneworld-motivated model [23]). Such constraints
have only been forecasted for future experiments [24–28].
Constraining the running of non-Gaussianity therefore
presents a major new opportunity to probe inflationary
physics, and is just becoming feasible. In this Letter, we
present the first such constraints.
Model. In this work we consider a physically motivated
generalization of the local model, where the parameter
fNL is promoted to a function of scale k. In particular, we
seek to constrain the two-parameter power-law subclass

∗ beckeram@umich.edu
† huterer@umich.edu

of the generalized models [25]
∗
fNL (k) = fNL



k
k∗

nfNL
,

(1)

∗
where k∗ is an arbitrary fixed parameter, leaving fNL
and nfNL as the parameters of interest in this model.
Such scaling is expected in inflation when more than one
field dominates or when there is self-interaction, and its
signatures in the CMB and LSS have been discussed in
the literature [24, 25, 29]. The parameter nfNL is often,
though certainly not always, expected to be . O(1) in
inflationary models, but in our phenomenological model
it is allowed to take any value.
∗
Bispectrum and fNL
estimator. The primordial bispectrum of the fNL (k) model from Eq. (1) is straightforward
to calculate:

F (~k1 , ~k2 , ~k3 ) = 2 [fNL (k1 )P (k2 )P (k3 ) + perm.] ,

(2)

where the full bispectrum is B(~k1 , ~k2 , ~k3 ) ≡ (2π)3 δ(~k1 +
~k2 +~k3 )F (~k1 , ~k2 , ~k3 ). Here P is the power spectrum of the
primordial curvature perturbations, and δ is the Dirac
delta function.
Constraining the running parameter nfNL seems difficult because of the apparent requirement to find an estimator for a parameter in an exponent. To avoid this, we
resort to an indirect approach where, for a fixed value of
∗
nfNL , we estimate the parameter fNL
using modifications
of the well-known KSW estimator [30], which is known
to be nearly optimal [31, 32]. We then iterate over the
values of the running nfNL to obtain the full likelihood
∗
L(fNL
, nfNL ).
The theoretical expectation for the bispectrum of the
temperature anisotropies in the cosmic microwave background can be explicitly evaluated, starting from the definition of the generalized non-Gaussian local model in
Eq. (1) to account for the running nfNL :
∗
∗
B`theory
(fNL
, nfNL ) = 2fNL
I`1 `2 `3 ×
1 `2 `3
Z ∞
r2 dr (α`1 (nfNL , r)β`2 (r)β`3 (r) + perm.) (3)
0

2
where I`1 `2 `3 is the Gaunt integral and
Z
2 1
α` (r) ≡
k 2+nfNL t` (k)j` (kr)dk
nfNL
π kpiv
Z
2
k 2 PΦ (k)t` (k)j` (kr)dk.
β` (r) ≡
π

(4)

(5)

Here, t` is the radiation transfer function, which can be
calculated using CAMB [33]. Following KSW [30] we can
define new, filtered maps A(n̂, r) and B(n̂, r),
X
b`
A(n̂, r) ≡
α` (nfNL , r) a`m Y`m (n̂),
(6)
C̃`
`,m
B(n̂, r) ≡

X
`,m

β` (r)

b`
a`m Y`m (n̂).
C̃`

(7)

Then, we write down the skewness S(nfNL ):
Z
Z
S(nfNL ) ≡ r2 dr d2 n̂ A(n̂, r)B 2 (n̂, r),

(8)

which requires nfNL as input (through A), and does not
∗
.
require a priori knowledge of fNL
The observed CMB bispectrum is defined as B`obs.
=
1 `2 `3
ha`1 m1 a`2 m2 a`3 m3 i, and S(nfNL ) therefore reduces to
S=

X

B`obs
B̃`theory
(fNL = 1)
1 `2 `3
1 `2 `3

`1 ≤`2 ≤`3

C̃`1 C̃`2 C̃`3

,

(9)

where B̃`theory
= b`1 b`2 b`3 B`theory
, and b` is the beam
1 `2 `3
1 `2 `3
transfer function.
We now define F ≡ F (nfNL ), the Fisher matrix for
∗
fNL
, equivalent to the cumulative signal-to-noise squared
∗
of the theoretical bispectrum for fNL
=1

2
∗
B̃`theory
(fNL
= 1)
X
1 `2 `3
F (nfNL ) =
.
(10)
C̃`1 C̃`2 C̃`3
`1 ≤`2 ≤`3
∗
The theoretical expectation for B`1 `2 `3 ∝ fNL
, so the
∗
cubic KSW estimator for fNL
is:

S
∗
fˆNL
= .
F

(11)

We used HEALPix, by way of HealPy, to do the forwards and backwards spherical harmonic transforms required to obtain the A and B maps.
Cut-sky maps. Equation (11) works well for a full-sky
map, but a sky cut introduces a spurious non-Gaussian
signal. To account for the masking of the CMB sky, we
make the substitution S → Scut = S/fsky + Slinear [34].
Slinear is an addition to skewness from Eq. (8), calibrated
to account for partial-sky observations:
Z
Z

1
2
2
Slinear = −
r dr d2 n̂ A(n̂, r)hBsim
(n̂, r)iM C
fsky
+2B(n̂, r)hAsim (n̂, r)Bsim (n̂, r)iM C ] .
(12)

The subscripted filtered maps Asim and Bsim are created
from Python-produced Monte Carlo realizations of the
cut CMB sky; the brackets hiM C indicate an average over
all 300 Monte-Python maps. The simulated maps were
produced using the prescription laid out in Appendix
A of the WMAP5 paper [35]; the only difference (aside
from using the WMAP7 cosmological model) is that we
used a uniform weighting for the maps, rather than the
slightly more complicated weighting given there, since it
only gives a marginal improvement in estimating fNL .
Likelihood Evaluation. To find the likelihood, we first
∗
find a χ2 statistic for fNL
, given a value of nfNL . Taking
the angular-averaged bispectrum B`1 `2 `3 as our observables, we have:
∗
χ2 (fNL
, nfNL ) =

2
theory
∗
∗
−
f
B̃
(n
,
f
=
1)
X B`obs
fNL NL
NL `1 `2 `3
1 `2 `3
`1 `2 `3

C̃`1 C̃`2 C̃`3

(13)

(Again, this works because the theoretical expectation for
∗
B`1 `2 `3 ∝ fNL
.) Using Eqs. (9) and (10), we can rewrite
2
χ as
2

S2
S
∗
∗
+ χ20 −
.
(14)
χ2 (fNL
, nfNL ) = F fNL
−
F
F
2
P
obs
where χ20 ≡
/(C̃`1 C̃`2 C̃`3 ) is the
`1 `2 `3 B`1 `2 `3
goodness-of-fit parameter for the data with respect to
∗
the fNL
= 0 case. Note that the numerator of χ20 is an
observed quantity, and the denominator is based solely
on the theoretical prediction for the power spectrum (as
well as a few noise and beam parameters of WMAP).
∗
or nfNL at all. We
Therefore, χ20 does not depend on fNL
∗
ˆ
can use the definition of fNL in Eq. (11) to rewrite the
expression for χ2 as follows

2
∗
∗
∗
∗ 2
χ2 (fNL
, nfNL ) = F fNL
− fˆNL
+ χ20 − (fˆNL
) F. (15)
For a fixed value of nfNL , the χ2 is, as expected,
∗
∗
∗
minimized in fNL
when fNL
= fˆNL
, and one obtains
2
2
∗ 2
ˆ
χmin (nfNL ) = χ0 − (fNL ) F .
A more interesting task is to calculate the constraints
when nfNL is allowed to vary. With an expression for
∗
χ2 (fNL
, nfNL ) in hand, we can write an expression for
∗
the likelihood, L(fNL
, nfNL ) ∝ exp(−χ2 /2) (dropping the
constant term with χ20 )


2 
#
"
∗
ˆ∗
F
f
−
f
∗ 2
NL
NL
(fˆNL
) F


∗
L(nfNL , fNL ) ∝ exp −
 exp
2
2
(16)
∗
To marginalize over fNL
is also straightforward
"
#
Z
ˆ∗ )2 F
1
(
f
∗
∗
NL
L(nfNL ) = L(nfNL , fNL
) dfNL
∝ √ exp
,
2
F
(17)

3

150

1200

Best fit fNL∗

Flat prior in fNL∗
Flat prior in log(fNL∗ )

1000

800

99%

fNL∗

%

95

68%

L(nfNL)

100
50

600

400

0

200

3

2

1

0 n 1
fNL

2

3

4

5

0

3

2

1

0 n 1
fNL

2

3

4

5

∗
∗
FIG. 1. Likelihood in the nfNL –fNL
plane (left panel) and marginalized over fNL
(right panel). The principal constraints,
∗
shown in the left panel and with the bold blue curve on the right, correspond to the flat prior on fNL
at the pivot value where
∗
the constraints on fNL and nfNL are uncorrelated (see Eq. (19)). In the right panel we also show the marginalized likelihood
∗
∗
∗
for nfNL with a prior on fNL
that is uniform in log(fNL
) for |fNL
| > 0.1 and zero otherwise. The dashed curve in the left panel
∗
∗
shows the quantity fˆNL , which is the best-fit value of the parameter fNL
for a fixed nfNL . See text for other details.

where, recall, F (nfNL ) is defined in Eq. (10).
WMAP7 constraints on nfNL . Figure 1 shows the like∗
plane, as well as the likelihood
lihood L in the nfNL – fNL
for nfNL alone, calculated from the WMAP7 temperature
maps. We used a weighted and masked combination of
the WMAP V and W band maps with the monopole and
dipole subtracted, as recommended by the WMAP team
[35]. To extract full information from WMAP maps,
we used multipoles out to `max = 800 for the sums in
Eqs. (6), (7) and (10). We did not find a significant improvement between `max = 700 and `max = 800; we chose
the higher value to be conservative in our analysis.
The quantity χ2 is independent of our choice for kpiv ,
but the likelihood itself is not, since F is inversely pro2nf
portional to kpiv NL . The true pivot scale favored by the
∗
are
data is the value of kpiv for which the errors in fNL
uncorrelated with the errors in nfNL . We find this scale
by using the likelihood to calculate the covariance matrix
∗
C between fNL
and nfNL
Cpi ,pj = h(pi − p¯i )(pj − p¯j )i.

(18)

We can easily find the pivot value kpiv that diagonalizes
the covariance matrix C (see e.g. Ref. [26])
Cf ∗ ,nf
kpiv = k∗ exp − ∗ NL NL
fNL CnfNL ,nfNL

!
.

(19)

∗
where k∗ is the (arbitrary) pivot used initially, and fNL
is the corresponding value used in C. Despite the fact
∗
that k∗ and fNL
show up in the expression, kpiv does
not depend on them: it is a fixed number telling us
roughly where the experiment has greatest power (and
where normalization and running of fNL (k) are precisely
WMAP7
uncorrelated). We find that kpiv
≈ 0.064 h Mpc−1 .
∗
The 68%, 95%, and 99% constraints on fNL
and nfNL are

shown at the left panel of Figure 1, assuming flat priors
∗
WMAP7
on fNL
and nfNL and k∗ = kpiv
≈ 0.064 h Mpc−1 .
Dependence on the prior. As with most present-day
cosmological measurements, the precise constraints depend on the prior probability on the parameters we are
∗
and
constraining. Even for a simple flat prior on fNL
nfNL , the actual effective prior depends on the a priori
chosen pivot in wavenumber k∗ . For example, a flat prior
∗ (1)
) ≡ fNL (k∗,1 ) defined at some pivot k∗,1 correon (fNL
∗
∗ (2)
(k∗,2 )
) ≡ fNL
sponds to a non-flat prior on some (fNL
∗ (2)
defined at some other pivot k∗,2 , since (fNL )
≡
∗ (1)
) (k∗,2 /k∗,1 )nfNL . If we assume some alternate
(fNL
∗
, the contours
pivot k∗,2 but hold the flat prior in fNL
∗
in the nfNL –fNL plane (left panel of Fig. 1) are stretched
vertically by a factor of (k∗,2 /0.064 h Mpc−1 )nfNL .
We have experimented with different k-pivot values for
∗
and nfNL . We have also investigated
a flat prior on fNL
other possibilities, such as the prior that assigns equal
∗
| above 0.1 (so uniform in
weight to each decade in |fNL
∗
log(fNL ), but cut off at the arguably lowest-ever observ∗
able value of |fNL
| = 0.1 so that the total integrated
likelihood is finite). We present the two aforementioned
examples, showing constraints on nfNL marginalized over
∗
fNL
, in the right panel of Fig. 1. In the end, we decide to
quote results for the flat prior and the uncorrelated kpiv
value from Eq. (19), which most closely follows priors to
both non-Gaussian and other cosmological parameters
applied in the literature.
Putting it all together, we can get the estimate for
∗
nfNL from the WMAP7 data for a flat prior on fNL
at
the pivot kpiv from Eq. (19). The 68% (95%) confidence
interval is
+0.78 (1.9)

nfNL = 0.30−0.61 (1.2) .

(20)

The current constraints are therefore fully consistent
with no running, as Fig. 1 clearly indicates. Figure 2

4

200

fNL(k)

150
100
50

99%

shows the constraints in the fNL (k) plane together with
a few representative models allowed by the data.

68%

95%

0
50
100

10-2

10-1

k (h/Mpc)

100

Conclusions. We have presented the first constraints
on the scale-dependence of (any form of) non-Gaussianity
using the WMAP7 data. The constraints are compatible
with zero running, nfNL = 0, with very mild (< 1-sigma)
preference for a positive value of nfNL . We will learn
more soon: the Planck data and the data from upcoming
large-scale structure surveys should be able to improve
constraints on the running of non-Gaussianity by about
an order of magnitude [24, 27, 28], thus shedding important new light on the physics of inflation.

FIG. 2. Constraints propagated to fNL (k). We also show
several models that are reasonable fits to the data (all within
the 99% confidence limit of the left panel of Fig. 1) to guide
the eye as to how typical models from our ansatz behave.

Acknowledgements. We thank Kendrick Smith for
initial encouragement, and Eiichiro Komatsu for useful
communications. We acknowledge the use of the publicly available CAMB [33] and HEALPix [36] packages.
We have been supported by DOE OJI grant under contract DE-FG02-95ER40899, NSF under contract AST0807564, and NASA under contract NNX09AC89G.

[1] E. Komatsu, B. D. Wandelt, D. N. Spergel, A. J. Banday,
and K. M. Gorski, Astrophys.J. 566, 19 (2002).
[2] E. Komatsu et al. (WMAP Collaboration), Astrophys.J.Suppl. 192, 18 (2011).
[3] N. Dalal, O. Doré, D. Huterer, and A. Shirokov, Phys.
Rev. D77, 123514 (2008).
[4] E. Komatsu and D. N. Spergel, Phys. Rev. D 63, 063002
(2001).
[5] A. P. Yadav and B. D. Wandelt, Phys.Rev.Lett. 100,
181301 (2008).
[6] K. M. Smith, L. Senatore, and M. Zaldarriaga, JCAP
0909, 006 (2009).
[7] A. Slosar, C. Hirata, U. Seljak, S. Ho, and N. Padmanabhan, JCAP 08, 031 (2008).
[8] N. Afshordi and A. J. Tolley, Phys. Rev. D78, 123507
(2008).
[9] J.-Q. Xia, C. Baccigalupi, S. Matarrese, L. Verde, and
M. Viel, JCAP 1108, 033 (2011).
[10] J. R. Fergusson, M. Liguori, and E. P. S. Shellard, Phys.
Rev. D 82, 023502 (2010).
[11] J. Smidt, A. Amblard, C. T. Byrnes, A. Cooray, A. Heavens, et al., Phys.Rev. D81, 123007 (2010).
[12] X. Chen, Phys. Rev. D 72, 123518 (2005).
[13] M. Liguori, F. K. Hansen, E. Komatsu, S. Matarrese,
and A. Riotto, Phys. Rev. D 73, 043505 (2006).
[14] J. Khoury and F. Piazza, JCAP 0907, 026 (2009).
[15] J. Kumar, L. Leblond, and A. Rajaraman, JCAP 04, 24
(2010).
[16] C. T. Byrnes and K.-Y. Choi, Adv. Astron. 2010, 724525
(2010).
[17] D. Wands, Class.Quant.Grav. 27, 124002 (2010).
[18] C. T. Byrnes, S. Nurmi, G. Tasinato, and D. Wands,
JCAP 02, 34 (2010).

[19] C. T. Byrnes, M. Gerstenlauer, S. Nurmi, G. Tasinato,
and D. Wands, JCAP 10, 004 (2010).
[20] A. Riotto and M. S. Sloth, Phys.Rev. D83, 041301
(2011).
[21] N. Barnaby, R. Namba, and M. Peloso, arXiv:1202.1469.
[22] T. Kobayashi and T. Takahashi, JCAP 1206, 004 (2012).
[23] R. Bean, X. Chen, H. Peiris, and J. Xu, Phys.Rev. D77,
023527 (2008).
[24] E. Sefusatti, M. Liguori, A. P. S. Yadav, M. G. Jackson,
and E. Pajer, JCAP 12, 22 (2009).
[25] A. Becker, D. Huterer, and K. Kadota, JCAP 1, 6
(2011).
[26] S. Shandera, N. Dalal, and D. Huterer, JCAP 1103, 017
(2011).
[27] T. Giannantonio, C. Porciani, J. Carron, A. Amara, and
A. Pillepich, Mon. Not. R. Astron. Soc. , 2888 (2012).
[28] A. Becker, D. Huterer, and K. Kadota, arXiv:1206.6165.
[29] M. LoVerde, A. Miller, S. Shandera, and L. Verde, JCAP
04, 014 (2008).
[30] E. Komatsu, D. N. Spergel, and B. D. Wandelt, Astrophys.J. 634, 14 (2005).
[31] K. M. Smith and M. Zaldarriaga, Mon. Not. Roy. Astron.
Soc. 417, 2 (2011).
[32] P. Creminelli, L. Senatore, and M. Zaldarriaga, JCAP
0703, 019 (2007).
[33] A. Lewis, A. Challinor, and A. Lasenby, Astrophys.J.
538, 473 (2000).
[34] A. P. S. Yadav, E. Komatsu, B. D. Wandelt, M. Liguori,
F. K. Hansen, and S. Matarrese, Astrophys. J. 678, 578
(2008).
[35] E. Komatsu et al. (WMAP), Astrophys. J. Suppl. 180,
330 (2009).
[36] K. Gorski, E. Hivon, A. Banday, B. Wandelt, F. Hansen,
et al., Astrophys.J. 622, 759 (2005).
