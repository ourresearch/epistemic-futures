---
title: "Paste & Cite"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2007
date: 2007-03-28
venue: "Louche Cannon (gbilder.com)"
authors: "Geoffrey Bilder"
source_url: "https://gbilder.com/blog/2007/03/paste-cite/"
retrieved: "2026-08-13"
content: "full-text"
notes: ""
---

# Paste & Cite

## Full text

I was recently asked by somebody to speculate about generalizable application features that might help researchers in their work. I responded to them directly, but thought it might be worth repeating part of my response here.

Since the early 1990s I’ve wished that the OS (any OS) would support a “Paste & Cite” feature and, now that I’m [involved](https://www.crossref.org/news/2006-12-05-geoffrey-bilder-to-join-crossref/) with [CrossRef](https://www.crossref.org/) and its linking and (nascent) plagiarism detection initiatives, I am even more convinced that such a feature would be immensely valuable to anybody who does research. The basic idea behind the feature would be that the clipboard would also copy “provenance” information whenever somebody chose to copy something. Then, when the user decided to paste the content someplace else, it would offer an optional “Past & Cite” menu item.

This is similar to [Ray Ozzie’s](https://en.wikipedia.org/wiki/Ray_Ozzie) concept of the [Live Clipboard](https://web.archive.org/web/20061117124343/http://rayozzie.spaces.live.com/blog/cns!FB3017FBB9B2E142!285.entry)– but I think it is simpler and with a different emphasis. The goal here is not to copy structured data around- it is to keep track of where it came from in the first place. In the simplest case, “Paste & Cite” would just paste in a URI pointing to the origin of the content (e.g. a local file, a file on an SMB share or a web page). This alone would help immensely with those situations where one “loses track” of where quoted text, copied pictures, etc. came from. Apparently a large number of semi- plagiarism cases stem from authors inadvertently losing track of the provenance of material that they copy and paste (with the best intentions of citing the material). In more sophisticated scenarios, the system would be opportunistic and “Paste & Cite” might make use of Dublin Core + PRISM metadata imbedded in HTML or XMP in PDFs/ Images or ID3 in mp3s, etc. Again the idea would be to give people a simple (possibly even simplistic) way of keeping track of the provenance of something. And of course- if a [DOI](https://www.doi.org/) were present, the provenance information could make use of it in order to ensure that the URI doesn’t break.

## Afterword (December, 2017)[#](#afterword-december-2017)

* Apple’s iBooks has a function like this now.
* I hope, that a proposed new [`cite-as` link relation type](https://tools.ietf.org/id/draft-vandesompel-citeas-00.html) will encourage more applications to provide this functionality with web resources.
