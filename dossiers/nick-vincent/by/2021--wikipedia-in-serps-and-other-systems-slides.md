---
title: "The Importance of Wikipedia to Search Engines (and other systems) — Wikimedia Research Showcase slides"
person: "nick-vincent"
section: "by"
type: "talk-transcript"
year: 2021
date: "2021-01-01"
venue: "Wikimedia Foundation Research Showcase, May 2021 (Figshare deposit)"
authors: "Nicholas Vincent"
source_url: "https://figshare.com/articles/presentation/WMF_Showcase_Wikipedia_in_SERPs_Other_Systems_pdf/14636994"
retrieved: "2026-08-13"
content: "full-text"
notes: "OpenAlex W3208601292. Text extracted from the deposited slide deck — this is slide text, not a spoken transcript. Corresponds to the May 2021 Wikipedia Research Showcase talk listed on his CV; video of the talk is noted in video.md."
---

# The Importance of Wikipedia to Search Engines (and other systems) — Wikimedia Research Showcase slides

## Slide text (full deck)

The Importance of Wikipedia to Search Engines (and
other systems)
https://www.mediawiki.org/wiki/Wikimedia_Research/Showcase

Nicholas Vincent. Discussing work done with my PhD adviser, Brent
Hecht.
Contact: www.nickmvincent.com | nickvincent@u.northwestern.edu | @nickmvincent


Structure of this short talk
1. Describe a specific study about SERPs and Wikipedia (will be
presenting at CSCW 2021)
a. If you were at WikiWorkshop 2020, this may sound familiar!
b. I’ll go a bit fast on methods, but I’d love to chat more after if
this sounds interesting!
2. Connect these phenomena to the (many) other examples of
Wikipedia fueling AI / ML / data science


Algorithms &
Platforms

“Data Labor”
Intelligent
Technologies


Why Study Data Labor?
● Economic concerns
○ Intelligent technologies linked with serious
societal harms from inequality
● Recognize and dignify data labor
● Sustainability of peer production
Make people aware of value, to make it possible for
them to leverage the value and create change
4


Why Study Data Labor?

Leverage value of data labor to create a computing paradigm
where economic benefits and power are shared much more
broadly
Could range from: paycheck for your data to more
recognition/agency for Wikipedia (and similar
communities)


So how exactly do Wikipedia and search engines fit into
“data labor” research?


Search engines
●
●

ubiquitous
hugely influential

Image from: Purcell, Kristen, Lee Rainie, and Joanna
Brenner. "Search engine use 2012." (2012).


26% click
through
rate

14% click
through
rate


Wikipedia was a top source of content and appeared in
80-90% of results pages for some categories.
● not true for every category
● not always in the top 3 results


takeaway: Wikipedia is one of the most important
sources of results for search engines


We had several generalization questions:
● What about search engines other than Google?
● What about mobile results?
Technical challenge:
● How do we handle the ever-changing Search Engine
Results Pages (“SERPs”) for multiple search engines?
○ SERPs are no longer just “10 blue links”


SERPs are not just 10 blue links

Knowledge Box, News Carousel, Twitter Carousel, etc.
Presumably very important to search


Methods

13


Search Engines, Devices, and Queries
a.
b.

c.

What search engines?
i. Google, Bing, and DuckDuckGo
What devices to emulate?
i. Desktop and Mobile (we also considered the effect of different
screen sizes)
What queries to make?
i. Critical and challenging
ii. Our approach: multiple important categories, drawing on past work


Query selection
“common” queries (100 from search engine optimization company ahrefs.com)
e.g. “facebook”, “youtube”, “amazon”, “gmail”
“trending” queries (282 from Google trends)
e.g. “World Cup”, “thank u, next”, “What is fortnite”
“medical” queries (50 from prior research that shared Bing data)
e.g. “how to lose weight”, “indigestion”
See:
●
●
●

Top Google searches (as of October 2019): 2019. https://ahrefs.com/blog/top-google-searches.
https://trends.google.com/trends/?geo=US
Soldaini, L. et al. 2016. Enhancing web search in the medical domain via query clarification. Information Retrieval Journal. 19, 1–2 (2016),
149–173.


Data collection
Our approach: use `puppeteer` (Node.js) to run headless Chrome
●
●

We forked NikolaiT’s amazing `se-scraper` library:
https://github.com/NikolaiT/se-scraper
Our fork focuses on recording and analyzing link coordinates with the space
of a single SERP


One approach for SERP scraping:
Researcher looks at SERP HTML

<div> … </div>
<div class=”searchResult_abc123”>
<a href=”wikiworkshop.org”> Wiki
Workshop 2020</a>
</div>
<div> … </div>

Write CSS rules to parse HTML page
into a ranked list
“find all elements with class of
searchResults_abc123”

1.
2.

wikiworkshop.org
twitter.com/wikiworkshop


How should
we turn this
into a
ranked list?


Spatial analysis: getting link coordinates
Get all the links (“a” elements) in a page:
await this.page.$$eval('a', getPos);

Calculate their position (x, y) with JavaScript:


A quick note if you want to collect SERP data
TODAY
●

I later created a “minimal” script for collecting link coordinates:
https://github.com/nickmvincent/LinkCoordMin
○
○

Caveat 1: I’ve recently run into some issues with Bing
Caveat 2: Localization (Location spoofing) is inconsistent and requires quite a bit of fiddling

Please reach out if you’re interested!
If you want to study Google using a ranked list approach, I suggest
https://github.com/gitronald/WebSearcher.
○

●

○

Great localization support (better than anything I’ve seen for puppeteer)


Spatial incidence rate definition
full page

above-the-fold

left-hand and right-hand


Incidence rates
●

how often is Wikipedia showing up
in SERPs?
○

●

If we collect 3 SERPs, and Wikipedia
appears in 2, incidence rate = 2 / 3

how often is Wikipedia showing up
in prominent parts of SERPs?
○

if Wikipedia appear “above-the-fold” in
only one of our 3 SERPs,
above-the-fold incidence rate = 1 / 3


Data validation - a tough task
SERP data changes constantly - remember this?


Data validation - visual inspection
Basic approach:
●
●
●

save screenshots of SERPs
visualize the analysis-ready data (i.e. the JSON files
for quantitative analysis)
make sure they seem to match up!


Results

26


Full page incidence rates

Very large incidence rates, but not for medical queries.


Above-the-fold incidence rates

Above-the-fold rate is much higher on desktop than mobile!


Left-hand and right-hand

Large right-hand incidence rates means Knowledge-panel
style elements are still using a lot of Wikipedia links


Summary of findings
●

●

Using the easy-to-understand (but limited) measure of incidence rates,
Wikipedia’s importance to the success of search engines extends
beyond Google and desktop-formatted search results
Queries and devices matter:
○
○

Wikipedia appears above the fold more often on desktop devices than mobile devices
Knowledge panel elements are a key source of Wikipedia content, but not the only sources


Limitations
●

Audit study!
○

●

Still US / en.wikipedia only
○

●

Small scale relative to actual query datasets
Wikipedia has geographic / language differences

Queries matter immensely.
○
○

Incidence rate can lose meaning very quickly, e.g. if we append “wikipedia”
to each query
Interpret accordingly


Wikipedia Matters Outside Wikipedia
Positive: effective peer production = effective
search results?
Negative biases in coverage / quality = impact
on search results?
(is it Wikipedia’s “fault” if Google SERPs are bad? no, but...)

This raises the stakes of Wikipedia-focused
research and Wikipedia findings


Data from the Public Fuels Intelligent
Technologies
● Are Wikipedia editors some of the most
important employees of search engines?
You cannot pay people to edit Wikipedia.
● What to do about this? It’s complicated
(as this
group iscredit
especially
aware)Credit individual
More
prominently
Wikipedia?
contributors? Solicit contributions? Donate to Wikipedia?


Two ways Wikipedia is used
The incidence rate results I presented mainly talk about
how Wikipedia results are “served” by computing systems.

But this is just the tip of the iceberg, because Wikipedia
also “trains” systems. Prominently, language models
(“teaching a machine how to write”).


Wikipedia as a Meal
vs.

"Steak Bowl" by Thai Yin is licensed under
CC BY-NC-ND 2.0

Wikipedia as a Recipe
(Obtained Via
Surveillance of an
Open Kitchen)
"Chefs in the open kitchen - Cumulus Inc" by
avlxyz is licensed under CC BY-SA 2.0


“Of all the understood
responses, Wikipedia is the
most prevalent individual
information source, providing
18.6% of the responses. It is
plausible to conclude that
the reliability of these
responses is only as reliable
as Wikipedia”
https://doi.org/10.1145/3449157


https://www.wired.com/story/youtub
e-will-link-directly-to-wikipedia-to-fig
ht-conspiracies/


Wikipedia articles as a meal (“served” by an
AI or sociotechnical system)
Many systems! Any task that benefits from high quality
knowledge about many topics stands to
●
●
●
●

Search engines
Voice Assistants
YouTube
Other social platforms (Reddit, StackExchange, more?)


Know some more?
Considering sharing them, here:

https://github.com/nickmvincent/UGCValue
Roundup/blob/main/wikipedia.md


https://arxiv.org/abs/2005.14165

https://arxiv.org/pdf/1704.00051.pdf


GPT-3 from OpenAI: >900
Question Answering from Facebook: >900
BERT from Google: >19,000
ImageNet 2015: >23000


Open Question
I think one can make a strong argument that Wikipedia is one of the
most important resource for open machine learning research?
Has this been acknowledged
● not enough
● too much
● just the right amount?
On the horizon: https://meta.wikimedia.org/wiki/Wikimedia_Enterprise


Fun blog post idea
If “Wikipedia” were treated as a collective “scientific author” entity,
where might it rank? How does the funding tech companies give to
Wikipedia compare to the funding they give to “superstar” academics
and technologists?


Many thanks to:
co-author Brent Hecht, thoughtful reviewers and colleagues
Open Software
● se-scraper / puppeteer
● numpy / pandas / seaborn / scipy ecosystem


Questions?
@nickmvincent on Twitter or nickvincent@u.northwestern.edu

Links:
paper: https://www.nickmvincent.com
se-scraper: https://github.com/NikolaiT/se-scraper
our se-scraper fork: https://github.com/nickmvincent/se-scraper
updated scraping repo: https://github.com/nickmvincent/LinkCoordMin
UGC Value Roundup:
https://github.com/nickmvincent/UGCValueRoundup/blob/main/wikipedia.md
