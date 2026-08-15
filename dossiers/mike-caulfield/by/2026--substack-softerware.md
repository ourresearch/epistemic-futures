---
title: "Softerware"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-03-09
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/softerware
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Softerware

*Keep your Claude skills loose for better performance*

## Full text

Saw this earlier today, and it’s funny because it’s true, as they say:

[](<https://substackcdn.com/image/fetch/$s_!iFCW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F335f6afd-ed6c-4b14-94f0-b87aa8090943_813x302.png>)

I've been doing some large scale things with Claude Code and Claude Cowork recently, and the thing I will tell you about these new “skills” based prompting frameworks is they are best developed as a set of values/objectives/reminders and a bit of code for those things that are tiresome to watch the LLM fumble toward each time. Any more than that? You’re probably mucking things up.  
  
These architectures are what I call "softerware", and the trick is to get some of the predictability of software while avoiding the rigidness of code.   
  
What you'll find with a lot of skills out there, especially ones people developed using Claude and haven't pruned back, is they are too fossilized, and have lost the benefits of that balance between code and in-the-moment problem-solving. The neat thing about the LLM skills-based approach is that the LLM can write a program in the moment that addresses not the generalized and abstracted problems software addresses, but a piece of code that is structured around the very specific version of the problem in front of it. You don’t want to lose that advantage!

As an example, were I to write _code_ to process a bunch of notes for transcription I might slowly build out a set of interrelated modules, whether Python or Node, that OCR documents. Maybe I use the Tesseract character recognition library. Maybe I get the PyMuPdf module for grabbing PNGs out of PDFs, feeding them to Tesseract, then taking the output and putting it back onto the PDF. And so on. 

But, of course, every step beyond that the code becomes a bit more dependent on me _foreseeing what the code will hit_. We get typed pages then suddenly hand-written notes — is Tesseract going to handle that? If I have a handwriting module, do I have a triage module that routes it to handwriting or typeset mode? What if it is rotated to landscape? The process of code quickly becomes a game of anticipating every possible condition, and what started as a simple solution becomes one of the most dreaded things known to man. 

It becomes a _codebase_.

What LLMs allow is for one to set a set of objectives and guiding principles and desired outputs and let them handle the instances I haven’t thought about without getting into the rigidness of code. I can say look, the point is for this to be accessible to screen-readers, and if it hits a landscape mode page it knows it needs to recreate that HTML as a “flow” and not as precise positioning. If it hits handwriting, it can just use its vision to read the handwriting. If I tell it to write something back into a PDF it can use PyMuPdf, but if it hits a particular problem that PyMuPdf can’t solve it can look for something else. 

The problem is that for a certain set of problems LLMs, reasoning from first principles, have to make a lot of mistakes. If my transcription engine is transcribing PowerPoints, I know, for instance, that the only real way you can deal with old PowerPoints (ppt’s not pptx’s) is to have the LibreOffice library installed, and convert them to pptx. I can’t watch Claude spend 20 minutes figuring out that this is the only way this is going to work every time I ask it to transcribe a ppt.

So what you want to do is put enough code or code guidance in there that you’re not watching the code fumble (or worse, choose solutions that violate the whole point of your exercise). But it has to stay loose enough that you haven’t just ended up creating a codebase, with all the rigidity that entails. 

It has to be, in a word, _softerware_ , and you have to rigorously defend the looseness, or you will lose the benefit.

Anyway, that’s my thought for the day.
