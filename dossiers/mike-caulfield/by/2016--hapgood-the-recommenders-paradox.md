---
title: "The Recommender\u2019s Paradox"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-01-12
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/01/12/the-recommenders-paradox/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# The Recommender’s Paradox

## Full text

A [recent-ish study](<http://delivery.acm.org/10.1145/2650000/2645737/p161-ekstrand.pdf?ip=69.166.35.226&id=2645737&acc=ACTIVE%20SERVICE&key=B63ACEF81C6334F5%2E3B1D11B7501B70D8%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&CFID=744550461&CFTOKEN=91462271&__acm__=1452622778_ae967937d8b15442fefdd4516c57c4dc>) looked at film recommendation systems and found an interesting result: perceived novelty of the recommendations was negatively correlated with user satisfaction, and user satisfaction was correlated adoption.

> One of the most striking things we found is that the novelty of recommended items has a significant negative impact on users’ perception of a recommender’s ability to satisfactorily meet their information needs. This effect was particularly strong in its impact on the user’s first impression of an algorithm, and was present even though we restricted the depth of the long tail into which our algorithms could reach.

And so you end up with what I’ll call the _recommender ’s paradox_. People turn to recommendation systems to find things they wouldn’t have thought of themselves, but they choose recommendation systems that largely provide them choices that don’t surprise them. Aspects of trust in the recommender relationship undermine efficacy.

One approach to the paradox is to introduce novelty slowly, after trust is built, but there’s some bad news there as well:

> Increasing the novelty of recommendations as the user gains more experience with the system and has had more time to consider its ability to meet their needs may provide benefit, but our results cannot confirm or deny this. The users in our study are experienced with movie recommendation in general and MovieLens in particular (the median user has rated 473 movies), and their first impressions were still heavily influenced by novelty.

One other way to think of this is that people think they want new films recommended to them but actually they really want to be  _reminded_ of films they had already been thinking about seeing but had forgotten about, or notified about familiar looking films that had slipped under their radar. My guess is the most successful engine (based on user satisfaction) would probably provide you with a wide range of films by directors and actors you know you like but had forgotten about, in genres that you know work for you. These results would seem tailored to you, but at the same time be things you would not have thought of yourself.

Obvious implications here on Open Educational Resource recommendation algorithms, Big Data, the Filter Bubble, and the problem of resistance to novelty in education more generally.
