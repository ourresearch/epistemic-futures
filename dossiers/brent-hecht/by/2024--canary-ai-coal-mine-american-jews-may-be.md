---
title: "A Canary in the AI Coal Mine: American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training"
person: brent-hecht
attendance: unconfirmed
section: by
type: conference-paper
year: 2024
date: 2024-05-11
venue: "arXiv (Cornell University)"
authors: "Heila Precel, Allison McDonald, Brent Hecht, Nicholas Vincent"
source_url: https://doi.org/10.1145/3613904.3642749
fulltext_url: https://arxiv.org/pdf/2403.13073
openalex_id: W4393064092
doi: https://doi.org/10.1145/3613904.3642749
oa_status: gold
cited_by_count: 4
retrieved: 2026-08-13
content: full-text
notes: "Full text retrieved from the open-access PDF at https://arxiv.org/pdf/2403.13073 (pdftotext; PDF not stored); full text is the arXiv preprint version of this work"
---

# A Canary in the AI Coal Mine: American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

## Full text

arXiv:2403.13073v1 [cs.CY] 19 Mar 2024

A Canary in the AI Coal Mine: American Jews May Be
Disproportionately Harmed by Intellectual Property
Dispossession in Large Language Model Training
Heila Precel

Allison McDonald

Brent Hecht

Nicholas Vincent

Boston University
Boston, United States

Boston University
Boston, United States

Northwestern University
Evanston, United States

Simon Fraser University
Burnaby, Canada

ABSTRACT

1

Systemic property dispossession from minority groups has often
been carried out in the name of technological progress. In this paper,
we identify evidence that the current paradigm of large language
models (LLMs) likely continues this long history. Examining common LLM training datasets, we find that a disproportionate amount
of content authored by Jewish Americans is used for training without their consent. The degree of over-representation ranges from
around 2x to around 6.5x. Given that LLMs may substitute for the
paid labor of those who produced their training data, they have
the potential to cause even more substantial and disproportionate
economic harm to Jewish Americans in the coming years. This paper focuses on Jewish Americans as a case study, but it is probable
that other minority communities (e.g., Asian Americans, Hindu
Americans) may be similarly affected and, most importantly, the
results should likely be interpreted as a “canary in the coal mine”
that highlights deep structural concerns about the current LLM
paradigm whose harms could soon affect nearly everyone. We discuss the implications of these results for the policymakers thinking
about how to regulate LLMs as well as for those in the AI field who
are working to advance LLMs. Our findings stress the importance
of working together towards alternative LLM paradigms that avoid
both disparate impacts and widespread societal harms.

One of the most prominent critiques of large language models
(LLMs) is that they train on massive amounts of content without the
consent of the authors of that content [8, 59, 73, 91, 98, 103, 109, 124–
126]. This concern is exacerbated by one of the core promises of
LLMs: their ability to use patterns in their training data to substitute
for the paid labor of those who created said data. People in a wide
range of professions (e.g., fiction-writing and journalism) are now
accusing language modeling companies of not only stealing their
content (e.g., novels and news stories), but also of using this very
content to put them out of a job (e.g., [58, 98, 105, 116]). Indeed,
the dominant approach to training LLMs has been called LLMs’
“original sin” [60] and a “property land grab” that is “so brazen
it has unified a wide range of interests” [91]. According to wellknown novelist Margaret Atwood [8], LLMs enable an author such
as herself to be “dispensed with—murdered by my replica...who
needs the cow when the milk’s free?”
Large-scale property dispossession in the name of progress—
whether the property is physical or intellectual—is far from an
unprecedented event, and history teaches us that it often does not
occur uniformly across demographic lines (e.g., [30, 93]). In this
paper, we seek to explore whether the “[intellectual] property land
grab” [91] by LLM companies continues this historical pattern and
disproportionately affects certain groups more than others. The
stakes here are very high: it is not just the right to control what
people can do with their content that is at risk (i.e., intellectual
property dispossession harms); the labor substitution potential of
LLMs means that the ability to pursue one’s chosen profession
may also be seriously affected [1, 16, 39, 130] (i.e., labor substitution
harms).
We focus on property dispossession from American Jews as a
case study in this paper, motivated by 1) the long history of property dispossession—including intellectual property (IP)—suffered by
Jewish populations [5, 10, 84], and 2) the contextual expertise of the
author group, which can be particularly valuable given the sensitive
nature of studies like this one. Importantly, however, this line of
investigation is likely relevant to many other minority groups (e.g.,
Asian Americans, Hindu Americans) and, as we discuss below, far
beyond these groups as well. Model builders’ intentional decision
to not provide public documentation of the data used for training
contributes substantially to the difficulty in studying dispossession
at scale, making a case-study based approach much more tractable
at this time.
The results in this paper are clear and concerning: our findings
indicate that American Jews are likely to be disproportionately
affected by language models’ alleged theft of intellectual property

CCS CONCEPTS
• Social and professional topics → Intellectual property; •
Computing methodologies → Machine learning.

KEYWORDS
large language models, economic impacts, dataset documentation
ACM Reference Format:
Heila Precel, Allison McDonald, Brent Hecht, and Nicholas Vincent. 2024.
A Canary in the AI Coal Mine: American Jews May Be Disproportionately
Harmed by Intellectual Property Dispossession in Large Language Model
Training. In Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI ’24), May 11–16, 2024, Honolulu, HI, USA. ACM, New York,
NY, USA, 17 pages. https://doi.org/10.1145/3613904.3642749
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
CHI ’24, May 11–16, 2024, Honolulu, HI, USA
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0330-0/24/05. . . $15.00
https://doi.org/10.1145/3613904.3642749

INTRODUCTION

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

and the corresponding downstream effects on the value of their
labor. Using inference methods developed in Jewish demographic
literature, we find that content authored by American Jews is substantially over-represented in important LLM training datasets by
between approximately 2x and approximately 6.5x. These findings
raise the possibility that if the current language modeling paradigm
is allowed to continue, the initial wave of economic disruption
could introduce a novel and significant material bias against Jewish
populations.
This paper likely has a number of significant implications for
legal experts, policymakers, researchers, and the tech industry. Perhaps most urgently, our results highlight that any legal finding that
current LLM training practices are allowed under some definition of
“fair use” (or any new law along those lines; see [68] for an overview)
could have a substantial disparate negative impact on American
Jews, and probably other minority groups as well. Critically, our results should also encourage policymakers, funders, and researchers
to shift resources away from the current language model paradigm
and towards promising new approaches that allow for power and
revenue to be distributed to content owners in a fashion that is
more aligned with the value they create for LLM companies. We
provide some discussion of these alternative paradigms below.
The results in this paper also add urgency to calls (e.g., [16]) to focus significantly more research and development resources on LLM
applications that augment or complement human labor and significantly fewer resources on applications that substitute for human
labor. This requires the creation of significant extrinsic incentives
to make it more likely that this occurs (e.g., policy incentives). As
we discuss below, the labor substitution harms highlighted in this
paper can be significantly mitigated if we as an industry are successful in this endeavor. Many researchers think extensive labor
substitution is likely (e.g., [16, 39, 52]) and, importantly, near-total
labor substitution is the explicitly stated goal of key LLM actors
like OpenAI [90]. However, it is possible that through changes in
the sociotechnical landscape of LLMs and the technologies they
power—changes that researchers and practitioners in the HCI community can help drive—some of this family of harms can be averted
and even reversed.
It is important to acknowledge that this paper deals with unusually sensitive issues, the very highlighting of which in a research
paper could cause harm. While we made every attempt to make
evidence-backed decisions to minimize any negative effects to the
Jewish community and others (e.g., from anti-Semitic actors), some
risk could remain. Ultimately, the author group—of which half is
Jewish—estimated that the benefits of highlighting the uncovered
evidence far outweighed the potential harms of publishing it. Additionally, in developing our methodologies, we consulted with
several demographers of Jewish populations, who have extensive
experience handling these challenges in their work.
Finally, before continuing with Related Work, it is useful to
reflect on the title we selected for the paper. It is often said that
when new forms of prejudice emerge against the Jewish population,
they are a “canary in the coal mine” [42, 88] for serious systemic
issues whose harms will soon spread well beyond Jews. Applying
this analogy to the findings in this paper is imperfect in some
ways, e.g., we know of no evidence of the antisemitic intent that
is common when the analogy is typically employed. However, the

Precel et al.

“canary in the coal mine” phrase does capture possibly the most
important property of our results: rather than anything specific
to the American Jewish community, the effects we observe here
must be viewed as an additional flashing-red warning sign for the
foundational flaws in the current LLM paradigm that are already
affecting hundreds of millions of non-Jews as well. Indeed, without
strong action, these harms may extend to nearly all participants
in the economy; for example, researchers are working to use LLM
techniques for robotics in ways that would create similar challenges
for those who earn their living from manual labor [133]. All of
that said, shared harms also means shared solutions: the many
promising alternatives to the current LLM paradigm that are being
explored—changes that need more attention and resources—can
not only remedy issues for American Jews, but can do the same
for the much larger group of people outside the Jewish community
who will otherwise be similarly harmed.

2 BACKGROUND
2.1 Broader Historical Context on Property
Dispossession
There is an extensive literature on the long history of property
dispossession from marginalized groups, which we present here
not to draw a direct comparison but rather to situate the current
dispossession within historical context. One key teaching of this
literature is that the effects of dispossession can be both tremendous and long-lasting. The nearly total dispossession of property
rights—including bodily rights—suffered by African slaves in the
United States led to a wealth gap that has lasted for generations
since slavery ended [29]. The effect of property dispossession on
indigenous peoples around the world is similarly long-lasting [18].
Advocates of the current LLM paradigm argue that nonconsensual training on content is necessary to unlock the significant technological progress manifest in LLMs. The literature on
property dispossession highlights that this type of justification is
common: “progress”, including technological progress, is often a
key part of the stated justification for the seizing of property rights
from marginalized groups. For example, during the English Enclosure movement, large swaths of the poor English population lost
rights to farm on land they had been using for generations. New
agricultural techniques were one stated reason Enclosure policies
were enacted [93]. This justification ignored ways the “technological dividend” from the use of new techniques could be distributed
more equitably to those who had the original property rights [40].
The dispossession of property rights that occurred in Enclosure
led to decades of major riots and civil unrest [74]. An interesting precedent also comes from the story of Henrietta Lacks, an
African-American woman whose cells helped create countless new
innovations in healthcare but were acquired and used without her
knowledge [30]. Her descendants recently reached a “groundbreaking” [92] settlement with a major biotechnology company over
their claims that the company was “unjustly enriched” by using her
cells without her consent, an argument that some have made about
the LLM industry [103].
Mass property dispossession from Jews has occurred for centuries. Jews in most of Eastern and Central Europe were forbidden
from owning land for much of the second millennium [118], for

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

example. Similarly, the Expulsion of Jews from Spain in 1492 was
preceded by the forced liquidation of all Jewish property in that
region (at significantly depressed values) [10]. Unsurprisingly, the
Nazi government in Europe in the 1930s and 1940s coupled its
policies that led to the death of nearly half the Jewish population [85] with policies that seized nearly all Jewish property in
Nazi-controlled territories [84]. These policies, which are grouped
under the label “Aryanization” [84], forced Jews to either sell property at greatly reduced prices or, beginning in 1938, have it seized
by the government.
The Nazi dispossession of property rights from Jews was not
limited to physical property: the government also seized Jewish intellectual property. For example, in 1939, all Jews in Nazi-controlled
territories had to change their middle names to “Israel” or “Sara” to
increase the visibility of their Jewish identities, which had the effect
of making it very difficult to renew (or apply for) any IP protections.
This led to the complete reproduction of Jewish works without the
consent of their authors [5] and even to Jewish scientists leaving
their names off of patents so that the patents would be granted [11].
Of course, no direct comparison can be made between events
like the Holocaust and the IP dispossession we discuss in this paper.
Indeed, we are aware of no evidence that dispossession by LLM
developers intends to target the affected parties. However, the IP
dispossession we identify in this paper is not without historical
parallels and this context is necessary to understand the lasting
effects that IP dispossession has had on affected groups throughout
history.

2.2

LLMs and Economic Harms

For people who create content, current LLMs create two separate
but compounding economic harms: 1) dispossession of intellectual
property rights, and 2) the use of the dispossessed IP to substitute for
their labor. Below, we discuss research that highlights the presence
and significance of both of these harms. We highlight how it is
useful to understand these harms separately, and while one may
come to dominate in material outcomes (e.g., substitution could
be the primary concern in a world in which LLMs act as laborreplacing technologies), both require addressing.
2.2.1 IP Dispossession Harms. It is now public knowledge that
all prominent large language models have been trained on enormous amounts of digital content—both natively digital content (e.g.,
Wikipedia and forum comments) and digitized documents (e.g., novels and scientific publications). With few exceptions, this is done
without the consent of the creators of that content and without
any form of compensation going to those creators [91]. This is true
both for language models that generate text (e.g., OpenAI’s ChatGPT [96] and Meta’s LLaMA [46]) and those that generate images
(e.g., Stable Diffusion [59, 122]).
Those who make content for a living are beginning to take significant action against model builders in an attempt to reclaim some
of the rights to their IP. OpenAI, Meta, and other companies that
build and use LLMs are subject to a large and growing number of
lawsuits, an effort that has been led in part by prominent Jewish
content creators such as Michael Chabon [46] and Sarah Silverman [32]. Major content-creating institutions are also beginning
to sue model builders; most notably, The New York Times has sued

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

Microsoft and OpenAI [47, 96]. Legal action is far from the only
avenue being used. The Authors’ Guild and many others [48] are
working to enact new legislation in many parts of the world to
protect creator rights, and content owners are taking direct action
to prevent their content from being used without their consent.
For example, most prominent news websites now forbid model
builders from accessing their content by editing their robots.txt
files [15, 96].
There is much legal debate about how these lawsuits will be
decided and in which jurisdictions. Similarly, there has been significant reporting about new laws drafted around the world to regulate
language models. We discuss the implications of the results of our
study for the legal debate and policy conversations in Discussion.
It is important to note here, however, that courts and governments
throughout history have blessed mass property dispossessions that
are now widely considered moral abominations and have had significant negative long-term implications for both the dispossessors
and the dispossessed populations. This is true of nearly all the
events discussed above. As we are concerned with IP dispossession
broadly, we do not focus on any specific legal jurisdiction’s interpretation of what constitutes a violation of IP laws—rather, we are
interested in potential harms from content use without consent.
We hope to contribute to the evolving conversations around which
legal doctrine(s), if any, should be used to prevent such harms.
This broad form of dispossession deprives creators of the right
to choose which systems and organizations their outputs bolster,
and potentially prevents their ability to receive compensation for
their works. While highly related, this potential harm is distinct
from the possibility that AI systems will lower the demand for
future labor, which we address in the next subsection. In simple
economics terms, we can think of the difference as creators losing
expected compensation from content already created, or having
their compensation redirected to organizations with which they
are unaffiliated, versus creators losing new labor opportunities in
the future. This new dispossession represents a violation of the
implicit social contract that motivated people to invest time and
money in training themselves; those who undertook training in
a pre-LLM era had different expectations about how their work
might be utilized.
2.2.2 Labor Substitution Harms. The use of one’s creations without consent and without the ability to extract value from this use
is a major harm in and of itself. However, the way that LLMs use
content makes this harm potentially exponentially larger: a key
stated reason for developing LLMs is so the models can learn from
the content on which they are trained to “do more and more of the
work” of content creators and cause “the price of many kinds of
labor to fall towards zero” [4]. Put another way, a core value proposition of large language models is to substitute for the paid labor of
the people who create their training content. This means that the
creators of content used in the model are not only fighting to get
their share of the value their content is creating—they are fighting
for the ability to continue working in their profession of choice
at all. Many American Jews (and members of other populations
that have suffered property dispossession) have grown up with the
phrase “They can’t take your education away from you.” In these
ways, LLMs might very much do this, or at least may take away

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

the ability to earn a living from an education (and other training
and experience).
While the degree of labor substitution from LLMs that will occur remains unclear, there is a growing line of work attempting to
forecast the impacts of LLMs on various labor markets. A key conclusion of this work is that professions that have contributed a lot
of training content to the models may be much more affected than
those that have not. For example, Eloundou et al. found that workers with more formal education such as lawyers, graphic designers,
and database administrators are more exposed to LLMs, which is in
line with similar work forecasting the impact of ChatGPT on the
labor market [132].

2.3

Dataset Documentation

Our work aims to contribute to the ongoing discussion about data
documentation, and to specifically highlight how current practices
within the AI research community may be obfuscating potential
harms. Many of the methodological challenges (though not all of
them) presented in this paper could have been avoided with better
dataset documentation, a practice that scholars have called for many
times over the years [44, 94]. The field of dataset documentation
provides important context for our methodological choices. Here,
we give some context on this research area.
Broader interest in dataset documentation was highly influenced
by work on “Datasheets for Datasets” [44], which proposed that
every dataset be accompanied by a datasheet. This would facilitate greater transparency and enable practitioners to select more
appropriate datasets for their tasks. The Datasheets concept has
led to uptake in documentation practices (shaping, for instance,
the Dataset track at NeurIPS1 ). In practice, the ML community has
taken tangible steps to improve data documentation for some kinds
of contributions.
However, in the space of language modeling, the massive scale
(“web-scale”) of data—and the choice by the ML community to
deprioritze documenting this web-scale data before using it—is a
major barrier to documentation, a concern that was highlighted as
early as 2021 [12]. In short, web-scale data is simply expensive and
challenging to retroactively document, and typically lacks much in
the way of structured data. As a result, much of the LLM industry
suffers from “documentation debt”, making it difficult to know
even basic information about how a model was trained, e.g., what
datasets were used, who authored an entry in a given dataset, etc.
It is important to note that this debt is intentional and explicitly so;
model builders purposely avoid releasing information about their
training data [89, 120].
Still, efforts to document data relevant to generative AI have been
undertaken. One such dataset that is open, documented in some
dimensions, and widely used for LLM training is the The Pile [43].
This is the dataset we focused on studying, in part because the
prevailing documentation practices left us few other choices. Prior
work has attempted to document the BookCorpus dataset, touching on topics like copyright and acknowledging the authors that
underlie the training data [9]. With the purpose of identifying the
1 See, e.g., information about the 2023 track at https://nips.cc/Conferences/2023/

CallForDatasetsBenchmarks.

Precel et al.

authors whose work was used in training Meta’s LLaMA, a journalist recently processed and identified over 170,000 books contained
in the Books3 dataset, finding that the majority were still under
copyright and were published in the last two decades [100]. There
is also ongoing work aimed at urgently remedying the dataset documentation crisis in the context of LLMs. For instance, “The Data
Provenance Project” has compiled metadata on popular LLM training datasets [75], revealing a large amount of prevailing ambiguity
and the need for policy guidance.
The lack of consistent documentation in web-scale training
datasets is especially relevant to this research because author attribution is necessary for estimating group-level dispossession. As a
result, we were forced to exclude some datasets (most saliently, all
web crawl data) from our analysis.

2.4

Contributor Attribution

2.4.1 Challenges of Ethnic Identification. Compounding the data
documentation issue for this research is the fundamental difficulty of ethnic identification, especially for small ethnic and ethnoreligious populations. Ethnic boundaries are often fluid and hard to
define, and are only sometimes captured in demographic surveys.
Assigning labels to individuals without directly surveying them
is itself fraught and will inevitably miscategorize some members
of a population, but a true survey of all group members is prohibitively expensive in both time and resources. Yet, it is critical for
communities to understand the needs and challenges facing their
members, and formal population measurements can be the gateway
to official recognition and institutional support [78]. As a result,
groups have developed a variety of alternate strategies for counting
and surveying their members.
In this paper, we focus on the American Jewish community,
a small ethnoreligious group (about 1.8–2.4% of the U.S. population [22, 106, 107]) with a robust literature of community studies at
local and federal levels (e.g., [21, 27, 57, 77, 111, 114]). These studies
are designed to capture the size, character, demographic profile,
and needs of U.S. Jews and synthesize findings into actionable insights for the Jewish community [7]. However, the U.S. Census
doesn’t collect information on religion and the Jewish community
is small enough to make identifying a representative sample via
Random Digit Dialing (RDD) or other common random surveying
approaches extremely costly [107]. As a result, Jewish demographic
studies have relied on probabilistic methods to identify a representative sample and extrapolate findings to communities at large.2
2.4.2 Distinctive Jewish Names (DJNs). One method developed by
the American Jewish community for in-group surveying is the
Distinctive Jewish Names (DJN) frame. In this method, lists of potential survey respondents (whether via landline RDD, cellphone
dialing, or otherwise) are filtered to candidates with a surname
that is distinctively Jewish: that is, both common in the Jewish
community and largely unique to Jews. This increases the chances
that a respondent will be Jewish, thus potentially lowering survey
costs. The DJN frame has a rich history: it was initially proposed
2 Defining membership in the Jewish community is a complex topic, discussion of
which is beyond the scope of this paper. We rely on definitions from Brandeis’s AJPP
Report [107], the AJYB population counts [114], and Pew Research Center’s Jewish
American studies [21, 22]. For an overview of how these definitions were developed,
see pages 3-6 of [107].

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

in the 1940s by Kohs [57] and has since been used in numerous
community studies through to the present day [114]. In some cases,
DJN-based lists were used alongside other sampling methods, primarily RDD; in others, they were the primary or only sampling
frame. Some studies were designed to actually survey community
members while others estimated a Jewish population count in a
particular context based on DJNs in membership lists or phone
books. See the “United States Jewish Population” chapters of the
American Jewish Yearbook series for a detailed account of such
studies [114].
In this study, we use DJNs as our primary form of analysis. We
estimate the size of a Jewish population from a total list of names,
using content authors identified from model training data as our
population. Here, we provide a brief overview of our rationale
before elaborating on the method itself in Section 3. For a more detailed overview of the literature on DJNs and the frame’s limitations,
see Appendix A.4.
In general, a DJN-only approach is recommended for identifying
the size of a Jewish population a) only as a rough estimate, and b)
only when one already has prior knowledge of Jewish population
estimates for the area of interest. Both of these are true for our
study: we are reporting order of magnitude estimates at the national
scale, for which we have a number of high-authority population
estimates [22, 107].
Additionally, the DJN-only approach to population estimation
assumes that Jews in the sample with DJNs are representative of
those without; in this case, that Jews with DJNs are no more likely
than Jews without DJNs to produce content that appears in LLM
datasets. There is some prior evidence to suggest that DJN samples do not show significant differences in income [26, 112] and
education [57]—two potential proxies for IP generation—as compared to the general Jewish population. The greatest disparities are
around Jewish religious knowledge and engagement with Jewish
life. Absent a compelling hypothesis for why DJN samples would
significantly differ from the general population on occupation or
writing output, one can have reasonable confidence that our estimates provide order-of-magnitude bounds.
Ultimately, the research in this paper assumes that characterizing the nature of IP dispossession by LLMs with respect to potential
impact on the Jewish community is important enough to use the
best method available, even if it won’t provide a highly-precise
point estimate. Our analysis accounts for this by making reasonable assumptions that lead to upper and lower bound estimates
with robustness checks to ensure order-of-magnitude correctness.
Details on these assumptions are in Section 3.2.

allow a small base model, trained on either public domain or fullconsent content [82] and combined with document retrieval techniques at runtime to dynamically generate output (e.g., [71]). This
approach allows enough transparency and control for individual
content owners to be able to make decisions about where they want
their data to end up, and bargain for specific contracts that pass
value back to content owners based on usage or related metrics.
Recent work has begun to explore exactly how markets operated
with carefully designed sharing incentives (e.g., “data consortia” in
which multiple organizations pool their content together) might
work in practice [19, 129]. Scaling up support for this kind of data
sharing is another way to shift LLMs towards sharing some portion
of their economic winnings with content creators. Finding ways
to make participation appealing to LLM developers could be an
effective way to work towards an alternative LLM data paradigm.
Another idea that has been the subject of early discussions about
the economic impacts of AI and automation is to implement some
kind of broad “data dividend” [123], through which the profits from
AI technologies are shared with training data creators. A criticism
against this idea is that a very broad remuneration system might
hurt incentives for the creation of new content (compared to e.g.
new content markets). However, this option could be complementary to other approaches: because many groups have content and IP
in the training sets for web-scale models, there is a strong argument
for at least some degree of broad remuneration.
As noted above, the individual viability of these alternative
paradigms may change suddenly if certain legal decisions are
reached (e.g., if “fair use”-based training is broadly supported, or
broadly banned) or if new regulations are passed. Thus, navigating the sea of possible paradigms will require the consideration of
all possible options, and ideally will include experiments with the
proposals listed here and more.

3

New LLM Paradigms

Researchers have begun to explore new LLM paradigms that seek
to minimize the ethical, legal, and other risks of the current approach which depends on uncompensated access to vast amounts
of content used without the owner’s consent. These explorations
are a burgeoning area of research.
One promising direction emerges out of the retrieval augmentation and enhancement literature (e.g., [131]). These techniques

METHODS

The key methodological challenge of this research is figuring out
how a group concerned about disproportionate IP dispossession and
labor substitution in the wake of language models might go about
quantifying the costs it is likely to face. Addressing this question
as it pertains to Jewish Americans involves dealing with a large
amount of unavoidable noise.
In this section, we discuss how we sought to reduce the amount
of noise in our estimates to a minimum. We describe our methods
in two parts: first, we describe the LLM training datasets we use in
our analysis and the process we use to collect metadata; and second,
we present our strategy for assessing Jewish authorship.

3.1
2.5

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

Datasets

Here, we describe the datasets we used, starting with the rationale
underlying dataset selection.
We wanted to analyze datasets that would give a reasonable
estimate of the overall relative magnitude of intellectual property
dispossession faced by Jewish authors. We assume that an IP dispossession event occurs each time an author’s work is included in
a training set without that author’s explicit consent. For this analysis, a single work equals a single document (e.g., scientific paper,
law paper, code repository, book) and works with n authors count

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

for n IP dispossession events. We note that, as discussed in Section 2.2.1, dispossession is separate from (but related to) copyright,
and copyright practices vary between the types of documents.
If we had metadata describing the author(s) of every document in
a web-scale training dataset and the group identifications of those
authors, we could very quickly identify which groups are most
impacted. For instance, if a firm were able to scrape the entire web
and performed no filtering, the degree of disparate impact would
map directly to group-level differences in web content creation.
Whichever group published the most documents on the web would
see the most IP dispossession in absolute and relative terms. However, in practice the entire web is not used directly for training (see,
e.g., [89]). Major firms use various filtering processes to select only
some works for use in training data. The processes used by most
major firms are currently proprietary [89], creating a significant
barrier to analyses like those in this paper.
However, there exist “open” LLMs that, because they release
their training data, implicitly reveal their filtering methods. One
very popular dataset used by these LLMs—and the one we analyze
in this research—is the Pile [43], curated by EleutherAI. The Pile
includes a variety of high-quality data sources that are largely
associated with specific professions and institutionalized platforms
(e.g., ArXiv, GitHub, FreeLaw). Many of these include some level of
author attribution for individual works.
Open models, such as those trained using the Pile, are seeing
substantial gains and catching up in performance with private
offerings (see, e.g., comparison between GPT-NeoX-20B and GPT-3
[14], as well as the performance of the LLama models [120]). This
suggests that the data quality filtering and weighting used in the
Pile is somewhat comparable to private filtering strategies, and that
by studying this heuristically filtered (i.e., carefully selected) data,
we can make claims that generalize reasonably well to LLMs as a
class of technology. In other words, we expect the general practice
of studying and documenting “open” web-scale training data to
provide insights that apply to commercial LLM products. While it
is unknown if Meta’s “open” Llama 2 model directly used the Pile
as details about pretraining are omitted [120], it seems likely (the
original LLaMA paper did report using The Pile [119]).
We focused in our analysis on high quality subsets of the Pile
that clearly map to content that is unambiguously composed of
individual pieces of literary, scientific, artistic, and/or professional
works that are typically subject to intellectual property governance
and norms. By estimating the number of (document × author) pairs
present in the Pile, we get a general assessment of the magnitude of
IP dispossession and potential labor substitution faced by authors
whose works are in the Pile.
3.1.1 Dataset Selection and Curation. Below, we describe the specific datasets from the Pile that we studied in order to work towards
an estimate of the relative exposure of Jewish Americans to IP dispossession. We also describe some of the dataset-specific processing
steps we followed, as well as our data processing pipeline at a high
level.
The Pile consists of a set of plaintext documents derived from
a set of datasets with minimal additional processing. At time
of writing, it is hosted by EleutherAI [38], and many of the
subsets are also available via original sources. For our analysis,

Precel et al.

we selected five Pile components ordered by weight, which the
Pile documentation defines as “percentage of bytes in the final
dataset occupied by each dataset” [43]: PubMed Central, Books3,
ArXiv, GitHub, and FreeLaw. We excluded web scrape components
(Pile-CC and OpenWebText2) because we were unable to identify
usable author metadata from web scrape data and re-linking
this metadata would be prohibitively difficult. Overall, the five
components used in our analysis total 49.14% of the final Pile
dataset by weight [43]. We processed each of the datasets as follows:
(1) PubMed Central. We downloaded the PubMed Open
Access Subset directly from NCBI [23]. We used the June
2023 baseline bulk files for our analysis and PubMed
Parser [2] to parse metadata (including author surname) for
each article dropping 5 unreadable files (out of 3,529,109
total).
(2) Books3. We obtained the Books3 metadata from the website
of the creator of the Books3 dataset [99]. The json file
contained fields such as title, authors, publication details,
and description. Any errors in the author name field will
result in an undercount of Jewish authors, as mislabeled
documents will still be included in the denominator, regardless of whether the authors have DJNs. It is important to
note that Books3 is a particularly controversial component
of the Pile; large model builders are currently being sued by
book authors for their use of Books3 (e.g., [103]).
(3) ArXiv We downloaded ArXiv metadata from the official
ArXiv Kaggle dataset maintained by Cornell University [24].
Data was downloaded on July 23rd, 2023. We parsed author
names using Clement et al.’s ArXiv data tools [24, 25].
(4) GitHub We downloaded the list of GitHub repositories
used in the Pile from EleutherAI’s GitHub Downloader [37]
and used the GitHub API [45] to collect author names for
a uniformly distributed random sample of ∼5% (9,980) of
repositories. We used a random sample because limitations
set by the GitHub API prevented us from downloading data
for all repositories. The “Name” field is often unpopulated
on GitHub profiles, and even when populated is not
standardized. We parsed this field by selecting the most
commonly occurring pattern (<First Name> <Last Name>).
(5) FreeLaw We downloaded FreeLaw’s CourtListener Opinion
and People datasets from FreeLaw’s bulk data files [28] on
May 31, 2023. We joined these datasets based on the Author
ID column and filtered out opinions with no authors.

3.2

Assessing Jewish Authorship

Here, we describe the process we used to identify Jewish authors in
the datasets described above and produce an estimate of the relative
magnitude of IP dispossession experienced by Jewish Americans.
3.2.1 Name Classification. The DJN list we used for this analysis is
a 35-name list that has been used in studies from the 1940s until the
present day with very few changes, and has consistently maintained

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

a relative proportion of roughly ∼10–12% of Jews with DJNs to Jews
as a whole in large American Jewish communities [51, 56, 111]. It
was also designed to have very high precision: i.e., people with
these surnames are highly likely to be Jewish. See Section 2.4.2 for
additional details on these numbers.

3.2.2 Data Processing Procedure. We conducted several levels of
additional processing that culminated in calculating an estimated
percent Jewish authorship via a DJN-based frame. At a high level,
our data processing consisted of five steps. We follow these steps
for each of our five Pile subsets.
(1) Extract author names
(2) Match DJNs to (document × name) pairs and calculate percentage of pairs with DJNs
(3) Adjust estimated percentage to account for non-Jews with
DJNs
(4) Adjust estimated percentage to account for Jews without
DJNs
(5) Estimate an expected percentage of U.S. Jewish authors per
dataset (i.e., the number we would expect to see if U.S. Jews
were proportionally represented) and compare it to the observed percentage
Below, we explain each of these steps in more detail.
Extract author names. First, we attempted to extract the authors of each document in each dataset to create a list of (document
× name) pairs. Using (document × name) as our unit of measurement allows us to center authors as those experiencing harm: each
pair represents one instance of a given author’s work being used
in LLM training data.
Match DJNs to (document × name) pairs and calculate
percentage of pairs with DJNs. We use our DJN list as a filter on
author names to produce a subset of DJN-matched documents. We
calculate the percentage of resulting (document × name) pairs for
which the name is a DJN.
Adjust estimated percentage to account for non-Jews with
DJNs. To account for the potential that DJN matching may identify some people who are not Jewish, we rely on false positive
estimates from Himmelfarb and colleagues [57] (“about 90–92% of
these names are Jewish”), Rosenwaike’s analysis of leading Jewish
surnames, which includes estimates of 76.6–95.1% (m=88.7%) precision for 15 of the 35 names [102], and Phillips’ 91.8% Boston-area
estimate [97].
Because these are all approximations, we use a range of 80–
90% for our analysis. In other words: if our method found 1000
(document × name) pairs that matched DJNs, we assumed this
represented between 800-900 Jewish authors.
Adjust estimated percentage to account for Jews without
DJNs. For this step, we again refer to [57, 67, 97], which estimate
that Jews with names from the DJN list we used comprise ∼10%–
12% of the U.S. Jewish population. We validated this number by
calculating the percentage of people included in the 2010 U.S. census
[20] with one of the DJNs, accounting for false positives as above,

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

and comparing it to estimates of the Jewish U.S. population in
2010 [21, 106].3
We used the resulting figure of 9.15–11.18% for our analysis.
Following from the above example, if our method finds 1000 DJN
pairs (adjusted in step four to a range of 800-900 Jewish authors),
this means we’d extrapolate in step four to a lower bound of 800 ∗
1
0.1118 = 7156 Jewish authors total.
We note that both of these adjustment steps simply involve multiplying DJN percentage values, so their order does not matter. The
ability to perform these adjustment steps with only multiplication
rests on two distributional assumptions:
• That the distribution of names among Jewish Americans
who contributed to LLM training data is roughly the same as
the population of Himmelfarb et al. [57] and Rosenwaike’s
[102] respective studies.
• That there is no difference in job category representation and
propensity to contribute IP to LLM training data between
Jewish Americans with DJNs and those without (i.e., for each
DJN document-name pair, there is a proportionate number
of document-name pairs that would be attributable to Jewish
Americans without DJNs upon deep investigation).
Estimate an expected percentage of U.S. Jewish authors per
dataset. Finally, the fifth step is to contextualize these estimated
percentages in terms of relative dispossession magnitude. We want
to know how the observed amount of IP from Jewish American authors compares to the expected amount of IP from Jewish American
authors if LLM operators were to representatively sample works
from the whole population. Because we focus here on the relative
representation of Jewish American authors, we introduce two new
factors we must account for: changing demographics over time and
how much data in each dataset comes from American authors.
Some of the datasets we investigate represent content that
was produced over many decades. In Appendix A.3, we explored
whether our estimates would change if we accounted for changes in
the Jewish population over time. We tested this using FreeLaw—the
dataset with by far the largest time window—and found minimal
impact on our results.
To account for country-level distribution of training data, we
estimated the percentage of documents from each dataset published
in the U.S. and account for this in calculating our “expected percentage” of U.S. Jewish content. One can think of these numbers as
checking how overrepresented U.S. authors might be in general in
order to correctly calculate the percentage of American Jews.
• Free Law: 100% published in the U.S., as CourtListener only
indexes U.S. opinions.
• Books3: We do not have data on what percent of Books3
is international. As a result, we act as if 100% of the dataset
were published in the U.S. to intentionally use a conservative
lower-bound estimate of the actual figure, even at the top
end of our ranges.
• GitHub: 24.6% published in the U.S., based on data from
[127].
3We use the following equation, with a precision of 85% and a Jewish population of
# of DJNs in the population ∗ precision
1.8-2.2%: U.S. population ∗ % of Jews in the U.S.

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

Precel et al.

• PubMed Central: 28.6% published in the U.S., based on our
own estimation (details in Appendix A.2.1).
• ArXiv: 27.3% published in the U.S., based on our own estimation (details in Appendix A.2.2).

will continue to happen until the broader LLM community takes
measures to change the approaches in their work.

We note that there is another source of uncertainty relating to
geography: some of the authors with DJNs could be non-American
Jewish authors. We don’t expect this to change our results substantially because we expect surname distributions and spellings to be
different in other countries, and around 40% of the world Jewish
population lives in the U.S.

As described above, our method required us to make several careful
assumptions in order to obtain reasonable, bounded estimations for
the proportion of Jewish Americans in each of these datasets. We
note that these estimation approaches are somewhat atypical in the
HCI community, which often operates with better documented data.
When deciding to do this work, we took inspiration from the carbon
impact estimation research literature, which also operates in a very
high-stakes domain and has to use a wide variety of estimation
techniques with large informal error bounds [117]. That literature
has shown that if the research question is important enough, estimates with somewhat wide ranges and important qualifiers can
greatly assist with decision-making towards critical goals [117].

3.3

Ethical Considerations and Broader Impacts

The approaches we use in this work—and indeed the choice to
conduct the research at all—were carefully weighed against the
methodological challenges and ethical questions of doing so. Specifically, many of the methodological choices above were designed
in part to minimize potential harm to the Jewish community and
other stakeholders.
First, we considered the risks and challenges of labeling authors
as Jewish. Identity inference from attributes like names is not new,
but it is controversial [35]. One area with significant prior work
and critique is the realm of gender: multiple studies in HCI have
documented the harms of gender detection and recognition systems, from individual harms of misgendering [49] to societal harms
from operationalizing reductive and exclusionary definitions of
gender [61]. As in our study, it is not always possible to get affirmative self-identification for attributes; yet knowing the demographic
distribution in a dataset can be a critical aspect of evaluating the
impact of systems.
We took a number of actions to mitigate common risks in identity
inference. The list of DJNs and other methodological approaches we
used were selected in consultation with Jewish demographers, who
are experts at navigating the fraught ethical choices surrounding
the inference of Jewish identity. One alternative approach we considered but ultimately rejected was deploying a large-scale survey
to all of the authors of works in the Pile we could identify to inquire as to their claimed ethno-religious identity. However, surveys
like these targeting the Jewish population are known to be very
difficult to execute due to the small size of the Jewish population.
Also, deploying a survey asking about Jewish identity of course has
its own ethical considerations, and even if successful, would not
remove the significant noise present due to the LLM community’s
poor documentation practices.
Additionally, as we are attempting to calculate the proportion
of Jewish authors in these datasets, our method does not require
that any specific author be labeled Jewish with 100% accuracy, thus
minimizing the harm of misclassifying specific individuals (either
as Jewish or as non-Jewish).
The second major ethical consideration for our study was the
risk that our findings would be used to harm the Jewish community should they be leveraged by anti-Semitic actors, which we
further discuss in Appendix A.4. Ultimately, we decided that the
consequences of not doing the work were greater than the potential harms, a decision-making process that was led by the Jewish
members of the authorship group. We stress that IP dispossession
is happening regardless of how well it is documented, and that it

3.4

4

Methodological Limitations

RESULTS

Using the method described above, we calculated relative dispossession magnitude—a ratio of observed to expected numbers of
documents written by U.S. Jews in the dataset.
Relative Dispossession Magnitude =
% U.S.-Jewish authored documents in dataset
Expected % U.S.-Jewish authored documents in dataset
We first calculated lower and upper bounds for the relative dispossession magnitude of each individual dataset based on the lowerbound and upper-bound estimation techniques discussed above.
Then, we calculated two averages: a total relative dispossession
magnitude (the mean across datasets with each dataset weighted
equally) and a weighted total relative dispossession magnitude (the
mean across datasets with each dataset weighted by number of
documents × document size). In other words, weighted total relative dispossession magnitude reflects the total overrepresentation
of American Jewish authorship accounting for the size of each
individual dataset and the length of its average documents.
Looking at the first column in Table 1 (which is not limited to
U.S. documents), we see that the percent of (document × name)
pairs whose authors have DJNs—who represent a small fraction of
Jewish authors—is already greater in almost every case than the
percent of Jews in the world (0.19–0.28%) [33, 86]. Although we have
less certainty about world statistics as many of our variables are
designed to focus on the U.S. Jewish population, this is strong early
support for the hypothesis that American Jews are over-represented
in these datasets and suggests that this is true of Jewish authorship
globally.
In the second column, we have lower and upper bounds for
the percent of IP dispossession events—(document × name) pairs—
from U.S. Jewish authorship. As noted above, we consider a range of
parameter values to account for some of the uncertainty introduced
by our methods. Our estimate here is parameterized by precision
(how unique are the DJNs to the Jewish population) and coverage
(how much of the Jewish population do the DJNs represent). Our
lower bound uses lowest precision / highest coverage estimates;
our upper bound uses highest precision / lowest coverage.

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

0.19
0.98
0.28
0.29
0.93

% IP with
U.S. Jewish
author
1.39-1.91
7.01-9.64
2.01-2.77
2.08-2.86
6.65-9.14

% Expected
IP with U.S.
Jewish author
0.5-0.7
1.8-2.4
0.5-0.7
0.4-0.6
1.8-2.4

0.54
0.37

3.83-5.26
2.63-3.61

1.0-1.3
0.8-1.0

Dataset

% IP with
DJN author

PubMed Central
Books3
ArXiv
GitHub
FreeLaw
Total
Weighted Total

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

Relative Dispossession
Magnitude
2.02-3.71 X
2.92-5.36 X
3.07-5.63 X
3.53-6.46 X
2.77-5.08 X
2.86-5.25 X
2.46-4.51 X

Table 1: From left to right: (1) percentage of dataset (documents × authors) with DJNs; (2) estimated percentage of dataset
(documents × authors) with U.S. Jewish authors; (3) expected percentage of dataset (documents × authors) with U.S. Jewish
authors; (4) relative dispossession magnitude.

Table 2 shows the parameters we use for each estimate: precision
ranges from 80% to 90%, coverage from 9.15–11.18%, and percent
of the U.S. that is Jewish from 1.8%–2.4% (see Section 3.2.2 for
details). Critically, these ranges are not uncertainty ranges: they are
assumption-based and indicate a range of reasonable possibilities
for a parameter in our equation. Our lower bound is the lowest
possible estimate given our assumptions; our upper bound is the
highest. In Appendix A.1, we include a robustness check in which
we consider the most extreme possibilities for each parameter that
would still demonstrate a relative dispossession magnitude > 1.
We found that U.S. Jewish authorship ranged, per dataset, between 1.39–9.64%. As expected, the more U.S.-centric sources see
higher percentages of U.S. Jewish-authored documents (6.7–9.1%
for FreeLaw; 7.0–9.64% for Books3) while less U.S.-centric sources
see lower percentages (PubMed Central: 1.4–1.9%, ArXiv: 2.0–2.8%,
GitHub: 2.1–2.9%).
Parameter
% precision of DJNs
% coverage of DJNs
% of US population
that is Jewish

Lower bound
80%
11.18%
2.4%

Upper bound
90%
9.15%
1.8%

Table 2: Parameters used in estimation calculation. From
left to right: (1) name of parameter; (2) value used for lower
bound estimations in Table 1; (3) value used for upper bound
estimations in Table 1.

The final column in Table 1 shows the amount of dispossession
experienced by U.S. Jewish authors relative to U.S. content producers more generally, i.e., the numbers we are most interested in
for the purposes of this paper. The results in this column clearly
show a structural bias against U.S. Jews across all datasets: the lowest lower-bound dispossession magnitude we observed was 2.02,
meaning that U.S. Jewish suffer double the dispossession of the U.S.
population as a whole at the very minimum (across the datasets we
considered). The highest upper-bound magnitude was 6.46, which
corresponds to over six times more dispossession than the general

population. This table presents a strong argument that, at least
with respect to U.S. content, LLMs rely disproportionately on Jewish American intellectual property obtained without the creator’s
consent, and do so extensively.

5

DISCUSSION

Our results indicate there is very real risk that Jewish Americans
may see substantial and disproportionate economic harms as LLMbased technologies are deployed more widely. Below, we discuss the
implications of these results for a number of key discussions happening around AI law, regulation, and practice. We also highlight
key areas of future work.

5.1

Implications for Legal and Policy
Discussions

The findings above have important implications for the rapidlydeveloping legal and policy debates surrounding language models.
The introduction of new structural material biases against minorities has not been broadly considered in these debates, and our
results suggest they very much should be.
With regards to developments in the legal sphere, many dimensions of LLM training practices are being examined by courts in
different jurisdictions, e.g., “fair use,” privacy rights, publicity rights,
labor law, contract law and many others [69, 104, 110]. However,
our results suggest that disparate material impact suffered by protected groups is another dimension that needs to be explored. It is
clear, for instance, that any U.S. decision that current LLM training
practices constitute “fair use” could introduce a significant new
structural bias that disproportionately harms American Jews—and
likely other minority groups—in the short term. As discussed in the
Introduction, should these disparate harms play out, they are likely
to represent a “first wave” of harms, with almost all participants in
the economy eventually being affected.
The evidence above also suggests that policymakers should more
deeply consider structural bias against minority groups in the discussions about language models. Lawmakers in the United States
considering encoding current LLM content usage into law must
wrestle with the new systemic biases against American Jews they

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

would be creating. Similarly, those working on efforts to strengthen
the rights of content owners and producers (e.g., [63]) may consider our findings to be an additional reason to push forward in
that direction. Our results also highlight the importance of agency
decision-makers, regulators, and policymakers shifting the growing amounts of public funding for LLM research towards the many
promising approaches that do not create the structural biases of
current approaches. There are a number of other reasons that have
been identified in the literature to do so, e.g., the potential of the
current paradigm to substantially decrease the material welfare of
the general public [4, 16], which likely contradicts the mandates of
many national research funding agencies.
This study represents a first step towards understanding grouplevel contributions to training data. Policymakers will likely want to
consider additional analyses that extend this line of thinking. This
could involve adapting similar methods to those we employed here,
perhaps augmented with recent work on detecting pre-training data
[115] or incorporating new methods for estimating racial disparities
using surnames [79], though this may require support from dataset
creators and curators.

5.2

Implications for Developers and
Researchers of AI Systems

At the highest level, the results above add to the growing list of
reasons AI developers and researchers should consider shifting
resources and attention away from the current LLM paradigm and
towards both 1) LLM systems and techniques that only train on
content with consent, and 2) mitigating the negative impacts that
previous decision-making in the LLM industry may have caused.
This paper highlights that those simply seeking to advance the current paradigm must reckon with the new structural biases against
minority groups to which they may be contributing. They must also
know that they are asking the Jewish community (and likely other
minority communities as well) to make disproportionate sacrifices
for the benefit of their mission. This is especially true for organizations like OpenAI, whose non-profit mandate requires that they
build AI for the public good. More generally, like a number of other
recent papers and opinion pieces [8, 91], this paper highlights that
if we—as design researchers and practitioners—do not make significant changes to our approach, even if the community is successful
at building something like an artificial general intelligence, such
an accomplishment risks being forever tarnished with legitimacy
issues originating from how it learned what it knows.

5.3

Implications for Jewish Americans Who
Author Digital Content

Our results suggest a few strategies for action that can help Jewish
Americans. It seems that if the groundwork were laid for easily
accessible “data opt out actions”—via national laws (e.g., [63]) or
normatively adopted data use policies (e.g., [81])—Jewish Americans may be able to organize a very impactful opt out campaign,
i.e., a “data strike” [124]. Additionally, this would suggest a natural
incentive for AI firms to tackle the concerns laid out in this paper
head on: if legal or technical tools for exerting data agency at the
group level proliferate, any groups that currently see high levels of
exposure to property dispossession could create significant leverage

Precel et al.

if there is sufficient buy-in (which may require pressuring or convincing institutions that own the rights to some members’ content).
These dynamics also mean that affinity and interest groups seeking
to protect the welfare of minority groups—e.g., organizations that
support the Jewish community—may have a natural alliance with
efforts to promote a content generator-friendly AI paradigm.

5.4

Implications for Other Minority Groups

Our results suggest that Jewish Americans are not the only minority
group that will likely serve as a “canary in the coal mine” and experience negative effects from the current LLM paradigm sooner than
the general population. Much of the highest-value content used
by language models requires significant education to create (e.g.,
consider the typical author of a paper in PubMed). Jewish Americans have a high relative average educational attainment [83] and,
although other factors may be involved (e.g., a tendency to choose
careers involving more public knowledge sharing), that is likely one
reason we saw the effects that we did. Jewish Americans, however,
are of course far from the only minority group in the United States
(let alone outside of it) with high average educational attainment:
this is true of Asian Americans [41] and Hindu Americans [83]
as well, for instance. Assuming the link between education and
valuable technical content for LLM training datasets is quite strong,
Asian Americans and Hindu Americans are likely to be similarly
affected by language models. Replicating and extending this work
to examine the effect of non-consensual content training on these
groups is a critical area of future work.
Our hypotheses are less clear regarding the potential effects of
LLM-caused intellectual property dispossession for minority groups
outside the United States. Countries around the world are rapidly
engaging in policy discussions around language models, and doing
work to understand if trends similar to those observed here affect
minority groups in places like the EU, the UK, and elsewhere is also
critical research that should happen quickly.

5.5

Balancing Dispossession Concerns and
Group-level Performance Gap Concerns

There is a large body of early and field-defining work in algorithmic
fairness that has highlighted issues with performance gaps that
arise when minoritized groups are underrepresented in training
data (see, e.g., Mehrabi et al. for a survey [80]). Though concerns
with under-representation could be seen as in tension with the
argument we’ve put forth here, these two ideas are not mutually
incompatible.
Generally, under-representation is most concerning when technologies downstream from the dataset impact people subject to the
technologies. For instance, facial recognition systems—which can
be used to unlock a phone screen or for policing—have been shown
to have serious issues with respect to skin tone and gender [17].
In the context of LLM-based technologies enabling labor substitution, however, data contributors do not necessarily derive utility
from the technology nor are they subject to model outputs; rather,
they are primarily subject to labor market dynamics.
This suggests that while there may be cases in which underrepresentation concerns dominate (and vice versa), in general the
ML community will need to adopt a balanced approach to data

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

representation. It can be simultaneously the case that some groups
see harms related to lack of representation and others see harms because they have provided a large share of creative works. Ultimately,
dataset curators are charged with the challenging but necessary
task of gathering data that both accurately represents the world
itself and accounts for the preferences of data subjects (and in some
cases, includes some element of fair remuneration).

5.6

Implications for HCI

HCI has long been a leader in identifying and working to address
challenges in the power dynamics between content producers and
AI systems that consume their content. While HCI’s contributions
have primarily focused on crowd markets and their use in older
generations of AI (e.g., [3, 50, 62]), the research in this paper highlights the importance of continuing and strengthening this line of
work in the LLM era. What kind of platforms could be created to
help content producers receive a fair share of the value they are
creating? (e.g., [65, 66]) How can we empower collective action
among content producers to maximize their ability to do so? (e.g.,
[72]) These are all questions that can help to create new and more
equitable LLM paradigms, and they require significant leadership
from HCI researchers.
The large area of research addressing “algorithmic bias” can trace
some of its origins to work at HCI venues like CHI (e.g., [55]). This
paper highlights the need for the HCI community to continue to
push this line of work forward. While algorithmic bias research
has mostly focused on “representation harms” [31] and gender and
racial dimensions, this work highlights the urgent need to expand
(but certainly not shift) our lens to consider direct material harms
[53, 54] and additional dimensions.
HCI researchers have also looked at how we can best communicate AI design and fairness concepts to end users, including how
the presentation of information about transparency can impact
perceptions [121]. For instance, Anik et al. [6] investigate how
explanations of training data in ML systems can increase transparency and influence trustworthiness of systems. Further work
in HCI could explore how disparate impacts and IP dispossession
interact with perceptions of accuracy, trustworthiness, and fairness
of LLMs. Similarly, HCI has also contributed to toolkits for ML
practitioners to support better decision-making around fairness,
bias, and transparency [70]. As one example, Madaio et al. [76] codesigned AI fairness checklists with practitioners to ground them
in the realities of the day-to-day work, paying particular attention
to the organizational and sociotechnical factors that inhibit fairness
work. Future work from HCI researchers might consider how dispossession and disproportionate impact on minority communities
can be reckoned with within organizations.
Finally, as noted above, many of the harms from property dispossession identified in this paper can be mitigated if the net outcome
of LLM-based technologies is to augment human labor rather than
to substitute for it, a net outcome that the HCI community can help
manifest. Indeed, if we were to be successful in doing so, groups
may want their data to appear in training sets as it could an enhance
LLM’s ability to augment their labor. While substituting for human
labor is a core tenant of important LLM actors like OpenAI [90],
as discussed above, economists have suggested that large-scale net

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

substitution is not a certainty (e.g., [16]). These economists argue
that researchers and practitioners in the computing community
should focus on building LLM-based applications that keep human
labor as input and create entirely new capabilities or augment existing ones, rather than building tools that implicitly seek to remove
human inputs. In broad productivity terms, this means focusing on
creating novel outputs rather than trying to drive human inputs to
zero. As key problem-definers and developers of novel applications,
as well as being a research community responsible for understanding users and their needs, the HCI community is well-positioned
to lead the push for more augmentative LLM-based applications.

6

CONCLUSION

We find evidence that Jewish Americans likely have experienced a
disproportionate share of the potential IP dispossession stemming
from longstanding model training practices of AI companies and
the broader AI research community. These practices may lead to
serious economic harms with disturbing historical parallels, and
call for urgent reflection about the future of the AI ecosystem. We
discuss implications for a range of impacted groups and society as
a whole.

ACKNOWLEDGMENTS
The authors would like to thank the many other scholars—in the
Jewish community and beyond—who took the time to give us feedback on this work. We in particular thank Glen Weyl, Moshe Vardi,
and Gideon Taylor for their essential advice & feedback on earlier
drafts. We also thank Pearl Beck, Elizabeth Tighe, and Ira Sheskin
for their invaluable inputs on demographic methods and DJN use.
This research was not supported by institutions other than our
home universities. Other lines of research by the authors have
been supported by companies that produce LLMs and LLM-based
applications including Microsoft, OpenAI, and Google.

REFERENCES
[1] Daron Acemoglu, David Autor, Jonathon Hazell, and Pascual Restrepo. 2022.
Artificial intelligence and jobs: evidence from online vacancies. Journal of Labor
Economics 40, S1 (2022), S293–S340.
[2] Titipat Achakulvisut, Daniel E. Acuna, and Konrad Kording. 2020. Pubmed
Parser: A Python Parser for PubMed Open-Access XML Subset and MEDLINE
XML Dataset XML Dataset. https://doi.org/10.21105/joss.01979
[3] Ali Alkhatib, Michael S. Bernstein, and Margaret Levi. 2017. Examining Crowd
Work and Gig Work Through The Historical Lens of Piecework. In Proceedings
of the 2017 CHI Conference on Human Factors in Computing Systems (Denver,
Colorado, USA) (CHI ’17). Association for Computing Machinery, New York,
NY, USA, 4599–4616. https://doi.org/10.1145/3025453.3025974
[4] Sam Altman. 2021. Moore’s Law for Everything. https://moores.samaltman.
com/
[5] Steve Andreadis. 2022. The Seizure of Jewish Intellectual Property Ahead of
World War II. https://blogs.loc.gov/copyright/2022/04/the-seizure-of-jewishintellectual-property-ahead-of-world-war-ii
[6] Ariful Islam Anik and Andrea Bunt. 2021. Data-Centric Explanations: Explaining Training Data of Machine Learning Systems to Promote Transparency. In
Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems
(CHI ’21). Association for Computing Machinery, New York, NY, USA, Article
75, 13 pages. https://doi.org/10.1145/3411764.3445736
[7] Janet Krasner Aronson, Matthew Boxer, and Leonard Saxe. 2016. ‘All Politics is
Local’: Challenges in the Study of Local Jewish Communities. Contemporary
Jewry 36, 3 (Oct 2016), 361–380. https://doi.org/10.1007/s12397-016-9200-7
[8] Margaret Atwood. 2023.
Murdered by My Replica?
https:
//www.theatlantic.com/books/archive/2023/08/ai-chatbot-training-booksmargaret-atwood/675151/

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

[9] John Bandy and Nicholas Vincent. 2021. Addressing "Documentation Debt"
in Machine Learning: A Retrospective Datasheet for BookCorpus. In Proceedings of the Neural Information Processing Systems Track on Datasets and
Benchmarks, J. Vanschoren and S. Yeung (Eds.), Vol. 1. Curran, San Diego, CA,
USA. https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/
2021/file/54229abfcfa5649e7003b83dd4755294-Paper-round1.pdf
[10] Miranda Bannister. 2022. A 1492 Letter Regarding Jewish Property in Spain.
https://mjhnyc.org/blog/1492-letter-regarding-jewish-property-in-spain/
[11] Lida Barner. 2017. “Aryanization” Expanded?: Patent Rights of Jews under the
Nazi Regime. Central European University Press, Budapest, Hungary, 127–144.
https://www.jstor.org/stable/10.7829/j.ctt1t6p66t.10
[12] Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret
Shmitchell. 2021. On the Dangers of Stochastic Parrots: Can Language Models
Be Too Big?. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (Virtual Event, Canada) (FAccT ’21). Association for
Computing Machinery, New York, NY, USA, 610–623. https://doi.org/10.1145/
3442188.3445922
[13] Edwin Black. 2012. IBM and the Holocaust: The Strategic Alliance Between Nazi
Germany and America’s Most Powerful Corporation-Expanded Edition (2nd edition
ed.). Dialog Press, USA.
[14] Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence
Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, Michael
Pieler, USVSN Sai Prashanth, Shivanshu Purohit, Laria Reynolds, Jonathan Tow,
Ben Wang, and Samuel Weinbach. 2022. GPT-NeoX-20B: An Open-Source
Autoregressive Language Model. https://doi.org/10.48550/arXiv.2204.06745
arXiv:2204.06745 [cs].
New York Times, CNN and Australia’s ABC
[15] Ariel Bogle. 2023.
block OpenAI’s GPTBot web crawler from accessing content.
https://www.theguardian.com/technology/2023/aug/25/new-york-timescnn-and-abc-block-openais-gptbot-web-crawler-from-scraping-content
[16] Erik Brynjolfsson. 2022. The Turing Trap: The Promise and Peril of Human-Like
Artificial Intelligence. https://digitaleconomy.stanford.edu/news/the-turingtrap-the-promise-peril-of-human-like-artificial-intelligence/
[17] Joy Buolamwini and Timnit Gebru. 2018. Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification. In Proceedings of the 1st
Conference on Fairness, Accountability and Transparency (Proceedings of Machine
Learning Research, Vol. 81), Sorelle A. Friedler and Christo Wilson (Eds.). PMLR,
New York, NY, USA, 77–91. https://proceedings.mlr.press/v81/buolamwini18a.
html
[18] Ann M. Carlos, Donna L. Feir, and Angela Redish. 2022. Indigenous Nations
and the Development of the U.S. Economy: Land, Resources, and Dispossession.
The Journal of Economic History 82, 2 (June 2022), 516–555. https://doi.org/10.
1017/S0022050722000080 Publisher: Cambridge University Press.
[19] Raul Castro Fernandez. 2023. Data-Sharing Markets: Model, Protocol, and
Algorithms to Incentivize the Formation of Data-Sharing Consortia. Proceedings
of the ACM on Management of Data 1, 2 (June 2023), 172:1–172:25. https:
//doi.org/10.1145/3589317
[20] Census.gov. 2021. Frequently Occurring Surnames from the 2010 Census. https:
//www.census.gov/topics/population/genealogy/data/2010_surnames.html
[21] Pew Research Center. 2013. A portrait of Jewish Americans: Findings from a
Pew research center survey of US Jews.
[22] Pew Research Center. 2021. Jewish Americans in 2020.
https://www.
pewresearch.org/religion/2021/05/11/jewish-americans-in-2020/
[23] PubMed Central. 2023. PMC Open Access Subset. https://www.ncbi.nlm.nih.
gov/pmc/tools/openftlist/
[24] Colin B. Clement, Matthew Bierbaum, Kevin P. O’Keeffe, and Alexander A.
Alemi. 2019. arxiv-public-datasets. https://github.com/mattbierbaum/arxivpublic-datasets/blob/master/README.md
[25] Colin B. Clement, Matthew Bierbaum, Kevin P. O’Keeffe, and Alexander A.
Alemi. 2019. On the Use of ArXiv as a Dataset. ArXiv abs/1905.00075 (2019),
1–7. https://api.semanticscholar.org/CorpusID:141496572
[26] Steven M. Cohen. 2016. Deficient, If Not Distorted: Jewish Community Studies
That Totally Rely upon Known Jewish Households. Contemporary Jewry 36, 3
(Oct 2016), 343–360. https://doi.org/10.1007/s12397-016-9187-0
[27] Steven M. Cohen, Frank Mott, Lorraine Blass, Jim Schwartz, Jonathon Ament,
Vivian Klaff, and Laurence Kotler-Berkowitz. 2001. 2000-01 National Jewish
Population Survey. https://www.jewishdatabank.org/databank/search-results/
study/307
[28] CourtListener. 2010. CourtListener. https://www.courtlistener.com/help/api/
bulk-data/
[29] Thomas Craemer, Trevor Smith, Brianna Harrison, Trevon Logan, Wesley Bellamy, and William Darity. 2020. Wealth Implications of Slavery and Racial
Discrimination for African American Descendants of the Enslaved. The Review
of Black Political Economy 47, 3 (Sept. 2020), 218–254. https://doi.org/10.1177/
0034644620926516 Publisher: SAGE Publications Inc.
[30] Maria Cramer. 2021. Henrietta Lacks, Whose Cells Were Taken Without Her
Consent, Is Honored by W.H.O. https://www.nytimes.com/2021/10/13/science/
henrietta-lacks-cells-who.html

Precel et al.

[31] Kate Crawford. 2017. The Trouble With Bias. The Annual Conference on Neural
Information Processing Systems (NeruIPS), San Diego, CA, USA.
[32] Wes Davis. 2023. Sarah Silverman is suing OpenAI and Meta for copyright
infringement. https://www.theverge.com/2023/7/9/23788741/sarah-silvermanopenai-meta-chatgpt-llama-copyright-infringement-chatbots-artificialintelligence-ai
[33] Sergio DellaPergola. 2022. World Jewish Population, 2021. Springer International
Publishing, Cham, 313–412. https://doi.org/10.1007/978-3-030-99750-2_8
[34] Nick Diakopoulos. 2023. Finding Evidence of Memorized News Content in GPT
Models. https://generative-ai-newsroom.com/finding-evidence-of-memorizednews-content-in-gpt-models-d11a73576d2
[35] Catherine D’Ignazio and Lauren Klein. 2020. 4. “What Gets Counted Counts”.
MIT Press, Cambridge, MA, USA, Chapter 4, 1–27. https://data-feminism.
mitpress.mit.edu/pub/h1w0nbqp
[36] David Dutwin. 2016. Everything You Need to Consider When Deciding to Field a
Survey of Jews: Choices in Survey Methods and Their Consequences on Quality.
Contemporary Jewry 36, 3 (Oct 2016), 297–318. https://doi.org/10.1007/s12397016-9189-y
[37] EleutherAI. 2020. github-downloader. https://github.com/EleutherAI/githubdownloader
[38] EleutherAI. 2023. EleutherAI. https://www.eleuther.ai
[39] Tyna Eloundou, Sam Manning, Pamela Mishkin, and Daniel Rock. 2023. GPTs
are GPTs: An Early Look at the Labor Market Impact Potential of Large Language
Models. https://doi.org/10.48550/arXiv.2303.10130 arXiv:2303.10130 [cs, econ,
q-fin]
[40] Simon Fairlie. 2009. A Short History of Enclosure in Britain. https://www.
thelandmagazine.org.uk/articles/short-history-enclosure-britain
[41] National Center for Education Statistics. 2023. Educational Attainment of
Young Adults. https://nces.ed.gov/programs/coe/indicator/caa/young-adultattainment
[42] Jonathan Freedland. 2018. Antisemitism matters: Jews are the canary in
the coalmine. https://www.theguardian.com/commentisfree/2018/mar/30/
antisemitism-jews-canary-coalmine-fake-news
[43] Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles
Foster, Jason Phang, Horace He, Anish Thite, Noa Nabeshima, Shawn Presser,
and Connor Leahy. 2021. The Pile: An 800GB Dataset of Diverse Text for
Language Modeling. CoRR abs/2101.00027 (2021), 1–39. arXiv:2101.00027 https:
//arxiv.org/abs/2101.00027
[44] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman
Vaughan, Hanna Wallach, Hal Daumé III, and Kate Crawford. 2021. Datasheets
for Datasets. Commun. ACM 64, 12 (2021), 86–92.
[45] GitHub. 2022. GitHub REST API Documentation. https://docs.github.com/en/
rest?apiVersion=2022-11-28
[46] Jill Goldsmith. 2023. Michael Chabon, David Henry Hwang, Other Writers
Sue Meta AI Platform LLaMA For Copyright Infringement, Seek Class Action
Status. https://deadline.com/2023/09/michael-chabon-david-henry-hwangwriters-sue-meta-ai-llama-copyright-1235544842/
[47] Michael M. Grynbaum and Ryan Mac. 2023. The Times Sues OpenAI and
Microsoft Over A.I. Use of Copyrighted Work. https://www.nytimes.com/2023/
12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html
[48] The Authors Guild. 2023. Authors Guild Submits Written Testimony in Senate
AI Hearing. https://authorsguild.org/news/ag-submits-written-testimony-insenate-ai-hearing/
[49] Foad Hamidi, Morgan Klaus Scheuerman, and Stacy M. Branham. 2018. Gender
Recognition or Gender Reductionism? The Social Implications of Embedded
Gender Recognition Systems. In Proceedings of the 2018 CHI Conference on
Human Factors in Computing Systems (CHI ’18). Association for Computing
Machinery, New York, NY, USA, 1–13. https://doi.org/10.1145/3173574.3173582
[50] Kotaro Hara, Abigail Adams, Kristy Milland, Saiph Savage, Chris Callison-Burch,
and Jeffrey P. Bigham. 2018. A Data-Driven Analysis of Workers’ Earnings on
Amazon Mechanical Turk. In Proceedings of the 2018 CHI Conference on Human
Factors in Computing Systems (CHI ’18). Association for Computing Machinery,
New York, NY, USA, 1–14. https://doi.org/10.1145/3173574.3174023
[51] Harriet Hartman and Ira M Sheskin. 2013. Estimating the Jewish student
population of a college campus. Journal of Jewish Communal Service 88, 1-2
(2013), 95–109.
[52] Jan Hatzius, Joseph Briggs, Devesh Kodnani, and Giovanni Pierdomenico.
2023. The Potentially Large Effects of Artificial Intelligence on Economic
Growth. https://www.gspublishing.com/content/research/en/reports/2023/03/
27/d64e052b-0f6e-45d7-967b-d7be35fabd16.html
[53] Brent Hecht. 2017. HCI and the U.S. Presidential Election: A Few Thoughts on
a Research Agenda. In CHI ’18 Panel Presentation: The 2016 US Election and HCI:
Towards a Research Agenda. The Conference on Human Factors in Computing
Systems (CHI), Denver, CO, 1–5. https://brenthecht.com/publications/chi17_
bhecht_election2016panel.pdf
[54] Brent Hecht. 2017. The Origins, Present, and Future of Algorithmic Bias. (2017).
[55] Brent Hecht and Darren Gergle. 2010. The Tower of Babel Meets Web 2.0: UserGenerated Content and Its Applications in a Multilingual Context. In CHI ’10:

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

28th International Conference on Human Factors in Computing Systems (CHI ’10).
ACM, Atlanta, GA, 291–300. https://doi.org/10.1145/1753326.1753370 ACM ID:
1753370.
[56] Harold S. Himmelfarb. 1986. Further comments on the use of DJN. Contemporary
Jewry 7, 1 (Jan 1986), 99–102. https://doi.org/10.1007/BF02967946
[57] Harold S. Himmelfarb, R. Michael Loar, and Susan H. Mott. 1983. Sampling by
Ethnic Surnames: The Case of American Jews. The Public Opinion Quarterly 47,
2 (1983), 247–260. http://www.jstor.org/stable/2749024
[58] Ayesha Javed. 2023. AI Could Destroy Journalism as We Know It. Media
Mogul Barry Diller Hopes to Save It. https://time.com/6279147/barry-diller-aijournalism/
[59] Harry H. Jiang, Lauren Brown, Jessica Cheng, Mehtab Khan, Abhishek Gupta,
Deja Workman, Alex Hanna, Johnathan Flowers, and Timnit Gebru. 2023. AI
Art and its Impact on Artists. In Proceedings of the 2023 AAAI/ACM Conference
on AI, Ethics, and Society (AIES ’23). Association for Computing Machinery, New
York, NY, USA, 363–374. https://doi.org/10.1145/3600211.3604681
[60] Kevin Roose and Casey Newton. 2023. Casey Goes to the White House + The
Copyright Battle Over Artificial Intelligence + HatGPT. https://www.nytimes.
com/2023/11/03/podcasts/hard-fork-executive-order-ai-copyright.html?
[61] Os Keyes. 2018. The Misgendering Machines: Trans/HCI Implications of Automatic Gender Recognition. Proceedings of the ACM on Human-Computer
Interaction 2, CSCW (Nov 2018), 88:1–88:22. https://doi.org/10.1145/3274357
[62] Aniket Kittur, Jeffrey V. Nickerson, Michael Bernstein, Elizabeth Gerber, Aaron
Shaw, John Zimmerman, Matt Lease, and John Horton. 2013. The Future of
Crowd Work. In Proceedings of the 2013 Conference on Computer Supported
Cooperative Work (CSCW ’13). ACM, New York, NY, USA, 1301–1318. https:
//doi.org/10.1145/2441776.2441923 00108.
[63] Kate Knibbs. 2024. Congress Wants Tech Companies to Pay Up for AI Training
Data. https://www.wired.com/story/congress-senate-tech-companies-pay-aitraining-data/
[64] Barry A. Kosmin and Stanley Waterman. 1985. The Use and Misuse of Distinctive
Jewish Names in Research on Jewish Populations. Jewish Population Studies 19
(1985), 1–9. https://api.semanticscholar.org/CorpusID:146336902
[65] Airi Lampinen and Barry Brown. 2017. Market Design for HCI: Successes and
Failures of Peer-to-Peer Exchange Platforms. In Proceedings of the 2017 CHI
Conference on Human Factors in Computing Systems (Denver, Colorado, USA)
(CHI ’17). Association for Computing Machinery, New York, NY, USA, 4331–4343.
https://doi.org/10.1145/3025453.3025515
[66] Airi Lampinen, Christoph Lutz, Gemma Newlands, Ann Light, and Nicole Immorlica. 2018. Power Struggles in the Digital Economy: Platforms, Workers,
and Markets. In Companion of the 2018 ACM Conference on Computer Supported Cooperative Work and Social Computing (CSCW ’18 Companion). Association for Computing Machinery, New York, NY, USA, 417–423. https:
//doi.org/10.1145/3272973.3273004
[67] Bernard Lazerwitz. 1986. Some comments on the use of distinctive Jewish names
in surveys. Contemporary Jewry 7, 1 (Jan 1986), 83–91. https://doi.org/10.1007/
BF02967944
[68] Katherine Lee, A. Feder Cooper, James Grimmelmann, and Daphne Ippolito.
2023. AI and Law: The Next Generation. In GenLaw ’23 (at ICML ’23). The
International Conference on Machine Learning (ICML), San Diego, CA, USA,
1–21. http://dx.doi.org/10.2139/ssrn.4580739
[69] Katherine Lee, A. Feder Cooper, FatemehSadat Mireshghallah, Madiha Zahrah,
James Grimmelmann, David Mimno, Deep Ganguli, and Ludwig Schubert. 2023.
Generative AI + Law (GenLaw) ’23. The GenLaw Center. https://genlaw.github.
io/
[70] Michelle Seng Ah Lee and Jat Singh. 2021. The Landscape and Gaps in Open
Source Fairness Toolkits. In Proceedings of the 2021 CHI Conference on Human
Factors in Computing Systems (CHI ’21). Association for Computing Machinery,
New York, NY, USA, Article 699, 13 pages. https://doi.org/10.1145/3411764.
3445261
[71] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim
Rocktäschel, Sebastian Riedel, and Douwe Kiela. 2020. Retrieval-Augmented
Generation for Knowledge-Intensive NLP Tasks. In Advances in Neural Information Processing Systems, Vol. 33. Curran Associates, Inc., San Dieco,
CA, USA, 9459–9474.
https://proceedings.neurips.cc/paper/2020/hash/
6b493230205f780e1bc26945df7481e5-Abstract.html
[72] Hanlin Li, Bodhisattva Alarcon, Sara Milkes Espinosa, and Brent Hecht. 2018.
Out of Site: Empowering a New Approach to Online Boycotts. In CSCW ’18: 2018
ACM Conference on Computer Supported Cooperative Work. ACM, New York, NY,
USA, 1–28.
[73] Hanlin Li, Nicholas Vincent, Stevie Chancellor, and Brent Hecht. 2023. The
Dimensions of Data Labor: A Road Map for Researchers, Activists, and Policymakers to Empower Data Producers. In Proceedings of the 2023 ACM Conference
on Fairness, Accountability, and Transparency. ACM, New York, NY, USA, 1151–
1161.

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

[74] Christian D. Liddy. 2015. Urban Enclosure Riots: Risings of the Commons in
English Towns, 1480–1525. Past & Present 226, 1 (Feb. 2015), 41–77. https:
//doi.org/10.1093/pastj/gtu038
[75] Shayne Longpre, Robert Mahari, Niklas Muennighoff, Anthony Chen, Kartik
Perisetla, William Brannon, Jad Kabbara, Luis Villa, and Sara Hooker. 2023.
The Data Provenance Project. In GenLaw Workshop at ICML. The International
Conference on Machine Learning (ICML), San Diego, CA, USA, 1–8.
[76] Michael A. Madaio, Luke Stark, Jennifer Wortman Vaughan, and Hanna Wallach.
2020. Co-Designing Checklists to Understand Organizational Challenges and
Opportunities around Fairness in AI. In Proceedings of the 2020 CHI Conference on
Human Factors in Computing Systems (Honolulu, HI, USA) (CHI ’20). Association
for Computing Machinery, New York, NY, USA, 1–14. https://doi.org/10.1145/
3313831.3376445
[77] David A. Marker, Shelley Brock, Darby Steiger, Jill DeMatteis, and Hanna Popick.
2021. Jewish Community Studies in the Twenty-First Century. Contemporary
Jewry 41, 2 (Jun 2021), 349–368. https://doi.org/10.1007/s12397-021-09388-w
[78] Pablo Mateos. 2014. Classifying Ethnicity Through People’s Names. In Names,
Ethnicity and Populations (Advances in Spatial Science). Springer, Berlin, Heidelberg, 117–144. https://doi.org/10.1007/978-3-642-45413-4_6
[79] Cory McCartan, Jacob Goldin, Daniel E. Ho, and Kosuke Imai. 2023. Estimating
Racial Disparities When Race is Not Observed. arXiv preprint arXiv:2303.02580
abs/2303.02580 (2023), 1–29. arXiv:2303.02580 [stat.AP]
[80] Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, and Aram
Galstyan. 2021. A Survey on Bias and Fairness in Machine Learning. ACM
computing surveys (CSUR) 54, 6 (2021), 1–35. http://arxiv.org/abs/1908.09635
[81] Cullen Miller. 2023. ai.txt: A new way for websites to set permissions for AI.
https://spawning.substack.com/p/aitxt-a-new-way-for-websites-to-set
[82] Sewon Min, Suchin Gururangan, Eric Wallace, Hannaneh Hajishirzi, Noah A.
Smith, and Luke Zettlemoyer. 2023. SILO Language Models: Isolating Legal
Risk In a Nonparametric Datastore. https://doi.org/10.48550/arXiv.2308.04430
arXiv:2308.04430 [cs].
[83] Caryle Murphy. 2016.
The most and least educated U.S. religious
groups. https://www.pewresearch.org/short-reads/2016/11/04/the-most-andleast-educated-u-s-religious-groups/
[84] United States Holocaust Memorial Museum. 2017. Aryanization. https://
encyclopedia.ushmm.org/content/en/article/aryanization
[85] United States Holocaust Memorial Museum. 2023. Jewish Population of Europe. https://encyclopedia.ushmm.org/content/en/gallery/jewish-populationof-europe
[86] United Nations. 2021. Global Population. https://www.un.org/en/globalissues/population
[87] NCBI. 2023. National Center for Biotechnology Information. https://www.ncbi.
nlm.nih.gov/
[88] U.S. Department of State. 2020. Building Coalitions and Alliances - The Canary
in the Coal Mine? The Need for Cooperation. https://www.youtube.com/
watch?v=Ne3dGStTN8Q
[89] OpenAI. 2023. GPT-4 Technical Report. https://doi.org/10.48550/arXiv.2303.
08774 arXiv:2303.08774 [cs].
[90] OpenAI. 2023. OpenAI Charter. OpenAI. https://openai.com/charter
[91] Andrew Orlowski. 2023. The internet’s ‘original sin’ means AI will be a nightmare. https://www.telegraph.co.uk/business/2023/08/21/internets-originalsin-ai-nightmare/
[92] Anil Oza and Mariana Lenharo. 2023. How the ‘groundbreaking’ Henrietta Lacks
settlement could change research. https://doi.org/10.1038/d41586-023-02479-8
[93] UK Parliament. 2023. Enclosing the land.
https://www.parliament.uk/
about/living-heritage/transformingsociety/towncountry/landscape/overview/
enclosingland/
[94] Amandalynne Paullada, Inioluwa Deborah Raji, Emily M Bender, Emily Denton, and Alex Hanna. 2021. Data and its (dis) contents: A survey of dataset
development and use in machine learning research. Patterns 2, 11 (2021), 1–14.
https://doi.org/10.1016/j.patter.2021.100336
[95] Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru,
Alessandro Cappelli, Hamza Alobeidli, Baptiste Pannier, Ebtesam Almazrouei,
and Julien Launay. 2023. The RefinedWeb dataset for Falcon LLM: outperforming curated corpora with web data, and web data only. arXiv preprint
arXiv:2306.01116 abs/2306.01116 (2023), 1–32. arXiv:2306.01116 [cs.CL] https:
//arxiv.org/abs/2306.01116
[96] Jay Peters and Wes Davis. 2023. The New York Times blocks OpenAI’s web
crawler.
https://www.theverge.com/2023/8/21/23840705/new-york-timesopenai-web-crawler-ai-gpt
[97] Benjamin Phillips. 2007. Numbering the Jews: Evaluating and Improving Surveys of American Jews.
Brandeis University ProQuest University Publishing I (Feb 2007), 1–506.
https://www.semanticscholar.
org/paper/Numbering-the-Jews%3A-Evaluating-and-Improving-ofPhillips/4fb989e9344020d0a3ca85caf27417e15417077a
[98] Associated Press. 2023. James Patterson, Margaret Atwood among thousands of
writers urging AI companies to honor copyrights. https://apnews.com/article/
patterson-atwood-ai-open-letter-f2c434694ed22a64bd09abbb5742c1e5

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

[99] Shawn Presser. 2023. Books3 Metadata.
https://web.archive.org/web/
20230000000000*/https://battle.shawwn.com/books3-metadata.jsonl, last accessed 11/30/2023.
[100] Alex Reisner. 2023. Revealed: The Authors Whose Pirated Books Are Powering
Generative AI.
https://www.theatlantic.com/technology/archive/2023/08/
books3-ai-meta-llama-pirated-books/675063/
[101] Adam Roberts, Colin Raffel, Katherine Lee, Michael Matena, Noam Shazeer,
Peter J. Liu, Sharan Narang, Wei Li, and Yanqi Zhou. 2020. Exploring the Limits
of Transfer Learning with a Unified Text-to-Text Transformer. The Journal of
Machine Learning Research 21, 1 (2020), 5485–5551.
[102] Ira Rosenwaike. 1990. Leading Surnames Among American Jews. Names 38
(Jun 1990), 31–38. https://doi.org/10.1179/nam.1990.38.1-2.31
[103] Emma Roth. 2023. Another group of writers is suing OpenAI over copyright
claims. https://www.theverge.com/2023/9/11/23869145/writers-sue-openaichatgpt-copyright-claims
[104] Pamela Samuelson. 2023. Generative AI meets copyright. Science 381, 6654 (July
2023), 158–161. https://doi.org/10.1126/science.adi0656 Publisher: American
Association for the Advancement of Science.
[105] Melissa Santos. 2024. ChatGPT and AI replacing jobs is a worry for workers,
per WSU survey. https://www.axios.com/local/seattle/2024/02/09/chat-gpt-aiworkers-replace-employees
[106] Jonathan D. Sarna. 2019. Appendix: American Jewish Population Estimates,
1660–2015. Yale University Press, New Haven, CT, USA, 391–392. https://doi.
org/10.2307/j.ctvhrczf4.13
[107] Leonard Saxe, Daniel Parmer, Elizabeth Tighe, Raquel Magidin de Kramer,
Daniel Kallista, Daniel Nussbaum, Xajavion Seabrum, and Joshua Mandell. 2021.
American Jewish Population Estimates 2020: Summary & Highlights. Brandeis
University.
[108] Kevin Schaul, Szu Yu Chen, and Nitasha Tiku. 2023. Inside the secret list of
websites that make AI like ChatGPT sound smart. https://www.washingtonpost.
com/technology/interactive/2023/ai-chatbot-learning/
[109] Martin Senftleben. 2023. Generative AI and Author Remuneration. IIC - International Review of Intellectual Property and Competition Law 54, 10 (Nov. 2023),
1535–1560. https://doi.org/10.1007/s40319-023-01399-4
[110] Congressional Legal Service. 2023. Generative Artificial Intelligence and Copyright Law. Technical Report. Congressional Legal Service. https://crsreports.
congress.gov/product/pdf/LSB/LSB10922
[111] Ira M. Sheskin. 1998. A Methodology for Examining the Changing Size and
Spatial Distribution of a Jewish Population: A Miami Case Study. Shofar: An
Interdisciplinary Journal of Jewish Studies 17, 1 (1998), 97–116. https://doi.org/
10.1353/sho.1998.0041
[112] Ira M. Sheskin. 2016. Good Practices in Local Jewish Community Studies.
Contemporary Jewry 36, 3 (Oct 2016), 319–341. https://doi.org/10.1007/s12397016-9184-3
[113] Ira M. Sheskin and Arnold Dashefsky. 2012. Jewish Population in the United
States, 2012. The American Jewish Year Book 109/112 (2012), 143–211.
[114] Ira M. Sheskin and Arnold Dashefsky (Eds.). 2012-2023. American Jewish Year
Book (series). Jewish Publication Society; American Jewish Committee, USA.
https://www.springer.com/series/11193
[115] Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra
Blevins, Danqi Chen, and Luke Zettlemoyer. 2023. Detecting Pretraining Data
from Large Language Models.
https://doi.org/10.48550/arXiv.2310.16789
arXiv:2310.16789 [cs].
[116] Ray A. Smith. 2024. AI Is Starting to Threaten White-Collar Jobs. Few Industries
Are Immune. https://www.wsj.com/lifestyle/careers/ai-is-starting-to-threatenwhite-collar-jobs-few-industries-are-immune-9cdbcb90 Section: Management.
[117] Yanqiu Tao, Debbie Steckel, Jiří Jaromír Klemeš, and Fengqi You. 2021. Trend
towards virtual and hybrid conferences may be an effective climate change
mitigation strategy. Nature Communications 12, 1 (Dec. 2021), 7324. https:
//doi.org/10.1038/s41467-021-27251-2 Number: 1 Publisher: Nature Publishing
Group.
[118] Adam Teller. 2010. Economic Life. https://yivoencyclopedia.org/article.aspx/
economic_life
[119] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume
Lample. 2023. LLaMA: Open and Efficient Foundation Language Models. https:
//doi.org/10.48550/arXiv.2302.13971
[120] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi,
Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models.
arXiv preprint arXiv:2307.09288 abs/2307.09288 (2023), 1–77. https://arxiv.org/
abs/2307.09288
[121] Niels van Berkel, Jorge Goncalves, Daniel Russo, Simo Hosio, and Mikael B. Skov.
2021. Effect of Information Presentation on Fairness Perceptions of Machine
Learning Predictors. In Proceedings of the 2021 CHI Conference on Human Factors
in Computing Systems (CHI ’21). Association for Computing Machinery, New
York, NY, USA, Article 245, 13 pages. https://doi.org/10.1145/3411764.3445365

Precel et al.

[122] James Vincent. 2023. Getty Images sues AI art generator Stable Diffusion in the
US for copyright infringement. https://www.theverge.com/2023/2/6/23587393/
ai-art-copyright-lawsuit-getty-images-stable-diffusion
[123] Nicholas Vincent and Brent Hecht. 2023. Sharing the Winnings of AI with Data
Dividends: Challenges with “Meritocratic” Data Valuation.
[124] Nicholas Vincent, Brent Hecht, and Shilad Sen. 2019. “Data Strikes”: Evaluating
the Effectiveness of a New Form of Collective Action Against Technology
Companies. In The World Wide Web Conference (San Francisco, CA, USA) (WWW
’19). Association for Computing Machinery, New York, NY, USA, 1931–1943.
https://doi.org/10.1145/3308558.3313742
[125] Nick Vincent and Hanlin Li. 2023. ChatGPT Stole Your Work. So What Are
You Going to Do? https://www.wired.com/story/chatgpt-generative-artificialintelligence-regulation/
[126] Nicholas M. Vincent. 2020. Don’t give OpenAI all the credit for GPT-3: You might
have helped create the latest “astonishing” advance in AI too. People, Space, and
Algorithms Research Group. https://www.psagroup.org/blogposts/62
[127] Johannes Wachs, Mariusz Nitecki, William Schueller, and Axel Polleres. 2022.
The Geography of Open Source Software: Evidence from GitHub. Technological
Forecasting and Social Change 176 (Mar 2022), 121478. https://doi.org/10.1016/j.
techfore.2022.121478
[128] Wikipedia. 2023. René Carmille. Wikipedia. https://fr.wikipedia.org/w/index.
php?title=Ren%C3%A9_Carmille&oldid=210288825 Page Version ID: 210288825.
[129] Siyuan Xia, Zhiru Zhu, Chris Zhu, Jinjin Zhao, Kyle Chard, Aaron J. Elmore,
Ian Foster, Michael Franklin, Sanjay Krishnan, and Raul Castro Fernandez. 2022.
Data station: delegated, trustworthy, and auditable computation to enable datasharing consortia with a data escrow. Proceedings of the VLDB Endowment 15,
11 (July 2022), 3172–3185. https://doi.org/10.14778/3551793.3551861
[130] Erdem Dogukan Yilmaz, Ivana Naumovska, and Vikas A. Aggarwal. 2023. AIDriven Labor Substitution: Evidence from Google Translate and ChatGPT. https:
//doi.org/10.2139/ssrn.4400516
[131] Hamed Zamani, Fernando Diaz, Mostafa Dehghani, Donald Metzler, and Michael
Bendersky. 2022. Retrieval-Enhanced Machine Learning. In Proceedings of the
45th International ACM SIGIR Conference on Research and Development in Information Retrieval. Special Interest Group on Information Retrieval (SIGIR), NYC,
NY, USA, 2875–2886. https://doi.org/10.1145/3477495.3531722 arXiv:2205.01230
[cs].
[132] Ali Zarifhonarvar. 2023. Economics of ChatGPT: A Labor Market View on the
Occupational Impact of Artificial Intelligence. https://doi.org/10.2139/ssrn.
4350925
[133] Fanlong Zeng, Wensheng Gan, Yongheng Wang, Ning Liu, and Philip S. Yu.
2023. Large Language Models for Robotics: A Survey. ArXiv abs/2311.07226
(2023), 1–19. https://api.semanticscholar.org/CorpusID:265149884

A

APPENDIX

This appendix covers three topics across five sections:
• Additional robustness checks and analyses we performed to
increase confidence in our methods (A.1, A.2, A.3).
• More information on the history and use of DJNs (A.4).
• A supplementary analysis that measures IP dispossession by
industry. We include it here as both a robustness check (the
results seem to support our conclusions) and as a topic for
future research (A.5).

A.1

How Wrong Would Our Estimates Have To
Be To Achieve No Impact

In the main body of this study, we identify a reasonable range for
each parameter to determine lower and upper bounds for each
estimate. Here, we check how robust the results are to even more
conservative parameter values. All of these values are massive
departures from the best available data discussed in the main body
of our paper; we include this section to validate the robustness of
our claims. To do this, we calculated what value each parameter
would have to have in order to indicate no over-representation. We
held all parameters other than the one under investigation constant
at the original lower bound estimates. We found that in order for
the weighted relative dispossession magnitude to be ∼1 X (ie: no
overrepresentation), the following would have to be true:

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

• 32.6% or fewer of people with DJNs are Jewish (the remaining
67.4% are non-Jews).
• 27.4% or more of the U.S. Jewish population have DJNs.
• 5.9% of the U.S. population is Jewish.
These precise values for each parameter are in Tables 3-5.
Parameter
% precision of DJNs
% coverage of DJNs
% of US population that is Jewish
Relative Dispossession Magnitude
Total
Weighted Total

Estimates
32.6%
11.18%
2.4%

us increase our confidence in our estimate of the relative representation of Jewish Americans relative other Americans. An alternative
approach in future work might be to consider representative purely
at the global level.
A.2.1 Pubmed Central. We used journal countries of publication [87] as a proxy for author countries to estimate an expected
0.6% of Jewish authorship as compared to the 1.95-2.21% we see
(Table 6).
Journals by Country
of Publication
U.S. Other
3,499
1,000 2,499
Table 6: Publication countries of PMC journals, intended as a
rough estimate of percentage of the dataset that is U.S. based
or affiliated.
Journals
in PMC

1.17 X
1.00 X

Table 3: All parameters other than precision are held constant at lower bound estimates. With precision at 32.6%, the
weighted total relative dispossession magnitude would be
1.00 X.

Parameter
% precision of DJNs
% coverage of DJNs
% of US population that is Jewish

Estimates
80%
27.4%
2.4%

Relative Dispossession Magnitude
Total
Weighted Total

1.17 X
1.00 X

Table 4: All parameters other than coverage are held constant at lower bound estimates. With coverage at 27.4%, the
weighted total relative dispossession magnitude would be
1.00 X.

A.2.2 ArXiv. We estimated the number of U.S. authors who had
submitted work to ArXiv. We scoped U.S. authorship to those who
work at U.S. institutions, as they are most likely U.S. residents. Using
data from the U.S. Department of Education’s National Center for
Education Statistics (NCES),4 which tracks educational institutions
that accept federal funding, we identified U.S. higher education
institutions. We then manually inspected all ArXiv institutions containing the word “hospital” or “medical” to find research originating
in U.S. hospital systems. We then sorted the remaining institutions
by highest number of submissions and added U.S. research institutes (e.g., NIST, Los Alamos National Laboratory) and companies
(e.g., Intel, IBM) to our list, until no U.S.-based institutions remained
in the top 500 institutions. From this list, we calculated the number
of U.S. submissions. This is likely to be an undercount, as there are
over 6200 educational institutions and there are likely formatting
inconsistencies between ArXiv and NCES that will have unintentionally excluded U.S. institutions.

A.3
Parameter
% precision of DJNs
% coverage of DJNs
% of US population that is Jewish

Estimates
80%
11.18%
5.9%

Relative Dispossession Magnitude
Total
Weighted Total

1.16 X
1.00 X

Table 5: All parameters other than the % of the U.S. population that is Jewish are held constant. With U.S. Jews at 5.9%
of the population, the weighted total relative dispossession
magnitude would be 1.00 X.

A.2

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

Estimation of U.S. Representation In
Dataset

Here, we discuss how we investigated the extent to which each
dataset included content from people based in the U.S. This helped

Robustness Check for Document Age in
FreeLaw

We considered constructing a weighted average of Jewish population over time based on the publication dates of documents in the
dataset. When we used FreeLaw as a case study (because it is the
dataset with the oldest records, covers the greatest time span, and
is entirely U.S.-based), we found that it barely affected our expected
Jewish population percentage. Because documents in the rest of
the sources are more recent, and the Jewish population has stayed
somewhat constant over the past 10-15 years (when many of the
documents across datasets were produced), we decided not to stray
from the naive approach to account for document age. We note
here that if a significant number of documents in a source were
published between 2000-2010 we’d expect to see a slightly lower
percentage of Jews, and if a significant number of documents were
published between 1920-1970 we’d expect to see a slightly higher
percentage.
4 https://nces.ed.gov/

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

A.4

Additional Detail On the Distinctive Jewish
Names-Based Methodology

As summarized briefly in Section 2.4.2, DJNs have a long history in
the world of Jewish demography. The original concept is attributed
to Kohs, who found that the most common surnames on Jewish
Federation membership lists represented a significant proportion of
overall membership [57]. Later surveys in the 1960s-80s confirmed
that, depending on the list used, the national proportion of Jews
with DJNs remained roughly constant at ∼11-12%. Since then, DJNs
have been used in numerous studies, including (a) as the basis
for the sampling frame (or more likely, as the basis for one of
several sampling frames) for local Jewish community studies; (b)
to measure the change in size of a Jewish community over time;
and (c) to estimate the overall size of a Jewish community within
a larger local population (e.g., the number of Jews on a college
campus [51]).5 Any potential use of DJNs should be measured
on at least two axes—coverage and representativeness—which we
elaborate on below.
A.4.1 Coverage. Research that uses DJN-based lists as a sole sampling frame by definition can only cover the percentage of the
population with a Jewish surname. In local community studies, this
puts a strong cap on possible participants [36]. As the current study
does not directly survey a sub-population, coverage in that sense
is not an issue so long as we can calculate the proportion of the
U.S. Jewish community that our sample captures. In the earliest
studies of DJNs, researchers estimated that between 11–12% of the
national Jewish population had one of ∼35 surnames ( [57, 64, 67]).
However, they caution that these numbers vary significantly across
local subsets of the Jewish community, so smaller studies should be
wary of applying the 11–12% figure “unless they have prior knowledge about the actual size of the proportion of the population that
DJN persons constitute and the stability of that proportion over
time.” [56].
These numbers have remained largely consistent over time for
large U.S. Jewish communities. In 2007, Phillips found that 12.4%
of Greater Boston Area Jews had a DJN, and 91.8% of people with
a DJN were Jewish. In a 2012 review of local area studies, Sheskin
and Dashefsky noted, “the fact that about 8–12% of American Jews,
despite rising intermarriage, continue to have one of 36 Distinctive
Jewish Names... facilitates making reasonable estimates of the Jewish population.” [113] As additional confirmation, we used Hartman
and Sheskin’s method to calculate an “expansion factor” based on
the Pew 20136 Jewish population estimate [21] in conjunction with
the U.S. Census’s 2010 surname frequency data [20].7 We found
that ∼9.15–11.18% of the U.S. Jewish population at the time was
covered by the DJN frame, which is aligned with prior estimates.
A.4.2 Representativeness. Another concern with using a DJN-only
frame is as follows: making claims about all Jews on the basis of
Jews with DJNs relies on the assumption that the latter group does
5 See the “United States Jewish Population” chapters of the American Jewish Yearbook

series for a detailed account of such studies [33, 114].
6We use the 2013 estimate rather than the 2020 estimate in order to align with Census
data, of which 2010 is the latest available.
7 To do this, we counted the number of people with DJNs represented on the list,
accounted for non-Jews with DJNs as described in 3.2.2, and compared the resulting
number to the total number of Jews in the U.S. counted by Pew.

not differ significantly in character from the former. A number of

Precel et al.

studies have been conducted on the representativeness of DJNs
with mixed conclusions (in part due to lack of standardization with
regards to which DJNs are used in a given study). It seems to be
largely the case that DJN samples underrepresent intermarried Jews
and their children, Jews with self-defined partial, mixed, or nonreligions connections to Judaism, younger Jews, and (expectedly)
Jews without Jewish parents [26, 36, 67, 112]. Critics of DJNs generally argue that the type of Jews least likely to be counted by DJNs
are “on the margin,” which is especially problematic for studies
whose goal it is to help Jewish community leaders best serve their
constituents [26]. However, because our study strictly estimates
population size without surveying individuals, representation is
only important insofar as it relates to likelihood of producing IP
that appears in our dataset. As long as this is the case, our expansion
factor should account for any undercount.
While we do not have prior reason to suspect such a bias, it is a
limitation of our method that we cannot test for it directly. There is
some evidence to suggest that DJN samples do not show significant
differences in income [26, 112] and education [57] as compared to
the general population; we did not find direct comparisons between
the occupations of DJN and non-DJN samples (which would be
the most direct proxy). Absent a compelling hypothesis for why
DJN samples would significantly differ from the general population
on occupation or writing output, it is reasonable to assume that
our estimates provide order-of-magnitude bounds for the target
variables.
A.4.3 Broader Considerations. While it is not the focus of this paper and we defer to the large literature on this topic for further
discussion (e.g. [13]), it is useful to reflect on the broader considerations surrounding our need to rely on methodologies like
those described above. Historical context is critical here. Previous
databases of people with Jewish identity have been extremely dangerous to the Jewish community, with notable examples of these
databases contributing to the deaths of millions of Jews in World
War II [13]. Indeed, there is at least one person who was killed by
the Nazi government for intentionally introducing noise into these
databases [128].
Given this history, and although this is out of scope for this work
and not necessarily a consensus view, there is a reasonable belief
that the best balance between being able to make data-driven assessments relevant to the Jewish community and protecting members
of the community from serious material harm is through a noisy
sensor like those provided by DJNs.

A.5

Measuring IP Dispossession by Industry

Above, our analysis focused heavily on looking at carefully selected
subsets of training data, each of which mapped to a particular job
category or industry.
Many LLMs have been trained using filtered subset of the wideranging Common Crawl dataset. This data is not as structured
as any of the the specific Pile subsets we looked at, which each
have underlying institutional norms that drive some of the implicit
formatting, tone, and content standards.
Past work has already identified evidence of IP related to specific jobs in LLM training data. One case study showed that GPT-4
appears to have memorized content from the New York Times [34],

American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

and the lawsuit against OpenAI filed by the New York Times provided further evidence of this memorization [47]. Investigation
by the Washington Post and AI2 looked into the domains that
contributed the most tokens to Google’s C4 [101] dataset (one filtered version of Common Crawl) [108]. In the top 10 domains
alone, we see domains with IP produced by people in law (e.g.
patents.google.com), media and journalism (e.g. nytimes.com), and
science and medicine (e.g. journals.plos.org). The descriptive stats
from Schaul et al.’s analysis [108] further substantiate the idea that
IP-heavy job categories like law, media, journalism, science, and
medicine help constitute much of the LLM training data outside
careful subsets.
As a supplementary analysis, we conducted a small investigation
into another filtered Common Crawl variant, RefinedWeb [95]. We
approximated a random sample by randomly downloading 0.4% of
the roughly 5300 data files shared by the RefinedWeb curators on
HuggingFace. We ranked the domains in this sample by number of
total words. We found found very similar results to the C4 investigation – journalists, scientists, medical researchers, lawyers, and other
professional classes were dominant. Specifically, of the top 200 domains in C4, 131 were in at least the top 1000 of RefinedWeb. There
are numerous subjective design choices involved in this minor analysis (when to consider subdomains like ‘patents.google.com’, how
to label a domain as pertaining to a specific job category), so we
leave a full comparison along these lines to future work beyond the
scope of our case study focusing on Jewish Americans.

CHI ’24, May 11–16, 2024, Honolulu, HI, USA

The prior results related to job-specific memorization and potential IP dispossession further suggests that any groups whose
economic well-being is highly tied to job market participation in IP
heavy fields may be especially vulnerable to economic harms from
the deployment of any labor-replacing LLM-based technologies.
We compared the self-reported job category numbers from a
Pew Research study on Jewish Americans to U.S. Bureau of Labor
Statistics numbers on the distribution of American workers by job
category. While the BLS and job categories reported by Jewish
respondents to the Pew survey did not map directly to each other,
we were able to manually find some close mappings between them.
This process required us to manually map the BLS categories to the
Pew categories (which were not based on any formal taxonomy).
Based on this mapping, it seems likely that Jewish American
workers participate in several IP-relevant professions at high rates,
potentially around 4x for law and STEM.
Thus, it is also likely possible to support the broad argument
of our paper – that Jewish Americans and other minority groups
might be especially prone to IP dispossession and therefore to
economic harms – primarily using data on relative representation
of group members in different job categories and connecting these
job categories to LLM training data and LLM-replaceable labor.
In the future, it could make sense to investigate IP dispossession
targeted at other groups with many members in these fields. Alternatively, professional organizations may wish to lead the charge
themselves.
