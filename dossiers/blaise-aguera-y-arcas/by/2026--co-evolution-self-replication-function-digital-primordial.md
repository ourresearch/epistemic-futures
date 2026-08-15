---
title: "Co-evolution of self-replication and function in a digital primordial soup"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2026
date: 2026-07-10
venue: "arXiv (Cornell University)"
authors: "Francesco Cicala, Eyvind Niklasson, Ettore Randazzo, Sami Boukortt, Alessio Basti, Mayalen Etcheverry, Rif A. Saurous, Ben Laurie, James Manyika, Blaise Aguera-Arcas, Blake Richards"
source_url: https://arxiv.org/abs/2607.09211
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W7168328530, W7168157657 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2607.09211."
---

# Co-evolution of self-replication and function in a digital primordial soup

## Full text

### Abstract (from OpenAlex metadata)

While traditional evolutionary algorithms hard-code reproduction, self-replication can emerge spontaneously within digital ``primordial soups''. This paper investigates the co-evolution of this emergent self-replication alongside problem-solving capabilities. We initialize a population of random 32-byte Z80 assembly programs, requiring self-replication to arise purely through random assembly-level mutations and pairwise program interactions. To link these behaviors, we introduce a task-based validation step: correctly evaluating a polynomial raises a program's interaction probability above a baseline rate. Our experiments yield four primary findings. First, self-replication and mathematical problem-solving successfully co-evolve from initial randomness. Second, the pressure to compute accelerates the emergence of compact, robust reproductive architectures that preserve memory for task execution. Third, applying metabolic constraints increases the likelihood that programs evolve conditional halting, terminating early during validation while bypassing the halt during interaction to execute block-copy replication. Finally, when programs are partitioned into spatial task niches, spontaneous self-replication generates an emergent learning curriculum, utilizing simple solutions as stepping stones toward complex polynomials. Altogether, these results demonstrate an interactive feedback loop: environmental task demands actively shape the physical architecture of self-replication, while spontaneous replication alters the evolutionary trajectory of functional problem-solving.

---

C O - EVOLUTION OF SELF - REPLICATION AND FUNCTION IN A
DIGITAL PRIMORDIAL SOUP
A P REPRINT
Francesco Cicalaa,1 , Eyvind Niklassona,1 , Ettore Randazzoa,1 , Sami Boukortta , Alessio Bastib , Mayalen Etcheverrya ,
Rif A. Saurousa , Ben Lauriea , James Manyikaa , Blaise Agüera y Arcasa,c , and Blake A. Richardsa,d,e,f,2

arXiv:2607.09211v1 [cs.NE] 10 Jul 2026

b

a
Google, Paradigms of Intelligence Team
University “G. D’Annunzio” of Chieti-Pescara
d
Mila - Quebec AI Institute
e
McGill University
f
CIFAR

July 13, 2026

A BSTRACT
While traditional evolutionary algorithms hard-code reproduction, self-replication can emerge spontaneously within digital “primordial soups”. This paper investigates the co-evolution of this emergent
self-replication alongside problem-solving capabilities. We initialize a population of random 32-byte
Z80 assembly programs, requiring self-replication to arise purely through random assembly-level
mutations and pairwise program interactions. To link these behaviors, we introduce a task-based
validation step: correctly evaluating a polynomial raises a program’s interaction probability above a
baseline rate. Our experiments yield four primary findings. First, self-replication and mathematical
problem-solving successfully co-evolve from initial randomness. Second, the pressure to compute
accelerates the emergence of compact, robust reproductive architectures that preserve memory for
task execution. Third, applying metabolic constraints increases the likelihood that programs evolve
conditional halting, terminating early during validation while bypassing the halt during interaction
to execute block-copy replication. Finally, when programs are partitioned into spatial task niches,
spontaneous self-replication generates an emergent learning curriculum, utilizing simple solutions as
stepping stones toward complex polynomials. Altogether, these results demonstrate an interactive
feedback loop: environmental task demands actively shape the physical architecture of self-replication,
while spontaneous replication alters the evolutionary trajectory of functional problem-solving.
Keywords Artificial Life · Spontaneous Replication · Computational Evolution · Automated Curricula

1

Introduction

Origin of life research has long debated the fundamental drivers required for life to emerge from non-living matter
[Preiner et al., 2020]. Genetics-first accounts hold that life began with self-replicating, information-bearing molecules
[Gilbert, 1986], whereas metabolism-first accounts posit that energy-harnessing autocatalytic networks preceded genetic
replication [Wächtershäuser, 1997, Lancet et al., 2018, Kauffman, 1986, Hordijk and Steel, 2018, Kauffman, 2000]. A
complementary tradition treats the two as jointly necessary, with frameworks such as Gánti’s chemoton [Gánti, 2003]
and Dyson’s double-origin hypothesis [Dyson, 1999] positing that a minimal living system must couple metabolism with
replication. This inquiry extends naturally into Artificial Life (ALife), which seeks to explore the universal principles of
living systems across abstract computational substrates [Scharf et al., 2015, Fontana, 1990, Hutton, 2002, Kruszewski
1
2

F.C., E.N., and E.R. contributed equally to this work.
To whom correspondence should be addressed. E-mail: blakerichards@google.com

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

and Mikolov, 2022]. Across both biological and digital domains, the spontaneous emergence of self-replication
marks a critical phase transition from pre-evolutionary interactions to Darwinian evolution [Nowak and Ohtsuki,
2008, Agüera y Arcas et al., 2024, Spiegelman et al., 1965]. However, platforms studying the evolution of complex
behaviors—whether via cellular automata, agentic simulators, or assembly-language organisms—typically bypass
the stochastic hurdles of this transition by hard-coding reproduction or seeding their environments with hand-crafted
ancestral replicators [Neumann and Burks, 1966, Langton, 1984, Sayama, 1999, Oros and Nehaniv, 2007, Schmickl
et al., 2016, Mordvintsev et al., 2020, Sinapayen, 2023, Chang and Lipson, 2018, Randazzo et al., 2021, Goldberg,
1989, Randazzo and Mordvintsev, 2023, Lu et al., 2024, Lenski et al., 2003, Ofria and Wilke, 2004, Kumawat et al.,
2025, Ray, 1991, 1994].
To bridge the gap between pre-life emergence and life-era evolution, it is vital to study environments where reproduction
is not an axiomatic guarantee. While early ALife models [Rasmussen et al., 1990, 1991, Pargellis, 1996] and recent
studies [Agüera y Arcas et al., 2024] have successfully demonstrated that self-replicating programs can spontaneously
emerge from random, unseeded initializations without explicit fitness landscapes, these works generally do not explore
the essential next step: the evolution of complex problem-solving. In this paper, we build directly upon the foundational
digital primordial soup framework of Agüera y Arcas et al. [2024] to link the spontaneous emergence of reproduction to
the evolution of complex algorithmic behaviors. Specifically, we investigate how the capacity to solve increasingly
complex mathematical tasks co-evolves alongside the spontaneous origination of reproduction itself.
We explore this by situating a population of random programs on a spatial grid where each entity is a Z80 assembly
program executed by an emulated microprocessor. Here, reproduction is not a system-level command, but a behavior
that must be discovered through the execution of assembly instructions. To investigate the relationship between
primordial reproduction and complex problem-solving, we introduce a competence-gated interaction rule. Under
this regime, a program’s opportunity to execute and potentially reproduce is contingent upon a validation step: the
program is challenged to evaluate a specific mathematical polynomial. The instruction set lacks a native multiplication
instruction, requiring the evolution of complex iterative loops to perform polynomial evaluation, thus presenting a
rugged algorithmic search space. This setup differs significantly from platforms such as Avida [Lenski et al., 2003,
Ofria and Wilke, 2004, Kumawat et al., 2025], where solving a task can be viewed as a form of computational
metabolism [Adami, 1998] that is rewarded with the execution of a built-in copy command, thereby explicitly binding
competence and reproduction together. Crucially, our system instead decouples the two: a successful polynomial
evaluation merely increases the likelihood that a program will receive an opportunity to interact with its neighborhood,
and does not facilitate or trigger replication. For a lineage to persist in our model, therefore, it must satisfy two
independent conditions: the program must pass the validation step and it must also possess its own evolved mechanism
for self-replication. Solving the task is therefore insufficient for propagation if the program does not simultaneously
encode the instructions required to copy itself into the available memory space.
Our experiments yield four primary findings that highlight the interaction between emergent reproduction and the
evolution of task solutions. First, we find that self-replication and task-solving co-evolve within individual programs.
Replication is a strict prerequisite for propagation: a task solution cannot spread through the population unless the
program carrying it can also copy itself. Task-solving is not strictly required to reproduce, but it confers a selective
advantage, since a program that solves its task is far more likely to be selected for interaction than one that does not.
Under this combined pressure, robust and efficient reproductive architectures reliably emerge from random noise and,
in the same programs, acquire the ability to solve mathematical tasks of increasing complexity. This joint emergence
establishes the platform for the three findings that follow.
Second, we find that the pressure to solve tasks reshapes the way the reproductive machinery itself evolves. The earliest
replicators to emerge copy themselves by devoting nearly the entire program to the reproduction operation, leaving
no room for the instructions needed to solve a task. More compact replication mechanisms occupy just a few bytes
and leave the rest of the tape free, so that the same program can both reproduce and compute. Because these compact
replicators can do both, the demand to solve tasks accelerates the population’s transition toward them. In short, the
pressure to solve tasks feeds back onto the architecture of how a program reproduces.
Third, we show that if we apply a metabolic constraint to the task solutions [Kempes et al., 2017] (i.e. we decrease a
program’s chance to interact based on how many operations it uses to solve a task), then the programs evolve conditional
operations to distinguish between task solution runs and program interaction runs.
Finally, we find that the dynamics of reproduction influence the evolution of task solutions. Specifically, we find
that in unstructured (panmictic) environments, where programs interact freely with any other programs, populations
consistently fail to compute high-degree polynomials. We demonstrate that this failure is an instance of the objective
paradox [Stanley and Lehman, 2015, Lehman and Stanley, 2011], in which explicitly rewarding progress deceives the
search and explains why a smoothed fitness landscape fails to aid discovery. Rather, we demonstrate that the emergence
of programs computing high-degree polynomials is reliably observed only when the grid is partitioned into distinct

2

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

task niches, coupled with sparse migration [Wright, 1932, Rainey and Travisano, 1998]. We show that this spatial
structure generates an emergent curriculum, utilizing previously solved simpler tasks as genetic stepping stones for
higher-complexity tasks.
Altogether, these results demonstrate that self-replication and the ability to solve tasks of increasing complexity
co-evolve. As well, pressure to solve complex tasks can influence the emergence and mechanics of spontaneous
reproduction, and in turn, the presence of niches for reproduction can help to shape task solutions through emergent
curricula.

2

Results

2.1

Model overview

To study the co-emergence of self-replication and task solving, we create a population of random programs across a
set of separate niches, each assigned a different mathematical task. Evolution proceeds through repeated epochs, in
which programs are mutated, tested on their niche’s task, and paired for interaction. Solving the task makes a program
more likely to be selected for interaction, and when two programs interact, one program can run assembly instructions
that copy its own bytes over those of the other. Because an interaction overwrites the two programs with its result, a
program that copies itself spreads through the substrate, while one that does not tends to be overwritten by those that do.
Concretely, the population is divided into 32 niches, and each niche is a separate two-dimensional grid of cells, with
one program per cell. A program is a sequence of ℓ = 32 bytes, which we also call a “tape” (Fig. 1A). Within a niche,
position matters, because a program interacts mostly with its immediate neighbors on the grid. The niches have no
spatial arrangement relative to one another, so they act as a collection of separate populations. Each niche is assigned
one of 32 polynomial functions, and a program’s task is to evaluate the polynomial of its niche. Across all niches the
population totals 219 programs, all initialized as random byte sequences.
Each epoch begins with a mutation step, in which every program has a small chance of having one random byte
reinitialized (Fig. 1B). The programs are then evaluated, and a subset is selected for pairwise interaction, as we describe
next.
The program evaluation is a competence test we call “validation”. The program is run on its own by a Z80 emulator (see
Methods for details), and we check whether it evaluates its niche’s polynomial correctly on a few randomly sampled
inputs. This validation yields a binary success or failure signal, meaning the program passes only if it computes
the correct output for all sampled inputs. Executing a program writes its final memory state back to its cell, so any
modification it makes to its own bytes during validation persists, just as it does during an interaction.
A program that passes validation becomes much more likely to be selected for interaction, though this likelihood is
reduced by a metabolic penalty that grows with the number of steps it used to pass the validation (Fig. 1C). A program
that fails is still selected sometimes, but only at a low baseline rate (see Methods for the exact rule).
A selected program is then paired with a partner. Most of the time, with probability 0.95, the partner is one of its
immediate neighbors in the same niche. The rest of the time the partner is any program drawn uniformly from the
whole population (Fig. 1D). This occasional long-range pairing, which we call cross-niche pollination (CNP), lets a
solution found in one niche spread into another, and we show later that it is key for solving the harder tasks.
In an interaction, the two programs’ tapes are concatenated into a single 2ℓ-byte memory space, and execution begins
at the first byte of the first program. Replication is never imposed by the system; it occurs only when the executed
code, on its own, copies one program’s bytes over the second program’s memory region. Whatever the combined tape
contains at the end of a fixed instruction budget is split back into two 32-byte halves and written back into the cells the
two programs came from, carrying the result into the next epoch.
2.2

Self-reproduction and task solutions emerge from a primordial soup

Over one million epochs of evolution, robust self-replication and task-solving capabilities consistently co-emerged from
completely random initial programs, as successful self-replicating lineages spread to dominate the grids (Fig. 1E). This
result shows that spontaneous replication and the ability to solve increasingly complex tasks can co-evolve. Indeed, the
two abilities reinforce each other. A program that cannot replicate is inevitably overwritten by one that can, regardless
of its task-solving competence. Conversely, among replicating programs, those that successfully solve their niche’s
polynomial are selected for interaction at a higher rate. Over time, the lineages that dominate a niche tend to integrate
both behaviors.
3

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

Figure 1: System architecture. (A) The 32 task niches, each a 128 × 128 grid of 32-byte Z80 programs and each
assigned a target polynomial f (x). (B) Selected pairs concatenate their tapes, execute from left to right, undergo random
byte-flip mutation, and the resulting halves replace the originals. (C) Competence gating: register D is initialized
to a sampled input x ∈ {0, . . . , 15}, the program is executed for up to B = 512 instructions, and register E is read
as the output. Producing f (x) on three independent inputs raises the interaction probability from pbase = 0.3 to
psucc = 1, optionally discounted by a metabolic penalty proportional to execution steps. (D) Most pairings are local von
Neumann neighbour interactions; with probability π the partner is instead drawn uniformly from any niche (cross-niche
pollination, CNP). (E) A view of three intermediate states of the system at different epochs of a simulation. Each pixel
in the grid corresponds to a program. Each program’s color is obtained by averaging the RGB vectors assigned to a
subset of its bytes according to a handcrafted colormap. The color of programs that successfully passed their most
recent validation is biased toward green. Note the homogenization of the program content as self-replicators take over,
as well as the gradual emergence of solutions in specific niches (each block corresponds to a different niche).

In contrast to a standard evolutionary algorithm, our system never copies or reproduces programs. It provides only
random initialization, mutation, and a validation step that biases how frequently programs interact. This bias induces a
fitness landscape, but the system offers immediate no means of climbing it, since reproduction must be discovered by
the executed code. The evolutionary machinery therefore emerges from random bytes together with the ability to solve
problems, rather than being supplied in advance.
2.3

Tasks alter the dynamics of emergent self-replication

The co-emergence of replication and task-solving raises a natural question: how do the two interact as evolution
proceeds? One might expect a simple sequence, in which a replicator is discovered, replicates until it dominates the
population, and only afterwards evolves to solve tasks. Instead, we found a more intricate coupling, in which the
pressure to solve tasks and the architecture of replication shape one another. Two types of replicators came to dominate
the population at different epochs. The first, a simple replicator we call ‘Load-Push’, consists of a string of paired
4

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

‘Load’ and ‘Push’ instruction bytes. Because the Z80’s PUSH instruction operates on 16-bit registers, each pair copies
the program two bytes at a time to the adjacent memory space of a partner program (Fig. 2A). Lacking a loop, full
replication requires a long chain of these pairs, meaning a Load-Push replicator consumes the entire 32-byte tape.
A second replicator, the ‘Load Increment Repeat’ (LDIR) replicator, reliably took over later. It utilizes a specialized
Z80 block-copy instruction (LDIR) that automatically loops to copy a sequence of bytes from one location in memory
to another. Rather than a long, repetitive sequence of instructions, it needs only to initialize its copy parameters to copy
from P1 into P2 once before the single instruction executes the entire copy. This allows a program to achieve replication
using only a few bytes (Fig. 2B), leaving the rest of its memory free for task-solving code (see Methods for the exact
register mappings).
As noted above, the Load-Push replicators were the first to appear and dominate the grids (Fig. 2D, solid green line), but
they eventually gave way to the LDIR replicators (Fig. 2D, solid purple line). The number of tasks solved tracked this
turnover (Fig. 2D, solid blue line). Specifically, the number of tasks solved dropped as the Load-Push replicators spread,
then recovered and grew as the LDIR replicators took over. The reason for this dynamic is that a Load-Push replicator
uses the entire tape to copy itself, leaving no room for task-solving code, so its spread displaces programs that solve
tasks. The LDIR replicator, by contrast, needs only a few bytes and leaves the rest of the program free; accordingly, its
emergence always preceded the growth in task-solving programs, indicating that it unlocked the ability to both replicate
and solve tasks. Consistent with this, removing the task-based gating of interactions (see Methods for details) slowed
the Load-Push-to-LDIR transition but did not prevent it (Fig. 2D, dotted line). The transition is intrinsically driven by
differences in mutational robustness among the replicators (which we quantify below), with tasks serving to accelerate
it.
To determine whether the accelerating effect of task pressure is specific to the LDIR instruction, we ran control
experiments where we removed LDIR and its close relatives (LDI and LDDR) from the language. In their absence, we
observe the consistent emergence of a different replication mechanism based on the LDD instruction, though it takes
over the population much more slowly than LDIR had (Fig. 2E, solid lines). This transition occurs consistently only
under task pressure; without it, the transition from Load-Push is extremely slow and fails to complete within one
million epochs (Fig. 2E, dashed lines). While LDIR has a built-in repeat mechanism that copies the entire program
once its parameters are initialized, LDD copies only a single byte at a time. An LDD-based replicator must therefore
not only initialize its parameters to copy from P1 to P2 but it also must implement an explicit, multi-byte loop to
achieve replication (Fig. 2C), representing a more complex reproductive architecture. These results show that when one
solution for reproduction is blocked, another is found, and that task pressure again accelerates the change. To verify our
hypothesis that LDIR replicators naturally come to dominate because there is a robustness hierarchy of the replicators,
we quantified how well each reproduction architecture tolerates replication errors (see Methods). Our measurements
revealed a clear robustness hierarchy (LDIR > LDD > Load-Push), where LDIR programs remain functional after
successive mutations significantly more often than LDD loops, which in turn outperform the Load-Push sequences
(Fig. 2F).
Taken together, these experiments show that the way a program reproduces keeps evolving after self-replication first
appears. Robustness to mutation drives the population toward more compact replicators on its own, but the pressure to
solve mathematical tasks accelerates that shift, because a compact replicator leaves room in the tape for task-solving
code needs. The fitness landscape created by the tasks thus reshapes the replication machinery, so that how a program
computes and how it reproduces evolve together.
2.4

Metabolic constraints drive efficient, conditional execution

In biological systems, computation is not free; organisms must balance the energy spent processing information with the
resources required for replication. To study how such efficiency constraints shape algorithmic evolution, we introduced
a “metabolic cost” to the validation phase, discounting a program’s interaction probability in proportion to the number
of execution steps it takes to solve its task (see Methods). We asked whether this constraint would drive the evolution of
more efficient programs, and how it might affect the replication phase where the constraint does not apply.
While the metabolic constraint left the overall rate of task solution emergence unchanged, it profoundly altered how
those solutions were implemented. As the metabolic penalty coefficient increased, the average number of execution steps
spent during validation fell significantly (Fig. 3A). This efficiency was achieved because evolved programs consistently
began incorporating a HALT instruction, which terminates execution as soon as the correct output is computed.
In a minority of simulations, programs went further, evolving context-dependent behavior by exapting register D as
a sensory cue to distinguish between the validation and interaction phases. In our execution protocol, the emulated
environment uses register D to pass the task input x ∈ {0, . . . , 15} during validation, meaning it contains a non-zero
value fifteen times out of sixteen. During the interaction phase, however, the environment always initializes D to zero.
5

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

Figure 2: Emergence of self-replicators and accelerating effect of tasks: (A) Illustration of a Load-Push replicator.
(B) Illustration of a LDIR replicator. (C) Illustration of an LDD replicator. (D) Populations of Load-Push and LDIR
replicators over time, with and without tasks. Data shown is mean over 100 seeds. Number of tasks solved also shown
as mean ± 95% C.I. (E) Populations of Load-Push and LDD replicators over time with and without tasks, when LDIR
replicators are blocked. Data shown is mean over 100 seeds. Number of tasks solved also shown as mean ± 95% C.I.
(F) Percentage of programs with no replication errors following one byte mutation (left), four byte mutations (middle),
and eight byte mutations (right) for Load-Push, LDIR, and LDD replicators. Error bars represent 95% Wilson score
intervals. LDIR replicators were significantly more robust than LDD, which in turn were significantly more robust
than Load-Push across all mutation levels (one-sided two-proportion Z-test with Bonferroni correction; n = 100 per
group; all pair-wise comparisons showed p < 0.05 after correction, max adjusted p = 0.042 for LDD vs. Load-Push at
8 mutations).

Evolving programs occasionally co-opted this difference, executing a conditional branch that triggers a HALT instruction
only when the value in D is non-zero. Although this conditional halting remained a minority strategy in absolute terms,
the probability of its emergence rose significantly as the metabolic penalty became more severe (Fig. 3B).
This behavior represents a case of one evolved sequence serving two distinct roles depending on the environmental
context. Because the same program is executed during both validation and interaction, the metabolic pressure on
computation (the task-solving phase) can shape how the program behaves during reproduction (the interaction phase),
even though the reproductive step itself carries no metabolic penalty. This provides a further example of how computation
and reproduction can become coupled within a single, short program.
2.5

Cross-niche pollination produces emergent curricula

To evaluate the learning capabilities of a system where reproduction and problem-solving co-evolve, we tested its
capacity to solve tasks of increasing complexity. In our system, solving higher-order polynomials depended crucially
on the spatial organization of the population. When programs were structured into niches that exchanged material
sparsely through cross-niche pollination, solutions to simpler tasks could seed niches working on harder ones. This
spatial structure allowed the population to advance through a sequence of intermediate problems, forming an emergent
curriculum that led toward a complex target. While such curricula are typically hand-designed by an experimenter to
guide evolutionary search, in our system they arose spontaneously from the way the reproductive process propagated
solutions across the grid.
The effectiveness of this emergent curriculum depends critically on the rate of program interaction between niches.
Varying the cross-niche pollination (CNP) rate (the probability that a program’s interaction partner is drawn uniformly
from the whole population rather than from its local neighborhood; see Methods) revealed that moderate rates of CNP
6

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

Figure 3: Impact of metabolic constraints on program halting behavior: (A) Average number of execution steps of
a run as a function of the strength of the metabolic penalty coefficient. Data points show values for individual runs (100
runs for each of the 8 penalty coefficients). Box plots show the median and interquartile range (IQR), with whiskers
extending to 1.5 × IQR. The penalty coefficient correlates negatively with the average execution length (Spearman’s
rank correlation; ρ = −0.61, p < 0.0001, N = 800). (B) Percentage of programs with different forms of halting
behavior. Data shown is median with bootstrapped 95% C.I. over 100 simulations with different random seeds for each
of the 8 penalty coefficients. The occurrence of conditional halting at the validation phase positively correlated with the
metabolic penalty coefficient (Spearman’s rank correlation; ρ = 0.21, p < 0.0001, N = 800).

Figure 4: Impact of niche dynamics on task success: (A) Percentage of simulations where at least N tasks are solved
for different rates of cross-niche pollination (CNP). A CNP rate of 0.05 solved significantly more tasks compared to
both the 0.0 and 0.5 rates (Mann-Whitney U test; vs. 0.0: U = 0.5, p < 0.0001; vs. 0.5: U = 6858.0, p < 0.0001;
n = 200 per group). (B) Percentage of simulations where at least N tasks are solved when there are niches (CNP)
or not (Single Task), and when the fitness function is smoothed or not. CNP significantly increased the number of
tasks solved compared to single-task setups under both coarse (U = 9979.0, p < 0.0001) and smooth (U = 9976.5,
p < 0.0001) fitness landscapes. However, there was no significant difference in performance between smooth and
coarse fitness in either setup (Mann-Whitney U test; all p > 0.65; n = 100 per group).

were essential for solving higher-order tasks (Fig. 4A). At one extreme, fully segregated niches (a rate of zero) solved
nothing beyond first-order polynomials, while at the other extreme, high rates impaired the evolution of solutions to
higher-order polynomials.
We tested whether explicitly smoothing the fitness function by other means could replicate the benefit of applying a
moderate CNP rate. The binary success/fail signal was therefore replaced with a graded one, scaling the interaction
probability linearly with how far a program’s outputs fell from the correct values on the validation inputs (see Methods
for the exact formulation). We ran a control setup where each of the tasks was evolved in complete isolation (the ‘Single
Task’ setup). In these runs, we kept the exact same overall compute budget and 512 × 1024 grid structure as the CNP
system. Consequently, the population dedicated to a single task (524, 288 programs) was 32 times larger than a single
128 × 128 niche in the CNP setup. Despite this 32-fold population advantage per task, these isolated populations failed
to progress, solving at most 15 of the simplest tasks out of the total set (Fig. 4B). In contrast, the CNP system, which
partitioned the same global population across 32 smaller, interconnected niches, drastically outperformed them. This
difference reveals a dynamic related to the objective paradox within algorithmic evolution—the phenomenon where
7

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

Figure 5: Evidence of an emergent curriculum: (A) Genealogy of programs based on most recent ancestors’ niches.
Note the non-uniform, non-symmetric genealogy, implying that solutions to certain tasks tend to evolve from existing
solutions to specific easier tasks. Red arrows indicate a common genealogical path, used for constructing the ‘optimal’
curriculum. (B) Success rate per task for the full cross-niche pollination system (top), a naive curriculum moving from
simple to harder tasks (middle), and a curriculum based on the genealogy shown by the red arrows in panel A (bottom).
Note the greater success on quadratic and cubic tasks for the optimal curriculum based relative to the simple curriculum.

directly optimizing for a complex target objective often prevents its discovery, whereas optimizing for intermediate
stepping stones succeeds. Assembling complex logic (such as nested accumulation loops for polynomial evaluation)
requires distinct, discontinuous algorithmic modules, and the spatial structure of the CNP system allowed these modules
to be combined across niches, whereas they would be unlikely to arise in a single-task population.

3

Discussion

In this paper, we examined the co-evolution of self-replication and problem solving within a digital primordial soup
(Fig. 1). Building upon Agüera y Arcas et al. [2024], we found that self-replication and task solutions both reliably
emerged from random noise. Unlike traditional evolutionary systems where reproduction is a fixed background rule,
here replication and problem-solving mechanisms co-evolved and shared a 32-byte memory. (It should be noted, though,
8

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

that unlike the case with the origins of life on Earth, our programs were initialized with elements that have predefined
computational semantics.) The transition from pre-evolutionary stochasticity to Darwinian evolution was shaped by the
pressure exerted by the tasks. This computational pressure drives a feedback loop where the demand to solve tasks
actively reshapes the machinery of heredity itself, steering populations away from naive copying mechanisms that
monopolize the tape and accelerating the emergence of more compact, robust replication architectures, such as LDIR and
LDD loops, that leave room for task-solving code (Fig. 2). In this way, the demands placed on what a program computes
feed back onto the architecture of how it reproduces. Similarly, metabolic constraints encouraged the evolution of
programs that halt at appropriate times to optimize their execution budget. Notably, these halting behaviors sometimes
evolved to function in a conditional manner, allowing programs to distinguish between validation and interaction
executions (Fig. 3).
We leveraged spatially structured task niches as a framework to investigate the learning capabilities of this coevolutionary system. In our experiments, populations working in isolation consistently failed to solve non-trivial
polynomials. This failure demonstrates that direct optimization toward a difficult target is fundamentally insufficient
in this landscape. Instead, partitioning the population into separate niches connected by sparse pollination allowed
the system to self-organize an evolutionary curriculum, where simpler tasks served as essential stepping stones to
seed solutions for more complex ones (Fig. 4). When we compared this self-organized process to a hand-designed
curriculum of steadily increasing complexity, the hand-designed path failed. This contrast highlights that the spatial
niche structure acts as a decentralized engine for discovering evolutionary pathways (Fig. 5).
One limitation of this study is that we did not systematically investigate the interaction dynamics for the emergence of
genetic diversification, such as recombination or symbiogenesis. Our interaction protocol does not preclude genetic
mixing, and accidental recombination may have played a role in evolutionary transitions. This contrasts with traditional
genetic algorithms where crossover is fixed a priori [Goldberg, 1989, Eiben and Smith, 2015]. However, most of
the dominant replicators we manually inspected employed asexual reproduction. Investigating whether programs can
spontaneously discover reciprocal genetic exchange remains an important direction for future work.
Another limitation of this study was that the tasks used (calculating polynomials) were, despite Z80 lacking a multiplication instruction, relatively simple and drawn from the same class. While the use of simple tasks and restricted
domains is in line with previous work on algorithmic evolution in ALife [Ofria and Wilke, 2004, Kumawat et al., 2025],
follow-up research could explore how tasks and self-replication co-evolve when the tasks and their domains are wider
and drawn from a real-world relevant set. Finally, there was a ceiling on the complexity of algorithmic solutions that
could be discovered, both due to the hard limit of 32-byte program lengths, and due to the absence of cooperative
mechanisms for programs to co-solve tasks. Future research could explore how self-replication and tasks co-evolve
when more complex, potentially multi-agent, solutions are possible.
In total, our work demonstrates that mechanisms of inheritance and fitness optimization can co-evolve to shape one
another, and supports the perspective that origin-of-life and evolutionary computation research can view evolution not
merely as a static search algorithm, but as a dynamic, plastic property of an open-ended learning system.

4

Methods

4.1

Competence-gated interaction and metabolic constraints

Interactions between programs are biased by their ability to solve the polynomial task assigned to their niche (Fig. 1C).
Before a selected program P1 is allowed to interact, it undergoes a validation phase. We place P1 in the first half of the
2ℓ-byte memory and zero the second half, and execute the tape for a maximum budget of B = 512 instructions. For
this validation run, the Z80 registers are initialized as follows: registers HL, BC, and E, and the program counter PC are
set to zero; register A and the stack pointer are set to 0xFF; and register D is initialized with the task input x. Since the
emulated address space is limited to 2ℓ bytes and every memory access is taken modulo 2ℓ, the stack pointer value 0xFF
resolves to the last byte of the tape, so stack writes grow backwards from the end of the memory. The output is read
from register E (which, being an 8-bit register, implicitly stores the result modulo 28 ). During the subsequent interaction
phase, the register initialization is identical, except that register D is initialized to zero rather than the task input.
To pass validation, P1 must satisfy E = f (x) mod 28 for three inputs drawn without replacement from {0, . . . , 15},
where f is the polynomial associated with P1 ’s niche. Evaluating a subset of three inputs is sufficient to make accidental
successes by incorrect programs highly improbable. Programs that pass receive an elevated interaction probability
psucc = 1.0; programs that fail keep the baseline probability pbase = 0.3.
9

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

To simulate metabolic constraints, we discount the interaction probability of validated programs in proportion to the
number of execution steps they spend during validation. The interaction probability is

p(interaction) =


p

succ − C



pbase

k
B

if validated
otherwise

where k is the average number of execution steps taken over the three validation runs, B = 512 is the maximum
instruction budget, and C is the metabolic penalty coefficient. The penalty is applied only to validated programs; the
probability of a failed program is fixed at pbase = 0.3 regardless of its execution cost. Unless otherwise stated we set
C = 0.3; the sweep reported in Fig. 3 instead varies C across [0, 0.7].
Validation is distinct from solving a task. Validation gates interaction and is decided on three sampled inputs, whereas
we report a task as solved on the basis of the full input range. Concretely, throughout the paper we count a niche as
having solved its task when at least 10% of its programs produce f (x) mod 28 correctly for every x ∈ {0, . . . , 15},
and not merely for the three validation draws.

4.2

Smooth fitness landscape control

In control experiments evaluating the impact of a smoothed fitness landscape, we replaced the binary success/fail
validation with a graded interaction probability. The probability was scaled linearly with the average numerical distance
between the program’s outputs and the target values across the validation inputs:
kC
512
P

penalty = 1 −

avg dist =

y∈f (X)

mod(y,ŷ)
128

|X|

p(interaction) = max (0.3, (1 − 0.7 · avg dist) · penalty)
where mod(a, b) refers to the distance between a and b modulo 256, X = {x1 , x2 , x3 } is the set of inputs for
verification, y = f (X) is the set of target outputs for the polynomial function f , and ŷ is the set of outputs from the
program for each input.

4.3

Simulation protocol

Simulations run for Tmax = 106 epochs starting from uniformly random bytes. Parameters are summarized in Table 1.

Table 1: Simulation parameters.
Program length ℓ
Instruction budget B
Global grid
CNP sub-environments
Baseline interaction prob. pbase
Success interaction prob. psucc
Cross-niche pollination π
Per-program mutation rate
Validation draws
Validation domain
Output modulus
Max epochs Tmax
Replicates per condition

10

32 bytes
512
512 × 1024
32 (each 128 × 128)
0.3
1.00
0.05
1/64
3 inputs, no replacement
x ∈ {0, . . . , 15}
28
106
100

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

Algorithm 1: Evolution through competence-gated interaction.
Input :Grid of 512 × 1024 programs in L sub-environments
Output :Evolution trace until epoch Tmax
Initialize all programs with random bytes
for epoch ← 1 to Tmax do
foreach program P do
With probability 1/64: mutate one random byte in P
Mark all programs as available
foreach program P1 in random order do
if P1 is available then
P2 ← random available von Neumann neighbour of P1
if P2 exists then
Mark P1 , P2 unavailable
if random() < π (CNP only) then
P2 ← random program from any sub-environment
Load target f for P1 ’s niche
if P1 produces f (x) mod 28 on 3 random x ∈ {0, .., 15} then
Execute concat(P1 , P2 ) with prob. psucc
else
Execute concat(P1 , P2 ) with prob. pbase
Split result into two ℓ-byte programs to replace P1 , P2

To implement the pairwise interaction loop in Algorithm 1 without overlapping or order bias, candidate pairs are
generated each epoch by randomly shuffling all grid positions and drawing a partner for each selected program. Because
programs can be drawn more than once across candidate pairings, any pair containing a duplicate program assignment
is filtered out before execution to ensure that no cell is evaluated or overwritten more than once per step. Because of
this filtering step, the pairing algorithm is stochastic, and a randomly varying number of programs (on average roughly
56% of the population) are selected every step for validation and interaction.
4.4

Replicator population dynamics with and without tasks

To understand the extent to which imposing task validation influences the underlying methods of replication, we
compared replicator population dynamics with and without tasks being applied. We present the results of this
investigation in Figs. 2D and 2E. To calculate the population counts, we used a byte-matching search to count known
replicators of each type. Specifically, we scanned for the following consecutive byte sequences corresponding to
key instructions for each replicator, which rely on the Z80’s core block-copy registers (HL for source address, DE for
destination address, and BC for copy length):
• LDIR ([0xED, 0xB0]): The repeating block-copy instruction. Setting HL to the start of parent P1 , DE to the
start of partner P2 , and BC to 32 copies the entire program automatically in a single step as pointers increment
and BC decrements to zero.
• LDDR ([0xED, 0xB8]): A close relative of LDIR that decrements the pointers instead of incrementing.
• LDI ([0xED, 0xA0]): A non-repeating variant of LDIR that increments pointers and decrements BC but does
not loop automatically.
• LDD ([0xED, 0xA8]): A non-repeating variant that decrements pointers and decrements BC but does not
loop automatically, requiring an explicit external loop to achieve replication.
• LoadPush families: Rely on a sequence of paired load and stack-push instructions (e.g., loading bytes into a
register and pushing them onto the stack). We tracked four variants based on the registers used:
– LoadPush (BC): [0x01, 0xC5, 0x01, 0xC5]
– LoadPush (DE): [0x11, 0xD5, 0x11, 0xD5]
– LoadPush (HL): [0x21, 0xE5, 0x21, 0xE5]
– LoadPush (HL_2): [0xE5, 0x2A, 0xE5, 0x2A]
We identified these key instructions by manually inspecting our runs and looking at execution traces to see what
elements of tape were responsible for replication.
11

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

A tape was counted if it contained the target sequence at least once. Formally, for a set of tapes T and a byte pattern p,
the population count Cp is given by:
Cp =

X

I(p ⊆ t)

t∈T

where I is the indicator function returning 1 if the pattern p exists as a contiguous subsequence in tape t, and 0 otherwise.
The overall counts for the LDIR and LoadPush families were calculated as the sum of these unique tape counts across
their respective variants (v):
X

CLDIR =

Cv

v∈{LDIR, LDDR, LDI, LDD}

CLoadPush =

X

CLoadPush(v)

v∈{BC, DE, HL, HL_2}

We note that this is not an exhaustive list of possible replicators, and likewise not a perfect search for replicators of this
type (for instance, a NO-OP instruction could easily exist between the bytes of an LDIR, and it would functionally
behave the same, but wouldn’t be picked up by our search). However, in all cases the sum of all replicator families
closely matches the total tape population size, so we expect the figures to be a sufficiently faithful count of the majority
of replicator tapes.
To generate Fig. 2D, we initialized 100 runs with different random seeds for each of the two experiment types: with task
validation applied, and without it. In both settings, the number of niches and the number of tapes remained the same.
For the experiments without task validation, we simply skipped the validation step (including penalizing execution
length), and every tape proceeds to interaction. We then computed the average population counts of the replicators
across these 100 seeds every 1000 steps.
To generate Fig. 2E, we repeated the same experiment as for Fig. 2D, but in this case we customized the Z80 emulator
we were using to turn the key instruction byte pairs for all the LDIR-family replicators except LDD into the equivalent
of NO-OPs. In other words, we deactivated all LDIR-family instructions except LDD. We then computed population
counts the same way as for Fig. 2D.
In both cases, Tasks Solved is defined as the number of niches where ≥ 10% of the tapes successfully solve the task
across the entire input domain.
4.5

Replicator robustness to mutations

To compare how well the three replicator architectures tolerate mutation (Fig. 2F), we measured whether each one
retains its ability to copy itself after a number of mutation events. We seeded each test with a canonical replicator of the
relevant type. The LDIR replicator was the four bytes [0x1E, 0x20, 0xED, 0xB0], which set register E to 32 and
then executed the LDIR instruction while relying on the default initialization HL = BC = 0, followed by 28 uniformly
random bytes drawn independently in each trial to fill the tape to 32 bytes. Because the LDIR instruction copies all 32
bytes verbatim, the content of this trailing region does not affect replication and is reproduced faithfully along with
the functional prefix. The LDD replicator was the eleven bytes [0x2E, 0x1F, 0x1E, 0x3F, 0x0E, 0x20, 0xED,
0xA8, 0x28, 0xFC, 0x76], which initialize registers L, E, and C, run the LDD instruction inside a loop closed by a
conditional relative jump, and end with a HALT, again padded with zeros to 32 bytes. The Load-Push replicator was the
byte pair [0x01, 0xC5], a load followed by a stack push, repeated sixteen times to fill the 32 byte tape.
Each robustness trial consisted of n successive mutation and replication cycles, with n ∈ {1, 4, 8}. In every cycle
we first mutated the current genome by selecting one byte position uniformly at random among its 32 positions and
replacing it with a uniformly random byte in {0, . . . , 255}, exactly as in the simulation’s mutation operator. Because
each position is drawn afresh, the replacement may coincide with the original byte and the same position may be
selected in more than one cycle. We then placed the mutated genome in the first half of a 2ℓ-byte tape, set the second
half to zeros, and executed the tape for up to B = 512 instructions under the same register initialization used during
interaction. The first half of the resulting tape, which holds the program itself, became the genome carried into the next
cycle. We classified a trial as a success when, on the final cycle, the second half of the executed tape, which had started
as zeros, was byte-for-byte identical to the first half, indicating that the mutated program had copied all 32 of its bytes
into the empty partner.
12

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

For each replicator type and each value of n we ran 100 independent trials and report the fraction that succeeded, with
error bars given by 95% Wilson score intervals. Pairwise differences between replicator types at each mutation level
were assessed with one-sided two-proportion Z-tests using Bonferroni correction across the comparisons.

4.6

Metabolic penalty sweep and halting behavior

To probe how the metabolic constraint shapes the evolved programs (Fig. 3), we swept the penalty coefficient C across
the eight values 0.0, 0.1, . . . , 0.7. For each value we ran 100 independent simulations, giving N = 800 runs in total.
Every run used the standard configuration of 32 niches with cross-niche pollination for 106 epochs. All quantities below
were measured on the final state of each grid.
For the average execution length (Fig. 3A), we performed a single validation run for every program in the final grid.
We set register D to one input x sampled uniformly from {0, . . . , 15} for each program, placed the program in the
first half of a 2ℓ-byte tape with the second half set to zeros, and executed for up to B = 512 instructions, recording
the number of instructions executed, which equals B when the program never halts. This per-program count is the
validation execution step quantity k plotted in Fig. 3A. We averaged this count over all programs in the grid to obtain
one value per run. The 100 values at each coefficient are shown as box plots, with median, interquartile range, and
whiskers at 1.5× the interquartile range, and the individual runs overlaid. The association between C and the per-run
average was quantified with Spearman’s rank correlation over the N = 800 runs.
For the halting behavior (Fig. 3B), we restricted attention to the programs that produced the correct output on a single
sampled input, that is, the programs whose validation run above returned E = f (x) mod 28 . Each such program was
executed in two environments that differ only in the value of register D, in both cases with the partner half of the tape set
to zeros and a budget of B = 512 instructions. In the validation environment register D held the sampled input x; in
the interaction environment register D was zero, as it is during a normal interaction. In each environment we recorded
whether the program reached a HALT within the budget or instead ran to the budget without halting, and we assigned
the program to one of four mutually exclusive categories: it halted in both environments (Both), only in the validation
environment (Validation), only in the interaction environment (Interaction), or in neither (Neither).
Within each run we normalized these counts to percentages of the filtered set of programs, so that the four categories
sum to 100% and every run carries equal weight regardless of how many programs it contributed. Each subplot of
Fig. 3B corresponds to one category: the bar height is the median percentage across the runs at that coefficient, and
the error bars are the 95% confidence interval of the median, obtained by non-parametric bootstrapping with 1000
resamples and drawing the lower and upper caps at the 2.5th and 97.5th percentiles of the resulting distribution of
medians. The Validation category corresponds to the conditional halting described in the main text, in which a program
halts during validation but skips the halt during interaction. Its association with C was quantified with Spearman’s rank
correlation over the N = 800 runs.

4.7

Computation of the ancestor contribution matrix

To trace the phylogenetic history of the emergent programs and uncover the evolutionary pathways (Fig. 5A), we
tracked the niche of origin for all lineages throughout the simulation. At initialization (epoch 0), every program in the
grid was labeled with an ancestor niche ID equal to its own niche j ∈ {0, . . . , L − 1}, where L = 32 is the total number
of niches. This label was then carried through interactions to record the most recent solved niche from which each
lineage received material. When a validated program P1 interacted with a neighbor P2 within its own niche, the two
programs written back in their place both took on P1 ’s ancestor niche ID. When instead a cross-niche pollination event
paired P1 with a partner P2 drawn from a different niche, the program written back in place of P2 adopted the current
niche index of P1 as its ancestor niche ID, but only when P1 ’s niche had already been marked as having solved its task.
A program’s ancestor niche ID therefore identifies the most recent solved niche from which its active replicating lineage
received material, defaulting to its niche of origin.
We defined a niche i as having successfully solved its assigned task i at the earliest epoch t where the fraction of
programs in the niche solving the task across the entire input domain (16 distinct inputs) was at least 10% (corresponding
to ≥ 1, 639 programs in a 128 × 128 subgrid). At this exact epoch, we recorded a snapshot of the ancestor niche IDs
of all programs in niche i. Specifically, we computed a raw ancestor contribution vector for niche i, where the j-th
component Ai,j represents the number of programs in niche i belonging to lineages that originated in niche j:
To aggregate this data across multiple independent runs, we performed the following normalization steps. First, for
each simulation run g ∈ {1, . . . , G} (where G = 2000 is the total number of random seeds), we normalized the raw
13

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

counts to obtain the relative contribution of each source niche to the solution of task i:
(g)

Ai,j
(g)
Ni,j = P (g)
k Ai,k
P (g)
(g)
conditioned on the task being solved in that run ( k Ai,k > 0), and setting Ni,j = 0 otherwise. Next, we computed
the conditional average of these relative contributions across all runs where task i was successfully solved:
PG
(g)
g=1 Ni,j
P

Vi,j = P
(g)
G
g=1 I
k Ai,k > 0
The matrix V represents the average proportion of the population in niche i originating from niche j at the moment the
task was solved, conditioned on task i being solved. Finally, to construct the unified heatmap (Fig. 5A), we applied a
row-wise min-max normalization to highlight the relative significance of different source niches for each target task,
independent of the absolute magnitude of contributions:
Wi,j =

Vi,j − mink Vi,k
maxk Vi,k − mink Vi,k

where Wi,j ∈ [0, 1] is the normalized relative contribution of source task j to target task i.
4.8

Curriculum learning

To investigate curriculum learning, we maintain the same spatial topology as the CNP configuration: a population of
Np = 524, 288 programs distributed across a grid divided into L = 32 separate niches (subgrids of 128×128 programs),
with local neighborhood pairing and a global cross-niche pollination rate of π = 0.05. However, instead of each niche
evaluating programs on a distinct static task from the task library, all L niches in the population are evaluated on the same
target task Ti at any given epoch. This target task is updated dynamically as the population traverses a linear curriculum
sequence C = ⟨t1 , t2 , . . . , tK ⟩, which is defined as either: Coptimal = ⟨2n, n2 +n, 2n2 +n, n3 +n2 +n, n3 +n2 +n+3⟩,
or Csimple = ⟨n, n2 , n3 , n3 + n, n3 + n2 + n, n3 + n2 + n + 3⟩.
To enable evolutionary scaffolding and prevent the loss of capabilities acquired in the previous step, the interaction
probability is:

kC
1.0 − 512
kC
p(interaction) = 0.65 − 512

0.3

if Ti validated
else if Ti−1 validated
otherwise

where Ti is the active task and Ti−1 is the immediately preceding task in the curriculum (with T0 defaulting to not
validated), k is the average number of execution steps taken over the three validation runs, B = 512 is the maximum
instruction budget, and C is the metabolic penalty coefficient.
The active curriculum task advances globally from Ti to Ti+1 (setting the target task for all niches to Ti+1 ) at the end of
any logging batch if at least one program in any of the niches successfully solves the active task in its complete domain.
The total computational budget is kept identical to the CNP benchmark runs.

Author Contributions
F.C., E.N., E.R., and B.R. designed research; F.C., E.N., E.R., and S.B. performed research; F.C., E.N., and A.B.
analyzed data; and F.C., E.N., E.R., S.B., A.B., M.E., R.S., C.K., B.L., J.M., B.A.A., and B.R. wrote the paper.

References
Martina Preiner, Silke Asche, Sidney Becker, Holly C. Betts, Adrien Boniface, Eloi Camprubi, Kuhan Chandru,
Valentina Erastova, Sriram G. Garg, Nozair Khawaja, Gladys Kostyrka, Rainer Machné, Giacomo Moggioli,
Kamila B. Muchowska, Sinje Neukirchen, Benedikt Peter, Edith Pichlhöfer, Ádám Radványi, Daniele Rossetto,
Annalena Salditt, Nicolas M. Schmelling, Filipa L. Sousa, Fernando D. K. Tria, Dániel Vörös, and Joana C.
Xavier. The future of origin of life research: Bridging decades-old divisions. Life, 10(3), 2020. ISSN 2075-1729.
doi:10.3390/life10030020. URL https://www.mdpi.com/2075-1729/10/3/20.
14

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

Walter Gilbert. Origin of life: The RNA world. Nature, pages 618–618, February 1986. doi:10.1038/319618a0. URL
https://www.nature.com/articles/319618a0.
Günter Wächtershäuser. The origin of life and its methodological challenge. J. Theor. Biol., 187(4):483–494, August
1997.
Doron Lancet, Raphael Zidovetzki, and Omer Markovitch. Systems protobiology: origin of life in lipid catalytic
networks. J. R. Soc. Interface, 15(144), July 2018. ISSN 1742-5689, 1742-5662. doi:10.1098/rsif.2018.0159. URL
http://dx.doi.org/10.1098/rsif.2018.0159.
Stuart A. Kauffman. Autocatalytic sets of proteins. Journal of Theoretical Biology, 119(1):1–24, 1986. ISSN 00225193. doi:https://doi.org/10.1016/S0022-5193(86)80047-9. URL https://www.sciencedirect.com/science/
article/pii/S0022519386800479.
Wim Hordijk and Mike Steel. Autocatalytic networks at the basis of life’s origin and organization. Life, 8(4), December
2018. ISSN 0024-3019. doi:10.3390/life8040062. URL https://www.ncbi.nlm.nih.gov/pmc/articles/
PMC6315399/.
Stuart A Kauffman. Investigations. Oxford University Press, 2000.
Tibor Gánti. The principles of life. Oxford University Press, 2003.
Freeman Dyson. Origins of life. Cambridge University Press, 1999.
Caleb Scharf, Nathaniel Virgo, H James Cleaves, II, Masashi Aono, Nathanael Aubert-Kato, Arsev Aydinoglu, Ana
Barahona, Laura M Barge, Steven A Benner, Martin Biehl, Ramon Brasser, Christopher J Butch, Kuhan Chandru,
Leroy Cronin, Sebastian Danielache, Jakob Fischer, John Hernlund, Piet Hut, Takashi Ikegami, Jun Kimura, Kensei
Kobayashi, Carlos Mariscal, Shawn McGlynn, Brice Menard, Norman Packard, Robert Pascal, Juli Pereto, Sudha
Rajamani, Lana Sinapayen, Eric Smith, Christopher Switzer, Ken Takai, Feng Tian, Yuichiro Ueno, Mary Voytek,
Olaf Witkowski, and Hikaru Yabuta. A strategy for origins of life research. Astrobiology, 15(12):1031–1042,
December 2015.
Walter Fontana. Algorithmic chemistry: A model for functional self-organization. In Artificial Life II, 1990. URL
https://api.semanticscholar.org/CorpusID:18574369.
Tim J. Hutton. Evolvable Self-Replicating Molecules in an Artificial Chemistry. Artificial Life, 8(4):341–356, 10 2002.
ISSN 1064-5462. doi:10.1162/106454602321202417. URL https://doi.org/10.1162/106454602321202417.
Germán Kruszewski and Tomáš Mikolov. Emergence of Self-Reproducing Metabolisms as Recursive Algorithms in an
Artificial Chemistry. Artificial Life, 27(3–4):277–299, 03 2022. ISSN 1064-5462. doi:10.1162/artl_a_00355. URL
https://doi.org/10.1162/artl_a_00355.
Martin A. Nowak and Hisashi Ohtsuki. Prevolutionary dynamics and the origin of evolution. Proceedings of
the National Academy of Sciences, 105(39):14924–14927, 2008. doi:10.1073/pnas.0806714105. URL https:
//www.pnas.org/doi/abs/10.1073/pnas.0806714105.
Blaise Agüera y Arcas, Jyrki Alakuijala, James Evans, Ben Laurie, Alexander Mordvintsev, Eyvind Niklasson, Ettore
Randazzo, and Luca Versari. Computational life: How well-formed, self-replicating programs emerge from simple
interaction, 2024. URL https://arxiv.org/abs/2406.19108.
S Spiegelman, I Haruna, I B Holland, G Beaudreau, and D Mills. The synthesis of a self-propagating and infectious
nucleic acid with a purified enzyme. Proc. Natl. Acad. Sci. U. S. A., 54(3):919–927, September 1965. ISSN
0027-8424. doi:10.1073/pnas.54.3.919. URL http://dx.doi.org/10.1073/pnas.54.3.919.
John Von Neumann and Arthur W. Burks. Theory of Self-Reproducing Automata. University of Illinois Press, USA,
1966.
Christopher G. Langton. Self-reproduction in cellular automata. Physica D: Nonlinear Phenomena, 10(1):135–144,
1984. ISSN 0167-2789. doi:https://doi.org/10.1016/0167-2789(84)90256-2. URL https://www.sciencedirect.
com/science/article/pii/0167278984902562.
Hiroki Sayama. Toward the realization of an evolving ecosystem on cellular automata. In Proceedings of the Fourth
International Symposium on Artificial Life and Robotics (AROB 4th ’99). unknown, February 1999.
Nicolas Oros and Chrystopher L. Nehaniv. Sexyloop: Self-reproduction, evolution and sex in cellular automata. In
2007 IEEE Symposium on Artificial Life, pages 130–138, 2007. doi:10.1109/ALIFE.2007.367788.
Thomas Schmickl, Martin Stefanec, and Karl Crailsheim. How a life-like system emerges from a simple particle motion
law. Sci. Rep., 6:37969, November 2016. ISSN 2045-2322. doi:10.1038/srep37969. URL http://dx.doi.org/
10.1038/srep37969.
Alexander Mordvintsev, Ettore Randazzo, Eyvind Niklasson, and Michael Levin. Growing neural cellular automata.
Distill, 2020. doi:10.23915/distill.00023. https://distill.pub/2020/growing-ca.
15

Co-evolution of self-replication and function in a digital primordial soup

C ICALA ET AL .

Lana Sinapayen. Self-replication, spontaneous mutations, and exponential genetic drift in neural cellular automata.
Qeios, May 2023. ISSN 2632-3834. doi:10.32388/JPUWVB. URL https://doi.org/10.32388/JPUWVB.
Oscar Chang and Hod Lipson. Neural network quine, 2018.
Ettore Randazzo, Luca Versari, and Alexander Mordvintsev. Recursively Fertile Self-replicating Neural Agents. volume
ALIFE 2021: The 2021 Conference on Artificial Life of Artificial Life Conference Proceedings, page 58, 07 2021.
doi:10.1162/isal_a_00367. URL https://doi.org/10.1162/isal_a_00367.
David E. Goldberg. Genetic Algorithms in Search, Optimization and Machine Learning. Addison-Wesley Longman
Publishing Co., Inc., USA, 1st edition, 1989. ISBN 0201157675.
Ettore Randazzo and Alexander Mordvintsev. Biomaker ca: a biome maker project using cellular automata, 2023.
Chris Lu, Michael Beukman, Michael Matthews, and Jakob Foerster. Jaxlife: An open-ended agentic simulator, 2024.
URL https://arxiv.org/abs/2409.00853.
Richard E. Lenski, Charles Ofria, Robert T. Pennock, and Christoph Adami. The evolutionary origin of complex
features. Nature, 423(6936):139–144, May 2003. ISSN 1476-4687. doi:10.1038/nature01568. URL http:
//dx.doi.org/10.1038/nature01568.
Charles Ofria and Claus O. Wilke. Avida: A software platform for research in computational evolutionary biology.
Artificial Life, 10(2):191–229, March 2004. ISSN 1530-9185. doi:10.1162/106454604773563612. URL http:
//dx.doi.org/10.1162/106454604773563612.
Bhaskar Kumawat, Alexander Lalejini, Monica M. Acosta, and Luis Zaman. Evolution takes multiple paths to evolvability when facing environmental change. Proceedings of the National Academy of Sciences, 122(1):e2413930121,
2025. doi:10.1073/pnas.2413930121. URL https://www.pnas.org/doi/abs/10.1073/pnas.2413930121.
Thomas S. Ray. Evolution and optimization of digital organisms. Scientific Excellence in Supercomputing, 1991. URL
https://cir.nii.ac.jp/crid/1571135649926553856.
Thomas S Ray. Evolution, complexity, entropy and artificial reality. Physica D: Nonlinear Phenomena, 75(1-3):
239–263, 1994.
Steen Rasmussen, Carsten Knudsen, Rasmus Feldberg, and Morten Hindsholm. The coreworld: Emergence and
evolution of cooperative structures in a computational chemistry. Physica D: Nonlinear Phenomena, 42(1):111–134,
1990. ISSN 0167-2789. doi:https://doi.org/10.1016/0167-2789(90)90070-6. URL https://www.sciencedirect.
com/science/article/pii/0167278990900706.
Steen Rasmussen, C. Knudsen, and Rasmus Feldberg. Dynamics of programmable matter. In J. D. Farmer et al., editor,
Proceedings of the Second Artificial Life Workshop, pages 211–254. Addison-Wesley, 1991.
A.N. Pargellis. The evolution of self-replicating computer organisms. Physica D: Nonlinear Phenomena, 98(1):111–127,
1996. ISSN 0167-2789. doi:https://doi.org/10.1016/0167-2789(96)00089-9. URL https://www.sciencedirect.
com/science/article/pii/0167278996000899.
Christoph Adami. Introduction to Artificial Life. Springer, 1998.
C. P. Kempes et al. Drivers of bacterial maintenance and minimal energy requirements. Frontiers in Microbiology, 8:31,
2017.
Kenneth O. Stanley and Joel Lehman. Why Greatness Cannot Be Planned: The Myth of the Objective. Springer
Publishing Company, Incorporated, 2015. ISBN 3319155237.
Joel Lehman and Kenneth O. Stanley. Abandoning objectives: Evolution through the search for novelty alone.
Evolutionary Computation, 19(2):189–223, 2011.
Sewall Wright. The roles of mutation, inbreeding, crossbreeding, and selection in evolution. In Proceedings of the Sixth
International Congress of Genetics, volume 1, pages 356–366, 1932.
Paul B. Rainey and Michael Travisano. Adaptive radiation in a heterogeneous environment. Nature, 394(6688):69–72,
1998.
A. E. Eiben and J. E. Smith. Introduction to Evolutionary Computing. Natural Computing Series. Springer, Berlin,
Heidelberg, 2nd edition, 2015.

16
