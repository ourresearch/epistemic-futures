---
title: "New Features and Usage-Based Pricing"
person: jason-priem
section: by
type: blog-post
year: 2026
date: 2026-02-24
venue: "OpenAlex blog"
authors: "Jason Priem"
source_url: https://blog.openalex.org/openalex-api-new-features-and-usage-based-pricing/
retrieved: 2026-08-13
content: full-text
notes: "Byline from WordPress author field (user 'jason') on the merged Impactstory/OurResearch/OpenAlex blog. Originally published on blog.openalex.org."
---

# New Features and Usage-Based Pricing

## Full text

Today we’re adding some features to the OpenAlex API: better search, content download, and new docs. Most importantly, we’re also introducing usage-based pricing.

## **New features**

### **Advanced search at last**

We’ve had lots of request for advanced search features to support systematic reviews. Good news: they’re here!

- **Proximity search**: find terms near each other
- **Exact matching**: skip stemming when you need precision
- **Wildcards**: for when you’re not sure of the exact form
- **Lonnnnng queries**: Searches can be up to several pages in length (8kb)

Find details and examples of advanced search in the [new developer docs here](https://developers.openalex.org/guides/searching).

*Note for developers: the old filter syntax for search is now deprecated; the ?search= parameter approach remains. It’ll be the [One Way To Do It](https://peps.python.org/pep-0020/) moving forward. Filter searches will redirect to the ?search param.*

### **Semantic search**

We’re also launching semantic search. Instead of just matching keywords, it uses embeddings to match the meaning of your search–so a search for “[kelp biomechanics](https://openalex.org/works?page=1&search.semantic=kelp+biomechanics&sort=relevance_score:desc)” also finds articles about algae and wave mechanics. But you don’t have to stop there: you can even paste a whole abstract into the search bar to find related papers!

Semantic search is in beta; we don’t recommend using it for sensitive production workflows yet. But we would love to hear your feedback! If it’s well-used we’ll continue to invest more resources into it.

### **Full-text downloads**

We’re hosting PDFs and [TEI XML](https://tei-c.org/release/doc/tei-p5-doc/en/html/SG.html) for our 60M open-access works. You can search and filter for works of interest, filter to get just ones with PDFs, and then download the PDFs in bulk—all with the API. Or you can use our new [OpenAlex CLI](https://pypi.org/project/openalex-official/) to do it from the command line, massively parallelized, in a single command. Or your agent can—they love CLIs.

``` wp-block-code
openalex download \ 
  --api-key YOUR_KEY \ 
  --output ./climate-pdfs \ 
  --filter "topics.id:T10325,has_content.pdf:true" \ 
  --content pdf
```

See the [full-text documentation](https://openalex.mintlify.app/download/full-text-pdfs) for details.

### **New docs**

We’ve completely rebuilt our [documentation](https://openalex.mintlify.app/). The old docs are deprecated and will redirect soon. The new docs are clearer, cleaner, up to date, and AI-optimized. We want to make OpenAlex as easy as possible to use for everyone, whether they’re an expert or a novice vibe-coding their first app.

### **API keys are now required.**

As [we announced in January](https://groups.google.com/g/openalex-users/c/rI1GIAySpVQ), you’ll need an API key for all requests. Getting one is free and takes about 30 seconds: create an account at [openalex.org](https://openalex.org/), then grab your key at [openalex.org/settings/api](https://openalex.org/settings/api). You can still make a few calls without an API key for demo purposes, but it’s not suitable for any kind of production use. The API keys are essential for our new usage-based pricing model. What’s a usage-based pricing model? Gentle Reader, a mere centimeter now separates you from the answer. 👇

## **Usage-based pricing**

Different API operations cost us different amounts to run. Doing stuff with PDFs is expensive, but looking up a single work by ID is nearly free. We think it’s essential that our pricing reflects these actual costs. Usage-based pricing is a natural fit for this: it’s transparent, sustainable, and fair.

Here’s what things cost. See [the developer docs](https://developers.openalex.org/) for more details.

|                                 |                   |                          |
|---------------------------------|-------------------|--------------------------|
| **endpoint**                    | **cost per call** | **cost per 1,000 calls** |
| single work lookup by DOI or ID | 0                 | 0                        |
| list and filter                 | \$0.0001          | \$0.10                   |
| search                          | \$0.001           | \$1.00                   |
| PDF/XML download                | \$0.01            | \$10.00                  |

### **Free usage**

Every API key gets **\$1 of free usage per day**. We’ve always subsidized free users using revenue from paying ones–this makes the exact extent of that subsidy clear, transparent, and unambiguous.

What does that daily dollar get you? Assuming you return 100 works per request:

|  |  |  |
|----|----|----|
| **endpoint** | **daily free calls** | **daily free results** |
| single work lookup by DOI or ID | [unlimited](https://en.wikipedia.org/wiki/Limitless_(film))  | unlimited |
| list and filter | 10,000 | 1,000,000 |
| search | 1,000 | 100,000 |
| PDF/XML download | 100 | 100 |

To use a real-world example: grabbing all 694k works by Finnish authors takes about 7k paginated requests at \$0.10 per thousand or \$0.70. That’s covered by your free daily allowance. But if you want all 9 million works from Japan, that will cost about \$9. (You could even download all 480M works in OpenAlex this way for \$480—but don’t do that lol, [download the full dataset](https://openalex.mintlify.app/download/download-to-machine) instead, it’s free).

It’s easy to track your usage: every API response includes headers showing how much you’ve spent and how much you’ve got left. You can also check [openalex.org/settings/usage](https://openalex.org/settings/usage) anytime.

### **Prepaid usage**

Most users will find that the free plan covers all their needs. However, for some projects, you may need more usage. The great thing about usage-based pricing is that most of the time this will only cost you a few bucks. You’re just paying for what you need. You can [buy prepaid usage](https://openalex.org/pricing) in 1min with your credit card, whenever you want, however much you want. It supplements your daily free allowance.

### **Organizational plans**

Organizations also buy prepaid usage. But many will want to get annual plans instead, which offer major discounts, data sync, curation dashboards, and more. Check out our new [Member, Member+, and Supporter](https://openalex.org/pricing) plans for more details.

## **FAQ**

**I thought it was free?** The data remains free. The [full OpenAlex dataset](https://developers.openalex.org/download/download-to-machine)—all 480M works, all the metadata—is free to download, share, remix, and build on. We’re committed to keeping it sustainably free by charging for a service (the API) built on that dataset. Free data, paid service–this is the path laid out in the [POSI principles](https://openscholarlyinfrastructure.org/), which [we’ve signed and enthusiastically support](https://blog.openalex.org/posi/). 

**How do I track my usage?** Every API response includes usage info; you can also call the rate-limit endpoint or check [your usage page](https://openalex.org/settings/usage) on openalex.org. [Learn more here](https://developers.openalex.org/api-reference/authentication#keeping-tabs-on-costs). 

**How is my usage data used?** We analyze usage data to improve the overall service and we provide institutions aggregated usage summaries for their institutions upon request. We only collect what we need to run OpenAlex. We aren’t building tools to monitor individuals and we don’t sell your data. You can read our full privacy policy [here](https://openalex.org/OpenAlex_privacy_policy.pdf).

**Why charge per request instead of per result?** We’re trying to link our costs to our pricing, and our costs mostly scale with requests, not results; a search that returns 10 results costs us about the same as one that returns 10,000.

**Will prices change?**

Yes, probably. The point of this model is to keep our prices tightly linked to our costs, and our costs will likely change with new tech, new use cases, and new data.

## **Where from here?**

AI accelerates every day. The future of knowledge is getting rebuilt, right now. If we build on checkerboards of [enclosed](https://en.wikipedia.org/wiki/Enclosure), walled gardens, we build a fragmented, incoherent future for scholarship and humanity.

We think OpenAlex can help with that. We’re gathering and connecting the literature into a cohesive living library, complete and organized and accessible to everyone. Today’s new pricing model helps us stay in this for the long haul.

An *API-based* sustainability model lets us deliver (and monetize) value in the *post-GUI* era. Soon, users won’t go to openalex.org (or any SaaS website), they’ll use APIs to vibe-code a custom interface for any question in minutes. \[1\] The post-GUI world will be [tough on some open sustainability models](https://github.com/tailwindlabs/tailwindcss.com/pull/2388#issuecomment-3717222957). But it’s also an amazing opportunity for [open infrastructure](https://openscholarlyinfrastructure.org/), if we adapt our pricing model correctly. That’s what we’re doing today.

We’re so very excited about this next chapter. Questions? Hit us up at support@openalex.org.

Let’s build!

\[1\] Check out our [Q1 town hall](https://www.youtube.com/watch?v=q9KF_eARJaY) for more on our post-GUI strategy, and check out [this vibe-coding webinar](https://www.youtube.com/watch?v=BX5qFM8j9MU&t=9s) to see several real-life examples of building five-minute custom OpenAlex dashboards.
