---
title: "How Prompting Is Evolving"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-07-03
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/how-prompting-is-evolving
retrieved: 2026-08-13
content: full-text
notes: ""
---

# How Prompting Is Evolving

*If you're a good teacher you'll soon be a good prompter too*

## Full text

My prompting style has always felt miles away from what people recommend. Sure, I have a little role-based stuff in [Deep Background](<http://checkplease.neocities.org/>), but most of my 3500 words look like this:
    
    
    ## Sources Table Method
    When instructed to create a "sources table" about a subject:
    
    1. Find strong links with a fact-checking ethic and conflicting information on the chosen question or topic.
    2. Present results in a markdown table with structure: "Source | Description of position on issue | Link"
    3. Format links as [link](url)
    4. Search for additional links with conflicting information and update the table
    5. Add columns for Initial Usefulness Rating and specificity of claims (date? place? reference? testimony?)
    6. When prompted for "another round," find if possible at least:
       - One source that conflicts with the majority view
       - One source that supports the majority view
       - One source with a completely different answer
       - Update the table with these new sources
       - A pattern where low quality sources say one thing and high another is worth noting

Then I came across this recent video, and I think maybe my approach isn’t as weird as I thought. Broadly, the previous approaches to prompting — which were heavily based on role definition — are getting outdated as context windows grow and LLMs become better at following complex multi-stage instructions and adhering to desired output formats. 

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

I think of this as part of the “weird computer” shift in thinking about these systems. Rather than thinking of the target for the prompt as a linguistic model of conversational partner, it’s now a bucket of various capabilities that you can get to interact in weird ways. You can pull context in via search, have it analyzed in a table, then have the LLM look at the table, critique it with assessment criteria, then run supplemental searches based on that assessment. You can put a bunch of heuristics for it to make decisions. You can ask it to shell out and make sure that all figures are double-checked in Javascript:
    
    
    ## Calculations
    
    Always check calculations (ages, years passed, physics calculations, currency, interest) using javascript.
    Always check things like word counts, etc, using javascript.
    Always use javascript to get current date before making date-based claims or calculations.
    Always console.log the formula used to get a calculation and show steps in console.log.

When asking it to analyze evidence, you can note that people saying they did something for a given reason isn’t always sufficient proof of something:
    
    
    ### People stating their motives
    
    People are experts in knowing their motives but they don't always tell the whole truth, often giving what seem rational reasons for actions that are actually motivated by self-interest, hatred, or the like. For a stated motivation to be fully believed it must be consistent with personal history and behavior, not just statements.

I don’t think that this is a skill that we’ll be teaching most students. But I do think there is something interesting happening here. One theory about these systems has been as they got better there would be less need for complex prompts — and that’s true! You can get a much better answer nowadays by just asking a straight question than you used to. 

The other theory was that prompting would become more and more an art as these systems got more capable. And that’s also true! As the systems are able to process more complex instruction sets, people who have, for instance, taught people critical reasoning for decades and can break that down for students suddenly have an advantage. They can now break it down for a machine.

Both things are true at once — simpler usage for the public, and more benefits accruing to people who understand and can explain how to apply complex analytical models. 

If you’re a teacher and you’ve been doing simple prompts, that made sense in the past. But as the capabilities increase, it might be worth your while thinking of your prompt as a little mini-textbook on how to do something, complete with describing tool use and outputs, and having stages where the model grades its own work with the rubrics you’ve developed. Get a paid version on one of the platforms and go a bit wild. 

It’s a great time to have an ability to explain things in natural language, which is to say it’s a great time to be a teacher. Take advantage of that!

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
