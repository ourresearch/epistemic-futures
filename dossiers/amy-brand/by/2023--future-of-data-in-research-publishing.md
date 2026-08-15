---
title: "The Future of Data in Research Publishing: From Nice to Have to Need to Have?"
person: amy-brand
section: by
type: journal-article
year: 2023
venue: "Harvard Data Science Review"
authors: "Christine L. Borgman; Amy Brand"
doi: https://doi.org/10.1162/99608f92.b73aae77
openalex_id: https://openalex.org/W4390047334
source_url: https://doi.org/10.1162/99608f92.b73aae77
retrieved: 2026-08-13
content: full-text
notes: "Open access (Harvard Data Science Review). Text extracted from the accepted-version PDF hosted by OpenAlex."
---

# The Future of Data in Research Publishing: From Nice to Have to Need to Have?

## Full text

Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 1 of 20

Just Accepted
DOI: 10.1162/99608f92.b73aae77
ISSN: 2644-2353

                          The Future of Data in Research Publishing:

                                   From nice to have to need to have?
                     Christine L. Borgman, UCLA and Amy Brand, The MIT Press

                     Harvard Data Science Review, special issue on Democratizing Data

1     Why Open Access to Data? ..................................................................................................... 2
2     Transitional Status of Research Data....................................................................................... 4
    2.1       Utility of Research Data.................................................................................................. 5
    2.2       Benefits and Costs of Open Access to Research Data .................................................... 7
    2.3       Risks of Open Access to Research Data ......................................................................... 9
3     Conclusions ........................................................................................................................... 11
4     References ............................................................................................................................. 12

                                                                Abstract

Science policy promotes open access to research data for purposes of transparency and reuse of

data in the public interest. We expect demands for open data in scholarly publishing to

accelerate, at least partly in response to the opacity of artificial intelligence algorithms. Open

data should be findable, accessible, interoperable, and reusable (FAIR), and also trustworthy and

verifiable. The current state of open data in scholarly publishing is in transition from ‘nice to

have’ to ‘need to have.’ Research data are valuable, interpretable, and verifiable only in context

of their origin, and with sufficient infrastructure to facilitate reuse. Making research data useful

    Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 2 of 20

is expensive; benefits and costs are distributed unevenly. Open data also poses risks for

provenance, intellectual property, misuse, and misappropriation in an era of trolls and

hallucinating AI algorithms. Scholars and scholarly publishers must make evidentiary data more

widely available to promote public trust in research. To make research processes more

trustworthy, transparent, and verifiable, stakeholders need to make greater investments in data

stewardship and knowledge infrastructures.

1   Why Open Access to Data?

Policy makers expect open access to research data to improve scholarship and to serve the public

interest by making the research process more transparent, improving the ability to verify methods

and findings, increasing reproducibility, facilitating reuse of data, and democratizing

participation in research. These are among the stated goals of the recent Nelson memo that

applies to U.S. Federal research funding and of similar policy statements in Europe, Asia, and

elsewhere (European Union Publications Office, 2018; GO FAIR, 2020; Nelson, 2022; Office of

The Director, National Institutes of Health, 2020).

At the same time, the rapid rise of generative AI (artificial intelligence), large-language models,

and machine learning are undermining our ability to trust the authenticity of artifacts of

knowledge – books, journal articles, news stories, data visualizations, and other media (Bly &

Brand, 2023; Loukides, 2023; Milano et al., 2023). Current AI technologies such as ChatGPT

can produce remarkably persuasive texts, but these tools also are known to ‘hallucinate,’ i.e, ‘to

produce false information contrary to the intent of the user and present it as if true and factual’

(Kuta, 2023; Norlen & Barrett, 2023). Examples include citing imaginary journal articles as

    Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 3 of 20

sources. The opacity of current AI algorithms is a primary driver for government and industry

regulation, with calls to label AI-generated content, to disclose data sources used to train large

language models, and to promote ‘algorithmic transparency’ by which AI tools explain their

reasoning (Biden, 2023; Electronic Privacy Information Center, 2023; Rotenberg, 2022).

Tensions between the transparency goals of open science and the opacity of AI algorithms may

be the tipping point that moves data sharing from ‘nice to have’ to ‘need to have’ in scholarly

publishing. Access to research data offers a means to audit the published record and to verify AI-

generated content. The FAIR principles (Findable, Accessible, Interoperable, Reusable) that

form the basis for most open data policies are aspirational and focus largely on technical aspects

of data release (Wilkinson et al., 2016). The FAIR principles do not provide guidance on the

ability to interpret or trust research data, once released. As scholarly publishers seek new means

to promote trust in their journals, access to datasets is an important mechanism to strengthen

evidence for conclusions and to promote transparency of the research process.

While the goals of open research data policies are clear, the consequences for stakeholders are

not. The types, uses, and reuses of data vary widely across disciplines, context, and over time

(Borgman, 2015; Pasquetto et al., 2017). An important factor in the ability to reuse data is the

degree to which communities agree on standard formats for data production. The astronomy

community, for example, established a common structure for observational data from telescopes

in the late 1970s. As a consequence, large corpora of astronomical observations exist that can be

analyzed with available software tools (Borgman, Darch, et al., 2016; Scroggins & Boscoe,

2020). Qualitative data such as interview transcripts are more difficult to structure, although

    Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 4 of 20

software tools to mark up and analyze qualitative data are now available widely. Regardless of

format, considerable labor is required to contextualize data for reuse (Borgman et al., 2021;

Pychlau & Wagner, 2023). The short- and long-term costs of providing open access to data are

high regardless of data type and discipline. Economic models for open data are poorly

understood, as are the myriad risks associated with data access (Lane et al., 2024).

2   Transitional Status of Research Data

Our objective here is to highlight key issues arising as open research data becomes essential to

scientific and scholarly publication. We address concerns about data utility within and between

communities, imbalance of costs and benefits, and risks associated with open access to data. The

growth of AI is a subtext to these transitions, rather than a primary driver.

Nearly 20 years ago, Philip Bourne (2005), then serving both as Editor-in-Chief of PLoS

Computational Biology and as Codirector of the Protein Data Bank, asked, ‘what is the

difference between an entry in a database and an article in a journal?’. His answer was to

characterize the difference ‘as a mix of perception and content.’ Ideally, a scholar can search a

data archive and link directly from a sequence or specimen to the paper describing the methods

and findings. Conversely, the scholar can read a paper and link directly to the evidentiary

materials on which the paper is based. The publication and dataset have complementary, but not

equivalent value, as they serve different purposes in scholarly communication. Bourne proposed

several means of strengthening the relationship between publications and datasets, largely with

the goal of improving discoverability of individual units of content and relationships between

      Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 5 of 20

them. Digital object identifiers (DOIs) are now assigned routinely to datasets, one proposed

improvement, but adding more markup and structure to publications remains rare.

While most research communities now consider data products to be beneficial assets,

investments in the knowledge infrastructures necessary to sustain access to datasets in ways that

they maintain their utility is spotty at best (Borgman, 2015; Borgman & Bourne, 2022).

However, datasets are becoming more readily discoverable due to advances in retrieval tools and

data citation mechanisms (Borgman, 2016; Cousijn et al., 2019; DataCite Metadata Scheme for

the Publication and Citation of Research Data, 2022; Fenner et al., 2019; Gregory et al., 2019,

2020, 2023; Groth et al., 2019; Koesten et al., 2021; Parsons et al., 2019; Zhang et al., 2023).

2.1    Utility of Research Data

The epistemology of data has a long history (Meadows, 2001; Meyns, 2019; Rosenberg, 2013).

Research data are entities constructed by people for specific purposes, often based on implicit

models and unstated assumptions. Most scientific data are tightly coupled with instrumentation

used to generate them and with software used to generate, process, analyze, interpret, and display

them. Some instruments and software are standardized within research communities, but many

are highly customized technical methods developed for a narrowly defined inquiry. Customized

data pipelines and other tools often are the ‘secret sauce’ of a research team.

While datasets produced by specialized tools are released and interpretable by others, data

creators retain the advantage of intimate knowledge about how those data were created

(Pasquetto et al., 2019). Researchers frequently use open data for comparisons, ‘ground

    Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 6 of 20

truthing,’ exemplars, and background. However, to reuse a dataset to pursue a new form of

inquiry, researchers benefit from direct contact with the data creators.

Consider the field of child language acquisition, which thrives on data collected from

spontaneous interactions between children and caregivers in naturally occurring situations, and

on cross-linguistic comparisons of the language learning process. In 1984, researchers at

Carnegie Mellon University launched a shared data resource called the Child Language Data

Exchange System (CHILDES) to serve as a central repository for data concerning first language

acquisition. It originally contained transcripts of audiotapes from the 1960s of child utterances in

several language populations. In the intervening years, it has grown to include hundreds of

corpora across 26+ languages, in different media, and has been cited as a resource in thousands

of publications (Child Language Data Exchange System (CHILDES), 2023).

The existence of CHILDES and the development of computational tools to manipulate the data it

contains are considered significant factors in the steep growth of cross-linguistic research on

child language during the late 20th century. Researchers without the time or resources to travel to

different parts of the world to collect relevant longitudinal data could use this rich online

resource instead.

Early users of the CHILDES database accessed human-transcribed text, without having access to

the audio recordings on which those transcriptions were based. Metadata accompanying the

transcripts indicated the ages of the children recorded. Descriptions of where and when a given

recording was made were also typically provided. Beyond that, however, the data reuser had to

      Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 7 of 20

make a leap of faith concerning the reliability of the transcripts, knowing that the opportunity for

inaccuracies and human error in transcription was significant, and recognizing that the utterances

of very young children are often difficult to interpret, even first-hand (Pierce, 1989).

The researcher who recorded the utterances in real time has the most certainty in coding and uses

of these data. However, it is important to recognize that both data creator and reuser are

vulnerable to implicit biases and motivated reasoning. Reproducibility of research results using

qualitative data such as childhood utterances is an issue when multiple researchers are asking the

same question of the data. More commonly, resources such as CHILDES are source material for

myriad research questions, whether alone or in combination with other data sources. Researchers

can address concerns about subjective judgements in coding and analysing transcripts by

methods of iterative coding and hypothesis testing (Glaser & Strauss, 1967; Strauss & Corbin,

1998).

2.2    Benefits and Costs of Open Access to Research Data

In the simplest economic terms, most of the benefits of open access to research data accrue to the

reusers of data and most of the costs are borne by the data providers. Open data is a ‘commons

problem,’ in the economic sense, in need of governance structures, and subject to ‘free riders’

(David, 2004, 2005; Hess & Ostrom, 2007; Ostrom, 1990).

To acquire research data, researchers expend great effort, and often great sums of money,

whether in the sciences, social sciences, humanities, medicine, engineering, arts, or other

disciplines. The time spent acquiring data for a paper might be short, such as one night on a

telescope or one day of recording child language, or very long, in the case of longitudinal or

    Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 8 of 20

comparative studies. In either case, the time and labor devoted to analyzing, interpreting, and

writing for publication are usually far greater than that spent in data acquisition (Borgman, 2015;

Borgman, Golshan, et al., 2016).

Processing research data in ways they can be released for use by others is another labor cost, and

one that often requires very different skill sets. Archiving and publishing data involves transfer

into standardized formats that can be read by available software and maintained in stable

structures; includes documentation to facilitate interpretation and manipulation; contains

sufficient metadata and provenance information to ensure their validity and authority; and gives

credit to the originators (Baker & Mayernik, 2020; Borgman & Wofford, 2021; Koesten et al.,

2020, 2021). As Bourne (2005) noted, authors are reluctant to invest more effort than necessary

in structuring their publications or their datasets. Advances in information retrieval methods,

including those based in AI, can improve the discovery of publications, datasets, and

relationships between them (Gregory et al., 2019, 2020, 2023; Lane, 2020; Lane et al., 2020;

Zhang et al., 2023).

One research project may yield one dataset and one publication, in which case the relationship

between dataset and publication is clear. More often, one-to-many or many-to-many

relationships exist between projects, publications, authors, universities, and funding sources, as

data are mined and combined to address multiple research questions over time. Determining how

to extract a dataset associated with a specific paper is a nontrivial matter, as is maintaining the

chain of provenance (Borgman, 2015).

      Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 9 of 20

Responsibility for the labor, costs, and expertise required to transform research data into portable

datasets, to steward these data resources for long periods of time, or to provide access to those

data resources rarely is specified by the policies of governments, funding agencies, journals, or

universities. Rather, responsibility for these aspects of data stewardship is diffuse. As explored in

a prior article in this journal, ‘it takes a village to manage and share data’ (Borgman & Bourne,

2022; Borgman & Brand, 2022).

2.3    Risks of Open Access to Research Data

The risks of providing open access to research data have received little empirical attention to

date, although they are a common theme in researchers’ private conversations (Borgman, 2015).

Some researchers are concerned about other investigators using their data without investing the

labor of obtaining grants, conducting the research, analyzing those data, and writing the paper.

When reusers were labeled ‘data parasites,’ a biomedical community established a ‘data parasite

award’ for those who reuse datasets most effectively (The Research Parasite Awards:

Celebrating Rigorous Secondary Data Analysis, 2021; Wofford, 2022)

Some researchers view the loss of control over their data as a risk, and one that is compounded

by lack of attribution and credit to the originator. Provenance trails facilitate credit, authority,

ownership, licensing, and the ability to assess the integrity of research data. Better data citation

mechanisms and practices are the usual response to attribution concerns. Over the course of the

last decade or so, data citation practices have matured with the availability of formal schema,

assignment of DOIs, and repository support for these mechanisms (Borgman, 2016; Cousijn et

al., 2019; DataCite Metadata Scheme for the Publication and Citation of Research Data, 2022;

Fenner et al., 2019; Groth et al., 2019; Parsons et al., 2019).

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 10 of 20

Researchers have been slow to adopt formal citation practices for many reasons, however.

Cataloging datasets requires professional expertise, and only a small subset of available research

data are described sufficiently for formal data citation. When authors do cite datasets, it is often

via mentions in text or footnotes, both of which are difficult to extract for search and retrieval

(Pepe et al., 2014; Uhlir, 2012). Recent developments in automated extraction of dataset

mentions are a promising, if partial, response to problems of attribution and provenance (Lane,

2020, 2019; Lane et al., 2020)

Intellectual property (IP) concerns in reusing data arose in the earliest days of electronic

publishing. By the mid-1960s, the Text Encoding Initiative was maneuvering around the

landmines of IP rights (The Text Encoding Initiative, 2006). By the early 2000s, the Google

Books project and related scanning initiatives brought authors, publishers, libraries, and readers

to legal battles, a contest that accelerated during the COVID-19 pandemic over laws governing

access to digital content (Hachette v. Internet Archive, 2020; Harris, 2020; Hernandez, 2023;

Roberts, 2020; Streitfeld, 2023). A battle currently is brewing about AI-based large language

models that mine intellectual property without attribution or compensation (Bly & Brand, 2023;

Loukides, 2023; Milano et al., 2023).

Long-simmering tensions over misuses and misinterpretations of research data are also coming

to the fore. Scientists working on climate change face skeptics who ‘cherry pick’ their data to

extract facts and figures out of context, claiming alternative conclusions. The COVID-19

pandemic brought scientists, medical and public health professionals, and policy makers into

    Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 11 of 20

storms of skeptics attempting to reuse research data for contradictory claims. The trolls are

everywhere, challenging paradigms from archaeology to zoology. Public engagement in

scholarship has risks, as well as benefits. Data creators, data reusers, publishers, and the public

can benefit when evidentiary data are widely available, especially if documented sufficiently to

ensure their validity and veracity.

Artificial intelligence raises a whole host of risks to scholarly publishing, open science, and open

access to data. Among the risks in uses of open data that are apparent at the current state of AI

development are known errors such as stating unverifiable ‘facts,’ citing non-existent sources,

interpreting data in ways incompatible with scientific reasoning, and combining unrelated data to

draw conclusions that are not scientifically supportable. These are but a few of the many risks

about AI, science, scholarship, data, and truth raised to date (Crawford, 2021; Gil, 2009; Hutson,

2018; OECD, 2023; Williamson et al., 2021).

3    Conclusions

The ubiquity of AI-generated text will continue to diminish our ability to trust digital content,

including published research, unless and until AI companies are required to disclose the

provenance and verifiability of the content on which their large language models are trained and

the reasoning algorithms employed. Already, the research community and general public are

demanding more transparency of the ‘evidence’ necessary to discern trustworthy content. For

readers to trust digital content, they need information about the provenance of assertions. Experts

in a domain need the ability to audit data and to inspect statistical analyses underlying those

assertions.

    Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 12 of 20

Depositing data associated with publications is now accepted practice in most scholarly

disciplines. Data release is enforced by policies of funding agencies and by publisher guidelines.

In our vision of the future, open data will play large roles in democratizing and accelerating

research and in supporting evidence-based knowledge. We acknowledge that different fields of

research have different relationships to data, and fields vary in the degree of apparatus required

to be interpretable and reusable. Data do not ‘speak for themselves;’ rather, they are useful only

in relation to their origins and context, and the knowledge of the user. Nonetheless, we expect to

see rapid growth in data sharing requirements for publication in all fields of research. We hope,

furthermore, that more open sharing of data brings more globally equitable participation in the

research process.

4    References

Baker, K. S., & Mayernik, M. S. (2020). Disentangling knowledge production and data

        production. Ecosphere, 11(7), e03191. https://doi.org/10.1002/ecs2.3191

Biden, J. R. (2023). FACT SHEET: President Biden Issues Executive Order on Safe, Secure, and

        Trustworthy Artificial Intelligence. US Government.

        https://www.whitehouse.gov/briefing-room/statements-releases/2023/10/30/fact-sheet-

        president-biden-issues-executive-order-on-safe-secure-and-trustworthy-artificial-

        intelligence/

Bly, A., & Brand, A. (2023, August 7). AI is muddying the truth. We’ve known how to fix it for

        centuries. Boston Globe. https://www.bostonglobe.com/2023/08/07/magazine/ai-is-

        muddying-truth-weve-known-how-fix-it-centuries/

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 13 of 20

Borgman, C. L. (2015). Big data, little data, no data: Scholarship in the networked world. MIT

       Press.

Borgman, C. L. (2016). Data Citation as a Bibliometric Oxymoron. In C. R. Sugimoto (Ed.),

       Theories of Informetrics and Scholarly Communication (pp. 93–116). De Gruyter Saur.

       https://doi.org/10.1515/9783110308464-008

Borgman, C. L., & Bourne, P. E. (2022). Why It Takes a Village to Manage and Share Data.

       Harvard Data Science Review, 4(3). https://doi.org/10.1162/99608f92.42eec111

Borgman, C. L., & Brand, A. (2022). Data blind: Universities lag in capturing and exploiting

       data. Science, 378(6626), 1278–1281. https://doi.org/10.1126/science.add2734

Borgman, C. L., Darch, P. T., Sands, A. E., & Golshan, M. S. (2016). The durability and fragility

       of knowledge infrastructures: Lessons learned from astronomy. Proceedings of the

       Association for Information Science and Technology, 53, 1–10.

       http://dx.doi.org/10.1002/pra2.2016.14505301057

Borgman, C. L., Golshan, M. S., Sands, A. E., Wallis, J. C., Cummings, R. L., Darch, P. T., &

       Randles, B. M. (2016). Data Management in the Long Tail: Science, Software, and

       Service. International Journal of Digital Curation, 11(1), 128–149.

       https://doi.org/10.2218/ijdc.v11i1.428

Borgman, C. L., & Wofford, M. F. (2021). From Data Processes to Data Products: Knowledge

       Infrastructures in Astronomy. Harvard Data Science Review, 3(3).

       https://doi.org/10.1162/99608f92.4e792052

Borgman, C. L., Wofford, M. F., Golshan, M. S., & Darch, P. T. (2021). Collaborative

       qualitative research at scale: Reflections on 20 years of acquiring global data and making

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 14 of 20

       data global. Journal of the Association for Information Science and Technology, 72(6),

       667–682. https://doi.org/10.1002/asi.24439

Bourne, P. E. (2005). Will a biological database be different from a biological journal? PLoS

       Computational Biology, 1. http://dx.doi.org/10.1371/journal.pcbi.0010034

Child Language Data Exchange System (CHILDES). (2023). https://childes.talkbank.org/

Cousijn, H., Feeney, P., Lowenberg, D., Presani, E., & Simons, N. (2019). Bringing Citations

       and Usage Metrics Together to Make Data Count. Data Science Journal, 18, 9.

       https://doi.org/10.5334/dsj-2019-009

Crawford, K. (2021). Atlas of AI: Power, Politics, and the Planetary Costs of Artificial

       Intelligence. Yale University Press.

DataCite Metadata Scheme for the Publication and Citation of Research Data. (2022). DataCite.

       http://schema.datacite.org/

David, P. A. (2004). Can ‘Open Science’ be protected from the evolving regime of intellectual

       property protections. Journal of Institutional and Theoretical Economics, 160.

       http://www-econ.stanford.edu/faculty/workp/swp03011.pdf

David, P. A. (2005). Creating the Information Commons for e-Science. Creating the Information

       Commons for E-Science: Toward Institutional Policies and Guidelines for Action.

       http://www.codataweb.org/UNESCOmtg/pres-pdavid.pdf

Electronic Privacy Information Center. (2023). AI Policy. https://epic.org/issues/ai/ai-policy/

European Union Publications Office. (2018). Turning FAIR data into reality: Final report and

       action plan from the European Commission expert group on FAIR data.

       https://publications.europa.eu/en/publication-detail/-/publication/7769a148-f1f6-11e8-

       9982-01aa75ed71a1/language-en/format-PDF

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 15 of 20

Fenner, M., Crosas, M., Grethe, J. S., Kennedy, D., Hermjakob, H., Rocca-Serra, P., Durand, G.,

       Berjon, R., Karcher, S., Martone, M., & Clark, T. (2019). A data citation roadmap for

       scholarly data repositories. Scientific Data, 6(1), 28. https://doi.org/10.1038/s41597-019-

       0031-8

Gil, Y. (2009). From data to knowledge to discoveries: Artificial intelligence and scientific

       workflows. Scientific Programming, 17(3), 231–246. https://doi.org/10.3233/SPR-2009-

       0261

Glaser, B. G., & Strauss, A. L. (1967). The discovery of grounded theory: Strategies for

       qualitative research. Aldine Publishing.

GO FAIR. (2020, January 29). Universities Push for Greater Global Open Access to Research

       Data. GO FAIR. https://www.go-fair.org/2020/01/29/universities-push-for-greater-

       global-open-access-to-research-data/

Gregory, K. M., Groth, P., Cousijn, H., Scharnhorst, A., & Wyatt, S. (2019). Searching Data: A

       Review of Observational Data Retrieval Practices in Selected Disciplines. Journal of the

       Association for Information Science and Technology, 70(5), 419–432.

       https://doi.org/10.1002/asi.24165

Gregory, K. M., Groth, P., Scharnhorst, A., & Wyatt, S. (2020). Lost or Found? Discovering

       Data Needed for Research. Harvard Data Science Review, 2(2).

       https://doi.org/10.1162/99608f92.e38165eb

Gregory, K. M., Groth, P., Scharnhorst, A., & Wyatt, S. (2023). The Mysterious User of

       Research Data: Knitting Together Science and Technology Studies with Information and

       Computer Science. In K. Bijsterveld & A. Swinnen (Eds.), Interdisciplinarity in the

       Scholarly Life Cycle: Learning by Example in Humanities and Social Science Research

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 16 of 20

       (pp. 191–211). Springer International Publishing. https://doi.org/10.1007/978-3-031-

       11108-2_11

Groth, P., Cousijn, H., Clark, T., & Goble, C. A. (2019). FAIR Data Reuse – the Path through

       Data Citation. Data Intelligence, 78–86. https://doi.org/10.1162/dint_a_00030

Hachette v. Internet Archive. (2020, October 9). Electronic Frontier Foundation.

       https://www.eff.org/cases/hachette-v-internet-archive

Harris, E. A. (2020, June 1). Publishers Sue Internet Archive Over Free E-Books. The New York

       Times. https://www.nytimes.com/2020/06/01/books/internet-archive-emergency-library-

       coronavirus.html

Hernandez, J. (2023, March 26). A judge sided with publishers in a lawsuit over the Internet

       Archive’s online library. National Public Radio.

       https://www.npr.org/2023/03/26/1166101459/internet-archive-lawsuit-books-library-

       publishers

Hess, C., & Ostrom, E. (2007). Understanding knowledge as a commons: From theory to

       practice. MIT Press.

Hutson, M. (2018). Artificial intelligence faces reproducibility crisis. Science, 359(6377), 725–

       726. https://doi.org/10.1126/science.359.6377.725

Koesten, L., Gregory, K. M., Groth, P., & Simperl, E. (2021). Talking datasets – Understanding

       data sensemaking behaviours. International Journal of Human-Computer Studies, 146,

       102562. https://doi.org/10.1016/j.ijhcs.2020.102562

Koesten, L., Vougiouklis, P., Simperl, E., & Groth, P. (2020). Dataset Reuse: Toward

       Translating Principles to Practice. Patterns, 100136.

       https://doi.org/10.1016/j.patter.2020.100136

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 17 of 20

Kuta, S. (2023). “Hallucinate” Is Dictionary.com’s Word of the Year for 2023. Smithsonian

       Magazine. https://www.smithsonianmag.com/smart-news/hallucinate-is-dictionarycoms-

       word-of-the-year-for-2023-180983443/

Lane, J. I. (2020). Democratizing Our Data: A Manifesto. MIT Press.

Lane, J. I. (2019). The Coleridge Initiative. https://coleridgeinitiative.org/richcontext

Lane, J. I., Mulvaney, I., & Nathan, P. (Eds.). (2020). Rich Search and Discovery for Research

       Datasets: Building the Next Generation of Scholarly Infrastructure. Sage.

Lane, J. I., Spector, A., & Stebbins, M. (2024). An Invisible Hand for Creating Value from Data:

       The opportunities resulting from new legislation and technologies. Harvard Data Science

       Review, (this issue).

Loukides, M. K. (2023). What are ChatGPT and its Friends? : Opportunities, costs, and risks for

       large language models. O’Reilly Media.

Meadows, A. J. (2001). Understanding Information. K. G. Saur.

Meyns, C. (2019). ‘Data’ in the Royal Society’s Philosophical Transactions, 1665–1886. Notes

       and Records: The Royal Society Journal of the History of Science, 74(3), 507–528.

       https://doi.org/10.1098/rsnr.2019.0024

Milano, S., McGrane, J. A., & Leonelli, S. (2023). Large language models challenge the future

       of higher education. Nature Machine Intelligence, 1–2. https://doi.org/10.1038/s42256-

       023-00644-2

Nelson, A. (2022). Ensuring Free, Immediate, and Equitable Access to Federally Funded

       Research. Office of Science and Technology Policy, Executive Office of the President,

       US Government. 08-2022-OSTP-Public-access-Memo.pdf

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 18 of 20

Norlen, N., & Barrett, G. (2023, December 12). Dictionary.com’s 2023 Word Of The Year Is….

       https://content.dictionary.com/word-of-the-year-2023/

OECD. (2023). Artificial Intelligence in Science: Challenges, Opportunities and the Future of

       Research. Organisation for Economic Co-operation and Development. https://www.oecd-

       ilibrary.org/science-and-technology/artificial-intelligence-in-science_a8d820bd-en

Office of The Director, National Institutes of Health. (2020). Final NIH Policy for Data

       Management and Sharing (NOT-OD-21-013:). National Institutes of Health.

       https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html

Ostrom, E. (1990). Governing the Commons: The Evolution of Institutions for Collective Action

       (First Edition). Cambridge University Press.

Parsons, M. A., Duerr, R. E., & Jones, M. B. (2019). The History and Future of Data Citation in

       Practice. Data Science Journal, 18(1), 52. https://doi.org/10.5334/dsj-2019-052

Pasquetto, I. V., Borgman, C. L., & Wofford, M. F. (2019). Uses and Reuses of Scientific Data:

       The Data Creators’ Advantage. Harvard Data Science Review, 1(2).

       https://doi.org/10.1162/99608f92.fc14bf2d

Pasquetto, I. V., Randles, B. M., & Borgman, C. L. (2017). On the Reuse of Scientific Data.

       Data Science Journal, 16. https://doi.org/10.5334/dsj-2017-008

Pepe, A., Goodman, A., Muench, A., Crosas, M., & Erdmann, C. (2014). How Do Astronomers

       Share Data? Reliability and Persistence of Datasets Linked in AAS Publications and a

       Qualitative Study of Data Practices among US Astronomers. PLOS ONE, 9(8), e104798.

       https://doi.org/10.1371/journal.pone.0104798

Pierce, A. E. (1989). On the emergence of syntax: A crosslinguistic study [Thesis, Massachusetts

       Institute of Technology]. https://dspace.mit.edu/handle/1721.1/13993

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 19 of 20

Pychlau, S., & Wagner, D. T. (2023). The data of others: New and old faces of archival research.

       In APA handbook of research methods in psychology: Data analysis and research

       publication, Vol. 3, 2nd ed (pp. 481–500). American Psychological Association.

       https://doi.org/10.1037/0000320-022

Roberts, J. J. (2020). As libraries fight for access to e-books, a new copyright champion emerges.

       Fortune. https://fortune.com/2020/11/28/digital-publishing-copyright-champion-lila-

       bailey-internet-archive/

Rosenberg, D. (2013). Data before the Fact. In L. Gitelman (Ed.), “Raw Data” is an Oxymoron

       (pp. 15–40). MIT Press.

Rotenberg, M. (2022). Artificial Intelligence and the Right to Algorithmic Transparency. In E.

       Stefanini, L. Liguori, M. Ienca, O. Pollicino, & R. Andorno (Eds.), The Cambridge

       Handbook of Information Technology, Life Sciences and Human Rights (pp. 153–165).

       Cambridge University Press. https://doi.org/10.1017/9781108775038.015

Scroggins, M. J., & Boscoe, B. M. (2020). Once FITS, Always FITS? Astronomical

       Infrastructure in Transition. IEEE Annals of the History of Computing, 42(2), 42–54.

       https://doi.org/10.1109/MAHC.2020.2986745

Strauss, A., & Corbin, J. M. (1998). Basics of Qualitative Research: Techniques and Procedures

       for Developing Grounded Theory. SAGE Publications.

Streitfeld, D. (2023, August 13). The Dream Was Universal Access to Knowledge. The Result

       Was a Fiasco. The New York Times.

       https://www.nytimes.com/2023/08/13/business/media/internet-archive-emergency-

       lending-library.html

   Borgman / Brand, HDSR Future of Data in Research Pub, Final Formatted Version, Dec 19, 2023, Page 20 of 20

The Research Parasite Awards: Celebrating rigorous secondary data analysis. (2021).

       http://researchparasite.com/

The Text Encoding Initiative. (2006). http://www.tei-c.org/

Uhlir, P. F. (Ed.). (2012). For Attribution -- Developing Data Attribution and Citation Practices

       and Standards: Summary of an International Workshop. The National Academies Press.

Wilkinson, M. D., Dumontier, M., Aalbersberg, Ij. J., Appleton, G., Axton, M., Baak, A.,

       Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J.,

       Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T.,

       Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data

       management and stewardship. Scientific Data, 3, 160018.

       http://dx.doi.org/10.1038/sdata.2016.18

Williamson, H. F., Brettschneider, J., Caccamo, M., Davey, R. P., Goble, C. A., Kersey, P. J.,

       May, S., Morris, R. J., Ostler, R., Pridmore, T., Rawlings, C., Studholme, D., Tsaftaris, S.

       A., & Leonelli, S. (2021). Data management challenges for artificial intelligence in plant

       and agricultural research. F1000Research, 10, 324.

       https://doi.org/10.12688/f1000research.52204.1

Wofford, M. (2022). Parasitic Knowledge Infrastructures: Data Reuse by Anthropogenic Climate

       Change Skeptics. Proceedings of the Association for Information Science and

       Technology, 59(1), 837–839. https://doi.org/10.1002/pra2.743

Zhang, P., Gregory, K., Yoon, A., & Palmer, C. (2023). Conceptualizing Data Behavior:

       Bridging Data-centric and User-centric Approaches. Proceedings of the Association for

       Information Science and Technology, 60(1), 856–860. https://doi.org/10.1002/pra2.878

©2023 Christine L. Borgman and Amy Brand. This article is licensed under a Creative Commons Attribution
(CC BY 4.0) International license, except where otherwise indicated with respect to particular material
included in the article.
