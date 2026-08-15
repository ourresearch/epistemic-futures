---
title: "Minor SIFT Toolbox for Claude 3.7 Update"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-04-24
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/minor-sift-toolbox-for-claude-37
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Minor SIFT Toolbox for Claude 3.7 Update

*Adding a "Potential Leads" Section*

## Full text

(Just need the example prompts? Click [here](<https://mikecaulfield.substack.com/i/161930544/sample-prompts>). For prompt code, click [here](<https://checkplease.neocities.org/>).)

One thing I have struggled with in SIFT Toolbox for Claude is its tendency to guess when it doesn’t quite know. The problem is that you can use language to turn down its tendency to guess, but then you often miss important information. Turn the tendency to guess up, and suddenly you have the opposite problem, with the Toolbox making large leaps. I could never get it right. In fact, sometimes when I told it _not_ to guess it would end up even more credulous.

A couple days ago I stumbled on a solution. Instead of trying to set the right credulity level I added a section called “Potential Leads”. And that’s about it, really, just added a section to put potential leads into. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

And that… seemed to work? It’s not perfect, but the system having a place to put things it is not sure about without having to decide on them has solved a lot of the problems I was seeing. You can use the Potential Leads section to follow up, well, “potential leads”. It’s a place where the tool can park an assessment like “I think the photo here might be from this event but I’m not sure,” etc. 

Of course, this tends to build the solution around the sorts of things I use it for, where we are looking at poor contextualized information online and trying to contextualize it. But after hammering on the new revision for a couple days (I know how to party on my vacation) I’m confident its an improvement and am releasing it. As usual the prompt language is below, followed by a couple test prompts. You can use text prompts too — they are actually far easier for the system to process. I put the screenshot prompts because they tend to be more complex. 

Also, **Anna Mills** did a recent test of the code in Gemini 2.5 with some good results, so you might try it there. I had been disappointed with the way the code performed in the previous version of Gemini, but the new version looks very promising! Let me know how that works if you try it.

## Instructions Text

* * *

The most recent instructions can be found on the [SIFT Toolbox site](<https://checkplease.neocities.org/>).

* * *

## Sample prompts

[](<https://substackcdn.com/image/fetch/$s_!lagP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7296ec25-dd83-4591-a4ad-8d5bf6c96254_661x589.png>)

> [Jabbari Claim](<https://claude.ai/share/8c1ea4fd-9729-41f8-a334-834ca07a818c>) (For research purposes only)

[](<https://substackcdn.com/image/fetch/$s_!oBQe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7b8e3ab-6842-4ef5-adcb-1c96b0b5fd15_648x647.png>)

> [Dead Loop Claim](<https://claude.ai/share/8f4c67ad-9c44-450b-a736-1565c2a3ade6>) (For research purposes only)

[](<https://substackcdn.com/image/fetch/$s_!K32w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1a19e80-d982-4653-b70f-f2d7dfe02fc7_518x842.png>)

> [Fauci Net Worth Claim](<https://claude.ai/share/2ed5e153-6992-4a54-8174-c4292fc329d9>) (For research purposes only)

[](<https://substackcdn.com/image/fetch/$s_!tp9N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febd4fbd8-e791-4553-b710-911dc7881034_689x851.png>)

> [Rocket-Looking Thing](<https://claude.ai/share/30f9c326-03c6-41d3-b766-2cdfba5ed002>) (This one goes badly wrong — common problem with LLM “vision”)

[](<https://substackcdn.com/image/fetch/$s_!7P6i!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65ae2c2a-82a5-42a0-8294-10da879f7ca8_524x239.png>)

> [Alexa privacy](<https://claude.ai/share/a901179b-a7cf-4ebb-907a-56d0ed783ba6>) (For research purposes only)

[](<https://substackcdn.com/image/fetch/$s_!UVzD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5b57e58-19aa-445f-8a4e-71106f589e1d_676x586.png>)

> [Pope Lambo](<https://claude.ai/share/c3577811-1944-4ed5-b346-addf6040d977>) (For research purposes only)

[](<https://substackcdn.com/image/fetch/$s_!PwnK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd12e96d3-f6a0-4383-ada7-bc0e07a51c33_669x573.png>)

> [Dye Phase-Out](<https://claude.ai/share/f595389f-a93d-48f2-b939-98e091b5e0ac>) (for research purposes only)

[](<https://substackcdn.com/image/fetch/$s_!HJ66!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f07a9c8-5714-4005-b6fc-c46404019168_1179x1431.jpeg>)

> [Trump on Crimea/Ukraine](<https://claude.ai/share/9e3ec277-b170-4a34-acb0-c3d0ea3664f5>) (for research purposes only)

[](<https://substackcdn.com/image/fetch/$s_!7cLY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d44f556-14c3-49bd-bc18-68fdb3f9bf7f_1107x1422.png>)

> [CT Income](<https://claude.ai/share/06094fda-80aa-4f8a-a719-374f4c4e75e9>) (Research purposes only)

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
