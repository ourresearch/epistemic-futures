---
title: "Copying a Whole Site Is Remarkably Easy In Smallest Federated Wiki"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-08-21
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/08/21/copying-a-whole-site-is-remarkably-easy-in-smallest-federated-wiki/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Copying a Whole Site Is Remarkably Easy In Smallest Federated Wiki

## Full text

Operations in Smallest Federated Wiki tend to be page-level — dashboard style site managers have been avoided for the moment. Still, the speed at which operations can be executed makes site-wide stuff pretty easy. This video shows how to copy a small fifteen page site in about a minute.

If you think about how long it would take you to log into a dashboard interface, export a site, log into another dashboard interface, and upload the file to the import process — Smallest Federated Wiki compares favorably.

How is this speed achieved? First of all, moving the integration to the browser allows us to pull two sites together into a single interface. Importantly, neither site has to have any knowledge of the other before the drag, because to the browser a site is just another data source. It’s the difference between the two models below, with the federated model on the right.

[](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/08/fedwiki.png>)

 

 

Client-based integration is more amenable to fluid reuse because it can have a single integrated view of multiple sites in a way that server-based systems can not.

The second reason it’s so quick is the parallel pages structure. The multiple pages on the screen are less impressive looking than your average web page. But you pay a massive tax for that look in the form of the “click-forward, act, click-backward” actions you perform every single day. Here you see how much eliminating that speeds up interaction, as you click on a list that stays in place and then fork the pages without playing the “forward-back” game.

As a side note, having used SFW for a while, I now get frustrated in “normal” web interfaces that use the single-page model. It feels ridiculously kludgy. Forward and back in 2014? Are you kidding?

The third reason the operation flows well is the data-based nature of it. We’re not shipping layout to the new site, we are essentially copying the database record for that page. No formatting surprises to greet you after the copy operation.

So fine — this is fifteen pages. What if you wanted to fork a site of a hundred pages? Well, it’d probably take seven times this long, so maybe 10 minutes?

That’s ten minutes to fork a picture perfect copy of any SFW site in the world. I’m not even sure you can do that in GitHub in ten minutes.

(Are people beginning to get the power of these few small interface changes yet?)
