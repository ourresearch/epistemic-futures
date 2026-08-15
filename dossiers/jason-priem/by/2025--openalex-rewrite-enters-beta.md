---
title: "OpenAlex rewrite enters beta! 🎉"
person: jason-priem
section: by
type: blog-post
year: 2025
date: 2025-10-01
venue: "OpenAlex blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/openalex-rewrite-enters-beta-%f0%9f%8e%89/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.openalex.org."
---

# OpenAlex rewrite enters beta! 🎉

## Full text

It’s a big week at OpenAlex. On Monday, we announced that [OpenAlex is now our top-level brand](https://blog.openalex.org/were-now-openalex/) (and retired the “OurResearch” name). Yesterday we unveiled our [new logo](https://blog.openalex.org/were-now-openalex/). And today, we’re thrilled to launch the beta release of our fully-rewritten codebase (codenamed [Walden](https://www.reddit.com/r/minimalism/comments/3h7ot4/a_passage_from_henry_david_thoreaus_walden/))!

Walden is faster, bigger, and more maintainable–that means quicker bug fixes, more content, easier feature development, and a smoother experience all around.

Throughout October, we’ll be running Walden and the old system (Classic) side by side, with Classic remaining the default. On November 1 2025, Walden becomes default, and we’ll publish the last data snapshot from the old system ([more info on timelines here](https://blog.openalex.org/were-rebuilding-openalex-while-its-running-heres-whats-changing/)).

## **How to test-drive Walden**

Walden beta is already live in the API and UI so you can start exploring it right away!

- **In the UI**: click the little 🧪 test-tube icon in the top right (or [click here](https://openalex.org/?v2=true)).
- **In the API**: just add data-version=2 to your request, like this: <https://api.openalex.org/works?data-version=2>.
- **In [OREO](https://oreo.openalex.org/)**: Compare Classic to Walden using the OpenAlex Rewrite Evaluation Overview (OREO, yum). Using OREO you can see [exactly what’s changed](https://oreo.openalex.org/works/tests) (good and bad), view [known issues](https://oreo.openalex.org/known-issues), and [track our continuous improvements](https://oreo.openalex.org/changelog) throughout our October beta

Just remember that it’s still in beta: there are lots of known issues and it’s changing every day. If you notice an that’s not already in OREO tests or known issues, [report it here](https://oreo.openalex.org/known-issues).

## Key improvements

When you check it out, what should you expect to see? The best way to view a list of improvements is to check out the tests in [OREO](https://oreo.openalex.org/), especially [work tests](https://oreo.openalex.org/works/tests). But here’s a high-level overview:

- **150M+ new works:** Newly indexed articles, books, datasets, software, dissertations, and more! You can explore just the newly added works [here.](https://openalex.org/works?v2=true&page=1&filter=is_xpac:true)
- **Better consistency**: Unpaywall and OpenAlex will now always agree.
- **Better metadata**: more citations, more language and retraction coverage, better keywords, more OA data.

## **Looking Ahead**

The last year of rewriting OpenAlex was tough. We couldn’t move as fast as we wanted on new features, and support often lagged. But now we’re equipped to **move fast without breaking things**. Expect faster improvements, better support, and more ambitious features dropping in Q4, including:

- **Community curation**: fix mistakes (like in Wikipedia) and see them reflected in days.
- **Vector search endpoint**: find relevant works and other entities based on semantic similarity of free-form text
- **Download endpoint:** Access PDF text from DOI or OpenAlex ID
- **Better funding metadat**a: New grants entity with better coverage of grant objects and linkages to research outputs and funders

This is a turning point for OpenAlex—and we’re excited to build the future of research infrastructure together with you. The engine’s rebuilt. The road ahead is wide open. **Let’s go.**

PS want to learn more about Walden? Come to our webinar Oct 7th at 10am Eastern. You can register to attend [here](https://zoom.us/webinar/register/WN_POwr-xAQRx2ujF6hRbnivg).
