---
title: "Spam Filtering Statistics from oreilly.com"
person: tim-oreilly
section: by
type: blog-post
year: 2006
date: 2006-06-19
venue: "O'Reilly Radar (radar.oreilly.com, legacy site)"
authors: "Tim O'Reilly"
source_url: http://radar.oreilly.com/archives/2006/06/spam_filtering_statistics_from.html
retrieved: 2026-08-13
content: full-text
notes: "Legacy O'Reilly Radar post. radar.oreilly.com now blanket-301s to the current /radar/ root and every old path is dead, so this was retrieved from a Wayback Machine snapshot using the id_ replay form (no Wayback chrome in the text). Byline verified as Tim O'Reilly on the archived page. Comment threads, tag lists and site navigation stripped."
---

# Spam Filtering Statistics from oreilly.com

## Full text

I thought readers might enjoy this message that O'Reilly sys admin chief Bob Amen just wrote on our internal mailing list:"Below is a summary of the incoming email to our gateway mail servers for all domains that we accept email for (there are 57 domains). This summary is for the last 7 days: 

> Our mail servers accepted 1,438,909 connections, attempting to deliver 1,677,649 messages. We rejected 1,629,900 messages and accepted only 47,749 messages. That's a ratio of 1:34 accepted to rejected messages! Here is how the message rejections break down:

> Bad HELO syntax: 393284   
>  Sending mail server masquerades as our mail server: 126513   
>  Rejected dictionary attacks: 22567   
>  Rejected by SORBS black list: 262967   
>  Rejected by SpamHaus black list: 342495   
>  Rejected by local block list: 5717   
>  Sender verify failed: 4525   
>  Recipient verify failed (bad To: address): 287457   
>  Attempted to relay: 5857   
>  No subject: 176   
>  Bad header syntax: 0   
>  Spam rejected (score => 10): 42069   
>  Viruses/malware rejected: 2575   
>  Bad attachments rejected: 1594 

> The order that the rules are listed above is the order in which the rules are tested on each message.

> I hope you find this interesting. Consider also that this is all done with open source software running on two Linux machines. The MTA is Exim with SpamAssassin used for spam analysis and ClamAV for virus analysis. I spend less than an hour a week maintaining these two systems. That's a pretty good ROI.

I'm sure you have your own similar (or worse) statistics. What a waste! (And thanks to all the developers and administrators who've make this problem much less intrusive to ordinary users, leaving it to people like Bob who have to shovel out the sh*t. Ordinary users still think spam is bad, but they don't really know just how bad....)
