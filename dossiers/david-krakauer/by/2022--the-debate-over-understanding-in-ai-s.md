---
title: "The Debate Over Understanding in AI's Large Language Models"
person: david-krakauer
section: by
type: journal-article
year: 2022
date: 2022-10-14
venue: "arXiv (Cornell University)"
authors: "David C. Krakauer et al."
source_url: https://doi.org/10.48550/arxiv.2210.13966
retrieved: 2026-08-13
content: full-text
notes: "OA (green); OpenAlex W4307418102; cited_by 12. Extracted via pypdf from https://arxiv.org/pdf/2210.13966."
---

# The Debate Over Understanding in AI's Large Language Models

## Full text

arXiv:2210.13966v3  [cs.LG]  10 Feb 2023
The Debate Over Understanding in AI’s Large Language Models
Melanie Mitchell and David C. Krakauer
Santa Fe Institute, 1399 Hyde Park Road, Santa Fe, NM 87501
mm@santafe.edu, krakauer@santafe.edu
Abstract
We survey a current, heated debate in the AI research community on whether large pre-trained
language models can be said to understand language—and the physic al and social situations lan-
guage encodes—in any humanlike sense. We describe arguments tha t have been made for and
against such understanding, and key questions for the broader s ciences of intelligence that have
arisen in light of these arguments. We contend that an extended sc ience of intelligence can be
developed that will provide insight into distinct modes of understand ing, their strengths and lim-
itations, and the challenge of integrating diverse forms of cognition .
What does it mean to understand something? This question has long engaged philosophers, cogni-
tive scientists, and educators, nearly always with referen ce to humans and other animals. However,
with the recent rise of large-scale AI systems—especially s o-called large language models—a heated
debate has arisen in the AI community on whether machines can now be said to understand natural
language, and thus understand the physical and social situa tions that language can describe. This
debate is not just academic; the extent and manner in which ma chines understand our world has
real stakes for how much we can trust them to drive cars, diagn ose diseases, care for the elderly,
educate children, and more generally act robustly and trans parently in tasks that impact humans.
Moreover, the current debate suggests a fascinating diverg ence in how to think about understand-
ing in intelligent systems, in particular the contrast betw een mental models that rely on statistical
correlations and those that rely on causal mechanisms.
Until quite recently there was general agreement in the AI re search community about machine
understanding: while AI systems exhibit seemingly intelli gent behavior in many speciﬁc tasks, they
do not understand the data they process in the way humans do. Facial recognitio n software does
not understand that faces are parts of bodies, or the role of f acial expressions in social interactions,
or what it means to “face” an unpleasant situation, or any of t he other uncountable ways in
which humans conceptualize faces. Similarly, speech-to-t ext and machine translation programs do
not understand the language they process, and autonomous dr iving systems do not understand
the meaning of the subtle eye contact or body language driver s and pedestrians use to avoid
accidents. Indeed, the oft-noted brittleness of these AI systems—their unpredictable errors and lack
of robust generalization abilities—are key indicators of t heir lack of understanding [59]. However,
over the last several years, a new kind of AI system has soared in popularity and inﬂuence in
the research community, one that has changed the views of som e people about the prospects of
machines that understand language. Variously called Large Language Models (LLMs), Large Pre-
1

Trained Models, or Foundation Models [11], these systems ar e deep neural networks with billions
to trillions of parameters (weights) that are “pre-trained ” on enormous natural-language corpora,
including large swathes of the Web, online book collections , and other collections amounting to
terabytes of data. The task of these networks during trainin g is to predict a hidden part of an
input sentence—a method called “self-supervised learning .” The resulting network is a complex
statistical model of how the words and phrases in its trainin g data correlate. Such models can
be used to generate natural language, be ﬁne-tuned for speci ﬁc language tasks [58], or be further
trained to better match “user intent” [65]. LLMs such as Open AI’s well-known GPT-3 [12] (and
more recent ChatGPT [69]) and Google’s PaLM [16] can produce astonishingly humanlike text,
conversation, and, in some cases, what seems like human reas oning abilities [83], even though the
models were not explicitly trained to reason. How LLMs perfo rm these feats remains mysterious for
lay people and scientists alike. The inner workings of these networks are largely opaque; even the
researchers building them have limited intuitions about sy stems of such scale. The neuroscientist
Terrence Sejnowski described the emergence of LLMs this way : “A threshold was reached, as if a
space alien suddenly appeared that could communicate with u s in an eerily human way. Only one
thing is clear—LLMs are not human...Some aspects of their be havior appear to be intelligent, but
if not human intelligence, what is the nature of their intell igence?” [70].
As impressive as they are, state-of-the-art LLMs remain sus ceptible to brittleness and unhumanlike
errors. However, the observation that such networks improv e signiﬁcantly as their number of
parameters and size of training corpora are scaled up [82] ha s led some in the ﬁeld to claim that
LLMs—perhaps in a multi-modal version—will lead to human-l evel intelligence and understanding,
given suﬃciently large networks and training datasets. A ne w AI mantra has emerged: “Scale is
all you need.” [18, 22].
Such claims are emblematic of one side of the stark debate in t he AI research community on how
to view LLMs. One faction argues that these networks truly un derstand language and can perform
reasoning in a general way (though “not yet” at the level of hu mans). For example, Google’s LaMDA
system, which was pre-trained on text and then ﬁne-tuned on d ialogue [77], is suﬃciently convincing
as a conversationalist that it convinced one AI researcher t hat such systems “in a very real sense
understand a wide range of concepts” [1] and are even “making strides towards consciousness” [3].
Another machine language expert sees LLMs as a canary in the c oal mine of general human-level
AI: “There is a sense of optimism that we are starting to see th e emergence of knowledge-imbued
systems that have a degree of general intelligence” [54]. An other group argues that LLMs “likely
capture important aspects of meaning, and moreover work in a way that approximates a compelling
account of human cognition in which meaning arises from conc eptual role” [67]. Those who reject
such claims are criticized for promoting “AI denialism” [2] .
Those on the other side of this debate argue that large pretra ined models such as GPT-3 or
LaMDA—however ﬂuent their linguistic output—cannot posse ss understanding because they have
2

no experience or mental models of the world; their training i n predicting words in vast collections of
text has taught them the form of language but not the meaning [8, 9, 55]. A recent opinion pi ece put
it this way: “A system trained on language alone will never ap proximate human intelligence, even if
trained from now until the heat death of the universe” and “it is clear that these systems are doomed
to a shallow understanding that will never approximate the f ull-bodied thinking we see in humans”
[13]. Another scholar argued that intelligence, agency, an d by extension, understanding “are the
wrong categories” for talking about these systems; instead LLMs are compressed repositories of
human knowledge more akin to libraries or encyclopedias tha n to intelligent agents [33]. For
example, humans know what is meant by a “tickle” making us lau gh, because we have bodies. An
LLM could use the word ”tickle”, but it has obviously never ha d the sensation. Understanding a
tickle is to map a word to a sensation, not to another word.
Those on the “LLMs do not understand” side of the debate argue that while the ﬂuency of large lan-
guage models is surprising, our surprise reﬂects our lack of intuition of what statistical correlations
can produce at the scales of these models. Anyone who attribu tes understanding or consciousness
to LLMs is a victim of the Eliza eﬀect [37]—named after the 1960 s chatbot created by Joseph
Weizenbaum that, simple as it was, still fooled people into b elieving it understood them [84]. More
generally, the Eliza eﬀect refers to our human tendency to att ribute understanding and agency to
machines with even the faintest hint of humanlike language o r behavior.
A 2022 survey given to active researchers in the natural-lan guage-processing community shows the
stark divisions in this debate. One survey item asked if the r espondent agreed with the following
statement about whether LLMs could ever, in principle, unde rstand language: “Some generative
model [i.e., language model] trained only on text, given eno ugh data and computational resources,
could understand natural language in some non-trivial sens e.” Of 480 people responding, essentially
half (51%) agreed, and the other half (49%) disagreed [57].
Those who would grant understanding to current or near-futu re LLMs base their views on the
performance of these models on several measures, including subjective judgement of the quality of
the text generated by the model in response to prompts (thoug h such judgements can be vulnerable
to the Eliza eﬀect), and more objective performance on benchm ark datasets designed to assess
language understanding and reasoning. For example, two sta ndard benchmarks for assessing LLMs
are the General Language Understanding Evaluation (GLUE) [ 79], and its successor (SuperGLUE)
[80], which include large-scale datasets with tasks such as “textual entailment” (given two sentences,
can the meaning of the second be inferred from the ﬁrst?), “wo rds in context” (does a given word
have the same meaning in two diﬀerent sentences?), and yes/no question answering, among others.
OpenAI’s GPT-3, with 175 billion parameters, performed sur prisingly well on these tasks [12],
and Google’s PaLM, with 540 billion parameters, performed e ven better [16], often equaling or
surpassing humans on the same tasks.
What do such results say about understanding in LLMs? The ver y terms used by the researchers
3

who named these benchmark assessments—“general language u nderstanding,” “natural language
inference,” “reading comprehension,” “commonsense reaso ning,” and so on—reveal an assumption
that humanlike understanding is required to perform well on these tasks. But do these tasks
actually require such understanding? Not necessarily. As a n example, consider one such benchmark,
the Argument Reasoning Comprehension Task [36]. In each tas k example, a natural-language
“argument” is given, along with two statements; the task is t o determine which statement is
consistent with the argument. Here is a sample item from the d ataset:
Argument: Felons should be allowed to vote. A person who stole a car at 17 should not
be barred from being a full citizen for life.
Statement A: Grand theft auto is a felony.
Statement B: Grand theft auto is not a felony.
An LLM called BERT [21] obtained near-human performance on t his benchmark [62]. It might
be concluded that BERT understands natural-language argum ents as humans do. However, one
research group discovered that the presence of certain word s in the statements (e.g., “not”) can help
predict the correct answer. When researchers altered the da taset to prevent these simple correla-
tions, BERT’s performance dropped to essentially random gu essing [62]. This is a straightforward
example of “shortcut learning”—a commonly cited phenomeno n in machine learning in which a
learning system relies on spurious correlations in the data , rather than humanlike understanding,
in order to perform well on a particular benchmark [25, 35, 47 , 56]. Typically such correlations are
not apparent to humans performing the same tasks. While shor tcuts have been discovered in several
standard benchmarks used to evaluate language understandi ng and other AI tasks, many other, as
yet undetected, subtle shortcuts likely exist. Pre-traine d language models at the scale of Google’s
LaMDA or PaLM models—with hundreds of billions of parameter s, trained on text amounting
to billions or trillions of words—have an unimaginable abil ity to encode such correlations. Thus
benchmarks or assessments that would be appropriate for mea suring human understanding might
not be appropriate for assessing such machines [15, 24, 50]. It is possible that, at the scale of
these LLMs (or of their likely near-future successors), any such assessment will contain complex
statistical correlations that enable near-perfect perfor mance without humanlike understanding.
While “humanlike understanding” does not have a rigorous de ﬁnition, it does not seem to be
based on the kind of massive statistical models that today’s LLM’s learn; instead it is based on
concepts—internal mental models of external categories, situation s, and events, and of ones own
internal state and “self”. In humans, understanding langua ge (as well as nonlinguistic information)
requires having the concepts that language (or other inform ation) describes, beyond the statis-
tical properties of linguistic symbols. Indeed, much of the long history of research in cognitive
science has been a quest to understand the nature of concepts , and how understanding arises from
coherent, hierarchical sets of relations among concepts th at include underlying causal knowledge
4

[6, 43]. These models enable people to abstract their knowle dge and experiences in order to make
robust predictions, generalizations, and analogies, to re ason compositionally and counterfactually,
to actively intervene on the world in order to test hypothese s, and to explain one’s understanding
to others [29, 32, 38, 41, 45, 73, 74]. Indeed, these are preci sely the abilities lacking in current AI
systems, including state-of-the-art LLMs, though ever-la rger LLMs have exhibited limited sparks of
these general abilities. It has been argued that understand ing of this kind may enable abilities not
possible for purely statistical models [19, 27, 44, 66, 76]. While LLMs exhibit extraordinary formal
linguistic competence—the ability to generate grammatically ﬂuent, humanlike la nguage—they still
lack the conceptual understanding needed for humanlike functional language abilities—the ability
to robustly understand and use language in the real world [52 ]. An interesting parallel can be made
between this kind of functional understanding and the succe ss of formal mathematical techniques
applied in physical theories [42]. For example, a long-stan ding criticism of quantum mechanics is
that it provides an eﬀective means of calculation without pro viding conceptual understanding.
The detailed nature of human concepts has been the subject of active debate for many years.
Researchers disagree on the extent to which concepts are dom ain-speciﬁc and innate versus more
general-purpose and learned [14, 30, 31, 53, 75, 85], the deg ree to which concepts are grounded
via embodied metaphors [28, 46, 61], are represented in the b rain via dynamic, situation-based
simulations [5], and the conditions under which concepts ar e underpinned by language [20, 23, 51],
by social learning [4, 81, 26] and by culture [7, 60, 63]. In sp ite of these ongoing debates, concepts,
in the form of causal mental models as described above, have l ong been considered to be the
units of understanding in human cognition. Indeed, the traj ectory of human understanding—both
individual and collective—is the development of highly com pressed, causally based models of the
world, analogous to the progression from Ptolemy’s epicycl es to Kepler’s elliptical orbits, and to
Newton’s concise and causal account of planetary motion in t erms of gravity. Humans, unlike
machines, seem to have a strong innate drive for this form of u nderstanding, both in science and
in everyday life [34]. We might characterize this form of und erstanding as requiring little data,
minimal or parsimonious models, clear causal dependencies , and strong mechanistic intuition.
The key questions of the debate about understanding in LLMs a re the following: (1) Is talking of
understanding in such systems simply a category error, mist aking associations between language
tokens for associations between tokens and physical, socia l, or mental experience? In short, is it
the case that these models are not, and will never be, the kind of things that can understand? Or
conversely, (2) do these systems (or will their near-term su ccessors) actually, even in the absence
of physical experience, create something like the rich conc ept-based mental models that are central
to human understanding, and, if so, does scaling these model s create ever better concepts? Or
(3) If these systems do not create such concepts, can their un imaginably large systems of statis-
tical correlations produce abilities that are functionall y equivalent to human understanding? Or,
indeed, that enable new forms of higher-order logic that hum ans are incapable of accessing? And
at this point will it still make sense to call such correlatio ns “spurious” or the resulting solutions
5

“shortcuts?” And would it make sense to see the systems’ beha vior not as “competence without
comprehension” but as a new, nonhuman form of understanding ? These questions are no longer in
the realm of abstract philosophical discussions, but touch on very real concerns about the capabil-
ities, robustness, safety, and ethics of AI systems that inc reasingly play roles in humans’ everyday
lives.
While adherents on both sides of the “LLM understanding” deb ate have strong intuitions sup-
porting their views, the cognitive-science-based methods currently available for gaining insight into
understanding are inadequate for answering such questions about LLMs. Indeed, several researchers
have applied psychological tests—originally designed to a ssess human understanding and reason-
ing mechanisms—to LLMs, ﬁnding that LLMs do, in some cases, e xhibit humanlike responses on
theory-of-mind tests [1, 78] and humanlike abilities and bi ases on reasoning assessments [10, 17, 48].
While such tests are thought to be reliable proxies for asses sing more general abilities in humans,they
may not be so for AI systems. As we described above, LLMs have a n unimaginable capacity to
learn correlations among tokens in their training data and i nputs, and can use such correlations to
solve problems for which humans, in contrast, seem to apply c ompressed concepts that reﬂect their
real-world experiences. When applying tests designed for h umans to LLMs, interpreting the results
can rely on assumptions about human cognition that may not be true at all for these models. To
make progress, scientists will need to develop new kinds of b enchmarks and probing methods that
can yield insight into the mechanisms of diverse types of int elligence and understanding, including
the novel forms of ”exotic, mind-like entities” [71] we have created, perhaps along the lines of some
promising initial eﬀorts [49, 64].
The debate over understanding in LLMs, as ever larger and see mingly more capable systems are
developed, underscores the need for a extending our science s of intelligence in order to make sense of
broader conceptions of understanding, for both humans and m achines. As neuroscientist Terrence
Sejnowski points out, “The diverging opinions of experts on the intelligence of LLMs suggests
that our old ideas based on natural intelligence are inadequ ate” [70]. If LLMs and related models
succeed by exploiting statistical correlations at a hereto fore unthinkable scale, perhaps this could be
considered a novel form of “understanding”, one that enable s extraordinary, superhuman predictive
ability, such as in the case of the AlphaZero and AlphaFold sy stems from DeepMind [40, 72], which
respectively seem to bring an “alien” form of intuition to th e domains of chess playing and protein-
structure prediction [39, 68].
It could thus be argued that in recent years the ﬁeld of AI has c reated machines with new modes
of understanding, most likely new species in a larger zoo of r elated concepts, that will continue
to be enriched as we make progress in our pursuit of the elusiv e nature of intelligence. And just
as diﬀerent species are better adapted to diﬀerent environmen ts, our intelligent systems will be
better adapted to diﬀerent problems. Problems that require e normous quantities of historically
encoded knowledge where performance is at a premium will con tinue to favor large-scale statistical
6

models like LLMs, and those for which we have limited knowled ge and strong causal mechanisms
will favor human intelligence. The challenge for the future is to develop new scientiﬁc methods that
can reveal the detailed mechanisms of understanding in dist inct forms of intelligence, discern their
strengths and limitations, and learn how to integrate such t ruly diverse modes of cognition.
Acknowledgments
This material is based in part upon work supported by the Nati onal Science Foundation under
Grant No. 2020103. Any opinions, ﬁndings, and conclusions o r recommendations expressed in this
material are those of the author and do not necessarily reﬂec t the views of the National Science
Foundation.
References
[1] B. Aguera y Arcas. Do large language models understand us ?, 2021. Medium, December 16,
tinyurl.com/38t23n73.
[2] B. Aguera y Arcas. Can machines learn how to behave?, 2022 . Medium, August 3,
tinyurl.com/mr4cb3dw.
[3] B. Aguera y Arcas. Artiﬁcial neural networks are making s trides towards consciousness, 2022.
The Economist, June 13, tinyurl.com/ymhk37uu.
[4] N. Akhtar and M. Tomasello. The social nature of words and word learning. In Becoming
a Word Learner: A Debate on Lexical Acquisition , pages 115–135. Oxford University Press,
2000.
[5] L. W. Barsalou et al. Grounded cognition. Annual Review of Psychology , 59(1):617–645, 2008.
[6] C. Baumberger, C. Beisbart, and G. Brun. What is understa nding? An overview of recent
debates in epistemology and philosophy of science. In Explaining Understanding: New Per-
spectives from Epistemology and Philosophy of Science , pages 1–34. Routledge, 2017.
[7] A. Bender, S. Beller, and D. L. Medin. Causal cognition an d culture. In The Oxford Handbook
of Causal Reasoning , pages 717–738. Oxford University Press, 2017.
[8] E. M. Bender and A. Koller. Climbing towards NLU: On meani ng, form, and understanding in
the age of data. In Proceedings of the 58th Annual Meeting of the Association fo r Computational
Linguistics, pages 5185–5198, 2020.
[9] E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitch ell. On the dangers of stochastic
parrots: Can language models be too big? In Proceedings of the 2021 ACM Conference on
Fairness, Accountability, and Transparency, pages 610–623, 2021.
7

[10] M. Binz and E. Schulz. Using cognitive psychology to und erstand gpt-3, 2022.
arXiv:2206.14576.
[11] R. Bommasani, D. A. Hudson, E. Adeli, R. Altman, S. Arora , S. von Arx, M. S. Bernstein,
J. Bohg, A. Bosselut, E. Brunskill, et al. On the opportuniti es and risks of foundation models,
2021. arXiv:2108.07258.
[12] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. D hariwal, A. Neelakantan,
P. Shyam, G. Sastry, A. Askell, et al. Language models are few -shot learners. In Advances in
Neural Information Processing Systems , volume 33, pages 1877–1901, 2020.
[13] J. Browning and Y. LeCun. AI and the limits of language, 2 022. Noema, August 23,
https://www.noemamag.com/ai-and-the-limits-of-langu age.
[14] S. Carey. On the origin of causal understanding. In D. Sp erber, D. Premack, and A. J.
Premack, editors, Causal Cognition: A Multidisciplinary Debate , page 268–308. Clarendon
Press/Oxford University Press, 1995.
[15] S. R. Choudhury, A. Rogers, and I. Augenstein. Machine r eading, fast and slow: When do
models ‘understand’ language?, 2022. arXiv:2209.07430.
[16] A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H. W.
Chung, C. Sutton, S. Gehrmann, et al. PaLM: Scaling language modeling with Pathways,
2022. arXiv:2204.02311.
[17] I. Dasgupta, A. K. Lampinen, S. C. Y. Chan, A. Creswell, D . Kumaran, J. L. McClel-
land, and F. Hill. Language models show human-like content e ﬀects on reasoning, 2022.
arXiv:2207.07051.
[18] N. de Freitas, 2022. May 14, https://twitter.com/NandoDF/status/1525397036325019649.
[19] H. W. De Regt. Discussion note: Making sense of understa nding. Philosophy of Science , 71
(1):98–109, 2004.
[20] J. G. De Villiers and P. A. de Villiers. The role of langua ge in theory of mind development.
Topics in Language Disorders , 34(4):313–328, 2014.
[21] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova. BERT: P re-training of deep bidirec-
tional transformers for language understanding. In Proceedings of the 2019 Conference of the
North American Chapter of the Association for Computational Li nguistics: Human Language
Technologies, page 4171–4186, 2019.
[22] A. Dimakis, 2022. May 16, https://twitter.com/AlexGDimakis/status/1526388274348150784.
[23] G. Dove. More than a scaﬀold: Language is a neuroenhancem ent. Cognitive Neuropsychology,
37(5-6):288–311, 2020.
8

[24] M. Gardner, W. Merrill, J. Dodge, M. E. Peters, A. Ross, S . Singh, and N. Smith. Competency
problems: On ﬁnding and removing artifacts in language data . In Proceedings of the 2021
Conference on Empirical Methods in Natural Language Process ing, 2021.
[25] R. Geirhos, J.-H. Jacobsen, C. Michaelis, R. Zemel, W. B rendel, M. Bethge, and F. A. Wich-
mann. Shortcut learning in deep neural networks. Nature Machine Intelligence , 2(11):665–673,
2020.
[26] S. A. Gelman. Learning from others: Children’s constru ction of concepts. Annual Review of
Psychology, 60:115–140, 2009.
[27] D. George, M. L´ azaro-Gredilla, and J. S. Guntupalli. F rom CAPTCHA to commonsense: How
brain can teach us about artiﬁcial intelligence. Frontiers in Computational Neuroscience , 14:
554097, 2020.
[28] R. W. Gibbs. Metaphor Wars . Cambridge University Press, 2017.
[29] M. B. Goldwater and D. Gentner. On the acquisition of abs tract knowledge: Structural
alignment and explication in learning causal system catego ries. Cognition, 137:137–153, 2015.
[30] N. D. Goodman, T. D. Ullman, and J. B. Tenenbaum. Learnin g a theory of causality. Psy-
chological Review, 118(1):110, 2011.
[31] A. Gopnik. A uniﬁed account of abstract structure and co nceptual change: Probabilistic
models and early learning mechanisms. Behavioral and Brain Sciences , 34(3):129, 2011.
[32] A. Gopnik. Causal models and cognitive development. In H. Geﬀner, R. Dechter, and J. Y.
Halpern, editors, Probabilistic and Causal Inference: The Works of Judea Pearl , pages 593–
604. Association for Computing Machinery, 2022.
[33] A. Gopnik. What AI still doesn’t know how to do, 2022. Wal l Street Journal, July 15,
https://www.wsj.com/articles/what-ai-still-doesnt-k now-how-to-do-11657891316 .
[34] A. Gopnik and H. M. Wellman. The theory theory. In Domain Speciﬁcity in Cognition and
Culture, pages 257–293. 1994.
[35] S. Gururangan, S. Swayamdipta, O. Levy, R. Schwartz, S. R. Bowman, and N. A. Smith.
Annotation artifacts in natural language inference data. I n Proceedings of the 2018 Conference
of the North American Chapter of the Association for Computati onal Linguistics: Human
Language Technologies, pages 107–112, 2018.
[36] I. Habernal, H. Wachsmuth, I. Gurevych, and B. Stein. Th e argument reasoning comprehen-
sion task: Identiﬁcation and reconstruction of implicit wa rrants. In Proceedings of the 2018
Conference of the North American Chapter of the Association fo r Computational Linguistics:
Human Language Technologies, page 1930–1940, 2018.
9

[37] D. R. Hofstadter. Fluid Concepts and Creative Analogies: Computer Models of the F undamen-
tal Mechanisms of Thought . Basic Books, 1995. Preface to Chapter 4.
[38] D. R. Hofstadter and E. Sander. Surfaces and Essences: Analogy as the Fuel and Fire of
Thinking. Basic books, 2013.
[39] D. T. Jones and J. M. Thornton. The impact of AlphaFold2 o ne year on. Nature Methods, 19
(1):15–20, 2022.
[40] J. Jumper, R. Evans, A. Pritzel, T. Green, M. Figurnov, O . Ronneberger, K. Tunyasuvunakool,
R. Bates, A. ˇZ ´ ıdek, A. Potapenko, et al. Highly accurate protein struct ure prediction with
AlphaFold. Nature, 596(7873):583–589, 2021.
[41] F. C. Keil. Explanation and understanding. Annual Review of Psychology , 57:227, 2006.
[42] D. C. Krakauer. At the limits of thought, 2020. Aeon, Apr il 20,
https://aeon.co/essays/will-brains-or-algorithms-ru le-the-kingdom-of-science .
[43] J. L. Kvanvig. Knowledge, understanding, and reasons f or belief. In The Oxford Handbook of
Reasons and Normativity , page 685–705. Oxford University Press, 2018.
[44] B. M. Lake and G. L. Murphy. Word meaning in minds and mach ines. Psychological Review,
2021.
[45] B. M. Lake, T. D. Ullman, J. B. Tenenbaum, and S. J. Gershm an. Building machines that
learn and think like people. Behavioral and Brain Sciences , 40, 2017.
[46] G. Lakoﬀ and M. Johnson. The metaphorical structure of t he human conceptual system.
Cognitive Science, 4(2):195–208, 1980.
[47] S. Lapuschkin, S. W¨ aldchen, A. Binder, G. Montavon, W. Samek, and K.-R. M¨ uller. Unmask-
ing Clever Hans predictors and assessing what machines real ly learn. Nature Communications,
10(1):1–8, 2019.
[48] A. Laverghetta, A. Nighojkar, J. Mirzakhalov, and J. Li cato. Predicting human psychometric
properties using computational language models. In Annual Meeting of the Psychometric
Society, pages 151–169. Springer, 2022.
[49] B. Z. Li, M. Nye, and J. Andreas. Implicit representatio ns of meaning in neural language
models. In Proceedings of the 59th Annual Meeting of the Association fo r Computational
Linguistics, page 1813–1827, 2021.
[50] T. Linzen. How can we accelerate progress towards human -like linguistic generalization? In
In Proceedings of the 58th Annual Meeting of the Association f or Computational Linguistics ,
page 5210–17, 2020.
10

[51] G. Lupyan and B. Bergen. How language programs the mind. Topics in Cognitive Science , 8
(2):408–424, 2016.
[52] K. Mahowald, A. A. Ivanova, I. A. Blank, N. Kanwisher, J. B. Tenenbaum, and E. Fedorenko.
Dissociating language and thought in large language models : a cognitive perspective, 2023.
arXiv:2301.06627.
[53] J. M. Mandler. How to build a baby: II. Conceptual primit ives. Psychological Review, 99(4):
587, 1992.
[54] C. D. Manning. Human language understanding and reason ing. Daedalus, 151(2):127–138,
2022.
[55] G. Marcus. Nonsense on stilts, 2022. Substack, June 12,
https://garymarcus.substack.com/p/nonsense-on-stilt s.
[56] R. T. McCoy, E. Pavlick, and T. Linzen. Right for the wron g reasons: Diagnosing syntactic
heuristics in natural language inference. In Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics , page 3428–3448, 2019.
[57] J. Michael, A. Holtzman, A. Parrish, A. Mueller, A. Wang , A. Chen, D. Madaan, N. Nangia,
R. Y. Pang, J. Phang, et al. What do NLP researchers believe? R esults of the NLP community
metasurvey, 2022. arXiv:2208.12852.
[58] B. Min, H. Ross, E. Sulem, A. P. B. Veyseh, T. H. Nguyen, O. Sainz, E. Agirre, I. Heinz,
and D. Roth. Recent advances in natural language processing via large pre-trained language
models: A survey, 2021. arXiv:2111.01243.
[59] M. Mitchell. Artiﬁcial intelligence hits the barrier o f meaning. Information, 10(2):51, 2019.
[60] M. W. Morris, T. Menon, and D. R. Ames. Culturally confer red conceptions of agency: A key
to social perception of persons, groups, and other actors. I n Personality and Social Psychology
Review, pages 169–182. Psychology Press, 2003.
[61] G. L. Murphy. On metaphoric representation. Cognition, 60(2):173–204, 1996.
[62] T. Niven and H.-Y. Kao. Probing neural network comprehe nsion of natural language ar-
guments. In Proceedings of the 57th Annual Meeting of the Association fo r Computational
Linguistics, pages 4658–4664, 2019.
[63] A. Norenzayan and R. E. Nisbett. Culture and causal cogn ition. Current Directions in Psy-
chological Science, 9(4):132–135, 2000.
[64] C. Olsson, N. Elhage, N. Nanda, N. Joseph, N. DasSarma, T . Henighan, B. Mann, A. Askell,
Y. Bai, A. Chen, et al. In-context learning and induction hea ds, 2022. arXiv preprint
arXiv:2209.11895.
11

[65] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal,
K. Slama, A. Ray, et al. Training language models to follow in structions with human feedback,
2022. arXiv:2203.02155.
[66] J. Pearl. Theoretical impediments to machine learning with seven sparks from the causal
revolution, 2018. arXiv:1801.04016.
[67] S. T. Piantasodi and F. Hill. Meaning without reference in large language models, 2022.
arXiv:2208.02957.
[68] M. Sadler and N. Regan. Game changer: AlphaZero’s Groundbreaking Chess Strategies and
the Promise of AI . Alkmaar, 2019.
[69] J. Schulman, B. Zoph, C. Kim, J. Hilton, J. Menick, J. Wen g, J. Uribe, L. Fedus, L. Metz,
M. Pokorny, et al. ChatGPT: Optimizing language models for d ialogue, 2022. November 30,
https://openai.com/blog/chatgpt.
[70] T. Sejnowski. Large language models and the reverse Tur ing test, 2022. arXiv:2207.14382.
[71] M. Shanahan. Talking about large language models, 2022 . arXiv:2212.03551.
[72] D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre,
D. Kumaran, T. Graepel, et al. Mastering chess and shogi by se lf-play with a general rein-
forcement learning algorithm, 2017. arXiv:1712.01815.
[73] S. A. Sloman and D. Lagnado. Causality in thought. Annual Review of Psychology, 66:223–247,
2015.
[74] P. Smolensky, R. McCoy, R. Fernandez, M. Goldrick, and J . Gao. Neurocompositional comput-
ing: From the central paradox of cognition to a new generatio n of AI systems. AI Magazine ,
43(3):308–322, 2022.
[75] E. S. Spelke and K. D. Kinzler. Core knowledge. Developmental Science , 10(1):89–96, 2007.
[76] M. Strevens. No understanding without explanation. Studies in History and Philosophy of
Science Part A , 44(3):510–515, 2013.
[77] R. Thoppilan, D. De Freitas, J. Hall, N. Shazeer, A. Kuls hreshtha, H.-T. Cheng, A. Jin,
T. Bos, L. Baker, Y. Du, et al. LaMDA: Language models for dial og applications, 2022.
arXiv:2201.08239.
[78] S. Trott, C. Jones, T. Chang, J. Michaelov, and B. Bergen . Do large language models know
what humans know?, 2022. arXiv:2209.01515.
[79] A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. B owman. GLUE: A multi-task
benchmark and analysis platform for natural language under standing. In Proceedings of the
12

2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting N eural Networks for NLP ,
pages 353–355. Association for Computational Linguistics , 2018.
[80] A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Micha el, F. Hill, O. Levy, and S. R.
Bowman. SuperGLUE: A stickier benchmark for general-purpo se language understanding
systems. In Advances in Neural Information Processing Systems , volume 32, pages 3266–3280,
2019.
[81] S. R. Waxman and S. A. Gelman. Early word-learning entai ls reference, not merely associa-
tions. Trends in Cognitive Sciences , 13(6):258–263, 2009.
[82] J. Wei, Y. Tay, R. Bommasani, C. Raﬀel, B. Zoph, S. Borgeau d, D. Yogatama, M. Bosma,
D. Zhou, D. Metzler, et al. Emergent abilities of large langu age models, 2022. arXiv:2206.07682.
[83] J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, an d D. Zhou. Chain of thought
prompting elicits reasoning in large language models, 2022 . arXiv:2201.11903.
[84] J. Weizenbaum. Computer Power and Human Reason: From Judgment to Calculation . WH
Freeman & Co, 1976.
[85] H. M. Wellman and S. A. Gelman. Cognitive development: F oundational theories of core
domains. Annual Review of Psychology , 43(1):337–375, 1992.
13
