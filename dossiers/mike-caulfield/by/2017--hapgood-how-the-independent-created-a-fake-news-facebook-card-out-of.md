---
title: "How the Independent created a fake news Facebook card out of a real story"
person: mike-caulfield
section: by
type: blog-post
year: 2017
date: 2017-09-07
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2017/09/07/how-the-independent-created-a-fake-news-facebook-card-out-of-a-real-story/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# How the Independent created a fake news Facebook card out of a real story

## Full text

Here’s a thing going around Facebook today: Chicago mayor Rahm Emmanuel banned Trump from Chicago!

So did Rahm just go Rahm-bo? Did he ban Trump from the city? Clicking through and seeing the headline on the actual article suggests a less dramatic story:

And the quote in context?

> _[Chicago Mayor Rahm Emmanuel] added: “Chicago, our schools, our neighborhoods, our city,_ as it relates to what President Trump said _, will be a Trump-free zone. You have nothing to worry about. And I want you to know this, and I want your families to know this. And rest assured, I want you to come to school … and pursue your dreams.” [italics mine]_

So in other words, the Facebook headline is a complete lie. Emmanuel was simply saying he was not going to spend resources to enforce federal law in Chicago. Trump himself has not been banned from anything at all.

So where did that initial headline come from? The clickbait one on Facebook which tells a flat-out lie? Was it made by Facebook? Or added by a deceitful user?

Nope. It was written by the Independent.

Let me repeat that. The Independent wrote the fake headline.

So why do we not see it on the Independent site? Well, a little known fact about newspapers and other websites is they embed code in invisible HTML “meta” tags that provide  _different headlines to different platforms,_ when the content is shared. And if we look in those meta tags we see that someone at the Independent coded the false headline in the meta tags, even though they would never dare publish such a headline on their web site.

Here’s the title you’ll see in your browser bar or tab (and the title that used to be shared with sharing services) as it appears in the HTML:

> _< title>_**_Chicago mayor declares city ‘Trump-free zone’ after US President declares he will scrap DACA immigration programme | The Independent_** _< /title>_

Here’s the title that people see, again, as it sits in the HTML on the actual page:

> _< h1 itemprop=”headline” class=” “>_**_Chicago mayor declares city ‘Trump-free zone’ after US President declares he will scrap DACA immigration programme_** _< /h1>_

And here is where the HTML tells Twitter and Facebook what to use:

> _< meta property=”og:title” content=”_** _Chicago just banned Donald Trump from the city_** _” / >_

> _…_

> _< meta name=”twitter:title” content=”_** _Chicago just banned Donald Trump from the city_** _” / >_

The only places in that code where the Independent even  _mentions_ a “ban” are visible in Facebook and Twitter but not on the site, so the site can publish clickbait into social platforms while still retaining a shred of respectability on its website. And if people complain about the Facebook headline, they can always point to the headline on their site as being more or less valid (although it’s still horrible, tbh).

Does this sort of deception work? Why, yes it does. This story has been shared on Facebook [**almost half a million times in 24 hours**](<https://graph.facebook.com/?id=https%3A%2F%2Fwww.independent.co.uk%2Fnews%2Fworld%2Famericas%2Fchicago-mayor-trump-free-zone-rahm-emanuel-daca-dreamers-programme-us-president-sanctuary-city-a7931646.html>). That likely makes it one of the top shares, if not  _the_ top share of the day. And they accomplish this by abuse of the platform-specific headline codes. The whole thing is shameful, and an insult to the good work that the Independent’s reporters do. And it’s time for it to stop.

### Solutions

Normally I don’t offer bullet-pointed solutions to things. But the solutions are almost ridiculously simple here. It’s just a matter of will, ethics, and incentives to get them done:

  * Papers: stop doing this. Apply procedures and oversight to meta tags.
  * Facebook: stop tolerating it. Scanning the semantic difference between og:title and <h1> title is an easy fact check. Write code to do that and flag offenders. This is Spam 101.
  * People: Click through before you share. Always. And demand better from established papers. The “reverse mullet” headline (party in the front, business in the back) must die, once and for all.
