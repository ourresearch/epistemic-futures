---
title: "Siderean – Trees, tags and facets"
person: david-weinberger
section: by
type: blog-post
year: 2005
date: 2005-09-16
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2005/09/16/siderean-trees-tags-and-facets/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# Siderean – Trees, tags and facets

## Full text

I met with Siderean‘s Robert Petrossian and Brad Allen a couple of days ago to hear about where the company is going. They’re up to some very interesting stuff that might both spread tagging and make it more useful. Siderean says it sells navigation software, by which they mean their stuff helps users navigate big, complex sets of information. At its heart, Siderean is a faceted classification provider. [Note: If you already understand faceted classification, skip the rest of this paragraph and the next.] FC is hard to explain without a demo, but here goes: Take a set of data with multiple categories of metadata, or, if you prefer, multiple columns. Expose to the user the categories plus the sets of values. E.g., a database of restaurants might have columns for type of food, review stars, and price ranges. The faceted system would show you all the values in each of those three categories of metadata. If you click first on “Price Range: Cheap,” you’ll see a list of all the restaurants that match that criterion. On the side there will be a list that lets you click on values in Review Stars or Types of Food. If there are no Cheap restaurants that have 5 stars, you simply are not given the 5-star option.

Whew. If you want to see faceted classification in action, the Resource Connection is a Siderean customer with a site you can try.

So, faceted classification lets users walk through a complex tree of data, choosing which branches, without ever coming to a branch with no leaves. The tree is not pre-computed. It constructs itself as the user decides first to go down this branch and then down that. That’s incredibly useful, especially as the data sets get large, because the owners of the information don’t have to dictate what the proper (= only) path through it is. Siderean has always allowed their customers to embed hierarchical trees within their faceted classification system when appropriate. E.g., if someone is navigating via the geography category, the system can know that SoHo is in NYC which is in NY state which is in the US. And Siderean has shown an early curiosity about tags: Its fac.etio.us thought-experiment/demo turns del.icio.us bookmarks into a faceted system. Now, I learned, future releases of their navigation software are going to incorporate tagging more directly, enabling users to annotate/tag the data they find. This is exciting not just because, culturally, tagging breaks the old assumption that the owners of information own the organization of that information, but also because a faceted system might add a right amount of organization to a pile of tags, making that pile far more useful. Imagine a folksonomic faceted system. Now draw it on a hyper-napkin and send it to me, because I have trouble imagining it. Of course, it all depends on the particularities of Siderean’s implementation… [Tags: EverythingIsMiscellaneous taxonomy siderean tags tagging]
