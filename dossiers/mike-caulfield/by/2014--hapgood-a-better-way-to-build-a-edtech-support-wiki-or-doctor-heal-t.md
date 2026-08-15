---
title: "A Better Way to Build a EdTech Support Wiki (or, Doctor, Heal Thyself)"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-01-30
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/01/30/a-better-way-to-build-a-edtech-support-wiki-or-doctor-heal-thyself/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# A Better Way to Build a EdTech Support Wiki (or, Doctor, Heal Thyself)

## Full text

This post is going to be a bit geeky, and a tad technical. So there’s your warning.

I’ve been thinking a lot about the [forkable Domain of One’s Own wiki](<http://timmmmyboy.com/posts/please-steal-domain-of-ones-own>), with its GitHub underpinning. And I’ve been watching a lot of Ward Cunningham’s videos on the concept of [federated wikis](<http://www.wired.com/wiredenterprise/2012/07/wiki-inventor/>).

And the thing I’ve come to realize is the institutional educational technology unit support site is a perfect microcosm of our more general OER challenges. What do I mean? Here’s my support wiki:

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/01/mywiki.png>)

And here’s Keene State’s site:

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/01/keene.png>)

And here’s Thompson Rivers:

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/01/blende2d.png>)

Here’s some UMW documentation on using digital audio:

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/01/players.png>)

Just as with class materials, the reusability paradox rears its ugly head. There are bits mixed into these sites that are very institution specific. The players site above links to some UMW-specific stuff. The Keene site mixes in announcements about local presentations with more generic pieces on using screencasting as a tool. These are small things, but the feeling of local integration is important to the faculty hitting these resources. You really do want the faculty reading the material on screencasting to finish the article with a link to someone on campus they can contact, and as silly as it is, you’d like the faculty to feel locally supported, so the prospect of everything being a link to other university’s websites is unappealing.

But the way we accomplish this is a bit ridiculous, really. We reinvent the wheel a dozen times a month so that we can get that 10% difference that preserves the impact we want.

Is there another way to get that balance? It’s possible that a federated approach could provide the impact of local integration with the efficiency (and culture) of syndication. Playing around with Cunningham’s radical version of federation has convinced me it’s a bit much for people to swallow at this point. But the basic principle — that instead of every page on a site have an edit button, there is a “clone” or “fork” button is compelling. In such a world, if I saw a useful article on screencasting from Judy Brophy at Keene State, I’d hit the “Clone This” button on it (or perhaps hit a scriptlet button in my browser), and pull it over to my own support site. There I’d edit it to make it fit my faculty needs better.

Here’s the important thing — cloned articles would retain their history and relation. So the pieces of this that were Judy’s would still be attributed on the back end to Judy automagically, and the edits that were mine would be attributed to me. Better yet, since my page is seen by the version control repository as a fork, when Judy updates her article to cover new versions of Jing (complete with updated screenshots) those edits are pushed to me to accept or reject. And when I link to things on my site from the cloned page, Judy can check if she would like to clone some of those pages into her own site.

I don’t quite know how to build this, but it seems to me that the work that UMW is doing with dokuwiki could be a step towards this sort of world. And it could form the basis of a solution to some persistent problems in ed-tech around balancing distributed production and local autonomy. Best of all, unlike the classroom, how we build our support wikis is completely within our control.

Does anyone want to look at this idea with me, head down the path with it a quarter-mile or so, and see if it’s worthwhile or completely cracked? In short, what we’re looking at is collaboration in a world where open-licensing and version-control software make forks much, much less painful to manage…

(Note: In addition to Ryan Brazzel and Tim Owens and Jim Groom, I am indebted to both Alan Levine and Brian Lamb who have talked before about embedded content which is the *syndicated* way of doing this, this is really just taking that a step further towards *federation*.)
