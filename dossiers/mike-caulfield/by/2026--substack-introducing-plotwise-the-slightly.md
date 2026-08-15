---
title: "Introducing Plotwise, the slightly weird film explorer"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-05-29
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/introducing-plotwise-the-slightly
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Introducing Plotwise, the slightly weird film explorer

*Running a recommendation engine off of HTML and 5 MB of JSON*

## Full text

[](<https://substackcdn.com/image/fetch/$s_!TcNw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6281e08b-2fee-4e54-84d8-13668ff562bd_1538x954.png>)

**UPDATE: Plotwise is now[Plot.fyi](<https://plot.fyi>), and you should check it out. The post below refers to an earlier version called plotwise.**

Plotwise, the film explorer idea I’ve been working on for the past month or so, [is up](<https://plot.fyi>). 

It’s a tool for film geeks, and it’s not particularly user friendly at the moment. I mainly built it for my own use, and wasn’t planning to publish it until I was surprised how well it worked. 

I’ll talk about how I built it later but here’s what you can do with it. 

You can find matches for any film in the database (there’s 10,000+ films). Here’s matches for [The Others](<https://checkplease.neocities.org/plotwise/#c/The%20Others>). You get this by typing in “match The Others” in the command line.

[](<https://substackcdn.com/image/fetch/$s_!Stj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F771ff72b-f4c2-4a70-98eb-472828106dc1_1555x915.png>)

If you can’t quite remember the name, type “find” plus a word from the title, as here with [find Mulholland](<https://checkplease.neocities.org/plotwise/#c/find%20Mulholland>) (if you screw up spelling I can’t help).

[](<https://substackcdn.com/image/fetch/$s_!AbSa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb172cd11-f45d-4a87-a6e2-af06fa61271f_1573x514.png>)

Then [click in](<https://checkplease.neocities.org/plotwise/#c/match%20Q272608>).

[](<https://substackcdn.com/image/fetch/$s_!MBvE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b302a7f-d3c3-4b59-9b9f-13847019023d_1548x994.png>)

If you want to know why a film matched, [click explain](<https://checkplease.neocities.org/plotwise/#c/explain%20Q272608%20%2F%20Q482626%20--exclude%20a%3A*_film%20a%3A*_film*>).

[](<https://substackcdn.com/image/fetch/$s_!-YP7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b1249e2-3c32-4e52-a2c9-8935a2b4ad49_1551x876.png>)

Note that the key to a good recommendation engine that gets you unexpected connections is _permissive tagging_ , that is, in setting your tagging precision rate low enough so that the tags cast wide enough a net to pull in interesting connections but not so wide that they are useless. So if you are looking at this and exclaiming “According to my analysis these are nothing like the films of Ari Aster!” all I can say is you can try to build a tagging system where only 7 films in a 10,000 film set get tagged _asteresque_ , but I think if you think that through you’ll see the problem with that logic.

The union function is new, just made this morning, but if you hit the union operator it tries to use two films as “co-anchors” and do similarity based on the intersection of their tags. It’s not quite there yet, but it’s already interesting. [Click the little union button](<https://checkplease.neocities.org/plotwise/#c/match%20Q272608%20%7C%20Q125772>) in the results. Here we union Solaris with Mulholland Drive, and get [a good result set](<https://checkplease.neocities.org/plotwise/#c/match%20Q272608%20%7C%20Q125772>) for that I think.

[](<https://substackcdn.com/image/fetch/$s_!4cOH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04300a3e-9b68-4449-abac-3491e540aec0_1546x911.png>)

The clustering doesn’t work quite yet, but will cluster films in the list according to intra-list similarity when done.

If you need help, just [type ](<https://checkplease.neocities.org/plotwise/#c/help>)_[help](<https://checkplease.neocities.org/plotwise/#c/help>)_.

At some future point I’ll be open to suggestions or criticisms, but right now questions like “why aren’t there' more films like X in there” or “how come Y is matched with Z I don’t like that” will probably earn you my annoyance if you treat this like a product to which you have some form of user demand. On the other hand, noting interesting patterns (even if those are suboptimal) will garner my interest. In other words, when you use this thing you’re eating a meal in my home, not a restaurant, so please act accordingly and don’t make me regret putting my personal project up. 

Also the JSON file represents over a month of work on my personal time to tag it. While legally you could probably steal it, I’d appreciate if you asked before grabbing it for your own project. Not only do I get paid zero dollars to do this, but I don’t even currently have a job that rewards research, so my decision to put it up really is mostly I want to help people get more into films. Looking at it to see how it works of course is fine.

Oh, and per the subtitle — yes, this recommendation engine is just HTML. No server side processing, no run-time AI. Just a 5MB json and bunch of HTML processing 10,000 records and doing similarity computations.
