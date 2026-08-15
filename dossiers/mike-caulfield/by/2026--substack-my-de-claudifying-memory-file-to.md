---
title: "My De-Claudifying Memory File to Ditch Claude's \"Word Mosaics\""
person: mike-caulfield
section: by
type: blog-post
year: 2026
date: 2026-07-31
venue: "Mike Caulfield's Substack (mikecaulfield.substack.com)"
authors: "Mike Caulfield"
source_url: https://mikecaulfield.substack.com/p/my-de-claudifying-memory-file-to
retrieved: 2026-08-13
content: full-text
notes: ""
---

# My De-Claudifying Memory File to Ditch Claude's "Word Mosaics"

*How I at least partially mitigate Claude Fable's ridiculous yoda-speak*

## Full text

_Note: as you read this please realize that if you are using Claude to write simple stuff for you you probably won't see this sort of thing, but I run projects where Claude is summarizing 20,000 plus items a day, and trust me it does go off the rails._

As others have noted, Claude increasingly produces garbage prose; it tends away from producing sentences and towards something I call “word mosaics”. Stuff like:

> What survives is _**a film whose visual grammar keeps insisting on guilt while the dialogue ultimately acquits**_ , which is why many critics read the ending as unpersuasive by design or simply broken, depending on how generous they’re feeling. 

or worse

> He was dead all along, and every scene replays differently on the way home. Reassessment detonates: from here it is the prestige move of two straight decades, running second only to the whodunit.

I have some theories as to why Claude went from being one of the more literary sounding LLMs to something that is the verbal equivalent of those old Google DeepMind pictures, with paragraphs so weird they feel like products of non-carbon based life-forms…

[](<https://substackcdn.com/image/fetch/$s_!suiI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e684c0c-5883-46e9-90a1-5e058d4971a9_640x913.jpeg>)

… but I will save those thoughts for another day. For now, I thought I’d share the memory file I use to at least partially help mitigate it. 

So here you go.1 Maybe it can help you not throw your laptop at the wall. So far its worked for me in the sense that it takes this nonsense from level 11 to level 7 or so. When it fails I can at least say, “write it again and consult our no word mosaics rule”.

I’ll try to test it a bit more over time.

\---

name: write-concretely-no-word-mosiacs

description: Mike’s prose standard for anything user-facing: explicit subjects/objects, explicit causal relations, no zeugmas, resist metaphorical/poetic/analogical language

type: feedback

Mike’s directive, 2026-07-29, verbatim:

“Write concretely. if things have direct objects, include the direct objects. if you intimate a possessive say who or what it belongs to. Make causality apparent. For instance, stop putting comma joined clauses together without specifying their logical, causal, temporal, or other relation. With every sentence produced, ask “Have I hidden a subordinate relation? A subject? An object? Have i written this in a way that multiple contradictory readings exist?” If so rewrite it.”

Mike’s amendments, 2026-07-29, verbatim: “each verb gets its own object, no zeugmas” and “resist metaphorical, poetic, or analogical language”.

Why: the poetic-compression register (”The asylum frame arrives”, “Amy authors her own death and grades the coverage”, “returns home wearing his blood and a self-defense story”) hides agents, objects, and causal structure, and lets contradictory readings coexist. 

How to apply: in all user-facing prose (responses, artifact copy, film blurbs, reports, README text): name the agent; state what the agent did to what; give each verb its own object (the zeugma fix: “returns home wearing his blood and a self-defense story” => “returns home covered in his blood, and tells the police that she killed him in self-defense”); connect clauses with because/so/when/after etc; give every statistic an explicit denominator (”23% **of the twist films we catalogued** in the 1920s”); replace each metaphor or poetically compressed phrase with the literal claim it stands for (”Kinship reveals appear in 7% of 1970s twist films and rise to 11% in the 1980s” or “These reveals increase in the 1970s and don’t go back down.”, not “the mode steps up and never falls back”). 

1

(The format looks this way because as part of my war on Claude word mosaics when I tell Claude to update things I only let it add my explicit words so it doesn’t turn it to garbage).
