---
title: "Why the Comprehensive Attribution Statement Makes Sense"
person: mike-caulfield
section: by
type: blog-post
year: 2014
date: 2014-05-05
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2014/05/05/why-the-comprehensive-attribution-statement-makes-sense/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Why the Comprehensive Attribution Statement Makes Sense

## Full text

The other day I was pointed via a tweet by David Wiley to the [Comprehensive Attribution Statement (CAS)](<http://lumenlearning.com/attribution-architecture/>) that Lumen uses. The CAS is part of Lumen’s “attribution architecture”, which is to say it provides a standard way to cite content sources. In short, it’s a sort of endnote format for remixed content. Here’s the distinctions it makes:

> The LLAA builds up a comprehensive attribution statement (CAS) from several smaller attribution primitives (AP). Each individual attribution primitive corresponds to a type of content:
> 
>   * Original content – Material that was either created specifically for the Open Course Framework (OCF) or material created previously that has never been published before (e.g., a faculty member’s lecture notes)
>   * CC licensed content – Materials previously released under a Creative Commons license
>   * Copyrighted video content – Materials from YouTube, Vimeo, and other sources whose Terms of Use allow embedding
>   * Public domain content – Materials no longer covered by copyright
>   * CC licensed content with specific attribution requirements
> 

> 
> Attribution primitives should be listed in this order, with all type 1 attributions preceding all type 2 attributions, all type 2 attributions preceding all type 3 attributions, etc. The exception to this rule is attribution of original content created by Lumen Learning, which should always be listed last.

And here’s what a statement like that might look like in practice:

> This page is licensed under a [Creative Commons Attribution License](<http://creativecommons.org/licenses/by/3.0/>) and contains content from a variety of sources published under a variety of open licenses, including:
> 
>   * Original content contributed by Mr. Putey of the Anglo-French Silly Walk Initiative.
>   * Content created by Edmund Blackadder for the History of English Dictionaries project, originally published at [http://someurl456.org/](<http://someurl359.org/>) under a CC BY license.
> 

>   * The video documentary of the Kennedy assassination was created by Dave Lister and published at <http://youtube.com/linktovideo>. This video is copyrighted and is not licensed under an open license. Embedded as permitted by YouTube’s Terms of Use.
> 

>   * Content created by Henry Wensleydale.
>   * Original content created by Lumen Learning.
> 

Why is this a big deal? Because attribution of remixed content is a bit of a mess. Actually, not a “bit” of a mess — it’s a disaster.

For example, photos are put up, and linked a dozen different ways. Here’s a [great example](<http://www.neontommy.com/news/2010/11/uc-berkeley-students-protest-after-fee-hike-approved>) of someone trying to do the right thing in a useless fashion:

> [](<http://mikecaulfield.wordpress.com/wp-content/uploads/2014/05/comprehensive_attribution_statement.png>)

This is a good attempt, but there’s no link to the original, no statement about what CC license is used. No photographer listed. And my guess is that that is largely because the decision was made to cram the attribution into the caption. Unfortunately it misses the major purposes of open content attribution — first, that I should be able to use attribution to find the original (if possible) and related work of the author/photographer. Second, that a person that wants to reuse this image has sufficient information to do their own attribution of it (and to not break any laws). The easiest way to do that is to give up the ad hoc methods of citation and come up with a more mundane but predictable approach.

Text gets even messier to cite. If I rewrite a text, for example, a worksheet on twitter in the classroom, it’s easy to get bogged down in the detail of how that was used. I’ve cited such text a dozen ways, trying to explain whether the borrowed text was written in collaboration, just borrowed — whether pieces were “used” or whether pieces were “written for”, whether it was “based on” vs. “contains material from”, what bits were under what licenses, etc. The Lumen approach to this gets _some_ of those distinctions in while not losing sight of the fact the main purpose of the statement is to provide a path to the original and a concise desciptions of the conditions of reuse. So for instance, if some of Reclaim Learning’s materials are borrowed from UMW’s Domain of One’s Own project and edited by Jim Groom, Reclaim’s Attribution might look like this:

> This page is licensed under a Creative Commons Attribution License and contains content from a variety of sources published under a variety of open licenses, including:
> 
>   * Original content by Jim Groom for Reclaim Learning
>   * Content created by Ryan Brazell and Martha Burtis for UMW’s Domain of One’s Own project, originally published at <http://docs.umwdomains.com/general/pluggin-into-rss> under a CC BY license.
>   * Data image created by Tom Woodward, originally published at <https://www.flickr.com/photos/bionicteaching/2920562020/> under a CC BY license.
>   * The Introduction to RSS video was created by Common Craft and published at <http://www.youtube.com/watch?v=0klgLsSxGsU>. This video is copyrighted and is not licensed under an open license. Embedded as permitted by YouTube’s Terms of Use.
> 

What I really like about this is two things. First, having struggled with attribution, these categories make sense — highlighting what is crucial and ignoring what is not. Second, I like that if I take this page and edit it for my own uses, I just add in the reference for the original content and put my attribution on top:

> This page is licensed under a Creative Commons Attribution License and contains content from a variety of sources published under a variety of open licenses, including:
> 
>   * Content created by Michael Caulfield
>   * Content created by Jim Groom for Reclaim Learning, originally published at <http://wiki.reclaimhosting.com/whateverurlitwas> under a CC BY license.
>   * Content created by Ryan Brazell and Martha Burtis for UMW’s Domain of One’s Own project, originally published at <http://docs.umwdomains.com/general/pluggin-into-rss> under a CC BY license.
>   * Data image created by Tom Woodward, originally published at <https://www.flickr.com/photos/bionicteaching/2920562020/> under a CC BY license.
>   * The Introduction to RSS video was created by Common Craft and published at <http://www.youtube.com/watch?v=0klgLsSxGsU>. This video is copyrighted and is not licensed under an open license. Embedded as permitted by YouTube’s Terms of Use.
> 

This follows the document around attached to the bottom of it, out of the way, but accessible. I’d go a step further on student-facing pages and make it a clickable hidden div to minimize distraction while enforcing structure, but YMMV (example of how that might look here: <http://screencast.com/t/cW9xkzwjOq5t>). For different sorts of projects, the format could vary (open data projects, for example, have particular requirements). But there would be on the site a statement of what the customized format was and how to interpret it.

As I was saying in a private conversation with Jared Stein, I’ve been waiting for the open metadata revolution for quite a number of years. Header-embedded metadata is neat to think about. But ultimately a simple endnote set of conventions would get us 90% of what we want, today. And if Google Scholar can create citation indexes out of APA and MLA citations, there’s no reason that a format like this could at least start to form the basis of a reuse tracking system.
