---
title: "Monitorama 2014 wrapup"
person: selena-deckelmann
section: by
type: blog-post
year: 2014
date: 2014-05-10
venue: "chesnok.com (personal blog)"
authors: "Selena Deckelmann"
source_url: https://www.chesnok.com/daily/2014/05/10/monitorama-2014-wrapup/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the blog's WordPress REST API (wp-json/wp/v2/posts); HTML converted to markdown."
---

# Monitorama 2014 wrapup

## Full text

I’m just settling back into the daily routine after [RelEng/RelOps’ workweek](http://www.chesnok.com/daily/2014/05/02/release-engineering-a-draft-of-an-architecture-diagram/) and then [Monitorama](http://monitorama.com) back-to-back.

Videos [will eventually be posted here](http://vimeo.com/monitorama).

I thought it was awesome [the conference started with some #hugops](https://twitter.com/Monitorama/status/463560111240126464).

Here are my highlights:

- 
I gave a talk about [crontabber](https://speakerdeck.com/selenamarie/the-final-crontab)! I have my speakers notes if you’re interested!

- 
[Dan Slimmons gave a nice talk about basic probability](http://www.slideshare.net/danslimmon/car-alarms-smoke-alarms-monitorama) and how understanding the difference between sensitivity and specificity can help you choose more useful alerts. It was super basic stats stuff, but a good foundation for building up stats competency in teams.

- 
[James Mickens](https://research.microsoft.com/en-us/people/mickens/) gave a hilarious talk about the cloud that is well-worth finding when it goes up.

- 
Ashe Dryden gave a talk about gender issues and “our most wicked problem”. It was very well-received by the audience, which was gratifying for me personally. I think the audience walked away with some very practical things to do: speak up among peers when someone says things that make you uncomfortable and ask questions about equal treatment in your company for things like salary, perks and benefits.

- 
Several talks were given about monitoring and managing ops inside companies. [My favorite was from Daniel Schauenberg](https://speakerdeck.com/mrtazz/a-whirlwind-tour-of-etsys-monitoring-stack) (contributor to statsd) of Etsy. and Scott Sanders spoke about similar topics in [this presentaton on Github’s outage lifecycle](https://speakerdeck.com/jssjr/the-lifecycle-of-an-outage). And related, but not at the conference, Heroku [just published an incident response runbook](https://blog.heroku.com/archives/2014/5/9/incident-response-at-heroku).

- 
There was a hilarious lightning talk about the failure of the Swedish ship Vasa as an object lesson for massive project failure. [Here’s a link to the case study](http://pete.io/Jra5) the lightning talk was based on.

- 
Larry Price (@[laprice](http://twitter.com/laprice)) gave a 5-minute talk about Postgres autovacuum tuning, which was awesome, and I hope he posts the slides. It reminded me that I should do a couple brownbags about Postgres config this summer!

- 
I was struck by how many people said they used Postgres in production. Someone else asked the question during a talk, and nearly half the audience raised their hands.

- 
[InfluxDB](http://influxdb.org/), a new timeseries database emphasizing an HTTP API (remind anyone of CouchDB? :D), seemed interesting, although maybe rough around the edges when it came to documenting useful features/best practices. When I mentioned it on Twitter, I found a few folks already trying to use it in production and got at least one bug filed. 🙂

- 
I also saw an amazing demo of [Kibana](http://www.elasticsearch.org/overview/kibana/), which seems like a very interesting dashboard/investigation/querying interface to Elastic Search. I watched a friend deploy it in about an hour to look at their ES systems last Wednesday.

- 
[Dashing](http://shopify.github.io/dashing/) from Shopify was also very interesting, although a rubyist project, so not easy to integrate with our Pythonic world. However, putting on a contributor relations hat — it could be a wonderful and beautiful way for contributors to interact with our many APIs.

I’m looking forward to the videos coming out and a list of slide decks, as I missed a few talks during hallway track conversations. I met several people who are managing similar or larger event loads than we do with Socorro, so it was fun swapping stories and seeing how their software stacks are evolving. RabbitMQ was a weapon of choice for reporting environments, along with Storm. Lots of love for Kafka was out there for the people dealing with real-time customer response.

Overall, highly recommend attending Monitorama to dip a toe into the state of the art with regard to system operations, monitoring and ops management.
