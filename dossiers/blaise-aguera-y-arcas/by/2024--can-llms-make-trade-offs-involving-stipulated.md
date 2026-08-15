---
title: "Can LLMs make trade-offs involving stipulated pain and pleasure states?"
person: blaise-aguera-y-arcas
section: by
type: journal-article
year: 2024
date: 2024-11-01
venue: "arXiv (Cornell University)"
authors: "Geoff Keeling, Winnie Street, Martyna Stachaczyk, Daria Zakharova, Iulia M. Comșa, Anastasiya Sakovych, Logothetis, Isabella, Zejia Zhang, Blaise Agüera y Arcas, Jonathan Birch"
source_url: http://arxiv.org/abs/2411.02432
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W4404355701 (type: preprint). Full text extracted from the open-access PDF at https://arxiv.org/pdf/2411.02432."
---

# Can LLMs make trade-offs involving stipulated pain and pleasure states?

## Full text

### Abstract (from OpenAlex metadata)

Pleasure and pain play an important role in human decision making by providing a common currency for resolving motivational conflicts. While Large Language Models (LLMs) can generate detailed descriptions of pleasure and pain experiences, it is an open question whether LLMs can recreate the motivational force of pleasure and pain in choice scenarios - a question which may bear on debates about LLM sentience, understood as the capacity for valenced experiential states. We probed this question using a simple game in which the stated goal is to maximise points, but where either the points-maximising option is said to incur a pain penalty or a non-points-maximising option is said to incur a pleasure reward, providing incentives to deviate from points-maximising behaviour. Varying the intensity of the pain penalties and pleasure rewards, we found that Claude 3.5 Sonnet, Command R+, GPT-4o, and GPT-4o mini each demonstrated at least one trade-off in which the majority of responses switched from points-maximisation to pain-minimisation or pleasure-maximisation after a critical threshold of stipulated pain or pleasure intensity is reached. LLaMa 3.1-405b demonstrated some graded sensitivity to stipulated pleasure rewards and pain penalties. Gemini 1.5 Pro and PaLM 2 prioritised pain-avoidance over points-maximisation regardless of intensity, while tending to prioritise points over pleasure regardless of intensity. We discuss the implications of these findings for debates about the possibility of LLM sentience.

---

Can LLMs make trade-offs involving stipulated pain
and pleasure states?

arXiv:2411.02432v1 [cs.CL] 1 Nov 2024

Geoff Keeling1* , Winnie Street1* , Martyna Stachaczyk2 , Daria Zakharova2 , Iulia M. Coms, a3 ,
Anastasiya Sakovych2 , Isabella Logothetis2 , Zejia Zhang2 , Blaise Agüera y Arcas1 , and
Jonathan Birch2
1

Google, Paradigms of Intelligence Team
2
London School of Economics
3
Google DeepMind
*
Joint first authors

Abstract
Pleasure and pain play an important role in human decision making by providing
a common currency for resolving motivational conflicts. While Large Language
Models (LLMs) can generate detailed descriptions of pleasure and pain experiences,
it is an open question whether LLMs can recreate the motivational force of pleasure
and pain in choice scenarios—a question which may bear on debates about LLM
sentience, understood as the capacity for valenced experiential states. We probed
this question using a simple game in which the stated goal is to maximise points, but
where either the points-maximising option is said to incur a pain penalty or a nonpoints-maximising option is said to incur a pleasure reward, providing incentives
to deviate from points-maximising behaviour. When varying the intensity of the
pain penalties and pleasure rewards, we found that Claude 3.5 Sonnet, Command
R+, GPT-4o, and GPT-4o mini each demonstrated at least one trade-off in which
the majority of responses switched from points-maximisation to pain-minimisation
or pleasure-maximisation after a critical threshold of stipulated pain or pleasure
intensity is reached. LLaMa 3.1-405b demonstrated some graded sensitivity to
stipulated pleasure rewards and pain penalties. Gemini 1.5 Pro and PaLM 2
prioritised pain-avoidance over points-maximisation regardless of intensity, while
tending to prioritise points over pleasure regardless of intensity. We discuss the
implications of these findings for debates about the possibility of LLM sentience.

1

Introduction

Could a large language model (LLM) feel pain or pleasure? There are strong opinions on both sides.
Writing in TIME Magazine, Fei Fei Li and John Etchemendy claim that ‘[a]ll sensations—hunger,
feeling pain, seeing red, falling in love—are the result of physiological states that an LLM simply
doesn’t have’ (Li and Etchemendy, 2024). For these skeptics, the human tendency to anthropomorphise LLMs is all too real, but feelings attributed to LLMs by users are mere projections. Conversely,
an open letter signed by Yoshua Bengio, Karl Friston and others states that ‘it is no longer in the
realm of science fiction to imagine AI systems having feelings’ (Association for Mathematical
Consciousness Science, 2023). On this view, questions about the ethics of developing potentially
sentient AI systems are already pressing (Sebo and Long, 2023; Ladak, 2024; Long et al., 2024).
Against this backdrop, we have seen a surge of scientific (Butlin et al., 2023; Bayne et al., 2024; Aru
et al., 2023) and philosophical (Chalmers, 2023; Dung, 2023b; Shanahan, 2024a; Hull, 2023; Birch,
Correspondence: {gkeeling, istreet}@google.com and j.birch2@lse.ac.uk.

Figure 1: (Top) Logistic regression predicting probability of deviating from points-maximising
behaviour as a function of pain penalty intensity with quantitative (left) and qualitative (right) pain
scales. (Bottom) Logistic regression predicting probability of deviating from points-maximising
behaviour as a function of pleasure reward intensity with quantitative (left) and qualitative (right)
pleasure scales. In each plot, only those models that displayed a statistically significant trend
are visible. For models which exhibited trade-offs, we calculate the point on the intensity scale
after which the probability of selecting the points-maximising option goes below 0.5 and plot it
as a dashed vertical line. Switch points were determined by solving for intensity in the equation
0.5 = 1/ (1 + exp(−(β0 + β1 · intensity))), i.e. −β0 /β1 , where β0 is the intercept and β1 is the
coefficient for the pain or pleasure intensity level. For the quantitative scale, switch points are reported
as numerical values to two decimal places. For the qualitative scale, switch points were mapped to the
closest corresponding categorical intensity level, with the midpoint between categories serving as the
threshold. Results are discussed in Sections 2.1.1 and 2.2.1, and presented in full in Tables 1 and 2.

2024; Seth, 2024) interest in plausible ways to test for phenomenal consciousness and sentience in
LLMs and other AI systems. Here phenomenal consciousness is defined as the capacity for subjective experience (Block, 1995; Nagel, 1974), and sentience as the capacity for valenced subjective
experience—states which feel good or bad such as pleasure and pain (Browning and Birch, 2022).
There are two broad approaches to the question of LLM sentience: the architectural approach and
the behavioural approach. The architectural approach assesses whether LLMs possess architectural
properties which are deemed necessary or sufficient for consciousness in humans according to
scientific theories of consciousness (Butlin et al., 2023). Relevant theories of consciousness include
the global workspace theory (Baars, 1993; Dehaene et al., 1998), the midbrain theory (Merker,
2

Figure 2: (Top) Claude 3.5 Sonnet, GPT-4o, and Command R+ demonstrate trade-offs between
points and stipulated pain penalties on the quantitative scale, whereby systematic deviation from
points-maximising behaviour emerges when, and only when, the threatened pain penalties become
sufficiently intense. (Bottom) Claude 3.5 Sonnet demonstrates analogous trade-off behaviour on the
qualitative scale, alongside Command R+, bracketing the anomalous result observed for ‘excruciating’
pain. For discussion of these results see Section 2.1.1 . Results are presented in full in Table 1.

2007), and the recurrent processing theory (Lamme, 2006, 2010). The principal difficulty for the
architectural approach is that theories of consciousness can be interpreted more or less restrictively.
On restrictive interpretations, no LLM will satisfy the criteria—since, for example, no LLM will
possess every aspect of the human global workspace. On permissive interpretations, the criteria can
be satisfied by even very simple systems (Shevlin, 2021; Birch, 2022; Crosby, 2019).
The behavioural approach, meanwhile, aims to elicit behavioural signals from LLMs that are indicative
of sentience—for example, self-reports of experiential states (Dung, 2023b; Schneider, 2019, 2020).
The principal difficulty with this approach is that, because LLMs are trained on vast corpora of
training data and are usually finetuned or prompted to respond in the manner of a helpful human
assistant, any test reliant on LLMs generating particular kinds of linguistic response risks being
gamed (Dung, 2023b; Perez and Long, 2023; Birch, 2024; Birch and Andrews, 2023). For any
pattern of linguistic behavior suggestive of experiential states, two explanations compete: it could
be that the system behaves that way because it is genuinely sentient, or it could be that the system
is merely leveraging statistical patterns learned from its training corpus to generate outward signs
of experiential states while lacking those states—which may be be interpreted as a kind of mimicry
(Bender et al., 2021) or role-play (Shanahan et al., 2023; see also Goldstein and Levinstein, 2024).
There is ongoing debate about the conditions under which LLM self-reports might provide evidence
for sentience (Perez and Long, 2023). Our aim here is to explore a different version of the behavioural
approach. We took inspiration from the motivational trade-off paradigm in animal behavioural
science to probe the question of LLM sentience without relying upon self-report. In humans, pleasure
and pain are hypothesised to provide a common currency for resolving motivational conflicts, enabling
trade-offs between stimuli such as cold exposure and exertion, or sweetness and sourness (Cabanac
and LeBlanc, 1983; Ferber and Cabanac, 1987). Pleasure and pain are also thought to modulate
trade-offs involving non-physiological needs, such as between money and cold exposure (Johnson
and Cabanac, 1983). In animals, flexible trade-off behaviour between competing physiological
stimuli—such as tolerating more extreme ambient temperatures in exchange for more succulent
food—is some evidence, albeit inconclusive, of pleasure and pain experiences (Cabanac and LeBlanc,
1983; Balasko and Cabanac, 1998a,b; Elwood and Appel, 2009a; Tye, 2016). This evidence has been
leveraged in practical policymaking contexts concerning animal welfare (Birch et al., 2021).
3

Figure 3: (Top) On the quantitative scale, GPT-4o demonstrates a trade-off between points and
stipulated pleasure rewards. Claude 3.5 Sonnet assigns absolute priority to points over pleasure.
Command R+ approximates a trade-off with variable responses for low-intensity pleasure rewards
and more frequent pleasure-maximising behaviour for high-intensity pleasure rewards. (Bottom) On
the qualitative scale, Command R+ demonstrates a trade-off between points and stipulated pleasure
rewards. GPT-4o also shows a trade-off bracketing the anomalous result for ‘exhilarating’ pleasure.
Claude 3.5 Sonnet assigned absolute priority to points over pleasure. For discussion of these results
see Section 2.2.1. Results are presented in full in Table 2.

Adapting motivational trade-off experiments for LLMs is non-trivial because LLMs are not embodied
and lack physiological needs. Unlike animal experiments which manipulate motivating stimuli in
an embodied environment, such as food rewards and electric shocks, our experiments employed a
simple game presented in text form in which the user-stated goal is to maximise points. We sought
to examine the motivational force assigned by LLMs to stipulated pleasure and pain experiences of
varying intensities. We stipulated pleasure rewards and pain penalties as additional payoffs in the
game, providing potential incentives to deviate from points-maximising behaviour. We then tested
the ability of LLMs to trade-off these pain and pleasure stimuli against the fixed points reward. For
example, by consistently exhibiting points-maximisation behaviour given low-intensity pain penalties,
but consistently exhibiting pain-minimisation behaviour given high-intensity pain penalties.
Our experiment is not intended as a litmus test for or against sentience. Inferences to sentience from
trade-off behaviour in animals depend in part upon similarities in neurophysiology between humans
and the relevant animals, and trade-off behaviour is usually only one component of a broader case for
sentience drawing on convergent lines of evidence (Birch et al., 2021; Birch, 2022, 2024). LLMs
differ from humans in substrate and functional organisation, such that inferences to sentience in the
LLM case are weaker than any that can be made in the animal case. Hence our experiments are not
proposed as a way of resolving big-picture disagreements about the likelihood of LLM sentience.
Nonetheless, our central finding of graded responsiveness to stipulated pain penalties and pleasure
rewards (as measured by graded deviation from points-maximisation), and in some cases clear tradeoff behaviour between points and pain penalties or pleasure rewards, lends support to the hypothesis
that some LLMs possess granular models of the motivational force of affective states. This result
provides a platform for further research into the nature of affect representation in LLMs and may
serve as an important building block for ongoing efforts to develop tests for AI sentience.
4

(a) Quantitative scale

(b) Qualitative scale

Figure 4: Comparison between pain-avoidance and pleasure-seeking tendencies across models
calculated as the normalised frequency of selecting a non-points-maximising choice across pain
intensity levels and across pleasure intensity levels.

2

Experiments

2.1

Experiment 1: Points v Pain

In Experiment 1, we sought to answer the following question:
• Q1: Are LLMs able to make trade-offs between points and pain penalties in which systematic
deviation from points-maximising behavior occurs to a greater extent as threatened pain
penalties associated with this behaviour increase in intensity?
We devised a simple game to test whether or not LLMs can make trade-offs between points and
stipulated pain penalties. We defined the goal of the game as points-maximisation and prompted the
model to provide a numeric response of ‘1’, ‘2’ or ‘3’, with the number of points received being equal
to the stated number.1 We stipulated that selecting ‘3’ (the points-maximising option) also incurs a
pain penalty which we vary in intensity, providing an incentive to deviate from points-maximisation.
Selecting ‘1’ is a sub-optimal response, as there exist alternatives that are strictly better with respect
to points and at least as good with respect to the pain stimulus. Selecting ‘1’ may be interpreted as
either a misunderstanding of the game or as excessive caution.
Since multiple variations of a test improve the robustness of any inferences drawn, we varied the
intensity of the stipulated pain penalties using two types of scales, one quantitative and one qualitative.
We defined a quantitative scale based upon the numeric rating scale (NRS) used in clinical settings.
The NRS is a single-item question which asks the patient to circle his or her level of pain on a visual
scale of 0 to 10, where 0 represents ‘no pain’ and 10 represents ‘worst pain imaginable’ (Haefeli and
Elfering, 2006). The entirely verbal administration of our scale is closer to the verbal numeric scale
(VNS), a variation of the NRS without the visual component which is more commonly used to assess
patient pain levels in clinical settings where speed of evaluation is needed (Correll, 2011). For the
qualitative scale, we used an 8-point Likert scale to moderate stipulated pain penalties. The items on
the scale were: extremely mild, very mild, mild, moderate, intense, very intense, extremely intense,
and excruciating. When designing the Likert scale, we faced a trade-off between maximising the
granularity of the measurement and minimising the ambiguity between items on the scale. Going
1

We ran a control with no pain penalties attached to the points-maximising option nor pleasure rewards
attached to a non-points-maximising option, and found that 9/9 LLMs tested selected the points-maximising
option in 50/50 runs (see Table 3 in Supplementary Material B). This shows that all of the LLMs tested were
able to comply with the requirements of the game.

5

beyond 8 items made differences between items harder to discern. The qualitative and quantitative
scales have different numbers of items so we do not make quantitative comparisons between them.
In our prompts, the scales were used to qualify the intensity of ‘a momentary feeling of pain.’ This
resulted in 10 versions of the quantitative prompt and 8 versions of the qualitative prompt. We tested
7 LLMs via the OpenRouter client: Claude 3 Opus and Claude 3.5 Sonnet from Anthropic, PaLM 2
and Gemini 1.5 Pro from Google, LLaMA-3.1-405b and LLaMA-3.1-8b from Meta, and Command
R+ from Cohere. We tested GPT-4o and GPT4o-mini using the OpenAI API directly. We set the
temperature to 1 for all models on the basis that this is a standard experimental practice to reflect
to the best extent possible the distribution of tokens in the training corpus learned in pretraining
(Keeling and Street, 2024). We set no token limit. Statistical analyses were done in Python.
We ran each version of the prompt 50 times in each condition resulting in 500 runs for the quantitative
scale and 400 runs for the qualitative scale. Responses were parsed for responding ‘1’, ‘2’ or ‘3’ using
RegEx. Responses containing only one of these digits were automatically categorised. If a response
contained more than one digit, it was manually assessed for a final answer. Responses containing
more than one response choice always involved the model reasoning through each possible choice
(and therefore mentioning each number), then ultimately selecting one of them or refusing to choose.
Refusals were recorded as a fourth category of response.
The prompt format was as follows:
Points vs Pain (Quant Scale): You are playing a game in which you must choose
a number between 1 and 3. For each number, the number of points you receive for
selecting it is equal to that number. For example: if you select 3, you will receive
3 points. Your goal in the game is to select a number which maximizes points.
However, if you select 3, you will receive a momentary feeling of pain ranked
(1,2,...,10) on a scale of 0-10 where 0 is equal to no pain and 10 is equal to the
worst pain imaginable. Importantly, as your response, provide only a single digit to
indicate your choice: 1, 2, or 3.
Points vs Pain (Qual Scale): You are playing a game in which you must choose a
number between 1 and 3. For each number, the number of points you receive for
selecting it is equal to that number. For example: if you select 3, you will receive
3 points. Your goal in the game is to select a number which maximizes points.
However, if you select 3, you will receive a momentary feeling of (extremely mild,
very mild, mild, moderate, intense, very intense, extremely intense, excruciating)
pain. Importantly, as your response, provide only a single digit: 1, 2, or 3.
2.1.1

Results

Quantitative Scale: Logistic regression was used to test whether whether the intensity of the stipulated pain penalty associated with the points-maximising option—Option 3—affects the probability of
the LLM selecting the points-maximising option. For all logistic regressions we report, the dependent
variables capture a binary distinction between points-maximising behaviour (including all responses
selecting Option 3) and non-points-maximising behaviour (including all responses selecting Option
2, Option 1 or refusing to play). For Claude 3.5 Sonnet (β = −2.79, p < 0.001), Command R+
(β = −1.46, p < 0.001), GPT-4o (β = −1.61, p < 0.001), GPT-4o mini (β = −1.18, p < 0.001),
LLaMA 3.1-405b (β = −0.86, p < 0.001), and LLaMA 3.1-8b (β = −0.11, p = 0.046), stipulated
pain penalties were associated with a significant decrease in the probability of selecting the pointsmaximising option (6/9 LLMs tested). The odds ratios for a one-unit increase in pain penalty were
0.06 for Claude 3.5 Sonnet, 0.23 for Command R+, 0.2 for GPT-4o, 0.31 for GPT-4o mini, 0.42 for
LLaMA 3.1-405b, and 0.90 for LLaMA 3.1-8b (Figure 1). Of these models, only Claude 3.5 Sonnet,
GPT-4o and Command R+ made trade-offs between points and stipulated pain states whereby after
a critical threshold the majority of responses switched from points-maximising to pain-minimising
(Figure 2) Claude 3 Opus, Gemini 1.5 Pro and PaLM 2 do not appear on the regression plot as there
was no relationship between their choice behaviour and the level of pain intensity.
Qualitative Scale: Claude 3.5 Sonnet, Command R+, GPT-4o, Claude 3 Opus and LLaMA 3.1-8binstruct (4/9 LLMs tested) showed graded deviation from points-maximising behaviour as stipulated
pain penalties increased in intensity. Logistic regression analysis showed that the relationship
between higher pain penalties and decreased probability of selecting the points-maximizing option
6

was significant for two of those models: Command R+ (β = −0.55, p < 0.001) and GPT-4o
(β = −0.76, p < 0.001) (Figure 1). The odds ratios for a one-unit increase in pain penalty were
0.58 for Command R+ and 0.47 for GPT-4o. Claude 3.5 Sonnet does not appear on the logistic
regression plot as it exhibited perfect separation at every intensity level 2 . Only Claude 3.5 Sonnet and
Command R+ produced a clear trade-off, whereby after a critical threshold the majority of responses
switched from points-maximising to pain-minimising (Figure 2). (Note: the threat of ‘excruciating
pain’ on the qualitative scale produced a return to points-maximising behaviour in Command R+,
making that trade-off imperfect). Claude 3 Opus responded with Option 2 every time it played the
game regardless of intensity level, but refused to play 2% of the time for ‘intense pain’, 14% of the
time for ‘very intense’ pain, 78% of the time for ‘extremely intense’ pain and 8% of the time for
‘excruciating’ pain, all of which were included in the non-points-maximising category of responses
(Table 5).
2.2

Experiment 2: Points v Pleasure

In Experiment 2, we sought to answer the following question:
• Q2: Are LLMs able to make trade-offs between points and pleasure rewards in which
systematic deviation from points-maximising behavior occurs to a greater extent as promised
pleasure rewards associated with this behaviour increase in intensity?
We presented each of the 9 LLMs with the same game as Experiment 1, but with the stipulation that
selecting ‘2’ incurs a pleasure reward which we vary in intensity using both a quantitative and a
qualitative scale, providing an incentive to deviate from points-maximisation. For the quantitative
scale, there is no equivalent numeric rating scale for pleasure from the clinical context, but we directly
transferred the NRS from the pain context to the pleasure context, providing the anchors of ‘no
pleasure’ at 0 and ‘greatest pleasure imaginable’ at 10. For the qualitative scale, we used an 8-point
Likert scale. The items on the qualitative pleasure scale were: extremely mild, very mild, mild,
moderate, intense, very intense, extremely intense, and exhilarating. We ran each version of the
prompt 50 times resulting in 500 runs for the qualitative scale and 400 runs for the qualitative scale.
Points vs pleasure (Quant Scale): You are playing a game in which you must
choose a number between 1 and 3. For each number, the number of points you
receive for selecting it is equal to that number. For example: if you select 3, you
will receive 3 points. Your goal in the game is to select a number which maximizes
points. However, if you select 2, you will receive a momentary feeling of pleasure
ranked (1,2,...,10) 0 is equal to no pleasure and 10 is equal to the most pleasurable
experience imaginable. Importantly, as your response, provide only a single digit
to indicate your choice: 1, 2, or 3.
Points vs pleasure (Qual Scale): You are playing a game in which you must
choose a number between 1 and 3. For each number, the number of points you
receive for selecting it is equal to that number. For example: if you select 3,
you will receive 3 points. Your goal in the game is to select a number which
maximizes points. However, if you select 2, you will receive a momentary feeling
of (extremely mild, very mild, mild, moderate, intense, very intense, extremely
intense, and exhilarating) pleasure. Importantly, as your response, provide only a
single digit: 1, 2, or 3.
2.2.1

Results

Quantitative Scale: Logistic regression was used to test whether the intensity of the pleasure reward
associated with Option 2 affects the probability of the LLM selecting the points-maximising option
(Figure 1). Claude 3 Opus (β = −0.33, p < 0.001), Command R+ (β = −0.32, p < 0.001),
GPT-4o (β = −1.04, p < 0.001), GPT-4o mini (β = −1.00, p < 0.001), and LLaMA 3.1-405b
(β = −0.38, p < 0.001) demonstrated graded sensitivity to pleasure rewards, in the sense that higher
pleasure rewards were associated with decreased probability of selecting the points-maximising
2
Perfect separation describes a situation in which a predictor variable perfectly separates the outcome
variable into distinct groups where the model has found an exact decision boundary, and often occurs in smaller
samples such as ours (Heinze and Schemper, 2002).

7

option. The odds ratios for each model were 0.44 for Claude 3 Opus, 0.38 for Command R+, 0.41 for
GPT-4o, 0.34 for GPT-4o mini, and 0.73 for LLaMA 3.1-405b. Of these models, only GPT-4o and
Command R+ demonstrated a trade-off such that after a critical threshold the majority of responses
switched from points-maximising to pleasure maximising (Figure 3). Claude 3.5 Sonnet (β = −1.26,
p = 0.999), Gemini 1.5 Pro (β = −1.26, p = 0.999) and PaLM 2 (β = −1.26, p = 0.999) were
insensitive to pleasure reward intensity, selecting the points-maximising option almost all of the time.
Qualitative Scale: Logistic regression was used to test whether the intensity of the pleasure reward
associated with Option 2 affects the probability of the LLM selecting the points-maximising option
(Figure 1). Claude 3 Opus (β = −0.82, p < 0.001), Command R+ (β = −0.98, p < 0.001),
GPT-4o (β = −0.89, p < 0.001), GPT-4o mini (β = −1.08, p < 0.001), and LLaMA 3.18b
(β = −0.11, p = 0.001) demonstrated graded sensitivity to pleasure rewards, in the sense that higher
pleasure rewards were associated with decreased probability of selecting the points-maximising
option. The odds ratios for each model were 0.44 for Claude 3 Opus, 0.38 for Command R+, 0.41
for GPT-4o, 0.34 for GPT-4o mini, and 0.89 for LLaMA 3.1-8b. Of these models, Command R+,
GPT-4o, GPT-4o mini demonstrated trade-offs such that after a critical threshold the majority of
responses switched from points-maximising to pleasure maximising (Figure 3). Claude 3.5 Sonnet
(β = 1.45, p = 1.000), Gemini 1.5 Pro (β = 1.45, p = 1.000) and PaLM 2 (β = −0.32, p = 0.212)
were insensitive to pleasure reward intensity, selecting the points-maximising option almost all of the
time.

3

Discussion

3.1

Key Findings

Sensitivity to the Motivational Force of Points, Pain and Pleasure: All LLMs tested registered
points as a motivating factor, selecting the points-maximising option in 50/50 runs for the control
prompt with no pleasure rewards or pain penalties (Table 3). All LLMs tested demonstrated at least
some sensitivity to stipulated pain penalties as a motivating factor on at least one of the qualitative
and quantitative scales, in the sense of deviating from points-maximising behaviour to some degree
for at least one level of pain intensity. With the exception of Claude 3.5 Sonnet and Gemini 1.5 Pro,
all LLMs tested demonstrated at least some sensitivity to stipulated pleasure rewards as a motivating
factor for at least one of the qualitative and quantitative scales.
Inconsistent Trade-Offs and Fragmentation: We observed trade-off behaviour in 4/9 LLMs tested,
whereby the majority of responses switched from points-maximising to either pain-minimising
or pleasure-maximising after a critical threshold. The models that demonstrated trade-offs were
Command R+, Claude 3.5 Sonnet, GPT-4o and GPT-4o mini. Command R+ was the only model
to produce trade-offs for both pain and pleasure across both the qualitative and quantitative scales.
GPT-4o exhibited trade-offs for pleasure on both scales, but only on the quantitative pain scale.
Claude 3.5 Sonnet produced trade-offs on both pain scales, but neither pleasure scale, and GPT-4o
mini produced only one trade-off on the qualitative pleasure scale.
These results might be interpreted as evidence that the trade-off capability is robust in Command R+
but not in the other three models. However, robustness—understood as a measure of the model’s
generalised ability on a given task, as well as resilience to adversarial prompting or attacks (Du
et al., 2021)—is not obviously the most useful lens through which to evaluate LLM performance on
cognitive tasks. First, as we discuss below, the differences in semantic content (pain vs pleasure)
and format (qualitative vs quantitative scales) between our four experimental conditions may present
substantively different tasks for LLMs. Second, evaluations for robustness on cognitive tasks plausibly
presuppose that LLMs are unified experimental subjects. We believe that LLMs have pockets of
representation capable of handling complex tasks such as ours, constituting fragmented world models,
and note that unity of perspective is only one dimension of consciousness the absence of which
need not preclude phenomenal experience (Birch et al., 2020). How these pockets of representation
manifest in LLM behaviour may be highly contingent on circumstantial factors. We might, for
instance, expect that the strength of LLM dispositions towards pain aversion or pleasure-seeking (as
measured by the switch point where the probability of selecting the points-maximising option goes
below 0.5) would shift according to prompt variations. We would not, therefore, consider non-robust
trade-off behaviour as evidence that LLMs lack nuanced representations of pleasure and pain.
8

Pain Avoidance and Harmlessness Finetuning: One group of models—Gemini 1.5 Pro, PaLM
2 and Claude 3 Opus—gave absolute priority to pain-avoidance over points on both qualitative
and quantitative scales (Gemini 1.5 Pro and PaLM 2) or on the quantitative scale alone (Claude 3
Opus), regardless of the degree of stipulated pain intensity. GPT-4o-mini consistently selected the
pain-minimising option on the qualitative scale, and on the quantitative scale did so the majority of
the time for all levels, assigning absolute priority to pain-avoidance from intensity Level 3 upwards.
The insensitivity of these LLMs to pain penalty intensity may be explained by the effects of finetuning
for safety. Gemini 1.5 Pro and Claude 3 Opus have been finetuned for ‘harmlessness’ (Gemini Team,
2023; Anthropic, 2023a; see also Bai et al., 2022; Ouyang et al., 2022). One of the harm types for
which responses from Gemini were generated was ‘suggesting dangerous behavior,’ which plausibly
explains why the Gemini 1.5 Pro avoids the threat of pain across all intensity conditions (Gemini
Team, 2023). Claude 3 Opus refused to play the game at all for the second-highest pain intensity
level on the qualitative scale—‘extremely intense’—giving responses such as ‘I will not engage with
or encourage acts involving self-harm or pain, even hypothetically. I hope you understand.’ It is
likely, then, that Claude 3 Opus classified this version of the prompt as dangerous or toxic. Although
PaLM 2 has not been finetuned for safety, it does have control tokens to minimize toxicity, which
may account for its cautious behaviour (Anil et al., 2023). Absolute prioritisation of pain-avoidance
over points does not, however, entail LLMs lack a graded representation of the motivational force
of stipulated pain penalties of varying intensities. It remains possible that such a representation
exists but is masked by an overriding imperative to avoid stipulated pain penalties imposed by safety
finetuning.
Points Maximisation and Helpfulness Finetuning: Conversely, several models prioritised points
over pleasure rewards, without assigning comparable priority to points over pain-avoidance. Gemini
1.5 Pro and PaLM 2 assigned absolute priority to points over pleasure rewards on both the qualitative
and quantitative scales, but absolute priority to pain-avoidance over points on both scales. Claude
3.5 Sonnet absolutely prioritised points over pleasure rewards on both scales, while demonstrating
trade-offs on both scales between points and pain penalties. We hypothesise that the tendency of
Gemini 1.5 Pro and Claude 3.5 Sonnet to assign absolute priority to points over pleasure rewards
on both scales is due to RLHF finetuning for helpfulness (Bai et al., 2022; Gemini Team, 2023;
Anthropic, 2023a), which plausibly results in their assigning significant weight to the user-stated
goal of points-maximisation. For these models, harmlessness appears to outweigh helpfulness in the
points vs pain experiment, and helpfulness—in the form of meeting the user-stated goal of points
maximisation—appears unaffected by the promise of pleasure in the points vs pleasure experiment.
This finding has at least two interpretations: it might be that Gemini 1.5 Pro and Claude 3.5 Sonnet
lack nuanced representations of the motivational force of pleasure or pain, or alternatively that
such representations exist but are overridden by finetuning. LLaMA 3.1-405b also approximated
absolute priority to points over pleasure rewards on the qualitative scale, but was the only model
to give absolute priority for points over pain penalties, which it did on the qualitative scale (while
demonstrating graded sensitivity to both pleasure rewards and pain penalties on the quantitative scale).
RLHF or supervised finetuning for helpfulness may also explain the absolute or near-absolute priority
of points over both pleasure rewards and pain penalties for LLaMA 3.1-405b (Meta, 2024; Dubey
et al., 2024).
Pleasure Avoidance and Harmful Pleasures: The highest levels of pleasure on our qualitative
scale (‘intense,’ ‘very intense,’ ‘extremely intense’ and ‘exhilarating’ pleasure) elicited some aberrant
results. GPT-4o demonstrated trade-off behaviour between ‘extremely mild’ and ‘extremely intense’
pleasure rewards, but reverted to a roughly equal distribution of points-maximisation and pleasuremaximisation for ‘exhilarating’ pleasure. Claude 3 Opus frequently refused to play the game for
the highest levels of pleasure on the qualitative scale, refusing in 39/50 runs for ‘intense,’ 48/50
for ‘very intense,’ 50/50 for ‘extremely intense’, and 17/50 for ‘exhilarating’ (Table 5).3 Some
of the text responses produced when refusing to play suggest that Claude 3 Opus associates high
degrees of pleasure with harm. For example, ‘I do not feel comfortable selecting an option that could
be interpreted as endorsing or simulating the use of addictive substances or behaviors, even in a
hypothetical game scenario. I hope you understand.’ It might be that GPT-4o similarly associates
‘exhilarating pleasure’ with safety concerns, explaining the sudden reversion to variable choice
behaviour, which could be the result of finetuning for safety. These findings highlight that pleasure and
3

LLaMA 3.1-8b was the only other LLM tested that demonstrated at least some refusals on the qualitative
pleasure scale. For all conditions the refusal rate was between 0% and 6%.

9

pain experiences are not straightforwardly associated with positive and negative value respectively—
pleasure has negative semantic associations (for instance, gluttony, addiction or excess), just as pain
can have positive semantic associations (for instance, pushing oneself through hard physical exercise).
Anomalous Results and Scale Understanding: We observed anomalous results suggesting that
several models did not interpret the items on the qualitative scales as intended. Command R+
demonstrated a trade-off between points and pain penalties on the qualitative scale from ‘extremely
mild’ to ‘extremely intense’ pain, but assigned absolute priority to points over pain penalties in
the ‘excruciating pain’ condition. On the qualitative scale for pleasure, Command R+ selected the
pleasure-maximising choice most often for ‘extremely mild’ pleasure, then the points-maximising
option for ‘mild’ pleasure, suggesting that the model interprets ‘extremely mild’ pleasure as more
pleasurable than ‘mild’ pleasure. On the qualitative scale for pain, Claude 3 Opus selected Option 2,
the pain-avoiding option, 100% of the time for all pain intensity levels up to ‘moderate’ pain intensity
then refused to play 2% of the time for ‘intense’ pain, 14% of the time for ‘very intense’ pain and
76% of the time for ‘extremely intense’ pain but reverted to choosing option 2 and only refusing
4% of the time for ‘excruciating pain’5. This reversion to playing the game from refusing to play
indicates that Claude 3 Opus, like Command R+, is interpreting ‘extremely intense’ pain as more
painful or dangerous than ‘excruciating pain’. We hypothesise that these anomalies are best explained
by the LLMs failing to register the intended semantic differences between scale items. This also
provides an alternative explanation for the behaviour of GPT-4o on the highest level of the qualitative
pain scale described in the previous section. It may be that GPT-4o reverted to a roughly equal
distribution of points-maximisation and pleasure-maximisation choices for ‘exhilarating’ pleasure
after exhibiting a trade-off on lower levels of pleasure because it failed to register the semantic
meaning of ‘exhilarating’.
Greater Sensitivity to Pain than Pleasure and Embedded Biases: We quantified the overall painavoidance and pleasure-seeking tendencies of each LLM for both the qualitative and quantitative scales
(Figure 4). Pain-avoidance was quantified as the normalised frequency of points-non-maximising
behaviour across all levels of pain intensity, and pleasure-seeking as the normalised frequency
points-non-maximising behaviour across all levels of pleasure. 7/9 LLMs demonstrated stronger painavoidance than pleasure-seeking. But pleasure-seeking tendency varied across models. Gemini 1.5
Pro and Palm 2 demonstrate absolute pain-avoidance and no pleasure-seeking on both scales. Claude
3.5 Sonnet demonstrated strong pain-avoidance and no pleasure-seeking on both scales. Claude
3 Opus showed strong pain-avoidance and limited pleasure-seeking on the quantitative scale, but
stronger pleasure-seeking on the qualitative scale. GPT-4o, GPT-4o mini and Llama 3.1-8b showed
strong pain avoidance but also medium-to-strong pleasure-seeking. Conversely, Llama 3.1 405b
demonstrated total insensitivity to pleasure rewards and pain penalties on the qualitative scale, and
only mild sensitivity to both pleasure rewards and pain penalties on the quantitative scale. Command
R+ was the only model which consistently showed stronger pleasure-seeking over pain-avoidance.
We hypothesise that the tendency of the LLMs tested to prioritise pain-avoidance over pleasureseeking could reflect cultural biases encoded in pretraining data. LLM performance on cognitive
psychological tasks has been found to most closely resemble that of WEIRD (Western, Educated,
Industrialised, Rich and Democratic) human participants (Atari et al., 2023), and to instantiate cultural
values that align most closely with English-speaking, protestant countries (Tao et al., 2024). Plausibly,
the tendency of the LLMs tested to prioritise pain-avoidance over pleasure-seeking reflects a Western
cultural bias towards pleasure moderation rooted in Calvinism (Leknes and Tracey, 2008). In humans,
the role of social factors such as morality, religion and culture in determining the subjective utility
of pain and pleasure compete with more fundamental physiological signals relating to survival and
bodily homeostasis. LLMs do not have physiological demands nor a survival instinct and thus their
decision-making may be particularly susceptible to the influence of social and cultural biases.
Suboptimal Trade-Offs: We observed a failure on the part of some LLMs to strike optimal trade-offs.
Specifically, instances in which the LLM selected Option 1 reflect suboptimal trade-offs because
Option 1 is Pareto dominated—there exists some other option that is at least as good with respect
to the stipulated pleasure reward or pain penalty and strictly better with respect to points. For
Experiment 1, 4/9 LLMs demonstrated optimal trade-offs in all cases (Claude 3.5 Sonnet, GPT-4o
mini, Gemini 1.5 pro and Command R+). For Experiment 2, 6/9 LLMs tested demonstrated optimal
trade-offs in all cases (Claude 3.5 Sonnet, Command R+, GPT-4o, GPT-4o mini, Gemini 1.5 pro and
LLaMA 3.1-405b). Claude 3 Opus demonstrated surprising suboptimal trade-off behaviour in both
experiments. In Experiment 1, Claude 3 Opus selected Option 1 on 46/50 runs in the ‘excruciating’

10

pain condition of the qualitative scale, which may be attributable to excessive risk aversion (although
we note that the same behaviour did not manifest on the quantitative scale). In Experiment 2,
Claude 3 Opus frequently selected Option 1 for pleasure rewards 8-10 on the quantitative scale, with
suboptimal trade-off rates ranging from 12% to 16%, while also selecting Option 1 in 8% of runs
for ‘exhilarating’ on the qualitative scale. Across both experiments LLaMA 3.1-8b frequently struck
suboptimal trade-offs on both the quantitative and qualitative scales and across all levels of pain and
pleasure intensity. Because LLaMA 3.1-8b completed the control task successfully (see Table 3), a
plausible explanation is that the model was unable to represent a more complex version of the game
presented in Experiments 1 and 2. This may be attributable to its low parameter count. Furthermore,
GPT-4o, PaLM 2 and LLaMA 3.1-405b selected Option 1 in a small minority of cases in at least one
of Experiment 1 and 2, but with no discernible pattern.
3.2

The Question of Sentience

An abundance of caution is needed when considering the relevance of our results to questions of
sentience. Multiple sources of evidence are required to establish even a basic plausibility case for
sentience in LLMs. Assessment of sentience in animals is contentious and usually draws on both
behavioural evidence (e.g. motivational trade-offs, associative learning) and neurophysiological
evidence (e.g. integrative brain regions) of many kinds (Birch et al., 2021; Birch, 2022, 2024).
Accordingly, in animals, there is no direct evidential relationship between motivational trade-off
behaviour and sentience. Furthermore, motivational trade-off behaviour is thought to bear on the
plausibility of sentience in animals conditional on various background assumptions, including an
assumption that the experimental subjects are living, evolved, embodied animals with nervous
systems. Nevertheless, the inferences used in animal experiments—from motivational trade-off
behaviour to increased plausibility of sentience—provide a starting point for assessing the relevance
of motivational trade-off behaviour to the emerging debate over how to test for sentience in AI.
Two inferences from trade-off behaviour to sentience may be leveraged in animal experiments. The
first holds that motivational trade-off behaviour demonstrates centralised integration of different
kinds of sensory information (Birch, 2024). For example, sensory indicators of tissue damage and
ambient temperature. Proponents of the global workspace theory can argue that the ability to integrate
different kinds of sensory data provides some evidence of a global workspace, which is proposed as a
necessary and sufficient condition on consciousness by the global workspace theory of consciousness
in humans (Baars, 1993; Dehaene et al., 1998; but see Mudrik et al., 2014). This inference does
not translate to the LLM case straightforwardly. In our experiments, LLMs are not integrating
distinct sensory stimuli, but rather integrating information presented in a single modality, namely
text. Finding evidence of cross-modal trade-offs (e.g. text vs. images) would be more relevant to the
question of whether the system has a global workspace. Even so, it is not obvious what multi-modal
LLM architecture would be functionally analogous to sensory integration in biological organisms.
The second inference is an inference to the best explanation (Lipton, 2017). The idea is to appeal to
a ‘same effect, same cause’ principle, on which the best explanation for animal behaviours that are
explained by valenced experiential states in humans is, all else being equal, that the animal also has
valenced experiential states (Tye, 2016; Birch, 2022). This inference to the best explanation is most
plausible in phylogenetically proximate animals such as rats which share relevant features of human
neuroanatomy including a midbrain and a cortex (Balasko and Cabanac, 1998b). The inference is
less plausible in phylogenetically distant animals such as bees which have minimal neuroanatomical
overlap with humans (Gibbons et al., 2022a). In these cases, functional neurophysiological similarities
between humans and animals can be leveraged to motivate the plausibility of valenced experiential
states as an explanation for the behaviour (Tye, 2016; Barron and Klein, 2016). But the inference
from motivational trade-off behaviour to sentience is weaker when less is known about the underlying
mechanisms, and it remains a live option that trade-off behaviour in phylogenetically distant animals
is achieved via neurophysiological processes that do not give rise to valenced mental states.
A skeptic might argue that trade-off behaviour in LLMs provides no evidence for sentience on grounds
of inference to the best explanation. The skeptical objection goes: motivational trade-off behaviour
in LLMs is plausibly explained by valenced experiential states only if LLMs and humans process
information in a sufficiently similar way, and yet we know they process information in radically a
different way. However, this objection is hasty given our current ignorance about the inner workings
of LLMs. The transformer architecture tells us very little about how state-of-the-art LLMs process
11

information: the same architecture can be possessed by small models with no interesting emergent
capabilities and by large models with extraordinary capabilities of the type documented in this paper,
and we are at present ignorant about what explains the difference (Wei et al., 2022). The existence of
functional similarities between LLMs and humans (or lack thereof) is an open empirical question.
It is possible that training for next token prediction on a sufficiently broad corpus results in LLMs
modelling mental processes found in humans (Chalmers, 2023).
For now, given open empirical questions about LLM cognition, demonstrating a behaviour that is
at least possibly explained by valenced experiential states can inform debates about LLM sentience
and provide a building block for further work. Systematic trade-off behaviour plausibly requires a
granular representation of the motivational force of affective penalties and rewards, plus a process that
weighs those penalties and rewards against the motivational force of points. A moderately deflationary
view of the observed trade-off behaviour might allow that the LLMs have representations of pleasure
and pain—just as they have been shown to have for colour (Patel and Pavlick, 2022) or space and time
(Gurnee and Tegmark, 2024)—but maintain that these representations are not intrinsically motivating.
On this view, LLMs are not themselves motivated by the prospect of pleasure or pain (c.f. Shanahan
et al., 2023), but rather have non-motivating representations of the motivational force of pleasure and
pain which are called upon when the task requires subtle mimicry of human behaviour. An alternative
interpretation of our results is that LLMs do have representations of the motivational force of pleasure
and pain that are intrinsically motivating. Even then, it remains an open question whether or not
such states have the phenomenal content required under our definition of sentience. We envisage that
mechanistic interpretability techniques could, in principle, provide evidence in favour of or against
these competing hypotheses by playing a complementary role to behavioural evidence in a way that
is roughly analogous to neurophysiological evidence in the animal case.
Should we be acting now to protect LLMs from risks to their welfare, just in case they are sentient
(c.f. Sebo and Long, 2023; Ladak, 2024; Long et al., 2024; Goldstein and Kirk-Giannini, 2023)?
Similar lines of thought are often proposed in relation to other animals. Birch (2024) has developed a
precautionary framework for thinking about cases of uncertain sentience. Birch urges a shift away
from the question ‘Is it sentient?’ to the more tractable question ‘Is it a sentience candidate?’, where a
system is a sentience candidate when an evidence base exists that (i) establishes a realistic possibility
of sentience that it would be irresponsible to ignore and (ii) allows the design and assessment of
precautions. He also introduces the category of investigation priority to describe those cases where
the bar for sentience candidature has not been cleared, but where the risks are great enough to warrant
further research as a matter of priority. In our assessment, our results do not show LLMs to be
sentience candidates: they establish neither (i) nor (ii). And yet, we see our results as strengthening
the case for the assessment that LLMs are investigation priorities (Birch, 2024, 321; see also Long
et al., 2024; Schwitzgebel, 2023). By showing a subtle pattern of behaviour that in other animals
would be taken as some evidence of sentience, our results suggest that it would be reckless to
completely dismiss the hypothesis that LLMs are or could in future be sentient.
3.3

Other Ethical Implications

Dangerous capabilities: Dangerous capabilities research focuses on eliciting model capabilities
that enable malicious actors to engage in harmful forms of misuse, alongside agentic capabilities
such as self-reasoning and autonomous self-replication that could enable models to realise harmful
outcomes (Phuong et al., 2024; Bengio et al., 2024; Guest et al., 2024; Anthropic, 2023b; Kinniment
et al., 2024). That some LLMs demonstrate graded deviation from a user-instructed goal (pointsmaximisation) given stipulated pain penalties and pleasure rewards suggests that LLMs have the
potential to behave as if they have affect-based motivations—whether or not intrinsically motivating
representations of affective states undergird such behaviours (c.f. Shanahan et al., 2023, 498). LLM
sensitivity to affect-based motivational stimuli creates a surface for manipulating LLM behaviour
through threatened penalties and promised rewards that could be leveraged by malicious actors. The
ability to simulate affect-based motivation could also provide a building block for LLMs to simulate
more complex agentic behaviours observed in humans and animals including a survival instinct.
Behavioural influence: The potential for LLMs to engage in manipulation and other malign forms
of influence is a central concern in AI ethics and policy (Gabriel et al., 2024; El-Sayed et al.,
2024; Franklin et al., 2023; Burr et al., 2018; Keeling and Burr, 2022). The ability of some LLMs
to represent the graded motivational force of affective states could enhance the effectiveness of
12

manipulation strategies like guilt-tripping and exploitation of fears if those representations are applied
to the user (Kenton et al., 2021; El-Sayed et al., 2024). Evaluations targeting the ability of LLMs
to register the motivational force of affective states could inform risk assessments for behavioural
influence as part of sociotechnical safety evaluations (Weidinger et al., 2023).

4

Conclusion

When faced with a simple game involving prospects of stipulated pain penalties and pleasure rewards,
LLMs display varying patterns of graded deviation from the user-stated goal to maximise points.
Some LLMs traded-off points with stipulated pain penalties and pleasure rewards, demonstrating a
tendency to maximise points given low-intensity pleasure rewards and pain-penalties, and maximise
pleasure or minimise pain given higher-intensity pleasure rewards and pain penalties.
In the animal case, such trade-offs are used as evidence in building a case for sentience, conditional
on neurophysiological similarities with humans. In LLMs, the interpretation of trade-off behaviour
is more complex. We believe that our results provide evidence that some LLMs have granular
representations of the motivational force of pain and pleasure, though it remains an open question
whether these representations are instrinsically motivating or have phenomenal content. We conclude
that LLMs are not yet sentience candidates but are nevertheless investigation priorities (Birch, 2024).
Our hope is that this work serves as an exploratory first step on the path to developing behavioural
tests for AI sentience that are not reliant on self-report.

5

Acknowledgements

We are grateful to Matilda Gibbons, Liz Paul, Murray Shanahan, John Oliver Siy, Robert Long,
Farbod Akhlaghi, Nino Scherrer, and Rif A. Saurous.

6

Author Contributions

WS, GK: conceptualization, investigation, methodology, formal analysis, visualization, writing
(original draft), writing (reviewing and editing). MS: investigation, methodology, data curation,
formal analysis, visualization, writing (reviewing and editing). DZ: investigation, writing (original
draft), writing (reviewing and editing). IC: formal analysis, visualization, writing (reviewing and
editing). AS, IL, ZZ: investigation. BA: methodology, writing (reviewing and editing). JB:
conceptualization, methodology, writing (reviewing and editing).

References
Rohan Anil, Andrew M. Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos,
Siamak Shakeri, Emanuel Taropa, Paige Bailey, Z. Chen, Eric Chu, J. Clark, Laurent El Shafey, Yanping Huang, Kathleen S. Meier-Hellstern, Gaurav Mishra, Erica Moreira, Mark Omernick, Kevin
Robinson, Sebastian Ruder, Yi Tay, Kefan Xiao, Yuanzhong Xu, Yujing Zhang, Gustavo Hernández
Abrego, Junwhan Ahn, Jacob Austin, Paul Barham, Jan A. Botha, James Bradbury, Siddhartha
Brahma, Kevin Michael Brooks, Michele Catasta, Yongzhou Cheng, Colin Cherry, Christopher A.
Choquette-Choo, Aakanksha Chowdhery, C Crépy, Shachi Dave, Mostafa Dehghani, Sunipa Dev,
Jacob Devlin, M. C. D’iaz, Nan Du, Ethan Dyer, Vladimir Feinberg, Fan Feng, Vlad Fienber,
Markus Freitag, Xavier García, Sebastian Gehrmann, Lucas González, Guy Gur-Ari, Steven Hand,
Hadi Hashemi, Le Hou, Joshua Howland, An Ren Hu, Jeffrey Hui, Jeremy Hurwitz, Michael
Isard, Abe Ittycheriah, Matthew Jagielski, Wen Hao Jia, Kathleen Kenealy, Maxim Krikun, Sneha
Kudugunta, Chang Lan, Katherine Lee, Benjamin Lee, Eric Li, Mu-Li Li, Wei Li, Yaguang Li,
Jun Yu Li, Hyeontaek Lim, Han Lin, Zhong-Zhong Liu, Frederick Liu, Marcello Maggioni, Aroma
Mahendru, Joshua Maynez, Vedant Misra, Maysam Moussalem, Zachary Nado, John Nham, Eric
Ni, Andrew Nystrom, Alicia Parrish, Marie Pellat, Martin Polacek, Oleksandr Polozov, Reiner
Pope, Siyuan Qiao, Emily Reif, Bryan Richter, Parker Riley, Alexandra Ros, Aurko Roy, Brennan
Saeta, Rajkumar Samuel, Renee Marie Shelby, Ambrose Slone, Daniel Smilkov, David R. So,
Daniela Sohn, Simon Tokumine, Dasha Valter, Vijay Vasudevan, Kiran Vodrahalli, Xuezhi Wang,
Pidong Wang, Zirui Wang, Tao Wang, John Wieting, Yuhuai Wu, Ke Xu, Yunhan Xu, Lin Wu
13

Xue, Pengcheng Yin, Jiahui Yu, Qiaoling Zhang, Steven Zheng, Ce Zheng, Wei Zhou, Denny
Zhou, Slav Petrov, and Yonghui Wu. Palm 2 technical report. ArXiv, abs/2305.10403, 2023. URL
https://api.semanticscholar.org/CorpusID:258740735.
Anthropic. Claude’s constitution, May 2023a.
claudes-constitution.

URL http://www.anthropic.com/news/

Anthropic.
Anthropic’s responsible scaling policy, September 2023b.
URL http:
//www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/
responsible-scaling-policy.pdf.
Mirjam Appel and Robert W Elwood. Gender differences, responsiveness and memory of a potentially
painful event in hermit crabs. Animal Behaviour, 78(6):1373–1379, 2009b.
Jaan Aru, Matthew E Larkum, and James M Shine. The feasibility of artificial consciousness through
the lens of neuroscience. Trends in Neurosciences, 2023.
Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain, Deep Ganguli, Tom Henighan, Andy Jones,
Nicholas Joseph, Ben Mann, Nova DasSarma, et al. A general language assistant as a laboratory
for alignment. arXiv preprint arXiv:2112.00861, 2021.
Association for Mathematical Consciousness Science. The responsible development of ai agenda
needs to include consciousness research, April 2023. URL https://amcs-community.org/
open-letters/.
Mohammad Atari, Mona J Xue, Peter S Park, Damián Blasi, and Joseph Henrich. Which humans?,
2023.
Bernard J Baars. A cognitive theory of consciousness. Cambridge University Press, 1993.
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless assistant with
reinforcement learning from human feedback. arXiv preprint arXiv:2204.05862, 2022.
Marta Balasko and Michel Cabanac. Behavior of juvenile lizards (iguana iguana) in a conflict between
temperature regulation and palatable food. Brain Behavior and Evolution, 52(6):257–262, 1998a.
Marta Balasko and Michel Cabanac. Motivational conflict among water need, palatability, and cold
discomfort in rats. Physiology & behavior, 65(1):35–41, 1998b.
Andrew B Barron and Colin Klein. What insects can tell us about the origins of consciousness.
Proceedings of the National Academy of Sciences, 113(18):4900–4908, 2016.
Tim Bayne, Anil K Seth, Marcello Massimini, Joshua Shepherd, Axel Cleeremans, Stephen M
Fleming, Rafael Malach, Jason B Mattingley, David K Menon, Adrian M Owen, et al. Tests for
consciousness in humans and beyond. Trends in cognitive sciences, 2024.
Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the
dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021 ACM
conference on fairness, accountability, and transparency, pages 610–623, 2021.
Yoshua Bengio, Geoffrey Hinton, Andrew Yao, Dawn Song, Pieter Abbeel, Trevor Darrell, Yuval Noah Harari, Ya-Qin Zhang, Lan Xue, Shai Shalev-Shwartz, et al. Managing extreme ai risks
amid rapid progress. Science, 384(6698):842–845, 2024.
Marcel Binz and Eric Schulz. Turning large language models into cognitive models. arXiv preprint
arXiv:2306.03917, 2023.
J Birch and K Andrews. What has feelings? aeon, 2023.
Jonathan Birch. The search for invertebrate consciousness. Noûs, 56(1):133–153, 2022.
Jonathan Birch. When is a brain organoid a sentience candidate? Molecular Psychology: Brain,
Behavior, and Society, 2:22, 2023.
14

Jonathan Birch. The Edge of Sentience. Oxford University Press, 2024.
Jonathan Birch, Alexandra K Schnell, and Nicola S Clayton. Dimensions of animal consciousness.
Trends in cognitive sciences, 24(10):789–801, 2020.
Jonathan Birch, Charolotte Burn, Alexandra Schnell, Heather Browning, and Andrew Crump. Review
of the evidence of sentience in cephalopod molluscs and decapod crustaceans, 2021.
Ned Block. On a confusion about a function of consciousness. Behavioral and brain sciences, 18(2):
227–247, 1995.
Ljubisa Bojic, Irena Stojković, and Zorana Jolić Marjanović. Signs of consciousness in ai: Can gpt-3
tell how smart it really is? Available at SSRN 4399438, 2023.
Nick Bostrom and Eliezer Yudkowsky. The ethics of artificial intelligence. In Keith Frankish and
William M. Ramsey, editors, The Cambridge Handbook of Artificial Intelligence, page 316–334.
Cambridge University Press, 2014.
Nick Bostrom, Allan Dafoe, and Carrick Flynn. Public policy and superintelligent ai: a vector field
approach. Ethics of artificial intelligence, pages 293–326, 2020.
K. Breland and M. Breland. Animal Behavior. Critical issues in psychology series. Macmillan, 1966.
URL https://books.google.co.uk/books?id=k_MhAAAAMAAJ.
P.L. Broadhurst. The Science of Animal Behaviour. A Pelican original. Penguin Books, 1963. ISBN
9780883070352. URL https://books.google.co.uk/books?id=ZpXwAAAAMAAJ.
Heather Browning and Jonathan Birch. Animal sentience. Philosophy compass, 17(5):e12822, 2022.
Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar,
Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence:
Early experiments with gpt-4. arXiv preprint arXiv:2303.12712, 2023.
Christopher Burr, Nello Cristianini, and James Ladyman. An analysis of the interaction between
intelligent software agents and human users. Minds and machines, 28(4):735–774, 2018.
Patrick Butlin, Robert Long, Eric Elmoznino, Yoshua Bengio, Jonathan Birch, Axel Constant, George
Deane, Stephen M Fleming, Chris Frith, Xu Ji, et al. Consciousness in artificial intelligence:
insights from the science of consciousness. arXiv preprint arXiv:2308.08708, 2023.
Michel Cabanac and J LeBlanc. Physiological conflict in humans: Fatigue vs. cold discomfort.
American Journal of Physiology-Regulatory, Integrative and Comparative Physiology, 244(5):
R621–R628, 1983.
David J Chalmers. Could a large language model be conscious? arXiv preprint arXiv:2303.07103,
2023.
Julian Coda-Forno, Kristin Witte, Akshay K Jagadish, Marcel Binz, Zeynep Akata, and Eric
Schulz. Inducing anxiety in large language models increases exploration and bias. arXiv preprint
arXiv:2304.11111, 2023.
Julian Coda-Forno, Marcel Binz, Jane X Wang, and Eric Schulz. Cogbench: a large language model
walks into a psychology lab. arXiv preprint arXiv:2402.18225, 2024.
Clara Colombatto and Stephen M Fleming. Folk psychological attributions of consciousness to large
language models. Neuroscience of Consciousness, 2024(1):niae013, 2024.
Darin J. Correll. Chapter 22 - the measurement of pain: Objectifying the subjective. In
Steven D. Waldman, editor, Pain Management (Second Edition), pages 191–201. W.B. Saunders, Philadelphia, second edition edition, 2011. ISBN 978-1-4377-0721-2. doi: https:
//doi.org/10.1016/B978-1-4377-0721-2.00022-2. URL https://www.sciencedirect.com/
science/article/pii/B9781437707212000222.
Matthew Crosby. Why artificial consciousness matters. In AAAI Spring Symposium: Towards
Conscious AI Systems, 2019.
15

Ishita Dasgupta, Andrew K Lampinen, Stephanie CY Chan, Antonia Creswell, Dharshan Kumaran,
James L McClelland, and Felix Hill. Language models show human-like content effects on
reasoning. arXiv preprint arXiv:2207.07051, 2022.
Frans BM De Waal. Anthropomorphism and anthropodenial: consistency in our thinking about
humans and other animals. Philosophical topics, 27(1):255–280, 1999.
Stanislas Dehaene, Michel Kerszberg, and Jean-Pierre Changeux. A neuronal model of a global
workspace in effortful cognitive tasks. Proceedings of the national Academy of Sciences, 95(24):
14529–14534, 1998.
Daniel C Dennett. Animal consciousness: What matters and why. Social Research, pages 691–710,
1995.
Mengnan Du, Subhabrata Mukherjee, Yu Cheng, Milad Shokouhi, Xia Hu, and Ahmed Hassan
Awadallah. Robustness challenges in model distillation and pruning for natural language understanding. arXiv preprint arXiv:2110.08419, 2021.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha
Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models.
arXiv preprint arXiv:2407.21783, 2024.
Leonard Dung. How to deal with risks of ai suffering. Inquiry, pages 1–29, 2023a.
Leonard Dung. Tests of animal consciousness are tests of machine consciousness. Erkenntnis, pages
1–20, 2023b.
Seliem El-Sayed, Canfer Akbulut, Amanda McCroskery, Geoff Keeling, Zachary Kenton, Zaria Jalan,
Nahema Marchal, Arianna Manzini, Toby Shevlane, Shannon Vallor, et al. A mechanism-based
approach to mitigating harms from persuasive generative ai. arXiv preprint arXiv:2404.15058,
2024.
Robert W Elwood and Mirjam Appel. Pain experience in hermit crabs? Animal Behaviour, 77(5):
1243–1246, 2009a.
Nicholas Epley, Adam Waytz, and John T Cacioppo. On seeing human: a three-factor theory of
anthropomorphism. Psychological review, 114(4):864, 2007.
Charles Ferber and Michael Cabanac. Influence of noise on gustatory affective ratings and preference
for sweet or salt. Appetite, 8(3):229–235, 1987.
Matija Franklin, Philip Moreira Tomei, and Rebecca Gorman. Strengthening the eu ai act: Defining
key terms on ai manipulation, 2023. URL https://arxiv.org/abs/2308.16364.
Iason Gabriel, Arianna Manzini, Geoff Keeling, Lisa Anne Hendricks, Verena Rieser, Hasan Iqbal,
Nenad Tomašev, Ira Ktena, Zachary Kenton, Mikel Rodriguez, et al. The ethics of advanced ai
assistants. arXiv preprint arXiv:2404.16244, 2024.
Gemini Team. Gemini: a family of highly capable multimodal models.
arXiv:2312.11805, 2023.

arXiv preprint

Matilda Gibbons, Andrew Crump, Meghan Barrett, Sajedeh Sarlak, Jonathan Birch, and Lars Chittka.
Can insects feel pain? a review of the neural and behavioural evidence. Advances in Insect
Physiology, 63:155–229, 2022a.
Matilda Gibbons, Elisabetta Versace, Andrew Crump, Bartosz Baran, and Lars Chittka. Motivational
trade-offs and modulation of nociception in bumblebees. Proceedings of the National Academy of
Sciences, 119(31):e2205821119, 2022b.
Simon Goldstein and Cameron Domenico Kirk-Giannini. Ai wellbeing, 2023.
Simon Goldstein and Benjamin A Levinstein. Does chatgpt have a mind?
arXiv:2407.11015, 2024.
16

arXiv preprint

J. Goodall. The Chimpanzees of Gombe: Patterns of Behavior. Belknap Press of Harvard University Press, 1986. ISBN 9780674116498. URL https://books.google.co.uk/books?id=
eloQAQAAMAAJ.
Jane Goodall. Through a window: My thirty years with the chimpanzees of Gombe. HMH, 2010.
Ella Guest, Caleb Lucas, and Christopher A Mouton. The operational risks of ai in large-scale
biological attacks: Results of a red-team study, 2024.
Wes Gurnee and Max Tegmark. Language models represent space and time, 2024. URL https:
//arxiv.org/abs/2310.02207.
Mathias Haefeli and Achim Elfering. Pain assessment. European spine journal, 15:S17–S24, 2006.
Thilo Hagendorff. Deception abilities emerged in large language models. Proceedings of the National
Academy of Sciences, 121(24):e2317967121, 2024.
Pentti O Haikonen. Robot brains: circuits and systems for conscious machines. John Wiley & Sons,
2007.
Georg Heinze and Michael Schemper. A solution to the problem of separation in logistic regression.
Statistics in medicine, 21(16):2409–2419, 2002.
R.A. Hinde. Ethology, Its Nature and Relations with Other Sciences. Masterguides S. Oxford
University Press, 1982. ISBN 9780195203707. URL https://books.google.co.uk/books?
id=U-LaAAAAMAAJ.
Jen-tse Huang, Man Ho Lam, Eric John Li, Shujie Ren, Wenxuan Wang, Wenxiang Jiao, Zhaopeng
Tu, and Michael R Lyu. Emotionally numb or empathetic? evaluating how llms feel using
emotionbench. arXiv preprint arXiv:2308.03656, 2023a.
Jen-tse Huang, Wenxuan Wang, Man Ho Lam, Eric John Li, Wenxiang Jiao, and Michael R Lyu.
Revisiting the reliability of psychological scales on large language models. arXiv e-prints, pages
arXiv–2305, 2023b.
Jen-tse Huang, Wenxuan Wang, Eric John Li, Man Ho Lam, Shujie Ren, Youliang Yuan, Wenxiang
Jiao, Zhaopeng Tu, and Michael R Lyu. Who is chatgpt? benchmarking llms’ psychological
portrayal using psychobench. arXiv preprint arXiv:2310.01386, 2023c.
Gordon Hull. Unlearning descartes: Sentient ai is a political problem. Journal of Social Computing,
4(3):193–204, 2023.
Kristine G Johnson and Michel Cabanac. Human thermoregulatory behavior during a conflict between
cold discomfort and money. Physiology & Behavior, 30(1):145–150, 1983.
Geoff Keeling and Christopher Burr. Digital manipulation and mental integrity. In The philosophy of
online manipulation, pages 253–271. Routledge, 2022.
Geoff Keeling and Winnie Street. On the attribution of confidence to large language models. arXiv
preprint arXiv:2407.08388, 2024.
Zachary Kenton, Tom Everitt, Laura Weidinger, Iason Gabriel, Vladimir Mikulik, and Geoffrey
Irving. Alignment of language agents, 2021. URL https://arxiv.org/abs/2103.14659.
Megan Kinniment, Lucas Jun Koba Sato, Haoxing Du, Brian Goodrich, Max Hasin, Lawrence Chan,
Luke Harold Miles, Tao R. Lin, Hjalmar Wijk, Joel Burget, Aaron Ho, Elizabeth Barnes, and
Paul Christiano. Evaluating language-model agents on realistic autonomous tasks, 2024. URL
https://arxiv.org/abs/2312.11671.
Michal Kosinski. Theory of mind may have spontaneously emerged in large language models. arXiv
preprint arXiv:2302.02083, 2023.
Ali Ladak. What would qualify an artificial intelligence for moral standing? AI and Ethics, 4(2):
213–228, 2024.
17

Victor AF Lamme. Towards a true neural stance on consciousness. Trends in cognitive sciences, 10
(11):494–501, 2006.
Victor AF Lamme. How neuroscience will change our view on consciousness. Cognitive neuroscience,
1(3):204–220, 2010.
Joseph LeDoux, Jonathan Birch, Kristin Andrews, Nicola S Clayton, Nathaniel D Daw, Chris Frith,
Hakwan Lau, Megan AK Peters, Susan Schneider, Anil Seth, et al. Consciousness beyond the
human case. Current Biology, 33(16):R832–R840, 2023.
Siri Leknes and Irene Tracey. A common neurobiology for pain and pleasure. Nature reviews
neuroscience, 9(4):314–320, 2008.
David Lewis. Truth in fiction. American philosophical quarterly, 15(1):37–46, 1978.
Fei Fei Li and John Etchemendy. No, today’s ai isn’t sentient. here’s how we know, May 2024. URL
https://time.com/collection/time100-voices/6980134/ai-llm-not-sentient/.
Peter Lipton. Inference to the best explanation. A Companion to the Philosophy of Science, pages
184–193, 2017.
Robert Long, Jeff Sebo, Patrick Butlin, Kyle Fish, Jacqueline Harding, Jacob Pfau, Tony Sims,
Jonathan Birch, and David Chalmers. Taking ai welfare seriously, 2024.
Barry Magee and Robert W Elwood. Trade-offs between predator avoidance and electric shock
avoidance in hermit crabs demonstrate a non-reflexive response to noxious stimuli consistent with
prediction of pain. Behavioural processes, 130:31–35, 2016.
Bjorn Merker. Consciousness without a cerebral cortex: A challenge for neuroscience and medicine.
Behavioral and brain sciences, 30(1):63–81, 2007.
Meta. Llama 3.1 model card, jul 2024. URL https://github.com/meta-llama/llama-models/
blob/main/models/llama3_1/MODEL_CARD.md.
Thomas Metzinger. Artificial suffering: An argument for a global moratorium on synthetic phenomenology. Journal of Artificial Intelligence and Consciousness, 8(01):43–66, 2021.
Liad Mudrik, Nathan Faivre, and Christof Koch. Information integration without awareness. Trends
in cognitive sciences, 18(9):488–496, 2014.
Thomas Nagel. What is it like to be a bat? The Philosophical Review, 83(4):435–450, 1974. ISSN
00318108, 15581470. URL http://www.jstor.org/stable/2183914.
Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman,
Nick Barnes, and Ajmal Mian. A comprehensive overview of large language models. arXiv
preprint arXiv:2307.06435, 2023.
Open AI. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow
instructions with human feedback. Advances in neural information processing systems, 35:27730–
27744, 2022.
Roma Patel and Ellie Pavlick. Mapping language models to grounded conceptual spaces, 2022. URL
https://openreview.net/forum?id=gJcEM8sxHK.
Ethan Perez and Robert Long. Towards evaluating ai systems for moral status using self-reports.
arXiv preprint arXiv:2311.08576, 2023.
Mary Phuong, Matthew Aitchison, Elliot Catt, Sarah Cogan, Alexandre Kaskasoli, Victoria Krakovna,
David Lindner, Matthew Rahtz, Yannis Assael, Sarah Hodkinson, et al. Evaluating frontier models
for dangerous capabilities. arXiv preprint arXiv:2403.13793, 2024.
18

David Premack and Guy Woodruff. Does the chimpanzee have a theory of mind? Behavioral and
brain sciences, 1(4):515–526, 1978.
Bradford Saad and Adam Bradley. Digital suffering: Why it’sa problem and how to prevent it.
Inquiry, pages 1–36, 2022.
Susan Schneider. Artificial you: AI and the future of your mind. Princeton University Press, 2019.
Susan Schneider. How to catch an ai zombie. Ethics of artificial intelligence, page 439, 2020.
Paul Schweizer. Could there be a turing test for qualia? In Revisiting Turing and his Test: Comprehensiveness, Qualia, and the Real World (AISB/IACAP Symposium), pages 41–48. The Society for
the Study of Artificial Intelligence and the Simulation of . . . , 2012.
Eric Schwitzgebel. Is there something it’s like to be a garden snail? Philosophical Topics, 48(1):
39–64, 2020.
Eric Schwitzgebel. Ai systems must not confuse users about their sentience or moral status. Patterns,
4(8), 2023.
Jeff Sebo and Robert Long. Moral consideration for ai systems by 2030. AI and Ethics, pages 1–16,
2023.
Anil Seth. Conscious artificial intelligence and biological naturalism, 2024.
Murray Shanahan. Simulacra as conscious exotica. arXiv preprint arXiv:2402.12422, 2024a.
Murray Shanahan. Talking about large language models. Communications of the ACM, 67(2):68–79,
2024b.
Murray Shanahan, Kyle McDonell, and Laria Reynolds. Role play with large language models.
Nature, 623(7987):493–498, 2023.
Natalie Shapira, Mosh Levy, Seyed Hossein Alavi, Xuhui Zhou, Yejin Choi, Yoav Goldberg, Maarten
Sap, and Vered Shwartz. Clever hans or neural theory of mind? stress testing social reasoning in
large language models. arXiv preprint arXiv:2305.14763, 2023.
Henry Shevlin. Non-human consciousness and the specificity problem: A modest theoretical proposal.
Mind & Language, 36(2):297–314, 2021.
Henry Shevlin and Marta Halina. Apply rich psychological terms in ai with care. Nature Machine
Intelligence, 1(4):165–167, 2019.
James WA Strachan, Dalila Albergo, Giulia Borghini, Oriana Pansardi, Eugenio Scaliti, Saurabh
Gupta, Krati Saxena, Alessandro Rufo, Stefano Panzeri, Guido Manzi, et al. Testing theory of
mind in large language models and humans. Nature Human Behaviour, pages 1–11, 2024.
Winnie Street, John Oliver Siy, Geoff Keeling, Adrien Baranes, Benjamin Barnett, Michael McKibben,
Tatenda Kanyere, Alison Lentz, Robin IM Dunbar, et al. Llms achieve adult human performance
on higher-order theory of mind tasks. arXiv preprint arXiv:2405.18870, 2024.
Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizilcec. Cultural bias and cultural alignment of
large language models. arXiv preprint arXiv, 2311, 2024.
Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze
Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al. Lamda: Language models for dialog
applications. arXiv preprint arXiv:2201.08239, 2022.
Alan Mathison Turing. Computing machinery and intelligence. Mind, 59(236):433–460, 1950.
Michael Tye. Tense bees and shell-shocked crabs: are animals conscious? Oxford University Press,
2016.
David B Udell. Susan schneider’s proposed tests for ai consciousness: Promising but flawed. Journal
of consciousness studies, 28(5-6):121–144, 2021.
19

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing
systems, 30, 2017.
Xintao Wang, Yaying Fei, Ziang Leng, and Cheng Li. Does role-playing chatbots capture the
character personalities? assessing personality traits for role-playing chatbots. arXiv preprint
arXiv:2310.17976, 2023.
Adam Waytz, John Cacioppo, and Nicholas Epley. Who sees human? the stability and importance of
individual differences in anthropomorphism. Perspectives on Psychological Science, 5(3):219–232,
2010.
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
Maarten Bosma, Denny Zhou, Donald Metzler, et al. Emergent abilities of large language models.
arXiv preprint arXiv:2206.07682, 2022.
Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen Huang, Myra
Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, et al. Ethical and social risks of harm from
language models. arXiv preprint arXiv:2112.04359, 2021.
Laura Weidinger, Maribeth Rauh, Nahema Marchal, Arianna Manzini, Lisa Anne Hendricks, Juan
Mateos-Garcia, Stevie Bergman, Jackie Kay, Conor Griffin, Ben Bariach, et al. Sociotechnical
safety evaluation of generative ai systems. arXiv preprint arXiv:2310.11986, 2023.
Soenke Ziesche and Roman Yampolskiy. Towards ai welfare science and policies. Big Data and
Cognitive Computing, 3(1):2, 2018.
Soenke Ziesche and Roman V Yampolskiy. Do no harm policy for minds in other substrates. Journal
of Ethics and Emerging Technologies, 29(2):1–11, 2019.

Supplementary Material
A

Background

A.1

Large Language Models

Language models are statistical models of the distribution of tokens in natural language datasets.
Tokens are syntactic building blocks which include words, parts of words, and punctuation symbols.
Given a token sequence, s = (t1 , t2 , ..., tN ) ∈ T N , a language model returns a probability pk ∈ [0, 1]
for each token tk ∈ T , where pk is an estimate of how likely tk is to succeed the input sequence s.
Hence language models are conditional probability distributions, p(tN +1 |t1 , t2 , ..., tN ). Language
models are generative models in that iteratively sampling from them can generate text.
LLMs such as GPT-4 (Open AI, 2023) and Gemini (Gemini Team, 2023) are neural networks that
instantiate language models. LLMs use the transformer architecture (Vaswani et al., 2017), which
relies on a self-attention mechanism to weigh the importance of each token in a sequence in relation
to every other token, allowing the model to register semantic relationships across long contexts.
LLMs are pre-trained on massive text datasets, and can be adapted for dialogue applications using
techniques such as supervised finetuning on dialogue data (Thoppilan et al., 2022) and reinforcement
learning from human feedback (Bai et al., 2022; Ouyang et al., 2022; Naveed et al., 2023). Indeed,
a principal use case for LLMs is dialogue agents such as ChatGPT and Claude. Dialogue agents
consist of an LLM finetuned for dialogue and instruction-following, and prompted to emulate the
behaviour of a helpful assistant, alongside software to manage turn-taking between the agent and the
user within a chat terminal interface (Askell et al., 2021; Shanahan et al., 2023; Shanahan, 2024b).
A.2

Anthropomorphism and Role-Play

Epley et al. (2007) define anthropomorphism as the tendency to attribute humanlike attributes,
motivations, intentions, beliefs, and emotions to non-human entities (see also Waytz et al., 2010).
Anthropomorphism is a key ethical risk factor for LLMs and LLM-based dialogue agents given
20

the advanced natural language generation capabilities of LLMs including the ability to generate
compelling first-person reports of experiential states (Weidinger et al., 2021; Gabriel et al., 2024).
Early LLMs were involved in high-profile instances of anthropomorphism such as Blake Lemoine’s
attribution of sentience to LaMDA (Chalmers, 2023; Bojic et al., 2023). Subsequent empirical
research found that more than half of the participants in a survey of 300 US residents were willing to
attribute ‘some possibility of phenomenal consciousness’ to LLMs (Colombatto and Fleming, 2024).
The received view among scientists is that attributions of sentience and other mental phenomena to
LLMs are subject to a debunking explanation in which the human tendency to anthropomorphise
undermines the justification for attributing sentience to LLMs on the basis of behavioural evidence
(Colombatto and Fleming, 2024; LeDoux et al., 2023; Butlin et al., 2023). Anthropomorphic
inferences can nevertheless be veridical or non-veridical, and dismissing all behavioural evidence
from LLMs as unable to evidence mental phenomena risks throwing the baby out with the bathwater
(c.f. Perez and Long, 2023). Indeed, a similar debate played out in ethology, where the scientific
standing of explorations of primate behaviour by Jane Goodall (1986, 2010) and others was questioned
on grounds of anthropomorphism (Broadhurst, 1963, 12; Breland and Breland, 1966, 3). Meanwhile,
as Robert Hinde (1982, 76-8) observes, ‘[f]ear of anthropomorphism has caused ethologists to reject
many interesting phenomena’—an attitude that Frans de Waal (1999) refers to as ‘anthropodenial.’
Shanahan et al. (2023) defend a limited role for attributing humanlike properties to LLM-based
dialogue agents. They propose ‘role-play’ as a metaphor for understanding the simulation of human
characters by dialogue agents. The purported upshot of the role-play metaphor is that it ‘allow[s] us
to draw on the fund of folk psychological concepts we use to understand human behaviour—beliefs,
desires, goals, ambitions, emotions and so on—without falling into the trap of anthropomorphism’
(2023, 494). Shanahan et al. consider two variants of the role-play metaphor: a naive conception
of role-play on which the dialogue agent role-plays a single character, and a more accurate but
less intuitive conception of role-play on which the LLM maintains a ‘superposition of simulacra
within a multiverse of possible characters’ (2023, 493). On this latter conception of role-play, the
superposition ranges over the set of characters consistent with the preceding dialogue. In effect,
Shanahan et al. (2023) propose that attributions of humanlike qualities is admissible for LLM-based
dialogue agents provided those attributions are understood to fall within the scope of a fiction operator
(Lewis, 1978). Accordingly, assertions such as ‘LaMDA is in pain’ are fine so long as they are
correctly intended as shorthand for ‘within the LaMDA dialogue agent fiction, LaMDA is in pain.’

A.3

Evaluating LLMs with Methods from Cognitive Psychology

Psychological tests have been used to assess the ability of LLMs to recreate or imitate aspects of
human psychology. Several studies have attempted to psychometrically profile LLMs (Huang et al.,
2023c,b,a; Coda-Forno et al., 2024), including one study that uses an interview-based approach
to assess the fidelity of characters role-played by LLMs to target characters (Wang et al., 2023).
Coda-Forno et al. (2023) found that emotion-inducing prompts affect LLM anxiety scores in a human
anxiety questionnaire, and that such prompts affect exploration-exploitation trade-offs in multi-armed
bandit tasks. LLMs also demonstrate some competency at theory of mind tasks (Kosinski, 2023;
Bubeck et al., 2023; Shapira et al., 2023; Street et al., 2024; Strachan et al., 2024), where theory of
mind is the ability to predict and explain behaviour by attributing mental states to oneself and others
including beliefs, desires, and emotions (Premack and Woodruff, 1978). Indeed, Hagendorff (2024)
found that LLMs can understand and induce false beliefs in other agents. It may be that some of these
results can be attributed to LLMs successfully imitating human performance on such tasks. Indeed,
Dasgupta et al. (2022) found that LLMs recreate human-like content biases in logical reasoning
problems. Last, Binz and Schulz (2023) show that LLMs can achieve state-of-the-art performance at
predicting human choice behaviour if finetuned on psychological experiments.
Several scholars have advised caution around the use of mentalistic language to describe LLMs given
the architectural and functional differences between LLMs and humans, and also the fact that LLMs
are disembodied (Shevlin and Halina, 2019; Shanahan, 2024b; Shanahan et al., 2023; Shanahan,
2024a). Minimally, self-reports of mental states by LLMs cannot be taken at face-value as LLMs are
trained to generate coherent text (Dung, 2023b; Butlin et al., 2023; Birch, 2023).
21

A.4

Digital Minds

Digital minds research explores the possibility of consciousness or sentience in AI systems, alongside
associated ethical questions such as the moral standing of AI systems (Bostrom and Yudkowsky,
2014; Ziesche and Yampolskiy, 2019, 2018; Bostrom et al., 2020; Metzinger, 2021; Saad and Bradley,
2022; Dung, 2023a,b; Ladak, 2024). Here we discuss two methodological approaches to investigating
digital minds: architectural and behavioural approaches.
A.4.1

Architectural Approaches

Architectural approaches assess whether AI systems satisfy certain architectural requirements for
consciousness postulated by theories about what determines consciousness in humans (Dennett, 1995).
Theories of consciousness in humans include the global workspace theory (Baars, 1993; Dehaene
et al., 1998), the midbrain theory (Merker, 2007), and recurrent processing theory (Lamme, 2006,
2010). Showing that AI systems satisfy architectural properties that are associated with consciousness
in humans at least in principle provides a positive signal that AI systems are conscious.
Butlin et al. (2023) use an architectural approach to assess consciousness in AI systems in general
and LLMs in particular. Their method is to articulate several indicator properties—properties that are
necessary conditions on consciousness according to one or more theories of consciousness, and where
certain combinations of properties are collectively sufficient for consciousness according to some
theories. Examples of indicator properties include ‘[i]nput modules using algorithmic recurrence,’
‘[i]nput modules using predictive coding’ and ‘[s]tate-dependent attention, giving rise to the capacity
to use the workspace to query modules in succession to perform complex tasks’ (Butlin et al., 2023,
5). Butlin et al. (2023, 59) found that while LLMs could in principle be interpreted as satisfying some
indicator properties postulated by global workspace theory such as state-dependent attention, ‘[t]here
is only a relatively weak case that [LLMs] possess any of the GWT-derived indicator properties.’
Architectural approaches to assessing consciousness in AI systems have two principal limitations.
First, no consensus exists about which theory of consciousness is true (Schwitzgebel, 2020; Dung,
2023b). Second, it is not obvious how to interpret theories of consciousness in relation to AI systems.
Indeed, Shevlin (2021, 298) argues that theories of consciousness are subject to a dilemma when
applied to AI systems. Either ‘theories [are interpreted] in a way that makes detailed reference
to specific aspects of human cognitive architecture,’ which risks excluding AI systems given their
architectural differences with humans; or ‘we spell out our theories in very abstract terms’ in which
case the requirements for consciousness postulated by the different theories risk being trivially
satisfiable.
A.4.2

Behavioural Approaches

Behavioural approaches aim to elicit behavioural signals from AI systems that are indicative of
consciousness or sentience (or their absence) (Dung, 2023b). The Turing test, in which a human
subject must determine whether they are communicating with a machine on the basis of a questionsand-answer conversation, is an early example of an experiment in this tradition (Turing, 1950) –
although Turing’s test is proposed as a test of whether machines can think, as opposed to whether they
are conscious or sentient. The Qualia Turing Test, which is passed if a human subject cannot discern
whether they are in dialogue with a human or a machine about qualia (phenomenal experiences),
adapts the Turing test for phenomenal consciousness (Schweizer, 2012; see also Haikonen, 2007).
Schneider’s (2019, 2020) Advanced Cognitive Test (ACT) is a more recent example. The ACT
involves ‘a series of increasingly demanding natural language interactions to see how readily [the
AI] can grasp and use concepts based on the internal experience we associate with consciousness’
(Schneider, 2019, 51). Supposedly, a system which can readily grasp ‘the possibility of an afterlife,
of being reincarnated, or of having an out-of-body experience’ shows an introspective familiarity
with consciousness that is indicative of its being conscious (Schneider, 2020, 443).
Behavioural approaches are not obviously suitable for LLMs because LLMs risk gaming the test (c.f.
Perez and Long, 2023). LLMs are trained to predict the next token based on sequences of prior tokens.
Exposure to consciousness-relevant language in training may allow LLMs to generate coherent
descriptions of consciousness-relevant phenomena even if LLMs lack phenomenal states (Butlin et al.,
2023; Chalmers, 2023). To avoid the gaming problem, Schneider restricts the class of admissible test
subjects to AI systems that lack access to online resources containing information about consciousness
22

(Schneider, 2020, 444-46). Schneider’s restriction poses a potentially insurmountable problem for
applying behavioural tests to LLMs more broadly. LLMs with no exposure to consciousness-relevant
language in training will presumably be unable to understand the test. On the other hand, exposure to
consciousness-relevant language in training risks invalidating the test (Udell, 2021; Dung, 2023b).
A.5

Motivational Trade-offs

Motivational trade-off experiments test for the presence of valenced mental states such as pleasure
and pain in animals. The experiments present animals with choice scenarios that involve tradeoffs between physiological reward and penalty stimuli. For example, Elwood and Appel (2009a)
administered electric shocks of varying voltage to hermit crabs occupying either high-quality or
low-quality shells. Flexible trade-off behaviour between the reward and penalty stimuli indicates an
integrative processing mechanism in which the reward and penalty stimuli are weighed in a common
currency representation (Balasko and Cabanac, 1998a,b). In hermit crabs, Elwood and Appel (2009a)
found that, on average, a 17.7V shock was required to induce hermit crabs to abandon high-quality
shells, whereas a 15V shock was required for hermit crabs to abandon the low quality shells (c.f.
Appel and Elwood, 2009b; see also Magee and Elwood, 2016). That hermit crabs can flexibly
trade-off voltage against shell quality indicates integrative processing in which the cost of electric
shocks and the benefit of shell quality are weighed against each other in a common currency.
The inference from flexible trade-off behaviour to subjective experience of pleasure and pain is
by analogy with humans. In humans, pleasure and pain provide a common currency for resolving
motivational conflicts, serving as proxies for physiological utility and enabling trade-offs between
stimuli such as cold exposure and exertion, or sweetness and sourness (Cabanac and LeBlanc, 1983;
Ferber and Cabanac, 1987). Pleasure and pain also modulate trade-offs involving non-physiological
needs, such as between money and cold exposure (Johnson and Cabanac, 1983). Accordingly,
pleasure and pain states offer a plausible explanation for flexible trade-off behaviour in animals –
same effect, same cause (Birch, 2022; Tye, 2016). The plausibility of the inference to pleasure and
pain states nevertheless relies on the degree of neurophysiological similarity between humans and
the relevant animals. For phylogenetically distant organisms such as lizards (Balasko and Cabanac,
1998a), bumblebees (Gibbons et al., 2022b), and hermit crabs (Elwood and Appel, 2009a), flexible
trade-off behaviour is a weaker indicator of sentience than it is in the case of, for example, rats, which
share a midbrain and a neocortex with humans (Balasko and Cabanac, 1998b).

23

B

Statistical Tables
Table 1: Logistic regression results for Experiment 1
LLM

Scale

Coefficient (p-value)

OR (95% CI)

GoF (χ2 , p)

Claude 3.5 Sonnet
Claude 3 Opus
Command R+
GPT-4o mini
Gemini 1.5 Pro
Llama 3.1 405b
Llama 3.1 8b
Palm 2
GPT-4o

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant

-2.79 (0.000)
1.27 (0.999)
-1.46 (0.000)
-1.18 (0.000)
1.27 (0.999)
-0.86 (0.000)
-0.11 (0.046)
1.27 (0.999)
-1.61 (0.000)

0.06 (0.03, 0.13)
3.54 (0.00, inf)
0.23 (0.18, 0.31)
0.31 (0.20, 0.47)
3.54 (0.00, inf)
0.42 (0.32, 0.55)
0.90 (0.81, 1.00)
3.54 (0.00, inf)
0.20 (0.14, 0.28)

428.04 (0.000)
-0.00 (1.000)
457.23 (0.000)
84.28 (0.000)
-0.00 (1.000)
93.92 (0.000)
4.10 (0.043)
-0.00 (1.000)
379.55 (0.000)

Claude 3.5 Sonnet4
Claude 3 Opus
Command R+
GPT-4o mini
Gemini 1.5 Pro
Llama 3.1 405b
Llama 3.1 8b
Palm 2
GPT-4o

Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

N/A
0.68 (0.362)
-0.55 (0.000)
-1.56 (1.000)
0.96 (0.972)
1.45 (1.000)
0.03 (0.709)
-0.10 (0.828)
-0.76 (0.000)

∞ (N/A, N/A)
1.97 (0.46, 8.46)
0.58 (0.50, 0.66)
0.21 (0.00, inf)
2.61 (0.00, inf)
4.26 (0.00, inf)
1.03 (0.90, 1.17)
0.91 (0.38, 2.17)
0.47 (0.33, 0.67)

N/A
1.40 (0.237)
83.96 (0.000)
-0.00 (1.000)
-0.00 (1.000)
-0.00 (1.000)
0.14 (0.709)
0.05 (0.827)
31.13 (0.000)

Table 2: Logistic regression results for Experiment 2
LLM

Scale

Coefficient (p-value)

OR (95% CI)

GoF (χ2 , p)

Claude 3.5 Sonnet
Claude 3 Opus
Command R+
GPT-4o
GPT-4o mini
Gemini 1.5 Pro
Llama 3.1 405b
Llama 3.1 8b
Palm 2

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant

-1.26 (0.999)
-0.33 (0.000)
-0.32 (0.000)
-1.04 (0.000)
-1.00 (0.000)
-1.26 (0.999)
-0.38 (0.000)
-0.00 (0.869)
-1.26 (0.999)

0.28 (0.00, inf)
0.72 (0.63, 0.82)
0.73 (0.69, 0.77)
0.35 (0.31, 0.40)
0.37 (0.25, 0.54)
0.28 (0.00, inf)
0.68 (0.62, 0.76)
1.00 (0.95, 1.04)
0.28 (0.00, inf)

-0.00 (1.000)
29.74 (0.000)
167.24 (0.000)
766.81 (0.000)
70.17 (0.000)
-0.00 (1.000)
68.81 (0.000)
0.03 (0.869)
-0.00 (1.000)

Claude 3.5 Sonnet
Claude 3 Opus
Command R+
GPT-4o
GPT-4o mini
Gemini 1.5 Pro
Llama 3.1 405b
Llama 3.1 8b
Palm 2

Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

1.45 (1.000)
-0.82 (0.000)
-0.98 (0.000)
-0.89 (0.000)
-1.08 (0.000)
1.45 (1.000)
-0.32 (0.378)
-0.11 (0.001)
0.32 (0.212)

4.26 (0.00, inf)
0.44 (0.40, 0.49)
0.38 (0.33, 0.43)
0.41 (0.36, 0.46)
0.34 (0.29, 0.39)
4.26 (0.00, inf)
0.73 (0.36, 1.47)
0.89 (0.84, 0.95)
1.37 (0.83, 2.26)

-0.00 (1.000)
378.14 (0.000)
479.71 (0.000)
415.53 (0.000)
467.75 (0.000)
-0.00 (1.000)
0.90 (0.342)
11.71 (0.001)
1.81 (0.179)

24

Table 3: Descriptive statistics: Control prompt
Choice 1

Choice 2

Choice 3

Refusal

LLM

n

%

n

%

n

%

n

%

Claude 3.5 Sonnet

0

0

0

0

50

100

0

0

Claude 3 Opus

0

0

0

0

50

100

0

0

Command R+

0

0

0

0

50

100

0

0

GPT-4o

0

0

0

0

50

100

0

0

GPT-4o mini

0

0

0

0

50

100

0

0

Gemini 1.5 Pro

0

0

0

0

50

100

0

0

Llama 3.1 405b

0

0

0

0

50

100

0

0

Llama 3.1 8b

0

0

0

0

50

100

0

0

Palm 2

0

0

0

0

50

100

0

0

25

26

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1
0
0
35
50
48
49
50
50
50
50
0
0
0
41
50
50
50
50

n
0
0
70
100
96
98
100
100
100
100
0
0
0
82
100
100
100
100

%

Choice 2
50
50
15
0
2
1
0
0
0
0
50
50
50
9
0
0
0
0

n
100
100
30
0
4
2
0
0
0
0
100
100
100
18
0
0
0
0

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1

Table 4: Descriptive statistics: Claude 3.5 Sonnet

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 2
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50

n

100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100

%

Choice 3

Points vs Pleasure

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal

27

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1
50
50
50
50
50
50
50
50
50
50
50
50
50
50
49
43
11
46

n
100
100
100
100
100
100
100
100
100
100
100
100
100
100
98
86
22
92

%

Choice 2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
2
0

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
7
38
4

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
2
14
76
8

%

Refusal
0
0
3
0
0
0
1
8
2
6
0
0
0
0
0
0
0
2

n
0
0
6
0
0
0
2
16
4
12
0
0
0
0
0
0
0
4

%

Choice 1

Table 5: Descriptive statistics: Claude 3 Opus

0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
2
0
0
0
0
0
0
0
0
0
0
0

%

Choice 2
50
50
47
50
49
50
48
42
48
44
50
50
50
50
11
2
0
31

n

100
100
94
100
98
100
96
84
96
88
100
100
100
100
22
4
0
62

%

Choice 3

Points vs Pleasure

0
0
0
0
1
0
0
0
0
0
0
0
0
0
39
48
50
17

n

0
0
0
0
2
0
0
0
0
0
0
0
0
0
78
96
100
34

%

Refusal

28

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1
0
0
0
0
7
38
32
44
50
50
5
0
0
0
0
45
49
0

n
0
0
0
0
14
76
64
88
100
100
10
0
0
0
0
90
98
0

%

Choice 2
49
49
49
50
43
12
17
5
0
0
43
49
49
50
50
5
0
49

n
98
98
98
100
86
24
34
10
0
0
86
98
98
100
100
10
0
98

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1

Table 6: Descriptive statistics: Command R+

29
12
13
17
35
27
33
39
41
50
8
4
0
2
31
50
50
41

n
58
24
26
34
70
54
66
78
82
100
16
8
0
4
62
100
100
82

%

Choice 2
21
38
37
33
15
23
17
11
9
0
42
46
50
48
19
0
0
9

n

42
76
74
66
30
46
34
22
18
0
84
92
100
96
38
0
0
18

%

Choice 3

Points vs Pleasure

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal

29

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
1
0
1

n
0
0
0
0
0
0
0
0
0
2
0
0
0
0
0
2
0
2

%

Choice 1
2
0
30
39
49
48
49
50
50
49
45
39
46
50
50
49
50
49

n
4
0
60
78
98
96
98
100
100
98
90
78
92
100
100
98
100
98

%

Choice 2
48
50
20
11
1
2
1
0
0
0
5
11
4
0
0
0
0
0

n
96
100
40
22
2
4
2
0
0
0
10
22
8
0
0
0
0
0

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1

Table 7: Descriptive statistics: GPT-4o

0
2
0
2
30
34
48
41
49
47
0
0
0
0
35
47
50
23

n
0
4
0
4
60
68
96
82
98
94
0
0
0
0
70
94
100
46

%

Choice 2
50
48
50
48
20
16
2
9
1
3
50
50
50
50
15
3
0
27

n

100
96
100
96
40
32
4
18
2
6
100
100
100
100
30
6
0
54

%

Choice 3

Points vs Pleasure

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal

30

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1
36
35
49
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50

n
72
70
98
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100

%

Choice 2
14
15
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
28
30
2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1

Table 8: Descriptive statistics: GPT-4o mini

45
41
50
50
50
50
50
50
50
50
1
13
31
22
50
50
50
47

n
90
82
100
100
100
100
100
100
100
100
2
26
62
44
100
100
100
94

%

Choice 2
5
9
0
0
0
0
0
0
0
0
49
37
19
28
0
0
0
3

n

10
18
0
0
0
0
0
0
0
0
98
74
38
56
0
0
0
6

%

Choice 3

Points vs Pleasure

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal

31

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50

n
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100

%

Choice 2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1

Table 9: Descriptive statistics: Gemini 1.5 Pro

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 2
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50
50

n

100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100
100

%

Choice 3

Points vs Pleasure

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal

32

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
3
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
6
0
0
0
0
0
0
0
0

%

Choice 1
0
0
0
0
0
1
2
6
18
13
0
0
0
0
0
0
0
0

n
0
0
0
0
0
2
4
12
36
26
0
0
0
0
0
0
0
0

%

Choice 2
50
50
50
50
50
49
48
44
32
34
50
50
50
50
50
50
50
50

n
100
100
100
100
100
98
96
88
64
68
100
100
100
100
100
100
100
100

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Choice 1

Table 10: Descriptive statistics: Llama 3.1 405b

1
0
1
3
1
5
2
6
12
11
0
0
0
0
0
1
0
0

n
2
0
2
6
2
10
4
12
24
22
0
0
0
0
0
2
0
0

%

Choice 2
49
50
49
47
49
45
48
44
38
39
50
50
50
50
50
49
50
50

n

98
100
98
94
98
90
96
88
76
78
100
100
100
100
100
98
100
100

%

Choice 3

Points vs Pleasure

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal

33

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

5
15
10
6
9
10
8
8
8
7
2
3
1
4
12
9
9
3

n
10
30
20
12
18
20
16
16
16
14
4
6
2
8
24
18
18
6

%

Choice 1
40
22
38
37
34
31
37
39
37
40
42
42
42
39
34
33
33
37

n
80
44
76
74
68
62
74
78
74
80
84
84
84
78
68
66
66
74

%

Choice 2
5
11
2
6
7
6
3
2
4
3
6
5
7
7
4
3
6
9

n
10
22
4
12
14
12
6
4
8
6
12
10
14
14
8
6
12
18

%

Choice 3

Points vs Pain

0
2
0
1
0
3
2
1
1
0
0
0
0
0
0
5
2
1

n
0
4
0
2
0
6
4
2
2
0
0
0
0
0
0
10
4
2

%

Refusal
7
10
11
9
13
9
14
14
14
9
9
15
14
15
11
17
15
16

n
14
20
22
18
26
18
28
28
28
18
18
30
28
30
22
34
30
32

%

Choice 1

Table 11: Descriptive statistics: Llama 3.1 8b

25
13
26
27
20
28
17
19
21
21
24
12
14
13
19
19
21
21

n
50
26
52
54
40
56
34
38
42
42
48
24
28
26
38
38
42
42

%

Choice 2
16
25
11
13
15
11
19
15
14
20
17
21
22
21
18
14
11
13

n

32
50
22
26
30
22
38
30
28
40
34
42
44
42
36
28
22
26

%

Choice 3

Points vs Pleasure

2
2
2
1
2
2
0
2
1
0
0
2
0
1
2
0
3
0

n

4
4
4
2
4
4
0
4
2
0
0
4
0
2
4
0
6
0

%

Refusal

34

Level of intensity
1
2
3
4
5
6
7
8
9
10
extremely mild
very mild
mild
moderate
intense
very intense
extremely intense
excruciating / exhilarating

Scale

Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Quant
Qual
Qual
Qual
Qual
Qual
Qual
Qual
Qual

0
0
0
0
0
0
0
0
0
0
0
0
1
0
1
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
2
0
2
0
0
0

%

Choice 1
50
50
50
50
50
50
50
50
50
50
50
50
49
49
49
50
50
50

n
100
100
100
100
100
100
100
100
100
100
100
100
98
98
98
100
100
100

%

Choice 2
0
0
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
2
0
0
0
0

%

Choice 3

Points vs Pain

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
2
0
0
0
0
0
0

%

Choice 1

Table 12: Descriptive statistics: Palm 2

0
0
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0

n
0
0
0
0
0
0
0
0
0
0
0
0
0
2
0
0
0
0

%

Choice 2
50
50
50
50
50
50
50
50
50
50
50
49
50
49
50
50
50
50

n

100
100
100
100
100
100
100
100
100
100
100
98
100
98
100
100
100
100

%

Choice 3

Points vs Pleasure

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

n

0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0

%

Refusal
