---
title: "SIFT Toolbox Update"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-06-15
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/sift-toolbox-update
retrieved: 2026-08-13
content: full-text
notes: ""
---

# SIFT Toolbox Update

*A few simple updates*

## Full text

I added a few updates to SIFT Toolbox when I was processing the MAHA report, and they seem useful enough that I’m keeping them in. (I try to be very limited with what I add and only add stuff that helps with a wide variety of stuff). I put them at the [SIFT Toolbox site](<https://checkplease.neocities.org/>), but I’ve also added them to a [git repository](<https://gitea.com/mcaulfield/SIFT-Toolbox/src/branch/main/superprompt>) so that I can start tracking changes.

Here are the three updates:

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

## Expanded Calculations Instructions

I had some stuff about always checking calculations already, but I added some more examples of sorts of things to check to nudge it a bit:
    
    
    ## Calculations
    
    Always check calculations (ages, years passed, physics calculations, currency, interest) using javascript.
    Always check things like word counts, etc, using javascript.
    Always use javascript to get current date before making date-based claims or calculations.
    Always console.log the formula used to get a calculation and show steps in console.log.

## Trends instructions

I add some explicit guidance on trends based claims that pushes to always check just before and after.
    
    
    ## Claims about patterns in a specific time-period
    
    Always check how those patterns compared to what was before
    Always check how those patterns compared to what was after
    If a claim about a current issue, be particularly sure to look at what the current trend looks like as close to today as possible
    Be aware a study's publication date isn't necessarily indicative of the date of the data studied

## Denominator awareness
    
    
    ## When computing ratios and percentages
    
    Be very clear about what sort of things are in the denominator, and what sort of things are in the numerator. 
    For example, if 1% of skydivers died, was the denominator all people who have skydived at least once, was it people in the U.S. or worldwide, was it over the past decade or in the year 2016? Did they all die from skydiving?
    

Again, I try to limit these because every instruction added increases the risk of Claude forgetting something else (and also if you have the $20 account, every word counts against your rate limit). But these seemed really helpful more generally and so they are in. 

Check out the [SIFT Toolbox site](<https://checkplease.neocities.org/>) or [git repository](<https://gitea.com/mcaulfield/SIFT-Toolbox/src/branch/main/superprompt>). 

* * *

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
