---
title: "Linking DOIs using HTTPs: the background to our new guidelines"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2017
date: 2017-01-17
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/linking-dois-using-https-the-background-to-our-new-guidelines/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/6xkdj-gzr09."
---

# Linking DOIs using HTTPs: the background to our new guidelines

## Full text

**12 minute read.**

## Linking DOIs using HTTPs: the background to our new guidelines

Recently we announced that we were making some new recommendations in our DOI display guidelines. One of them was to use the secure HTTPS protocol to link Crossref DOIs, instead of the insecure HTTP.

Some people asked whether the move to HTTPS might affect their ability to measure referrals (i.e. where the people who visit your site come from).

## TL;DR: Yes

Yes. If you do **not** move your DOI links to HTTPS, Crossref, its members and the members of [other DOI registration agencies](http://www.doi.org/registration_agencies.html) (e.g. DataCite, JLC, CNKI)  will find it increasingly difficult to accurately measure referrals. You should link DOIs using HTTPS.

In fact, if you do not support HTTPS on your site **now**, it is likely that your ability to measure referrals is already impaired. If you do not already have a plan to move your site to HTTPS, you should develop one.

If you have already transitioned your site to HTTPS, you should follow the new guidelines and link DOIs via HTTPS as soon as possible. As it stands, you are not sending any referrer information when DOIs are clicked on and followed from your site. You should also make sure that the URLs you have registered with Crossref are HTTPS URLs, otherwise *you* will not get referrer information on your site when they are followed.

Read on if you want some grody details. We’ll try to keep it as non-technical as possible.

## Two protocols, one web

To start with your web browser supports two closely related protocols, HTTP and HTTPS.

The first, HTTP, is the protocol that the web started out with. It is an unencrypted protocol and it is also easy to intercept and modify. It is also very easy and inexpensive to implement.

The second protocol, HTTPS, is a secure version of the first protocol. It is very difficult to intercept and modify. It has historically been more complex and expensive to implement.

Here you might say - “Great, but HTTPS has been around for a long time. We’ve used it for sensitive transactions like authentication and credit card transactions. Why do we want to use DOI links with HTTPS?” Why are you suggesting that we should even consider moving our entire site to HTTPS? 

## The pressure to move to HTTPS

The insecure HTTP protocol has become a major vector for a lot of security issues on the web. It allows user web pages to be intercepted and modified between the server and the browser. This flaw is being abused for everything from spying, to inserting unwanted advertisements into web pages, to distributing viruses, ransomware and botnets.

As such, there has been a steady drumbeat of industry encouragement to move to the more secure HTTPS protocol for all website functions.

We are not going to argue all the points here. Instead we will mention the major constituencies that are advocating for a move to HTTPS and provide you with some pointers. We apologise that these are all so US-centric, but a lot of the web’s global direction does seem to be presaged by US adoption trends.

## Google

It is probably easiest to start with Google, since its practices tend to focus the attention of those managing websites.

Back in 2014 [Google announced that they would slowly move toward including the use of HTTPS as a ranking signal](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html). In 2015 they upped the ante by announcing that [they would start indexing HTTPS versions of pages by default](https://security.googleblog.com/2015/12/indexing-https-pages-by-default.html). It looks like in early 2017 they will really start to take the gloves off as they [modify their Chrome browser to flag sites that do not use HTTPS as being `insecure`](https://www.chromium.org/Home/chromium-security/marking-http-as-non-secure).

## Every top website, [evah](http://www.urbandictionary.com/define.php?term=evah)

It looks like Google's plan is working too. Their [2016 transparency report](https://www.google.com/transparencyreport/https/grid/?hl=en) shows that most top websites have already transitioned to HTTPS and that this translates to approximately 25% of all web traffic worldwide taking place using HTTPS. Indeed, over 50% of all web pages viewed by desktop users are delivered via HTTPS.

## Government agencies

The USA’s Whitehouse issued [[a directive instructing all Federal websites to adopt HTTPS](https://www.whitehouse.gov/blog/2015/06/08/https-everywhere-government)]. As of December 2016 [64%](https://pulse.cio.gov/) of federal websites have made the transition.

## Libraries

Much of the pressure to move to HTTPS is coming from the library community who have a historical tradition of protecting patron privacy and resisting efforts to censor content. The third principle of the American Library Association's code of ethics reads:

We protect each library user’s right to privacy and confidentiality with respect to information sought or received and resources consulted, borrowed, acquired or transmitted.

Recently there has been [a major push by the Electronic Frontier Foundation](https://www.eff.org/deeplinks/2016/12/librarians-act-now-protect-your-users-its-too-late) to get libraries to adopt a number of security and privacy practices, including the use of HTTPS by all library systems as well as those used by library vendors.

## What are Crossref members doing about HTTPS?

How big an issue is this? How many of our members have moved to HTTPS? How many plan to? Well, we looked at the URLs that are registered with Crossref and we tested them with both protocols. Eventually we will write a blog post detailing our findings - but the highlights are:

* Slightly fewer than half of the member domains tested only support HTTP.
* Slightly fewer than half of the member domains tested support both HTTP and HTTPS.
* About 370 of the member domains tested only support HTTPS.

## The transition to HTTPS and the issue of DOI referrals

The HTTP referrer is a piece of information passed on by a browser that indicates the site from which the user navigated.

So, for example, if a user visiting site `A` clicks on a link which takes them to site `B`, site `B` will then record in its logs that a user visited them from site A. Obviously, this is important information for understanding where your web site traffic comes from.

The default rules for referrals are[1](#fn1):

1. If you link between two sites with the same level of security, all referral information is retained.
2. When you follow a link from an insecure (HTTP) web site to a secure (HTTPS) site, referral data is passed on to the secure web site.
3. If you follow a link from a secure (HTTPS) web site to an insecure (HTTP) site, referral data is not passed on to the insecure web site.

So let's see what the situation would look like with normal links. If we had two sites, `A` & `B`, the following table maps the possible combinations of protocols that can be used to link from `A` to `B`. So, for example, row #2 reads:
> A user browses site A using HTTP and clicks on a HTTPS link to publisher B who hosts their site using HTTPS.

The last column indicates if the referrer information is passed along by the browser. In the case of row #2, the answer is “yes”. The user has navigated from a less secure site to a more secure site.

|  |  |  |
| --- | --- | --- |
| **User views site A using** | **Site A links to site B using** | **Browser reports referrer to site B** |
| HTTP | HTTP | Yes |
| HTTP | HTTPS | Yes |
| HTTPS | HTTP | No |
| HTTPS | HTTPS | Yes |

But this gets a little more complicated with DOIs. In this case publisher `A` links to publisher `B` through the DOI system. This means there are two parts to the link. The first `(A->doi.org)` results in a redirect (A->B). Again we use the last columns to indicate when referrer information is passed along to site B. Again, let’s look at row #2. It reads:

A user browses the site of member A using HTTP and clicks on a HTTP DOI link. The DOI system redirects the browser to member B using an HTTPS link registered with Crossref by member B. The middle column and the last column records whether Crossref and the publisher were able to see referrer information. The answer in both cases is “yes”. In the first case (A->DOI) because the link was from a less secure site (HTTP on A) to a more secure site (HTTPS at DOI). The second case because the link is between two sites at the same security level (HTTP).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **User views site A using** | **Site A links DOI using** | **Browser reports referrer to Crossref[2](#fn2)** | **Crossref redirects to site B using[3](#fn3)** | **Browser reports referrer to site B** |
| 1 | HTTP | HTTP | Yes | HTTP | Yes |
| 2 | HTTP | HTTP | Yes | HTTPS | Yes |
| 3 | HTTP | HTTPS | Yes | HTTP | Yes |
| 4 | HTTP | HTTPS | Yes | HTTPS | Yes |
| 5 | HTTPS | HTTP | No | HTTP | No |
| 6 | HTTPS | HTTP | No | HTTPS | No |
| 7 | HTTPS | HTTPS | Yes | HTTP | No |
| 8 | HTTPS | HTTPS | Yes | HTTPS | Yes |

## So what does this mean?

Our old display guidelines recommended linking DOIs using HTTP. Rows #1, #2, #5, #6 represent the status quo.

About half of our members support HTTPS. A few support it exclusively and it seems, given the industry pressures mentioned above, those who support both protocols are likely doing so as a transition stage to HTTPS-only sites.

This means that **the scenarios represented in row #5 & #6 are already happening**. The referral information for any user viewing one of our member sites using HTTPS is being lost when they click on DOIs that use the HTTP protocol. Crossref doesn’t get the referral data and neither does the member whose DOI has been clicked on.

Of course this applies to non-member sites that link to DOIs as well. Wikipedia is the largest referrer of DOIs from outside the industry. In 2015 The Wikimedia Foundation [made a highly publicised transition](https://blog.wikimedia.org/2015/06/12/securing-wikimedia-sites-with-https/) to HTTPS on all of their sites. This means that any of our members who are running HTTP sites have already lost the ability to see any referral information from Wikipedia on their own sites. However, Crossref [worked closely with Wikimedia](http://blog.crossref.org/2016/05/https-and-wikipedia.html) to ensure that, at the very least, Crossref was still able to record Wikimedia referral data on behalf of our members.

## A solution

It is largely this work with Wikimedia that has helped us to understand just how important it is for Crossref to get ahead of the curve in helping our community to transition to HTTPS.

As long as our members are running a combination of HTTP and HTTPS sites, there is no way for our community to avoid some disruption in the flow of referral data. And we certainly would never entertain the notion of asking our members to keep using HTTP.The best we can do is recommend a practice that will help smooth the transition to HTTPS. That is what we are doing.Our new recommendation is to move to linking DOIs using HTTPS. This is represented in rows #3, #4, #7 and #8 in the table above.

This is a particularly important step for our members who have already moved to hosting their sites on HTTPS. As long as they are using HTTP DOIs on their site, they will be sending no referral traffic to Crossref, other Crossref members or other users of the DOI infrastructure. This is captured in scenarios #5 and #6.

If our linking guidelines are followed during the industry’s transition to HTTPS, then scenario #5 and #6 will eventually be replaced with scenario #7. It is still not perfect, but at least it means that, during the transition, publishers who are still running HTTP sites will be able to get some DOI referral data via Crossref. And of course, once our members have widely transitioned to HTTPS, everything will go back to normal and they will be able to see referral data on their own sites as well (i.e.they will have moved from the state represented in row #1 to state represented in row #8.)

In summary, please change your sites to use HTTPS to link DOIs. They should look like this:

[<https://doi.org/10.7554/eLife.20320>](https://doi.org/10.7554/eLife.20320)

## FAQ

**Q:** If I have moved my site to HTTPS, do I need to redeposit my URLs to that they use the HTTPS protocol instead?

**A:** Yes. If you want to be able to still collect referrer information on your site (scenario #8) as opposed to via Crossref (scenario #7).

---

**Q:** But can’t I avoid redepositing my URLs and get referrer data again if I simply redirect HTTP URLs to HTTPS on my own site?

**A:** No. The browser will strip referrer information if there is any HTTP step in the redirects. Even if the redirect is done on your own site.

---

**Q:** Can I avoid having to redeposit all my URLs? Can’t Crossref just update the protocol on our existing DOIs for us?

**A:** Contact [[support@crossref.org](mailto:support@crossref.org)](mailto:support@crossref.org). We’ll see what we can do.

---

**Q:** What about all the old PDFs that are are there? They link to DOIs using HTTP.

**A:** That is true. But links followed from PDFs don’t send referrer information anyway.

---

**Q:** And what about my new PDFs? Should I start linking DOIs from them using HTTPS.

**A:** Probably. But not because of the DOI referrer problem. Simply because HTTPS is a more secure, private, and future-proof protocol.

---

**Q:** Don’t some countries block HTTPS?

**A:** Typically countries block specific sites and/or services. We do not know of any countries that have a blanket block on the HTTPS protocol.

---

**Q:** I use a link resolver that uses OpenURL + a  cookie pusher to redirect my users to local resources. What do I need to do?

**A:** You need to change your cookie pusher script to enable the `Secure` attribute for cookies for HTTPS-linked DOIs.   

---

**Q:** Can I use protocol-relative URLs (e.g. [//doi.org/10.7554/eLife.20320](https://doi.org/10.7554/eLife.20320))?

**A:** Protocol-relative URLs can be used in HTML HREFs to help ease the transition from HTTP to HTTPS, but use the full protocol in the text of the DOI link itself. So, for example, the following is fine:

```
https://doi.org/10.7554/eLife.20320
```

---

**Q:** I hear that HTTP and HTTPS versions of URI identifiers are considered to be different identifiers. Doesn’t this mean that by moving to HTTPS we are essentially doubling the number of DOI-based identifiers out there?

**A:** Yes. It isn’t a problem that is only being faced by DOIs. Basically all HTTP-URI based identifiers face the same issue. We will put in place appropriate same-as assertions in our metadata and HTTP headers to allow people to understand that the HTTP and HTTPS representations of the DOI point to the same thing.

*On a personal note (@gbilder speaking- don’t blame @CrossrefOrg) - it breaks my brain that the official line is that the protocol difference means they are different identifiers. As a practical matter (a concept the W3C seems to be increasingly alienated from), it would be insane for anybody to follow this policy to the letter. You can probably be pretty safe swapping the protocols on DOIs and being sure you will get the same thing.*

---

**Q:** I see that the Crossref site isn’t running on HTTPS. Are you just a bunch of hypocrites?

**A:** ~~Yes. The site will be moving to HTTPS-only very soon. Then we won’t be.~~ We do now.

## References

1. These rules can be tweaked using meta referrer tags (https://www.w3.org/TR/referrer-policy/), but not in any way that both avoids the fundamental problems outlined here **and** that preserves the security/privacy characteristics that are the very reason to implement HTTPS in the first place.
2. To be pedantic- it actually passes referrer information to the DOI proxy (https://doi.org/), which in turn is reported to Crossref.
3. To continue with the pedantry- the DOI proxy does the redirect based on the URL member B has deposited with Crossref.
