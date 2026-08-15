---
title: "A User-Friendly Dark Energy Model Generator"
person: adam-becker
section: by
type: preprint
year: 2015
date: 2015-06-16
venue: "arXiv (Cornell University)"
authors: "Kyle A. Hinton, Adam Becker, Dragan Huterer"
source_url: https://doi.org/10.48550/arxiv.1506.05088
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W1515926064; full text from arXiv preprint https://arxiv.org/abs/1506.05088 (pdftotext); may differ from published version. oa_status=green; cited_by=0."
---

# A User-Friendly Dark Energy Model Generator

## Full text

### Abstract (from OpenAlex metadata)

We provide software with a graphical user interface to calculate the phenomenology of a wide class of dark energy models featuring multiple scalar fields. The user chooses a subclass of models and, if desired, initial conditions, or else a range of initial parameters for Monte Carlo. The code calculates the energy density of components in the universe, the equation of state of dark energy, and the linear growth of density perturbations, all as a function of redshift and scale factor. The output also includes an approximate conversion into the average equation of state, as well as the common $(w_0, w_a)$ parametrization. The code is available here: http://github.com/kahinton/Dark-Energy-UI-and-MC

### Full text (arXiv preprint version, pdftotext extraction)

A User-Friendly Dark Energy Model Generator
Kyle A. Hinton,1, ∗ Adam Becker,2, † and Dragan Huterer1, 3, 4, ‡
1

arXiv:1506.05088v2 [astro-ph.CO] 9 Jul 2015

Department of Physics, University of Michigan, 450 Church St, Ann Arbor, MI 48109-1040
2
Freelance, Oakland, CA 94610
3
Max-Planck-Institut for Astrophysics, Karl-Schwarzschild-Str. 1, 85741 Garching, Germany
4
Excellence Cluster Universe, Technische Universität München, Boltzmannstrasse 2, 85748 Garching, Germany
We provide software with a graphical user interface to calculate the phenomenology of a wide class
of dark energy models featuring multiple scalar fields and potentials that are arbitrary functions
of exponentials. The user chooses a subclass of models and, if desired, initial conditions, or else a
range of initial parameters for Monte Carlo. The code calculates the energy density of components
in the universe, the equation of state of dark energy, and the linear growth of density perturbations,
all as a function of redshift and scale factor. The output also includes an approximate conversion
into the average equation of state, as well as the common (w0 , wa ) parametrization. The code is
available here: http://github.com/kahinton/Dark-Energy-UI-and-MC

I.

INTRODUCTION

The puzzle of dark energy is one of the most important
outstanding questions in all of physics. Studying the observational signatures of dark energy – and using those
signatures to understand the nature of dark energy – has
been a highly active area of research since the first signs
of dark energy were discovered over 15 years ago. (For a
review, see e.g. Frieman et al. [1].) Dark energy models
have a rich phenomenology, leaving varied fingerprints
on the growth of cosmic structure and on geometrical
quantities in the universe.
We have written a piece of software that makes it
easier to compute quantitative predictions for dark energy models broader than a simple cosmological constant.
These models possess a richer phenomenology that can
be tested with ongoing and future experiments. They
also complement the choice of dark energy models – and
computer code – made by others [2]. Our software is
capable of handling a wide class of models with multiple scalar fields, and specifically makes two subclasses
particularly easy to calculate with a simple user input.
In these models, the user can calculate the expansion
history and the growth of structure in the linear regime,
therefore enabling the user to obtain various implications
for observable quantities in cosmology. The code also returns an approximate conversion of the equation of state
of dark energy w(a) into two commonly used parameters
(w0 , wa ), as well as several other commonly used parameters.
II.

jikawa [3], and originally developed by Refs. [4, 5]. The
starting assumption is the existence of n scalar fields, and
a Lagrangian density that takes the following form
Lfields =

n
X

Xi g(Xi eλi φi )

(1)

i=1

where Xi ≡ −g µν ∂µ φi ∂ν φi /2 is the kinetic term for i-th
field, and g(Y ) is an arbitrary function of its argument
Y ≡ X eλφ , where λ is a dimensionless parameter. The
existence of scaling solutions dictates that this be the
most general form of the Lagrangian density for exponential potentials [4, 5]. A noteworthy special case of our
class of models is quintessence with a single field (n = 1),
and a simple exponential potential V (φ) = c exp(λφ), for
which g(Y ) = 1 − c/Y . As we explain below, this class
of models also includes ghost condensate models [6] featuring a background scalar field which, despite having a
kinetic term of the “wrong” sign, are stable and feasible
due to suitable higher-order kinetic terms.
Our code allows a user to test models with an arbitrary

DARK ENERGY MODELS

We choose two classes of “assisted dark energy” models, based specifically on the analysis by Ohashi and Tsu-

∗ kahinton@umich.edu
† adam@freelanceastro.com
‡ huterer@umich.edu

FIG. 1. Sample screenshot of the software, showing text inputs for dark energy model parameters, as well as checkboxes
for selecting the desired plots.

2

FIG. 2. Example plots generated by our program, showing output for a single model for our quintessence (left panel) or ghost
condensate (right panel) class of models. The user can choose to plot this for any arbitrary choice of model parameters, as a
function of either scale factor a or redshift z.

function g(Y ), for an arbitrary number of fields n. As an
example we also provide two special cases which have
been run through the Monte Carlo generator, and whose
results can be accessed with very simple inputs in the
graphical user interface (GUI):
g(Yi ) = 1 − ci /Yi

(quintessence)

(2)

g(Yi ) = −1 + ci Yi

(ghost condensate).

(3)

In each case, the temporal evolution of all quantities is
most easily tracked in terms of scaled variables
√
ρr
φ̇i
e−λi φi /2
xi ≡ √
; yi ≡ √
; u≡ √
(4)
6H
3H
3H
where ρr is the radiation energy density. The evolution
equations, expressed in terms of the time variable N ≡
ln(a), are [3]
"
#
n
X
√
xi
dxi
2
2
=
3+3
xi g(Yi ) + u − 6λi xi
dN
2
i=1
√
h
i
√
6
A(Yi ) λi Ωφi − 6{g(Yi ) + Yi g 0 (Yi )}xi ,
+
2
"
#
n
X
√
yi
dyi
2
2
=
3+3
xi g(Yi ) + u − 6λi xi ,
(5)
dN
2
i=1
"
#
n
X
du
u
2
2
=
−1 + 3
xi g(Yi ) + u .
dN
2
i=1

(6)

We numerically evolve these equations. Then all physical quantities of interest can be found, for example the
energy densities of matter and dark energy
ΩDE =

n
X

x2i [g(Yi ) + 2Yi g 0 (Yi )]

(7)

i=1

and the dark energy equation of state
Pn
Pn
2
pφ
i=1 xi g(Yi )
wDE ≡ Pni=1 i = Pn
2
0
i=1 ρφi
i=1 xi [g(Yi ) + 2Yi g (Yi )]

(8)

where the time-dependent parameter Yi can be calculated via Yi = x2i /yi2 . Note that for quintessence, the
functional form of g(Yi ) in Eq. (2) implies that the potential isP
the sum of exponential potentials for each field,
V (φ) = i ci exp(λi φi ).

III.

USING THE PROVIDED SOFTWARE

Our code can be found at the following
GitHub repository:
http://github.com/kahinton/
Dark-Energy-UI-and-MC. The code gives the user
several tools for testing and analyzing various models
of dark energy. The first step in being able to use
these tools is to run a model through our Monte Carlo
generator. The user must supply several inputs to the
MC generator: a specific function g(Y ), as described
above; a name to differentiate the model from others;
and the number of different initial conditions to test the
model over. The provided name will be used to label
this model in the user interface. The user must also
specify the values for several parameters governing each
model. Specifically these parameters are the number
of fields that will be acting as dark energy, n, as well
as the range for the initial conditions of xi , yi , ci , and
u. In our code we adopt a simplification suggested in
[3], which assumes that a single field will act to assist
inflation in the early universe before becoming small,
while the remaining fields will be small in the early
universe before becoming the dominant form of energy
at late times. The “assisted inflation” field will have
one set of unique initial conditions, while the remaining
n − 1 fields will all share the same initial conditions.
This later simplification drives the value of wDE as close
to −1 as possible at late times, and also allows models to
be tested at the same speed independent of the number
of fields being used.
By using these simplifications the user only needs to
specify the range of initial conditions for the first two
fields. The code then assumes, for example, that all values of x2 to xn are equal. To ensure that a scalar field

3

FIG. 3. Left panel: the first two principal components used to convert from w(z) to wave and (w0 , wa ); note that wave requires
only the first principal component. The components are based on the NASA/DOE Figure of Merit Science Working Group
analysis [7]; see Appendix for details. Right panel: a sample scatterplot made from the user interface. Here one can see the
results of w0 and wa for 10,000 pre-supplied ghost condensate models, case with 15 fields.

dominated solution is produced, the values for λi are
chosen automatically, according to the inequalities (see
Eqs. (29) and (32) in [3])
λ21
> 88.9;
p,X

λ22−n
< 2,
p,X

(9)

Here p is the Lagrangian density, and p,X ≡ ∂p/∂X.
When the code is run, for each specific test, the initial
conditions for each parameter are chosen from a random
flat distribution over the selected range. When all of
the tests have finished running the model will be added
to the user interface automatically. As an example of
what is output to the user interface, we have included
the results of tests of quintessence and ghost condensate
models having 5, 10, 15, and 20 fields.
The user interface also contains two optional tools.
The first of these allows the user to run a single instance
of any model having been run through the Monte Carlo
generator. Each of the required parameters are assigned
a set of fiducial values that depend on which model is chosen; however, the range over which the model has been
tested is also supplied, allowing the user to experiment
with values other than those provided. Once the user selects values for these parameters, they can choose to plot
various quantities as a function of either scale factor a or
redshift z. These quantities include:
• Energy densities in units of critical (radiation
ΩR (a), matter ΩM (a), dark energy ΩDE (a));
• Equation of state of dark energy w(a);
• Linear growth of density fluctuations D(a) (we plot
the quantity D(a)/a).
In order to provide the growth of linear perturbations,
concurrently with the other equations we also evolve
D00 +D0 (H 0 /H +2)−3/2(H0 /H)2 ΩM (1+z)3 D = 0 (10)

where D(a) ≡ (δρ/ρ)/(δρ/ρ)a=1 is the linear growth rate
of matter perturbations, and where the primes indicate
a derivative with respect to ln(a). The quantity D/a
for the selected model will immediately be displayed on
screen for the user to examine.
The second option available to the user is to examine
the results from the Monte Carlo generator. Specifically,
this tool allows the user to generate two-dimensional scatterplots on the fly for further analysis – for example,
to see what range of phenomenological outcomes is produced by a given model or class or models. Each point in
a given scatterplot corresponds to an output of a single
model. The output can be any of the following parameters or functions:
• Initial conditions from each model including x1 , x2 ,
y1 , y2 , c1 , c2 , λ1 , λ2 , u, and n;
• Energy densities in matter and dark energy today
ΩM and ΩDE , as well as the equation of state today
wDE (a = 1).
• Effective “average” equation of state wave , calculated from the first principal component, as described in the Appendix.
• Effective values for the parameters w0 and wa based
on parametrization [8] w(a) = w0 + wa (1 − a), derived from the first two principal components as
described in the Appendix.
An example of the Monte Carlo output showing the w0 −
wa plane is shown in the right panel of Fig. 3.
ACKNOWLEDGMENTS

We thank Eric Linder for useful comments. Our work
has been supported by NSF under contract AST-0807564
and DOE under contract DE-FG02-95ER40899.

4
Appendix: Principal components, wave , and (w0 , wa )

Here we explain in more detail how to calculate the
aforementioned quantities w0 , wa , and wp from the principal components of the equation of state, following
[9, 10]. First, we formally expand the equation of state
in terms of principal components
X
1 + w(a) =
αi ei (a),
(11)
i

where αi is the coefficient of the i-th principal component
ei (a). The idea is to convert the first principal component α1 into the averaged value of the equation of state
wave , and first two principal components (α1 , α2 ) into
(w0 , wa ). This approach is justified because the first few
principal components carry essentially all the necessary
information about the effects of dark energy dynamics on
the expansion of the universe on observable scales.
The principal components ei can be determined for any
given dataset; here we use the Figure of Merit Science
Working Group’s (FoMSWG) publicly available code [7],
and a combination of Planck+BAO+SN+WL available
in their code. Note that, while the component shapes
— especially the all-important peak value of e1 (a) that
shows the temporal epoch of maximum sensitivity to the
equation of state — depend on the cosmological probe as
well as specifications of a given experiment, once we combine the probes the pull of different probes is expected
to average out, leading to a fixed set of shapes.
While the normalization of the ei (a) is arbitrary in
principle, the FoMSWG
R principal components that we
use are normalized as e2i (a)da = 1. The coefficients αi
can be obtained as
Z
αi = [1 + w(a)] ei (a) da
(12)

The final step is converting the first principal component into wave , and the first two into w0 and wa ; we do
this via [10]
1 + wave =

α1
β1

(average w)

(13)

and
1 + w0 ≡

α1 (γ2 − β2 ) + α2 (β1 − γ1 )
β1 γ 2 − β2 γ 1

(14)

α1 β2 − α2 β1
wa ≡
β1 γ2 − β2 γ1
where αi are defined in Eq. (12), and
Z
βi ≡

Z
ei (a) da;

γi ≡

a ei (a) da

(15)

where w(a) is the actual equation of state of the theoretical dark energy model we are studying.

Equations (13) and (14) are now our definitions of the
parameters wave and (w0 , wa ), respectively, given a dark
energy history w(z) which determines the αi . Previous
work [10] confirms that the two-parameter equation of
state closely follows the true w(z) over the redshift range
most effectively probed by the data.
Note too that the constraint w0 ≥ −1, which follows
from w(z) ≥ −1, is not strictly obeyed by w0 obtained in
this way since w0 and wa are now essentially a fit to the
dark energy equation of state history. In other words,
the derived parameter w0 can be slightly smaller than
−1; this is again because we are fitting these three wparameters and forcing them to the model’s actual equation of state evolution. These parameters are nevertheless provided since 1) they provide a very useful test bed
to gauge the effectiveness of the range of dark energy
model behavior, and 2) they are fairly representative of
these models, since actual dark energy models often do
exhibit the w0 + wa (1 − a) scaling.

[1] J. Frieman,
M. Turner,
and D. Huterer,
Ann.Rev.Astron.Astrophys.
46,
385
(2008),
arXiv:0803.0982 [astro-ph].
[2] D. J. Marsh, P. Bull, P. G. Ferreira, and A. Pontzen,
Phys.Rev. D90, 105023 (2014), arXiv:1406.2301 [astroph.CO].
[3] J. Ohashi and S. Tsujikawa, Phys.Rev. D80, 103513
(2009), arXiv:0909.3924 [gr-qc].
[4] F. Piazza and S. Tsujikawa, JCAP 0407, 004 (2004),
arXiv:hep-th/0405054 [hep-th].
[5] S. Tsujikawa and M. Sami, Phys.Lett. B603, 113 (2004),
arXiv:hep-th/0409212 [hep-th].

[6] N. Arkani-Hamed, H.-C. Cheng, M. A. Luty, and
S. Mukohyama, JHEP 0405, 074 (2004), arXiv:hepth/0312099 [hep-th].
[7] A. Albrecht, L. Amendola, G. Bernstein, D. Clowe,
D. Eisenstein, et al., (2009), arXiv:0901.0721 [astroph.IM].
[8] E. V. Linder, Phys.Rev.Lett. 90, 091301 (2003),
arXiv:astro-ph/0208512 [astro-ph].
[9] D. Huterer and G. Starkman, Phys.Rev.Lett. 90, 031301
(2003), arXiv:astro-ph/0207517 [astro-ph].
[10] D. Huterer and H. V. Peiris, Phys.Rev. D75, 083503
(2007), arXiv:astro-ph/0610427 [astro-ph].
