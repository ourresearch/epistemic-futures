---
title: "Prism: A Proposal for a Choral Approach to OER"
person: mike-caulfield
section: by
type: blog-post
year: 2016
date: 2016-06-02
venue: "Hapgood (hapgood.us)"
authors: "Mike Caulfield"
source_url: https://hapgood.us/2016/06/02/prism-a-proposal-for-a-choral-approach-to-oer/
retrieved: 2026-08-13
content: full-text
notes: ""
---

# Prism: A Proposal for a Choral Approach to OER

## Full text

If you’ve read [Choral Explanations](<https://hapgood.us/2016/05/13/choral-explanations/>), you know that I’ve proposed a new (well, as much as anything is ever new) approach to OER use and production that is based on trends in both wiki and question and answer sites. (If you haven’t read Choral Explanations, you can read it [here](<https://hapgood.us/2016/05/13/choral-explanations/>)).

In the time since I wrote that piece, I’ve kept coming back to it. And the more I look at it, the more I see a simple yet powerful idea at the center of it. I could be wrong, but I’m starting to feel there’s a huge opportunity here that is ripe for the taking. And unlike other stuff I’ve worked on (Wikity, federated wiki) it’s not that hard to build software around it. This post is going to attempt to outline how such software might work, and how it could dramatically change how we approach OER.

Grandiose enough? 😉

## Choral Explanations

Those who have not read Choral Explanations should go read it; this article assumes you have. But for those who have already read it (and those who will ignore this warning anyway) here’s the quick review of what I proposed in that piece.

In general, the way we often think of resources in a class is that we want to select the perfect piece to explain a concept to our students. So an OER provisioning process looks something like:

  * Identify course goals, objectives, assessments
  * Use course goals etc., to determine necessary content
  * Find best piece of open content for each content need
  * Sew these OER together in LMS or other software, sand down rough edges, publish.

What this misses is that people are often helped by having multiple explanations of concepts and issues available to them. The trend, for example, in question and answer sites over the last six years has been towards something I call (with a nod to Ward Cunningham) “the chorus”. These modern Q&A sites are based on the idea that there may be better and worse answers for individuals but we benefit when we have _access to a wide range of explanations and examples_ , because the explanation that may work for someone else may not work for someone else. (I cover this issue explicitly in my e-Literate piece [We Have Personalization Backwards](<http://mfeldstein.com/we-have-personalization-backwards/>)).

Again, this is meant only as a recap. Please read [Choral Explanations](<https://hapgood.us/2016/05/13/choral-explanations/>) for more detail on this. (In particular, you’ll need to understand what separates choral approaches from traditional forum approaches).

## OER and the Chorus

I have an expansive, mind-bending idea of where these efforts could go. But I want to tone it down to show you how simple Choral OER could be. Because really, it wouldn’t be hard at all. (Thanks to Lumen’s Bracken Mosbacker, who talked with me over Twitter DM last night, for talking me down in scale).

So imagine we create a Q&A style website that is designed around some simple question types:

  * What are some reasons why understanding Thing X is important?
  * What are some examples of Thing X in action?
  * What problems does Thing X solve?
  * What are some Y’s associated with Thing X?
  * What do we still not know about Thing X?

So given something like “unconscious bias” in a sociology of race module:

  * What are some of the reasons understanding unconscious bias is important?
  * What are some prominent or common examples of unconscious bias having negative effects?
  * What do we still not know about unconscious bias?

Multiple teachers take a stab at these, and they use the “choral” pattern we discusssed in Choral Explanations. So “what are some examples” might have five short posts under it, where a variety of teachers describe examples:

  * One discusses recent findings in hiring patterns.
  * Another describes a situation in Iowa schools where 98% of teachers are white, and white teachers are found to push black students less forcefully to excel.
  * A third recalls a story in the Gladwell book “Blink” where a cop makes a split second decision and shoots an unarmed man. It’s later shown that cops think a fraction of a second less before pulling the trigger on black suspects than they do on whites — even if the officer is black herself.

You can link directly to these questions from your course, or spend a fun day answering them (I’m not being sarcastic — these sorts of things are fun if you like the subject; much more fun than writing a textbook!).

In my dream world, sites like this start becoming the protoplasm out of which OER gets made, by both students and teachers. But here’s where Bracken thoughtfully slows me down — how could we leverage existing OER to build this community in a smaller way?

## Choral Sidebars

Here’s a simpler case.

Take a textbook on Biology. Let’s take a chapter on mitosis, since I realized yesterday I know stunningly little about mitosis, and tried to learn a bit more. Here’s a textbook page from Lumen’s online version of OpenStax’s Introductory Biology text:

OK, lets mock this up a bit. Let’s replace the media link with something we’ll call “Insights and Perspectives”, which links to our imaginary software product “Prism”:

When you click one of these links as a student, you get the choral explanation. Each explanation is a different route to understanding, complete in itself, but along with the other explanations forms a sort of 360 degree view of the question.

For instance, here’s some entries on _Why Mitosis Matters_ , which I’ve mocked up based on a simplified version of Quora’s design, shamelessly rebranded (we’re just going for general effect here).

This is a quick mockup, but you see how it works. Instuctors (and perhaps students eventually as well) answer these questions, but not in wiki form. Instead, the array of answers provides multiple ways into the material for the student.

These explanations are rated up by other answer authors (for accuracy) and by students (for usefulness). The ideal answer is accurate and useful to students, but the rating there only changes the position of the question in the scroll.

I think this example, although contrived, starts to show the sort of areas this approach could excel. While I was trying to learn mitosis yesterday night, I was just zoning out as I read it (much like a student). I didn’t have a route in, a way to connect previous knowledge to new knowledge to make the slog easier or more engaging.

I found these two examples gave me a way in. Chemotherapy, because I lost my father to cancer a number of years back now, and I remember what those drugs did to him, and I couldn’t stop wondering why they couldn’t make a drug that didn’t make you nauseous or lose your hair, and make you such a shell of your former self in your last days. And it turns out the answer is not quite “Oh, well the drug is poisoning you but poisoning the cancer faster.” which is what everybody tells you. It turns out a much more precise answer deals with mitosis.

So one reason why we want to understand mitosis better is we could make drugs that work better or make people suffer less.

Another thing I found engaging was the issue of Alzheimer’s. I actually don’t have personal experience with Alzhiemer’s, apart from a great aunt who died when I was young. But I’m a bit of a political junkie, and I remember the whole stem cell debate and its relation to abortion. And I remember Nancy Reagan, based on Ronald Reagan’s Alzheimer’s disease, came out for supporting stem cell research.

Well, why is that so important for Alzheimer’s? It turns out that nerve cells are “amitotic”: they don’t undergo mitosis. And they don’t even have the machinery to do so — they are missing the centrioles that would begin the process of pulling a single cell into two cells. So when your neurons get damaged, whether as part of a mental disease such as Alzheimer’s or an injury that takes away the feeling in your hand, nerves don’t grow back. This is different from when you cut your finger and you get new skin, for example.

Stem cells are important because they can divide, multiply and turn into _new_ nerve cells. That fact connects into my previous political interest and knowledge.

So these two examples are perfect for me, but the idea would be there would be a dozen other examples that might not be. I just look through them as a student until I find the one that really sticks.

There’s little things here we could borrow from Quora and other Q&A sites. Real names. Micro-biographies that attempt to answer the question “Why should you trust me?” View counts to remind contributors of how much their answer has helped students or been reused by professors in their courses.

## Instructor/Author View

Instructor/Author view would be a bit different. Here’s how it might work.

The instructor gets the book with these links in it. They click through to the link and look at the examples. But because they have an account, if they don’t like the examples or have a better one they are asked to contribute it:

If you want to add your answer, you click there and add it.

This starts to get instructors and students contributing to open textbooks without having to edit the main narrative of the text. When editing the main narrative of the text, the many voices can sound incoherent, with Prism, the many voices and perspectives becomes a strength. And with the process of supplementing the text in this way made this easy, we might finally begin to up the rates of profs extending and remixing OER.

## Sustainability Model?

Sustainability with projects that are about fostering a commons is always hard. They don’t call it “The Tragedy of the Commons” for nothing. So what I propose here is meant to be a pass at how this might be sustained, and I’m hoping people might have better ideas as well.

To my way of thinking, the instructor piece gives us a possible business model. All text on Prism would be CC-BY. Use of Prism would be free.

But instructors might want to write answers that they don’t share with the general public, but just with their class. Or they might want to customize the answers their students see. Or perhaps they’d want to see the answers that their particular students found most helpful. A small per class charge for these features, even if it was paid for by only a fraction of those using it, could finance the operation of the central site, just as those on GitHub wishing for private repositories subsidize the activities of those using open repositories.

You’d probably also have to put some poison pills in the architecture, functionality, or governance of the site so that you’d be sure the company or foundation running it would not pull a Flat World Knowledge on everybody. But if you could make sure that the content on it would always be free and forkable, it could eventually also become the OER protoplasm site I dream of, where you say “What are the questions we need to answer with content in this course?”, upload them to the site, and watch as hundreds of teachers and students from across the country slowly build your course for you.

Failing that?

You could try to do this through a consortium/association, such as AASCU or AAU. I haven’t seen this sort of thing work yet, but one could try.

Another approach might be for a university to build and maintain this, with enough grant funding or consortial support that people would believe that the project would be safe from the vicissitudes of university budgeting.

Finally, why not a state government in the U.S. (or a country or province elsewhere)? There are actually a number of funded OER initiatives that could attempt to pin a service like this on. There’s the freeloader problem, but it’s probably far cheaper to open your doors and let the world write your textbooks than fund them yourself. In a recent study of WSU we found that eliminating textbooks from our top 7 freshmen-enrolled classes would save our students something like $1 million a semester. Across all of Washington, of course, the savings would be much higher. Surely even a sliver of this money could support such a site?

But for now, we don’t even need a huge plan or a huge site. We need a relatively simple site, plugged into existing OER, and managed by a government, non-profit or ethical corporation, just to see if this can work. Can we all build this please?
