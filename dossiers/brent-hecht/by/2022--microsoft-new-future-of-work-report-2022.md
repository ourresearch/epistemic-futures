---
title: "Microsoft New Future of Work Report 2022"
person: brent-hecht
attendance: unconfirmed
section: by
type: report
year: 2022
venue: "Microsoft Research (Technical Report MSR-TR-2022-3)"
authors: "Jaime Teevan, Brent Hecht, Sonia Jaffe, Nancy Baym, Mary Czerwinski, Shamsi Iqbal, Kristina Nowak, Abigail Sellen, Sean Rintel (eds.)"
source_url: https://www.microsoft.com/en-us/research/publication/microsoft-new-future-of-work-report-2022/
retrieved: 2026-08-13
content: full-text
notes: "Multi-author edited Microsoft Research report; Hecht is one of the editors/contributing authors, so only part of the text is his own writing. Full text from the report PDF (pdftotext; PDF not stored). No OpenAlex record found."
---

# Microsoft New Future of Work Report 2022

## Full text

Microsoft New
Future of Work
Report 2022
A summary of recent research
from Microsoft and around the
world that can help us create a
new and better future of work.

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Editors and Authors
Editors: Jaime Teevan (Chief Scientist and Technical Fellow), Nancy Baym (Senior Principal Research
Manager), Jenna Butler (Senior Applied Research Scientist), Brent Hecht (Director of Applied Science),
Sonia Jaffe (Principal Researcher), Kate Nowak (Senior Behavioral Researcher), Abigail Sellen
(Distinguished Scientist), Longqi Yang (Senior Applied Research Scientist).

Authors: Marcus Ash, Kagonya Awori, Nancy Baym, Mia Bruch, Jenna Butler, Piali Choudhury, Adam
Coleman, Scott Counts, Shiraz Cupala, Mary Czerwinski, Ed Doran, Elizabeth Fetterolf, Mar Gonzalez
Franco, Kunal Gupta, Aaron Halfaker, Constance Hadley, Brent Hecht, Brian Houck, Kori Inkpen, Shamsi
Iqbal, Sonia Jaffe, Eric Knudsen, Stacey Levine, Siân Lindley, Jennifer Neville, Jacki O’Neill, Kate Nowak,
Rick Pollak, Victor Poznanski, Sean Rintel, Abigail Sellen, ​Neha Shah, Siddharth Suri, Jaime Teevan, Adam
Troy, Mengting Wan, Longqi Yang.
Referencing this report:
•

On social media, please include #newfutureofwork and the report URL (https://aka.ms/nfw2022).

•

In academic publications, please cite as: Teevan, J., Baym, N., Butler, J., Hecht, B., Jaffe, S., Nowak, K., Sellen, A., and
Yang, L. (Eds.). Microsoft New Future of Work Report 2022. Microsoft Research Tech Report MSR-TR-2022-3
(https://aka.ms/nfw2022), 2022.

•

To reference an individual section, add the authors listed at the front of the section to the citation text above.
2

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Welcome to the Microsoft New Future of Work Report 2022
Due to the “Great Remote Work Experiment” that began in March 2020 when workplaces around the
world rapidly shut down, work is changing faster than it has in a generation. As many people now
return to the workplace and begin to experiment with hybrid work, a range of different outcomes is
possible. Thankfully, researchers at Microsoft and from around the world have been investigating
evolving hybrid work practices and developing technologies that will address the biggest new
challenges while taking advantage of the biggest new opportunities.
This Microsoft New Future of Work Report 2022 summarizes important recent research developments
related to hybrid work. It highlights themes that have emerged in the findings of the past year and
brings to the fore older research that has become newly relevant. Our hope is that the report will
facilitate knowledge sharing across the research community and among those who track research
related to work and productivity. This research area is unfolding as rapidly as work is changing, and
the purpose of this report is to help the community build on what has been learned this past year.
Never before has there been such an opportunity to actively shape the future of work. With research
and careful study, we can create a new future of work that is meaningful, productive, and equitable.
Jaime Teevan, Chief Scientist and Technical Fellow
3

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

This report emerges from Microsoft’s New Future of Work Initiative
Microsoft has helped shape information work since its founding.
The current moment, however, presents a unique opportunity
for the company to reimagine how digital technology can make
work better for the people who return to the office, those who
stay remote, and those who find the mix of the two that works
for them, the people in their lives, and their organization.

https://aka.ms/nfw

In response to this opportunity, hundreds of researchers from
across Microsoft, LinkedIn, and GitHub have come together to
form the largest research initiative in the company’s history,
called the New Future of Work Initiative. This report is one of the
many public resources the initiative has produced.
The New Future of Work Initiative has also published numerous
research papers, a variety of practical guides, and several
whitepapers that can inform the development of remote and
hybrid work technologies. These resources are available at
https://aka.ms/nfw.
4

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

This report is organized by changes in work practices at four different “scales”
Scale is one framework we use to organize our research efforts into remote and hybrid work. We look
at work at the scales of the individual, team, organization, and society, as well as at their intersections.
• The individuals scale considers topics like the effects of remote
and hybrid work on productivity and wellbeing, as well as the
evolving relationship between work and ‘life’.

Table of Contents
•

Introduction......................1-6

•

Individuals…….................7-22

•

Teams………….................23-53

• The organizations scale considers topics like social capital, crossteam communication, systemic loneliness, office space, employee
expectations, and the Great Reshuffle.

•

Organizations……........54-73

•

Society…….…..................74-85

•

Forecasts………….........86-105

• The society scale considers topics like the changing geography of
work and remote work, disparate impacts, and sustainability.

•

Appendix…................106-111

• The teams scale considers topics like patterns of collaboration, the
role of different tools, meetings and asynchronous collaboration,
and virtual and mixed reality.

Throughout, we highlight research – from Microsoft and elsewhere – using methods like the latest
advances in AI, causal inference, experimentation, field work, surveys, interviews, and prototypebuilding to uncover challenges and opportunities facing workers.

5

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

A selection of key themes in this report
•

The Hybrid Work Era has begun: Employees strongly prefer hybrid work (Slide 8) and employers are increasingly planning
for a hybrid future (Slide 9). The emerging Hybrid Work Era represents a sea change in the geography of work (Slide 76),
and the computing industry will play a large role in whether its benefits are maximized and equitably distributed (Slide 81).

•

New technologies are rapidly improving work: When and where work happens is in flux and co-evolving with the
technology. We are seeing new hybrid meeting environments (Slide 39), transformative improvements in asynchronous
collaboration (Slide 51), novel applications of recommender systems in the workplace (Slide 65), and, of course, the use of
VR and AR productivity environments (Slides 42-48). The share of patents in this space is growing over time (Slide 97).

•

Improved practices can make work better now: Technology improvements may take time, but some changes don't have
to wait. Meetings can immediately become more effective by carefully selecting locations and configurations to complement
their purposes (Slide 32). Managers can expand their set of strategies (Slides 24, 102), leaders can avoid common
misconceptions about hybrid work (Slide 64), and organizations can experiment with meeting-free days (Slide 26).

•

The definition of productivity is expanding: Organizations and employees are increasingly recognizing that wellbeing
(Slide 14), the balance between work and life (Slide 17), inclusivity (Slides 105), and other aspects of the employee
experience are important (Slide 14), and taking steps to address these in a work context (Slide 18).

•

There is much to learn about The Hybrid Work Era: This report provides some answers, but also raises new and exciting
research questions. Will the prevalence of home offices change the way people use office space (Slide 75)? What new AI
scenarios are enabled by the recent acceleration of the digital transformation (Slides 50, 51, 65, 91)? Can we end video
fatigue (Slide 35)? How will remote innovations like meeting chat translate to a hybrid setting (Slides 29, 37)? What will
hybrid work look like in developing markets (Slide 79)? How can we ensure hybrid work makes work more inclusive (Slides
50, 103)?

6

Individual
Productivity and
Wellbeing
Key Contributors: Mary Czerwinski,
Brian Houck, Shamsi Iqbal, Eric
Knudsen, Rick Pollak

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Information workers prefer hybrid over other modes, at least for now
In survey after survey, a plurality or majority of respondents (from a variety of populations) report
wanting to work partly at home and partly in-office. That said, there are signs of shifting preferences.
•

For individuals, hybrid work refers to working part of the time in the office and part time from somewhere else. For
organizations, hybrid can also refer to having a mix of fully on-site and fully off-site employees.

•

Bloom (2021) reports that 47% of American workers prefer to work in a hybrid model, 21% want to return to the
office full time, and 32% want to stay fully remote.
•

The average number of days Americans workers want to work from home (among those who can work from
home) is around 2.8 as of March 2022 (Barrero et al. 2022).

•

A survey in the United Kingdom found an even stronger preference for hybrid – 59% hybrid, 18% full-time office, 23%
fully remote (Bloom et al. 2021).

•

In a global survey, 21% of respondents who had quit their jobs in 2021 reported doing so because of lack of flexible
working hours or location (Microsoft WTI 2022).

•

Employees value flexibility in work location at non-trivial percentages of their salary, e.g., approx. 9% in one recent
survey of U.S. workers who have worked from home during COVID (Barrero et al. 2021) and 8% in a pre-pandemic
controlled experiment (Mas & Pallais 2017).

•

Preferences may shift over time: approximately half of surveyed remote workers reported thinking of switching to
hybrid and vice versa (Microsoft WTI 2022).
•

In a Glint (2021) survey of LinkedIn members, top concerns flagged by employees about working even partly
outside of the office include lower socialization (61%) and lower visibility to leadership (42%).

Barrero, J. M. et al. (2021) “Survey of Working Arrangements and Attitudes December 2021 Updates.” WFH Research.
Barrero, J. M. et al. (2022) “Survey of Working Arrangements and Attitudes April 2022 Updates.” WFH Research.
Bloom, N., et al. (2021). Returning to the Office Will Be Hard. VoxEU.Org.
Bloom, N. (2021). “Hybrid Is the Future of Work.” Stanford Institute for Economic Policy Research.
Microsoft Study: Glint (2021). "Concerns on Virtual Work in a Hybrid World". [Internal]
Mas, A. & Pallais, A. (2017). Valuing Alternative Work Arrangements. American Economic Review 107(12): 3722–59.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.

Barrero et al. (2022) survey of U.S. workers

8

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

More employers are embracing hybrid work, but not to the extent that
employees want

There has been a major increase in employer acceptance of hybrid work, but employees still want more
flexibility than employers are planning. We don’t yet know how this will play out.

•

From uncertainty to hybrid: Employers who were on the fence with their post-COVID plans have overwhelmingly chosen to
go with a hybrid work model, where employees work from home some, but not all of the time. This was a large driver
behind the near-doubling just in 2021 of U.S. employees who said their employer was planning a hybrid work model, from
16.5% to 28.4% (Barrero 2022).

•

Employees appear to be embracing hybrid with their behavior when they have the chance: Health conditions in China made
hybrid work more possible in China in 2021 than elsewhere, and although experiments with hybrid work were rare there,
there was good uptake when the opportunity arose, e.g., around 50% (depending on definition) in recent study by Bloom et
al. (2022) and a survey of Microsoft China employees in mid-2021 found that 35% of employees were working from home
1-2 days/week (Wang et al 2021).

•

However, employers are still embracing hybrid less than employees want: As of March 2022, U.S. employees still want to
work from home more than employers are planning to allow (around 0.5 days/week, depending on type of worker) ( Barrero
et al. 2022). Globally, we see the same dynamic: In AIPAC, 40% of employers are planning flexible work in 2022, but 60% of
employees want it (Microsoft WTI 2022).

•

And fulltime in-person work is more persistent than many believe: Barrero (2022) found ~45% of workers expect to be
working full-time in-person after COVID and in one large global survey, 50% of business leaders in information worker roles
reported that they will require full-time in-person work in 2022 (Microsoft WTI 2022). In Microsoft China in mid-2021, 31%
of survey respondents were working full-time in-person despite the ability to work from home, with connectivity,
collaboration, and equipment as the primary drivers for in-office work (Wang et al. 2021).

•

Barrero (2022)
Sample: U.S. workers

Big questions remain: Will employers become more flexible, or will workers come back to the office? Will they quit instead?
What are the implications of a strong vs. weak labor market? In a weaker labor market, would they behave the same?

Barrero, J. M. (2022). “Economic Review” The Work From Home Outlook in 2022 and Beyond.” Presented at the 2022 ASSA Meetings.
Barrero, J. M., et al. (2022). Survey of Working Arrangements and Attitudes April 2022 Updates. WFH Research.
Mas, A. & Pallais, A. (2017). Valuing Alternative Work Arrangements. American (12): 3722–59.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Microsoft Study: Wang, Y., et al. (2021). GCR Hybrid Workplace Survey. [Internal]

9

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The word productivity has different meanings to different people
Moreover, individual definitions of personal productivity are often multi-faceted.
• Productivity cannot be reduced to a single dimension (or metric), so frameworks
include multiple dimensions. Performance/Outcomes, Collaboration, and
Efficiency are examples of potential dimensions to consider (Forsgren et al.
2021).
• Often causal relationships can only be established with intermediate or
proxy variables.
• Managers are more likely to define productivity as outcomes, and individual
contributors are more likely to define productivity as output (Storey et al. 2021)
• Productivity is something that happens over time, and choosing a specific time
interval is yet another dimension (Smith et al. 2021).
• This diversity of definitions is in addition to many other dimensions introduced
by looking at productivity at different scales: e.g., organizational, national.
• One broader definition of productivity that has been proposed emphasizes
several new dimensions in addition to what is typically considered by managers:
well-being, collaboration, and innovation (Teevan 2021).
Microsoft Study: Forsgren, N., et al. (2021). The SPACE of Developer Productivity. ACM Queue 19(1): 1-29.
Harding, W. B. (2021). Software effort estimates vs popular developer productivity metrics: case study of empirical correlation.
Microsoft Study: Storey, M. A., et al. (2021) How Developers and Managers Define and Trade Productivity for Quality. arXiv preprint, arXiv:2111.04302v2.
Smith S., & Carette, J. (2021). Long-Term Productivity Based on Science, not Preference. arXiv:2112.12580v1.
Microsoft Study: Teevan, J. 2021. Let’s Redefine “Productivity” for the Hybrid Era. Harvard Business Review.

Storey et al. (2021)

10

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The evidence is mixed about short-term productivity during the pandemic
The evidence from attempts to measure short-term productivity following the onset of widespread
remote work paints a mixed picture, with output per unit time potentially differing from self-reported
productivity.
•

Prior to the pandemic, two studies found positive average productivity effects when flexible work policies were introduced
(Bloom et al. 2015; Choudhary et al. 2019).

•

A study of GitHub developers in 2020 found signs of increased output, with pull request volume and push volume up by 17%
and 16% respectively (Forsgren et al. 202)

•

A recent international survey found that self-reported ‘efficiency’ was slightly higher when working from home in every country
surveyed. U.S. workers reported the highest gain at 7.0%, China had the lowest at 0.2%. The average across all countries was 4%
(Aksoy et al. 2022).

•

Self-report data in other surveys is mixed, with typically a large subset of the sample reporting increases and another subset
reporting decreases (e.g., Ford et al. 2021).

•

In a study of a large Asian IT services firm, productivity as measured by output/time dropped by 8-19%. Output declined only
slightly, but time spent working increased from ~5 to ~7 hours per day (Gibbs et al. 2021).

•

In a large global survey, 80% of employees reported being as or more productive since going remote, but 54% of business
leaders reported fearing that productivity was negatively affected since the shift (Microsoft WTI 2022).

Gibbs et al. (2021)

Aksoy et al. (2022)
Aksoy, C.G., et al. (2022). Working From Home Around the World. WFH Research.
Bloom, N., et al. (2015). Does Working from Home Work? Evidence from a Chinese Experiment. The Quarterly Journal of Economics 130(1), 165–218.
Choudhury, P., et al. (2021) Work-from-Anywhere: The Productivity Effects of Geographic Flexibility. Strategic Management Journal 42(4).
Microsoft Study: Ford, D., et al. (2022) A Tale of Two Cities: Software Developers Working from Home During the COVID-19 Pandemic. ACM Transactions on Software Engineering and Methodology 31(2).
Microsoft Study: Forsgren, N., et al. (2020). State of the Octoverse: Finding balance between work and play. GitHub.
Gibbs, M., et al. (2021). Work from Home & Productivity: Evidence from Personnel & Analytics Data on IT Professionals. Social Science Research Network, 3841567.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.

11

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Hybrid work may be able to maximize individual productivity through flexibility
The flexibility that hybrid affords may be able to maximize productivity by allowing people to work in
the way that works best for them (via a hybrid workforce) or by allowing different tasks to be done at
the office and at home (for hybrid employees) – or both.
• In a survey at the start of the shift to remote work, similar numbers of engineers felt
more productive as felt less productive (37% and 32%, respectively) (Ford et al. 2020).
• Even within job type (program managers or developers) and family situation
(having children at home or not) there were substantial numbers of people in
both the more productive and less productive groups.

• “Focused work” was cited as a reason by both 58% of Microsoft employees who plan
to spend more time in the office and a 58% of those who plan to spend more time at
home (Microsoft 2021).
• Hybrid represents a trade-off between the benefits of being in-person versus the
benefits of not having to go into the office. Blending both may increase overall
productivity by 5% (Bloom 2021).

Ford et al. (2021)

• A proviso is that some of the benefits of hybrid hinge on having a critical mass in the
office, so this needs to be managed.

Bloom, N. (2021). Hybrid Work is Here to Stay. Now What? (Back to Work, Better) HBR IdeaCast.
Microsoft Study: Ford, D., et al. (2022). A Tale of Two Cities: Software Developers Working from Home During the COVID-19 Pandemic ACM Transactions on Software Engineering and Methodology 31(2).
Microsoft Study: Microsoft (2021). To Thrive in Hybrid Work, Build a Culture of Trust and Flexibility. Microsoft Worklab: Work Trend Index Pulse Report.

12

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Environmental factors at home and at work might be affecting productivity
Air quality, lighting, temperature, and other environmental factors are often overlooked elements of
work environments. Research has found that these factors are linked to meaningful changes in
productivity, which raises concerns about some work environments, at home and in the office.
• Increased PM2.5 indoor air pollution caused errors by players in chess
tournaments to go up (Künn et al. 2019).
• Warmer temperatures have been linked to lower PSAT performance in the
United States (Park et al. 2020)
• High-noise environments negatively affected memory and motivation and
increased feelings of tiredness in a lab experiment (Jahncke et al. 2011).
• One major open research question is how to prevent the noise pollution
from increased remote calls from exacerbating these effects in open
floorplan offices. Improvements in background noise suppression can help
on the remote side of the call, but challenges remain on the local side (see
e.g., Reddy et al. 2021).

Jahncke, H., et al. (2011). Open-Plan Office Noise: Cognitive Performance and Restoration. Journal of Environmental Psychology 31(4): 373–82.
Künn, S., et al. (2019). Indoor Air Quality and Cognitive Performance. IZA Discussion Paper No. 1263.
Park, R. J. (2020). Heat and Learning. American Economic Journal: Economic Policy 12(2): 306–39.
Microsoft Study: Reddy, C. K. A., et al. (2021). Interspeech 2021 Deep Noise Suppression Challenge. arXiv preprint, arXiv:2101.01902.

Jahncke et al. (2011)

13

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Wellbeing has multiple facets, each of which manifest in work settings
Wellbeing is a term that is often used without a clear understanding of its concrete meaning. However, it
is well-studied in the literature and is often considered to have three components: subjective,
eudaimonic, and social.
•

Subjective (or hedonic) wellbeing focuses on the aspect of experiencing a pleasant life – which is a combination of
positive emotions, and the lack of negative affects to the extent possible (Diener et al. 1991; Schimmack 2007).
• At work it refers to experiencing a satisfactory work life, comprising a combination of positive affect (e.g., enthusiasm,
inspiration), lack of negative affect (e.g., stress and frustration) and people's attitude around their job (Fisher 2014)​.

•

Eudaimonic wellbeing focuses on flourishing, self-realization, or positive psychological functioning (Keyes 2002; Keyes
2005) and is related to the satisfaction of basic human needs for competence, autonomy, relatedness and selfacceptance (Ryff 2014; Fisher 2014; Ryan & Deci 2001).
•

•

At work it involves identifying closely with one’s work (job involvement), finding vigor, dedication and absorption in work
(work engagement), learning, developing oneself (thriving), feeling of doing something important (meaning in work) and
contributing to a greater good (calling at work)

Social wellbeing focuses on the quality connections which are seen as sources of energy (Dutton 2003) as well
as constructs such as social acceptance, social coherence, social contribution and integration, and organizational
belongingness (Fisher 2014).
• At work, it includes satisfaction with peers and satisfaction and exchange relationship with leaders; social support (a
potential buffer against workplace stress) which includes giving and receiving (Shakespeare-Finch & Obst 2011); feeling
of belonging; being embedded in work communities; and group cohesion.

Fisher (2014)

Constructs associated with wellbeing at work

Diener, E., Sandvik, E., & Pavot, W. (1991). Happiness is the frequency, not the intensity, of positive versus negative affect. In F. Strack,et al. (Eds.), Subjective well-being: An interdisciplinary perspective (pp. 119–139). NY: Pergamon.
Dutton, J. E. (2003). Energize your workplace: How to create and sustain high-quality connections at work. John Wiley & Sons.
Fisher, C. (2014). Conceptualizing and Measuring Wellbeing at Work. Wellbeing, C.L. Cooper (Ed.).
Ryan, R., & Deci, E. (2001). On Happiness and Human Potentials: A Review of Research on Hedonic and Eudaimonic Well-Being. Annual Review of Psychology, 52, 141-166.
Ryff C. D. (2014). Psychological well-being revisited: advances in the science and practice of eudaimonia. Psychother Psychosom, 83(1):10-28.
Schimmack, U. (2007). Methodological issues in the assessment of the affective component of subjective well being. Handbook of methods in positive psychology, A. Ohn, & M. van Dulmen (Eds.), Oxford: Oxford University Press. 14
Shakespeare-Finch, J., & Obst, P. L. (2011). The development of the 2-way social support scale: A measure of giving and receiving emotional and instrumental support. Journal of Personality Assessment, 93, 483–490.

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Individuals are recognizing wellbeing as an important component of
workplace experiences

Post-pandemic, individuals are increasingly recognizing the relationship between their workplace
experiences and their wellbeing, and the challenges span across subjective, eudaimonic, and social
wellbeing needs.
• In a study of 31,000 people from 31 countries published by Microsoft in 2022, 53% of
survey respondents are more likely to prioritize their health and wellbeing over
work than before the pandemic (Microsoft WTI 2022).
• Since the onset of the COVID-19 pandemic, a number of pre-cursors of subjective
and eudaimonic wellbeing (e.g., feeling cared for, fair/equitable treatment) have
become stronger statistical correlates of employee happiness compared with prior to
the pandemic (Glint 2021).
• One diary study showed that common self-reported "top challenges" shifted from
meeting frequency (i.e., too many meetings) early in the pandemic to physical and
mental wellbeing issues as the pandemic has continued (Butler & Jaffe 2021).
• Over time following the onset of COVID-19, negative impacts on
physical wellbeing (e.g., fatigue) were most likely to persist among on-site
employees. (Michel et al. 2021).

Butler & Jaffe (2021)

Microsoft Study: Butler, J., & Jaffe, S. (2021). Challenges and gratitude: A diary study of software engineers working from h ome during covid-19 pandemic. 2021 IEEE/ACM 43rd International Conference on Software
Engineering: Software Engineering in Practice (ICSE-SEIP), 362-363.
Microsoft Study: Glint (2021). "Employee Happiness and Success in the New World of Work". LinkedIn. [Internal]
Michel, J. S., et al. (2021). Flattening the Latent Growth Curve? Explaining Within-Person Changes in Employee Well-Being during the COVID-19 Pandemic. Occupational Health Science, 5(3), 247-275.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.

15

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Work-life relationships have evolved over time
The interplay between work and personal life has undergone a series of transformations. Early work
showed work and life as two competing domains, followed by a focus on equal balance and more
recently they are considered complementary where attention can shift fluidly based on priority.
•

Work-life conflict: A few decades ago work-life relationships were viewed as two competing
sides of a vertical axis, termed as work-life conflict (Greenhaus & Beutell 1985). The conflict
arises from cases where the time devoted to the needs of one role makes it difficult to fulfil
needs of the other, strain from participation in one role makes it difficult to fulfill needs of
the other, and specific behaviors needed by one role impacts the requirements of the
other.

•

Work-life balance: Later in the early 2000s the focus shifted towards acknowledging equal
importance of both work and life in work-life relationships (Kaliath & Brough 2008).
Conceptualizations of work-life balance include equity across, satisfaction with and
perceived control between multiple roles, relationship between the conflict and facilitation
and compatibility with one’s life priorities.

•

Work-life integration: More recently, the concept of work-life integration is gaining
popularity. Work and life demands are dynamic and transactional, and is a function of the
amount of segmentation and flexibility possible to maintain a balance that prioritizes one
over the other fluidly (Feigon et al. 2018).

Work-Family Role Pressure Incompatibility
(Greenhaus & Beutell 1985)

Feigon, M., et al. (2018). Work-life integration in neuropsychology: a review of the existing literature and preliminary recommendations. The Clinical Neuropsychologist, 2018, 32(2), 300-317.
Greenhaus, J. H., & Beutell, N. J. (1985). Sources of conflict between work and family roles. Academy of Management Review, 31(1), 72-92.
Kalliath, T., & Brough, P. (2008). A review of the meaning of the balance construct. Journal of Management and Organization, 14, 323-327.

16

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Priorities have shifted towards tighter integration of work and personal needs
People report a greater need for prioritizing health, wellbeing, and family over work compared to prepandemic times and they wish to better integrate those needs through how and where they work. This
requires renewed focus on spillover effects of performance, skills and affect across work and personal
life.
Compared to pre-pandemic, how likely are you to
prioritize your health and wellbeing over work?”

•

In Microsoft's Work Trend Index study, 47% of the survey respondents reported that they are more likely to
put family and personal life over work than they were before the pandemic (Microsoft WTI 2022).

• 53% reported they were more likely to prioritize their health and wellbeing over work than before (see
chart).
• Flexibility in where and how people work is a key priority moving forward: 51% of the hybrid employees
reported that they will consider a switch to remote, and 57% remote employees said that they will
consider a switch to hybrid.
•

As people embrace hybrid and remote work, renewed focus is needed to best manage work-life integration
challenges. Pre-pandemic research on work-life integration has highlighted areas of importance (Edwards &
Rothbard 2000); these topics must be revisited with the current shift in working preferences.

• Performance: risk of pursuing the domain (between work and life) that offers greater rewards and
fulfilment at the expense of the other.
• Health and wellbeing: risk of increase in stress, fatigue and burnout due to resource drain in one
domain leaving insufficient resources for the other.

• Enrichment: benefits of skills, abilities, values and moods in one domain positively enhancing the
quality of life in another domain.

Microsoft WTI (2022)
Edwards, J. R., & Rothbard, N. P. (2000). Mechanisms linking work and family: Clarifying the relationship between work and family constructs. Academy of Management Review, 25, 178-199.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.

17

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Successful work-life integration requires goal prioritization and adjustments
to work patterns

Work-life integration is highly personalized and depends on one's goals and circumstances. People have
been adapting their existing ways of getting things done according to their priorities and there is a
great opportunity for technology to help.
•

A review of work-life integration challenges in neurophysiology suggests that it is a highly personalized path based on one’s go als,
pursuits, roles and circumstances. Recommendations include developing plans of career growth, establishing expectations and
boundaries early, delegation and prioritizing self-care (Feigon et al. 2018).

•

Anthropological studies of the way people separate work and life suggest that some people compartmentalize work and life in a way
that one doesn't interfere with the other (Nippert-Eng 1996), but it becomes challenging when work and life coexist in the same place
(e.g., when people work from home).

•

With a shift to remote work and elimination of physical boundaries knowledge workers felt a sense of being 'always-on'. Tools that
help individuals disconnect after work can reduce stress and promote employee wellbeing and reduce employee liability stemmin g
from after-hour work (Williams 2018).

•

Microsoft released Virtual Commute to help Teams users transition out of work at the end of the day.

•

Remote work has also changed how people track their productivity and plan their work and life. Because of the greater work-life
integration, people find it effective to break down their tasks more and manually track their time (Ahmetoglu et al. 2021).

•

Meeting free days can help individuals find time to do individual work and reduce the stress of meeting overload. Studies have shown
on average 78% reduction in meeting volume and 22% increase in focused work on meeting free days (Houck 2021).

Screenshot from Microsoft
Viva’s Virtual Commute

Ahmetoglu, Y., et al. (2021). Disengaged From Planning During the Lockdown? An Interview Study in an Academic Setting. IEEE Pervasive Computing, 20(4): 18-25.
Feigon, M., et al. (2018). Work-life integration in neuropsychology: a review of the existing literature and preliminary recommendations. The Clinical Neuropsychologist, 32(2): 300-317.
Microsoft Study: Houck, B. (2021). “Happy and productive hybrid developers: How to have it all” [video].
18
Nippert-Eng, C. E. (1996). Home and work: Negotiating boundaries through everyday life. Chicago: University of Chicago Press.
Microsoft Study: Williams, A. C., et al. (2018). Supporting Workplace Detachment and Reattachment with Conversational Intelligence. Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems., Paper 88, 1–13.

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Remote work can have mixed effects on wellbeing
Pre-pandemic research on the relationship between remote work practices and wellbeing has shown
mixed results. Remote work and subsequent work-life balance and job autonomy can improve job
satisfaction, but employees may feel socially isolated, guilty and try to overcompensate.
• An extensive pre-pandemic meta review of 63 studies emphasizes the complex relationship between remote work and
work-related wellbeing – listing both positive and negative outcomes (Charalampous et al. 2019).
• Anderson et al. (2015) and others showed that remote workers reported higher degrees of positive emotions and lower
degrees of negative emotions. However, working from home can cause increase in other negative emotions such as guilt
and irritability (Mann & Holdsworth 2003), often leading to overcompensating at work.
• Feelings of autonomy through remote work positively affects job satisfaction and decreased emotional exhaustion
(Sadesmukh 2012) but remote work is also associated with lower perceived career prospects (Gajendran & Harrison 2009).
• Social support is most depleted when employees work from home which also increases emotional exhaustion (Sardeshmukh
2012) but with organizational support employees feel less isolated, subsequently improving their job satisfaction levels
(Bentley 2016).

Anderson, A. J., et al. (2015). The impact of telework on emotional experience: When, and for whom, does telework improve dai ly affective well-being? European Journal of Work and Organizational Psychology, 24, 882–897.
Bentley, T. A., et al. (2016). The role of organisational support in teleworker wellbeing: A socio-technical systems approach. Applied Ergonomics, 52, 207–215.
Charalampous, M., et al. (2018). Systematically reviewing remote e-workers’ well-being at work: a multidimensional approach. European Journal of Work and Organizational Psychology 28: 51 - 73.
Gajendran, R. S., & Harrison, D. A. (2007). The good, the bad, and the unknown about telecommuting: Meta-analysis of psychological mediators and individual consequences. Journal of Applied Psychology, 92, 1524–1541.
Mann, S., & Holdsworth, L. (2003). The psychological impact of teleworking: Stress, emotions and health. New Technology, Work and Employment, 18, 196–211.
Sardeshmukh, S. R., et al. (2012). Impact of telework on exhaustion and job engagement: A job demands and job resources model. New Technology, Work and Employment, 27, 193–207.

19

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Working from home offers flexibility but also impacts permeability across domains
One’s level of work-life integration or segmentation depends on both the flexibility – one’s ability to
shift one’s boundary spatially or temporally to meet the demands of the other domain – and the
permeability – how much intrusion occurs from one domain to the other
•

According to a national survey that followed Canadian workers between September 2019 and April -June 2020, during
the pandemic, work-life conflict decreased for people with no children at home, or with older children compared to prepandemic. In contrast people with children < 12 years old did not see any change in the contention between work and
life demands (Schieman et al. 2021).

•

A study with Redditors showed that choosing when and how to work gave them more freedom and flexibility to choose
how to spend their remaining time – including more leisure time with family, more time to work on personal projects and
hobbies and more freedom to exercise (Cho et al. 2022).

•

On the other hand, flexible work patterns impact permeability- intrusion of work into personal time. Research has shown
emergence of a ‘third productivity peak’, where work hours are extending beyond the regular pre -pandemic 9-5, and
emails are shown to be the most frequent activity during the after-hour work (Morshed et al. 2021).

•

Telemetry also showed an increase in the span of work time – a 46 minute increase in the span of workdays, 28%
increase in after-hours work, and a 14% increase in weekend work (Microsoft WTI 2022).

•

After-hour communications may impact colleagues’ work-life balance. In a survey, 78% of engineers reported that it had
been challenging establishing a work-life boundary during COVID. Engineers who reported such challenges were 22%
more likely to report decreased productivity (Ford et al. 2021).

Cho, J., et al. (2022). Topophilia, Placemaking, and Boundary Work: Exploring the Psycho-Social Impact of the COVID-19 Work-From-Home Experience. Proceedings
of the ACM Human.-Computer Interact. 6, GROUP, Article 24.
Microsoft Study: Ford, D., et al. (2022). A Tale of Two Cities: Software Developers Working from Home During the COVID-19 Pandemic. ACM Transactions on
Software Engineering and Methodology 31(2).
Microsoft Study: Morshed, B. M., et al. (2022). Advancing the Understanding and Measurement of Workplace Stress in Remote Inf ormation Workers from Passive
Sensors and Behavioral Data. (Under Review)
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Schieman, S., et al. (2021). Work-life conflict during the COVID-19 pandemic. Socius: Sociological Research for a Dynamic World 7 (2021), 1–19.

Additional productivity peak after hours as indicated by
keyboard activity on productivity app (Morshed et al. 2021)

After hour collaboration is inversely related to worklife balance favorability scores (Storey et al. 2021)

20

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Burnout has been on the rise during the pandemic
Burnout, characterized by emotional exhaustion, depersonalization, and a reduced sense of
accomplishment (Maslach & Jackson 1981) jumped in summer 2020 and currently remains high.

• An analysis of employee engagement survey comments also demonstrated increases in mentions of staffing and
workload issues (Glint 2020).

• Microsoft’s longitudinal interviews with organizational decision makers over four time periods in 2020 also
highlighted rising burnout (Coleman 2020).
o June 2020: moving to remote work had driven higher employee output, but many leaders saw these
productivity gains happening via longer working hours, not increased efficiency.
o September 2020: these same leaders struggled with burnout given the breadth of new challenges they faced:
e.g., employees relocating to new states or countries, client revenues falling, and the need to connect with
employees on a more regular, personalized basis.
“I am a naturally caffeinated person - I am ready to go into meetings and bring energy - but doing this
remotely is simply exhausting as I have to look at the camera for 9 hours, it is a lot. I over energize”
– Head of Global Ops & Strategy (Entertainment & Media) US

• A survey of 2067 attorneys demonstrated that one cause of burnout is the work of feigning appropriate emotional
displays, an expectation in many other careers as well (Powers & Myers 2020).

Burnout Signal Rate
(Rolling Three Month Average)
8%

Estimated start of business
impact of COVID-19

7%
6%

5%

Jul. 2019
Aug. 2019
Sep. 2019
Oct. 2019
Nov. 2019
Dec. 2019
Jan. 2020
Feb. 2020
Mar. 2020
Apr. 2020
May 2020
Jun. 2020
Jul. 2020
Aug. 2020
Sep. 2020
Oct. 2020
Nov. 2020
Dec. 2020
Jan. 2021
Feb. 2021
Mar. 2021
Apr. 2021
May 2021
Jun. 2021
Jul. 2021
Aug. 2021
Sep. 2021
Oct. 2021
Nov. 2021
Dec. 2021
Jan. 2022
Feb. 2022

• Glint's February 2021 Employee Well-Being Report (Glint 2021) identified three top contributors to employees’ sense
of burnout. Among the survey respondents who reported feeling burned out, these the most common stated
reasons were:
o Feeling disconnected from colleagues (selected by 41% of survey respondents who also reported feeling
burned out).
o Overwhelming workload (selected by 38% of burned out respondents).
o Conflict between demands from home and work (selected by 35% of burned out respondents).

Glint (2022)
Note: Glint’s Burnout Signal Rate (BSR) represents the percent of
comments from a global sample accompanying the key
Engagement question and assigned the tag 'Burnout' by
Narrative Intelligence.

Microsoft Study: Coleman, A (2020): 2020's indelible impact on the way we will work in the future. Microsoft Research.
Microsoft Study: Glint (2020). Employee Well-Being Report. LinkedIn.
Microsoft Study: Glint (2021). Employee Well-Being Report. LinkedIn.
Microsoft Study: Glint (2022). Employee Well-Being Report. LinkedIn.
Maslach, C., & Jackson, S. (1981). The measurement of experienced burnout. Journal of Organizational Behavior, 2(2), 99-113.
Powers, S. R., & Myers (2020). Work-Related Emotional Communication Model of Burnout: An Analysis of Emotions for Hire. Communication Management Quarterly, 34(2), 155-187.

21

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Stress is costly and can lead to burnout at work, but interventions can help
Work-related stress increases the risk of mental and physical health disorders, decreases productivity
due to absenteeism and burnout, impairs decision making, decreases overall job satisfaction & increases
rates of stress-related accidents and employee medical, legal, and insurance costs.
•

Workplace is the #1 stressor for American adults, costing the U.S. economy $300 billion annually (APA 2017).
COVID-19 has exacerbated these issues.

•

Workplace stress can also spillover into life outside of work, disrupting the overall wellbeing of workers
(Grzywacz et al. 2002).

•

Workplace stress intervention strategies such as organizational changes, individual stress management skills
training, & therapeutic counseling are recommended for long-term stress reduction (Cooper et al. 1997).

•

Individual-based stress management interventions (e.g., cognitive-behavioral skills , meditation, exercise, etc.)
have been shown effective on psychological, physiological, and organizational outcome measures (Richardson
et al. 2008; Howe et al. 2022).

•

We have an opportunity to tightly integrate digital micro-interventions into productivity tools to significantly
reduce stress (Howe et al. 2022).

•

In a survey of tech employees, frequent and intense stressors are commonly associated with work overload
and its impact on work-life balance (Morshed et al. 2022, see figure).
Morshed et al. (2022)

APA Working Group on Stress and Health Disparities (2017). Stress and health disparities: Contexts, mechanisms, and interventions among racial/ethnic minority and low-socioeconomic status populations.
Cooper, C. L., & Cartwright, S. (1997). An intervention strategy for workplace stress. Journal of psychosomatic research 43(1), 7–16.
Grzywacz, J. G., et al. (2002). Work– family spillover and daily reports of work and family stress in the adult labor force. Family relations 51(1).
Microsoft Study: Howe, E., et al. (2022). Design of Digital Workplace Stress-Reduction Intervention Systems: Effects of Intervention Type and Timing. CHI Conference on Human Factors in Computing Systems (CHI ’22).
Microsoft Study: Morshed, M. B., et al. (2022). “Advancing the Understanding and Measurement of Workplace Stress in Remote In formation Workers from Passive Sensors and Behavioral Data.” (Under Review)
Richardson, K. M. & Rothstein, H. R. (2008). Effects of occupational stress management intervention programs: a meta-analysis. Journal of Occupational Health Psychology 13(1).

22

Team
Collaboration
Key Contributors: Sean Rintel, Abigail
Sellen, Mar Gonzalez Franco, Aaron
Halfaker, Victor Poznanski, Kori
Inkpen, Marcus Ash, Piali Choudhury,
Shiraz Cupala, Kunal Gupta

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Remote and hybrid team leadership requires a focus on relationships
Relationship-focused leadership can motivate and support virtual team members to help address
unfulfilled team needs, especially as virtual team size increases.
•

Effective leadership in hybrid conditions requires new skills. Leaders need to play four roles - conductor, catalyst,
coach, and champion - across two modes: virtual coordination mode and in-person collaboration mode
(Hooijberg & Watkins 2021) .

•

Research on virtual leadership has generally assumed that physical dispersion and technology dependence
represent obstacles to be overcome. However, there may also be virtues to separation depending on task
complexity, collocation of the worker with experienced peers, and manager supervisory experience (Bell et al.
2019).

•

Brown et al.’s (2021) meta-analysis of 116 empirical studies of leadership in virtual teams explores the relative
effectiveness of relationship-focused leadership (focused on mission, collegiality, and interpersonal
engagements) and task-focused leadership (focused on processes and procedures). Both relationship and taskfocused leadership have positive effects on team performance, but relationship-focused team leadership shows
stronger effects on virtual team performance in teams with larger team size. Relationship-focused leadership
had equal effects on virtual team performance in long term and ad-hoc teams, but task-oriented leadership had
weaker effects for ad-hoc teams compared to long-term teams.

Hooijberg & Watkins (2021) argue that hybrid
work requires multimodal leadership

Bell, B. S., et al. (2019). Leading from a distance: Advancements in virtual leadership research. In R. N. Landers (Ed.), The Cambridge Handbook of Technology and Employee Behavior (pp. 387–418). Cambridge.
Brown, S. G., et al. (2021). Leadership and virtual team performance: A meta-analytic investigation. European Journal of Work and Organizational Psychology, 30(5): 672-685.
Hooijberg, R., & Watkins, M. (2021). The Future of Team Leadership Is Multimodal. MIT Sloan Management Review.

24

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Interpersonal trust is key to successful virtual and hybrid teams
Remote and hybrid teams need to develop methods for establishing and maintaining trust. Swift trust in
short-term teams depends heavily on team composition and an open conversational environment.
•

Interpersonal trust is about confidence in people and a willingness to be vulnerable to one another (Ma et al. 2019). Team
trust has a cognitive aspect (reciprocal knowledge of competences and credibility) and an affective dimension (reciprocal
perception of emotional investment, care, and concern about others) (Alves et al. 2022).

•

Morrison-Smith & Ruiz (2020) find that geographical, temporal, and perceived distance all reduce awareness of activities
and schedules. As these decrease, so too does confidence in others and willingness to seek help. As a result, there may be
increased interpersonal and task conflicts. There are other contributing factors, such as the nature of work, management
and leadership, and group composition, but interpersonal trust is often key. Virtuality also has its opportunities. Alves et al.
(2022) find that virtuality may have a buffering effect that reduces conflict, but this still requires cognitive trust to be high.

•

Organizations should explicitly assist creation of team common ground (shared vocabulary, mental models, practices,
experiences etc.) and work standards, facilitate team communication, provide mechanisms for teamwork transparency
(Morrison-Smith et al. 2020; Lechner & Mortlock, 2021). HR also has an important role to play in improving practices for
workload sharing, group rewards, and team competency development, which are antecedent to building the interpersonal
trust needed for team collaboration, and ultimately feed into team innovation Bulińska-Stangrecka & Bagieńska, 2019).

•

Not all teams are permanent. Fast-response virtual teams (FRVTs) form to deal with periodic needs or emergent challenges.
Team composition is crucial (Kroeger, et al. 2021), but to avoid the risk of intuitive decisions, establishing a safe
conversational space for exploring diverse perspective is important (Yu, et al. 2021).

•

Technology can assist in building interpersonal trust, making it easy to see who is working where and what they have
contributed (e.g., Microsoft Loop), while also improving spontaneous engagement through the day (see also: “Spatial
environments are conducive to spontaneous engagement”).

Interpersonal trust has a crucial place in team
innovation, and HR has an important role to play
(Bulińska-Stangrecka & Bagieńska 2019)

Alves, M. P., et al. (2022). Can virtuality be protective of team trust? Conflict and effectiveness in hybrid teams. Behaviour & Information Technology, Article 2046163.
Bulińska-Stangrecka, H., & Bagieńska, A. (2019). HR Practices for Supporting Interpersonal Trust and Its Consequences for Team Collaboration and Innovation. Sustainability, 11(16) , Article 4423 .
Kroeger, F., Racko, G., & Burchell, B. (2021). How to create trust quickly: A comparative empirical investigation of the bases of swift trust. Cambridge Journal of Economics, 45(1): 129–150.
Lechner, A., & Mortlock, J. T. (2021). How to create psychological safety in virtual teams. Organizational Dynamics, 6, Article 00849.
Ma, J., et al. (2019). Interpersonal Trust in Organizations. Oxford Research Encyclopedia of Business and Management.
Morrison-Smith, S., & Ruiz, J. (2020). Challenges and barriers in virtual teams: a literature review. SN Applied Science, 2, Article 1096.
Microsoft Study: Microsoft (2021). To Thrive in Hybrid Work, Build a Culture of Trust and Flexibility. Microsoft Worklab: WTI Pulse Report.
Yu, X., Shen, Y., & Khazanchi, D. (2021). Swift Trust and Sensemaking in Fast Response Virtual Teams. Journal of Computer Information Systems, Article 1978114.

25

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Global teamwork must be intentional
Temporal brokerage is the unofficial enabler of global teams. Global teams may succeed fast
but fail slowly. Cultural Intelligence training increases global team performance.
•

Temporal brokerage (Mell at al. 2021) is an informal coordination role that an employee takes on within a
dispersed team’s set of time zones bridging subgroups that have little or no temporal overlap with each other.
Two large studies (N=4553 and N=123,586) find that temporal brokering increases the ability of teams to do
complex projects. This comes at a cost of increased workload and reduced number of projects for the temporal
broker, but the projects completed were, on average, of higher quality. Other factors in the experience or skills
of a temporal broker may shape team-level performance, such as the broker’s level of multicultural experience
and their facility with virtual communication. Leaving the temporal broker unofficial risks uncertainty. Temporal
brokerage may be considered as an aspect of the conductor role in relationship-first leadership. (See previous
slide on leadership and relationships.)

•

Mors & Waguespack (2021) compared times and outcomes of 5,250 teams working together on collaborative
documents for the Internet Engineering Task Force (IETF). Dispersed research teams reached success faster than
non-dispersed teams, which may result from choosing low risk projects or, when choosing high risk projects,
investing more early effort to minimize coordination challenges. However, dispersed teams fail more slowly than
non-dispersed teams, possibly unwilling to let go of their idea or forgo upfront investments. This slow failure
may delay reinvestment of resources in other projects.

•

Technology to coordination and handover would benefit global teams. This might enable temporal brokers to
concentrate on relational aspects of teamwork, while removing some burdens of the unofficial role. Planning for
global team success should also involve up-front clarity around early milestones.

•

Cultural Intelligence training also increases global team performance, both in the team and of individuals (Yari,
et al. 2018; Prebitero & Toledano 2018).

The temporal broker is the ‘middle of the bow
tie’ playing an unofficial role coordinating
global teamwork (Mell et al. 2021)

Global teams succeed fast and fail slow
(Mors & Waguespack 2021)

Mell, J. N., et al. (2021). Bridging Temporal Divides: Temporal Brokerage in Global Teams and Its Impact on Individual Performance. Organization Science, 32(3): 731–751.
Mors, M. L., & Waguespack, D. M. (2021). Fast success and slow failure: The process speed of dispersed research teams. Research Policy, 50(5), Article 104222.
Presbitero, A., & Toledano, L. S. (2018). Global team members’ performance and the roles of cross-cultural training, cultural intelligence, and contact intensity: The case of global teams in IT offshoring sector.
The International Journal of Human Resource Management, 29(14): 2188–2208.
Yari, N., Lankut, E., Alon, I., & Richter, N. F. (2020). Cultural intelligence, global mindset, and cross-cultural competencies: A systematic review using bibliometric methods. European Journal of International
Management, 14(2): 210–250.

26

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Mixed gender groups have a higher collective intelligence
Women’s communication in teams often provides significant leadership and coordination, even if they
are not in official roles. On the other hand, gender inequalities may be exacerbated in video meetings.
•

Collective intelligence (Wooley et al. 2015) improves when more women are part of a mixed group ( Riedl et al, 2021).
Having more women in a team has a significant positive impact on how strategy and effort contribute to collective
intelligence, and “other things being equal, a group with one standard deviation higher CI would increase task
performance by 18%, plus or minus about 12%”. Further, overall, group collaboration process is more important in
predicting collective intelligence than the skill of individual members (Riedl et al. 2021).

•

Thinnyun et al. (2021) found that women in a collaborative learning community posted more questions than men (but
answer proportions are balanced), spent more time on the site, and achieve higher reputation scores on average. In
Garcia et al.’s (2021) study of student teams using Slack to complete an eight-week project, women sent far more
messages than men, and provided significant unofficial leadership, coordination, and project-monitoring.

•

The coordinative work of women’s communication is a form of leadership which should be rewarded, instead of being
unrecognized glue work often undertaken by women (Reilly 2018). Organizations should select promising combinations
of people for teams instead of over-indexing on individual skill, evaluate groups as well as individuals, and scaffold
coordination with technological aids such as intelligent project overviews and task tracking ( Reidl et al. 2021).

•

However, video meetings may exacerbate inequalities faced by women in meetings, such as being held to higher or
stereotypical appearance standards than men, and negative treatment of how they talk (Dhawan et al. 2021). Standaert
& Thunus (2022) found that men participated in more meetings than women pre-pandemic and participate in even
more virtual meetings since the pandemic. Women also report more difficulty speaking up in virtual meetings than men.

Dhawan, N., et al. (2021.) Videoconferencing Etiquette: Promoting Gender Equity During Virtual Meetings. Journal of Women’s Health, 30(4): 460–465.
Garcia, R., et al. (2022). Gender Influence on Communication Initiated within Student Teams. ACM SIGCSE’22, 1: 432–438.
Reilly, T. (2018) Being Glue. No Idea Blog.
Riedl, C., et al. (2021). Quantifying collective intelligence in human groups. Proceedings of the National Academy of Sciences, 118(21), Article e2005737118.
Standaert, W. & Thunus, S. (2022). Virtual Meetings during the Pandemic: Boon or Bane for Gender Inequality. 30th European Conference on Information Systems.
Thinnyun, A., et al. (2021). Gender and Engagement in CS Courses on Piazza. ACM SIGCSE’21: 432–438.
Woolley, A.W., et al. (2015) Collective Intelligence and Group Performance. Current Directions in Psychological Science, 24(6): 420-424.

Women have a significant impact on collective
intelligence (Riedl et al. 2021)

Difficulty reported by men and women
related to speaking up in virtual meetings
(Standaert & Thunus 2022)

27

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Meeting-free days improve both cooperation and self-reliance
Having some meetings is essential for coordination and social ties, but meeting-free days improve
overall work and satisfaction. The change to fewer meetings requires better meeting management.
•

Laker et al. (2022) surveyed 76 companies employing more than 1,000 people across 50 countries about meeting-free days
(that is, prohibiting synchronous 1:1 to large meetings, but not asynchronous communication such as email or messaging).
o Participants reported perceptions of cooperation, autonomy, communication, cooperation, engagement, productivity,
satisfaction, stress, and micromanaging.
o

More meeting-free days were associated with better autonomy, (lower) stress, and (perhaps surprisingly) better
communication.

o Four meeting-free days per week was associated with better cooperation, engagement, productivity, and (lower)
micromanaging.
o Four meeting-free days per week was associated with the highest satisfaction.
o As such, allocating some days for meetings is essential for the maintenance of social ties and management of schedules
that, in turn, impact cooperation etc.
•

In a study of 435 Microsoft employees from one product group during COVID-19, No Meeting Fridays had a very positive
response. 75% of people liked them and 93% said it was respected by their manager. In addition, 73% of people said it was
good for their wellbeing and 77% said it gave them more focus time. However, some verbatims said that this made their
Thursdays or Mondays too meeting heavy, and thus the practice was instituted every second week (Butler & Jaffe, 2020).

•

Limiting meeting days requires planning. Pushing all meetings to a different day can lead to scheduling overload and stress a nd
limit employees’ flexibility. Managers should solicit feedback before and during a period of change (see also Perlow, et al.
2017), encourage asynchronous communication, and ensure that the meetings they do have are run more intentionally (Rintel
et al. 2021).
Meeting-free days improve overall work and
satisfaction (Laker et al. 2022)

Microsoft Study: Butler, J., & Jaffe, S. (2021). Challenges and gratitude: A diary study of software engineers working from h ome during covid-19 pandemic. ICSE-SEIP’21, 362-363.
Laker, B., et al. (2022). The Surprising Impact of Meeting-Free Days. MIT Sloan Management Review.
Perlow, L. A., et al. (2017). Stop the Meeting Madness. Harvard Business Review.
Microsoft Study: Rintel, S., et al. (2021). A guide to having better remote meetings by being more intentional. The New Future of Work.

28

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Chat workspaces can replace some meetings, when used thoughtfully
Routine meetings can be replaced with text-based chat, but there is a need to manage chat overload.
Successful teams align work routines to communicate in bursts, interspersed with individual work
periods.
•

Stray et al. (2021) report on two groups in a software company using Slack. Chat reduced the number of some routine
meetings, but also often sparked ad hoc meetings. Chat could also be overwhelming in volume, requiring context
switching and interrupting focused work.

•

Shi et al. (2021) used natural language processing to analyze over 173K dialogs of developer chat in Glitter. To reduce chat
overload (volume, frequency and timing of notifications etc.), they suggest that individuals provide examples when seeking
help, avoid asking new questions in ongoing discussions, and be aware of others’ quiet/focus time. Communities should
also improve information repositories such as FAQs and onboarding documentation, so that chat is used for problem
solving.

•

Riedl & Woolley (2017; 2020) found that successful remote teams work and communicate in bursts, interspersed with
periods of individual work or non-work. In an experiment using 260 people working in geo- and time zone-distributed
teams of 5, they found that high performing teams had high levels of responsiveness and coordination, but this
coordination was not associated with predictable points such as beginning, middle, or end of work, or external temporal
rhythms. As such, Reidl and Williams Wooley propose changing team assumptions about asynchronous communication as
meaning ‘everyone sending messages whenever they feel like it’ and instead align work routines to communicate in short
periods when everybody can respond rapidly and attentively. This can be extrapolated to also choosing communication
modalities (meetings or chat/email) suited to task responsiveness. Tools that help people communicate and create in the
same space (e.g., Microsoft Loop) will reduce context switching and allow better integration of content creation and coworking.

Shi et al. (2021) analyze OSS developer chat in Glitter

Riedl, C., & Woolley, A. W. (2017). Teams vs. Crowds: A Field Test of the Relative Contribution of Incentives, Member Ability, and Emergent Collaboration to Crowd-Based Problem Solving Performance. AMD 3(4), 382–403.
Riedl, C., & Woolley, A. W. (2020). Successful Remote Teams Communicate in Bursts. Harvard Business Review.
Shi, L., et al. (2021). A first look at developers’ live chat on Gitter. AMC ESEC/FSE’21: 391–403.
Stray, V., et al. (2021). Using Objectives and Key Results (OKRs) and Slack: A Case Study of Coordination in Large-Scale Distributed Agile. TechRxiv. Preprint, Article 16892161.

29

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Team creativity may benefit from low-fidelity asynchronous methods
Group creativity is not necessarily always at its best when people are together. Technological constraints
may suit asynchronous ideation methods such as brainwriting, and may improve decision quality.
•

The lack of shared collaboration tools has been a reported pain point for team creativity in remote and hybrid work, but
reviews show that individual ideation can be richer than group ideation, because the processes of sharing ideas live can bloc k
ideation (Paulus & Kenworthy 2022; Thompson 2020). Further, while in-person two-person ideation may lead to the
generation of more ideas than video meetings, the decision quality of ideas in video meetings can be higher than in-person
(Brucks & Levav 2022).

•

Toumi et al. (2021) review a range of technologies for group design ideation and found that even low fidelity systems for
brainwriting (where participants write independently then pass their contribution to the next participants) or digital sticky
notes can work well for the actual process, but social loafing remains a problem (some members may do less work in a
group). Social loafing may be less noticeable when remote/hybrid than in-person – but may also be difficult to disambiguate
from difficulty of remote participation in general.

•

Brainwriting (Rituzzi & De Napoli 2020) and related asynchronous concepts such as the idea tree (Stokols, et al. 2019) are
especially well suited to asynchronous creativity, as there are general findings that task alternation seems to reduce fixati on
effects on early ideas (Sio et al. 2017; Diehl & Stroebe 1987).

•

Creativity does not ‘just happen’: training in effective group processes is crucial and the process needs to be managed. Taskappropriate diversity of participants (e.g., people from the set of roles for whom a solution is being determined) is also
helpful for creativity, and may be enabled more in remote and hybrid situations (Paulus & Kenworthy 2022; Michinov &
Jeanson 2021).

Asynchronous ideation methods such as
brainwriting suit distributed groups

Brucks, M.S., Levav, J. (2022). Virtual communication curbs creative idea generation. Nature, Article s41586-022-04643-y.
Diehl, M., & Stroebe, W. (1987). Productivity loss in brainstorming groups: Toward the solution of a riddle. Journal of Personality and Social Psychology, 53(3): 497–509.
Michinov, N., & Jeanson, S. (2021). Creativity in Scientific Research: Multidisciplinarity Fosters Depth of Ideas Among Scientists in Electronic “Brainwriting” Groups. Human Factors.
Paulus, P. B., & Kenworthy, J.B. (2022). Research Findings on Ideational Creativity in Groups. In Doboli, S., et al. (eds) Creativity and Innovation. Understanding Complex Systems. Springer.
Rizzuti, S., & De Napoli, L. (2020). Proposal of a Framework Based on Continuous Brainwriting to Expand Mindfulness in Concept Generation. In Design Tools and Methods in Industrial Engineering, Springer: 352–360.
Sio, U. N., Kotovsky, K., & Cagan, J. (2017). The Facilitating Role of Task Alternation on Group Idea Generation. Journal of Applied Research in Memory and Cognition, 6(4): 485-295.
Stokols, D. et al. (2019) Idea tree: A tool for brainstorming ideas in cross-disciplinary teams. Integration and Implementation Insights.
Thompson, L. (2020). Virtual Collaboration Won’t Be the Death of Creativity. MIT Sloan Management Review, 62(2): 42-46.
Toumi, K., et al. (2021). Technologies for Supporting Creativity in Design: A View of Physical and Virtual Environments with Regard to Cognitive and Social Processes. Creativity. Theories – Research – Applications, 8(1): 189–212.

30

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Spontaneous and serendipitous talk is still hard for distributed teams
Opportunistic informal talk is harder for remote and hybrid teams, but is crucial for knowledge sharing,
trust, and morale. In the short term, informal talk can be organized around social rituals.
• The loss of spontaneous and serendipitous informal talk by the watercooler, in the
hallway or breakroom, coming in/out of meetings etc. was keenly felt during COVID19 (Bleakley et al. 2021; Miller et al. 2021; Lal et al. 2021; Methot et al. 2021).
• Such opportunistic talk enables knowledge sharing, trust, and morale building but it
may also be distracting or exclusionary for some employees, so teams should ensure
that work does not rely too heavily on it (Methot et al. 2021).
• Teams should organize social rituals, which provide both moments to socialize and a
sense of ongoing team culture (Methot et al. 2021); Bleakley et al. 2021). These may
be either traditional rituals such as eating together, or new ones such as playing
video games together. This can also include joining meetings early to engage in small
talk (Allen et al. 2014; Reed & Allen, 2021).

• Spatial environments may enable more persistent opportunities for informal talk not
just throughout the day, but also the pre- and post-meeting talk (Gonzalez Diaz
2022) (see also: “Spatial environments are conducive to ad hoc engagement”).

Spontaneous talk outside of formal engagements is
crucial to work, both in rituals such as coffee (top)
and hallway or pre/post meeting talk (bottom).

Allen, J. A., et al. (2014). Linking pre-meeting communication to meeting effectiveness. Journal of Managerial Psychology, 29(8), 1064–1081.
Bleakley, A., et al. (2021). Bridging social distance during social distancing: exploring social talk and remote collegialityin video conferencing. Human–Computer Interaction.
Microsoft Study: Gonzalez Diaz, et al. (2022). “Making Space for Social Time: Supporting Conversational Transitions Before, During, and After Video Meetings.” ACM CHIWORK’22.
Lal, B., et al. (2021). Working from Home During Covid-19: Doing and Managing Technology-enabled Social Interaction With Colleagues at a Distance. Information Systems Frontiers.
Methot, J. R., et al. (2021). Office Chitchat as a Social Ritual: The Uplifting Yet Distracting Effects of Daily Small Talk at Work. Academy of Management Journal 64(5), 1445–1471.
Microsoft Study: Miller, C., et al. (2021). “How Was Your Weekend?” Software Development Teams Working From Home During COVID-19. ACM ICSE’21, 624–636.
Reed, K. M., & Allen, J. A. (2021). Suddenly Virtual: Making Remote Meetings Work. John Wiley & Sons.

31

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Meetings improve when business objectives drive technology choices
All meetings need good voice and task sharing capabilities but building trust and resolving conflict
benefit from showing people’s video streams.
• Standaert et al. (2021) used data from the
organizers of 612 business meetings at a large
global technology company to develop a
decision matrix for how to match meeting
goals/needs to communication modes.
• The ability to hear voice and share screens – but
not video of participants – was identified by
Standaert et al. (2021) as critical to all business
meeting objectives. However, resolving conflicts
and building trust were reported to benefit from
views of gestures, facial expressions, and what
people are looking at.

Decision matrix for matching meeting goals to
communication modes

• Considerations may change when participants
have disabilities (Das et al. 2021) (see also:
“Collaboration systems need to be more
accessible”).
Standaert et al. (2021)

Microsoft Study: Das, M., et al. (2021). Towards Accessible Remote Work: Understanding Work-from-Home Practices of Neurodivergent Professionals. Proc. ACM-HCI 5 (CSCW1), Article 183.
Standaert, W., et al. (2021). How shall we meet? Understanding the importance of meeting mode capabilities for different meeting objec tives. Information & Management, 58(1), Article 103393.

32

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Hybrid meetings can work when participation is encouraged
Early post-pandemic adopters are finding that hybrid meetings have value, with the strong
requirement that participation is encouraged and moderated
•

The technological struggles of hybrid meetings are well known, such as the difficulty of
hearing/seeing remote attendees and the ability for in-person attendees to use devices for parallel
chat and other collaboration (Saatçi et al. 2019, 2020). While current technology can be carefully set
up (Frisch & Greene 2021), and the technology will improve, there are practices to ensure equitable
engagement and meeting success. (See slide 39 on new hybrid meeting technologies.)

•

Early post-pandemic adopters of hybrid meetings are findings some benefits, according to a June
2021 survey of 1000 knowledge workers (Reed & Allen 2022). While hybrid meeting satisfaction lags
video and in-person, hybrid meetings scored better than in-person, video, and telephone meetings in
having: the most participation (although it is unclear if this includes equal remote and in-person
participation), less counterproductive behaviours (such as complaining, monologues, multitasking);
less ‘surface acting’ (faking expected emotions – a practice that related to meeting fatigue); and in
requiring the least meeting recovery time (the time required to reset intellectually, emotionally, and
physically after a meeting).

•

Individual participation is even more important to meeting satisfaction and effectiveness in hybrid
meetings in comparison to in-person, video, and telephone meetings. Further, as leader-initiated
participation increases, individual participation increases. (For detailed guides, see Hybrid Work
Solutions for a Hybrid Workplace, 2022; Reed & Allen 2022, Mroz et al. 2018).
Participation is key to hybrid meeting satisfaction and
effectiveness (Reed & Allen 2022)

Frisch, B., & Greene, C. (2021, June 3). What It Takes to Run a Great Hybrid Meeting. Harvard Business Review.
Microsoft Study: Microsoft (2022). Hybrid Work Solutions for a Hybrid Workplace.
Mroz, J. E., et al. (2018). Do We Really Need Another Meeting? The Science of Workplace Meetings. Current Directions in Psychological Science, 27(6), 484–491.
Reed, K. M., & Allen, J. A. (2022). Suddenly Hybrid: Managing the Modern Meeting. John Wiley & Sons.
Microsoft Study: Saatçi, B., et al. (2019). Hybrid Meetings in the Modern Workplace: Stories of Success and Failure. In H. Nakanishi, H., et al. (Eds.), Collaboration Technologies and Social Computing (pp. 45–61). Springer.
Saatçi, B., et al. (2020). (Re)Configuring Hybrid Meetings: Moving from User-Centered Design to Meeting-Centered Design. Computer Supported Cooperative Work, 29, 769-294.

33

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The Leaf Blower Problem is an open challenge for remote meetings
When we share the same room, we implicitly understand how we are perceived. When joining a meeting
remotely, a lack of common ground may lead to misunderstandings about what others perceive.
•

The Leaf Blower Problem occurs when only one side of a conversation experiences a major
disruption (like a leaf blower or children) and that disruption is only perceptible to those on
that side of the conversation, leading to significant confusion in the conversation (Hecht et al.
2021). The Leaf Blower Problem is a new manifestation of an old problem in human-centered
AI and UX design: the grounding error. Grounding errors happen when we lack shared
understanding. Shared understanding is what makes effective conversation possible (Clark
1996).

•

A related problem is the lack of reciprocity of perception or not knowing how we are perceived
by others which is a particular problem in technology-mediated conversations, which in turn
underpins and contributes to the difficulty of turn-taking in video calls. Early research into
communicating through video (Heath & Luff 1991, 1992) showed how always having think
about how you are heard and how you are seen means that the flow of a conversation is
disrupted and interaction becomes an effortful performance.

•

This is made worse in hybrid meetings where the asymmetries in perception are amplified. In
an all-remote situation, we may have a better understanding of how others perceive us
because we are in similar situations. Not so in hybrid meetings, where knowing how you are
seen and heard in a meeting room is more difficult. This can be made even worse if the
camera through which remote people are viewing a meeting and the place in the room where
they are displayed are not lined up resulting in head turning and gaze cues being distorted
(Gaver 1993).

Clark, H. H. (1996). Using Language. Cambridge University Press.
Gaver, W. W., et al. (1993). One is not enough: Multiple views in a media space. ACM INTERACT'93 and CHI’93: 335-341.
Heath, C., & Luff, P. (1992). Media space and communicative asymmetries: Preliminary observations of video-mediated interaction. Human–Computer Interaction, 7(3), 315-346.
Heath, C., & Luff, P. (1991). Disembodied conduct: Communication through video in a multi-media office environment. CHI’ 91: 99-103.
Microsoft Study: Hecht et al. (2021) The “Leaf Blower Problem” and the importance of common ground. Microsoft Research.

34

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Video meeting fatigue is a multidimensional problem
Video meeting fatigue stems from a combination of unnaturally low or high cognitive load imposed by
the user interface combined with intense/inappropriate use.
•

Reidl (2021) developed a synthetic definition from a review of 45 articles: “[Video meeting fatigue] is defined
as somatic and cognitive exhaustion that is caused by the intensive and/or inappropriate use of
videoconferencing tools, frequently accompanied by related symptoms such as tiredness, worry, anxiety,
burnout, discomfort, and stress, as well as other bodily symptoms such as headaches.”

•

Video meeting tools introduce two poles of unnaturalness compared to being in person: lack of information
(e.g., lack of body language, eye contact) and too much information (e.g., self mirror, artificial grouping of
faces) (Bailenson 2021). However, unnaturalness alone is not enough, the key to fatigue is “intensive and/or
inappropriate use“ – that is, too many meetings, held too close together, for goals that are not always suited
to its use (Reidl 2021; Döring 2022).

•

In a study of approximately 10k participants during COVID-19, Fauville et al. (2021) found that daily video
meeting usage predicts amount of fatigue and that women reported greater fatigue than men. They found
that mirror anxiety mediated the difference in fatigue across gender, with race, age, and personality possibly
also relating to fatigue.

•

On personality, Kuhn (2022) reports two studies in which people with the personality trait of higher public self consciousness had a more negative attitude toward their virtual meetings the more often their own face was
visible, whereas for people with low public self-consciousness had more favourable attitudes toward using
video in meetings.

•

For people who are deaf or hard of hearing, however, the artificial frontal view of all participants in a video
meeting may make meetings less fatiguing, because it aids identification and lip reading (Tang 2021).

Video conference fatigue has multidimensional inputs (Raake et al. 2022)

Bailenson, J. N., (2021). Nonverbal Overload: A Theoretical Argument for the Causes of Zoom Fatigue. Technology, Mind, and Behavior. 2(1), Article tmb0000030 .
Döring, N. (2022). Videoconference Fatigue: A Conceptual Analysis. International Journal of Environmental Research and Public Health, 19(4), Article 2061.
Fauville, G., et al. (2021). Nonverbal Mechanisms Predict Zoom Fatigue and Explain Why Women Experience Higher Levels than Men. Social Science Research Network, 3820035.
Kuhn, K. M. (2022). The constant mirror: Self-view and attitudes to virtual meetings. Computers in Human Behavior, 128, Article 107110.
Raake, A., et al. (2022). Technological Factors Influencing Videoconferencing and Zoom Fatigue, arXiv preprint, arXiv.2202.01740.
Riedl, R. (2021). On the stress potential of videoconferencing: definition and root causes of Zoom fatigue. Electronic Markets, December 6.
Microsoft Study: Tang, J. (2021). Understanding the Telework Experience of People with Disabilities. Proc. ACM-HCI 5(CSCW1), Article 30.

35

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Video often benefits remote meetings, but should be used intentionally
Research suggests that video is a valuable tool for remote (and hybrid) meetings, but in specific
circumstances there might be reasons to stick with audio.
•

During and after the primary COVID-19 pandemic, many groups had to negotiate when video should be on or off in
remote meetings (Castelli et al. 2021).

•

Cutler et al. (2021), using a very large data set from a global technology company, found that video usage is often
correlated with more inclusive meetings.
• This is particularly the case for participants who are deaf or hard of hearing (Tang 2021)

•

There are reasons teams may sometimes want to be intentional about the use of video in meetings.
• Video may be less inclusive for people who are low-vision or neurodivergent (Tang 2021).
• Pressure to use video can make interactions feel forced, or lead to anxiety and privacy helplessness, all of which
may lead to worse subjective productivity (Okabe-Miyamoto et al. 2021) and video conference fatigue. (See
previous slide on video meeting fatigue.)
• People frequently turn off video when they are only monitoring meetings and want to multitask (Cao et al. 2021).

•

Video is useful in hybrid meetings, but can be challenging when remote participants are sized unequally compared to
those in the room. Screen and microphone placement can also cause confusion about who is speaking or being
referenced (Saatçi et al. 2020).
• These issues are starting to be addressed by new practices – such as collocated participants turning their laptop
video on – and new technologies – like Front Row (Microsoft 2021), MSR Perspectives (Microsoft Research 2021),
and MSR Virtual Cube (Zhang et al. 2021).

Correlations from in-client end-of-meeting survey
(Cutler et al. 2021)

Microsoft Study: Cutler, R., et al. (2021). Meeting Effectiveness and Inclusiveness in Remote Collaboration. Proc. ACM-HCI, 5(CSCW1), Article 173.
Okabe-Miyamoto, K., et al. (2021). Did zoom bomb? Negative video conferencing meetings during COVID-19 undermined worker subjective productivity. Human Behavior and Emerging Technologies, 3(5), 1067–1083.
Castelli, F. R., & Sarvary, M. A. (2021). Why students do not turn on their video cameras during online classes and an equitable and inclusive plan to encourage them to do so. Ecology and Evolution, 11(8), 3565–3576.
Microsoft (2022). The Future of Hybrid Work – See What’s next for the Future of Hybrid Work.
Microsoft Study: Panel: Perspectives on the new future of hybrid meetings. (2021). Microsoft Research Summit 2021.
Microsoft Study: Tang, J. (2021). Understanding the Telework Experience of People with Disabilities. Proc. ACM-HCI, 5(CSCW1), Article 30.
Microsoft Study: Cao, H., et al. (2021). Large Scale Analysis of Multitasking Behavior During Remote Meetings. ACM CHI’21, Article 448.
Saatçi, B., et al. (2020). (Re)Configuring Hybrid Meetings: Moving from User-Centered Design to Meeting-Centered Design. Computer Supported Cooperative Work, 29, 769-294.
Microsoft Study: Zhang, Y., et al. (2022). VirtualCube: An Immersive 3D Video Communication System. IEEE Transactions on Visualization and Computer Graphics. 28(5), 2146–2156.

36

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Meeting chat has promise and peril
Parallel chat allows groups to communicate flexibly but may be distracting.
• Sarkar et al. (2021) report that parallel chat has become essential in many video
meetings. Parallel chat in meetings is seen as a net positive. It can help organize
the meeting, work around problems, and manage turn taking. During the
pandemic, the usage of parallel chat increased greatly by women aged 25-34,
this, along with qualitive reports of parallel chat as an inclusive space, may
indicate that it is especially important in overcoming some problems of turntaking that are inherent to video meetings.
• However, many people report being distracted by parallel chat, and there are
different expectations around how on-topic or formal chat needs to be.
Distraction may be a particular challenge for people who are neurodivergent.
• Chat may also be inaccessible to people with reading difficulties, those
struggling with written sentiment, or blind and low vision people.
• Future AI may help people manage different information flows of AV and parallel
chat in meetings. For example, annotating distinct categories of chat messages
could reveal patterns of activity and enable effective scanning.

Parallel chat in meetings is seen as a net positive, albeit with
some issues around distraction (top table). Its usage increased
greatly by women aged 25-34, which may be indicative of
providing a space for inclusion (Sarkar et al. 2021)

37
Microsoft Study: Sarkar, A., et al. (2021). The promise and peril of parallel chat in video meetings for work. ACM CHI EA’21, Article 260.

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Collaboration systems need to be more accessible
From meetings to document collaboration, there are more opportunities to broaden inclusion.
•

Workspaces have improved the base level of accessibility over the last few years. The pandemic has
accelerated some improvements. However, tools could go further to support personalized needs
and more diverse methods of representation.

•

Both Leprorini et al. (2021) and Tang (2021) report challenges and opportunities with video
collaboration platforms for blind, deaf blind and deaf. These include screen reader navigation of
platforms, video-based screen sharing, and visibility of interpreters.

•

Tang (2021) reports that deaf and hard of hearing (DHH) people are unable to lip-read when others
do not turn their camera on, and there are ongoing issues ensuring that deaf people and sign
language interpreters are seen and identified correctly. Closed captioning can help DHH people
(when available); its accuracy rates can be high enough for university education (Millet 2021),
but sometimes manual captioning is still desired. (See slide 46 on avatar acceptance.)

•

The social-emotional-sensory needs of neurodiverse people require attention (Zolyomi & Snyder
2021). Das et al. (2021) report that for neurodiverse people, seeing people’s backgrounds may be a
distraction, and being seen by others or seeing themselves in self view may make them
uncomfortable with the way they demonstrate attention or their need to focus using support
objects.

•

CollabAlly uses spatial audio, earcons, and voice fonts to help blind and
low vision users collaborate on documents (Lee, et al., 2022).

Beyond meetings, document collaboration (Lee et al. 2021) and collaboration that requires an
ecosystem of tools, such as programming (Pandey et al. 2021), also need improvement for
individuals who use assistive technology.

Microsoft Study: Das, M., et al. (2021). Towards Accessible Remote Work: Understanding Work-from-Home Practices of Neurodivergent Professionals. Proc. ACM-HCI 5(CSCW1), Article 183.
Lee, C. Y. P., et al. (2021). CollabAlly: Accessible Collaboration Awareness in Document Editing. ACM CHI’22, Article 596.
Leporini, B., et al. (2021). Distance meetings during the covid-19 pandemic: are video conferencing tools accessible for blind people? ACM W4A ’21, Article 7 .
Millett, P. (2021). Accuracy of Speech-to-Text Captioning for Students Who are Deaf or Hard of Hearing. Journal of Educational, Pediatric & (Re) Habilitative Audiology, 25, Article 21.
Pandey, M. (2021). Understanding Accessibility and Collaboration in Programming for People with Visual Impairments. Proc. ACM-HCI 5(CSCW1), Article 129.
Microsoft Study: Tang, J. (2021). Understanding the Telework Experience of People with Disabilities. Proc. ACM-HCI 5(CSCW1), Article 30.
Wolfe, R., et al. (2021). State of the Art and Future Challenges of the Portrayal of Facial Nonmanual Signals by Signing Avat ar. In Universal Access in Human-Computer Interaction. Design Methods and User Experience, Springer,
Zolyomi, A., & Snyder, J. (2021). Social-Emotional-Sensory Design Map for Affective Computing Informed by Neurodivergent Experiences. Proc. ACM-HCI 5(CSCW1), Article 77.

38

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

New hybrid meeting technologies are showing significant promise
Hybrid meetings are difficult to run effectively and combining the best of remote and in-person meetings is a
major open challenge. Fortunately, new prototypes show significant short- and long-term potential.
•

The primary challenge of hybrid meetings is that endpoints have asymmetrical perspectives.
Remote and local people see and hear one another differently, are grouped in artificial ways,
and have different access to shared resources. This tends to advantage groups in rooms and
disadvantage individual remote users (Saatçi, et al. 2020).

•

Both the MSR Perspectives Prototype (Panel 2021) and the VirtualCube prototype (2022) strive
to provide equitable and immersive views of meeting participants without the need for headmounted displays.

•

The MSR Perspectives Prototype (Panel 2021), is designed for small hybrid meetings. All
participants, including people who are co-located, join the meeting as individual video streams
with background removed. Each endpoint has a unique perspective, and consistent ‘around the
table’ spatial positioning is preserved. Remote users experience the meeting as sitting at a
shared virtual table, while people in the room experience it as an extension of the physical
room. Spatial audio streams are provided for each attendee. This approach takes advantage of
natural spatial cues for taking turns, enabling a stronger sense of co-presence, and more
dynamic engagement, resulting in the feeling of sharing a common space in an equitable way.

•

VirtualCube (2022) takes the view of each person one step further by using multiple Azure
Kinects at each endpoint to create photo-realistic life size 3D views of each person, with correct
eye-contact and natural user interactions between remote participants including side
conversions in a group meeting and seamlessly sharing of work items remotely.

•

As we develop new ways to enable hybrid meetings, we should make sure to include people
who are participating using any approach: in-person in the room, over audio using a phone,
remotely using a computer desktop, or virtually using VR or AR headsets.

The MSR Perspectives Prototype local room view (left)
and a remote user’s view (right) (Panel 2021)

VirtualCube from Zhang et al. (2022)

Saatçi, B., et al. (2020). (Re)Configuring Hybrid Meetings: Moving from User-Centered Design to Meeting-Centered Design. Computer Supported Cooperative Work, 29, 769-294.
Microsoft Study: Panel: Perspectives on the new future of hybrid meetings. (2021). Microsoft Research Summit 2021.
Microsoft Study: Zhang, Y., et al. (2022). VirtualCube: An Immersive 3D Video Communication System. IEEE Transactions on Visualization and Computer Graphics. 28(5), 2146–2156.

39

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Telepresence robots provide autonomy at a distance
While they may be expensive, telepresence robots have had positive results for team building and
remote user presence in retail, education, healthcare and more.
•

Mobile Robotic telePresence (MRP) systems provide a combination of videoconferencing and locomotion.
A remote pilot may log in to and move an MRP autonomously around a local activity space, engaging in
both structured and informal talk with others in that environment. They are already used, albeit sometimes
experimentally, in a range of contexts including conferences (Neustaedter et al. 2018), retail (Singh 2021),
education (Lei et al. 2022), healthcare (Isabet et al. 2021), and even domestic contexts (Boudouraki, 2022).

•

The autonomy of connecting to an organizational space without the need for a call to a specific individual
or meeting, and being able to move around that space, has significant positive benefits for hybrid
organizations. They have been found to enable virtual team building (Keller et al. 2021), although like other
hybrid videoconferencing applications the ability of remote pilots to hear and be heard among a group of
real people may be challenging.

•

One specific challenge of MRP usage is that remote pilots do not see or hear in the local environment as
well as local people, and may have trouble navigating around physical obstacles. In such cases, local people
may treat the MRP pilot in a manner that affects their influence, role, and power (Boudouraki et al. 2021).

•

To increase the sense of belonging for both ends, telepresence robots may be enhanced with overlayed
life-size avatars viewed through augmented reality HMDs, and immersive VR piloting (Jones et al. 2021).
Telepresence robots at work (top) and the VROOM system
with overlayed avatars (bottom) (Jones, et al. 2022)

Boudouraki, A., (2022). Mediated Visits: Longitudinal Domestic Dwelling with Mobile Robotic Telepresence. ACM CHI ‘22, Article 251.
Microsoft Study: Boudouraki, A., et al. (2021). “I can’t get round”: Recruiting Assistance in Mobile Robotic Telepresence. Proc. ACM-HCI 4(CSCW3), Article 248.
Isabet, B., et al. (2021). Social Telepresence Robots: A Narrative Review of Experiments Involving Older Adults before and during the COVID-19 Pandemic. International Journal of Environmental Research and Public Health,
18(7), 3597.
Microsoft Study: Jones, B., et al. (2021). Belonging There: VROOM-ing into the Uncanny Valley of XR Telepresence. Proc. ACM-HCI 5(CSCW1), Article 59.
Keller, L., et al. (2021). Driving Success: Virtual Team Building Through Telepresence Robots. In P. Zaphiris & A. Ioannou (Eds.), Learning and Collaboration Technologies: Games and Virtual Environments for Learning (pp.
278–291). Springer.
Lei, M., et al. (2022). The Acceptance of Telepresence Robots in Higher Education. International Journal of Social Robotics, 2022 Jan 27:1-18 .
Neustaedter, C., et al. (2018). From Being There to Watching: Shared and Dedicated Telepresence Robot Usage at Academic Conferences. ACM TOCHI, 25(6), Article 33.
Singh, S., et al. (2021). Combating COVID-19: Study of robotic solutions for COVID-19. AIP Conference Proceedings, 2341(1), 020042.

40

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Devices need to be better together rather than adding friction
Device ecosystems need to support natural work transitions, home/work connections, and security.
• Information workers move between activities, places,
and devices, interacting with different people and
kinds of information – but using devices together
often comes with high friction. (Brudy et al. 2018;
Nguyen 2021).
• Remote and hybrid workers face difficulties in using
devices (individually or in combinations) from home
or in meeting rooms where they must bring their own
device. Difficulties include friction using devices
together, difficulty connecting to work device,
different devices at home and work, tensions over
device management, and home personal device and
IoT security threats (Ford et al. 2022; Edelmann et al.
2021; Barlette et al. 2020)
Overview of the cross-device design space (Brudy et al. 2018)

Barlette, Y., et al. (2021). Bring Your Own Device (BYOD) as reversed IT adoption: Insights into managers’ coping strategies. International Journal of Information Management 56, Article 102212.
Brudy, F., et al. (2019). Cross-Device Taxonomy: Survey, Opportunities and Challenges of Interactions Spanning Across Multiple Devices. CHI’19, Article 562.
Edelmann, N., et al. (2021). Remote Work in Public Sector Organisations: Employees’ Experiences in a Pandemic Context. DG.O2021, 408–415.
Microsoft Study: Ford, D., et al. (2022) A Tale of Two Cities: Software Developers Working from Home During the COVID-19 Pandemic. ACM TOSEM, 31(2), Article 27.
Nguyen, N. T., et al. (2021). Intelligent Shifting Cues: Increasing the Awareness of Multi-Device Interaction Opportunities. ACM UMAP ’21, 213–223 .

41

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The metaverse is a phase shift in the era of immersive technologies
The metaverse was first coined in 1992 in Neil Stephenson’s novel Snowcrash. Interest in the metaverse
grew during remote work. However, definitions vary, presenting challenges and opportunities.
•

A common definition for the metaverse is an online world that fulfills real-world desires and activities. It offers the
possibility to step outside of the normal bounds of reality and realize goals in a new way (Slater & Sanchez -Vives 2016).
It is also about data persistency and represents a shift from devices to content (Gonzales-Franco 2021).

•

The metaverse requires a rethinking of how applications and a society of devices work in new digital spaces. A better
understanding of the role it plays in respect to our devices is needed. Results from a Microsoft study in progress show
people estimate they will use the metaverse for 5-10% of their meetings while keeping PC the preferred method to work.

•

Another important component of the metaverse is the social component. It is not just about content, but about social
content. The metaverse is a web of social, networked immersive environments in persistent multiuser platforms
(Mystakidis 2022). The social component creates opportunities for the metaverse as a transaction platform, since
wherever there are people there are transactions. While methods like Blockchain (Jeon et al. 2021) can ensure trust in
transactions, transactions do not need to made be in cryptocurrencies or NFTs. Thus the success of the metaverse is not
tied to cryptocurrencies or vice versa (Fenwick & Jurcys 2022; Yang et al. 2022).

•

The metaverse is based on the convergence of technologies that enable multisensory interactions ( Mystakidis 2022;
Gonzales-Franco & Lanier 2017). It can be considered an aggregator of technologies like other interaction breakthroughs
with content, e.g., smartphones (Huynh-The et al. 2022). Metaverse skepticism often stems from this facet since a single
platform does not exist and agreement from many players is required for progress.

•

Despite skepticism, the metaverse represents a new form of interaction with digital content that has potential to be very
disruptive. There are many large industry players in the space and devices have improved over the years. Multiple
adoption channels currently exist, including gaming and entertainment, front line workers, and information workers.
Widespread adoption comes with security and privacy issues that must be carefully addressed (Buck & McDonnell 2022).

Buck, L., & McDonnell, R. (2022). Security and Privacy in the Metaverse: The Threat of the Digital Human. ACM CHI EA ’22.
Fenwick, M., & Jurcys, P. (2022). The Contested Meaning of Web3 and Why it Matters for (IP) Lawyers. Social Science Research Network, 4017790,
Gonzalez-Franco, M. (2021). Keynote Speaker: Metaverse from Fiction to Reality and the Research Behind It, ISMAR’21: 17-17.
Microsoft Study: Gonzalez-Franco, M., & Lanier, J. (2017). Model of illusions and virtual reality. Frontiers in Psychology, 8, 1125.
Huynh-The, T., et al. (2022). Artificial Intelligence for the Metaverse: A Survey. arXiv preprint, arXiv:2202.10336.
Jeon, H., et al. (2021). Blockchain and AI Meet in the Metaverse. IntechOpen.
Mystakidis, S. (2022). Metaverse. Encyclopedia 2(1), 486–497.
Slater, M., & Sanchez-Vives, M. V. (2016) "Enhancing our lives with immersive virtual reality." Frontiers in Robotics and AI, 3 (2016), Article 74.
Yang, Q., et al. (2022). Fusing Blockchain and AI with Metaverse: A Survey. arXiv preprint, arXiv:2201.03201.

Microsoft Mesh

42

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Social presence in AR/VR does not equate to realistic people or environments
Presence depends on the application context and the ability to share meaning.
•

Social presence is the salience of people who are interacting and their interpersonal relationship(s) (Short et al. 1976).

•

“Imitating reality to some degree when meeting remotely is beneficial, but it is not always necessary and perhaps even harmful,
since they give way to both negative and positive aspects of physical interactions” ( Zibrek et al. 2021).

•

Whether social presence equates/requires total sensory realism (e.g., photorealistic avatars) is a central problem in develop ing
AR/VR collaboration systems, especially because improving sensory realism incurs a high cost in hardware. Jung & Lindeman’s
(2021) overview shows better or more visual, auditory, or haptic cues may lead to increased realism, but not necessarily
increased presence. In their model for quality of VR experience, realism intersects with, rather than equates to, presence.

•

Wienrich et al. (2021) argue that spatial presence, not just presence in AR, requires specific attention in three areas:
• Because AR blends rather than replaces the real world, how should decisions be made about real or digital frame of
reference, e.g., when should the virtual environment occlude the physical environment?
• Given that the user moves in a real physical world, what metaphors of transportation connect the user to other
people/objects – is it instant or does it take time?
• Given the obvious incongruence between the real and virtual world, perhaps this gives license for digital people and
objects to not be realistic?

•

The key design feature for enabling the sense of touch in AR/VR is shifting emphasis from focusing on realistic touches (e.g.,
the touch of a finger) to instead developing tools that allow people to establish common understanding about the meaning of
haptic feedback that may not be realistic (Price et al. 2022). Particularly since study participants frequently interpret physical
feedback as aligning with visual cues, even when it does not (Kim et al 2022).

•

McVeigh-Shultz & Isbister (2021) argue for evolving AR and VR team collaboration beyond simulation to enabling social
superpowers such as the tracking of signals to support emotional communication, social affiliation, and shared navigation, and
new geometries of attention for large group interactions.

Jung & Lindeman (2021) propose a new
model for quality of VR experience in
which realism is a subset of coherence, and
intersects with than equates to presence

Jung, S., & Lindeman, R. W. (2021). Perspective: Does Realism Improve Presence in VR? Suggesting a Model and Metric for VR Experience Evaluation. Frontiers in Virtual Reality, frvir.2021.693327.
Kim, M. J. et al. (2022). SpinOcchio: Understanding Haptic-Visual Congruency of Skin-Slip in VR with a Dynamic Grip Controller. ACM CHI’22, Article 433.
McVeigh-Schultz, J., & Isbister, K. (2021). A “beyond being there” for VR meetings: Envisioning the future of remote work. Human–Computer Interaction, 1994860.
Price, S., et al. (2022). The Making of Meaning through Dyadic Haptic Affective Touch. ACM TOCHI, 29(3), Article 21.
Short, J., et al. (1976). The Social Psychology of Telecommunications. John Wiley, New York, NY.
Wienrich, C., et al. (2021). Spatial Presence in Mixed Realities–Considerations About the Concept, Measures, Design, and Experiments. Frontiers in Virtual Reality, 25, Article frvir.2021.694315.
Zibrek, K., et al. (2021). Editorial: Meeting Remotely—The Challenges of Optimal Avatar Interaction in VR. Frontiers in Virtual Reality, 4, Article frvir.2021.773258.

43

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

AR/VR team collaboration requires more than just avatars in a space
Development of AR/VR spaces requires a blending of space, place, and embodiment in coordinating
work, and accounting for the needs of a wide variety of users.
•

Jetter et al. (2021) propose the concept of Transitional Interfaces (TIs) enabling seamless
integration of systems along the Reality to Virtual Reality continuum, depending on users’ tasks
and needs.

•

Radu et al. (2021) developed a set of 18 core needs for collocated AR. Active needs include
awareness of others’ attention and activities, and coordination of attention and instructions.
However, privacy adds a key complexity, because the need for shared awareness is in tension
with preventing the leakage of private information.

•

Miller & Bailenson (2021) note that a current specific limitation for AR is that the digital field of
view is a subset of the full human field of view. Virtual characters outside the digital field of
view receive lower social presence scores, but task performance is not lower. Application
designers may expect some users to look around to bring ‘missing’ things back into view, but
a subset of people may never look back or around when focused on a task.

•

The Transitional Interface continuum (Jetter et al. 2021)

VR/AR collaboration research has well-documented accessibility problems. As interest
increases, accessibility must be a priority design issue from the outset (Mott et al. 2020).

Jetter, H. C., et al. (2021). Transitional Interfaces in Mixed and Cross-Reality: A new frontier? ISS’21: 46–49.
Miller, M. R., & Bailenson, J. N. (2021). Social Presence Outside the Augmented Reality Field of View. Frontiers in Virtual Reality, 7, Article frvir.2021.656473
Microsoft Study: Mott, M. et al. (2020). “I just went into it assuming that I wouldn't be able to have the full experience”: Understanding the Accessibility of Virtual Reality for People with Limited Mobility. ACM ASSETS’20,
Article 43.
Radu, I., et al. (2021). A Survey of Needs and Features for Augmented Reality Collaborations in Collocated Spaces. ACM-HCI, 5(CSCW1), Article 160.

44

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Acceptance for avatars in professional settings is increasing – with caveats
We have yet to understand the appropriateness and ethical implications of different kinds of avatars across
diverse contexts and for users with disabilities.
•
•

Nordin Forsberg & Kirchner (2021) report on largely positive experiences with avatars helping overcome
professional networking shyness. However, they also report difficulty judging likelihood to talk based on age or
demeanor cues.
Increased avatar realism does not also equate to a simple linear increase in value. In AR meetings, participants rate
the communicative functionality of realistic avatars higher than cartoon avatars, but participants accommodate to
cartoon avatars over time (Dobre et al. 2022). Avatar acceptance for accessibility needs may be dependent on more
than avatar realism. For deaf and hard of hearing (DHH) users, those with earlier age of sign language acquisition
are more sensitive to movement quality problems than those with later sign language acquisition (Quandt, et al.
2021).

•

Avatars may be a replacement for real-time video in traditional video meetings (Higgins & McDonnell, 2021; Panda,
et al., 2022). Avatar facial expressions may be driven by live facial capture (Wen et al, 2021), neural rendering from
still images (Rings & Steincke, 2022), or derived from speech (audio visemes) (Chai, 2021). Neural rendered and
audio viseme avatars may reduce the need for costly facial capture, and enable a range of positive outcomes, such
as increased privacy, overcome situational impairment (e.g., mobile, driving, no camera), personal needs or
accessibility preferences, fixing eye gaze, or making current speakers more prominent by rendering them with a 3D
effect (Rings & Steincke, 2022).

•

As positive as the above scenarios are, the replacement of real-time video brings with it significant ethical dilemmas
around authenticity. Unfortunately, there is limited research on the ethical dimensions of avatar use in team
collaboration, especially with respect the issues around the deceptive replacement of real video. Early research
points to risks ranging from inappropriate influence, through cultural appropriation, to deceptive impersonation
(Hancock & Bailenson, 2021; Mullen, 2022). (See slide 72 on security threats in video meetings.)

Avatars networking at a professional event
(Nordin Forsberg & Kirchner, 2022)

Cartoon vs realistic avatars (Dobre et al. 2022)

Chai, Y., et al. (2021). Speech-driven facial animation with spectral gathering and temporal attention. Frontiers in Computer Science, 16, Article 163703.
Microsoft Study: Dobre, G. C., et al. (2022). Nice is Different than Good: Longitudinal Communicative Effects of Realistic and Cartoon Avatars in Real Mixed Reality Work Meetings, ACM CHI EA’22, Article 437.
Hancock, J. T., & Bailenson, J. N. (2021). The Social Impact of Deepfakes. Cyberpsychology, Behavior, and Social Networking, 24(3), 149–152.
Higgins, D., & McDonnell, R. (2021). A Preliminary Investigation of Avatar Use in Video-Conferencing. IEEE Computer Society, 540–541.
Mullen, M. (2022). A New Reality: Deepfake Technology and the World Around Us. Mitchell Hamline Law Review, 48, 1, Article 5.
Nordin Forsberg, B., & Kirchner, K. (2021). The Perception of Avatars in Virtual Reality During Professional Meetings. In HCII‘21 – Posters: 290–294.
Microsoft Study: Panda, P., et al. (2022 frth). All Together: Effect of Avatars in Mixed-Modality Conferencing Environment. ACM CHIWORK’22.
Quandt, L. C., et al. (2022). Attitudes Toward Signing Avatars Vary Depending on Hearing Status, Age of Signed Language Acquisition , and Avatar Type. Frontiers in Psychology, Article fpsyg.2022.730917
Rings, S., & Steinicke, F. (2022). Local Free-View Neural 3D Head Synthesis for Virtual Group Meetings. 2022 IEEE VRW: 333–337.
Wen, L., et al. (2022). A Survey of Facial Capture for Virtual Reality. IEEE Access, 10: 6042–6052.

45

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

AR/VR design fiction enables experimentation with work practices
AR/VR environments enable rapid but rich experiments with radical changes to work environments.
• Design fictions are explorations of speculative scenarios that are expressed
in design artifacts such as images and objects.

• Immersive Speculative Enactments (ISEs) (Simeone et al. 2022) use AR/VR
applications for design fictions. They enable users to experiment with
simulations of technologies in context that are too expensive, difficult, or
infeasible to examine in the real world. The use of VR/AR overcomes the
limitation of static and non-functional artifacts as well as the lack of
context for their use. ISEs can immerse users in open-ended environments,
within which they are free to interact with a tangible rendition of a
possible future. For example, they imagine near term scenarios from crossreality lectures to future scenarios such as a Mars mission.

Immersive Speculative Environments enable exploration
of issues in future-oriented scenarios

• McVeigh-Shultz et al. (2018) present a case study of Steelcase reimagining
their work practices. Steelcase designers used a range of novel tools in VR
to both change their own ideation practices (e.g., a camera eyeball that
helps coordinate joint attention) and to try furniture concepts such as
chairs with AR controls for the workplace.

Steelcase’s hybrid virtual/physical chair concept could be
presented in an AR environment
McVeigh-Schultz, J., et al. (2018). Immersive Design Fiction: Using VR to Prototype Speculative Interfaces and Interaction Rituals within a Virtual Storyworld. ACM DIS’18: 817–829.
Simeone, A. L., et al. (2022). Immersive Speculative Enactments: Bringing Future Scenarios and Technology to Life Using Virtu al Reality. ACM CHI ’22, Article 17.

46

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Blended realities enable new forms of real-time collaborative creativity
Avatars in brainstorming, flexible video windows, and AI-augmented tools may evolve remote and
hybrid creativity to be better than in person.
•

In comparison to brainstorming in video meetings, immersive brainstorming may enable greater use of
clustering around shared resources in dynamic ways, such as how people move around physical
whiteboards (Tuomi 2021). AI Agents can also be a more dynamic resource for brainstorming. “Avatarmediated brainstorming” uses AI-agent avatars in place of static persona documents, to improve
designer empathy in feature brainstorms (Bonnardel & Pichot 2020).

•

One problem with remote brainstorming in traditional 2D video meetings is the limitations that
traditional video grids place on referencing people and content in a dynamic manner. MirrorBlender
(Grønbæk et al. 2021) takes advantage of the malleability of video streams by treating all streams as
translucent ‘mirrors’ that can be repositioned in a What-You-See-Is-What-I-See videoconferencing
system.

•

Dynamic virtual avatars (Bonnardel & Pichot 2020) are a
tool for increasing designer empathy

Chung et al’s (2021) review of AI-augmented creativity support tools (e.g., aids for creating images)
notes the rise of tools that support production roles (e.g., novices or experts) or execution assistance
(e.g., providing layout, colour, or form assistance in the form of ideas or actual changes to the humanproduced material). Such aids can improve the sketching of novices or broaden the concepts from
experts in brainstorming. However, there is still limited research on how AI-aided creativity interacts with
who uses the tool, the biases of such tools, and how those who use (or even come to depend) on such
tools will deal with biases in tools.
MirrorBlender (Grønbæk et al. 2021) uses video
translusence to enable naturalistic cues

Bonnardel, N., & Pichot, N. (2020). Enhancing collaborative creativity with virtual dynamic personas. Applied Ergonomics, 82: Article 102949.
Chung, J. J. Y., et al. (2021). The Intersection of Users, Roles, Interactions, and Technologies in Creativity Support Tools, ACM DIS ’21: 1817–1833.
Grønbæk, J. E., et al. (2021). MirrorBlender: Supporting Hybrid Meetings with a Malleable Video-Conferencing System’ ACM CHI’21, Article 451.
Toumi, K. (2021). Technologies for Supporting Creativity in Design: A View of Physical and Virtual Environments with Regard to Cognitive and Social Processes. Creativity. Theories – Research – Applications, 8(1): 189–212.

47

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Simulation sickness is a significant speedbump for AR/VR collaboration
Content, visual stimulation, locomotion, and exposure times have effects on reported sickness in AR/VR
systems, but results are biased by studies conducted on very limited populations.
• Saredakis et al. (2020) reviews 55 studies of adverse symptoms
from head-mounted displays (HMD) for virtual reality (VR)
applications. Content significantly influences VR sickness
symptoms. VR sickness profiles were also influenced by visual
stimulation, locomotion and exposure times. (See also Lawson &
Stanney 2021.)
• There are many anecdotal reports of HMD sickness affecting
women more than men, but studies have conflicting or weak
results. However, more research is needed because many studies
do not directly address sickness, do not collect gender, or rely
mainly on men as subjects (Saredakis et al. 2020; MacArthur et
al. 2021; Grassini & Laumann 2020; Criado Perez, 2019).
VR sickness levels and content (Saredakis et al. 2020)

Criado Perez, C. (2019). Invisible Women: Exposing Data Bias in a World Designed for Men. Random House.
Grassini, S., & Laumann, K. (2020). Are Modern Head-Mounted Displays Sexist? A Systematic Review on Gender Differences in HMD-Mediated Virtual Reality. Frontiers in Psychology, Article fpsyg.2020.01604
Lawson, B. D, & Stanney, K. M. (2021). Editorial: Cybersickness in Virtual Reality and Augmented Reality. Frontiers in Virtual Reality, frvir.2021.759682.
MacArthur, C., et al. (2021). You’re Making Me Sick: A Systematic Review of How Virtual Reality Research Considers Gender & C ybersickness. ACM CHI’21, Article 401.
Saredakis, D., et al. (2020). Factors Associated With Virtual Reality Sickness in Head-Mounted Displays: A Systematic Review and Meta-Analysis. Frontiers in Human Neuroscience, fnhum.2020.00096

48

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The power of AI in the future of work hinges on getting the role of AI right
Human–AI collaboration is likely to increasingly augment human abilities, but human-centric AI points
to empowering rather than emulating humans.
• Managers need to be vigilant about the dualities/tensions that
introducing highly capable AI might create in human–machine work
environments (Seeber et al. 2020). For example, an AI might drive
higher quality decision making on some dimensions, but this must not
come at the cost of reducing the capability of team members to
criticize decisions on dimensions that the AI does not consider.
• Getting the allocation of roles right between humans and machine is
therefore critical in designing AI systems for the future of work.
Shneiderman (2020) argues that human-centric AI should view AI
systems as intelligent tools rather than human-like teammates. Users
want to be in control of technologies that support self-efficacy,
responsibility and creativity.
• Microsoft’s Guidelines for Human-AI Interaction (Amershi et al. 2019)
give practical guidance for getting the relationships right.
Four sets of issues raised by adopting either emulation or
application goals in developing AI (Shneiderman 2020)

Microsoft Study: Amershi, S., et al. (2019). Guidelines for Human-AI Interaction. Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, Article 3300233.
Seeber, I., et al. (2020). Machines as teammates: A research agenda on AI in team collaboration. Information & Management, 57(2), 103174.
Shneiderman, B. (2020). Human-Centered Artificial Intelligence: Three Fresh Ideas. AIS Transactions on Human-Computer Interaction, 12(3), 109-124.

49

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

AI may help with inclusive and effective meeting behaviors
From turn-taking patterns, to the vocal patterns of effective or productive meetings, AI can help uncover
patterns that are hard for people to perceive.
•

AI can be used to capture inclusive behaviours that are verbal and non-verbal (e.g., turntaking, sentiment, consensus, questions). A study of longitudinal use in a large global
technology company showed that post-meeting dashboards with explanations of
inclusivity measures and suggestions may enable both personal reflection and
organizational meeting training (Samrose et al. 2021).

•

Neibuhr et al. (2021) report that meetings that are perceived to be more effective are
characterized by affectively calmer, simpler, and shorter prosody (patterns of voice stress
and intonation). However, more objectively productive meetings (generating a high
output of feasible or good ideas) are characterized by lively, interactive, stimulating
prosody. Such meeting productivity is correlated with the overall sound of the individual
meetings, with pitch features being the most diverse and powerful predictors. Prosodic
analysis of meetings could be implemented in AI dashboards such as those above,
enabling methods for tracking meeting effectiveness that preserve privacy by not
requiring transcript analysis.

•

Margariti et al. (2022) note that when talk behaviours are tracked for inclusion reporting,
it is important to look beyond simplistic assumptions. For example, overlapping talk is
not necessarily negative – it may be either competitive or cooperative, and either may be
indicative of positive or negative inclusion. They also argue for privacy preserving
methods for finding and tracking such talk.

Post-meeting dashboards of collected inclusive behaviours can Improve
meeting culture and training (Samrose et al. 2021)

Microsoft Study: Margariti, E., et al. (2022). Automated mapping of competitive and collaborative overlapping talk in video m eetings. ACM CHI EA’22, Article 311.
Niebuhr, O., et al. (2021). On the Sound of Successful Meetings: How Speech Prosody Predicts Meeting Performance. ICIMI’21, 240-248.
Microsoft Study: Samrose, S., et al. (2021). MeetingCoach: An Intelligent Dashboard for Supporting Effective & Inclusive Meetings. ACM CHI’21, Article 252.

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

AI summarization may reduce meeting FOMO and improve asynchronous work
Summarization technology allows us to make better use of recorded meetings and take better notes
making asynchronous participation possible and synchronous participation better.
• Past research has identified lightweight interaction patterns that
enable users to work in collaboration with AI – noting important
moments (Nathan 2012) and letting the AI do the hard work of
capturing what was said (Zhu 2021).

• Perception science also gives us strong hypotheses about how
to present automatic summaries to users so that they can
understand and browse the structure of a meeting (Zacks 2001).
• Extracting action items, key decisions, and other discourse
acts provides a focal point for asynchronous coordination and
has shown the potential to improve synchronous meeting focus
as well (Zhang 2018).

Hierarchical structure of event perception (Jeffery 2001) applied to
meeting summarization
Nathan, M., et al. (2012). In case you missed it: benefits of attendee-shared annotations for non-attendees of remote meetings. CSCW’12, 339-348.
Zacks, J. M., et al. (2001). Perceiving, remembering, and communicating structure in events. Journal of Experimental Psychology: General, 130(1), 29–58.
Microsoft Study: Zhang, A. X., & Cranshaw, J. (2018). Making Sense of Group Chat through Collaborative Tagging and Summarization. Proc. ACM-HCI 2018, 2(CSCW), Article 196.
Microsoft Study: Zhu, C., et al. (2021). MediaSum: A large-scale media interview dataset for dialogue summarization. arXiv preprint: arXiv.2103.06410.

51

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Async meeting experiences are needed, and summarization tech can help
Advanced information filtering and summarization systems may help improve the information choice
and overload challenges of pre-meeting materials, parallel chat, and post-meeting catch-up.
• There has been a 252% increase in weekly time
spent in meetings for the average Teams user since
February 2020 (Microsoft WTI 2022).
• Improving async collaborations has the promise of
making meetings more effective and reduce this
meeting load (Rogelberg 2018).

• Large language models / summarization methods
can convert raw meeting content to structured
async artifacts such as notes and action items for
post-meeting catchup and engagement (Sachdeva
et al. 2021).
Active pre-meeting document and related email recommendations in
Microsoft Outlook (Qian 2018)
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Rogelberg, S. G. (2018). The Surprising Science of Meetings: How You Can Lead Your Team to Peak Performance. Oxford.
Sachdeva, K., Maynez, J., & Siohan, O. (2021). Action Item Detection in Meetings Using Pretrained Transformers. IEEE ASRU’21, 2021, 861-868.
Microsoft Study: Zhao, Q., et al. (2018). Calendar-Aware Proactive Email Recommendation. ACM SIGIR ’18, 655–664 .

52

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Collaboration tools are not neutral
Technology shapes team activities and teams shape the way technology is used. Flexible collaborative
environments, co-created with workers, are likely to be most successful.
•

The relationship between team members in person is different than their relationship using a collaboration tool.
Managers should consider how teams and tools are partners forming “technologized team relationships” (Soga et al.
2021). Technologized team relationships are those in which the technology is an intermediator, an active participant that
influences, and is also influenced by, the human actors in the relationship. Very active examples include ‘to do’ apps that
prompt action or recommendations of documents or people. A less active but just as important example would be a
tool’s file upload, storage, and sharing capabilities, which directly impact information access and transparency.

•

Opportunities for valuable technologized team relationships lie in technologies doing what people find hard, such as
prioritization of work and awareness of project history (El Mezouar et al. 2021). However, technologized team
relationships may have unintended consequences, such as increased tendency towards trusting command-and-control
over relational engagement, tensions between transparency and the perception of surveillance, and problems over- or
under-estimating participation (Soga et al. 2021).

•

Meluso et al.’s (2022) review of reviews from management journals on distributed work found that the heterogeneity of
identities, incentives, and information in team collaboration means that no technology environment is likely to fit all
teams. They argue that flexible collaborative environments, co-created with workers, are most likely to be successful. This
needs to go beyond attempts to recreate yesterday’s work systems and instead capitalize on novel patterns and
capabilities, taking the technologized team relationship as a starting point.

•

Technology designed for this new way of working should be flexible enough to be used by different people in different
ways, while still allowing for focused work. It should also address known hybrid work issues, like working in different time
zones and catching up on what others have done since a person was last engaged in the work. As we build new tools, it
will be critical to get user feedback on if they are meeting the new needs of users. New frameworks for feedback, such as
BLUE (2022), can be used to get the best possible user feedback.

The future of team collaboration requires
deciding who are we together in this system and
then experimenting with and co-creating
flexible collaborative environments

El Mezouar, M., et al. (2021). Exploring the Use of Chatrooms by Developers: An Empirical Study on Slack and Gitter. IEEE Transactions on Software Engineering, Article 3109617.
Meluso, J., et al. (2022). Flexible Environments for Hybrid Collaboration: Redesigning Virtual Work Through the Four Orders of Design. Design Issues, 38(1), 55–69.
Soga, L. R., et al. (2021). Web 2.0-enabled team relationships: an actor-network perspective. European Journal of Work and Organizational Psychology 30(5), 639–652.
Microsoft Study: Hillman, S., et al. (2022) The BLUE Framework: Designing User-Centered In-Product Feedback for Large Scale Applications. ACM CHI EA’22, Article 21.

53

Organizational
Change
Key Contributors: Kagonya Awori, Nancy
Baym, Adam Coleman, Ed Doran,
Elizabeth Fetterolf, Constance N. Hadley,
Stacey Levine, Rick Pollak, Sean Rintel,
Neha Shah, Amy Stevenson, Mengting
Wan

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Communication in organizations became more siloed with more remote work
Remote work has influenced the way people collaborate in organizations, resulting in denser connections
within groups and weaker connections across groups. These effects may make it harder for employees to
acquire and share new information across the organizational network. Fortunately, hybrid work can likely help.
• In 2020, communication networks in organizations around the world became more modular or siloed compared to
2019 (Larson et al. 2021).
• This pattern broadly holds across countries and seems to coincide with the imposition of national emergency
orders.
• Study based on anonymized metadata from over 4,000 organizations worldwide, including 1.4 billion accounts.

Number of Bridging Ties

• Causal analysis shows that firm-wide remote work caused the collaboration network of workers to become more
static and siloed (Yang et al. 2021).
• People had 9% fewer bridging ties.
• There was a 40% drop in the share of collaboration time spent with bridging ties.
• Employees already working remotely were the “control” group to separate the effects of firm-wide remote work
from other confounding factors.
• Study based on anonymized metadata from Outlook and Teams for ~62k US MSFT employees.

• Pandemic remote work led to the loss of more than 480K weak ties among researchers at MIT (Carmody et al.
2022).
• There is strong reason to believe hybrid work will ameliorate some or most of these effects, and research is
underway at Microsoft to more fully explore this hypothesis.
• Spatial co-location during hybrid work helped bring back some lost ties at MIT (Carmody et al. 2022).

Yang et al. (2021)

Carmody, D., et al. (2022). "The effect of co-location of human communication networks." arXiv preprint, arXiv:2201.02230.
Microsoft Study: Larson, J., et al. (2021). "Dynamic Silos: Increased Modularity in Intra-organizational Communication Networks during the Covid-19 Pandemic." arXiv preprint, arXiv:2104.00641.
Microsoft Study: Yang, L., et al. (2021). The Effects of Remote Work on Collaboration among Information Workers. Nature Human Behavior, 6, 43-54.

55

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Building and maintaining relationships is harder in remote work
The social side of workplace relationships, including exchanges of non-work-related information, social
support and even small talk, is particularly influential role in building trust and fostering innovation.
• Social work relationships, and social support in particular, promote
job satisfaction, organizational commitment, and the success of remote
work (Charalampous et al. 2019).
• Small talk enhances positive social emotions at work, translating into
heightened organizational citizenship behaviors (OCB) and wellbeing at the
end of the workday (Methot et al. 2021).

• Emotional demands of work diminish job performance. Having colleagues
with whom you can vent and relax can buffer these negative effects
(Parker et al. 2022).
• The difficulty of social support and small talk may be one factor in the
increased siloing of collaboration networks in remote work. (See previous
slide on collaboration networks.)

Glint (2021)

Charalampous, M., et al. (2019). Systematically reviewing remote e-workers’ well-being at work: A multidimensional approach. European Journal of Work and Organizational Psychology, 28(1), 51-73.​
Microsoft Study: Glint (2021). People science culture consultation deck. LinkedIn. [Internal]
Methot, J. R., et al. (2021). Office chitchat as a social ritual: The uplifting yet distracting effects of daily small talk at work. Academy of Management Journal, 64(5), 1445-1471.​
Parker, A., et al. (2022). "The coevolution of emotional job demands and work-based social ties and their effect on performance." Journal of Management (2022).​

56

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The pandemic raised awareness about workplace loneliness
Workplace loneliness was a problem before the pandemic and continues to be one now, as remote and
gig workers may experience even greater isolation.
•

The pandemic has increased public awareness of loneliness in the workplace, but it is not a new issue. U.S. Surgeon General
Vivek Murthy declared a workplace Loneliness Epidemic in 2017. CIGNA (2020) estimated that 62% of U.S. workers were
lonely in 2019.

•

In a survey of global executives just prior to the pandemic, most struggled to make deep connections to others at work
despite working on multiple concurrent teams (Hadley & Mortensen 2020).

•

Worker loneliness is associated with debilitating health problems and work problems (e.g., lowered performance, creativity,
and decision-making) (Holt-Lunstad et al. 2010).

•

Loneliness is estimated to be extremely costly to economies around the world (e.g., US: $406B/year; UK: £2.5B/year)
(CIGNA, 2020; Peytrignet et al. 2020).

•

Remote work is often lonely. A 2021 study found that almost 2/3rds of people working from home feel isolated or lonely at
least sometimes and 17% do all the time (American Psychiatric Association, 2021).

•

55% of hybrid employees and 50% of remote employees feel lonelier at work than before going hybrid or remote
(Microsoft WTI, 2022).

•

59% of hybrid employees and 56% of remote employees report having fewer work “friendships” since going hybrid or
remote (Microsoft WTI 2022).

•

Gig or freelance workers report significantly higher loneliness rates than those working for a private company (e.g., 82% vs.
61%) (Glavin et al. 2021; CIGNA 2020).

American Psychiatric Association (2021) As Americans Begin to Return to the Office, Views on Workplace Mental Health Are Mixed. Psychiatry.org.
CIGNA (2020). Loneliness and the Workplace 2020 US Report.
Glavin, P., et al. (2021). Über-Alienated: Powerless and Alone in the Gig Economy. Work and Occupations, 48(4), 399–431.
Hadley, C., & Mortensen, M. (2020) Are Your Team Members Lonely? MIT Sloan Management Review.
Holt-Lunstad, J., et al. (2010) Social Relationships and Mortality Risk: A Meta-analytic Review. PLoS Med 7(7): e1000316.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Murthy, V. (2017) Work and the Loneliness Epidemic: Reducing isolation at work is good for business. Harvard Business Review.
Ozcelik, H., & Barsade S. G. (2018). No Employee an Island: Workplace Loneliness and Job Performance. Academy of Management Journal, 61(6) 2343-2366.
Peytrignet, S., et al. (2020). Loneliness monetization report. Simetrica.

Breakdown of Costs
of Employee Loneliness
(2019 U.K. Estimate)
Increased staff
turnover

1%
9%

26%
64%

Lower
wellbeing and
productivity
Impact of
caring
responsibilities
Ill health
absences

57

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Socio-tecture was essential to many SMBs during the pandemic
Globally, 80% of organizations are small and medium businesses (SMBs). In Africa, many heavily relied
on socio-tecture to catalyze technology adoption and survive the pandemic.
•

•

Socio-tecture is a fundamental quality of business activity, observed in SMBs in Africa, where the social
and business are tightly coupled. It involves building for relationships and networks as integral to
building for business. Key facets of socio-tecture are:
•

Heavy reliance on networks: preference of strong ties over loose ties, and loose ties over no ties.

•

Establishing strategic (instead of only transactional) relationships when conducting business.

•

People as the primary source of knowledge : The experiences of ties are heavily relied upon by
SMBs for tech use and tech purchase decisions, as opposed to e.g., YouTube ads or feature emails.
As summarized by an SMB, “It’s only when somebody I know says a tool worked for them that I
believe it will work for me” (Awori et al. 2022).

During the pandemic, technology adoption was guided by socio-tecture.
•

When choosing communication tools, SMBs preferred WhatsApp over others, as it better enabled
them to build trusted relationships and strengthen loose ties – for example, requiring users' phone
numbers to connect on WhatsApp helped the SMB engage more personally with their customers;
WhatsApp groups helped SMBs build closed networks with people they could verify (Awori et
al. 2022).

•

Many SMBs and their customers prefer social commerce – a development in e-commerce that
leverages social media and participatory Web 2.0 technologies to enable interaction between
businesses and their customers, and among customers (Turban et al. 2010) – because it affords
better social engagement and interaction (Pon 2020; Naghavi 2019).

Based on a study with SMBs in Kenya during the
pandemic, SMBs prefer communication tools that better
afford the creation/management of strong ties, a key facet
of socio-tecture
(Awori et al. 2022)

Microsoft Study: Awori, K., et al. (2022). “It’s only when somebody says a tool worked for them that I believe it will work f or me”: Socio-tecture as a lens for digital transformation. (Under Review)
Turban, E., et al. (2010). Social Commerce: An e-Commerce Perspective. ICEC ‘10 Association for Computing Machinery, 33-42.
Naghavi, N. (2019). Social commerce in emerging markets: Understanding the landscape and opportunities for mobile money. GMSA
Pon, B. (2020). The race to digitize commerce in sub-Saharan Africa: How Jumia and Facebook are competing, even though they’re playing different games. Medium.com

58

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The work of building social capital increased, but was often unrecognized
Social capital is essential to the success of organizations, but social capital builders are often uncredited
and unrewarded. These dynamics likely got worse during the pandemic.
•

Social capital is a collective good. It is both a resource exchanged within relationships and a structure of relationships (A dler &
Kwon 2009). Organizational networks rich in equitable strong and weak ties can lead to less absenteeism and turnover, better
performance, more creativity, more efficiency, and more revenue (Ben Hador 2016; Sözbilir 2017; Westlund & Adam 2010).

•

In on-site work, relationship building often happens alongside the formal events of the day (Kraut et al. 1990). Without
opportunities for spontaneous informal interaction in remote work, it takes additional effort to build and maintain relationships
(Charalampous et al. 2019).

•

43% of leaders say building social capital is the biggest challenge of remote and hybrid work (Microsoft WTI 2022), yet
organizations often privilege work that produces products and services directly over “nonmonetized production” (Jarrett 2014)
such as building relationships. This kind of “connective labor” (Pugh 2021) is often disproportionately expected of women (Ja rrett
2014).

•

In a survey of 850 American office workers, 51% indicated they have made greater efforts to provide support for their colleag ues
than before the pandemic, while only 15% said they were doing less. 85% of employees said their organizations encouraged or
strongly encouraged people to support each other and 80% said they felt somewhat or strongly obligated to go above and
beyond to support co-workers. Yet nearly 25% indicated that in their organization, providing support for others was not at all
rewarded, and only 34% said providing such support was strongly rewarded (Baym et al. in progress).

•

New tools aim to help by suggesting potential weak ties, such as Bridger (Portenoy et al. 2022), which is designed to facilitate
discovery of scholars in areas somewhat related but also somewhat novel to a researcher's current areas of work.

Adler, P. S., & Kwon, S. W. (2009). Social Capital: The Good, The Bad, and The Ugly (Working Paper MKT 03-09; Marshall Research Paper Series, pp. 89–115). University of Southern California.
Microsoft Study: Baym, N., et al. (in progress). Social Support Among Co-workers: A survey of American Office Workers.
Charalampous, M., et al. (2019). Systematically reviewing remote e-workers’ well-being at work: A multidimensional approach. European Journal of Work and Organizational Psychology, 28(1), 51-73.
Ben Hador, B. (2016). How intra-organizational social capital influences employee performance. Journal of Management Development, 35(9), 1119–1133.
Jarrett, K. (2014). The Digital Housewife, Routledge.
Kraut, R., et al. (1990). Informal communication in organizations: Form, Function, and Technology in Human Reactions to Technology: Claremont Symposium on Applied Social Psychology.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Pugh, A. (2021). Emotions and the systematization of connective labor. Theory, Culture & Society.
Sözbilir, F. (2018). The interaction between social capital, creativity and efficiency in organizations. Thinking Skills and Creativity, 9.
Westlund, H., & Adam, F. (2010). Social Capital and Economic Performance: A Meta-analysis of 65 Studies. European Planning Studies, 18(6), 893–919.
Portenoy, J. et al. (2022) Bursting Scientific Filter Bubbles: Boosting Innovation Via Novel Author Discovery. ACM SIGCHI 2022.

People report being expected to
provide support more than they
report being rewarded for it
(Baym et al.)

59

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Culture is a leading driver of the Great Reshuffle
Several studies have found strong correlations between toxic company culture and people’s decisions to
seek new jobs.
•

A Pew Research Center poll found that 57% of Americans who resigned 2021 cited feeling “disrespected at work” as a
reason for leaving; 35% said it was a “major reason” (Parker & Horowitz 2022).
•

Globally, while the Microsoft (2022) Work Trends Index survey did not ask about culture specifically, it found
that the top two reasons employees quit were: personal wellbeing or mental health (24%) and work-life
balance (24%).

•

In an analysis of 500 of the largest US companies, researchers found that companies whose Glassdoor descriptions
indicated healthier organizational cultures had lower-than-average turnover (estimated from Revelio Labs profiles)
relative to other companies in the same industry. Furthermore, in this NLP analysis, toxic corporate culture was 10.4
times more important than compensation in predicting attrition (Sull et al. 2022a).

•

A variety of factors can contribute to cultural toxicity. The strongest predicters of employees’ ratings of a culture and
company attrition rates were Glassdoor reviews referring to disrespectful, non-inclusive, unethical, cutthroat and
abusive elements (Sull et al. 2022b). A qualitative analysis of Glassdoor reviews similarly highlighted how normalizing
racism, sexism, and discrimination contributes to cultural toxicity (Bergstrom 2022).

•

In surveys, employees who feel cared for at work are 3.2x more likely to be happy at work and 3.7x more likely to
recommend working at their company. Both of these likelihoods increased 35% over the course of the pandemic
(LinkedIn 2021).

Microsoft Study: Baym, N., et al. (in progress). Social Support Among Co-workers: A survey of American Office Workers.
Bergstrom, K. (2022). When a Door Becomes a Window: using Glassdoor to examine Game Industry Work Cultures. Information, Communication and Society.
Microsoft Study: LinkedIn (2021). Internal employee engagement research.
Parker, K., & Horowitz, J. M. (2022). Majority of workers who quit a job in 2021 cite low pay, no opportunities for advancement, feeling disrespected. Pew
Research Center.
Sull, D., et al. (2022a). Toxic Culture is Driving the Great Resignation. Sloan Management Review.
Sull, D., et al. (2022b) Why Every Leader Needs to Worry About Toxic Culture. Sloan Management Review.

Sull et al. (2022b)

60

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

New data points to hybrid work helping to reduce employee turnover
A recent experiment, backed by prior work, suggests hybrid work may be one way for firms to keep
their employees, although it is unclear how market dynamics will evolve.
• In a preliminary analysis of a randomized experiment with college graduates
at a large multinational firm based in China, Bloom et al. (2022) found that
fixed weekly 3-2 hybrid (three days at work, two days at home each week,
with those days fixed across the firm) reduced quit rates by 35% and sick
leave by 12%. There was no statistically significant effect on performance or
promotions.
• This work builds on prior research that also saw reduced turnover with
alternative working arrangements (Bloom et al. 2015; Moen et al. 2012), as
well as earlier work that found that job satisfaction at a large IT firm peaked
at 2 days WFH per week (Golden and Veiga 2005).

Bloom et al. 2022

• Hybrid work arrangements are much rarer in China, and this may have
affected attrition rates. It is unclear whether similar effects would be
observed in a market in which hybrid work is much more common.
Golden & Veiga (2005)
Bloom, N. et al. (2015). Does Working from Home Work? Evidence from a Chinese Experiment. The Quarterly Journal of Economics. 130(1), 165–218.
Bloom, N. et al. (2022). How Hybrid Work From Home Works Out (Preliminary).
Golden, T.D. & Veiga, J.F. (2005). The Impact of Extent of Telecommuting on Job Satisfaction: Resolving Inconsistent Findings. Journal of Management. 31(2), 301–318.
Moen, P., et al. (2011). Does Enhancing Work-Time Control and Flexibility Reduce Turnover? A Naturally Occurring Experiment. Social problems. 58(1), 69–98

61

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Microsoft’s history with hybrid reinforces the role of managers and technology
Since its founding in 1975, Microsoft has had remote and hybrid employees, yet much of the company
experienced a pandemic learning curve that was not that different from many other organizations.
•

Microsoft’s original mission of “a computer on every desk and in every home” included an emphasis on supporting
at-home business activities.

•

Microsoft has done research on remote work and telepresence for 30+ years (Teevan & Hecht 2020). Microsoft
product offerings reflect that, starting with MS-DOS support for modems in 1981.

•

The company began in a hybrid fashion, with co-founder Bill Gates working remotely from Harvard.

•

However, remote work was not a norm for all but a few functions, like sales. That is because the physical workplace
has historically been an important enabler of work. Microsoft developers needed to go into the office since that was
where the computers and connectivity were fastest, and even the field was dependent on business equipment at the
office in the 80s and 90s. The ability to work from home depended on the reliability and performance of the
expanding internet infrastructure.

•

Work hours at Microsoft have always been flexible. An early employee handbook from Fall 1985 states: “You should
establish your normal working hours with your manager and agree with him/her on the degree of acceptable
variance in those hours.”

•

Microsoft employees did not historically spend all of their time at the office working, however. Code compilation
used to mean many minutes of downtime for developers. Personal activities at work remain culturally acceptable.

Microsoft Study: Stevenson, A. (2022). Microsoft’s Pre-Pandemic History of Hybrid 1975-2020: A Perspective from the Corporate Archivist. [Internal]
Microsoft Study: Teevan, J. & Hecht, B, (2020). “How research can enable more effective remote work.” Microsoft Research Blog.

A snippet of the floor plan from the first Microsoft office
in Albuquerque,1976, shows Bill Gates’ future workspace.

62

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Leaders may not be keeping up with evolving employee expectations
Employees are increasingly seeking flexibility, autonomy, and to be heard, but there are gaps between
their expectations and what organizations are currently offering them.
•

Over half of managers in Microsoft’s global Work Trend Index (external survey) reported that leadership at their company is out of touch with
employee expectations. Even more say they lack the influence or resources to create change in their team. Half of surveyed le aders plan to require
full-time in-person work, despite 52% of surveyed employees being likely to consider going hybrid or remote in year ahead (Micro soft WTI 2022).
•

For the 18% of respondents who quit their jobs in 2021, work-life balance and lack of flexible work hours/location were among the top five
reasons, with pay near the bottom of the list.

•

The survey also found while over 80% of employees feel they have been just as or more productive since the shift to remote or hybrid, 54%
leaders fear productivity has been negatively impacted.

•

A 2021 Gartner study of 4000 employees showed a significant difference between executives' and employees’ perceptions: 75% of executives said
their companies offered flexibility, but only 57% of employees did (Baker 2021).

•

An internal survey for Citrix’s Work 2035 Project in May 2021 showed that while 86% of employees prefer to work for a company that prioritizes
outcomes over output, only 50% of HR directors said their organization would be more productive if employees felt their emplo yer/senior
management team trusted them to get the job done without monitoring their progress (Minahan 2021).

•

Many organizations still rely on one way organization-to-employee relationships, but organizations with means for employees to communicate
upwards build stronger organization-employee relationships and are more resilient (Kim 2021). Insights from customer interviews reinforce this
increasing need to adapt and think differently about employees, as encapsulated by this participant comment:
•

“Trust people to do the job they are employed to do. We moved forward 10-15 years in how the organization thinks about employees just in
the past 18 months” - Senior Wealth Manager | Banking | UK (Coleman 2021).

Citrix citation in HBR (2021). What Your Future Employees Want Most. Hybrid Business Review.
Microsoft Study: Coleman, A. (2021). How business leaders are preparing for a new period of workplace uncertainty. Microsoft Research.
Baker, M. (2021). What is work really like today? Leaders and employees see things differently. Gartner.
Kim, Y. (2021). Building organizational resilience through strategic internal communication and organization-employee relationships. Journal of Applied Communication Research.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Minahan, T. (2021). What Your Future Employees Want Most. Harvard Business Review.

50%

of leaders say their
company requires or
plans to require full-time
in person work in the
year ahead

74%
of managers say they
don’t have the influence
or resources to make
change for employees

54%
of managers say
leadership is out of touch
with employees

63

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Organizations must eschew common misconceptions about hybrid work
Below are a few common misconceptions about hybrid work, and how to rethink them.
• Misconception: “Where to work is purely a ‘personal decision’.”
o Network effects like the ability to collocate with a colleague make work location a team and
organizational conversation, not purely an individual one. Hybrid work can provide additional
individual flexibility, but it must be balanced with the needs of one’s coworkers and one’s
organization.
• Misconception: “All workers should have the same experience, regardless of their work location.”
o The literature makes clear that remote and collocated work have very different strengths and
weaknesses (Allen et al. 2015). Policy and technology should seek to accentuate the benefits and
mitigate the weaknesses of each separately. An analogy can be drawn to the different experiences
afforded by smartwatches, smartphones, and desktop computers. See graphic for one way we
operationalize this idea.
• Misconception: “Hybrid work is only about flexibility in work location.”
o Hybrid work should also involve flexibility on the temporal dimension (i.e., when people work). A
major implication is that many teams should agree on collocated hours (e.g., 10-3pm), not days,
as this will allow for people to avoid traffic and dramatically cut down on time spent commuting,
one of the most significant downsides of collocated work (Ford et al. 2021).
• Misconception: “The office is only useful for collaboration.”
o While offices certainly have some important affordances for collaboration, and these are one of
the reasons hybrid work can be so powerful, offices are also useful for a number of other reasons.
For instance, offices provided much-desired work/life separation for some and, for those who do
not have adequate focus space at home (remote work can require larger residences), they make it
possible to focus while doing one’s job. Relatedly, home offices are likely be better for
collaboration than offices for certain types of meetings, e.g., large read-out style meetings.

Instead of designing products (and policy) to provide
the same experience for remote and collocated
workers, instead think about how to accentuate the
unique strengths of each mode and mitigate each
mode’s unique weaknesses

Allen, T. D., et al. (2015). How Effective Is Telecommuting? Assessing the Status of Our Scientific Findings. Psychological Science in the Public Interest 16(2) 40–68.
Microsoft Study: Ford, D., et al. (2022). A Tale of Two Cities: Software Developers Working from Home During the COVID-19 Pandemic. ACM Transactions on Software Engineering and Methodology 31(2).

64

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Workplace recommendation systems can help with remote work challenges
Sustaining interpersonal connections has been challenging during remote work. Workplace
recommendation systems can help facilitate meaningful connections by suggesting related people,
content, and knowledge.
• Cross-industry analysis showed that workplace social media improves organizations'
operational efficiency and innovativeness (Lam et al. 2016).
• “People You May Know” recommendations in LinkedIn (Yin et al. 2021) helped
members, regardless of their network strength, make effective professional connections.
• Recommendation systems have the potential to drive positive behavior change that
improves productivity, e.g., surfacing alternative choices, prioritizing actions (Schrage 2021).
• Workplace recommendation systems are the core AI engine for social platforms that can
improve business outcomes. (See slide 69 on AI-powered social platforms.)

LinkedIn’s “People you may know”

Lam, H. K., et al. (2016). The impact of firms’ social media initiatives on operational efficiency and innovativeness. Journal of Operations Management.
Schrage, M., (2021). The Transformational Power of Recommendation. MIT Sloan Management Review, 62(2), pp.17-21.
Microsoft Study: Yin, Q., et al. (2021). Optimizing People You May Know (PYMK) for equity in network creation. LinkedIn Engineering.

65

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Technology choices may trade off intra-team and cross-org effectiveness
When teams choose different sets of remote collaboration tools, they are trading off intra-team against
inter-team effectiveness. Practical facilitation and technical solutions are needed to bridge teams.
• Hu et al. (2022) conducted a large ethnography of multiple scientific
teams within an organization during the COVID-19 pandemic, using
the “Distance Matters” framework (Olson & Olson 2000, 2013).
• They found that while sets of remote collaboration tools, such as
the Microsoft 365 ecosystem, have improved intra-team remote
work, inter-team remote work can suffer when different teams
use different sets of tools (e.g., one team might use only
Microsoft tools and another uses only open-source tools).
• Hu et al. (2022) propose there is a need for facilitation and technical
bridges between teams, and a broader understanding of the
ramifications of technology choices for intra- and inter-team goals.
Market factors are likely to limit technical connections unless major
players can agree on shared standards or access.
• Cross-team tool alignment also facilitates mobility within the
organization.

There is a trade-off between intra-team and interteam effectiveness when they use different sets of
remote collaboration tools (Hu et al. 2022)

Olson, J. S., & Olson, G. M. (2013). Working Together Apart: Collaboration over the Internet. Synthesis Lectures on Human-Centered Informatics 6(5), 1–151.
Olson, G. M., & Olson, J. S. (2000). Distance matters. Human-Computer Interaction 15(2), 139–178.
Xinlan E. H., et al. (2022). A "Distance Matters" Paradox: Facilitating Intra-Team Collaboration Can Harm Inter-Team Collaboration. Proceedings of the ACM on Human-Computer Interaction, 6(CSCW1), Article 48.

66

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Office space can pay for itself with improved productivity
Focusing too much on cost-savings when thinking about space can be counterproductive.
•

Rent and facility costs are often a small fraction of payroll. A useful rule of thumb is that facility costs are 10% of
wages (JLL 2016).
o

•

If an office can boost productivity by 10%, it pays for itself. Conversely, if eliminating an office reduces
productivity by 10%, it hasn’t improved net revenue.

Many studies point to properties of work environments boosting productivity at 10% or more.
o Office noise can reduce memory, motivation and energy by about 10% (Jahncke et al. 2011).
o Academics are approximately 20-30% more likely to get a grant for every 100ft of additional overlap in
common paths they travel in the office (Kabo et al. 2014).
o

Sharing a building increases collaboration among MIT scientists by a significant margin (Miranda & Claudel
2021).

•

Putting two people nearby each other might be the most powerful easily-available way to catalyze collaboration
outside of top-down methods.

•

New technologies that make the office even more useful will likely increase the productivity effect of the office.

•

An important implication is that decisions about reducing office space should be made for reasons other than
cutting costs. Reducing space might be the right decision, but because it’s right for an organization for other
reasons, not cost savings.

Jahncke, H., et al. (2011). “Open-Plan Office Noise: Cognitive Performance and Restoration.” Journal of Environmental Psychology 31(4), 373–82.
JLL (2016), A Surprising Way to Cut Real Estate Costs.
Kabo, F. W., et al. (2014). “Proximity Effects on the Dynamics and Outcomes of Scientific Collaborations.” Research Policy 43(9), 1469–85.
Miranda, A. S., & Claudel, M. (2021). “Spatial Proximity Matters: A Study on Collaboration.” PLOS ONE 16, no. 12.

Miranda & Claudel (2021)

67

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Spatial environments are conducive to ad hoc engagement, at least in bursts
Spatial environments allow natural transitions between focused and ad hoc interactions, both for work
and social purposes, but all-day use and accessibility are still in question.
•

Students prefer learning in the 2D videogame style spatial environments of systems like Gather.Town or Sococo in
comparison to other learning platforms. An important aspect of this preference is the ease of moving between social
encounters (Latulipe & De Jaeger 2022; McClure & Williams 2021).

•

Spatial environments are reported to encourage both focused and ad hoc collaboration (Najjar et al. 2022).

•

More abstract spatial environments that do not have illustrated characters and maps, but do have spatial audio, are also
rated highly for enabling quick transitions between focused presentations, workshops, and networking at events
(Rogers et al. 2021).

•

Jacobs and Lindley (2021) report that such spaces tend to be popular in bursts – for short periods in a day or for a few
days for a conference. However, it remains to be seen if such spaces are fatiguing or lose their novelty throughout full
workdays and over weeks and months.

•

Being based on a videogame paradigm, most also require significantly more accessibility support for blind and low
vision (BLV) users, users with motor impairments, and other people with disabilities.

2D videogame style environments such as
Gather enable transitions between different
kinds of talk

Jacobs, N. J., & Lindley, J. (2021). Room for improvement in the video conferencing “space.” AoIR Selected Papers of Internet Research.
Latulipe, C., & De Jaeger, A. (2022). Comparing Student Experiences of Collaborative Learning in Synchronous CS1 Classes in Gather.Town vs. Zoom. SIGCSE 2022.
McClure, C. D., & Williams, P. N. (2021). Gather.town: an opportunity for self-paced learning in a synchronous, distance learning environment. Journal of Learning and Teaching.
Najjar, N., et al. (2022). Evaluating Students’ Perceptions of Online Learning with 2-D Virtual Spaces. SIGCSE 2022.
Rogers, B., et al. (2021). BubbleVideo: Supporting Small Group Interactions in Online Conferences. In Human-Computer Interaction – INTERACT 2021, Springer International Publishing, Cham, 67–75.

68

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

AI-powered social platforms have potential for improving business outcomes
There is growing evidence suggesting that algorithmically curated online communities, enterprise
knowledge collections, and company feed have great potential for improving business outcomes and
employee experiences.​
•

A study across 281 firms found that launching enterprise social platforms (e.g., internal communication platforms, external
customer community platforms) can improve organizations' operational efficiency (transforming operational resources to
output) and innovativeness (innovation ratings by Fortune) (Lam et al. 2016).

•

A survey conducted across 89 high-tech enterprises in China revealed that knowledge sharing practices, through
institutionalized knowledge collections and social interactions, are positively associated with organizational innovation and
firm performance (Wang & Wang 2012).
o

Explicit knowledge sharing (e.g., through institutionalized knowledge collections) has more significant positive
effects on innovation speed (e.g., speed in new product launching) and firm financial performance (e.g., average
profit, profit growth).

Lam et al. (2016)

o Tacit knowledge sharing (e.g., through social interactions) has more significant positive effects on innovation quality
(e.g., quality of new product development) and firm operational performance (e.g., customer satisfaction, cost
management).
•

A structurally diverse ego-network with both strong/bonding ties and weak/bridging ties can provide access to new
knowledge and resources, possibly affecting firm productivity, innovation, and performance (Burt, 2007).

•

Quantitative simulations on Twitter data showed that AI-powered recommender systems can be designed to balance
engagement and outcomes that are important to healthy networks: they diminish engagement only a marginal amount
and increase information flow, diversity, novelty, and efficiency across the network (Sanz-Cruzado & Castells 2018).

Wang & Wang (2012)

Lam, H. K., et al. (2016). The impact of firms’ social media initiatives on operational efficiency and innovativeness. Journal of Operations Management.
Wang, Z., & Wang, N. (2012). Knowledge sharing, innovation and firm performance. Expert Systems with Applications, 39(10), 8899-8908.
Burt, R. S. (2007). Brokerage and Closure: An Introduction to Social Capital. Oxford University Press.
Sanz-Cruzado, J., & Castells, P. (2018). Enhancing structural diversity in social networks by recommending weak ties. In Proceedings of the 12th ACM conference on recommender systems.

69

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Employee-centered privacy is a major priority in remote and hybrid work
In remote and hybrid work, technology mediates more of people’s work than ever before. This offers
opportunities to support workers and organizations in new ways, but also presents privacy risks.
Employee-centered privacy is about maximizing the reward and minimizing the risk.
• Potential benefits of increased technological mediation of people’s interactions with other people and information at work
include intelligent scheduling assistance, work-life balance support, more personalized intelligent technologies, and others.
• However, increased mediation also presents risks to employee privacy. Reductions of employee privacy has been associated
with higher worker stress levels, reduced organizational commitment, reduced trust in management, paradoxically increased
deviance, reduced short-term productivity, reduced creativity, and other negative outcomes (Thiel et al. 2021; Chory et al.
2015; Ravid et al. 2020).
• Employee-centered privacy seeks to unlock the benefits of technological mediation while minimizing the risks.
• The literature on privacy at work points to some design principles that can enable worker-centric privacy, such as
maximizing transparency and end user control, protecting against mission creep, educating stakeholders about the risks and
benefits of recording certain types of information, and educating stakeholders about the specific inferences that can (and
cannot) be made from specific types of data (Ravid et al. 2020).

Chory, R. M., et al. (2016). Organizational Surveillance of Computer-Mediated Workplace Communication: Employee Privacy Concerns and Responses. Employee Responsibilities and Rights Journal 28(1):23–43.
Microsoft Study: Ravid, D. M., et al. (2020). A Meta-Analysis of the Effects of Digital Surveillance of Workers: A Psychology Focused Approach. In New Future of Work Symposium, Microsoft.
Thiel, C., et al. (2021). Stripped of Agency: The Paradoxical Effect of Employee Monitoring on Deviance. Academy of Management Proceedings, 1.

70

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Employee-centered privacy matters across the socioeconomic spectrum
Past research has found that privacy risks at work are more severe for lower wage, hourly employees
than for those with more autonomy over their work.
• According to a 2021 report from the European Commission, workers with low levels of
autonomy in their jobs (such as low wage service workers) were more at risk of the negative
psycho-social effects of worker privacy issues than those with high levels of autonomy (such
as information workers) (Ball 2021).
• Interviews with workers, scholars, and labor organizations found that low-wage, hourly
workers are particularly at risk of precarity, work speedups, and racial profiling due to
employee privacy issues (Nguyen 2021).
• Through participant observation, documentary research, and 40 in-depth interviews, Vargas
(2017) found that managers used invasive technologies to treat low-wage, marginalized
dollar store employees with suspicion, creating an environment in which these vulnerable
workers were set up to fail.
• Risks in this domain have particularly negative impact on workers who already face
discrimination in the workplace; female employees have reported discomfort with facial
recognition (Stark et al. 2020) and workers of color are more at risk of negative pyschosocial outcomes (Ball 2021).
Nguyen (2021)
Ball, K. (2021). Electronic monitoring and surveillance in the workplace: Literature review and policy recommendations. Joint Research Centre of the European Commission.
Nguyen, A. (2021). The Constant Boss: Work under digital surveillance. Data & Society Research Institute.
Stark, L., et al. (2020). “I Don’t Want Someone to Watch Me While I’m Working”: Gendered Views of Facial Recognition Technology in Workplace Surveillance. Journal of the Association for Information Science and
Technology, 71: 1074– 1088.
Vargas, T. L. (2017). Employees or Suspects? Surveillance and Scrutinization of Low-Wage Service Workers in U.S. Dollar Stores. Journal of Labor and Society, 20(2), 207–230.

71

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Threats to security of video meetings: Network scraping and deepfakes
Real identities determined from posted images of meetings and faked identities created through AI may
allow malicious activities.
•

Network scraping attacks use publicly posted images of meetings as a seed for identifying and maliciously acting
upon individuals or teams. Kagan et al. (2020) show how a person’s face and other extracted features may be
compared against social media posts to enable identification. Photos from multiple meetings may also identify
co-workers and content. This may then be used against individuals, families, teams, and organizations.
•

•

Organizations should inform employees about risks from posting meeting photos/videos to social media.
Platforms could support more privacy modes.

Deepfakes in video meetings (Westerland 2019) are AI-generated realistic-appearing artificial representations of
people generated from image, video, and/or voice samples. They allow one person to appear as another and have
potential for misuse when team members meet with unknown others (Mullen 2022). They also may be used for
cultural identity appropriation (Bode et al. 2021), such as a white person representing themselves as a black
person, which could affect team trust and morale. Creating and detecting deepfakes is an ongoing arms race
(Zhou 2021; Kagan 2022; Mullen 2022). (See slide 45 on avatar acceptance.)
•

Public posting of video meeting images
allows malicious aggregation (Kagan et
al. 2020)

Industry coalitions like the Content Authenticity Initiative and C2PA (of which Microsoft is a founding
member) working on digital content provenance present possible strategies for mitigating these and
related risks.

Aliev, A. (2022). Avatarify Python.
Kagan, D., et al. (2020). Zooming Into Video Conferencing Privacy and Security Threats. arXiv preprint, arXiv:2007.01059.
Mittal, T., et al. (2020). Emotions Don’t Lie: An Audio-Visual Deepfake Detection Method using Affective Cues. In Proceedings of the 28th ACM International
Conference on Multimedia.
Mullen, M. (2022). A New Reality: Deepfake Technology and the World Around Us. Mitchell Hamline Law Review 48(1), Article 5.
Westerlund, M. (2019). The Emergence of Deepfake Technology: A Review. Technology Innovation Management Review 9(11),, 40–53.
Zhou, Y., & Lim, S. (2021). Joint Audio-Visual Deepfake Detection. IEEE/CVF International Conference on Computer Vision, 14800–14809.

Aliev’s (2022) Avatarify Python’s
deepfake video of the Mona Lisa as a
videoconferencing participant

72

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Organizations will need to be prepared for ongoing disruptions beyond COVID-19
With climate disasters and public health crises on the horizon, organizations must foster resilience
•

Margherita & Heikkilä (2021) investigated the actions undertaken by 50 world-leading corporations to respond
to COVID-19 to develop a five-level framework to ensure continuous collaboration in the face of disruption. The
levels are: operations, customer, workforce, leadership, and community-related responses.

•

A report by McKinsey highlighted disruptions due to climate change as a major future trend that will shape how
organizations function and present a potential barrier to thriving (Pinner et al. 2020).

•

Chen et al. (2021) conducted exploratory case studies (using textual data, such as company materials, media
coverage, employee accounts, and annual reports) of six major companies deemed highly resilient, including
Microsoft. They found five dimensions of resilience—capital, strategic, relationship, cultural, and learning—that
allowed these companies to continue growing after a crisis.

•

Organizational resilience has direct impacts on employees. A study of 2,225 software developers from 53
countries found that for these employees, fear of both the current pandemic and future bio-events might
be facilitating lower productivity and well-being. Disaster preparedness among employees was correlated with
higher perceived productivity and organizational support was deemed essential (Ralph et al. 2020). Furthermore,
a survey of prospective employers by Krasna et al. (2020) found that 91.7% of respondents thought that the need
for employees with training that encompasses both public health and climate change responses will grow over
the next decade.

The organizational resilience
process (Chen et al. 2021)
Chen, R., et al. (2021). Defining, Conceptualizing, and Measuring Organizational Resilience: A Multiple Case Study. Sustainability, 13, 2517.
Krasna. H., et al. (2020). The Future of Careers at the Intersection of Climate Change and Public Health: What Can Job Postings and an Employer Survey Tell Us? International Journal of Environmental Research and Public Health.
Margherita, A., & Heikkilä, M. (2021). Business continuity in the COVID-19 emergency…. Business Horizons 64(5), 683–695.
Pinner, D., et al. (2020). Addressing climate change in a post-pandemic world. McKinsey Quarterly.
Ralph, P., et al. (2020). Pandemic programming: how COVID-19 affects software developers and how their organizations can help. Empirical Software Engineering 25(6).

73

Societal Impacts
Key Contributors: Siddharth Suri, Scott
Counts, Mia Bruch

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

We are likely entering a new era in the geography of work
There have been roughly five eras in the geography of work in the history of the United States. There is
evidence we are now beginning a sixth: the Hybrid Work Era.
•

•

•

•

Although geographers may quibble about the specifics, prior to the pandemic, there were
roughly five eras in the geography of work since the founding of the United States.
•

1) Industrial Revolution, 2) Skyscraper, 3) Suburbs, 4) Edge City, 5) Superstar City.

•

The coming Hybrid Work Era will be our sixth.

New technologies often drive the transition between eras.
•

Steel-frame construction helped bring about the Skyscraper Era.

•

Democratized access to cars enabled people to commute to work in the Suburbs Era.

•

Digital technologies like Office, Outlook, and Teams will shape the Hybrid Work Era.

The key spatial relationships in the Hybrid Work era are those between digital technologies and
space. There are three ways digital and spatial technologies can interact:
•

Digital technology can help people understand changes in how space is used for work,

•

Digital technology can substitute for space (e.g., replace meeting rooms), and

•

Digital technology can complement space (e.g., help people use offices in new ways).

New eras in the geography of work generally bring many large benefits (e.g., better living
standards), but also new challenges (e.g., uneven distribution of those standards). Those in the
tech ecosystem will need to work hard to not repeat past mistakes by ensuring that the benefits
are not limited to some groups of people and other challenges are minimized.

Bi s hop, B. (2009). The Big Sort: Why the Clustering of Like-Minded America Is Tearing Us Apart. Ma ri ner Books.
Ca i rncross, F. (2001). The Death of Distance: How the Communications Revolution Is Changing our Lives. Ha rva rd Business Review Press.
Ga rreau, J. (1991). Edge City: Life on the New Frontier. Doubleday.
Greenstein, S., et al. (2018). How Geography Shapes—and Is Shaped by—the Internet. The New Oxford Handbook of Economic Geography. G.L. Cl ark, M.P. Feldman, M.S. Gertler, and D. Wójcik, eds.
Ra mani, A. & Bl oom, N. (2021). The Donut Effect of Covi d-19 on Ci ties. National Bureau of Economic Research Working Paper Series, 28876.

75

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Interest in innovation sector jobs is spreading geographically
Cities with less of a historical tech presence are seeing growth in hires and interest.
•

In 2005-2017, 90% of US innovation sector (highest-tech, highest-R&D ‘advanced’ industries) job growth was
in 5 cities: Seattle, Boston, San Francisco, San Diego, and San Jose (Atkinson et al. 2019).
•

As a result, the gap in wages between top earning metros and others increased.

•

By 2017 “One-third of the nation’s innovation jobs resided in just 16 counties, and more than half are
concentrated in 41 counties.”

•

More recently, LinkedIn data shows areas like Miami, FL (+17%), Jacksonville, FL (+14%), and Tampa, FL
(+10%), emerged as the biggest gainers of talent inflows, while San Francisco, CA (-15%), Portland, OR (13%), and Seattle, WA (-11.7%) saw the greatest outflows of workers (Kimbrough 2022).

•

Since 2020, interest in U.S. innovation sector jobs (technology, science, engineering) has grown everywhere,
especially in rural counties, shrinking the urban/rural gap (Counts 2022; Chancellor & Counts 2018 for
method).
•
Huge spike in interest as reflected by job searches on Bing – years of growth in just a few months (see
graph).

•

•

The spike precedes a late 2020 labor-market rebound.

•

Interest in innovation sector jobs has also become more evenly distributed across U.S. counties.

The new NSF directorate on Technology, Innovation, and Partnerships may contribute to this trend with its
goal of “tapping into the full breadth of the nation's demography and geography” (National Science
Foundation 2022).

Atkinson, R. D., et al. (2019). The case for growth centers: How to spread tech innovation across America. Brookings.
Microsoft Study: Chancellor, S. & Counts, S. (2018). Measuring Employment Demand Using Internet Search Data. ACM Conference on Human Factors
in Computing Systems (CHI).
Microsoft Study: Counts, S. (2022). Pandemic Job Search Trends. [Internal]
Microsoft Study: Kimbrough, K. (2022). The Great Reshuffle in 2022: Top Trends to Watch. LinkedIn.
National Science Foundation (2022). Meet TIP – Technology, Innovation and Partnerships.

Counts (2022)

76

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Interest in digital economy jobs broadly is also increasing
Years' worth of growth in interest happened in just a few months.
•

Similar to innovation sector work, job interest in all remotecapable digital economy employment sectors (innovation
sector + business, finance, art) in the U.S. spiked during the
onset of the pandemic.

•

Searches for digital economy jobs on Bing jumped by about
5% compared to before the pandemic, including sustained
growth following the initial pandemic shock (Counts 2022;
Chancellor & Counts 2018 for method).
• The interest surge was most pronounced for small
urban and rural areas.

•

LinkedIn reports a 5x increase in remote job postings, and
that people in cities across the Sun Belt in particular are
applying to remote jobs at a rate substantially higher than
the national average (Anders 2021).
Counts (2022)

Microsoft Study: Anders, G. (2021). “America's new remote-work havens: 20 cities that pursue faraway jobs. LinkedIn.
Microsoft Study: Chancellor, S., & Counts, S. (2018). Measuring Employment Demand Using Internet Search Data. ACM Conference on Human Factors in Computing Systems (CHI).
Microsoft Study: Counts, S. (2022). Pandemic Job Search Trends. [Internal]

77

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Those without broadband may be left out of geographic expansion of tech
Fast and reliable internet is not yet ubiquitous and not evenly spread around the U.S.
•

In a 2020 survey, only 65% of Americans reported having
fast enough internet to support video calls. The remaining
35 percent do not have sufficiently good home internet to
work from home (Bloom 2020).

•

In the U.S. 24% of rural adults say access to high-speed
internet is a major problem in their local community,
compared to 9% of suburban adults and 13% of urban
adults (Anderson 2018).

•

80% of white households have broadband access
compared to 71% of Black households and 65% of
Hispanic households (Pew 2020, see graph).

•

Because of broadband infrastructure inequalities already
present in the U.S. today, remote work policies could
disproportionately exclude Black, Hispanic, and rural
workers from entering the innovation sector.

•

Government agencies (e.g., USDA) and other organizations
(e.g., Microsoft’s Airband initiative) are working to expand
broadband access, with equity concerns a primary driver.

Anderson, M. (2018). About a quarter of rural Americans say access to high-speed internet is a major problem. Pew Research Center.
Bloom, N. (2020). Stanford research provides a snapshot of a new working-from-home economy. Stanford News.
Pew Research Center (2021). Internet/Broadband Fact Sheet.
Microsoft (2022). Airband Initiative.

Pew (2020)

78

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Only a minority of global jobs can be done remotely on a day-to-day basis
Remote work is not an option for many types of jobs such as frontline work among others.
•

Across countries, between 5% and 26% of workforce can work
remotely more than half the time without productivity loss
(Lund et al. 2020).

•

Globally, 80% of the workforce is “deskless.” It is difficult to do
these jobs remotely. Top 8 deskless industries: Agriculture,
Education, Healthcare, Retail, Hospitality, Manufacturing,
Transportation, and Construction, employing 2.7B employees
(Emergence 2018).

•

In the U.S. only 37% of jobs can be done remotely, far less in
countries with lower per capita GDP (Dingel & Neiman 2020).
• Even among high-GDP countries, the numbers vary
depending on the mix of industries and professions.

McKinsey Global Institute (2020)
Lund, S., et al. (2020). What’s next for remote work: An analysis of 2,000 tasks, 800 jobs, and nine countries. McKinsey Global Institute.
Emergence (2018). The Rise of the Deskless Workforce.
Dingel, J., & Neiman, B. (2020). How Many Jobs Can Be Done at Home? National Bureau of Economic Research Working Paper Series, 26948.

79

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

There was a shift in the types of gig jobs done during the pandemic
The gig economy as a whole did not grow during the pandemic, but there was an increase in the
number of people doing in-person gig work as opposed to online work.
• The gig economy showed only moderate, if any, growth during the pandemic. In the 12
months prior to August 2021, 9% of U.S. adults reported earning money in the gig economy
compared to 8% in the year before that and 8% in 2016. These numbers are within the margin
of error of each other (Pew 2021, 2016). So, the substantial job losses early in the pandemic
(April 2020) did not result in a large or sustained shift in the overall population of gig workers.
• By August 2021 unemployment had dropped to a low of 5.2% (BLS 2022), so it is
possible that people temporarily found gig work in April 2020 but returned to non-gig
work prior August 2020. They would not have been counted in the 9%.
• For example, Upwork had two spikes in worker registrations during the pandemic but
did not see sustained growth (Ozimek 2022).
• In 2021 and in 2016, 58% and 60%, respectively, of gig workers said the money they earn
was “essential” or “important” (Pew 2016, 2021).
• Between 2016 and 2021 there was a dramatic shift in the type of gig work done. In 2016 the
most common types of gig work were online tasks like surveys, data entry, etc. In contrast, in
2021 the most common types of gig work were in-person tasks like deliveries, shopping,
household tasks, and ride-hailing (Pew 2016, 2021).

Anderson, M. et al. (2021) The State of Gig Work in 2021. Pew Research Center.
Bureau of Labor Statistics, U.S. Department of Labor, (2021). Unemployment rate drops to 5.2 percent in August 2021. The Economics Daily,
Ozimek, A. (2022). Work Marketplaces and Dynamism. Upwork.
Smith, A. (2016). Gig Work, Online Selling and Home Sharing. Pew Research Center.

Smith (2016

Anderson et al (2021)

80

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The traditional location-based workplace was better for some than others
People of color and women are more likely to prefer remote work.
•

Studies have shown that compared to white men, people of color and women prefer remote work slightly more
(Subramanian et al. 2021).
o

In the United States, 86% of Hispanic and 81% of Black knowledge workers said they prefer remote work
preferred hybrid or remote work, compared to 75% of white knowledge workers.

o

Globally, 50% of working mothers said they preferred to work remotely, compared to 43% of fathers.

•

In a LinkedIn study, women (28%) reported flexibility in location as a driver for changing employer more often
than men (20%) (Anders 2022).

•

For these demographics, some have a sense that remote work means an opportunity to be judged more based
on their contribution, rather than their ability to “fit in” to prevailing office culture.
o

•

Since May 2021, a sense of belonging at work increased for 24% of Black knowledge workers, compared
to 5% of white knowledge workers (Future Forum 2022).

The emphasis hiring managers place on perceived "culture fit" can mean that some demographics are more
likely to be excluded from consideration because they don't match the existing model of an employee. Remote
work could mitigate this type of exclusion (Goldberg 2022).

Goldberg, E. (2022). A two-year, 50-million-person experiment in changing how we work. The New York Times.
Subramanian, S., & Gilbert, T. (2021). A new era of workplace inclusion: moving from retrofit to design. Future Forum.
Microsoft Study: Anders, G. (2022). What job hunters really want: 43% of women seek to cut workplace stress. LinkedIn Blog.
Future Forum Pulse (2022). futureforum.com/pulse-survey.

81

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Proximity bias could disproportionately impact people of color and working parents
Organizations need to actively combat the proximity biases observed pre-pandemic or they will
disadvantage certain groups of workers.
•

In Bloom et al.’s (2015) study of a call center, conditional on performance,
working from home caused 50% lower rates of promotion.
• Wider acceptance and adoption of remote work could potentially
mitigate this presence bias going forward.

•

For the reasons discussed on the previous slide, Hispanic, Asian and Black
knowledge workers in the US may spend less time in the office under
hybrid work than white knowledge workers.

•

75% of working parents prefer work remotely or hybrid, compared to
63% of non-parents (Future Forum 2022).

•

In the US, white knowledge workers are spending the most time in the
office by a significant margin – as great as 17 percentage points (Future
Forum 2022).

•

Forty-one percent of executives cite the potential for inequities to
develop between remote and in-office employees as their top concern
(Future Forum 2022).

Bloom, N., et al. (2015). Does Working from Home Work? Evidence from a Chinese Experiment. The Quarterly Journal of Economics 130(1), 165–218.
Future Forum (2022). Leveling the playing field in the hybrid workplace. Future Forum Pulse.

Future Forum (2022)

82

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Organizations are struggling to keep roles filled amid the Great Reshuffle
Both quit rates and hires have increased, though it varies by industry.

•

Trends and reasons vary by industry:

•

Industry data show marked employment decreases in the Food, Hospitality, Healthcare, and Education
sectors; increases in Transportation and Science sectors (BLS data, see bottom figure).

•

In the leisure industry the steep increase in quits was driven by people going directly to a new job, but in
manufacturing they were not (Birinci & Amburgey 2022).

•

A study of human service workers proposed high levels of emotional labor as a mechanism (Costakis et
al. 2021). Research on nurses (a group who might experience similar emotional burnout) found lack of
autonomy over schedules to be key (Bergman et al. 2021).

Bergman, A., et al. (2021). The Role of Schedule Volatility in Home Health Nursing Turnover. Medical Care Research and Review: 10775587211034310.
Birinci, S., & Amburgey, A. (2022). The Great Resignation vs. The Great Reallocation: Industry-Level Evidence. Economic Synopses 2022, 4.
Bureau of Labor Statistics. (2022a). Job Openings and Labor Turnover Summary - 2022 M01 Results.
Bureau of Labor Statistics (2022b) Current Employment and Earnings data.
Costakis, H. R., et al. (2021). Implications of Emotional Labor on Work Outcomes of Service Workers in Not-for-Profit Human Service Organizations. Human Service
Organizations: Management, Leadership & Governance 45(1), 29–48.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Parker, K., & Horowitz, J. (2022). Majority of workers who quit a job in 2021 cite low pay, no opportunities for advancement, feeling disrespected. Pew Research.

Job openings

Hires

Feb-22

Sep-21

Apr-21

Nov-20

Jun-20

Jan-20

Aug-19

Mar-19

Oct-18

May-18

Dec-17

Jul-17

Feb-17

However, in a Pew Research Center survey of Americans, the top 3 reasons for quitting a job in 2021 were low
pay (63%), no opportunities for advancement (63%) and feeling disrespected at work (57%) (Parker 2022).
(Differences could be due to the question phrasing or study recruitment, not necessarily a global / US
difference.)

Sep-16

•

Apr-16

Somewhat surprisingly, “not receiving promotions or raises I deserved” was number seven on the list at 19%.

Nov-15

•

Jun-15

Globally, the Microsoft WTI (2022) external survey found that the top five reasons employees quit were:
personal wellbeing or mental health (24%), work-life balance (24%), risk of getting COVID-19 (21%), lack of
confidence in senior management/leadership (21%), and lack of flexible work hours or location (21%).

•

18,000
16,000
14,000
12,000
10,000
8,000
6,000
4,000
2,000
0

Jan-15

In the US, a record 47.8 million people quit their jobs in 2021. However, hires increased as well, with 75.6 million
individuals finding new work (Bureau of Labor Statistics 2022).

•

Seasonally-adjusted nonfarm openings,
hires, and separations
Thousands

Separations

Graph based on data from BLS (2022b)

Graph based on data from BLS (2022b)

83

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Corporate impact on society is becoming more important to workers
Employees are placing increased importance on employers contributing to society.
•

•

In a global survey of approximately 3k English-speaking LinkedIn
members, females were more likely than males to report that it
has become more important to them that organizations
advocate for and make changes to support social justice issues
(40% vs 31%; p<.01), as well as regularly contribute (money or
products/services) to charities or causes (30% vs 26%; p<.05)
(Glint 2021).
In addition to energy poverty and broadband access, many more
social responsibility issues increasingly are aligned with
corporate goals.
• More than 300 companies have joined the Amazon Climate
Pledge, committing to net-zero carbon emissions by 2040
(Amazon 2022).
• 38% of 8,500 companies in the MSCI All Country World
Index are aligned with the United Nations Sustainable
Development Goals (World Economic Forum 2021).

Amazon (2022). The Climate Pledge.
Microsoft Study: Glint (2021). Expectations of Corporate Social Responsibility. Linkedin. [Internal]
Neufeld, D. (2021). UN Sustainable Development Goals: How Do Companies Stack Up? World Economic Forum.

Compared to one year ago, how important is it to you that a
potential employer do the following?
Never was
important

Less
important

Equally
important

More
important

Not sure

Gi ve back to the communities i n
whi ch it does business

5%

4%

51%

38%

3%

Del iver i ts products/services i n
envi ronmentally s ustainable ways

5%

3%

45%

45%

2%

Advoca te for a nd make changes to
s upport social justice i ssues

11%

6%

44%

33%

6%

Encoura ge community vol unteer
a cti vi ties for employees

10%

6%

50%

29%

4%

Regularly contribute
(money/products/services) to
cha ri table causes

10%

5%

54%

27%

4%

Glint (2021)

84

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Work is only one reason people live in cities
Remote work will permit some people to move away from their location of work, as we saw in 2020, but
other forces still push for urbanization.
•

There is a centuries-old worldwide trend towards urbanization despite the
invention of many groundbreaking communications technologies.

•

People move to cities for a variety of reasons. In the U.S. in 2000, only 1/3
of moves between counties were for job-related reasons. The rest are for
family, housing, amenities and other reasons (Schacter 2001).

•

The pandemic caused moves overall to decrease in 2020, but Haslag &
Weagley’s (2022) analysis of data from a major moving company (more
representative of upper-income and inter-state moves) find a decrease in
the share of moves that survey respondents report were for a job as well
as a few percentage point drop in the share of moves to urban areas.

•

In the short term, the 20% of jobs (Deskless Workforce 2018) that could
potentially be done remotely may affect the global trend towards
urbanization (see figure) slightly. But since most jobs cannot be done
remotely and people move to cities for reasons besides jobs, the overall
trend will likely continue.

Haslag, P. H., & Weagley, D. (2022). From L.A. to Boise: How Migration Has Changed During the COVID-19 Pandemic. Social Science Research Network, 3808326.
Ritchie, H., & Roser, M. (2018). Urbanization. Our World in Data.
Emergence (2018). The Rise of the Deskless Workforce.
Schacter, J. (2001). Why People Move: Exploring the March 2000 Current Population Survey. U.S. Census Bureau.

Ritchie & Roser (2018)

85

Forecast
Looking ahead: Challenges and
opportunities

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Work isn’t going to snap back to the way it was pre-pandemic
As workplaces open back up, the jobs that shifted to remote work during the pandemic are unlikely to
return to pre-pandemic practices. Instead, people and organizations will carry forward their learnings
from the past two years and develop new hybrid work practices that are fundamentally different.
• As restrictions lift, many companies have adjusted their policies to accommodate employee preferences (Barrero et al. 2021).
• During the pandemic people made decisions to accommodate an increase in remote work that will have long-term ramifications
on what in-person and hybrid work look like moving forward.
• Some organizations made decisions about office space that will make returning hard (e.g., giving up leases).
• Many employees made decisions that make it easier for them to work remotely (e.g., setting up home offices or purchasing
larger houses) and that will make it hard for them to return in the future (e.g., moving to remote locations).
• In Microsoft’s global Work Trend Index study, 47% of respondents say they are more likely to put family and personal life
over work than they were before the pandemic. And 53%—particularly parents (55%) and women (56%)—say they’re more
likely to prioritize their health and wellbeing over work than before (Microsoft WTI 2022).
• Future waves of Covid are likely to continue to disrupt work practices in a localized manner. For example, a surge of Omicron
infections has recently prompted lockdowns in China (Bradsher 2022).
• Given the scale of the disruption experienced during the pandemic, if work practices return to the way they used to be, it will
represent a failure to capture an opportunity to improve work.

Barrero, J. M., et al. (2021). Why Working from Home Will Stick. National Bureau of Economic Research Working Paper Series, 28731.
Bradsher, K. (2022). Surge of Omicron infections prompts lockdowns in China. The New York Times.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.

87

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

The future is uncertain and full of possibilities
All evidence in the social science literature suggests that it is very difficult to make very-high-confidence
predictions about the state of work even a few years from now. But forecasts can help us understand the wide
range of possible outcomes.
• As the saying goes, the “social sciences are the hard sciences”: work is the
outcome of (and input to) a huge variety of societal processes, each of which is
difficult to predict and is affected by all the others.

• Some societal processes that can dramatically change future of work outcomes
include: housing policy (e.g., cost of housing near offices), immigration law (e.g.,
can people work across borders more easily?), tax law (e.g., which jurisdiction
gets income taxes for remote work?), network effects that alter work location
preferences (e.g., if everyone is in the office, you might want to be there too),
and of course, the course of technological development.
• Highlighting uncertainty does not mean giving up. Organization leaders around
the world know how to handle situations like this: diversification. Now is likely
not the time for a single huge bet on the future of work – rather, it is a time for
experimentation and planning for a range of possible outcomes.
• Predictions can help us understand this range even if most predictions are highly
unlikely to manifest as stated. Some predictions are also implicit or explicit
attempts at self-fulfilling prophecies (Weyl 2022), for better or worse.
Cairncross, F. (2001). The death of distance : 2.0 ; how the communications revolution will change our lives (2nd ed.]. ed.). London: Texere.
Weyl, E. G. (2022). Sovereign Nonsense. RadicalxChange (blog).
Greenstein, S, et al. (2018). How Geography Shapes—and Is Shaped by—the Internet. In The New Oxford Handbook of Economic Geography.

In 2001, it was predicted that technology
would make distance / co-location irrelevant.
And yet, in the subsequent 20 years, it has only
become more relevant (Greenstein et al. 2018).

88

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

We will learn from an unprecedented level of experimentation in work models
We are likely entering the biggest period of experimentation in work models in decades. Some
companies will see a willingness to try new things as a differentiator in a tight labor market, others will
try for a productivity edge.
• In addition to many variations of remote / hybrid / onsite work, we expect to see
companies trying
o Alternative pay structures – expecting a certain output from employees
rather than a time spent working
o Remote work may accelerate transition to gig work
o Alternative organizational structures, perhaps similar to those that have
been used in the entertainment industry (Baym 2018)
• But, importantly, “trying new things” is not the same as true experimentation. To
learn as much as possible moving forward, companies should implement new
policies within the context of a scientific framework of experimentation and
learning.

(Weber, WSJ 2021)

(Albeck-Ripka, NYT 2022)

(Gelles, NYT 2021)

89
Microsoft Study: Baym, N. K. (2018). Playing to the Crowd: Musicians, Audiences, and the Intimate Work of Connection. 1st Edition. New York: NYU Press, 2018.

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

In the tech industry, forecasting is just the first step
Our job in the tech industry is not just to forecast the future of work but to create it. The tools we are
building right now will shape how our customers, our employees, and people around the world get
things done in the future.
•

The future of work is very difficult to predict given the number of
socioeconomic and sociotechnical variables involved. One great
way to predict the future of work with some accuracy is to create
it.

•

In the tech industry, we have more agency in shaping what the
future of work looks like than people in many other industries.
With this comes the responsibility to ensure that it is a better
future of work for all.

•

The next time someone asks, “What will the future of work look
like in {2025, 2030, etc.}?”, it might be more useful to ask, “What
should the future of work look like, and what do we need to do to
get there?”

•

Forecasts certainly have a great deal of value – they can help us
see the wide variety of potential outcomes – but they are just a
first step towards selecting and shaping outcomes for the better.

The capabilities of Teams and other hybrid work
experiences and devices could play a role in defining the
character of work for a generation.

90

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Remote and hybrid work increase the opportunity for AI to transform work
The pandemic significantly accelerated the digital transformation already underway at many companies,
and work-related data is now generated at an unprecedented pace. Combined with significant advances
in AI, this will drive a significant change in how people work.
• The rapid digital transformation of the past two years across a variety of industries enabled the capture
of training data at scale for a broad range of work. For example, the monthly use of meeting recordings
in Microsoft Stream more than doubled from March 2020 to February 2022 (Microsoft WTI 2022).

• AI is good at learning and scaling patterns, meaning for these activities people can instead focus on
doing things in new ways and generating novel ideas. For example, someone might:
• Write a document by merely listing the ideas it should include. The details can be fleshed out
automatically, much like developers use Copilot to flesh out ideas through code (Github 2022).
• Attend a meeting asynchronously by, before the meeting, asking the system to capture ideas on
their behalf to share at the meeting, and, after the meeting, hearing the responses people had to
those ideas in the meeting summarized by a large-scale language model (Tang 2012).
• Learn a new skill from an AI-based coach that increase their cognitive abilities and improves their
performance. E.g., Speaker Coach helps improve people's presentation skills (Microsoft 2021).

Github Copilot (2022)

• Uncertainty will be become a fundamental part of productivity systems, as correcting mistakes made by
AI and training AI models becomes an increasingly important part of how people get things done.
• Because AI systems will not just support work but change people’s work practices, they will need to be
designed in a way that is privacy-preserving, responsible, and equitable.
Scott, K. (2022). I Do Not Think It Means What You Think It Means: Artificial Intelligence, Cognitive Work & Scale. Journal of the American Academy of Arts & Sciences.
Github (2022). GitHub Copilot: Your AI pair programmer.
Microsoft (2021) Rehearse your slide show with Speaker Coach.
Microsoft Study: Microsoft WTI (2022). Great Expectations: Making Hybrid Work Work. Microsoft WorkLab: Work Trend Index 2022.
Microsoft Study: Samrose, S., et al. (2021). Meeting Coach: An intelligent dashboard for supporting effective and inclusive meetings. CHI 2021.
Microsoft Study: Tang, J., et al. (2012). Time Travel Proxy: Using Lightweight Video Recordings to Create Asynchronous, Interactive Meetings. CHI 2012.

Speaker Coach (2021)

91

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Guest Forecasts
To provide a broad range of perspectives, we asked leading external experts from relevant research
fields to forecast what the future of work might hold based on recent findings in their areas of
expertise. Forecasting the future of work is a very difficult task, and we are grateful to the below
experts for accepting this challenge to help us understand the range of possible outcomes:
•

Jeremy Bailenson (Stanford University)

•

Nale Lehmann-Willenbrock (Universität Hamburg)

•

Nathan Benaich (Air Street Capital)

•

Paul Leonardi (University of California, Santa Barbara)

•

Ethan Bernstein (Harvard Business School)

•

Gloria Mark (University of California, Irvine)

•

Michael Bernstein (Stanford University)

•

Alexandra Samuel (alexandrasamuel.com)

•

Nicholas Bloom (Stanford University)

•

Jane Shakespeare-Finch (Queensland University of Technology)

•

Tawanna Dillahunt (University of Michigan)

•

Willem Standaert (University of Liège)

•

Benjamin Laker (Henley Business School)

•

Melissa Valentine (Stanford University)

The guest forecasts reflect the contributors’ views of future scenarios, not those of Microsoft.
They are not legal analyses and are only a discussion of possible trends.
GUEST FORECAST

92

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Jeremy Bailenson (Stanford University)
The metaverse will mostly be for training and work
When you go through the history of VR, it’s all about training – starting with the Flight Simulator in
1929. This won’t change, given VR’s success training people, but rather will grow into more interactive,
collaborative immersive training.
• Current metaverse platforms are home to hundreds or sometimes thousands of
daily users, not millions. On the other hand, VR training is already touching
millions and that number will increase over the next 2-3 years.
• Workers will increasingly access their corporate training via the metaverse, and will
benefit from new capabilities within immersive training, such as learning in teams,
that will lead to a new wave of workforce skills.
• The metaverse comes with a set a difficult challenges around consumer data
privacy, security, and even climate change.

HBR article highlights specific case studies to
demonstrate why training is such a valuable use case for
VR and the metaverse.

Bailenson, J. (2020). Is VR the Future of Corporate Training? Harvard Business Review.

GUEST FORECAST

93

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Nathan Benaich (Air Street Capital)
Beyond programming, more general AI assistants could revolutionize work
OpenAI’s programming assistant Codex brought hope of making the life of millions of developers
easier. But future AI assistants will be much more general, and could revolutionize the workflows of
billions of users.
•

Google has been steadily adding new machine learning features to Google Workplace. Among
others: text completion and summarization on Google Docs, formula prediction on Sheets.

•

In other Google offices, DeepMind developed the AndroidEnv environment in 2021 where they
trained RL agents to perform various tasks such as setting alarm clocks, booking flights, playing
games, all while virtually swiping on a screen, clicking on icons, etc.

•

UiPath is already making incredible strides in task automation, but an AI-first approach could make
work assistants more generally capable.

•

Future work assistants will use their navigation agility at the operating system level in order to
perform tasks across different AI-powered apps/software. By mimicking human gestures and
workflows, assistants will be easier to interact with and instruct.

Hassan, H. (2019). Google Brings AI-powered Auto-Complete to Google Docs Thurrott.com
Saleh, M., et al. (2022). Auto-generated Summaries in Google Docs Google AI Blog.
Singh, R., et al. (2021). Predicting Spreadsheet Formulas from Semi-structured Contexts. Google AI Blog
Toyama, D., et al. (2021). AndroidEnv: A Reinforcement Learning Platform for Android. arXiv preprint, arXiv.2105.13231.

GUEST FORECAST

94

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Ethan Bernstein (Harvard Business School)
Talent, particularly elite talent, will continue to become more impatient
To remain competitive (as the Great Resignation – or Great Attraction—continues), organizations will
finally leave behind traditional, organization-centric approaches to succession in favor of new talent
development paradigms that are more human-centric.
Among other trends, this will manifest in the following ways:
• Ladders of progression will be replaced by individualized pathways that allow employees to make progress as they define it.
• Successful organizations will stop focusing on what an employee can be (e.g., a manager, a VP, etc.) and instead enable a path to what they want to do.
• That will put pressure on talent leaders to figure out how to appropriately recognize work and progress.
• Side hustles and side gigs will become even more mainstream, as demands for flexibility continue.
• Successful organizations will embrace employees’ side gigs as learning and experimentation environments that can complement the main gig; “On the Job Training” may
happen in side gigs with credit accruing to the main gig.

• The most forward-thinking companies may even restructure jobs to allow employees to turn their main gig for the organization into a side gig from time to time.
• Careers will become a patchwork of experiences (composed of distinct S-curves), and responsibility for piecing them together into a meaningful quilt will fall increasingly on
individuals rather than organizations.
• Successful organizations will provide more opportunities for employees to experiment and prototype more ‘unusual’ career moves.
• Demands for coaching and mentorship will continue to rise.
• Most employees will, at some point, have at least one fully virtual role.
• A Note of Caution: These opportunities are unlikely to be distributed evenly; without intervention, these trends are likely to amplify differences between office work and
front-line work; between white collar and blue collar work; between haves and have-nots.
Bernstein, E., et al. (Expected Spring 2024). Hire Your Next Job (Working Title). New York: Harper Collins.

GUEST FORECAST

95

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Michael Bernstein and Melissa Valentine (Stanford University)
Software will help support rapid organizations: OrgOS
As organizations make increasing numbers of data- and AI-driven decisions, the traditional organizational
designs that we use to support these decisions will become dynamic.
• Organizations are adapting their structures based on data: as customer data
surfaces patterns in behavior and needs, teams are getting dynamically assembled
and staffed. (Think: Netflix creating shows for the data-driven customer segments
that they identify.)
• These “rapid response” organizational changes are high velocity, as needs evolve:
teams grow and shrink, they shift goals, they adapt.
• In computing, operating systems translate high-level goals into low-level
implementation decisions. Imagine an organizational operating system, OrgOS,
that aids teams in navigating these rapid response challenges: helping with critical
basic building blocks (e.g., staffing teams) and tracking health (e.g., early warning
systems of team interpersonal issues).

Zhou, S., Valentine, M.,, & Bernstein, M. S. (2018). "In search of the dream team: Temporally constrained multi -armed bandits for identifying effective team structures." Proceedings of the 2018 CHI Conference on Human
Factors in Computing Systems.

GUEST FORECAST

96

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Nicholas Bloom (Stanford University)
Working from home will continue to grow as the technology improves
During the pandemic WFH has continued to grow as firms and employees adapt to this. Better
equipment and new technology will continue this growth of WFH over the next decades.
• The number of full WFH days will rise from 5% prepandemic in 2019 to 25% post-pandemic in 2023,
generating a 5x increase in the market for WFH
technology.
• This is driving increases in development of hardware and
software to support WFH as the market for these
technologies expands.
• So the next 20 years will involve impressive improvements
in WFH technologies like VR, holograms, and portable
compute.
• These technologies will radically improve WFH, just as
videocalls and cloud file-sharing did over the past 20
years.
Bloom, N., et al. (2021), COVID shifted patent applications toward technologies that support working from home. American Economic Association Papers and Proceedings
Barrero, J., et al. (2021), Why working from home will stick. National Bureau of Economic Research working paper series, 28731.

GUEST FORECAST

97

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Tawanna Dillahunt (University of Michigan)
Inclusive, accessible, and sustainable work environments must be imagined
In addition to supporting job seekers in navigating the existing labor market, we must seek alternatives
to support what work could look like
• New methods of technology development must center marginalized job
seekers and account for their unique situations, strengths, and everyday
resilience (Putnam et al. 2022; Lu et al. 2022).
• Future interventions must consider existing social and human infrastructures,
reinforce and amplify community-based mentorship and support, training,
skilling, and entrepreneurship (Dillahunt et al. 2022; Hui et al. 2020;
Ogbonnaya-Ogburu et al. 2019).
• Inclusive work environments will require accessible and nurturing
interventions to recruit, support, and retain talented marginalized employees
(Dillahunt et al. 2021).

Dillahunt, T. R., et al. (2022). The Village: Infrastructuring Community-Based Mentoring to Support Adults Experiencing Poverty. CHI 22 (to appear).
Dillahunt, T. R., et al. (2021). Implications for Supporting Marginalized Job Seekers: Lessons from Employment Centers. PACM 2021.
Hui, J., et al. (2020). Community Collectives: Low-tech Social Support for Digitally-Engaged Entrepreneurship. 2020. PACM 2020.
Lu, A., et al. (2022). Emotional Labor in Everyday Resilience: Class-Based Experiences of Navigating Unemployment Amid the COVID-19 Pandemic in the U.S. (minor revision to PACM 2022).
Ogbonnaya-Ogburu, I. F., et al. (2019). Towards an Effective Digital Literacy Intervention to Assist Returning Citizens with Job Search. 2019. CHI 2019.
Putnam, M., et al. (2022). New Directions in Employment and Training Research and Evaluation: Digital Employment Tools Created with Approaches from Human-Computer Interaction.

GUEST FORECAST

98

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Benjamin Laker (Henley Business School, University of Reading)
Workers will be willing to pay to avoid commuting
If the pandemic has taught us anything is that far more work can be done remotely than we previously thought. The
steep global rise in commuting costs and the willingness of employees who have grown accustomed to working
from home seek to cement the shift away from office working.
• Research from the U.K. and U.S. has shown perhaps the most significant impact of the
pandemic on working lives has been the shift in the amount of time spent working
from home and in shifting to flexible working options (Barrero et al. 2021).
Researchers have found that the most loathed aspect of working in the office is not
working in an office itself.
• A 2022 Henley Business School report shows workers are willing to sacrifice
compensation to work from home. The work suggests that about a quarter of
employees (27%) would be willing to take a salary reduction to work from home.
• This timely research illustrates the amount that workers are willing to give up is not
trivial, with employees being willing to forgo over $4,300 per annum to be able to
work from home full time. As costs rise, employers may be eager? Last year, Google
was reputed to have considered cashing in on employees’ willingness to pay to work
from home. So, how much are you willing to pay? It may not be that long until your
employer asks you (Henley Business School 2022).
Barrero, J. M., et al. (2022). “Why Working from Home Will Stick,” National Bureau of Economic Research Working Paper Series, 28731.
Henley Business School (2022). The four-day week: The pandemic and the evolution of flexible working. Henley Business School. White Paper.

GUEST FORECAST

Percentage of workers finding these
flexible working options attractive
80%

70%
60%

50%
40%

30%
20%
10%

0%
Being able to work Working for four days Working for four days
from home when you a week while being a week while being
need to
paid a full-time salary, paid a full-time salary,
with days worked
with days worked
chosen by the
being chosen you
employer

2021

2019

Data from Henley Business School (2022)

99

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Nale Lehmann-Willenbrock (Universität Hamburg)
Metaverse meetings will boost team dynamics and meeting effectiveness
As team members experience presence and entitativity when meeting in the metaverse,
the limited group dynamics of remote team meetings will be overcome
• Effective team meetings are important for team and organizational functioning.
• Entitativity, the feeling of groupness or being part of an actual group, is the prerequisite
for positive team meeting dynamics such as cohesion, mutual trust, and team flow.
Entitativity is typically limited in virtual meetings.
• Immersive meeting platforms with realistic avatars can overcome this by promoting a
sense of presence and provide a basis for experiencing entitativity in the metaverse.
• Based on enhanced entitativity, metaverse meetings will enable positive team dynamics
that are equal to F2F interactions, while allowing additional possibilities for
collaboration and inclusion.
Cross-Disciplinary Lab Computational Human
Dynamics (CHD) @Universität Hamburg
Blanchard, A. L., & McBride, A. (2020). Putting the “group” in group meetings: Entitativity in face-to-face and online meetings. In A. L. Meinecke, J. A. Allen, & N. Lehmann-Willenbrock (Eds.), Managing meetings in organizations
(pp. 71-92). Emerald.
Freiwald, J. P., et al. (2021). Effects of avatar appearance and locomotion on co-presence in virtual reality collaborations. In Mensch und Computer 2021 (pp. 393-401).
Lehmann-Willenbrock, et al. (2018). The critical importance of meetings to leader and organizational success: Evidence-based insights and implications for key stakeholders. Organizational Dynamics, 47(1), 32-36.
Steinicke, F., et al. (2020). A first pilot study to compare virtual group meetings using video conferences and (immersive) virtual reality. SUI '20: Symposium on Spatial User Interaction, October 2020, Article No.: 19.

GUEST FORECAST

100

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Paul Leonardi (University of California, Santa Barbara)
Relational analytics will begin to revolutionize HR and management practice

People analytics is growing. But the focus is typically on employees’ individual attributes. The best
predictors of performance and wellbeing don’t come from data about people themselves, but from the
structure of their relationships at work.
•

To date, people analytics has focused mostly on employee attribute data, of which there are two kinds:
(1) Trait: facts about individuals that don’t change, such as ethnicity, gender, and work history (2) State:
facts about individuals that do change, such as age, education level, company tenure, value of received
bonuses, commute distance, and days absent.

•

Decades of research show that the relationships employees have with one another—together with their
individual attributes—can better explain their workplace performance and wellbeing. The key is finding
structural signatures: patterns in the data that correlate to some form of good (or bad) performance or
wellbeing

•

The rich digital trace data that employees generate while working on and through digital platforms
provides social network data on actual working relationship that have been extremely difficult to
capture in the past, and have made relational analytics difficult to compute. The digital work revolution
has changed that.

•

Workplace leaders will need tools to analyze these data and use them to identify structural signatures
that can help them mentor employees and make key staffing decisions. Questions about privacy and
data ownership will loom large.

Example of Structural Signature computed from digital
trace data (Leonardi & Contractor 2018)

Cross, R., et al. (2018). “Collaboration Without Burnout,” Harvard Business Review 96(4), 134-137.
Leonardi, P., & Contractor, N. (2018). Better people analytics. Harvard Business Review, 96(6), 70-81.
Leonardi, P., & Neeley, T. (2022). The Digital Mindset: What It Really Takes to Thrive in the Age of Data, Algorithms, and AI. Boston: Harvard Business Review Press.

GUEST FORECAST

101

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Gloria Mark (University of California, Irvine)
New management practices and new awareness technologies will be needed
to handle challenges posed by WFH settings
WFH settings provide flexibility but present new challenges. Managers will develop new strategies to
manage emerging diversity and to increase motivation using integrative team management approaches.
New awareness technologies will be developed to increase visibility and sociability of coworkers in
remote settings, providing personalized and relevant information for supporting remote WFH teams.
Important challenges will be:
•

New types of diversity will become relevant: deeper-level diversity is emerging in WFH settings and will
become consequential for teamwork (Breideband et al. 2022). These types include differing home life
responsibilities which affect communication, coordination and performance. Different personal work
rhythms in WFH settings will require additional coordination to maintain team performance.

•

Work motivation will change. In WFH settings, there is less opportunity to draw on social interaction to
motivate work, through maintaining a positive work image to others and informal discussions of work
(Borghouts et al. 2022). Personalized approaches will be used to motivate workers (see figure).

Borghouts, J., et al. (2022). Motivated to Work or Working to Stay Motivated: A Diary and Interview Study on Working From Home. Proc. of the ACM Human-Computer Interaction., CSCW, 25 pages.
Breideband, T., et al. (2022). Home-life and work rhythm diversity in distributed teamwork: A study with information workers during the COVID-19 pandemic. Proc. of the ACM on Human-Computer Interaction, CSCW, 23 pages.

GUEST FORECAST

102

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Alexandra Samuel (alexandrasamuel.com)
Hybrid equity will be the key to a thriving organization
At least 50% of employees in industrialized countries are in jobs that can only be done on site. Bridging
the divide between on-site and hybrid employees is key to organizational cohesion, culture and
collaboration. Employers need strategies and tactics that foster hybrid equity.
•

Hybrid work opportunities are not distributed evenly: in the US, employees who are white, male, older and
higher educated are more likely to be in “teleworkable” jobs (Gezici & Ozay 2020)

•

In the majority of high-employment US industries, at least 1 in 5 jobs can be done remotely (Dingel & Neiman
2020) - which means most employers face a potential hybrid equity challenge.

•

The divide between remote-friendly and on-site work compounds obstacles to advancement in a labor market
that is already polarized between high- and low-skill workers (Chuang & Graham 2018).

•

For on-site workers, working with remote/hybrid colleagues can negatively affect work experience and
retention (Golden 2007).

•

Employers can prevent or address these resentments with strategies and tactics like transparency and flexibility
on work arrangements, and more sick time for on-site workers (Kelly & Shoemaker 2021).

Chuang, S., & Graham, C. (2018). Embracing the sobering reality of technological influences on jobs, employment and human resource development. European Journal of Training and Development, 42(7/8), 400-416.
Dingel, J., & Neiman, B. (2020). How many jobs can be done at home? Journal of Public Economics, 189, 104235.
Gezici, A., & Ozay, O. (2020). How Race and Gender Shape COVID-19 Unemployment Probability. Social Science Research Network, 3675022.
Golden, T. (2007). Co-workers who telework and the impact on those in the office: Understanding the implications of virtual work for co-worker satisfaction and turnover intentions. Human Relations, 60(11), 1641-1667.
Kelly, M., & Shoemaker, N. (2021). Telecommuting: Creating a Resentful On-Site Workforce. Journal of Organizational Psychology, 21(1), 11-15.

GUEST FORECAST

103

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Jane Shakespeare-Finch (Queensland University of Technology)
Employers will be pressured to provide comprehensive mental health care

Employers will be increasingly held accountable if they fail to provide proactive and reactive mental
health care to their employees.

• Mental ill-health in the workplace has costs beyond productivity. Psychological problems
impact not only individuals, but also their families, organizations and communities.
Psychological issues are also linked to physical problems such as cardiovascular and
respiratory diseases, drug and alcohol abuse disorders, and diabetes (Goetzel et al. 2018).
• Providing psychological education and support is not only a contributor to positive
workplace environment and economic productivity, and an ethical duty, but also a legal
requirement in many jurisdictions (Freckelton & Poppa 2018), especially in workplaces
where there is a foreseeable risk of psychiatric injury.
• Employers need to do more than react when it has already become evident that an
employee is psychologically unwell. Proactive mental health education and interventions
can prevent problems before they arise, building an environment of resilience, connection
and care (Foster et al. 2018; Shakespeare-Finch & Daley 2017), and improving
organizational culture overall.
Foster, K., et al. (2018). On PAR: A feasibility study of the Promoting Adult Resilience program with mental health nurses. International Journal of Mental Health Nursing, 27, 1470-1480.
Freckelton, I., & Popa, T. (2018) ‘Recognisable Psychiatric Injury’ and Tortious Compensability for Pure Mental Harm Claims in Negligen ce Saadati v Moorhead [2017] 1 SCR 543 (McLachlin CJ and Abella, Moldaver, Karakatsanis,
Wagner, Gascon, Côté, Brown and Rowe JJ), Psychiatry, Psychology and Law, 25(5), 641-652.
Goetzel, R. Z., et al. (2018). Mental Health in the Workplace. Journal of Occupational and Environmental Medicine, 60(4), 322-330.
Shakespeare-Finch, J., & Daley, E. (2017). Workplace Belongingness, Psychological Distress and Resilience in Emergency Service Workers. Psychological Trauma: Research, Theory Practice & Policy, 9, 32-35.

GUEST FORECAST

104

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Willem Standaert (University of Liège)
There will be adaptable virtual meeting technology for diverse disabilities
By designing virtual meetings for inclusion of people with (permanent) disabilities, many others can
benefit as they are faced with situational sensory constraints
•

Because of ubiquitous connectivity, participants can join meetings from anywhere. However, adaptable capabilities are
key for effective participation when facing temporal or situational disabilities (see picture).

•

Indeed, virtual meeting technology design choices have a significant impact on the experience and representation of
people with (permanent) disabilities (Tang 2021).

•

Through IoT sensors and artificial intelligence technologies, meeting technology will be able to automatically detect
such situations and adapt the offered communication capabilities in response.

•

For instance, while driving in a car, the shared screen is disabled from the car entertainment system, to avoid dangerous
distraction. But when the car is parked, this is automatically switched on. Likewise, noise coming from big trucks or from
kids in the backseat of the car will not be transmitted to other participants.

•

Other useful dynamic capabilities include switching from speech to text when in a noisy environment or zooming in on
particular areas of a shared screen when on a phone.

•

Moreover, additional information will need to be displayed to generate mutual situational awareness (e.g., add icon for
people unable to watch the screen, similar to the muted icon) (Gergle et al. 2013).

Gergle, D., et al. (2013). Using Visual Information for Grounding and Awareness in Collaborative Tasks. Human-Computer Interaction, 28(1), 1-39.
Microsoft Study: Microsoft Design (2016). Inclusive Toolkit.
Microsoft Study: Tang, J. (2021). Understanding the Telework Experience of People with Disabilities. Proc. ACM Hum.-Comput. Interact. 5, CSCW1, Article 30, 27 pages.

GUEST FORECAST

Microsoft Design – Inclusive Toolkit
(2016)

105

Appendix

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Glossary
API: Application Programming Interface – a programming interface that allows two computers or pieces of software to communicate.
Asynchronous/Async communication: Communication between members of a team that does not happen " in real time."
Augmented Reality (AR): Technology that supplements reality, by integrating 3-D objects into the user's real environment (Azuma 1997).

Avatar: An icon or image meant to represent a particular person within a computer-mediated environment.
Chat: In this report, this refers to messaging via Microsoft Teams or similar applications where people type text-based messages to each other.
“Parallel chat” refers to the chat stream that appears during meetings.
Cognitive Science: The study of thought, learning, and mental organization.

Collegiality: Companionship and cooperation between colleagues.
Deepfakes: AI-generated, realistic-appearing representations of people, created using image, video, and/or voice samples (Westerland 2019).
Design fiction: Explorations of speculative scenarios that are expressed in design artifacts such as images and objects.

Gig work: Contract work that is short-term, without benefits, and often mediated through a platform, like Uber or Upwork (Bajwa et al. 2018).
Hybrid Work: Refers to a mix of co-located (in office or facility) and non-co-located work or workers, see What is hybrid?
Inclusion: Fostering a welcoming, empowering environment for all employees. (Microsoft 2021).

Azuma, R. T. (1997). A Survey of Augmented Reality. Presence: Teleoperators and Virtual Environments, 6(4), 355–385.
Westerlund, M. (2019). The Emergence of Deepfake Technology: A Review. Technology Innovation Management Review, 9(11), 40–53.
Bajwa, U., et al. (2018). The health of workers in the global gig economy. Globalization and Health, 14(1), 124.
Microsoft Study: Microsoft. (2021). Diversity & Inclusion Report. Microsoft.

107

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Glossary
IoT: Internet of Things – refers to a web of everyday objects, connected by the Internet.
Onboarding: The process of integrating new hires into the organization.
Productivity: A measure of output divided by units of input (such as hours worked, number of workers or cost of labor). Output is hard to measure
in the case of intangible work products. Certain types of inputs (e.g., hours worked) may also be difficult to measure

Prosody: Patterns of voice stress and intonation.
Remote Work: Work that does not require an employee to commute to an office or workplace.
Social Capital: A resource created by the makeup and qualities of a social network, which can be utilized by both individual actors, like employees,
as well as collective ones, like a company (Adler & Kwon 2009).

Socio-tecture: A heavy reliance on social networks in which the relational is prioritized over the transactional, and people are viewed as the primary
source of knowledge (Awori et al. 2022).
Ties (Strong and Weak): A connection between two actors in a social network, the strength of which is determined by the amount of time, intimacy,
emotional intensity, and reciprocity of the relationship (Granovetter 1973).
Transitional Interfaces: Interfaces that enable seamless integration of systems along the reality to virtual reality continuum, depending on
users’ tasks and needs (Jetter et al. 2021).
Virtual Reality (VR): Technology that completely immerses the user in a virtual environment (Azuma 1997).
Workload: The work that an individual employee is responsible for at any given time.
Adler, P. S., & Kwon, S.-W. (2009). Social Capital: The Good, the Bad, and the Ugly. Knowledge and Social Capital: Foundations and Applications, Eric L. Lesser, ed., Butterworth-Heinemann, Boston, MA, pp. 89-115.
Granovetter, M.S., (1973). The strength of weak ties. American journal of sociology, 78(6), 1360-1380.
Jetter, H.-C., et al. (2021). Transitional Interfaces in Mixed and Cross-Reality: A new frontier? Interactive Surfaces and Spaces, 46–49.
Azuma, R. T. (1997). A Survey of Augmented Reality. Presence: Teleoperators and Virtual Environments, 6(4), 355–385.

108

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Limitations
This report draws on numerous different studies using diverse methodologies to identify phenomena
across a wide range of employees and organizations. However, the report does have its limitations: We
draw primarily on English language research, often focused on the United States. We also focus mostly
on information workers. The future of work undoubtedly includes a wider range of workers than those
addressed in depth here, including frontline workers, freelancers, contractors, gig workers, creative
workers, agricultural workers, and more. We hope that this report provides useful insights or
counterpoints to those seeking to understand these and other dimensions of the future of work.
Ultimately, the future of work is yet to be determined. Technologies, practices, and norms are rapidly
evolving. We hope this report helps nurture a better future of work, one in which all kinds of workers in
all places can thrive.

109

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

This is the second annual New Future of Work Report
This report builds on the first annual New Future of Work report, which summarized research from the
peak of the pandemic-driven work-from-home period and remains a valuable resource for us here at
Microsoft. This year, inspired by the State of AI Report (https://stateof.ai), we decided to use a slide deck
format. Our hope is that this will make it easy to skim through the significant body of new research and
focus on what interests you most, as well as support the sharing of self-contained, bite-sized findings.

https://aka.ms/nfw2021

https://aka.ms/nfw2022
110

Introduction Individuals Teams Organizations Society Forecast

#newfutureofwork

Acknowledgements
•

The format was inspired by the State of AI (http://stateof.ai) report by Nathan Benaich and Ian Hogarth. Thanks especially to
Nathan Benaich for taking the time to walk us through the advantages and disadvantages of the slide deck as a genre for
research synthesis.

•

Thank you to our guest forecasters Jeremy Bailenson (Stanford University), Nathan Benaich (Air Street Capital), Ethan Bernstein
(Harvard Business School), Michael Bernstein (Stanford University), Nicholas Bloom (Stanford University), Tawanna Dillahunt
(University of Michigan), Benjamin Laker (Henley Business School) Nale Lehmann-Willenbrock (Universität Hamburg), Paul
Leonardi (Northwestern University), Gloria Mark (University of California, Irvine), Alexandra Samuel (alexandrasamuel.com),
Jane Shakespeare-Finch (Queensland University of Technology), Willem Standaert (University of Liège), and Melissa Valentine
(Stanford University).

•

Thank you to our external reviewers Ethan Bernstein (Harvard Business School), Gloria Mark (University of California, Irvine),
Judith Olson (University of California, Irvine), Alexandra Samuel (alexandrasamuel.com), Jane Shakespeare-Finch (Queensland
University of Technology), and Willem Standaert (University of Liège).

•

Thank you also to Ethan Mollick (Wharton) for capturing so much relevant research in his Twitter feed, as well as Tammy D.
Allen (University of South Florida), Timothy D. Golden (Rensselaer Polytechnic Institute), and Kristen M. Shockley (University of
Georgia) for synthesizing so much of the pre-pandemic social science research on remote and hybrid work in their 2015 survey
paper “How Effective Is Telecommuting? Assessing the Status of Our Scientific Findings”.

•

This report was a company-wide effort. In addition to our authors and contributors already listed, we are grateful for the help
and support we received from the broader Microsoft team. This was truly a One Microsoft effort!

111
