---
title: "“More Slowly”"
person: tim-oreilly
section: by
type: blog-post
year: 2025
date: 2025-06-25
venue: "O'Reilly Radar"
authors: "Tim O'Reilly"
source_url: https://www.oreilly.com/radar/more-slowly/
retrieved: 2026-08-13
content: full-text
notes: "Retrieved via the oreilly.com/radar WordPress REST API (people_taxonomy=tim-oreilly); HTML converted to markdown."
---

# “More Slowly”

## Full text

My friend David Eaves has the best tagline for [his blog](<http://eaves.ca>): “if writing is a muscle, this is my gym.” So I asked him if I could adapt it for my new biweekly (and occasionally weekly) hour-long video show on oreilly.com, [_Live with Tim O’Reilly_](<https://www.oreilly.com/products/new-live-online-sessions.html>). In it, I interview people who know way more than me, and ask them to teach me what they know. It’s a mental workout, not just for me but for our participants, who also get to ask questions as the hour progresses. Learning is a muscle. _Live with Tim O ’Reilly_ is my gym, and my guests are my personal trainers. This is how I have learned throughout my career—having exploratory conversations with people is a big part of my daily work—but in this show, I’m doing it in public, sharing my learning conversations with a live audience.

[My first guest, on June 3, was Steve Wilson](<https://learning.oreilly.com/live-events/building-secure-code-in-the-age-of-vibe-coding-steve-wilson-live-with-tim-oreilly/0642572189716/>), the author of one of my favorite recent O’Reilly books, [_The Developer’s Playbook for Large Language Model Security_](<https://learning.oreilly.com/library/view/the-developers-playbook/9781098162191/>). Steve’s day job is at cybersecurity firm Exabeam, where he’s the chief AI and product officer. He also founded and cochairs the Open Worldwide Application Security Project (OWASP) Foundation’s Gen AI Security Project.

During my prep call with Steve, I was immediately reminded of a passage in Alain de Botton’s marvelous book [_How Proust Can Change Your Life_](<https://www.alaindebotton.com/literature/>), which reconceives Proust as a self-help author. Proust is lying in his sickbed, as he was wont to do, receiving a visitor who is telling him about his trip to come see him in Paris. Proust keeps making him go back in the story, saying, “More slowly,” till the friend is sharing every detail about his trip, down to the old man he saw feeding pigeons on the steps of the train station.

Why am I telling you this? Steve said something about AI security that I understood in a superficial way but didn’t truly understand deeply. So I laughed and told Steve the story about Proust, and whenever he went by something too quickly for me, I’d say, “More slowly,” and he knew just what I meant.

This captures something I want to make part of the essence of this show. There are a lot of podcasts and interview shows that stay at a high conceptual level. In _Live with Tim O’Reilly_ , my goal is to get really smart people to go a bit more slowly, explaining what they mean in a way that helps all of us go a bit deeper by telling vivid stories and providing immediately useful takeaways.

This seems especially important in the age of AI-enabled coding, which allows us to do so much so fast that we may be building on a shaky foundation, which may come back to bite us because of what we only _thought_ we understood. As my friend [Andrew Singer](<https://dev.ecoguineafoundation.com/in-memoriam.html>) taught me 40 years ago, “The skill of debugging is to figure out what you really told your program to do rather than what you thought you told it to do.” That is even more true today in the world of AI evals.

“More slowly” is also something personal trainers remind people of all the time as they rush through their reps. Increasing time under tension is a proven way to build muscle. So I’m not entirely mixing my metaphors here. 😉

In my interview with Steve, I started out by asking him to tell us about some of the top security issues developers face when coding with AI, especially when vibe coding. Steve tossed off that being careful with your API keys was at the top of the list. I said, “More slowly,” and here’s what he told me:

As you can see, having him unpack what he meant by “be careful” led to a Proustian tour through the details of the risks and mistakes that underlie that brief bit of advice, from the bots that scour GitHub for keys accidentally left exposed in code repositories (or even the histories, when they’ve been expunged from the current repository) to a humorous story of a young vibe coder complaining about how people were draining his AWS account—after displaying his keys in a live coding session on Twitch. As Steve exclaimed: “They are secrets. They are meant to be secret!”

Steve also gave some eye-opening warnings about the [security risks of hallucinated packages](<https://youtu.be/HA-fbyyph6E>) (you imagine, “the package doesn’t exist, no big deal,” but it turns out that malicious programmers have figured out commonly hallucinated package names and made compromised packages to match!); some spicy observations on [the relative security strengths and weaknesses of various major AI players](<https://youtu.be/fwVVq5mC1p4>); and why [running AI models locally in your own data center isn’t any more secure](<https://youtu.be/mVX67oHBVq4>), unless you do it right. He also talked a bit about [his role as chief AI and product officer at information security company Exabeam](<https://www.youtube.com/watch?v=AW0YhTsuKoQ>). You can [watch the complete conversation here](<https://learning.oreilly.com/videos/building-secure-code/0642572018926/>).

[My second guest, Chelsea Troy](<https://learning.oreilly.com/live-events/chelsea-troy-live-with-tim-oreilly/0642572203368/>), whom I spoke with on June 18, is by nature totally aligned with the “more slowly” idea—in fact, it may be that [her “not so fast” takes](<https://learning.oreilly.com/videos/coding-with-ai/0642572017171/0642572017171-video386935/>) on several much-hyped computer science papers at the recent O’Reilly AI Codecon planted that notion. During our conversation, her comments about [the three essential skills still required of a software engineer](<https://youtu.be/ouMKcv07QC8>) working with AI, why [best practice is not necessarily a good reason to do something](<https://youtu.be/0RM2QCQ16M0>), and [how much software developers need to understand about LLMs under the hood](<https://youtu.be/gx3r4wIwh_w>) are all pure gold. You can [watch our full talk here](<https://learning.oreilly.com/videos/ai-and-developer/0642572020332/0642572020332-video390079/>).

One of the things that I did a little differently in this second interview was to take advantage of the O’Reilly learning platform’s live training capabilities to bring in audience questions early in the conversation, mixing them in with my own interview rather than leaving them for the end. It worked out really well. Chelsea herself talked about her experience teaching with the O’Reilly platform, and how much she learns from the attendee questions. I completely agree.

Additional guests coming up include [Matthew Prince](<https://en.wikipedia.org/wiki/Matthew_Prince>) of Cloudflare (July 14), who will unpack for us Cloudflare’s [surprisingly pervasive role in the infrastructure of AI](<https://www.justthink.ai/blog/cloudflare-the-secret-weapon-for-building-ai-agents>) as delivered, as well as his fears about [AI leading to the death of the web as we know it](<https://searchengineland.com/ai-killing-web-business-model-455157>)—and what content developers can do about it ([register here](<https://www.oreilly.com/live/live-with-tim-oreilly-a-conversation-with-matthew-prince.html>)); [Marily Nika](<https://en.wikipedia.org/wiki/Marily_Nika>) (July 28), the author of [_Building AI-Powered Products_](<https://www.oreilly.com/library/view/building-ai-powered-products/9781098152697/>), who will teach us about product management for AI ([register here](<https://www.oreilly.com/live/live-with-tim-oreilly-a-conversation-with-marily-nika.html>)); and [Arvind Narayanan](<https://en.wikipedia.org/wiki/Arvind_Narayanan>) (August 12), coauthor of the book [_AI Snake Oil_](<https://press.princeton.edu/books/hardcover/9780691249131/ai-snake-oil?srsltid=AfmBOoomtix-VDWW39hvK48jv7_TUrWdKrAspCXVGzrAoMjSYfybAz7X>), who will talk with us about his paper “[AI as Normal Technology](<https://knightcolumbia.org/content/ai-as-normal-technology>)” and what that means for the prospects of employment in an AI future.

We’ll be publishing a fuller schedule soon. We’re going a bit light over the summer, but we will likely slot in more sessions in response to breaking topics.
