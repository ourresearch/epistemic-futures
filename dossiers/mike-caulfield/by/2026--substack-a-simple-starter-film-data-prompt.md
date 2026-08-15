---
title: "A simple starter film data prompt: Calculating on-screen film deaths in 1998"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-06-05
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/a-simple-starter-film-data-prompt
retrieved: 2026-08-13
content: full-text
notes: ""
---

# A simple starter film data prompt: Calculating on-screen film deaths in 1998

*A simple prompt to understand some basic LLMs + data + interface concepts*

## Full text

I didn’t mean for the last post about [Plot.fyi](<https://plot.fyi/>) to be a tutorial about how to create an enriched dataset using Claude Code. I can’t really show you how to build Plot.fyi, because building something like that is something that happens over time. I have at this point about two dozen helper scripts in Python to help with the processing of that site, for example.

That said, I realize that people who haven’t done a lot of LLM-based data-processing may have trouble even realizing what the work _looks_ like. So I put together a little prompt for Claude code that demonstrates some of the major concepts of building a data processing and visualization app. It also could be suitable to use in a class or workshop on learning how to prompt. 

Here it is:

  1. _Step one: Take this URL and go through the months of 1998 to build a list of films. Iterate the URL by switching out the month and get january - december: https://www.boxofficemojo.com/month/may/1998/?ref_=bo_ml_table_31_

  2.  _Step two: We’re going to create a JSON file. For each unique film create a JSON record in that JSON file that has the essentials of the film, including cast and crew, any awards, etc.  using SPARQL against Wikidata to enrich the records. Include release month. _

  3. _Step three: For every film in the record, go through and estimate how many people died in the film. Try to do this with your internal knowledge. If that is impossible, resort to search. Add a field to the JSON called deaths that shows the number of deaths for each film._

  4. _Step four: Use the JSON to create an HTML page that shows a cumulative line graph showing the month by month “body count” in all films that debuted each month combined. When you click on that data point the HTML page should show you a breakdown of the estimated deaths in each film._

  5. _Step five: Spin up a server on localhost and give me the URL to view my page._

If you’ve done no Claude Code work before, this probably shouldn’t be your first app. At the very least you’re going to have to learn how to set your Claude Code permissions so that you have safe operation without having to babysit every permission request. If you put this in and find yourself having to approve a request every few seconds, find an introduction to Claude Code and work through the first bit of it, then come back to this.1

After you run the above prompt, you should have a [page like this](<https://1998moviebodycount.netlify.app/>), hopefully, though it may take up to a half-hour for it to process.

[](<https://substackcdn.com/image/fetch/$s_!-OqC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F343b1527-cbcf-4525-9bc7-a1bd2ed926a2_1149x861.png>)That big spike is a Disney film — can you guess which one? And is it accurate?

But the important piece that this prompt is not a magic set of words. The net step is to understand all the pieces we used here and the general approach. For instance:

**One:** We start by creating a dataset, with clear inclusion rules (Had substantial box office returns in 1998).

**Two:** We then fetch that dataset. That’s our data core. 

**Three:** We then turn to a second data source to enrich the core, in this case Wikidata. We do this using SPARQL to get that data and a format called JSON to store it. 

You will need to research both of these things (Wikidata and JSON) and learn what they are, as well as understand the concept of enrichment: get your core data and then use that core as a list that you layer data from other sources onto. (Enrichment through external data).

[](<https://substackcdn.com/image/fetch/$s_!rpF6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43da1a07-293e-4faf-aa2f-307de3bc28ea_1144x298.png>)

**Four:** We then use a different enrichment method. In this case we ask the LLM to make a judgment on each record, and to estimate the deaths in the film. We tell it to use search (which is expensive) only if necessary, because we are just goofing off here. We’ll check its work when we’re done. We don’t need perfect here but we do need to be in the right ballpark each month. We also ask it to make a computation. (Enrichment through LLM).

**Five:** We then create a visualization using the JSON, and describe its behavior. We ask Claude to spin up a little web server so we can look at it, since sometimes JSON-based web visualizations don’t work if you just open it as a file.

**Six:** We check it and see if it looks right. 

**Seven:** When we’ve done the proper amount of checking for our purpose, we put it up. For small projects, I use a free account on Netlify, or my $5 a month account on neocities. For larger projects I use Cloudflare pages. This one is on Netlify. [Check it out](<https://1998moviebodycount.netlify.app/>).

## Keep going

You think at this point you’ve just built a graph. You haven’t. You’ve built a dataset with a graph on top. You now have a 500KB dataset of almost 300 films from 1998. What are you going to do with it?

[](<https://substackcdn.com/image/fetch/$s_!heyL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F614b9b6d-3cd8-424f-aa68-9933d3303a89_1332x610.png>)

First, you may want to poke at your data. People often ask “But is it accurate?” and my response is “accurate for what?” Having the data presented visually lets you develop the questions that let you poke at the accuracy of the data in the right places. For instance, almost _half_ of the increase here comes from the claim that _Mulan_ has 2,000 deaths. Seeing this like this you’d want to push on that. You might look for broad patterns — for instance the low confidence around films with war scenes and punt all such films to human review (i.e. you!). 

A lot of people think getting the data in this format and finding errors is a sign of a bad process. This misunderstands how things work. You get things into this format so you can a) think about which kinds of errors matter to you, and b) find and correct them. The quick visualization process helps you find the important questions and the relevant data needed. You look at the graph and drill down to the detail. Now perhaps your question is not “Is the data in my graph accurate?” but rather “Is the character Mulan the greatest killer in all of 90s cinema?” That’s going to require you tighten up the data in some places and allow you to leave it loose in others. 

Or maybe another question sparks your interest. Maybe you ask for a visualization of deaths in animated films compared to non-animated, or family films compared to non-family films. Follow the same pattern. Enrich the dataset with the new attribute (family/non-family). Create a visualization to explore it. Spin up a local webserver to look at it. Each question you explore builds out and refines your dataset. And you can go a different direction entirely — have it layer in information from the Open Movie Database (omdb), links to reviews, or tags about whether violence is seen to solve problems in the film, make it worse, or is ambiguous. Have it write a sentence long defense of the decision for you to spot check and evaluate. If the decisions are bad, reformulate the decision criteria or adjust effort level and rerun.

Hopefully this will give people a starting point to what data processing, enrichment, and eventual visualization looks like in a workflow. 

If you want to use this as part of a two to three hour workshop on how to use Claude Code for visualization, be my guest. If you’d like me to lead a workshop for you on it to your staff or faculty I do do a limited number of workshops per year for a keynote-sized fee, and if you have recently adopted a coding agent I can show you how to do this.

## Notes

I check the data on the apps I build for myself, but I have not checked this data. That’s something you can absolutely do if you want, but that would turn this thirty minute morning post into many more hours of effort,2 and I’m really only showing how to do this as a favor to people. But if you wanted to improve this data, I think the first step would be to take a pass at everything with a low confidence rating and ask the LLM to use the search tool to re-evaluate.

For clarity’s sake I made the prompt as simple as possible. That makes it easier to see the core structure but is also means there’s less direction to it on how to implement it, so it’s going to produce very different things sometimes. The way to get it to produce what you want is to a) critique what it produces if it is not suited to your needs and have it fix it, and b) learn more about this process over time so you can specify the methods you would like it to use and be more specific about the output.

There is no warranty made or implied about this prompt, and there is no support for it offered. 

1

I’ll note that you’ll be using a language called SPARQL which has a lot of syntax that Code will flag as ‘obfuscation’.

2

If you looked at that sentence and said “Aha! See, this does not save time because you still have to check things!” please hit the unsubscribe button. You’ve cooked your brain reading Bluesky or something. You have apparently never done a data project that required precision, because you have no idea of what precision normally costs. I’m done having conversations about fact-checking with people who think that in the pre-AI days of yore things were easier. They were easier if you never did the work.
