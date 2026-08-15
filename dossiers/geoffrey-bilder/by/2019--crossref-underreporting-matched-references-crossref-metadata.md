---
title: "Underreporting of matched references in Crossref metadata"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2019
date: 2019-02-05
venue: "Crossref blog"
authors: "Geoffrey Bilder"
source_url: "https://www.crossref.org/blog/underreporting-of-matched-references-in-crossref-metadata/"
retrieved: "2026-08-13"
content: "full-text"
notes: "Crossref blog post. DOI 10.64000/esvws-a7b66."
---

# Underreporting of matched references in Crossref metadata

## Full text

**4 minute read.**

## Underreporting of matched references in Crossref metadata

## TL;DR

About 11% of available references in records in our OAI-PMH & REST API don’t have DOIs when they should. We have deployed a fix, but it is running on billions of records, and so we don’t expect it to be complete until mid-April.

Note that the Cited-by API that our members use appears to be *unaffected* by this problem.

## The gory details

When a Crossref member registers metadata for a publication, they often include references. Sometimes the member will also include DOIs in the references, but often they don’t. When they don’t include a DOI in the reference, Crossref tries to match the reference to metadata in the Crossref system. If we succeed, we add the DOI of the matched record to the reference metadata. If we fail, we append the reference to an ever-growing list which we re-process on an ongoing basis.

You may have seen that [the R&D team has been doing work to improve our reference matching system](https://doi.org/10.64000/e6ey2-wce96). We will soon be rolling out a new reference matching process that will increase recall significantly.

But while testing our new reference matching approach, we started to see inconsistent results with our existing legacy reference matching system. When we implemented new regression tests, we noticed that, even when using our legacy system, we were consistently getting *better* results than were reflected in the metadata we exposed via our APIs. For example, we would pick a random Crossref DOI record that included 3 matched references, and when we tried matching all the references in the record again using our existing technology, we would get *more* matched references than were reported in the metadata.

At first, we thought this might have something to do with sequencing issues. For example, that article *A* might cite article *B*, but somehow article *A* would get its DOI registered with Crossref prior to article *B*. In this theoretical case, we would initially fail to match the reference, but it would eventually get matched as we continued to reprocess our unmatched references. But this wasn’t the issue. And the problem was not with the matching technology we are using. Instead, we discovered a problem with the way we process references on deposit.

When a member deposits references with Crossref, each reference has to include a member-defined key that is unique to each reference they are depositing in the DOI record. When we match a reference- we report to the members that we matched the reference with key X to DOI Y. The problem is that sometimes members would deposit references with an empty key. If there was only one such reference, then, technically, it would pass our test for making sure the key was unique within the record. So we would process the reference, and match it, and report it via our Cited-by service, but later in the process, when we went to include the matched DOI in the reference section of our API metadata, we’d skip including DOIs for references that had blank keys. The reference itself would be included in the metadata, it would just appear that we hadn’t matched it to a DOI when we actually had.

Again, we estimate this to have resulted in about 11% of the references in our metadata to be missing matched DOIs. We are processing our references again and inserting the correctly matched DOIs in the metadata. We expect the process to complete in mid-April. We will keep everybody up-to-date on the progress of this fix.

We will also be integrating the new matching system that we’ve developed. As mentioned at the start of this post, this matching system will also increase the recall rate of our reference matching and so, the two changes combined, should result in users seeing a significant increase in the number of matched references included in Crossref metadata.

And finally, as part of the work that we are doing to improve our reference matching, we are putting a comprehensive testing framework that will make it easier for us to detect inconsistencies and/or regressions in our reference matching.

Please contact [Crossref support](mailto:support@crossref.org) with any questions or concerns.
