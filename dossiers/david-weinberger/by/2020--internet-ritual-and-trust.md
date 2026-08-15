---
title: "Internet Ritual and Trust"
person: david-weinberger
section: by
type: blog-post
year: 2020
date: 2020-02-15
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2020/02/15/ritual-internet-and-trust/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# Internet Ritual and Trust

## Full text

Well, here are two things I never heard of before. First:

Through this intriguing Register report I learned about the DNSSEC root-signing ceremony. It happens quarterly in alternating fashion on the east and west coasts of the US. The carefully scripted ceremony, lasting over two hours, is meant to anchor the web of trust in the DNS, the Internet’s domain name system. To this end it is streamed live and archived for posterity.

So writes Keith Dawson (twitter) in a post on the A Recovering Physicist blog.

Then he notes the resemblance to the second thing:

Reading about this modern ceremony, performed quarterly for 10 years now, immediately put me in mind of a similar ritual, the Trial of the Pyx, staged in London for 738 years, for a substantially similar purpose: anchoring trust in the English currency.

I’d bet against either of these on a “Bluff the Listener” game on Wait Wait Don’t Tell me. But they’re both real.

Here’s some information about the DNSSEC ceremony, taken from the post Keith links to:

The root DNS zone contains information about how to query the top-level domain (TLD) name servers (.com, .edu, .org, etc). It enables Internet users to access domain names in all TLDs, even brand new ones like .software and .bank, making it an integral part of the global Internet.

In How DNSSEC Works, we explained how trust in DNSSEC is derived from the parent zone’s DS resource record. However, the root DNS zone has no parent, so how can we trust the integrity and authenticity of its information?

The article ably describes the trust systems involved, which include trusted institutions and individuals, redundancy, and encryption. And ceremony.

Trust won’t anchor itself.

(Actually that’s quite contestable.)
