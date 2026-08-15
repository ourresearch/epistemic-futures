---
title: "Governing AI Through SEC Disclosure: Materiality Standards and Incident Reporting—Lessons from Cybersecurity"
person: tim-oreilly
section: by
type: report
year: 2025
date: 2025-10-30
venue: "AI Disclosures Project, Social Science Research Council (Working Paper No. 04, 2025/10)"
authors: "Ilan Strauss; Tim O'Reilly; Sruly Rosenblat; Isobel Moure"
source_url: https://ai-disclosures.org/assets/papers/Governing-AI-Through-SEC-Disclosure-Strauss-OReilly-Rosenblat-Moore_SSRC_10302025.pdf
retrieved: 2026-08-13
content: full-text
notes: "Open working paper PDF from the AI Disclosures Project (SSRC); text extracted with pdftotext -layout. DOI 10.35650/AIDP.4120.d.2025."
---

# Governing AI Through SEC Disclosure: Materiality Standards and Incident Reporting—Lessons from Cybersecurity

## Full text

WORKING PAPER SERIES

Governing AI Through SEC Disclosure

Materiality Standards and Incident Reporting—
Lessons from Cybersecurity

Ilan Strauss

Program Director

Social Science Research Council

Tim O’Reilly

Program Director

Social Science Research Council

Sruly Rosenblat

Program Associate

Social Science Research Council

Isobel Moure

Program Associate

Social Science Research Council

                                                WORKING PAPER NO. 04

                                                             2025/10
About the AI Disclosures Project
Led by technologist Tim O’Reilly and economist Ilan Strauss, the AI Disclosures Project addresses
the potentially harmful societal impacts of AI's unrestrained commercialization. By improving
corporate and technological transparency and disclosure mechanisms, it aims to ensure that
economic incentives don't compromise safety or equity, and avoid fostering excessive risks.
Disclosures are vital for well-functioning markets yet remain lacking in AI. Just as financial
disclosure standards fostered robust securities markets, standardized AI disclosures can build trust,
expedite adoption, and spur innovation. Through research, collaboration, and policy engagement,
the AI Disclosures Project aims to develop a systematic framework for meaningful “Generally
Accepted AI Management Principles.” The project is generously funded by the Omidyar Network,
Alfred P. Sloan Foundation, and Patrick J. McGovern Foundation. 

DOI: 10.35650/AIDP.4120.d.2025  

This working paper can be referenced as follows: 
Strauss, Ilan, O’Reilly, Tim, Rosenblat, Sruly, and Isobel Moure. “Governing AI Through SEC
Disclosure.” Working Paper. Social Science Research Council, October 2025. https://www.ssrc.org/
publications/governing-ai-through-sec-disclosure-materiality-standards-and-incident-reporting-
lessons-from-cybersecurity/

 

                                                                            Website: AI Disclosures Project

                                                                            Substack: Asimov’s Addendum

                                                                            X: @AIDisclosures
               Governing AI Through SEC Disclosure
        Materiality Standards and Incident Reporting – Lessons from Cybersecurity

             Ilan Strauss ∗1,2 , Tim O’Reilly1,2,3 , Sruly Rosenblat1 , and Isobel Moure1

                           1
                               AI Disclosures Project, Social Science Research Council
                 2
                     Institute for Innovation and Public Purpose, University College London
                                                  3
                                                      O’Reilly Media

                                                       Abstract

          AI technologies now contribute substantially to corporate performance and risk but using
      several data points we show that investors lack decision-useful information. Drawing on over
      7,800 8-K filings on AI by companies we show that around two-thirds are overwhelmingly pos-
      itive in nature and avoid ‘negative’ news. Drawing on the SEC’s 2023 cybersecurity reporting
      rule, we propose a materiality-first AI disclosure regime involving: (1) SEC guidance clarifying
      what a ‘material’ AI risk is; (2) A dedicated AI-incident item on the 8-K form; (3) A standing
      section in the annual 10-K form on AI strategy, governance, risk, and dependencies; and (4)
      SEC enforcement against AI-washing and other violations. We urge reversing 2012 JOBS Act
      changes that let large private firms avoid public reporting and registration. Focusing on material
      impacts – not abstract capabilities – offers an important underexplored avenue to discipline AI
      deployment and improve market oversight.

      Keywords: AI Governance, SEC Reporting, AI Disclosures, AI washing, 8-K, 10-K.

  ∗
     We gratefully acknowledge funding and support from Alfred P. Sloan Foundation, the Omid-
yar Network, and the Patrick J. McGovern Foundation.         Corresponding author is Dr.   Ilan Strauss:
istrauss@aidisclosures.org.      This draws on:    Ilan Strauss and Tim O’Reilly, “AI Isn’t a Super-
intelligence.  It’s a Market in Need of Disclosure,” Tech Policy Press, October 27, 2025, https:
//www.techpolicy.press/ai-isnt-a-superintelligence-its-a-market-in-need-of-disclosure;              and
Strauss, Ilan, O’Reilly, Tim, Rosenblat, Sruly, and Isobel Moure.    “Governing AI Through SEC Disclo-
sure.” Policy Brief. Social Science Research Council, October 2025. https://www.ssrc.org/publications/
governing-ai-through-sec-disclosure-materiality-standards-and-incident-reporting-lessons-from-cybersecurity/
1     The Need for Material Corporate AI Disclosures
The recent push by the federal government to move away from quarterly corporate reporting has
sparked a debate about the value of corporate reports, with important takeaways for AI-related
reporting requirements [Atkins, 2025].

John Authers notes in the Financial Times [Authers, 2025], quoting Sarah Williamson at FCLT
Global, that disclosures are not really about timing, but “materiality” (i.e., importance): “What
really matters . . . is the materiality of what to tell investors, not the periodicity.” And the bar for
what is material should be lower, she argues. That is, more events should be considered materially
important for companies to disclose, rather than fewer.

This principle has potentially far-reaching implications for AI disclosures. Rather than getting
caught up in debates over how often AI companies should report, we should be asking: What risk
events in AI systems are already material enough to investors to warrant immediate disclosure by
corporations? And how exactly should these be disclosed by public companies?

In line with our previous work on corporate disclosures for large digital platforms with Prof. Mari-
ana Mazzucato, we argue that disclosures must evolve with the changing structure of the economy,
reflecting the new types of risks and operational facts that are material to investors [Mazzucato
et al., 2023, O’Reilly et al., 2023]. This ultimately prioritizes disclosure quality – judged by its
relevance and depth – above reporting frequency.

SEC Policy Suggestions. Drawing on the SEC’s 2023 rule on cybersecurity incident reporting
[U.S. Securities and Exchange Commission, 2023a], this paper proposes the following steps to bring
AI governance within the SEC’s existing public reporting framework:

    1. Clarify how existing SEC disclosure rules apply to AI. The SEC should issue “Disclosure
      Guidance” [U.S. Securities and Exchange Commission, 2025b] specifying what AI activities
      and risks are material and should be disclosed. Clearly defining material AI incidents –
      e.g., systematic model failures, major service outages, errors requiring widespread customer
      remediation, loss of essential third-party model access – will help companies disclose only
      what matters.

    2. Integrate AI-specific risks into existing disclosure filings. In 2023, the SEC introduced a
      cyber rule [U.S. Securities and Exchange Commission, 2024b] requiring companies to report
      material cyber events within four days on Form 8-K and describe cyber-risk management in
      annual 10-Ks. We suggest the same for AI: add an AI incident item to the 8-K and require
      annual discussion of AI governance and risk management.

    3. Enforce the rules. In crypto and cyber [Simona, 2025, U.S. Securities and Exchange Com-
      mission, 2024b], improved disclosures followed real prosecutions [Valdetero and van Wengen,
      2025, Jennings et al., 2011]. The SEC should continue to bring any material cases against AI

                                                   1
        washing, misleading claims, and fraud.1

    4. Remove the loopholes that allow private companies to avoid going public. For any of these
        disclosure obligations to apply to OpenAI and Anthropic, as private entities, 2012 JOBS Act
        must be reversed. The act made it easier for large capital raisers to avoid public disclosure
        by raising money from private capital through special purpose vehicles (SPVs). Previously,
        companies like Google and Facebook became too big to remain private and were forced to go
        public. Those obligations were watered down significantly in 2012.

In contrast to managing AI through arbitrary technical thresholds, our approach emphasizes AI
governance based initially on its potential material impacts to the real economy. The reporting met-
ric is not an abstract AI capability but consequential effects on a company’s operations, customers,
or financial results – a language legislators, courts, investors, and the public already understand.
Our recommendations support AI-related disclosure obligations that are more comparable, timely,
and granular – and that incentivize greater company risk mitigation measures.

2       Literature Review
Corporate disclosure regimes address information asymmetries through mandatory reporting re-
quirements, anchored in the materiality principle articulated in TSC Industries v. Northway [U.S.
Supreme Court, 1976]. Material information is that for which there is a substantial likelihood that
a reasonable investor would consider it important in making an investment decision.2

The Securities Acts of 1933 and 1934 codified disclosure as the primary regulatory mechanism,
premised on the view that transparency enables market discipline rather than direct government
intervention [Coffee, 1984, Mahoney, 1995]. Regulation FD (2000) further curbed selective disclo-
sure. Evidence suggests well-designed regimes improve risk management and market transparency,
especially when paired with credible enforcement against misstatements [Ettredge and Richardson,
2003, Gordon et al., 2010]. Seminal theory and evidence linking disclosure to market outcomes
and managerial incentives include: [Diamond and Verrecchia, 1991, Botosan, 1997, Lambert et al.,
2007, Healy and Palepu, 2001, Verrecchia, 2001, Leuz and Wysocki, 2016].

The SEC’s framework has proven adaptable across technological and economic shifts – from environ-
mental disclosures [Cohen, 1966] to cybersecurity, though effectiveness depends on clear guidance,
timely reporting mechanisms, and credible enforcement [Healy and Palepu, 2001, Jennings et al.,
2011]. The SEC’s iterative updates to Regulation S-K, including the 2020 modernization of business
and risk factor disclosure requirements [U.S. Securities and Exchange Commission, 2019], reflect
    1
    Compare with the arguments in: Atkins and Bondi [2008].
    2
    Basic v. Levinson (probability–magnitude), Staff Accounting Bulletin No. 99 (qualitative factors can render small
items material), Matrixx Initiatives v. Siracusano (materiality not reducible to numerical thresholds), and Omnicare
v. Laborers (opinions and omissions) [U.S. Supreme Court, 1988, U.S. Securities and Exchange Commission, 1999,
Matrixx Initiatives, Inc. v. Siracusano, 2011, Court, 2015].

                                                         2
some efforts to maintain disclosure relevance amid evolving sources of corporate risk [U.S. Securi-
ties and Exchange Commission, 2019]. The SEC’s 2020 modernization efforts also aimed to curb
boilerplate disclosure and elicit decision-useful, firm-specific discussion of risks, but it’s unclear if
it actually did so [U.S. Securities and Exchange Commission, 2019].

Despite this adaptability, the framework has not always been applied to new areas of economic
significance, such as large diversified digital platforms and their non-price operating disclosures
[Mazzucato et al., 2023, O’Reilly et al., 2023].

Regulatory precedents show how emerging risks can be incorporated into SEC frameworks. The 2024
climate-disclosure rule successfully organizes reporting around governance, strategy, risk manage-
ment, and metrics (portions stayed pending litigation) and draws on the TCFD template that
the ISSB’s IFRS S1–S2 has now generalized into a global investor-focused baseline [U.S. Securities
and Exchange Commission, 2024a, Bloomberg and Task Force on Climate-related Financial Dis-
closures, 2017, IFRS, 2023, IFRS Foundation, 2025]. The ISSB’s IFRS S1–S2 standards require
companies to disclose sustainability and climate risks using four mandatory categories: governance
structures (who is accountable), strategy (how risks affect the business model and cash flows), risk-
management processes, and quantitative metrics (including Scope 1–3 emissions). This framework
is designed to produce comparable, standardized information that investors can use to assess and
price sustainability risks across companies [IFRS Foundation, 2025, IFRS, 2023]. Cyber is another
salient precedent we address later [U.S. Securities and Exchange Commission, 2023a]. These prece-
dents suggest AI risks – which affect companies’ governance, strategy, and operational resilience –
can fit fairly naturally within existing disclosure architecture. AI does, however, present distinct
and unique challenges: black-box opacity, rapid capability evolution, emergent behaviors, difficulty
attributing causation [Kaur et al., 2022] – all of which cannot be fully addressed within a corporate
disclosures framework.

Existing incorporation of AI risks in the SEC’s regime has so far occurred primarily through the
enforcement channel (e.g., “AI-washing”) rather than via prescriptive disclosure items [Vanderford,
2023, Leiva et al., 2025]. But the two work best in combination with one another to ensure no gaps
in coverage.

Internationally, the EU AI Act imposes post-deployment obligations on high-risk AI systems:
providers must operate post-market monitoring, maintain and review logs, and report serious inci-
dents to market-surveillance authorities within specified timelines. Deployers must ensure human
oversight, maintain logs, and promptly inform providers and authorities upon detecting serious
incidents. A voluntary GPAI Code of Practice targets general-purpose model providers pending
full standards rollout [European Parliament, 2025].

The EU governance duties complement rather than replace financial reporting obligations though
and are no substitute for leveraging existing established societal-scale institutions for governing

                                                   3
corporate risks. That being said, these emerging EU disclosure and monitoring obligations for AI
risks create data points and tools that could be incorporated into SEC guidance, since companies
subject to EU AI Act requirements are already collecting incident data, logs, and monitoring
reports.

3     AI as a Market Technology – Materiality and Disclosure
Paul Atkins, the chair of the U.S. Securities and Exchange Commission (SEC), argues that corporate
disclosures should be driven by the materiality principle [Atkins, 2025] – disclose what a reasonable
investor would care about when making an investment decision [U.S. Supreme Court, 1976]. Let’s
“stick to business”. And what is becoming a bigger business than AI?

AI’s contribution to the economy is already staggering: In the first half of 2025, AI-related capital
expenditures contributed 1.1% to GDP growth [Aliaga, 2025], more than the U.S. consumer, if the
capital items were not largely imported. As a percent of GDP [Kedrosky, 2025], capital expenditures
on data centers (1.2%) were greater than the telecom spending in all of 2020 (1%), estimates
economist Paul Kedrosky. However, much of this is imported capital inputs and so would be
deductions from GDP [Tan, 2025]. Investments in AI are on track to surpass those made in the
internet during the boom years of 1995-2000 [Ip, 2025]. Meanwhile 80% of the stock market gains
in 2025 (until October) were due to AI companies [Cembalest, 2025].

3.1   AI as a commercially-orientated market technology

Princeton computer scientists Arvind Narayanan and Sayash Kapoor call AI a ‘normal technology’
– transformative but not unlike previous inventions, such as railroads or electricity, where impacts
were felt gradually over time as adoption ramped up [Narayanan and Kapoor, 2025]. ChatGPT’s
rapid uptake illustrates that digital markets are the ultimate ‘normalizing’ force, though. Once a
market takes hold, its logic imprints itself into a technology’s DNA. Social media began as a way
to stay connected with friends through a social graph, but monetization pressures transformed it
into an engagement-maximizing machine with endless scroll and algorithmically-driven recommen-
dations added to keep users addicted. OpenAI CEO Sam Altman calls algorithmic feeds “the first
at-scale misaligned AIs” [Altman, 2025]. AI’s sycophantic capabilities, monetized as companions
[Fried, 2025] or bottomless video feeds [Campbell, 2025], already exhibit a similar trajectory.

Given AI’s commercial character, we argue that public oversight should start with the SEC’s
corporate disclosure regime. AI markets currently lack full and timely information, since prominent
AI companies remain private and, in the absence of guidance, companies disclose platitudes[Uberti-
Bona Marin et al., 2025]. In turn, allocations of AI-related capital cannot be properly evaluated,
litigation is ballooning [Williams and Csathy, 2025], ‘AI washing’ and fraud are commonplace, and
technologies are being deployed prematurely under a ‘move fast and break things’ ethos [Leiva

                                                 4
et al., 2025, Milstead et al., 2025, The Economist, 2025, O’Reilly and Strauss, 2025].

After the 1929 crash, the SEC mandated corporate disclosures to surface material risks to investors
by requiring companies to publish annual 10-K reports, quarterly 10-Qs, and event-driven 8-Ks
when an incident occurs. This remains one of the few proven systems for assessing corporate risk
at scale.

The SEC’s ‘materiality’ standard transforms private knowledge into public disclosure [Hadfield and
Clark, 2023], creating the information substrate on which markets for audit, insurance, and research
can operate. This ecosystem not only informs but disciplines, rewarding sound AI governance
through lower capital costs and punishing poor risk management through market pressures.

4        Cyber Risks as a Model Disclosure Framework for AI-Related
         Risks
Perhaps as a result of a recent proposal from the Long Term Stock Exchange,3 President Trump
proposed that public companies’ quarterly reporting should instead become biannual (twice a year)
[Driebusch, 2025, Financial Times, 2025]. Trump made the case for it based on the same LTSE ar-
gument: that quarterly reporting places undue burdens on public companies and pushes executives
into short-termism – so-called “expectations management.”

Time-based reporting requirements incentivize companies to structure decisions around a company’s
financial calendar. But this might delay crucial information from being released by companies to
the public as they occur.

The 8-K form offers a solution for this issue. The 8-K can be thought of as a breaking news
bulletin, used by the corporations to announce significant events within four business days. The
list of “Items” that triggers a filing can vary. Many items are triggered automatically by an event,
like a corporate bankruptcy, others are based on the company’s judgment around whether the event
is “material” i.e., sufficiently likely that a reasonable investor would care about it – and only then
would they file an 8-K form. A cybersecurity incident is one such “if it’s important enough” thing
to disclose (Item 1.05).

An important and relatively new corporate disclosure requirement that uses the 8-K Form is the
SEC’s 2023 Cybersecurity Incident rule for public companies [U.S. Securities and Exchange Com-
mission, 2023a]. The Cyber rule says that when a company suffers a material cybersecurity incident
it must report it to shareholders within four business days through the 8-K Form. And when it’s
a material cyber event impacting shareholders, then it can be filed through the newly added Item
1.05, specifically for cyber incidents.
    3
        Tim O’Reilly is an investor in the Long Term Stock Exchange.

                                                          5
In combination with strong SEC enforcement, the Cyber rule seems to have worked [U.S. Secu-
rities and Exchange Commission, 2023a]. Cyber incidents are disclosed in a far more timely and
comparable manner now, and companies appear to be devoting more resources to the problem.
Moreover, companies absorbed these new requirements with ease because they were well prepared
from previous guidance.

Part of the Rule’s innovation is that the material event-triggered 8-K filing for cyber incidents
sits alongside a new standing annual 10-K disclosure requirement for companies specifically for
cyber-related issues (Reg S-K Item 106), covering things like board and management oversight,
processes for identifying and managing material cyber risks, whether such risks materially affect
the company, and more.

This did not come out of the blue. It built on two decades of guidance beginning with the 2011 CF
Disclosure Guidance on cybersecurity risks [U.S. Securities and Exchange Commission, Division of
Corporation Finance, 2011, U.S. Securities and Exchange Commission, 2023a]. The Commission
progressed from interpretive guidance (2011) and a Commission statement (2018) to a 2023 final
rule that created Form 8-K Item 1.05 for material cyber incidents and Regulation S-K Item 106 for
governance, strategy, and risk processes, with the aim of delivering “timely, consistent, comparable,
decision-useful” information [U.S. Securities and Exchange Commission, Division of Corporation
Finance, 2011, U.S. Securities and Exchange Commission, 2018, 2023a].

Next, the question then is whether AI-specific risks require a similar treatment to cyber ones.
Below we show that a substantial “disclosure gap” already exists for AI. This is the gap between
the AI-risks already out there facing AI companies, and what they are currently disclosing.

5     Evidence on the Disclosure Gap
What corporate reporting would enable responsible investment decisions by investors about AI
companies? Share prices are unable to reveal inadequate disclosure – since by definition they only
incorporate information already available to the market. But several other data sources can be
used to clearly highlight disclosures that investors and the market are demanding by companies
around their AI usage. We look at these sources one by one.

5.1   Litigation

Litigation shows market dissatisfaction with existing corporate AI disclosures to be high. Fisher
Phillips’ AI litigation tracker for the U.S. currently shows 92 cases [Fisher & Phillips LLP, 2025].
Litigation on securities class action lawsuits covering false or misleading statements on AI is on
a near exponential rise in the U.S., from 7 cases in 2023, 14 cases in 2024, and 12 cases so far
in 2025 [Walker et al., 2025]. AI-usage now exposes companies to a range of risks from product
liability & negligence, wrongful death, defamation, and publicity and privacy, to name but a few.

                                                 6
For example, in Garcia v. Character.AI & Google, the court has let the case proceed (May 22,
2025) over a teen’s suicide, allegedly encouraged by a chatbot’s messages. Claims include wrongful
death, negligence, and deceptive trade practices.

5.2    10-K Disclosures

To manage growing AI-specific risks, companies are signaling greater disclosure to shareholders,
but only superficially. An analysis by Arize AI, as reported by the Financial Times [Kinder, 2024,
Arize AI, 2024], found that 56% of Fortune 500 companies cited AI as a “risk factor” in their most
recent 2024 annual 10-K reports. Netflix, Motorola, and Salesforce all discuss AI-specific risks –
yet only in superficial boilerplate terms, according to a recent and comprehensive academic study
on 10-K disclosures for AI [Uberti-Bona Marin et al., 2025]. Similarly, SEC staff letters [Mogilevich
et al., 2024] to companies show that much of the guidance was thin on details. Staff consistently
requested more specifics from companies on disclosure details for AI-related topics.

Aware of the AI-disclosures gap, the SEC launched in 2024 AI-specific guidance and enforcement
covering AI washing, conflicts of interest, and systemic risk, along with enforcement actions [Van-
derford, 2023, U.S. Securities and Exchange Commission, 2023b, Gensler, 2024]. The SEC now
even has a newly dedicated Chief AI Officer (CAIO) Valerie A. Szczepanik, who will oversee a
new SEC AI Task Force, though its focus is more on internal innovations [Szczepanik, 2025, U.S.
Securities and Exchange Commission, 2025a].

5.3    8-K Disclosures

To analyze 8-K filings, we constructed our own dataset of all AI-related event-driven filings between
November 1, 2022 until September 18, 2025, covering 1,741 corporate issuers. It highlights at least
three key AI-related corporate disclosure gaps:

The first is that 8-K disclosures almost exclusively concern a company’s commercial ventures (Figure
1 below), covering important agreements (Item 1.01), such as model licensing, cloud/compute
commitments, strategic data deals, and reseller/partnership agreements; but also financial matters
(Item 2.02).

Safety and guardrails, i.e., AI-risks, rarely feature. Overwhelmingly most AI filings at 66% (two-
thirds) are positive in nature. In other words, companies have a tendency to use the 8-K to alert
investors to news that may help their business prospects. More specifically, using GPT 5 nano, we
classified filings containing sufficient text (n=7,440) into three buckets of sentiment and found 4,952
(66.6% of) 8-K filings with “positive” sentiment, 1,367 (18.4%) as “negative”, and 1,121 (15.1%) as
neutral.4
   4
    We were unable to extract text from all disclosure filings so we were left with a smaller sample size (compared
to our full dataset of 7,856).

                                                        7
Figure 1. 8-K filings by public companies in the U.S. on artificial intelligence and generative AI, by Item topic.
(n=7,856)

                                                        8
Most disclosures for AI-related impacts are through Item 8.01: a voluntary catch-all event category
useful for AI updates that are not yet a mandated material trigger but still market-relevant. This
implies that companies are not yet sure where to put such AI-triggered events – or are unsure when
an event is sufficiently material to disclose it elsewhere.

Big firms need a 10-K mandate. Finally, 8-K filings on AI-related matters are driven by smaller
companies since submissions reflect the universe of filing firms. Big Tech’s 8-K disclosures are,
as expected, not very prominent, since they only constitute 0.34% of the companies making 8-K
submissions in our data. AMZN made 14 submissions, followed by NVDA (11), MSFT (10), and
META (12), and GOOGL/GOOG (9 each).

Practically, this means that any new 10-K requirement that covers AI-specific business activities
and risks in detail could significantly enhance market transparency, since these mega-cap firms have
an outsized impact on the AI market (together with OpenAI, Anthropic, and a few others).

6    The rise of private AI companies
For these changes to have their intended effect, the relevant players must be public companies.
OpenAI and Anthropic – and other central companies to the emerging AI stack (such as Stripe,
xAI, Databricks, Perplexity) – are private, so they sit outside the SEC’s public-company disclosure
regime, despite being multibillion-dollar enterprises. Although private companies remain subject
to SEC anti-fraud rules and investor protections, they are exempt from ongoing disclosure require-
ments.

Previously, companies like Google and Facebook were compelled to go public as they became larger
with more shareholders [Schmidt, 2010, Gustin, 2011]. But the 2012 JOBS Act raised the threshold
for mandatory registration fourfold and loosened restrictions on private fundraising [U.S. Securities
and Exchange Commission, 2016, Seward & Kissel LLP, 2012]. Capital raised through special
purpose vehicles (SPVs) now count as a single shareholder and the threshold of total shareholders
required in order to force public registration was raised from 500 shareholders of record to 2,000
shareholders of record – or 500 non-accredited investors (whichever comes first). Employees who
received stock compensation are excluded from the count entirely. Moreover, most venture investors
and many employees are accredited investors (high income or net worth), and so do not count toward
the 500 limit.

The 2012 JOBS Act changes combined with the incredible growth in VC, private equity, and
sovereign wealth funds capital has resulted in an explosion of late-stage private capital raising that
enables very large companies to stay private and avoid public reporting requirements. The role
of venture private capital in funding private AI companies is unprecedented compared with other
technologies [Hu et al., 2025]. In 2025, OpenAI, Anthropic, and xAI “captured” over $50 billion in
VC funding [Hu et al., 2025]. OpenAI’s capped-profit partnership and Anthropic’s public-benefit

                                                   9
corporation might sound civic-minded, but ultimately insulate them from market-oversight.

This has created a bifurcated market where major technology companies operate at unprecedented
scale through Regulation D offerings and special purpose vehicles while remaining exempt from
periodic disclosure requirements, raising concerns about transparency and investor protection in
systemically important sectors [Ewens and Farre-Mensa, 2020].

Despite being private – and so outside the realm of public disclosure obligations – OpenAI is caus-
ing major swings in the public stock market [Vlastelica, 2025]. OpenAI’s decision to partner with
Shopify, Etsy, and now Advanced Micro Devices (AMD) has sent their shares soaring. Its partner-
ships with chipmakers AMD and Nvidia involve fairly opaque, “circular”, financing deals [NVIDIA
Newsroom, 2025, Forgash and Ghosh, 2025]. Notes a leading investment strategist in Bloomberg:
“it is certainly an odd situation for a private company to have so much impact. . . [OpenAI] can be
more agile and creative, and that leads to the ripple effect we see in other companies, both good and
bad.” Further complicating matters are the incredible investments made in private AI companies
by major listed companies, such as Amazon in Anthropic and Microsoft in OpenAI [Bishop, 2025,
Barr, 2025]. This increases risks arising from the reverse impacts of these investments on to the
investing company.

7     Policies: What should we be aiming for?
Public oversight should begin with the corporate disclosure machinery we already have. In the
wake of the 1929 crash, Congress created the SEC and required companies to surface material risks
through annual 10-K reports, quarterly 10-Qs and event-driven 8-Ks. That regime remains one of
the few proven, scalable checks on corporate behavior – ‘Truth in securities.’ Or, as Justice Louis
Brandeis put it, “Sunlight is said to be the best of disinfectants; electric light the most efficient
policeman.”

High-quality disclosure can work. Material disclosures convert a company’s private knowledge into
publicly verifiable facts. This powers an entire ecosystem, from auditing and banking to journalism
and securities law, that keep most firms honest.

But the AI market’s center of gravity now sits outside of key existing public standards. Despite their
reach, OpenAI and Anthropic – but also Stripe, Databricks, and other decades-old tech companies
– disclose less than public peers about what matters: their financials and business operations.

If AI is going to be governed as a market technology, it must be brought into the market’s account-
ability machinery. Five policy tweaks would help kickstart this process:

    1. SEC Guidance Note on AI. To get the ball rolling, an SEC guidance note (called “CF Dis-
      closure Guidance”) could help companies understand how existing corporate disclosure rules
      apply to AI-related matters. At its core this should define material AI incidents in plain

                                                   10
  English to include systemic model failures, major outages, widespread customer remediation,
  loss of essential third-party model access, impactful changes to safety guardrails, and so on. It
  should also clarify how AI-driven events fit within existing 8-K categories and how to disclose
  relevant AI-activities within a company’s annual 10-K report.

  A guidance note is not binding law, but it can strongly influence company filings and SEC
  actions. For example, the 2011 Cybersecurity memo (Topic No. 2) told issuers what to discuss
  under Risk Factors, MD&A, Business, and other items in their 10-K report.

  An AI guidance note would provide the same practical roadmap as the 2011 Cyber memo:
  specific, concrete examples showing companies how to disclose AI risks and opportunities
  substantively across business operations (S-K Item 101), risk factors (Item 105), trends and
  uncertainties in MD&A (Item 303), and other key sections – avoiding generic boilerplate

  Part of the guidance might encompass AI-related escalation criteria for potential Form 8-K
  reporting. Companies should maintain disclosure controls that identify AI-related develop-
  ments which, if material, may require a current report on Form 8-K.

  Quantitative indicators (escalation): Statistically significant deviations from historical base-
  lines in KPIs plausibly affected by AI system changes – e.g., engagement (DAU/MAU, time-
  on-platform), monetization (CTR, conversions), and risk metrics (credit approval or denial
  rates, charge-offs, loss ratios, harmful-output and jailbreak rates, fraud-detection efficacy).
  Indicators inform but do not by themselves determine materiality and Item applicability, con-
  sistent with SEC KPI/MD&A guidance [U.S. Securities and Exchange Commission, 2020].

  Qualitative indicators (escalation): Changes to AI objectives, guardrails and policies with
  expected impact on harmful-output rates or regulatory exposure; material data-provenance
  shifts (e.g., addition of sensitive datasets); dependency changes (e.g., migration of core func-
  tionality to third-party models and APIs); or significant compute capacity loss or outage.
  Counsel should assess whether any specific 8-K Item is implicated (e.g., Items 1.05, 1.01,
  2.06, or 8.01).

2. Create a new AI-risk item on the 8-K disclosure Form for material AI-driven events as they
  happen – modeled on Item 1.05, Cybersecurity Incidents (2023). Note that it is not the
  technology (AI) itself that triggers a filing rather than a material, incident-style impact. The
  trigger is not “an AI model changed,” but that “the change or failure had a meaningful effect
  on operations, customers, compliance, or financial results.”

  Companies already use the 8-K Form to alert investors when something important happens
  between annual or quarterly reports. The idea here is to add a dedicated item for AI-related
  material incidents, so that there is a clear place to report them when they matter. This
  can help ensure that companies do not skip reporting the “risks” when disclosing material

                                              11
  AI-related events.

  An “AI incident” is a development arising from the use of AI systems that has a meaningful
  effect on the business. Examples include: a model failure that misprices loans; an AI system
  outage interrupting service; an AI-driven error requiring customer remediation; or a sudden
  loss of access to a third-party model on which a product depends. The trigger is the impact
  itself.

3. Add a standing AI section in the annual 10-K Form that explains how a company manages
  AI. One-off 8-K event reports are, by themselves, insufficient. Investors also need a clear,
  yearly picture of how a company runs its AI-related activities, covering: how it is used in
  products and operations, who oversees it, what the main risks are, and what controls are in
  place. A new 10-K item would provide that exact structure, thereby encouraging companies
  themselves to adopt a longer view of these risks.

  Companies would explain their approach to risk management (how they test and monitor
  systems, how they roll out changes, how they respond when something goes wrong); their
  strategy (where AI fits in the business and why); and their governance (who is accountable
  at the management and board level). They would also describe key dependencies that could
  affect reliability or cost (such as reliance on outside model providers, critical data sources, or
  a single cloud vendor), along with any concentration risks that come with those choices.

  The goal is not to jam in unnecessary detail into the 10-K but to make the business implica-
  tions of AI understandable to the investing public: where the leverage points are, how failure
  is prevented, and what the plan is when problems occur.

  Finally, labeling the main AI elements with standard, machine-readable (iXBRL) tags (the
  same way the SEC does for several other disclosures, such as the SEC’s cyber rule) would let
  analysts and watchdogs compare companies more easily and spot patterns over time.

4. Enforce the rules. In crypto and cyber, improved disclosures followed real prosecutions [Jen-
  nings et al., 2011, Simona, 2025, U.S. Securities and Exchange Commission, 2024b, Valdetero
  and van Wengen, 2025]. The SEC should continue to bring any material cases against AI
  washing, misleading claims, and fraud.

5. Reverse the JOBS Act loopholes that allow companies to raise billions from hundreds of in-
  vestors while remaining private. If you access public savings at scale, you should meet public
  disclosure standards.

  Today’s most consequential AI firms can avoid Exchange Act reporting due to higher Section
  12(g) thresholds and “holders of record” counting rules introduced by the 2012 JOBS Act –
  later implemented by SEC rulemaking. Targeted fixes would close this transparency gap and
  bring widely held private issuers accessing public savings within the same disclosure discipline

                                              12
      [112th. Congress, 2012].

      So-called “Regulation D” exemptions currently permit unlimited private capital raises from
      accredited investors by a company without triggering reporting requirements.

      We propose: treating SPVs as look-through entities so consolidated shareholder counts cannot
      be gamed; narrowing the employee shareholder exemption; and capping Reg D fundraising
      (e.g., $1 billion lifetime or 250 shareholders) before companies must register as reporting
      entities.

7.1   Conclusion: Empower Markets with Information

Unlike capability thresholds, the SEC disclosure approach for public reporting companies anchors
oversight in materiality: what AI does to a firm’s operations, customers, and earnings that an
investor would care about. It rewards evidence – not hype. It is a language investors, courts, and
boards already understand.

No disclosure regime will fix every AI risk. But a materiality-based framework can better align
company incentives, surface urgent hazards, and give democratic institutions leverage over a pro-
foundly commercial technology. If quarterly reporting goes, the quid pro quo should be stronger
event-driven transparency and annual reporting.

                                                13
References
112th. Congress. Jumpstart Our Business Startups Act. https://www.govinfo.gov/content/
  pkg/PLAW-112publ106/pdf/PLAW-112publ106.pdf, 2012. Pub. L. 112-106, 126 Stat. 306.
Stephanie Aliaga.   Is AI Already Driving U.S. Growth?        https://am.jpmorgan.
  com/us/en/asset-management/adv/insights/market-insights/market-updates/
  on-the-minds-of-investors/is-ai-already-driving-us-growth/, 2025.       Accessed:
  2025-11-03.
Sam Altman.       GPT-OSS Announcement on              X.       https://x.com/sama/status/
  1872703565497811137, 2025. Accessed: 2025-11-03.
Arize AI.     The Rise of Generative AI in SEC Filings.          Technical report,
  Arize AI, 2024.         URL https://www.arize.com/wp-content/uploads/2024/07/
  The-Rise-of-Generative-AI-In-SEC-Filings-Arize-AI-Report-2024.pdf.      Accessed:
  2025-11-03.
Paul Atkins. Let the market decide how often companies report. Financial Times, 2025. URL
  https://www.ft.com/content/0f6be08a-fd24-4558-b373-6ada31e18900. Accessed: 2025-
  11-03.
Paul S Atkins and Bradley J Bondi. Evaluating the mission: A critical review of the history and
  evolution of the SEC enforcement program. Fordham J. Corp. & Fin. L., 13:367, 2008.
John Authers. We’ll FOM See How Long the Risks Can Be Ignored. Bloomberg Opinion
  Newsletters, 2025. URL https://www.bloomberg.com/opinion/newsletters/2025-09-17/
  fomc-investors-see-stocks-overvalued-expect-inflation-to-pick-up. Accessed: 2025-
  11-03.
Alistair Barr.    Microsoft Is Close to Getting a Giant New Equity Stake in
  OpenAI.      Business Insider, 2025.     URL https://www.businessinsider.com/
  microsoft-openai-equity-stake-early-bet-openai-2025-9. Accessed: 2025-11-03.
Todd Bishop.      Amazon Deepens Anthropic Ties with Equity Conversion, Adding Bil-
  lions to Q1 Profit.     GeekWire, 2025.      URL https://www.geekwire.com/2025/
  amazon-deepens-anthropic-ties-with-equity-conversion-adding-billions-to-q1-profit/.
  Accessed: 2025-11-03.
Michal R Bloomberg and Task Force on Climate-related Financial Disclosures.   Recom-
 mendations of the Task Force on Climate-related Financial Disclosures. Final report,
 Financial Stability Board, 06 2017. URL https://www.fsb-tcfd.org/publications/
 final-recommendations-report-2017/.
Christine A Botosan. Disclosure level and the cost of equity capital. Accounting review, pages
  323–349, 1997.
Ian Carlos Campbell.         OpenAI’s TikTok of AI slop hit one million downloads
  faster than ChatGPT.         Engadget, 2025.   URL https://www.engadget.com/ai/
  openais-tiktok-of-ai-slop-hit-one-million-downloads-faster-than-chatgpt-181216271.
  html. Accessed: 2025-11-03.
Michael Cembalest. The Blob: Capital, China, Chips, Chicago and Chilliwack. Eye on the Market,

                                              14
  09 2025. URL https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/
  eye-on-the-market/the-blob-amv.pdf.
John C Coffee, jr. Market failure and the economic case for a mandatory disclosure system. Virginia
  Law Review, pages 717–753, 1984.
Milton H Cohen. "Truth in Securities" Revisited. Harvard Law Review, 79(7):1340–1408, 1966.
U.S. Supreme Court. Omnicare, Inc. v. Laborers Dist. Council Constr. Indus. Pension Fund, 575
  U.S. 175 (2015), 2015. Supreme Court of the United States.
Douglas W Diamond and Robert E Verrecchia. Disclosure, liquidity, and the cost of capital. The
 Journal of Finance, 46(4):1325–1359, 1991.
Corrie Driebusch.   The Renewed Bid to End Quarterly Earnings Reports.      The
  Wall Street Journal,   2025.      URL https://www.wsj.com/finance/regulation/
  the-renewed-bid-to-end-quarterly-earnings-reports-ae5d62d8. Accessed: 2025-11-
  03.
Michael L. Ettredge and Vernon J. Richardson. Information Transfer Among Internet Firms: The
 Case of Hacker Attacks. Journal of Information Systems, 17(2):71–82, 2003.
European Parliament.    EU AI Act: First Regulation on Artificial Intelligence. Euro-
  pean Parliament News, 2025. URL https://www.europarl.europa.eu/topics/en/article/
  20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence. Accessed:
  2025-11-03.
Michael Ewens and Joan Farre-Mensa. The Evolution of the Private Equity Market and the Decline
 in IPOs. Review of Financial Studies, 33(8):3719–3755, 2020.
Financial Times. Donald Trump calls for US companies to ditch quarterly reporting. Financial
  Times, 2025. URL https://www.ft.com/content/d5d46365-a2ad-41ee-9c6b-6f382e8d1ce8.
  Accessed: 2025-11-03.
Fisher & Phillips LLP.  AI Litigation Tracker: Comprehensive View of AI-Technology-
  Related   Lawsuits.        https://www.fisherphillips.com/en/innovations-center/
  ai-litigation-tracker.html, 2025. Accessed: 2025-11-03.
Emily    Forgash     and  Agnee    Ghosh.        OpenAI’s    Nvidia,   AMD     Deals
 Boost     $1    Trillion   AI   Boom     With   Circular  Deals.         Bloomberg,
 2025.                  URL     https://www.bloomberg.com/news/features/2025-10-07/
 openai-s-nvidia-amd-deals-boost-1-trillion-ai-boom-with-circular-deals.        Ac-
 cessed: 2025-11-03.
Ina Fried. Meta’s AI Future: Your Friends Are Bots. Axios, 2025. URL https://www.axios.com/
  2025/05/02/meta-zuckerberg-ai-bots-friends-companions. Accessed: 2025-11-03.
Gary Gensler.          Office Hours with Gary Gensler:      Systemic Risk in Arti-
 ficial    Intelligence.           https://www.sec.gov/newsroom/speeches-statements/
 gensler-transcript-systemic-risk-artificial-intelligence-091924, September 2024.
 Accessed: 2025-11-03.
Lawrence A. Gordon, Martin P. Loeb, and Tashfeen Sohail. Market Value of Voluntary Disclosures
  Concerning Information Security. MIS Quarterly, 34(3):567–594, 2010.

                                                15
Sam Gustin. Facebook Faces IPO or SEC Disclosure in 2012. Wired, 2011. URL https://www.
  wired.com/2011/01/facebook-2012/. Accessed: 2025-11-03.
Gillian K. Hadfield and Jack Clark. Regulatory Markets: The Future of AI Governance. arXiv
  preprint, arXiv:2304.04914, 2023. URL https://arxiv.org/abs/2304.04914. Accessed: 2025-
  11-03.
Paul M Healy and Krishna G Palepu. Information asymmetry, corporate disclosure, and the capital
  markets: A review of the empirical disclosure literature. Journal of Accounting and Economics,
  31(1-3):405–440, 2001.
Susan Hu, Taylor Criswall, Miles Ostroff, and Kyle Stanford. Q3 2025 Quantitative Per-
  spectives: A Fork in the Road.      Technical report, PitchBook, 2025. URL https:
  //files.pitchbook.com/website/files/pdf/Q3_2025_Quantitative_Perspectives_A_
  Fork_in_the_Road_20179.pdf. Accessed: 2025-11-03.
IFRS. IFRS S1 General Requirements for Disclosure of Sustainability-related Financial Informa-
  tion. International Sustainability Standards Board Standards, 2023. Investor-focused baseline:
  governance, strategy, risk, metrics/targets.
IFRS Foundation.        Introduction to the ISSB and IFRS Sustainability Dis-
  closure    Standards.           https://www.ifrs.org/sustainability/knowledge-hub/
  introduction-to-issb-and-ifrs-sustainability-disclosure-standards/, 2025.      Ac-
  cessed: 2025-11-03.
Greg Ip.    Behind Job Weakness Are Hints of a Productivity Revival. Is AI the Rea-
  son?        The Wall Street Journal, 2025.   URL https://www.wsj.com/tech/ai/
  behind-job-weakness-are-hints-of-a-productivity-revival-is-ai-the-reason-cf6309da.
  Accessed: 2025-11-03.
Jared Jennings, Simi Kedia, and Shivaram Rajgopal. The deterrent effects of SEC enforcement and
  class action litigation. Available at SSRN 1868578, 2011.
Davinder Kaur, Suleyman Uslu, Kaley J Rittichier, and Arjan Durresi. Trustworthy artificial
  intelligence: a review. ACM computing surveys (CSUR), 55(2):1–38, 2022.
Paul Kedrosky.   Honey, AI Capex Ate the Economy.           https://paulkedrosky.com/
  honey-ai-capex-ate-the-economy/, 2025. Accessed: 2025-11-03.
Tabby Kinder. Biggest US companies warn of growing AI risk. Financial Times, August 2024. URL
  https://www.ft.com/content/5ee96d38-f55b-4e8a-b5c1-e58ce3d4111f. Accessed: 2025-
  11-03.
Richard Lambert, Christian Leuz, and Robert E Verrecchia. Accounting information, disclosure,
  and the cost of capital. Journal of Accounting Research, 45(2):385–420, 2007.
Katia Sophia Leiva, Allison Kernisky, and Jessica B. Magee.         SEC and DOJ
 Warm Up to Enforcement over AI Washing.        Holland & Knight SECond Opin-
 ions Blog, 2025.   URL https://www.hklaw.com/en/insights/publications/2025/07/
 sec-and-doj-warm-up-to-enforcement-over-ai-washing. Accessed: 2025-11-03.
Christian Leuz and Peter D Wysocki. The economics of disclosure and financial reporting regulation:
  Evidence and suggestions for future research. Journal of Accounting Research, 54(2):525–622,
  2016.

                                                16
Paul G Mahoney. Mandatory disclosure as a solution to agency problems. The University of
  Chicago Law Review, 62(3):1047–1112, 1995.
Matrixx Initiatives, Inc. v. Siracusano. 563 U.S. 27, 2011. Supreme Court of the United States.
Mariana Mazzucato, Ilan Strauss, Tim O’Reilly, and Josh Ryan-Collins. Regulating Big Tech: The
 Role of Enhanced Disclosures. Oxford Review of Economic Policy, 39(1):47–69, 2023. doi: 10.
 1093/oxrep/grac040. URL https://academic.oup.com/oxrep/article-abstract/39/1/47/
 7030605. Accessed: 2025-11-03.
Virginia F. Milstead, Mark R.S. Foster, and Paige Gillard. Investors Increasingly Claim
  That AI Hype Is Securities Fraud. Skadden, Arps, Slate, Meagher & Flom LLP Insights,
  2025. URL https://www.skadden.com/-/media/files/publications/2025/08/investors_
  increasingly_claim_that_ai_hype_is_securities_fraud.pdf. Accessed: 2025-11-03.
Marsha Mogilevich, Albert Vanderlaan, J.T. Ho, and Hong Tran. SEC Comment Letter Trend:
 AI-Related Disclosures. Orrick Insights, 2024. URL https://www.orrick.com/en/Insights/
 2024/12/SEC-Comment-Letter-Trend-AI-Related-Disclosures. Accessed: 2025-11-03.
Arvind Narayanan and Sayash Kapoor. Ai as normal technology: An alternative to the vision of
  ai as a potential superintelligence. Knight First Amendment Institute, 04 2025. URL https:
  //knightcolumbia.org/content/ai-as-normal-technology.
NVIDIA Newsroom.       OpenAI and NVIDIA Announce Strategic Partnership to De-
 ploy 10 Gigawatts of NVIDIA Systems.              https://nvidianews.nvidia.com/news/
 openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems,
 September 2025. Letter of intent; NVIDIA intends to invest up to US$100 billion in OpenAI;
 Accessed: 2025-11-03.
Tim O’Reilly and Ilan Strauss. The hot blood leaps over the cold decree. Asimov’s Addendum, 2025.
  URL      https://asimovaddendum.substack.com/p/the-hot-blood-leaps-over-the-cold.
  Accessed: 2025-11-03.
Tim O’Reilly, Ilan Strauss, and Mariana Mazzucato. Regulating Big Tech through Digital Disclo-
  sures. UCL Institute for Innovation and Public Purpose, 2023.
Eric Schmidt.    How I Did It:     Google’s CEO on the Enduring Lessons of a
  Quirky IPO. Harvard Business Review, May 2010.    URL https://hbr.org/2010/05/
  how-i-did-it-googles-ceo-on-the-enduring-lessons-of-a-quirky-ipo. Accessed: 2025-
  11-03.
Seward & Kissel LLP.           “JOBS”’ Act Passed to Remove Prohibition of Gen-
  eral  Solicitation   and   Marketing   in Regulation D    Offerings and   Increase
  500    Record      Owner    Threshold.       https://www.sewkis.com/publications/
  jobs-act-passed-to-remove-prohibition-of-general-solicitation-and-marketing-in-regulation-d-
  March 2012. Accessed: 2025-11-03.
Mola.  Simona.          SEC     Cryptocurrency   Enforcement:         2024 Update,
 2025.           URL      https://www.cornerstone.com/wp-content/uploads/2025/01/
 SEC-Cryptocurrency-Enforcement-2024-Update.pdf. Accessed: 2025-11-03.
Valerie A. Szczepanik. Valerie A. Szczepanik – Chief AI Officer. https://www.sec.gov/about/
  division-office-directors/valerie-szczepanik, 2025. Accessed: 2025-11-03.

                                               17
Huileng Tan. AI’s Economic Boost Isn’t Showing Up in GDP, and Goldman Sachs Says That’s
 a $115 Billion Blind Spot. Business Insider, 2025. URL https://www.businessinsider.
 com/ai-tech-economy-us-gdp-boost-chips-blindspot-goldman-sachs-2025-9. Accessed:
 2025-11-03.
The Economist.    AI labs’ all-or-nothing race leaves no time to fuss about safety.
  The Economist, 2025.       URL https://www.economist.com/briefing/2025/07/24/
  ai-labs-all-or-nothing-race-leaves-no-time-to-fuss-about-safety.        Accessed:
  2025-11-03.
Lucas G. Uberti-Bona Marin, Bram Rijsbosch, Gerasimos Spanakis, and Konrad Kollnig. Are
  Companies Taking AI Risks Seriously? A Systematic Analysis of Companies’ AI Risk Disclosures
  in SEC 10-K Forms. arXiv preprint, arXiv:2508.19313, 2025. doi: 10.48550/arXiv.2508.19313.
  URL https://arxiv.org/pdf/2508.19313. Accessed: 2025-11-03.
U.S. Securities and Exchange Commission. Staff Accounting Bulletin No. 99: Materiality. SEC
  Staff Accounting Bulletin, 1999.
U.S. Securities and Exchange Commission. Changes to Exchange Act Registration Requirements
  to Implement Title V and Title VI of the JOBS Act. https://www.sec.gov/files/rules/
  final/2016/33-10075.pdf, May 2016. Release No. 33-10075; 34-77757; File No. S7-12-14; 81
  FR 28689; Accessed: 2025-11-03.
U.S. Securities and Exchange Commission. Commission statement and guidance on public company
  cybersecurity disclosures. Commission Statement and Guidance, 2018.
U.S. Securities and Exchange Commission. Modernization of regulation s-k items 101, 103, and
  105. Final Rule, 2019. Release No. 33-10668; 84 FR 44358.
U.S. Securities and Exchange Commission. Commission Guidance on Management’s Discussion
  and Analysis of Financial Condition and Results of Operations. https://www.sec.gov/files/
  rules/interp/2020/33-10751.pdf, February 2020. Release No. 33-10751; 34-88094; Accessed:
  2025-11-03.
U.S. Securities and Exchange Commission. Cybersecurity risk management, strategy, governance,
  and incident disclosure. Final Rule, 2023a. Creates Form 8-K Item 1.05 and Reg S-K Item 106.
U.S. Securities and Exchange Commission. Conflicts of Interest Associated with the Use of Predic-
  tive Data Analytics by Broker-Dealers and Investment Advisers. https://www.sec.gov/files/
  rules/proposed/2023/34-97990.pdf, July 2023b. Release Nos. 34-97990; IA-6353; File No.
  S7-12-23; Accessed: 2025-11-03.
U.S. Securities and Exchange Commission. The Enhancement and Standardization of Climate-
  Related Disclosures for Investors. Final Rule, 2024a. Adopted 2024; aspects stayed pending
  litigation.
U.S. Securities and Exchange Commission. SEC Charges Four Companies With Misleading Cy-
  ber Disclosures. https://www.sec.gov/newsroom/press-releases/2024-174, October 2024b.
  Press Release No. 2024-174; Accessed: 2025-11-03.
U.S.   Securities    and    Exchange      Commission.       SEC     Creates    Task     Force
  to    Tap     Artificial   Intelligence   for   Enhanced   Innovation     and    Efficiency
  Across     the       Agency.              https://www.sec.gov/newsroom/press-releases/

                                               18
  2025-103-sec-creates-task-force-tap-artificial-intelligence-enhanced-innovation-efficiency-a
  August 2025a. Press Release No. 2025-103; Accessed: 2025-11-03.
U.S. Securities and Exchange Commission. Disclosure guidance.  https://www.sec.gov/
  rules-regulations/staff-guidance/disclosure-guidance, 2025b. Accessed: 2025-11-03.
U.S. Securities and Exchange Commission, Division of Corporation Finance. Cf disclosure guidance:
  Topic no. 2 — cybersecurity. Guidance, 2011.
U.S. Supreme Court. TSC Industries, Inc. v. Northway, Inc., 1976. URL https://supreme.
  justia.com/cases/federal/us/426/438/. Decided June 14 1976; Accessed: 2025-11-03.
U.S. Supreme Court. Basic Inc. v. Levinson, 485 U.S. 224, 1988. Supreme Court of the United
  States.
Jena M. Valdetero and Wouter van Wengen.             SEC Cybersecurity Disclosure
  Trends:     2025 Update on Corporate Reporting Practices.       Greenberg Trau-
  rig, LLP Insights,    2025.     URL https://www.gtlaw.com/en/insights/2025/2/
  sec-cybersecurity-disclosure-trends-2025-update-on-corporate-reporting-practices.
  Accessed: 2025-11-03.
Richard Vanderford. SEC Head Warns Against “AI Washing,” the High-Tech Version of
  “Greenwashing”’. The Wall Street Journal, 2023. URL https://www.wsj.com/articles/
  sec-head-warns-against-ai-washing-the-high-tech-version-of-greenwashing-6ff60da9.
  Accessed: 2025-11-03.
Robert E Verrecchia. Essays on disclosure. Journal of Accounting and Economics, 32(1-3):97–180,
  2001.
Ryan Vlastelica. OpenAI Is Fast Becoming a Whale in Stock Market It Has Shunned.
  Bloomberg News, 2025. URL https://www.bloomberg.com/news/articles/2025-10-06/
  openai-is-fast-becoming-a-whale-in-stock-market-it-has-shunned. Accessed: 2025-11-
  03.
Melanie E. Walker, Richard Zelichov, and Emma Peplow.            AI-Related Securities
 Class Action Filings Are on the Rise:       Key Observations.   DLA Piper Insights,
 2025.        URL      https://www.dlapiper.com/en-us/insights/publications/2025/09/
 ai-related-securities-class-action-filings-are-on-the-rise-key-observations.
 Accessed: 2025-11-03.
Avery Williams and Peter Csathy. AI Litigation Tracker: Regular Updates on Generative AI
  Copyright-Infringement Litigation. https://www.mckoolsmith.com/newsroom-ailitigation,
  2025. Accessed: 2025-11-03.

                                               19
  Social Science Research Council 
300 Cadman Plaza West, 15th Floor 
            Brooklyn, NY 11201, USA
