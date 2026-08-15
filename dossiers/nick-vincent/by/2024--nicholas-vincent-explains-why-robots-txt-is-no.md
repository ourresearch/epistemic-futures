---
title: "Nicholas Vincent explains why robots.txt is no longer enough to protect against web scraping"
person: "nick-vincent"
section: "by"
type: "interview"
year: 2024
date: "2024-03-21"
venue: "IT Brew"
authors: "Interviewed by Tom McKay"
source_url: "https://www.itbrew.com/stories/2024/03/21/prof-nicholas-vincent-explains-why-robots-txt-is-no-longer-enough-to-protect-against-web-scraping"
retrieved: "2026-08-13"
content: "full-text"
notes: "Q&A interview, edited for length and clarity by IT Brew. Filed in by/ per the 'voice is the payload' rule."
---

# Nicholas Vincent explains why robots.txt is no longer enough to protect against web scraping

## Full text

The only thing between a website and an internet scraper’s database is a tiny file called robots.txt, a small configuration file that tells web crawlers for services ranging from Google to OpenAI which parts of a site they can and can’t access.

This first and last line of defense lacks nuance—bots on the list are either permitted by default or totally blocked—and is purely voluntary, as the exclusions lack legal force, making it a lightning rod of contention in an era where generative AI services are gobbling up all the data they can for training sets. While some bots, like OpenAI’s GPTBot, respect robots.txt exclusions, others don’t.

Nicholas Vincent, an assistant professor of computing science at Simon Fraser University, talked with IT Brew about why organizations should be concerned about their data being scraped—and how something better than robots.txt is needed.

This interview has been edited for length and clarity.

Why is robots.txt insufficient protection against data harvesting?

The current status quo is an interesting mix of actual clear legal definitions, but also just loosely agreed upon norms.

There’s a really deep tension, which is that if I’m running a blog, or a content website, or even a large journalism website, I might be really concerned that these AI companies are going to financially benefit from all of the education and skills and knowledge that my employees have and make available via their writing. I don’t want that to happen. But at the same time, I don’t want these models to not know that my site exists, or for the subset of models that do try to do some degree of linking or attribution. I want readers to be sent to my site.

The current, really sort of un-nuanced paradigm, just a simple yes or no decision—whether that’s legally enforced or just a new sort of addition or alternative to robots.txt—really fails to capture that nuanced set of incentives, and the nuanced kind of decisions that I might want to make.

###### Top insights for IT pros

From cybersecurity and big data to cloud computing, IT Brew covers the latest trends shaping business tech in our 4x weekly newsletter, virtual events with industry experts, and digital guides.

Subscribe

By subscribing, you accept our Terms & Privacy Policy.

Why should organizations be concerned about their public data being scraped for AI models?

If you are being scraped willy-nilly with no protections whatsoever, there’s a very serious concern that your employees are basically automating themselves out of a job. Whether it’s journalistic content, or poems, or code in a particular language, with no sort of governance over this at all or no room to put your foot down and bargain.

Are there other reasons why companies should be thinking about how to protect against scraping?

I think that for a lot of organizations, thinking about large language models as search engines that are really hesitant to actually link send users to your website is a pretty useful point of comparison.

Google introduced the answer box widget into their search engine results pages. And so you’d ask the question, some president, what year were they born? And instead of giving you 10 blue links to different websites with the biography of that president—which is what would happen in 2005—instead there would be a box at the top that’ll just answer your question and you don’t have to click any links. The idea is you never have to leave Google…Think about large language models as that on steroids.

A lot of companies are also just going to put up more extravagant paywalls and anti-scraping measures. Reddit has struck a deal with Google to basically license their data for AI training. But that means in order to actually have leverage to make that deal, they had to make it really harder for everybody else to get the data.

Copy

#### Top insights for IT pros

From cybersecurity and big data to cloud computing, IT Brew covers the latest trends shaping business tech in our 4x weekly newsletter, virtual events with industry experts, and digital guides.

Subscribe

By subscribing, you accept our Terms & Privacy Policy.
