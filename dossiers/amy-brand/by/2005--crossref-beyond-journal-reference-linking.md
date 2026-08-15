---
title: "CrossRef: beyond journal reference linking"
person: amy-brand
section: by
type: journal-article
year: 2005
venue: "Serials The Journal for the Serials Community"
authors: "Amy Brand; Chuck Kosher"
doi: https://doi.org/10.1629/18199
openalex_id: https://openalex.org/W2051145108
source_url: https://doi.org/10.1629/18199
retrieved: 2026-08-14
content: full-text
notes: "UKSG Serials 18(3), November 2005; co-authored with Chuck Koscher (OpenAlex records the surname as 'Kosher'). Full text recovered from the journal's proof-galley PDF (https://serials.uksg.org/articles/874/files/submission/proof/874-1-874-1-10-20150210.pdf). Text extracted with pdftotext."
---

# CrossRef: beyond journal reference linking

## Full text

Serials – 18(3), November 2005

Amy Brand and Chuck Koscher

CrossRef: beyond journal reference linking

CrossRef: beyond journal reference linking
The CrossRef network today covers millions of journal
articles and other scholarly content from several hundred
academic publishers and societies. CrossRef launched in
early 2000 as a co-operative venture among publishers to
support persistent, industry-wide citation linking in
journals using the Digital Object Identifier, or DOI.1
In five-plus years of operation, CrossRef has grown steadily
in many dimensions, including the number of voting
members and participating publishers; the number of
journals covered; the types of content to which DOIs are
assigned; coverage of scholarly and professional disciplines;
usage by the research community; and overall technical
functionality. This article briefly surveys recent CrossRef
developments, focusing on functional enhancements to
the CrossRef system.

Beyond journal content
Approximately 10,000 new content objects are registered each day in the CrossRef metadata database.
As soon as a DOI is added to CrossRef, the item it
identifies becomes ‘visible’ for linking; that is,
thousands of other participating organizations –
publishers, intermediaries and libraries – that have
programmatic processes in place to query the
CrossRef system can now automatically retrieve a
link to that item.2 What can be assigned a DOI and
registered in the metadata database is defined by
CrossRef’s XML deposit schema. CrossRef initially
supported the registration of journal article metadata only, but the database has grown recently to
cover books, conference proceedings, working
papers, technical reports, and components such as
images and supplementary materials. The CrossRef
schema is currently undergoing another extension
and will soon support registration of theses, datasets and patents as well.
As of September 2005, CrossRef encompasses
over 400 voting members, 1,500 participating publishers and societies, 12,500 journals and 17.3 million
DOIs, including well over a million DOIs for nonjournal items. The 17.3 million DOIs registered
with CrossRef reflect the content deposits shown
in Table 1.

AMY BRAND
Director of
Business
Development

CHUCK
KOSCHER
Director of
Technology

CrossRef/PILA

Content type

No. of DOIs

Journals

15,975,523

Books
Conference proceedings
Components

279,138
1,036,275
3,917

Table 1.

Far fewer publishers (17) are currently registering books than journals, as many publishers have
only just begun to digitize their book publications,
and reference linking in books is still a relatively
new development. The 279,138 book DOIs in
CrossRef at this time come from 10,146 individual
book titles. Hence, the majority of these book DOIs
are being assigned at the more granular chapter
level. Figure 1 shows one of 65,000 DOIs assigned
to the entries within a single work, the Oxford
Dictionary of National Biography.
CrossRef began supporting deposit of components in late 2004, so that publishers could assign
DOIs to images, figures and other supplemental
information within a journal article. The American
Society for Clinical Investigation is one of three
publishers that have begun making component
deposits. Figure 2 contains an example of a DOI
assigned to supplementary information within a
Journal of Clinical Investigation article.

199

CrossRef: beyond journal reference linking

Amy Brand and Chuck Koscher

Serials – 18(3), November 2005

Figure 1. DOI assigned to reference work entry

Figure 2. Example of component DOI

The web deposit option
Most publishers deposit DOIs to CrossRef using an
XML-based batch upload process. In order to make
it possible for smaller publishers who may not
200

be tagging their publications in XML to participate
in CrossRef, CrossRef now offers a web deposit
interface for manual DOI registration. The system
automatically builds an XML deposit file from
metadata entered in the form shown in Figure 3.

Serials – 18(3), November 2005

Amy Brand and Chuck Koscher

CrossRef: beyond journal reference linking

Figure 3. CrossRef ’s web deposit form

The manual deposit option is available for conference proceedings and books as well as journal
articles.

Forward Linking
CrossRef was established to provide a uniform
approach to reference linking between publishers,
but the metadata deposited with CrossRef can
be applied to a variety of other services. Given
CrossRef’s mission to improve the accessibility of
scholarly content via reference linking, the most
natural next step is to provide a ‘cited-by’ service.
With Forward Linking, CrossRef delivers the DOIs
of articles that reference a particular target article.
Many publishers who already offered their readers
lists of citing articles from within their own platform can now extend those listings to the content
of other publishers. In addition, publishers of small
collections who may not otherwise have the
resources to offer any cited-by listings now have
an efficient and simple source for this data, one
that allows them to provide this feature to their
readers at a low cost and at a low level of technical
complexity.

As with the reference linking, the value of
CrossRef’s Forward Linking service will be truly
realized when the metadata repository grows large
enough to provide comprehensive coverage of
the literature. In the near term, the cited-by links
available through CrossRef are concentrated in the
subject areas of medicine and physics. As the
repository fills with more metadata, coverage will
expand in much the same way it has for the reference linking service.
After less than one year in operation, the repository already holds over 20 million cited-by relationships and has over 24 million waiting to be
resolved (that is, when the DOI of the citing article
has yet to be deposited with CrossRef). Over one
hundred publishers have opted in to the Forward
Linking service thus far. For many participating
publishers, CrossRef is already providing significant quantities of links. Figure 4 shows an article
from PLoS Biology that contains 22 CrossRef-enabled
cited-by links.3
Figure 5 illustrates how Blackwell delineates the
cited-by items provided through CrossRef from
those that are internal links to other Blackwell
content on the Synergy platform.

201

CrossRef: beyond journal reference linking

Amy Brand and Chuck Koscher

Figure 4. Forward Linking on the PLoS platform

Figure 5. Forward Linking on Blackwell Synergy platform
202

Serials – 18(3), November 2005

Serials – 18(3), November 2005

Amy Brand and Chuck Koscher

Multiple Resolution
Today’s web is built from countless numbers of
simple links, each of which points to the specific
location of a content object. Links break or become
inactive when an object is no longer available at its
original location. DOIs solve this problem by
replacing a hard-coded URL with a simple identifier that operates via redirection. Thus, the DOIbased URL remains unchanged and active even
though the location of the content may change.
Multiple Resolution takes this solution to a
higher dimension in which the DOI can now point
to more than one URL, such as different locations
of the same content or to related content items.
Multiple Resolution thereby provides a framework
to solve certain ‘appropriate copy’ problems.
CrossRef is currently modeling possible uses for
DOI Multiple Resolution. To date, these fall into
two categories: (1) a DOI linking to an interim page
that presents a list of available sources for the
content, and (2) a DOI that resolves to multiple
URLs for the same content, where the appropriate
URL is automatically selected, based on the
geographic location of the user.
Figure 6 illustrates the first case, showing how a
set of choices is presented to the reader who
arrives at this page after clicking on the reference
link. Here, the referring publication need not
‘know’ that multiple locations for the cited article
exist. Hence, changes to the list of sources can be
made without affecting the reference link itself.
The second application of Multiple Resolution
described above does not require the user to make

CrossRef: beyond journal reference linking

a selection after clicking on the DOI. Instead, the
selection will be made automatically based on the
reader’s geographic location. The motivating
scenario is the distribution of online scholarly
content to Chinese institutions. As a result of network configuration issues, Chinese subscribers
sometimes have difficulty accessing content that is
not within their native network infrastructure.
Readers attempting to navigate DOI-based reference links that only resolve to a non-native location
may otherwise experience a broken link. This is a
classic example of the well known ‘appropriate
copy’ problem.

CrossRef and OpenURL
The DOI and OpenURL are mutually supportive
technologies. CrossRef has long offered services
that support OpenURL-based resolvers and DOI
redirection for context-sensitive linking.4 More
recently, CrossRef has launched a NISO Z38.88 –
2004 compliant OpenURL resolver5 that requires
no login credentials for use. This means that institutions may now build links to the hundreds of
publisher platforms networked through CrossRef
using this single resolver address.
OpenURL is a syntax for metadata transport,
not a service. An OpenURL, like any URL, can be
viewed as having two parts, as shown in Figure 7.
The address identifies a service location and the
query string contains metadata that the service
at the location will understand. The OpenURL
standard defines the composition of the query

Figure 6. Multiple Resolution interim page
203

CrossRef: beyond journal reference linking

Amy Brand and Chuck Koscher

Serials – 18(3), November 2005

Figure 7. Sample OpenURL

string, while it is up to implementers to create
a service that knows what to do with the query
string. Without a service or resolver address,
OpenURLs do not function as links. Since
CrossRef has a central repository of over 17
million items from hundreds of publishers, it is
well positioned to offer a single physical address
to anyone wishing to resolve OpenURLs to
publisher platforms.

CrossRef’s impact
The success of CrossRef as a linking standard for
the scholarly and professional publishing community is perhaps best measured by its impact on
the research experience. DOIs are currently being
used at a rate of between eight and nine million
clicks per month, which translates roughly into

Figure 8. Growth in DOI clicks

204

280,000 end-user clicks per day. Figure 8 charts the
monthly growth in DOI resolutions from January
2002 to the present.
In summary, after five years CrossRef is well on
its way towards succeeding in its mission to connect online readers to primary research content by
providing a robust, accessible network of crosspublisher links. CrossRef will continue to grow its
coverage of scholarly and professional content and
its service offerings. In addition to the content-type
dimension, the linking network will expand along
three other key dimensions:
1. backwards in time, as publishers and institutions digitize archival material
2. to more granular levels, as DOIs get assigned to
various sub-parts of publications
3. via enhanced functionality of the DOI, as with
Forward Linking and Multiple Resolution.

Serials – 18(3), November 2005

Amy Brand and Chuck Koscher

CrossRef: beyond journal reference linking

The authors would like to thank Oxford University

References

Press, The American Society for Clinical Investigation,
1. For more information about the DOI, please go to:
http://www.doi.org
2. For a recent overview of CrossRef, the reader is

the Public Library of Science, Blackwell Publishing, and
GeoScience World, for use of screenshots containing
their proprietary content.

referred to Publishers Joining Forces through
CrossRef. Serials Review, 2004, 30 (1) 3–9.

Article © Amy Brand and Chuck Koscher

3. For an overview of Forward Linking and more
examples, please see:
http://www.crossref.org/02publishers/forward_
linking_howto.html
4. Please see:
http://www.crossref.org/03libraries/16openurl.
html for information on how CrossRef works with
the OpenURL.
5. Resolver is available at:

■ Amy Brand, Director of Business Development
Chuck Koscher, Director of Technology
CrossRef/PILA
40 Salem Street
Lynnfield, MA 01940, USA
Tel: 781-295-0072
Fax: 781-295-0077
E-mail: abrand@crossref.org

http://www.crossref.org/openurl

To view the original copy of this article, published in Serials, the journal of the UKSG, click here:
http://serials.uksg.org/openurl.asp?genre=article&issn=0953-0460&volume=18&issue=3&spage=199

For a link to the full table of contents for this article, please click here:
http://serials.uksg.org/openurl.asp?genre=issue&issn=0953-0460&volume=18&issue=3

205
