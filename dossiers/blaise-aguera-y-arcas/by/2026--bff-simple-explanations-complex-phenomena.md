---
title: "BFF: Simple explanations for complex phenomena"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2026
date: 2026-07-01
venue: "arXiv (Cornell University)"
authors: "Charlotte Knierim, Luca Versari, Robert Obryk, Blaise Agüera y Arcas, Rif A. Saurous"
source_url: https://doi.org/10.48550/arxiv.2607.01483
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W7167265539, W7167380584 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2607.01483."
---

# BFF: Simple explanations for complex phenomena

## Full text

### Abstract (from OpenAlex metadata)

The ''Computational Life'' paper (Agüera y Arcas et al., 2024) argues that paired interactions in a computational soup are an effective way to find self-replicators. In this work, aided by recent developments in self-replicator detection, we explore the alternate hypothesis that self-replicators can be found at least as easily using simple mutation random walks in program space. We also explore the claim that capping the maximum ''depth'' and ''width'' of the ancestry tree stops self-replicators from emerging, showing instead that it merely stops self-replicators from taking over the soup.

---

BFF: Simple explanations for complex phenomena
Charlotte Knierim, Luca Versari, Robert Obryk, Blaise Agüera y Arcas, Rif A. Saurous

arXiv:2607.01483v1 [cs.NE] 1 Jul 2026

Google, Paradigms of Intelligence Team
July 3, 2026
Abstract
The “Computational Life” paper (Agüera y Arcas et al., 2024) argues that paired interactions in a
computational soup are an effective way to find self-replicators. In this work, aided by recent developments in self-replicator detection, we explore the alternate hypothesis that self-replicators can be found
at least as easily using simple mutation random walks in program space. We also explore the claim
that capping the maximum “depth” and “width” of the ancestry tree stops self-replicators from emerging,
showing instead that it merely stops self-replicators from taking over the soup.

1

Introduction

In the “Computational Life” paper (Agüera y Arcas et al., 2024), self-replicators were detected by observing
that they had “taken over” a computational soup. We observed this transition by measuring the size of a
compressed version of the soup, which rapidly becomes significantly smaller as a self-replicator takes over the
soup. In the interim, we have developed (reasonably) reliable direct self-replicator detectors. These detectors
allow us to disentangle the initial appearance of self-replicators, which occurs in system with random mutation
alone as well as ones with program interaction alone, and their widespread diffusion through the soup, which
requires program interaction.
The work presented here suggests that, in BFF, distributionally tuned random mutation is at least
as powerful as pairwise interactions for finding self-replicators, and potentially for evolving programs with
specific purposes.

1.1

Overview

The BFF system consists of a soup of random strings of length 64 (also called tapes). Those tapes are
interpreted as programs in BFF, a dialect of the Brainfuck language [5]. The I/O in BFF works via two
heads that also sit on the tape, meaning that programs can modify themselves while they run.
The system runs by repeatedly choosing two programs uniformly at random, concatenating them and
running the result, length 128, as if it were a single program.1 After execution, the tapes are taken apart
and the two pieces are placed back into the soup in their new state.
Note that we have seen many different variants of BFF: different ways to map bytes to ops, slightly
different operator sets, different soup sizes, interactions with all programs paired up simultaneously or one
interaction at a time. This document aims to be generic in the BFF dialect; we repeated the experiments
for multiple variants, with very similar results. The main variant we use, bff_selfmove [3], only has one
copy operation and automatically moves the read head on a copy.

1.2

Main Results

Our primary finding is that we can easily find BFF self-replicators by executing a simple “random walk
mutation” process in program space faster than we can find them by evolving the soup via paired computation.
1 We have an upper bound on the number of steps in case the resulting program has an infinite loop.

1

We measure time according to the number of programs seen during the process, and observe faster selfreplicator emergence.
Statistics on the number of self-replicators in other computational systems and parallels to biology have
been explored in [4].
More generally, these experiments support the view that program interaction in BFF (or similar systems
involving the dyadic interaction of short fixed-length tapes) is not an unusually powerful search operator.
We continue to believe, for substantial theoretical and empirical reasons, that biology makes powerful use of
recombination (both standard crossover and horizontal gene transfer (HGT)). However, we do not currently
consider program interaction in BFF to be an effective model of these processes. Finding good computational
instantiations of crossover and HGT remains an open problem.
As a second finding we present an analysis of compositionality in the BFF system. Even if the system
does not find self-replicators faster than a random process, if we could see that self-replicators emerge in a
compositional way that would be an interesting connection to biological evolution. We define a merger to be
a consecutive copy of multiple bytes that have not been previously copied together. We conduct experiments
that limit the depth or width of a merger. The depth of a merger captures the compositional complexity of
the resulting string: a string of high depth implies that it is composed of strings that have been merged and
copied previously. The width of a merger controls how much complexity a single step can add. We show
that even if we block low-depth and low-width mergers, the system still generates self-replicators, although
blocking merges does stop them from taking over the soup.
We start this document with a short section that introduces how our self-replicator detection works.
Afterwards, we describe the experiments we conducted and the conclusions drawn from them.

2

Self-replication detector

To better identify whether there are self-replicators in the soup, we developed a self-replication detector.
Intuitively, we want to test that a given program produces children that are identical to itself independently of what the program it is with (as long as the program is the first one in the pair). However, an
exact comparison is not what we want: some self-replicators copy their functionality and most of their bytes
but have some non-executed bytes that are kept from the original program. Similarly, some self-replicators
invert themselves and will produce an exact copy only after an even number of executions. The following is
a pseudo-code version of our self-replication detector [2]:
Algorithm 1 Self-replication detection
Input: Program P
for i ∈ [0..9] do
Initialize tape Ti with the first half Ti,1 and the second half Ti,2
Ti,2 ← P
repeat 5 times
Ti,1 ← Ti,2
Ti,2 ← N oise
Run tape Ti
end
end for
Compare the results (see text)
For the result comparison, we collect the nine final tapes together and compare their halves separately.
For the first halves, we compute the number of bytes that match the original program in at least three of
the final tapes. For the second halves, we count the number of bytes that are identical in at least three of
the resulting tapes. We do not compare the second halves to the first halves, as there are self-replicators
that invert themselves in each iteration. We take the minimum score over the first and the second half and
use that as the self-replication score. Note that in most cases the comparison of the first halves will be the
2

minimum and the comparison of the second halves can be seen as extra robustness against breaking when
encountering a 0 during execution. A schematic drawing of the process is depicted in Figure 1.
The basic intuition is that a self-replicator can replicate itself reliably and repeatably. The parameters are
chosen somewhat arbitrarily: small enough to have a fast runtime, yet large enough to avoid false positives.
We extend the chain of running the programs to a length of five to ensure it keeps being functional after
executing itself, we have different branches to ensure the self-replicator is robust. We check for bytes in the
exact same position, so our detector does not fire for “semi-replicators” that copy themselves into a different
position on the destination tape. Ensuring that the length of this chain is odd is important, as this allows
us to detect self-replicators that invert themselves with every execution.
The self-replication score is an integer between 0 and 64. Note that requiring the program to have a score
of 64 would require the program to exactly self-replicate itself, which often does not happen: not all bytes
are important for functionality, so it is acceptable for a self-replicator to leave some bytes of the program
untouched.
We consider a program to be a self-replicator if the self-replication score is at least 48. This is a somewhat
arbitrary choice, and results do not change significantly for thresholds of at least ≈ 20. Intuitively, if the
program is classified as a self-replicator, then the resulting tapes agree on a fraction of the bytes that is much
higher than sampling nine random tapes would explain. In this case, the program must have successfully
written bytes in a way such that even after five iterations it is still functional, which is rare for anything
that is not a self-replicator2 .

3

BFF experiments

In this section, we describe experiments in the BFF setting. Most of the experiments replace the standard
BFF interactions with a random process that alters the tapes.
We will compare BFF’s execution model to a simpler model which mutates individual programs. Of
course, a random process that treats programs as independent entities will never lead to the soup being
taken over. But if we compare the BFF system to the creation of life, then we are much more interested in
the moment the first living being or self-replicator emerges. The development of our self-replicator detector
makes this measurement possible.
To compare how long a system takes to self-replication is we consider two different metrics. In the
first approach, we compare the number of programs tested for self-replication. That is, a single interaction
potentially changes both programs so we re-test both programs after every interaction, meaning that each
interaction counts as two tested programs. In the second approach, we measure the number of bytes changed
in the system. This metric might seem like the more fair comparison if we think that sampling the program
from scratch every time injects too much entropy into the system. Both of these analyses take advantage of
our self-replicator detector.

3.1

Sampling random programs

As a baseline, we tested how long running the BFF system takes to see the first self-replicator. While
previous work (see [1]) has always looked at the point the soup gelates (takes over the soup), we instead use
our self-replication test. This also allows us to observe situations where a self-replicator appears but dies
out before taking over a significant fraction of the soup.
All sampling experiments in this section were conducted by sampling 109 random programs. When
comparing a beta prior to a beta posterior in this setting, the variance is on the order of at most 103 and
thus negligible compared to the differences in means we observe.
2 One program that gets a very high score when testing for self replication is a program that consists of the alternating byte
sequence 128, 130 with a minimal copy program (4 bytes long) in positions 3 to 6. This way, as the head positions are two
apart, in each execution the program shifts itself by two positions. As most of the program is invariant to this shift, this causes
56 bytes to still be the same as in the original program but eventually the functional copy mechanism will wrap around to the
front and be destroyed

3

New random program

Program

Execute

Execute

Execute

Execute

Start 9
independent
execution
paths

Execute

Execute

Execute

Execute

Execute

Execute

Collect all
the results
and the
starting
program
Compare the bytes. Count the
number of positions that are equal
to the starting program in at least
3 out of the 9 programs for
positions in the first half (0-63),
and count the number of positions
from the second half (64-127) that
agree on the byte value in at least
3 out of the 9 programs.

Take the
minimum over
those two counts
to be the
self-replication
score of the
starting program

Figure 1: A schematic drawing of the self-replication detector

4

216
215
214
213
0

32

64

96

128

160

192

224

256

Figure 2: Frequencies of lasting changes into a given character (logscale on y). Here, by “lasting” we mean
that if a byte gets changed multiple times during the same interaction, we only consider the last of these
changes.
Experiment 3.1 The average time to first self-replicator in BFF is ≈ 2.5 · 106 interactions, which corresponds to 5 · 106 programs tested. This was measured by taking the average over 100 seeds.
One easy way to compare BFF to a random process is to replace every interaction with a process that
creates two completely new random tapes. In this setting, we simply sample programs uniformly at random
until a self-replicator is found.
Experiment 3.2 When sampling random byte strings of length 64, we see 2.9 · 107 programs on average
before finding a self-replicator.
Comparing Experiments 3.1 and 3.2, we see that pure random sampling is about 6 times slower than
running BFF.
Experiment 3.2 sampled programs from a uniform distribution over bytes. However, only a small fraction
of bytes are BFF operators. We now consider settings where we sample from a distribution better suited to
find self-replicators.3 For this, we first looked at the distribution of bytes written by the BFF system.
Definition 3.3 We define the distribution BF F to be the distribution where bytes are drawn according to
the frequencies given in Figure 2. This distribution was empirically measured by recording which bytes the
BFF system writes shortly before a self-replicator takes over the soup.
We now use this distribution to sample bytes when creating random bytes.
Experiment 3.4 When sampling random byte strings of length 64, where every byte is sampled from BF F,
we see 1.7 · 106 programs on average before finding a self-replicator.
This is roughly a factor of 3 faster in terms of programs tested than running the BFF system.
If the distribution discovered by BFF were the best distribution one could find, then we could argue
that the value in running the BFF system lies in discovering this distribution and it might be hard to find
a similarly good distribution manually or with a randomized strategy. The next experiment shows that this
is not the case.
Definition 3.5 Define the distribution CU ST as follows: for each byte b, we flip a fair coin to decide
whether b is an operator or a no-op, then choose b uniformly at random from the chosen class.
Experiment 3.6 When sampling random byte strings of length 64, where every byte is sampled from CU ST ,
we see 4.5 · 105 programs on average before we find a self-replicator.
3 To make a biological analogy, we imagine a “soup” that is enriched with the precursors of life relative to a completely
random soup.

5

This is a factor of 10 times more efficient at finding self-replicators than running BFF.
We introduce a slight optimization of this distribution, where we add the byte with value 64 to the
operator bucket. The rationale behind this is to make it easier to start with head positions that are exactly
64 positions apart. Head positions that are exactly 64 apart imply that the two heads start in the same
location in the first and second program respectively. This makes producing an exact copy of the first
program much easier as there is no need to align the heads first.
Definition 3.7 Define the distribution CU ST 64 as follows: for each byte b, we flip a fair coin to decide
whether b is in the class of ‘operator or 64’ or a no-op, then choose b uniformly at random from the chosen
class.
Experiment 3.8 When sampling random byte strings of length 64, where every byte is sampled from
CU ST 64, we see 9.4 · 104 programs on average before we find a self-replicator.
This is roughly a factor of 25 times more efficient at finding self-replicators than running BFF.
One could argue that the experiments from this section change the system more than running BFF does
and this explains the difference in speed. In the next section, we change our method from sampling whole
programs to a random process that mutates every byte with a given probability p.

3.2

Analyzing the number of changed bytes

In our next experiment, we measured the number of bytes changed in the BFF system in every interaction.
We chose the mutation probability p by measuring the number of changed bytes per interaction with varying
rates that are similar to the rate of change we observed in the BFF system.
The probability p can be seen as a parameter chosen by the BFF system, similar to the distribution of
characters we write. In bff_selfmove, the fraction of bytes that change per interaction grows from 1/100
to ≈ 1/50 and then sharply increases as the soup gelates4 .
The experiments in this section look at the following random process:
1. Start with a random soup.
2. Mutate every byte in the soup with probability p, according to a given distribution.
3. Check all the programs for self-replicators.
4. Repeat Steps 2 and 3 until we find a self-replicator.
We ran this for different distributions and mutation probabilities. The results are summarized in Table 1.
Note that the setup with p = 1 is identical to the experiments in Section 3.1. All results in this table were
obtained by testing 1010 programs each. For almost all of the results the variance is at least an order of
magnitude smaller than the expected time to self-replication. For the uniform distribution with mutation
probability of 1/100 and 1/200 the values are only about one variance apart and can thus not be ordered
with certainty.
In Figure 3 we plot the durations from Table 1 for each of the distributions. One can clearly see they
behave in a similar pattern, just shifted. With increasing mutation rate the time until we find a self-replicator
goes down for all the distributions. If we constrain ourselves to mutation probabilities that are on the lower
range of what we see in the BFF system, we can still outperform the BFF system if we choose the right
distribution (using CUST 64 beats running the BFF system even for p = 1/200).
From these experiments, we can conclude that the BFF system is not better than our simple random
process at finding self-replicators. It is left to ask whether running the BFF system exhibits other interesting
properties.
4 For other BFF dialects, this value tends to stay constant at values in the range 1/200 → 1/100 before increasing due to
gelation. We have not looked into why different systems behave differently in this regard. However, we do not consider this
crucial for this write-up.

6

Programs tested until self-replicator

Table 1: Expected time to find 1 replicator (Total Programs Tested / Replicators Found).
Mutation Probability Uniform
BF F
CU ST
CU ST 64
1
8
7
6
9.5 · 10
3.5 · 10
7.9 · 10
1.9 · 106
200
1
4.4 · 108
1.9 · 107 4.1 · 106 9.9 · 105
100
1
8
2.0 · 10
1.0 · 107 2.1 · 106 5.2 · 105
50
1
2.9 · 107
1.7 · 106 4.5 · 105 9.4 · 104

109
108
107

BFF System (5 · 106 )

106
105
10

4
1
200

1
100

1

1
50

Mutation probability

Uniform
BFF
CUST
CUST64

Figure 3: Programs tested until we find the first self-replicator

3.3

Blocking experiments

The idea of having more and more complex programs appear over time echoes biological evolution where
more and more complex life forms evolve from previous ones. A natural way to test for compositionality in
a system is to limit the depth of a merger, defined as a consecutive copy of at least two bytes that were not
copied together before. These mergers, over the history of the soup, form a tree.
The depth of a merger is the depth it has in the merger tree. Limiting this depth means that we forbid
the BFF system from completing mergers above a specific depth: if such a merger happens, we cancel the
interaction and return the programs to the soup in their original state. Similarly, we can define the width of
a merger to be the number of unique parents a string5 has in this tree, and we can ask what happens if we
prohibit mergers above a certain width. Both notions capture the complexity of the strings arising from the
BFF process.
The idea of a compositional structure, and with it the essentialness of merger depth or width for the
discovery of self-replicators, in a sense contradicts the results we saw in Sections 3.1 and 3.2. Randomness
is not able to construct mergers, as every program develops independently. To give a conclusive answer to
the question of whether randomness explains everything that is going on in the BFF system, we analyze the
setup with limited merger depth or width in more detail.
In Figure 4, we track the time until the first self-replicator appears, with various limits on depth and
width. We see that emergence of self-replicators is quite robust to merger blocking, with the process merely
slows down somewhat when the depth or width limit is as low as 2.
Note that limit 0 (and also 1 in case of depth) is special: it forbids any kind of copy, which means that
the only way to find self-replicators is to use + and - to modify the bytes. This is a restriction that goes
beyond just blocking mergers: in particular, it is significantly more restrictive than the random walk setting.
This system still finds self-replicators, it is just significantly slower. When running for 50 million epochs, the
5 The tree looks at strings that are created with copy operations of consecutive source bytes instead of complete programs.

7

Figure 4: Percentages of runs that see a self-replicator with different restrictions for mergers
percentage of programs that find a self-replicator already increases to 40%.
This gives evidence for the hypothesis that limiting the width or depth of a merger does not actually
prevent the emergence of self-replicators, but rather prevents them from taking over the soup. Thus compositionality is not needed for the discovery of self-replicators in the BFF system.

Acknowledgments
We thank Vassilis Papadopoulos for bringing the issue of randomness being fast at solving self-replicators to
our attention and for the fruitful discussions.

References
[1] Blaise Agüera y Arcas, Jyrki Alakuijala, James Evans, Ben Laurie, Alexander Mordvintsev, Eyvind
Niklasson, Ettore Randazzo, and Luca Versari. Computational life: How well-formed, self-replicating
programs emerge from simple interaction. arXiv preprint arXiv:2406.19108, 2024.
[2] Self-replication
detector
in
the
CUBFF
codebase
https://github.com/paradigms-ofintelligence/cubff/blob/main/common_language.h. [Online; accessed 24-Feb-2026].
[3] bff_selfmove
in
the
CUBFF
codebase
https://github.com/paradigms-ofintelligence/cubff/blob/main/bff_selfmove.cu. [Online; accessed 24-Feb-2026].
[4] Nitash C G, Thomas LaBar, Arend Hintze, and Christoph Adami. Origin of life in a digital microcosm.
Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences,
375(2109):20160350, 11 2017.
[5] Müller, Urban. dev/lang/brainfuck-2.lha,1993.https://aminet.net/package/dev/lang/brainfuck-2.
[Online; accessed 24-Feb-2026].

8
