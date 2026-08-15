---
title: "Auto-Annotating News Articles To Scaffold Media Literacy Skills In Students"
person: mike-caulfield
section: by
type: blog-post
year: 2017
date: 2017-05-10
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2017/05/10/auto-annotating-news-articles-to-scaffold-media-literacy-skills-in-students/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Auto-Annotating News Articles To Scaffold Media Literacy Skills In Students

## Full text

I’ve been playing around a bit with auto-annotating news articles to foster better literacy reflexes in students. Here’s the latest work in progress: I’ve made an annotation bot that goes out and finds articles mentioning industry front groups and asks students to do research to confirm or deny the connection.

How does this work? I compiled a list of over 150 known front groups — groups that present as social activism groups, but are thought to be industry-funded astroturf.

Since most people don’t understand bots, I want to be really clear about what I’m about to show you. My code doesn’t annotate in real time. It runs as a “batch” process overnight, goes and tries to find new articles mentioning front groups, and has new pages annotated for the general public when you wake up. (It’s a surprisingly quick process, actually, so if you wanted to run it during the day or during a coffee break you could).

Got it? This goes out and annotates pages based on the fact they mention some potentially dubious organizations. But it does so in a way that anyone can look at the annotations.

So let’s show an example. Some test crawls from last night showed this story here (among about [a couple hundred other stories](<https://hypothes.is/users/contextbot?q=>)):

Ignore the “Untitled Document” bit right now — that’s a bug being worked out. Future annotations will display titles.

In any case, we go check this article out. Maybe we’re just interested. Or maybe as a student we were told to check out one of the results of contextbot and further annotate it. Here’s what we find:

It’s an op-ed from a researcher who talks about their lab’s cute little test piglet “Slinky” and how much they adored him. It’s pretty folksy stuff:

> Let me tell you about Slinky.
> 
> Slinky was sweet and full of personality, an adorable and playful piglet who grew to be a gentle and smiley giant. Everyone who met him was smitten instantly. He was purchased when he was 2 months old to help us develop surgical solutions to congenital heart defects in children.

It goes on. And the point of the article (which I actually don’t disagree with) is that animal testing is necessary to save human lives. The subpoint, which is more debatable, is that scientists in these industries already do their best to minimize the suffering of animals where possible, and more regulation isn’t necessary. That point I don’t actually have an opinion on — so it’s great to see a view from inside the process from a dedicated scientist.

At the end of the article is this byline:

The byline identifies the author as chair of Americans for Medical Progress. It’s the sort of thing an perceptive student would select and search on, to find more about the source of the information. And it’s the kind of thing a majority of students wouldn’t notice or think about at all. What you notice above, however, is that we’ve already _pre-annotated this_ using our Hypothes.is-based bot.

The highlight calls the students eye to the name of the organization. Clicking the annotation brings up this:

The annotation displayed informs the student that this may be a front organization — an organization that attempts to appear independent but is really there to do the bidding of others. But it doesn’t solve it for the student — it invites the student to add to the investigation.

Clicking on the investigate link brings up a page that reveals, among other things, that [the organization is primarily run and funded by pharmaceutical companies](<http://www.sourcewatch.org/index.php/Americans_for_Medical_Progress>) and a large supplier of lab animals:

> AMP’s board of directors consists of senior executives and other representatives employed by the pharmaceutical and vivisection industries. They include [Charles River](<http://www.sourcewatch.org/index.php/Charles_River> "Charles River"), [Abbott Laboratories](<http://www.sourcewatch.org/index.php/Abbott_Laboratories> "Abbott Laboratories"), [GlaxoSmithKline](<http://www.sourcewatch.org/index.php/GlaxoSmithKline> "GlaxoSmithKline"), [Pfizer](<http://www.sourcewatch.org/index.php/Pfizer> "Pfizer"), [AstraZeneca](<http://www.sourcewatch.org/index.php/AstraZeneca> "AstraZeneca"), [Sanofi-Aventis](<http://www.sourcewatch.org/index.php/Sanofi-Aventis> "Sanofi-Aventis") and [Merck](<http://www.sourcewatch.org/index.php/Merck> "Merck"). [[2]](<http://www.sourcewatch.org/index.php/Americans_for_Medical_Progress#cite_note-2>) Charles River Laboratories is the world’s largest supplier of laboratory animals. It has been described as the “General Motors of the laboratory animal industry”. [[3]](<http://www.sourcewatch.org/index.php/Americans_for_Medical_Progress#cite_note-3>) Board members also represent universities and institutions receiving government grants for vivisection. Many corporations and institutions on AMP’s board have amassed a history of gross animal welfare violations in the United States and Europe and been the focus of animal, health, consumer and [human rights](<http://www.sourcewatch.org/index.php/Human_rights> "Human rights") advocates. See also sections 2 & 4 & SW articles on individual companies.

It follows with a list of animal welfare violations of the companies of the board members.

Is this believable? Reliable? We don’t know. SourceWatch, the source of the page on this organization, leans left and is a fairly anti-corporate site. But this gives the student enough search terms, context, and momentum to start their own investigation. Armed with these facts, we search Google for connections and find this Google book (from Springer, though students will not recognize publisher quality. The book explains the group was largely set up by the US Surgical Corporation which came under fire for the use of live dogs to demonstrate surgical staples:

Again, I don’t necessarily trust this, or think it’s cause to throw out the argument made in the column. But it’s a heck of a qualifier. So we add to the stub that the annotation bot has added a link to this reference, as a reply to the botted annotation:

In the annotation we link to the passage in the book directly, and add a link to citations of Garner’s work in Google Scholar, to show that he’s respected in this field.

More students can come, do more searches, and add more information. The process is similar to the process Wikipedia uses to generate “stubs” — we use publicly available resources plus automation to find work that needs to be done and provide a scaffold for starting it. Students can be graded on the strength of their contribution — either directly, or through conversation with other students to keep them impartial.

I’m pretty excited about this. It provides the sort of scaffolding and direction that students may need in this area while still allowing students to do authentic, public work.

What do you all think?
