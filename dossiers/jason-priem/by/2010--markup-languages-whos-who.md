---
title: "Markup languages: who’s who?"
person: jason-priem
section: by
type: blog-post
year: 2010
date: 2010-04
venue: "jasonpriem.org (personal blog)"
authors: "Jason Priem"
source_url: https://web.archive.org/web/20141106185650/http://jasonpriem.org/2010/04/markup-languages-whos-who/
retrieved: 2026-08-13
content: full-text
notes: "Personal blog, defunct; retrieved from the Internet Archive Wayback Machine. Original URL: http://jasonpriem.org/2010/04/markup-languages-whos-who/"
---

# Markup languages: who’s who?

## Full text

[![markup languages timeline](http://jasonpriem.com/wp-content/uploads/2010/04/markup-comic-small-copy.jpg "markup languages timeline")](http://jasonpriem.com/wp-content/uploads/2010/04/markup-comic-small-copy.jpg)Is HTML XML?  This question came up in a conversation with Sarah and @k8lin, and ended up being harder than I thought it’d be.  There seems to be a fair amount of confusion on the topic, especially given the W3C’s recent abandonment of XHTML 2.0 and growing use of HTML5.

So, I decided to lay it all out in a (relatively) simple timeline format; as far as I know, this doesn’t exist anywhere else.  You’re welcome, The Internet.  Below are my sources and some notes; where possible, links are to the original recommendations or RFCs:

SGML is an [ISO](http://en.wikipedia.org/wiki/International_Organization_for_Standardization) standard [from the 80′s](http://en.wikipedia.org/wiki/Sgml#Standard_versions).  Unlike the other standards on this list, it’s not open (the ISO [sells copies](http://www.iso.org/iso/catalogue_detail.htm?csnumber=16387) for \>\$200).  [HTML is an “SGML application](http://www.w3.org/TR/html401/intro/sgmltut.html)“, and has been [from the beginning.](http://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt) The [Wikipedia article](http://en.wikipedia.org/wiki/Html#First_specifications) has a lot more information on its origins, as does the [W3C](http://www.w3.org/MarkUp/html-spec/).

[HTML 2.0](http://tools.ietf.org/html/rfc1866) and [HTML 3.2](http://www.w3.org/TR/REC-html32) , the first two W3C specs, are both pretty straightforward. Also straightforward is XML, which dropped in [February 1998](http://www.w3.org/TR/1998/REC-xml-19980210). Like HTML, XML is “an application profile…of SGML.”

In December 1999, the HTML 4.01 recommendation came out, followed a month later by XHTML 1.0.  The important thing to note *is that both of these are still HTML 4*; however, XHTML is [“a reformulation of HTML 4 as an XML 1.0 application,”](http://www.w3.org/TR/xhtml1/) while HTML 4.01 [is still plain ol’ SGML](http://www.w3.org/TR/html401/).

No one knows yet exactly what [HTML5](http://dev.w3.org/html5/spec/Overview.html) is going to look like, as it’s still several years off.  However, the W3C [tells us](http://www.w3.org/2009/06/xhtml-faq.html) that the HTML5, like HTML4, is going to have two different “serializations.”  One will be an XML syntax, and is currently being called XHTML 5 (wait, why not “XHTML 2?”  Hang on, we’ll get there). You might expect that the other serialization would be SGML a la HTML 4.01.  You’d be wrong.

Although HTML is technically SGML, most browsers and authoring tools couldn’t care less about the broader SGML standard; they just implement HTML.  So the W3C’s plan seems to be to [ditch the SGML legecy and replace it with “html”](http://www.w3.org/QA/2008/01/html5-is-html-and-xml.html) (note the lowercase), an entirely new standard…which happens to look pretty much like HTML has always looked.

Whew, we’re almost done.  OK, what about [XHTML2](http://www.w3.org/TR/xhtml2/)?  Despite the name, project was not a “next step;” it was a huge break with the whole HTML/XHTML tradition, an effort to completely remake web markup.  In July, the W3C decided to let it die on the vine and focus on HTML5.  So XHTML 5, with its HTML lineage, will be a more incremental change than XHTML 2 would’ve been.

There you have it.  If I missed anything or got something turned around, let me know.
