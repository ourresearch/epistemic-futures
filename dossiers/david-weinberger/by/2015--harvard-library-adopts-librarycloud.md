---
title: "Harvard Library adopts LibraryCloud"
person: david-weinberger
section: by
type: blog-post
year: 2015
date: 2015-01-07
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2015/01/07/harvard-library-adopts-librarycloud/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# Harvard Library adopts LibraryCloud

## Full text

According to a post by the Harvard Library, LibraryCloud is now officially a part of the Library toolset. It doesn’t even have the word “pilot” next to it. I’m very happy and a little proud about this.

LibraryCloud is two things at once. Internal to Harvard Library, it’s a metadata hub that lets lots of different data inputs be normalized, enriched, and distributed. As those inputs change, you can change LibraryCloud’s workflow process once, and all the apps and services that depend upon those data can continue to work without making any changes. That’s because LibraryCloud makes the data that’s been input available through an API which provides a stable interface to that data. (I am overstating the smoothness here. But that’s the idea.)

To the Harvard community and beyond, LibraryCloud provides open APIs to access tons of metadata gathered by Harvard Library. LibraryCloud already has metadata about 18M items in the Harvard Library collection — one of the great collections — including virtually all the books and other items in the catalog (nearly 13M), a couple of million of images in the VIA collection, and archives at the folder level in Harvard OASIS. New data can be added relatively easily, and because LibraryCloud is workflow based, that data can be updated, normalized and enriched automatically. (Note that we’re talking about metadata here, not the content. That’s a different kettle of copyrighted fish.)

LibraryCloud began as an idea of mine (yes, this is me taking credit for the idea) about 4.5 years ago. With the help of the Harvard Library Innovation Lab, which I co-directed until a few months ago, we invited in local libraries and had a great conversation about what could be done if there were an open API to metadata from multiple libraries. Over time, the Lab built an initial version of LibraryCloud primarily with Harvard data, but with scads of data from non-Harvard sources. (Paul Deschner, take many many bows. Matt Phillips, too.) This version of LibraryCloud — now called lilCloud — is still available and is still awesome.

With the help of the Library Lab, a Harvard internal grant-giving group, we began a new version based on a workflow engine and hosted in the Amazon cloud. (Jeffrey Licht, Michael Vandermillen, Randy Stern, Paul Deschner, Tracey Robinson, Robin Wendler, Scott Wicks, Jim Borron, Mary Lee Kennedy, and many more, take bows as well. And we couldn’t have done it without you, Arcardia Foundation!) (Note that I suffer from Never Gets a List Right Syndrome, so if I left you out, blame my brain and let me know. Don’t be shy. I’m ashamed already.)

The Harvard version of LibraryCloud is a one-library implementation, although that one library comprises 73 libraries. Thus the LibraryCloud Harvard has adopted is a good distance from the initial vision of a single API for accessing multiple libraries. But it’s a big first step. It’s open source code [documentation]. Who knows?

I think it’s impressive that Harvard Library has taken this step toward adopting a platform architecture, and it’s cool beyond cool that this architecture is further opening up Harvard Library’s metadata riches to any developer or site that wants to use it. (This also would not have happened without Harvard Library’s enlightened Open Metadata policy.)
