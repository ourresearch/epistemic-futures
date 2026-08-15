---
title: "A Department-Based Twitter Aggregator in Google App Engine"
person: mike-caulfield
section: by
type: blog-post
year: 2009
date: 2009-12-17
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2009/12/17/a-department-based-twitter-aggregator-in-google-app-engine/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# A Department-Based Twitter Aggregator in Google App Engine

## Full text

We have a department twitter account here at CELT. The idea of that account is it’s a place to share edtech and ed design info without forcing faculty members to sort through my political rants, Jenny’s comments about beer and biking, etc.

But obviously it’s makes very little sense for us to log into that account whenever we have a new edtech insight or retweet. We’d like to just stay in our own spaces, and let the @kcelt feed pick up the pertinent stuff.

So I built this little aggregator to compile all of our tweets that use the kcelt keyword.

[http://twaggart.appspot.com/?g=kcelt&a=raganmd,holden,gobman,judybrophy,scastriotta](<http://twaggart.appspot.com/?g=kcelt&a=raganmd,holden,gobman,judybrophy,scastriotta>)

where basically param ‘g’ is the keyword you choose to mark stuff you want to go to the group acct, and ‘a’ is the set of twitter accounts you want to look in for that key word.

Once you get to that point (a clean RSS 2 feed) you just have twitterfeed check it every half-hour and do the required postings. You can also embed the RSS in your blog, or Pipe it to a thousand other uses.

To make sure the call stays under the 30 sec limit for App Engine threads, it makes only one call to twitter (searching for the key term) then goes through the results filtering out those authors that are not approved.

Here’s the code (Python in App Engine’s wsgi env):

<http://docs.google.com/View?id=dcb2rjpn_16f9cxvknp>

Here’s how you might post to it if you are using the params we set

And here’s how that comes out after Twitterfeed posts from the aggregated feed:

Obviously, you would likely use a different keyword and different accounts. But it’s App Engine, so feel free to use it if you want, and let others know about it.

You can see our newly rejuvenated kcelt feed, with everyone’s contributions, [here](<http://twitter.com/kcelt>).
