---
title: "The New Future of Work: Research from Microsoft into the Pandemic’s Impact on Work Practices"
person: brent-hecht
attendance: unconfirmed
section: by
type: journal-article
year: 2021
date: 2021-01-25
venue: "Microsoft technical report (1st ed., 2021), eds. J. Teevan, B. Hecht, S. Jaffe"
authors: "Jaime Teevan, Brent Hecht, Sonia Jaffe, Nancy K. Baym, rachel-bergmann, Matt Brodsky, Bill Buxton, Jenna Butler, Adam Coleman, Mary Czerwinski, Brian Houck, Ginger Hudson, Shamsi T. Iqbal, Chandra Maddila, Kate Nowak, Emily Peloquin, Ricardo Reyna Fernandez, Sean Rintel, Abigail Sellen, Tiffany J. Smith, margaret-anne-storey, Siddharth Suri, Hana Wolf, Longqi Yang"
source_url: https://www.microsoft.com/en-us/research/publication/the-new-future-of-work-research-from-microsoft-into-the-pandemics-impact-on-work-practices/
fulltext_url: https://www.microsoft.com/en-us/research/wp-content/uploads/2021/01/NewFutureOfWorkReport.pdf
openalex_id: W3126823042
oa_status: closed
cited_by_count: 24
retrieved: 2026-08-13
content: full-text
notes: "Full text of the Microsoft technical report PDF (pdftotext; PDF not stored); edited volume of Microsoft Research findings; Hecht is a co-editor/co-author"
---

# The New Future of Work: Research from Microsoft into the Pandemic’s Impact on Work Practices

## Full text

The New Future of Work
Research from Microsoft into the Pandemic’s Impact on Work Practices
The coronavirus pandemic not only caused a public health crisis, it also caused
technological, social, and cultural disruption. This past year, people across the globe
experienced a rapid shift to remote work that upended their existing practices and will
have long-term implications for how work gets done in the future. Looking forward,
we expect that some of those who used to work from offices will continue to work
remotely, while others will adopt hybrid models that will involve a combination of
working from the office and working remotely. The current moment presents a unique
opportunity to understand the nature of work itself, to improve remote support for a
range of work practices, and to use what we have learned through remote work to
improve in-office and hybrid practices.
As a company whose mission is to empower every person and every organization on
the planet to achieve more, it is vital that Microsoft understands the massive transition
currently underway so that we can help our customers come through this challenging
time stronger and more resilient. We are all right now participants in a giant, natural,
uncontrolled remote work experiment from which Microsoft must learn. Just as
research has been fundamental in developing ways to prevent and treat COVID-19, it
is also fundamental to understanding and supporting evolving the sociotechnical work
practices.
At the start of the pandemic, researchers from across Microsoft formed an ongoing
cross-company initiative to coordinate efforts with the goal of understanding the
impact of remote work and identifying opportunities to support new working
practices. The initiative consists of over 50 research projects conducted by teams that
span a range of disciplines (including engineering, research, marketing, human
resources, and facilities) and divisions (including Microsoft Research, Office,
Windows, Azure, Xbox, GitHub, and LinkedIn). The projects employ many different
methodologies, ranging from small-scale, formative interviews with customers to
large-scale modeling exercises and even EEG measurements of electrical impulses in
the brain.
This report provides a synthesis of the findings from these many research projects.
We believe it represents the largest compilation of research related to the pandemic’s
impact on work practices available to date. The findings highlight a number of acute
challenges and suggest opportunities to develop new work practices that are more
efficient, equitable, and energizing. Work will never again be the same. With care and
effort, however, we hope to make it better.
Jaime Teevan (Chief Scientist, Experiences and Devices)

TABLE OF CONTENTS
Introduction .................................................................................................................................................................5
1 Collaboration and Meetings.....................................................................................................................................7
1.1 Introduction .........................................................................................................................................................7
1.2 Impact on Working Patterns and the Nature of Collaboration ...........................................................................7
1.2.1 The shift to remote work increased meeting and IM loads, while stretching workdays. ............................. 7
1.2.2 The move to remote work was particularly hard on some kinds of collaboration, such as creative work,
“thinking big,” and decision-making. ...................................................................................................................8
1.2.3 Informal and spontaneous interaction particularly suffered in remote work, affecting collaboration. .........9
1.3 The Impact of Remote Meetings ........................................................................................................................ 10
1.3.1 Video conferences are fatiguing................................................................................................................. 10
1.3.2 Fatigue was also increased by meeting load and the challenges of coordinating meeting tools. ............... 10
1.3.3 Interaction in remote meetings is challenging in ways that are fundamentally different from in-person
meetings. ............................................................................................................................................................. 11
1.3.4 The use of video in meetings is both a personal and group affair. ............................................................. 12
1.3.5 Parallel chat became a pervasive component of meetings. ........................................................................ 13
1.4 Inclusion and Forming Connections ................................................................................................................. 13
1.4.1 Remote work affected inclusion both negatively and positively. ............................................................... 13
1.4.2 Many people not only maintained their existing networks post-COVID but made new connections. ....... 14
1.5 Looking Forward............................................................................................................................................... 15
1.5.1 People are creative and resilient, and are developing new work practices to adapt to a changing world. . 15
1.5.2 The best hybrid future will retain many new work practices and focus on flexibility. .............................. 16
2 Personal Productivity and Well-being .................................................................................................................. 18
2.1 Introduction ....................................................................................................................................................... 18
2.2 Productivity, Satisfaction, and Work Patterns .................................................................................................. 18
2.2.1 On average, self-reported productivity was unchanged, but it varied with role and experience. ............... 18
2.2.2 While some reported satisfaction with remote work, it varied with organization, role, and experience. ... 19
2.2.3 Average workdays got longer during COVID. .......................................................................................... 19
2.2.4 Some, but not all, employees with children struggled with childcare. ....................................................... 20
2.2.5 Managers appeared to be especially hard hit. ............................................................................................ 20
2.2.6 The effect of remote work differed across roles and individual characteristics. ........................................ 21
2.3 Challenges and Benefits Are Closely Linked ..................................................................................................... 22
2.3.1 Remote work provided flexibility during the pandemic while also blurring the work-life boundary in
problematic ways. ............................................................................................................................................... 22
2.3.2 Non-work distractions increased, whereas work-related distractions decreased for many. ....................... 22
2.3.3 Many workers felt collaboratively and socially isolated. ........................................................................... 23
2.3.4 Remote work provided some benefits for worker health, but also many challenges, particularly with
regard to well-being. ........................................................................................................................................... 24
2.3.5 Employees worried that their hard work would not be visible to their managers. ..................................... 25
2.3.6 Conversely, there was increased concern about how their work did show up. .......................................... 25
2.4 Looking Forward............................................................................................................................................... 25
2.4.1 Roles of managers and leaders are evolving to adapt the challenges of remote work. .............................. 25
2.4.2 Where to work once it is safe? Workers report mixed preferences but lean toward a hybrid model. ........ 26
2.4.3 Business decision-makers are considering long-term changes. ................................................................. 27
2

3 Software Engineering Experiences ........................................................................................................................ 28
3.1 Introduction ....................................................................................................................................................... 28
3.2 Productivity, Satisfaction, and Work Patterns .................................................................................................. 28
3.2.1 Engineering output measures were stable or showed an increase when moving to remote work. ............. 28
3.2.2 Self-reported productivity suggests a more mixed picture than developer activity metrics. ...................... 29
3.2.3 The increased engineering output seems to have come with increased burnout. ....................................... 30
3.2.4 Collaboration output measures were healthy, but engineers who experienced collaboration challenges
reported lower personal productivity and lower team productivity. ................................................................... 31
3.2.5 Onboarding software engineers during COVID-19 presented new challenges. ......................................... 31
3.3 Challenges and Benefits Are Closely Linked ..................................................................................................... 32
3.3.1 While engineers adapted to remote work and many found they could focus better, they also felt the lack
of in-person interactions hindered their creativity. ............................................................................................. 32
3.3.2 Software engineers felt gratitude for their team and empathy for remote work. ........................................ 33
3.3.3 Two sides to the same coin: some factors that some engineers saw as a benefit, others saw as a challenge.
............................................................................................................................................................................ 33
3.4 Looking Forward............................................................................................................................................... 33
4 IT and Security ....................................................................................................................................................... 34
4.1 Introduction ....................................................................................................................................................... 34
4.2 IT & Security Organizations Experienced a Major Shift to Remote Work ........................................................ 34
4.2.1 The vast majority of Microsoft’s commercial customers encouraged their IT and security organizations to
work from home.................................................................................................................................................. 34
4.2.2 A large portion of Microsoft’s enterprise customers were able to adopt remote work environments during
the COVID-19 crisis. .......................................................................................................................................... 34
4.3 New Security and Compliance Risks ................................................................................................................. 34
4.3.1 Security threats increased, with phishing attacks experiencing the largest increase. ................................. 34
4.3.2 Increased remote work surfaced several security-related gaps that increased organizational compliance
risks. .................................................................................................................................................................... 35
4.4 Specific IT challenges........................................................................................................................................ 35
4.4.1 Poor internet performance and not having the appropriate equipment were major problems for the
commercial workforces while working remotely................................................................................................ 35
4.4.2 Adequately educating end users about best practices for working remotely and training them to
effectively use remote tools emerged as some of the most prevalent problems for IT admins, security
professionals, and compliance IT specialists. ..................................................................................................... 35
4.4.3 IT admins struggled to provide adequate support to their end users. ......................................................... 36
4.5 Looking Forward............................................................................................................................................... 36
4.5.1 IT and the tools they provide have increased in importance for decision makers. ..................................... 36
4.5.2 Some organizations may be able to avoid layoffs by modernizing their IT infrastructure to facilitate
remote work. ....................................................................................................................................................... 37
5 Devices and Physical Ecosystems .......................................................................................................................... 38
5.1 Introduction ....................................................................................................................................................... 38
5.2 Challenges for Home Offices ............................................................................................................................ 38
5.2.1 The rapid shift to remote work left little to no time to consider the implications of workers’ physical
environments. ...................................................................................................................................................... 38
5.2.2 Many information workers struggled to find a workspace that was comfortable and distraction free. ...... 38
5.2.3 Working from home in make-shift offices highlighted the importance of ergonomics. ............................ 40
3

5.2.4 Many people dealt with connectivity challenges when working from home (e.g., Wifi, VPN). ............... 41
5.3 Evolving Use of Devices .................................................................................................................................... 41
5.3.1 More online meetings while working from home led to new behaviors related to device use. ................. 41
5.3.2 The increased frequency of remote meetings with video placed greater importance on cameras. ............. 42
5.3.3 People spent more time on screens while stuck at home, most notably on their mobile phones. .............. 43
5.4 Looking Forward............................................................................................................................................... 43
5.4.1 Company leaders are seeking tools that enable flexibility and productivity in a world where remote work
is the norm. ......................................................................................................................................................... 43
5.4.2 Decision-makers are navigating a complex set of challenges related to planning the return to work. ....... 44
5.4.3 Companies are faced with making new hybrid work policies and workplace modifications to ensure a
safe environment and instill confidence with employees. ................................................................................... 44
5.4.4 Many companies and schools are experimenting with and planning for more outdoor spaces and other
reimagined gathering spaces. .............................................................................................................................. 45
6 Societal Implications............................................................................................................................................... 46
6.1 Introduction ....................................................................................................................................................... 46
6.2 Widespread Trends ............................................................................................................................................ 46
6.2.1 The shift toward remote work has accelerated. .......................................................................................... 46
6.2.2 A more distributed workforce will impact the communities where workers live. ..................................... 47
6.2.3 There is a need to mitigate pervasive social deficits and societal burnout. ................................................ 47
6.2.4 Weak ties are growing scarcer. .................................................................................................................. 47
6.3 Impacts on Businesses ....................................................................................................................................... 48
6.3.1 Long-term decisions are being made based on short-term data. ................................................................ 48
6.3.2 There are innovation risks related to remote work. .................................................................................... 49
6.3.3 Small and medium businesses are embracing freelance labor. .................................................................. 49
6.3.4 Well-being is an emerging professional priority. ....................................................................................... 50
6.3.5 Remote work highlights discussions around electronic performance monitoring...................................... 50
6.4 Growth of Systemic Inequalities ........................................................................................................................ 50
6.4.1 Remote work can be a source of structural inequality. .............................................................................. 50
6.4.2 There has been uneven impact of layoffs due to COVID-19. .................................................................... 51
6.4.3 There are structural inequalities in the risks of returning to the workplace. .............................................. 51
6.4.4 Inequalities in at-home learning environments may impact the future makeup of the information
workforce. ........................................................................................................................................................... 52
6.4.5 Gender and caregiving imbalances create risks to the labor market. ......................................................... 52
6.4.6 There is an increased risk of job loss for professionals with disabilities. .................................................. 53
6.4.7 As video proliferates, professionals with disabilities face increased pressure to disclose. ........................ 53
6.5 Looking Forward............................................................................................................................................... 54
Acknowledgements and Attribution ........................................................................................................................ 55
BIBLIOGRAPHY ...................................................................................................................................................... 57

4

INTRODUCTION
By Jaime Teevan, Brent Hecht, and Sonia Jaffe
This report presents a synthesis of the research done at Microsoft to understand the impact of the COVID-19
pandemic on work practices. It focuses on information workers – people who do non-routine cognitive work
creating, manipulating, or analyzing information – including software engineers, architects, engineers, designers,
accountants, administrators, lawyers, and marketers, among many others. Over 40% of the US workforce is
comprised of information workers [43] and the segment has more than doubled in the past 30 years [183]. The
COVID-19 pandemic impacted different people's work practices in different ways. Some continued to commute to a
workplace as essential workers, others were unable to continue working as restrictions were put into place to
manage the pandemic, and over a third transitioned to some form of remote work [25]. Much of this last category is
comprised of information workers, and the significant shift that these workers experienced resulted in many changes
to their individual work practices, their collaborative practices, the way their organizations functioned, and society at
large.
To capture this shift, this report pulls together the findings from over 50 different research studies conducted across
Microsoft since the pandemic began, and supplements those findings with recent research from the academic
community, including, for example, the studies shared at the virtual symposium on the New Future of Work
(http://aka.ms/nfw2020) that Microsoft hosted in August 2020. It also draws on the 30+ years of existing research
into remote work that has come out of Microsoft Research [164] and the academic community prior to the
pandemic. We believe this report is the most comprehensive summary on this topic to date.
Given Microsoft is focused on supporting work, the company already had, pre-pandemic, a number of rich signals in
place with which to conduct research into COVID-19’s impact on work practices. The research in this report
benefits from these signals in accordance with the extensive work that has been done to ensure they uphold
Microsoft’s rigorous privacy standards (see http://privacy.microsoft.com for more). The signals are drawn from the
existing qualitative channels that we use to understand our customers and our employees through surveys,
interviews, and focus groups, quantitative channels based on de-identified telemetry data, and a particularly in-depth
view into several specific information worker segments such as software engineers and IT admins.
When information workers around the globe shifted to remote work in early 2020, teams across the company
responded quickly to make use of these existing channels to understand what was happening, as well as to develop
new channels. Novel research was conducted by a variety of teams spanning a range of disciplines – including
engineering, research, marketing, human resources, and facilities – and divisions – including Microsoft Research,
Office, Windows, Azure, Xbox, GitHub, and LinkedIn. These teams came together in a massive cross-company
initiative to share research questions and findings. While each team approached their research with its own unique
methodologies, objectives, and research philosophies, by working together they were able to build on the work done
by others and create a rich shared picture that has driven significant impact around the company.
Across the various different studies that the teams conducted, there were a range of populations studied, from
information workers broadly to specific studies of engineers, business decision makers, data scientists, IT admins,

Count

%

Internal MSFT

18

40%

External

21

47%

Both

6

13%

Figure 1: An overview of the populations studied as part of the research included in this report.

5

Count

%

Quantitative

11

24%

Qualitative

15

33%

Both

19

42%

Figure 2: Methodologies employed by the studies included in this report.

and program managers, with some studies actively looking at differences across these populations. The specific
breakdown of 45 studies in the initiative can be seen in Figure 1. About half sought to understand internal Microsoft
populations, and half external populations. Microsoft is a global company, and the pandemic has had a global
impact, so studies looked at populations from around the world.
The studies also used a range of methods, from analysis of large-scale telemetry to surveys to in-depth interviews,
even including EEG measurements of electrical impulses in the brain. These are shown for 45 studies in the
initiative in Figure 2. About half employed qualitative methods, and half quantitative. These different approaches
make it easier to understand both what is happening and why. For example, a study based on telemetry data
suggested people’s output remained high as they moved to remote work, but another study based on survey data
showed that this was in part because some people were employing unsustainable work practices.
Some of the research included in this report has begun to appear in top-tier scientific publication venues. These
publicly available, peer-reviewed articles are included in the bibliography and serve as good resources if you would
like additional details beyond what is covered here. We expect more publications to become available in the coming
months; keep an eye on http://aka.ms/newfutureofwork for the most up-to-date list. Other research projects included
in this report were designed primarily for internal consumption, creating limits on how much detail can be shared
publicly. These are flagged in the bibliography as “Microsoft (internal)”; contact newfutureofwork@microsoft.com
if you are interested in learning more about that work.
A lot has happened this past year. Early in the pandemic, people’s work practices changed rapidly as the world
around them shifted. Later people began to adapt to their new working lives. In some parts of the world, people are
even starting to transition to hybrid work as workplaces open back up. This report includes research from each of
these stages, and while each individual study provides an important piece of the puzzle, it is only by looking at them
all together, with the range of populations they studied and methodologies they employed, that we can start to see
the big picture.
The findings are organized into six chapters: 1) Collaboration and Meetings; 2) Personal Productivity and Wellbeing; 3) Software Engineering Experiences; 4) IT and Security; 5) Devices and Physical Ecosystems; and 6)
Societal Implications.

6

1 COLLABORATION AND MEETINGS
By Nancy Baym, Rachel Bergmann, Adam Coleman, Ricardo Reyna Fernandez, Sean Rintel, Abigail Sellen, and
Tiffany Smith
1.1 Introduction
Perhaps the most obvious change that information workers experienced when moving to remote work as a result of
COVID-19 was that the meetings they had previously attended in-person shifted to being remote, resulting in many
new kinds of ‘meetings’ and other collaborative practices that attempted to make up for the loss of the full range of
social interaction people had previously relied on at work. Thus, we begin by looking at the way collaboration and
meeting practices evolved over the course of the pandemic. In addition to how meetings and other forms of
collaboration have changed, we also discuss how remote work affected inclusion and the collaborative connections
people form, and what changes people hope or expect will continue post-COVID.
1.2 Impact on Working Patterns and the Nature of Collaboration
1.2.1 The shift to remote work increased meeting and IM loads, while stretching workdays.
An ordinary day at a physical workplace includes a mix of pre-planned and spontaneous interaction that supports
collaboration, productivity, and connection. With the move to remote work, both task-focused and informal
communication moved to online platforms. Results from many studies, both of Microsoft employees and
information workers external to the company, show that people had a higher meeting load during the pandemic than
they did pre-COVID. In one survey of over a hundred information workers across a variety of industries, 57% said
their meeting load had increased [160]. In an internal company-wide survey, more than half of respondents reported
more meeting time [128]. Relatedly, a study of the working patterns of Microsoft China employees found that voice
and video calls doubled from 7 to 14 hours a week after the transition to remote working [131]. Other studies
suggest that scheduled meetings were also running longer. One internal study found that meetings were less likely to
end on time, due in part to the lack of physical reminders that a meeting was done (e.g., the next group walking into
your conference room, people shuffling papers, people standing up, etc.) [26]. Increased meeting load may not be
special to the conditions of the pandemic: a study of 800 employees in a Microsoft subsidiary in the Netherlands,
who underwent a 10 week remote working experience in 2018, found a 10% increase in meeting time [149].
Internal studies show that people were also holding more short meetings, those lasting 30 minutes or less, such as
quick check-ins and 1:1s with team members and managers [26,91,138,163]. Analysis of telemetry data from the
Modern Workplace Transformation team [91] found that 1:1s increased by 18%, and check-ins and team social
meetings grew by 10% – half of these new meetings were recurring. Further telemetry data from Microsoft US
employees show unscheduled calls in Teams more than doubled [182].
Instant message (IM) chats also substantially increased during this period of remote working [91,130,181]. Studies
show IM traffic increased for different Microsoft teams by 65% to 72% [91,130], this being most dramatic amongst
managers, with a 115% increase from pre-COVID figures. This finding is buttressed by an external study of
information workers across a range of industries, where quick one-off and in-person conversations were being
replaced with instant messaging via Teams, G-Chat and Slack [160].
All these meetings and messages were spread out over a longer workday. Research with one Microsoft team in the
US found that the share of IMs sent between 6 pm and midnight increased by 52%, and that people who previously
did not work much on weekends saw their weekend collaboration triple [66]. One participant in this study suggested
that flexible working hours contribute to the problem: “If a colleague working flex hours sends a message at 9 pm, I
feel like I need to respond.” It appears that working outside of normal working hours results in more IMs being sent,
but also that sending (and others’ receiving) IMs can result in people working at unusual times of the day [66].
These changes in meeting hours differ depending on role, whether one is a manager, and how experienced one is in
remote work. For example, Workplace Analytics data comparing metrics pre and post pandemic show that people in
marketing, IT, sales, and program manager roles experienced a larger increase in collaboration time (as measured by
amount of meetings, email and message time) than data center workers, applied scientists, software engineers and
researchers [182] . After-hours collaboration time significantly increased for applied scientists, software engineers,
and data center workers, and significantly decreased for people in marketing and sales. After-hours collaboration
time remained steady for researchers, program managers, and IT professionals.
Managers experienced more pronounced changes in meeting patterns than independent contributors. Company-wide
managers were more likely than individual to import an increase in meetings [128]. In a 3,500-person org, telemetry
7

data showed a 25% increase in managers’ afterhours meetings [69]. At the same time, in a study of external
customers, almost a third of participants reported fewer meetings with their manager [29], suggesting that some
managers were facing more time demands than they could accommodate. For more on the importance of managers
in adapting to change, see the following chapter on Personal Productivity and Well-being.
Finally, because remote work entails a learning curve, experience helps. A study of collaboration patterns of
Microsoft employees found differences between people who were new to remote working and those who had
previously worked remotely [182]. The same study also suggests that recent hires experienced a larger drop in
collaboration than established employees. While time in Teams meetings increased for both “always remote”
workers and “new remote workers” (compared to pre-pandemic metrics), new remote workers saw a 47% point
larger increase. New remote workers also made more 1:1 connections via Teams than always remote workers (13
connections per week compared to 9). In a separate survey of Microsoft employees, those with remote work
experience were less likely to report a drop in productivity at the start of the pandemic [46].
1.2.2 The move to remote work was particularly hard on some kinds of collaboration, such as creative work,
“thinking big,” and decision-making.
The movement of work to entirely digital communication platforms had mixed results for collaboration. Some teams
found it more efficient to be remote, such as one of our Beijing teams [176] who reported meetings were generally
more efficient and focused. This same study found a substantial increase in use of all communication tools (online
documents, Teams, email, phone calls and WeChat). Outside Microsoft, one of study of information workers shows
that people worked through an initial remote work learning curve (e.g., learning how to use many of the capabilities
of Teams [156]), to quickly ramp up their skills with online collaboration tools. And research that studied
freelancing in small and medium businesses found that remote work made them more incline to work with
freelancers [104,180], suggesting that collaborating with people who normally work remotely was easier once teams
have gained the experience needed for effective remote work [104,180].
However, there are many indications that different kinds of teams struggled with the transition from in-person to
remote for certain types of teamwork. A survey of thousands of software developers found that 46% were
experiencing difficulty communicating with their team members, affecting their ability to collaborate and reach
milestones [46,156]; similar patterns were seen in external surveys [142]. In one internal study focused on
developers (see the chapter on Software Engineering Experiences for more), people reported difficulties conducting
the kinds of technical discussions they would normally have had around a whiteboard: “We don’t yet have an
awesome replacement for getting the right nerds in a room at the same time, with a whiteboard” [69] (see the chapter
on Devices and Physical Ecosystems for more about the use of physical devices in remote work.) A large external
study of information workers [156] found that teams often lacked clear systems for communication and integration
of working sets of information, resulting in challenges finding files, tracking the status of an element of a project,
and other coordination tasks.
The challenges appear to run deeper than access to seamless, shared, collaborative working spaces, however. In one
study of external information workers [15], an emerging theme was that remote work favors “solo work” over the
collaborative generation of new ideas, finding clarity and alignment within a team, bonding emotionally, and the
ability to change direction as a team. This qualitative study tracked a set of people over time and found that the
emphasis on solo work meant that collaborators often fell out of rhythm with one another leading to unnecessary redos of work. A more quantitative survey of external information workers [156] added further weight to this claim;
they found that 30% of respondents said that brainstorming and generating new ideas was the most challenging type
of collaboration to do while working remotely. Also problematic were: planning (17%), sharing information (17%),
and solving problems (16%).
Studies of Microsoft employees generate similar findings. An internal study of Office Experience Organization
(OXO) teams reports that the ability to do work that involves new ideas, goals and big picture thinking was
diminished when working remotely [26]. Another internal survey at the beginning of the pandemic had 57% of
respondents reporting a decrease in their ability to brainstorm with their colleagues [114]. Similarly, a study focused
specifically on the remote-meetings experiences during COVID-19 of over 800 Microsoft employees found that
brainstorming, workshops, and meetings that require social interaction were amongst the most challenging types of
meetings to carry out remotely [139]. One proviso, however: in this same study, employees in business and sales
roles were over 2.5 times as likely to report that brainstorming had become more effective during mandatory
working from home, in comparison to those in development roles. Why might this be the case? We know that those
in business and sales roles are much more likely to have distributed teams, and thus have developed established
8

practices with remote or hybrid brainstorming meetings. Thus, the transition to all-remote work levels the playing
field and may well have created a net improvement for brainstorming in these roles.
A study of Microsoft employees’ experiences in remote meetings during COVID-19 [138] also looked specifically
at teams’ ability to pivot or change direction. When asked specifically about decision-making in meetings,
most respondents agreed that they felt able to influence decision-making in meetings, and that dissenting
opinions were discussed in meetings. However, significant proportions felt that both their influence, and the
discussion of dissenting opinions (32% and 26% respectively), had lessened during mandatory work from home
(11% and 12% respectively felt they had increased). Further, those with some prior remote work experience felt
substantially more able to influence decision making in meetings than those without prior experience: this was the
case before the pandemic, and even more so after. Those with prior remote work
experience were over twice as likely to ‘strongly agree’ to feeling influential when asked to work from home
than those without prior experience.
To understand why decision-making may be difficult, it is interesting to examine some of the participants’
comments in this study [138]. Here we found that lack of physical cues, body language, and ability to gauge
emotions were said to be significant hurdles to productive disagreement and decision making. A troubling pattern
was for debate to be deferred (“let’s take this offline”) in the name of efficiency and to make use of limited time,
but people often did not follow up. Another factor here was that, while some found online meetings more inclusive,
due to the ‘level playing field’ of all-remoteness, it was also reported that those who were less likely to speak up in
physical meetings were also less likely to contribute to online meetings. And without space constraints, it is easier to
have online meetings of larger groups, which might seem more inclusive, but where fewer people will have a chance
for their voices to be heard.
1.2.3 Informal and spontaneous interaction particularly suffered in remote work, affecting collaboration.
In addition to the task-focused work of collaboration, the ties that spark creative ideas and foster productive
collaboration are built through interpersonal connection, informal communication, and spontaneous interaction, all
of which can be harder to achieve remotely. Friendship at work positively affects both task accomplishment and job
satisfaction [80,178]. Prior research on remote work has found evidence that the quality of relationships with
coworkers tends to go down [1,116,150] and feelings of social isolation tend to increase [135]. An internal-facing
survey of engineers with a focus on teams, found that “66% of respondents reported a decrease in social connection
with their team members, and 78% and 65% cited a decrease in impromptu and scheduled social activities,
respectively. Across the board, we saw a dramatic decrease in feelings of social connection and team cohesion”
[114]. Importantly, they show that this lack of informal communication and cohesion was seen as negatively
impacting productivity. Two Microsoft studies of information workers [156,160] found that they struggled with
isolation from coworkers and friends. One internal study of engineers and program managers [46]found that among
the most frequent challenges faced were “missing social interactions” and being “less awareness of what colleagues
are working on.” A similar finding is reported by a Microsoft team in Beijing, where social interaction in the
physical workplace was reported to be one of the aspects of working life missed the most in working from home
[176].
The concept of a ‘meeting’ has always been a fluid category in terms of the work accomplished, but in this period
where remote work was required, it increasingly included encounters related to the fabric of collegiality. Many of
the short hallway conversations, or dropping by someone’s desk, were taking place through short video or audio
calls. Hallway and casual interaction, some of which is related to coordination of work or sharing of status, was also
moved to meetings [149] or accomplished through IMs. People made deliberate efforts to schedule regular
touchpoints and virtual social rituals such as lunches or happy hours [91,138,156,160]. A study of Xbox console
gamers who said they gamed with co-workers found that while they were split as to whether they talked about work
while gaming, and that those who did reported higher quality gaming experiences [15].
At the beginning of the pandemic, Microsoft employees reported that in-meeting social talk increased at the start of
many meetings, centering primarily around sharing experiences of the current pandemic [138]. These same
participants mentioned the mood was frequently lightened by talking about people’s backgrounds (actual or replaced
with images) or the invasion of children, spouses, and pets [138] during ongoing meetings (although others report
that such invasions were embarrassing [156]). However, as meetings became more focused on productivity within
the context of increased meetings (see later in this chapter), there is evidence that this social interaction over time
was squeezed out, which, paradoxically may have relieved some of the burnout from meetings while increasing the
stress of isolation [138]. (See also the following chapter on Personal Productivity and Well-being).
9

Social talk is one aspect of the fabric of collegiality, but another is the serendipity of social connection in the
physical workspace. It is perhaps no surprise, then, that while existing tools may help facilitate deliberate social
connections and quick check-ins with known colleagues, studies report that people are struggling to replace the
casual, spontaneous “watercooler” conversations that they are missing [26,69]. Note that these are a different kind of
casual conversation from those discussed so far because they involve meeting and connecting with people whom
one would not normally set out to connect with, to check-in with, or to arrange any kind of deliberate meeting with.
We need, therefore, to distinguish between social talk amongst colleagues one plans to see, and conversations that
are unplanned, including the awareness of others that comes from this kind of social activity. It is also important to
remember that not all workplace interactions are pleasant. One external study found employees reported fewer
interpersonal conflicts as they were better able to avoid some people [72].
Our study of Microsoft employees’ experiences in remote meetings during COVID-19 [138] confirms the
importance of spontaneous interaction. Most people said spontaneous interaction mattered to them, though they
were polarized over whether it had become more or less important to them over the pandemic. However, 67% of
participants said their needs for spontaneous interaction were not met, regardless of how much they said it mattered
to them. Some evidence suggests that many whose needs were not met were reliant on informal and unplanned
conversations in social spaces at their workplace. For others, social interactions at home were at least partially
fulfilling their needs for spontaneous interaction.
1.3 The Impact of Remote Meetings
1.3.1 Video conferences are fatiguing.
The idea of meeting fatigue rose to prominence during the pandemic, and our research supports the notion that
constraints of video conferencing technology, when combined with increased cadence in meetings, contribute to
perceptions of fatigue. Numerous studies have identified reasons that video conference meetings may cause fatigue,
including reduced nonverbal cues that inhibit the ability to “read people” in a conversation, the need for sustained
attention, the pressure to perform paying attention for others, low media quality, and the fact that crowded remote
meetings require cognitive multitasking [49,153,172].
One study from the Human Factors team found that brainwave indicators of mental effort were higher when two
people performed a collaborative task remotely, than when they shared the same space [19]. In another study, the
same team measured EEG and heart rate of 12 Microsoft employees and found that brainwave markers showed
significantly higher levels of stress in video meetings as compared to typical non-meeting work [19]. Further,
fatigue due to concentration began to increase 30-40 minutes into video meetings. Looking at days filled with video
meetings, dramatic changes in brainwave patterns, consistent with being over-worked or stressed, began to set in
after about two hours. More recent, but preliminary results from this same team found that brainwave measures
showed lower levels of stress and concentration when Teams “Together” mode was used compared to the more
usual “Gallery” mode [19]. We conjecture in the traditional “Gallery” mode, the brain must override the sensory
perception that all participants are in different places to treat them as gathered in one conversation. “Together” mode
removes the different backgrounds of participants and the artificial separation of a grid, instead showing their cutout images in a single naturalistic virtual arrangement (such as an image of an auditorium with each person in their
own seat), reducing the workload necessary to perceive everyone as together. A related contributing factor to video
conferencing fatigue is the lack of variety of what is shown on the screen – endless views of either talking heads or
screensharing and presentations with very limited views of people [138].
1.3.2 Fatigue was also increased by meeting load and the challenges of coordinating meeting tools.
However, it was not just the dynamics of individual meetings that made them tiring during the pandemic. Their
sheer quantity and the way they played out over time may have damaged productivity and increased burnout. As one
study of external information workers found [156], the lack of a break between meetings in itself can be exhausting.
As one participant said, the schedule of remote meetings led to “alot of stacked meetings…mentally you have
to context switch…. I take a deep breath before, go click on the next and remind myself who is going to be in the
meeting and what is it about before I joined because it really is that difficult when it’s all stacked one the other”.
This points to a need for what these researchers refer to as “micro mental breaks” in order to do context or task
switching. Two studies of employees [149] suggest that the increased number of meetings coupled with the lack of
natural transitions between meetings in the office, such as walking between meeting locations, also reduced the
overall physical movement of employees, contributing to fatigue.

10

Meetings, of course, need to be considered within the broader picture of collaboration workload. Many external
information workers reported feeling “overwhelmed by the significant increase in the number of chats, channels, and
documents they need to reply to, be aware of, and contribute to for collaborative projects” [156]. In a different study
of external information workers, many also reported feeling “overwhelmed” by the sheer volume of incoming
messages and being “tied to their desks” since IMs can come in any time of day [160]. An internal study focused on
OXO Engineering teams, identified “too many meetings” as one of the most frequently cited pain points [26]. This
is a sentiment echoed in a study focusing on Microsoft engineers [69], which found that, despite output measures for
collaborative practices being either stable or increasing over time, the need to collaborate and to be seen to be
productive, may well have contributed to burn-out and reports of perceived decreases in productivity. (See the
chapter on Software Engineering Experiences for more detail.)
Several ongoing studies found that the diversity of tools in use also presented challenges. One study of external
information workers [160] found that the diversity of communication media contributed to the stress of
collaboration. They moved between email, video calls, phone calls and chat, and the products used varied depending
on their colleagues. In a later set of findings [160], the extra overhead of moving between different tools, and
constantly checking different places for communication during the workday, was a catalyst causing teams to settle
on one collaboration tool, although this was not always entirely possible when work had both internal and external
stakeholders [138]. An external study of information workers also found that information workers felt overwhelmed
and that the “which tool when” problem has been highlighted by the pandemic [156]. It is no wonder that
participants in one study mention that remote methods seemed more effortful than simply stopping by a colleague’s
desk with a quick question [160]. Ultimately, differentiating the fatigue attributable to video conferencing and other
qualities of remote work from that which is attributable to living through a pandemic will be important to tease apart
over time.
1.3.3 Interaction in remote meetings is challenging in ways that are fundamentally different from in-person
meetings.
Video conferences are comprised of multiple channels of cues – auditory, visual, and textual – which happen
simultaneously and differently than they do when in-person. Evidence suggests that voice is the most important
channel. In internal study of online meetings, 51% of the participants ranked the ability to “hear people” as the most
important communicative feature of meetings [138]. This is in line with prior research that has found that voice is
the central communicative mode and should be optimized for, even in video meetings [124,137].
However, video is important in terms of “social presence” – the sense of intimacy and immediacy with others. The
importance of presence (and the consequences of its absence) recurs frequently in research across internal and
external studies. In multiple studies of Microsoft employees’ experiences during COVID-19, participants reported
that small group or one-on-one meetings with video turned on can be engaging and interactive, especially if people
in these small meetings know each other well [26,138]. As group size grows, however, people reported feeling
increasingly invisible. Independent of the number of people, social presence is difficult to attain when the meeting is
primarily focused on screensharing or presentations. In those cases, Microsoft employees who were presenting
reported that they were “speaking into the void”, with no sense of audience and thus no way to adjust how to
proceed. Similarly, attendees became largely invisible, especially if they muted their microphones and cameras to
ensure that the presenter could speak without distraction, which led in turn, to increased disengagement [138].
However, this same study also found changes over time. Video was turned on more initially during the pandemic,
but as time passed, this was reported to happen less often due to bandwidth problems and the fatigue caused by
people feeling like they always had to be presentable [138]. At the same time, the study found that the use of video
(choosing to turn it on or not) did not correlate strongly with other factors measured, such as feeling effective,
feeling tired, being able to engage, feeling comfortable, feeling that meetings are well-managed, and multitasking.
This response appears to be at odds with the finding that visual presence is important. It is likely that this
complicated issue is pointing to multiple factors at play which need further disentangling.
Even without a presentation, “reading the room,” – knowing what people are attending to, what activities are taking
place, and being able to perceive non-verbal interaction – is difficult in remote meetings, especially as group size
increases. A study of Microsoft employees’ experiences in remote meetings during COVID-19 [138] showed that
“knowing who is speaking” was one of the three most important features of video conference quality, yet that could
be difficult to discern. While current speakers might be heard, not knowing where to locate that speaker’s visual
representation (video or an audio placeholder) was reported to make it more difficult to judge when to take a turn.

11

In fact, turn-taking (the prediction and management of which person should take the next turn to talk [144]) was the
most frequently reported issue when asking about interactivity challenges in a study of Microsoft employees’
experiences in remote meetings during COVID-19 [138]. Users reported uncertainty about the best way to deal with
overlapping and interruptive talk [138]. This is also an aspect of remote meetings that research has explored for
decades [146]. Even with video on, audio latency makes it more difficult to take turns and to separate meaningful
and non-meaningful delays in responses [142]. The limited field of view and flattened view from webcams, as well
as the arbitrary ordering of video rectangles also make it difficult to notice both the subtle visual cues that someone
wants a turn at talk and the associated subtle visual cues that other group members are attending to a potential bid to
talk [173]. The hand-raising feature in Teams was reported as helpful for overcoming at least the issue of bidding for
a turn, but it was new and its use was only beginning to be ingrained [138].
Some of these challenges are caused by social cues we would normally use in-person not being present, others are
caused by limitations of internet connections, especially shared domestic connections. It is important to note,
however, that research has shown that even with no perceptible audio or video lag, conversations that are mediated
by audio or video technology are significantly less interactive than in-person meetings. Mediated conversations have
less overlapping speech and may be perceived as more formal [146]. Problems with internet connections, such as
choppy audio and video, can have lead people to turn off their microphones and video, limiting everyone's ability to
perceive one another [138], further reducing everyone's sense of togetherness, and hence undermining the kind of
mutual social joys and obligations that are central to the experience of meeting in person. (For more about
bandwidth and latency problems, see Chapter 5 on Devices and Physical Ecosystems.)
1.3.4 The use of video in meetings is both a personal and group affair.
One study of Microsoft employees’ experiences in remote meetings during COVID-19 [138] also found that there
are many reasons why people choose to keep their video off, or not to turn it on in a remote meeting. As we have
already noted, technical performance issues were rated as amongst the most important. However, the other major
factors cited were: other people turning their video off, people wanting to multitask, and people feeling selfconscious about their appearance. “Not actively participating” and “The effort of being seen” were also rated as
highly important by many participants, but this was less clear-cut. In general, there were no differences by gender,
role or prior remote work experience.
Examining the comments from participants, the study found peer-mimicry to be ubiquitous: people looked to others
in the meeting for cues as to whether to turn video on or not, especially looking to a meeting leader or customer
establishing the norm. Many people also mentioned (and conflated) the effort of appearing presentable, appearing
attentive by looking at the camera, managing their background, managing family interruptions, and feelings of selfconsciousness. Non-standard meeting hours were commonly to blame for video off in early mornings, late nights,
and after workouts or showers. However, some mentioned this perception of effort and self-consciousness was
decreasing, greatly influenced by team culture. Video in general was seen as adding more social and engagement
value—it was rarely spoken about in terms of improving work efficiency or output.
A second set of questions explored the value of video in different kinds of meetings: small group discussions, small
group collaboration around shared documents or presentations, and large presentations. In small group discussions
(with no shared documents), most people reported benefits to video, indicating that video for the most part was not
distracting, that it boosted engagement, and provided important information for the collaboration. This situation
changed, however, when there was a shared document or presentation in a small group. Whereas the video for this
scenario was still not found to be distracting for most, it was also not always seen to boost engagement. Half of
respondents in this case also said they wanted more information about others in this situation (53%), but a sizable
minority did not (21%). People were divided when it came to seeing video of audience members during
large presentations. When presenting, 27% of people said they found video of the audience distracting while 55%
did not; 53% wished for more information about the audience while 25% did not. When in the audience, sizeable
groups did and did not find video of the audience distracting (50% and 39% respectively), and did and did not wish
for more information about the audience (34% and 53%).
On the whole then, people were more likely to find video of others distracting in large group presentation scenarios
(whether presenting or audience) than in small-group scenarios. People were less likely to want more information
about people who had their video off in the audience scenario, than in any other scenario (presenting, discussion, or
collaboration). This was borne out in free text entries where it was generally judged that video was a net positive for
small meetings, and a net detractor in big meetings. In big meetings, audiences liked to see video of the presenter,

12

and active question-askers, but not the audience, whereas presenters felt like the lack of audience video left them
speaking into a void (as noted above).
Examining people’s comments in relation to these questions reveals that the use of video in meetings presents a
conundrum: on the one hand, the video of others can be irrelevant or even distracting (e.g., when others are clearly
multitasking or not paying attention). On the other hand, visual information we normally glean from in-person
meetings is clearly important for interaction and engagement, but difficult to convey in video conferences. As one
participant put it, “[…] it’s not information that’s readily distilled, nor is it information that comes across well with a
bunch of little video boxes. It’s information that’s often not even possible: who’s sitting with who, who’s having a
side conversation when […] Who’s smiling and who’s nodding is something you might get on camera...but people
do behave differently when there's a camera on their face than when they're just in a room. […]”
The modern video meeting attendee thus sits at the intersection of three phenomena: 1) the diminished utility of
video since people cannot produce the interactional information they would have in person; 2) the need, as a
speaker, to understand people’s engagement (attention, emotion, etc.); and 3) the pressure, as a listener, to return the
courtesy of relaying engagement information to the speaker. The result is that the provision of engagement
information, which is universally acknowledged as valuable, is forcibly coupled to the consumption of irrelevant
video information and a constant, unnatural physical configuration.
1.3.5 Parallel chat became a pervasive component of meetings.
Although the audio and visual channels are primary when video conferencing, most platforms also enable attendees
to simultaneously post text, images, files, links etc. into a parallel chat area. A study of Microsoft employees’
experiences in remote meetings during COVID-19 [128,138] found that over two-thirds (69.7%) reported using
parallel chat in meetings, 26.6% reported using parallel chat in every meeting or almost every meeting, and 24.1%
using parallel chat at least once a week. Thus people are splitting their attention across modalities. We know from
previous studies [136,155] that attendees engage in backchannel chat because they want clarification on meeting
contents, or want to participate, and/or influence others in the meeting when it is difficult to get a word in edgewise.
This parallel conversation may augment the main discussion by allowing more people to contribute their ideas and
share resources and can hence increase inclusion. But parallel chat can also create new challenges for meeting
organizers and participants: chat can distract attendees from the main agenda, and organizers may have trouble
integrating chat conversation with the overall meeting discourse. It is further unclear how meeting chat and the
meeting proper are integrated into a holistic understanding for all participants.
One study of Microsoft employees’ experiences in remote meetings during COVID-19 [138] also found that people
were using chat more, some people found it more distracting than others, but most agreed it was a net positive. The
top perceived positive uses of chat were allowing communication without interrupting the speaker and making large
meetings more inclusive where it was tough for everyone to speak. The top reason for chat being distracting was
when the chat conversation diverged from the audio-visual discussion, making it difficult for attendees to allocate
attention. Respondents who were most positive about chat tended to list specific uses, suggesting that people who
were successful at chat formed strong models of what chat is good for and when to ignore it or not use it, in order to
mitigate its distractive effects.
It seems then that in-meeting parallel chat is one way that people can make their voices heard and their presence felt
in an all-remote world. This appears to be a new habit that has gained strength and a feature that we are beginning to
rely on and learn to use in this new world of work, and a way to compensate for some of the shortcomings of
current, collaborative tools.
1.4 Inclusion and Forming Connections
1.4.1 Remote work affected inclusion both negatively and positively.
Difficulties in having a sense of presence and in having all voices heard point to some of the downsides of remote
collaboration tools and their impact on inclusion. For example, when it comes to online meetings, it appears that
junior (career level as self-reported in verbatims) Microsoft employees found it especially difficult to gain turns at
talk or have their presence noticed, making hierarchies more conspicuous [138]. A recent study comparing the first
90 days of new hires in Azure Edge [69] to those of new hires the previous year found that new hires had a difficult
time connecting with others, impacting their productivity. For that group, new hire meeting hours, meetings
attended, emails and IMs sent, collaboration hours, internal and external network size were all down relative to
2019. Consistent with pre-pandemic research [86,87], new hires interviewed felt more positive when they had
“formalized, consistent and sustained 1:1 interactions with onboarding buddies, mentors and their managers.”
13

Furthermore, over-reliance on the visual channel in remote meetings can make telework especially challenging for
people who are blind or low vision, and the assumption that everyone can hear the audio channel equally well can be
difficult for the deaf. More specifically, our research shows that people who rely on screen readers for compute
output (those who are low vision or have dyslexia) encountered were especially challenged when other people
shared their screens with them, putting the screen reader voice of the shared screen and the speaker's voice in
competition [163]. Another interesting finding is that those who are deaf and speak through ASL interpreters are
disadvantaged by systems that use active speaker detection to choose which video streams to display. Such systems
highlight the interpreter rather than the person who is signing leading these users to feel unintentionally digitally
“erased” from the interaction [163].
At the same time, we are finding evidence of many benefits of all-remote work when it comes to inclusivity. As an
example, some participants who previously felt excluded reported that their social presence increased during the
pandemic. One study, designed to explore telework with and for people with disabilities [163], suggests that the shift
to remote work has been a social leveler in some respects. People who under normal circumstances had to work
from home were now ‘experts’ in teleworking, and some said that they preferred this new normal because they were
no longer at a disadvantage simply by virtue of being the only one ‘not in the room.’ This same study found that
some deaf participants who lip read said that all-remote meetings were much better for them because the frontal
views of each participant were captured: this made it much easier to lip read, compared to calling into a conference
room where the camera captures side views of people in a meeting [163]. These results show that who is included
and who is excluded by which configurations of technologies and social practices is a complex issue, but one that
deserves to be put front and center of our research, design and development efforts.
Another important point is that this “social levelling” effect is in fact of more general significance: in a study of
Microsoft employees’ experiences in remote meetings during COVID-19 [138], the equalizing effect of everyone
being remote was a major theme in the journal study. For example, one participant said, “When we’re meeting in a
conference room, it’s easy for people who are remote and on Teams to be overlooked or marginalized. […] Having
everyone on Teams means everyone has the same opportunities to speak and has the same challenges in terms of
hearing/presenting.” This is confirmed by other studies: Several participants in an external study of decision makers
commented on senior leadership being more accessible online as opposed to being largely unavailable when
working from a big corner office [62]. An important point here is that this effect will likely disappear when some
people return to the office and we are then experiencing more hybrid meetings situations where some people are copresent and others are remote. Designing for the hybrid meeting situation raises a whole new set of challenges to
make sure interaction is inclusive.
1.4.2 Many people not only maintained their existing networks post-COVID but made new connections.
Given the challenges of collaborating remotely, we might surmise that people’s collaborative networks would suffer.
Some internal studies showed that many people’s professional networks were either maintained or even grew at the
start of the pandemic. This was not universal, however.
Early in the pandemic, for example, a study of Microsoft employees in China [131] found that people’s networks did
not change substantially after enforced working from home. After shifting to remote work, a quarter of employees
experienced no significant change, and two thirds of employees maintained a network within 30% of their original
size.
A different internal study analyzed the connections made by over 92,000 Microsoft employees [148] in order to
explore the “meaningful connections” they made (emails, instant messages, and calls) pre and post enforced working
from home, with a focus was on outbound connections to 4 or fewer recipients. The data show that most employees
did not drop their meaningful connections in the transition to remote work and in fact increased contact with their
prior connections by 3%. More than this, they were also found to increase the size of their networks, making 24%
more than in the month prior to the shift to remote work. Most surprising, perhaps, was that 22% of these were
outside of people’s usual working groups. The researchers suggest that this is the sign of a resilient organization
where deliberate efforts are made to adapt working patterns to the new conditions.
An additional source of data comes from a study of Microsoft employees’ experiences in remote meetings during
COVID-19 [138]. This found that the strength of people’s indirect connections (people they do not normally work
with but are otherwise aware of) was generally perceived to be getting weaker, with the lack of spontaneous
interaction cited as a significant factor here. People were also having variable success in maintaining their
connections with their direct network (the colleagues they work with on a day-to-day basis), with a bimodal
14

distribution here of 36% participants who felt this was weaker, and 42% who felt it was stronger (22% reported no
change). The majority of people in the study reported making new connections while working remotely, or forming
new working relationships with existing connections. However, success with new connections appears to depend on
role and experience. Some of our evidence shows that people in non-developer roles were more likely to form new
connections, and people with previous remote work experience also fared better in this regard [138].
An external LinkedIn study of event attendees [179], however, shows that the networking that would have happened
at on-site events was substantially undermined when events went online. The people interviewed found two-way
video chat most conducive to forming those new connections but also found such video conferencing fatiguing. The
picture on networks is complex and involves a variety of factors. The kind of network matters, be it direct close
colleagues, indirect connections, or new connections. In addition, we have seen that role matters, as well as
experience in remote working. There is little doubt, however, that the “levelling effect” of everyone being remote is
at play, with physical location receding into the background and thus everyone feeling “as close” to everyone else
(at least for those in the same time zone). We also need to understand whether these findings generalize outside of
Microsoft, and to organizations which are perhaps less resilient, and with less technical infrastructure to rely on.
1.5 Looking Forward
1.5.1 People are creative and resilient, and are developing new work practices to adapt to a changing world.
In the face of the challenges outlined above, people are developing innovative new work practices at individual,
team, and institutional levels. These can be effective but can also have undesirable downstream effects.
For example, from early in the pandemic, teams in Microsoft were developing new strategies to address meeting
challenges, being thoughtful and deliberate in how they manage their meetings while everyone is remote: for
example, people were trying to be more inclusive in their scheduling [138,149], more intentional about how and
why they hold meetings [29], more punctual [138], turning on video to signal engagement [149,163], recording
meetings, and immediately distributing presentation content [149]. It turns out that these kinds of practices are
important: evidence suggests that good quality meetings and effective communication were associated with better
perceived productivity [149]. On the flipside, meetings without clear agendas contributed to increased frustration
and meeting fatigue [149].
Looking a little closer at how both preparation for meetings and meeting follow-up might have changed during
working from home, we turn again to an internal study of online meetings [138]. This study found that while a small
majority (55%) experienced a change in preparation for meetings, a substantial cohort (45%) did not. For those who
experienced a change, all types of preparatory work were cited as being more frequent (pre-reads, agendas, goals,
async and sync discussion) leading to most (66%) feeling better prepared for meetings. However, the picture was
very unclear as to the overall value of preparatory work, with split opinions on whether it made other people better
prepared, made meetings run more smoothly, or whether it improved productivity. However, there was strong
agreement that better meeting preparation did not reduce the number of meetings overall.
With regard to meeting follow-up, an overwhelming majority (94%) of participants said they experienced more of at
least one type. Here, Teams personal chat was seen as a positive way to follow up (63% reported an increase), while
additional meetings were viewed as negative (40% of people reported an increase). There were modest increases in
the use of action items and document collaboration, and mixed results for the use of Teams channels, meeting chat
threads, and email. There was no strong evidence for positive impact of increased follow-up from meetings, possibly
because of the negative impact of more email and more meetings being seen to undermine productivity. Good action
items were seen as positive, although some comments indicated that they were often not tracked. Other pain points
included lack of time at the end of meetings devoted to confirming follow up actions, and the problem of post
meeting-related discussion being fragmented across Teams chats, channels, meeting chats, etc.
Teams were also developing some norms around shorter meetings and no-meeting days, and there were reports of
leaders developing new meeting habits for teams. To deal with some of the problematic interactional issues in
remote meetings, Microsoft employees reported that meeting moderation was becoming increasingly common [138]:
either people were being assigned this role officially or they were taking it on in a more ad hoc way. Many
moderators felt that they were providing a crucial service for their team. Other groups were questioning whether
meetings were always the best route, and recommended considering when a Teams meeting should be an email
[9,181]. However, people had mixed success in trying to reduce meetings through more asynchronous means, such
as Teams chat, email, Teams channels and document collaboration [138].

15

These emergent practices can also have unexpected downstream consequences. One study of external information
workers found: “Everyone’s calendars look full,” so people often have to ping coworkers to determine their
availability, which in turn “[takes] more time and [leads] to more distractions” [156]. Moderators in meetings find
that their own ability to contribute effectively to the discussion is diminished. No-meeting Fridays also resulted in
reports of even more meetings compressed into even longer workdays from Monday to Thursday. Which strategies
will work best for which individuals and teams remains an object of further research. Developing more deliberate
practices takes time, is hard work, new team members need to be taught, and it may not work outside one’s team,
leading to some frustration [138].
It seems, then, that we are collectively taking this opportunity to learn new skills in managing and making the most
of remote meetings. Capturing and learning from this experience will be a key issue when we do start to go back to
the office, both for the benefit of remote workers and for those who can meet in person.
1.5.2 The best hybrid future will retain many new work practices and focus on flexibility.
To close out the study of Microsoft employees’ experiences in remote meetings during COVID-19 [138], a poll was
sent out to dig deeper into participants’ opinions about a hybrid future, given their experiences over the course of
working from home. One question asked which meeting practices developed during mandatory working from home
should persist. These included: seeking to reduce meetings, uploading profile images, using active moderation,
including time to confirm next actions, not scheduling meetings back-to-back, using chat to increase participation,
having agendas, and turning video on. There was near-universal support for retaining almost all practices (<10%
disagreement). The one major exception was ‘everyone should turn on video’: 31% disagreed or strongly disagreed
this practice should be carried forward. This reflects previous earlier findings (above) exploring why people turn
video off, which showed that video is not considered necessary for meeting effectiveness in most cases and comes
with a host of negative costs.
Another question asked what types of activities should be prioritized in opportunities for same-room meetings. In a
hybrid working world, opportunities for same-room meetings are scarce, so the aim was to understand the most
effective use of that time together. It was near-universal (<6% disagreement) that we should: prioritize hybrid
meetings where remote attendees engage fully; and prioritize same room meetings which are well-planned, so that
meetings are efficient. There was also majority support (45-60%) for: building in 1:1 and group social time, and
prioritizing meetings for which planning is difficult to facilitate creativity (but there was a reasonable minority
opposition, 15-20%). Prioritizing ‘meetings for which planning is difficult’ saw substantially more support from
those without prior remote work experience (62% for; 10% against), than those with prior experience (40% for, 23%
against). It is possible that remote workers underestimate the value of co-location in resolving ill-defined tasks – and
it is possible that office workers overestimate it.
The verbatim responses that accompanied the poll reveal just how uncertain the future of hybrid meetings is, and
how much flexibility we will need to have. Many participants indicated that they felt that the default mode of work
should change permanently to remote asynchronous work, predicting there will be little or no opportunity for entire
teams to be physically co-present in the future. However, there was also a strong voice from those who appreciate
the benefits of physical co-presence. These people cited creative and social meetings as good candidates for
prioritizing if any time in the same room is possible. In general, responses overwhelmingly cited a need for
flexibility in whatever happens in future–solved team by team, need by need, and not top down, while supported by
flexible technologies.
While the above research considers what people think of hybrid working in prospect, Microsoft employees in China
have already been experiencing hybrid working and two studies report early findings from a staggered schedule of
returning to the office [176].
One study of three Microsoft offices in China used a survey and interview technique to explore people’s decisions to
return to the office or not [176]. The study found that two of the main motivations at play in deciding to return to the
office were the ability to have meetings in person and social engagements with colleagues, underscoring the
importance of in-person connection in working life and the degree to which working from home can undermine it.
One general finding was a perception of higher productivity and increased job satisfaction when in hybrid work
mode compared to all remote working pointing to the success of this mode of working.
However, a key question is: as a result of prolonged working from home, are there permanent changes in how
people work? What will persist when some people transition back to the office and what is temporary? To explore
this, the Workplace Analytics team [131] examined telemetry data from Microsoft employees in China. Early trends
16

indicate that collaboration patterns established during working from home have so far largely persisted. Increased
use of instant messaging has stayed at the same elevated level as during the work-from-home phase, remaining
steady as a way of communicating both within meetings and outside of them. At the same time, Teams voice and
video calls have fluctuated considerably and even increased as people began to return to the office, probably
reflecting the fact that many people were still working from home.

17

2 PERSONAL PRODUCTIVITY AND WELL-BEING
By Jenna Butler, Mary Czerwinski, Shamsi Iqbal, Sonia Jaffe, Kate Nowak, Emily Peloquin, and Longqi Yang
2.1 Introduction
We now turn to understanding the impact that COVID-19 had on the personal productivity and well-being of
information workers as their work practices were impacted by remote work. This chapter overviews people’s
productivity, satisfaction, and work patterns, and shows that the challenges and benefits of remote work are closely
linked. Looking forward, the infrastructure surrounding work will need to evolve to help people adapt to the
challenges of remote and hybrid work.
2.2 Productivity, Satisfaction, and Work Patterns
2.2.1 On average, self-reported productivity was unchanged, but it varied with role and experience.
Since information worker productivity is hard to measure, many studies looked at self-reported productivity and
satisfaction. Individually, some people flourished – and hoped to continue working from home at least part of the
time post-COVID – but others struggled. In a March survey of US-based Microsoft software engineers and program
managers, 34% said their productivity had decreased while working from home, and 34% said it had increased. In a
July survey of employees in Puget Sound, 32% agreed that returning to the office would make them more productive
and 30% disagreed [109]. Externally, we saw an initial information overload as people adjusted to new tools and
ways of working [77]. Some people reported liking the new interpersonal communication patterns while others were
hoping for a return to the “old way” [77].
Microsoft employees were more likely to report a decrease in productivity while working from home if they
reported little prior experience with remote work, a shorter tenure at the company, fewer pre-pandemic
collaborations (including meetings), or fewer standups. Also, software engineers were more likely than program
managers to report their productivity being negatively affected [46]. Geographically, employees in Puget Sound
were also more likely to report a decrease in productivity and lower satisfaction [46,128], potentially due to their
having less experience with remote collaboration. In a survey of Microsoft employees in China, perceived personal
and team productivity while working from home were significantly correlated with how one felt about physical
health and mental well-being, perceived workplaces’ setup and boundaries, meetings, team culture and workplace
status.
Externally, in a spring 2020 survey of US workers commissioned by Stanford, 35% of respondents said they could
be fully effective at their jobs while working remotely, 28% said they could do their jobs with 50 to 90% efficiency,
and 37% said that they could not do their jobs at home or would be less than 50% efficient [18]. A pre-pandemic
study [66] that used Occupational Information Network (O*NET) data on job content estimated that 37% of jobs
(representing 46% of wages) could be done remotely [38]. In addition to job characteristics, individual
circumstances mattered: a study of information workers found that whether they felt they could work from home
productively depended on 1) the layout of their workspace and 2) whether they lived with others. Those living with
others found their productivity hinged upon the needs of their co-habitants – children, partners needing help with
errands or tasks, etc. [156].
These results are in line with prior remote work experiments. Nick Bloom and colleagues ran an experiment with
call center workers who had expressed interest in working from home and found that, while the average effect of
doing so was positive, some people were negatively affected. Those who were less productive at home were more
likely to return to the office after the experiment ended [17]. A different experiment at the US Patent Office also
found positive average effects, particularly for those who chose to move to areas with lower cost of living [32].
Prior research also found that factors like personality [125] and gender [1,63] played roles in remote work outcomes.
Previous work also suggests that work that is easily codified is more amenable to remote work [14,168], but that
creative work [59], new workstreams [53,140], and tasks that require extensive collaboration will suffer when done
remotely [59,168]. Connecting these findings to the roles and types of work done at Microsoft is an important topic
for future research.
While it is hard to measure productivity objectively, there are available objective measures for short-term developer
activity; see the following chapter on Software Engineering Experiences for more details. On average, pull requests
stayed constant or increased slightly. However, according to an internal study [69], the number of pull requests per
new hire that started following the post-COVID move to remote work were 34% lower compared to pull requests
per new hire during the same period in 2019; a greater percentage of developer new hires had not completed any
18

pull requests in the first 90 days and the median time to complete a first pull request increased by 28% relative to
2019 [69]. New hires may not know the team as well, they may lack context, and it might be especially hard for
managers to manage them remotely. The same study found that vendors completed 27% fewer pull requests on
average this year compared to 2019.
2.2.2 While some reported satisfaction with remote work, it varied with organization, role, and experience.
Just as productivity varied extensively by role and experience, so did job satisfaction. In a survey of US-based
Microsoft software engineers and program managers, 31% said that their job satisfaction had decreased, but 32%
said it had increased [46]. Similarly, 33% of Microsoft Puget sound employees responding to a survey agreed that
returning to the office would improve their overall well-being while 29% disagreed [109]. In a CSEO (Core Services
Engineering and Operations) survey in November 2020, 81% of global Microsoft employees were satisfied (12%
dissatisfied) with work from home [128]; a study in OXO (Office Experience Organization) yielded similar results,
with over 60% reporting they're satisfied working from home [26].
Employees were more likely to be satisfied with working from home during COVID-19 if they had experience
working from home prior to the pandemic [46,128]; in the CSEO survey 85% of global Microsoft employees who
worked from home weekly before COVID-19 were satisfied working from home during COVID-19 (compared to
69% of those who never worked from home previously). This is also consistent with the results of an OXO survey,
in which 61% of respondents said the challenges they faced early on improved over time [26]. Some people who
worked remotely prior to COVID-19 reported that the totally-remote meetings they had in spring 2020 worked
better than meetings pre-COVID when they were remote and everyone else was in a conference room [163].
People’s satisfaction was correlated with their feelings of commitment, motivation, focus and being overworked.
Nearly one-third (31%) of respondents to an external survey who felt committed to their team goals preferred
working from home over the office, compared with 18% of those who felt disconnected from their team’s objectives
[180]. In the OXO study [26], people were less likely to report being satisfied with their work on days they
mentioned challenges with motivation, focus, or feeling overworked. The same study found that mental and physical
health, along with motivation and feeling overworked, were strongly associated with someone reporting being
satisfied on less than 60% of their nightly responses. These challenges and the relationship to job satisfaction were
not specific to working from home but could have been exacerbated by it. Managers in OXO were less likely than
individual contributors to at some point report challenges related to motivation and collaboration, but more likely to
have challenges around meetings, kids, and well-being [26].
A study from eXperience Collective Planning & Research [156] proposed five common remote work “journeys”
based on feedback collected from external information workers, a framework that could help categorize the
aforementioned experiences. The first category was the Positive experience, where people felt well-prepared for the
challenge and embraced the benefits that it presented. The second category, Growing, represented the experiences of
those who struggled initially, but then adapted and ended up feeling good. The third group, Resilient, represented
those whose productivity and attitude towards remote work varied day by day. The fourth group, Struggling,
included people who initially enjoyed the benefits of remote work, but later struggled as negative effects of isolation
and distraction crept in. Finally, the last journey, Negative, represented those who felt overwhelmed with the
challenges from the beginning and continued to have a negative experience. Of note here, the individual’s particular
“journey” was very much impacted by their job demands, workplace setup and whether they cohabitated with other
people.
2.2.3 Average workdays got longer during COVID.
On average, the workday during COVID started earlier and ran later [22,26,66,128,151]. One internal study found
that seven out of ten people experienced workweeks that expanded by at least three hours, that many people started
to skip the lunch hour, and that the share of instant messages sent between 6 pm and midnight increased by 52% on
average [3,66]. A study of external Teams users showed an 100% uptick in instant messages on Teams, particularly
after hours [6]. GitHub data on developer activity also showed a lengthening of the workday for non-Microsoft
employees [47]. In a study of information workers external to Microsoft, people reported that they found it more
difficult than expected to stop working at the end of the day [156]. Internally, the change of workdays varied by
roles [182]; sales and marketing professionals experienced shorter work days, and the changes for IT and researchers
were not significant.
We see a similar pattern globally, potentially exacerbated by time zone differences. When Microsoft China offices
switched to remote, average workday length (the time between the first and last work activity) increased. When they
19

began to return to offices, it lengthened still more [131]. In a study of India-based Microsoft employees, it was
found that the greater the time difference with collaborators, the bigger the challenge in managing the length of the
workday [83]. Many people spent much of the day on other responsibilities – such as parenting or taking care of the
household – and worked in the evenings.
Work also started extending into weekends more than it had before COVID-19. Using SwiftKey data as a proxy for
mobile users, Microsoft Customer Insights Research (MMX) analyzed how usage of Teams and Outlook changed
between February (before COVID-19 required people to work remotely) and April (after the transition to remote
work); they found that weekend usage of mobile Teams increased from 25% of weekday usage to 35%, and
weekend usage of PC Teams increased from 36% to 44%. Also, for SwiftKey users, weekend use of Outlook grew
more than weekday usage; This may suggest that some communications are extending into weekends, and that
mobile apps are seen to be more suitable for these communications.
Importantly, the observed longer workdays may be partially due to the increased interweaving of work and life tasks
(see later in this chapter), meaning that the increase in actual time spent working may be smaller than the increase in
the workday. However, this is unlikely to be the only factor. Prior research found that remote workers were more
likely to work overtime than those with more traditional workplace arrangements [122]. Remote workers may be
inclined to work more hours to signal “work devotion” in lieu of being able to do so through consistent physical
presence at the office [54].
Another potential source of additional working hours is the elimination of commutes. Microsoft survey respondents
reported an average total commute time of approximately one hour per day and about half of them said that not
having to commute was a very important benefit of working from home [46]. In a survey of Microsoft employees in
China, 59% listed commute time as a reason they continued to work from home some days after the offices opened
[176].
The previous chapter on Collaboration and Meetings provided additional detail about increases in meeting time and
after-hours meetings and communications.
2.2.4 Some, but not all, employees with children struggled with childcare.
Multiple studies reported that the additional childcare responsibilities due to COVID-19 complicated working from
home [83,156]. When asked about the top factors contributing to work stress, 24% of information and firstline
workers in India and 21% in Brazil selected “Balancing childcare or homeschooling with work,” compared to 16%
in the US, 15% in the UK, 14% in Australia, 12% in Germany and 4% in Japan [154]. In an external survey of
remote workers [35], 85% of women with childcare responsibilities reported that their caregiving responsibilities
were making it somewhat or much more difficult to attend to work, as did 70% of men who were caregivers [35].
The same survey also found other differences in the work-from-home experience of people with caregiving
responsibilities. People with childcare responsibilities commented on exhaustion, the need to work around the clock
to catch up, and challenges in homeschooling children; they were eating less healthily than before and exercising
less [35]. Overall, the study found that older males without childcare responsibilities had a more positive work from
home experience than those who had to balance work with caregiving responsibilities.
However, at Microsoft, the effect appeared to be smaller; fewer than 60% of employees with children reported
difficulty in handling childcare responsibilities. Difficulty with childcare was correlated with self-reported
productivity, but just having children was not: 43% of those who reported childcare difficulties reported their
productivity had decreased while working from home compared to 29% for those who did not have children in
school or daycare prior to COVID-19 and 23% for those with children who reported no difficulty with childcare.
There were also cultural nuances: in India, some employees reported that staying with larger family meant having to
disproportionately take on more of the household responsibilities while losing the benefits of having household help
[83]. Employees with family duties also tended to report different specific challenges. Employees who previously
had children in school or childcare were more likely to indicate major challenges of “More distractions or
interruptions” and “Less time to complete my work”, and less likely to indicate “Lack of motivation” [46]. In OXO,
5% of people consistently reported issues related to “Kids and Distractions” as the hardest part of their day for the
first 7 weeks following the move to remote work [26].
2.2.5 Managers appeared to be especially hard hit.
An internal study [69] found that while all members of a 3,500-person org were, on average, working a bit more,
managers seemed to be the hardest hit. Relative to the same period in 2019, software engineering people managers
showed a 300% increase in afterhours instant messaging; 25% increase in afterhours meetings; as well as a 24%
20

increase in completed pull requests. This suggests that people managers were both doing more to manage their
teams and doing additional IC work. Another internal study found that managers represented a disproportionate
amount of those employees who had experienced an increase in both workweek and collaboration hours [151].
These changes to manager collaboration appeared to be explained by a combination of remote work and the fact that
they were working during a pandemic, and by comparing managers who were new to remote work with managers
who were already working from home. A different study [182] found that remote work specifically increased
managers’ scheduled meetings by 5%. A study looking at Microsoft customers similarly found that increases in
business planning and direct report reach-outs had a hefty impact on managers’ collaboration hours [6]. A
potentially concerning trend for managers is the possibility that this additional workload will not subside with the
return to the office. In Microsoft China, where employees have begun to return to the workplace, the return-to-work
period has seen manager 1:1 time climb even higher than during the fully remote period [176].
2.2.6 The effect of remote work differed across roles and individual characteristics.
Remote work disrupted the ways that people spent their workdays, and the changes – like the changes in reported
productivity and satisfaction – differed by role [151,182]. Certain workers and types of work were more affected by
the transition. According to an external survey [35], people’s ability to focus was impacted by childcare
responsibilities, compared to those without childcare responsibilities. There was also a gender divide – more female
caregivers (26%) found it extremely difficult to focus, compared to 10% of male caregivers.
Causal inference on telemetry data [182] shows that while scheduled meetings for Microsoft US employees
increased, the effect attributable to an individual working from home – as opposed to COVID-19 more broadly – is
actually negative (-4%). Remote work increased unscheduled call hours (+112%), emails sent (+2.6%) and instant
messages sent (+30%). For individual contributors, the total of scheduled meeting hours + unscheduled call hours
remained flat, while unscheduled in-person interactions necessarily fell, implying a drop in synchronous
communication time. This is consistent with prior literature [1] showing that people tend to exchange less
information when moving to remote. These effects also varied across roles: they were significant for people
specialized in sales, marketing, program management, and business support, but were insignificant for researchers,
scientists, and software engineers [182].
The previous chapter on Collaboration and Meetings provided more information on how different types of meetings
have been affected by the shift to remote work.
Individual characteristics also appeared to affect how well people were able to focus and collaborate effectively
while working from home. Some challenges were particularly acute for neurodivergent professionals (such as those
with autism, ADHD, learning disabilities, or psychosocial disabilities), where sensory stimuli in the home office,
workspace setup, and getting into the mindset of working when surrounded by home could all make it difficult to
focus [100]. Actions neurodiverse professionals took to mitigate some of the challenges included avoiding placing
their desk near a window to avoid mind wandering, using timers to prevent time agnosia (inability to perceive
passage of time), using fidget spinners to help remain focused, and creating spatially separate locations for work and
life (e.g., not working in the bedroom) to compartmentalize their thought processes. Many neurodiverse individuals
worked overtime (12-14 hours) to perform their individual focused work after combating all the attentional
challenges. The flexibility that the option to work from home offers also made work more accessible to some people
with disabilities, by avoiding mobility challenges around commuting, affording more flexible scheduling, and
allowing people to have more ability to customize their work environments [163].
Video collaboration elicits a diverse range of accessibility issues. Because video calling (like remote collaboration
technology in general) relies heavily on the visual channel, it presents obvious challenges to people who are blind or
low vision. However, video calling is vital to people who rely on lip reading, especially since the pandemic response
afforded capturing frontal views of each individual, which is actually better than the view one gets in a meeting inperson. It can also be challenging for neurodivergent professionals; they often prefer having their videos off as they
occasionally perform certain activities to remain stimulated (e.g., fidgeting, pacing back and forth) or to calm down
(e.g., petting a stuffed toy) during a meeting. These activities can be misconstrued as lack of attention or can cause
distraction for other attendees. Turning off video means that they do not need to “pass” as paying attention during a
meeting [100]. See Chapter 6 on the Societal Implications of remote work for additional discussion of how
professionals with disabilities are being impacted.

21

Collaboration difficulties can also decrease the productivity of focus time. For example, in external interviews, some
people reported that they had more flexibility to focus on their solo work during the day, but the focus in isolation
sometimes led to misalignments and the need to redo tasks [15].
The previous chapter on Collaboration and Meetings provided more detail regarding general changes and variations
in collaboration patterns.
2.3 Challenges and Benefits Are Closely Linked
2.3.1 Remote work provided flexibility during the pandemic while also blurring the work-life boundary in
problematic ways.
Flexibility was reported as an important benefit of working from home across surveys in different geographies, both
inside and outside of Microsoft [26]. Many people whose flexibility increased used it to interweave life and work
(e.g., do a load of laundry between meetings, take time to cook a better lunch, or move more during the day)
[26,46,69,128,156]. In one study, a Microsoft employee expressed appreciation for having the ability to create their
own work schedule: they liked, for example, being able to split the work day into a morning block and a late
afternoon block with two hours in between to recharge and take care of home duties [66].
However, as seen in prior research on remote work [1], the downside of the flexibility of remote work, particularly
when it involves working from home, is the blurring of the boundary between work and home life that comes from
the elimination of physical boundaries separating the office and home – as well as the temporal boundary afforded
by a commute [26]; in a survey of US Microsoft employees, 72% of those who said flexibility is an important
benefit also said that “lack of boundary between work and personal life” was a challenge in working from home.
Information workers internal and external to Microsoft reported feeling ‘always on’ and having a difficult time
switching off [26,128,156]. Many find it challenging to manage household chores, the immediate needs of
dependents, and work meetings all at the same time in the same space [22,26,69,128,156]. A reminder that everyone
is experiencing the pandemic differently from a survey commissioned by Microsoft in August 2020: a higher
proportion of information and firstline workers in India, Brazil and Japan (>37%) say the lack of separation between
work duties and personal obligations has negatively impacted their well-being compared to those in the US, UK and
Australia (<26%) [154].
People also reported missing the time for quiet thinking and listening to podcasts that was afforded by their
commutes [26]. A study with external business decision makers found that leaders and managers were aware of
these challenges [62].
Unfortunately, some people taking advantage of the flexibility (e.g., to manage caregiving responsibilities during the
day and work in the evening) can make it hard for others to maintain work-life boundaries: respondents in multiple
surveys reported that the work patterns of collaborators can impact their ability to maintain temporal boundaries
between work and personal life as increasing number of work-related emails and messages are sent after hours
[26,100]. Some people reported adapting their practices to remain productive – they replaced old routines and
notions of boundaries with new structures and rituals to condition for productivity, e.g., dressed up formally even
while working from home to set the tone for productivity, or included micro mental breaks to help with context
switching when meetings are stacked [15]. Some neurodivergent survey respondents reported trying to keep nonwork related artifacts out of sight during work time to maintain the boundaries of work and non-work [100]. There
was evidence of adaptation as people settle into long-term remote work in an OXO study: the number one reported
challenge after 20 weeks of remote work was “work” while challenges such as “distractions” and “work-life
balance” became less common [26].
See Chapter 5 on Devices and Physical Ecosystems for additional discussion of physical boundaries.
2.3.2 Non-work distractions increased, whereas work-related distractions decreased for many.
About half of Microsoft software engineers and program managers surveyed said they had experienced an increase
in non-work related distractions (e.g., children, laundry, TV) [46]. In an external survey, over 65% of the
respondents reported that they find it difficult to concentrate during remote work due to external interruptions [35].
In a different external study, people specifically reported challenges in carving out time to focus [156]. This is
consistent with prior work: “Interviews with telecommuters have suggested that the ability to avoid distractions is
important to being effective as a remote worker.” [58]. Non-work related distractions can be particularly problematic
for neurodivergent individuals in a home-office setting [100]. They strive to keep workspace and personal space
completely separate so that they do not get distracted by non-work related items.
22

The picture for work distractions is more mixed. Studies have found an increase in IMs among Microsoft employees
and information workers in an external survey reported that the messaging was disruptive [156,182]. However, 40%
of US Microsoft employees surveyed said they have fewer work-related distractions while working remotely, and
only 21% said they have more [46]. Microsoft employees in China also reported the ability to focus as a big benefit
of remote work. In an OMEX study [181] some Microsoft employees reported that working from home allowed
them to focus more, but a hybrid approach would eventually be most beneficial as some tasks might be better
performed at home and other tasks are more suitable in the office (e.g., collaboration).
For neurodivergent professionals, work-related distractions can originate from the remote meeting platforms in ways
that do not affect neurotypical people [100]. For example, visual background or noise from meeting partners’ can be
particularly distracting to neurodivergent people. Some virtual backgrounds can be distracting for neurodivergent
individuals as they can get fixated on the background and lose focus on the meeting content [100]. The increasing
number of notifications also create additional challenges for neurodivergent individuals; they often turn off
notifications to maintain their focus on their ongoing activities [100], but that can result in missing time-sensitive
information, as also shown in past work [78].
The previous chapter on Collaboration and Meetings discussed the potentially distracting role of meeting chats and
other forms of multitasking. We discuss the childcare challenges specific to COVID-19 work from home later in this
chapter.
2.3.3 Many workers felt collaboratively and socially isolated.
People are missing casual water cooler conversations and reporting increased feelings of isolation and lack of
connection [5,22,26,69,128,156]. In one employee survey “Isolated”, “Disconnected” and “Lonely” were amongst
the top words Microsoft employees used to describe how they were feeling [128]. New hires may face heightened
risk of isolation: data on software engineers shows recent new hires have fewer collaboration hours and smaller
networks compared to new hires who joined Microsoft before the pandemic [69].
A study on Microsoft workers from India found that it was primarily those who were new to the workforce who
thrive on the community experience and are missing working in the office the most [83]. In other internal surveys,
46% of respondents said that their needs for spontaneous interaction were not being met and a majority of
respondents considered all types of social meetings to be least effective [138] . Many neurodivergent professionals
do not enjoy online social meetings, because often a few people do most of the talking (often those who start the
meeting) and their topic of interest may not align with everyone [100]. Also, the absence of organic side
conversations in remote calls (breakout rooms are more formal) makes participation more difficult, if the main topic
of conversation is not interesting [100].
In a global study by Qualtrics and SAP, 75% of people say they feel more socially isolated since the outbreak of the
pandemic. In an HBR report, 1 in 3 employees say their team does not maintain informal contact (e.g., asking how
each person, team, etc. is doing) while working from home. People who are lacking in informal contact are 19%
more likely to report a decline in mental well-being [143]. Another survey found that people without caregiving
responsibilities are feeling more isolated than those with such responsibilities [35]. Information workers often found
communication tools to be a poor substitute for in-person connections [156]. Earlier in the post-COVID period many
meetings included a check-in time to socialize or talk about mental, emotional and physical well-being. These have
since largely gone and are being replaced by intentional meetings for this purpose, but due to video conferencing
being draining, people are choosing not to attend these social meetings and losing out on the social opportunities
entirely [138]. An internal study found many people use gaming to try and build social capital and are gaming more
often. They also found many people (50%) are reporting doing more social capital building activities, with the most
common being listening to coworkers who need to talk [138].
A study that analyzes telemetry data [182] also shows that people are more collaboratively isolated when working
from home: more focused time and less meeting time. In a global Microsoft survey in April, 42% of employees
reported feeling less connected (22% more) and 32% feel they have fewer opportunities to collaborate during
COVID-19 (24% more); particularly employees with less prior remote work experience, those in management and
those in Puget Sound and Engineering feel less connected (>50%) [128]. In a separate study, the share of individual
contributors who reported favorably on their team connectiveness dropped from 90% in April to 74% in December;
for managers it drop from 95% to 83% [110]. Prior work suggests that these feelings of increased isolation are not
due solely to COVID-19 and quarantine. A number of studies on telecommuters prior to COVID-19 reported that
remote workers feel socially isolated from their colleagues [116,135], with in-person interaction in the office being
23

most important for maintaining workplace friendships [150]. Workers on crowdsourcing and freelancing platforms
like Mechanical Turk or Upwork, where remote work is the norm, often form off-platform social networks to
provide each other with companionship and social support. More generally, the evidence suggests that long-term
ubiquitous remote work negatively affects relationships among coworkers and teams [1,12]. Telemetry from Surface
devices around the world has shown an increase in audio website and app usage, driven largely by communication
apps, while entertainment usage has decreased since the pandemic [64]. In Western Europe, we saw an increase in
IMs that did not decrease when they returned to a hybrid office [151]. Across Microsoft we saw an increase in
emails marked as “focus” during the beginning of the pandemic, but this has since reached a new low baseline. On
the contrary, Teams usage has gone up and stayed up [166]. All of this suggests people are looking for more ways to
communicate and are using a variety of methods (emails, Teams, Zoom, WhatsApp, etc.) to do so while remote.
2.3.4 Remote work provided some benefits for worker health, but also many challenges, particularly with regard to
well-being.
In addition to increased flexibility, working from home has created other quality-of-life benefits for many. Less time
spent commuting, more time spent with family, reduced health risks from the pandemic, and improved diets were
some of the benefits mentioned in internal surveys [26,46,128]. Some people also reported more opportunities for
micro-exercise (e.g., yoga during Teams meetings with the camera off or walking 1:1s over the phone), but others
felt they had become more sedentary [26]. In the OMEX study [181] some people reported that inclusivity had
improved as team members were more tolerant of differences in working style.
In contrast with the above benefits, some employees and external information workers reported feelings of stress and
a feeling of always working [26,128,156]. About 85% of the respondents in an external survey of US-based
respondents including technology professionals, academics, marketing and public relations professionals said that
they feel nervous and stressed [35]. People are also reporting being more overworked as remote work continues
[26]; this may be aggravated by people not taking vacation since COVID-19 means they cannot travel and reporting
having a harder time getting back into work when they do [26]. Survey respondents and researchers question
whether the current work pace is sustainable and raise concerns about long-run burnout [26]. A couple of days in
May were designated “COSINE Health Days”; it seems that about two-thirds people actually took the days off and
many were appreciative: “I didn’t realize how badly I needed a break” [69].
A global study of over 2,700 employees across more than 10 industries undertaken by Qualtrics and SAP during
March and April 2020 showed that since the outbreak of the pandemic, 65% of people report higher stress, 57% are
feeling greater anxiety, and 53% say they feel more emotionally exhausted [143]. The same study showed that 40%
of people at every seniority level of a company have seen a decrease in mental well-being [143], while another study
of 1200 US full-time employees conducted by Ginger, the leader in on-demand mental healthcare, showed that 70%
of workers said the pandemic has been the most stressful time in their careers [81]. From a survey commissioned by
Microsoft in August 2020, over 30% of information and firstline workers say the pandemic has increased their sense
of burnout at work. This number jumps to 44% in Brazil and drops to 10% in Germany compared to 31% in the US.
The same survey found that causes of workplace stress differ between remote and firstline workers: lack of
separation between work and life and feeling disconnected from co-workers are the top 1 and 2 stressors for remote
workers, while the inability to socially distance/worry about getting COVID-19 and unmanageable
workload/workhours are the top 1 and 2 stressors for Firstline workers. 70% of information and firstline workers
surveyed said they think meditating could help them decrease their work-related stress. Again, this number jumps to
92% in India and 84% in Brazil, compared to 73% in the US and 53% in the UK [154].
Challenges in having to adapt in-person practices through new digital tools that may result in broken workflows also
contribute to mental stress and exhaustion. Survey respondents reported that technical challenges resulted in more
annoyance and frustration compared to in-person work, as information workers were relying so heavily on digital
tools to get their work done [156].
In addition to mental stress, there is the additional physical stress on the body from remaining in one place, as
people no longer need to walk between offices, or walk as far to the restroom or to get coffee, etc.
[26,46,128,149,163], and this is causing physical pain [26,128]. People are complaining of their eyes being sore
from staring at the screen; stiffness; aches; carpel tunnel pain; and back issues [26]. In a study of external workers,
90% reported spending more time on their electronic devices [35]. People are reporting not moving for an entire day
except for bio breaks or to get food, and this is concerning knowing the negative effects of spending most of the day
sitting (increased risk of high blood pressure, blood sugar concerns, cancer, and even premature mortality) [1]. The
decrease in movement may also be aggravated by COVID-19 causing gym closures – in one survey 75% of
24

respondents said they were getting less exercise than prior to the pandemic [35]. The potential long-term health
implications of ubiquitous remote work are serious but under-researched [1].
Lastly, brain scan-based studies provide some evidence that virtual meetings require more cognitive load, but that
the Teams Together mode may reduce load relative to the traditional grid view and could help eliminate online
meeting fatigue [79]. Another study found that an “attentional spotlight” of the audience based on their affective
responses provided presenters with a better notion of how their talk was going, and where there was agreement or
questions/confusion relative to the current Teams’ grid view of the audience or a randomly chosen spotlight of an
audience member [118]. This reduced the cognitive burden and stress from not being able to “read the room” or
know how your presentation was accepted. The previous chapter on Collaboration and Meetings discussed how the
increase in virtual meetings added to both physical and mental stress.
Chapter 5 on Devices and Physical Ecosystems describes more research on the specific physical effects of working
from home.
2.3.5 Employees worried that their hard work would not be visible to their managers.
Microsoft employees and external information workers have expressed concerns about the need to “look productive”
and the fact that their work is now less visible to their manager or team [26]. This may be aggravated by job security
concerns resulting from COVID-19’s effect on the economy, but it is also expected from the prior literature on
remote work: physical presence in the office is a typical means of signaling “work devotion,” and remote workers
before the pandemic frequently felt the need signal devotion in other ways (e.g., by working longer hours as
discussed earlier) [54,122]. In this vein, while some Microsoft employees appreciate the benefit, some have
indicated reluctance to take the Paid Pandemic School and Childcare Closure Leave [26,69]. One benefit of a
stronger desire to see and be seen may be that people are being more open to ask for help and there are more open
discussions [15].
While employees are being more demonstrative about work due to concerns about job security, a survey of external
business decision-makers found that leaders want to use KPIs and project completion to evaluate employees and are
not interested in monitoring employee behavior [62], suggesting that at least in some cases, employee concerns
about looking productive may be unwarranted. These leaders are already speculating about how to best assess
productivity and performance in a new “flexi-work” or “hybrid” work environment [62].
2.3.6 Conversely, there was increased concern about how their work did show up.
While people worried their work would not be visible, they also expressed increased concern about the fact that
traces of their work often persisted. Because technology mediates more of the work a person does when working
remotely, more interactions can end up being recorded, including written text (e.g., email or IM) and video (e.g.,
remote meetings). This made some employees more hesitant to ask potentially stupid questions while working
remotely, and when they did ask questions they sometimes spent a lot of time on wordsmithing to make sure the
question was clear (since clarifying can harder when not co-located) and made them look good [26].
“Working from home also takes away the easy access to colleagues nearby for a quick question or a "hallway
meeting". Yes, the tools to attempt to replace that are available but aren't perfect replacements. Everything is
recorded in writing (chats) or I'd have to pick up the phone and call which takes a bit more effort so I'm just
less likely to do it.” [160]

The notion of “remote work as surveilled work” gained prominence during the ubiquitous work-from-home period
[145]. Prior literature on remote work has documented employers’ desire to ensure workers are working when
expected [1], but also identified negative effects of electronic performance monitoring, including on employee
productivity, creativity, trust and well-being [11].
2.4 Looking Forward
2.4.1 Roles of managers and leaders are evolving to adapt the challenges of remote work.
There is preliminary evidence that managers may be able to help with any workday length and productivity
challenges: Microsoft employees who received prioritization support from their managers were 2.5 times more
likely to report maintaining their productivity levels and work-life balance in comparison to those who did not
receive prioritization support [110]. A study of telemetry of one organization in the company found that employees
who had the most 1:1 time with their managers saw a much smaller increases in weekly working time (1.5 hours vs.
3 hours) [4]. Similarly, a study of Microsoft employees in Denmark found that the average meeting and email load
decreased as managers’ 1:1 time increased. The inverse relationship suggests 1:1 time enabled managers to help
25

employees prioritize work and resolve issues faster [151]. Research has also shown employees who have more oneon-one time with their managers are less likely to be disengaged [121]. Leadership in OXO instituted a policy to
increase manager check-ins, which had a positive effect on 41% of survey respondents (4% negative) [26].
Managers are critical points of connection in terms of providing holistic support to employees – reducing negative
impact on physical and mental well-being, maintaining morale over reduction in force and so on, suggesting soft
skills of managers are becoming even more important than ever before [62]. Recent research of external decisionmakers has shown that the roles of managers and leaders are also evolving with the changes that remote work
brings: leaders are moving faster to make decisions to take quick action on maintaining business continuity and
stability, but with the potential negative consequences of bypassing regular checks that might emerge downstream
[62].
Alignment of the lived experience of leaders and managers is important to create a working environment that caters
to the needs of employees with different challenges. Senior leaders recognize their role in creating a more
democratized and humanized workplace and set examples of how they show up on video from home as well as
appearing to be more accessible online compared to in person [62].
A meta-analysis of past research showed a positive correlation between remote work outcomes and manager
relationship quality, but since it was cross-sectional the association could be due entirely to the fact that (under
normal circumstances) managers may only allow remote work for employees with whom they have a good
relationship [51].
2.4.2 Where to work once it is safe? Workers report mixed preferences but lean toward a hybrid model.
Multiple surveys have found that, for the post-COVID workplace, most employees want a hybrid model of work in
which people work part-time in the office and part-time from home.
In Microsoft China, where offices have reopened, a large majority of respondents to a survey preferred a hybrid
model of work (69%) compared to purely remote work (19%) or the traditional office model (11%) because it
enabled people to combine the advantages of both remote and in office [176]; the same survey found that 69% of
people thought that they were most productive in a hybrid work model. These numbers align closely with those of a
similar survey from COSINE, in which 65% of employees said they wanted a hybrid model post-COVID (vs. 26%
remote-only and 9% traditional) [69]. Additionally, from the CSEO Global Employee Satisfaction Survey (GESS) in
November 2020, 63% of Microsoft employees ideally want a hybrid model compared to 35% fully remote and 3%
never remote [128]. Similarly, 66% of Google employees want a hybrid model compared to 20% fully remote and
10% never remote [94] For some, these preferences are in spite of concerns that a hybrid model will be harder to
manage and potentially create inequality between people in the workplace and people working remotely [26].
There are differences in how people think hybrid work will work best. In a poll regarding same-room vs. hybrid vs.
remote meetings, Microsoft study participants with prior remote work experience were much less likely to support
“Prioritize same room meetings for which planning is difficult,” suggesting maybe remote workers underestimate
the value of co-location in resolving ill-defined tasks and office workers overestimate it [138]. On the other hand,
there was near-universal agreement on “Prioritize hybrid meetings in which all attendees engage fully” and
“Prioritize same-room meetings which are well-planned so that meetings are efficient.”
Results from outside Microsoft also reveal a preference for hybrid work, although the traditional model does better
in these findings. A survey of US workers found that, post-COVID, 24% would like to work from home all of the
time, 56% would like to work from home at least some of the time, and 20% would like to return to the office fulltime [18]. Interestingly, the preferences of company leaders with regards to hybrid work likely differ from those
of their employees. A survey of firms found that, on average, they only want the percent of working days worked
from home to increase from 5.5% pre-COVID to 16.6% post-COVID [2].
All of the above findings refer to workers’ self-reported preferences for a biologically-safe post-COVID world. In
the short-term, people are less positive about returning to the office, whether that is in a hybrid or in a traditional
model. In May 2020, Microsoft employees expressed concerns, anxiety, and even fear around returning to the office
given the challenges of social distancing. Some specifically mentioned they will not return to the workplace or travel
until there is a COVID-19 vaccine. In November 2020, despite soft openings across many regions, 94% of Microsoft
employees continued to work from home full-time (80% across Asia region) [128]. In an external survey of
information workers, 78% of respondents reported that they did not want to return to the workplace yet and that
cleanliness of the workplace is an important factor for them in deciding whether they want to return [35].
26

Even pre-COVID, the desire for location flexibility was prominent among young people. In a global external survey
of youths aged 16-25, 72% agreed that “My ability to choose how and when I work impacts how satisfied I am with
my job” (11% disagreed). In the same survey, 63% agreed that “I can be a productive and effective employee for an
organization without going to the workplace every day” (18% disagreed) [103]. However, many young people rely
on the office for socializing as well, meaning hybrid may still be preferred by them to fully remote work [56].
2.4.3 Business decision-makers are considering long-term changes.
Chapter 6, which covers Societal Implications, will discuss some long-term implications of companies planning for
a future with more remote work, including changes to real estate footprint and use of freelancers. Some business
leaders are being empathic in deciding who should return to work with special consideration of the physical and
mental well-being of the employees [62]. However, planning for the hybrid model is logistically complex – and
reorganizing the physical environment to support distancing needs was identified as a goal by business leaders [62]
and as a need by employees [35]. Employee well-being is quickly becoming a key priority for employers – listed as
one of the top 5 business priorities in FY21Q1 by roughly a third of Microsoft’s global customer and partners [33].
There is a latent desire among IT and Business decision makers for metrics to provide a broad understanding of the
well-being, productivity and collaboration of the employee base – without intruding on privacy [42].

27

3 SOFTWARE ENGINEERING EXPERIENCES
By Brian Houck, Chandra Maddila, and Peggy Storey
3.1 Introduction
While we have looked at the personal productivity and well-being experience for information workers in general, the
software engineering experience is of particular interest to Microsoft, both because Microsoft employs a large
number of software engineers and because we work closely with the developer community through GitHub and our
partner ecosystem.
Developer productivity is a complex construct which cannot be explained with simple metrics such as lines of code
alone [88]. Several pre-COVID studies showed that developer productivity may refer to time spent designing new
features, writing code and documentation, reviewing code written by others, meeting with team members and end
users, and many other tasks [108]. Objective measures from engineering system telemetry data are important signals
of engineering productivity, while self-reported measures of developer productivity and satisfaction are also needed
to understand the entire engineering experience, especially in times of significant change [158].
3.2 Productivity, Satisfaction, and Work Patterns
3.2.1 Engineering output measures were stable or showed an increase when moving to remote work.
Key metrics of developer activity were flat or showed a small increase in the months following March 2020. This
was true both for software engineers at Microsoft [47,69,99,152] and contributors to projects hosted at GitHub [47].
Metrics that stayed stable or improved include:
•
•
•
•
•
•

Number of pull requests created or closed,
Code review activity,
Number work items like tasks, bug fixes, new features,
Documentation activity,
Average lifetime of pull requests, and
Size of the pull requests.

Pull Requests

A quantitative study of engineering data conducted at MSR [99] showed that a greater number of pull requests were
created and closed March through June 2020 compared with the same time frame in 2019 and 2018, as shown in
Figure 3. Though there was an increase in number of pull requests created, the average age of pull requests seems to
be comparable across these two time periods (30.7 hours in 2020 vs. 30.92 hours in 2019). The size of the pull

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50

Week of the Year
2019

2020

Figure 3: Weekly pull requests over time.

28

requests (number of files edited through a pull request), which is a proxy for complexity and magnitude of changes,
was also observed to be consistent with previous years. It was also observed that the number of new repositories
created was slightly lower in 2020 as compared to 2019 and 2018.
When drilling into one engineering organization at Microsoft, the Core Operating Systems and Intelligent Edge
(COSINE) organization, Cosine researchers observed that increases in completed pull requests were the result of an
increase in total hours worked and improved efficiency per hour. In COSINE, pull requests completed per hour of
active development increased by 1% compared to the same period in the previous release cycle [69].
An important metric of the quality of developer activity is the type of work item completed, such as, for examples,
new features or bug fixes vs. refactoring or other trivial maintenance activities. There was a slight increase in the
number of bug fixes and new tasks created (18.1% increase in bug fixes and 15.67% increase in ‘new tasks’) postCOVID as compared to previous years. Code review activity remains consistent with previous years, with 78.4% of
code review requests are completed in 2020 compared to 79.8% in 2019 and 83.08% in 2018. This indicates that
developers were contributing to their team by ensuring that the quality of others’ code remained high. Other related
studies in OXO [26], COSINE / Azure Edge + Platform [69], Experiences and Devices [152] show similar trends
across different organizations and teams.
In addition to the studies mentioned above, which look at the Microsoft software engineering experience, a similar
study was conducted at GitHub on open source projects and paid organization accounts [47]. The GitHub study
reinforces the finding that developer activity remained largely consistent or increased in 2020 compared to previous
years. A 17% increase was seen in pull request volume and 16% increase in push volume. Also, there was a 27%
increase in the number of new opensource projects compared to previous years. An external study of engineering
system output conducted at Baidu, one of the largest IT companies in China, found that engineering output was
more stable with software engineers working from home than onsite [12].
3.2.2 Self-reported productivity suggests a more mixed picture than developer activity metrics.
In addition to engineering system telemetry data, engineering productivity can also be assessed using subjective
measures, such as a developer’s perceived productivity [158]. While telemetry metrics suggest that developer
productivity was stable or increasing at Microsoft and elsewhere post-COVID, findings from a survey in mid-March
of 1387 Microsoft engineers (developers, program managers, engineering managers) shows a more nuanced picture
when it comes to self-reported perceived productivity [46]:
•
•
•
•
•

8% indicated they felt significantly more productive since working from home,
22% felt more productive,
32% felt about the same,
32% felt less productive, and
6% felt significantly less productive.

Engineers’ responses to the survey further indicate that their perception of time spent on engineering activities –
creating and completing pull requests, creating documentation, engineering design work, feature development and
bug fixes – remained ‘about the same’ or has ‘slightly increased’ [46].
In the internal survey [46], developers and program managers were asked to explain their change in productivity
through an open-ended question; Figure 4 shows the main themes that emerged from coding a sample of 400
responses. For engineers that self-reported higher productivity, one commonly reported reason was having fewer
work interruptions and being able to focus on their engineering work. Past research also found that having fewer
interruptions was important for improving development productivity [108]. Telemetry data supports this perception;
one organization of 4500 engineers found the average length of uninterrupted focus within an IDE increased by 6%
post-COVID compared to the same period in 2019 [69]. For engineers that self-reported lower productivity, having
poor equipment and slow connections was reported to negatively affect their productivity and that a lack of informal
communication and waiting for others to complete engineering tasks were factors [46].

29

Figure 4: Reasons for higher or lower self-reported engineering productivity.

The themes that emerged from this internal engineering survey resonate with previous research where many factors,
the majority non-technical, are associated with different levels of reported productivity and developer satisfaction
[119,157]. Some of the most important factors reported in this previous research included job enthusiasm, team
culture, peer feedback, autonomy over one’s work, quality of the engineering system and work environment.
Murphy-Hill et al. also noted in their study of developer productivity across several organization that the factor “use
of remote work to concentrate” had the lowest variance across all the studied companies [119]. New factors that
emerged the survey post-COVID include less time on commute (for increased productivity), and home distractions
(for reduced self-reported productivity).
3.2.3 The increased engineering output seems to have come with increased burnout.
“It’s seems to be getting more and more difficult to be productive. And I feel pretty
worn out. It could be because I worked most of last weekend?” [26]
“Trying to do that best job I can, it’s just so much more work” [69]

As nearly ubiquitous remote work continues, engineers are increasingly expressing feelings of being “overworked”:
feeling burnt out, not being able to stay on top of email, and feeling overwhelmed [26]. In a survey of Microsoft
engineers and program managers, 49% said they were working more hours than prior to the pandemic, with only 9%
said they were working fewer hours [46]. This survey also found developers reported spending more hours on
development tasks, including individual coding tasks as well as tasks that contribute to their team such as code
review and documentation creation. This increased workload (real or perceived) may be compounding these
expressed feelings of burnout [46]. An external survey with more than two thousand developers worldwide in the
early weeks of the pandemic, found that developers’ productivity and their well-being are suffering following the
rapid shift to remote work. Dealing with the pandemic and home office ergonomics affected well-being and
productivity, and women, parents, and people with disabilities may be disproportionately affected [133].
The GitHub developer study shows longer workdays post-pandemic were not unique to Microsoft. Developer
activity in private and public GitHub repositories showed longer workdays, including on the weekends [47].
Qualitative interviews done with internal Microsoft engineers suggest that these longer working hours were not
sustainable and contributed to existing or impending burnout [26,69].
Collaboration challenges may also contribute to burnout, as one survey respondents noted: “It is challenging to have
good visibility on the impact of my work” [46]. An increase in the number of meetings and other collaboration
challenges were also seen as ongoing pain points for engineering teams [26,46]. An increase in meeting time is
reported in other studies, as well. For example, half of the respondents in the CSEO study report that they are
spending more time in meetings (51% more time vs 12% less time) [128]. See Chapter 1 on Collaboration and
Meetings for more details.
“I didn’t realize how badly I needed a break” [69]

30

One organization attempted to help address the increased burnout by taking two “Health Days,” which resulted in a
four-day weekend. Pull request volume for this four-day span was only 30% the average volume seen over the
previous nine weeks, indicating high participation in the shared break. However, the two weeks following the Health
Days had pull request volumes 15% higher than at the same point in 2019, which may suggest the extra days off
provided some relief to burnout [69].
“I want to focus on my team, because that’s the work I find most rewarding, but there’s still all the same
expectations on my other work” [69]

Engineering Leads appeared at particular risk of being overworked. In a study of the COSINE organization, people
managers completed 24% more pull requests per person than they did during the same time period in 2019, which
indicates a substantial increase in individual activity. Those people managers also spent 50% more time in time in
1:1s per direct report than in 2019, even though the average number of direct reports had only increased by 8%. That
increase in both people management work, as well as increased individual engineering output resulted in a 25%
increase in after-hours meetings and a 309% increase in afterhours IMs [69].
“Onboarding new hires and interns. It’s been a challenge to make sure they’re getting everything they need to
be successful. There’s a bigger time sync to get people ramped up, and it’s harder to delegate some of these
things.” [69]

It appears there is a risk of people managers being overworked and this having negative consequences for
onboarding new hires, although other studies suggest a more nuanced picture. More on this can be found in the next
section.
While this chapter focuses on developers, these findings are consistent with other populations. See the previous
chapter on Personal Productivity and Well-being for a more general view of well-being associated with information
workers, and the upcoming chapter on Societal Implications for a discussion of the downstream impacts of largescale burnout across many organizations.
3.2.4 Collaboration output measures were healthy, but engineers who experienced collaboration challenges
reported lower personal productivity and lower team productivity.
In collaborative projects, pull requests and work items are how developers “tell others about changes they make to a
repository” [47] and issues are an important mechanism for communicating and planning work [47]. Code review
and documentation activities are also important signals of engineering productivity at a team level. Engineering
output measures for collaboration practices post-COVID were stable or showed an increase over time for both
internal and external developers. For internal Microsoft engineers, pull requests and work items were either stable or
showed an increase over time [69,99,152]. Code review and documentation edits also increased internally [69,99].
For external developers, the time to merge pull requests became shorter for open source repositories hosted on
GitHub, with a spike in distinct collaborators for open source projects [47]. Data from enterprise repositories hosted
on GitHub showed an adjustment period to remote work where a drop in issues has been followed by a return to
previous levels from before COVID-19 [47].
Although these signals showed stable or even an increase in engineering output at the team level, collaboration and
communication challenges were associated with reported decreases in perceived productivity (one third reported a
decrease) and team productivity (one quarter reported a decrease). Specifically survey respondents who reported a
decrease in “Communication ease with colleagues”, “Effectiveness of communication with colleagues”, “Quality of
scheduled meetings”, “Positive interactions with their team”, and “Knowledge flow within their team” were more
likely to report lower (perceived) productivity, team productivity and work satisfaction [46].
Engineers and program managers without prior remote experience were more likely to report a decrease in
productivity; perhaps surprisingly, people with fewer meetings and fewer interactions with people in general were
also more likely to say their productivity had decreased [46]. This may be due to them having fewer or lessestablished social connections.
3.2.5 Onboarding software engineers during COVID-19 presented new challenges.
A study in Azure found that new hires who joined since the start of mandatory work-from-home were producing
34% fewer pull requests per-person in their first 90-days than new hires during the same period in 2019. For entrylevel software engineering new hires, 24% completed zero pull requests in their first 90-days, and only 16%
completed their first PR within their first two weeks of joining Microsoft (a decrease of 4% from 2019) [70].
“Not feeling especially connected to the team…” [141]

31

A Microsoft survey of software engineering new hires within part of the Azure organization during COVID-19
found that only a third felt socially connected to their team. Forty percent said they did not have at least one 1:1
communication from someone on their team daily [141]. They also communicated with 33% fewer people overall,
attended 11% fewer meetings and met with their direct manager 17% less than new hires who joined in the six
months immediately prior to the move to remote work [70].
Frequently cited concerns from these new hires about their onboarding experience included lack of 1:1 connection
with mentors, managers (both direct and skip-level) and their colleagues [182]. There is good news here, however:
recent research from a company-wide survey suggests that those new hires whose manager was actively involved in
their onboarding were substantially more satisfied with their onboarding experience [111,141].
There are teams that appeared to have more success at building connectedness for their new hires. Microsoft’s
Atlanta site, for example, supplements the standard New Employee Orientation (NEO) with an additional NEO
activity called “New Employee Atlanta” entirely devoted to culture and building a sense of community. They also
hold “Quarterly Social Breakouts” to continue this community building on an ongoing basis. These investments
appear to have helped with onboarding, with software engineering new hires who onboarded to one of the Atlanta
teams communicating with 28% more people, spending 15% more time in meetings, and meeting with their direct
manager 16% more than the average Azure software engineering new hire [70]. These community building activities
were originally designed for in-person onboarding but were adapted to remote while those in the Atlanta site
continue to work from home.
“We are creating something special. We want to keep that communal feel, that sense of community.” [69]

3.3 Challenges and Benefits Are Closely Linked
3.3.1 While engineers adapted to remote work and many found they could focus better, they also felt the lack of inperson interactions hindered their creativity.
“In some ways it feels more productive. In terms of engagement on Teams; everyone is really engaged.” [69]
“We don’t yet have an awesome replacement for getting the right nerds in a room at the same time, with a
whiteboard” [69]

Many engineers reported that working remotely allowed them to focus more effectively on their engineering work as
unscheduled work interruptions (referred to by some as “drive-bys” and “randomizations”) disappeared [46].
However, engineers also reported missing in-person interactions (especially the use of whiteboards) and informal
communication around work (e.g., in hallways, in team rooms and around the watercooler [69]). They described
these informal interactions as being particularly important for sharing information, building relationships, and
creating awareness about engineering work [46]. Lack of awareness of what colleagues are working on and a
decrease in the ability to brainstorm with team members were both found to be associated with lower perceived team
productivity [114]. To some extent, virtual standups, lunch, and coffee breaks helped fill this gap [46,69], but they
still reported that “non-verbal communication in meetings [was] more challenging” [46] and a lack of personal
information cues, such as standing up when a meeting has ending, impacted on meeting quality [26]. These were
discussed in greater detail in the earlier chapter on Collaboration and Meetings.
While engineers reported difficulty replicating these in-person interactions virtually, some found the new
alternatives more inclusive. For example, one person said, “Hallway or whiteboarding conversations, I actually find
those situations so much better now because we have to record things and with people sitting by their computer you
have to be a little more aware about giving people space to speak and that becomes a little more democratic” [69].
Respondents to internal surveys also reported that they found a lack of in-person interactions hindered their
engagement and lowered their engineering creativity [26,46]. Figure 5 illustrates how OXO engineers’ self-reported
ability to do work that involves new ideas, goals and big picture thinking decreased when they moved to remote
work [26].

32

Ability to do creative/big-picture work during WFH
250
200
150
100
50
0
Much worse

Worse

About the same

Better

Much better

Figure 5: Responses to: “How has your ability to do work that involves new ideas, goals and big picture thinking changed since
the [work-from-home] directive? (In contrast to work that was already planned, scheduled, etc.)” [26].

The pandemic posed a unique set of challenges to software engineers with low vision or who are blind. When
working with other teammates remotely and doing peer programming or live debugging, it can be very difficult to
get the feedback from the user interface and develop spatial awareness. Begel et al. proposed ideas for improving
user interface feedback for low vision or blind software engineers working with others remotely [16]. They found
that transferring visual user interface cues to audio icons that convey cursor movement and direction, as well as
corresponding screen reader output upon item selection, was able to provide the same spatial awareness benefits to a
low vision or blind software engineer as their sighted counterparts.
3.3.2 Software engineers felt gratitude for their team and empathy for remote work.
Although many software engineers reported feeling isolated in the months following the move to remote work, as
well as missing social connections with their team [46] and concern about their team culture [69], many also
reported gratitude for the support provided by their team to them. One respondent noted, “My coworkers are great
people to work with and very patient too” [26]. Empathy for remote workers also grew, as one participant noted,
“Now that everyone’s on Teams, we’re all on equal footing” [69].
3.3.3 Two sides to the same coin: some factors that some engineers saw as a benefit, others saw as a challenge.
There were many challenges with working remotely during COVID-19, but also many benefits that Microsoft
engineers were grateful for [26,46,69]. Many changes to working patterns can be viewed positively or negatively
based on other variables that affect the overall experiences. The previous chapter on Personal Productivity and Wellbeing discussed many of the individual benefits and challenges of remote work. In a study of developers working
from home during the pandemic that was conducted at Baidu (the largest IT company in China), they found similar
benefits and challenges that helped explain increased and decreased productivity [12].
3.4 Looking Forward
Many of the challenges and opportunities what we observe in the software engineers experience echo those from the
chapter on Personal Productivity and Well-being, with software engineers appearing particularly likely to benefit
from the increased focus remote work can provide, while still facing many similar challenges to other information
workers. As we look to the future where workplaces begin to open up again, there is an opportunity to think about
how to design hybrid workplaces that help mitigate the challenges engineers are experiences while still capturing the
benefits.

33

4 IT AND SECURITY
By Matt Brodsky and Adam Coleman
4.1 Introduction
Another specific population that Microsoft cares deeply about includes IT and security professionals. This chapter
looks at how the IT and security professions experienced the pandemic, and shows that these roles significantly
changed as a result of the new security and compliance risks that emerged and the evolving IT needs remote work
created for information workers around the globe.
4.2 IT & Security Organizations Experienced a Major Shift to Remote Work
4.2.1 The vast majority of Microsoft’s commercial customers encouraged their IT and security organizations to
work from home.
In a recent survey [22] of IT admins of commercial (mostly enterprise) Microsoft customers, an overwhelming
majority (104/105 responses or 99%) indicated that their organizations have encouraged their workforce to work
remotely as a result of the COVID-19 crisis. Similarly an additional survey with enterprise customers in IT
organizations, found that almost everyone (98%, n=43) said they were working from home, while most of those
(86%, n=43) used to work on company premises [101]. These findings were reinforced by a separate survey of
enterprise security professionals, including SOC analysts, security admins and CISOs [167]; 95% (n=85) of
respondents reported that their entire information security teams had moved to work remotely as a result of the
COVID-19 crisis. Similar findings were further reported in an analysis of compliance IT professionals who ensure
that their organizations are compliant with internal and external policies and regulations. This study found that most
compliance teams (87%, n=47) had also transitioned to work remotely [106]. Moreover, for the roughly 13% of
compliance IT professionals who indicated that some of their Compliance team remains onsite, the reasons were
related to maintenance of classified systems that are only accessed onsite [106].
4.2.2 A large portion of Microsoft’s enterprise customers were able to adopt remote work environments during the
COVID-19 crisis.
When IT administrators from commercial Microsoft customers were polled in a recent survey [22] with regards to
what percentage of the people in their organization who were able to work remotely, a strong majority of the polled
customers (89.5%) indicated that more than 50% of their organization are able to work remotely. A lesser majority
of these same respondents indicated that more than 75% of commercial end users would be able to work remotely
(64%, 67/105 responses). This observation was quite similar to one found in a poll of security professionals [167]
where a majority of the respondents (77%, n=85) reported that more than 75% of their organizations are able to
work remotely, and further supported by a finding that 83% (n=47) of Compliance IT professionals report that at
least 50% of their employees are able to work from home [106].
4.3 New Security and Compliance Risks
4.3.1 Security threats increased, with phishing attacks experiencing the largest increase.
Security threats increased during the COVID-19 crisis at Microsoft’s commercial customer organizations. In a
recent survey [167], security professionals including SOC Analysts, security admins and CISOs, were polled with
regards to the rates of increase of security threats since the beginning of the switch to remote work. Only 20% of the
respondents said they did not encounter any increased security threats. A majority (62%) of the respondents (n=85)
reported phishing campaigns were the most increased security threats during the COVID-19 crisis. This aligns with
the findings in another recent study by Google [55].
Information workers also reported being worried about increased security threats in a work-from-home environment
[160]. Specifically, information worker concerns appeared to be related to downloading content, accessing work
information on a private WiFi networks that may not be as secure as work connections, and – in line with security
professionals’ concerns – falling victim to phishing scams:
"I only use my work laptop for work related things. But phishing emails are becoming more common during
this pandemic, so sometimes it can be hard to stay alert when an email looks very realistic." – Information
Worker

Information workers said they believed these new concerns would be mitigated by IT if they were still able to work
from the office.
34

4.3.2 Increased remote work surfaced several security-related gaps that increased organizational compliance risks.
In a recent survey on the effects of the COVID-19 crisis on compliance IT professionals, the respondents expressed
that as their organization’s employees moved to remote work compliance risks and threats increased. Specifically,
the use and need for new collaboration tools were reported as the biggest threat to a company's compliance posture
by 45% of respondents (n =47). Additionally, 28% of the polled compliance IT professionals reported that an
increase in the number of devices employees were using to access company data was the biggest threat [106]. Many
of these risks may have existed before COVID-19, but the speed with which companies had to pivot to remote work
shed new light on the potential risks.
For example, here are a few quotations from compliance IT professionals on the compliance issues they began to
encounter due to the increase in remote work:
“Working from home hinders the ability for real time status updates between compliance and all other
departments. Enforcing compliance is also hindered, as many employees remote connect from their own
devices.“ - Compliance survey respondent
“The main issue is forcing compliance on individuals who previously did not work remotely. Cloud storage of
classified information is not allowed. All data must be stored on premises. Individuals try to use commercial
options, like OneDrive, which is a security risk.” - Compliance survey respondent

4.4 Specific IT challenges
4.4.1 Poor internet performance and not having the appropriate equipment were major problems for the
commercial workforces while working remotely.
An online survey was conducted to learn more about the changes IT organizations made over the first few weeks of
the COVID-19 crisis and how their IT admins coped [22]. The IT admin participants ranked the most common
issues encountered by their end users. The polled customers indicated that poor internet performance and not having
the appropriate technology or equipment were the most common problems for the workforce while working
remotely. Similar results were seen when enterprise customers involved in IT decision making were polled as part of
the Microsoft Compass program; these participants included “Network and connectivity” and “Enabling devices for
remote use” as major tech issues as a results of the COVID-19 crisis [101].
On their most common issues encountered by their end users, IT admins report:
"Ensuring they have all the available tools necessary to work effectively while remote. As remote work was
actively discouraged at our company prior to the COVID-19 outbreak, most users did not have things like
headsets (For Teams)." – IT admin respondent
"Adoption of tools in remote worker settings and adjusting to different type of work environment with child
care in some cases." – IT admin respondent
"Remote connectivity/home network provider bandwidth. Most individuals are used to dual monitors in the
office and at home are working from a single laptop which may not have an external monitor connected." – IT
admin respondent

More information about many of these concerns can be found in the chapters on Collaboration and Meetings,
Personal Productivity and Well-being, and Devices and Physical Ecosystems.
4.4.2 Adequately educating end users about best practices for working remotely and training them to effectively use
remote tools emerged as some of the most prevalent problems for IT admins, security professionals, and compliance
IT specialists.
One of the biggest issues IT administrators faced as people moved quickly to remote work involved educating
customers on how to use remote software and best practices around working remotely [22,101,167]. Large portions
of the workforce had never been expected to work remotely, at least to the extent that was required post-COVID,
and thus were not properly trained, shown how to access appropriate tools, or given specific guidance for working
from home [62]. With no physical offices, classrooms, or in-person interactions, many end users experienced a steep
learning curve. For IT staff extra priorities they have assumed include training end users on productivity apps or
enabling devices for remote use [101]. In one survey IT admins reported that “Training for Remote Best Practices”
was the most prevalent problem for admins when it comes to end user education [22].

35

Similarly, end-user security education with secure remote access was perceived as the most long term impacts of
COVID-19 crisis by the security professionals (37%) and many security professionals had an increased workload
specifically educating end users [167], as seen in this quotation:
"I spend a lot more time helping people connect remotely which gives me less time to do my daily work."Security Professional

This finding was further echoed in a series of customer interviews, where representative IT admins employed in
enterprise, small and medium businesses, and educational organizations all expressed the need for educators to have
access to tutorial videos on using Microsoft Teams in order to properly have a remote workforce [23].
“…teachers do not know how to fix Teams issues. What has been helpful is that our IT team sends tutorial
videos.” - Edu IT Admin

4.4.3 IT admins struggled to provide adequate support to their end users.
IT admins have reported difficulty providing remote support to their end users and that some IT issues need to be
resolved in person. In a series of IT admin interviews regarding struggles encountered since the COVID-19 crisis
began, multiple IT admins expressed difficulty providing remote support to their organization’s end users [23]. This
echoes findings described in another survey where 46% of IT admins reported that they have had issues providing
their people with support as a result of the COVID-19 crisis [22]. Additionally, a few admins referenced that some
IT issues needed to be resolved in person and the lack of access to hardware prevented them from being able to
provide IT support.
“We do remote debugging by getting on calls for software issues. For hardware issues we can’t do that. The
biggest pain points are people using a variety of devices, i.e. phones…In office this is easy because it is
same/similar hardware” - Ent IT Admin

One university IT admin specifically voiced the difficulty of providing any form of IT support without the help of
their regular on-premises student workforce.
"Working remotely has affected how I assist the end users. Such as, help desk phone calls get forwarded to
help desk manager now. Normally, we have student workers on the phone as our trained first-line technicians.
But now, they are off campus and not getting paid to do it anymore." - Edu IT Admin

4.5 Looking Forward
At the onset of COVID-19 we saw a broader role for IT in business, and looking forward we expect to see this trend
continue as organizations continue to need to rely on the appropriate technological infrastructure to enable their
workforce.
4.5.1 IT and the tools they provide have increased in importance for decision makers.
Given the expectation that employees working from home, potentially in a hybrid environment, will continue postCOVID (see Chapter 6 on Societal Implications for a discussion of this), many companies report they are
accelerating moves to the cloud and increasing their overall IT spending. This is despite a broader focus on reducing
overhead expenses and driving operational efficiency. IT spending to cope with COVID-19 was often well outside
planned budgets due to the speed of COVID-19 spread and the rapid move to remote work. Importantly for
Microsoft, the emergency situation showed companies they could make tech deployment decisions far more rapidly
than anyone expected, with successful organization-wide deployments measured in mere days from decision to full
availability to employees. For many, this experience has led to IT being regarded as more strategically important
within companies than they were prior to COVID-19, and crucial to maintaining the ability for the company to
operate moving forward. It has also made decision makers want to have plans in place to avoid similar global
challenges in the future. [55,62].
This increased focus on IT as a more strategic part of the business is helping drive demand for certain technology
needs (e.g., data visualization, CRM platforms, virtualization) and a review of other technology choices made
quickly during the early stages of the pandemic (e.g., video conferencing). Some decision makers are also beginning
to reimagine their approaches to how technology can both help the employee with their productivity when working
from home, and help the company as well to assess the employee's performance when this is no longer a largely inperson relationship [55,167].
"There needs to be a better way to measure productivity without everyone being at their desk" – Business
decision maker, Telecom, Australia

36

“There is more pressure to justify positions working remotely…we need a system that can also quantify the
abstract for performance management.” – Business decision maker,, Insurance, Australia

4.5.2 Some organizations may be able to avoid layoffs by modernizing their IT infrastructure to facilitate remote
work.
The pressures of the COVID-19 crisis have forced organizations to make consequential decisions regarding their
workforce due to the state of their IT infrastructure. Certain commercial organizations have chosen to layoff workers
rather than modernize their IT infrastructure to facilitate remote work. When describing the difficulties they had
encountered since the COVID-19 crisis began, an IT director of an east coast call center described their organization
choosing to lay off over half of their employees (150 people), rather than purchase laptops, VOIP software, and
appropriate internet connectivity for their employees homes [23]. This additional technology would have enabled
members of the organization to easily work from home and keep their jobs.
This example shows that there is an opportunity to save businesses on the brink of massive layoffs by providing or
enabling them with the appropriate technological infrastructure needed to work remotely.

37

5 DEVICES AND PHYSICAL ECOSYSTEMS
By Ginger Hudson, Bill Buxton, and Tiffany Smith
5.1 Introduction
Though most information workers interactions became virtual during the pandemic, the physical spaces people
worked from and the devices they used to connect virtually remained integral to their experiences. This chapter
looks at the devices and physical ecosystems people used for remote work. It starts with an overview of the
challenges people had with their home workspaces – particularly the lack of private, distraction-free space, the
ergonomics of their physical setups, and remote connectivity issues. It highlights how remote work and virtual
meetings changed how people used devices, with a focus on their use of phones and video cameras, and discusses
how companies are thinking about devices and workspaces going forward.
5.2 Challenges for Home Offices
5.2.1 The rapid shift to remote work left little to no time to consider the implications of workers’ physical
environments.
When companies began transitioning employees to work from home in the winter and spring of 2020, technical and
business decision makers experienced significant disruption. Many were required to move entire workforces to
distributed, remote locations in a matter of days while maintaining business continuity [20,21,62]. The most
common approaches taken by leaders in order to enable the rapid transition to remote work included: scaling
existing technology, accelerating deployment of new technology, purchasing and/or distributing new
devices/hardware based on need and availability (e.g., laptops, keyboards/mice, phones, monitors, and tablets [21]
and allowing employees to take home equipment and devices from their offices when possible [62].
Successfully navigating the rapid and widespread transition to remote work frequently involved bypassing finance
departments, administrative processes, and other “red tape” processes that tend to characterize decision-making at
scale [62]. In fact, many IT admins had been advocating for some of these changes for years prior to the pandemic,
such as establishing VDIs and VPNs, migrating employees from legacy communications tools (e.g., landline
phones) to modern solutions like Teams, exchanging desktops for laptops, etc., only to finally get approval to move
forward when the work from home mandates began, leaving IT teams with little to no time to prepare [20,62]. The
previous chapter on IT and Security provided additional detail about the challenges IT admins experienced as they
responded and adapted to the move to remote work.
“All of this is forcing us to digitize. Now that it’s a priority, it’s unfortunately a big ‘I told you so.’”
– Global IT Manager, ITDM, US

5.2.2 Many information workers struggled to find a workspace that was comfortable and distraction free.
A longitudinal study based upon the impact of COVID-19 on information workers found that two key factors deeply
impacted a person’s ability to be productive when working from home: the physical size and layout of their living
space (e.g., do they live in a house or apartment, 2000 square feet or 500 square feet) and the social make-up of their
living situation (e.g., do they live alone, with kids, with other adult family members, with roommates, etc.) [156].
Researchers found that in general, the smaller a person’s space and the more people they live with, the more
challenging it can be to carve out an office of one’s own [156].
An internal Microsoft survey found that 64% of employees reported having a private room dedicated for work,
while 22% said they had no dedicated workspace [46]. Evidence from external research suggests that a lack of
dedicated space is much more prevalent among the broader information worker population, especially those living in
more urban areas where living spaces are smaller and people tend to split rent with housemates, as well as other
countries where homes tend to be smaller (e.g., Netherlands, Japan) [75,156].
The images in Figure 6 show examples of home offices that were submitted by external information workers in an
interview study about their work-from-home experiences [75,156].

38

Figure 6: Spaces people re-purposed for work-from-home [156].

Alongside the physical space constraints often came a range of distractions that interfered with productivity,
including children participating in distance learning, pets, and noise from others working remotely nearby
[46,156]. The earlier on Personal Productivity and Well-being provided additional detail about what we have learned
about these distractions.
“My bed doesn’t allow me to keep correct posture as it should be while working for long hours. I don’t have a
comfortable chair to sit for long hours and work.” [156]
“My makeshift office gets deconstructed every day for breakfast, lunch and dinner.” [156]
“…with four people in the house right now it makes finding your own space a bit difficult. If I could change it,
I would have the main office as my workspace” [156]
“The space is not ideal. Ideally I would have a separate room for an official office” [156]

Despite struggling with non-optimal spaces, most information workers attempted to set up workstations that would
allow them to be comfortable and productive, often re-purposing other rooms to use as an office (e.g., kitchen,
bedroom, garage) or sharing spaces with family or housemates [30,156]. External longitudinal research finds that
workstations evolved some over the many months during the pandemic, but only modestly [74,75,156]. Most
commonly, people added items such as earbuds or headphones to help with focus, a single external monitor to
expand screen real estate, keyboards and mice, and low-cost, non-tech objects (e.g., plants, a new coffee mug) to
make their workstations more cheerful [74,75,156]. Information workers report that employers, for the most part,
allowed them to bring home certain items from the office, but the majority did not provide a stipend for buying
additional items that would make working from home more comfortable [74]. As far as why information workers
have not continued to make more dramatic improvements to their workstations, some expressed that despite
anticipating a future with more hybrid work, they were hesitant to invest more of their own money into their home
offices, especially with there still being so much uncertainty ahead [74].

39

Figure 7: A workspace at the beginning of work-from-home and 1 month later [156].
“I really don't want to spend money on making it more comfortable and I knew it wasn't going to be forever...
I really have no idea if they will let me continue [to work from home] when things open up.” [74]

One of the most significant challenges that employers will have to address as they plan for and adapt to more
flexible, hybrid work arrangements in the future is that of space: how can employers aspire to a fair and equitable
workplace across wildly difference workspaces? See the following chapter on Societal Implications to learn more
about inequalities in home workspaces.
5.2.3 Working from home in make-shift offices highlighted the importance of ergonomics.
Prior to the transition to remote work following COVID-19, many information workers worked from home on an
occasional basis to accomplish focused work or for personal reasons, which did not necessitate investing in a full
ergonomic set-up like what they were using in their office settings [156]. Without the convenience and comfort of
office chairs, desks/standing desks, large/multiple monitors, and docking stations, some information workers found
it challenging to maintain their typical level of productivity [156,161]. Along with digital tools, some reported
missing more analog items like whiteboards and pinboards that they had access to in their offices [69] that provided
more physical space to sketch ideas and collaborate with others. Space issues, as mentioned in the previous section,
often influence the extent to which information workers can integrate equipment into their environments, even if
companies offer to provide it for them.
Not surprisingly, many of those making do with spaces and furniture already in the home experienced physical pain
and fatigue, including eye strain, neck and back pain, and carpal tunnel symptoms [26,36]. Contributing to this
physical stress were extended hours of online meetings, often on video requiring users to stay visible in a narrow
field of view, longer workdays, and fewer breaks taken to walk and stretch [26,46,128]. Chapter 2, which discussed
Personal Productivity and Well-being, provided additional detail on health issues related to remote work.
Companies’ investment in ensuring employees have ergonomic furniture (e.g., ergo chair, footrest) and equipment
(e.g., keyboards, ergo mice, monitor arms) in their homes could avoid costly longer-term health issues for their
workforce.

40

Figure 8: The at-home workstations for several different information workers [156].
“In my office, I have a dual monitor set up and a dedicated workspace. At home, I do not have that set up and
am working from my laptop typically at the kitchen counter or dining room table. I had a small desk in our
guest bedroom that I was using but we moved that to make room for workout equipment.” [160]
"Making my work station comfortable has been a struggle. I have a standing desk I usually use but I'm not able
to use it at home. My arm hurts from the position I end up in." [161]
"My bed doesn’t allow me to keep correct posture as it should be while working for long hours. I don’t have a
comfortable chair to sit for long hours and work.” [156]

5.2.4 Many people dealt with connectivity challenges when working from home (e.g., Wifi, VPN).
Poor internet performance ranked as the top issue identified by IT professionals when asked about the biggest
challenges for employees working from home [22]. Many households had multiple people simultaneously working
remotely, participating in online learning, and consuming entertainment, putting a strain on available bandwidth.
Other issues involve infrastructural challenges in certain regions that cause unreliable internet and cell service,
creating huge barriers to information worker productivity at home [24].
An internal study noted that the situation improved for Microsoft employees over time, with fewer employees
reporting internet problems over the course of working from home [98], but the broader community of information
workers in the US continued to struggle with network bandwidth and VPN/RDP consistency [128]. Over half (59%)
of those in an external study reported using their mobile phone for online meetings, either as the sole device or as
secondary device to the PC, to avoid potential disruption caused by unreliable internet performance [75]. Twentythree percent of information workers said they used their mobile device as a hotspot when their home internet
became weak, laggy, or stopped working altogether [75]. According to NPD, this hotspot usage trend is expected to
continue for the population at large as networks continue to be stretched [123].
"There is an overload of our systems because we were not prepared for this many people working remotely. . .
this is causing some of our software that we use to get locked up at times.” [162]
“There's definitely been some issues because there's multiple people remotely working here, and we've had
some Wi-Fi issues.” [156]
“Although using the phone can make meetings a bit easier, I do wish that there was a more convenient way to
connect to the internet. During meetings, if there is a video I need to show, streaming over Wi-Fi is difficult in
that it is slow and the video will be choppy.” [75]
“What’s working well is that I don’t have too many wifi problems during the calls because I can use cellular
data [on my mobile] when the WiFi isn’t working.” [75]

5.3 Evolving Use of Devices
5.3.1 More online meetings while working from home led to new behaviors related to device use.
Online meeting app usage saw unprecedented highs post-COVID [8,40,89], and this led to new behaviors related to
device usage. For example, the use of a secondary device, most commonly a mobile phone, to support online
41

meetings became more prevalent [75]. This behavior reportedly was adopted for a few keys reasons: 1) unreliable
Wifi or poor performance while using PC, especially when video is involved (e.g., video gets choppy on PC, but the
audio on the phone is stable so that participation in the meeting can continue without interruption), 2) the desire to
engage in different meeting activities on separate screens while in a meeting (e.g., use the phone for audio and
video, and the PC for chat or viewing shared documents), 3) the ability to manipulate the camera in the mobile
device to show things in physical environment such as sketches on a notepad, concept on a whiteboard, models, and
prototypes, and 4) the flexibility to multi-task while joined to online meetings (e.g., ability to move around the room
and accomplish other tasks, type emails on PC) [75].
“There have been other meetings where I use my phone app when I need to show illustrations or things on my
whiteboard. The phone makes it easier to show my work and explain concepts. The camera on the phone is
easier to navigate.” [75]
"In order to connect visually as well as audibly a mobile device or pc is required. I use both.” [75]
"I use my mobile device for zoom meetings because it allows me to join the zoom meeting while still leaving
my laptop free to use for other work while the meeting is ongoing. It's nice to have a secondary device that can
join the meetings.” [75]

In addition to online meetings, other factors while working from home such as different workspaces, new mobility
patterns, and reduced access to office equipment, appeared to prompt information workers to use multiple devices at
the same time to multi-task and provide access to more screens for accomplishing their work [75,147,156]. As
discussed earlier, many people do not have space or budget for big screens or multiple monitor set-ups in their
homes, so they used additional devices, often personal ones, like laptops, tablets, and phones to optimize their
workflows [75,147].
Multi-device usage is not without seams and tension today; information workers encounter inconsistent user
experience across devices, broken flows when trying to accomplish tasks, and lack of synchronization, just to name
a few [147]. These user frustrations present opportunities for companies to design experiences that work across all
devices and different screen sizes.
5.3.2 The increased frequency of remote meetings with video placed greater importance on cameras.
A study by the devices team that looked at Microsoft employees and external information workers found that the
majority (64%) reported using the integrated camera in their primary devices (laptop, 2-in-1) for online meetings
using video [30]. There are associated challenges for information workers using the integrated camera instead of, or
in additional to, a standalone webcam including performance and integration with other equipment (multiple
displays) and the ability to capture the individual’s desired angle on camera [138]:
“Camera angle of the Surface Pro is not ideal” [30]
“Camera is not centered on my gaze due to using multiple monitors. I am using the camera in my laptop but
running Teams on a wall mounted monitor.” [30]
“It would be easier to leave my laptop shut and use an external camera. This laptop is also off to the side so it
often looks like I am not looking at the camera.” [30]

An internal study using EEG found that online meetings with video require a high degree of visual concentration
which can lead to fatigue after 30-40 minutes into a meeting and increased stress after approximately two hours
[19]. The brain struggles to keep track of things like misaligned eye gaze and only partial or no view of others’ hand
gestures, body language, and interaction with materials in their environments, which can lead to increased fatigue
and a subpar meeting experience [19,65].
We also learned from enterprise customer feedback that video meetings may be a particularly strong driver of
physical workspace needs [29]. Several participants in a diary study of Microsoft employees reported having to
modify their workspaces over time specifically to better support meetings, including adding monitor arms, external
webcams, and lighting [138].

42

Figure 9: At-home workstations set up so as to support remote meetings [75].

5.3.3 People spent more time on screens while stuck at home, most notably on their mobile phones.
As people strived post-COVID to maintain connection with others, work remotely, stay informed and be entertained
without leaving the house, screen time across devices, including laptops, tablets, smart TVs, and mobile phones rose
markedly [7,8,50,75,123]. People reported doing a lot more of the same activities (e.g., social media, games, video
calls, conference calls for work) as well as some new things (e.g., restaurant/food delivery apps, shopping for deals,
checking for supplies in stock, Teams calls) on their mobile phones [7,50,123]. Cellular data consumption on
smartphones was up by 75% [123] and weekly time spent in apps is up 20% from the previous year worldwide [8].
This translated into more downloads, with apps such as Disney+, Zoom, TikTok, and Houseparty leading the way,
and consumer spending at a level never before seen at over $23 billion in Q1 2020 alone [8]. Although mobile phone
usage and app downloads increased post-COVID, people also reported that they expect to wait longer to upgrade
their phones (from 2.5 years to 2.7 years) in 2020 due to reduced disposable income and economic uncertainty
[52,61].
“Entertainment work, emails, everything I’m working from home... I have to use my phone for meetings, Zoom
meetings. Phone use has increased dramatically.” [50]
“It’s definitely increased my screen time by like 100%.” [50]
“I’d say from a work standpoint I’m definitely doing a lot more walking meetings where I can, like if I’m doing
a 1:1 with somebody and I don’t need to be taking down notes, or sharing my screen, or facilitating a call, I’ll
be a little bit more mobile that way.” [50]
“I think about had this happened 20 years ago, we would have lost our minds without the phones, without
Facebook, without being able to feel connected through technology.” [50]

5.4 Looking Forward
5.4.1 Company leaders are seeking tools that enable flexibility and productivity in a world where remote work is the
norm.
Decision-makers are considering the evolving device and equipment needs of employees who are likely to work
with much greater flexibility between home and the office in the future. In a study conducted in June 2020 with
ITDMs, the following were identified as areas of improvement for future devices and workstation set-ups [72]:
•
•
•
•

Higher capacity cameras for video conferencing,
Noise cancelling microphones and headphones as an accessory,
More on-line tutorials for self-learning of device capabilities, and
Ergonomic design for employees with standing desk.
“We are still in the very early stages of figuring out what the long term impact is going to be to how we work,
how we communicate, and how we commune culturally. And so, within that, the next device refresh, we are
really going to have to explore.” – Head of Global Operations & Strategy, Media and Entertainment [62]

43

According to Gartner, the massive shift resulted in an uptick in IT spending including devices and peripherals as
people moved to remote work post-COVID to accommodate massive transitions to remote work, however it’s
anticipated that companies will pull back spending given growing concerns around an economic downturn [52,97].
As companies acknowledge that remote work will be the norm moving forward, many are shifting more to the cloud
and exploring new and emerging technologies to better enable flexible work [62]. This will impact device choices
for employees that could mean more versatile form factors like tablets/2-in-1s, ultra-portable laptops, and Chrome
devices, or cloud-provisioned devices that can connect to virtually any peripherals for easy deployment [52].
5.4.2 Decision-makers are navigating a complex set of challenges related to planning the return to work.
Many decision-makers from enterprises across the US, UK, and AU are planning for a hybrid environment with
some employees being in the office, some working remotely, and the majority rotating between the two. Many also
indicated that they will be prioritizing both the improvement of home office set-ups for employees and the redesign
of office spaces for safety and social distancing in 2021 [62].
“In a nutshell approximately 33% of the workforce will be from home, it’s become a lot
more acceptable...would be good to have an ability to interact with each other in a real manner (e.g.,
a Common Room people can drop in and out of). Experience each other the same way as in the workspace.” –
Customer Delivery Director, Telecom [62]
“We are now learning the difference between a butt in the seat and a productive employee.”
Company [62]

– Global Retail

“Lots of doors have been opened that cannot now be shut – no way we'll go back to exactly how it was from a
work perspective.” – Global Bank [62]

This seems to reflect the desires of employees, the majority of whom say that they prefer the flexibility of a hybrid
workstyle post-pandemic, working some weekdays in the office and some from home [75]. In another survey
conducted with Microsoft employees that have already begun phasing back into the office in Asia, 80% of
employees indicated that providing compensation to improve home office setups was one of the most important
things to change about working from home [176]. This was further reinforced by the selection of “better workplace
facility” as the top motivator for employees choosing to work from the office. Respondents of this survey
overwhelmingly stated a preference for a mix of working from and in-office as opposed to be completely remote.
5.4.3 Companies are faced with making new hybrid work policies and workplace modifications to ensure a safe
environment and instill confidence with employees.
Specific workplace modifications and policies that have been suggested by the CDC include: improved ventilation
and HVAC systems, modify workstations and common areas to maintain social distancing, install transparent
barriers between workstations, stagger employees’ schedules to limit people in office, reminders of proper handwashing techniques, face coverings at all times, and enhanced office cleaning and disinfecting. Design and
commercial real estate firms (e.g., Vicus Partners, Cushman & Wakefield) have proposed additional measures to
nudge people towards behaviors that prevent the spread of infection including: visual markers (stickers, signs,
colored floor designs) to signal proper distancing and foot traffic flow, more sensor technology to reduce touching
of surfaces (lights, sinks, doors), app that will chime when people are too close to one another, and disposable paper
“placemats” that go on desks to minimize contact on surfaces [174,177]. For devices, ease of cleaning and hygiene
are top concerns for IT decision-makers, especially those in industries where employees share devices and
contamination is a concern (e.g., healthcare, retail, food processing) [73].
While contemplating the protocol and timing of the return, many decision-makers are continuing to speculate
commercial real estate reductions in order to reduce operating costs in 2021 [62] among other key purchasing
decisions.
"We can save money by better leveraging our space. The dinosaurs of business are having to change their ways
and accept it's possible; where in the past they've been reticent.” – Strategy Director, Sports &
Entertainment [62]
“What we’re really up against in term of the timeline is whether this will happen again… I think it’s the end of
7 thousand people in a building. Those are days are over. I think we could get really carried away by
reinventing the workspace, and then if it happens again.. I think there will be a lot of people holding off on
making changes. WFH is here to stay. We’ve adapted. It was unthinkable before that you could put a call center
into peoples homes as long as you have the right encryptions and confidentially in place.” – Regional
Development Manager, Banking [62]

44

“We built an app that will beep if you are too close – the data stays on the device itself, and it’s geo-locked to
our offices only. You may also receive a message if someone has COVID and you need to self-isolate.” –
Business Analyst, Management Consulting [62]

Such decisions will amplify the importance of providing compensation for employees to improve work set-ups at
home.
5.4.4 Many companies and schools are experimenting with and planning for more outdoor spaces and other
reimagined gathering spaces.
We can expect that spaces where people are co-located to work or learn will look different in the future. Many
companies are planning for more outdoor meeting spaces by reimagining balconies, rooftops, and company
greenspaces [93]. Higher education, such as Rice University, have begun holding classes outdoors in semipermanent tents or open green spaces [105]. Seattle public schools have announced they are working on plans for
what outdoor classrooms might look like in the upcoming months [187]. In a recent study of external information
workers and students [75], many had attempted to work outdoors but experienced challenges while attempting to be
productive on their PCs outdoors including: PC battery did not last long enough, poor wireless internet connection,
PC screen suffered from glare (could not see content due to sun), mic picked up too much background noise. These
barriers experienced by individuals can serve as a proxy for companies to learn from and inspire solutions for when
office re-opening occurs.

Figure 10: Outdoor learning and working spaces.

45

6 SOCIETAL IMPLICATIONS
By Siddharth Suri and Hana Wolf
6.1 Introduction
The previous chapters have all focused on the experience of information workers during and after the sudden shift to
remote work that occurred in early 2020. In this chapter, we widen our lens to examine the many broader societal
implications of this sudden shift. We discuss how involuntary job losses in the United States since the beginning of
the pandemic disproportionately impacted women, members of Spanish-speaking and Black communities, and
individuals with disabilities. We provide evidence that women with caregiving obligations experienced pronounced
disparities in well-being that could increase income inequality, decrease women’s representation in decision-making
and leadership roles, and damage the size and quality of the labor market moving forward. This chapter additionally
highlights the experiences of people who cannot do their work remotely; these jobs are disproportionately held by
poorer people of color.
This chapter also discusses the decoupling of private and professional geographies that is occurring for those who
can work remotely, as well as the implications for labor markets, housing markets, and civic infrastructure. Fluidity
across multiple dimensions may be the single most significant societal implication for those who can shift to remote
work. Location, duration of workday, proportion of professional vs. familial labor, and employed vs. freelance status
all became more dynamic for individuals and communities in response to physical distancing requirements, the
related economic changes, and emerging technological and behavioral adaptations.
Many companies responded to the pressures of COVID-19 by accelerating the pace of decision-making – in some
cases choosing long-term strategies based on short-term data – with unknown implications for revenue, security,
productivity, well-being, and other business-critical factors over time. This chapter explores how future
macroeconomic growth and technological progress are at risk due to a potential drop in innovation, related to the
challenges of collaborating, focusing, and thinking creatively while working remotely (as discussed in other
chapters). It highlights how small and medium businesses – often considered leading indicators of business trends –
have begun displaying an increased openness to hiring freelancers as a source of agile and affordable talent. While
companies’ values and workers’ needs influence all of these dimensions, the data on inequalities in education,
hiring, job loss, wealth, and well-being strongly suggest that the nature of work for individuals, companies, and
societies is also driven by complex external pressures, with work model preference being a privilege that is certainly
not afforded to all.
6.2 Widespread Trends
6.2.1 The shift toward remote work has accelerated.
Remote work is not new; some professions have been trending toward it since the Oil Crisis of the 1970s caused
commuting costs to skyrocket [1]. But in 2020, the global spread of COVID-19 drove a profound increase in the
magnitude and speed of the shift toward remote work, with 88% of organizations from around the world surveyed in
March reporting that they were encouraging employees to work from home [2] and over a third of US workers
transitioning to remote work between March and April [18]. Figure 11 provides some additional numbers on the
share of workers who can and were working from home. This massive acceleration, as well as its complex
relationship with the global health crisis that drove it, is already influencing economics, corporate norms, equality,
innovation, geography, and the environment.

Figure 11: Remote Work by the Numbers (sources: [2,18,184]).

Pre-COVID, Americans who worked from home 3+ days/week

< 5%

During COVID-19 (April 2020), Americans working from home full time

42%

Americans who reported they could do their jobs at home with 100% effectiveness

35%

Estimated share of US jobs that can be done remotely

37%

Percentage of US wages represented by those jobs

46%

46

6.2.2 A more distributed workforce will impact the communities where workers live.
Prior to COVID-19, only 6% of working days in America were done from home [2]. Conversely, 94% of the
working days were done away from home, implying that people generally lived near enough to where they work to
make a regular commute feasible. Since cost of living expenses vary so much depending on where a worker lives, it
is understandable that 87% of companies reported using geographic data to inform compensation rates pre-COVID
[184]. The growing trend of permanent “fully remote” and “remote first” employment policies [76], especially (but
not only) in the technology industry, presents the potential for a decoupling of where professionals work and where
they live at an unprecedented scale. Some companies have embraced remote-only or remote-first policies in order to
reduce facilities costs or gain access to bigger pools of talent [85].
“I can have a local IC3 who’s ok for $165k, or an IC6 who’s a rock star, remotely, for $125K and I’m
overpaying them for their market to compensate for the time difference. What would you do?” - Silicon
Valley Product Exec. [104]

If companies divest physically and financially from communities that sprang up in large part to support them, or that
shifted substantially in response to their growth, this is likely to impact those places. There could be negative effects
on infrastructure and employment ratios, as well as positive effects on housing availability and affordability. The
implications are important to understand, but difficult to model due in part to workers’ and companies’
stated preferences for diverse hybrids of on-site and remote work (see the end of the chapter on Personal
Productivity and Well-being) as well as the complexities of the many societal factors involved.
6.2.3 There is a need to mitigate pervasive social deficits and societal burnout.
As discussed in Chapters 2 (Personal Productivity and Well-being) and 3 (Software Engineering Experiences),
professionals across roles and regions continue to work longer hours while reporting reduced social
connectedness [37,114] compared to pre-COVID levels, and rates of burnout are rising. In August, 58% of polled
US workers reported symptoms of burnout, up from 45% in April [39]. These issues are likely connected,
since social isolation [27] and overwork [45] are both associated with increases in stress.
Unfortunately, hybrid work does not necessarily mitigate the social deficits and increased work hours that contribute
to burnout, as we saw when Microsoft China re-opened [131]. To protect employees’ health and comply with related
regulations, many employers around the world are encouraging or requiring workers to reduce or alternate their time
in office. Some are implementing “podding,” in which individuals socialize exclusively within designated groups in
order to reduce the risk of exposure to COVID-19. These practices have at least partly prevented the return of the
social interactions – especially serendipitous encounters – that professionals have reported missing so profoundly.
They also increase the likelihood that only some collaborators on a given project will be physically present together,
compared to pre-COVID when it was much more likely that all or most project workers would be physically present.
6.2.4 Weak ties are growing scarcer.
The strength of a social relationship between two people, which is called a “tie” in the sociology literature, is a
combination of the amount of time, the emotional intensity, the intimacy, and the reciprocal services which
characterize the relationship [57]. Intuitively, two people who spend a lot of time together or who have a very
intimate relationship have a “strong tie.” It turns out that if two people have a strong tie they are more likely to have
many friends in common (for example, colleagues who report to the same manager). This social group is more likely
to share lots of interests and information; they know many of the same things and the same people. As a result,
strong ties are often sources of redundant information.
On the other hand, two people who are on a first name basis but only communicate by saying, “Hi,” to each other
periodically have a “weak tie.” Two people who have a weak tie are more likely to be in different social circles
compared to two people with a strong tie. They may be experts in different fields, members of different
organizations, they may engage with different media, and they likely associate with different groups. They are also
more likely to belong to different social classes or reside in different locations. As a result, weak ties are sources of
novel information and perspectives.
If we take this perspective and look back over the findings on the effects of COVID-19 and remote work on
professionals’ networks reported in the Collaboration and Meetings chapter, we see that the stronger ties seemed to
endure and the weaker ties seemed to atrophy. The reduction in weak ties may have been caused by the following
documented effects of social distancing and the trend towards remote work:
47

•

•

•

•

“Interpersonal synchrony,” which is a sense of social coordination that stems from subtle signals of
listening and being heard, is harder to achieve via video than it is in person [19], yet synchrony is important
to building rapport. One Microsoft study showed that relationships which began in person and then moved
online were easier on the brain than those which began online [19]. In the current climate of remote and
location-hybrid connection and collaboration, more relationships are beginning online.
Some familial caregivers, especially female caregivers [92], reported more stress and less free time due to
increases in their unpaid responsibilities toward children, elders and households caused by facility closures
and the desire to avoid the pandemic risks associated with in-home help [35,83]. Caregivers, who represent
most working-age women, may therefore be investing less time and attention in the development of weaktie relationships.
Professional events, such as industry conferences, moved online, and online events are less likely to
provide opportunities for networking (the formation of weak ties) compared to pre-COVID in-person
events. Event attendees’ mental models are also shifting; attendees are less likely to prioritize networking
as the top reason for attending an online event [179].
Social distancing and remote work have reduced serendipitous encounters such as coffee break chats and
shared commutes [114,131,138]; like external events, these provide low-stakes opportunities for weaklytied individuals to engage.

6.3 Impacts on Businesses
6.3.1 Long-term decisions are being made based on short-term data.
Many companies are experiencing significant losses due to COVID-19 and related social distancing policies; some
are embracing efficiencies associated with remote work to help them recoup those costs and maximize shareholder
value. Time-sensitive financial dependencies, like expiring leases and fiscal year reporting pressures, are pushing
business leaders to make hard calls about remote working policies and related workforce changes without sufficient
data on the longer-term business costs and societal implications.
“I don’t think we will ever go back to the way we were doing things, I honestly think that we’re not going to
renew the lease for the office space and (will) try to do more work remotely. We are actually becoming more
productive now that we aren’t in the office. Which is so surprising. All that stuff is a waste of time and money.
We will save $2 million on the facility and it’s going to be awesome.”
- A small business decision-maker whose firm has implemented a remote-working policy as well as layoffs and
outsourcing [104]

In interviews, 38% of Tech, Media, and Telecom business leaders (and 26% of leaders across all represented
industries) reported plans to reduce their real estate footprint by, for example, closing retail locations [107]. In the
same study, 74% of CFOs and finance leaders said they planned to move at least 5% of their previously on-site
workforce to permanently remote positions even after COVID-19 [90].
It may appear that more remote work enables companies to save on office space and physical equipment [104], but
looking beyond those apparent benefits the net longer-term outcomes are less clear. For instance, if companies must
spend more on bandwidth, software, and IT support to enable remote work, how much will they save overall?
Estimates are that companies currently spend 2% to 3% of revenues on office space [132].
The secondary effects of these decisions, on a societal scale, are already significant and complex. While fewer
people in the US appear to be moving out of state compared to pre-COVID averages and home sales were down in
the early months of the pandemic, these figures may reflect short-term uncertainty regarding the duration of the
pandemic and its economic pressures. In July, US home sales showed a record gain, and the National Association of
Realtors reported “a shift toward bigger homes and properties away from urban centers as companies allow
employees flexibility to work from home because of the coronavirus” [120].
In India, meanwhile, COVID-19 prompted a “reverse migration” of populations away from cities and back to more
rural regions, with serious implications for these groups’ access to care, employment and technology and with
related implications for the availability of labor in urban centers over time [126].
In addition, the urgent need to ensure business continuity in the short term has required many decision makers and
their teams to forgo normal checks and balances that have traditionally added rigor – and time – to planning and
execution. These provide further examples of pressures in the present forcing a shift from sustainably strategic
thinking toward reactive and potentially short-sighted tactics which could inhibit longer-term growth. One study
48

found that “the crisis created a unique moment where policy, culture and normal ‘red tape’ of finance and regulation
were tossed aside in exchange for action to achieve some degree of business continuity and stability.” [62]
“The whole notion of DR (disaster recovery) is kind of blown up, in that you thought geographic redundancy
could save you, or you thought multiple countries could save you. We just didn’t think that everything all at
once at the same time wouldn’t be available. What would a complete loss of premise do?”
– Managing Director, Global Investment Banking Firm [62]

Leaders in this study worried about downstream impacts of cutting corners within the decision-making process; they
cited potential vulnerabilities including financial miscalculations, regulatory and legal missteps (or simply missed
steps, which can result in significant penalties and loss of customer trust) and security gaps resulting from
accelerated hardware, software and equipment implementations. [62] See the chapters on IT and Security and
Devices and Physical Ecosystems for more on this topic.
As companies consider eliminating or reducing of their physical footprints, the following questions warrant
additional investigation:
•
•
•
•
•

What will happen to the price of corporate real estate and to existing norms and policies related to lease
durations, property tax distribution, and funding for civic infrastructure?
How will representation of different socioeconomic classes and ethnic groups shift across urban and rural
environments? How will this influence access to technology and services?
What are the alternatives to long-term unemployment for firstline workers previously employed as support
staff for physical office ecosystems (e.g., cleaning crews, food service professionals, and security staff)?
Critically, what are the long-term implications of the many findings in this report and elsewhere related to
creativity, social capital, innovation, social isolation, and other factors?
More generally, what are the hidden costs of this complex migration for corporations, individuals, and
society?

6.3.2 There are innovation risks related to remote work.
“I fear this collapse in office face time will lead to a slump in innovation. The new ideas we are losing today
could show up as fewer new products in 2021 and beyond, lowering long-run growth.” – Nicholas Bloom [56]

A number of tech companies have announced that their employees can work remotely indefinitely. However, little
is known about the long-term effects of remote work on innovation, which is a powerful catalyst for long-term
macroeconomic growth [41]. In the short term, as discussed in the chapter on Personal Productivity and Well-being,
professionals report that they have less time for or find it harder to do brainstorming [15] and
collaboration [22,26,69,128,156], ideation [15,47], creative work [26], and big-picture thinking [26] – all known
drivers of innovation. One study also reported that working from home resulted in teams having a shorterterm outlook, which may also decrease long-term innovation [15].
Innovation can often arise from two people interacting. But, as discussed earlier, the strength of indirect
connections, which are a primary avenue for people to get new information from which innovations can stem [57], is
generally perceived to be getting weaker [138].
Recent results from an analysis of data on US employees of Microsoft [182] show that the shift to firm-wide remote
work led to communication patterns that may not be conducive to the collaborative production of high quality
knowledge work. More specifically, workers communicated more via less information rich media, like email and
IM, that are poorly suited to the transfer of complex ideas, and spent more time collaborating
in dyadic configurations that may reduce parallel learning and slow ideation.
Will collaboration and creativity return naturally as professionals get used to the new tools and rhythms of remote
work? For example, another way to create is for two people to think about a problem on their own and then combine
their answers. Will this style of collaboration be more fruitful [156]? Will new technologies emerge to fill the
gaps? Or will isolation, distraction and the pressure to perform lead to a less creative culture? [14] For more on these
topics, see the chapters on Collaboration and Meetings and Personal Productivity and Well-being.
6.3.3 Small and medium businesses are embracing freelance labor.
The shift toward widespread remote work has changed small and medium business leaders’ perceptions regarding
productivity and the use of freelance labor [104]; the following quote is representative of sentiments captured across
15 interviews with decision makers in small and medium businesses during the early months of the pandemic.
49

“I used to think letting my W2 employees work from home…[was] an excuse to slack off… the team has stepped
up and found ways to really maximize productivity. So that gives me kind of a renewed faith in freelancers.”
-Small/medium business CEO

A second theme from this study is that once small and medium businesses started thinking about remote work, they
made an equivalence between remote work and hiring freelancers:
“…we might even work more with freelancers, because working with a freelancer is the same as working
remotely …we saw productivity go up when we started working from home… and basically working right now
with your own team is also hiring freelancers in a way…which made us realize that we can make this a more
nimble and dynamic operation by getting a higher percentage of freelance workers.”
-Freelance User (200-employee marketing company)

In this quotation, the freelance user is additionally pointing out some advantages that freelancers provide compared
with full-time employees. More broadly, the project found that roughly half of the small and medium businesses
studied expected to increase their freelance hiring after the pandemic and the other half either expected to keep their
level of freelance hiring the same or were not sure. Very few expected to decrease their freelance hiring after the
pandemic. If these expectations prove true, society overall might end up moving many full-time employees to
freelance roles. Because freelancers in the United States generally do not receive benefits like health insurance,
retirement, or unemployment insurance, this would result in a transition from a information workforce that has a
social safety net provided by their employers to one that does not.
6.3.4 Well-being is an emerging professional priority.
The Personal Productivity and Well-being chapter discussed the challenges that remote work and the pandemic
created for employees’ well-being. In a survey of external populations, about 86% of people think that a company’s
culture should support mental and emotional well-being [188]. The share is even higher for Millennials and
Gen Zers, who are the largest demographics in the workforce [85,188] Half of Millennials and 75% of
Gen Zers have left roles in the past for mental well-being reasons, compared to 34% of respondents overall.
The year 2020 saw a dramatic increase in the screening for and diagnosis of conditions that negatively impact
mental health. While improved awareness and social acceptance of these conditions is crucial, widespread access to
care is also necessary. LGBTQ+ people, Millennials, and Gen Zers are likely to experience mental health symptoms
for longer durations and were also more open to diagnosis, treatment, and talking about them at work. Almost half
of Black and Latino/Latina people have left a job at least partly for mental health reasons, compared to 32% of
Caucasian respondents [85,188].
6.3.5 Remote work highlights discussions around electronic performance monitoring.
Remote work leaves more digital traces than traditional office work, and this raises important questions about how
to maximize the beneficial uses of these traces (e.g., well-being support) while preventing potential harmful ones
(e.g., general surveillance). Research has shown that the use of digital signals to understand people’s work
performance, sometimes referred to as “electronic performance monitoring” [134], must be done with careful
attention to the privacy, autonomy and well-being of those being monitored. Failure to do so can result in a number
of negative outcomes, including:
•
•
•
•
•

Increased stress levels among workers [134],
Lower levels of well-being (measured via anxiety, depression, and both extrinsic and intrinsic job
satisfaction) [67,134],
Reduced creativity and motivation [11], as well as decreased work quality and productivity [102],
Reduced organizational commitment and reduced trust in management [31,68]
Exacerbation of systemic inequalities due to demographic differences in the populations that are monitoring
and those that are being monitored [10,34,127,175].

6.4 Growth of Systemic Inequalities
6.4.1 Remote work can be a source of structural inequality.
While remote work enabled many to continue working during the pandemic, it has also reflected, reinforced, and
created sources of structural inequality. In the US, those who work in jobs that must be done onsite rather than
remotely are more likely to be non-white and be in the bottom half of the income distribution [115,170]. The
overrepresentation of BIPOC workers in firstline and other onsite-only industries may be contributing to the
50

observed higher rates of COVID-19 within these communities. For example, “the five business sectors most affected
by the pandemic represent almost 50% of revenues for Hispanic- and Latino-owned businesses,” according to a
McKinsey & Company report [113]. As of June 2020, Latinos/Latinas made up 34% of coronavirus cases in the US,
but only 18% of the population [71]. These structural factors likely also contribute to the increased death rates of
BIPOC workers due to COVID-19. A CDC study done in New York City “identified death rates among Black or
African American persons (92.3 deaths per 100,000 population) and Hispanic/Latino persons (74.3) that were
substantially higher than that of white (45.2) or Asian (34.5) persons” [169].
Remote work can also exacerbate existing urban-rural inequalities; the jobs that can most easily be done from home
are generally information work, which typically requires a broadband internet connection. In the US only about 1%
of urban households have no broadband internet connection; on the other hand, about one quarter of all rural
households have no broadband internet connection [84]. In Canada, while 85.7% of households have a broadband
internet connection, in rural communities that number drops to 40.8% [28].
Finally, even among those who can work from home, those who can afford a separate space to work and the
appropriate equipment, and who have fewer caregiving responsibilities at home report having had a more
productive and smoother transition to working from home [35].
6.4.2 There has been uneven impact of layoffs due to COVID-19.
The COVID-19 pandemic resulted in a number of layoffs, especially among those who were unable to work
remotely. Across the US, workforce the layoffs resulting from COVID-19 disproportionately affected women,
African Americans, and Hispanics. According to the US Bureau of Labor Statistics, employment in the US fell by
1.4M in March 2020, an astounding 20.7M in April 2020, and rose by 2.5M in May 2020 [169]. Examining the
20.7M jobs lost in April 2020, one can see that 7.65M were lost in the leisure and hospitality industry and an
additional 2.54M were lost in the education and health services industries, jointly accounting for half of the shocking
number of losses in that month [48]. The move to remote work due to COVID-19 is the likely cause of a huge
reduction in business travel which, in turn, is likely a major cause of the layoffs in the leisure and hospitality
industry.
We do not know the exact gender and race breakdown of the jobs lost in these industries, but we do know the gender
and race breakdown of these industries as a whole [185]. If we assume the demographics of the jobs lost are
representative of their whole industries, the table in Figure 12 shows how these job losses disproportionately
affect Hispanics and Latinos/Latinas, African Americans, and women. Hispanics and Latinos/Latinas make up about
one quarter of the employees in the hospitality industry but only 17.6% of the working age population, a
36% overrepresentation. Similarly Blacks or African Americans make up 15.1% of the employees in the health
services industry but 12.3% of the working age population, an overrepresentation of 23%. Finally, women make up
almost 75% of the employees in the education and health services industry but make up 47% of the working age
population, an almost 60% overrepresentation.
6.4.3 There are structural inequalities in the risks of returning to the workplace.
As we look forward to a reduction in the number of COVID-19 cases, remote work may still be safer than returning
to the workplace for professionals at higher risk of severe COVID-19 symptoms or outcomes. Due to the unequal

Figure 12: Percent of workforce by gender, race, or ethnicity in selected industries.

Women

White

Black or
African Am.

Asian

Hispanic or
Latino/Latina

Age 16 or older

47.0

77.7

12.3

6.5

17.6

Employed in Leisure &
Hospitality

51.2

74.6

13.1

6.9

24.0

Employed in Education
& Health Services

74.8

75.3

15.1

6.4

13.5

51

geographic distribution of co-occurring or pre-existing conditions, as well as unequal distribution of the population
by age, these risks are concentrated in some regions of the US.
A return to the workplace prior to widespread COVID-19 immunity could introduce additional health risks and
socioeconomic pressures for the tens of millions of workers for whom medical conditions including asthma, diabetes
and weakened immune systems increase the likelihood of extreme illness from COVID-19. These risks would
disproportionately impact aging professionals and would compound the pressure to conform and perform often felt
by workers as they approach retirement – especially in an unstable economy. Of note, however, vaccine deployment
strategies may mitigate most of these risks.
Regional concentrations of chronic health conditions may also lead to increased macroeconomic effects in heavily
affected areas, if an unusually vulnerable population returns to work en masse without widespread immunity [129].
These effects could include increased strain on public and private healthcare, decreased productivity at scale, and
increased caregiving obligations especially for women in the community.
6.4.4 Inequalities in at-home learning environments may impact the future makeup of the information workforce.
Simultaneous with the shift to remote work, many, if not most, schools in both the US and Canada shifted to
remote learning, which is not equally accessible to all, and this is likely to have an impact on the makeup of the
future information workforce. Without access to broadband it is difficult for students in a household to watch
educational videos, participate in online classes, or even access shared documents [117]. Given the geographic
disparities in broadband access discussed above, this could open up new educational gaps between urban and rural
schools as pandemic-induced remote learning has continued for two semesters in many school districts. Remote
learning also poses additional challenges for students with special needs whose in-classroom support and
accommodations may not translate well to online settings [82].
The move to online learning additionally exacerbated another structural inequality along the income dimension. The
Washington Post reports [96] that students from families with incomes under $75,000 are nearly twice as likely to
say they “canceled all plans” to take college classes this fall as compared with students from families with incomes
over $100,000, according to a US Census Bureau survey in late August [171]. This is a troubling statistic because,
historically, only 13% of those who stop going to college ever restart [96].
There are a number of reasons why lower income students may not attend college during the pandemic. First,
COVID-19 already disproportionately affected the jobs of lower-income people in the US, making it difficult to
afford to attend. Second, COVID-19 has disproportionately infected BIPOC families, resulting in those who would
have otherwise enrolled needing to earn money or caregive to support their families. Third, lower income people are
less likely to have space, security, and more generally, an at-home environment that is conducive to learning. For
many the in-person, on-campus experience is not a “nice to have” perk of college, it is a necessity.
6.4.5 Gender and caregiving imbalances create risks to the labor market.
People with caregiving responsibilities, and especially caregiving women, have reported struggling more than others
with the shift to remote work during COVID-19. This finding emerged from an external survey of information
workers conducted by Microsoft researchers during the summer of 2020 [35]. Research featured in Marketplace has
also shown that “moms are reducing work hours 4-5 times more than dads during pandemic” [186], and the New
York Times reports that “in some families buckling under the caregiving burden, the lower wage earner is leaving the
work force. Usually that’s the wife” [60]. Researchers at Microsoft have also observed a related trend in India, in
which the labor previously done by domestic support workers is now almost exclusively born by the woman headof-household (on top professional and family obligations) because the support workers have returned to their homes
(and home regions) during the pandemic [83,112].
Inequalities in social expectations and compensation may lead to further reductions in opportunities for women who
stay in the workforce while also tending to children or elders if their productivity is compared directly to that of
other workers without similar familial responsibilities. These factors could further discourage women from entering
or remaining in full-time employment due to the growing likelihood of damage to their well-being and reductions
in their opportunities to succeed. A widespread withdrawal of caregiving women from the workforce could
potentially reduce the absolute size of the labor market by a significant degree, given 86% of women are
mothers by the age of 40 in the United States [95].
This growing inequality could also significantly reduce the gender diversity of the labor market,
further diminishing gender representation in high-level decision-making, product development, and other areas of
52

widespread societal influence. As one study observed, “Notably, the most positive outlook about the current
situation comes from males without childcare responsibilities. This is an important point, as in many organizations,
older males are in decision making positions. If their experience is substantially different than those of the rest of the
workforce, we may continue to see policies that disfavor employees with care-giving responsibilities” [35].
6.4.6 There is an increased risk of job loss for professionals with disabilities.
During the pandemic professionals with disabilities were almost twice as vulnerable to job losses related to social
distancing and COVID-19, and more than twice as likely to seek reskilling, compared to the general population [41].
In a survey fielded in April 2020 and intended to gauge the economic impacts of COVID-19, 51% of workers with
disabilities reported that they had lost jobs, been laid off or furloughed, or believed they would lose their jobs within
three months; only 28% of workers without disabilities reported the same. This discrepancy aligns directionally with
pre-COVID data; one study in 2016 found that “men and women with disabilities are, respectively, 75 and 89%
more likely to experience an involuntary job loss than men and women without disabilities in the United States”
[44].
In addition, the COVID-related survey found that workers with disabilities were more than twice as likely as those
without to report a belief that they would need to switch careers in coming months. Associated needs for
reskilling, paired with the poor accessibility of many leading online learning platforms, will likely create additional
new obstacles for these professionals. These more novel obstacles will only compound the significant blockers to
achievement experienced by professionals with disabilities prior to COVID-19, such as inaccessible workplace
toolsets or communication platforms, low availability of virtual accommodation supports (e.g., localized sign
language interpretation), and low discoverability (so that even when accessible tools or options exist, they are likely
hard to find).
"As we continue to adjust to our new business environments, and the world of work shifts to become more
remote, it will be important for companies to understand the impact and the opportunity of continuing to
leverage a workforce that is diverse and includes the largest diversity segment, individuals with disabilities."
- Meg O'Connell, CEO & Founder of Global Disability Inclusion [44]

6.4.7 As video proliferates, professionals with disabilities face increased pressure to disclose.
As remote work has grown widespread, some professionals with disabilities who previously worked remotely
expressed appreciation or amusement at their newfound status as experts on telework [163]. Others observed that not
much changed for them as others move fully online, and still others struggled with new situations that may uncover
aspects of their disabilities or accommodations that they did not intend to disclose [163]. Now that so many workers
are connecting to meetings remotely from home, interest in seeing people over video can create increased pressure
to turn on video, which some professionals with disabilities may prefer not to share for a variety of reasons. Screen
sharing has benefits for many who want to visually follow content. However, there are implications for blind, low
vision, and deaf users as well as others, who then must rely on assistive technology to read, magnify, adapt color
contrast or have ‘tennis eye’ as they follow content, as well as interpreters, speakers and captions [163].
Some individuals may appreciate the ways in which remote work and video interactions are more accessible than
their in-person equivalents, but they also need video and screen sharing technologies that integrate with their
assistive tools. In addition, while some neurodivergent professionals prefer the flexibility to choose among video,
audio, or textual communications compared to in-person interactions, and therefore welcome the shift to remote
work, others experience an amplified version of the meeting fatigue currently experienced by so many workers
across the spectrum [163]. Chapters 1 and 2 also discuss the benefits and challenges of remote work for
professionals with disabilities for Collaboration and Meetings and Personal Productivity and Well-being.
On a societal level, visible differences can lead to increased awareness and acceptance; this is a known benefit of
mainstreaming in education [159]. However, up to 70% of disabilities are invisible. While many professionals with
disabilities have found it empowering to disclose broadly or selectively to colleagues, it is also the case that being
compelled to reveal one’s identity in this way can be profoundly stressful, stigmatizing, and damaging to one’s
productivity and well-being [13]. Professionals with disabilities are likely better served through
adaptive accommodations that honor their needs for privacy and autonomy as society explores new ways of working
together, apart.

53

6.5 Looking Forward
As the COVID-19 pandemic and the corresponding widespread shift to remote work approach the one-year mark, it
is clear there is much we still do not know. In addition to the many direct effects on society that we have already
observed, we expect there to be continuing ripple effects. And yet companies have to make decisions now about
their work practices, workforces, and workspaces that will have implications for years to come. It will take
continued research to develop a complete picture of all of the ways that things have changed and to find the best
ways to help create meaningful positive outcomes.
Already at Microsoft we have identified changes in how professionals make new connections and strengthen
existing ties, and this has informed product improvements across the company while leaving us with important,
unanswered questions about the unequal impact of remote work on professionals who are lacking in social support
or social capital. We have observed new trends in business decision making, resource allocation, and flexible or
fluid work arrangements that carry complex implications for the future of corporate structures. And we have
uncovered ways that COVID-19 and the unintended consequences of the rapid, global shift toward remote work
have contributed to imbalances in well-being and access to opportunity. It is our hope that this report will help
others act quickly to respond to people’s acute emergent needs using the best research currently available, while also
carefully considering the long-term and broad-ranging impact of their decisions.

54

ACKNOWLEDGEMENTS AND ATTRIBUTION
This report is the result of work of the Future of Remote Work Initiative in Microsoft. In addition to the many
researchers whose work is included, we would like to acknowledge the work of:
Organizing Team: Peter Bergen (Senior PM, Workplace Intelligence), Jenna Butler (Senior Software Engineer,
Office eXperience Organization and MSR Productivity & Intelligence), Alana Dickson (Program Manager,
Workplace Intelligence), Brent Hecht (Director of Applied Science, Experiences and Devices), Sonia Jaffe (Senior
Research Economist, Office of the Chief Economist), Abigail Sellen (Deputy Director, MSR Cambridge), Jaime
Teevan (Chief Scientist, Experiences and Devices).
Research Track Leaders: Nancy Baym (Senior Principal Researcher, MSR New England), Rachel Bergmann
(Research Assistant, MSR New England), Matt Brodsky (User Researcher, Essential Products, Inclusive
Community), Jenna Butler (Senior Software Engineer, Office eXperience Organization and MSR Productivity &
Intelligence), Bill Buxton (Partner Researcher, MSR Redmond), Adam Coleman (Principal Design Researcher,
Office Planning and Research), Mary Czerwinski (Partner Research Manager, MSR Redmond), Brian Houck
(Principal Program Manager Lead, Azure Edge + Platform), Ginger Hudson (Principal User Research Lead,
Devices), Shamsi Iqbal (Principal Researcher, MSR Redmond), Sonia Jaffe (Senior Research Economist, Office of
the Chief Economist), Chandra Maddila (Senior Research SDE Lead, MSR India), Kate Nowak (Solutions Design
Lead, M365 Insights), Emily Peloquin (Senior Design Researcher, Core Services Engineering and Operations),
Ricardo Reyna Fernandez (Program Manager, Office Experience Engineering Organization), Sean Rintel (Principal
Researcher, MSR Cambridge), Abigail Sellen (Deputy Director, MSR Cambridge), Tiffany Smith (Design
Researcher, Office Planning and Research), Peggy Storey (Consulting Researcher, 1ES and Professor of Computer
Science, University of Victoria), Siddharth Suri (Senior Principal Researcher, MSR Redmond), Hana Wolf
(Principal Researcher, LinkedIn), Longqi Yang (Senior Data & Applied Scientist, Office of Applied Research).
Advisory Board: Eric Horvitz (Technical Fellow and Chief Scientific Officer), Kirk Koenigsbauer (COO-CVP of
Data Platform + Growth), Jared Spataro (CVP of Modern Work), Emma Williams (CVP of Office Verticals).
Additional contributors: Angie Anderson, Callie August, Stephanie Beers, Steve Clayton, Amy Coleman, Meena
Culver, Brian Flock, Tara Grumm, Aaron Halfaker, Dave Haspas, Sharon Kallander, Dawn Klinghoffer, Jenny LayFlurrie, Ronnie Martin, Greg Martinez, Tricia Mayer, Anne Nergaard, Amy Pannoni, Brenda Potts, Prienca Punhani,
Jeff Running, Kanwal Safdar, Bahar Sarrafzadeh, David Smith, Colette Stallbaumer, John Tang, Jen Viencek,
Jessica Voelker, Megan Yoshimura, Mengting Wan, Traci Williams, Garrett Young.
Cite this report as:
Teevan, Jaime, Brent Hecht, and Sonia Jaffe, eds. The New Future of Work: Research from Microsoft on the Impact
of the Pandemic on Work Practices. 1st ed. Microsoft, 2021. https://aka.ms/newfutureofwork.
Or cite individual chapters:
Chapter 1: Baym, Nancy, Rachel Bergmann, Adam Coleman, Ricardo Reyna Fernandez, Sean Rintel, Abigail
Sellen, and Tiffany Smith. “Collaboration and Meetings.” In The New Future of Work: Research from Microsoft on
the Impact of the Pandemic on Work Practices, edited by Jaime Teevan, Brent Hecht, and Sonia Jaffe, 1st ed.
Microsoft, 2021. https://aka.ms/newfutureofwork.
Chapter 2: Butler, Jenna, Mary Czerwinski, Shamsi Iqbal, Sonia Jaffe, Kate Nowak, Emily Peloquin, and Longqi
Yang. “Personal Productivity and Well-Being.” In The New Future of Work: Research from Microsoft on the Impact
of the Pandemic on Work Practices, edited by Jaime Teevan, Brent Hecht, and Sonia Jaffe, 1st ed. Microsoft, 2021.
https://aka.ms/newfutureofwork.
Chapter 3: Houck, Brian, Chandra Maddila, and Peggy Storey. “Software Engineering Experiences.” In The New
Future of Work: Research from Microsoft on the Impact of the Pandemic on Work Practices, edited by Jaime
Teevan, Brent Hecht, and Sonia Jaffe, 1st ed. Microsoft, 2021. https://aka.ms/newfutureofwork.
Chapter 4: Brodsky, Matthew, and Adam Coleman. “IT and Security.” In The New Future of Work: Research from
Microsoft on the Impact of the Pandemic on Work Practices, edited by Jaime Teevan, Brent Hecht, and Sonia Jaffe,
1st ed. Microsoft, 2021. https://aka.ms/newfutureofwork.

55

Chapter 5: Hudson, Ginger, Bill Buxton, and Tiffany Smith. “Devices and Physical Ecosystems.” In The New
Future of Work: Research from Microsoft on the Impact of the Pandemic on Work Practices, edited by Jaime
Teevan, Brent Hecht, and Sonia Jaffe, 1st ed. Microsoft, 2021. https://aka.ms/newfutureofwork.
Chapter 6: Suri, Siddharth, and Hana Wolf. “Societal Implications.” In The New Future of Work: Research from
Microsoft on the Impact of the Pandemic on Work Practices, edited by Jaime Teevan, Brent Hecht, and Sonia Jaffe,
1st ed. Microsoft, 2021. https://aka.ms/newfutureofwork.
To learn more, visit:
The New Future of Work (http://aka.ms/newfutureofwork)
Read Microsoft’s research into emerging work practices, including peer reviewed papers and scholarly content.
WorkLab (https://microsoft.com/en-us/worklab)
Discover stories and insights based on this research on how to connect more, create more, and unlock ingenuity.
© Microsoft 2021

56

BIBLIOGRAPHY
1.
2.
3.
4.

5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.
26.

Tammy D. Allen, Timothy D. Golden, and Kristen M. Shockley. 2015. How Effective Is Telecommuting?
Assessing the Status of Our Scientific Findings. Psychological Science in the Public Interest 16, 2: 40–68.
https://doi.org/10.1177/1529100615593273
David Altig, Jose Barrero, Nick Bloom, Steven J. Davis, Brent Meyer, Emil Mihaylov, and Nick Parker.
2020. Firms Expect Working from Home to Triple. Retrieved from
https://www.frbatlanta.org/blogs/macroblog/2020/05/28/firms-expect-working-from-home-to-triple
Erik Anderson. 2020. The human side of business continuity. Home | Work Blog from Microsoft Workplace
Insights. Retrieved from https://insights.office.com/workplace-analytics/the-human-side-of-businesscontinuity/
Erik Anderson, Abhinav Singh, and Kevin Sherman. 2020. The new manager 1:1: nurturing employee
resiliency during disruption and change. FoRW Project: Home | Work Blog from Microsoft Workplace
Insights. Retrieved from https://insights.office.com/workplace-analytics/the-new-manager-11-nurturingemployee-resiliency-during-disruption-and-change/
Andrea Briggs and Jera Nyman. 2020. BAP Studio Remote Work Culture. Microsoft (Internal).
Andrew Leach. Business Continuity Dashboard. Microsoft (Internal).
Travis Andrews. 2020. Our iPhone weekly screen time reports are through the roof, and people are ‘horrified.’
Washington Post.
App Annie. 2020. Weekly Time Spent in Apps Grows 20% Year Over Year as People Hunker Down at Home.
App Annie.
Marcus Ash, Charles Yiu, and Sean Oh. EPIC Employee Global Experience. Microsoft (Internal).
Richard A. Bales and Katherine V. W. Stone. 2020. The Invisible Web at Work: Artificial Intelligence and
Electronic Surveillance in the Workplace. Berkeley Journal of Employment &amp; Labor Law 41, 1: 1.
Kirstie Ball. 2010. Workplace surveillance: an overview. Labor History 51, 1: 87–106.
https://doi.org/10.1080/00236561003654776
Lingfeng Bao, Tao Li, Xin Xia, Kaiyu Zhu, Hui Li, and Xiaohu Yang. 2020. How does Working from Home
Affect Developer Productivity? -- A Case Study of Baidu During COVID-19 Pandemic. arXiv:2005.13167
[cs]. Retrieved January 16, 2021 from http://arxiv.org/abs/2005.13167
Lucy Barnard-Brak, DeAnn Lechtenberger, and William Lan. 2010. Accommodation Strategies of College
Students with Disabilities. The Qualitative Report 15, 2.
Sergi Basco and Martí Mestieri. 2018. Mergers Along the Global Supply Chain: Information Technologies
and Routine Tasks. Oxford Bulletin of Economics and Statistics 80, 2: 406–433.
https://doi.org/10.1111/obes.12165
Harald Becker and Ming-Li Chai. 2020. ENVSN “A Good Day” Research - Attention, focus & flow in modern
workplace (pre & during Covid19). Microsoft (Internal).
Andrew Begel. 2020. Application-Sensitive Accessible Communication. Microsoft (Internal).
Nicholas Bloom, James Liang, John Roberts, and Zhichun Jenny Ying. 2015. Does Working from Home
Work? Evidence from a Chinese Experiment. The Quarterly Journal of Economics 130, 1: 165–218.
https://doi.org/10.1093/qje/qju032
Nick Bloom. 2020. How working from home works out. Stanford University. Retrieved from
https://siepr.stanford.edu/research/publications/how-working-home-works-out
Michael Bohan and Steven Dong. 2020. Remote work EEG research. Microsoft (Internal).
Phillippe Boutros. 2020. Nearly 80% of Business Activity is Disrupted by Coronavirus. Microsoft (Internal).
Matt Britton and Geoff Colon. 2020. Now what? Modern life reimagined - Microsoft & the U.S. Consumer
during Uncertain Times. Microsoft (Internal).
Matthew Brodsky. 2020. The Effects of COVID-19 Crisis on Commercial IT Admins. Microsoft (Internal).
Matthew Brodsky and Sarah Karmali. 2020. Microsoft 365 Admin Center: Intercept Insights on IT Admins
during the COVID-19 Crisis. Microsoft (Internal).
Douglas Broom. 2020. Coronavirus has exposed the digital divide like never before. World Economic Forum.
Retrieved May 21, 2020 from https://www.weforum.org/agenda/2020/04/coronavirus-covid-19-pandemicdigital-divide-internet-data-broadband-mobbile/
Erik Brynjolfsson, John Horton, Adam Ozimek, Daniel Rock, Garima Sharma, and Hong Yi Tu Ye. 2020.
COVID-19 and Remote Work: An Early Look at US Data. National Bureau of Economic Research.
https://doi.org/10.3386/w27344
Jenna Butler and Sonia Jaffe. 2020. Challenges and Gratitude: A Diary Study of Software Engineers Working
From Home During Covid-19 Pandemic. In Microsoft New Future of Work Symposium. Retrieved from
57

27.
28.
29.
30.
31.
32.
33.
34.
35.
36.
37.
38.
39.
40.
41.
42.
43.
44.

45.
46.

47.

https://www.microsoft.com/en-us/research/publication/challenges-and-gratitude-a-diary-study-of-softwareengineers-working-from-home-during-covid-19-pandemic/
John T. Cacioppo, Stephanie Cacioppo, John P. Capitanio, and Steven W. Cole. 2015. The
Neuroendocrinology of Social Isolation. Annual review of psychology 66: 733–767.
https://doi.org/10.1146/annurev-psych-010814-015240
Canadian Radio-television and Telecommunications Commission (CRTC) Government of Canada. 2016.
Broadband Fund: Closing the Digital Divide in Canada. Retrieved January 17, 2021 from
https://crtc.gc.ca/eng/internet/internet.htm
Pete Card, Caolan Mannion, Katherine Reed, Margrete Sævareid, Amit Saxena, Gayle Thompson, and John
Westworth. 2020. Compass customer feedback (BDM + ITDM). Microsoft (Internal).
Shuling Chen and Eric Lovelin. 2020. Device Accessory Needs when WFH. Microsoft (Internal).
Rebecca Chory, Lori E. Vela, and T. Avtgis. Organizational Surveillance of Computer-Mediated Workplace
Communication: Employee Privacy Concerns and Responses. Retrieved from
https://link.springer.com/article/10.1007/s10672-015-9267-4
Prithwiraj Choudhury, Cirrus Foroughi, and Barbara Larson. 2019. Work-from-anywhere: The Productivity
Effects of Geographic Flexibility. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.3494473
Katherine Costain. CPE Relationship Survey. Microsoft (Internal).
Sarah Coury, Jess Huang, Ankur Kumar, Sara Prince, Alexis Krivkovich, and Lareina Yee. 2020. Women in
the Workplace 2020. McKinsey & Company. Retrieved from https://www.mckinsey.com/featuredinsights/diversity-and-inclusion/women-in-the-workplace
Mary Czerwinski, Shamsi T. Iqbal, Daniel McDuff, Jina Suh, and HUE Team. 2020. Health, Well-being and
Productivity During COVID-19: A Study of Boundaries and Adaptation. Microsoft (Internal).
Beth DeCarbo. 2020. Working From Home for the Long Haul? Get the Ergonomics Right. Wall Street
Journal. Retrieved May 21, 2020 from https://www.wsj.com/articles/working-from-home-for-the-long-haulget-the-ergonomics-right-11588286604
Evan DeFilippis, Stephen Michael Impink, Madison Singell, Jeffrey T. Polzer, and Raffaella Sadun. 2020.
Collaborating During Coronavirus: The Impact of COVID-19 on the Nature of Work. National Bureau of
Economic Research. https://doi.org/10.3386/w27612
Jonathan Dingel and Brent Neiman. 2020. How Many Jobs Can be Done at Home? National Bureau of
Economic Research, Cambridge, MA. https://doi.org/10.3386/w26948
Eagle Hill Consulting. 2020. Employee Burnout from COVID-19 on the Rise, With 58% of U.S. Workers
Reporting Burnout. Retrieved from https://www.prnewswire.com/news-releases/employee-burnout-fromcovid-19-on-the-rise-with-58-of-us-workers-reporting-burnout-301122967.html
Charlie Edmonds and Guo Danfeng. 2020. MMX Insights - SwiftKey mobile analytics. Microsoft (Internal).
David Encaoua, Bronwyn H. Hall, François Laisney, and Jacques Mairesse (eds.). 2000. The Economics and
Econometrics of Innovation. Springer, Boston.
Erin Arcuri, Adam Coleman, Brandon Haist, Hugh North, Tiffany Smith, and Shelly Marston. 2020.
Learnings from Enterprise customers as they navigate the impact of the COVID-19 pandemic. Microsoft
(Internal).
Federal Reserve Bank of Saint Louis. 2016. Job polarization. FRED Blog. Retrieved January 24, 2021 from
https://fredblog.stlouisfed.org/2016/04/job-polarization/
Anne Fitzsimmons. 2020. Global Disability Inclusion Survey Reports People with Disabilities Are More
Negatively Affected by The Economic Impact of COVID-19. Retrieved from
https://www.prnewswire.com/news-releases/global-disability-inclusion-survey-reports-people-withdisabilities-are-more-negatively-affected-by-the-economic-impact-of-covid-19-301052873.html
Ramona Florea and Radu Florea. 2016. Individual and Organizational Implications of Work-related Stress.
Economy Trandisciplinarity Cognition Vol. 19, ISSN: 2067-5046: 28.
Denae Ford, Margaret-Anne Storey, Thomas Zimmermann, Christian Bird, Sonia Jaffe, Chandra Maddila,
Jenna L. Butler, Brian Houck, and Nachiappan Nagappan. 2020. A Tale of Two Cities: Software Developers
Working from Home During the COVID-19 Pandemic. arXiv:2008.11147 [cs]. Retrieved January 19, 2021
from http://arxiv.org/abs/2008.11147
Nicole Forsgren, Gregory Ceccarelli, Derek Jedamski, Scot Kelly, and Clair Sullivan. 2020. State of the
Octoverse: Finding balance between work and play. GitHub. Retrieved from
https://octoverse.github.com/static/github-octoverse-2020-productivity-report.pdf

58

48.
49.
50.
51.
52.
53.
54.
55.
56.
57.
58.
59.
60.
61.
62.
63.

64.
65.
66.
67.
68.
69.
70.
71.
72.
73.

Thomas Franck. 2020. Hardest-hit industries: Nearly half the leisure and hospitality jobs were lost in April.
Retrieved from https://www.cnbc.com/2020/05/08/these-industries-suffered-the-biggest-job-losses-in-april2020.html
Renate Fruchter and Marisa Ponti. 2010. Distributing attention across multiple social worlds. AI & SOCIETY
25, 2: 169–181. https://doi.org/10.1007/s00146-009-0251-0
Linda Gagner and Danny Kelly. 2020. Android Smartphone & iPhone Switcher Study. Microsoft (Internal).
Ravi S. Gajendran and David A. Harrison. 2007. The good, the bad, and the unknown about telecommuting:
Meta-analysis of psychological mediators and individual consequences. Journal of Applied Psychology 92, 6:
1524–1541. https://doi.org/10.1037/0021-9010.92.6.1524
Gartner. 2020. Forecast: PCs, Ultramobiles and Mobile Phones, Worldwide, 2018-2024, Gartner, April 2020
Update. Gartner.
Edward L Glaeser and Giacomo A.M. Ponzetto. 2007. Did the Death of Distance Hurt Detroit and Help New
York? National Bureau of Economic Research. https://doi.org/10.3386/w13710
Timothy D. Golden and Kimberly A. Eddleston. 2020. Is there a price telecommuters pay? Examining the
relationship between telecommuting and objective career success. Journal of Vocational Behavior 116:
103348. https://doi.org/10.1016/j.jvb.2019.103348
Google. Google Safe Browsing – Google Transparency Report. Retrieved May 21, 2020 from
https://transparencyreport.google.com/safe-browsing/overview
Adam Gorlick. 2020. The productivity pitfalls of working from home in the age of COVID-19. Stanford
News. Retrieved January 21, 2021 from https://news.stanford.edu/2020/03/30/productivity-pitfalls-workinghome-age-covid-19/
Mark S. Granovetter. 1973. The Strength of Weak Ties. American Journal of Sociology 78, 6: 1360–1380.
https://doi.org/10.1086/225469
Christine A. Grant, Louise M. Wallace, and Peter C. Spurgeon. 2013. An exploration of the psychological
factors affecting remote e‐worker’s job effectiveness, well‐being and work‐life balance. Employee Relations
35, 5: 527–546. https://doi.org/10.1108/ER-08-2012-0059
Shane Greenstein, Chris Forman, and Avi Goldfarb. 2018. How Geography Shapes—and Is Shaped by—the
Internet. In The New Oxford Handbook of Economic Geography, Gordon L. Clark, Maryann P. Feldman,
Meric S. Gertler and Dariusz Wójcik (eds.).
Alisha Haridasani Gupta. 2020. Why Did Hundreds of Thousands of Women Drop Out of the Work Force?
The New York Times. Retrieved January 17, 2021 from https://www.nytimes.com/2020/10/03/us/jobs-womendropping-out-workforce-wage-gap-gender.html
GWI. 2020. Coronavirus Research: Multi-market research wave 2. Microsoft (Internal).
Brandon Haist, Hugh North, Shelly Marston, and Tiffany Smith. 2020. Decision-makers Study. Microsoft
(Internal).
Leslie B. Hammer, Margaret B. Neal, Jason T. Newsom, Krista J. Brockwood, and Cari L. Colton. 2005. A
longitudinal study of the effects of dual-earner couples’ utilization of family-friendly workplace supports on
work and family outcomes. The Journal of Applied Psychology 90, 4: 799–810. https://doi.org/10.1037/00219010.90.4.799
David Hands. 2020. COVID and Audio Study. Microsoft (Internal).
David Hands and Danny Kelly. 2020. Video Presence Study. Microsoft (Internal).
Christina Hegele and Abhinav Singh. 2020. Can we balance work and life under one roof? Home | Work Blog
from Microsoft Workplace Insights. Retrieved from https://insights.office.com/workplace-analytics/balancingwork-and-life-under-one-roof/
David Holman. 2002. Employee wellbeing in call centres. Human Resource Management Journal 12: 35–50.
https://doi.org/10.1111/j.1748-8583.2002.tb00076.x
Matthew Holt, Bradley Lang, and Steve G. Sutton. 2016. Potential Employees’ Ethical Perceptions of Active
Monitoring: The Dark Side of Data Analytics. Journal of Information Systems 31, 2: 107–124.
https://doi.org/10.2308/isys-51580
Brian Houck. 2020. COSINE Productivity During WFH. Microsoft (Internal).
Brian Houck. 2020. Onboarding new hires during COVID-19. Microsoft (Internal).
Shawn Hubler, Thomas Fuller, Anjali Singhvi, and Juliette Love. 2020. Many Latinos Couldn’t Stay Home.
Now Virus Cases Are Soaring in Their Communities. The New York Times. Retrieved from
https://www.nytimes.com/2020/06/26/us/corona-virus-latinos.html
Ginger Hudson. 2020. ITDM in Commercial: Post-pandemic device considerations. Microsoft (Internal).
Ginger Hudson. 2020. Device Hygiene Study. Microsoft (Internal).
59

74.
75.
76.
77.
78.
79.
80.
81.
82.
83.
84.
85.
86.
87.
88.
89.
90.

91.
92.
93.
94.

95.

Ginger Hudson. 2020. Workstation Evolution During the Pandemic. Microsoft (Internal).
Ginger Hudson and Steven Derhammer. 2020. Devices and Remote Work Study. Microsoft (Internal).
Lori Ioannou. 2020. 1 in 4 Americans will be working remotely in 2021, Upwork survey reveals. CNBC.
Retrieved January 21, 2021 from https://www.cnbc.com/2020/12/15/one-in-four-americans-will-be-workingremotely-in-2021-survey.html
Shamsi Iqbal and Kirk Daues. 2020. Enterprise Customer Adaptation to Remote Work and Planning for a
Hybrid Future. Microsoft (Internal).
Shamsi T. Iqbal and Eric Horvitz. 2010. Notifications and awareness: a field study of alert usage and
preferences. In Proceedings of the 2010 ACM conference on Computer supported cooperative work - CSCW
’10, 27. https://doi.org/10.1145/1718918.1718926
Jared Spataro. Reimagining virtual collaboration for the future of work and learning. Retrieved from
https://www.microsoft.com/en-us/microsoft-365/blog/2020/07/08/reimagining-virtual-collaboration-futurework-learning/
Karen A. Jehn and Priti Pradhan Shah. 1997. Interpersonal relationships and task performance: An
examination of mediation processes in friendship and acquaintance groups. Journal of Personality and Social
Psychology 72, 4: 775–790. https://doi.org/10.1037/0022-3514.72.4.775
Jen Porter, Bernie Wong, and Kelly Greenwood. 2020. How to Form a Mental Health Employee Resource
Group. Harvard Business Review. Retrieved from https://hbr.org/2020/05/how-to-form-a-mental-healthemployee-resource-group
Anya Kamenetz. 2020. Families Of Children With Special Needs Are Suing In Several States. Here’s Why.
NPR. Retrieved from https://www.ijpr.org/education/2020-07-23/families-of-children-with-special-needs-aresuing-in-several-states-heres-why
Prerrna P. Kapoor, Abhijit Bairagi, and Anita Isola. 2020. Impact of COVID-19 crisis on the future of work in
India. In Microsoft New Future of Work Symposium. Retrieved from https://www.microsoft.com/enus/research/publication/impact-of-covid-19-crisis-on-the-future-of-work-in-india/
Harmeet Kaur. 2020. Why rural Americans are having a hard time working from home. CNN. Retrieved from
https://www.cnn.com/2020/04/29/us/rural-broadband-access-coronavirus-trnd/index.html
Kristi Kelly and Darren Austin. 2020. Mental Wellbeing. Microsoft (Internal).
Dawn Klinghoffer, Candice Young, and Dave Haspas. 2019. Every New Employee Needs an Onboarding
“Buddy.” Harvard Business Review. Retrieved January 21, 2021 from https://hbr.org/2019/06/every-newemployee-needs-an-onboarding-buddy
Dawn Klinghoffer, Candice Young, and Xue Liu. 2018. To Retain New Hires, Make Sure You Meet with
Them in Their First Week. Harvard Business Review. Retrieved January 21, 2021 from
https://hbr.org/2018/06/to-retain-new-hires-make-sure-you-meet-with-them-in-their-first-week
Andrew J. Ko. 2019. Why We Should Not Measure Productivity. In Rethinking Productivity in Software
Engineering, Caitlin Sadowski and Thomas Zimmermann (eds.). Apress, Berkeley, CA, 21–26.
https://doi.org/10.1007/978-1-4842-4221-6_3
Ella Koeze and Nathaniel Popper. 2020. The Virus Changed the Way We Internet. New York Times.
Justin Lavelle. 2020. Gartner CFO Survey Reveals 74% Intend to Shift Some Employees to Remote Work
Permanently. Gartner. Retrieved January 17, 2021 from https://www.gartner.com/en/newsroom/pressreleases/2020-04-03-gartner-cfo-surey-reveals-74-percent-of-organizations-to-shift-some-employees-toremote-work-permanently2
Heather Layne and Giancarlo Cozzi. 2020. The rise of the 30-minute meeting. Home | Work Blog from
Microsoft Workplace Insights. Retrieved from https://insights.office.com/workplace-analytics/the-rise-ofshorter-meetings-and-other-ways-collaboration-is-changing-with-remote-work/
Kyung-Hee Lee and Ellen Ernst Kossek. 2020. The coronavirus & work–life inequality: Three evidence-based
initiatives to update U.S. work–life employment policies. Behavioral Science and Policy Association.
Lydia Lee. 2020. Post-COVID, More Office Designs Include Permanent Outdoor Workspaces. Metropolis.
Retrieved January 21, 2021 from https://www.metropolismag.com/architecture/workplace-architecture/postcovid-outdoor-workspaces/
Life at Google. 2020. Most Googlers want to return to the office at some point, even if not every day. #️⃣1⃣
reason: to work face-to-face w/teammates #️⃣2⃣ reason: to socialize w/ teammates #️⃣3⃣ reason: collaboration
https://t.co/YfRdEG43Lo. @lifeatgoogle. Retrieved January 21, 2021 from
https://twitter.com/lifeatgoogle/status/1308529123984203778
Gretchen Livingston. 2018. U.S. Women More Likely to Have Children Than a Decade Ago. Pew Research
Center’s Social & Demographic Trends Project. Retrieved January 17, 2021 from
60

96.
97.
98.
99.
100.
101.
102.

103.
104.
105.
106.
107.

108.

109.
110.
111.
112.
113.

114.

115.
116.

117.

https://www.pewsocialtrends.org/2018/01/18/theyre-waiting-longer-but-u-s-women-today-more-likely-tohave-children-than-a-decade-ago/
Heather Long and Danielle Douglas-Gabriel. The latest crisis: Low-income students are dropping out of
college this fall in alarming numbers. Washington Post. Retrieved January 17, 2021 from
https://www.washingtonpost.com/business/2020/09/16/college-enrollment-down/
Angus Loten. 2020. IT Spending Forecasts Take a Hit as Coronavirus Slams Global Markets. Wall Street
Journal.
M365 Marketing. 2020. Work Trend Index. Retrieved from https://www.microsoft.com/en-us/microsoft365/work-productivity-trends-report
Chandra Maddila. 2020. Nudge study (Developer Productivity Trends during COVID-19). Microsoft
(Internal).
Maitraye Das, John Tang, Kathryn E. Ringland, and Anne Marie Piper. 2021. Towards Accessible Remote
Work: Understanding Work-from-Home Practices of Neurodivergent Professionals. In ACM CSCW ’21.
Caolan Mannion. 2020. Compass customers - WFH survey. Microsoft (Internal).
Angela J. Martin, Jackie M. Wellen, and Martin R. Grimmer. 2016. An eye on your work: How empowerment
affects the relationship between electronic surveillance and counterproductive work behaviours. The
International Journal of Human Resource Management 27, 21: 2635–2651.
https://doi.org/10.1080/09585192.2016.1225313
Matthew Ayres. 2020. Future Workforce Study. Microsoft (Internal).
Kelli McGee, Liane Scult, Sean Rintel, and Siddharth Suri. 2020. SMB Freelance Study. Microsoft (Internal).
Alison Medley. 2020. Rice University will hold classes in outdoor tents, asks students to bring own chairs.
Houston Chronicle. Retrieved January 21, 2021 from https://www.chron.com/local/article/Outdoor-tents-forclassrooms-That-s-now-the-15410068.php
Jacqueline Meijer-Irons. 2020. Compliance in the time of COVID-19. How remote work is changing the work
of compliance professionals. Microsoft (Internal).
Rob van der Meulen. Gartner CFO Survey Reveals That 62% of CFOs Plan SG&A Cuts This Year Due to
Coronavirus Related Disruptions. Gartner. Retrieved January 17, 2021 from
https://www.gartner.com/en/newsroom/press-releases/2020-04-06-gartner-cfo-survey-reveals-that-62-percentof-cfos-plan-sganda-cuts-this-year-due-to-coronavirus
André N. Meyer, Thomas Fritz, Gail C. Murphy, and Tom Zimmermann. 2014. Software Developers’
Perceptions of Productivity. In FSE ’14: Proceedings of the 22nd ACM SIGSOFT International Symposium
on the Foundations of Software Engineering. Retrieved January 21, 2021 from
https://www.microsoft.com/en-us/research/publication/software-developers-perceptions-of-productivity/
Microsoft Human Resources Business Intelligence (HRBI). 2020. Microsoft Pre-Opening Planning Survey.
Microsoft (Internal).
Microsoft Human Resources Business Intelligence (HRBI). 2020. Daily Pulse Survey. Microsoft (Internal).
Microsoft Human Resources Business Intelligence (HRBI). 2020. Impact of COVID and the Future of Work.
Microsoft (Internal).
Microsoft IDC. 2020. Microsoft IDC Pre-Opening Planning Survey. Microsoft (Internal).
Ingrid Millán, Nick Noel, Lucy Pérez, and Alfonso Pulido. 2020. US Hispanic and Latino lives and
livelihoods in the recovery from COVID-19 | McKinsey. McKinsey & Company. Retrieved January 17, 2021
from https://www.mckinsey.com/industries/public-and-social-sector/our-insights/us-hispanic-and-latino-livesand-livelihoods-in-the-recovery-from-covid-19
Courtney Miller, Paige Rodeghero, Margaret-Anne Storey, Denae Ford, and Thomas Zimmermann. 2021.
“How Was Your Weekend?” Software Development Teams Working From Home During COVID-19. In
International Conference on Software Engineering (ICSE) 2021. Retrieved from
https://arxiv.org/abs/2101.05877
Simon Mongey and Alex Weinberg. 2020. Characteristics of Workers in Low Work-From-Home and High
Personal-Proximity Occupations. Retrieved from https://bfi.uchicago.edu/working-paper/characteristics-ofworkers-in-low-work-from-home-and-high-personal-proximity-occupations/
Valerie J. Morganson, Debra A. Major, Kurt L. Oborn, Jennifer M. Verive, and Michelle P. Heelan. 2010.
Comparing telework locations and traditional work arrangements: Differences in work‐life balance support,
job satisfaction, and inclusion. Journal of Managerial Psychology 25, 6: 578–595.
https://doi.org/10.1108/02683941011056941
Danielle Muoio, Nick Niedzwiadek, and Marie J. French. 2020. Rural areas struggle with remote learning as
broadband remains elusive. Politico PRO. Retrieved January 17, 2021 from https://politi.co/3cGM5ZE
61

118. Prasanth Murali, Javier Hernandez, Daniel McDuff, Kael Rowan, Jina Suh, and Mary Czerwinski. 2021.
AffectiveSpotlight: Facilitating the Communication of Affective Responses from Audience Members during
Online Presentations. In ACM SIGCHI 2021.
119. E. Murphy-Hill, C. Jaspan, C. Sadowski, D. Shepherd, M. Phillips, C. Winter, A. Knight, E. Smith, and M.
Jorde. 2019. What Predicts Software Developers’ Productivity? IEEE Transactions on Software Engineering:
1–1. https://doi.org/10.1109/TSE.2019.2900308
120. Lucia Mutikani. 2020. U.S. home sales rack up record gain; tight supply, COVID-19 seen slowing
momentum. Reuters. Retrieved January 17, 2021 from https://www.reuters.com/article/us-usa-economyhousing-idUSKCN24N22B
121. Nina Shikaloff and Ryan Fuller. 2017. What great managers do daily. Microsoft Workplace Insights.
Retrieved from https://insights.office.com/productivity/what-great-managers-do-daily/
122. Mary C. Noonan and Jennifer L. Glass. 2012. The hard truth about telecommuting. Monthly Labor Review:
38–45.
123. NPD Group. 2020. March Cellular Data Usage Surges in the U.S. Amid COVID-19 Spread. NPD Group.
124. Brid O’Conaill, Steve Whittaker, and Sylvia Wilbur. 1993. Conversations Over Video Conferences: An
Evaluation of the Spoken Aspects of Video-Mediated Communication. Human–Computer Interaction 8, 4:
389–428. https://doi.org/10.1207/s15327051hci0804_4
125. Thomas A. O’Neill, Laura A. Hambley, and Angelina Bercovich. 2014. Prediction of cyberslacking when
employees are working away from the office. Computers in Human Behavior 34: 291–298.
https://doi.org/10.1016/j.chb.2014.02.015
126. Namrata S. Panwar and Alok Kumar Mishra. 2020. COVID-19 crisis and urbanization, migration and
inclusive city policies in India: A new theoretical framework. Journal of Public Affairs 20, 4: e2249.
https://doi.org/10.1002/pa.2249
127. Julianne Payne. 2018. Manufacturing Masculinity: Exploring Gender and Workplace Surveillance. Work and
Occupations 45, 3: 346–383. https://doi.org/10.1177/0730888418780969
128. Emily Peloquin, Sheri Panabaker, Patty Clusserath, Nalini Iyer, Hope Idaewor, and Emily Downing. 2020.
CSEO WFH Study / GESS (Global Employee Satisfaction Survey). Microsoft (Internal).
129. Nadja Popovich, Anjali Singhvi, and Matthew Conlen. 2020. Where Chronic Health Conditions and
Coronavirus Could Collide. New York Times. Retrieved from
https://www.nytimes.com/interactive/2020/05/18/us/coronavirus-underlying-conditions.html
130. Mark Powers. 2020. In China, managing people, relationships, and more meetings remotely. Home | Work
Blog from Microsoft Workplace Insights. Retrieved from https://insights.office.com/workplace-analytics/inchina-managing-teams-and-meetings-remotely/
131. Mark Powers and Jasminder Thind. 2020. Lessons from China: A return to the office, but not to the old way
of working. Workplace Analytics. Retrieved October 5, 2020 from https://insights.office.com/workplaceanalytics/lessons-from-china-a-return-to-the-office-but-not-to-the-old-way-of-working/
132. Dana Mattioli and Konrad Putzier. 2020. When It’s Time to Go Back to the Office, Will It Still Be There?
Wall Street Journal. Retrieved May 21, 2020 from https://www.wsj.com/articles/when-its-time-to-go-back-tothe-office-will-it-still-be-there-11589601618
133. Paul Ralph, Sebastian Baltes, Gianisa Adisaputri, Richard Torkar, Vladimir Kovalenko, Marcos Kalinowski,
Nicole Novielli, Shin Yoo, Xavier Devroey, Xin Tan, Minghui Zhou, Burak Turhan, Rashina Hoda, Hideaki
Hata, Gregorio Robles, Amin Milani Fard, and Rana Alkadhi. 2020. Pandemic Programming: How COVID19 affects software developers and how their organizations can help. Empirical Software Engineering 25, 6:
4927–4961. https://doi.org/10.1007/s10664-020-09875-y
134. Daniel M. Ravid, Jerod C. White, Dave L. Tomczak, Ahleah F. Miles, and Tara S. Behrend. 2020. A MetaAnalysis of the Effects of Digital Surveillance of Workers: A Psychology Focused Approach. In Microsoft
New Future of Work Symposium. Retrieved January 17, 2021 from https://www.microsoft.com/enus/research/publication/a-meta-analysis-of-the-effects-of-digital-surveillance-of-workers-a-psychologyfocused-approach/
135. Patricia Reaney. 2012. Sizable Minority Of Global Workers Don’t Commute To An Office. HuffPost.
Retrieved May 20, 2020 from https://www.huffpost.com/entry/workers-telecommute_n_1228004
136. Julie A. Rennecker, Alan R. Dennis, and Sean Hansen. 2010. “Invisible Whispering”: Restructuring Meeting
Processes with Instant Messaging. In Handbook of Group Decision and Negotiation, D. Marc Kilgour and
Colin Eden (eds.). Springer Netherlands, Dordrecht, 25–45. https://doi.org/10.1007/978-90-481-9097-3_3
137. Sean Rintel. 2010. Conversational management of network trouble perturbations in personal
videoconferencing. Retrieved May 20, 2020 from https://www.microsoft.com/en62

138.
139.

140.
141.
142.
143.
144.
145.
146.
147.
148.

149.
150.
151.

152.
153.
154.
155.

us/research/publication/conversational-management-of-network-trouble-perturbations-in-personalvideoconferencing/
Sean Rintel, Abi Sellen, Advait Sarkar, Priscilla Wong, Nancy Baym, and Rachel Bergmann. 2020. 2020
Study of Microsoft Employee Experiences in Remote Meetings During COVID-19 (Project Tahiti). Microsoft
Research. Retrieved from https://www.microsoft.com/en-us/research/project/meeting-during-covid-19/
Sean Rintel, Priscilla Wong, Advait Sarkar, and Abigail Sellen. 2020. Methodology and Participation for 2020
Diary Study of Microsoft Employees Experiences in Remote Meetings During COVID-19. Retrieved January
20, 2021 from https://www.microsoft.com/en-us/research/publication/methodology-and-participation-for2020-diary-study-of-microsoft-employees-experiences-in-remote-meetings-during-covid-19/
Elena Rocco. 1998. Trust breaks down in electronic contexts but can be repaired by some initial face-to-face
contact. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’98), 496–
502. https://doi.org/10.1145/274644.274711
Paige Rodeghero, Thomas Zimmermann, Brian Houck, and Denae Ford. 2020. Please Turn Your Cameras
On: Remote Onboarding of Software Developers during a Pandemic. arXiv:2011.08130 [cs]. Retrieved
January 19, 2021 from http://arxiv.org/abs/2011.08130
Karen Ruhleder and Brigitte Jordan. 2001. Co-Constructing Non-Mutual Realities: Delay-Generated Trouble
in Distributed Interaction. Computer Supported Cooperative Work 10, 1: 113–138.
https://doi.org/10.1023/A:1011243905593
Ryan Smith. 2020. How CEOs Can Support Employee Mental Health in a Crisis. Harvard Business Review.
Retrieved from https://hbr.org/2020/05/how-ceos-can-support-employee-mental-health-in-a-crisis
Harvey Sacks, Emanuel A. Schegloff, and Gail Jefferson. 1974. A Simplest Systematics for the Organization
of Turn-Taking for Conversation. Language 50, 4: 696–735. https://doi.org/10.2307/412243
Adam Satariano. 2020. How My Boss Monitors Me While I Work From Home. The New York Times.
Retrieved May 19, 2020 from https://www.nytimes.com/2020/05/06/technology/employee-monitoring-workfrom-home-virus.html
Abigail Sellen. 1995. Remote conversations: The effects of mediating talk with technology. Human-Computer
Interaction 10. Retrieved May 20, 2020 from https://www.microsoft.com/en-us/research/publication/remoteconversations-the-effects-of-mediating-talk-with-technology/
Teddy Seyed, Nathalie Riche, Ken Hinckley, Bill Buxton, Jonathan Goldstein, Michel Pahud, Nicolai
Marquardt, Molly Nicholas, Christian Holz, Hugo Romat, and Rojin Vishkaie. 2020. Devices at Home Survey.
Microsoft (Internal).
Neha Shah and Jonathan Larson. 2020. Toward resilience: Adapting to crisis through the lens of
organizational networks. Home | Work Blog from Microsoft Workplace Insights. Retrieved from
https://insights.office.com/networks/toward-resilience-adapting-to-crisis-through-the-lens-of-organizationalnetworks/
Kevin Sherman and Shailendra Hegde. 2020. When office work shifts to remote, what will we learn? Home |
Work Blog from Microsoft Workplace Insights. Retrieved from https://insights.office.com/workplaceanalytics/remote-work-data/
Patricia M. Sias, Hannah Pedersen, Erin B. Gallagher, and Irina Kopaneva. 2012. Workplace Friendship in the
Electronically Connected Organization. Human Communication Research 38, 3: 253–279.
https://doi.org/10.1111/j.1468-2958.2012.01428.x
Natalie Singer-Velush, Carlos Morales Torrado, and Ainize Cidoncha. 2020. In Microsoft Denmark, data and
inclusion are key to navigating disruption. Workplace Analytics. Retrieved January 16, 2021 from
https://insights.office.com/workplace-analytics/in-microsoft-denmark-data-and-inclusion-are-key-tonavigating-disruption/
Gurkaran Singh and David Spiers. 2020. E+D Engineering Systems Health. Microsoft (Internal).
Julia Sklar. 2020. ‘Zoom fatigue’ is taxing the brain. Here’s why that happens. National Geographic.
Retrieved May 20, 2020 from https://www.nationalgeographic.com/science/2020/04/coronavirus-zoomfatigue-is-taxing-the-brain-here-is-why-that-happens/
Jared Spataro and Ronnie Martin. 2020. Presentation on research behind blog post "A pulse on employees’
wellbeing, six months into the pandemic". Retrieved January 21, 2021 from https://www.microsoft.com/enus/microsoft-365/blog/2020/09/22/pulse-employees-wellbeing-six-months-pandemic/
Keri K. Stephens. 2012. Multiple Conversations During Organizational Meetings: Development of the
Multicommunicating Scale. Management Communication Quarterly 26, 2: 195–223.
https://doi.org/10.1177/0893318911431802

63

156. Meghan Stockdale, Therese Okraku, Megan Brown, Jamie Miller, Bella Chiu, and Shelly Marston. 2020.
Study of Impact on Information Worker Productivity. Microsoft (Internal).
157. Margaret-Anne Storey, Emelie Engstrom, Martin Höst, Per Runeson, and Elizabeth Bjarnason. 2017. Using a
Visual Abstract as a Lens for Communicating and Promoting Design Science Research in Software
Engineering. In 2017 ACM/IEEE International Symposium on Empirical Software Engineering and
Measurement (ESEM), 181–186. https://doi.org/10.1109/ESEM.2017.28
158. Margaret-Anne Storey, Thomas Zimmermann, Christian Bird, Jacek Czerwonka, Brendan Murphy, and Eirini
Kalliamvakou. 2019. Towards a Theory of Software Developer Job Satisfaction and Perceived Productivity.
IEEE Transactions on Software Engineering: 1–1. https://doi.org/10.1109/TSE.2019.2944354
159. Joanne Suomi, Douglas Collier, and Lou Brown. Factors Affecting the Social Experiences of Students in
Elementary Physical Education Classes. Journal of Teaching in Physical Education 22, 2: 186–202.
160. Alaina Talboy and Paula Bach. 2020. COVID-19 Impact to IWs Research Series: Communication Difficulties.
Microsoft (Internal).
161. Alaina Talboy and Paula Bach. 2020. COVID-19 Impact to IWs Research Series: Work-Life Balance
Difficulties. Microsoft (Internal).
162. Alaina Talboy and Paula Bach. 2020. COVID-19 Impact to IWs Research Series: Browser and Work Tool
Difficulties. Microsoft (Internal).
163. John Tang. 2021. Understanding the Telework Experience of People with Disabilities. In ACM CSCW ’21.
164. Jaime Teevan and Brent Hecht. 2020. How research can enable more effective remote work. Microsoft
Research. Retrieved January 20, 2021 from https://www.microsoft.com/en-us/research/blog/how-researchcan-enable-more-effective-remote-work/
165. Jaime Teevan and Alexander Hehmeyer. 2013. Understanding how the projection of availability state impacts
the reception incoming communication. In Proceedings of the 2013 conference on Computer supported
cooperative work - CSCW ’13, 753. https://doi.org/10.1145/2441776.2441860
166. Alan Thomas. 2020. Post-pandemic effects on e-mail. Microsoft (Internal).
167. Sarah Tian and Yonatan Dubinsky. 2020. Information Security Professionals in the time of COVID-19.
Microsoft (Internal).
168. Ozgur Turetken, Abhijit Jain, Brandi Quesenberry, and Ojelanki Ngwenyama. 2011. An Empirical
Investigation of the Impact of Individual and Work Characteristics on Telecommuting Success. IEEE
Transactions on Professional Communication 54, 1: 56–67. https://doi.org/10.1109/TPC.2010.2041387
169. U.S. Bureau of Labor Statistics. 2020. Frequently asked questions: The impact of the coronavirus (COVID19) pandemic on The Employment Situation for May 2020. Retrieved from
https://www.bls.gov/cps/employment-situation-covid19-faq-may-2020.pdf
170. U.S. Bureau of Labor Statistics. Labor force characteristics by race and ethnicity, 2019. Retrieved January 21,
2021 from https://www.bls.gov/opub/reports/race-and-ethnicity/2019/home.htm
171. US Census Bureau. 2020. Week 13 Household Pulse Survey: August 19 – August 31. Census.gov. Retrieved
January 17, 2021 from https://www.census.gov/data/tables/2020/demo/hhp/hhp13.html
172. D. Alexander Varakin, Daniel T. Levin, and Roger Fidler. 2004. Unseen and Unaware: Implications of Recent
Research on Failures of Visual Awareness for Human-Computer Interface Design. Human-Computer
Interaction 19, 4: 389–422. https://doi.org/10.1207/s15327051hci1904_9
173. Roel Vertegaal, Ivo Weevers, and Changuk Sohn. 2002. GAZE-2: an attentive video conferencing system. In
CHI ’02 Extended Abstracts on Human Factors in Computing Systems (CHI EA ’02), 736–737.
https://doi.org/10.1145/506443.506572
174. Vicus Partners. 2020. 6 Office Design Trends For the Post Covid-19 World. Vicus Partners. Retrieved
January 16, 2021 from https://vicuspartners.com/articles/6-office-design-trends-post-covid-19/
175. Mihaela Vorvoreanu and Carl H Botan. 2000. Examining electronic surveillance in the workplace: A review
of theoretical perspectives and research findings. In the Conference of the International Communication
Association.
176. Yun Wang, Ying Liu, Weiwei Cui, John Tang, Haidong Zhang, Doug Walston, and Dongmei Zhang. 2020.
Returning to the Office During the COVID-19 Pandemic Recovery: Early Indicators from China. Microsoft
(Internal).
177. Mark Wilson. 2020. Move over, Zoom. This magic interface is the future of videoconferencing. Fast
Company. Retrieved May 21, 2020 from https://www.fastcompany.com/90498000/move-over-zoom-thismagic-interface-is-the-future-of-videoconferencing

64

178. Barbara A. Winstead, Valerian J. Derlega, Melinda J. Montgomery, and Constance Pilkington. 1995. The
Quality of Friendships at Work and Job Satisfaction. Journal of Social and Personal Relationships 12, 2: 199–
215. https://doi.org/10.1177/0265407595122003
179. Hana Wolf. 2020. Learnings from LinkedIn Online Events. LinkedIn User Experience (Internal).
180. Hana Wolf, Leslie Forman, Sunny Patel, Anton Zadorozhnyy, Lindsay Kelly, and Amulya Aradhyula. 2020.
Project Moxie. Microsoft (Internal).
181. Muiris Woulfe. 2020. OMEX Survey. Microsoft (Internal).
182. Longqi Yang, Sonia Jaffe, David Holtz, Siddharth Suri, Shilpi Sinha, Jeffrey Weston, Connor Joyce, Neha
Shah, Kevin Sherman, C.J. Lee, Brent Hecht, and Jaime Teevan. 2020. How Work-From-Home Affects Work
Practices: A Large-Scale and Quasi-experimental Study. arXiv:2007.15584 [cs]. Retrieved from
http://arxiv.org/abs/2007.15584
183. Josh Zumbrun. 2016. The Rise of Knowledge Workers Is Accelerating Despite the Threat of Automation.
WSJ. Retrieved January 24, 2021 from https://blogs.wsj.com/economics/2016/05/04/the-rise-of-knowledgeworkers-is-accelerating-despite-the-threat-of-automation/
184. 2009. Geographic Pay Differential Practices. Retrieved from https://www.shrm.org/resourcesandtools/hrtopics/compensation/pages/geographicpay.aspx
185. 2020. Labor Force Statistics from the Current Population Survey. U.S. Bureau of Labor Statistics. Retrieved
from https://www.bls.gov/cps/cpsaat18.htm
186. 2020. Moms reduce work more than dads during pandemic — study. Marketplace. Retrieved January 17,
2021 from https://www.marketplace.org/2020/07/16/moms-are-reducing-work-hours-4-5-times-more-thandads-during-pandemic/
187. Outdoor Education Update. Retrieved January 21, 2021 from
https://www.seattleschools.org/district/calendars/news/what_s_new/outdoor_education_update
188. Mind Share Partner’s 2019 Mental Health at Work Report. Mind Share Partners. Retrieved from
https://www.mindsharepartners.org/mentalhealthatworkreport

65
