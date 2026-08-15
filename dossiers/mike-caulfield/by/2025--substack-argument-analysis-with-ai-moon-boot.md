---
title: "Argument Analysis with AI: Moon Boot"
person: mike-caulfield
section: by
type: blog-post
year: 2025
date: 2025-01-20
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/argument-analysis-with-ai-moon-boot
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Argument Analysis with AI: Moon Boot

*Example and comment*

## Full text

I’m going to start putting up more examples of analysis I’ve done with my LLM-based Toulmin analyzers. You can avoid them by looking for the prefix above. 

In this one I captured a frame from a popular TikTok moon landing conspiracy theory video and feed it to the Toulmin analyzer:

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.

[](<https://substackcdn.com/image/fetch/$s_!mQTL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6804cd7-d435-4d81-92ed-9a0f7af07d96_687x904.png>)

Here’s the output, and I’ll review it below.

# _**Analysis of Apollo Moon Landing Claim**_

 _This document examines a common conspiracy theory that questions the authenticity of the Apollo 11 moon landing based on alleged discrepancies between the sole of an astronaut’s suit and the bootprint left on the lunar surface._

* * *

### _**Claim** :_

_The Apollo moon landing is questioned because the boot sole shown does not match the bootprint left on the lunar surface._

* * *

### _**Evidence (Data or Grounds)** :_

_The evidence consists of two images:_

  1. _The sole of the Apollo 11 space suit, which appears smooth or with minimal tread._

  2. _The well-defined, ridged bootprint on the lunar surface._

#### _**Backing for Evidence** :_

  * _The image of the suit sole (**documentation**): Presumably from a museum display or official archive._

  * _The bootprint on the lunar surface (**documentation**): A famous NASA photo from the Apollo 11 mission._

* * *

### _**Warrant (Assumption)** :_

_If the sole of the astronaut’s boot does not match the bootprint on the moon, this discrepancy undermines the authenticity of the lunar landing._

#### _**Backing for Warrant** :_

  * _(Implied): It is expected that the boot sole shown on the suit matches the bootprints on the lunar surface._

  * _(Implied): If a mismatch exists, it could suggest deception or misrepresentation by NASA._

* * *

### _**Rebuttals** :_

  1. _**Overshoes Worn on the Moon** : Apollo astronauts wore extra footwear called lunar overshoes, which had a different tread pattern from the suit soles. The bootprints were made by these overshoes, not the suit soles visible in the museum display._

     * _**Backing** : NASA documentation and images show the lunar overshoes separately, confirming their ridged pattern._

  2. _**Selective Presentation** : The image only shows the primary space suit, omitting any reference to the overshoes._

  3. _**Misleading Implication** : The evidence presented does not prove the moon landing was faked; it reflects a misunderstanding or omission of the full astronaut gear._

* * *

### _**Known Evidence Outside This Argument** :_

  * _Extensive documentation exists of the Apollo missions, including photos, videos, and physical artifacts such as lunar samples._

  * _Independent tracking of Apollo missions by global observatories corroborates the landings._

  * _Technology and knowledge at the time align with the feasibility of the missions._

* * *

### _**Summary**_

 _**Verdict** : **Lacks evidence**_

 _The claim relies on a misunderstanding of astronaut gear, specifically the use of lunar overshoes that created the bootprints. The evidence presented does not account for the full context and omits crucial details, such as the overshoes' design. The high bar of counterevidence against Apollo moon landing authenticity is unmet, given the extensive independent verification and documentation of the missions. Additional evidence debunking this claim includes detailed NASA archives and accounts from global space agencies._

# Review of Analysis

Lot’s of good things here but also some nits to pick. First, on the evidence it does really well:

####   
_**Evidence (Data or Grounds)** :_

_The evidence consists of two images:_

  1. _The sole of the Apollo 11 space suit, which appears smooth or with minimal tread._

  2. _The well-defined, ridged bootprint on the lunar surface._

#### _**Backing for Evidence** :_

  * _The image of the suit sole (**documentation**): Presumably from a museum display or official archive._

  * _The bootprint on the lunar surface (**documentation**): A famous NASA photo from the Apollo 11 mission._

What this shows is the proper distinction between evidence and backing. The evidence is sort of “the fact itself” here, the boot and the bootprint. The _backing_ for the evidence is how we come to know that fact: in this case the photos. It makes one small mistake I’d point out here — I’d stress from the beginning of that second bullet that the backing was not the bootprint itself, but the photo of it. It gets there in the second half of the bullet, but could put that up front. 

The backing for the warrant is a bit sloppier. Let’s look at why.

### _**Warrant (Assumption)** :_

_If the sole of the astronaut’s boot does not match the bootprint on the moon, this discrepancy undermines the authenticity of the lunar landing._

#### _**Backing for Warrant** :_

  * _(Implied): It is expected that the boot sole shown on the suit matches the bootprints on the lunar surface._

  * _(Implied): If a mismatch exists, it could suggest deception or misrepresentation by NASA._

I think the warrant/assumption is right. The main warrant is well expressed. But the backing here should be a bit more general — not additional assumption. 

The question we’re asking when we look at the warrant’s backing is what is the answer if you were to say the warrant (“If these two things don’t match, it suggests a larger deception about the landing”) and someone was to say “Well, I don’t agree.” How could you show them that disagreeing with the warrant is inconsistent with other things they agree with? 

Imagine you answering that with a sentence starting with “Well, would you would agree that…”

So this one doesn’t really make sense — it just restates the warrant. If you disagree with the warrant you disagree with this, it gets you nowhere:

  * _(Implied): If a mismatch exists, it could suggest deception or misrepresentation by NASA_

Instead, back it up a bit. “Well, would you agree that…”

  * If small things are faked, it suggests larger deception

And yeah, I’d agree with that. If you found, for example, that police had faked some footprints in a murder case, even if those footprints weren’t crucial to the case you’d say, huh, I’m reconsidering everything at the crime scene now. Good backing for warrants should have some portability across different arguments. 

This one annoys me because it’s really a warrant, not backing:

  * _(Implied): It is expected that the boot sole shown on the suit matches the bootprints on the lunar surface._

Here’s how I might do a quick rewrite of this, setting up the warrant in this case as a causal chain:

### _**Warrant (Assumption)** :_

  1. _The bootprint should match the sole of the shoe in the photo._

  2. _There is no better explanation for the bootprint mismatch than fakery._

  3. _If the bootprint was faked, they may be hiding other things._

#### _**Backing for Warrant** :_

  * _(#1, Commonly accepted): Prints can be inferred by looking at soles_

  *  _(#3, Commonly accepted): If small things are faked, it can suggest a larger deception_

Again, there’s no perfect model of this but if you imagine each piece of this warrant being questioned it would go pretty naturally. You say “The bootprint should match” and you have pretty god backing for that — we do this all the time. It’s not weird to expect it to match. You say if it doesn’t match, it calls things into question. And so on. 

We don’t have backing for #2, that the mismatch shows fakery, but that’s also where the error of the argument lies. I think it’s fine to leave it empty.

One thing that I think is going on here is that the model is seeing Warrant (singular) and leaning into supplying only one assumption, then throwing the others into backing. It may kill me — because it’s very unToulminesque — but I might call the middle section Warrants (plural) and see if it generates more assumptions. 

In this case the warrant failure is in a catch-all warrant that is often the point of failure:

  * _There is no better explanation for the bootprint mismatch than fakery._

The way you would generally back that is by showing that a scan of the relevant literature and reporting surfaces no alternate explanations. Of course, the conspiracy theorist can’t do that because a scan very much does show the alternate explanation, one that has been either intentionally or unintentionally hidden from the audience. 

I could talk about the rebuttals, which are being used here a bit differently than Toulmin, but I think are still very useful. But let’s leave this one. 

On the whole, not bad. Good treatment of claim, evidence, and warrant, with the exception the warrant is underspecified and the backing is mucked up. It’s be an A for an undergrad, but because we’re shooting higher than that I’m going to give it a graduate school B+. 

If you teach Toulmin, or warrants in general, let me know if you agree in the comments!

Thanks for reading The End(s) of Argument! Subscribe for free to receive new posts and support my work.
