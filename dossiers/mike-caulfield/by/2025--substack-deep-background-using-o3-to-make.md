---
title: "Deep Background: Using o3 to make an annotation layer to the \"MAHA\" report"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-06-03
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/deep-background-using-o3-to-make
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Deep Background: Using o3 to make an annotation layer to the "MAHA" report

*We can think bigger on how to add context to public documents when we can fact-check -- in the original sense of the word -- at greater efficiency and scale*

## Full text

I’ll probably be doing a few posts on the HHS “MAHA” report, because it’s such an interesting example of the sort of thing which can benefit from expert context but is also just too vast to check using normal methods. There’s stuff in it that is correct (antibiotic use in children is out-of-control in this country and though new measures are starting to have some impact they are far too limited, most newer depression medications seem to have limited effectiveness for children, despite rising prescriptions). And there’s stuff that is wrong or backwards (newer guidelines for lumbar puncture have actually _reduced_ use of the procedure, not increased it, stimulant medication for ADHD generally has positive effects, even if it can’t bring children up to a non-ADHD level of behavior).

But it’s just page after page after page of it. Stuff that is fairly solid mixed with stuff that misrepresents the studies it cites, and so forth.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

So I tried a little experiment. I took the bullet points from a section here:

[](<https://substackcdn.com/image/fetch/$s_!ewzp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72210fbc-975f-4803-ac12-dc6740f8c96d_1249x800.png>)

Then I ran those through SIFT Toolbox (mostly in a one-shot without many “another rounds” — I just wanted a proof of concept). And then I told o3 to make a “Genius.com-like annotation page” that summarized the findings of SIFT Toolbox. 

And you know what? It kind of worked…

[](<https://substackcdn.com/image/fetch/$s_!_0Xo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43d6b9d1-5494-4d55-a46e-f3eb29f3c882_1527x796.png>)

You can play with it — and fork your own version — here:

<https://chatgpt.com/canvas/shared/683e5d7374bc8191a54016d29c6b844c>

I was thinking that it’d be cool to have a product — call it “Deep Background” or something similar — that could draft an annotation layer like this then put it through a human-in-the-loop process. Or maybe something like this for one’s _own_ documents — before you publish something out you explore your own document, and make sure you’ve not made any bone-headed mistakes or put your thumb on the scale in ways you didn’t realize. There’s probably something out there that does something like this already, though I wonder if it can do it this well?

Anyway, try it out, fork it, make it your own. If I can do this in an evening while half-watching TV, my guess is a press outfit with real money could do something much more interesting. 

And before you tell me fact-checking doesn’t work — I don’t aim to convince Uncle Adam on Facebook or pepelover44 on 4chan. That has never been my model of how improving discourse environments helps things. In fact, that’s always struck me as a ridiculous model. Let Uncle Adam think what he wants, and stay off 4chan.

But a wide array of professionals (policy makers, practitioners, politicians) depend on government sources of information to make real-world decisions. Helping those professionals sort the stuff grounded in evidence from flights of speculative fancy has real-world consequences. It’s worthwhile to support anyone engaged in such efforts. Annotation has long been a tool for that, and it would be exciting if newer technologies allowed for its broader use.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
