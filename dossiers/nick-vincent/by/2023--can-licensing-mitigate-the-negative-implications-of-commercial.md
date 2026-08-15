---
title: "Can Licensing Mitigate the Negative Implications of Commercial Web Scraping?"
person: "nick-vincent"
section: "by"
type: "journal-article"
year: 2023
date: "2023-10-13"
venue: "Workshop at CSCW 2023, 2023"
authors: "Hanlin Li, Nicholas Vincent, Yacine Jernite, Nick Merrill, Jesse Josua Benjamin, Alek Tarkowski"
source_url: "https://dl.acm.org/doi/abs/10.1145/3584931.3611276"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W4387607091; CV ref [W6]; Full text via the OpenAlex Content API (GROBID TEI of the OA PDF) (https://content.openalex.org/works/W4387607091.grobid-xml)."
---

# Can Licensing Mitigate the Negative Implications of Commercial Web Scraping?

## Full text

The rise of prominent AI models such as ChatGPT and Stable Diffusion has brought the scale of commercial web scraping to the forefront attention of content creators and researchers.Billions of webpages and images are used to train these models without content creators' knowledge, sparking extensive criticism and even lawsuits against AI firms.Amidst such debates, licensing is proposed by researchers and legal experts to be a potential approach to mitigate content creators' concerns and promote more responsible data reuse.However, it remains unclear what specific licensing terms will be effective and what sociotechnical environments are necessary to facilitate the use of licensing at scale.This workshop will provide a venue for researchers, content creators, and legal experts to identify opportunities and challenges in licensing content in the context of AI training.


## INTRODUCTION

Web scraping has become a prominent way for tech companies, from OpenAI to Google, to collect data and content from other organizations and platforms.Yet at times, scraping may impose costs on individuals and societies in the form of wealth concentration, privacy invasion, and lack of consent, in addition to potential copyright infringements [8].As more AI systems that rely on web scraping for training data are developed and deployed, content producers have expressed concerns about the extractive nature of this data collection technique and the consequences of its deployment [10].

In the midst of these potential negative implications, most proposals have focused on technical remediation such as protecting content creators' personal style [7] and supporting opt-out requests for scraped datasets [11]; scholars and content creators have proposed a social mechanism to promote more responsible data use: old-fashioned licensing [3,9].There are two specific ways of licensing web content.The first and more long-standing approach is to license copyrighted content with a fee as a way to protect creators' copyrights, as commonly seen in the creative industry.The second and emergent approach is to license content with use restrictions -otherwise known as behavioral use licensing Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.Copyrights for components of this work owned by others than ACM must be honored.Abstracting with credit is permitted.To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.Request permissions from permissions@acm.org.or "Responsible AI Licensing" (RAIL) -to promote and enforce ethical norms around data and content [3].The second approach serves to deter certain controversial use of datasets (e.g."cannot be used to impersonate others without their consent") and has been gaining rapid traction among developers and researchers [1].For example, on Hugging Face, over 800 datasets have been licensed under RAIL-related licenses.Other open datasets also take approaches similar to behavioral use licensing.For example, the Casual Conversations Dataset was shared by Meta under the term that this dataset should not be used to infer personal information, among many other restrictions [6].Theoretically, copyright licensing and behavioral use licensing complement each other; while copyright licenses protect content creators' copyrights, behavioral use licenses give content creators rights to privacy and control over their work.

However, key sociotechnical questions about how these licensing mechanisms will play out among content creators We will host a series of lightning talks followed by group discussions with workshop participants.We will welcome presentations that address the following aspects of web scraping and licensing:

• Understanding the current landscape of web scraping and investigating how firms and developers approach the legal and ethical risks of scraping and aggregating web content.

• Understanding current practices around licensing among content creators, e.g.how content creators license their content and what rights they would like to preserve when making their content publicly visible.

• Identifying specific opportunities to operationalize licensing to counter the negative effects of web scraping and other unauthorized data reuses, including but not limited to privacy violation, lack of compensation for content creators, copyright infringements, etc.

• Examining parallels between licensing and other creator-oriented responsible AI initiatives, such as data stewardship [2,5] and refusal [4].

This exchange-oriented part will be supplemented by design tasks in groups.Participants and presenters will build upon ideas and research discussed in earlier sessions to chart out ways to implement licensing in content creation and software development practices.In particular, we hope to make progress in the following directions:

• How will web scraping practices likely adapt in response to copyright and behavioral use licensing?

• What do we need to do to realistically impact commercial web scraping practices through licensing?

• How to help content creators choose licensing terms and set licensing fees?

• Is there any existing infrastructure that we may learn from about facilitating the adoption of copyright and behavioral use licensing?

• How will copyright and behavioral use licensing intersect with Creative Commons licenses?

More broadly, this workshop will aim to foster interdisciplinary conversations about data scraping and reuse, open source, and responsible AI.We will reflect on what other governance frameworks, besides licensing, may be helpful in fostering responsible innovation and how to navigate the tension between openness and privacy in data reuse.


## WORKSHOP LOGISTICS

We plan to host a one-day virtual workshop that consists of lightning talks and group discussions.


## Planned Activities

We will start with open remarks by organizers to set the workshop's agenda, followed by sessions of lightning talks.Each session of lightning talks will have time for participants to ask questions and provide feedback.From past experience, we find that lightning talks help stimulate discussion among workshop participants.

After lightning talks, participants will build upon prior discussion to prototype licensing scenarios, chains of events, artifacts, and stakeholders that may emerge in the process from scraping data to model development (e.g., of a Large Language Model) and deployment.These scenarios will be discussed to arrive at a pragmatic output for the workshop around which participants can gather and build a community or generate forms of dissemination, such as a spectrum or matrix for decision-making in the licensing process.

We will encourage collaborative note-taking using Miro.Participants will be invited to capture their takeaways, questions, and discussions on a Miro board shared with the group.At the end of the workshop, we will have a short debriefing session to discuss next steps and opportunities to continue the discussion on data scraping and licensing.


## Recruitment

Our workshop will be open to all CSCW attendees but participants who are interested in presenting will need to submit an extended abstract.We will post our call for participation on social media and directly to communities that create, aggregate, and maintain datasets.We welcome participation and expertise from a wide range of domains and disciplines, including but not limited to social computing, copyright, and open source.Abstracts will be reviewed by our organizing team for relevance.We will have two to three reviewers for each submission and reviewer comments will be shared with authors.We welcome submissions in various formats, from analytical reports to essays to design fiction.Accepted abstracts will be given a lightning talk opportunity.We expect a maximum of 50 participants for this workshop.


## Post-Workshop Plans

We will summarize our workshop discussion in the format of a public-facing blog post.We hope to use the blog post as a call for the broader creator, developer, and researcher communities to consider and adopt licensing as a way to mitigate the negative implications of web scraping and as a step toward responsible AI.We will solicit feedback from workshop participants on our blog post before making it public and we plan to create an online space in the form of a listerv or Google Group to continue the conversation.


## Organizers

Our team consists of researchers and practitioners from a diversity of domains including research, policymaking, and advocacy.Part of our team members is associated with the RAIL initiative 1 and we hope to use this workshop as an opportunity to connect the CSCW community with the RAIL initiative to exchange research ideas and identify opportunities to collaborate on data governance.

Hanlin Li is an assistant professor at the University of Texas at Austin.She studies the social and economic impact of user-generated data and explores approaches to collective, responsible data governance.

Nicholas Vincent is a postdoc scholar at the University of California, Davis.His work focuses on studying the dependence of modern computing technologies, including the broad set of systems called "AI", on human-generated data, with the goal of mitigating negative impacts of these technologies.

and those that seek to scrape content remain unanswered.Who has the right to license what type of content and what incentives are necessary for firms or their scrapers to honor licensing agreements?What license clauses are desirable and effective in mitigating concerns about unauthorized content reuse?Ultimately, how can licensing mitigate various negative implications of web scraping?This workshop will explore the intersection of licensing and content scraping and aim to offer a pragmatic roadmap toward responsible data collection and use.

Can licensing mitigate the negative implications of commerical web scraping?Conference acronym 'XX, June 03-05, 2018, Woodstock, NY
