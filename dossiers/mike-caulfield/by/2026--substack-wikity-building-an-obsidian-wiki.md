---
title: "Wikity: Building an Obsidian wiki out by leaving corrective notes for Claude Code in it"
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-04-12
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/wikity-building-an-obsidian-wiki
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Wikity: Building an Obsidian wiki out by leaving corrective notes for Claude Code in it

*How to build through commenting and think through adopting an editor's eye...*

## Full text

_Note: the video above is sped up, and the part where it does all the edits it had queued is clipped out because it would be boring to wait._

This one is for people with a bit of technical skill. A method for building out an Obsidian wiki by leaving notes on what you want done: 

1) We have a bash script that gets triggered by alt-o and looks in Obsidian markdown for a notes syntax (==!). We leave Claude notes on what we don't like about the wiki Sometimes we say what's missing and ask for new pages. We hit alt-o 

2) Bash script picks up unresolved notes with grep, sanitizes, passes back with context to Claude as editing instructions. 

3) Claude fixes that stuff. 

4) Every 10 comments, Claude reviews the comments and makes a note of how to write a better first pass.

This is only the quickest little video because it’s late and it’s tax season, but I actually have it set up where you generate a very basic wiki and it slowly becomes much better as you cruise around and make notes. This is after many notes were left, the initial wiki was 10 pages. It makes pages, fills gaps, finds evidence, removes LLM speak, links quotes. 

Building it out by leaving notes is interesting. I think I actually end up mentally processing a lot of it in good ways. After all, I have to read it closely enough to see what’s missing, what’s unsupported, etc. I think it helps with cognitive offloading. 

I used to be known for wiki experiments and this reminds me to get back to that.

If this video raises more questions for you than answers it did its job (Sorry!). 

If you think this through it’s easy enough to have Claude build you your own version. I run it sandboxed in WSL and launch Obsidian from there, but I will note that file reads and writes combined with web search poses risks, so don’t do this unless you’re ok with that on the machine you’re on.

## The “chorus of voices” style (Update)

Ok, as usual when I work on wiki projects I get obsessed.

I am starting to get it to follow my preferred style which is text that loosely pulls together sourced quotes to keep _visible grounding_ on all pages. And — it’s cool actually. I’ve chosen to have it follow what I call loosely an “oral history style” with the source quoting stitched together with connective prose and declarative headings. 

[](<https://substackcdn.com/image/fetch/$s_!Avj3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58b140ff-9c8c-4acf-97af-042843522c3e_813x616.png>)

This to me reflects something like the old index cards we used to do back in the day during library research. You write the quote and the source on the front. You write what it means on the back. You keep flipping through those as you develop your own ideas. 

This brings me to a point about the subject of the wiki. I think people think I do film stuff because I’m a film nut. It’s quite the opposite. I want to be a film nut, but only got into film about 18 months ago. I find it a fascinating area because I don’t have domain knowledge, I’m a passionate novice trying to skill up, just like many of our students. Doing film as a subject with this stuff is a way to see if I am building a tool that helps with learning new things, or only consolidating extensive existing knowledge.1

So far here is the command palette for the wiki:

  * Claude activity & status

  * Expand sourcing: add more quoted voices to current page

  * Expand sourcing (all tagged): process every ==!exp== page

  * Open edit history for current page (Alt + H)

  * Process change requests

  * Review whole vault with Claude (maintainer) (Alt + O)

  * Save & process with Claude (Ctrl + Shift + E)

  * Source loose quotes and check for hallucination (Alt + Q)

  * Style pass: check and humanize wiki pages

More soon…

1

One neat thing about being a novice here is there is a test of that at sorts right now, which is I’ve started doing this film podcast called Couch to 4k, which is just me and an old friend talking about the 4k films we’re buying and watching. So I’m going to try to use this to see if I can get a fluidity in talking about these films. We’ll see.
