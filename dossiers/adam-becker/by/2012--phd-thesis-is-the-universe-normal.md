---
title: "Is the Universe Normal? Constraining Scale-Dependent Primordial Non-Gaussianity."
person: adam-becker
section: by
type: dissertation
year: 2012
date: 2012-01-01
venue: "University of Michigan (PhD dissertation, Physics)"
authors: "Adam M. Becker"
source_url: https://hdl.handle.net/2027.42/93893
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W601992439. PDF retrieved via the OpenAlex Content API (content.openalex.org/works/W601992439.pdf) because the Deep Blue landing page is behind a Cloudflare challenge; text extracted with pdftotext. Doctoral committee chaired by Dragan Huterer."
---

# Is the Universe Normal? Constraining Scale-Dependent Primordial Non-Gaussianity.

## Full text

### Abstract (from OpenAlex metadata)

Non-Gaussianity is a potentially powerful probe of inflationary physics in the very early universe. The detection of significant primordial non-Gaussianity would be a serious challenge to the simplest models of inflation. Models with non-Gaussianity that varies with spatial scale are of particular interest; this is generically predicted by single-field inflationary models with interactions and most multi-field models. In this dissertation, I focus on a scale-dependent generalization of the local model of non- Gaussianity, in which the parameter quantifying departures from Gaussianity, fNL, is promoted to a function of scale, fNL(k). I forecast constraints on fNL(k) expected from upcoming large-scale structure and cosmic microwave background data. Finally, I use the WMAP7 data to obtain the first constraints on the scale-dependence of non-Gaussianity.

### Full text (pdftotext extraction)

Is the Universe Normal?
Constraining Scale-Dependent Primordial
Non-Gaussianity

by
Adam M. Becker

A dissertation submitted in partial fulfillment
of the requirements for the degree of
Doctor of Philosophy
(Physics)
in the University of Michigan
2012

Doctoral Committee:
Assistant Professor Dragan Huterer, Chair
Professor August Evrard
Professor Timothy A. McKay
Assistant Professor Christopher John Miller
Assistant Professor Kathryn Zurek

The fact that we live at the bottom of a deep gravity well, on the surface of a gas covered planet
going around a nuclear fireball 90 million miles away, and think this to be normal is obviously
some indication of how skewed our perspective tends to be – but we have done various things over
intellectual history to slowly correct some of our misapprehensions.
– Douglas Adams

To be able to see Nobody! And at that distance, too! Why, it’s as much as I can do to see real
people, by this light!
– Through The Looking-Glass

c

Adam M. Becker
2012
All Rights Reserved

ACKNOWLEDGEMENTS

Technical acknowledgements. Nearly all of the computational work for
this dissertation was done using the Python programming language, along with the
NumPy and SciPy quantitative and scientific computing packages. All of the figures,
with the exception of Figs. 1.3 and 1.4, were created using the matplotlib package
for Python. The work that I did not do in Python mostly involved CAMB (Code
for Anisotropies in the Microwave Background), maintainted by Antony Lewis, and
HEALPix, maintained by NASA/JPL. I also made use of the GNU Scientific Library
(GSL) in some of this work. I was supported by a grant from the NSF in the course
of this work.
Personal acknowledgements. There are many people who have helped me
through the process of researching and writing this dissertation, and in graduate
school more generally. A few require special thanks:
• Dragan Huterer, for the major role he played in this research, in addition to
being the best advisor I could possibly have hoped for.
• Kenji Kadota, for the work he did on much of this research – Chapter II, in
particular, would have been impossible without him.
• Chris Byrnes, Sarah Shandera, and Amit Yadav for many helpful discussions
and e-mail exchanges.

ii

• Gus Evrard, Tim McKay, Chris Miller, and Kathryn Zurek, for agreeing to serve
on my thesis committee.
• Bob Ziff, for being understanding about my choices in research.
• Cameron Gibelyou, for helping me and being generally awesome throughout.
• Daniel Jordan, for showing me that there should be one – and preferably only
one – obvious way to do it.
• Marshall Weir and his family, for tea, Thanksgiving, and all the rest.
• Stefan Richter, for getting me through rough spots, and also to the gym.
• Kate Hanley and the Clarks, for their hospitality and friendship.
• Andrew McNair, for never letting me down.
• Adrienne Grant, for following me around the country and letting me steal her
friends.
• Andrew Schwarzkopf, for asking the right questions and having faith in my
insanity.
• My friends at the Telluride House, for giving me a home and an extended family.
• My parents, for being supportive and patient, and for answering far more questions than they ever expected to be asked.
• And Elisabeth, who knows why.

iii

TABLE OF CONTENTS

ACKNOWLEDGEMENTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

ii

LIST OF FIGURES

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

vi

LIST OF TABLES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

vii

LIST OF APPENDICES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

viii

CHAPTER
I. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1
1.2

1

Constraining models of inflationary-era physics . . . . . . . . . . . . . . . . .
Non-Gaussianity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.1 Modeling non-Gaussianity . . . . . . . . . . . . . . . . . . . . . . .
1.2.2 Detecting non-Gaussianity . . . . . . . . . . . . . . . . . . . . . . .
Beyond the local model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3.1 Scale-dependent non-Gaussianity . . . . . . . . . . . . . . . . . . .

1
3
3
5
6
7

II. Forecasted constraints on scale-dependent non-Gaussianity from LSS . . .

13

1.3

2.1

2.2

2.3

2.4

Non-Gaussianity and bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.1 The effect of a non-vanishing bispectrum on bias . . . . . . . . . .
2.1.2 Beyond the high-peak approximation . . . . . . . . . . . . . . . . .
Forecasted constraints on scale-dependent non-Gaussianity from large-scale
structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1 Fisher matrix analysis . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.2 Survey properties . . . . . . . . . . . . . . . . . . . . . . . . . . . .
i
2.2.3 Forecasted constraints on the fNL
. . . . . . . . . . . . . . . . . . .
Projection and principal components . . . . . . . . . . . . . . . . . . . . . .
2.3.1 Constraining other fNL (k) models . . . . . . . . . . . . . . . . . . .
2.3.2 Principal components . . . . . . . . . . . . . . . . . . . . . . . . . .
Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

13
13
16
17
17
18
19
20
20
22
24

III. Forecasted constraints on scale-dependent non-Gaussianity from the CMB 25
3.1
3.2

3.3

Signatures of the generalized local model in the CMB . . . . . . . . . . . . .
Results and joint constraints . . . . . . . . . . . . . . . . . . . . . . . . . . .
i
3.2.1 Forecasted constraints on the fNL
. . . . . . . . . . . . . . . . . . .
3.2.2 Principal component analysis . . . . . . . . . . . . . . . . . . . . .
3.2.3 Projecting constraints on the power-law model of fNL (k) . . . . . .
Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

iv

25
28
28
29
30
33

IV. Constraints on the running of local-type non-Gaussianity from WMAP
7-year data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1
4.2
4.3

36

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Estimating nfNL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Results and conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.1 WMAP7 constraints on nfNL . . . . . . . . . . . . . . . . . . . . .
4.3.2 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

36
36
40
40
42

V. Summary and conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

44

APPENDICES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

47

BIBLIOGRAPHY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

76

v

LIST OF FIGURES

Figure
1.1

Comparison of Gaussian and non-Gaussian distributions . . . . . . . . . . . . . . .

4

1.2

Further comparison of Gaussian and local non-Gaussian distributions . . . . . . . .

10

1.3

Effects of local non-Gaussianity on N-body simulations of large-scale structure . . .

11

1.4

Effects of local non-Gaussianity on Monte Carlo simulations of the CMB sky . . .

12

2.1

The peak-background split . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

14

2.2

i
from LSS . . . . . . .
Forecasted constraints on piecewise-constant parameters fNL

21

2.3

The forecasted best-measured principal components from LSS . . . . . . . . . . . .

23

2.4

Forecasted RMS error on each principal component from LSS.

. . . . . . . . . . .

24

3.1

i
from LSS, Planck, and combined data sets . . .
Forecasted constraints on the fNL

26

3.2

The forecasted best-measured PCs from LSS and Planck . . . . . . . . . . . . . . .

29

3.3

The forecasted best-measured PCs of fNL (k) from the joint data set. . . . . . . . .

30

3.4

Forecasted RMS error on each principal component for LSS, Planck, and combined
data sets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

31

3.5

Forecasted constraints on the power-law model of fNL (k) . . . . . . . . . . . . . . .

32

3.6

The same as Figure 3.5, but with different LSS survey parameters

. . . . . . . . .

33

3.7

The same as Figure 3.5, but with a fiducial fNL (k) = 0. . . . . . . . . . . . . . . .

34

4.1

χ2min − χ20 as a function of nfNL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

39

4.2

∗
A contour plot of the likelihood in the fNL
- nfNL plane. . . . . . . . . . . . . . . .

39

4.3

∗
A three-dimensional plot of the likelihood, L(fNL
, nfNL ). . . . . . . . . . . . . . . .

40

4.4

∗
The likelihood marginalized over fNL
as a function of nfNL , for several pivots. . . .

41

4.5

Several models of fNL (k) with high likelihood . . . . . . . . . . . . . . . . . . . . .

42

A.1

How the fiducial fNL affects forecasted constraints from a future galaxy survey. . .

52

vi

LIST OF TABLES

Table
3.1

∗
Forecasted constraints on fNL
and nfNL from LSS, CMB, and combined data sets .

31

3.2

∗
Forecasted constraints on fNL
from different LSS surveys, assuming different fiducial models, along with forecasted constraints from Planck for comparison. . . . . .

35

vii

LIST OF APPENDICES

Appendix
A.

B.

C.

D.

i
Finding the derivative of the halo bias with respect to fNL and the fNL
. . . . . . . .

48

A.1 Constant fNL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.2 Scale-dependent fNL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A.2.1 The Desjacques et al. term . . . . . . . . . . . . . . . . . . . . . .
A.3 The effect of the fiducial value on constraints . . . . . . . . . . . . . . . . . .

49
50
51
52

Statistical methods: Fisher matrices, principal components, and all that. . . . . . . .

54

B.1 Fisher information matrices: a brief introduction. . . . . . . . . . . . . . . .
B.1.1 Bayes’s theorem, likelihood, and the Fisher information matrix . .
B.1.2 Using Fisher matrices to estimate parameter errors . . . . . . . . .
B.2 Calculating the error on an arbitrary parametrized fNL (k) . . . . . . . . . .
B.3 Principal components of fNL (k) . . . . . . . . . . . . . . . . . . . . . . . . .

54
54
57
57
59

Calculating the CMB bispectrum Fisher matrix for local-type non-Gaussianity . . . .

62

C.1 Calculating the CMB bispectrum . . . . . . . . . . . . . . . . . . . . . . . .
C.1.1 Bispectrum and derivatives for fNL and fNL (k) . . . . . . . . . . .
C.2 The covariance of the bispectrum . . . . . . . . . . . . . . . . . . . . . . . .
C.3 Computational details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
C.3.1 ` sampling and binning . . . . . . . . . . . . . . . . . . . . . . . . .
C.3.2 Calculating the Wigner 3j-symbol . . . . . . . . . . . . . . . . . .

62
65
66
68
68
68

The KSW estimator and the modified KSW estimator . . . . . . . . . . . . . . . . .

70

D.1 The KSW estimator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
D.2 Modifying the KSW estimator for a power-law fNL (k) . . . . . . . . . . . . .

70
73

viii

CHAPTER I

Introduction

1.1

Constraining models of inflationary-era physics

The Friedmann-Robertson-Walker metric commonly used to describe our universe
is based on the assumption that the universe looks the same everywhere, in all
directions. While this is nearly true on large scales, it is manifestly untrue on small
scales, as demonstrated by our existence, and more broadly the existence of galaxies
and galaxy clusters. The evolution of these structures is reasonably well understood;
the cosmic microwave background (CMB) gives us evidence for density perturbations
on the order of one part in 105 at the time of recombination, and their evolution to
the large density perturbations that we see today is described well by gravitational
collapse. But the origin of those perturbations is far less well understood. Our best
guess comes from inflation. Inflation posits that the primordial density perturbations
have their origin in quantum fluctuations of the inflaton field that were “blown up”
to macroscopic scale during the inflationary era in the first ∼ 10−33 seconds after
the Big Bang. Inflation is a remarkably successful theory – it neatly resolves several
major problems regarding the very early universe, it’s passed every observational
test we have thrown at it, and it has been very theoretically fruitful. If anything,
though, it’s been too fruitful – in the thirty years since it was first proposed by Guth

1

2

(Guth (1981); Albrecht and Steinhardt (1982); Linde (1983)), inflation has grown
from a single theory into a large class of theories. Since we have very little empirical
access to the inflationary era, these theories have proliferated with few constraints
placed upon them by observation. Furthermore, there are theoretical alternatives to
inflation, such as ekpyrotic models, which cannot be ruled out on the basis of current
observations.
It is difficult to place observational constraints on the physics of inflation because
the inflationary epoch is so early in the history of the Universe. Very few signals
remain from that epoch, and there are none uncontaminated by late-time effects.
Most hopes for placing constraints on inflation are pinned on seeking out properties
of the primordial density perturbations that were left behind after reheating1 . The
power spectrum of the primordial perturbations has been of particular interest: its
amplitude As , spectral index ns , the running (scale-dependence) of the spectral index
dns
, and the tensor-to-scalar ratio r have all been measured or constrained, largely
d ln k

through measurements of the CMB. While all of these parameters can tell us about
the physics of inflation, the spectral index is especially notable. Standard slow-roll
inflation predicts that ns is just below one, and the WMAP CMB data confirm this
prediction (Komatsu et al. (2011)): ns = 0.963 ± 0.014. This is perhaps the greatest
observational triumph of standard inflation, but the spectral index carries limited
information about the physics of inflation – and there are many different types of
inflation (and alternatives to inflation altogether) which predict the same value for
ns . A large number of these models are also consistent with current measurements
s
of As , ddn
, and r, leaving us with dozens of alternatives and few prospective means
ln k

of choosing among them.
1 While there is some hope of detecting gravitational waves from inflation, it is entirely possible that these waves
are far too weak to be seen with a detector smaller than the observable universe.

3

1.2

Non-Gaussianity

One way to mine the primordial density perturbations for more information
about the physics of inflation is go beyond the power spectrum and search for nonGaussianity in the distribution of the perturbations. Single-field slow-roll inflation,
with a canonical kinetic term in a Bunch-Davies vacuum, predicts that the primordial distribution of density perturbations at all scales should be very nearly Gaussian
– to about one part in 108 , though this would be reduced to one part in 106 by secondary and late-time effects (See Maldacena (2003), among many others; for a more
recent review, see Yadav and Wandelt (2010)). Specifically, the magnitude of the
primordial fluctuations should follow a Gaussian distribution at all scales (see Figure
1.1). This follows from Wick’s theorem, which guarantees that the Nth-order correlation function of the inflaton field will be equal to the Nth moment of a Gaussian
distribution, given the assumptions of standard inflation (slow-roll, Bunch-Davies
vacuum, canonical kinetic term, and a single inflaton field). Thus, the detection of
significant non-Gaussianity would be a serious challenge to the simplest models of
inflation, and would be a corresponding boon to non-standard inflationary theories.
1.2.1

Modeling non-Gaussianity

Unfortunately, searching for non-Gaussianity is not as simple as searching for a fit
to a given probability distribution – “non-Gaussianity” is a wildly non-specific term.
(Calling a distribution “non-Gaussian” is like calling an object “not a puppy” – many
things (hats, lions, sonic screwdrivers) are not puppies.) The universe is so close to
Gaussian that merely searching for deviations from Gaussianity in the distribution
of the primordial perturbations isn’t an enlightening line of inquiry (Figure 1.2). But
sensitive estimators of non-Gaussianity can be constructed if a particular model is

4
45000

P( φ )
40000

35000

30000

25000

20000

15000

10000

5000

φ
0
0.00003

0.00002

0.00001

0.00000

0.00001

0.00002

0.00003

Figure 1.1: A comparison of a Gaussian distribution (black curve) with a non-Gaussian distribution
of the local type (Equation 1.1; blue curve). Here, the non-Gaussianity parameter fNL = 104 , much
larger than it is in our universe; I have made it large so the difference between the two distributions
is visible. (See Figure 1.2.) The slight excess in the high tail of the non-Gaussian distribution (blue
filled region) is the key region for detecting non-Gaussianity in large-scale structure today.

picked. The most commonly discussed model of non-Gaussianity, known as the local
or “squeezed” model, is defined via (see e.g. Komatsu and Spergel (2001)):
(1.1)

Φ(x) = φG (x) + fNL (φG (x)2 − hφG (x)2 i).

Here, Φ denotes the primordial curvature perturbations (Bardeen’s gauge-invariant
potential), and φG (x) is a Gaussian random field. The parameter fNL characterizes
the level of non-Gaussianity – in a Gaussian universe, fNL = 0. Looking more
carefully at (1.1), we will have non-Gaussianity of order unity when the second term
is roughly equal to the first term; that is, when fNL ∼ 1/φG ∼ 105 .
The local model has been much studied, in part because it is the first two terms
of the most general local form of non-Gaussianity (Babich et al. (2004)). This model

5

is also theoretically well-motivated: various popular forms of inflation, including
curvaton, multi-field, and modulated reheating models, all predict some amount
of local non-Gaussianity (Yadav and Wandelt (2010)). Perhaps the most interesting
thing about the local model is the remarkable result from Creminelli and Zaldarriaga
(2004): the detection of fNL much greater than unity would rule out all single-field
inflation models, regardless of the dynamics involved.
1.2.2

Detecting non-Gaussianity

In addition to the vagueness of the term “non-Gaussianity,” there is the further
problem that neither the primordial curvature perturbations Φ(k) nor the primordial
density fluctuations δρ/ρ are directly observable. To learn more about primordial
non-Gaussianity, we have to turn the clock back: we must infer properties of the
primordial perturbations from their “descendants,” the CMB anisotropies and the
large-scale structure (LSS) of the universe today. (See Figures 1.3 and 1.4.) Since
the universe is so close to Gaussian – and since Gaussian distributions are fully
described by their one- and two-point functions – we must look at higher-order
correlation functions (and their Fourier transforms, the polyspectra) in order to test
any given model of non-Gaussianity. The polyspectra generally offer a much larger
number of observables, yielding a large signal-to-noise ratio even if S/N is small in
each individual observable. For example, if there was non-Gaussianity of the local
type in the primordial universe, then the bispectrum (the Fourier transform of the
three-point function) of the CMB is directly proportional to fNL ; and the number
of angular-averaged terms B`1 `2 `3 in the bispectrum is proportional to `3max , where
`max ∼ 500 for WMAP. In fact, the best constraints on the Gaussianity of the universe
have until recently come from the bispectrum2 of the CMB: WMAP has constrained
2 Some models of non-Gaussianity exist that lead to modifications in the four-point function and its Fourier
transform, the trispectrum; these are often characterized using the parameters gNL and τNL . These are not quite as

6

fNL to roughly 30 ± 20 (Komatsu et al. (2011)), corresponding to a universe that is
Gaussian to about one part in 103.5 . However, Dalal et al. (2008) pointed out that
a non-zero fNL leads to a strongly scale-dependent dark matter halo bias, which can
be detected in the power spectrum of large-scale structure; this technique has since
emerged as a source of constraints already competitive with the CMB (Slosar et al.
(2008)).3
Applying these methods in the context of scale-dependent models of non-Gaussianity
is the focus of the rest of this work. In the rest of this chapter, I will examine the
local model in greater detail, along with scale-dependent extensions of that model;
in Chapter II, I’ll discuss the relatively new method of constraining non-Gaussianity
from the power spectrum of the LSS, following Dalal et al. (2008), in the context of
scale-dependent models; in Chapter III, I’ll discuss methods of constraining scaledependent models from the CMB; in Chapter IV, I’ll give actual constraints from
current WMAP data on a particular scale-dependent model; finally, Chapter V comprises my overall conclusions and a summary.
1.3

Beyond the local model

Switching over to Fourier space, the local model takes the form:
Z
(1.2)

Φ(k) = φG (k) + fNL

d3 k 0
φG (k 0 )φG (k − k 0 ).
(2π)3

For this model, the primordial curvature bispectrum takes a relatively simple form:
(1.3)

Bφ (~k1 , ~k2 , ~k3 ) = 2fNL (2π)3 δ(~k1 + ~k2 + ~k3 )(Pφ (k1 )Pφ (k2 ) + perm.).

well-studied, in part because there are few truly computationally-efficient algorithms to calculate the trispectrum. I
will not be considering such models in this work.
3 There are also other techniques involving large-scale structure, most notably the galaxy bispectrum and cluster
counts – but the former is not practical to calculate, and the latter is not nearly as sensitive a probe of non-Gaussianity
as the halo bias.

7

Here, Pφ is the power spectrum of the primordial curvature perturbations, and δ
is the Dirac delta function, enforcing the condition that the three k-vectors must
form a triangle. Assuming translational symmetry, the primordial bispectrum for
any model can always be written in the form (Babich et al. (2004)):
(1.4)

Bφ (~k1 , ~k2 , ~k3 ) = (2π)3 δ(~k1 + ~k2 + ~k3 )F (~k1 , ~k2 , ~k3 ),

where F is known as the shape function, so called because it determines which shapes
of triangles in k-space are the dominant contributions to the bispectrum. Thus, we
can characterize different models of primordial non-Gaussianity by looking at the
shape functions that they produce. We can easily see that F for the local model is
(1.5)

Flocal (k1 , k2 , k3 ) = 2fNL (Pφ (k1 )Pφ (k2 ) + perm.),

where Pφ (k) ∝ k −(4−ns ) is the primordial curvature power spectrum. This function is
maximized for triangles with one side much shorter than the others: k3 << k1 ∼ k2 –
a long thin “squeezed” isosceles triangle. (Hence the name “squeezed model” for the
local model.) Other models of non-Gaussianity favor triangles of different shapes.
The equilateral model, as the name suggests, has much of its power in near-equilateral
triangles; this type of non-Gaussianity is seen in DBI inflation, ghost inflation, and
other inflationary models with non-standard kinetic terms. Models of inflation that
drop the assumption of a Bunch-Davies vacuum can give rise to non-Gaussianity
with a shape function that favors “folded” triangles: k1 ∼ k2 ∼ k3 /2 (see e.g. Babich
et al. (2004); Chen (2005)).
1.3.1

Scale-dependent non-Gaussianity

While these models each favor a different shape of triangle, the deviation from
Gaussianity in each model is independent of scale.4 But there is good theoretical
4 Scale-independence for a particular model of non-Gaussianity does not imply that similar triangles of different
sizes in k-space contribute equally to the primordial curvature bispectrum associated with that model. A glance

8

motivation to think that non-Gaussianity, if it exists, will be scale-dependent; this is
a generic result of single-field inflationary models with interactions, along with most
multi-field models (e.g. Salopek and Bond (1990); Luo and Schramm (1993); Wang
and Kamionkowski (2000); LoVerde et al. (2008); Sefusatti et al. (2009)). We can
introduce scale-dependence to the local model by promoting the parameter fNL to a
function of scale, fNL (k). The curvature pertubations in this new model are
Z
(1.6)

Φ(k) = φ(k) + fNL (k)

d3 k 0
φ(k 0 )φ(k − k 0 ).
(2π)3

This form of non-Gaussianity is expected in curvaton or modulated reheating scenarios (see e.g. Byrnes et al. (2010) and Shandera et al. (2011), where this form explicitly
appears in the study of these models; see also Linde and Mukhanov (1997); Lyth
and Wands (2002); and Zaldarriaga (2004), among many others). Note that this new
ansatz is not local, which is clear when we transform back into real space:
(1.7)

Φ(x) = φ + fNL (x) ∗ (φ(x)2 − hφ(x)2 i),

where ∗ represents convolution and x denotes a three-dimensional spatial coordinate.
The shape function F for this model takes the form:
(1.8)

F (k1 , k2 , k3 ) = 2 (fNL (k3 )Pφ (k1 )Pφ (k2 ) + 2 perm.)

We can parametrize fNL (k) in a way that is valid for any general form of fNL (k)
by breaking fNL (k) into a set of piecewise-constant (in wavenumber) bins, such that
i
fNL (k) is equal to fNL
in the ith wavenumber bin (Becker et al. (2011)):

(1.9)

i
fNL
≡ fNL (ki ).

at (1.5) confirms this: Flocal (λk1 , λk2 , λk3 ) = λ−(8−2ns ) Flocal (k1 , k2 , k3 ). This scale-dependence comes from the
fact that we are looking at the primordial curvature bispectrum, which is related to the bispectrum of density
perturbations through the Poisson equation.

9

In this work, we pay special attention to this parametrization of fNL (k), as well as
a simple form of non-Gaussianity analogous to the conventional parameterization of
the power spectrum
(1.10)

∗
fNL (k) = fNL



k
kpiv

nf

NL

.

∗
Here, kpiv is an arbitrary fixed parameter, leaving fNL
and nfNL as the parameters of

interest in this model (Shandera et al. (2011); Becker et al. (2011)).
In the rest of this work, I will forecast and find constraints on scale-dependent
non-Gaussianity of the form (1.6). Chapters II and III are focused on projecting
constraints on the piecewise-constant parameters in (1.9) using LSS and the CMB,
respectively. In Chapter IV, I find the constraints placed on nfNL from the WMAP7
CMB temperature data set – to the best of my knowledge, a novel result.

10
45000

P( φ )
40000

35000

fNL =104

30000

25000

20000

15000

10000

5000

φ
0
0.00003

0.00002

0.00001

0.00000

0.00001

0.00002

0.00003

45000

P( φ )
40000

35000

fNL =103

30000

25000

20000

15000

10000

5000

φ
0
0.00003

0.00002

0.00001

0.00000

0.00001

0.00002

0.00003

45000

P( φ )
40000

35000

fNL =102

30000

25000

20000

15000

10000

5000

φ
0
0.00003

0.00002

0.00001

0.00000

0.00001

0.00002

0.00003

Figure 1.2: A further comparison of Gaussian and local non-Gaussian distributions. As the text
in each panel indicates, the top panel has fNL = 104 , the middle has fNL = 103 , and the bottom
panel has fNL = 102 . For fNL < 103 , it is quite difficult to tell the difference between the Gaussian
and non-Gaussian one-point functions; thus, higher-order correlation functions and estimators are
needed.

11

fNL= -5000

fNL= -500

fNL= 0

80 Mpc/h

fNL= +500

fNL= +5000
375 Mpc/h

Figure 1.3: The effects of local non-Gaussianity on N-body simulations of large-scale structure
(Dalal et al. (2008)). Here, we have five different simulations, each with a different value of fNL ,
but all with exactly the same initial conditions. Local non-Gaussianity introduces a scale-dependent
bias into the halo power spectrum; see Chapter II.

12

fNL= -5000

fNL= +5000

fNL= 0
fNL= -500

fNL= +500

Figure 1.4: Effects of local non-Gaussianity on Monte Carlo simulations of the CMB sky, based on
Elsner and Wandelt (2009).

CHAPTER II

Forecasted constraints on scale-dependent non-Gaussianity
from LSS

2.1

Non-Gaussianity and bias

2.1.1

The effect of a non-vanishing bispectrum on bias

Dalal et al. (2008) found, analytically and numerically, that the bias of dark
matter halos acquires strong scale dependence if fNL 6= 0:
(2.1)

b(k) = b0 + fNL (b0 − 1)δc

3Ωm H02
.
a g(a)T (k)c2 k 2

Here, b0 is the usual Gaussian bias (on large scales, where it is constant), δc ≈ 1.686
is the collapse threshold, a is the scale factor, Ωm is the matter density relative
to the critical density, H0 is the Hubble constant, k is the wavenumber, T (k) is
the transfer function, and g(a) = g(1) D(a)
is the growth suppression factor . This
a
result has been confirmed by other researchers using a variety of methods, including the peak-background split (e.g. Afshordi and Tolley (2008)), perturbation theory (e.g. McDonald (2008)), and numerical (N-body) simulations (e.g. Desjacques
et al. (2009)). Astrophysical measurements of the scale dependence of the large-scale
bias, using galaxy and quasar clustering as well as the cross-correlation between the
galaxy density and CMB anisotropy, have recently been used to impose constraints
Portions of this chapter first appeared in:
Becker, A., Huterer, D., Kadota, K., Scale-dependent non-Gaussianity as a generalization of the local model, Journal
of Cosmology and Astroparticle Physics, 2011, vol. 1, p. 006, doi:10.1088/1475-7516/2011/01/006

13

14

Halos

3

δρ/ρ
2

δc

1

0

1

2

Total (short + long) fluctuations Long-wavelength fluctuations

3

0.0

0.2

0.4

0.6

0.8

Figure 2.1: The peak-background split. Halos form when the local matter overdensity δρ/ρ
exceeds the critical threshold for collapse, δc (red dashed line). In our toy model here, small-scale
fluctuations are added to the large-scale fluctuations (green line) to get the overall fluctuations
(black line). A given fluctuation is more likely to exceed the threshold and form a halo (blue
regions) when it is sitting on top of a large-scale overdensity than when it is sitting on top of a
large-scale underdensity; this is why there are more blue halos on the left than there are on the
right.

on fNL already comparable to those from the cosmic microwave background (CMB)
anisotropy, giving fNL = 28 ± 23 (1σ), with some dependence on the assumptions
made in the analysis (Slosar et al. (2008)). In the future, constraints on fNL are
expected to be on the order of a few (Dalal et al. (2008); Cunha et al. (2010)). The
sensitivity of the large-scale bias to other models of primordial non-Gaussianity has
not yet been investigated much (though see analyses in e.g. Desjacques and Seljak
(2010); Verde and Matarrese (2009)).
To get a physical picture of how halo bias is sensitive to local non-Gaussianity,
first remember that halos form when the local matter overdensity δρ/ρ exceeds the
critical threshold for collapse, δc . Therefore, a given small-scale fluctuation is more

1.0

15

likely to exceed the threshold when it is sitting on top of a large-scale overdensity
than when it is sitting on top of a large-scale underdensity (see Figure 2.1). This
picture is called the peak-background split, and it is the primary source of the linear
halo bias: δhalo = b0 δmatter .
Local non-Gaussianity introduces a coupling between the power in primordial
curvature fluctuations, Φ, at small scales and large scales. Φ and δρ are related
by the Poisson equation: Φ ∼ kδρ2 . Thus, when fNL 6= 0, the power in small-scale
density fluctuations becomes tied to the power in large-scale density fluctuations,
which introduces a scale-dependent term ∆b(k) ∼ k −2 into the halo bias.
We can get a more rigorous derivation of this extra term by starting with the
full Poisson equation, to find the relation between Φ(k) and the present-time (z=0)
smoothed linear overdensities δR :
(2.2)

δR (k) =

2 k 2 T (k)
W̃R (k)Φ(k) ≡ MR (k)Φ(k);
3 H02 Ωm

where T (k) is the matter transfer function, H0 is the Hubble constant, Ωm is the
matter density relative to critical today, and W̃R (k) is the Fourier transform of
the top-hat filter with radius R. The smoothing spatial scale R is related to the
smoothing mass scale M via
(2.3)

4
M = πR3 ρm,0 ,
3

where ρm,0 is the matter energy density today.
One can expand the two point correlation function of dark matter halos, ξh (x1 , x2 ),
(N )

in terms of high-order correlation functions of the underlying density field, ξR . In
the high-threshold limit (ν  1), this becomes the so-called MLB formula (Grinstein

16

and Wise (1986); Matarrese et al. (1986)):
ξh (x1 , x2 ) = ξh (x12 )

(2.4)


= −1 + exp 

∞ N
−1
X
X





x1 , ..., x1 ,
x2 , ..., x2
ν
1

(N ) 
ξ

 ;
R
N
j!(N
−
j)!
σ
R
N =2 j=1
j times (N − j) times
N

where xij = |xi − xj |, ν = δc /σR is the peak height, and ξR (n) (r) is the n-point
correlation function of the underlying matter density field smoothed with a top-hat
filter of radius R. Keeping the terms up to the three-point correlation function, which
is reasonable for the observationally allowed range of fNL , the expansion series gives
us the halo correlation function in terms of the density field correlation functions:
(2.5)

ξh (x12 ) =

ν 2 (2)
ν 3 (3)
ξ
(x
,
x
)
+
ξ (x1 , x1 , x2 ) + . . .
1
2
σR2 R
σR3 R

The power spectrum is given, to the same expansion order as Eq. (2.5), by
ν2
ν3
Ph (k) = 2 PR (k) + 3
σR
σR

(2.6)

Z

d3 q
BR (k, q, |k − q|) + . . .
(2π)3

The first term on the right-hand side includes the familiar (Gaussian) bias b =
ν/σR (in the high-peak limit for which the MLB formula is valid) for the Gaussian
fluctuations. The effects of non-Gaussianity on the galaxy bias are represented by
the second term, including the bispectrum BR , which vanishes for the Gaussian
fluctuations.
2.1.2

Beyond the high-peak approximation

The expression (2.1) is only correct in the high-peak, small-k limit. Desjacques
et al. (2011) pointed out an additional term is required for the exact expression:
(2.7)

F (k)
∆b(k) = 2
MR (k)



δc
d ln F (k)
(b0 − 1)
+
D(z)
d ln σ0s

17

where

(2.8)

Z
1
F (k) ≡ 2 2
dk1 k12 MR (k1 )Pφ (k1 )
8π σR


Z 1
Pφ (k2 )
×
dµMR (k2 ) fNL (k)
+ 2fNL (k2 ) .
Pφ (k)
−1

The new term (second term on the left-hand side of Equation 2.7) vanishes when
the fiducial fNL (k) = 0, but it remains relevant for any other constant or scaledependent fiducial value, even for the piecewise-constant parametrization of fNL (k)
from equation (A.13). (See Appendix A.2.1 for details on this.) Desjacques et al.
have found that this new term explains previously mysterious discrepancies (Shandera et al. (2011)) between the theoretical expectation for the scale-dependent bias
and the results of numerical simulations.
2.2

Forecasted constraints on scale-dependent non-Gaussianity from largescale structure

2.2.1

Fisher matrix analysis

We would like to project constraints on scale-dependent non-Gaussianity for future
galaxy redshift surveys. To do this, we can calculate the Fisher information matrix
j
for the parameters fNL
that describe the piecewise-constant fNL (k). The Cramér-

Rao inequality tells us that the inverse of the Fisher matrix sets a lower bound
i
on the covariance matrix we can get on our parameters fNL
from our hypothetical

survey. Specifically, given the Fisher matrix Fij , the minimum possible marginalized
p
√
i
and unmarginalized errors for a particular fNL
are Fii−1 and 1/ Fii , respectively.
Thus, the Fisher matrix allows us to forecast the extent to which scale-dependent
non-Gaussianity could be constrained by future galaxy surveys. (For more on Fisher
matrix analysis in general, see Appendix B.1. Details on calculating the derivative of
the bias with respect to fNL and fNL (k), a necessary intermediate step in calculating

18

the Fisher matrix, are in Appendix A.)
We consider measurements of the power spectrum Ph (k) of dark matter halos
(galaxies or clusters, for example) averaged over thin spherical shells in k-space. The
variance of Ph (k) ≡ Ph in each shell is (Feldman et al. (1994))
σP2 h =

(2.9)

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

where Vshell = 4πk 2 dk/(2π)3 is the volume of the shell in Fourier space (we are
ignoring redshift distortion effects for simplicity here). Therefore, the Fisher matrix
for measurements of Ph (k, z) is the standard expression from Tegmark (1997):
(2.10)

Fij =

X

Z kmax
Vm

m

kmin

∂Ph (k, zm ) ∂Ph (k, zm )

∂pi
∂pj

1
Ph (k, zm ) +

k 2 dk
,
2
1 (2π)2
n

where Vm is the comoving volume of the m-th redshift bin, each redshift bin is
centered on zm , and we have summed over all redshift bins. We adopt kmin =
10−4 h−1 Mpc, and we choose kmax as a function of z so that σ(π/(2kmax ), z) = 0.5
(Seo and Eisenstein (2003)), which leads to kmax (z = 0) ≈ 0.1h Mpc−1 . Ph is the
dark matter halo power spectrum, related to the true dark matter power spectrum
P through
Ph (k) = b(k)2 P (k),

(2.11)

where each quantity implicitly also depends on redshift. Finally, pi are the paramei
ters of interest; in our case, these are the fNL
.

2.2.2

Survey properties

We assume a future survey covering one-quarter of the sky (about 10,000 square
i
degrees) out to z = 1, and find constraints for a set of 20 fNL
uniformly spaced in

log k in the range 10−4 ≤ k/(h Mpc−1 ) ≤ 1, with a smoothing scale of Msmooth =

19

1014 M . We assume a flat universe and a fiducial model of constant non-Gaussianity
i
at the value favored by the seven-year WMAP CMB data: fNL (k) = 30 = fNL
. We
i
include six cosmological parameters in our Fisher matrix aside from the fNL
: Hubble’s

constant H0 ; physical dark matter and baryon densities Ωcdm h2 and Ωb h2 ; equation of
state of dark energy w; the log of the scalar amplitude of the matter power spectrum,
log As ; and the spectral index of the matter power spectrum, ns . Fiducial values
of these parameters correspond to their best-fit WMAP7 values (Komatsu et al.
(2011)). We also added the forecasted cosmological parameter constraints from the
CMB experiment Planck by adding its Fisher matrix as a prior (W. Hu, private
communication). Note that the CMB prior does not include CMB constraints on
non-Gaussianity; the CMB constraints on fNL (k) are studied separately in Chapter
i
, we include five
III. Finally, in addition to the cosmological parameters and the fNL

Gaussian bias parameters in our Fisher matrix – one b0 (z) for each redshift bin.1 The
fiducial values of these parameters are set by the Sheth-Tormen formalism (Sheth
and Tormen (1999)). All of the hypothetical galaxy redshift surveys in this chapter
and in Chapter III have these same assumptions, unless explicitly stated otherwise.
2.2.3

i
Forecasted constraints on the fNL

i
We already have the derivatives of b(k) with respect to each of the fNL
(see
i
Appendix A for these), so the derivative of Ph (k) with respect to the fNL
is just

(2.12)

∂Ph (k)
∂b(k)
=2
b(k)Pmat (k);
i
i
∂fNL
∂fNL

Pmat (k) is the ΛCDM matter power spectrum, easily obtained from a numerical
code – in this case, CAMB. Since we only consider information from large scales
1 Using six cosmological parameters along with five b (z) and 20 f i
0
NL led us into some issues with floating-point
errors and numerical precision. The 31 × 31 Fisher matrix we obtained was rather ill-conditioned and difficult to
invert reliably using 64-bit precision; we were eventually forced to move to 128-bit precision in order to accurately
marginalize over the cosmological parameters and nuisance parameters.

20

(k ≤ kmax ≈ 0.1 h Mpc−1 ), we do not model the small amount of nonlinearity present
i
at the high-k end of these scales. (Note that, while some of the fNL
have support

at k > kmax (z = 1) ≈ 0.2 h Mpc−1 , we only use information about those (and other)
parameters coming from k < kmax (z) in each z-bin.)
The constraints vary considerably as a function of the k at which these parameters
i
are defined. The best-constrained fNL
corresponds to the 10−0.6 < k < 10−0.4 bin,
17
and it has an estimated unmarginalized error of σ(fNL
) = 28; for comparison, the
i
worst-constrained fNL
, which corresponds to the largest scale (smallest k) bin, has

an unmarginalized error well over 1011 . As expected, the marginalized constraints for
the best-constrained parameters are a bit weaker than the unmarginalized constraints
i
– the best-measured fNL
has an estimated marginalized error of 41. In general,

dependence of the constraints on the value of k is determined by two competing
factors: as k increases, there is a larger number of modes, each with a smaller signal
(given by the smaller nongaussian bias ∆b). The best-constrained k is also affected
by the fact that only information out to k = kmax = 0.1h Mpc−1 is assumed from
the galaxy survey. In particular, we have checked that if we unrealistically assume
information to be available at all k (instead of at k < kmax ) without modeling the
i
nonlinearities, the unmarginalized constraints on fNL
improve monotonically with
i
increasing k. Therefore, the raw signal-to-noise ratio in fNL
increases with k.

2.3

Projection and principal components

2.3.1

Constraining other fNL (k) models

i
Once the Fisher matrix F has been obtained for the set of parameters fNL
, it is
i
quite simple to find the best possible constraints on the fNL
that could be obtained

from a future galaxy redshift survey. By projecting this Fisher matrix into another
basis, it is also possible to find the constraints on any arbitrary fNL (k) without

21

106

106

i
Forecasted Error in fNL

107

i
Forecasted Error in fNL

107

105

105

104

104

103

103

102

102

101
0
1010
-4

101

10-3

10-2

k (h/Mpc)

10-1

0
1010
-4

100

10-3

(a) Unmarginalized errors

10-2

k (h/Mpc)

10-1

100

(b) Marginalized errors

Figure 2.2: Forecasted unmarginalized (left panel) and marginalized (right panel) constraints on
i
piecewise-constant parameters fNL
assuming a future galaxy survey covering one-quarter of the
sky out to z = 1, with average number density of 2 × 10−4 gal/Mpc3 . For comparison, the green
horizontal line is the constraint found for a constant fNL using the same survey assumptions . While
i
are poorly constrained as expected, their few best linear combinations
the individual parameters fNL
– the principal components – are well measured; see the next section and text for details.

calculating a new Fisher matrix from scratch. A trivial example can be found in
Appendix B.2, where we find that the estimated error on a constant fNL , assuming
the same future survey as in the previous section, is σ(fNL ) = 8.7. (Note that
this forecasted constraint is on a par with the error expected from Planck, where
σ(fNL ) ∼ 5.)
For another, scale-dependent example, consider a power-law form for fNL (k) (as
in Equation 1.10):
(2.13)

∗
fNL (k) = fNL



k
kpiv

nf

NL

,

∗
where kpiv is an arbitrary fixed parameter, leaving fNL
and nfNL as the parameters

of interest in this model. (kpiv is generally chosen to minimize degeneracy between
∗
fNL
and nfNL for the observable of interest. We have set kpiv = 0.20h Mpc−1 , close to

the optimal value in our case; in CMB analysis, the optimal value is lower, around
i
0.08h Mpc−1 .) The partial derivatives of our basis of fNL
with respect to these

22

parameters are:
(2.14)

i
∂fNL
=
∗
∂fNL

(2.15)

i
∂fNL
∂nfNL

=



k
kpiv


∗
fNL

nf

NL

;
k
kpiv

nf



NL

log

k
kpiv


.

i
Starting in a basis of 20 fNL
evenly spaced in log k, we project down to a basis
∗
of fNL
and nfNL in order to forecast constraints on the two new parameters from a

survey covering one-quarter of the sky out to z = 1. We are using the same limits of
∗
integration as in Section 2.2.1, along with the fiducial values fNL
= 30 and nfNL = 0.

The forecasted constraints on these parameters, marginalized over each other, are
∗
σfNL
= 8.7 and σnfNL = 0.85.

2.3.2

Principal components

We now represent a general function fNL (k) in terms of principal components
(PCs). In this approach, the data determine which particular modes of fNL (k) are
best or worst measured. The PCs also constitute a useful form of data compression,
so that one can keep only a few of the best-measured modes to make inferences about
the function fNL (k). Finally, the PCs will also enable us to measure the degree of
similarity between our scale-dependent ansatz and the local and equilateral forms of
non-Gaussianity.
It is rather straightforward to start from the covariance matrix for the piecewise
i
constant parameters fNL
and obtain the PCs of fNL (k). The PCs are weights in

wavenumber with amplitudes that are uncorrelated by construction, and they are
ordered from the best-measured (i = 0) to the worst-measured (i = 19) for the
assumed fiducial survey. The construction of the PCs is described in Appendix B.3. A
few of these PCs of fNL (k) are shown in Fig. 2.3. For example, the best-measured PC
has most of its weight around k = 10−0.4 h Mpc−1 , which agrees with sensitivities of

PC0

0
0

-1

10

10

10

-2

-3
10

10

0
10

10

-2
10

10

10

-3

-1

PC2

-4

e(2) (k)
e(3) (k)

10

10

-2
10

10

PC1

-4

e(1) (k)

10

-3

-1

1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0 -4
10
-4

e(0) (k)

23

PC3

10-3

10-2

10-1

100

Figure 2.3: The forecasted best-measured principal components of fNL (k). The PCs, e(j) (k), are
i
, and are ordered from the best-measured one (j = 0)
eigenvectors of the Fisher matrix for the fNL
to the worst-measured one (j = 19) for the assumed fiducial survey.

piecewise-constant parameters shown in Fig. 2.2. Again, the sensitivity is not greatest
at the largest value of k (1 h Mpc−1 ) because we assumed cosmological information
from k ≤ kmax = 0.1 h Mpc−1 . We checked that information available at a higher
kmax would shift the “sweet spot” of sensitivity to higher wavenumbers in this case
as well.
The forecasted error in the best-measured PC is 19.3; the error in the next-best
measured PCs are 31.3 and 34.7, but the accuracy rapidly drops off from there. Thus,
the first three or four PCs should be enough for any conceivable application. The
forecasted error in each PC is plotted on a logarithmic scale in figure 2.4.

24

105
104
103
102
101
100 0

2

4

6

8

10

Principal Component

12

14

Figure 2.4: Forecasted RMS error on each principal component from LSS.

2.4

Conclusions

In this chapter, we used forecasted constraints from an intermediate-future galaxy
i
survey to calculate errors on individual parameters fNL
(see Fig. 2.2). Projecting
i
down to a different basis, we were able to project
the Fisher matrix for the fNL

constraints on the power-law model of fNL (k) (1.10). We further calculated the
principal components of fNL (k), and thus identified the best-measured configurations
(in wavenumber) of this function (see Fig. 2.3). While the sensitivity of the survey
to non-Gaussianity increases with increasing k, restricting the survey information to
scales where linear perturbation theory is valid imposes a “sweet spot” in sensitivity
of k ∼ 0.2h Mpc−1 . We will see a similar effect – but at a different scale – in the
i
next chapter, where we forecast constraints on the fNL
from the CMB.

CHAPTER III

Forecasted constraints on scale-dependent non-Gaussianity
from the CMB

3.1

Signatures of the generalized local model in the CMB

Traditionally, the best constraints on non-Gaussianity have come from the CMB.
This is done almost exclusively through estimators involving the N-point correlation
functions for N > 2 and their Fourier transforms, the polyspectra. Most emphasis
has been on the N = 3 case, or the bispectrum of temperature fluctuations in the
CMB, if only because of its relative computational simplicity. The well-known general
expression for the CMB bispectrum, re-derived in Appendix C.1, is
 3 r

Z
2
(2`1 + 1)(2`2 + 1)(2`3 + 1) `1 `2 `3
pqr
B`1 `2 `3 =
k12 dk1 k22 dk2 k32 dk3
π
4π
000
Z ∞
p
q
r
× BΦ (k1 , k2 , k3 )t`1 (k1 )t`2 (k2 )t`3 (k3 )
r2 dr j`1 (k1 r)j`2 (k2 r)j`3 (k3 r).
(3.1)
0

In principle, we can use this to find the Fisher matrix Fij for the CMB bispectrum:
(Babich and Zaldarriaga (2004); Komatsu and Spergel (2001))
(3.2)

FijCMB = fsky

∂B`pqr
∂B`lmn
−1
1 `2 `3
1 `2 `3
(C`1 `2 `3 )lmn,pqr
∆`1 `2 `3 ∂pi
∂pj
lmn,pqr 2≤` ≤` ≤`
X

1

X

1

2

3

Here, C is the covariance of the bispectrum and pi,j are the parameters of interest.
∆`1 `2 `3 is a combinatoric term – equal to 6 when `1 = `2 = `3 , 1 when `1 6= `2 6= `3 ,
and 2 otherwise (Spergel and Goldberg (1999)). The indices i, j, k and p, q, r run
25

26

107
i
Forecasted Error in fNL

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

100

(a) LSS

(b) Planck

107
i
Forecasted Error in fNL

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

100

(c) Combined

Figure 3.1: LSS (top left), CMB (top right), and combined (bottom) forecasted constraints on the
i
in the generalized local model. All constraints are unmarginalpiecewise constant parameters fNL
ized. The LSS constraints come from the power spectrum of halos, assuming the same survey
parameters as Section 2.2.2, while the CMB constraints come from the bispectrum of temperature
and polarization fluctuations. See text for details. For reference, the green line is the forecasted
error on a constant fNL using the same assumptions. There are bins “missing” on the rightmost
end of the Planck plot; those bins correspond to k-values too large to be probed when `max = 2000,
as it is here.

independently over all eight possible ordered triplets of temperature and polarization
fields (TTT, TTE. . . EEE). C can be thought of as a 6-point function, being the
covariance of the 3-point function; since fNL  105 , it is reasonable to only consider
the Gaussian contribution to the covariance of the bispectrum, C. Using Wick’s
theorem, this is:
(3.3)

C`1 `2 `3 = C`1 C`2 C`3

27

, and the derivatives of the bispectrum are
Further details of calculating C, B`pqr
1 `2 `3
all in Appendix C.
Equation (3.1) is a totally general result for the bispectrum of the CMB in terms
of the primordial Bardeen curvature bispectrum BΦ ; we have not picked a particular
model of non-Gaussianity. But (3.1) is not useful without an expression for BΦ . For
the local model (i.e. constant fNL ), BΦ is:
BΦ (k1 , k2 , k3 ) = 2∆2φ fNL

(3.4)

!

1
3−(ns −1) 3−(ns −1)
k2

+ perm.

k1

where ∆φ is the amplitude of the primordial Bardeen curvature power spectrum.
Using Eqs. (3.2), (C.29), and (C.24), we have the following expression for the CMB
bispectrum Fisher information in the constant fNL case:
FfCMB
NL

=

4∆4φ


2
(2`1 + 1)(2`2 + 1)(2`3 + 1) `1 `2 `3
1
∆`1 `2 `3
4π
000
∆`1 `2 `3
lmn,pqr 2≤` ≤` ≤`
X

1

×

2

3

(C`−1
)lp (C`−1
)mq (C`−1
)nr
1
2
3
Z ∞

(3.5)

1

X

×

2

r dr
0

Z ∞

2

r dr

α`l 1 (r)β`m2 (r)β`n3 (r) + perm.




0

α`p1 (r)β`q2 (r)β`r3 (r) + perm.




.

For the scale-dependent generalized local model, with fNL (k) in place of fNL ,
things are somewhat more complicated. The Bardeen curvature bispectrum is:
!
f
(k
)
NL
3
+ perm. .
(3.6)
BΦ (k1 , k2 , k3 ) = 2∆2φ
3−(n −1) 3−(n −1)
k1 s k2 s
Using the piecewise-constant parametrization of fNL (k) together with (3.2), (C.29),
i
and (C.25), we get an expression for the Fisher matrix of the fNL
that is similar to

(3.5):

28

FijCMB

=

4∆4φ

`X
max


2
(2`1 + 1)(2`2 + 1)(2`3 + 1) `1 `2 `3
∆`1 `2 `3
4π
000
lmn,pqr 2≤` ≤` ≤`
X

1

×
(3.7)

1

2

1

3

(C`−1
)ip (C`−1
)jq (C`−1
)kr
1
2
3

Z ∞

2



r dr
∆`1 `2 `3
0

Z ∞

q
p,j
r
2
r dr α`1 (r)β`2 (r)β`3 (r) + perm. .
×

α`l,i1 (r)β`m2 (r)β`n3 (r) + perm.



0

Despite appearances, calculating the full Fisher matrix F CMB is relatively straightforward, and it takes roughly half an hour (on four 2.2 GHz processors) for twenty
i
parameters with `max ≈ 2000. (Some tabulation is necessary for the α and β
fNL

functions, and the Wigner 3j-symbol is not easy to calculate for large `. Details on
all of this are in Appendix C.) We did not include other cosmological parameters in
this Fisher matrix, as the CMB bispectrum does not constrain them terribly well,
nor is fNL expected to be terribly degenerate with them; the CMB power spectrum
places much stronger constraints on other cosmological parameters.
3.2

Results and joint constraints

3.2.1

i
Forecasted constraints on the fNL

We have performed a CMB Fisher matrix analysis to forecast errors from the
Planck mission: we take `max = 2000 and noise parameters from the Planck “blue
book.” Figure 3.1 shows the (unmarginalized) constraints on the piecewise constant
i
parameters fNL
in the generalized local model from the LSS and Planck forecasts

individually, as well as combined. Note that both types of surveys have comparable
constraints at the pivot wavenumber, and the pivots also agree (though this statement
is only approximate given the huge range of scales on both axes). Away from the
pivot, the Planck constraints are expected to be better than those from the LSS,
but both rapidly deteriorate away from the pivot kpiv ≈ 0.1h Mpc−1 . Finally, the

(a) LSS PCs

10
0

-1

10

10

10

-2

-3
10

0

-1

10

10

10

-2

-3
10

10

100

0

-1
10

10

10

-2

-3

-4

PC2

-4

e(2) (k)
e(3) (k)

10

10-1

PC1

10

10
0

-1
10

10

-2

-3
10

10

PC3

10-2

PC0

-4

e(1) (k)
0

-1
10

10

-2

-3
10

10

-4

PC2

10-3

1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0 -4
10
10

0
10

10

10

-2

-3
10

10

PC1

-4

e(1) (k)
e(2) (k)
e(3) (k)

e(0) (k)

PC0

-1

1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0 -4
10
-4

e(0) (k)

29

PC3

10-3

10-2

10-1

100

(b) Planck PCs

Figure 3.2: The forecasted best-measured principal components of fNL (k) from LSS and Planck,
i
with a fiducial fNL (k) = 30. The PCs, e(j) (k), are eigenvectors of the Fisher matrix for the fNL
,
and are ordered from the best-measured one (j = 0) to the worst-measured one (j = 19) for the
assumed fiducial survey.

combined constraints are significantly helped by breaking of the degeneracies between
the CMB and the LSS, and lead to better constraints across a wider range of scales.
We will make these statements more quantitative below when we study the specific
case where fNL (k) is a pure power law in k.
Note that our Fisher matrices for the CMB – but not for the LSS – assume
i
are fixed (known). Adding priors
all cosmological parameters other than the fNL

from other data sets (e.g. SN Ia, the power spectrum of the CMB) constrains other
cosmological parameters well enough that we would not get appreciably different
results if we had those other parameters and their priors in our Fisher matrix.
3.2.2

Principal component analysis

As in Chapter II, we can represent a general function fNL (k) in terms of principal components (PCs). Figure 3.2 shows the forecasted PCs of LSS and Planck
separately, while Fig. 3.3 shows the combined PCs. Fig. 3.4 shows the forecasted
1-σ errors on the PCs for LSS, Planck, and the two combined. Typically, the lowest
principal component (PC0) serves to see how well we can find the deviation of fNL (k)

PC0

0
10

10

-2
10

10

0
10

10

-2
10

10

e(3) (k)

0
10

10

-2
10

10

10

-3

-1

PC2

-4

e(2) (k)

10

-3

-1

PC1

-4

e(1) (k)

10

-3

-1

1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0
1.0
0.5
0.0
0.5
1.0 -4
10
-4

e(0) (k)

30

PC3

10-3

10-1

10-2

100

Figure 3.3: The forecasted best-measured principal components of fNL (k) from the joint LSS +
Planck data set.

at its pivot (i.e. best-determined wavenumber) from the fiducial value. The higher
PCs (PC1, PC2, etc) serve to probe the k-dependence of fNL .
While the combined principal components are dominated by the contribution from
the Planck PCs in this particular case, the relative strength of the LSS constraints
is strongly dependent on two factors: volume of the LSS survey and, to a slightly
lesser extent, fiducial (i.e. true) value of fNL (k). We investigate these dependences
further in the next section.
3.2.3

Projecting constraints on the power-law model of fNL (k)

As in section 2.3.1, we can project our Fisher matrix down to a different basis in
order to study the power-law parameterization of fNL (k) (see Equation 1.10):
(3.8)

∗
fNL (k) = fNL



k
kpiv

nf

NL

.

31

105

LSS
Planck
Combined

104

Error

103
102
101
100 0

2

4

6

8

10

Principal Component

14

12

Figure 3.4: Forecasted RMS error on each principal component for LSS, Planck, and combined data
sets.

We find a story similar to the one we found with the PCs; see Table 3.1. We can use
∗
the constraints on fNL
and nfNL to find constraints on fNL (k) as a whole, through

the usual methods of error propagation:
(3.9)
s
σ(fNL (k)) =

2 
2
∂fNL
∂fNL ∂fNL
∂fNL
∗
σ(fNL ) +
σ(nfNL ) + 2 ∗
Cf ∗ ,n ,
∗
∂fNL
∂nfNL
∂fNL ∂nfNL NL fNL

∗
∗ ,n
where CfNL
is the covariance between fNL
and nfNL . Using this relation, and given
fNL

some fiducial model of fNL (k), we can plot the forecasted constraints on fNL (k) as a
function of k. This is what we have done in Figure 3.5 for the Planck bispectrum, a
∗
Projected errors σ(fNL
) and σ(nfNL ), and the corresponding pivots

Variable

LSS

LSS + Planck C` s

Planck bispectrum

LSS + all Planck

∗
σ(fNL
)

17

8.7

4.4

3.9

σ(nfNL )

2.0

0.85

0.29

0.22

kpiv

0.12

0.20

0.080

0.096

∗
Table 3.1: Fiducial fNL
= 30; fiducial nfNL = 0. Each column’s numbers are for the pivot in
that column; thus the errors in the two parameters are uncorrelated in each column. LSS survey
parameters are the same as in Section 2.2.2.

32

100 L

a

(zmrge-sca
ax = 1
, fskle stru
y = 1/ ctu
4) re +
c

80 Plan

fNL(k)

ck bi

60

LSS +

trum

k bis

pectr

(z =0)

osmo
logic

spec

Planc

LSS kmax

al pr

iors

um

40
20

Fiducial fNL(k) =30

100 -4

10-3

10-2

k (h/Mpc)

10-1

100

Figure 3.5: Forecasted constraints on fNL (k) from several different data sets, assuming the power∗
law model of scale-dependent non-Gaussianity: fNL (k) = fNL
(k/kpiv )nfNL , projecting down from
i
basis. The red dashed line is the maximum k for which information was
the piecewise-constant fNL
kept in the LSS Fisher matrix at z = 0.

future large-scale structure survey, and the combination of both (along with priors
on cosmological parameters from the Planck power spectrum).
The constraints on fNL (k) from a large-scale structure survey are quite sensitive to
the survey parameters. Unlike the constraints on fNL (k) from the CMB bispectrum,
the forecasted constraints from LSS are also sensitive to the choice made for the
∗
fiducial model of fNL (k), as shown in Appendix A.3. Forecasted constraints on fNL

and nfNL for a couple of different LSS surveys, with a couple of different fiducial
models, are compared to forecasted constraints from Planck in Table 3.2. (Note
∗
that all values of nfNL are equally likely for the fiducial model where fNL
= 0, since

fNL (k) = 0 no matter what nfNL is in that case.) Figures 3.6 and 3.7 are analogous

33

100 Larg
(zm

fNL(k)

80

e-sca

ax = 2

, fskle stru
y = 1/ ctu
2) re +

Planc

k bis

60

pectr

LSS + P

20

cosm

(z =0)

ologi
c

al pr

ior

um

lanck bi

40

LSS kmax

spectru

m

Fiducial fNL(k) =30

100 -4

10-3

10-2

k (h/Mpc)

10-1

100

Figure 3.6: The same as Figure 3.5, but with different survey parameters for large-scale structure,
similar to the planned Euclid survey.

to Figure 3.5, but for different choices of survey parameters and fiducial values of
∗
and nfNL , respectively.
fNL

3.3

Conclusions

In this chapter, we studied how well the generalized local model (1.6) can be
probed with the combination of cosmic microwave background data and large-scale
structure surveys. As in Chapter II, we started by forecasting errors on the individual
i
parameters fNL
(see Fig. 3.1). We also found the best-measured linear combinations
i
of the fNL
through principal component analysis (see Fig. 3.2). We also projected the

Fisher matrix down to the two-parameter space for the power-law form of fNL (k),
and then propagated the errors from those parameters to fNL (k) as a whole (see

34

Larg
(z e-sc

LSS kmax

max = ale
1 st

40

(z =0)

Planc
, fs ruc
ky =
k bisp
1/4)ture +
LSS +
e
c
t
r
cosm
u
Planc
m
olog
k bisp
ical
ectru
20
m
prio

fNL(k)

rs

0 Fiducial f (k) =0
NL

20
40
10-4

10-3

10-2

k (h/Mpc)

10-1

100

Figure 3.7: The same as Figure 3.5, but with a fiducial fNL (k) = 0.

Figures 3.5, 3.6, and 3.7.)
We found that both the bispectrum measurement from the CMB Planck survey
and power spectrum measurement from an LSS survey can constrain fNL (k) tightly
in a relatively narrow range of wavenumbers around k ≃ 0.1h Mpc−1 . The scale best
constrained by the CMB is larger (i.e. at a smaller k) than the scale best constrained
by LSS: we get complementary information about fNL (k) from the two data sets.
Constraints from the CMB and LSS should remain comparable if systematics are
properly controlled for – but systematics are arguably more difficult to control for
LSS surveys (witness the larger number of nuisance parameters and degeneracies
in the LSS Fisher matrix). The ability of LSS to constrain fNL (k) effectively at a
wide range of scales also depends on the survey parameters and the fiducial model

35

∗ , σn
Projected errors (σfNL
) for different surveys and different fiducial fNL (k)
fNL

zmax = 1, fsky = 1/4

zmax = 2, fsky = 1/2

Planck

Fiducial fNL (k) = 30

(8.7, 0.85)

(2.2, 0.28)

(4.4, 0.29)

Fiducial fNL (k) = 0

(2.9, ∞)

(0.41, ∞)

(4.4, ∞)

∗
Table 3.2: Forecasted constraints σfNL
from different LSS surveys, assuming different fiducial models. Forecasted constraints from Planck are also shown for comparison. (All values of nfNL are
∗
equally likely in the second fiducial model, where fNL
= 0. )

of fNL (k) chosen, as is clear from Figures 3.5 - 3.7 and Table 3.2. Nonetheless, large
galaxy redshift surveys planned for the future may well be competitive with, or even
better than, the constraints on the magnitude and running of fNL (k) expected from
Planck.

CHAPTER IV

Constraints on the running of local-type non-Gaussianity
from WMAP 7-year data

4.1

Introduction

As mentioned elsewhere in this work (e.g. equation 1.10), a common parametrization of fNL (k) is a simple power law:
∗
fNL (k) = fNL

(4.1)



k
kpiv

nf

NL

Despite the relative popularity of this model, nobody has ever placed actual constraints on nfNL , nor any other form of running of non-Gaussianity with scale. In
this chapter, we use CMB data – specifically, the seven-year data set from the Wilkinson Microwave Anisotropy Probe (WMAP7) – to place the first-ever constraints on
nfNL , the running of local-type non-Gaussianity.
4.2

Estimating nfNL

In order to extract information about primordial non-Gaussianity from actual
CMB data, we need to have an unbiased estimator. Estimators relate the observable
quantities on the CMB sky (pixels) to theoretical parameters of interest (e.g. fNL ).
Unfortunately, it is difficult (if not actually impossible) to construct an estimator for
nfNL directly. Instead, we have adopted an alternative procedure.

36

37

We start with a fast cubic estimator for fNL due to Komatsu, Smith, and Wandelt
∗
(Komatsu et al. (2005)) and modified it to get an estimator for fNL
. (The details

of the KSW estimator and our modification of it are in Appendix D.) We used this
∗
modified estimator to construct the likelihood as a function of both fNL
and nfNL .
∗
Then we marginalized over fNL
to get the likelihood as a function of nfNL alone,

which in turn gave us an estimate of nfNL .
∗
To find the likelihood, we first find a χ2 statistic for fNL
, given a value of nfNL .

The χ2 statistic for a set of observables Oi is defined as:

2
theory
obs
X Oi − Oi
(4.2)
χ2 ≡
2
σtheory,i
i
Taking the angular-averaged bispectrum B`1 `2 `3 as our observables, and defining
B`theory
(nfNL ) as the theoretical expectation for the angular-averaged bispectrum in
1 `2 `3
∗
the case where fNL
= 1, we have:

2
theory
obs
∗
B
−
f
B
(n
)
X
fNL
NL `1 `2 `3
`1 `2 `3
∗
χ2 (fNL
, nfNL ) =
C̃`1 C̃`2 C̃`3
`1 `2 `3

2
2
theory
theory
obs
obs
∗
∗
B
B
B
B
−
2f
(n
)
+
f
(n
)
X
fNL
fNL
NL `1 `2 `3 `1 `2 `3
NL `1 `2 `3
`1 `2 `3
=
(4.3)
.
C̃`1 C̃`2 C̃`3
`1 `2 `3
∗
(This works because the theoretical expectation for B`1 `2 `3 ∝ fNL
.)

Using the skewness parameter S(nfNL ) from the KSW estimator (equation (D.24)),
∗
and taking advantage of the definition of the Fisher matrix F (nfNL ) for fNL
(equation

(D.25)), we can rewrite χ2 as:
"
X
∗
(4.4)
χ2 (fNL
, nfNL ) =

B`obs
1 `2 `3

2 #

C̃`1 C̃`2 C̃`3
`1 `2 `3

∗ 2
∗
) F (nfNL ).
− 2fNL
S(nfNL ) + (fNL

We can simplify this expression by introducing the following definition:

X B`obs` ` 2
1 2 3
(4.5)
χ20 =
.
C̃
C̃
C̃
`
`
`
1
2
3
`1 `2 `3

38
∗
= 0 case,
χ20 is the goodness-of-fit parameter for the data with respect to the fNL

hence the notation. Note that the numerator of χ20 is an observed quantity, and the
denominator is based solely on the theoretical prediction for the power spectrum (as
well as a few noise and beam parameters of WMAP). Therefore, χ20 does not depend
∗
on fNL
or nfNL at all.

Now we can rewrite χ2 as:
(4.6)

∗
∗
∗ 2
χ2 (fNL
, nfNL ) = χ20 − 2fNL
S + (fNL
) F.

Completing the square, we find:
(4.7)

∗
χ (fNL
, nfNL ) = F
2


2
S
S2
∗
fNL −
+ χ20 − .
F
F

Finally, we can take advantage of the definition of the modified KSW estimator itself,
∗
(nfNL ) ≡ S/F (equation (D.26)):
fˆNL

(4.8)

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
) F.

∗
∗
∗
:
= fˆNL
when fNL
χ2 is minimized in fNL

(4.9)

∗ 2
χ2min (nfNL ) = χ20 − (fˆNL
) F.

Figure 4.1 is a plot of χ2min − χ20 as a function of nfNL .
∗
We don’t have to settle for minimizing χ2 over fNL
, though. We can actually find
∗
∗
an expression for the likelihood, L(fNL
, nfNL ), and marginalize over fNL
to find the

likelihood as a function of nfNL alone. We can get the likelihood from χ2 :
(4.10)

∗
L(nfNL , fNL
) ∝ exp

 2
2
∗ −fˆ∗
ˆ∗ 2
F (fNL
χ2
χ
0 −(fNL ) F
NL )
2
2
−
= e−
e−
2

∗
Figure 4.2 is a contour plot of this likelihood in the nfNL - fNL
plane, and figure 4.3
∗
is a three-dimensional plot of L(nfNL , fNL
).

39

0
1

2 −χ 2
χmin
0

2
3

4
5
66

4

2

0

nfNL

4

2

6

8

Figure 4.1: χ2min − χ20 as a function of nfNL .

200
∗
f̂NL

150

98%
95%

68%

fNL∗

100

50

0

50

2

0

2

nfNL

4

6

∗
Figure 4.2: A contour plot of the likelihood in the fNL
- nfNL plane.

40

0.0030
0.0025
0.0020
0.0015
0.0010
0.0005
0.0000
200
150
100

∗

f NL

50
0
50

0

2

2

nfNL

4

6

∗
Figure 4.3: A three-dimensional plot of the likelihood, L(fNL
, nfNL ).

∗
To marginalize over fNL
, we integrate the likelihood:

Z
L(nfNL ) =

(4.11)

ˆ∗ 2
χ2
1
0 −(fNL ) F
∗
∗
2
.
L(nfNL , fNL
) dfNL
∝ √ e−
F
χ2
0

Remembering that χ20 is constant, e− 2 merely contributes to the normalization, and
we are left with:
(4.12)

∗ )2 F
1 (fˆNL
L(nfNL ) ∝ √ e 2 .
F

4.3

Results and conclusions

4.3.1

WMAP7 constraints on nfNL

Figure 4.4 shows L as a function of nfNL for three different values of the pivot scale
kpiv . χ2 is independent of our choice for kpiv , but the likelihood itself is not, since F
2nf

is inversely proportional to kpiv NL . This is not especially surprising, since choosing
∗
a different pivot is equivalent to choosing a different effective prior in fNL
. The true

41

500

kpiv =0.0538 Mpc−1
kpiv =0.05 Mpc−1
kpiv =0.02 Mpc−1

400

L(nfNL)

300

200

100

0

6

4

2

0

nfNL

2

4

6

8

∗
as a function of nfNL for the true pivot, along
Figure 4.4: The likelihood marginalized over fNL
with two other pivots.

∗
pivot scale favored by the data is the value of kpiv for which the errors in fNL
are

uncorrelated with the errors in nfNL . We find this scale by using the likelihood to
∗
calculate the covariance matrix C between fNL
and nfNL :

(4.13)

Ci,j = h(pi − p̄i )(pj − p¯j )i.

With C in hand, we can find kpiv (Shandera et al. (2011)):
!
∗ ,n
CfNL
fNL
(4.14)
kpiv = k∗ exp − ∗
.
fNL CnfNL ,nfNL
∗
Here, k∗ is the pivot used when evaluating C; similarly, fNL
is the value used in C.
∗
Despite the fact that k∗ and fNL
show up in the expression, kpiv does not depend

on them – the same value of kpiv will come out of (4.14) no matter what values of
∗
WMAP7
k∗ and fNL
are used. We find that kpiv
≈ 0.0538 Mpc−1 ; this corresponds to the

likelihood shown by the bold blue line in Figure 4.4.

42

1000

800

fNL(k)

600

∗
fNL
= 20; nfNL = −0.25
∗
fNL
= 30; nfNL = 0
∗
fNL = 50; nfNL = 1
∗
fNL
= 30; nfNL = 1.5
∗
fNL = 70; nfNL = 1.9
∗
fNL
= 70; nfNL = 2.5
∗
fNL
= 60; nfNL = 4

400

200

0
10-4

10-3

10-2

−1

k (Mpc )

10-1

100

Figure 4.5: Several models of fNL (k) with high likelihood. All of the models shown here lie within
the 68% confidence region in Figure 4.2, and they all use the pivot favored by the data, kpiv = 0.0538
Mpc−1 .

The central value for nfNL is the value which maximizes the likelihood at the correct pivot, and the uncertainty comes from the width of the likelihood (our likelihood
is manifestly not Gaussian, so we can’t just use the uncertainty from C). Putting it
all together, we have the following estimate for nfNL from the WMAP7 data, with a
68% (95%) confidence interval:
+2.1(+4.2)

(4.15)
4.3.2

nfNL = 1.9−1.4(−2.1)
Conclusions

These constraints in nfNL , (4.15), are the first constraints on the scale-dependence
of any form of non-Gaussianity. They are, admittedly, somewhat loose constraints
– there are still a variety of power-law models for fNL (k) that the data do not rule
out (Figure 4.5). While the WMAP7 data are compatible with nfNL = 0, the shape

43

of the likelihood function does hint at a positive value for nfNL . We will learn more
about this hint soon with the Planck data, due out next year. For the fiducial
value fNL = 30 favored by the WMAP7 data, the forecasted Planck error on nfNL in
Table 3.2 is σnPlanck
= 0.29, indicating that Planck may be able to improve upon our
f
NL

WMAP7 constraints by nearly a full order of magnitude.

CHAPTER V

Summary and conclusions

Non-Gaussianity is a potentially powerful probe of inflationary physics in the
very early universe. Single-field inflationary models with interactions, along with
most multi-field models, generically produce scale-dependent non-Gaussianity. To
learn more about primordial non-Gaussianity, we must infer properties of the primordial perturbations from the anisotropies in the CMB and the large-scale structure
of the universe today, and we must look at higher-order correlation functions and
polyspectra in order to test any given model of non-Gaussianity.
The best constraints on the Gaussianity of the universe have, until recently, come
from the bispectrum of the CMB: WMAP has constrained fNL to roughly 30 ± 20
(Komatsu et al. (2011)). But Dalal et al. (2008) pointed out that a non-zero fNL
leads to a strongly scale-dependent dark matter halo bias, which can be detected in
the power spectrum of large-scale structure; this technique has since emerged as a
source of constraints already competitive with the CMB (Slosar et al. (2008)).
I have focused on an extension of the local model, Equation (1.6), in which the
usual local non-Gaussianity parameter fNL is promoted to a function of scale, fNL (k).
I have paid particular attention to a piecewise-constant parametrization of fNL (k)
i
into a set of constants fNL
, Equation (1.9), as well as a simple power-law model of

44

45

fNL (k), Equation (1.10).
i
In Chapter II, we used forecasted constraints on the individual parameters fNL

from an intermediate-future galaxy survey. We also projected constraints on the
power-law model of fNL (k). We calculated the principal components of fNL (k) to
i
find the best-measured linear combinations of fNL
. The sensitivity of the survey to

non-Gaussianity increases with increasing k, but restricting the survey information to
scales where linear perturbation theory is valid imposes a “sweet spot” in sensitivity
of k ∼ 0.1h Mpc−1 .
In Chapter III, we studied how well the generalized local model can be probed
with the combination of cosmic microwave background data and large-scale structure surveys. As in Chapter II, we started by forecasting errors on the individual
i
. We found the principal components and forecasted errors for the
parameters fNL

power-law form of fNL (k). We then propagated the errors from those parameters to
fNL (k) as a whole.
Constraints from the CMB and LSS should remain comparable if systematics are
properly controlled for – but systematics are arguably more difficult to control for
LSS surveys (witness the larger number of nuisance parameters and degeneracies in
the LSS Fisher matrix). Nonetheless, large galaxy redshift surveys planned for the
future may well be competitive with, or even better than, the constraints on the
magnitude and running of fNL (k) expected from Planck.
In Chapter IV, we used the WMAP7 data to obtain the first constraints on the
scale-dependence of non-Gaussianity of any form. The WMAP7 data are compatible
with nfNL = 0 : nfNL = 1.9+2.1
−1.4 . The Planck data, due out next year, should be able
to improve on these constraints enough to tell us whether the slight hint of a positive
nfNL is significant.

46

We are entering a very exciting era in cosmology; in the next few years, data
may finally be good enough to start placing serious constraints on entire classes of
inflationary models via primordial non-Gaussianity. Planck and the next generation
of large-scale structure surveys will be able to constrain the non-Gaussianity of the
universe down to one part in 105 . Non-Gaussianity, if we do find it, will give us new
insight into the physics at work in the first fraction of a second after the Big Bang.

APPENDICES

47

48

APPENDIX A

Finding the derivative of the halo bias with respect to fNL
i
and the fNL

If we denote the full bias of dark matter halos by b + ∆b, where b represents the
bias for the Gaussian fluctuations and ∆b is the non-Gaussian correction, then

2
Ph
∆b
2
(A.1)
=b 1+
,
PR
b
where Ph and PR are the power spectra of halos and dark matter, respectively. The
non-Gaussian correction to the linear peak bias to the leading order becomes
Z
∆b
ν
1
d3 q
(A.2)
(k) =
BR (k, q, |k − q|),
b
σR 2PR (k)
(2π)3
where BR is the matter bispectrum on scale R. Hence, the non-Gaussian correction
∆b(k) can be expressed in terms of the primordial potential fluctuations as (Matarrese and Verde (2008)):
∆b
δc
1
(A.3)
(k) =
2
2
b
D(z) 8π σR MR (k)

Z ∞
0

dk1 k12 MR (k1 )

Z 1
dµMR (k2 )
−1

Bφ (k1 , k2 , k)
.
Pφ (k)

We perform the integration over all triangles. The triangles’ sides are k1 , k2 , and k;
the cosine of the angle opposite k2 is µ, so k22 = k12 + k 2 + 2k1 kµ. MR (k) is the same
function defined in Eq. (2.2), and the redshift dependence of the critical threshold
for collapse is given as δc (z) = δc /D(z), with δc = 1.686.
Portions of this appendix first appeared in:
Becker, A., Huterer, D., Kadota, K., Scale-dependent non-Gaussianity as a generalization of the local model, Journal
of Cosmology and Astroparticle Physics, 2011, vol. 1, p. 006, doi:10.1088/1475-7516/2011/01/006

49

A.1

Constant fNL

Eq. (A.3) leads to the famous scale-dependent bias formula in the case of a constant fNL . For this model, the bispectrum is
(A.4)

Bφ (k1 , k2 , k3 ) = 2fNL [Pφ (k1 )Pφ (k2 ) + perm.].

Through Eq. (A.3), this leads to the result
∆b
δc
2fNL
(k) =
b
D(z) 8π 2 σR2 MR (k)
(A.5)

≡

Z

dk1 k12 MR (k1 )Pφ (k1 )

Z



Pφ (k2 )
+2
dµMR (k2 )
Pφ (k)



2fNL δc F(k)
,
D(z) MR (k)

where
(A.6)

1
F(k) ≡ 2 2
8π σR

Z

dk1 k12 MR (k1 )Pφ (k1 )

Z


Pφ (k2 )
+2 .
dµMR (k2 )
Pφ (k)


Note that there is a factor of 2 in Eq. (A.5) because we can exchange the order of
integration of terms corresponding to k1 and k2 .
Finally, we rewrite Eq. (A.5) by defining
(A.7)
(A.8)

Z
Z
1
2
F1 (k) ≡ 2 2
dk1 k1 MR (k1 )Pφ (k1 ) dµMR (k2 )Pφ (k2 );
8π σR MR (k)Pφ (k)
Z
Z
2
2
F2 (k) ≡ 2 2
dk1 k1 MR (k1 )Pφ (k1 ) dµMR (k2 ).
8π σR MR (k)

Then, for constant fNL ,
(A.9)

∆b
2fNL δc
(k) =
[F1 (k) + F2 (k)] ,
b
D(z)

and the derivative with respect to fNL is
(A.10)



∂
∆b
2δc
(k) =
[F1 (k) + F2 (k)] .
∂fNL b
D(z)

50

A.2

Scale-dependent fNL

Now we repeat the analysis of the previous section, but we allow fNL (k) to be
an arbitrary function of scale, adopting the ansatz in Eq. (1.6). We still assume
homogeneity, so fNL (~k) = fNL (k). The bispectrum is given by
(A.11)

Bφ (k1 , k2 , k3 ) = 2[fNL (k1 )Pφ (k2 )Pφ (k3 ) + perm.].

Here, the triangle condition always holds, so that (for example) k1 = |k~2 + k~3 |.
Following Eq. (A.3), we get

(A.12)

Z
∆b
δc
2
(k) =
dk1 k12 MR (k1 )Pφ (k1 )
b
D(z) 8π 2 σR2 MR (k)


Z
Pφ (k2 )
+ 2fNL (k2 ) .
×
dµMR (k2 ) fNL (k)
Pφ (k)

This looks like Eq. (A.5) – but this time, fNL (k) is a function, not a constant.
Thus, to find the derivative of ∆b/b(k) with respect to the relevant parameters, we
must parametrize fNL (k) in a way that is valid for any general form of fNL (k). We
consider the piecewise-constant (in wavenumber) parametrization where fNL (k) is
i
equal to fNL
in the ith wavenumber bin:
i
fNL
≡ fNL (ki ).

(A.13)

i
The derivative of ∆b/b(k) with respect to these fNL
is:


∆b
∂
δc
2
(ki ) =
×
j
2
2
D(z) 8π σR MR (k)
∂fNL b

Z
Z
1
2
(A.14)
δij
dk1 k1 MR (k1 )Pφ (k1 ) dµMR (k2 )Pφ (k2 )+
Pφ (k)
#
Z
Z
+2
dk1 k12 MR (k1 )Pφ (k1 ) dµMR (k2 ) ,
k2 ∈kj

where δij is the Kronecker delta function. Note that the last integral over k2 only
goes over the jth wavenumber bin.

51

This derivative can be rewritten more concisely as



∂
2δc 
∆b
(ki ) =
δij F1 (k) + F2j (k) .
j
D(z)
∂fNL b

(A.15)

The functions F1 and F2 are defined as in Eqs. (A.7) and (A.8), except that the
superscript in F2j indicates that the integral over k2 is to be executed only over the
jth wavenumber bin.
A.2.1

The Desjacques et al. term

The new term in the bias, pointed out by Desjacques et al. (2011), is the second
term of (2.7):
N (k) ≡

(A.16)

d ln F (k)
.
d ln σR

This is not a particularly computationally friendly form. We can make it more
tractable by using the chain rule:
σR dF
N (k) =
F (k) dM

(A.17)



dσR
dM

−1
.

i
, for our Fisher
Now we need to take the derivative of N with respect to the fNL

matrix.
−1


dσR
∂
1 dF
i
dM
∂fNL
F (k) dM

−1




σR dσR
∂
d
∂F
1 dF ∂F
=
−
.
i
i
i
F dM
∂fNL
dM ∂fNL
F dM ∂fNL

∂N
= σR
i
∂fNL
(A.18)



Equations (A.17) and (A.18) are everything we need to properly account for the
R
new term in our Fisher matrix. Note that σR and dσ
are the only z-dependent
dM

quantities in N ; since their z-dependence is linear and exactly the same, it cancels
entirely, leaving N independent of z.

52

Projected error on fNL from LSS survey

8
7

6
5

4
3
210

5

0

Fiducial value of fNL

5

10

Figure A.1: How the choice of fiducial fNL affects the forecasted constraints on constant fNL from
a future galaxy survey. See text for analytic explanation for why results are the best at a fiducial
value of fNL = 0.

A.3

The effect of the fiducial value on constraints

The fiducial value of fNL affects the Fisher matrix – and thus the forecasted
constraints on fNL itself – because the relationship between Ph (k) and fNL is nonlinear.

The fiducial fNL enters the Fisher matrix through the bias, by way of

Ph = (b2 (k))P (k). Assuming Ph (k)  1/n (a reasonable assumption at large angular
scales where non-Gaussianity constraints largely come from and where shot noise is
negligible), we find that the Fisher matrix element corresponding to fNL = const is
(A.19)

F

LSS

Z 
∝

∂b(k)
∂fNL

2

−2

b (k)dk =

Z 

∆b(k)
fNL (b0 + ∆b(k))

2
dk.

53

Thus, the expression on the right-hand side will, in general, be dependent on the
choice of fiducial fNL . Since |∆b(k)| blows up at small k, in that regime we have:

(A.20)

∆b(k)
fNL (b0 + ∆b(k))

2
≈

1
2
fNL

.

At large k, ∆b(k) goes to 0, taking the entire expression with it. Thus, the integral
is dominated by the contribution at low k, meaning we should expect a maximal
Fisher matrix element around a fiducial fNL = 0. And indeed, that is what we see
in Figure A.1: the forecasted constraints on fNL from a given sky survey depend on
the fiducial value chosen, with the tightest constraints at fNL = 0.

54

APPENDIX B

Statistical methods: Fisher matrices, principal components,
and all that.

B.1

Fisher information matrices: a brief introduction.

Fisher matrices are powerful tools for forecasting the constraints placed on a set
of parameters from an expected future data set. It is a purely analytic method; no
likelihood evaluation or parameter search of any kind is required. This makes it a
particularly fast and convenient method for error forecasting. In this subsection, I
will give a brief overview of the derivation and application of Fisher matrices in the
abstract. More details about how I performed specific Fisher matrix calculations are
provided in Chapters II and III.
B.1.1

Bayes’s theorem, likelihood, and the Fisher information matrix

Any reasonable interpretation of probability admits the following truth about
conditional probabilities:
(B.1)

P (A|B) =

P (AB)
P (B)

In other words, the probability of A given B is equal to the probability of both A
and B divided by the probability of B. Given B.1 and some other basic axioms of
Portions of this appendix first appeared in:
Becker, A., Huterer, D., Kadota, K., Scale-dependent non-Gaussianity as a generalization of the local model, Journal
of Cosmology and Astroparticle Physics, 2011, vol. 1, p. 006, doi:10.1088/1475-7516/2011/01/006

55

probability, we have the following chain of reasoning concerning the probability of a
hypothesis H and some data D:
P (H|D) = P (HD)/P (D)
P (D|H) = P (DH)/P (H)
P (H|D)P (D) = P (HD) = P (DH) = P (D|H)P (H)
(B.2)

∴ P (H|D) = P (D|H)P (H)/P (D)

This is Bayes’s theorem.

The probability of the hypothesis given the data,

P (H|D), is equal to the probability of the data given the hypothesis, P (D|H), multiplied by the probability of the hypothesis, P (H), divided by the probability of the
R
data, P (D). P (H) is known as the prior probability; P (D) = P (D|H 0 )P (H 0 )dH 0 is
the probability of the data marginalized over all hypotheses, and is therefore called
the marginal probability; P (H|D) is the posterior probability; finally, P (D|H), the
probability of observing the data given the truth of the the hypothesis, is known as
the likelihood. Bayes theorem, then, can be restated:
posterior probability = likelihood ×

prior probability
marginal probability

The marginal probability depends only on the data (and the chosen hypothesis
space), not on H itself; thus, it can be viewed as an overall normalization factor. For
a likelihood function sharply peaked in hypothesis space, it (nearly) doesn’t matter what method you’re using to assign priors to your hypotheses – the likelihood
function will pick out a narrow band of hypotheses so long as we have sufficiently
informative data.
But how do we quantify the notion of “sufficiently informative” for our data? Our
data is sufficiently informative if the models in our model space are sensitive to the

56

parameters our data tell us about. We already know that our models are sensitive
to the parameters we’re measuring if the likelihood function for those parameters
is sharply peaked in our model space. So we can quantify how useful our data will
be for distinguishing among different models in terms of the peak curvature of the
likelihood function – and we measure a function’s curvature by taking its second
derivative. Thus, we arrive at the Fisher information matrix, often just called the
Fisher matrix:

(B.3)

Fij =

∂ 2 ln L
−
∂pi ∂pj



Here, L is the likelihood, and the pi are the parameters of interest in the model (e.g.
any cosmological parameters). The Fisher matrix gives us a quantitative measure
of how well a data set can choose among available models – and thus, how much
information a data set can contain about the parameters that determine our models.
The brackets hi indicate an expectation value taken over realizations of the data;
this enables us to find an analytic expression for the Fisher matrix. We assume
that the data are distributed according to a multivariate Gaussian; in that case, the
covariance matrix of the data C has all the information about the distribution of the
data:
(B.4)



1
1
−1
T
L=
exp − (d − ¯
d)i Cij (d − ¯
d)j ,
(2π)n/2 | det C|1/2
2

where di are the data (with d¯i the mean for each i) and Cij is the covariance of the
data. After some tedious but straightforward algebra, (B.3) and (B.4) combine to
give an expression for the Fisher matrix:
(B.5)

1
Fij = Tr[C −1 C,i C −1 C,j ] + d¯,iT C −1 d¯,j
2

where ,i is the partial derivative with respect to pi .

57

In most cases, d¯,i and C will depend on the values chosen for the parameters pi ; in
order to calculate the Fisher matrix Fij , one must first choose fiducial values for these
parameters. So the Fisher matrix can be used to forecast constraints on the errors in
the pi – as we are about to see – but it obviously cannot give any information about
the most likely values for the pi themselves.
B.1.2

Using Fisher matrices to estimate parameter errors

The most straightforward way to use Fisher matrices in error forecasting is through
the Cramér-Rao bound, which states that an error in a cosmological parameter pi
will be greater than or equal to the corresponding Fisher matrix element:

(B.6)

σ(pi ) ≥


p


−1

 (F )ii (marginalized error)
√



 1/ Fii

(unmarginalized error)

Here, the marginalized error is the error in pi marginalized over the uncertainties in
all the other parameters in the Fisher matrix F , while the unmarginalized error is the
error in pi while holding all the other parameters perfectly fixed. The marginalized
errors are generally the quantities of interest, since we are usually trying to determine
the values of several parameters at once from the same set of data. Cramér-Rao only
gives us a lower bound on the marginalized error – but in practice, we assume that the
data will saturate the bound, allowing us to effectively forecast the best achievable
errors for a given set of observations using Fisher matrices.
B.2

Calculating the error on an arbitrary parametrized fNL (k)

i
Projecting the constraints from an old set of parameters fNL
≡ fNL (ki ) (i =

1, 2, . . . , N ) to new parameters (which we can call q; j = 1, 2, . . . , M for some M )
is in principle straightforward. The Fisher matrix in the new parameters, F new , is

58

given by
(B.7)

new
Fi,j
=

N
X
∂pk ∂pl

∂q i ∂q j
k,l=1

Fkl

so that
F new ≡ P T F P,

(B.8)

where Pij = ∂pi /∂q j is the derivative matrix of old parameters with respect to new.
Let us look at a couple of examples. Projecting to the case
(B.9)

fNL (k) = fNL = const

i
/dfNL = 1. Then
is particularly easy, since P is the column vector with Pi1 = dfNL

Fijnew is a 1 × 1 matrix that quantifies information on fNL , given by
new
F11
=

(B.10)

X

Fkl .

k,l

p new
The error on fNL is of course given simply by σ(fNL ) = 1/ F11
.
Another example is given by the function

(B.11)

fNL (k) =

k
k0

nNG
,

with two parameters, k0 and nNG . Then one can show that (labeling k0 ≡ q1 and
nNG ≡ q2 ):
(B.12)

Pi1

(B.13)

Pi2

 n
nNG ki NG
= −
;
k0
k0
   nNG
ki
ki
= ln
.
k0
k0

Then, using Eq. (B.8), one can simply obtain the 2 × 2 Fisher matrix in k0 and nNG .

59

B.3

Principal components of fNL (k)

We now show how to decompose the measurement of fNL (k) in principal components, which are essentially the eigenmodes of the covariance matrix for the aforementioned parameters fNL (ki ). This method has been widely used in cosmology,
including applications to parametrizing and describing dark energy (Huterer and
Starkman (2003); Albrecht et al. (2009)). It allows us to order the best-to-worst
measured weights in wavenumber of the function fNL (k).
Let the function fNL (k) be described in terms of piecewise constant parameters
i
fNL
≡ fNL (ki ), where

(B.14)

fNL (k) =

N
X

pi Θi (k).

i=1



Here, Θ(k) ≡ H(k − kilower ) − H(k − kiupper ) is the top-hat function of unit height
over the ith wavenumber bin, and we assume a total of N bins. kilower and kiupper
are the wavenumber bin boundaries, and H is the Heaviside step function. We have
effectively expanded the function around the zero value, though this is not crucial:
fid
fid
the left-hand side could be fNL (k)−fNL
(k), for any fiducial fNL
(k), and the formalism

still follows.
The Fisher matrix F is the inverse covariance matrix in the original piecewiseconstant parameters pi , so that Fij−1 = hpi pj i − hpi ihpj i. We first diagonalize the
Fisher matrix F :
(B.15)

F = W T DW,

where D is diagonal and W is some orthogonal matrix. The vector of uncorrelated
parameters, q, is related to the vector of original parameters p via
(B.16)

q = W p,

60

and it is easy to check that the q are uncorrelated; that is, hq qT i = D−1 . The rows
of W are therefore the new parameters.
Thus, to calculate the principal components:
1. Obtain the full Fisher matrix for N parameters pi , plus the cosmological parameters Ωb h2 , ΩCDM h2 , H0 , w, log As , and ns .
2. Marginalize over the cosmological parameters by inverting this larger Fisher
matrix, taking the N × N submatrix, then inverting back to get the Fisher
matrix of the pi ; we call this Fisher matrix F
3. Diagonalize F as in Eq. (B.15)
4. The rows of W are the principal components. More precisely, qa =

P

i Wai pi ,

and qa are the PCs.
Let us now change notation slightly (to agree with the commonly used one, e.g. Huterer
and Starkman (2003)), and define the shape of the a-th principal component in i-th
(a)

(a)

redshift bin as αi , so that αi

≡ Wai . Then we can represent the a-th principal

component, e(a) (k), in terms of the original parameters pi as1
(a)

(B.17)

e (k) =

N
X

(a)

αi pi Θi (k).

i=1

The PCs are obviously uncorrelated, and their eigenvalues λa , so that
(B.18)

(a) (b)

he e i ≡

N
X

(a)

(b)

αi αj hpi pj i =

i,j=1

δab
.
λa

where, recall, λa ≡ Daa .
Finally, let us calculate the coefficients c(a) in the expansion in principal components of an arbitrary fNL (k)
(B.19)

fNL (k) =

N
X

ca e(a) (k).

a=1
1 This is basically the continuous version of the relation q =
a

P

i Wai pi .

61
i
Let coefficients fNL
describe fNL (k) in our original basis, so that fNL (k) = const ≡
P i
i
i fNL pi Θi (k), with fNL being left arbitrary for now. Then, taking the expectation

value of the product with e(b) , we get
* N
!
X
c
b
i
(B.20)
=
fNL
pi ×
hfNL (k)e(b) i ≡
λb
i=1
(B.21)

=

N
X

N
X

!+
(a)

α j pj

j=1

(a)

i
fNL
αj (F −1 )ij ,

i,j=1

so that
(B.22)

ca = λ a

N
X

(a)

i
fNL
αj (F −1 )ij .

i,j=1
i
For example, in the simplest case of constant fNL (k), where fNL
= const ≡ fNL , the

coefficients of the principal components in the expansion of fNL (k) are
(B.23)

ca = λa fNL

X
ij

(a)

αj (F −1 )ij

(for fNL (k) ≡ fNL = const).

62

APPENDIX C

Calculating the CMB bispectrum Fisher matrix for
local-type non-Gaussianity

C.1

Calculating the CMB bispectrum

The non-averaged bispectrum is:
B`1 `2 `3 ,m1 m2 m3 = ha`1 m1 a`2 m2 a`3 m3 i

(C.1)

where the alm s are the coefficients on the spherical harmonic decomposition of the
CMB sky. The alm s can be related to the Bardeen curvature perturbations Φ(k) by:
Z
(C.2)

a`m =

∆T (k̂) ∗
Y`m (k̂) = 4π(−i)`
d k̂
T
2

Z

d3 k
∗
Φ(k)g` (k)Y`m
(k̂)
(2π)3

Here, g` (k) is the CMB temperature radiation transfer function. There are several
conventions used for this transfer function; g` (k) is related to the transfer function
T` (k) found in (Gibelyou et al. (2010)) by:
(C.3)

(−i)`
g` (k) = p
T` (k)
2`(` + 1)

We will be using yet another convention, as both of the transfer functions above
lead to messy prefactors later on. Throughout this paper, we denote the radiation
transfer functions as t` (k), defined as:
(C.4)

t` (k) =

1
1
g` (k) = p
T` (k)
`
(−i)
2`(` + 1)

63

With these transfer functions, (C.2) becomes:
4π

`

Z

(−1)
a`m = p
2`(` + 1)

(C.5)

d3 k
∗
Φ(k)t` (k)Y`m
(k̂)
3
(2π)

One last word on transfer function conventions: these transfer functions connect
the CMB sky to the Bardeen curvature perturbations, not the primordial curvature
perturbations.
The angular-averaged bispectrum B`1 `2 `3 is related to the raw bispectrum B`1 `2 `3 ,m1 ,m2 ,m3
of (C.1) by the relation:
(C.6)



X

B`1 `2 `3 =

m1 ,m2 ,m3

Here,

`1 `2 `3
m1 m2 m3




`1 `2 `3
B`1 `2 `3 ,m1 ,m2 ,m3
m1 m2 m3

is the Wigner 3j-symbol. This symbol ensures that `1 + `2 + `3 is

even, m1 + m2 + m3 = 0, and the triangle inequality (|`i − `j | ≤ `k ≤ `i + `j ) is
met for all i, j, k.1 Substituting (C.1) and (C.5) into (C.6), we obtain the following
expression for the angular-averaged bispectrum:
3

`1 +`2 +`3

B`1 `2 `3 = (4π) (−1)

X
m1 ,m2 ,m3

(C.7)



`1 `2 `3
m1 m2 m3

Z

d3 k1 d3 k2 d3 k3
(2π)3 (2π)3 (2π)3

×Y`∗1 m1 (kˆ1 )Y`∗2 m2 (kˆ2 )Y`∗3 m3 (kˆ3 )t`1 (k1 )t`2 (k2 )t`3 (k3 )hΦ(k1 )Φ(k2 )Φ(k3 )i

Using the definition of the Bardeen curvature bispectrum, BΦ ,
(C.8)

hΦ(k1 )Φ(k2 )Φ(k3 )i = (2π)3 δ(k1 + k2 + k3 )BΦ (k1 , k2 , k3 ),

we find:

Z
`1 `2 `3
1 X
d3 k1 d3 k2 d3 k3 Y`∗1 m1 (kˆ1 )Y`∗2 m2 (kˆ2 )Y`∗3 m3 (kˆ3 )
B`1 `2 `3 = 3
π m ,m ,m m1 m2 m3
1

(C.9)

2

3

×t`1 (k1 )t`2 (k2 )t`3 (k3 )δ(k1 + k2 + k3 )BΦ (k1 , k2 , k3 ).

1 There are some computational difficulties that arise when evaluating the 3j-symbol for high l
1,2,3 ; see Appendix
C.3.2 for more on this.

64

(The prefactor of (−1)`1 +`2 +`3 vanished because the Wigner 3j-symbol ensures `1 +
`2 + `3 is even.) Taking advantage of several identities in Wang and Kamionkowski
(2000) (their (12) and (13)), the orthogonality of the spherical harmonics, and the
Gaunt integral identity (Komatsu and Spergel (2001)), this becomes:
 3
Z
2
B`1 `2 `3 =
I`1 `2 `3 k12 dk1 k22 dk2 k32 dk3 BΦ (k1 , k2 , k3 )t`1 (k1 )t`2 (k2 )t`3 (k3 )
π
Z ∞
(C.10)
r2 dr j`1 (k1 r)j`2 (k2 r)j`3 (k3 r),
×
0

where I`1 `2 `3 is the Gaunt integral
r
(C.11)

I`1 `2 `3 =



(2`1 + 1)(2`2 + 1)(2`3 + 1) `1 `2 `3
.
4π
000

The real-space integral is now a one-dimensional integral in the spherical coordinate
r, starting at our location and ending at infinity. This real-space coordinate is
Rt
the difference in the conformal time ∆η = te0 dta = c(τ0 − τe ) between the time
when the CMB was emitted and the time when we saw it. Equivalently, it is the
difference between the radius of the particle horizon of the observable universe when
the CMB was observed and that radius when the CMB was first emitted. Thus,
nearly all of the contribution to the integral in r comes from a short period of time
around the surface of last scattering, and there are no physical contributions beyond
r > rmax = η0 = cτ0 ≈ 14.6 Gpc. For our purposes, when performing this integral in
Chapter III, we sampled the integral 150 times between rmax and rmax − 2r∗ , where
rmax − r∗ is the comoving distance to the surface of last scattering. We also sampled
50 times between rmax − 2r∗ and 0 to capture any impact that late-time effects might
have had. Increasing the sampling rate did not significantly improve our results.

65

C.1.1

Bispectrum and derivatives for fNL and fNL (k)

Using (C.10) along with (3.4), we get the following expression for the angularaveraged CMB bispectrum in the constant fNL case:
!
 3
Z
1
2
B`1 `2 `3 = 2∆2φ fNL
I`1 `2 `3 k12 dk1 k22 dk2 k32 dk3
+ perm.
3−(n −1) 3−(n −1)
π
k1 s k2 s
Z ∞
(C.12)
× t`1 (k1 )t`2 (k2 )t`3 (k3 )
r2 dr j`1 (k1 r)j`2 (k2 r)j`3 (k3 r)
0

Following equations 33 and 34 from Yadav and Wandelt (2010) (where they are
themselves following Komatsu and Spergel (2001), equations 17 and 18), we’ll define a
pair of functions, α` (r) and β` (r), to help us rewrite (C.12) in a more computationally
friendly way.

Z
2
k 2 t` (k)j` (kr)dk
α` (r) ≡
π
Z
2
β` (r) ≡
k −(2−ns ) t` (k)j` (kr)dk
π

(C.13)
(C.14)

Now (C.12) looks like this:
(C.15)

B`1 `2 `3 = 2∆2φ fNL I`1 `2 `3

Z ∞

r2 dr (α`1 (r)β`2 (r)β`3 (r) + perm.)

0

and (naturally)
1
∂B`1 `2 `3
=
B` ` ` .
∂fNL
fNL 1 2 3

(C.16)

For the scale-dependent fNL (k) case, we use (3.6) to find that the angular-averaged
CMB bispectrum is:
(C.17)

∂B`1 `2 `3
= 2∆2φ I`1 `2 `3
i
∂fNL

Z ∞

r2 dr α`i 1 (r)β`2 (r)β`3 (r) + perm.

0

where α`i is:
(C.18)

2
α`i (r) ≡

π

Z kiupper
kilower

k 2 t` (k)j` (kr)dk.



66

Polarization and cross-terms

The bispectrum for multiple fields is a simple extension of the single field case.
By analogy with (C.1) and (C.2), the multiple-field bispectrum is
(C.19)

= hap`1 m1 aq`2 m2 ar`3 m3 i,
B`pqr
1 `2 `3 ,m1 m2 m3

where
(C.20)

ap`m = p

4π

2`(` + 1)

`

(−1)

Z

d3 k
∗
Φ(k)tp` (k)Y`m
(k̂)
(2π)3

and ti` (k) is either the temperature or polarization radiation transfer function. Using
these definitions and running through equations (C.7) through (C.17) again, it’s
pretty clear that we can rewrite the bispectrum for multiple fields very easily if we
just change (C.13), (C.14), and (C.18) slightly:
(C.21)
(C.22)
(C.23)

2
α`p (r) ≡

Z

k 2 tp` (k)j` (kr)dk;
π
Z
2
p
k −(2−ns ) tp` (k)j` (kr)dk;
β` (r) ≡
π
Z upper
2 ki
p,i
k 2 tp` (k)j` (kr)dk.
α` (r) ≡
π kilower

So for the constant fNL case, we have
(C.24)

∂B`pqr
1 `2 `3
= 2∆2φ I`1 `2 `3
∂fNL

Z ∞
0

r2 dr α`p1 (r)β`q2 (r)β`r3 (r) + perm.



while for the piecewise-constant fNL (k) case, we have:
(C.25)
C.2

∂B`pqr
1 `2 `3
= 2∆2φ I`1 `2 `3
i
∂fNL

Z ∞
0

(r)β`q2 (r)β`r3 (r) + perm.
r2 dr α`p,i
1



The covariance of the bispectrum

It is usually a good assumption to consider only the Gaussian contribution to the
covariance of the bispectrum, C. Using Wick’s theorem, one can straightforwardly

67

show (Liguori et al. (2010); Babich and Zaldarriaga (2004); Spergel and Goldberg
(1999)):
(C.26)

C`1 `2 `3 = C`1 C`2 C`3

where
(C.27)

C` = C`CV + σ`2 W` = C`CV + C`N

C`CV is cosmic variance, while C`N is the variance due to the noise and beam width
in the survey. σ`2 is the variance of the noise in the survey per pixel, and W` is a
“window” term relating to the survey beam type and width (Cooray and Hu (2000);
Knox (1995)).2 For an experiment with multiple frequency channels (such as Planck
or WMAP), the basic form of equation (C.27) still holds, but finding C`N is slightly
trickier (Cooray and Hu (2000)):
(C.28)

X
X 1
1
1
=
=
.
2
N
N
σ
(ν)W
(ν)
C`
C
(ν)
`
`
`
ν
ν

For uncorrelated Gaussian noise, σ`2 (ν) = σ 2 (ν) is constant, and you can find its
value for a particular experiment fairly easily; for example, the Planck beam width
and noise parameters are found in the Planck mission “blue book.”
We have only been dealing with temperature (TT), but it is not significantly
harder to add in polarization (EE) and cross (TE) terms. The covariance matrix
here is (Yadav et al. (2007); Babich and Zaldarriaga (2004))

(C.29)

−1
−1
−1
(C−1
`1 `2 `3 )lmn,pqr = (C`1 )lp (C`2 )mq (C`3 )nr ,

where

(C.30)

TT
 C`

C` = 

C`T E



C`T E 
C`EE

.

2 Confusingly, Cooray and Hu (2000) uses w −1 for what we are calling σ 2 .

68

Noise is dealt with in the same way as in (C.27) for C`T T and C`EE in (C.30). Assuming
that the noise for T and E are uncorrelated, σT2 E = h∆T ∆Ei = h∆T ih∆Ei = 0, and
thus C`N,T E = 0 for all `.
C.3

Computational details

C.3.1

` sampling and binning

In evaluating equation (3.7), we do not actually use every ` ≤ `max ; that would be
incredibly computationally expensive. Instead, we sample and bin in `. The binning
in ` is progressive, not fixed-width: all `s are kept up through ` = 40, at which point
sampling drops off gradually until, at ` & 100, only every tenth ` is sampled. The
“width” of the bins in ` are given by the equation
(C.31)
C.3.2

∆`i =

1
1
[(`i − `i−1 ) + (`i+1 − `i )] = (`i+1 − `i−1 ).
2
2

Calculating the Wigner 3j-symbol

We need to be able to calculate the Wigner 3j-symbol for large (> 1000) values of `1,2,3 in order to evaluate many of the expressions we’re interested in. Unfortunately, the 3j function built in to the GNU Scientific Library can’t properly
evaluate the symbol for `1,2,3 & 70. Thus, we were forced to create our own specialpurpose 3j-evaluator. Thankfully, we’re only interested in the special case m1,2,3 = 0;
as it turns out, in this case, the 3j-symbol reduces to (see Wolfram Mathworld:
http://mathworld.wolfram.com/Wigner3j-Symbol.html):
(C.32)


`1 `2 `3
000


=


q


g!

2 )!(2g−2`3 )!
(−1)g (2g−2`1 )!(2g−2`
(2g+1)!
(g−` )!(g−` )!(g−` )!

if L = 2g;




0

if L = 2g + 1,

1

2

3

where L = `1 +`2 +`3 . Since (C.32) involves evaluating the factorials of relatively large
numbers when any of `1,2,3 are large, we used Stirling’s approximation to perform the

69

factorials – but we needed the factorials to remain accurate even when the arguments
were small, so we used six terms in the approximation.

70

APPENDIX D

The KSW estimator and the modified KSW estimator

D.1

The KSW estimator

Komatsu et al. (2005) found a fast cubic estimator for fNL based on a full-sky
CMB temperature map; Yadav et al. (2007) and Yadav et al. (2008) extended that
estimator to deal with polarization, sky cuts, and inhomogeneous noise. I will refer
to this estimator as the KSW estimator for convenience’s sake.
We start by recalling from Appendix C several useful definitions and equations
relating the primordial curvature bispectrum to that of the CMB. The angularaveraged CMB bispectrum B`1 `2 `3 is related to the shape function of the primordial
curvature bispectrum FΦ through the equation
 3
Z
2
theory
B`1 `2 `3 =
I`1 `2 `3 (k1 k2 k3 )2 dk1 dk2 dk3 FΦ (k1 , k2 , k3 ) t`1 (k1 ) t`2 (k2 ) t`3 (k3 )
π
Z ∞
(D.1)
×
r2 dr j`1 (k1 r)j`2 (k2 r)j`3 (k3 r),
0

where I`1 `2 `3 is the Gaunt integral
r


(2`1 + 1)(2`2 + 1)(2`3 + 1) `1 `2 `3
.
(D.2)
I`1 `2 `3 =
4π
000
We can reduce this to a considerably simpler form in the case of local non-Gaussianity
(i.e. when FΦ = FΦlocal ; see equation (1.5)) :
Z ∞
theory
(D.3)
B`1 `2 `3 (fNL ) = 2fNL I`1 `2 `3
r2 dr (α`1 (r)β`2 (r)β`3 (r) + perm.)
0

71

where α` (r) and β` (r) are defined (using a slightly different convention from Appendix
C, to play nicely with the output from CAMB) as
(D.4)
(D.5)

Z
2
α` (r) ≡
k 2 t` (k)j` (kr)dk
π
Z
2
β` (r) ≡
k 2 PΦ (k)t` (k)j` (kr)dk
π

Given a set of spherical harmonic coefficients a`m for the CMB sky, we can define
a set of “filtered” maps, A and B:
(D.6)

A(n̂, r) ≡

X

α` (r)

b`
a`m Y`m (n̂);
C̃`

β` (r)

b`
a`m Y`m (n̂),
C̃`

`,m

(D.7)

B(n̂, r) ≡

X
`,m

where C̃` = b2` C` + N` is the power spectrum corrected for beam width and noise.
Komatsu et al. (2005) construct a skewness parameter S from these filtered maps:
Z
(D.8)

S≡

2

Z

r dr

d2 n̂A(n̂, r)B 2 (n̂, r)

Equation (D.8) is the computationally friendly form of the skewness parameter, and
we can skip straight to (D.15) if we just want to calculate a full-sky estimator for
fNL . But to see how it leads us to that estimator, we have to do a little more work.
Keeping in mind that the observed CMB bispectrum is defined as
(D.9)

B`obs.
= ha`1 m1 a`2 m2 a`3 m3 i,
1 `2 `3

it is not hard to see that S reduces to
(D.10)

S=

X

B`obs
B̃`theory
(fNL = 1)
1 `2 `3
1 `2 `3

`1 ≤`2 ≤`3

C̃`1 C̃`2 C̃`3

where
(D.11)

B̃`theory
(fNL ) = b`1 b`2 b`3 B`theory
(fNL ).
1 `2 `3
1 `2 `3

72

to B̃ theory , we find (Komatsu et al. (2005)):
Performing a least-squares fit of B`obs
1 `2 `3
X

2
(f
=
1)
B̃`theory
NL
1 `2 `3

`1 ≤`2 ≤`3

C̃`1 C̃`2 C̃`3


S ≈ fNL

(D.12)

is proportional to fNL . Therefore,
/∂fNL , because B`theory
(fNL = 1) = ∂ B̃`theory
B̃`theory
1 `2 `3
1 `2 `3
1 `2 `3
we can write the Fisher matrix F for fNL as (see (3.5)):

(D.13)

F =

X

∂ B̃`theory
1 `2 `3

!2

∂fNL

`1 ≤`2 ≤`3


1
=
C̃`1 C̃`2 C̃`3
`1 ≤`2 ≤`3
X

2
B̃`theory
(f
=
1)
NL
1 `2 `3
C̃`1 C̃`2 C̃`3

.

This, in turn, means we can rewrite (D.12) as
S ∼ fNL F.

(D.14)
Thus, the KSW estimator for fNL is:

S
fˆNL ≡
F

(D.15)

While this estimator works well for a full-sky map, it breaks down for a cut-sky
map. To get around this, an extra term is introduced into the estimator (Yadav
et al. (2008)) to account for the spurious signal introduced by the sky cut:
1

Scut
f
fˆNL =
= sky
F

(D.16)

S + Slinear
F

.

Slinear is:
Slinear = −
(D.17)

1
fsky

Z

2

r dr

Z


2
d2 n̂ A(n̂, r)hBsim
(n̂, r)iM C

+2B(n̂, r)hAsim (n̂, r)Bsim (n̂, r)iM C ] .

The subscripted filtered maps Asim and Bsim are generated from Monte Carlo realizations of the cut CMB sky; the brackets hiM C indicate an average over all Monte
Carlo maps. The Monte Carlo maps were produced using the prescription laid out

73

in Appendix A of the WMAP5 paper (Komatsu et al. (2009)); the only difference
(aside from our use of the WMAP7 data) is that we used a uniform weighting for
the maps, rather than the slightly more complicated weighting given there, since it
only results in a marginal improvement of the estimation of fNL . We created the
Monte Carlo maps in Python; we plugged these Monte-Python maps into HEALPix,
by way of HealPy, to do the forwards and backwards spherical harmonic transforms
required to obtain the A and B maps.
D.2

Modifying the KSW estimator for a power-law fNL (k)

It is fairly simple to modify the KSW estimator for the case of a power-law fNL (k)
of the form
∗
fNL (k) = fNL

(D.18)



k
kpiv

nf

NL

.

∗
We want an estimator for the parameter fNL
. Note that the pivot scale, kpiv , is
∗
; the choice of pivot scale is largely arbitrary, and
completely degenerate with fNL

in fact we will see that kpiv cancels entirely from some (but not all!) quantities of
interest.
To get our new estimator, start with the shape function for the bispectrum associated with this fNL (k):
∗
fNL
nf
(D.19) FΦ = 2(fNL (k1 )P (k2 )P (k3 ) + perm.) = 2 nfNL (k1 NL P (k2 )P (k3 ) + perm.).
kpiv

Plugging (D.19) into (D.1), and deploying the usual tricks, we get:
(D.20)

∗
∗
(fNL
, nfNL ) = 2fNL
I`1 `2 `3
B`theory
1 `2 `3

Z ∞

r2 dr (γ`1 (nfNL , r)β`2 (r)β`3 (r) + perm.) .

0

Here, γ` (nfNL , r) takes the role of α` (r), and is similarly defined:
(D.21)

2 1
γ` (nfNL , r) ≡
nfNL
π kpiv

Z

k 2+nfNL t` (k)j` (kr)dk.

74

We can use γ` (r) to write down a new filtered map G(n̂, r),
G(nfNL , n̂, r) ≡

(D.22)

X

γ` (nfNL , r)

`,m

b`
a`m Y`m (n̂),
C̃`

and we can use G(nfNL , n̂, r) to write down a new skewness parameter S(nfNL ).
Z
Z
2
(D.23)
S(nfNL ) ≡ r dr d2 n̂G(nfNL , n̂, r)B 2 (n̂, r)
In the case where nfNL = 0, γ` (nfNL , r) = α` (r) and S(nfNL ) trivially reduces to (D.8).
The same argument that takes us from (D.8) to (D.10) applies here too, so S(nfNL )
must reduce to
(D.24)

X



theory
∗
B`obs
B̃
=
1,
n
)
(f
fNL
NL
`1 `2 `3
1 `2 `3

`1 ≤`2 ≤`3

C̃`1 C̃`2 C̃`3

S(nfNL ) =

∗
at a given value of nfNL as:
We can write the Fisher matrix F (nfNL ) for fNL

(D.25)
X

F =

`1 ≤`2 ≤`3

∂ B̃`theory
(nfNL )
1 `2 `3
∗
∂fNL

!2


X
1
=
C̃`1 C̃`2 C̃`3
`1 ≤`2 ≤`3

2
∗
=
1)
B̃`theory
(n
,
f
fNL
NL
1 `2 `3
C̃`1 C̃`2 C̃`3

.

The least-squares fit (D.12) still holds, so we have the following unbiased estimator
∗
for fNL
:

S(nfNL )
∗
fˆNL
=
∗ (nf
FfNL
)
NL

(D.26)

To account for a sky cut, the same arguments used by Yadav et al. (2008) hold
∗
here, as we are still using a cubic estimator. Thus, our actual estimator for fNL
is
1

(D.27)

Scut (nfNL )
f
∗
fˆNL
=
= sky
F

S(nfNL ) + Slinear (nfNL )
F

,

∗
where F is the appropriately-modified Fisher matrix element for fNL
, and Slinear (nfNL )

is
Slinear (nfNL ) = −
(D.28)

1
fsky

Z

2

r dr

Z


2
d2 n̂ G(nfNL , n̂, r)hBsim
(n̂, r)iM C

+2B(n̂, r)hGsim (nfNL , n̂, r)Bsim (n̂, r)iM C ] .

75
∗
Now we have an estimator for fNL
– and more importantly, we have a skewness
∗
parameter for fNL
, which allows us to get the likelihood function for nfNL in Chapter

IV.

76

Bibliography
Afshordi, N. and Tolley, A. J. Primordial non-gaussianity, statistics of collapsed
objects, and the Integrated Sachs-Wolfe effect. Phys. Rev. D, 78:123507, 2008,
[arXiv:0806.1046].
Albrecht, A. and Steinhardt, P. J. Cosmology for grand unified theories with radiatively induced symmetry breaking. Phys. Rev. Letters, 48:1220–1223, 1982.
Albrecht, A. J. et al. Findings of the Joint Dark Energy Mission Figure of Merit
Science Working Group. 2009, [arXiv:0901.0721].
Babich, D., Creminelli, P. and Zaldarriaga, M. The shape of non-gaussianities.
JCAP, 08:009, 2004, [astro-ph/0405356].
Babich, D. and Zaldarriaga, M. Primordial Bispectrum Information from CMB
Polarization. Phys. Rev. D, 70(8):083005, 2004, [astro-ph/0408455].
Becker, A., Huterer, D. and Kadota, K. Scale-dependent non-Gaussianity as a generalization of the local model. JCAP, 1:6, 2011, [arXiv:1009.4189].
Byrnes, C. T., Gerstenlauer, M., Nurmi, S., Tasinato, G. and Wands, D. Scaledependent non-Gaussianity probes inflationary physics.

JCAP, 10:004, 2010,

[arXiv:1007.4277].
Chen, X. Running Non-Gaussianities in DBI Inflation. Phys. Rev., D 72:123518,
2005, [astro-ph/0507053].
Cooray, A. R. and Hu, W. Imprint of reionization on the cosmic microwave background bispectrum. ApJ, 534:533–550, 2000, [astro-ph/9910397].

77

Creminelli, P. and Zaldarriaga, M. Single field consistency relation for the 3-point
function. JCAP, 0410:006, 2004, [astro-ph/0407059].
Cunha, C., Huterer, D. and Doré, O. Primordial non-gaussianity from the covariance
of galaxy cluster counts. Phys. Rev. D, 82(2):023004, 2010, [arXiv:1003.2416].
Dalal, N., Dore, O., Huterer, D. and Shirokov, A. The imprints of primordial nongaussianities on large- scale structure: scale dependent bias and abundance of
virialized objects. Phys. Rev. D, 77:123514, 2008, [arXiv:0710.4560].
Desjacques, V., Jeong, D. and Schmidt, F. Accurate predictions for the scaledependent galaxy bias from primordial non-gaussianity. Phys. Rev. D, 84:061301,
2011, [arXiv:1105.3476].
Desjacques, V. and Seljak, U. Signature of primordial non-Gaussianity of φ3 -type in
the mass function and bias of dark matter haloes. Phys. Rev. D, 81:023006, 2010,
[arXiv:0907.2257].
Desjacques, V., Seljak, U. and Iliev, I. T. Scale-dependent bias induced by local
non-Gaussianity: a comparison to N-body simulations. MNRAS, 396:85–96, 2009,
[arXiv:0811.2748].
Elsner, F. and Wandelt, B. D. Improved Simulation of Non-Gaussian Temperature
and Polarization Cosmic Microwave Background Maps. ApJS, 184:264–270, 2009,
[arXiv:0909.0009].
Feldman, H. A., Kaiser, N. and Peacock, J. A. Power spectrum analysis of threedimensional redshift surveys. ApJ, 426:23–37, 1994, [astro-ph/9304022].
Gibelyou, C., Huterer, D. and Fang, W.

Detectability of large-scale power

78

suppression in the galaxy distribution.

Phys. Rev. D, 82(12):123009, 2010,

[arXiv:1007.0757].
Grinstein, B. and Wise, M. B. Nongaussian Fluctuations and the Correlations of
Galaxies or Rich Clusters of Galaxies. ApJ, 310:19–22, 1986.
Guth, A. H. Inflationary universe: A possible solution to the horizon and flatness
problems. Phys. Rev. D, 23:347–356, 1981.
Huterer, D. and Starkman, G.

Parameterization of dark-energy proper-

ties: A principal- component approach.

Phys. Rev. Lett., 90:031301, 2003,

[astro-ph/0207517].
Knox, L. Determination of inflationary observables by cosmic microwave background
anisotropy experiments. Phys. Rev. D, 52:4307, 1995, [astro-ph/9504054].
Komatsu, E. and Spergel, D. N. Acoustic signatures in the primary microwave background bispectrum. Phys. Rev. D, 63(6):063002, 2001, [arXiv:astro-ph/0005036].
Komatsu, E., Spergel, D. N. and Wandelt, B. D.

Measuring Primordial Non-

Gaussianity in the Cosmic Microwave Background.

ApJ, 634:14–19, 2005,

[astro-ph/0305189].
Komatsu,

E. et al.

Five-Year Wilkinson Microwave Anisotropy Probe

(WMAP) Observations:Cosmological Interpretation. ApJS, 180:330–376, 2009,
[arXiv:0803.0547].
Komatsu, E. et al. Seven-year Wilkinson Microwave Anisotropy Probe (WMAP) Observations: Cosmological Interpretation. ApJS, 192:18, 2011, [arXiv:1001.4538].
Liguori, M., Sefusatti, E., Fergusson, J. R. and Shellard, E. P. S.

Primordial

Non-Gaussianity and Bispectrum Measurements in the Cosmic Microwave Back-

79

ground and Large-Scale Structure. Advances in Astronomy, 2010:980523, 2010,
[arXiv:1001.4707].
Linde, A. D. Chaotic inflation. Physics Letters B, 129:177–181, 1983.
Linde, A. D. and Mukhanov, V. F. Nongaussian isocurvature perturbations from
inflation. Phys. Rev. D, 56:535–539, 1997, [astro-ph/9610219].
LoVerde, M., Miller, A., Shandera, S. and Verde, L. Effects of Scale-Dependent NonGaussianity on Cosmological Structures. JCAP, 04:014, 2008, [arXiv:0711.4126].
Luo, X.-c. and Schramm, D. N. Testing for the gaussian nature of cosmological
density perturbations through the three-point temperature correlation function.
Phys. Rev. Lett., 71:1124–1127, 1993, [astro-ph/9305009].
Lyth, D. H. and Wands, D. Generating the curvature perturbation without an
inflaton. Phys. Lett., B 524:5–14, 2002, [hep-ph/0110002].
Maldacena, J. Non-gaussian features of primordial fluctuations in single field inflationary models. JHEP, 5:13, 2003, [astro-ph/0210603].
Matarrese, S., Lucchin, F. and Bonometto, S. A. A path-integral approach to largescale matter distribution originated by non-Gaussian fluctuations. ApJ, 310:L21–
L26, 1986.
Matarrese, S. and Verde, L. The effect of primordial non-Gaussianity on halo bias.
ApJ, 677:L77, 2008, [arXiv:0801.4826].
McDonald, P. Primordial non-Gaussianity: large-scale structure signature in the
perturbative bias model. Phys. Rev. D, 78:123519, 2008, [arXiv:0806.1061].
Salopek, D. and Bond, J. Nonlinear evolution of long wavelength metric fluctuations
in inflationary models. Phys. Rev. D, 42:3936–3962, 1990.

80

Sefusatti, E., Liguori, M., Yadav, A. P. S., Jackson, M. G. and Pajer, E. Constraining
running non-gaussianity. JCAP, 12:22, 2009, [arXiv:0906.0232].
Seo, H. and Eisenstein, D. J. Probing Dark Energy with Baryonic Acoustic Oscillations from Future Large Galaxy Redshift Surveys. ApJ, 598:720–740, 2003,
[astro-ph/0307460].
Shandera, S., Dalal, N. and Huterer, D. A generalized local ansatz and its effect on
halo bias. JCAP, 1103:017, 2011, [arXiv:1010.3722].
Sheth, R. K. and Tormen, G. Large-scale bias and the peak background split. MNRAS, 308:119–126, 1999, [astro-ph/9901122].
Slosar, A., Hirata, C., Seljak, U., Ho, S. and Padmanabhan, N. Constraints on
local primordial non-Gaussianity from large scale structure. JCAP, 08:031, 2008,
[arXiv:0805.3580].
Spergel, D. N. and Goldberg, D. M. Microwave background bispectrum. I. Basic
formalism. Phys. Rev. D, 59:103001, 1999, [astro-ph/9811252].
Tegmark, M. Measuring cosmological parameters with galaxy surveys. Phys. Rev.
Lett., 79(20):3806–3809, 1997, [astro-ph/9706198].
Verde, L. and Matarrese, S. Detectability of the effect of Inflationary non- Gaussianity on halo bias. ApJ, 706:L91–L95, 2009, [arXiv:0909.3224].
Wang, L.-M. and Kamionkowski, M. The cosmic microwave background bispectrum
and inflation. Phys. Rev. D, 61:063504, 2000, [astro-ph/9907431].
Yadav, A. P., Komatsu, E. and Wandelt, B. D. Fast Estimator of Primordial NonGaussianity from Temperature and Polarization Anisotropies in the Cosmic Microwave Background. ApJ, 664:680, 2007, [astro-ph/0701921].

81

Yadav, A. P. S., Komatsu, E., Wandelt, B. D., Liguori, M., Hansen, F. K. and
Matarrese, S. Fast Estimator of Primordial Non-Gaussianity from Temperature
and Polarization Anisotropies in the Cosmic Microwave Background. II. Partial Sky
Coverage and Inhomogeneous Noise. ApJ, 678(2):578, 2008, [arXiv:0711.4933].
Yadav, A. P. S. and Wandelt, B. D.
Cosmic Microwave Background.

Primordial Non-Gaussianity in the

Advances in Astronomy, 2010:565248, 2010,

[arXiv:1006.0275].
Zaldarriaga, M. Non-Gaussianities in models with a varying inflaton decay rate.
Phys. Rev. D, 69:043508, 2004, [astro-ph/0306006].
