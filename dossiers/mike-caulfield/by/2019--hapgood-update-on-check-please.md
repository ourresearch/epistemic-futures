---
title: "Update on Check, Please!"
person: mike-caulfield
section: by
type: blog-post
year: 2019
date: 2019-03-01
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2019/03/01/update-on-check-please/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Update on Check, Please!

## Full text

Short update on the Check, Please project. 

We’re about halfway into the coding hours on this which is a bit scary. We still have some expert hours from TS Waterman at the end to solve the hard problems but right now we’re solving the easy ones. 

A couple weeks ago we put out a prototype. The prototype was for one of the three moves we wanted to showcase, and it was functional, and used the original concept of a headless Chrome instance in the background to make these things. The protoype did what good prototypes do and showed that project was possible, but there were three weak spots:

  * First, the Chrome screenshots could usually be manipulated to capture the right part of the screen (e.g. scroll down to a headline or get the correct Google result scrolled into view). But this was a bit more fragile than hoped as we tested it on a wide array of prompts.
  * Second, headless chrome was really slow on some sites. Even on speedy sites, like Google, the fire-up and retrieval would normally be a couple seconds but could stretch to much much more. We were headless chroming three sites and on the occasional call where all three went slow we’d sometimes get over 30 seconds. This didn’t happen a lot (timings were usually about 10 – 15 seconds for the entire process) but it happened enough.
  * Finally, because headless chrome is headless a lot of things needed to make the animation instructive (mouse pointers, cursors, omnibars) have to be added anyway via image manipulation.

I played with the settings, with asynchrony, with using a single persistent instance of Chrome Driver, and things got better, but it became clear that we should offload at least some problems to a caching mechanism, and where possible use PIL to draw mockups off of an HTML request rather than doing everything through screenshots. So I’m in the middle of that rebuild now, with caching and some imaging library rework. Hoping to get it reliably under 10 seconds max.
