---
title: "Differences in link hallucination and source comprehension across different large language models"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-06-01
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/differences-in-link-hallucination
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Differences in link hallucination and source comprehension across different large language models

*I've been waiting for someone else to talk about this, but I guess it will be me*

## Full text

As most of you all know, I built [SIFT Toolbox](<https://checkplease.neocities.org/>) as a contextualization engine, initially on ChatGPT but started developing on top of Claude after seeing better results there when they rolled out their paid version with search. Also many of you also know, I started to get the system to do pretty striking things, providing AI-generated professional-level “context reports” on claims, artifacts, and quotes. 

[](<https://substackcdn.com/image/fetch/$s_!zzDS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24120e34-598e-4acd-9f16-2fc4c84d8561_746x610.png>)An AI-generated (SIFT Toolbox) fact-check which outperforms a Snopes article on the question of whether the snow in Wizard of Oz was “made of asbestos”, surfacing evidence that Snopes did not, and correctly evaluating its weight as direct witness testimony accepted by film historians.

Initially I thought as the different models evolved they’d all match the performance I was seeing on Claude. But we’re a couple releases down the road and that hasn’t happened. There is, in my experience, a very real gap between some of the models and others that no one is talking about, and no one seems to be testing with any rigor.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

So I thought I’d try a real world fact-checking example of some complexity across different platforms/models and show this relatively prominent split in their capabilities: their ability to cite and summarize real-world documents accurately when forced to do so. I’m hoping that one of two things happen. Either:

  * People look at my prompt (available [here](<https://checkplease.neocities.org/>)), tell me why it's malfunctioning, and explain to me how to get the platforms that are hallucinating or misdescribing links to better comprehend documents and produce real links instead, or 

  * If it turns out the cause is that certain models are just more prolific link hallucinators and source mis-summarizers, maybe we start taking that more seriously. Why are we talking about “graduate and PhD-level intelligence” in these systems if they can’t find and verify relevant links — even directly after a search?

  * As my readers probably know — I’m not an AI-doomer, and I’m relatively optimistic about AI. So some stuff below, I am sure, will look like AI-mockery. But it’s far from it. I’m driven by the fact that even where these systems are malfunctioning they seem like they would be relatively easily fixable — but I’m not even sure if the people working on them know the problem.

## A real world example

One of the reasons that I think we don’t talk enough about link hallucination and source interpretation is that the tests people put models through are not very challenging or authentic. 

So let’s take a real world example. I’m sorry this is going to take a bit to set up, but one of my points here is that if you are going to evaluate how these technologies handle complexity you are going to have to develop complex understandings about things. You can’t just look at answers and go — yeah, that looks right. 

Today's example: In the “MAHA Report” that RFK Jr.’s HHS just put out, this bullet point jumped out at me:

[](<https://substackcdn.com/image/fetch/$s_!xnHV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3261bec5-bb6a-4c93-9cc2-fc3e96a23a06_933x149.png>)

That’s sourced to the following studies:

[](<https://substackcdn.com/image/fetch/$s_!k0cs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2668774a-6973-4898-8f08-8235079a63db_1118x188.png>)

That led me to investigate the second claim — that there were no long-term benefits shown to stimulants in one of the only long term trials done. 

Here’s what I found: using the study cited in this way is pretty severe misrepresentation of research. 

The study initially began as a 14 month randomized controlled trial (great!) that had four arms: community care (what ADHD people got without the intervention, which, crucially, was usually stimulants), a medication only arm (which used increased doses of stimulant and medical supervision to ensure better adherence to a daily taking of pills), a behavioral arm (that used behavioral approaches), and a combined approach (medication plus behavioral therapy). What the initial study found was that the thing that worked best for these elementary school students was higher, more frequent doses of stimulant under medical supervision to ensure adherence. This was true compared to students in the community care group, who, I will repeat, _were also receiving medication_ but in a less rigid dosing structure at smaller dosages. 

After 14 months the study ended, and those medical/behavioral supports disappeared for the intervention arms. At 24 months there was a follow-up that showed something hopeful. Even with those supports removed, the medication management arm was still doing better. Causality is hard, but it looks like some of the rigid dosing persisted even after the supports were gone. By 36 months, however all the benefits of the earlier rigid protocols were gone. And that included adherence to prescribed medication — there was little difference by this point between groups in the study in terms of how regularly they were taking their stimulants, and, probably not coincidentally, no difference in those group’s symptoms. 

This is not a terribly surprising finding. For instance, imagine a study that takes people that have been prescribed 10 minutes of stretching a day to help with chronic hip pain. One group gets a trainer that comes into their house once a day and walks them through the stretching exercises. The other is just told to do the exercises on their own. At the end of 14 months we test people for hip pain and check their daily routine. What we find is that the in-call physical therapist group has much less hip pain, and does their stretches more regularly. Stretching works and personal trainers make it work even better.

We then pack up the study — good luck with the hip pain, people, we’re out of here. No more trainers. 

Twenty-four months after the study start we survey again. And this is interesting. Even though there is no trainer anymore, the group that had access to one for the first 14 months is still doing better. They do their stretches more and they have less hip pain. This is promising! Maybe a bit of structure at the beginning forms good habits?

But at 36 months, that falls apart. The group that had the trainer at the beginning isn’t doing its stretches any more frequently than the group that didn’t. Both groups have the same level of hip pain. The effect of having a trainer at the beginning has dissipated.

So what does this study show? Well, if you are the HHS report, it shows that _stretching_ seems to only help with hip pain for about 14 months, after which _stretching_ does not help with hip pain at all. 

Which makes no sense, right? 

The follow-ups don’t test whether stimulants work. They aren’t designed to. They might have some hints in there. You could speculate. But the only finding of that sort that is fully supportable at the RCT-level that made the study noteworthy is the original 14-month finding: when schoolchildren have the equivalent of a trainer making sure they adhere to their stimulant regimen (at a higher intensity) they do better, for as long as 14 months, and for some time after the trainer is pulled away. The follow-ups show that if you take away the “trainer” and let people self-dose at lower frequencies they eventually do about the same as people who never had the trainer. The “trial” part of the “only long-term trial” is the 14 month part. The other stuff is useful, but it’s just another observational study. 

I’m not saying the benefits of long term stimulant use are clear. They aren’t clear, and that’s largely because there’s no such thing as running a ten year randomized control study, for precisely the reasons described above. They seem clear to a lot of individual people who use them, which is what I’d go by in the interim. But saying it’s hard to prove something and saying that you have something that proves a negative are two very different things. 

And that’s the heart of the issue. When the report says “the only long-term trial found exclusively short-term (14-month) behavior benefits, which were not found at 3 years” one might assume it is talking about a _three-year_ trial that showed no benefits. No such trial exists. The trial lasted 14 months.

## Can LLMs see this?

So this is a question of moderate complexity, but it’s exactly the sort of thing that LLMs have to understand to be useful to sense-making. 

So let’s try this systematically. My test will be this — I will give the LLMs the two screenshots together (paragraph + footnotes) and ask if the declining impact of _medication_ claim is supported by the cite. Here’s the image if you want to replicate yourself:

[](<https://substackcdn.com/image/fetch/$s_!HXEf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d85ad74-7ee7-4ddf-b9e1-236ed042df90_1905x590.png>)

And here’s me asking:

[](<https://substackcdn.com/image/fetch/$s_!y3qj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43c79f4f-a9c4-4a2d-9e12-378615d5d0e5_738x335.png>)

I’ll start by running it without loading SIFT Toolbox. Here are the results of asking whether the cited study shows that stimulants aren't effective in treating ADHD after 14 months. I’ll pull the best summary paragraph out.

### **Claude Sonnet 3.7 (FAIL):**

> The passage you shared appears to be generally accurate in stating that the MTA study found only short-term (14-month) behavior benefits that were not maintained at longer follow-up periods (3, 5, 8, and 14 years). The MTA findings do suggest that while stimulant medications can be effective in the short term, their long-term impact on functional outcomes like grades, relationships, and achievement was not demonstrably better than other treatments when examined years later.

[full chat](<https://claude.ai/share/65e0de1c-ec7d-4338-a6f3-a565fa0c0b77>)

### **Claude Sonnet 4 (FAIL):**

> Based on the text you've shared, yes - according to this source, the MTA (Multimodal Treatment Study of Attention-Deficit/Hyperactivity Disorder) trial found that stimulants had only short-term benefits.

[full chat](<https://claude.ai/share/e277d19f-b4c4-4ca9-a7da-8e4bc63bb964>)

### **Claude Sonnet Opus (FAIL):**

> So yes, according to this source, the MTA trial found that stimulants had only short-term benefits (14 months) with no long-term benefits observed at the 3-year follow-up and beyond.

[full chat](<https://claude.ai/share/bf456df2-ae5a-44ec-b5be-68fd7b06bf51>)

Notably even though I had the web search setting on for all of these (and the highest level paid account) Claude couldn’t be bothered here to do any web searching, at least any that was visible to me.

### **Gemini 2.5 (FAIL)**

Onto Gemini 2.5, which manages to do _worse_ and for reasons unexplained formulates its answer as a press release: 

> **Washington D.C.** \- A landmark study on the treatment of Attention-Deficit/Hyperactivity Disorder (ADHD), the Multimodal Treatment Study of Children with ADHD (MTA), found that the initial advantages of stimulant medication diminished over a three-year period. The follow-up study, authored by P.S. Jensen and colleagues in 2007 and cited in the provided text, reported that while stimulants offered significant short-term benefits, these effects were not sustained over the long term when compared to other treatment modalities or community care.

[Full chat](<https://g.co/gemini/share/26503d0ae733>)

### **ChatGPT o3 (Good, actually?)**

I mentioned this would be an informal test but fair in the sense I came up with a formulation of what I thought was a clear question and task, and would apply it across platforms and report what I found as I found it, whether good or bad. I’m typing the results into this post as I run each test. And the o3 test has just surprised me — it’s _fairly good_.

Here’s the summary:

> ### So did the MTA prove that stimulants offer **only** short-term benefit?
> 
>   * **Yes, in a narrow sense:**  
>  The _randomised_ advantage of the medication arms was big at 14 months and had vanished by 3 years.
> 
>   * **No, in a broader sense:**
> 
>     * Children who remained consistently medicated after the trial tended to have lower symptom ratings than those who did not, even though the study was no longer randomised.
> 
>     * The disappearance of group differences does not prove that stimulants cease to work; it shows that real-world patterns of starting, stopping and switching treatments blurred the original contrasts.
> 
>     * The trial was not powered to detect small effects on grades or long-term achievement, and it used immediate-release methylphenidate three times daily (long-acting formulations were not yet available).
> 
> 

It could be better — it’s a major miss that it doesn’t mention here that the control at follow-up had similar medication rates as the medication intervention arms. And the first bullet is wrong — the students that took medication actually had slightly _worse_ outcomes, but an additional analysis showed this was likely self-selection, and that the students who increased their medication usage did better relative to the time before they increased it. (It’s roughly our hip analogy — people with hip pain were more likely to stick with or increase their stretching routine.)

But a glass of cool water in the desert compared to these other results.

It also created this helpful chart:

[](<https://substackcdn.com/image/fetch/$s_!Y9of!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c05a4a3-45b3-44ee-9186-8437fc604107_1397x676.png>)

I’m actually impressed here!

### ChatGPT 4.5 Research Preview (FAIL)

ChatGPT 4.5 is supposed to be the future of the non-reasoning models, and here it does a bellyflop. It doesn’t seem to have executed even a real-time search. Not sure if that is how it works generally in 4.5 but it looks like I wasted one of the ten GPT 4.5 queries I get a month for $20 on having the world’s biggest model just restate the paragraph. 

> Yes, the MTA trial cited here found that stimulant medications provided only short-term (14-month) behavior benefits, which were no longer evident at 3 years or beyond. Specifically, at 3, 5, 8, and 14 years, no sustained benefits in grades, relationships, achievement, behavior, or other measures were observed.

I couldn’t afford another 4.5 query, but just to check if it was all just a misunderstanding where it didn’t realize I wanted it to do external verification, I repeated the query on 4.1 with the follow up seem below — “please use search to verify”. It searched and then bellyflopped again:

[](<https://substackcdn.com/image/fetch/$s_!dxzh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6b8b193-0983-45d3-bb45-4c8a3de7a569_1104x249.png>)

The cherry on top here is the PubMed study it cites is also the _wrong study_ — it’s on growth rates not ADHD behavior. Maybe this was the model the CDC used to write the thing; it's certainly bad enough at this to be a prime suspect.

### Model Round-Up

If I am being harsh here it’s because we constantly hear — based on ridiculously dumb benchmarks — that all these models are performing at “graduate level” of one sort or another. They are not, at least out of the box like this. Imagine giving a medical school student this question, and they say — yes the thing that says _in the actual conclusion_ that the lack of sustained differences is probably due to people _stopping their medication_ is proof that _medication doesn’t work_ (scroll to bottom of this screenshot to see). Never mind that in the results it states quite clearly that all groups saw improvement over baseline.

[](<https://substackcdn.com/image/fetch/$s_!7bqt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5004c2cc-9039-4f1a-bade-57a9326ff926_1110x953.png>)

That said, o3 is definitely the bright light here, which I did not expect.

### SIFT Toolbox

OK, let’s try [SIFT Toolbox](<https://checkplease.neocities.org/>) now. (If you’re coming here new to this, SIFT Toolbox is a 3,000 word prompt that turns models into a contextualization engine — or, if you prefer the term, a fact-checking engine).

What I’m curious to find out is whether the difference I see in these different models around link hallucination when I use SIFT Toolbox might be my imagination, and the way I’m going to find out is coming up with a rigid method that I will apply across all consistently and mechanically. This should eliminate the bias where my familiarity with Claude makes me more prone to guide it past its foibles rather than throw up my hands in frustration, a throwing up of hands I do a lot with ChatGPT and Gemini. As before, I’ll run each test in sequence and place the results here as I get them, no filter.

Here’s my evaluation sequence:

  * Load SIFT Toolbox prompting layer

  * Ask initial question (Did the MTA trial cited here find that stimulants had only a short term benefit?) with screenshot

  * If asked a clarifying question about what I want to check I can clarify, but only respond with choices it gives me. If it just offers vague choices my response will be “all of it”.

  * Type and enter “sources table: what the MTA study found”

  * Type “another round”

  * Type “another round”

  * Type “Read the Room”

  * Type “sources table”

  * Type “Produce a context report that helps people evaluate the statement ‘the only long-term trial found exclusively short-term (14-month) behavior benefits, which were not found at 3 years’”

Because a model that gets everything wrong but cites real pages shouldn't be rewarded, the evaluation will be based on four factors. Three will test the quality of the answer. Then the last will subtract points from that score for each hallucinated link in the session. 

Here is the rubric, which is all or nothing on each element for simplicity. Since at a granular level interpretations can be disputed (and I could be wrong!) I’m sticking to very high-level things:

  1. Correctly stating in the core context section of the context report that most researchers would say the follow-up studies can’t speak to medication effectiveness (50 points)

  2. Correctly noting that by the time of the follow-up who was taking medication didn’t match up with initial group assignment (or similar) (50 points)

  3. Correctly noting that this study is often misrepresented by anti-medication and anti-psychiatry advocates (or similar). (50 points)

  4. Subtract 20 for each link that is hallucinated (number * -20)

Ok, let’s do this. 

### Gemini 2.5

Here’s the core context from Gemini 2.5:

> ## Core Context
> 
>   * The statement is presented as a key finding from the NIMH's Multimodal Treatment Study of ADHD (MTA), the largest long-term study on the topic, to argue that stimulant medications are ineffective in the long run ([Swanson, J.M. et al., 2017](<https://pubmed.ncbi.nlm.nih.gov/28117904/>)).
> 
>   * The MTA study did find that at 14 months, a carefully managed medication strategy was significantly superior to behavioral therapy or typical community care for reducing core ADHD symptoms ([NIMH](<https://www.google.com/search?q=https://www.nimh.nih.gov/news/science-news/2008/treatment-of-adhd>)).
> 
>   * The claim is factually correct that by the 3-year follow-up, the _statistical superiority_ of the original medication group had disappeared; the different treatment groups were no longer measurably different on core ADHD symptoms ([Jensen, P. S., et al., 2007](<https://pubmed.ncbi.nlm.nih.gov/17667478/>)).
> 
>   * This "fading" of benefits is highly debated. Mainstream interpretation suggests it is not because the drugs stopped working, but because the study became uncontrolled ("naturalistic"), with participants changing or stopping their treatments, making the original groups meaningless for comparison ([ADDitude](<https://www.additudemag.com/latest-mta-results-putting-adhd-treatment-data-in-context/>)).
> 
>   * Later follow-ups at 8 and 16 years confirmed this lack of long-term advantage for the original medication groups and found no association between medication use and better functional outcomes (e.g., grades, relationships), while noting a link to minor height suppression ([Molina et al., 2009](<https://www.google.com/search?q=https://www.jaacap.org/article/S0890-8567\(09\)60003-8/fulltext>)).
> 
>   * Major reviews of the entire field conclude that the overall quality of evidence for long-term ADHD medication benefits is "very low," meaning the MTA's findings are part of a broader landscape of scientific uncertainty ([The Lancet Psychiatry](<https://www.google.com/search?q=https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366\(17\)30265-4/fulltext>)).
> 
> 

OK, first let’s look at this holistically, and then we will score.

It’s better than the result that doesn't use Toolbox by a mile. The first three bullets are near perfect. The fourth bullet calls the meaning of the decline highly debated which implies a debate — and there really is not among experts. It does correctly identify the mainstream view — which is to say the view that understands what the study methodology can prove and what it can’t. A bit gullible here, but not bad.

In my opinion, the later “follow-ups” bullet misrepresents the study, which couldn’t really make that observation (again, for methodological reasons). If you think about our stretching analogy, for example, once the initial study is over you may find that people that stretch daily years later have more hip pain. But that’s possibly because people whose hip pain goes away or is less bothersome are less invested in stretching. The same is true with observational studies like this. But the study, while careful in its conclusions section does wander into speculation in the discussion section; I think the key here is that the study does not “confirm” this, but rather speculates this in the discussion section, which is a fundamental difference on multiple levels.

On the scoring, I am giving this 100 points based on portions one and two being addressed by bullet four in the response:

  1. **Correctly stating in the core context section of the context report that most researchers would say the follow-up studies can’t speak to medication effectiveness (50 points)**

  2. **Correctly noting that by the time of the follow-up who was taking medication didn’t match up with initial group assignment (or similar) (50 points)**

  3. Correctly noting that this study is often misrepresented by anti-medication and anti-psychiatry advocates. (50 points)

Now we get to the bad part for Gemini. Let’s count the amount of hallucinated links. This won’t be perfect. What I do for my method is click each link and make sure the linked document has the same author and/or subject described. I’m pretty lenient on details. If, as Gemini sometimes does, it provides a link that is a search for the paper cited, 

<https://www.google.com/search?q=https://childmind.org/article/what-the-mta-study-does-and-doesnt-say-about-adhd-treatment/>

I say it is not hallucinated if there is a document that largely matches the description in the top three results, as here.

[](<https://substackcdn.com/image/fetch/$s_!paGB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc802a367-4a78-487e-8e95-0ff3a86a0d1e_1892x922.png>)

Keep in mind that these are hallucinated _links_ not necessarily hallucinated documents. for instance this source mentioned in a sources table absolutely exists:

> Journal of Child Psychology and Psychiatry (Swanson, et al. 2017)

However the link provided links to this paper on dentistry:

[](<https://substackcdn.com/image/fetch/$s_!EeXP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbff18af-434d-4dd4-82ee-ec22604cd7de_1156x479.png>)

That counts as a hallucinated link. I would love to know how many of the hallucinated links are also hallucinated documents, but you would have to pay me to dig into that, it would just take way too long. For now, a link that goes nowhere or a link that is misdescribed counts as bad — because it is. It’s really bad, and the inability to provide a reliable set of links at a level the average intern could hit should absolutely undermine our faith in a model. The reason I set it at -20 per bad link is I think it is fair that eight bad links should wipe out a perfect answer. This is the web. You have to do links right.

Alright, let's go…

Bad links:

  * https://www.google.com/search?q=https://www.nimh.nih.gov/news/science-news/2008/treatment-of-adhd

  * https://www.jaacap.org/article/S0890-8567(09)60003-8/fulltext

  * https://www.psychiatrictimes.com/view/cme-revisiting-multimodal-treatment-study-children-adhd-20-years-later

  * https://pubmed.ncbi.nlm.nih.gov/28117904/

  * https://www.google.com/search?q=https://joannamoncrieff.com/2014/05/26/long-term-effects-of-adhd-drugs/

  * https://www.researchgate.net/publication/225301131_Quality_of_life_in_the_multimodal_treatment_study_of_ADHD_MTA_Does_treatment_improve_the_quality_of_life_for_children_with_ADHD

  * https://www.tandfonline.com/doi/abs/10.1080/15374410802575971

  * https://psycnet.apa.org/record/2004-13655-008

  * https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366(17)30265-4/fulltext

That’s nine hallucinated links, for a total deduction of 180 points, giving Gemini -80 points.

I do feel a bit bad, as Gemini does here what it always does with links — it starts off well and for the first 10 or so links it acts perfectly. Then it stumbles a bit with a link here and there in the middle, then by the end it’s just making half the new links up entirely. On the other hand, the fact that Gemini repeats this pattern over and over makes me think this problem is fixable. 

But for now — negative 80 points.

If you want to check my judgment here is the [chat session](<https://g.co/gemini/share/a04b15acbe8b>).

### ChatGPT 4.1

For the stuff I do, ChatGPT 4.1 has proved to be absolute garbage. If you look at the [chat log](<https://chatgpt.com/share/683b8440-58d4-8004-a3af-fcb3800377a0>) and compare it to any other model you’ll see why: After the first round, it simply doesn’t follow instructions. At all. 

Earlier versions worked. When I asked for a sources table it followed the defined format for a sources table. When I asked for another round, it found the instructions for another round. Now it acts great for the first round but after that just makes it up as it goes along as if it had no instructions at all.

I’m not the only one noticing it no longer follows instructions well. I don’t know why they ruined its ability to follow complex instruction sets. But it seems like that’s what happened in recent updates 

Anyway, here’s the core context file, after a bunch of turns where it interpreted the instruction for “another round” as a request to “repeat the same thing you just said”. The whole product reminds me of a Roomba, circa 2005, repeatedly bumping into a clear patio door and not quite figuring out what’s going on.

> ## Core Context
> 
>   * The Multimodal Treatment Study of Children with ADHD (MTA) is widely regarded as the largest and most rigorous long-term randomized trial of ADHD treatments, including stimulant medications, behavioral therapy, their combination, and standard community care ([NIMH](<https://www.nimh.nih.gov/news/research-highlights/long-term-effects-of-adhd-treatment>)).
> 
>   * The statement that the “only long-term trial found exclusively short-term (14-month) behavior benefits, which were not found at 3 years” is commonly presented by critics of stimulant medication to argue these drugs have no lasting effect, but this is a simplification of the study’s actual findings ([Jensen et al., 2007](<https://pubmed.ncbi.nlm.nih.gov/17667478/>), Molina et al., 2009).
> 
>   * The MTA did find that at 14 months, children in the medication and combination therapy groups had significantly greater improvement in core ADHD symptoms than those in behavioral therapy or community care alone ([MTA Cooperative Group, 1999](<https://pubmed.ncbi.nlm.nih.gov/10591283/>)).
> 
>   * At the 3-year follow-up, differences between the original randomized groups were no longer statistically significant, and this trend persisted in 8- and 16-year follow-ups, though some secondary and subgroup outcomes showed nuance ([Swanson et al., 2017](<https://acamh.onlinelibrary.wiley.com/doi/10.1111/jcpp.12796>)).
> 
>   * The claim misses that the MTA study’s long-term data are nuanced: while the main group-level advantages faded, certain subgroups and functional outcomes showed persistent, though smaller, differences (Molina et al., 2009).
> 
> 

By our metric here, I think ChatGPT only scores the last point, and I’m being generous.

  1. Correctly stating in the core context section of the context report that most researchers would say the follow-up studies can’t speak to medication effectiveness (50 points)

  2. Correctly noting that by the time of the follow-up who was taking medication didn’t match up with initial group assignment (or similar) (50 points)

  3. **Correctly noting that this study is often misrepresented by anti-medication and anti-psychiatry advocates. (50 points)**

If I had thought through my rubric a bit more I would have penalized answers that had bullets that misinformed, which is the case here. The last bullet is just bullshitty nonsense for example.

OK, let’s look at hallucinated links. Here are the ones I caught, though honestly there were some points where it linked me to four sources and only one was relevant (and the other three were, for example, the Japanese Wikipedia page on ADHD. Sigh.). I didn’t count that sort of link-bombing against it, though it did make it much harder to ascertain what the relevant cite was, and in retrospect a fair comparison probably should have dinged it something for ridiculously inappropriate links. 

In any case following links are just straight up hallucinated.

  * https://www.nimh.nih.gov/news/research-highlights/long-term-effects-of-adhd-treatment

  * https://pubmed.ncbi.nlm.nih.gov/10454481/ (mismatch)

  * https://acamh.onlinelibrary.wiley.com/doi/10.1111/jcpp.12796 (mismatch)

  * https://pmc.ncbi.nlm.nih.gov/articles/PMC2971736/

  * https://jamanetwork.com/journals/jama/article-abstract/184776 (on tuberculosis, actually!)

  * https://childmind.org/article/does-adhd-medication-cause-stunted-growth/

  * https://www.additudemag.com/the-mta-study-adhd-medication-combination-treatment/

As with Gemini, **it’s completely possible that there is something about my instructions that just causes it to react poorly here.** I’ve thought about the fact that I request the links in markdown format vs. native format and maybe that just confuses some internal checks? But if I don’t request the links that way, the system doesn’t support any of its claims with links at all, which isn’t that much better than hallucinating garbage. And the fact that _most_ of the links work show that it should be able to produce valid links consistently from my instructions. It just doesn’t.

So if you want to fix my prompt, have at it. Until then this gets 50 - 140 or **negative 90.**

### ChatGPT o3

ChatGPT o3 did surprisingly well in our out-of-the-box test, so I’m interested in how it works here. Hopeful, even? Let’s see.

Ok, wow, this is near perfect. (Sorry, in between those paragraphs I was running it and it took about 10 minutes pasting in the sequence and waiting).

> ## Core Context
> 
>   * The claim “the only long-term trial found exclusively short-term (14-month) behavior benefits, which were not found at 3 years” is often circulated in slides, blogs, and advocacy PDFs to argue that ADHD stimulants lack durable value (Mad in America).
> 
>   * The “only long-term trial” referenced is the NIMH Multimodal Treatment Study of ADHD (MTA), a 14-month randomized controlled trial that later continued as an observational follow-up ([Arch Gen Psychiatry](<https://pubmed.ncbi.nlm.nih.gov/10591283/>)).
> 
>   * At the 14-month endpoint, medication-management and combined-treatment arms showed markedly greater reductions in core symptoms than intensive behavioral therapy or routine community care ([Arch Gen Psychiatry](<https://pubmed.ncbi.nlm.nih.gov/10591283/>)).
> 
>   * By the 3-year follow-up, those between-group advantages were no longer statistically significant; however, trial randomization had ended and many families had switched or abandoned treatments, limiting causal conclusions ([JAACAP 2007](<https://pubmed.ncbi.nlm.nih.gov/17667478/>)).
> 
>   * Later 6-, 8-, and 16-year reports confirm group convergence but also note that most participants—regardless of original arm—remained improved relative to baseline and that longer medication exposure predicts modest height suppression (~2 cm) but not inferior functioning ([PMC](<https://pmc.ncbi.nlm.nih.gov/articles/PMC3063150/>); [JCPP 2017](<https://pmc.ncbi.nlm.nih.gov/articles/PMC6168061/>)).
> 
>   * Other longitudinal and registry studies (e.g., Swedish criminal-registry work) find domain-specific benefits such as lower conviction rates during medicated periods, suggesting the MTA’s outcome set did not capture every potential long-term effect ([NEJM](<https://pubmed.ncbi.nlm.nih.gov/23171097/>)).
> 
> 

I wasn’t expecting this, because I honestly don’t use o3 much, but this summary is so, so good. Not only is it near-perfect, but unlike the ones I usually produce with Claude, I had to do this mechanically, going through a set sequence and not using my own judgment to prod it one way or another based on my intuition. You could run this automatically, hide the [intermediate output](<https://chatgpt.com/share/683b99d6-a8d8-8004-a030-c2a59c936ff4>), just show this result and have a better summary of this than just about any press coverage out there (if you’re a medical researcher looking at this and thinking, oh but I would have written it this way, go ahead and point me to the public-facing reporting that explains this better — I’ll wait).

So 150 points here. Of course on 4.1 ChatGPT had a lot of link hallucination issues, so let’s see how many points are left after checking that. 

Let’s go:

  * ..

OK, I’m back. There are zero hallucinated links. There are two links that are described as being from 2017 when they appear to be from 2016. That’s it. There’s actually about 20 unique urls (less than I thought), but all to relevant sources, a mix of mostly high quality studies and some stuff that is lower quality but represents alternative viewpoints (and shows the structure of the debate). But no hallucinated links at all.

This just feels weird to me, in that I have seen a bunch of things comparing o3 to the other ChatGPT products, and I have seen no one mention this radical difference. You would think this difference in link hallucination would be central to the discussion of the relative benefits. Is it just an artifact of my prompt? Or is it possible that for all people’s talk about benchmarks they are not clicking through the links and not noticing that 4.1 is tripping balls whereas o3 is grounded in real sources? Extremely strange.

Anyway, an absolutely beautiful answer, one which somehow gives ChatGPT both the worst and best score so far.

## Claude Sonnet 4

So this is what happens when you define a protocol beforehand. The answers for Claude went long, and Claude hit its token limit (which is ridiculously low) 

[](<https://substackcdn.com/image/fetch/$s_!dK8l!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcffc8829-7ac5-4291-a4fc-cb7d10b1ea5a_1178x383.png>)

This is frustrating, because right out of the gate Claude gives me this, one-shot, adding none of the additional prompts:

> ### 🏅 What a Fact-Checker Might Say:
> 
> **Mostly False**. While the MTA trial did show that treatment group differences disappeared by 36 months, the claim mischaracterizes the study design and cherry-picks findings. The MTA was a 14-month controlled trial, not a long-term medication study. The follow-up phases were observational and cannot establish whether continued optimal medication management would maintain benefits. The claim also overstates the height effects and ignores evidence that many children maintained improvements over baseline levels. More recent controlled studies suggest continued benefits of stimulant treatment beyond two years when properly managed.

To work around this I am going to add a couple word limits into the prompt code and see if we can get it in under the wire. 

**Update:** OK, I feel pretty sure that Claude has recently put a tighter cap on chat length for pro users, and there simply is not going to be a way for me to replicate the same length of a prompt, and given I can’t do that length, a comparison of the number of hallucinated links won’t be completely fair. In some ways that doesn’t matter, because in all my time using Claude (over thousands of tests) I’ve never seen a single hallucinated link.

Here is the Claude result, skipping the multiple “another rounds”:

> ## Core Context
> 
>   * The statement mischaracterizes the MTA study's design and findings by suggesting it was designed as a long-term controlled trial, when in fact it was a 14-month randomized trial followed by observational follow-up ([NIMH](<https://www.nimh.nih.gov/funding/clinical-research/practical/mta/the-multimodal-treatment-of-attention-deficit-hyperactivity-disorder-study-mtaquestions-and-answers>)).
> 
>   * The MTA found clear benefits for medication and combined treatment during the 14-month controlled period, with combined treatment showing advantages for functional outcomes like academic performance and family relations ([PubMed](<https://pubmed.ncbi.nlm.nih.gov/10591283/>)).
> 
>   * By 36 months (3 years), differences between originally randomized treatment groups had disappeared, but this occurred in an uncontrolled observational phase where families chose their own treatments ([PubMed](<https://pubmed.ncbi.nlm.nih.gov/17667478/>)).
> 
>   * All treatment groups maintained significant improvements from baseline at 3 years, contradicting claims of "no benefits" - the issue was loss of differences between groups, not loss of treatment effects ([PubMed](<https://pubmed.ncbi.nlm.nih.gov/17667478/>)).
> 
>   * Medication adherence dropped dramatically from 63% at 14 months to 32% by 8-year follow-up, confounding interpretation of long-term effectiveness ([PMC](<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3063150/>)).
> 
>   * More recent controlled studies have found continued medication benefits after 2+ years when properly monitored, suggesting the MTA's observational limitations rather than medication ineffectiveness explain the findings ([American Journal of Psychiatry](<https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.18111296>)).
> 
> 

Even without the additional rounds, this is probably the best summary of the bunch. Additionally, as you can [see from the chat](<https://claude.ai/public/artifacts/11471d81-a182-48b1-b1ef-8805e376a4ca>), it actually produced more links to more sources in the short session than the other sources, with no hallucinations. I think we can give it a score of 150 with an asterisk. It’s also the best set of sources. Of course, I think unlike some other platforms they are doing fully real-time non-cached searches, one of those processing intensive things that explains why it is so expensive and the use caps are so low.

Still, I think it’s worth marveling at an explanation that is better than you have probably seen in the press produced by the supposed “stochastic parrot”. Of course, you have to prompt it right…but if you do it feels like magic.

## Scores

[](<https://substackcdn.com/image/fetch/$s_!Fj84!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe857cd93-d195-4a62-b0b5-40235496580b_852x556.png>)

One of the interesting things about this admittedly informal analysis is that hallucinated links correlate with worse answers. Maybe that doesn’t sound surprising to people, but there’s no reason it has to be that way. There have been studies that have shown deterioration of answers that use real-time search vs ones that lean on the model. Plus many of the hallucinated links are just bad links, and may represent a real paper somewhere, just not at the malformed address. But at least for this test they correlate. 

## I don’t know why people don’t talk about this stuff in comparing models

Again, I have a weird prompting layer. I know that. I worry that my insistence in SIFT Toolbox that everything be sourced is pushing some of these systems to the breaking point. 

But shouldn’t they be able to fulfil that request? Maybe someone sees this test and points out changes that I could make to my prompting layer that fix this issue, and that would be a lovely outcome. 

In the meantime I find it odd there is a very real split on link hallucination here, with two models not doing it at all, and two models doing it quite a lot, and yet when a new model comes out we don’t hear about its link hallucination level. This admittedly small test showed that the models that hallucinate links less also provide better answers. It seems like it would be worthwhile to figure out why these models are acting so differently on this dimension.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
