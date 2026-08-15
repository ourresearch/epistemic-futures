---
title: "NLM Blog Citation Guidelines"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2007
date: 2007-10-15
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/nlm-blog-citation-guidelines/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/xzyk4-gap48."
---

# NLM Blog Citation Guidelines

## Full text

**4 minute read.**

## NLM Blog Citation Guidelines

[I’ve just returned from Frankfurt Book fair and noticed that there has been some recent](http://www.boingboing.net/2007/10/12/howto-cite-blogs-in.html) in the [The NLM Style Guide for Authors, Editors and Publishers](http://www.ncbi.nlm.nih.gov/books/bookres.fcgi/citmed/frontpage.html) recommendations concerning [citing blogs](http://www.ncbi.nlm.nih.gov/books/bv.fcgi?rid=citmed.section.61024).

Which reminds me of an issue that has periodically been raised here at Crossref- should we be doing something to try and provide a service for reliably citing more ephemeral content such as blogs, wikis, etc.?

Personally, I cringe when I see people include plain old URLs (POUs?) in citations. What’s the point? They are almost guaranteed to [fail to resolve](http://en.wikipedia.org/wiki/Link_rot) after a few years. In citing them, you are hardly helping to preserve the scholarly record. You might as well just record the metadata associated with the content.

So why don’t we simply allow individuals to assign DOIs to their content?

As Chuck Koscher says, “Crossref DOIs are only as persistent as Crossref staff.” Crossref depends on its ability to chase down and berate member publishers when they fail to update their DOI records. Its hard enough doing this with publishers, so just imagine what it would be like trying to chase down individuals. In short, it just wouldn’t scale.

But what if we provided a different service for more informal content? Recently we have been in talking with Gunther Eysenbach, the creator of the very cool [WebCite](http://www.webcitation.org/) service about whether Crossref could/should operate a citation caching service for ephemera.

As I said, I think WebCite is wonderful, but I do see a few problems with it in its current incarnation.

The first is that, the way it works now, it seems to effectively leech usage statistics away from the source of the content. If I have a blog entry that gets cited frequently, I certainly don’t want all the links (and their associated [Google-juice](http://en.wikipedia.org/wiki/Google_juice)) redirected away from my blog. As long as my blog is working, I want traffic coming to my copy of the content, not some cached copy of the content (gee- the same problem publishers face, no?). I would also, ideally, like that traffic to continue to come to to my blog if I move hosting providers, platforms (WordPress, Moveable Type) , blog conglomerates (Gawker, Weblogs, Inc.), etc.

The second issue I have with WebCite is simpler. I don’t really fancy having to actually recreate and run a web-caching infrastructure when there is already a [formidable one](http://www.archive.org/index.php) in existence.

So what if we ran a service for individuals that worked like this:

1. For a fee, you can assign DOIs to your ephemeral, CC-licensed content.
2. When you assign a DOI to an item of content (or update an existing DOI), we will immediately archive said content with the Internet Archive (who, incidentally, [charges for this service](http://www.archive-it.org/))
3. We will direct those DOIs to your web site as long as you are both:
4. Paying the fee
5. Updating your URLs to point to the correct content
6. If you fail in either “a” or “b”, we will then redirect said DOIs to the cached version of the content on the Internet Archive (after having warned you repeatedly via automated e-mail).

(Note, as an aside, that we could in theory provide a similar dark-archive service for publishers with non free content using something like JStore as the archive)

This approach would help to ensure that a blogger’s version of content was always linked to as long it was available. It would also preserve the “persistence” of Crossref DOIs by making sure that we could always resolve the DOI even if we were not able to get the owner of said DOI to update it.

So back to the NLM guidelines… On the one hand, I’m delighted to see that the NLM has issued guidelines on citing blogs. It seems glaringly obvious that informal (and ephemeral) content such as blogs and wikis are increasingly becoming vital parts of the scholarly record. On the other hand, it also seems to me that recommending that somebody “cite” with a broken pointer (i.e. a URL) to content verges on tokenism. This isn’t the NLM’s fault- there just isn’t a reliable mechanism for citing informal content in a manner that ensures you can then retrieve and look at said content in the future.

And this is no longer a problem confined to the Scholarly/Professional publishing space. As Jon Udell has occasionally [pointed out,](http://blog.jonudell.net/2007/01/29/the-persistent-blogosphere/) citation is increasingly an important currency for \*any\* professional writer on the web. It seems to me that a system for reliably citing blogs and wikis would benefit many communities. I could easily see commercial hosted Blog services (Blogger, WordPress) offering a “Cached-DOI” feature as a premium service to their clients.

So what do you think? What am I missing? is this something we should be looking at?
