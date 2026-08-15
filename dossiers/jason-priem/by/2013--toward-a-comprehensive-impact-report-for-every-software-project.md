---
title: "Toward a comprehensive impact report for every software project"
person: jason-priem
section: by
type: journal-article
year: 2013
date: 2013-09-13
venue: "figshare (WSSSPE13 workshop submission)"
authors: "team Impactstory, Jason R Priem, Heather Piwowar"
source_url: https://doi.org/10.6084/m9.figshare.790651.v1
retrieved: 2026-08-13
content: full-text
notes: "Short workshop paper on software impact metrics (precursor to Depsy). OpenAlex W2244341329. Full text from figshare PDF."
---

# Toward a comprehensive impact report for every software project

## Full text

Toward a comprehensive impact report for every software project
Jason Priem, Heather Piwowar
Research software is increasingly important.  However, money, time, and opportunity are wasted because much
research software is unavailable for reuse.  Funds are spent on reinventing the wheel, time is wasted on paths
that others know to be fruitless, and research opportunities remain unexplored by those without skills or
resources to create needed software from scratch.  We're failing to claim all the value from each software
funding dollar.
Today, researchers have little incentive to share the software they develop, and little sharing occurs [Stodden
2010; Ince 2012].  They face a recurring dilemma: even in situations where scholarship may be best served by a
publishing and improving software, one’s own career is usually better served by putting that effort instead into
traditional article­writing. If we want to move to a more efficient, web­native science, we must make that
dilemma disappear: what is good for scholarship must become good for the scholar. We must build a new system
where all types of scholarly products, including software, are recognized, evaluated, and rewarded.
This transition has already begun: for example, the NSF has recently welcomed software as a type of first­class
Research Product in NSF proposal BioSketches.  The NSF Biology directorate has explicitly included software
in its data management plan requirements [Directorate for Biological Sciences 2012], and journals are starting to
require code as a condition of publication (i.e. Science [Science/AAAS]).
However, though these are important initiatives, without metrics of impact they aren’t enough: how can the
software evaluators know if the software has been used and found useful? [Piwowar 2013].  Researchers are
afraid their software, though used, will not be cited; this fear is a major deterrent to sharing code [Stodden 2010].
A “software paper” ­­ an article describing a software system that can be easily cited and evaluated as a
traditional paper [Journal of Open Research Software FAQ; Vandewalle 2012] ­­ has evolved to address this
issue, but it is a poor proxy [Jackson 2012].  Not only is writing a paper an extra step for the investigator, but
citations to a proxy paper fail to capture the natural indications of impact and engagement that occur with
deployed software and open source code [ImpactStory 2013].
Unfortunately, mechanisms to gather evidence about the scope and depth of software impact are still in their
infancy and face several significant obstacles: software lacks standard identifiers and citation norms [Stodden
2013], the scientific literature is unavailable for broad text­mining [Jha 2013], many contributions aren’t captured
in the literature, and most software projects do not systematically track their own usage statistics.
Now is the time to address these obstacles and move forward.  The wider open source community continues to
grow as more projects are hosted in centralized software repositories (see recent growth of GitHub and
continued growth of BitBucket and SourceForge [Berkholz 2012; Jakob 2012; Williams, 2013; Shockey 2013]).
Furthermore, although text­mining rights have been difficult to secure in the past, initiatives are underway that
promise to make it easier in the next few months and years [Van Noorden 2013].  Now ­­ at the very earliest
days of a feasible system ­­ is the time to initiate an open solution to scientific software metrics [Wilbanks].
Here we propose next steps toward a comprehensive impact report for every software project.
Building on the open­source ImpactStory web application, we propose to (a) mine the bulk of the scholarly
literature, (b) track downloads, installations, conversation, and reverse dependencies, and (c) present impacts in a
profile integrating diverse research outputs. This will support all researchers  in presenting meaningful impact
evidence in tenure, promotion, and funding applications.
1

Development Plan
ImpactStory (http://impactstory.org) is an open­source , open data web application that gathers and displays
diverse, web­based impact metrics applying to diverse research products. These altmetrics [Priem 2010] are
classified by audience and engagement type, and displayed through an ImpactStory profile CV (Figure 1),
Javascript badges that can be embedded on users’ websites, and an open API.
Figure 1: ImpactStory profile
As seen in Figure 2, ImpactStory has supports tracking some impact of software products today.  For example,
ImpactStory has uncovered that the GitHub repository containing data and software on an E Coli outbreak has
been mentioned in the full text of two PLOS papers, discussed in social media (18 tweets and 1 shared Facebook
post), and recommended within GitHub (43 stars).  Unless a software developer is doing manual searches
herself, this report will often be the first time she learns about relevant discussions and attributions.
Figure 2:  Software tracking available today in ImpactStory
from http://impactstory.org/item/url/https://github.com/ehec­outbreak­crowdsourced/BGI­data­analysis
This support is a good start, but it is very limited in scope and context.  Links to a repository’s GitHub URL are
detected but all other types of attributions are overlooked.  ImpactStory currently only searches PLOS papers for
attributions: the rest of the scholarly literature is ignored. Evidence of diverse impacts including reverse
dependencies, installations and usages, etc. are not represented.
The proposed project pushes this proof of concept ahead in three key ways: (a) mining evidence of impact from
within the literature, (b) uncovering uses outside the literature, and (c) presenting this evidence as part of
integrated impact research packages.
(a) Mining the literature
Because software is often mentioned but left uncited in the literature, we propose using full­text searches to
uncover heretofore invisible reuse. Using basic text mining, we’ll work to find mentions of software, and
describe context of mentions.  For instance, which section of a paper contained mention, the methods section,
the acknowledgements, or the background section?  We also propose to characterize the citing paper, using
2

indexing keywords to determine if it is a primary research article, a methods paper, a lit review, a software note,
or a review article.
We’ll start with identifying available Open Access content including the PMC OA subset,the CORE indexing api,
the Hindawi corpus, the SpringerOpen api, and the Scientific Research corpus.  We expect additional OA
resources will become available over the next two years in response to new US and UK OA funder rules and
publisher activity (for example, the ACM OA initiative [Boisvert 2013]).  We also plan to explore
free­but­not­OA resources through automated full text query APIs.  PMC and ArXiv offer this option, and other
resources may come online soon (SSRN API, etc).
Open and free resources comprise only a minority of available papers. By far the most ambitious and significant
part of this effort will be obtaining text­mining rights from the major commercial publishers, negotiating
access to their subscription content.  One of us has had success in previous text mining conversations with
Elsevier [Piwowar 2012a], so that will be a natural place to start. We anticipate contacting Springer, Wiley,
Nature, Taylor & Francis, ACM, IEEE, and others.
Finally, we propose to examine the article citation graph to uncover “second­order citations”: the number of
citations to articles that mention the software project.  Is the software mentioned in papers that are themselves
impactful?  Determining how to display this information in a way that is easily interpretable will be part of the
challenge.
(b) Tracking usage
After searching in the research literature for mentions of software, we plan to turn our attention to other online
tools and environments that capture indications of engagement.  A growing body of software is hosted on
centralized software repositories like GitHub and CRAN, making them a key resource for engagement metrics.
Many of them reveal download, viewing, and bookmarking statistics through an API, or have related rating
sites (ie R package ratings and reviews on http://crantastic.org/).  We’ll also expand our social media support
(Twitter, blogs, Facebook, etc) to include support for the diverse ways software is attributed.
We will locate reverse dependencies to the software from other software projects hosted in central software
library repositories.  This task is programming­language dependant so won’t be easy, but evidence of
component­level reuse is worth the effort.  We’ll explore both location­specific repositories (cran, cpan, pypy; ie
citations of R packages by other R packages [Rebecca 2009]) and mixed language platforms (github, bitbucket;
ie through http://www.githubarchive.org/).
Download, installation, and usage statistics are also crucial.  We propose to identify and support a
usage­tracking API that can be called from software to alert ImpactStory about significant events like
installation, registration, etc.  The functionality will be similar to Google Analytics for software.  We’ll educate
users in responsible use, and respect user privacy settings and opt­outs.
(c) Integration into Impact Profile
Software, data, conferences, blog posts, and even tweets can join papers in a coherent story or lineage, helping
show how these web­native products are important outputs of the scholarly endeavor.  We will support this
within ImpactStory profiles by implementing “research packages”, allowing users to roll software projects with
related products.  We will consult with academics from diverse communities, in informal and ongoing ways, to
learn how to best meet their needs; we currently envision the research packages as flexible hierarchical
headings, allowing researchers to bundle products by grant, project, subject, and so on; these will include a
chronological component, allowing users to trace the evolution of an idea or research program as different types
3

of products are produced.
Conclusion
Capturing indications of third­party engagement and reuse in an impact profile for every software project we will
create an incentive for researchers to value and improve the reusability of research software [Todorov 2012].
With evidence of impact, we look forward to the transition of software from an undervalued by­product to a
first­class research output worthy of investment and promotion.
References
Berkholz, Donnie. 2013. “GitHub Will Hit 5 Million Users Within a Year.” Donnie Berkholz’s Story of Data Blog.
http://redmonk.com/dberkholz/2013/01/21/github­will­hit­5­million­users­within­a­year/.
Boisvert, Ronald F., and Jack W. Davidson. 2013. “Positioning ACM for an Open Access Future.” Communications of the ACM 56 (2):
5. doi:10.1145/2408776.2408777. http://cacm.acm.org/magazines/2013/2/160170­positioning­acm­for­an­open­access­future/fulltext.
Directorate for Biological Sciences. 2012. “UPDATED Information About the Data Management Plan Required for All Proposals.”
http://www.nsf.gov/bio/pubs/BIODMP061511.pdf.
ImpactStory. 2013. “Uncovering the Impact of Software.” ImpactStory Blog.http://blog.impactstory.org/2013/01/18/github/.
Ince, Darrel C, Leslie Hatton, and John Graham­Cumming. 2012. “The Case for Open Computer Programs.” Nature 482 (7386)
(February 23): 485–8. doi:10.1038/nature10836. http://dx.doi.org/10.1038/nature10836.
Jackson, Mike. 2012. “How to Cite and Describe Software.” Software Sustainability Institute Blog.
http://software.ac.uk/so­exactly­what­software­did­you­use.
Jakob. 2012. “Are There Any Statistics That Show the Popularity of Git Versus SVN?” Programmers Stack Exchange.
http://programmers.stackexchange.com/questions/136079/are­there­any­statistics­that­show­the­popularity­of­git­versus­svn.
Jha, Alok. 2012. “Text Mining: What Do Publishers Have Against This Hi­tech Research Tool?” The Guardian.
http://www.guardian.co.uk/science/2012/may/23/text­mining­research­tool­forbidden.
Journal of Open Research Software. “FAQ.” http://openresearchsoftware.metajnl.com/faq/#q2.
Van Noorden, Richard. 2013. “Text­mining Spat Heats Up.” Nature 495 (7441) (March 21): 295. doi:10.1038/495295a.
http://www.nature.com/news/text­mining­spat­heats­up­1.12636.
Piwowar, Heather. 2012a. “Elsevier Agrees UBC Researchers Can Text­mine for Citizen Science, Research Tools.” ResearchRemix Blog.
http://researchremix.wordpress.com/2012/04/17/elsevier­agrees/.
Piwowar, Heather. 2013. “Altmetrics: Value All Research Products.” Nature 493 (7431) (January 10): 159. doi:10.1038/493159a.
http://dx.doi.org/10.1038/493159a.
Priem, Jason, Dario Taraborelli, Paul Groth, and Cameron Neylon. “Altmetrics: a Manifesto.” 2010. http://altmetrics.org/manifesto/.
Rebecca. 2009. “R Package Download and Usage Statistics.” Stack Overflow.
http://stackoverflow.com/questions/1689028/r­package­download­and­usage­statistics.
Science/AAAS. “Science/AAAS | Science Magazine: About the Journal: Information for Authors: General Information for Authors.”
http://www.sciencemag.org/site/feature/contribinfo/prep/gen_info.xhtml#dataavail.
Shockey, Kevin. 2012. “SourceForge Data Repository Shows Rapid New Project Growth.” Open Source Delivers Blog.
http://osdelivers.blackducksoftware.com/2012/07/20/sourceforge­data­repository­shows­rapid­new­project­growth/.
Stodden, Victoria. 2010. “The Scientific Method in Practice: Reproducibility in the Computational Sciences.” SSRN Electronic Journal
(February 9). doi:10.2139/ssrn.1550193. http://papers.ssrn.com/abstract=1550193.
Stodden, Victoria, Jonathan Borwein, and David H. Bailey. 2013. “‘Setting the Default to Reproducible’ in Computational Science
Research.” Siam News. http://www.siam.org/news/news.php?id=2078.
Todorov, Ilian. 2012. “Is the Work of Scientific Software Engineers Recognised in Academia?” Software Sustainability Institute Blog.
http://www.software.ac.uk/blog/2012­04­23­work­scientific­software­engineers­recognised­academia.
Vandewalle, Patrick. 2012. “Code Sharing Is Associated with Research Impact in Image Processing.” Computing in Science & Engineering
14 (4) (July 1): 42–47. doi:10.1109/MCSE.2012.63. http://www.computer.org/csdl/mags/cs/2012/04/mcs2012040042­abs.html.
Wilbanks, John. “Planting Trees.” DEL­FI Blog. http://del­fi.org/post/28843780726/planting­trees.
Williams, Alex. 2013. “Atlassian Bitbucket Passes 1 Million Users, Another Validation Of The Fast­Growing Developer Market.”
TechCrunch.
http://techcrunch.com/2013/06/04/atlassian­bitbucket­passes­1­million­users­another­validation­of­the­fast­growing­developer­mark
et/.
4
