---
title: "Data and the secret scramble for AI’s soul"
person: kenneth-cukier
section: by
type: blog-post
year: 2017
date: 2017-05-14
venue: "The Self-Driving Company (Medium)"
authors: "Kenneth Cukier"
source_url: https://medium.com/self-driving-company/data-and-the-secret-scramble-for-ais-soul-69afaf7c913f
retrieved: 2026-08-13
content: full-text
notes: "His own Medium publication 'the self-driving company'. Full text taken from the publication's RSS feed (content:encoded), which medium.com serves without the Cloudflare block that 403s the HTML pages; images/figures stripped, inline links preserved."
---

# Data and the secret scramble for AI’s soul

## Full text

##### The key resource of the AI era is labeled training data; a quiet rivalry is on to get it

A SILICON VALLEY saying from 2007 went: “If you’re not paying, then you’re the product.” It described the business model of the free web services like Google, Facebook, and others. A decade on, it can be updated: “You’re the training data.”

Data is the lifeblood of AI. The big web platforms rely on user interactions — and the “data exhaust” this generates — to improve their services in a continuous feedback loop.

**The “data economy” is upon us.**

In a recent piece in MIT Sloan Management Review ([here](http://sloanreview.mit.edu/article/whats-your-data-worth/)), James E. Short and Steve Todd raise two emblematic cases:

- In the 2016 bankruptcy of Caesars Entertainment, a gambling firm, some creditors put the worth of its loyalty-program data at $1 billion, its most valuable asset. A bankruptcy court examiner noted that sold-off Caesars properties without access to the data experienced a decline in revenue.
- In 2016 Microsoft acquired LinkedIn for $26 billion. It had 100 million active users per month (of 433 million total registered users), meaning Microsoft paid $260 per monthly active user.

**Yet that’s just data for the sake of classic analysis. What is new is the degree to which companies are vying to assemble training data, ie:**

- Google’s [Open Images Dataset](https://research.googleblog.com/2016/09/introducing-open-images-dataset.html) has 9 million images.
- Google’s [YouTube-8M Dataset](https://research.google.com/youtube8m/) has 8 million labeled videos.
- [ImageNet](http://www.image-net.org/), among the earliest open AI training-databases, has 14 million categorized images (compiled over two years by nearly 50,000 people).
- In 1961 the [Brown Corpus](https://en.wikipedia.org/wiki/Brown_Corpus) was the standard dataset for English words, at 1 million. In 2006 Google released an [n-gram file](https://research.googleblog.com/2006/08/all-our-n-gram-are-belong-to-you.html) of 1 trillion words.
- A Google DeepMind and Oxford University program in 2016 to train a lip-reading system contained 17,428 unique words, while a different Oxford project called LipNet had just 51 words. (It points to what I refer to as “AI’s ‘Data Gap’” [here](https://medium.com/self-driving-company/ais-data-gap-5e58562c604b)).
- In May 2017 Mapillary had 130 million images in its [Vistas Dataset](http://blog.mapillary.com/product/2017/05/03/mapillary-vistas-dataset.html) for self-driving car algorithms, under diverse conditions.
- In December 2016 Tesla [said](https://www.bloomberg.com/news/articles/2016-12-20/the-tesla-advantage-1-3-billion-miles-of-data) it had 1.3 billion miles of data from its cars in different road and weather worldwide. It also wants to share the data ([here](https://electrek.co/2017/05/06/tesla-data-sharing-policy-collecting-video-self-driving/)).
- [SpaceNet](https://aws.amazon.com/public-datasets/spacenet/) has 1,900 square kilometers of high-resolution satellite imagery (hey… It’s a start!) under a Creative Commons license.

A list of public datasets for training machine-learning models is at “[AI2](http://allenai.org/data.html),” the Allen Institute for Artificial Intelligence, and “[Fueling the Gold Rush](https://medium.com/startup-grind/fueling-the-ai-gold-rush-7ae438505bc2): The Greatest Public Datasets for AI,” by Luke de Oliveira in February 2017.

The point is not what the datasets are, but that they exist at all. It shows the degree to which the AI community recognizes that the valuable, scarce resource that will determine if there is a vibrant competition or market dominance in AI is the accessibility of the data to train the models.

**In fact, a lens with which to look at many of the recent deals has been about the scramble to secure access to data.**

Hence, IBM bought the Weather Channel’s digital-and-data assets in 2015 for $2 billion. It can produce hyperlocal weather forecast at a resolution as small as 0.2-mile, with the help of 195,000 personal weather stations (read [more](http://www.marketwatch.com/story/ibm-finally-reveals-why-it-bought-the-weather-company-2016-06-15)).

Yet IBM’s medical-data acquisitions are most notable. In 2015, it bought Explorys, a healthcare-tech company spun out of the prestigious Cleveland Clinic, for its 315 billion data points on financial, operational and medical records across on more than 50 million people (read [more](https://www-03.ibm.com/press/us/en/pressrelease/46585.wss)). Again that year, IBM bought Merge healthcare for $1 billion, to access its database of medical imagery (CT scans, MRIs, x-rays, etc) that by April 2017 exceeded 1 billion images (read [more](http://www.merge.com/Blogs/Enterprise-Imaging-Blog/April-2017/One-Billion-Images-in-the-Cloud-A-Merge-Milestone.aspx)). It acquired Phytel for 45 million patient records (read [more](https://www-03.ibm.com/press/us/en/pressrelease/46767.wss)). And in 2016 it bought Truven Health Analytics for $2.6 billion, adding 215 million patients to its data trove.

On the other side of the data equation, GE’s acquisitions have been to get AI expertise — such as Meridium, Wise.io and Bit Stew (read [more](https://www.bloomberg.com/news/articles/2016-09-14/ge-continues-shopping-spree-with-495-million-software-purchase) and [more](https://www.wsj.com/articles/general-electric-to-buy-two-tech-startups-for-its-digital-business-1479222001)) — since it already has access to the data itself, via its own industrial operations or its manufacturing partners. Likewise, Salesforce has made zillions of relatively small-sized acquisitions for AI capability (ie, Krux, PredictionIO, Implisit, BeyondCore) but not for data; its customers bring their data to the platform. But clearly Salesforce wants to get data: it bid for LinkedIn. And it’s probably eyeing InsideSales.com, a unicorn sitting on a massive treasure-chest of sales data, in which Salesforce’s CEO Marc Benioff is an investor.

**To be sure, the idea of the scramble to acquire data or value it has been around for a while.**

In an op-ed I co-wrote with [Viktor Mayer-Schönberger](https://www.oii.ox.ac.uk/people/viktor-ms/) in the Wall Street Journal a few years ago ([here](https://www.wsj.com/articles/SB10001424127887324178904578343120139164986)), we noted that:

“The value [of data] isn’t well understood. One reason is accounting rules, which have trouble handling intangibles. Ephemeral things such as brands are usually counted as an asset when one is purchased, since there has been a market transaction to give it a monetary worth. They cannot easily be recorded on the books when a company develops them internally. This is usually the case with data, too.”

And we also talked about how companies tried to place a value on data in our 2013 book “[Big Data](https://www.amazon.com/Big-Data-Revolution-Transform-Think/dp/0544227751)” (excerpt above).

Data is now one of the most important parts of a firm’s competitive advantage. The idea has given rise to “reciprocal data applications”. In the words of Drew Breunig, who appears to have coined the term ([here](https://medium.freecodecamp.com/the-business-implications-of-machine-learning-11480b99184d)): they are an exchange “designed to spur the creation of training data as well as deliver the products powered by the data captured. People get better apps and companies get better data.”

**A cover story in *The Economist* in May by my colleague Ludwig Siegele looked at the difficulty in creating a market for data (**[**here**](http://www.economist.com/news/briefing/21721634-how-it-shaping-up-data-giving-rise-new-economy)**). Among the nice aperçus:**

- “Data will be the ultimate externality: we will generate them whatever we do.” — Paul Sonderegger of Oracle.
- The “data-network effect”: using data to attract more users, who then generate more data, which improve services, which attracts more users.
- By the end of 2016, Tesla had 1.3bn miles-worth of driving data — orders of magnitude more than Waymo, Google’s self-driving-car division.
- The pricing difficulty explains why one firm might buy another, even if it is mainly interested in data. This was the case in 2015 when IBM reportedly spent $2bn on the Weather Company, to get its hands on mountains of weather data and the infrastructure to collect it.
- Data exhibit “decreasing returns to scale”: each additional piece of data is less valuable, and at some point, more does not add anything.
- Google is about the quality of the algorithms and the talent, not the data. It is about “recipes, not ingredients.” — Hal Varian, Google chief economist.
- With more and fresher data than others, “super-platforms” can quickly detect competitive threats. They can manipulate the markets they host by having their algorithms quickly react so that competitors have no chance of gaining customers by lowering prices. (Economist article on algorithmic collusion is [here](http://www.economist.com/news/finance-and-economics/21721648-trustbusters-might-have-fight-algorithms-algorithms-price-bots-can-collude))
- “Data is labour,” according to Glen Weyl, an economist at Microsoft Research. He is developing a system to measure the value of individual data contributions to create a basis for a fairer exchange.

***What’s next for data — as a resource and as an asset class? Drop me a line with your views via ***[***www.cukier.com***](http://www.cukier.com)*** or on twitter: @kncukier***

[Data and the secret scramble for AI’s soul](https://medium.com/self-driving-company/data-and-the-secret-scramble-for-ais-soul-69afaf7c913f) was originally published in [the self-driving company](https://medium.com/self-driving-company) on Medium, where people are continuing the conversation by highlighting and responding to this story.
