---
title: "Advanced Prompting: \"Data-Paging\" in LLMs"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-07-04
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/advanced-prompting-pseudo-data-paging
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Advanced Prompting: "Data-Paging" in LLMs

*Making up pretend code to to solve the real problem of having to pull data a bit at a time*

## Full text

One of the problems you hit with LLMs grabbing data, whether search results or something else, is that you can’t get everything in one go. Or at least it’s hard. You can push Claude or ChatGPT to make a lot of searches, but if you try to do them all in one go a variety of suboptimal things happen, the most common being that as the size of the task scales up, the size of the effort the LLM applies per turn stays constant.

This is particularly the case when you need a _lot_ of results, as I did for [this little project](<https://claude.ai/public/artifacts/23117054-2b3a-4088-b680-2adacba1fb98>):1

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

[](<https://substackcdn.com/image/fetch/$s_!RjwK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9f7bb9e-1cd7-4c77-ac4c-a303e11c4a28_1465x1299.png>)

Check it out [it’s pretty cool](<https://claude.ai/public/artifacts/23117054-2b3a-4088-b680-2adacba1fb98>).

Anyway, to have it pull all the data I need while I get to be as lazy as possible I used a little pseudo-code technique I call “LLM paging” where you embed a command in the prompt that can later be used to iterate over a range of data.   
  
The way it works is you define a process, like this:
    
    
    Search for cultural events in Europe happening week {#1} of July, and put them in a table with the date a description and a link. Use provided tips below. 

  
Then define a command that iterates like so:
    
    
    ## Template hotkey="next" 
    Replace {#1} in instructions with the next number (e.g. week 1 becomes week 2, week 2 becomes week 3)

The prompt will start by searching week one. When it’s done, type in “next” and it will search week two. Type next again and it will search week three.

In the weird world of LLMs I have to be quite clear — this is all pseudo-code. There is no native language I am tapping into here. I made all these attributes up, I made the format up. There is no “hotkey” function in Claude, I just want the system to sort of act like a hotkey tool. Why is the week number in braces? Because sometimes variables go in braces in templating code, so maybe that will make clearer what I want. If I put it in braces, it will probably get it into the right mindset. But you could do it a completely different way! It’s all made up!

Still, it works really well. In this case, we use this technique to pull data for four weeks in June by just typing “next” three times. I show that technique below. (Apologies for the poor quality of the video — I did a longer more polished thing, then realized it was too long for the specific task, so just did this one to replace it quickly. It shows the behavior, which is the main thing!)

If you watch the video you will see that there’s no way that Claude would have ever pulled in the amount of table rows here if we’d asked for all of June at once. It would have skimped more on the searches, and we would have ended up with about one week’s worth of events but just spread over a month.

I think in the near future we will get LLMs that are more comfortable doing these lengthy loops without stopping for human feedback, but for the time being this pseudo-code can tide you over. 

Here is the code for grabbing events:2
    
    
    # Base Instructions 
    
    Search for cultural events in Europe happening week {#1} of July, and put them in a table with the date a description and a link. Use provided tips below. 
    
    There should be at least 34. Categories might include music festivals, cultural celebrations, specialty/quirky events, folkloric stuff, pride events, arts and performance, food and lifestyle, maritime and aviation. Check table for any duplicate entries and remove. 
    
    ## Tips on date searching 
    When searching for events in certain date ranges, it is helpful to use "OR" logic with a series of specific dates, e.g. instead of searching for "july 3-july 9" search "july 3" OR "july 4" OR "jul 5" etc. within the date range. 
    
    Be aware of linguistic differences when searching dates, both language and formats. 
    
    ## Tips on searching 
    Remember the specific links you find talking about each festival, you will use these links later in the table.
    
    # Templates (run based on certain phrases/"hotkeys") 
    
    ## Template hotkey="double check" 
    Look at each entry in the table and double-check dates, location, and links, and report any errors 
    
    ## Template hotkey="next" 
    Replace {#1} in instructions with the next number (e.g. week 1 becomes week 2, week 2 becomes week 3)
    
    

To make the chart I put the markdown produced by the pseudo-code into a project, and then just asked it to make the chart using the project files. Obviously I don’t provide support for people trying to do this, but you’re welcome to share anything you make with it in the comments.

1

I know people are going to find errors in the chart — there are some! I think in general though the people who rush to “aha-ism” over small errors on goofy little proof of concepts vastly underestimate the level of error they have in their own work — just something to think about.

2

As always, if you run any prompting code I share in an unpaid version of an LLM please understand it is likely not to work. The reason it won’t work will almost always be you are using a free version, or not using a reasoning model on a paid version.
