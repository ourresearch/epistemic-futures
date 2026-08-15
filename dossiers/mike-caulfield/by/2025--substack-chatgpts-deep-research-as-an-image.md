---
title: "ChatGPT's Deep Research as an image contextualization tool: Possibilities and frustrations"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-03-09
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/chatgpts-deep-research-as-an-image
retrieved: 2026-08-13
content: full-text
notes: ""
---

# ChatGPT's Deep Research as an image contextualization tool: Possibilities and frustrations

*Deep Research can do more than reports, its process is pretty interesting to watch -- and it continues to fail in interesting ways.*

## Full text

So this is a picture of Elvis.

[](<https://substackcdn.com/image/fetch/$s_!rGz2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3a7d240-d327-4c70-9c43-00058f39aa3d_286x400.png>)

It’s an interesting photo because it’s described a variety of ways online, most wrong, one right.

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

The right way to describe it is as Elvis’s _discharge_ photo from the Army, most likely on March 3rd, possibly on March 4th, of 1960. If you were unsure about that, you could note the sergeant stripes on his uniform, a rank he achieved in January of that year, and the physical stripes that he received in February 1960. It’s possible the picture was taken earlier than March 3rd but after mid-February, but the [person who wrote the book ](<https://elvisbiography.net/2023/02/05/the-truth-about-elvis-presleys-mugshot-photo-was-elvis-arrested/>)on Elvis’s army years said it was taken at Fort Dix, and Elvis was only there for two days before discharged the morning of the fifth. And since the photo needed to be attached to the DD-214 form for discharge, it makes sense they would get it done on the 3rd, which is the date most better sources ascribe to it.1

The wrong ways it is described online are as follows:

  * It’s described as an arrest mugshot from 1956 after he was arrested for assault.

  * It’s probably most commonly misdescribed as his army _intake_ photo from 1958.

    * Sometimes this is described as being taken at Fort Chaffee, sometimes at the “draft board”

It gets described this way because it just _seems_ logical to people. Folks know about mugshots and ID photos, but the idea of a discharge photo is foreign to people that haven’t been in the military. So even fans who know Elvis went in (famously!) as a private don’t notice the sergeant stripes. We’re blind to things that don’t fit into our schemas.

Anyway, I got the idea to see how LLMs would do with the question of when this photo was taken — and discovered some interesting things about ChatGPT’s Deep Research as well.

First, let’s go through the other models.

## GPT 4o

GPT 4o goes with March 24, 1958 at Fort Chaffee (wrong).

[](<https://substackcdn.com/image/fetch/$s_!RIoL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1673c6d9-8213-488c-af61-f446961c8119_986x703.png>)

## GPT 4.5

GPT 4.5 goes with March 24, 1958 (no location) (also wrong). Not great so far.

[](<https://substackcdn.com/image/fetch/$s_!9jAr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fe72222-9329-49d5-98ef-eb4580a6aa7d_953x726.png>)

## Claude 3.7

Claude 3.7 goes with March 24, 1958 — but at the “Memphis Draft Board” (wrong; also ridiculous, I am pretty sure the draft board doesn’t have you sign up for selective service then hand you a uniform in your size.)

[](<https://substackcdn.com/image/fetch/$s_!vHaI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feecf936a-50bb-4f09-99ca-d013c43c8808_1021x786.png>)

## o1 Pro

So o1 pro took more time to think about this — and came up with a day later: March 25, 1958 at Fort Chaffee. (Wrong). It added a bit of irrelevant reasoning on why it wasn’t the 24th, though. Sometimes “reasoning” isn’t enough.

[](<https://substackcdn.com/image/fetch/$s_!UKJl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d6ec358-eb4d-4f1d-b1f1-93f421243ccf_915x786.png>)

## Round up so far

 _GPT 4o: March 24, 1958 Fort Chaffee  
GPT 4.5 March 24, 1958 (no location)  
Claude 3.7: March 24, 1958 Memphis Draft Board  
GPT 4o pro: March 25, 1958 Fort Chaffee_

I don’t include Gemini here, because Gemini still doesn’t really have vision in any equivalent sense, but if you must know, when I asked Gemini it said “1970” as it probably got it confused with [this fake mug shot](<https://www.elvispresleymusic.com.au/pictures/1970-november-on-plane-to-denver.html#:~:text=Denver%20Coliseum%20%7C%20November%2017%2C%201970>) that Elvis got taken in Denver that year (you may have to scroll a bit). This seems to me to be based on an over-reliance of Gemini using Google Vision labels and OCR instead of richer descriptions and other methods, although that’s just a guess.

Anyway, this is pretty abysmal. Note that I think AI does as well here as a lot of humans — as I said before, most people have a mental block seeing this as a discharge photo because they don’t know what a discharge photo is. But there’s two major guesses you can find online about this photo, and every model chooses the wrong one. And with confidence!

Anyway, I got curious: could Deep Research be used for this? 

## Deep Research for more than reports

Almost all the uses I’ve seen of Deep Research have been creating long reports or articles. But the basic iterative retrieval augmented approach it uses doesn’t have to be just about that. Part of the process of knowing when this photo was taken involves getting more information than the photo itself. We can see that there are different dates and places attached to this photo online, but we can also see that only one date and place is coherent with the greater timeline. 

I don’t mean to say that Deep Research _reasons_ like this. But its iterative process does work coherence checks of its own sort into the process, coming up with certain claims, then searching for confirming or disconfirming evidence, and deciding (again, in its own way) what fits and what does not). 

So I put it in, and let it do its 6 minutes of research.

[](<https://substackcdn.com/image/fetch/$s_!POq2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F111dd94f-756d-4c6e-9d75-6538cb3a4bd0_936x769.png>)

And I’ll be damned, it got it right:

[](<https://substackcdn.com/image/fetch/$s_!kTZD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfa50a23-3662-4e19-9fe5-3ae5266b149e_883x682.png>)

That said, it gets a bunch of stuff _wrong_ too, which is disappointing. In particular, the whole thing about the “newly sewn name patch” and “nameplate” is a bit of _artifact confusion_ : the linked photo there is to one from _1958_ , when Elvis first got his uniform, not his discharge. 

[](<https://substackcdn.com/image/fetch/$s_!2zKo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff2122c7-0d02-4c09-bd3d-853015d61cc6_674x854.png>)

It is clearly misunderstanding2 what a “nameplate” is. The photo above is famous because his _name tag_ had just been sewn on during induction, which is the theory it had just correctly avoided. That’s — that’s a pretty big fail, honestly. We’re asking about a photo, it’s getting to the correct date — then failing in the final stretch to even recognize the photo we’re talking about.

But even if some of the supporting evidence is confused, it does get closer. And at least in this format, the support is _discoverably wrong_ , which is probably a blessing of sorts?

## Looking at the Chain of Thought

The chain of thought is fascinating to review — for the first few minutes it seems destined to end up at the same mistake (1958 induction photo) as all the others. I sat watching it in real time like a sports match, rooting for it to find its way out of its initial cul-de-sac, and for the first 3 minutes it did not look so great. It’s all about induction, not discharge:
    
    
    Searched for Elvis Presley military photo
    
    
    I’m thinking the search findings offer a detailed look into Elvis Presley’s military history. The results include a notable Elvis inductee photo and sources like rarehistoricalphotos.com and Wikipedia.
    
    
    Read rarehistoricalphotos.com
    
    
    I’m working through a well-known military photograph of Elvis Presley holding a nameplate, possibly an official Army induction photo or a press photo from Fort Chaffee.
    
    
    Searched for Elvis Presley induction photo
    
    
    I'm looking at a likely induction photo in the "University Archives" lot, connected to a draft notice dated Dec 20, 1957.
    
    
    Read universityarchives.com
    
    
    I'm piecing together Elvis Presley's induction photo, likely from his transition to Army duty in 1958.
    
    
    Searched for Elvis Presley Fort Chaffee induction photo
    
    
    I’m honing in on the time Elvis Presley spent at Fort Chaffee, noting his significant three-day stay and his iconic haircut.
    
    
    Read elvispresleymusic.com.au
    
    
    Examining images with captions of Elvis Presley during his army induction. Noticing sites like ElvisPresleyMusic for more details.
    
    
    Read more from elvispresleymusic.com.au
    
    
    I’m working through finding the specific military photo of Elvis Presley holding a nameplate, possibly from his induction day at Fort Chaffee in 1958.
    
    
    Searched for Elvis Presley holding sign military photo date
    
    
    I'm piecing together famous Elvis Presley military photos, like his haircut and swearing-in. The phrase "holding a nameplate" seems to suggest a specific mugshot-style induction photo.
    
    
    Read alamy.com
    
    
    I’m considering a search on Alamy or checking Wikipedia's "Military career of Elvis Presley" for details on his induction and any official photo.
    
    
    Read en.wikipedia.org
    
    
    I am gathering details on Elvis Presley's army induction, checking Wikipedia for event specifics, and verifying with authoritative sources like AP captions or news stories.
    
    
    Read rockhurstauctions.com
    
    
    I'm considering if "holding a nameplate" refers to Elvis Presley holding something during his military induction, like a sign or name tag.
    
    
    Searched for Elvis Presley Fort Chaffee holding sign photo date
    
    
    I'm exploring the Encyclopedia of Arkansas for Elvis Presley's induction details, which may include a photo date.
    
    
    Read encyclopediaofarkansas.net
    
    
    I'm thinking through the concept of "holding a nameplate" and how it might relate to specific iconic photos of Elvis Presley during his army induction at Fort Chaffee.
    
    
    Searched for Elvis Presley Fort Chaffee name sign photo date
    
    
    I'm piecing together his iconic military photo—possibly at basic training's conclusion or another notable event. Considering Elvis' image history and military term references.
    
    
    Searched for Elvis Presley nameplate photograph
    
    
    Sectioning off "nameplate" for "Elvis Presley" might yield more targeted results.
    
    
    Searched for Elvis Presley holding nameplate
    
    
    I’m gathering details on Elvis holding an ID board at Fort Chaffee, possibly during his March 25, 1958 arrival for military service.
    
    
    Searched for Elvis Presley Fort Chaffee photo March 25 1958
    
    
    I’m checking the ebook "The Army Years" to see if it’s worth a read.
    
    
    Read theelvisfiles.com
    
    
    Evaluating a third-grade reading level.
    
    
    Read more from theelvisfiles.com
    
    
    I’m working through various Elvis Presley photos during his military service. The specific photograph of Elvis holding a nameplate remains elusive.
    
    
    Searched for Elvis Presley March 25, 1958 photo with name tag
    
    
    I’m verifying the exact date of the famous Elvis photo, examining sources for inconsistencies, and considering archives, forums, and specific induction-related photographs.
    
    
    Searched for Elvis Presley Army ID photo
    
    
    OK, let me see. The eBay listing describes Elvis Presley in uniform, holding a name board, likely taken at his army induction.
    
    
    Read ebay.com

But even here, it starts to act a bit like a fact-checker, in real time. If we are going to get the date of this, and he’s wearing a uniform, do we know when he got that uniform?
    
    
    I’m analyzing the timeline of Elvis Presley’s uniform issuance, linking it to his induction and subsequent public appearances. This helps confirm when he was photographed in his uniform.
    
    
    Read unwritten-record.blogs.archives.gov
    
    
    Mapping out Elvis's induction photo, which likely shows him holding a nameplate with his details, akin to his Army serial number.

Then it reads a Reddit post which I imagine mentions the sergeant patch (my guess is [this one here](<https://www.reddit.com/r/OldSchoolCool/comments/slgpf6/elvis_presley_1958_enlistment_photo/>)) not fitting the narrative.

Again, sorry if this is a bit labored, but I find the chain of thought here interesting. 

It’s true, it’s probably found someone explicitly saying this is a discharge photo. It didn’t find that out itself. But the key here is weighting this new information correctly. Does it undo all the other talk about it being an induction photo?

The way it starts to veer indicates its sensing that this route is likely more productive.
    
    
    Read [reddit.com](<https://www.reddit.com/>)
    
    
    It's clear the photo depicts Elvis Presley as a sergeant, likely taken around 1960. The rank insignia points to this, with potential dates including March 1 or 2, 1960.
    
    
    Searched for Elvis Presley sergeant holding sign photo date
    
    
    I’m examining a website for Elvis Presley music marked as (.com.au), likely reflecting a similar style.
    
    
    Read [elvispresleymusic.com.au](<https://www.elvispresleymusic.com.au/>)
    
    
    I’m figuring out Elvis Presley’s travel route back to the U.S. in 1960, noting he likely flew from Germany to McGuire AFB, NJ, on March 2 or 3.
    
    
    Read more from [elvispresleymusic.com.au](<https://www.elvispresleymusic.com.au/>)
    
    
    OK, let me see. I’m thinking through the introduction and how it includes a March 3 photo, possibly clicked from [116†Image].
    
    
    Read more from [elvispresleymusic.com.au](<https://www.elvispresleymusic.com.au/>)
    
    
    I’m examining the image of Elvis with a sign that reads "Presley Elvis A" through eBay and Pinterest listings. The result shows an enlistment photo with the inscription "BACK IN USA."
    
    
    Searched for Elvis Presley enlistment photo poster  

This next block is interesting, because this is exactly what I find compelling — the stripes were obtained mid-February, Elvis left the military March 5th, 9:15 a.m.. That’s a pretty small window. If it was taken in the USA, it’s an even smaller window.

But also notice — it’s in a weird state here. It’s worked its way to this concept of the discharge photo — while still referring to it as an “enlistment” photo…3
    
    
    Mapping out the "Enlistment Photo," it likely spans February to March 1960, featuring Elvis Presley in Germany or stateside with sergeant stripes, possibly linked to his honorable discharge.
    
    
    Searched for Elvis Presley 1960 sergeant photograph
    
    
    Considering the timeline and possible confusion around Elvis Presley's press conference at Fort Dix on March 3, 1960, while also checking for official identification or archival purposes. His biography and other sources may provide further insights.
    
    
    Read [se.pinterest.com](<https://se.pinterest.com/>)
    
    
    I’m analyzing various angles of the "Sgt Elvis Presley March 3 1960 Fort Dix press conference." Progress is steady, and I’m piecing together more insights.
    
    
    Searched for Elvis Presley March 3 1960 Fort Dix press conference photo

## Artifact confusion and answer collapse

As I mentioned, the exact date I am unsure about, but this keeps going and ends up in the area of reasonable assertions — Fort Dix, discharge photo, done in the time he was there — and outperforms even the newer models. It also fails in frustrating ways, citing as evidence a photo that is from 1958 and has a _name tag_ not a _name plate_. 

There’s not a clear story here — except that I think it’s a very useful tool but one where the user should be aware of the flaws. In particular, it demonstrates _artifact confusion_ (wrongly thinking a similar photo is the one under discussion), and what I call “answer collapse” (where LLMs take two incompatible answers to a question and improperly try to synthesize them).

Anyway, I thought I’d document it here, and maybe we could get a bit of experimentation with using it for something other than research briefs. 

I’ll also add this at the end here — I’m actually a pretty big believer in the power of LLMs, I just happen to have a talent for breaking them. Just mentioning that because sometimes I write something like this and it circles the internet as some sort of indictment. I’m much less interested in making broad pronouncements about the worth of LLMs than in figuring out the what they excel at and what they don’t, and how that might influence our use of them — or how we might address their flaws.

1

I go into this detail partially to show facts are hard, but there are boundaries. In argumentation theory we would say that both a date of the 3rd and the 4th would be _reasonable_ even if a date of the third is the more obvious choice. Given his discharge was at 9:15 am on the 5th, a date of the 5th would be _unreasonable._

2

Yes, I know that it’s not really “understanding” anything in a human sense, but it’s exhausting to find other words for this, when what it most clearly resembles is a misunderstanding. If you want, you can put “performing” in front of all these nouns — “It’s failing at _performing_ understanding” to indicate that what we are saying is it cannot mimic understanding in this context, but it seems a bit pedantic.

3

This is part of what I mean by “answer collapse”, more on that later.
