---
title: "Can we trust Big Data? Applying philosophy of science to software"
person: "ramon-alvarado"
section: "by"
type: "journal-article"
year: 2016
date: "2016-09-02"
venue: "Big Data & Society 3(2)"
authors: "John Symons, Ramón Alvarado"
source_url: "https://journals.sagepub.com/doi/full/10.1177/2053951716664747"
retrieved: "2026-08-14"
content: "full-text"
notes: "Open access (CC BY-NC-ND). PROVENANCE: retrieved from the OpenAlex Content API copy (content.openalex.org/works/W2511674954.pdf) with Bearer auth, extracted with pdftotext -layout. DOI 10.1177/2053951716664747. OpenAlex W2511674954."
---

# Can we trust Big Data? Applying philosophy of science to software

## Full text

Original Research Article
                                                                                                                  Big Data & Society
                                                                                                                  July–December 2016: 1–17
Can we trust Big Data? Applying                                                                                   ! The Author(s) 2016
                                                                                                                  Reprints and permissions:

philosophy of science to software                                                                                 sagepub.com/journalsPermissions.nav
                                                                                                                  DOI: 10.1177/2053951716664747
                                                                                                                  bds.sagepub.com




John Symons and Ramón Alvarado



Abstract
We address some of the epistemological challenges highlighted by the Critical Data Studies literature by reference to
some of the key debates in the philosophy of science concerning computational modeling and simulation. We provide a
brief overview of these debates focusing particularly on what Paul Humphreys calls epistemic opacity. We argue that
debates in Critical Data Studies and philosophy of science have neglected the problem of error management and error
detection. This is an especially important feature of the epistemology of Big Data. In ‘‘Error’’ section we explain the main
characteristics of error detection and correction along with the relationship between error and path complexity in
software. In this section we provide an overview of conventional statistical methods for error detection and review their
limitations when faced with the high degree of conditionality inherent to modern software systems.

Keywords
Big Data, epistemology, software, complexity, error, Critical Data Studies




                                                                           decades. What can Big Data technologies allow users to
Introduction                                                               know, what are the limits of these technologies, and in
The surveillance and manipulation of individuals and                       what sense is Big Data a genuinely new phenomenon?
populations through computing technologies for com-                        Answering these questions is essential for guiding our
mercial or policy purposes raises a range of diﬃcult                       moral and political responses to Big Data.
philosophical questions. While the most pressing chal-                        Popular literature on Big Data is often dismissive of
lenges have an obvious ethical and political component,                    philosophy of science and epistemology. Popular
we need to understand what levels of control and                           authors and journalists frequently suggest that the rise
insight so-called Big Data allows before we can make                       of Big Data has made reﬂection on topics like causation,
informed decisions concerning its moral status. Thus, in                   evidence, belief revision, and other theoretical notions
the paper we argue for a careful assessment of the epi-                    irrelevant. On this view, the turn towards Big Data is a
stemic status of the computational methods that are                        turn away from concern with a range of traditional
currently in use. These technologies are deployed in                       questions in the philosophy of science.2 Big Data,
pursuit of particular pragmatic ends in the service of                     according to some, ‘‘represents a move away from
corporate and political missions. The actions of corpor-                   always trying to understand the deeper reasons behind
ations and political entities can be evaluated independ-                   how the world works to simply learning about an asso-
ently of the technology that they deploy. However, the                     ciation among phenomena and using that to get things
extent to which users of Big Data can accomplish their                     done.’’ (Cukier and Mayer-Schoenberger, 2013: 32)
goals depends on the epistemic status of those technol-
ogies.1 In many contexts, moral and epistemic ques-
tions are inextricably intertwined, and our goal here is                   Department of Philosophy, Lawrence, KS, USA
to help lay the necessary groundwork for moral and
                                                                           Corresponding author:
political engagement with Big Data by understanding                        John Symons, Department of Philosophy, University of Kansas, 1445
as clearly as possible how the appearance of Big Data                      Jayhawk Blvd., Wescoe Hall, Room 3090, Lawrence, KS 66045-7590, USA.
has changed the epistemic landscape over the past two                      Email: johnsymons@ku.edu


                 Creative Commons NonCommercial-NoDerivs CC-BY-NC-ND: This article is distributed under the terms of the Creative Com-
                 mons Attribution-NonCommercial-NoDerivs 3.0 License (http://www.creativecommons.org/licenses/by-nc-nd/3.0/) which permits
non-commercial use, reproduction and distribution of the work as published without adaptation or alteration, without further permission provided the
original work is attributed as specified on the SAGE and Open Access pages (https://us.sagepub.com/en-us/nam/open-access-at-sage).
2                                                                                                        Big Data & Society

This atheoretical turn makes the false assumption that         challenge associated with any software intensive prac-
more data means better inquiry. Worse than merely              tice, the problem of determining error distribution.
being a superﬁcial view of knowledge and inquiry, the          Another feature of software intensive science (SIS)
atheoretical stance is blithely uncritical towards the cor-    that philosophers have highlighted in recent years
porations and governments that use technology to ‘‘get         is the eﬀect that errors in code can have for the reliability
things done’’.3 The assumptions governing the atheore-         of systems. Horner and Symons (2014a), for example,
tical turn are false and, as we shall see, studying Big Data   explained the role of software error in scientiﬁc contexts.
without taking contemporary philosophy of science into         Although primarily epistemic in nature, such con-
account is unwise (Frické, 2015). Some of the limitations     siderations have direct implications for policy, law,
and risks involved in the use of computational methods         and ethics.
in public policy, commercial, and scientiﬁc contexts only          As several authors have noted, the term ‘Big Data’
become evident once we understand the ways in which            does not refer strictly to size but rather to a range of
these methods are fallible. Thus, in the broader social        computational methods used to group and analyze data
and political context, a precondition for understanding        sets (Arbesman, 2013; Boyd and Crawford, 2012). Thus
the potential abuses that can result from the deployment       one cannot responsibly address the epistemic status of
of Big Data techniques by powerful institutions is a care-     ‘Big Data’ without understanding the implications of
ful account of the epistemic limits of computational           the use of software for inquiry. We are not arguing
methods. A clear sense for the nature of error in these        that philosophers of science have simply solved all the
systems is essential before we can decide how much trust       epistemic problems related to Big Data. In fact, given
we should grant them and what, if any, limits to their use     the central role of software in Big Data projects, trad-
we should impose.4                                             itional accounts of epistemic reliability drawn from
   Coming to understand error and trust in these con-          philosophy of science are likely to prove inadequate
texts involves a range of philosophical and social-            for reasons we explain below.
scientiﬁc questions. No single scholarly or scientiﬁc dis-         For some philosophers, the increasingly dominant
cipline has the resources to respond to the questions          role of computational methods is not a matter of sig-
and challenges posed by the rise of Big Data. Critical         niﬁcant philosophical interest. On this view, there are
Data Studies is the interdisciplinary ﬁeld that has begun      no novel, philosophically relevant problems associated
to consolidate around the task of engaging with these          with the increased use of computational methods in
questions. Critical Data Studies has, understandably,          inquiry (Frigg and Reiss, 2009). Others, like Eric
focused on the important political and social dimen-           Winsberg (2010) and Paul Humphreys (2009) have
sions of Big Data. However, this work urgently requires        defended the view that computational modeling and
attention to the assumptions governing the use of soft-        simulation are associated with distinctive and novel
ware in the manipulation of data and in the conduct of         strategies for inquiry. Another recent line of inquiry
inquiry more generally.                                        that has direct bearing on Big Data involves the prob-
   We will argue that critical attention to the formal         lem of tackling error in large software systems. The
features of software is important if we are to get a           eﬀect that increasing software dependency has wrought
proper understanding of the relationship between Big           with respect to the trustworthiness of scientiﬁc investi-
Data and reliable inquiry. We are friendly critics of          gation carries over directly to Big Data. Big Data is
existing work in Critical Data Studies: Our contention         part of a changed landscape of problems associated
is that the ﬁeld has neglected highly relevant recent          with the use of computational methods in scientiﬁc
work in philosophy of science. Critical Data Studies           inquiry. While the term ‘Big Data’ rarely ﬁgures in
has correctly recognized that the technology underlying        the work of philosophers of science, there is now a
Big Data has changed the epistemic landscape in                large literature that discusses the role of software in
important ways, but has been unclear with respect to           science, particularly insofar as it relates to modeling
what these changes have been (Kitchin, 2014). Many of          and simulation (see for example Frigg and Reiss,
these changes have taken place with the advent of com-         2009; Humphreys, 2009; Morrison, 2015; Winsberg,
putational methodology in general, but more speciﬁc-           2010). Symons and Horner have pointed, for example,
ally with the integration of computer simulations into         to what they call the path complexity catastrophe in SIS
the toolkit of ordinary scientiﬁc practice. Thus, part of      (see 2014; Horner and Symons, 2014; Symons and
our purpose is to connect debates in philosophy of sci-        Horner, forthcoming). In this paper, we will argue
ence concerning the status of computational models,            that the path complexity catastrophe will have conse-
simulations, and methods with the emerging ﬁeld of             quences for Big Data projects. We will explain why Big
Critical Data Studies. To this end, we explain the role        Data, as a paradigmatic instance of SIS is especially
of epistemic opacity in computational modeling and             vulnerable to intractably diﬃcult problems associated
close with an example of a basic epistemological               with error in large software systems.
Symons and Alvarado                                                                                                      3

   In ‘‘Introduction’’ section we introduce the many           focus on the ambiguity concerning the sources of such
attempts to deﬁne Big Data and explain their limita-           limitations. These limitations, we argue, exemplify the
tions. This section has multiple aims. We begin by pro-        deﬁciencies of an atheoretical approach but most
viding an overview of Big Data as currently practiced.         importantly they also clearly characterize the intrinsic
Given the diverse uses of the term ‘Big Data’, in this         epistemic challenges posed by large software systems
section we stipulate a working deﬁnition that is precise       conventional methods of error detection, correction,
enough for our purposes and that faithfully reﬂects the        and general assessment.
main features of current usage. The second aim of
‘‘Introduction’’ section is to show the unavoidable con-
nection between the methods used in Big Data and the
                                                               What is Big Data?
software dependence mentioned above. We conclude               The term ‘Big Data’ arose in the context of challenges
that Big Data is an example of what Horner and                 facing engineers dealing with large data sets and limited
Symons call Software-Intensive Science. As such, Big           computational resources. For example, as noted by Gill
Data epitomizes the kind of inquiry to which philo-            Press (2013), Cox and Ellsworth (1997) introduce the
sophical debates concerning the role of computers in           term ‘‘Big Data’’ in their discussion of challenges invol-
science should apply.                                          ving the limitations due to memory storage constraints
   In ‘‘Big Data meets Critical Data Studies’’ section,        and processing speed for data visualization at the NASA
we do several things. First we provide an overview of          Ames Research Center. That paper focused on data sets
recent criticisms of Big Data that originate from the          that exceeded only 100 Gbytes. Attempts to partition
Critical Data Studies literature. We provide reasons           those data yielded segments that were too large for any
to think that although they may be important to the            researcher to work with given the tools and techniques of
overall characterization of Big Data, the tools deployed       the time. Speciﬁcally, desktop computers available to
by this interdisciplinary ﬁeld of study are excessively        individual NASA engineers in the mid-1990s faced
anthropocentric and social in their orientation and            memory and processing constraints that limited their
are the product of debates in philosophy of science            capacity to make good use of the data at their disposal.
and social epistemology that have been largely super-          Cox and Ellsworth (1997) call this ‘‘the problem of Big
seded by the developments in recent decades. Notably,          Data’’. Contemporary usage of the term ‘Big Data’ dif-
since they are generally related to science as a whole,        fers in signiﬁcant ways from this original context. It is
the insights that derive from socially and historically        common today for everyday data storage applications to
oriented scholarship from the 1960s to 1980s shed rela-        reliably exceed 100 Gbytes. While there are signiﬁcant
tively little new light on the use of software in scientiﬁc,   technical challenges involved in managing large
corporate, and policy settings.                                amounts of data, ‘‘the problem of Big Data’’ as charac-
   The best way to address some of the epistemological         terized in the 1990s is not the pressing concern it once
worries highlighted by the Critical Data Studies litera-       was.
ture is to attend to debates in the philosophy of science         Most, if not all, early deﬁnitions focused on resource
concerning computational modeling and simulation.              constraints and data set size. This is not the case today.
We provide a brief overview of the principal debates           In fact, as Boyd and Crawford (2012) note, many data
in ‘‘The epistemic status of Big Data’’ section. In par-       sets considered to be paradigmatic in the Big Data lit-
ticular, we focus on issues that relate to what Paul           erature today are smaller than those used to coin the
Humphreys (2009) calls epistemic opacity. ‘‘The epi-           term. They cite, for example, the small size of the data
stemic status of Big Data’’ section concludes by               sets involved in analyzing Twitter trends when com-
noting that the existing debate in both Critical Data          pared to low-tech research into often very large-scale
Studies and philosophy of science has neglected the            data sets generated by the US Census Bureau from the
issue of error management and error detection. This            Nineteenth Century. So, although ‘Big Data’ connotes
is an especially important feature of the epistemology         the use of large data sets, size is not an essential feature
of Big Data. In ‘‘Error’’ section we explain the main          of current usage of the term.5
characteristics of error detection and correction along           Other deﬁnitions (e.g. Chen et al., 2014) focus on the
with the relationship between error and path complex-          way the diﬀerent elements of a data set relate and inter-
ity in software. In this section we provide an overview        act. In some cases this is described in terms of the
of conventional statistical methods for error detection        dynamic interaction of the 3V’s: velocity, variety, and
and review their limitations when faced with the high          volume. Whether a set is deemed to be a Big Data set
degree of conditionality inherent to software systems          has to do with the dynamical constraints of these three
used in Big Data. And ﬁnally, in ‘‘Example’’ section           factors. Volume is of course size, but variety and vel-
we oﬀer an overview of the limitations exhibited by            ocity are less easy to deﬁne. Variety, for example has to
Google’s Google Flu Trends (GFT). In particular, we            do with the kind of data in the sets (i.e. pixels vs. nodes)
4                                                                                                     Big Data & Society

while velocity has to do with the physical and temporal        made in the existing literature, we think that the crit-
resources required to economically process a set.              ical scholarship to date has fallen short of addressing
Whether these three factors are suﬃcient to deﬁne Big          the distinctive epistemic features of Big Data. In part,
Data is a topic of ongoing discussion. Some cite the           this is because most criticisms are focused on the
extra V’s of veracity, value, and visualization as neces-      social level of analysis rather than on any distinctive
sary components of a working deﬁnition. However,               features of the technology of Big Data per se. That is
regardless of the number of V’s one includes, all of           to say, the focus has been on limitations due to
the deﬁnitions agree that analytical tools and methods         human-centered interactions such as inescapable cog-
are a core component of the deﬁnition of Big Data              nitive and social biases and the overall value-ladenness
(Chen et al., 2014).                                           of human inquiry. The basic conceptual point made in
                                                               the ﬁeld of Big Data studies is that data must be
                                                               interpreted and that interpretation is subject to
A working definition
                                                               human bias. We agree that the processes by which
In this paper we adopt what we think is the most faith-        data is selected and interpreted are important topics
ful deﬁnition of what Big Data means in contemporary           of study. However, they are not unique to Big Data.
practice. Here, we follow the analysis provided by Chen        Thus, in this section the development of Critical Data
et al. (2014) about the uses of the term in commercial         Studies will be connected to its focus on the distinctive
contexts. They review the range of deﬁnitions of Big           characteristics of Big Data rather than on consider-
Data given by leading corporations in data manage-             ations that could be addressed to human inquiry in
ment (for example, International Data Corporation              general. In this spirit, and for the purpose of this
(IDC), IBM, and Microsoft) before settling on IDC’s            paper, we focus on the analysis of error, error distri-
2011 deﬁnition. They preface their choice of deﬁnition         bution assessment, testing and reliability, as they
by stating that ‘‘Big Data is not a ‘thing’ but instead a      relate to the computational methods employed by
dynamic/activity that crosses many IT borders.’’ They          Big Data.
cite an IDC report from 2011 deﬁning Big Data as                  Error is an epistemic concept and the treatment of
follows:                                                       epistemic questions arising from Big Data is in its early
                                                               stage. In a recent article in this journal, for example,
    ‘‘Big Data technologies describe a new generation of       Rob Kitchin (2014) argues that there are three main
    technologies and architectures, designed to economic-      types of account concerning the epistemic implications
    ally extract value from very large volumes of a wide       of Big Data. He contends that these derive from diﬀer-
    variety of data, by enabling high-velocity capture, dis-   ing general perspectives on the nature of science held by
    covery, and/or analysis.’’ (Gantz and Reinsel, 2011 as     scholars investigating Big Data. The three perspectives
    quoted in Chen et al., 2014)                               he identiﬁes are the paradigmatic, the empirical, and
                                                               the data-driven. Big Data theorists who follow a para-
This deﬁnition serves to highlight the most important          digmatic—or Kuhnian model—of scientiﬁc inquiry
and distinctive characteristics of Big Data, namely its        suggest that science normally functions within settled
use of statistical methods and computational tools of          patterns and only occasionally advances via radical
analysis. It will be particularly important to consider        shifts in methodology. Advocates of this view contend
this deﬁnition in detail in ‘‘The epistemic status of Big      that the advent of Big Data constitutes a paradigm shift
Data’’ section. It is in this section that the epistemic       of the sort described by Kuhn (Kitchin, 2014). That is,
status of Big Data is discussed and in which the case          that Big Data has indeed revolutionized not only the
is made that Big Data, insofar as it is an intrinsically       methods by which we conduct science but also the goals
computer-based method of analysis deployed in                  of scientiﬁc inquiry per se. The second camp is that of
inquiry, is a SIS par excellence. Thus, this deﬁnition         the empiricist.7 The motto of this camp is ‘‘the death of
is particularly apt since it clearly captures the interplay    theory’’ (see Anderson, 2008; Cukier and Mayer-
between the epistemic, normative, and economic                 Schoenberger, 2013; Steadman, 2013). They regard
dimensions of Big Data. Most importantly, this deﬁn-           the advent of Big Data and its capacity to detect pat-
ition will highlight the limitations concerning error          terns as replacing theoretical analysis with unrestricted
assessment characterized in ‘‘Error’’ section.                 sampling. On this view, raw data and correlation pat-
                                                               terns are suﬃcient for scientiﬁc development. In this
                                                               camp, terms such as causation, paradigmatic of scien-
Big Data meets Critical Data Studies
                                                               tiﬁc inquiry for centuries past, even in their conven-
This section presents and clariﬁes what we take to be          tional use in science, are regarded as being elusive
some of the most signiﬁcant critical studies of Big            and possibly even occult. The third camp, the data-
Data.6 Although we agree with many of the observations         driven one, is a hybrid of sorts in that ‘‘it seeks to
Symons and Alvarado                                                                                                     5

generate hypotheses and insights ‘born from the data’        theories, practitioners, and legacy methodology alike
rather than ‘born from theory’’’ (Kelling et al., 2009 as    (Kitchin, 2014).
cited by Kitchin, 2014). According to Kitchin (2014), a         As mentioned above, other Critical Data studies’
data-driven science is one whose epistemological strat-      authors provide similar criticisms of Big Data. Take
egy is to use ‘‘guided knowledge techniques to identify      Boyd and Crawford (2012), for example. In their article
potential questions (hypotheses) worthy of further           (2012) they address the ‘‘death of theory’’ camp, or
examination and testing.’’ (Kitchin, 2014) This last         ‘empiricists’, by questioning their implicit claims to
camp recognizes a role for conventional scientiﬁc            objectivity. They attack these claims because, according
terms and methods beyond mere pattern recognition,           to them, they are ‘‘necessarily made by subjects and are
but its hypotheses are derived from the data itself and      based on subjective observations and choices.’’ (Boyd
not ‘‘just’’ from guiding theoretical principles.            and Crawford, 2012) They also criticize assumptions 1
   Kitchin (2014) criticizes the ﬁrst two camps, focusing    and 2 by pointing that massive amounts of raw data are
primarily on claims made by those advocating the end         meaningless unless a question is posed, an experiment
of theory.8 According to Kitchin, the so-called empiri-      standardized and a sample curated (2012). All of which
cists have four main claims concerning the scope, reach,     are subjective endeavors. This is an insight drawn from
and assumptions of Big Data:9                                historically and socially oriented philosophy of science.
                                                             Kuhn’s work (1962) has been especially inﬂuential here,
1. full resolution (N ¼ All),                                along with the critical work of philosophers like
2. no a priori (theory/model/hypothesis) needed,             Longino (1990) and others.
3. agnostic data, and                                           While Kuhn, Longino, and other mid-to-late 20th
4. domain transcendence (the assumption that unre-           century philosophers have helped shape the contribu-
   stricted pattern recognition does away with scientiﬁc     tions of many in the Critical Data Studies community,
   specialization).                                          the project of understanding Big Data can beneﬁt from
                                                             taking advantage of additional philosophical resources.
   Given that many problems involving Big Data tech-         Acknowledging that human bias inﬂuences inquiry is a
niques are of a dynamic nature, in real time and invol-      reasonable, but relatively trivial philosophical observa-
ving changing demarcations and inputs, the N ¼ All           tion.11 Since it is applicable to all forms of inquiry at all
option is oﬀ the table10 (Bollier and Firestone, 2010).      levels (Longino, 1990), the recognition of bias is not a
That is to say, in a constantly dynamic landscape, like      contribution that adds anything distinctive to the study
the ones often involved in Big Data problems, one can        of Big Data.12 This is particularly the case considering
never be said to have all the data. However, for Kitchin     the developments computer technologies deployed in
the problem lies elsewhere. He thinks that the problem       the aid of science have undergone precisely in the last
has rather to do with sampling bias that originates in       70 years. Unfortunately, the inﬂuence of relativistic
the technology deployed, the collection methods, and         philosophy of science has impeded the development
the data ontology employed in the process. In other          of analyses of the epistemic questions that arise in the
words, the problems with one above have to do with           context of Big Data.
subjective limitations and biases of the agents conduct-        Similarly, the emerging ﬁeld of Software Studies,
ing the inquiry. This argumentative strategy is not          which attempts to develop critical perspectives on the
unique to Kitchin. It can be found in other widely           development and use of software, often relies on philo-
cited authors in the Critical Data Studies literature        sophical literature that although interesting in its own
(see for e.g. Boyd and Crawford, 2012) for whom the          right, is orthogonal to the core questions that arise
nature of the problems themselves (i.e. dynamic, real-       from the use of software. This is particularly problem-
time problem solving) is not recognized as a constraint      atic since some in the ﬁeld of Software Studies want to
on the quest for full resolution. Instead, they argue that   argue that the use of computational methods, in par-
constraints are due to the subjectivity inherent in the      ticular their capacity to deal with immense data sets in
choice of discretization and the highly value-laden          science and policy-making, does in fact bring about
social aspects of inquiry that inevitably come into play.    novel issues to explore (see Amoore, 2011, 2014;
   Similarly, ‘empiricist’ assumptions 2 and 3 are           Berry, 2011). Take the following example. In his book
rejected by Kitchin on the grounds that whatever meth-       The Philosophy of Software, David Berry (2011) deﬁnes
ods allow us to collect and analyze data are already         software studies as a research ﬁeld that includes discip-
theory/model-laden to begin with. He explains that           lines as broad as platform studies, media archaeology,
‘‘data are created within a complex assemblage that          and media theory, all of which focus on the develop-
actively shapes its constitution’’ and that ultimately,      ment, use, and historicity of hardware, operating sys-
identifying patterns in data ‘‘does not occur in a           tems, and even gaming devices (Berry, 2011). Berry
scientiﬁc vacuum’’ and is ‘‘discursively framed’’ by         argues that these technologies not only oﬀer novel
6                                                                                                     Big Data & Society

insight into the human experience, but that they are          involves the use of computational methods. The two
also a novel part of it. However, the philosophical           principal areas of philosophical inquiry that have
resources that he applies to these issues are restricted      been missing from Critical Data Studies to date are
to authors like Kuhn and Heidegger. While these are           contemporary philosophy of science and philosophy
deeply signiﬁcant ﬁgures in the history of philosophy,        of computer science. Connecting these debates to phil-
they oﬀer limited insight into the novel epistemic fea-       osophy of computer science is beyond the scope of the
tures of computational methods such as Big Data.              present paper.14 Instead, for the remainder of this
    Consider another prominent ﬁgure in software stu-         paper, we will demonstrate the relevance of more
dies: Louise Amoore. She addresses security risks in          recent and growing literature on software, models,
ways that are relevant to the discussion of Big Data.         and simulations, in the philosophy of science to ques-
She argues that modern security risks’ calculations can       tions of reliability and error in Big Data.
be understood by analogy with ﬁnancial derivatives
(Amoore, 2011). She oﬀers an analysis of the implica-
                                                              The epistemic status of Big Data
tions of Big Data in risk assessment in the context of
border security policy (Amoore, 2011). On her view,           The most distinctive aspect of Big Data, as we argued
risk posed by individuals can be understood as a prod-        above, is the prominence of computational methods
uct of correlational patterns that derive from assorted       and in particular the central role played by software.
data sets that include origin and destination of travel,      What are the novel epistemic challenges brought about
meal choice, etc. Security risk, according to her, is con-    the use of computational methods? Although there is a
strued as an emergent phenomenon, not reducible and           broad debate in philosophical literature about the epi-
frequently not directly related to the components from        stemic implications of the ‘introduction of computers’
which it arises. Financial derivatives, she argues arise in   into scientiﬁc inquiry15 (see Barberousse et al., 2009;
the same manner (Amoore, 2011). What she means here           Frigg and Reiss, 2009; Humphreys, 2009; Winsberg,
is that derivatives are not mere aggregations of ﬂuctu-       2010), it is important to recognize, following the work
ation in market stocks or patterns in debt, but are           of Evelyn Keller (2003) that this introduction took
instead a ﬁnancial instrument in their own right.             place gradually in a series of distinguishable stages
Because of the fragmentation and manipulation of              from the end of the Second World War until relatively
values derived from more conventional ﬁnancial instru-        recently. Evelyn Keller (2003) argues that just as the
ments, derivatives manage to have novel ﬁnancial prop-        introduction of computers was itself a gradual process
erties that are speciﬁc to them. According to her, the        that posed distinct challenges in distinct disciplines for
same can be said about risk assessment of individuals         diﬀerent reasons, the epistemic challenges emerged in
crossing borders that emerge from risk-based security         diﬀerent disciplines at diﬀerent times and at diﬀerent
calculations in contemporary security practice. The risk      stages of technological innovation.
travelers pose, although derivative of certain speciﬁc            Fox-Keller identiﬁes three main stages. The ﬁrst
choices and information about an individual, is often         begins with the use of computers to overcome the prob-
an independent feature that is not found in any of these      lem of mathematically intractable equations in the con-
choices and informational sets but as a product of an         text of research at Los Alamos in the years immediately
emergent whole. Although Amoore is indeed talking             following the Second World War.16 This stage repre-
about the inherent features of Big Data systems here,         sents an important deviation from conventional analyt-
like those involved in border-crossing security systems,      ical tools of the sciences at the time because it directly
we ﬁnd that she relies heavily on an anthropocentric          challenges the well-established use of diﬀerential equa-
treatment of risk that focuses on policy and decision-        tions as the main tool in the physical sciences (Keller,
making rather than on the distinctive features of those       2003). However, when computers were being used at
systems.13 Big Data systems also involve risks that are       this stage the primary concern was still to ‘simulate’
due not only to the eﬀects of design or policy choices,       conventional diﬀerential equations and their probable
but also from the nature of the software systems them-        solutions using Monte Carlo methods (Metropolis and
selves. While Amoore correctly points to the emergent         Ulam, 1949). In this respect the Monte Carlo methods
features of large complex systems as important areas of       are directed towards the solution of equations and are
inquiry, we think that the most important epistemic           removed in one step from the phenomena described by
problems facing them are due to the characteristic fea-       those equations. In other words, methods such as the
tures of software systems themselves and not mere con-        Monte Carlo method were not deployed to simulate
tingent limitations on the part of agents.                    any system, but rather to provide a wide range of pos-
    Insofar as Critical Data Studies understands itself to    sible solutions to diﬀerential equations later deployed
be addressing a distinctive area of research, scholars in     in order to understand a given system. With time, stat-
this ﬁeld ought to recognize that Big Data, at its heart,     istical approaches to problem solving (like Monte
Symons and Alvarado                                                                                                   7

Carlo) oﬀered a practical alternative to the diﬀerential     projects are generally not detached from speciﬁc prac-
equations themselves (Keller, 2003).17                       tical applications, nor do they involve testing or
   The second stage, according to Fox-Keller, has to do      demonstrating new theoretical frameworks.23 Big
with the use of dynamic models as representations of a       Data is a relatively conservative and pragmatically
target system, or ‘‘approximate analogous systems’’          motivated application of computational techniques,
(Frigg and Reiss, 2009). That is to say, the use of com-     especially when compared with examples of the third
puterized calculations was conﬁned ‘‘to follow the           part of Fox-Keller’s taxonomy.
dynamics of systems of idealized particles’’ (Keller,            What is meant by calling Big Data software intensive
2003). In this stage, scientists were no longer merely       is relatively straightforward. Computer scientists call a
simulating possible solutions to diﬀerential equations       system software intensive if ‘‘software contributes
but rather working under an assumed isomorphism              essential inﬂuences to the design, construction, deploy-
between the observed behavior of a phenomenon and            ment, and evolution of the system as a whole.’’ (IEEE,
the dynamics expressed by the artiﬁcial system, or com-      2000) Given this deﬁnition, by almost any standard, Big
puter model, constructed to track its idealized develop-     Data, like much of contemporary science, is software
ment. In other words, the aim was to simulate ‘‘an           intensive.24
idealized version of the physical system.’’ (2003) Fox-          One aspect of the heavy reliance on software by sci-
Keller identiﬁes two levels to the use of simulations in     entiﬁc or commercial enterprises is to say that the kinds
this second stage: (1) substitution of the natural for the   of insights available via computational methods would
artiﬁcial system, and (2) replacement of the diﬀerential     not be available without the use of software. Embedded
equations at the ﬁrst level for discrete, ‘‘computation-     in many of the deﬁnitions of Big Data is the assumption
ally manageable’’, processes.18 This second stage            that even just given the vast amount of information
already posed a challenge to the conventional epistemic      involved, no equation worked by paper and pencil
relation between theory construction and modeling.           could in practice be deployed to deal with it (Bryant
That is, while the mathematical formulations of the          et al., 2008). In other words, Big Data deals with prob-
diﬀerential equations had strong and direct ties to the-     lems where insights would be practically impossible
oretical principles to back them up, the discretized ver-    without the help of computers.
sions were now merely approximations without a direct            Big Data can also address problems involving com-
link to the underlying theory (Winsberg, 2010).              plex systems where the relevant dynamics are not obvi-
Nevertheless, what these simulations attempted to            ously accessible except through surveying vast amounts
represent were entire theories and some would say            of data (see Symons and Boschetti, 2013). In addition
that it is only in this second sense that the proper use     to those problems which would simply require raw
of the term ‘simulation’ in its current usage enters the     computing power beyond our innate capacities there
computational terminology (Hugues, 1999, as cited by         are also analytically intractable problems that require
Keller, 2003).19                                             simulation by computer rather than admitting of ana-
   Finally, the third stage, according to Fox-Keller, is a   lytic solutions.25 Big Data is generally not deployed
reliance on the analysis and model-building of particu-      because the problems in question are analytically
lar and localized systems rather than generalized theor-     intractable. However, as we shall see below, computa-
etical ones. Foregoing the wide scope of a full              tional models of the kind that are central to Big Data
theoretical framework, this approach focused on the          are of great interest precisely because they promise new
modeling of internally consistent mechanisms without         ways to explore phenomena that are diﬃcult to exam-
generalizable principles or wide ranging laws at their       ine by other means (Barberousse and Vorms, 2014;
core. As Keller (2003) notes, this change has important      Boschetti et al., 2012). As Symons and Boschetti
implications for scientiﬁc explanation (see also Symons,     (2013) note, computational models are currently allow-
2008).20 This third stage, according to Keller, departs      ing research into topics where cognitive, ethical, polit-
from the ﬁrst two in that it ‘‘is employed to model          ical, or practical barriers would otherwise loom large.
phenomena which lack a theoretical underpinning in           Whether in nuclear weapons testing, climate science,
any sense of the term familiar to physicist.’’ (2003)21      studies of the behavior of epidemics, or studies of the
   Big Data falls somewhere between ﬁrst and second          internal dynamics of stars, to take just a handful of
stage of Fox-Keller’s taxonomy. Big Data, we will            cases, computational models are often the only viable
argue, is a software intensive enterprise that is focused    research tool for scientists (2012: 809). Similarly, appli-
on revealing patterns that can be used for commercial,       cations of Big Data science to epidemics, energy usage,
political, or scientiﬁc purposes.22 Unlike the third stage   social movements, and the like all have the property of
applications of computational models that Fox-Keller         generating results that are otherwise inaccessible (at
describes, applications of Big Data are intended to          least within any practical timescales and resource con-
reveal features of natural or social systems. Big Data       straints) without the use of software.
8                                                                                                     Big Data & Society

    Another way of thinking about the intrinsic reliance    (Weisberg, 2013) whose key insights derive from the
of Big Data on software is to focus not only on its         dynamic nature of the visualization (Bollier and
methods but also on the nature of its results. These        Firestone, 2010).27
results mainly involve pattern discovery. We analyze a
set of granular data points in order to detect relational
                                                            Epistemic opacity
structures. Consider twitter trends. Millions of short
texts are mined to ﬁnd concurrent terms or combin-          Among the most challenging philosophical problems
ations thereof. These are in turn correlated to other       facing Big Data as a SIS is assessing its role in the
factors related to the authors, i.e. gender, geographic     process of creating, gathering, and uncovering new
location, etc. Patterns emerge. But the way we arrive at    insights and knowledge. The scientiﬁc status of Big
such patterns is through the statistical analysis of cor-   Data is a topic of ongoing debate. Lazer et al. (2014)
related data points. Whether these results are conveyed     have argued that most prominent applications of Big
via visualizations or mathematical formulas they are        Data are not properly scientiﬁc insofar as the sources of
the result of very large numbers of computations. As        data are unreliable. Speciﬁcally, they argue, the data
discussed above, even just considering the number of        that serve as the basis for Big Data projects are not
available data points, these methods are computational      derived from scientiﬁc instruments (Lazer et al., 2014).
and they are so as a matter of practical necessity.            By contrast, philosophers of science have debated
    Consider attempting to understand what is going on      whether computer-based methods generate models
inside a star like our Sun. We can know facts about the     that are closer to theoretical abstractions or to empir-
center of the Sun. We have indirect means of learning       ical experiments (Barberousse and Vorms, 2014;
about chemical composition through spectral analysis        Morrison, 2015).28 Addressing the epistemic challenges
and the like, but other than that, the only ways to draw    of computational methods in science Paul Humphreys
inferences about the processes taking place under the       (2009) argues that the central problem is the mediation
surface of the sun are those made available to us via       of our epistemic access to the phenomena of interest.
computational models. This applies almost by deﬁn-          This is because computational methods can involve an
ition (Gantz and Reinsel, 2011) to phenomena con-           ineliminable ‘‘epistemic opacity’’ (Barberousse and
sidered paradigmatic in the Big Data literature. This       Vorms, 2014; Humphreys, 2009), which Humphreys
is because many of the insights brought about with          deﬁnes in the following way:
Big Data techniques would otherwise be unavailable,
or simply neglected by other analytical methods. Thus         ‘‘A process is epistemically opaque relative to a cogni-
Big Data science is unavoidably software dependent.           tive agent X at time t just in case X does not know at t
    In addition to being an intrinsically computational       all of the epistemically relevant elements of the pro-
method, the value of Big Data derives from the patterns       cess.’’ (Humphreys, 2009)
it extracts and the correlations revealed thereby.
However, this means two things. First, tied to the          Epistemic opacity, understood in this sense is not a new
notion of pattern recognition and correlating millions      feature of scientiﬁc inquiry, nor is it unique to compu-
of bits of data comes the need to visualize them. Such      tational methods. Humphreys recognizes that a parallel
patterns and their insights would be of no use if they      issue arose with the emergence of Big Science, i.e. when
were presented to us solely via a spreadsheet and a         scientiﬁc inquiry became an ineliminably social endea-
mathematical function for example. As we discussed          vor in which no individual was in control of the com-
above the term Big Data was coined because of the           plete process of inquiry (Humphreys, 2009; Longino,
challenging constraints of memory and processing            1990). However, Humphreys regards the computational
power but more particularly as they relate to visualiza-    turn in science as generating a qualitatively diﬀerent
tion.26 Beyond the challenge of static visualization,       form of epistemic opacity. Some of the problems stem
many problems in Big Data involve real time inputs          from lower level operational issues such as the seman-
and processing and as such we can say that Big Data         tics of computational processes. In a relatively obvious
does not just create a static representations but rather    sense, human-level computer languages are already
creates artifacts that are more akin to scientiﬁc simula-   highly mediated with respect to machine-level imple-
tions. This is the case for example in the case of          mentation. This results simply from being compiled
Numerical Weather Prediction systems which not              through several syntactic layers in order for code to
only process past data to predict future occurrences        be accessible to human programmers. Another example
but also compare the model’s output to real time sen-       at a higher level are unavoidable numerical discret-
sors tracking the weather (Bauer et al., 2015). It is in    ization choices that enable higher-order representa-
this sense that the model ceases to be merely an            tional features such as visualizations (Humphreys,
explanatory representation and becomes a simulation         2009). According to Humphreys, both features of
Symons and Alvarado                                                                                                9

computational techniques represent novel instances of       central issue is the bias and subjectivity inherent in
epistemic opacity.                                          interpretation. The consequences of this epistemic opa-
    One concrete example of how the social nature of        city are not easily solved through some simple ﬁx or
software contributes to epistemic opacity in a novel        revision of appropriate methods to deal with them.
way is the eﬀect of so-called ‘‘legacy code’’. This is      Computational methods, as Humphreys argues are
programming code that has been built by engineers           ‘‘essentially epistemically opaque’’ (Humphreys, 2009).
either using programming languages that have fallen         A process is essentially opaque in this way to an agent
out of favor or that for some other reason may be dif-      at ‘‘if it is impossible, given the nature of X, for X to
ﬁcult for later programmers to understand. Coding is a      know all of the epistemically relevant elements of the
highly creative engineering task and although the code      process’’ (Humphreys, 2009).
may do its job appropriately there may, occasionally be         This last formulation of epistemic opacity serves to
no way for contemporary users to know exactly how it        elucidate the kinds of epistemic challenges at play in
achieves its function (2009). As a matter of fact, legacy   our discussion, namely those that are features of the
code is common in computer science. One could argue         systems in questions and not merely contingent limita-
that certain analogous legacy methods or processes are      tions of individual researchers or of teams of research-
part of traditional big-science projects. However, unlike   ers. As such, it also serves to distinguish the general
say a scientiﬁc instrument whose inner workings are         concept of epistemic opacity from a related issue con-
well-understood, it may not be evident how some             cerning the concept of black boxes in systems ana-
piece of legacy software contributes to the functional      lysis.30 Black box theory is in principle a
role of the whole piece of software. One could easily       mathematical approach that allows for schematization
imagine being able to reverse-engineer the functionality    of non-linear functions between an input and a result
of non-software aspects of a scientiﬁc project if one       without the need to know exactly what the internal
knew its function. However, it is not always the case       structure of the function is or without particular
that one can understand the function of legacy code in      regard to the nature of the input or results (Bunge,
some large system.                                          1963). It was later adopted by emerging ﬁelds in the
    When dealing with legacy code it may prove easier       study of complex systems (Ethiraj and Levinthal,
and more viable to merely work around the already           2004) and business related issues concerning organiza-
functioning code, even if no one actually understands       tional structures and product design (Brusoni and
it.29 In big, ongoing projects it is often economically     Prencipe, 2001). Although black boxes and epistemic
unfeasible to discard the legacy code and begin from        opacity are related in that both are issues concerning
scratch (Holzmann, 2015). This is particularly the case     gaps in knowledge of a given system, they are very dif-
with critically important systems whose operation           ferent concepts. In particular, black box theory is more
cannot be interrupted like ﬂight control software. In       of a pragmatic approach to an information system that
such cases the system must be kept running as it is         can function in a need-to-know basis. That is, it is an
being patched or updated.                                   attempt to schematize in a formal manner an informa-
    There are other distinctive sources of epistemic opa-   tion system with the minimum amount of information
city resulting from the use of computational methods        possible being transmitted from one state to the next
that have no parallel in other aspects of conventional      and to do so despite possible limitations. Epistemic
scientiﬁc inquiry. Consider weak emergence. Weak            opacity on the other hand is concerned with more
emergence is characterized by the emergence of unin-        than just the pragmatic constraints associated with spe-
tended/non-programmed/unexpected behavioral pat-            ciﬁc methods or technologies. It is about the nature of
terns in running simulations (Humphreys, 2009).             knowledge per se and in particular about the ways in
Patterns that were not known before the simulation          which knowledge can be conveyed or can fail to be so.
was turned on and ran (for more on this see Symons,         Black boxes are just one of the many instances of epi-
2002, 2008). Weakly emergent phenomena are charac-          stemic opacity. In other words, all black box problems
terized, among other things, by their dependence on the     are instances of epistemic opacity but not every
actual running of a simulation. That is to say, there       instance of epistemic opacity is a black box. But more
would be no way of having found those patterns              importantly, not all black boxes are instances of essen-
apart from running the simulation itself. They are the      tially opaque processes.
product of the actual dynamics of the simulation and
cannot be deduced from nor reduced to any of the
                                                            Error
elements that conform it (Bedau, 1997).
    Reliance on computational methods involves a dis-       Humphreys’ argument that computational methods
tinct kind of epistemic opacity from the social epistem-    suﬀer from epistemic opacity is strengthened when we
ology aspects of human-centered inquiry where the           consider the role of software error (see also
10                                                                                                       Big Data & Society

Barberousse and Vorms, 2014; Floridi et al., 2015;              simulations as a method that helps scientist assess
Newman, 2015).31 In this section, we examine the role           whether some source of error is absent in an experiment
of error in software intensive systems and explain why          by estimating ‘‘what they would be more or less likely
traditional approaches to handling error in a scientiﬁc         to observe if [any] source of error were present in the
context fall short. As brieﬂy stated above, by error we         experiment.’’ (Parker, 2008) Thus, we can have severe
simply mean the many ways in which a software system            testing of hypotheses concerning possible sources for
may fail. This may include erroneous calculations,              error in a particular experiment. For now, this ﬁrst
implementations, results, etc. The important point              step allows Parker to make the case that computer-
here is not error per se but our epistemic relation to it       based methods are a reliable source of evidence at
in the context of inquiry.                                      least with respect to sources of error in experiments
    Scientiﬁc claims are often—if not always—of a stat-         given Mayo’s account. When computer-based methods,
istical nature (Mayo and Spanos, 2010). Increasingly            such as simulations, are about a system that is not a
sophisticated manipulation, interpretation, and accu-           conventional experiment and for which we have no
mulation of data have made the probabilistic aspect             real-world access the same approach can be applied
of scientiﬁc claims become more pressing (see Keller,           according to Parker. Parker appeals to Mayo’s account
2003; Metropolis and Ulman, 1949). In light of the              in the following way.
statistical nature of contemporary science Deborah                 Simulation results are good evidence for H to the
Mayo has called for a new philosophy of statistical sci-        degree that:
ence in order to account for error and probability
inherent in modern scientiﬁc inquiry (Mayo and                   (i) results ﬁt the hypothesis, and
Spanos, 2010). Mayo proposes what she calls ‘severe             (ii) the simulation wouldn’t have delivered results that
testing’. A method by which a given hypothesis is said               ﬁt the hypothesis if the hypothesis had been false
to have various degrees of reliability depending on how              (Parker, 2008).
likely it is to have been falsiﬁed by a test. Unlike trad-
itional accounts of conﬁrmation, error-based statistical           For Parker one task is to ensure that (ii) holds. If (ii)
assessments such as Mayo’s measure the ability to               holds then we can apply Mayo’s notion of evidence to
choose from one hypothesis over another by virtue of            simulation experiments. This is even if such simulations
the extent of error-detecting testing methods applied to        are of the kind that cannot be immediately compared to
it. The degree to which these tests are able to detect          actual data from a system, like those simulations that
error determines their severity. A hypothesis that is           have to do with future states of a system. An example
tested with methods that have a high likelihood of ﬁnd-         of these simulations could be computer experiments
ing errors in it is said to pass a severe test. Severity is     seeking to predict future weather patterns (Parker,
formally deﬁned as follows:                                     2008). According to Parker, appeal to lower level sever-
                                                                ity tests, as explained above, can ensure that (ii) is the
     A hypothesis H passes a severe test T with data x0 if      case. That is, by making sure that errors that could
     1. x0 agrees with H, and                                   have been part of the simulation are absent from the
     2. with very high probability, test T would have pro-      simulation we can then say that simulations are good
        duced a result that agrees less well with H than does   sources of evidence and thus we can rely on them.
        x0, if H were false or incorrect.                       Parker oﬀers a taxonomy of error to help supplement
                                                                her point. Although this taxonomy in itself may have its
    Informally, the severity principle suggests that a          limitations and problems (i.e. see Floridi et al., 2015)32
high degree of trust is warranted in cases where a              Parker thinks that while it is unclear that there are in
hypothesis is not shown to be wrong in the face of              fact procedures that allow us to assess the magnitude of
tests that have a high probability of ﬁnding it wrong if        some error’s impact,33 the list nevertheless provides evi-
the hypotheses were indeed false (Parker, 2008).                dence that ‘‘we do have some understanding of the dif-
Further, Mayo suggests that concentrating on choos-             ferent sources of error that can impact computer
ing among highly probed hypotheses is crucially dis-            simulation results.’’ (Parker, 2008)34
tinct from those approaches that rely on highly
probable ones. In the former case we have a stronger
positive account for falsiﬁcation.
                                                                Path complexity and Big Data
    Wendy Parker (2008) argues that Mayo’s error-sta-           As discussed above, Big Data is a software-intensive
tistical approach, and in particular her severity prin-         science. Given this dependence on software, as we will
ciple can help make the case for the epistemic import           see below, testing applications of Big Data using con-
of computer-based methodology in science. This is               ventional statistical inference theory (CSIT) is not an
because, according to her, Mayo explicitly accepts              option. The reason for this is primarily due to the role
Symons and Alvarado                                                                                                  11

of conditionality in software (Horner and Symons,            into epistemically manageable modules we may indeed
2014; Symons and Horner, 2014).                              be able to carefully test each and every one of them
    The challenge is that for every conditional statement    independently and thus have a reliable error assessment
in piece of code the number of possible paths that must      of the system as a whole. If this is the case then, we can
be tested grows. Pieces of code frequently contain con-      independently rely on each of them and by extension on
ditional statements or their equivalents, that is, they      all of them together. At ﬁrst sight this sounds like a
take the form of ‘‘if. . .then/or else’’ statements. Thus,   plausible approach to the problem of path complexity
if a 10 line-long program has a conditional of this kind     in particular and epistemic opacity in general.
the lines to be tested would doubled to 20. Each of these    However, path complexity grows at catastrophic rates
conditionals augments the lines of code to be tested         even given relatively small numbers of lines of code.
exponentially. Each conditional line of code alters the      The interplay between modules will introduce untested
number of paths available to a given program. This           paths even in cases where the modules themselves are
increases the program’s path complexity. Assessment          reliable. The discussion above about the obstacles to the
of error distribution directly relates to degrees of reli-   deployment of conventional statistical methods shows
ability when testing software. Standard statistical tech-    that even at a smaller scale the only truly available test-
niques demand some degree of random distribution in          ing technique for assessment of error distribution would
the sample of interest. This element of random distri-       be an exhaustive brute force one. Even if we were to
bution is not available in the context of software test-     grant that massive modularity and exhaustive testing
ing. While random distributions are a reasonable             was a viable method for software design and testing,
assumption in natural systems, this is not the case in       integrating modules will result in epistemic opacity.
software systems since it is not feasible ahead of time to       Although modularity may indeed make black boxes
exclude the possibility that the distribution of error is    a bit more manageable, the dynamics among the mod-
caused by a non-random element in its constitution.          ules would quickly evolve into a particularly complex
Thus there is simply no way, other than by assumption        system with its own problems. One immediate concern
or by exhaustive testing, to know whether or not a par-      is the assumption that software (and indeed any other
ticular error distribution in software is the product of a   modular system) develops as a cohesive, all-encompass-
random element or not (Symons and Horner, forth-             ing unifying endeavor rather than as a patchwork
coming). Thus, there is no way, other than by mere           (Winsberg, 2010).
(unwarranted) assumption, to legitimately deploy stat-           While uniﬁcation and modularity can be part of a
istical techniques that demand that the error distribu-      protocol for future software development, it is not cur-
tion in a system have some degree of randomness to it.       rently in place and the question remains as to whether it
As exempliﬁed by the discussion on path complexity,          can be implemented in scientiﬁc inquiry and the large
brute force attempts at exhaustive testing, as Symons        software systems that already underlie it. Take climate
and Horner argue, for any conventional program is an         modeling for example. When considering climate
impractical task given meaningful time constraints.          models, Winsberg (2010) cites at least three kinds of
    Even the simplest computer programs have 1000þ           uncertainty that have to be taken into consideration:
lines of code and an average of one conditional state-       structural uncertainty, parameter uncertainty, and
ment per every 10 lines. Thus, for example, the time         data uncertainty. The most important source of uncer-
resources required for testing a program with 1000           tainty for our current discussion is structural uncer-
lines of code with this average of conditionals would        tainty of the model itself, which includes
exceed many-fold the age of the universe.35 A program        considerations regarding ‘‘a plethora of auxiliary
consisting of 1000 lines of code would be a very small       assumptions, approximations, and parameterizations
program for anything in the Big Data context. Most           all of which contribute to a degree of uncertainty
computer programs used in these context are large            about the predictions of these models.’’ (2010) Each
and in scientiﬁc applications more generally are com-        of these assumptions, approximations, and parameter-
monly in the hundreds of thousands of lines of code          izations is based upon segments, or modules of soft-
(Horner and Symons, 2014; Symons and Horner, 2014).          ware code that implement them. Let us for a second,
    The most important consequence of the path-              in a very simplistic and rough way, think of each of the
complexity catastrophe is the fact that statistical meth-    many modeling layers that go into the software that
ods no longer apply in a straightforward manner to the       predicts climate as modules. Even if we exhaustively
detection of error in software system.                       specify/test each module, the interactions among mod-
    It may be countered that modularity in software sys-     ules, their epistemic transparency, and therefore their
tems may be a way to diminish the impact of path com-        reliability as a functioning system them won’t be as
plexity and thus reduce the epistemic opacity related to     straightforward. Consider, for example, that after
it.36 Perhaps, it can be argued, by breaking a system        70þ years of climate modeling the complexity
12                                                                                                   Big Data & Society

surrounding the integration of so many diﬀerent (one         moments for GTF. One of them was the fact that it
may argue modular) systems/models has only allowed           failed to predict the A/H1N1 ﬂu pandemic in 2009.
scientist to claim a degree of accuracy that averages        This led Google to actually modify its original algo-
merely a day per decade (Bauer et al., 2015). That is,       rithm in an attempt to get more accurate results.
after seven decades, and the use of the most sophisti-       However, the second problem was that GTF suﬀered
cated and powerful software, the integration of the          from general gross overestimation. In particular, it
multiple modules of climate modeling is anything but         overestimated by a large margin 100 times out of 108
done. If anything this example elucidates the diﬃculty       during the ﬂu season between 2011 and 2012 (Lazer
of managing integration of large complex simulations         et al., 2014) and it greatly overreported ﬂu cases
systems. Furthermore, it exempliﬁes how modularity           during the 2012 and 2013 A/H3N2 pandemic (Olson
may not even be an option in scientiﬁc practice.             et al., 2013).
                                                                It is by now well known that Google’s ﬂu tracker
                                                             failed to achieve what it was designed to do, namely
Example
                                                             predict and report ILI’s better and faster than the con-
There has been a recent trend in the past decade or so to    ventional surveillance tools available. It simply didn’t
use the vast amount of data generated by internet            predict at all or predicted erroneously. Because of this,
searches in attempts to create predictive models. These      the project is often taken to exemplify ‘‘Big Data
models range from prediction of American Idol winners        hubris’’ (Lazer et al., 2014), the often underlying
(Ciulla et al. 2012), political election outcomes,           assumption that large amounts of data and the patterns
unemployment rates, box-oﬃce receipts for movies,            that are discovered through its analysis can yield results
and song positions in charts (Goel et al., 2010). But per-   independently from or without the aid of principled
haps the best known among these attempts has been the        theoretical underpinnings.
ﬂu tracker function: GFT. Researchers at Google                 Although the disappointing errors of GFT have been
expected the data from accumulated queries to yield cor-     rigorously documented and measured (Olson et al., 2013;
relational patterns that, all by themselves, would tell a    Salzberg, 2014; see the supplemental material in Lazer
story about the presence and spread of the disease (Lazer    et al., 2014) what is most interesting to our discussion is
et al., 2014; Lazer and Kennedy, 2015). GFT exempliﬁes       the ambiguity regarding their nature and source. Many
the spirit of so-called empiricist interpretation of Big     of these studies focus particularly on the margin of error
Data, discussed above. However, the researchers’             but are not clear about what caused the errors. Some
hopes did not materialize. Although some correlations        researchers (Cook et al., 2011) for example, ascribe the
were discovered, Google’s ﬂu tracker continued to con-       errors to issues like seasonality, the fact that outbreaks
sistently generate spurious correlations and, more ser-      happened outside of what is commonly thought to be ﬂu-
iously, reporting false ﬂu numbers (Lazer et al., 2014;      season. This meant that common ﬂu-related terms were
Lazer and Kennedy 2015; Olson et al., 2013).                 less likely to have been used in queries to the search
   GFT was designed to predict, in real time, the            engine.37 Others ascribe the errors to diﬀerences of age
advent of a ﬂu epidemic. The innovative aspect of this       distribution and geographical heterogeneity occurring
tracker was its reliance on the relatively loose search      during model ﬁtting periods of GFT (Olson et al., 2013).
queries typed into Google’s search engine. These data,          Lazer et al. (2014) oﬀer two possible culprits. The
they hoped, could serve as the basis for predictions         ﬁrst is due to neglect of traditional statistical tech-
concerning the behavior of the epidemic (Cukier and          niques. Some of the error here can be ﬁxed once GFT
Mayer-Schoenberger, 2013). The core idea behind this         incorporates conventional statistical methods that can
project was to provide an alternative to conventional        provide correlational ﬁlters. These methods inform
epidemiological surveillance and prediction systems          modern pattern ﬁnding techniques in traditional
which relied on medical reports of Inﬂuenza-like ill-        research beyond Big Data (Lazer et al., 2014). If con-
nesses (ILI’s) from regional clinics to the Centers for      ventional statistical methods were deployed along with
Disease Control and Prevention (CDC’s). In particular        the GFT a reﬂective equilibrium between data from
it hoped to foresee an epidemic outbreak from search         ILI’s surveillance and search terms could better cali-
queries that would indicate a strong presence of ﬂu-like     brate GFT. Given the results presented by Horner
symptoms based on speciﬁc ﬂu-related words and com-          and Symons the suggestion to take statistics seriously,
binations of these words typed into the search engine.       while generally sensible, might have additional compli-
This, they argued, could be done if not in real time, at     cations that are beyond the scope of this paper.
least faster than reports from patients seeking care at         Lazer et al. (2014) suggest that another possible
local clinics, which could take a number of days.            cause for the errors in GFT is what they call algorithm
However, after its launch as an open tool for ﬂu sur-        dynamics undergone by Google’s search algorithm.
veillance in 2008 there were two seriously embarrassing      Algorithm dynamics, according to them, are
Symons and Alvarado                                                                                                   13

modiﬁcations to Google’s search algorithms that are           described by Symons and Horner. Whatever eﬀorts we
introduced in order to enhance the functionality of           introduce to mitigate error in these systems will be under-
the search engine. They are of two kinds: blue team           mined by the fact that they incorporate a vast number of
dynamics, those that the service provider deploys for         individual machines and computational methods to yield
greater eﬃciency and usefulness of search results; and        even the simplest of results. And as discussed above, even
red team dynamics, those done by users of the service         if we characterize the problem in terms of modules, the
for personal beneﬁt such as prominence and visibility.        process is highly unlikely to become less opaque.
According to them, blue team dynamics are what is
most likely behind GFT’s errors. The evidence that
they cite is a correlation between reported changes to
                                                              Discussion
the algorithm and the surge of predictive errors in           Issues of path complexity and epistemic opacity are
GFT. According to the authors, what makes the                 more than merely abstract theoretical preoccupations.
system yield errors is the way in which search results        As stated in the introduction to this article, some of the
skew the queries themselves, queries which are in turn        limitations and risks involved in the use of computa-
used to extract the terms for the GFT to analyze. That        tional methods in public policy, commercial, and scien-
is, the search results of Google’s search engine inﬂuence     tiﬁc contexts only become evident once we understand
the prominence of search terms that users input and           the ways in which these methods are susceptible to
these skewed inputs then are used by GFT to predict           error. In the broader social and political context, a pre-
the presence or absence of the ﬂu (Lazer et al., 2014).       condition for understanding the potential abuses that
    That results generated by the search engine can modify    can result from the deployment of Big Data techniques
queries and input from the very source that is supposed to    by powerful institutions is a careful account of the epi-
be furnishing the data for prediction is troublesome          stemic limits of computational methods. A clear sense
enough. However, there is something deeper going on.          for the nature of error in these systems is essential
Although Lazer et al. (2014) deﬁne the blue team algo-        before we can decide how powerful they should
rithm dynamics undergone by Google’s search algorithms        become and how much trust we should grant them
in the context of Google’s particular business model, one     (see for example Paparrizos et al., 2016). By way of
can extend the term beyond Google or GFT. Other social        illustration, we have focused our attention on the limi-
media platforms engage in algorithm dynamics too, in          tations of GFT as a predictive tool that can be a sup-
particular blue team dynamics (Lazer et al., 2014). In        plement to ILI’s surveillance. The consequences of
fact, algorithm dynamics, insofar as they are deﬁned as       overestimation in this context are not as immediately
the changes made to any software product by those             troubling as the consequences for other systems that are
designing it, aﬀect all aspects of software production        in use in governmental and military contexts. For
and development. These modiﬁcations include model ﬁt-         example, if we relate our discussion to Software
ness processes and functional additions to the underlying     Studies research, such as that of Louise Amoore for
software that are necessary to its proper functioning.        example, we can see the immediately troublesome
Thus, algorithm dynamics are an essential feature of the      implications that a conventional account of epistemic
kind of artifact that software is (Holzmann, 2015) and not    trust on Big Data systems could have. In her research
merely a product of arbitrary human intervention.             (Amoore, 2011), Big Data systems are in charge of cal-
    Given the extent and scope of these dynamics in Big       culating and assessing the security risks posed by indi-
Data more generally, we have a bigger issue on our hands      viduals ﬂying from one part of the world to another.
than merely biased data gathering. In particular the          Without having a proper understanding of the nature
issues discussed in ‘‘The epistemic status of Big Data’’,     of error inherent to these systems, assessing whether
‘‘Error’’, and ‘‘Path complexity and Big Data’’ sections:     they are ﬂagging the right people, or the right number
epistemic opacity due to sheer volume of people, number       of people becomes ever more challenging.
of processes, legacy code, and path complexity catastro-          Debates concerning the epistemic status of Big Data
phe given the number of lines of code involved in projects    in the Critical Data Studies literature must take account
of such magnitude are at play. But the challenge is not       of the nature of error in software intensive contexts. We
merely related to product development and modiﬁca-            have shown that an account of error management and
tion. The epistemically relevant feature of this cycle of     reliability can be proﬁtably introduced into the agenda
updating software results from our inability to test for      of Critical Data Studies. Symons and Horner’s concept
error and our dependence on systems that are susceptible      of path complexity for example, highlights the limita-
to it. In other words, this is an issue of knowledge acqui-   tions of testing given intrinsic features of software. The
sition, reliability, and, therefore, trust.                   problem of reliability and the changing character of trust
    The software behind GTF and similar Big Data pro-         in the context of Big Data projects pose an ongoing
jects falls prey to the path complexity catastrophe as        challenge for Critical Data Studies.
14                                                                                                              Big Data & Society

Acknowledgments                                                        controversial assertion, but I would argue that transac-
We are very grateful to the anonymous referees of this journal         tion processing and data storage are largely solved prob-
as well as to the guest editors of the issue Andrew Iliadis and        lems.’’ (39)
Federica Russo for their helpful feedback.                          6. Most publications discussing Big Data over the past five
                                                                       years have praised the predictive power of the new meth-
                                                                       ods and the seemingly unprecedented insights brought by
Declaration of conflicting interests                                   the visualization techniques that it enables. Some have
The author(s) declared no potential conﬂicts of interest with          adopted a skeptical stance towards the commercial hype
respect to the research, authorship, and/or publication of this        surrounding Big Data (The most sophisticated of these
article.                                                               include Bollier and Firestone, 2010; Boyd and Crawford,
                                                                       2012; Kitchin, 2014).
Funding                                                             7. The use of the term ‘empiricist’ is only marginally related
                                                                       to views that philosophers would recognize as empiricist.
The author(s) received no ﬁnancial support for the research,
authorship, and/or publication of this article.                        A better label for this cluster of views might be ‘‘atheore-
                                                                       tical’’ or ‘‘anti-theoretical’’.
                                                                    8. He quickly dismisses the Kuhnian approach by saying
Notes                                                                  that paradigmatic accounts are overly ‘‘sanitized’’ and
 1. By taking the epistemic status of Big Data as the starting         ‘‘linear’’ accounts of scientific inquiry (2014).
    point, we should not be understood as claiming that the            Nevertheless, he endorses the Kuhnian notion of ‘‘para-
    users of these technologies are motivated primarily by the         digm’’ as useful in the Big Data debate.
    pursuit of truth.                                               9. Cukier and Mayer-Schoenberger argue the volume size in
 2. Chris Anderson’s provocative (2008) article ‘‘The end of           Big Data brings about three drastic changes to data ana-
    theory: the data deluge makes the scientific method obso-          lysis: unrestricted sampling (in accordance with (i)
    lete’’ is widely cited in this context although as Martin          above), tolerance of inaccuracy as a tradeoff of the vast-
    Frické (2015) notes, ‘‘apparently Anderson never believed         ness of possible correlations, and lastly giving up on ‘‘our
    or advocated the theses of his own paper but wrote it to           quest to discover the cause of things’’ in exchange for
    provoke response’’ (see also Norvig, 2008).                        predictive prowess. Although some of these correlate
 3. More recently the pitfalls associated with atheoretical            with Kitchin’s list, we think that the question about
    uses of Big Data have become clear even to large corpor-           whether scientific inquiry can do away with causal insight
    ate interests like IBM (Marr, 2015). In 2015, Marr con-            is a very important one that is not discussed carefully
    sidered a Data Guru by the industry participated in an             enough in the literature and that is worthy of a paper
    interview for IBM’s community podcast. In it, he dis-              in and of itself.
    cusses the main point of his forthcoming book. He              10. Thus, we can say that (1) is implausible given that in a
    emphasized that the full resolution, ‘more means more’             dynamic real world/real time problem N ¼ All as a
    approach to Big Data is misguided. The dynamic nature              sample is very difficult to obtain/define for problems of
    of Big Data problems require it to collect, analyze, and           practical interest.
    solve issues in real time. This means that old data may        11. Although it is widely acknowledged that the ‘‘end of
    not be as helpful to solve current problems. More inter-           theory’’ claims are hyperbolic at best (Boyd and
    estingly, he thinks that strategic inquiry before collection       Crawford) (Bollier and Firestone, 2010), most of the criti-
    is the new way to go. This position stands in sharp con-           cism is anthropocentric and social in nature. That is to
    trast to the ‘‘death of theory’’ thesis espoused by advo-          say, as discussed above, it often makes reference to some
    cates of the unrestricted correlation camp. See also               aspect of social epistemology such as individual and col-
    Jacobs (2009) for a discussion of the importance of ana-           lective biases.
    lysis in Big Data. What he calls ‘‘the pathologies of Big      12. Longino (1990) points out that these are features that
    Data’’ are due to an uncritical attitude towards accumu-           have a long history in the development of science as it
    lated data.                                                        grew from highly individual projects in the 1800s to
 4. By ‘‘error’’ we simply mean to encompass the wide range            multidisciplinary institutional ventures. However,
    of ways in which a software system may fail. This may              Contrary to Kitchin, Boyd and Crawford, Longino rede-
    include erroneous calculations, implementations, results,          fines objectivity as a product of the social character of
    etc. The important point here is not errors in coding per          science. For her, an addition of subjectivities tends to
    se but the epistemic implications of those errors in the           neutralize particular biases and sift out highly individua-
    context of inquiry. Thus, error detection and correction           lized values and preferences. So, for her, objectivity is not
    are the focus of this paper. For a more detailed account           absent in the scientific process, but rather stems from a
    of error in software see Parker (2008) and Floridi et al.          different source than conventionally thought.
    (2015).                                                        13. We are grateful to an anonymous referee for encouraging
 5. In 2009, Adam Jacobs describes the development of                  us to respond to Amoore’s work on security.
    increasingly powerful computing technology and argues          14. For a thorough overview of the many dimensions of
    that the challenges associated with Big Data are due to            interest in philosophy of computation see Rapaport
    analysis rather than size ‘‘The pathologies of Big Data are        (2015); for an interesting analysis on function and mal-
    primarily those of analysis. This may be a slightly                function in software see Floridi et al. (2015).
Symons and Alvarado                                                                                                                 15

15. One of the biggest questions arising from the use of com-            part of the empirical tools available to scientists (see for
    puter simulations in science is whether they are part of the         example Barberousse et al., 2009; Barberousse and
    scientist’s empirical toolkit (Barberousse et al., 2009;             Vorms, 2014; Winsberg, 2010).
    Floridi, 2012; Winsberg, 2010).                                  24. As discussed below, Symons and Horner sought to dis-
16. She cites the study of shock wave behavior and neutron               tinguish SIS from non-SIS science by virtue of the degree
    diffusion as topics to which Ulam, von Neumann, Fermi                of conditionality present in both (2014; forthcoming).
    and others applied novel computational techniques.               25. So, for example the problem of understanding the Stokes
17. Independently of the computations themselves though,                 flow over a finite cylinder is analytically intractable as are
    the method was a novel statistical approach to serial pro-           a range of other problems from fluid dynamics (see e.g.
    cesses that could not be made faster using the clas-                 Ferziger and Peric, 2012).
    sical—non statistical—approach even by using multiple            26. We must remember that one of the most important
    computers (Metropolis and Ulam, 1949). Thus the                      aspects in the development of computational methods
    method wasn’t only adding speed but also a conceptual                for analysis of dynamic systems was their visualization
    shift towards probability theory that brought with it                (Keller, 2003). In fact, some simulations, like cellular
    novel epistemic challenges (Winsberg, 2010).                         automata, later came to be regarded as powerful epi-
18. See also Symons (2008) for further discussion of the rela-           stemic tools, somewhat analogous to natural systems,
    tionship between computational modeling and                          because of the fact that their macroscopic properties,
    explanation.                                                         that is their visual evolutions, resembled real patterns vis-
19. For a very different perspective on the relationship                 ible in cell formation. Fox-Keller ascribed this key insight
    between simulation and theory see Morrison (2015). On                to joint work by Von Neumann and Ulam and further
    Morrison’s view simulations can play a role equivalent to            cites (Toffoli and Margolus, 1987).
    experimental evidence in relation to scientific theories.        27. Bollier, for example, argues that visualization in the data
20. What she has in mind here are models, like cellular auto-            industry is a sense-making tool. He ties this to his criti-
    mata that are not attempts to capture some specific phys-            cism of the ‘‘raw data’’ advocates and argues that many
    ical phenomenon. This third stage is targeted towards                of the insights drawn from Big Data can only emerge
    ‘‘phenomena for which no equations, either exact or                  when seen by an expert and seldom arise solely as a prod-
    approximate, exists (as, e.g., in biological development),           uct of numerical calculations. One example of this is how
    or for which the equations that do exists simply fall short          Google research found that two out of three cows align
    (as, e.g., turbulence).’’ (2003: 210; see also Symons, 2008).        their bodies to the north pole just by observing images
21. It is important to note that for Fox-Keller, this third sense        from Google Maps. No machine, he argues, could have
    of simulations is particularly important because its aim is          done this alone. This is important in our context, not
    no longer to simulate neither differential equations nor             because of the epistemic limitations on machine recogni-
    fundamental (albeit idealized) particles of a given system           tion, but rather because it shows the intrinsically visual
    but rather the phenomenon itself. That is, cellular auto-            nature of so much of Big Data analysis and the correl-
    mata, for example, were simulations that described and               ation this visualizations have with philosophical debates
    elucidated patterns about the systems carrying out the               about simulation.
    simulations themselves. Although cellular automata are           28. This distinction matters because of the epistemic import
    more famously considered to be a simulation similar to               of the methods themselves. If simulation is closer to
    those discussed on the second stage, this was only a con-            theory, some say, then no novel knowledge can be gen-
    sequence of the visualization similarities with real life cell       erated from them. All we can reasonably expect are
    formation. Originally however, they were constructed to              coherence assessments of internal theoretical principles.
    simulate themselves. Fox-Keller describes this confusion             If simulations are like experiments, on the other hand,
    by stating that ‘‘despite its explicitly biological allusion,        then we have reasons to include them in our empiricist
    [cellular automata] was developed by—and for the most                toolkit (Barberousse and Vorms, 2014).
    part has remained in the province of—physical scientists.’’      29. Furthermore, we must consider the possibility that in
    (2003) The resemblance to biological process of self repro-          adding new code to legacy code one may even be exacer-
    duction was only noted later.                                        bating its opacity.
22. The question of whether Big Data is indeed a suitable            30. We thank an anonymous referee for bringing to our
    scientific instrument is still an open question (Lazer               attention the similarity between black box theory and
    et al., 2014), for example have the following to say                 epistemic opacity as well as mentioning modularity as a
    about Google’s flu tracker reliance on Big Data method-              possible response to the problem of epistemic opacity.
    ology: ‘‘The core challenge is that most big data that have      31. Some efforts have been made to provide a taxonomy of
    received popular attention are not the output of instru-             error in software, however they focus on external sources
    ments designed to produce valid and reliable data amen-              such as inaccurate design. For a thorough review of mal-
    able for scientific analysis.’’ (Lazer, 2014)                        function in software see Floridi et al. (2015).
23. Whether any computational simulation does involve                32. For a detailed account of the degree to which this account
    either the testing and/or the expanding of any given                 of error may figure in the software that underlies simula-
    theory and to what extent it may do so is the subject of             tions see Floridi et al. (2015). In it they argue that certain
    a vast and open philosophical debate. This is particularly           kinds of error are only possible to a limited degree (a
    the case when computational simulations are taken to be              type/token distinction) in software. Further they argue
16                                                                                                              Big Data & Society

    that such error is always from an external source. That is,      Barberousse A and Vorms M (2014) About the warrants of
    all of the errors listed above are external to the software         computer-based empirical knowledge. Synthese 191(15):
    itself, since software will always do what it was designed          3595–3620.
    to do (whether the design fits the task intended for the         Bauer P, Thorpe A and Brunet G (2015) The quiet revolution
    software is an external problem).                                   of numerical weather prediction. Nature 525(7567): 47–55.
33. Parker makes some remarks concerning the limitations of          Bedau MA (1997) Weak emergence. Noûs 31(11): 375–399.
    this approach: first she thinks that severe testing on simu-     Berry DM (2011) The philosophy of software. In: Code and
    lations is rare; second, she acknowledges that formal stat-         Mediation in the Digital Age. London: Pal-grave..
    istical analysis of the kind used by Mayo to support             Bollier D and Firestone CM (2010) The Promise and Peril of
    simulation processes has much work to do and whether                Big Data. Washington, DC: Aspen Institute,
    it ends up playing ‘‘as large a role (or the same role)’’ in        Communications and Society Program, p. 56.
    simulations remains to be seen; third, error directly            Boschetti F, Fulton EA, Bradbury R, et al. (2012) What is a
    related to the model used to build the simulation is a              model, why people don’t trust them, and why they should.
    very hard problem, particularly considering that many               In: Raupach MR, McMichael T, Finnigan JJ, et al. (eds)
    traditional/observational assumption go into such                   Negotiating Our Future: Living Scenarios for Australia to
    models. She suggests an extra statistical approach to               2050. Canberra, ACT: Australian Academy of Science.
    deal with this last problem, however, for details that we        Boyd D and Crawford K (2012) Critical questions for big
    will explain below, this may not work either.                       data: Provocations for a cultural, technological, and schol-
34. In so far as application goes, the severity principle, as for-      arly phenomenon. Information, Communication & Society
    mulated by Mayo and as adopted by Parker’s in her dis-              15(5): 662–679.
    cussion of computer simulations, is still a philosophical        Brusoni S and Prencipe A (2001) Unpacking the black box of
    principle at its core and as such it does its job mainly as         modularity: Technologies, products and organizations.
    a background assumption at work when science is con-                Industrial and Corporate Change 10(1): 179–205.
    ducted. That is, the principle is mainly a meta consider-        Bryant R, Katz RH and Lazowska ED Big-data computing:
    ation about what constitutes appropriate epistemic                  Creating revolutionary breakthroughs in commerce, sci-
    support for a scientific hypothesis and how this may ultim-         ence and society, December 2008, pp. 1–15. Available at:
    ately be granted legitimization in the realm of scientific          http://www.cra.org/ccc/docs/init/Big_Data.pdf.
    explanation. We thank an anonymous reviewer for the              Bunge M (1963) A general black box theory. Philosophy of
    opportunity to clarify this.                                        Science 22: 346–358.
35. For details of the argument, please see Symons and               Chen M, Mao S and Liu Y (2014) Big Data: A survey. Mobile
    Horner (2014).                                                      Networks and Applications 19(2): 171–209.
36. Once again we thank an anonymous reviewer for bring-             Ciulla F, Mocanu D, Baronchelli A, et al. (2012) Beating the
    ing this to our attention.                                          news using social media: The case study of American Idol.
37. Researchers (Cook et al., 2011) believe that user’s search          EPJ Data Science 1(1): 1–11.
    terms change depending on the season even if the symp-           Cook S, Conrad C, Fowlkes AL, et al. (2011) Assessing
    toms are the same. Given the common seasonal patterns               Google flu trends performance in the United States
    of flu pandemics, even if users were exhibiting flu-like            during the 2009 influenza virus A (H1N1) pandemic.
    symptoms they would search for different terms in the               PloS One 6(8): e23610.
    winter from those in the spring.                                 Cox M and Ellsworth D (1997) Application-controlled
                                                                        demand paging for out-of-core visualization. In:
                                                                        Proceedings of the 8th conference on visualization’97,
References                                                              Phoenix, AZ, USA, 18–24 October 1997, Los Alamitos,
                                                                        CA, IEEE Computer Society Press.
Amoore L (2011) Data derivatives on the emergence of a               Cukier K and Mayer-Schoenberger V (2013) Rise of Big
  security risk calculus for our times. Theory, Culture &               Data: How it’s changing the way we think about the
  Society 28(6): 24–43.                                                 world, The. Foreign Affairs 92: 28.
Amoore L (2014) Security and the incalculable. Security              Ferziger JH and Peric M (2012) Computational Methods for
  Dialogue 0967010614539719.                                            Fluid Dynamics. Springer Science & Business Media.
Anderson C (2008) The end of theory: The data                        Ethiraj SK and Levinthal D (2004) Modularity and innovation
  deluge makes the scientific method obsolete.                          in complex systems. Management Science 50(2): 159–173.
  Available at: http://www.wired.com/science/discoveries/            Floridi L (2012) Big Data and their epistemological challenge.
  magazine/16-07/pb_theory (accessed 24 January 2016).                  Philosophy & Technology 25(4): 435–437.
Arbesman S (2013, August) Five myths about Big Data. The             Floridi L, Fresco N and Primiero G (2015) On malfunction-
  Washington Post. Available at: www.washingtonpost.com/                ing software. Synthese 192(4): 1199–1220.
  opinions/five-myths-about-big-data/2013/08/15/                     Frické M (2015) Big Data and its epistemology. Journal of the
  64a0dd0a-e044-11e2-963a-72d740e88c12_story.html                       Association for Information Science and Technology 66(4):
  (accessed 24 January 2016).                                           651–661.
Barberousse A, Franceschelli S and Imbert C (2009) Computer          Frigg R and Hartmann S (2012, Fall) Models in science. In:
  simulations as experiments. Synthese 169(3): 557–574.                 Zalta EN (ed) The Stanford Encyclopedia of Philosophy.
Symons and Alvarado                                                                                                                     17

   Available at: http://plato.stanford.edu/archives/fall2012/         Newman J (2015) Epistemic opacity, confirmation holism and
   entries/models-science (accessed 24 January 2016).                    technical debt: Computer simulation in the light of empir-
Frigg R and Reiss J (2009) The philosophy of simulation: Hot             ical software engineering. Available at: http://hapoc2015.
   new issues or same old stew? Synthese 169(3): 593–613.                sciencesconf.org/conference/hapoc2015/pages/Newman.
Gantz J and Reinsel D (2011) Extracting value from chaos.                pdf (accessed 24 June 2016).
   IDC iview 1142: 9–10.                                              Norvig P (2008) All we want are the facts, ma’am. Available
Goel S, Hofman JM, Lahaie S, et al. (2010) Predicting con-               at: http://norvig.com/fact-check.html (accessed 22 January
   sumer behavior with Web search. Proc Natl Acad Sci                    2016).
   107(41): 17486–17490.                                              Oberkampf WL, Trucano TG and Hirsch C (2004)
Holzmann GJ (2015) Code inflation. IEEE Software 22(2):                  Verification, validation, and predictive capability in com-
   10–13.                                                                putational engineering and physics. Applied Mechanics
Horner J and Symons J (2014) Reply to Angius and Primiero                Reviews 57(5): 345–384.
   on software intensive science. Philosophy & Technology             Olson DR, Konty KJ, Paladini M, et al. (2013) Reassessing
   3(27): 491–494.                                                       Google Flu trends data for detection of seasonal and pan-
Hilliard R (2000) Ieee-std-1471-2000 recommended practice                demic influenza: A comparative epidemiological study at
   for architectural description of software-intensive systems.          three geographic scales. PLoS Computational Biology
   IEEE 12: 16–20. Available at: http://standards.ieee.org               9(10): e1003256.
   (accessed 13 June 2016).                                           Paparrizos J, White RW and Horvitz E (2016) Screening for
Humphreys P (2009) The philosophical novelty of computer                 pancreatic adenocarcinoma using signals from web search
   simulation methods. Synthese 169(3): 615–626.                         logs: Feasibility study and results. Journal of Oncology
Jacobs A (2009) The pathologies of big data. Communications              Practice, p.JOPR010504.
   of the ACM 52(8): 36–44.                                           Parker WS (2008) Computer simulation through an error-
Keller EF (2003) Models, simulation, and ‘‘computer experi-              statistical lens. Synthese 163(3): 371–384.
   ments’’. Available at: http://www.informatics.indiana.edu/         Rapaport WJ (2015) Philosophy of computer science.
   jbollen/I501F11/readings/week8/Fox-Keller_2002_                       Available at: http://www.cse.buffalo.edu/rapaport/
   MODELS_SIMULATION_AND_COMPUTER_                                       Papers/phics.pdf
   EXPERIMENTS.pdf (accessed 24 January 2016).                        Salzberg S (2014) Why Google flu is a failure. Forbes. com
Kelling S, Hochachka WM, Fink D, et al. (2009) Data-inten-               [online]. pp. 03–24. Available at: http://www.forbes.com/
   sive science: A new paradigm for biodiversity studies.                sites/stevensalzberg/2014/03/23/why-google-flu-is-a-fail
   BioScience 59(7): 613–620.                                            ure/#33bbe7d4344a (accessed 24 January 2016).
Kitchin R (2014) Big Data, new epistemologies and paradigm            Steadman I (2013)Big Data and the death of the theorist.
   shifts. Big Data & Society 1(1): 1–12 DOI: 10.1177/                   wired. co. uk, Vol. 25, pp. 2013-01.
   2053951714528481.                                                  Symons J (2002) Emergence and reflexive downward caus-
Kuhn TS (1962) The Structure of Scientific Revolutions.                  ation. Principia: An International Journal of Epistemology
   Chicago: Chicago University Press.                                    6(1): 183–201.
Lazer D, Kennedy R, King G, et al. (2014) The parable of              Symons J (2008) Computational models of emergent proper-
   Google Flu: Traps in big data analysis. Science 434: 343.             ties. Minds and Machines 18(4): 475–491.
Lazer D and Kennedy R (2015) What we can learn from the               Symons J and Boschetti F (2013) How computational models
   epic failure of Google Flu Trends. Wired.                             predict the behavior of complex systems. Foundations of
Longino HE (1990) Science as Social Knowledge: Values and                Science 18(4): 809–821.
   Objectivity in Scientific Inquiry. Princeton, NJ: Princeton        Symons J and Horner J (2014) Software intensive science.
   University Press.                                                     Philosophy & Technology 27(3): 461–477.
Marr B (2015) Big Data: Using SMART Big Data, Analytics               Symons J and Horner J (forthcoming) Software error as a
   And Metrics To Make Better Decisions And Improve                      limit to inquiry for finite agents: Challenges for the post-
   Performance. Chichester, UK: John Wiley & Sons.                       human scientist. Available at: http://www.johnsymons.
Mayo DG and Spanos A (2010) Error and Inference: Recent                  net/wp-content/uploads/2016/06/Final-JKHJFS_
   Exchanges on Experimental Reasoning, Reliability, and the             20160320_0635_IACAP1.pdf (accessed 24 June 2016).
   Objectivity and Rationality of Science. New York, NY:              Toffoli T and Margolus N (1987) Cellular Automata
   Cambridge University Press.                                           Machines: A New Environment For Modeling. MIT press.
Metropolis N and Ulam S (1949) The Monte Carlo method.                Weisberg M (2013) Simulation and Similarity: Using Models
   Journal of the American Statistical Association 44(247):              to Understand the World. New York, NY: Oxford
   335–341.                                                              University Press.
Morrison M (2015) Reconstructing Reality: Models,                     Winsberg E (2010) Science in the Age of Computer Simulation.
   Mathematics, and Simulation. New York, NY: Oxford                     Chicago: University of Chicago Press.
   University Press.


   This article is a part of special theme on Critical Data Studies. To see a full list of all articles in this special theme, please
   click here: http://bds.sagepub.com/content/critical-data-studies.
