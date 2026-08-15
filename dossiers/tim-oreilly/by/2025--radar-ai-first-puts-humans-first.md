---
title: "AI First Puts Humans First"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-05-28
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/ai-first-puts-humans-first/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# AI First Puts Humans First

## Full text

While I prefer “AI native” to describe the product development approach centered on AI that we’re trying to encourage at O’Reilly, I’ve sometimes used the term “AI first” in my communications with O’Reilly staff. And so I was alarmed and dismayed to learn that in the press, that term has now come to mean “[using AI to replace people](<https://www.fastcompany.com/91332763/going-ai-first-appears-to-be-backfiring-on-klarna-and-duolingo>).” Many Silicon Valley investors and entrepreneurs even seem to view [putting people out of work as a massive opportunity](<https://www.theguardian.com/commentisfree/2025/may/12/for-silicon-valley-ai-isnt-just-about-replacing-some-jobs-its-about-replacing-all-of-them>).

That idea is anathema to me. It’s also wrong, both morally and practically. The whole thrust of my 2017 book [_WTF? What’s the Future and Why It’s Up to Us_](<https://www.oreilly.com/tim/wtf-book.html>) was that rather than using technology to replace workers, we can augment them so that they can do things that were previously impossible. It’s not as though there aren’t still untold problems to solve, new products and experiences to create, and ways to make the world better, not worse.

Every company is facing this choice today. Those that use AI simply to reduce costs and replace workers will be outcompeted by those that use it to expand their capabilities. So, for example, at O’Reilly, we have primarily offered our content in English, with only the most popular titles translated into the most commercially viable languages. But now, with the aid of AI, we can translate _everything_ into—well, not _every_ language (yet)—dozens of languages, making our knowledge and our products accessible and affordable in parts of the world that we just couldn’t serve before. These AI-only translations are not as good as those that are edited and curated by humans, but an AI-generated translation is better than no translation. Our customers who don’t speak English are delighted to have access to technical learning in their own language.

As another example, we have built quizzes, summaries, audio, and other AI-generated content—not to mention AI-enabled search and answers—using new workflows that involve our editors, instructional designers, authors, and trainers in shaping the generation and the evaluation of these AI generated products. Not only that, we [pay royalties to authors](<https://www.oreilly.com/radar/the-new-oreilly-answers-the-r-in-rag-stands-for-royalties/>) on these derivative products.

But these things are really not yet what I call “AI native.” What do I mean by that?

I’ve been around a lot of user interface transitions: from the CRT screen to the GUI, from the GUI to the web, from the web on desktops and laptops to mobile devices. We all remember the strategic conversations about “mobile first.” Many companies were late to the party in realizing that consumer expectations had shifted, and that if you didn’t have an app or web interface that worked well on mobile phones, you’d quickly lose your customers. They lost out to companies that quickly embraced the new paradigm.

“Mobile first” meant prioritizing user experiences for a small device, and scaling up to larger screens. At first, companies simply tried to downsize their existing systems (remember Windows Mobile?) or somehow shoehorn their desktop interface onto a small touchscreen. That didn’t work. The winners were companies like Apple that created systems and interfaces that treated the mobile device as a primary means of user interaction.

We have to do the same with AI. When we simply try to implement what we’ve done before, using AI to do it more quickly and cost-efficiently, we might see some cost savings, but we will utterly fail to surprise and delight our customers. Instead, we have to re-envision what we do, to ask ourselves how we might do it with AI if we were coming fresh to the problem with this new toolkit.

Chatbots like ChatGPT and Claude have completely reset user expectations. The long arc of user interfaces to computers is to bring them closer and closer to the way humans communicate with each other. We went from having to “speak computer” (literally binary code in some of the earliest stored program computers) to having them understand human language.

In some ways, we had started doing this with keyword search. We’d put in human words and get back documents that the algorithm thought were most related to what we were looking for. But it was still a limited pidgin.

Now, though, we can talk to a search engine (or chatbot) in a much fuller way, not just in natural language, but, with the right preservation of context, in a multi-step conversation, or with a range of questions that goes well beyond traditional search. For example, in searching the O’Reilly platform’s books, videos, and live online courses, we might ask something like: “What are the differences between Camille Fournier’s book _The Manager’s Path_ and Addy Osmani’s _Leading Effective Engineering Teams_?” Or “What are the most popular books, courses, and live trainings on the O’Reilly platform about software engineering soft skills?” followed by the clarification, “What I really want is something that will help me prepare for my next job interview.”

Or consider “verifiable skills”—one of the major features that corporate learning offices demand of platforms like ours. In the old days, certifications and assessments mostly relied on multiple-choice questions, which we all know are a weak way to assess skills, and which users aren’t that fond of.

Now, with AI, we might ask AI to assess a programmer’s skills and suggest opportunities for improvement based on their code repository or other proof of work. Or an AI can watch a user’s progress through a coding assignment in a course and notice not just what the user “got wrong~~,~~ ” but what parts they flew through and which ones took longer because they needed to do research or ask questions of their AI mentor. An AI native assessment methodology not only does more, it does it seamlessly, as part of a far superior user experience.

We haven’t rolled out all these new features. But these are the kind of AI native things we are trying to do, things that were completely impossible before we had a still largely unexplored toolbox that daily is filled with new power tools. As you can see, what we’re really trying to do is to use AI to make the interactions of our customers with our content richer and more natural. In short, more human.

One mistake that we’ve been trying to avoid is what might be called “putting new wine in old bottles.” That is, there’s a real temptation for those of us with years of experience designing for the web and mobile to start with a mockup of a web application interface, with a window where the AI interaction takes place. This is where I think “AI first” really is the right term. I like to see us prototyping the interaction with AI _before_ thinking about what kind of web or mobile interface to wrap around it. When you test out actual AI-first interactions, they may give you completely different ideas about what the right interface to wrap around it might look like.

There’s another mistake to avoid, which is to expect an AI to be able to do magic and not think deeply enough about all the hard work of evaluation, creation of guardrails, interface design, cloud deployment, security, and more. “AI native” does not mean “AI only.” Every AI application is a hybrid application. I’ve been very taken with Phillip Carter’s post, [LLMs Are Weird Computers](<https://www.phillipcarter.dev/posts/llms-computers>), which makes the point that we’re now programming with two fundamentally different types of computers: one that can write poetry but struggles with basic arithmetic, another that calculates flawlessly but can’t interact easily with humans in our own native languages. The art of modern development is orchestrating these systems to complement each other.

This was a major theme of our recent AI Codecon [Coding with AI](<https://www.oreilly.com/radar/takeaways-from-coding-with-ai/>). The lineup of expert practitioners explained how they are bringing AI into their workflow in innovative ways to accelerate (not replace) their productivity and their creativity. And speaker after speaker reminded us of what each of us still needs to bring to the table.

Chelsea Troy [put it beautifully](<https://youtu.be/bg4z70cOOF4>):

> Large language models have not wholesale wiped out programming jobs so much as they have called us to a more advanced, more contextually aware, and more communally oriented skill set that we frankly were already being called to anyway…. On relatively simple problems, we can get away with outsourcing some of our judgment. As the problems become more complicated, we can’t.

The problems of integrating AI into our businesses, our lives, and our society are indeed complicated. But whether you call it “AI native” or “AI first,” it does not mean embracing the cult of “economic efficiency” that reduces humans to a cost to be eliminated.

No, it means doing more, using humans augmented with AI to solve problems that were previously impossible, in ways that were previously unthinkable, and in ways that make our machine systems more attuned to the humans they are meant to serve. As Chelsea said, we are called to integrate AI into  “a more advanced, more contextually aware, and more communally oriented” sensibility. AI first puts humans first.
