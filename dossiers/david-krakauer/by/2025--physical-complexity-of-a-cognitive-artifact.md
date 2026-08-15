---
title: "Physical Complexity of a Cognitive Artifact"
person: david-krakauer
section: by
type: journal-article
year: 2025
date: 2025
venue: "arXiv (preprint)"
authors: "David C. Krakauer et al."
source_url: https://arxiv.org/abs/2509.12495
retrieved: 2026-08-13
content: full-text
notes: "arXiv preprint, open access. Extracted via pypdf from arXiv PDF."
---

# Physical Complexity of a Cognitive Artifact

## Full text

Physical Complexity of a Cognitive Artifact
G¨ulce Kardes ¸
Department of Computer Science, University of Colorado Boulder, Boulder, CO, USA and
Santa Fe Institute, Santa Fe, NM, USA
David Krakauer
Santa Fe Institute, Santa Fe, NM, USA
Joshua A. Grochow
Department of Computer Science, University of Colorado Boulder, Boulder, CO, USA and
Department of Mathematics, University of Colorado Boulder, Boulder, CO, USA
(Dated: September 9, 2025)
Cognitive science and theoretical computer science both seek to classify and explain the difficulty
of tasks. Mechanisms of intelligence can be understood as leading to reductions in task difficulty. We
map concepts from the computational complexity of a physical puzzle, the Soma Cube, onto cognitive
problem-solving strategies through a “Principle of Materiality”. By analyzing the puzzle’s branching
factor, measured through search tree outdegree, we quantitatively assess task difficulty and systemati-
cally examine how different strategies modify complexity. We incrementally enhance a trial-and-error
tree search with preprocessing (cognitive chunking), value ordering (cognitive free-sorting), variable
ordering (cognitive scaffolding), and pruning (cognitive inference). We discuss how the competent
use of artifacts reduces time complexity through the exploitation of physical constraints, and propose
a model of intelligence as a library of algorithms exploiting the capabilities of both mind and matter.
I. INTRODUCTION
There are currently two well established domains for
studying general problem solving. The first describes
strategies used by humans on both experimental and
real-world tasks. Human problem solving is captured
through a number of frameworks including skill acqui-
sition [1] and automaticity [2], the application of expert
knowledge [3, 4], the use of heuristics [5, 6], reinforce-
ment learning and conditioning [7, 8], Bayesian infer-
ence [9, 10], analogy making [11, 12], collective intel-
ligence and cognition [13, 14], simulation intelligence
[15], the use of external representations [16, 17] and the
synergy of mind and matter through exbodiment [18].
The second domain, computational problem solving,
investigates algorithms that enable computers to tackle
problems effectively. Within this domain, two branches
especially pertinent to the present question are: (i) com-
putational complexity theory, which analyzes the re-
sources (time, memory, etc.) required to solve prob-
lems as functions of input size, typically in the asymp-
totic limit; and (ii) the study of search algorithms, which
seeks efficient solutions to specific tasks (e.g., games
and puzzles) by exploiting the combinatorial structure
of state spaces, often via heuristics [19–22].
Although both humans and computers have been
shown to be capable of solving a large set of common
tasks [23, 24], and there is an extensive literature com-
paring natural and artificial intelligence [10, 25, 26],
comparing human and computer problem-solving re-
mains challenging. One problem is that algorithms can
be viewed as “white boxes” designed by humans to solve
problems efficiently, whereas human problem solving is
a “black box” evolved (or learned) to solve problems,
that can only be probed indirectly. Even with care-
fully constructed benchmarks, it is not at all obvious
whether humans and computers are really solving the
same problems [27].
Here, we present a new approach to the challenge
of making analogies between these two approaches
by mapping formal properties of search algorithms
onto the existing literature on experimentally observed
mechanisms of cognition. We seek to establish a com-
mon language for well-established phenomena from
both problem-solving domains. Using narrowly defined
problems [28] or benchmarks [29], which retain suf-
ficient richness to permit diverse solutions but whose
configuration space is modest enough to be amenable to
analysis, we set out on a path towards a convergence of
these perspectives. Our crucible for accomplishing this
goal will be the analysis of algorithmic puzzle-solving
applied to a physical artifact, the Soma Cube.
II. PHYSICAL ARTIFACT AND LOGICAL PUZZLE: THE
SOMA CUBE AND THE PRINCIPLE OF MATERIALITY
The Soma Cube is a 3D puzzle made of seven distinct
polycubic pieces. The goal is to assemble the pieces into
a 3×3×3 cube with no gaps (Fig. 1). There are 240
essentially distinct solutions to the Soma Cube, treating
solutions that are rotations or reflections of one another
as equivalent [30].
arXiv:2509.12495v1  [cs.AI]  15 Sep 2025

2
Figure 1. The seven pieces of the Soma Cube. In the original
puzzle these are not colored and color plays no part in the final
solution. We use a consistent coloring scheme throughout for
expositional purposes. Also shown is one of the 240 solutions
of the Soma cube: a 3×3×3 cube with no gaps or “voids” in
the structure.
The puzzle also serves as a physical realization of an
abstract mathematical problem, which can be expressed
in a variety of different formalisms. For example, there
are various Boolean formulae whose satisfying assign-
ments correspond to solutions of the Soma Cube, one
of which is shown in part in Fig. 2—an instance of the
Boolean Satisfiability (SAT) problem. The complete for-
mulaΦconsists of constraints that encode the valid
placements and orientations of the seven pieces within
the cube (the details of this encoding can be found in
App. A).
The physical Soma Cube and its abstract SAT formula-
tion are in some sense representations of the same puz-
zle. However, human solvers find the physical puzzle
to be tractable, whereas the corresponding SAT puzzle
with more than 10 5 clauses is intractable for humans
to solve through direct reasoning. This stark contrast
in solvability underscores a broader principle: sensi-
tivity to problem representation. The way a problem
is framed shapes its state space, and the combinatorial
properties of that space ultimately determine its com-
plexity, whether for human cognition, AI, or other algo-
rithms [31].
We represent the state space of the Soma Cube as a
configuration graphG P = (V P , EP ), where the vertices
VP encode distinct piece configurations, and the edges
EP ={(u, v) :u, v∈V P}encode legal single-step moves
between states (adding or removing a piece). Most nat-
ural solvers of the Soma Cube (beyond naive enumer-
ation) operate on a search space graphG S = (V S , ES)
that is a subgraph of the full configuration graphG P
[32]. The efficiency of a solver depends largely on the
structure and size of the search space it explores, as the
combinatorial properties ofG S directly impact compu-
tational complexity. Analyzing the combinatorial prop-
Figure 2. A fragment of the k-SAT formulation of the Soma
Cube puzzle. The variablesP ijkl represent whether pieceloc-
cupies position (i, j, k) in the 3×3×3 cube. Although only a
small portion is shown here, the complete formulation con-
sists of over 150,000 clauses that enforce both piece place-
ment and cell coverage constraints, ensuring that every piece
is used exactly once and every cell in the cube is occupied by
one piece.
erties of the state space graph uncovers determinants of
the problem’s difficulty and informs the algorithms best
suited to solve it (see App. B).
Among the many combinatorial properties of (the
state space of) this puzzle, we focus on analyzing its
branching factors, which provide a broad overview of
the complexity of both the configuration graphG P and
the search space graphsG S. The branching factor mea-
sures the number of possible moves available from any
given configuration when solving the puzzle. In triv-
ial puzzles, choices at each step are limited, whereas
more complex puzzles present multiple valid options,
expanding the search space. In the full configuration
graphG P of the Soma Cube puzzle, we find (Fig. 3(b))
that the branching factor varies significantly even at
depth 1 (where depth measures how many of the seven
pieces have been placed, from 0 to 7), with some states
having far more successor configurations than others.
This variation highlights the structural asymmetry of
the state space, which we later exploit to develop effi-
cient solving strategies.
Because of the size of the search space, we employ
a sampling approach to compute the branching factor
of the Soma Cube puzzle at varying depths usingG P
(Fig. 3(a); App. C). The average branching factor is
approximately 29.28 (95% CI: [27.84, 30.72]) [33] and
branching factors decrease monotonically as depth in-
creases. Fig. 3(b) visualizes the distribution of branch-
ing factors at each depth, showing an amorphous com-

3
(a) Average branching factor decay across depths for the Soma Cube
puzzle, showing exponential reduction in possible moves as pieces are
placed.
(b) Distribution of branching factors at different depths (1–6) in the
Soma Cube puzzle state space.
Figure 3. Branching factors in the Soma Cube puzzle: (a) The
average shows an exponential decay as the depth increases.
This is characteristic of puzzles where each new move adds
constraints on subsequent moves. (b) The frequency distri-
bution of branching factors at different depths, corresponding
to puzzle development, showing a characteristic three-phase
progression. At depth 1, any piece may be selected, result-
ing in a nearly uniform distribution as each piece contributes
a distinct branching factor. As depth increases, the distribu-
tion becomes increasingly centered around a lower median
value, reflecting the narrowing of available moves. By the fi-
nal depth, the variance collapses and the branching factor con-
verges to zero, indicating the placement of the last piece and
the dominance of unproductive states (the low density of so-
lutions) in the Soma Cube puzzle.
binatorial distribution at low depth, high variance with
an almost-smooth unimodal distribution at low depths,
followed by a narrowing of variance (number of avail-
able placements) at higher depth. This, overall, re-
veals the funnel-like topology of the puzzle towards so-
lutions where the width of the state-space graph con-
tracts significantly as depth increases. This combina-
torial structure is in contrast with some other puzzles
like the Rubik’s Cube or Sliding 8-Puzzle, which main-
tain an almost-constant branching factor throughout, or
chess, which does not seem to exhibit monotonic be-
havior (App. B). (However, random chess play does
show a bell-shaped distribution of branching factors in
its midgame, paralleling some of the dynamics we ob-
serve in the Soma Cube at middle depths (App. D).) We
will revisit how these mid-game constraints support the
emergence of landmarks in Sec. III E.
In the following, we consider various algorithmic ap-
proaches to solving the Soma Cube. We start with
depth-first search (DFS) with backtracking and pro-
gressively incorporate value ordering, variable ordering,
pruning, and landmark-based heuristics. These algo-
rithms abstract various natural strategies humans em-
ploy, guided by the presence of the physical artifact.
Like many puzzles, the Soma Cube is both a logical
problem and a physical device for solving it. The tangi-
ble pieces restrict how solvers traverse the search space
and, at the same time, reveal structure that supports ef-
ficient strategies. These observations lead us to propose
the followingPrinciple of Materiality:
Principle of Materiality: the physical em-
bodiment of a logical problem can alter
the geometry of the logical search space in
physically-derived ways that lead to a more
efficient search for its solution.
In particular, while it is understood [14, 17, 34] that
physical puzzles exploit perception — visual and tac-
tile — to distribute problem-solving, the Principle of
Materiality posits an additional benefit, in that physi-
cally embodied puzzles can effectively modify thelogical
structure of the search space.The Principle of Materiality
seeks to explain when, why, and how a formally identical yet
computationally difficult logical puzzle can become far more
tractable when instantiated as a physical artifact through a
formal change in the logical space.
III. COMPARING THE EFFICIENCY OF ALGORITHMS
SIMULATING PHYSICAL CONSTRAINTS
In this section, we present our quantitative results on
the impact of different heuristics on search efficiency,
summarized in Fig. 9. In Section IV, we revisit these al-
gorithms from a cognitive perspective, examining how
their efficiency relates to human problem-solving strate-
gies.
To quantify the efficiency of different search algo-
rithms, we focus on the effective branching factorb∗ (Eq.
(1)): the average number of children per node generated
during search,
6X
d=0
(b∗)d =N(1)

4
wheredstands for depth andNrepresents the total
number of nodes produced during search. This metric
is widely used to evaluate the effectiveness of heuristics
in improving search performance [35].
A. Depth-first search with backtracking
Our first and simplest algorithm is a randomized DFS
with backtracking. This corresponds to a scenario where
the solver does not use sophisticated strategies that ex-
ploit cube symmetries or piece constraints (which we
introduce as optimizations below), but can still avoid
repeating unproductive paths without using elaborate
learning techniques.
Figure 4. A solution path found by randomized DFS. Pieces
are placed in any empty cell regardless of contiguity.
At each iteration, the solver randomly selects from
available empty positions and explores different piece
orientations [36]. Upon exhausting valid moves, the
algorithm backtracks to the previous valid configura-
tion and explores alternative paths. The solver imple-
ments no adjacency requirements between pieces, al-
lowing placement at any unoccupied position within the
cube, as shown in Fig. 4.
B. Contiguous variable ordering
For the second solver, we implement cell-ordering,
where we require pieces to be placed in positions that
cover coordinates in a fixed sequence deterministically.
The solver starts from the (0,0,0) position at the bottom
corner of the cube and locates pieces contiguously, as
shown in Fig. 5(a).
(a) A solution path found through variable ordering by binding,
allowing only contiguous moves.
(b) A solution path found through layer-based variable ordering.
Figure 5. Comparison of two different solution paths.
We then apply layer-based variable ordering, a sec-
ondary ordering that prioritizes maximizing coverage of
the bottom layer before progressing to higher levels of
the Soma Cube during the search, as shown in Fig. 5(b).
This approach respects the “gravity constraints” of the
physical puzzle, simulating how it could be solved on a
flat surface in the physical world.
The efficiency of these solvers can be understood
through their branching factor trends across depths and
their impact on the distribution of backtracking events
in the search tree (Fig. 6). Randomized DFS with-
out contiguous variable ordering (Fig. 6(a)) exhibits a
heavily front-loaded backtracking pattern, as arbitrary
placements often lead to early failures, limiting deeper
exploration in a search space with many cycles. How-
ever, DFS with cell-ordered variable ordering (Fig. 6(b))
enforces adjacency constraints. The difference in back-
tracking distributions suggests early mistakes have a
disproportionately negative impact on search efficiency,
whereas deferring errors in a structured manner in-
spired by the physics of the puzzle enables a more
thorough exploration of promising regions in the state
space.
C. Dynamic pruning
Pruning improves search efficiency by eliminating
regions of the state space that cannot lead to a so-
lution [35]. Here we implement dynamic pruning,
where pruning decisions are made adaptively during
the search, based on the current puzzle configuration.
Our algorithm identifies small “voids” —disconnected
empty regions of size 1 or 2— which cannot be occupied
by any remaining piece (since all pieces have at least 3
cubes), and prunes and configuration with such voids.
D. Most constrained variable ordering (MCV)
In MCV ordering, we choose the next piece to place by
identifying the empty cell with the fewest valid place-
ment options, as determined by the current state of the
puzzle. This strategy examines each unassigned cell’s
possible moves, each defined by a legal combination
of piece and orientation, and selects the cell where the
number of legal pairs is minimal.
E. Landmarks and hierarchies
Modern graph navigation algorithms like ALT and
Contraction Hierarchies accelerate route-finding on
graphs by using landmarks and organizing nodes in
importance-based hierarchies [37, 38]. In our imple-
mentation for the Soma Cube, we evaluate partial con-

5
0 1 2 3 4 5 60
20
40
60
80
100
120
140
Depth
Branching Factor
Branching Factor
Effective b* (9.52)
2 3 4 5 60
10
20
30
40
50
60
Depth
% Backtracks
Backtracks
(a) Distribution of branching factors at different depths (1–6) for the
randomized DFS solver, and the associated backtrack distribution.
0 1 2 3 4 5 60
10
20
30
40
50
60
Depth
Branching Factor
Branching Factor
Effective b* (6.89)
2 3 4 5 60
10
20
30
40
50
Depth
% Backtracks
Backtracks
(b) Distribution of branching factors at different depths (1–6) for the
cell-ordered DFS solver, and the associated backtrack distribution.
Figure 6. Branching factors and backtrack distributions in the
Soma Cube puzzle. For both the randomized DFS and the cell-
ordered DFS the branching factor declines exponentially with
depth. Randomized DFS tends to backtrack sooner than cell-
ordered DFS because an incorrect random piece placement
forces a retreat to an earlier configuration. In contrast, the
cell-ordered algorithm makes more structured choices, lead-
ing to minimal corrections earlier and backtracking primarily
during the final piece placement.
figurations by determining the number of complete so-
lutions that can be derived from each. Configurations
that yield a substantial number of full solutions are
classified as high-importance landmarks, whereas those
that do not lie on any solution paths are designated anti-
landmarks (or dead states). We augment the solver so
that it can jump directly to designated high-importance
landmark states and then resume the search (e.g. via
DFS) from those landmarks (Fig. 7).
The landmark-based search algorithm is divided into
two distinct phases: preprocessing and querying. Dur-
ing preprocessing, a variable number of landmark
configurations and all encountered anti-landmarks are
identified and stored. In the subsequent querying
phase, these precomputed landmarks are invoked to
augment the search during the actual puzzle-solving
process. There is a trade-offbetween these two phases
(Fig. 8): as the number of landmarks increases, the pre-
processing time correspondingly rises, while the query-
ing time decreases.
Figure 7. Comparison of search space exploration strategies
for the Soma Cube puzzle. Left: Standard search space rep-
resented by nodes (configurations) and edges (legal moves),
with the blue shaded region illustrating the extent of explored
states by DFS. Right: Landmark-augmented search incorpo-
rating frequently occurring partial configurations as high-
importance nodes, with dashed edges representing precom-
puted successful paths to landmarks and the pink shaded re-
gion showing the reduced search space.
66 67 68 69 70 71 72 73 74 75
10
20
30
40
50
60
70
Querying cost [mean ops.]
Preprocessing cost
Preprocessing vs. Querying
Depth 3
Depth 2
Figure 8. Trade-offbetween preprocessing time (time spent
identifying and storing landmark configurations) and query-
ing time to reach a solution (actual puzzle-solving time) for
varying numbers of landmarks obtained at depth 2 and depth
3 via the cell-ordered DFS solver. At all depths, a reduc-
tion in querying cost (increased dependence on look-up ta-
bles) is achieved by an earlier increase in preprocessing time
(via comprehensive search for landmark configurations). This
trade-offis greatest at the puzzle depth where landmarks are
most important: a sweet spot defined by a high branching fac-
tor and non-trivial constraints on piece placement (Depth 2).
As branching factors decline querying provides a diminishing
marginal benefit (Depth 3).

6
Figure 9. Effective branching factors when combining dif-
ferent search strategies for the Soma Cube puzzle. Values are
rounded to a single decimal place. The heat map shows the ef-
fects of structured ordering, pruning, and guidance via land-
marks. The largest improvements (above the baseline of ran-
domized DFS) are associated with adding pruning and land-
marks. Both of these contract the logical search tree, one by
ruling out certain dead ends, and the other by additionally
caching shortest paths into lookup tables.
F . Quantitative comparison
Given these algorithms, our main result is summa-
rized in Fig. 9, which compares the effective branch-
ing factors across different search strategies. Among
these approaches, the landmark-based solver achieves
the greatest complexity reduction, as preprocessing to
identify high- versus low-importance states enables the
solver to bypass large portions of the search space. The
identification of anti-landmarks avoids dead ends, al-
lowing the solver to sidestep extensive backtracking
[39].
IV. CONNECTING PHYSICALLY-CONSTRAINED
ALGORITHMS TO COGNITIVE STRATEGIES
Each algorithm we designed to enhance search within
the logical space of the Soma Cube attempts to model
a physical aspect of the puzzle. In this section, we
ground each algorithm in empirical literature on cog-
nition with physical artifacts, connecting physical and
cognitive principles to logical search and constraints.
A. DFS with backtracking
DFS with backtracking implements a physical exclusion
principle. Solving thek-SAT formula is challenging in
part because the puzzle’s 27 atomic cubes combine to
form 7 compound shapes arranged in 3D space. Rota-
tion of a shape in physical space solves without effort the
harder task of rotating 3–4 bound cubes in the mind and
tracking their respective coordinates. Mental rotation
is a well-attested visuospatial challenge [40]. Indeed,
the difficulty of rotation was one of the primary argu-
ments in favor of the extended mind [41]. The simpler
problem of 2D rotation forms the basis of the Tetris puz-
zle, where the ability to quickly rotate and place pieces
is a characteristic of expert play [42]. Blindfold Tetris,
a more challenging variant that relies heavily on audi-
tory cues, further exemplifies this difficulty. Our DFS
with backtracking implementation simulates the steric
constraints of objects to eliminate non-viable configu-
rations: piece positions that would otherwise require
thousands of binary evaluations to discard in a purely
abstract logical search.
B. Contiguous variable ordering
Variable ordering implements local space filling. Lo-
cal growth of Soma Cube solutions (piece by piece as-
sembly) ensures that empty spaces or voids in partial
solutions are excluded. The physical pieces are natu-
ral void detectors which reveal ordinal relations (com-
patible physical sequences) directly to perception that
would otherwise need to be calculated based on inferred
intervals (perceived distances in logical space). The
ability to perceive spaces or intervals is harder than or-
dinal depth perception and this effect is amplified when
evaluated within continuous manifolds [43]. Overall
humans are poor at estimating 3D metric structures and
performance varies across rotation in viewing angles
[44].
Gravitational, layer-based variable ordering implements
layered assemblies. The difficulty of manipulating pieces
to achieve tesselation can be assisted by using a fixed
surface. By implementing a local growth rule con-
strained to layer-by-layer assembly, the “affordances” of
gravity are simulated to assist the dexterous placement
of pieces. A similar principle has been discovered for
“Robot-Grippers” where the manipulation capabilities
of a robotic hand are augmented by a high friction two
dimensional surface [45].

7
C. Dynamic pruning and most constrained variable
ordering
Dynamic pruning and most constrained variable order-
ing (MCV) capture the memory of common preferred pat-
terns and procedures using physical pieces. Board games
including chess, as well as simple regular lattice games
like Tic-Tac-Toe, have been studied extensively as mod-
els for working memory [17, 46–48]. Expertise in these
cases consists in sustained practice to form affective rep-
resentations of sensible configurations, from “opening
moves” through to “endgame moves” [28, 49]. In addi-
tion, master chess players prune inferior moves based
on fewer and more expansive board scans than ama-
teurs [50]. Dynamic pruning and MCV are surrogates of
physical scaffolds for reducing search spaces: MCV im-
poses the “opening game” rule of starting with corner
pieces that impose a maximum of constraints, whereas
pruning eliminates placements along search paths that
fail to find solutions.
D. Landmarks and hierarchies
Landmarks capture expert chunking and related cogni-
tive speed-bumps. The aggregation of pieces into larger
coherent aggregates as a function of repeat exposure, or
chunking [51], is a means of achieving significant “rank-
reduction” in data structures, allowing for faster per-
ceptual discrimination [47], leaps in performance [52],
efficient analogy-making [12], and improved speed and
accuracy [53]. Landmark algorithms simulate chunking
by replacing a multiplicity of possible paths with “pre-
computed” paths through high frequency assemblies.
In this way “preprocessing time” is used to significantly
reduce “querying time”, what has been called a “cogni-
tive speed bump” [54], which, in theoretical computer
science, can be described as a “contraction hierarchy” in
the search space graph [38].
V. DISCUSSION
A physical puzzle both poses a logical problem and of-
fers a mechanical tool for the solution of that problem.
We suggest that the quality of a puzzle can be measured
by how well the tool solves the problem, i. e., how effec-
tively the physical design guides you toward the solu-
tion. A well-known example is the Rubik’s Cube, which
is a tangible representation of a Cayley graph where the
cube’s face rotations act as the formal generators of the
underlying group, thereby mapping its entire configu-
ration space onto a physical artifact [55]. Solving the
cube optimally requires finding short paths in an expo-
nentially large graph, a problem that is computation-
ally difficult, yet routinely solved through the applica-
tions of manipulation algorithms [56]. In this study, we
reconceptualize the challenge of the Soma Cube [57] as
a search problem and explain why when mapped to a
physical artifact the search problem can be solved rather
effortlessly. We call this transformation of a challenging
logical problem into an easily solvable one through the
use of a physical artifact, the Principle of Materiality.
This paper examines how the Principle of Materiality
operates by mapping physical phenomena to algorith-
mic processes. Each algorithm emulates a specific phys-
ical constraint (rigidity, exclusion, rotation) that effec-
tively reduces the size of the search tree. Hence phys-
ical puzzles transform extensive logical problems into
contracted search spaces that are cognitively manage-
able for humans, under constraints of memory and in-
ference. Each of the algorithmic restrictions that we ob-
serve can be mapped onto a concept in cognitive science,
and this study recapitulates in a purely computational
setting the importance of chunking (landmarks and hi-
erarchies), spatial constraints and the role of physical
laws including gravity in assisting search (variable or-
dering), and the anticipatory elimination of nonviable
paths (pruning).
The use of games and puzzles have a long history
in mathematics [58], computer science [59], cognitive
science [3], economics [60] philosophy [61] and history
[62]. In one of the canonical texts on puzzles in math-
ematics, W. W. Rouse Ball organizes puzzles into prob-
lems of arithmetic, geometry, mechanics, and search (in
mazes). All physical puzzles are relegated to a chapter
on “Some Miscellaneous Questions” as they all deploy
some messy combination of arithmetic, geometry, and
mechanics, in novel ways. This paper aims to system-
atize and formalize some of these creative interplays.
Physical puzzles make connection to ideas of an “Ex-
tended Mind” [41], “Cognitive Artifacts” [63], “Cogni-
tion in the Wild” [64], “Distributed Cognition” [65], and
the role of material culture in the evolution of mind
[66]. They connect to the idea of a mental “physics en-
gine” that augments purely logical problem-solving [67]
and might be described as outsourced ”physical-physics
engines”. Owing to the simplicity and intuitive appre-
hension of games and puzzles, they provide a very con-
venient model system for exploring general cognitive
mechanisms [68].
It is important to distinguish that games are typically
designed for multiplayer contexts where competition
and coordination are paramount [60], while puzzles are
structured as solitary challenges centered on constraint
satisfaction [58]. Future work might further investi-
gate the cognitive and computational complexity mech-
anisms underlying these differences, potentially inspir-
ing novel designs that bridge the gap between recre-
ational puzzles and strategic gameplay.

8
These distinctions in design and engagement not only
shape how we interact with artifacts in games and puz-
zles, but also influence the computational strategies
used to analyze them. Traditional computational ap-
proaches to games and puzzles have followed two dis-
tinct paths: complexity theory, which analyzes asymp-
totic results for generalized versions of games (such as
n×nTic-Tac-Toe) that bear little relevance to human
problem-solving, and search algorithm development,
which focuses on optimizing tree traversal for specific
games like Chess and Go on modern computers. Sim-
ilarly, cognitive science research has traditionally fo-
cused on studying human subjects tackling computa-
tional complexity problems that are proven to be hard
in the asymptotic regime [69, 70].
A critical gap persists at the intersection of com-
plexity theory, algorithm design, cognitive science, and
cultural evolution: we lack a unified framework that
explains how the structural properties of finite puz-
zle instances (not just their asymptotic behavior) deter-
mine whether they are engaging or intractable for hu-
man solvers. This gap has limited our ability to con-
nect formal computational properties with empirically
observed patterns in human problem-solving behavior.
The present work uses the physical puzzle and its log-
ical implementation to provide the initial groundwork
for a theoretical framework bridging this divide.
ACKNOWLEDGMENTS
G. K. acknowledges Cris Moore and the SFI library
for the puzzles. D. C. K and G. K. are supported by the
Templeton World Charity Foundation, Inc. (funder DOI
501100011730) under the grant DOI:10.54224/20650
no. 20650 on “Building Diverse Intelligences through
Compositionality and Mechanism Design”, D.C.K. is
additionally supported by grant no. 81366 from the
Robert Wood Johnson Foundation on Using Emergent
Engineering for integrating complex systems to achieve
an equitable society. G. K. is additionally supported
from J. Grochow and R. Frongillo startup funds at the
University of Colorado Boulder. J. A. G. was partially
supported from NSF CAREER award CCF-2047756.
Data availability:All code and data used in this
study are freely available at GitHub (https://github.
com/gulcekardes/cognitive_artifacts).
Appendix A:k-SAT encoding
The Soma Cube puzzle consists of seven distinct
pieces that must be arranged to fill a 3×3×3 cube
without gaps or overlaps. We encode the puzzle as a
Boolean satisfiability problem by assigning a Boolean
variable to each potential piece placement, so that a
satisfying assignment corresponds to a valid assem-
bly. We begin by noting that each of the seven Soma
Cube pieces is defined by a set of unit cube coordi-
nates. For example, one piece may be represented as
z={(0,0,0),(1,0,0),(1,1,0),(2,1,0)}. To account for the
different spatial orientations, our code generates all dis-
tinct orientations for each piece by applying rotations
about thex,y, andzaxes. After rotations, each configu-
ration is normalized by translating it so that the small-
est coordinate becomes the anchor. The 3×3×3 cube
is represented by the set of coordinates{(x, y, z)|x, y, z∈
{0,1,2}}. For every piece, every orientation, and every
possible anchor position, the code computes an adjusted
placement (i. e., the translated coordinates that the piece
occupies). If all cells of a placement fall within the
cube, the placement is deemed valid and is assigned a
unique Boolean variable. We denote these variables as
Pxyzi ,where (x, y, z) (converted to 1-indexed form) indi-
cates the anchor coordinate, andi∈{1, . . . ,7}identifies
the piece. The overall SAT instance is described by a
Conjunctive Normal Form formula,Φ, which consists
of the following constraints:
a. Piece Constraints.For each piecei, we must
choose exactly one of its valid placements. LetP i be
the set of Boolean variables corresponding to the place-
ments of piecei. This constraint is encoded using:
1. Anat-least-oneclause:
_
P∈P i
P ,
which ensures that the piece is placed somewhere.
2.At-most-oneclauses, consisting of pairwise con-
straints:
¬P∨¬P ′,for all distinctP , P ′∈P i,
which guarantee that the piece is not placed in two
different locations simultaneously.
b. Cell Constraints.Similarly, each cell in the cube
must be covered by exactly one piece. For each cellc,
letC c be the set of Boolean variables corresponding to
placements that coverc. The constraint is again encoded
as:

9
1. Anat-least-oneclause:
_
P∈C c
P ,
ensuring that the cell is covered.
2.At-most-oneclauses:
¬P∨¬P ′,for all distinctP , P ′∈C c,
preventing more than one piece from occupying
the same cell.
Thus, the overall formulaΦis a conjunction of all these
clauses. The generated CNF formulaΦis then passed to
a SAT solver (specifically,Minisat22from the PySAT li-
brary). The solver searches for an assignment of truth
values to theP xyzi variables such thatΦevaluates to
true. A solution to the SAT instance directly corre-
sponds to a valid placement of all pieces in the cube.
c. Solution Enumeration.In addition to finding one
solution, our code employs a blocking clause method
to enumerate all solutions. After a solution is found,
a blocking clause (the negation of the current model) is
added, and the solver continues to search for other solu-
tions.
Appendix B: Branching factor
The branching factor of a node in a search tree refers
to the number of child nodes it has. In search trees
where the number of child nodes varies across differ-
ent nodes, calculating the average branching factor pro-
vides a useful measure of the tree’s breadth. The average
branching factor, denoted as ¯b, can be defined as:
¯b= 1
D
DX
d=1
Nd
Nd +L d
whereDrepresents the maximum depth of the search
tree,N d stands for the number of non-leaf nodes at
depthd, andL d is the count of leaf nodes at depthd
that are not solution nodes. The branching factor calcu-
lations in the main text of this article includeL d in the
formula. However, it is common practice to compute the
branching factor for most puzzles with regular search
spaces using only nonterminal nodes. For the sake of
comparison and reference, we have also provided the re-
sults of calculations that follow this convention, see Fig.
10.
0 1 2 3 4 5 60
100
200
300
400
500
600
700
800
688.00
319.12
130.63
44.31 8.73 2.03 1.00
Average Branching Factor
Figure 10. Soma Cube branching factors across depths.
Appendix C: Branching factors for various puzzles
The analysis of branching factors serves as a funda-
mental approach for evaluating the complexity inherent
in bothG P andG S. In state-space analysis, the diameter
(the maximum over all pairs of configurations, of their
shortest-path distance) quantifies the worst-case move
count between configurations. In a search space, a com-
parable measure of complexity is the tree’s maximum
depth.
0 5 10 15 20 25 30 35 40 45 50 550
5
10
15
20
25
30
35
Puzzle length
Branching Factor
Branching Factors of Puzzles
The Soma Cube
Rubik’s Cube
8-sliding puzzle
Slothouber–Graatsma
Magic Square 3 ×3
Figure 11. The relationship between branching factor and
depth for five classic puzzles.
Building on this, the worst-case complexity of a tree
search is controlled by two parameters, the branching
factor and the maximum depth, which determine its
time and space costs. A search algorithm must poten-
tially examine theb m nodes in total, since each of the
mlevels can have up tobbranches, leading to exponen-
tial time complexityO(b m). This relationship between

10
bandmdemonstrates why problems with high branch-
ing factors or large search depths quickly become com-
putationally intractable, even with sophisticated search
strategies.
Fig. 11 displays a taxonomic map of puzzles, or-
ganized by their branching factor patterns and depth
characteristics, where depth is defined as the minimum
number of moves required to solve the puzzle from
its worst-case position. For all puzzles except Rubik’s
Cube, data was generated using our GitHub code [71],
while the branching factor information for Rubik’s Cube
was obtained from [72].
Fig. 12 compares branching-factor evolution across
depths for chess, Rubik’s Cube, the 8 puzzle, and
three dissection puzzles: the Magic Square, Slothouber–
Graatsma, and the Soma Cube.
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 320
10
20
30
40
50
60
70
80
Depth
Branching Factor
Chess
Slothouber–Graatsma
Soma Cube
Rubik’s Cube
Magic Square 3×3
Sliding 8 Puzzle
Figure 12. Branching-factor evolution across multiple puz-
zles. Each curve shows how the average branching factor
changes with depth in the puzzle’s solution process. Chess
exhibits a non-monotonic branching factor due to piece dy-
namics. Rubik’s Cube maintains an almost constant branching
factor until the puzzle is nearly solved, reflecting its highly
regular structure and uniform move set. The 8 puzzle illus-
trates a sliding-tile puzzle with moderate non-monotonicity
as the empty space’s position affects available moves, while
still retaining a regular state space similar to Rubik’s Cube.
Three dissection puzzles, the 3×3 Magic Square, Slothouber–
Graatsma, and the Soma Cube, each exhibit a steady decline
in branching factor as pieces are placed, highlighting their
forward-directed, space-constrained nature.
As previously mentioned, variations such as changes
in branching factors or other combinatorial properties
across different puzzle depths could offer valuable in-
sights into puzzle characteristics and inform potential
solution strategies. Among the puzzles we examine
for comparison and contrast with the Soma Cube, dis-
section puzzles (including the Soma Cube itself and
two additional examples discussed below) feature irreg-
ular state spaces and follow a directed solution pro-
cess where each piece placement progressively restricts
future moves, leading to a consistent decrease in the
branching factor. In contrast, Rubik’s Cube maintains a
nearly constant branching factor until the end, whereas
chess and the sliding puzzle exhibit more complicated
trends.
In the case of the sliding puzzle, the branching fac-
tor is nearly constant, reflecting the reversible character
of its moves, similar to the Rubik’s Cube. However, in
the case of the sliding puzzle, the branching factor alter-
nates up and down every other move, because of simple
constraints on the moves: if you’re not allowed to back-
track, then when in a corner there is only 1 choice, on
a side there are 2 choices, and in the middle there are 3
choices. After being in a corner, one must move to a side;
after being in a side, one must move to a corner or the
center; after being in the center, one must move to the
side; and (without backtracking) one can never see the
sequence center–side–center. This explains the nearly-
constant but every-other-turn character of the branch-
ing factor of the sliding 8 puzzle. (This phenomenon
would not be present in a variant of the sliding-8 puzzle
played on a torus, that is, where the sides wrap around,
as in that setting every position is like every other posi-
tion, with a constant non-backtracking branching factor
of 3.)
In the case of chess, we see both a monotonically in-
creasing overall trend (in the first 25 rounds of the game
we simulated), but also an alternating up-and-down
pattern. The monotonically increasing overall trend in
the early moves is also reflected in real play [73], though
for fewer moves than we see in our random simulations.
But the latter pattern—that the second player seems to
systematically have fewer available moves than the first,
especially in the first few dozen rounds of the game—
has also been observed by David Barnes in his analysis
of 2.5M real chess games from ChessBase [73]. As far
as we are aware, there is as yet no explanation for this
phenomenon.
Appendix D: Supplementary Information 4
In addition to the Soma Cube puzzle, similar
branching-factor distributions appear in other combi-
natorial games, most notably chess. Although we do
not prove that landmarks necessarily arise whenever
a bell-shaped distribution occurs in the midgame, we
have strong indications that, when such a distribution
appears in a relatively unconstrained midgame (as at
depth 2 in the Soma Cube, and in chess, see [34, 74]
which demonstrate differences in midgame position
evaluation where chess masters outperform others due
to chunking), introducing landmarks can be beneficial.
Fig. 13 demonstrates that, much like in the Soma
Cube, the early branching-factor distribution in chess
appears relatively uniform, transitioning to a bell-

11
shaped distribution in the midgame. In the later stages,
this bell-shaped spread often develops a cluster near
zero moves, producing a mixed distribution that ul-
timately converges to a near-delta distribution in the
endgame.
Figure 13. Branching factor distributions in random chess at
two distinct ranges of depth.Top:Depths 1–10, where the
game is in its early stages and the distribution tends to be nar-
rower.Bottom:Depths 131–140, where many games have
ended (spiking at zero moves) or become heavily reduced,
causing a shift in the distribution and a lower average branch-
ing factor.
Here we simulated 10,000 random chess games using
thepython-chesslibrary [71]. Starting from the stan-
dard initial position, each ply (half-move) was chosen
uniformly at random from all legal moves, and the game
was terminated either when maximum depth 140 was
reached or when a checkmate/stalemate occurred. We
recorded the branching factor at each depth across these
simulations and then aggregated the results into his-
tograms, producing Fig. 13. This shows how the branch-
ing factor evolves from the opening (with relatively uni-
form move counts), through the midgame (where distri-
butions often become bell-shaped), to the endgame.
[1] A. M. Haith and J. W. Krakauer, The multiple effects of
practice: skill, habit and reduced cognitive load, Curr.
Opin. Behav. Sci.20, 196 (2018).
[2] J. W. Krakauer, Automatizing knowledge, inThe Rout-
ledge Handbook of Philosophy of Skill And Expertise(Rout-
ledge, Abingdon, Oxon; New York, NY: Routledge, 2021.
— Series: Routledge handbooks in philosophy, 2020) pp.
219–225.
[3] K. A. Ericsson, R. T. Krampe, and C. Tesch-R ¨omer, The
role of deliberate practice in the acquisition of expert per-
formance, Psychol. Rev.100, 363 (1993).
[4] N. Charness and M. Tuffiash, The role of expertise re-
search and human factors in capturing, explaining, and
producing superior performance, Hum. Factors50, 427
(2008).
[5] G. Gigerenzer, Embodied heuristics, Front. Psychol.12,
711289 (2021).
[6] E. P . Chronicle, J. N. MacGregor, and T. C. Ormerod,
What makes an insight problem? The roles of heuristics,
goal conception, and solution recoding in knowledge-
lean problems, J. Exp. Psychol. Learn. Mem. Cogn.30, 14
(2004).
[7] R. S. Sutton and A. G. Barto, Reinforcement learning: An
introduction, IEEE Trans. Neural Netw.9, 1054 (1998).
[8] M. Botvinick, S. Ritter, J. X. Wang, Z. Kurth-Nelson,
C. Blundell, and D. Hassabis, Reinforcement learning,

12
fast and slow, Trends Cogn. Sci.23, 408 (2019).
[9] T. D. Ullman and J. B. Tenenbaum, Bayesian models of
conceptual development: Learning as building models of
the world, Annu. Rev. Dev. Psychol.2, 533 (2020).
[10] T. L. Griffiths, C. Kemp, and J. B. Tenenbaum, Bayesian
models of cognition, inThe Cambridge Handbook of
Computational Cognitive Sciences(Cambridge University
Press, 2023) pp. 80–138.
[11] K. J. Holyoak, D. Gentner, and B. N. Kokinov, Introduc-
tion: The place of analogy in cognition, inThe Analogical
Mind(The MIT Press, 2001) pp. 1–20.
[12] D. R. Hofstadter, Epilogue: Analogy as the core of cog-
nition, inThe Analogical Mind(The MIT Press, 2001) pp.
499–538.
[13] I. D. Couzin, Collective cognition in animal groups,
Trends Cogn. Sci.13, 36 (2009).
[14] T. Dreyer, A. Haluts, A. Korman, N. Gov, E. Fonio,
and O. Feinerman, Comparing cooperative geometric
puzzle solving in ants versus humans, Proceedings of the
National Academy of Sciences122, e2414274121 (2025),
https://www.pnas.org/doi/pdf/10.1073/pnas.2414274121.
[15] A. Lavin, D. Krakauer, H. Zenil, J. Gottschlich, T. Matt-
son, J. Brehmer, A. Anandkumar, S. Choudry, K. Rocki,
A. G. Baydin, C. Prunkl, B. Paige, O. Isayev, E. Peterson,
P . L. McMahon, J. Macke, K. Cranmer, J. Zhang, H. Wain-
wright, A. Hanuka, M. Veloso, S. Assefa, S. Zheng, and
A. Pfeffer, Simulation intelligence: Towards a new gener-
ation of scientific methods, arXiv:2112.03235 (2021).
[16] D. A. Norman and etc.,Explorations in Cognition(W.H.
Freeman, New York, NY, 1975).
[17] J. Zhang, The nature of external representations in prob-
lem solving, Cogn. Sci.21, 179 (1997).
[18] D. C. Krakauer, Exbodiment: The mind made matter,
arXiv:2412.10957 (2024).
[19] R. E. Korf, Artificial intelligence search algorithms, in
Algorithms and Theory of Computation Handbook: Spe-
cial Topics and Techniques(Chapman & Hall/CRC, 2010)
p. 22, 2nd ed.
[20] D. E. Knuth,The Art of Computer Programming, Volume
4A: Combinatorial Algorithms, Part 1, The Art of Com-
puter Programming, Vol. 4A (Addison-Wesley Profes-
sional, 2011).
[21] C. Ans ´otegui, R. B ´ejar, C. Fern ´andez, C. Gomes, and
C. Mateu, Generating highly balanced sudoku problems
as hard problems, Journal of Heuristics17, 589–614
(2010).
[22] T. Rokicki, H. Kociemba, M. Davidson, and J. Dethridge,
The diameter of the Rubik’s cube group is twenty, SIAM
J. Discrete Math.27, 1082 (2013), see alsohttps://
kociemba.org/moves20.htm.
[23] S. Das, A. Dey, A. Pal, and N. Roy, Applications of ar-
tificial intelligence in machine learning: Review and
prospect, Int. J. Comput. Appl.115, 31 (2015).
[24] M. Mandal, S. Poddar, and A. Das, Comparison of hu-
man and machine based facial expression classification,
inInternational Conference on Computing, Communication
& Automation(IEEE, 2015).
[25] J. E. H. Korteling, G. C. van de Boer-Visschedijk, R. A. M.
Blankendaal, R. C. Boonekamp, and A. R. Eikelboom,
Human- versus artificial intelligence, Front. Artif. Intell.
4, 622364 (2021).
[26] M. Mitchell,Artificial intelligence(Farrar, Straus and
Giroux, 2019).
[27] J. McCarthy and P . J. Hayes, Some philosophical problems
from the standpoint of artificial intelligence, Readings in
artificial intelligence (1981).
[28] F. Mechner, Chess as a behavioral model for cognitive
skill research: Review of blindfold chess by Eliot Hearst
and John Knott, J. Exp. Anal. Behav.94, 373 (2010).
[29] F. Chollet, On the measure of intelligence,
arXiv:1911.01547 (2019).
[30] E. R. Berlekamp, J. H. Conway, and R. K. Guy,Win-
ning Ways for Your Mathematical Plays, Volume 4(A K Pe-
ters/CRC Press, 2004).
[31] S. Amarel, On representations of problems of reasoning
about actions, Machine intelligence (1968).
[32] A solver could in principle operate by putting together
several multi-piece configurations independently before
combining them, but we leave analysis of such solvers to
future work.
[33] This calculation compares the number of nodes created
in each iteration to the previous iteration. It includes all
nodes in the search tree except solution leaves, which
would have branching factor 0.
[34] W. G. Chase and H. A. Simon, Perception in chess, Cog-
nitive Psychology4, 55–81 (1973).
[35] S. J. Russell and P . Norvig,Artificial Intelligence: A Mod-
ern Approach, 3rd ed. (Pearson, Upper Saddle River, New
Jersey, 2010) pp. 94–95.
[36] Although randomization can be applied to piece selection
order, orientation sequences, position selection order, or
any combination thereof, for simplicity our implementa-
tion randomizes position selection while maintaining a
fixed piece and orientation order.
[37] A. V. Goldberg and C. Harrelson, Computing the shortest
path: A∗ search meets graph theory, inProc. 16th ACM-
SIAM Symp. Disc. Algorithms (SODA ’05)(Society for In-
dustrial and Applied Mathematics, 2005) pp. 156–165.
[38] R. Geisberger, P . Sanders, D. Schultes, and D. Delling,
Contraction hierarchies: Faster and simpler hierarchi-
cal routing in road networks, inExperimental Algorithms
(WEA ’08)(Springer Berlin Heidelberg, 2008) pp. 319–
333.
[39] For this figure we derive landmark values by comput-
ing upper bounds on the branching factor using anti-
landmark configurations. Because landmark sets vary be-
tween solvers, these values serve as conservative esti-
mates of the effective branching factors for solvers aug-
mented with the landmark approach.
[40] R. N. Shepard and J. Metzler, Mental rotation of three-
dimensional objects, Science171, 701 (1971).
[41] A. Clark and D. Chalmers, The extended mind, Analysis
58, 7 (1998).
[42] J. K. Lindstedt and W. D. Gray, Distinguishing experts
from novices by the mind’s hand and mind’s eye, Cogn.
Psychol.109, 1 (2019).
[43] J. F. Norman and J. T. Todd, Stereoscopic discrimination
of interval and ordinal depth relations on smooth sur-
faces and in empty space, Perception27, 257 (1998).
[44] J. T. Todd and J. F. Norman, The visual perception of
3-D shape from multiple cues: are observers capable of
perceiving metric structure?, Percept. Psychophys.65, 31

13
(2003).
[45] Q. Lu, A. B. Clark, M. Shen, and N. Rojas, An origami-
inspired variable friction surface for increasing the dex-
terity of robotic grippers, IEEE Robotics & Autom. Lett.
5, 2538 (2020).
[46] F. Galton, Psychology of mental arithmeticians and blind-
fold chess-players, Nature51, 73 (1894).
[47] F. Gobet and H. A. Simon, Recall of random and distorted
chess positions: implications for the theory of expertise,
Mem. Cognit.24, 493 (1996).
[48] T. W. Robbins, E. J. Anderson, D. R. Barker, A. C. Bradley,
C. Fearnyhough, R. Henson, and S. R. Hudson, Working
memory in chess, Mem. Cognit.24, 83 (1996).
[49] K. A. Ericsson and N. Charness, Expert performance: Its
structure and acquisition, Am. Psychol.49, 725 (1994).
[50] P . J. Blignaut, T. R. Beelders, and C.-Y. So, The visual span
of chess players, inProc. 2008 Symp. Eye Tracking Research
& Appl. (ETRA ’08)(ACM Press, New York, New York,
USA, 2008).
[51] W. G. Chase and H. A. Simon, Perception in chess, Cogn.
Psychol.4, 55 (1973).
[52] W. D. Gray and J. K. Lindstedt, Plateaus, dips, and leaps:
Where to look for inventions and discoveries during
skilled performance, Cogn. Sci.41, 1838 (2017).
[53] S. Wu, N. Elteto, I. Dasgupta, and E. Schulz, Chunking
as a rational solution to the speed-accuracy trade-offin a
serial reaction time task, Sci. Rep.13, 7680 (2023).
[54] J. K. Lindstedt and W. D. Gray, The “cognitive speed-
bump”: How world champion Tetris players trade mil-
liseconds for seconds, CogSci (2020).
[55] G. Cooperman, L. Finkelstein, and N. Sarawagi, Appli-
cations of Cayley graphs, inAppl. Algebra, Algebraic Al-
gorithms & Error-Correcting Codes: 8th Internat. Conf.
(AAECC-8, ’90)(Springer, 1991) pp. 367–378.
[56] E. D. Demaine, M. L. Demaine, S. Eisenstat, A. Lubiw, and
A. Winslow, Algorithms for solving Rubik’s cubes, in19th
Annual Eur. Symp. Algorithms (ESA ’11)(Springer, 2011)
pp. 689–700.
[57] D. H. Goodman and I. Garibi,Soma Puzzle Book, The:
A New Approach To The Classic Pieces(World Scientific,
2019).
[58] W. W. Rouse Ball,Mathematical recreations and essays,
11th ed. (Macmillan, London, England, 1939).
[59] J. H. Conway,On Numbers and Games, London Mathemat-
ical Society Monographs (Academic Press, San Diego, CA,
1976).
[60] J. von Neumann and O. Morgenstern,Theory of games and
economic behavior(Princeton University Press, Princeton,
NJ, 1953).
[61] B. Suits,The grasshopper(University of Toronto Press,
Toronto, ON, Canada, 1990).
[62] J. H. Huizinga,Homo ludens, 3rd ed. (HarperCollins Dis-
tribution Services, Glasgow, Scotland, 1970).
[63] D. A. Norman,The design of everyday things, The MIT
Press (MIT Press, London, England, 2013).
[64] E. Hutchins,Cognition in the Wild, Bradford Books (Brad-
ford Book, 2014).
[65] J. Zhang and V. Patel, Distributed cognition, representa-
tion, and affordance, Pragmat. Cogn.14, 333 (2006).
[66] D. C. Dennett,From bacteria to Bach and back(Penguin
Books, Harlow, England, 2018).
[67] S. Schwettmann, J. Tenenbaum, and N. Kanwisher, Evi-
dence for an intuitive physics engine in the human brain,
in2018 Conference on Cognitive Computational Neuro-
science(Cognitive Computational Neuroscience, Brent-
wood, Tennessee, USA, 2018).
[68] K. Allen, F. Br ¨andle, M. Botvinick, J. E. Fan, S. J. Gersh-
man, A. Gopnik, T. L. Griffiths, J. K. Hartshorne, T. U.
Hauser, M. K. Ho, J. R. de Leeuw, W. J. Ma, K. Mu-
rayama, J. D. Nelson, B. van Opheusden, T. Pouncy,
J. Rafner, I. Rahwan, R. B. Rutledge, J. Sherson, O. Sim-
sek, H. Spiers, C. Summerfield, M. Thalmann, N. Velez,
A. J. Watrous, J. B. Tenenbaum, and E. Schulz, Using
games to understand the mind, Nat. Hum. Behav.8, 1035
(2024).
[69] J. N. Macgregor and T. Ormerod, Human performance
on the traveling salesman problem, Perception & Psy-
chophysics58, 527–539 (1996).
[70] D. Reichman, F. Lieder, D. D. Bourgin, N. Talmon,
and T. L. Griffiths, The computational challenges of
means selection problems: Network structure of goal sys-
tems predicts human performance, Cognitive Science47,
10.1111/cogs.13330 (2023).
[71] G. Kardes, Soma-cube, GitHub repositoryhttps:
//github.com/gulcekardes/cognitive_artifacts
(2025).
[72] T. Rokicki, H. Kociemba, M. Davidson, and J. Dethridge,
God’s number is 20 (2010), accessed: 2025-01-06.
[73] D. Barnes, Answer to “What is the average number of le-
gal moves per turn?” on Chess StackExchange,https:
//chess.stackexchange.com/a/24325(2019), accessed
5 May 2025.
[74] P . F. Delaney, The role of long-term working memory
and template theory in contemporary expertise research,
Journal of Expertise1, 155 (2018).
