---
title: "Nonequilibrium phase transitions in biomolecular signal transduction"
person: david-krakauer
section: by
type: journal-article
year: 2011
date: 2011-11-23
venue: "Physical Review E"
authors: "David C. Krakauer et al."
source_url: https://doi.org/10.1103/physreve.84.051917
retrieved: 2026-08-13
content: full-text
notes: "OA status: green; OpenAlex W1992134603; cited_by 9. Abstract reconstructed from OpenAlex abstract_inverted_index. Full text recovered 2026-08-14 by the upgrade pass from best_oa_location.pdf_url (97,942 chars); OpenAlex has no stored content for this work."
---

# Nonequilibrium phase transitions in biomolecular signal transduction

## Full text

Non-equilibrium phase transitions in biomolecular signal transduction
Eric Smith(1) , Supriya Krishnamurthy(1,2,3), Walter Fontana (1,4) and David Krakauer(1)

arXiv:1108.4121v2 [q-bio.SC] 30 Aug 2011

(1):Santa Fe Institute, 1399 Hyde Park Road, Santa Fe, NM 87501, USA
(2): Department of Physics, Stockholm University, SE- 106 91, Stockholm, Sweden
(3): School of Computer Science and Communication, KTH, SE- 100 44 Stockholm, Sweden
(4): Department of Systems Biology, Harvard Medical School,
200 Longwood Avenue, Bostom MA 02115, USA
(Dated: November 6, 2018)
We study a mechanism for reliable switching in biomolecular signal-transduction cascades. Steady
bistable states are created by system-size cooperative effects in populations of proteins, in spite of
the fact that the phosphorylation-state transitions of any molecule, by means of which the switch is
implemented, are highly stochastic. The emergence of switching is a nonequilibrium phase transition
in an energetically driven, dissipative system described by a master equation. We use operator and
functional integral methods from reaction-diffusion theory to solve for the phase structure, noise
spectrum, and escape trajectories and first-passage times of a class of minimal models of switches,
showing how all critical properties for switch behavior can be computed within a unified framework.

I.
A.

INTRODUCTION

The emergence of devices from biomolecular
systems

Two related questions define a fundamental role for
statistical physics in systems biology: (1). How do
biomolecular systems achieve reliable “device-level” behavior when they consist of highly stochastic componentry [1], in particular molecular complexes held together by low-energy hydrogen or Van der Waals bonds?
(2). Are such systems structured in a modular fashion [2], i.e. can complex molecular networks decompose into quasi-autonomous functional units performing
identifiable tasks which are robust against many physical
parameter changes and are recombinable in evolution?
The device logic of biomolecular systems employs
many of the same abstractions as electronic engineering [3], including amplification, filtering, and switching.
Switches (which use elements of amplification and filtering) are used wherever a discrete sequence of events is
required, enabling committed threshold response to environmental cues during development [4, 5], establishing
“checkpoints” for intermediate states, in processes like
cell division that require strict sequencing of events [6],
or programming the complex progressions of cell-type differentiation [2].
Two classes of biomolecular processes in which modular switching is widely recognized are gene expression and
signal transduction. In gene expression, the switch states
are associated with patterns of genes activated for protein
production, and a stochastic component is introduced in
the system by the small number of weakly-bound transcription factors [7]. In signal transduction, the states of
the switch are frequently determined by the number of
phosphate or methyl groups covalently attached to specific target amino acid residues on one or more dedicated
proteins [8]. Stochasticity in this system can again be
caused by the small number of proteins or the complexes
these proteins form with the catalysts which promote

attachment or detachment of the phosphate or methyl
groups. Gene expression changes cell type on slower
timescales (minutes to hours) than signal transduction
(seconds), but since many cell-type changes occur in response to external signals [4, 5], or rely on amplification
and stabilization of internal signals [6], switching behavior is often produced by both systems acting together.

In this paper we consider the problems of mechanism
for the emergence of robust switching in stochastic molecular systems, and of quantitative estimation of the noise
and stability properties of switches. We consider switching in signal transduction via the mechanism of phosphorylation (addition of phosphate groups via the action of
a kinase) and dephosphorylation (removal of phosphate
groups by the action of a phosphatase) since these are
a common motif found in most if not all signalling networks. In addition, the relative simplicity of phosphorylation transitions lends itself to the abstraction of many
real transduction cascades in terms of a few processes,
allowing us to isolate the problems of formation, control, and robustness of the switch. We observe that the
most fundamental unit in signal-transduction cascades is
a single type of target protein with multiple phosphorylation states (called phosphoepitopes), among which
transitions are naturally modeled as a reaction-diffusion
process. The network properties necessary for switching,
which may be distributed in real systems among several
proteins in a signal-transduction cascade, or between the
cascade and the genetic transcription factors for the target proteins, are readily lumped together and assigned to
a single species to produce minimal models. This coarsegraining reduces network complexity while still keeping
its essential regulatory features. We are able to write
down exact master equations for such ideal models, and
to solve them systematically with field-theoretic methods
from reaction-diffusion theory.

2
B.

INPUT
(E1)

Senses of “switching”, their uses, and how they
are achieved robustly

Switching in biomolecular systems, at the least, refers
to sigmoidal response to input signals, termed “ultrasensitivity” [9]. Such response implies a sharp sigmoidal but
continuous response in the concentration of a molecule
over a narrow range of a (stationary) signal. In contrast, bistability [10] is a form of switching made possible when two stable states, S1 and S2 , co-exist over
a signal range. As a consequence, bistable systems exhibit two distinct thresholds as the signal is varied, one
at which a transition occurs from S1 to S2 and another
at which the system switches back from S2 to S1 . The
separation of thresholds leads to path dependence or hysteresis, and makes a switched state more impervious to
stochastic fluctuations of the signal around the transition point, than in the ultrasensitive case. Hysteresis
may be obtained by adding positive feedback to sigmoidal response [11]. Weak hysteresis may be used to
stabilize input signals, equivalent to signal “debouncing”
in engineering, while strong hysteresis leads to bistability, toggling, and long-term memory [12, 13]. We will
look specifically at toggling, because this subsumes all
the other phenomena of interest.
The molecular mechanisms used repeatedly in signal
transduction for amplification, threshold sensitivity, and
switching, are shown in Fig. 1, as they are instantiated
in the Mitogen-Activated Protein Kinase (MAPK) family
of transduction cascades. This widely duplicated and diversified homologue family is used througout the eukaryote kingdom [14], mostly to regulate gene expression in
response to cell-membrane received signals. MAPK cascades employ three proteins, each with an unphosphorylated state, and respectively one, two, and two phosphorylated states. Phosphorylation and dephosphorylation
of each protein is catalyzed by exogenous kinases and
phosphatases, and in addition the fully-phosphorylated
states of the first two proteins act as kinases (phosphorylation catalysts) on the proteins following them in the
cascade. The cascade is thus an actively driven, dissipative system, maintained away from equilibrium by
the supply of activated (high-energy) phosphate donors.
When used for switching, MAPK cascades may have positive feedback from the output to the highest-level protein, either through gene expression or through inhibition
of degradation of the active state [9].
The structure of MAPK and other cascades was abstracted by Goldbeter and Koshland [8] to the minimal
system shown in Fig. 2, which they propose as the signaling counterpart to the transistor (a better analogy
would be to the bistable flip-flop, as they use it). A single
protein species has a single phosphorylation site. Phosphorylation and dephosphorylation occur via the action
of catalysts/enzymes with which the protein can form
enzyme-substrate complexes. Depending on the rate of
these reactions, the steady state fractions of the phosphorylated (or unphosphorylated) protein can vary abruptly

MAPKKK

MAPKKK*

E2
MAPKK−PP

MAPKK−P

MAPKK

MAPKK P'ase

MAPK

MAPK−P

MAPK P'ase

MAPK−PP

OUTPUT

FIG. 1: The catalytic topology of the mitogen-activated protein kinase (MAPK) cascades (from Ref. [9], with dashed
positive feedback arrow representing polyadenylation that inhibits degradation of the top protein). Each level in the diagram represents the phosphorylation states of a single protein,
with phosphorylation and dephosphorylation transitions represented by arrows. Exogenous and internal catalysis is represented by (other) arrows pointing to the transition arrows.

as a function of these rates. This analogy has been extended to an elaborate analysis of the properties [12] and
combinatorial logic [3] of such switches. In particular,
[12] considers the case where the the phosphorylated epitope acts as an intermolecular autocatalyst on phosphorylation transitions of any unphosphorylated proteins in
the population, and shows that this leads to bistability.
However, autocatalytic feedback only creates a bistable
switch if the response of the underlying phosphorylation
chain is sigmoidal [11], which in this model requires saturation of the exogenous phosphatase rate via the formation of catalyst-substrate complexes as an intermediate
step between the unphosphorylated and phosphorylated
states of the protein.
E1

E1
WE1

W

W*
W*E2

E2

E2

FIG. 2:
The Goldbeter-Koshland minimal phosphorylation couple. A single protein species has an unphosphorylated state W and a singly-phosphorylated state W ∗ . Ref.[8]
chained such couples to model intermolecular phosphorylation, in combination with exogenous catalysts that are often
present for both transitions as well.

We note, however, that kinetic control through saturated complex formation is not the only way to obtain

3
sigmoidal response, because with two or more phosphorylation sites per protein, the concentration of the fullyphosphorylated state is a sigmoidal function of the ratio of exogenous kinase to phosphatase, even when all
catalysts act in the linear proportional regime (in other
words, when catalyst-substrate complexes act to catalyze
transitions effectively instantaneously, and are limited
only by their frequency of formation through binary encounters). This occurs as long as the catalytic activity
is distributive i.e., if at most one modification (phosphorylation or dephosphorylation) takes place at each
enzyme-substrate encounter [15], and ordered (if successive phosphorylations take place at different residues, an
ordered mechanism implies that dephosphorylation takes
place in strictly the inverse order) [16].
Two of the MAPK proteins have this structure, and
more significantly, the intermolecular catalysis within
the cascade is nonspecific to phosphorylation reactions
on a given protein, though each transition is catalyzed
through an independent event [9]. We show below
that, combining this form of sigmoidality with positive
feedback, it is possible to obtain bistability through a
non-equilibrium phase transition, in which the individual events of catalysis leads to a polarized distribution
of phosphorylation states of the target protein. Such
population-level cooperative effects, (proposed also in the
context of genetic switches in [7]), bestow the stability of
macroscopic (thermodynamic) systems on the otherwise
highly stochastic events of phosphorylation and dephosphorylation. We suggest that the properties of phasetransition-mediated switching are one source of adaptive
preference for multiple phosphorylation sites and nonspecific catalysis, which one encounters repeatedly (histidine kinase cascades may have as many as 26 phosphorylation sites [17]).
Previous studies have also shown that multisite phosphorylation with saturation kinetics at each modification
step can lead to bistability even in the absence of feedback [18, 19]. Hence both kinetic control and populationlevel polarization can lead robustly to bistability in some
parameter domains. However, the two mechanisms are
distinguished by their responses to mutations and by
their control parameters. Single-molecule control causes
switching properties to change if rate kinetics change, in
a way that population polarization does not, while the
role of nonspecific catalysis in models with populationlevel cooperative effects (at least in the form we will consider) creates a different kind of sensitivity. An important
constraint on the evolutionary innovation, preservation,
and diversification of phenotype (any expressed functionality) is the shape of its neutral network [20, 21] (the
degenerate space in the genotype/phenotype map with
regard to that functionality). The phenotype of phasetransition-mediated switching is more nearly controlled
by the topology of the catalytic network than by its kinetics, an idea that has been proposed as a source of
robustness in the segment-polarity network [2], and theoretically grounded in the case of general enzyme-driven

reaction networks in [19].
Note that we do not study spatio-temporal correlations induced by diffusion of enzymes and/or enzyme inactivation. A recent study [22] shows that even with
the enzymes acting according to a distributive mechanism, rapid rebindings of the enzyme molecules to the
substrate molecules can lead to a loss of ultrasenstivity
and bistability. We do not consider the effect of protein
degradation either. Our model is however a first theoretical fully stochastic study of the MAPK cascade, modelled earlier, to our knowledge, only via rate equations
[9, 16, 18, 23, 24] or stochastic simulations [25, 26].
In this context, we study quantitatively the three critical properties of a phase-transition mediated switch: the
conditions for existence of bistability, the noise characteristics of those fluctuations that preserve the domain
in the bistable phase, and the large excursions that limit
memory or reliability of the switch, and which near the
threshold for bistability, can lead to finite-particle number corrections to that threshold. These have only been
considered piecemeal before in other models, with conditions for bistability treated in the infinite-particle (deterministic) limit [10, 27], noise from internal and external
sources related through ad hoc response functions [28],
and stability treated at the level of bounds on scaling,
for systems already assumed reduced to one relevant dimension [13].

C.

Reducing to appropriate models

Most biological literature on this subject focuses on
phenomenological modeling of (usually mean-field behavior in) observed or designed systems [2, 4–6, 9, 10, 18, 27].
We are however more interested in the possibility of statistically motivated universality classification of strategies for switching, which might explain evolutionary regularities in cascades. Therefore, in addition to idealizing molecular mechanisms responsible for sigmoidal response and positive feedback as properties of single protein species, to make the polarization-based equivalent of
the flip-flop from adding feedback to our Fig. 2 (equivalent to Fig. 12 of Ref. [3]), we advisedly exploit symmetry, of either the catalytic topology or the parameters,
to make analysis tractable. This approach also aids in
decomposing effects responsible for switching, and relating these to other equilibrium or non-equilibrium phase
transitions. Thus our minimal models deliberately differ
from the familiar cascade families in areas not directly
related to the production of switching [29]. The model
of Markevich et al [18] is also in this category in demonstrating bistability (via kinetic control) at the level of a
single stage of the MAPK cascade.
The model we propose for a cooperativephosphorylation switch is shown in Fig. 3. Each of
N molecules of a single type of protein has J phosphorylation sites indexed j ∈ 1, . . . , J, which we suppose for
simplicity to be phosphorylated and dephosphorylated

4
in a definite order. All phosphorylations are catalyzed
by exogenous kinases, and all dephosphorylations by
exogenous phosphatases.
Because the enzymes are
assumed to operate in the linear regime where complex
formation is not rate limiting, the catalytic rate per
reaction is proportional to the numbers I and P of
kinase and phosphatase particles respectively (We set
the constant of proportionality equal to one by choice of
the units of time). The site modifications occur in a specific order, thus sidestepping combinatorial complexity.
Furthermore, phosphorylation and dephosphorylation of
substrate proteins is assumed to follow a distributive
mechanism, whereby a kinase (phosphatase) enzyme
dissociates from its substrate between subsequent modification events [30, 31]. Hence the substrate has J + 1
states.
a

b
I

0

pa
thw
ay
s

I

1

2

.......

J-1

J

0

1

2

.......

J-1

J

P

c

P

d
I

0

I

1

2

.......

J-1

J

0

P

1

2

.......

J-1

J

P

FIG. 3: Multisite phosphorylation and feedback structure.
(a) This panel depicts the basic phosphorylation chain without feedback in which a target protein with J sites is phosphorylated by a kinase I and dephosphorylated by a phosphatase
P . The ordered succession of phosphorylations yields J + 1
modification states, labelled 0, 1, . . ., J. (b) The fully phosphorylated target protein relays a signal into pathways that
eventually feed back on the phosphorylation chain. (c) Simplification of (b) in which the fully phosphorylated target protein
acquires kinase activity and directly feeds back on the chain.
We refer to this network configuration as the asymmetric circuit. (d) Schematic of the network with symmetric feedback
in which the substrate protein is bifunctional, whereby the
fully (de)phosphorylated form catalyzes (de)phosphorylation
of its own precursors.

We obtain positive feedback from intermolecular autocatalysis; specifically, proteins in the j = J state are
kinases that act interchangeably with the exogenous kinases (unequal catalytic power between j = J and exogenous kinases can easily be added, at the cost of another

parameter). The phosphorylation chain with feedback is
shown in the bottom half of Fig. 3. Panel (c) depicts
an asymmetric topology in which the fully phosphorylated substrate catalyzes its own phosphorylation, while
panel (d) shows the symmetric version in which a substrate molecule is bifunctional, acting as both a kinase
and phosphatase depending on its modification state. Kinase I and phosphatase P are exogenous forces on the
modification of the substrate, but the feedback is an endogenous force whose strength is proportional to the occupancy of the end-states of the chain. This occupancy is
subject to intrinsic fluctuations and depends on the total
number of substrate molecules.
The assumption of intermolecular autocatalysis is standard [12], and we consider below the self-consistent backgrounds with kinase-only autocatalysis, as the nearest
equivalent to the kinetically-controlled switch [8]. In order to analyse the model beyond mean-field theory (using
field theoretic techniques) we go further in the interest
of simplicity, and symmetrize the topology as in Fig. 3d,
by making the unphosphorylated state (indexed j = 0) a
phosphatase, interchangeable with the exogenous phosphatases.
The feedback topology of the model caricatures a few
elements present in biological systems. One such element is the competition between antagonistic pathways
that may underlie cellular decision processes (for example [32]). A multisite phosphorylation chain of the type
considered here could function as an evaluation point between competing and antagonistic pathways influenced
by different active phosphoforms of the chain, provided
these pathways feed back to the chain. In a less extreme
case, the fully phosphorylated form activates another kinase which then interacts with the chain. In these scenarios, feedback is mediated by a series of intervening
processes, which may well affect the propagation of fluctuations. Yet, if delays are not too large, the collapsed
scheme of Fig. 3c could be a reasonable proxy with the
added benefit of mathematical tractability.
A scenario corresponding more literally to our model
involves a bifunctional substrate capable of both kinase
and phosphatase activity, depending on the substrate’s
modification state. One example is the HPr kinase/PSer-HPr phosphatase (HprK/P) protein, which operates
in the phosphoenolpyruvate:carbohydrate phosphotransferase system of gram-positive bacteria. Upon stimulation by fructose-1,6-bisphosphate, HprK/P catalyzes the
phosphorylation of HPr at a seryl residue, while inorganic
phosphate stimulates the opposing activity of dephosphorylating the seryl-phosphorylated HPr (P-Ser-HPr) [33].
Another example of a bifunctional kinase/phosphatase is
the NRII (Nitrogen Regulator II) protein. It phosphorylates and dephosphorylates NRI. NRI and NRII constitute a bacterial two-component signaling system, in
which NRII is the “transmitter” and NRI the “receiver”
that controls gene expression. NRII autophosphorylates
at a histidine residue and transfers that phosphoryl group
to NRI. The phosphatase activity of NRII is stimulated

5
by the PII signaling protein (which also inhibits the kinase activity). Several other transmitters in bacterial
two-component systems seem to possess bifunctional kinase/phosphatase activity [34].
Both the network with asymmetric topology (autokinase only, Fig. 3c) and the network with symmetric
topology (Fig. 3d) but asymmetric catalytic concentrations I 6= P undergo formally first-order phase transitions, so that regions of bistability are always metastable
at finite N . However, in the topologically symmetric
case, these continue smoothly through a second-order
transition at I = P , in which symmetry of both topology and parameters ensures exact bistability with finite
residence time in domains, at all N where the phase transitions exists. This simplification permits us to estimate
the residence times with an expansion in semiclassical
stationary points of an effective action, without encountering the complexities of path integrals for metastable
processes [35], though numerically we expect this also to
be a good approximation to residence times in metastable
states with similar “barrier heights” in the first-order
case. Symmetry also permits the closed-form computation of the noise kernel about the monostable phase with
a unique equilibrium, which generates a natural measure
for “weakness” or “strongness” of the first-order transitions at nearby values of I/P as a function of N . We
therefore perform a thorough analysis of the second-order
transition, to establish methods and provide a reference
solution to qualitatively understand the mechanisms of
bistability and metastability in the more general cases
with similar stochastic structure.

D.

Methods of treatment for the stochastic
problem

While differential equations for mean chemical concentrations (the current standard method of analysis) can
give good estimates of the existence of hysteresis and
bistability when approximating systems with as few as
tens to hundreds of molecules, they of course preclude
the treatment of noise, fluctuation-induced corrections
to mean-field behavior at small particle number or near
critical points, and large excursions such as domain flips
(when the system switches from one bistable state to another). Pure mass-action models also ignore spatial constraints such as scaffolding by the cytoskeleton or the
proteins themselves, and the dimensionality of physical
diffusion in the cytosol or membranes.
A better approximation is given by the master equation for the probability of instantaneous particle distributions in models like that of Fig. 3, which in principle captures all orders of stochastic processes, though
such simple models still omit spatial effects. The general
properties of the master-equation (in the diffusion, or
“Fokker-Planck” approximation) for a one-dimensional
switch have been used to obtain scaling relations and
loose bounds on the stability achievable from such a

switch as a function of the number of molecules it employs [13].
Operator methods, analogous to Hamiltonian methods
in quantum mechanics, have been developed in reactiondiffusion theory (see [36] for a review) to efficiently
handle the collective excitations that diagonalize general
master equations without time-reversal symmetry. These
have been used in the context of gene expression [7] to
estimate the number of stable cell types made possible by
many randomly combined transcription factors, making
use of similarities to ground states of random-bond Ising
models.
From the operator-valued evolution kernel, one can
obtain an equivalent path-integral representation by expanding at each time in a basis of coherent states [37, 38].
Stationary-field expansion in the path integral generalizes the classical differential equation for concentrations to consistently incorporate fluctuation effects (by
means of a perturbatively-corrected effective action [39]),
and the sum over “approximate stationary points” of locally least-action identify the typical configuration histories associated with domain flips. More sophisticated approaches, similar to those used here, have also
been used to incorporate fluctuation effects into efficient
lumped-parameter expansions for networks with multiple
timescales [40].
Master equations can also be solved numerically by the
Gillespie algorithm [41], or simulated directly, and we
use such simulations to validate our anlaytic results below. The lack of convenient symmetries in real biomolecular systems promises to make analysis intractable for
most quantitative phenomenology, and recourse to numerics is likely to be the only general-purpose solution.
However, the path integral’s separation of moments in a
natural small-parameter expansion, and of perturbative
noise from formally non-perturbative large excursions,
provides an intuitive decomposition of the mechanisms
fundamental to switching and stability. At mean-field approximation, we find surprising similarities of the phase
transition in this driven system to the magnetization
transition in the discrete, equilibrium, mean-field Ising
ferromagnet, and a transition between this classical critical behavior at finite J and a condensation effect more
similar to Bose-Einstein condensation at J → ∞. The algebraic distinction between self-consistent backgrounds,
perturbative fluctuations, and non-perturbative domain
flips, elementary in the analysis, is also a subtle distinction, difficult to make without systematic measurement
biases, in the numerics.

E.

Main results from the analytical treatment

The mean-field results, which are reported in detail
in [29], and which can also be recovered from our
effective-action treatment in this paper, reproduce the
standard differential equations for mass action. The
stationary states arise from conditions of detailed bal-

6
ance between phosphorylation and dephosphorylation,
self-consistent with the concentrations they produce of
autocatalytic phosphoepitopes in relation to exogenous
catalysts. Specifically, we show how both symmetric and
asymmetric topologies create domains of mono- and bistability in the parameter space (I/N, P/N ), and how
the population asymmetry in the
√ self-consistent state depends on the coupling g ≡ N/ IP and exogenous asymmetry I/P .
The perturbative expansion in Gaussian fluctuations
about the self-consistent background provides a systematic construction of the noise spectrum of the phosphorylation chain. At lowest order it predicts a cusp
∼ 1/ |g − gc | in the variance of the order parameter,
equivalent to the Curie-Weiss prediction for the spin-1/2
mean-field ferromagnet. More surprising, we find that
the entire perturbative approximation to the noise spectrum on all sites is generated from a single bare mode,
effectively coupled to a single Langevin field. This result
replaces the ad hoc noise kernels one must entertain in
the absence of a first-principles treatment [28, 42].
The nonperturbative expansion in semiclassical configurations of locally least action predicts the leading
large-N dependence of the domain residence time in the
bistable regime, as a function
√ of the dimensionless rates
of the problem I/P and IP /N (though here we solve
only for the symmetric case I/P = 1, where bistability remains exact at finite particle numbers). These
configurations, the dissipative equivalent to the instantons of Euclidean equilibrium field theory [35], solve two
problems. First, from the high-dimensional configuration
space of the N -particle, (J + 1)-site chain, they extract
the one-dimensional contour of most likely configurations
to mediate domain flips, assumed given in Ref. [13].
Second, the action along this trajectory, ∝ N at fixed
(I/N, P/N ), is the leading exponential in the residence
time, for which Ref. [13] correctly predicts the scaling but
gives no algorithm to compute the coefficient (known in
large-deviations literature as the rate function [43]).
Similar leading-exponential dependencies have been
computed in Ref’s. [42, 44]. For reference to this work,
we note that the passage to the diffusion limit or FokkerPlanck equation in Ref. [13], and the closely-related
use of the Gaussian approximation for fluctuations in
Ref. [42],[55] are formally uncontrolled approximations,

whose limitations and ranges of validity are pointed out
in Ref. [44]. One purpose for our paper is to present the
larger systematic analysis within which such approximations arise.

F.

Layout of the paper

Sec. II introduces the master equation for the model
class of Fig. 3 c and d, and derives the phase diagram
for steady states from conditions of detailed balance of
the mean particle numbers. Sec. III converts the master
equation, first into the equivalent representation in terms
of a state in a Hilbert space, and then into the equivalent
path-integral representation through an expansion in intermediate Poisson distributions. Sec. IV derives the perturbative expansion in fluctuations about the mean fields
of the path integral, including the equivalent representation in terms of a Langevin equation, and the leadingorder perturbative approximation to the fluctuations in
the order parameter. Sec. V then considers the enlarged
expansion in approximate stationary points needed to derive the trajectories and rate of domain flips. Finally,
Sec. VI summarizes the consequences of these technical
results for the conceptual understanding of biomolecular
signal transduction and switching.

II.

MASTER EQUATION AND MEAN-FIELD
BACKGROUNDS

An instantaneous configuration of N proteins on the
J + 1 sites of Fig. 3 defines a vector n ≡ (n0 , n1 , . . . , nJ ),
where nj is the number on site j. Fixed particle number
implies that n lives on the integer lattice in the J-simplex
PJ
j=0 nj ≡ N . We denote a (generally time-dependent)
probability distribution on configurations P (n), and suppress the time index t in the notation.
A stochastic process for particle hopping is completely
defined by the master equation for P (n), which is the
“probability inheritance” equation induced by the transition probabilities on the simplex. For Fig. 3 with catalytic rates proportional to the number of catalytic particles, this is

J−1
X
∂
(I + nJ − δJ,j+1 ) (nj + 1) P (n + 1j − 1j+1 ) − (I + nJ ) nj P (n)
P (n) =
∂t
j=0


+ (P + n0 − δ0,j ) (nj+1 + 1) P (n − 1j + 1j+1 ) − (P + n0 ) nj+1 P (n) ,

where 1j denotes the vector with jth component equal
to 1 and all other components zero.

(1)

Our assumption that phosphorylation and dephosphorylation happen in a definite sequence makes transition

7
rates from site j proportional to nj and the catalyst concentration, without additional combinatorial factors. For
the asymmetric (auto-kinase only) topology, the factors
n0 and δ0,j in the second line of Eq. (1) are absent, and
dephosphorylation depends only on the nj and the exogenous phosphatase number P .
Time-dependent average particle numbers on each site
are defined as
X
hnj i ≡
P (n) nj ,
(2)
n

PJ

and it is easy to see from Eq. (1) that j=0 d hnj i /dt ≡
0.
It is also useful to write the equation
P for the center-ofmass of the system defined as C ≡ n,j jnj P (n). This
becomes
∂
C = N (I − P ) + [P hn0 i − I hnJ i]
∂t


+ N [hnJ i − hn0 i] + n20 − n2J

(3)

As we will see later, this exact equation can be used to
estimate the fluctuations of the order parameter for large
J.
In what follows, we first look at the mean-field approximation already elaborated on in [29]. The mean-field
approximation for evolution of hnj i under Eq. (1) replaces all joint expectations with products of marginals:
hnj nJ i ≈ hnj i hnJ i, etc.
A.

Detailed balance: symmetric topology

Under the mean-field approximation, the system of N
interacting particles essentially decouples into a system
of N independent particles executing a random walk on
the lattice of J + 1 sites. Within this approximation detailed balance of phosphorylation and dephosphorylation
between adjacent sites in the chain holds, and depends
on a catalytic ratio which we will denote x. For the
symmetric topology, x ≡ (I + hnJ i) / (P + hn0 i), and we
recognize two convenient nondimensional parameters:
I
≡ eλ ,
P

(4)

N
√
≡ g.
IP

(5)

and

As autocatalysis, scaled by N , induces bistable order (i.e.
it favours configurations in which most particles are piled
up towards one or the other end of the chain), and exogenous catalysis, scaled by I and P , induces homogeneity
(configurations in which particles are uniformly spread
out on the chain), g is the coupling strength of the model,
with strong coupling favoring broken symmetry. I/P is
then the measure of exogenous asymmetry.

In terms of these and the fractional occupations
hnj i /N , the catalytic ratio may be written
x≡

eλ/2 + g hnJ i /N
≡ eξ .
e−λ/2 + g hn0 i /N

(6)

By induction on j, time-independent solutions satisfy
hnj i = xj hn0 i , 0 ≤ j ≤ J,

(7)

and the normalization
N=

J
X
j=0

hnj i = hn0 i

1 − xJ+1
.
1−x

(8)

From Eq. (6) and Eq. (7) we can evaluate



sinh J2 ξ
2 sinh ξ−λ
2
g

,
hnJ − n0 i =
N
sinh J−1
2 ξ

(9)

and we can rewrite Eq. (8) as
hnJ − n0 i
=
N

 
ξ
2

sinh

sinh

J+1
2 ξ

2 sinh

J
2ξ





.

(10)

When Eq. (9) and Eq. (10) are nonzero, they have the
ratio



sinh J+1
sinh ξ−λ
2
2 ξ
 
(11)
g=
 .
ξ
sinh 2ξ sinh J−1
2

For I 6= P , Eq. (11) always holds (though it may be
negative or singular), while for I = P we have the possibility of the degenerate case where hnJ − n0 i = 0 and g is
unconstrained. For g < gC (λ = 0) (a second-order critical point) this is the stable asymptotic distribution, while
for g > gC (λ = 0) it is unstable. The graph of g versus
ξ for a few (non-positive) values of λ at J = 2 is shown
in Fig. 4. (Positive λ generate curves reflected through
ξ = 0.) The graph defines a pseudo-inverse ξ(g), which
gives the stationary solutions within the mean-field approxiation. Where ξ is triple-valued (not a well-defined
inverse), the central branch is in all cases unstable, and
the two outer branches are stable.
The character of the curves in Fig. 4 is preserved for
all J > 2, though the derivative of the stable curve for
I = P above its critical point becomes discontinuous at
ξ = 0 for J → ∞. This discontinuity is related to the
transition from Curie-Weiss to Bose-Einstein-like behavior of the order parameter, discussed below. The curves
corresponding to all λ have regular limits at large J.
We can identify a set of gC (λ) as the local minima in
Fig. 4 above which the ξ(g) graph becomes triple-valued.
The λ → 0 limit of these minima smoothly converges on
the second-order critical coupling
gC (λ = 0) ≡

J +1
.
J −1

(12)

8
15

λ=

-1.
5

1
0.9

J = 99

0.8

0

J =9

λ=

0.7

10

J =5

P/ N

λ=

g

0.6
J =3

0.5

0

0.4
J =2

5
0.3
λ=

0.2
λ=0

5
-1.

0
-3

0.1

-2

-1

0

1

2

3

ξ


Converting the pair λ, gC (λ) to (I/N, P/N ) values
yields the phase diagram shown in Fig. 5 for a range of J
values. The interior region I ∼ P and sufficiently small
√
IP /N ≡ 1/g is bistable, and outside this region the
sign of ξ = log x equals that of λ ≡ log I/P . As we
demonstrate in [29], these theoretical estimates match
very well with data from Monte carlo simulations.
Detailed balance: asymmetric topology

In the auto-kinase-only asymmetric model, positive λ
(I > P ) is never bistable, because the particles are already biased toward nJ , the only site with positive feedback. Therefore we graph only λ ≤ 0, though the algebraic solutions are valid everywhere.
Instead of Eq. (6), the catalytic ratio is x ≡
(I + hnJ i) /P , which reduces in nondimensional parameters to
x≡

eλ/2 + g hnJ i /N
≡ eξ .
e−λ/2

0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

1

I/N

FIG. 4: g(ξ) from Eq. (11) along contours of constant λ, for
which the two branches proceed outward from the ξ = 0 line
in order of increasing |λ| (different λ values are depicted by
different line styles). The branches with the lowest and largest
values of λ are marked on the figure. The other λ values can
be read on the left from the intersection with the abscissa
where ξ = λ. Where g(ξ) has a single-valued inverse, that
function ξ(g) defines the unique steady-state distributions.
Where the inverse is triple-valued, the largest |ξ| are stable
solutions, and the central branch is unstable.

B.

0

(13)

Equations (7) and (8) still hold, but instead of Eq. (9)
we choose the reduction


ξ−λ
2
sinh
2
hn0 i

 .
(14)
=
g
N
exp J − 12 ξ

FIG. 5: Phase diagram for the symmetric topology, from the
minima gC (λ) of Fig. 4, and their equivalents for a range of
J. The regions inside the chevrons are bistable.

The appropriate reduction of Eq. (8), counterpart to
Eq. (10), is now
 
sinh ξ2
hn0 i

.
(15)
=
N
exp J2 ξ sinh J+1
2 ξ

Eq. (14) and Eq. (15) are regular at all ξ, so we always
have a defined function g(ξ), of the form



2 sinh ξ−λ
sinh J+1
2
2 ξ
 
(16)
g=
 .
ξ
sinh 2ξ exp J−1
2

A graph at J = 2, which is the asymmetric-topology
counterpart to Fig. 4, is shown in Fig. 6. In the bistable
phase, there are still three branches for ξ at given g,
with the outer two stable and the central one unstable.
The obvious differences are that now there is a maximal
λ for bistability, and that the leftmost stable branch at
any λ moves positively in ξ as g increases because of the
asymmetric topology, whereas in the symmetric topology
it moved negatively in ξ.
At any λ below a (negative) J-dependent threshold, we
can extract the minimal and maximal g values for bistability (below the minimum, ξ follows λ ≡ log (I/P ) qualitatively; above the maximum, only the largest-ξ branch
is stable because of too-strong positive feedback). Inverting gmin(λ) and gmax (λ) to (I/N, P/N ), we obtain
the phase diagram for bistability shown in Fig. 7.
The upper boundary of each bistable region, defined
by gmin (λ), is a distorted counterpart to the upper gC (λ)
branch in Fig. 5, and the two converge to the same limit
as J → ∞ (where feedback from n0 becomes irrelevant).

9
formed this continuation smoothly by weighing the n0
catalytic strength with a parameter ε ∈ [0, 1].) Further, the first-order transition in g along any I/P ray
in the symmetric topology continues smoothly through
the second-order transition at I/P = 1, at the apex of
the domain of bistability. Whether the first-order transitions in the neigborhood of I/P = 1 are strong or weak
depends on the ξ-support of the stationary solution for
P (n) (a function of N ), in relation to the difference between the stable mean values at gC (λ).

λ = -2.5

15

g

10

5
λ=

-1.5

λ
0
-3

-2

-1

=0

0

C.

1

2

3

We now restrict attention to the case of symmetric
topology and exogenous catalysis setting I = P ≡ q, and
consider the behavior of the natural mean-field order parameter |hnJ − n0 i| /N as a function of J. Expanding
Eq. (10) in small ξ, and inverting Eq. (11) relative to
gc ≡ gC (λ = 0) in Eq. (12), we find the mean-field critical scaling of the discrete Ising ferromagnet, up to a
J-dependent prefactor:

ξ
FIG. 6: g(ξ) along contours of constant λ for the asymmetric
topology, J = 2 and the same λ values as in Fig. 4. The
maximal λ for bistability generates the curve whose minimum
derivative is zero.

1

√ 
1/2
|hnJ − n0 i|
6J g
−1
≈
.
N
J + 1 gc

0.9
J = 99

0.8

P/ N

0.6
J=9
J=2

0.4

J=3

J=5

1
|hnJ − n0 i|
→1− .
N
g

0.3
0.2

(18)

The exact mean-field prediction for |hnJ − n0 i| /N versus
g from Equations (10) and (11) is compared to numerical
simulations for J + 1 = [5, 10, 100], in Fig. 8.

0.1
0

(17)

The small-ξ approximation is valid for g − gc <
∼ gc −
1, above which the order parameter saturates to a Jindependent envelope value

0.7

0.5

Phase transition and order parameter versus J

0

0.1

0.2

0.3

0.4

0.5
I/N

0.6

0.7

0.8

0.9

FIG. 7: The phase diagram for auto-kinase feedback only.
The domains of bistability are somewhat smaller than in
Fig. 5, and are shifted toward smaller I/P , but otherwise
the characteristics are qualitatively and even quantitatively
similar.

The lower boundary, defined by gmax (λ), replaces the
reflected lower gC (λ) branch in Fig. 5, and converges to
the diagonal I = P at J → ∞.
Thus we see that classically, the first-order phase transitions are similar for symmetric and asymmetric feedback topology, one being deformable into the other in
the (I/N, P/N ) parameter space. (We could have per-

1

Since gc − 1 → 2/J for large J, Eq. (18) also gives the
behavior in the formal J → ∞ limit. The derivative of
the order parameter converges to one in arbitrarily small
neighborhoods of the critical point, rather than to ∞ as
in the Curie-Weiss regime; thus J → ∞ defines a different universality class than any finite J. Qualitatively,
the distinction between small and large-J is determined
by whether one or both reflecting boundaries are sensed
by the near-critical symmetry-broken state. The largeJ transition resembles Bose-Einstein condensation in the
sense that either n0 or nJ accounts for a finite fraction of
the particles, with the remainder “thermalized” with an
exponential distribution in j into the interior, at “temperature” self-consistently determined by q/N = 1/g. To
understand the nature of these transitions beyond meanfield theory we introduce the operator and path-integral
representations of the master equation and its solutions.

10
A classical distribution P (n) has the state representation in the n basis
X
|ψ) ≡
P (n) |n) .
(22)

0.7
0.6

n

<nJ - n0> / N

0.5
0.4
0.3
0.2
0.1
0
0.

1

1.5

2

2.5

3

3.5

g

FIG. 8: Order parameter |hnJ − n0 i| /N for the symmetric phosphorylation chain: mean-field theory (lines) and simulations (symbols). J + 1 = [5, 10, 100] corresponds to
[dot, dash, solid] for lines and [+, o, ×] for symbols. Particle numbers used in the simulations are respectively N =
[4000, 2000, 400].

The operator representation of master equations from
reaction-diffusion theory [36, 38] begins by introducing
raising and lowering operators a†j , aj for each site on
the lattice, with the commutation
of orthogonal
i
h relations
quantum harmonic oscillators aj , a†j ′ ≡ δj,j ′ . These
define a Hilbert space through their action on a “vacuum”
state aj |0) ≡ 0, ∀j, and its conjugate (0| a†j ≡ 0, ∀j.
Number states indexed by the vector n are defined
through the action of the raising operators
J
Y

a†j

j=0

nj

|0) ,

J−1
X

a†j+1 − a†j

 

1+

n̂0
q




 
n̂J
aj+1 − 1 +
aj
q

(24)
Here I = P ≡ q as mentioned earlier. The differential
equation (23) is formally reduced to quadrature to give
the time-dependent state relation
|ψt ) ≡ e−Ωt |ψ0 ) .

(25)

Normalization
of P (n) and the number states |n) implies
P
(0| exp
j aj |ψt ) = 1, ∀t. We further recognize the ex-

ogenous catalytic strength q ≡ 1/τ as defining a natural
timescale, and the natural coupling g ≡ N/q in Eq. (24),
as before.
B.

Coherent-state expansion and path integral

(19)

and differ from quantum-mechanical number states in being normalized with respect to a universal Glauber state
[36, 38]
P
a
(20)
(0| e j j |n) = 1, ∀n.

The number operator for each j is defined as n̂j ≡ a†j aj ,
and extracts the appropriate coefficient from n in the
Glauber norm,


X
(0| exp 
aj ′  n̂j |n) = nj .
(21)
j′

(23)

in which the nonlinear, diffusive Liouville operator that
evolves the state in time is given by

j=0

Operators, states, and time evolution

|n) ≡

d
|ψ) = −Ω |ψ) ,
dt

Ω=q

III. OPERATOR, STATE, AND PATH
INTEGRAL REPRESENTATIONS
A.

|ψ) is equivalent to a generating function f (z) of a
(J + 1)-component complex vector z, under the association a†j ↔ zj , aj ↔ ∂/∂zj . Glauber normalization is
equivalent to a prescription for shifting zj → zj + 1, and
evaluating the resulting function at zj = 0, ∀j. A thorough treatment of these methods for handling generating
functions and functionals is provided in Ref. [45] in the
context of the analysis of master equations for evolutionary games. However for the treatment that follows below,
we need only the definitions provided above in order to
proceed.
The master equation (1) corresponds to state evolution
equation known as the Liouville equation

At weak nonlinearity (small g), it is both intuitive and
computationally efficient to expand solutions to Eq. (25)
in eigenvectors of the annihilation operators aj [38],
which are the Poisson distributions in nj . We start with a
normalized initial state arbitrarily parametrized by mean
occupation numbers



X  †
(26)
n̄j aj − 1  |0) ,
|ψ0 ) = exp 
j

in which judicious choice of the n̄j cancels surface terms
associated with transients. (Self-consistency of these parameters with stationarity under Ω may be used from
the operator representation to obtain moments of P (n),

11
as was done in Ref. [7], though we will proceed directly
to the time-dependent field action here.) To form a basis
for coherent-state expansion (again, see [38] for detials
of this procedure) at increments of time, we introduce a
T
complex-valued vector field φt ≡ (φ0 , φ1 , . . . , φJ )t , and
′
†
its adjoint φt . At a set of t = k∆t, we insert the representation of identity
Z

dφ†t′ dφt′
π

e

−φ†′ ·φt′ a† ·φ ′
t
t

e

P

φ† ·a

|0) (0| e t′

=

X
n

|n) (n| = I
(27)



(0| exp
expressed
j aj |ψt ),
Eq.
(25)  and
Eq. (26)
as

P
P
†
−Ωt
|0). Though
exp
(0| exp
j n̄j aj − 1
j aj e
the coherent states are overcomplete, phase cancellations
in Eq. (27) leave the proper complete number basis at
′
each t .
By now-standard procedures [36, 38] we recognize that
the fields φ and φ† have somewhat different roles, with
fluctuations in φ about its mean value corresponding
roughly to fluctuations in number, and those in φ† sampling moments of the generating functional |ψ). Thus
we expand the complex-conjugate coefficients φ∗j of the
(row) vector φ† at each time as φ∗j ≡ φ̃j +1 at each t, with
shorthand φ†t ≡ φ̃t + 1, leaving φ to be determined physically. The resulting normalized generating functional has
the path-integral representation
into
through



Z
R
X


aj |ψt ) = Dφ̃ Dφe− dtL eφ̃0 ·(n̄−φ0 ) ,
(0| exp
j

(28)

in which the diffusive “Lagrangian” is




∂φ
L φ̃, φ = φ̃ ·
+ Ω φ̃ + 1, φ .
∂t

(29)

The Liouville operator (24)
a complex has induced


valued function of fields Ω φ̃ + 1, φ
stitution a†j → φ̃j + 1, aj

through the sub-

→ φj . We will see that, up
to care with signs and contours of integration that depend on what we wish to extract from this function, it
behaves as the equivalent of a Hamiltonian for an equilibrium system, with a few structural differences characteristic of stochastic processes(elaborated also in [45]).
The measure Dφ̃ Dφ in Eq. (28) is defined formally by
the skeletonization procedure for insertion of the coherent states, but in practice is usually defined implicitly by
perturbation theory in the diffusive Green’s function[56].
Linearization of Ω in either Eq. (23) or Eq. (28) (i.e.
keeping only terms linear in φ̃) provides the natural
expansion in independent collective fluctuations of the
master equation and gives results for expectation values
which are identical with the mean-field results presented

earlier. In the field form (29) it further provides a convenient and intuitive background-field expansion, in which
the backgrounds represent locally best-fit Poisson distributions with mean number equal to φ∗j φj for each component j.
C.

Structure of reaction-diffusion Lagrangians

To make use of the form of Ω, we introduce two projection matrices onto the catalytic sites j = 0, J, P± with
components (P+ )jj ′ ≡ δj,J δj ′ ,J , and (P− )jj ′ ≡ δj,0 δj ′ ,0 ,
and linear-diffusion matrices


1


..
 −1

.
,
D+ ≡ 
(30)


..

. 1 
−1 0




D− ≡ 



0 −1
1

..





,

..
. −1 
1
.

(31)

corresponding to phosphorylation and dephosphorylation
transitions, respectively.
Noting that for 1T the row vector of all ones, 1T D± ≡
0, we can use φ† or φ̃ as it is convenient, to write



1 †
1
†
Ω φ , φ = 1 + φ P− φ φ† D− φ
q
q


1 †
+ 1 + φ P+ φ φ† D+ φ. (32)
q
We extract the overall N -dependence of the action in
the path integral by descaling time with the definition
dz ≡ dtq ≡ dt/τ , and rescaling the Lagrangian to a Lagrangian density per particle, to write
R
R
e− dtL = e−N dzL̂ ,
(33)

with L̂ ≡ L/qN . If we similarly descale the field φ →
φ̂ ≡ φ/N , and the Liouvillian Ω → Ω̂ ≡ Ω/qN , we have
the Lagrangian density in terms of the natural coupling
g = N/q:


(34)
L̂ = φ̃ ∂z φ̂ + Ω̂ φ† , φ̂ ,
where





Ω̂ φ† , φ̂ = 1 + gφ† P− φ̂ φ† D− φ̂


+ 1 + gφ† P+ φ̂ φ† D+ φ̂.

(35)

Note that the natural fields define the D
relative
number
E
PJ
≡ 1.
operator φ†j φ̂j = nj /N ≡ νj , satisfying
ν
j=0 j

12
Now not only are the fields φ† and φ̂ expanded about different backgrounds, comparable fluctuations of φ̃ and φ̂
correspond to fluctuations of φ† and φ on scales differing
by N , with large N defining the domain of perturbation
theory.
To expand the functional integral (28) in Gaussian
fluctuations, we further separate out mean values from
¯
the fields, introducing notation φ̃ ≡ φ̃ + ϕ (so putting
¯
φ¯† = φ̃ + 1T and φ† = φ¯† + ϕ). Using a compact notation
i
Ω̂j for the tensor of i φ† -derivatives and j φ̂-derivatives
of Ω̂, the second-order Taylor expansion in ϕ is exact:


¯
L̂ = φ̃ · ∂z φ̂ + Ω̂ φ¯† , φ̂

i 1
h
 
+ ϕ · ∂z φ̂ + Ω̂1 φ¯† , φ̂ + ϕ2 : Ω̂2 φ̂ ,
2

(36)

and Ω̂2 is independent of φ¯† .
¯ ≡ 0 makes the first line of Eq. (36)
The background φ̃
¯ we can
vanish for general φ̂, and for more general φ̃
expand φ̂ in a classical background and perturbations,
¯ The ϕin which the linear order vanishes at that φ̃.
linear term in the second line of Eq. (36) enforces a δfunctional if ϕ is rotated to an imaginary
  integration con2
tour, and negative eigenvalues of Ω̂ φ̂ only soften the
δ-functional for their corresponding ϕ eigenvectors with a
convergent Gaussian envelope. We handle these eigenvalues in perturbation theory with a Hubbard-Stratonovich
transformation [46] and a Langevin (auxiliary) field [38].
We see below that in phases
  with no symmetry breaking,
the eigenvalues of Ω̂2 φ̂ are all zero or negative.[57]
 
Positive eigenvalues of Ω̂2 φ̂ , of which one appears in
the phase of symmetry breaking in this problem, require
different treatment. They produce a divergent envelope
for the δ-functional integral if ϕ is integrated along an
imaginary contour, while a real contour for a ϕ eigenvector does not enforce the expected δ-functional for the
corresponding component of the diffusion equation. We
expect, from experience with Euclidean field theories for
reversible systems, that these eigenvectors signal the existence of a continuous class of “approximate” stationary
points generally termed instantons [35]. ϕ diverges initially along a real contour, but for the appropriate joint
background of φ̂, nonlinearities in the equations of motion extend the
R divergence into a bounded trajectory of
locally least dz L̂, representing domain flips (a fluctuation that takes the system from one of the bistable phases
to the other) in the symmetry-broken phase. The integration over the unstable fluctuations of ϕ are not handled
in Gaussian perturbation theory about the static background, but replaced (with a proper measure term) with
the integral over all time-translates of the approximate
stationary solutions.

D.

Symmetries and conservations

Foregoing formal treatment of the convergence of
Langevin perturbation theory and its regulation by approximate stationary points [47], we observe two important global symmetries of the theory which hold as field
identities and also order-by-order in a large-N expansion.
These are useful in numerically solving for approximate
stationary points in low-dimensional examples.
The classical equations of motion following from
′
¯
Eq. (36) and its equivalent expansion for φ̂ = φ̂ + φ̂
are


¯
¯
(37)
∂z φ̂ + Ω̂1 φ¯† , φ̂ = 0,



¯
(38)
− ∂z φ¯† + Ω̂1 φ¯† , φ̂ = 0.

Both are O N 0 , as L̂ is defined in terms only of z, g, and
descaled fields. The equivalent equations in terms of φ†
and φ, resulting from shifts of the fields in the measure,
generate Ward identities of the theory to all orders in N .
The transformation φ† → eΛ φ† , φ̂ → e−Λ φ̂ at constant Λ is a symmetry of L̂ at generalφ† , φ̂, whose associated Noether charge is number: ∂z φ† · φ̂ = 0 as a

field equation. Time-translation is also a symmetry
of L̂

whose Noether charge is the potential: ∂z Ω̂ = 0. Both
of these follow immediately as properties of the classical
solutions of Eq’s. (37) and (38). About backgrounds that
¯
¯
are,
converge to, φ̃ ≡ 0, the constraints φ¯† · φ̂ = 1 and
 or 
¯
Ω̂ φ¯† , φ̂ = 0 specify a 2J-dimensional subspace of field
configurations in which all classical trajectories must lie.
We further note that, due to the quartic form (35),


¯
¯
¯
¯
φ̃ · ∂z φ̂ = −φ̃ · Ω̂1 φ¯† , φ̂

 1 2
 
¯
¯
¯ : Ω̂2 φ̂
= −Ω̂ φ¯† , φ̂ − φ̃
.
(39)
2
The classical action over any stationary trajectory is then


 
1 ¯2
¯
¯
L̂ φ¯† , φ̂ = − φ̃ : Ω̂2 φ̂
2





¯ ¯
¯
¯ ¯
¯
¯ φ̂
¯ φ̂
= −g φ̃P
φ̃D− φ̂ − g φ̃P
φ̃D+ φ̂. .
−
+

(40)
 
¯
The positive eigenvalues of Ω̂2 φ̂ , which create divergent ϕ fluctuations if we include them in the expansion of Eq. (36), correspond to trajectors that take L̂
below the value (L̂ = 0) of all classical (true) stationary points. However, we will see that the nonclassical
“approximate” stationary points of Eq’s. (37) and (38)
produce strictly positive L̂, so that domain flips are suppressed relative to the persistence amplitude within domains in the symmetry-broken phase. This will be more
transparent with the representation in terms of actionangle variables introduced in Sec. V.

13
E.

0.9

The background-field expansion to recover
mean-field theory

0.8
0.7
0.6
0.5
nJ

The relation (28) between the state and path integral
representations of the master equation gives the expected
first moment of the field


X
(41)
aj  n̂j |ψt ) = nj t ,
φj t = (0| exp 

0.4
0.3

j

where the second angle bracket in Eq. (41) denotes expectation in the probability Pt (n). While not a field equation (remember that φ∗j φj is the combination extracted
by n̂j ), this relates the classical mean-field solutions to
the stationary points of L̂. The classical solutions correspond to the subset of stationary points [36, 37]
∂L
=0
∂ φ̃ φ̃≡0

(42)

which solve Eq. (37) at φ¯† ≡ 1. These need not be timeindependent, and include the full suite of classical diffusion trajectories. However, if the n̄j in the initial condition (26) are set to the steady-state values, they satisfy
detailed balance under the ratio of catalytic rates corresponding to Eq. (6) (at λ = 0 in this case):
¯
1 + g φ̂J
x ≡ eξ =
¯ .
1 + g φ̂0

(43)

The fields themselves satisfy
φ̄j = xj φ̄0 , 0 ≤ j ≤ J,

(44)

per Eq. (7), and the remaining solutions for the coupling
follow.
IV.

FLUCTUATIONS ABOUT STATIC MEAN
FIELDS

Fig. 9 shows the general character of timeseries for the
population as represented by the number nJ , in a phase
with relatively strong symmetry breaking (g = 4.08 for
J = 2. As a reference the phase transition occurs at
g = 3). A timeseries is characterized by dense fluctuations about the mean value, in which nJ remains near the
mean-field value, punctuated by occasional large excursions that shift the mean. In this section we will consider
the Gaussian-order approximation to the dense fluctuations about the mean. In Sec. V we return to qualitatively different methods to handle the rare events which
change mean population state.
A.

Diffusion eigenvalues and eigenvectors

We compute the noise spectrum by further expanding
′
¯
¯
Eq. (36) about φ̃ ≡ 0, defining φ̂ ≡ φ̂ + φ̂ and letting

0.2
0.1
0
500000

502000

504000

506000

508000

510000

t

FIG. 9: Simulation results for a population history, represented by nJ (number of full-phosphorylated particles). We
have used a system of 100 particles and a g-value of 4.08.

¯
φ̂ be a constant solution to Eq. (42),
so that the linear

¯
term in ϕ vanishes. Using L̂ 0, φ̂ = 0, the second-order
expansion defines the Gaussian kernel, with the form
′

L̂ = ϕD0 φ̂ + ϕD2 ϕT + h.o.

(45)

and higher-order terms (h.o.) are left for perturbative
′
expansion. The diffusion kernel governing φ̂ in Eq. (45)
is




¯
¯
D0 = ∂z + 1 + g φ̂0 D− + 1 + g φ̂J D+


¯
¯
+ g D− φ̂1T P− + D+ φ̂1T P+ ,
(46)

while the kernel controlling the constraint field ϕ is



g
¯ ¯T
¯ ¯T
D− φ̂φ̂ P− + D+ φ̂φ̂ P+ + transpose .
D2 =
2
(47)
Remarkably, about general normalized solutions to
Eq. (7), the kernel (47) has only two nonzero eigenvalues
λ± , with eigenvectors v± :
D2 v± =

g
λ± v± .
2

(48)

We construct v± from convenient, orthonormal “center”
and “edge” components,
s


sinh (ξ)
(vc )j =
xj−J/2 , 1 ≤ j ≤ J − 1,
sinh [(J − 1) ξ]
(49)
and zero otherwise, and
J−1
±x±( 2 ξ)
(ve )j=(J/2±J/2) = p
2 cosh [(J − 1) ξ]

and zero otherwise.

(50)

14
A term that appears in the solution for the eigenvalues
is abbreviated
s
 
1
R (ξ) ≡ 1 + tanh [(J − 1) ξ] tanh
ξ ,
(51)
2

≈

ζ is δ-correlated in z with weight g/N ,

in terms of which
λ± = 2 {±R (ξ) − 1} cosh [(J − 1) ξ]

 !2

sinh 12 ξ

sinh J+1
2 ξ

g
(58)
hζz ζz′ i = δ (z − z ′ ) ,
N
′
and drives the field φ̂ through the inverse of D0 , acting
on v− . In the symmetric phase λ+ = 0 and this is all
there is to the bare noise kernel; in the symmetry-broken
phase we must still handle (by other means) the term
ϕ · v+ , which however remains orthogonal to the v− in
the Langevin term. Integration over ϕ in the symmetric
phase produces

,

(52)
and the orthonormal eigenvectors
o
n p
p
1
v± = p
vc R (ξ) ± 1 ∓ ve R (ξ) ∓ 1 . (53)
2R (ξ)
For g ≤ gc , only ξ = 0 is consistent, and we get λ+ ≡ 0,
λ− = −



2
J +1

2

,

′

φ̂z =

(54)

(59)

0

is defined in terms of Eq. (46) by

D0 G0 (z, z ′ ) ≡ δ (z − z ′ ) .

(60)

D ′E
Note that from Eq. 59 we see that φ̂z = 0, which
implies that there are no corrections to the mean-field
result for the expectation value in the symmetric phase.

Hubbard-stratonovitch transformation about
the symmetric phase
C.

Rather than complete the square in Eq. (45) (á la Onsager and Machlup [48]), which is cumbersome for one
eigenvector, we introduce into Eq. (28) an auxiliary-field
representation of unity at each time:
Z
R
2
N
(55)
1 = N Dζ̃e− 2g dzζ̃ ,

E
D
2
2
(nJ − n0 ) − hnJ − n0 i

!2 +
′
′
φ̂J − φ̂0
√
.
= 1+N (J + 1)
2N/ (J + 1)
2
z
(61)
From the field equation (59) and the correlator (58) we
′
obtain the φ̂ noise

The net effect on L̂ is the shift
1 2
ζ̃ + L̂
2g

*

′

′

φJ − φ0
√
2

!2 +
z

g
= −λ−
N

Z z
0

dz ′

Fluctuations about the symmetric order
parameter

As an example we compute to lowest order the fluctuations in the order parameter about the symmetric phase,
where the diffusive Green’s function is easy to compute
in closed form. Application of the number operators
first to the basis |n) and then to the coherent-states in
Eq. (28) yields the connected component of the variance
(expressed in descaled fields)

in which N is a time- and field-independent normalization. Shifting the auxiliary field ζ̃ (a symmetry of the
measure), we introduce the physical Langevin field ζ as
p
(56)
ζ̃ ≡ ζ − g −λ− (ϕ · v− ) .
L̂ →

Z z
p
−λ−
dz ′ G0 (z, z ′ ) v− ζz′

 ′
as a field equation to Gaussian order, in which G0 z, z

with eigenvector v− = ve . This algebraic result emphasizes the efficiency of expanding about Poisson backgrounds for weakly perturbed stochastic processes. The
only deviation from Poisson which must be handled perturbatively comes from a single mode of ϕ, whose fluctuations represent exchanges between n0 and nj by Eq. (50).
These are of course the noise in the catalytic rates that
feeds back into the distribution as a whole.
B.

 g

p
′
1 2
2
ζ + ϕ D0 φ̂ − −λ− v− ζ + λ+ (ϕ · v+ ) .
2g
2
(57)



−1 0 · · · 0 1
√
2



· G0 (z, z ′) · v−

*

!2

,

(62)

15
and it remains only to compute the mode expansion of
the diffusion kernel in D0 from Eq. (46) in the uniform
¯
background φ̂ = 1/ (J + 1).
The symmetric-phase D0 contains a symmetric
linear diffusion matrix with endpoint corrections,
so its eigenvectors vk have components (vk )j =
Nk cos [θk + κk (j − J/2)], with Nk a normalization. The
eigenvalues are immediate on the interior sites,


g
κk
λk = 4 1 +
sin2 ,
(63)
J +1
2
and consistency of the interior with the endpoint corrections then determines κk and θk .
Either sin (J + 1) κk /2 = 0 ⇒ κk = πk/ (J + 1), k
even, and θk = 0, or cos θk = 0 ⇒ θk = π/2 and κk
solves the matching equation
tan

g
J +1
κk
=
tan
κk .
2
J + 1 + 2g
2

(64)

Eq. (64) is regular for k ≥ 3 odd, and creates only a
small wavenumber shift from the free diffusion solution,
leaving κk ≈ πk/ (J + 1). The important mode for critical behavior is k = 1 as g → gc , where κ1 → 0 as


1
1
κ21
1
.
(65)
→
−
6
(J + 1)2 g gc

D

E
(nJ − n0 )2 − hnJ − n0 i2
2N/ (J + 1)

≈1+

G0 (z, z ′ ) = Θ(z − z ′ )

(68)

j=−J/2

from the discrete sum for the k = 1 norm, because C → 1
at large J, but differs somewhat at the smaller J of more
likely biological interest.
The approximation (67) to the closed-form mode expansion for the variance of the order parameter is compared to numerical simulations in Fig. 10. We have continued the analytic expression through the critical point
to show the peak, though the character of the modes
rapidly changes as the distribution becomes skewed in
the symmetry-broken phase. A similar mode expansion
exists in this phase, but requires the relaxation eigenvectors and eigenvalues for asymmetric diffusion. We have
not computed these in closed form, and do not pursue
them numerically because in the symmetry-broken phase
fluctuations quickly come to be dominated by the center-

J+1
X

e−λk (z−z ) vk vkT .
′

(66)

k=1

Only odd-k modes from G0 couple to v− in Eq. (62), by
symmetry, and the wavenumber sums from k ≥ 3 are
easily approximated with a two-dimensional k integral.
We note that for all these modes Nk2 ≈ 2/ (J + 1), and
the only values that contribute to the inner product come
from j = ±J/2, giving sin2 (κk J/2) ≈ 1. Thus the nonsingular modes in the diffusion kernel provide a smooth
background approximately linear in g.
The leading contribution from the k = 1 mode occurs when it is present in both factors of G0 . For small
g − gc this mode is almost linear in j, with normalization
PJ/2
N1−2 → κ21 j=−J/2 j 2 . Evaluating this singular term
separately, with Eq. (63) for the eigenvalue and Eq. (65)
for the limiting value of the wavenumber, and then combining with the background from the regular modes, we
obtain the approximation

8g log (J + 1)
6

+C
π (J + 1)
J +1 1+

It is convenient to separate the constant

−2
J/2  2
3
j 
(J + 1)  12 X
C= 2
J (J − 1) J
J

In terms of these the modal expansion of the free
Green’s function is

g2


g
J+1

.

(67)

|g − gc |

of-mass behavior we derive below in Eq. (70).
Three main observations are important. First, the singularity in the variance has the leading-order approximation
E
D
2
2
(nJ − n0 ) − hnJ − n0 i
const ∼ 1
≈
, (69)
2N/ (J + 1)
(J + 1) |g − gc |
comparable to that of the mean-field Ising ferromagnet,
like the scaling of the order parameter. The variance
has weight 1/ (J + 1), because the lowest diffusive mode,
corresponding to the average magnetization, is the only
collective fluctuation participating in the phase transition
near the critical point.
D Second, we
E see that the weak-coupling scaling of
2
2
(nJ − n0 ) − hn0 − nJ i is that of Poisson noise for an
average of N/ (J + 1) particles per site. (This is shown
in the inset of Fig. 10.)
Third – and the reason we do not pursue the loworder expansion for the symmetry-broken-phase twopoint function – we see that for g ≫ gc the variance

16
0.002
2

10 1

var(n') / N

10

10 0

10

1

0
0

10

10

fit
data

0.0015

var(n’) / N2

10

var(n') / (2N/(J+1))

10 2

0.001

0.0005

g

-1

0
10

-2

-0.0005
0.5
10 0

g

D

E
2
2
(nJ − n0 ) − hn0 − nJ i goes to a universal form N/g
for any J. The independence of this scaling regime from
J indicates that the particles interact with one end of
the chain and the exogenous catalysis only, suggesting a
strong-coupling limit.
In addition, for large J, the center-of-mass equation (3)
predicts (for I = P ), in steady state for the symmetrybroken phase, that the variance will equal


1 hne i
(70)
hne i N 1 − −
g
N

where ne signifies whichever of the end sites 0 or J is
occupied (which depends on which of the two bistable
states is chosen). In Fig. 11 we plot the simulation data
for the variance for J + 1 = 100 against the estimate
from Eq. (70). For the value of hne i, we simply take the
value of the order parameter at the corresponding value
of g. As we see, this explains the form of the fluctuation
spectrum for large J very well. The fact that we are
able to replace the order parameter |hnJ − n0 i| by ne
demonstrates that this scaling regime is independent of
J as well and the particles only interact with one end of
the chain all through the symmetry-broken phase.
V.

LARGE EXCURSIONS

From the 1/g scaling of the Lagrangian term for the
Langevin field in Eq. (57) and the presence of unstable eigenvalues in the fluctuation kernel (45) about static

1.5

2

2.5

3

3.5

4

4.5

5

g

10 1

FIG. 10: Fluctuations in the order parameter scaled for g
above and below critical. var (n′ ) stands for the variance
(n0 − nJ )2 − hn0 − nJ i2 . Lines are leading-order expansion
of Eq. (67) in fluctuations about the symmetric mean-field solution, continued through gc ; symbols from simulation, J + 1
values and markers as in Fig. 8. Large panel shows convergence of var (n′ ) to N/g at all J. Inset shows convergence of
var (n′ ) to Poisson result 2N/ (J + 1) as g → 0.

1

FIG. 11: The fluctuation in the order parameter for J + 1 =
100 and N = 400 is plotted against the fit predicted by Eq.
70.

stationary backgrounds, we anticipate that perturbation
theory containing fluctuations associated with domain
flips will not converge [47], and that the rates for these
large excursions will be computed as an essential singularity with respect to the perturbation expansion. The
remarkable similarity to Hamiltonian dynamical systems
created by this method for treating generating functions
reduces the problem of estimating both escape trajectories and first passage times to that of identifiying the
heteroclinic network [49, 50] in the associated dynamical
system.
We construct the expansion appropriate to the secondorder transitions, beginning with the analysis of the exact stationary points corresponding to solutions of the
classical diffusion equation from arbitrary initial conditions. From the structure of these solutions, we identify
the “approximate stationary points” associated with domain flips, and compute the trajectory and action for
a low-dimensional example numerically. Comparisons to
simulation suggest that this calculation correctly predicts
the leading exponential dependence on particle number
of the residence time in domains in the symmetry-broken
phase.

A.

The expansion in semiclassical stationary points

We define the stationary-point expansion of the path
integral (28) implicitly by the requirement that the residual perturbation theory converge. In principle we must
include not only the (generally unique) exact stationary
point specified by the initial state |ψ0 ), but also a sufficient set of “approximate” stationary points associated
with states that converge exponentially fast toward |ψ0 ),
with respect to prediction of late-time observables. In
this representation using generating functionals for probability distributions over spaces of histories, a “stationary

17


¯
¯ φ̂
point” refers to any full path φ̃,
satisfying the clas-

sical condition that the linear variations of L (including
time-derivative terms) vanish:
∂L
∂ φ̃

= 0;

∂L
= 0.
∂φ

(71)

If φ̃ = 0, the solution of Eq. (42) solves the above to
recover the mean-field solutions; in this section we relax
the requirement φ̃ = 0 to uncover a larger set of solutions
which result in a nonzero value for L.
Formally, then, the removal of the stationary-point
contribute leads to the functional form


X
aj  |ψt ) =
(0| exp 
j

R

X −N R dzL̂¯ Z
¯
′ −N
dz L̂−L̂ φ̃0 ·(n̄−φ0 )
e
Dϕ Dφ̂ e
e
,
¯ ¯
φ̃,φ̂

(72)


¯
¯
¯ φ̂
where L̂ denotes L̂ φ̃,
. As perturbative corrections

scale as powers of 1/N , by Eq. (62), to leading order
′
¯
we will treat L̂ − L̂ as a quadratic form in ϕ and φ̂ , of



(0| exp 

X
j



aj  |ψt ) =

∞
X
e−nS0

n=0

n!

T

Z

1 −S0
.
e
ζ0

We will check that the transition times of the instantons are finite and that they converge exponentially to
the static backgrounds, so that when they are improbable the dilute-gas sum is well defined. As we verify below,
¯
the classical solutions all have φ̃ ≡ 0 and zero action, and
R ¯
we denote by S0 the action N dz L̂ associated with a single instanton. Letting 1/ζ0 denote the Jacobean relating
the null eigenvalue to the measure for z-translation of the
instanton, we recast the sum in Eq. (72) as

dz1
,...,
ζ0

in which T denotes time-ordering in z of the positions of
the instantons. The presence of n factors of 1/ζ0 in the ninstanton determinant follows from the product structure
of functional determinants and the wide separation of
finite supports in z where the background differs from
that of a steady state [35].
Like the computation of the energy shift in the equilibrium double-well problem, we see that observables relating to persistence within a domain will receive contributions from the even terms in the sum over n, while
those relating to domain flips will receive contributions
from the odd terms. The likelihood of persistence decays
exponentially in z at early times with rate
rflip =

the form (45), now about more general time-dependent
backgrounds.
P
The formal sum φ̃,
¯ ¯ is properly a discrete sum in the
φ̂
number n ∈ 0, . . . , ∞ of domain flips, of a time-ordered
integral over their positions {z1 , . . . , zn }. The integral
is necessary [35], because as the domain flips converge
toward true stationary points, the fluctuation generated
by time translation of any solution becomes a null eigenvector of the functional determinant about that solution.
(This is a variant on Goldstone’s theorem [46], associated
with the time-translation symmetry spontaneously hidden by the instanton [45].) This eigenvector is replaced
by the integral (with a Jacobean), and the remaining
functional determinant is a product of positive eigenvalues, by construction.

(74)

The computation of the instanton action S0 , which is
responsible for the leading exponential dependence of rflip
is most easily carried out within the complete analysis of
the semiclassical stationary points, beginning with the
classical diffusion solutions.

Z

B.

dzn
ζ0

Z

′

Dϕ Dφ̂ e

−N

R

¯
dz L̂−L̂



eφ̃0 ·(n̄−φ0 ) ,

(73)

Action-angle variables and the structure of the
Hamiltonian

¯
¯ and φ̂
do not
The equations of motion (37,38) in φ̃
directly give the evolution of the physical particle numbers, or efficiently use the symmetries of Sec. III D. To
do both, it is convenient to transform the background
¯
fields as φ¯† j ≡ eσj , and φ̂j ≡ νj e−σj . νj is then the semiclassical approximation to the relative number hnj i /N .
This change of variables is equivalent to an action-angle
transformation in classical mechanics [51], and we check
in Ref. [45] that as well as producing a more convenient
form for the action, it leads to the correct measure for
fluctuations. The Lagrangian (34) retains a simple kinetic term, up to a total derivative:
¯
L̂ = σ · ∂z ν + Ω̂ (σ, ν) ,

(75)

and the equations of motion in the new variables become,
respectively,
∂z νj = −

∂ Ω̂
,
∂σj

(76)

18
and

+
∂ Ω̂
.
∂z σj =
∂νj

σ̄ ≡

j=0

(77)

With the interpretation of the number field ν as a position, and σ its canonically conjugate momentum, −Ω̂
becomes the correctly signed Hamiltonian for classical
solutions. The conservation law dΩ̂/dz = 0 is mathematically a conservation of energy, but the particular
value Ω̂ ≡ 0 associated with all stationary points initiated by classical distributions is a distinctive feature of
this stochastic-process application of Hilbert-space methods.
The global symmetry whose Noether charge is total
number becomes immediate in action-angle variables.
Defining
J
1 X
σj ,
J + 1 j=0

(σj − σ̄) ∂z νj + Ω̂ (σ, ν) ,
(79)

in which σ̄ multiples the z-derivative of conserved total
number in the first line, and only differences σi − σj appear in either the kinetic term or the Ω̂ of the second
line.
To expose the structure of the associated dynamical
system, and to make the terms in it readily visualizable
from the mean-field diffusive solutions, we perform a final
transformation by introducing the log ratio of particle
fluxes between sites j and j + 1,



(1 + gνJ ) νj
1
.
rj+1,j ≡ log
2
(1 + gν0 ) νj+1

(78)

the Lagrangian becomes


J
X
νj 
L̂ = σ̄∂z 

J
X

(80)

In terms of these the σ-dependence of Ω̂ may be simplified
to read

j=0

J−1
X √
p
νj+1 νj [cosh (rj+1,j ) − cosh (σj − σj+1 − rj+1,j )] .
Ω̂ (σ, ν) = 2 (1 + gν0 ) (1 + gνJ )

(81)

j=0

The one-dimensional geometry we have assumed for the graph of phosphorylation and dephosphorylation transitions
makes possible the definition of a function σ(ν) at each number configuration, satisfying
σj+1 (ν) − σj (ν) = −rj+1,j ,

(82)

(up to a convention for specifying σ̄ at each ν, which we may take to be arbitrary). σ(ν) is a reference point for the
canonical momentum coordinate σ, and σ − σ(ν) functions as the kinematic momentum for this system.
We may see this by introducing the Hamiltonian potential function
J−1
X√
p
νj+1 νj [cosh (rj+1,j ) − 1] ,
V (ν) = 2 (1 + gν0 ) (1 + gνJ )

(83)

j=0

in terms of which
J−1
n
h
i
o
X√
p
− Ω̂ (σ, ν) = 2 (1 + gν0 ) (1 + gνJ )
νj+1 νj cosh (σ − σ(ν))j − (σ − σ(ν))j+1 − 1 − V (ν) .

(84)

j=0

To leading order the explicit cosh in Eq. (84) is simply a quadratic form in σ − σ(ν), with a matrix of inverse masses defined by the remaining square-root terms.
When σ − σ(ν) = 0, Eq. (76) shows that ∂z ν = 0, verifying the interpretation of σ − σ(ν) as the kinematic momentum. Furthermore, if this kinematic momentum van-

ishes at any local minimum of V (ν), Eq. (77) shows that
∂z σ = 0, hence ∂z (σ − σ(ν)) = 0. The local minima satisfy V (ν) = 0 and are attained only when each rj+1,j = 0
independently, because the cosh terms in Eq. (83) are
never negative. These are of course exactly the (stable
and saddle-point) mean-field solutions with particle ex-

19

0.2

0.15

0.1

0.05

0

-0.05

0.6

0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

horizontal displacement on the unit simplex

0.4
vertical displacement on the unit simplex

In Fig. 13, we directly compute the trajectory of the
reverse bounded path, by integration along the saddle
instability of the equations of motion (76,77). The fact
that it nearly retraces the classical diffusive direction of
slowest flow checks the approximation that both trajectories are dominated by the potential −V (ν) itself.

vertical displacement on the unit simplex

change between adjacent sites obeying detailed balance.
We identify them in graphs below as the fixed points of
the classical diffusion equation.
It can be shown [45] that, as long as the quadratic expansion in σ is a good approximation, and as long as the
effective mass terms implicit in Eq. (84) are not a strong
function of ν (which we will verify), all stationary points
of the action closely approximate ordinary mechanical
trajectories in the potential −V (ν), with position coordinate ν and kinematic momentum σ−σ(ν). For the classical solutions σ ≡ 0, shown in Fig. 12, the unbounded trajectories are those that originate in non-equilibrium initial conditions and converge exponentially slowly on the
saddle or stable fixed points. The two bounded trajectories, between the saddle and either stable fixed point,
travel along the saddle path of the potential, −V (ν),
which is bounded above by 0 and unbounded below, and
make up part of the heteroclinic network [49, 50] of the
associated hyperbolic system.

0.2

FIG. 13: Flowfield of the instanton solution in J = 2, for
values ξ = 1, so g ≈ 4.0862. Fine lines are classical diffusion
solution from Fig. 12, and bold line is the instanton.

0
-0.2
-0.4
-0.6
-0.8
-1
-1.2
-1.4
-1

-0.5

0

0.5

1

horizontal displacement on the unit simplex

FIG. 12: Classical flowfield of the particle numbers νj for
P2
J = 2, shown on the simplex
ν ≡ 1. Upper left corner
j=0 j
is n0 = 1, upper right corner is n2 = 1, and bottom is n1 = 1.
Dots are a selection of initial conditions, and classical diffusion
solutions are the flowlines emanating from them. The uniform
distribution νj = 1/3 (open circle) is the saddle point, and
the stable fixed points (heavy dots) are attractors.

For ordinary mechanical flow, we know that the full
heteroclinic network consists of trajectories running both
ways between the stable and saddle fixed points. If this
were a purely mechanical system, the reverse trajectories would be strict time-reversal images of the bounded
classical diffusion trajectories. (Note that an exact reversal (σj − σj+1 ) → 2rj+1,j − (σj − σj+1 ) would also leave
Ω̂ = 0.) Here, a small ν-dependence of the effective mass
terms causes them to differ slightly from each other and
from the saddle path over −V (ν).

For an instanton in a classical equilibrium field theory,
the conjugate and the kinematic momentum would be
the same quantity. Both forward and reverse trajectories
along the saddle path in the potential −V (ν) would have
locally minimum but non-zero action, and in that sense
both would be “non-classical” trajectories [35]. The distinctive feature of the path integrals associated with master equations of the form we have considered here is the
offset σ(ν) from the canonical momentum that appears
in the kinetic term of the Lagrangian (75) to the kinematic momentum. This offset is responsible for S ≡ 0 for
all diffusion solutions, including the bounded trajectories
from saddle to stable fixed points, and it approximately
doubles the value of the Lagrangian (75) along the reverse trajectories. The value of this Lagrangian, along
the numerically determined path of Fig. 13, is shown in
Fig. 14. Like the Lagrangian for a classical problem,
it is positive definite, and approximates the WKB integral for barrier
p except with an extra factor of 2:
R √ escape,
S ≈ 2N
dν T mdν 2V (ν), where dν is a length element on the coordinate ν, and m is the matrix of effective
mass values implied by Eq. (84). This approximate form
follows simply from the nearly time-reverse character of
escapes versus classical paths of slowest-diffusion, and
may be derived from the original Gaussian-order approximation to such escapes by Onsager and Machlup [48].
Readers seeking a systematic derivation, including the
Onsager-Machlup small-fluctuation approximation, may
find these in Ref. [39] or Ref. [45].

20

4.5

x 10

-3

7. 5

7

3.5
6. 5

3
log τ

descaled Lagrangian density L

^

4

2.5

6

ﬁt (d log τ / dN) = 0.023

2
1.5

5. 5

1
5
50

0.5

60

70

80

90

100

110

120

130

N

0
0

5

10

15

20

25

time(z)

FIG. 14: Linear-scale plot of the Lagrangian density per
¯
particle L̂ of the instanton trajectory. A logarithmic plot
of the same quantity (not shown) demonstrates exponential
decay toward zero at early and late times.

¯
For the parameter values of Fig. 13, the integral dz L̂
under the curve of Fig. 14 converges to a value near
0.0206. Fig. 15 compares numerical estimates of the residence time in this model, inverse to the rate rflip of
Eq. (74), to particle number N . The slope of the logR ¯
arithm of 1/rflip should be dS0 /dN = dz L̂, up to corrections decaying as 1/N , and we observe quantitative
agreement with the numerical estimate of the instanton
to ∼ 10%.
Although we do not pursue the analytic forms in this
paper, the dependence of the coefficient of N (giving decay times[58]) on number of sites J and the distance from
criticality g − gC may also be found from simulations.
Fig. 16 symmarizes these numerical results, showing that
the dependence on small-integer J is roughly linear, and
the dependence on g − gC < 1 is weakly nonlinear.
R

C.

Summary of semiclassical results

We have seen that the classical “action” for this
reaction-diffusion theory, once constructed, yields quite
nicely the two extremes of behavior of interest in cooperative intermolecular phase transitions. The classical
stationary points coincide exactly with the usual massaction differential equations. Corrections to these from
cubic and higher-order fluctuation effects are readily incorporated (for an example, see Ref. [45]), but to the
resolution of our simulations, we cannot identify a need
for such corrections at these parameter values, so we have
not pursued them.
The nonclassical stationary trajectories are the projec-

FIG. 15: Plot comparing residence times to particle number
for the parameters of Fig. 14. Slope of numerical estimates,
R ¯
which should correspond to dS0 /dN = dz L̂ is best fit by
0.023, while direct integration under the curve of Fig. 14 yields
0.0206.

tion from this (2J + 2)-dimensional configuration space,
onto the one-dimensional path most likely to destabilize
the symmetry-broken phase, which closely approximates
the path of slowest diffusive correction. The methods
shown here therefore provide a compact and convenient
way to estimate the escape trajectories and first-passage
times for even quite richly structured nonlinear diffusion
processes of this kind. These methods, originally developed for applications to reaction-diffusion theory, are
increasingly finding applications in epigenetics [42, 44]
and systems biology [40] where particle numbers may be
small, making fluctuation effects important, while at the
same time the structure of the state space remains complex to describe.
The reduction to a one-dimensional system was assumed given, in the treatment in Ref. [13] of a switching
system comparable to ours; we have shown here a systematic approach to estimating such escape trajectories. We
have also verified that the action of the instanton, easily numerically integrated once the trajectory is found,
produces both the correct N scaling, and good quantitative agreement, with the domain residence times. We
expect that, while the treatment of the functional determinant will be more difficult for metastable domains in
first-order transitions, the classical-level analysis comparable to ours will be similar, and roughly as effective.

VI.

DISCUSSION AND CONCLUSIONS

We have tried to idealize in a reasonable way a large
class of biomolecular signal transduction systems, and
to apply the most complete formalism available to decompose and quantitatively estimate their properties as

21
20

A.

a

J=5

J=4

log τ

15

J=3
10

J=2, g=4.086
J=2, g=4
5

50

70

60

80

90

100

N

16

b

14

log τ

12

10

Technical advances

The operator treatments of gene-expression switching [7] extended traditional mass-action models to include perturbative noise from first principles. We have
further extended the operator methods to a path-integral
treatment, which adds an intuitive and computationally
tractable approach to large deviations.
We have demonstrated that expansion of weakly nonlinear stochastic processes about Poisson backgrounds
leads to very efficient perturbative schemes for correcting the full probability distribution (not very surprising in retrospect), and that in our particular idealized
model, the entire noise spectrum is driven by a single
bare Langevin field (perhaps somewhat more surprising,
and not noticed before).
Finally, we have shown that the nonlinear projection
of the full master equation onto the dominant trajectory participating in domain flips approximately, but not
exactly, reverses the unique trajectory of slowest diffusive correction in the classical flow. We have recovered
the exponential in N characteristic of extensive largedeviations scaling [43], and shown how to estimate the exact coefficient to refine the bounds of order unity that are
conventionally (and usually correctly) assumed in pure
scaling arguments [13].

8

B.

6

4

0

0.1

0.2

0.3

0.4
0.5
g − gC

0.6

0.7

0.8

FIG. 16: Plot of expected residence times τ from simulations
in the symmetry-broken state as functions of J, N , and distance of the coupling strength from its critical value, g − gC .
(a): log √
τ vs. N for J ∈ {2, . . . , 5}. In simulations I ≡ P ,
g = N/ IP is held constant, and g − gC is held equal to
1. Green curve for J = 2 and g = 4.0862 corresponds to
the value ξ ≡ 1, which we have computed analytically, corresponding to the coefficient d log τ /dN shown in Fig. 15. (b):
log τ vs. g − gC for values J ∈ {2, . . . , 9} (from bottom to
top) at N = 50.

switches. Our results thus combine a number of technical advances in recognized domains, with several conceptual insights relevant to the robustness and evolution of
devices. Of necessity in a short treatment, our idealizations of feedback and single timescales for all microscopic
motion have abstracted away from some important problems of connection with phenomenological models of real
regulatory protein systems.

Biological insights

The most concrete of our results for biologists seeking to understand the function of signal-transduction cascades and switches is that particle number (N ), as well as
exogenous kinase (I) and phosphatase (P ) numbers, can
be used to control the onset of switching, and in cases
of asymmetric topology, also the preferred domain of the
switch. The control through N offers a feedback from
gene expression into the function of the cascade, which
apparently has not been considered earlier.
We have demonstrated through the mode expansion
in the neighborhood of the phase transition, that only
the lowest-eigenvalue collective fluctuation of the diffusion operator induces the instability to symmetry breaking, and scales the divergence in the noise spectrum. For
large J, we can also predict fluctuations in the symmetrybroken phase because of a simplification induced by the
fact that the system senses only one boundary in the entire symmetry-broken phase. This enables us to simplify
an exact equation for the center-of-mass of the system to
predict fluctuations.
More abstractly, we have distinguished a mechanism
for switching based purely on population-level polarization of the protein pool, from mechanisms which depend
on limiting one or more transition rates through restrictions on catalytic kinetics. Polarization-based mechanisms make the function of the switch dependent on its
catalytic topology and concentrations, but not on kinetic
factors, a separation that has been proposed as a route to

22
modularity. We hope that such distinctions can at some
point be incorporated in evolutionary models that make
quantitative use of the structure of phenotypically neutral networks, where we hope they will explain at least
part of the ubiquity of multiple phosphorylation and nonspecific catalysis in cascades of the type we have considered.

DES thanks Insight Venture Partners for support of
this work. SK was supported by the swedish research
council.

[1] J. von Neumann. Probabilistic logics and the synthesis
of reliable organisms from unreliable components. Automata Studies, 34:43–, 1956.
[2] G. von Dassow, E. Meir, E. M. Munro, and G. M. Odell.
The segment polarity network is a robust developmental
module. Nature, 406:188, 2000.
[3] H. M. Sauro. The computational versatility of proteomic
signaling networks. Current Proteomics, 1:67, 2004.
[4] J. E. Jr. Ferrell. Xenopus oocyte maturation: new lessons
from a good egg. Bioessays, 21:833, 1999.
[5] J. E. Jr. Ferrell. Building a cellular switch: more lessons
from a good egg. Bioessays, 21:866, 1999.
[6] J. J. Tyson, A. Csikasz-Nagy, and B. Novak. The dynamics of cell cycle regulation. Bioessays, 24:1095, 2002.
[7] M. Sasai and P. Wolynes. Stochastic gene expression
as a many-body problem. Proc. Nat. Acad. Sci. USA,
100:2374–2379, 2003.
[8] A. Goldbeter and D. E. Koshland. An amplified sensitivity arising from covalent modification in biological
systems. Proc. Nat. Acad. Sci. USA, 78:6840–6844, 1981.
[9] C. Y. Huang and J. E. Jr. Ferrell.
Ultrasensitivity in the mitogen-activated protein kinase cascade.
Proc. Nat. Acad. Sci. USA, 93:10078, 1996.
[10] J. J. Tyson, K. C. Chen, and B. Novak. Sniffers, buzzers,
toggles and blinkers: dynamics of regulatory and signaling pathways in the cell. Curr. Opin. Cell Biol., 15:221,
2003.
[11] J. E. Ferrell and W. Xiong. Bistability in cell signaling:
How to make continuous processes discontinuous, and
reversible processes irreversible. Chaos, 11:227, 2001.
[12] J. E. Lisman. A mechanism for memory storage insensitive to molecular turnover: a bistable autophosphorylating kinase. PNAS, 82:3055, 1985.
[13] W. Bialek. Stability and noise in biochemical switches.
In T. K. Leen, T. G. Dietterich, and V. Tresp, editors,
Advances in Neural Information Processing, Cambridge,
2001. MIT Press.
[14] D. Kültz and M. Burg. Evolution of osmotic stress signaling via map kinase cascades. J. Exp. Biol., 201:3015,
1998.
[15] Jeremy Gunawardena. Multisite protein phosphorylation makes a good threshold but can be a poor switch.
Proc. Nat. Acad. Sci. USA, 102:14617–14622, 2005.
[16] Salazar, C. and Höfer, T. Versatile reglation of multisite
protein phosphorylation by the order of phosphate processing and protein-protein interactions. FEBS journal,
274:1046–1061, 2007.
[17] A. Kreegipuu, N. Blom, and S. Brunak. Phosphobase,
a database of phosphorylation sites: release 2.0. Nucleic
Acids Res., 27:237, 1999.
[18] N. I. Markevich, J. B. Hoek, and B. N. Kholodenko.
Signaling switches and bistability arising from multisite

phosphorylation in protein kinase cascades. J. Cell
Biol., 164:353–359, 2004.
[19] G. Craciun, Y. Tang, and M. Feinberg. Understanding
bistability in complex enzyme-driven reaction networks.
Proc. Nat. Acad. Sci. USA, 103:8697–8702, 2006.
[20] L. W. Ancel and W. Fontana. Plasticity, evolvability
and modularity in rna. J. Exp. Zool. (Mol. Dev. Evol.),
288:242–283, 2000.
[21] W. Fontana. Modeling ‘evo-devo’ with rna. Bioessays,
24:1164–1177, 2002.
[22] K. Takahasi, S. Tanase-Nicola, and P. Rein ten Wolde.
Spatio-temporal correlations can drastically change the
response of a mapk pathway. PNAS, 107:2473–2478,
2010.
[23] B. N. Kholodenko. Negative feedback and ultrasensitivity can bring about oscillations in the mitogen-activated
protein kinase cascades. Eur. J. Biochem, 267:1583–
1588, 2000.
[24] R. Heinrich, B. G. Neel, and T. A. Rapoport. Mathematical models of protein kinase signal transduction.
Mol. Cell., 9:957–970, 2002.
[25] X. Wang, N. Hao, H. G. Dohlman, and T. C. Elston.
Bistability, stochasticity and oscillations in the mitogenactivated protein kinase cascade. Biophys. J., 90:1961–
1978, 2006.
[26] Orsolya Kapuy, Debashis Barik, Maria Rosa Domingo
Sananes, John J. Tyson, and Béla Novák. Bistability by multiple phosphorylation of regulatory proteins.
Prog. Biophys. Mol. Biol., 100:47–56, 2009.
[27] B. Novak, Z. Pataki, A. Ciliberto, and J. J. Tyson. Mathematical model of the cell division cycle of fission yeast.
Chaos, 11:277, 2001.
[28] J. Paulsson and M. Ehrenberg. Noise in a minimal regulatory network: plasmid copy number control. Q. Rev. Biophys., 34:1, 2001.
[29] Supriya Krishnamurthy, Eric Smith, David C. Krakauer,
and Walter Fontana. The stochastic behavior of a molecular switching circuit with feedback. Biology Direct, 2:13,
2007. doi:10.1186/1745-6150-2-13.
[30] J. E. Ferrell and R. R. Bhatt. Mechanistic studies of
the dual phosphorylation of mitogen-activated protein kinase. J. Biol. Chem., 272:19008–19016, 1997.
[31] W. R. Burack and T. W. Sturgill. The activating dualphosphorylation of mapk by mek is nonprocessive. Biochemistry, 36:5929–5933, 1997.
[32] S. Gaudet, K. A. Janes, J. Albeck, E. A. Pace, D. A.
Lauffenburger, and P. K. Sorger. A compendium of signals and responses triggered by prodeath and prosurvival
cytokines. Mol. Cell Proteomics, 10:1569–1590, 2005.
[33] M. Kravanja, R. Engelmann, V. Dossonnet, M. Blüggel,
H. E. Meyer, R. Frank, A. Galinier, J. Deutscher,
N. Schnell, and W. Hengstenberg. The hprk gene of en-

VII.

ACKNOWLEDGEMENTS

23
terococcus faecalis encodes a novel bifunctional enzyme:
J. Phys. C, 11:L321 – L328, 1987.
the hpr kinase/phosphatase. Mol. Microbiol., 31:59–66,
[48] L. Onsager and S. Machlup. Fluctuations and irreversible
1999.
processes. Phys. Rev., 91:1505, 1953.
[34] A. J. Ninfa. Protein phosphorylation and the regulation
[49] John Gluckheimer and Philip Holmes. Structurally staof cellular processes by the homologous two-component
ble heteroclinic cycles. Math. Proc. Cam. Phil. Soc.,
regulatory systems of bacteria. Genet. Eng., 13:39–72,
103:189–192, 1988.
1991.
[50] John Gluckheimer and Philip Holmes. Nonlinear Oscil[35] Sidney Coleman. Aspects of symmetry. Cambridge, New
lations, Dynamical Systems, and Bifurcations of Vector
York, 1985.
Fields (Applied Mathematical Sciences vol.42). Springer,
[36] Daniel C. Mattis and M. Lawrence Glasser. The uses
Berlin, 2002.
of quantum field theory in diffusion-limited reactions.
[51] Herbert Goldstein, Charles P. Poole, and John L. Safko.
Rev. Mod. Phys, 70:979–1001, 1998.
Classical Mechanics. Addison Wesley, New York, third
[37] Gregory L. Eyink. Action principle in nonequilibrium
edition, 2001.
statistical dynamics. Phys. Rev. E, 54:3419–3435, 1996.
[52] Alex Kamenev.
Keldysh and doi-peliti tech[38] J.
Cardy.
Field
theory
and
nonniques for out-of-equilibrium systems.
pages
equilibrium
statistical
mechanics.
1999.
arXiv:cond–mat/0109316v2, 2001.
Lecture notes
presented at Windsor NATO school on “Field Thehttp://www-thphys.physics.ox.ac.uk/users/JohnCardy/home.html.
ory of Strongly Correlated Fermions and Bosons in
[39] Eric Smith. Large-deviation principles, stochastic effecLow-Dimensional Disordered Systems” (August 2001).
tive actions, path entropies, and the structure and mean[53] L. V. Keldysh. Diagram technique for nonequilibrium
ing of thermodynamic descriptions. Rep. Prog. Phys.,
processes. Sov. Phys. JETP, 20:1018, 1965.
74:046601, 2011. http://arxiv.org/submit/199903.
[54] P. C. Martin, E. D. Siggia, and H. A. Rose. Statistical
[40] N. A. Sinitsyn, Nicalas Hengartner, and Ilya Nemenman.
dynamics of classical systems. Phys. Rev. A, 8:423–437,
Adiabatic coarse-graining and simulations of stochas1973.
tic biochemical networks. Proc. Nat. Acad. Sci. USA,
[55] This form is originally due to Onsager and Machlup [48].
106:10546–10551, 2009.
[56] See Ref. [52] for a thorough development of fluctua[41] Daniel T. Gillespie. Why quantum mechanics cannot be
tions in both Doi-Peliti formulation of stochastic proformulated as a markov process. Phys. Rev. A, 49:1607–
cesses, and two-field methods more generally including
1612, 1994.
the Keldysh [53] and Martin-Siggia-Rose methods [54].
[42] E. Aurell and K. Sneppen. Epigenetics as a first exit
In these theories, Green’s functions describe the response
problem. Phys. Rev. Lett., 88:048101:1–4, 2002.
of either the observable or moment-sampling fields (φ or
[43] Hugo Touchette.
The large deviation approach to
φ† ) to point sources. They are the basis for Langevin and
statistical mechanics.
Phys. Rep., 478:1–69, 2009.
other expansions for the treatment of noise.
arXiv:0804.0327.
[57] Negative eigenvalues of this Hessian matrix correspond
[44] David Marin Roma, Ruadhan A. O’Flanagan, Andrei E.
to decaying modes in the usual sense. The apparent diRuckenstein, and Anirvan M. Sengupta. Optimal path to
vergence caused by the negative sign with which the Liepigenetic switching. Phys. Rev. E, 71:011902:1–5, 2005.
ouville operator L appears is canceled when the complex
[45] Eric Smith and Supriya Krishnamurthy. Symmetry and
conjugate fields φ∗j – considered as independent variables
collective fluctuations in evolutionary games. 2011. SFI
of integration from φj – are rotated to an imaginary inworking paper #11-03-010.
tegration contour.
[46] Steven Weinberg. The quantum theory of fields, Vol. II:
[58] In large-deviations terminology, this coefficient is called
Modern applications. Cambridge, New York, 1996.
the rate function [43].
[47] J. L. Cardy. Electron localisation in disordered systems
and classical solutions in ginzburg-landau field theory.
