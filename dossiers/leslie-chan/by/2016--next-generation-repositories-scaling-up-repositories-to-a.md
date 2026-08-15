---
title: "Next generation repositories: Scaling up repositories to a global knowledge commons"
person: leslie-chan
section: by
type: journal-article
year: 2016
date: 2016-06-26
venue: "Open Research Online - ORO (The Open University)"
authors: "Kathleen Shearer; Elóy Rodrigues; Andrea Bollini; Alberto Cabezas; Donatella Castelli; Leslie Carr; Leslie Chan; Chuck Humphrey; Rick Johnson; Petr Knoth; Paolo Manghi; Lazarus Matizirofa; and 7 others"
source_url: http://hdl.handle.net/1822/55027
retrieved: 2026-08-13
content: full-text
notes: "OpenAlex W2805339261; OA status: green. Full text retrieved from the OpenAlex Content API copy of W2805339261 (grobid_xml)."
---

# Next generation repositories: Scaling up repositories to a global knowledge commons

## Full text

## Abstract

Eric van de Velde: "Institutional Repository (IR) is obsolete. Its flawed foundation cannot be repaired. The IR

Eric van de Velde: "Institutional Repository (IR) is obsolete. Its flawed foundation cannot be repaired. The IR

But… repository systems are using old technologies developed over 15 years ago that do not support the functionalities we need.

Major strategic priority for COAR Working Group launched in April 2016 Aim: to identify functionalities and architectures for the next generation repositories within the context of scholarly communication

### Next Generation Repositories

User stories Types of metadata: descriptive and activity

• ResourceSync • Signposting • ETag • HTTP Signatures • IPFS • ORCID • OpenID Connect • Activity Streams 2.0 • SUSHI • SWORD •Sitemaps • Social Network Identities • Web Annotation Model & Protocol • WebID • WebID/TLS • WebSub • Webmention • IIIF • COUNTER • Creative Commons Licenses

### User stories and priority areas

• Discovering metadata that describe a scholarly resource • Discovering the identifier of a scholarly resource • Discovering usage rights • Resource syncing and notification • Recognizing the user • Commenting & annotating • Providing a social notification feed • Recommender systems for repositories • • Discovering metadata that describe a scholarly resource • Discovering the identifier of a scholarly resource • Discovering usage rights • Resource syncing and notification • Recognizing the user • Commenting & annotating • Providing a social notification feed • Recommender systems for repositories • Preservation • Peer-review • Comparing usage Three vertical discovery mechanisms »Batch -Transferring bulk data »Navigation -Helping robots to find resources in repositories by means of navigation »Notification -Enabling robots to subscribe to changes in repositories Signposting is an approach to make the scholarly web more friendly to machines exposing relations as Typed Links in HTTP Link headers, fully aligned with hypermedia (REST, HATEOAS) lines of thinking regarding web interoperability »Signposting is now implemented in DSpace-CRIS and OJS. DSpace 7 plans to provide Signposting support A license link type has been proposed to drive this information ResourceSync -http://www.openarchives.org/rs/toc »Successor of the OAI-PMH protocol and much more… »Faster, reliable and scalable »Allows real-time notification (and recovering of missed messages) »Drives resource synchronization: content and metadata are both managed ResourceSync -core specification » Based on the Sitemap protocol… » essentially some XML files that list your resources (ResourceList)…but also machine «discoverable» from well known URLs…auto explicative in the supported functionalities (CapabilityList) and able to eventually deal with changes (ChangeList) and synchronization of large amount of data (Dumps) » It is a framework: additional specifications add more features, for example the Change notification allows «push-based» synchronization ResourceSync Framework Specification (ANSI/NISO Z39.99-2017) A Next Generation Repository… » manages and provides access to a wide diversity of resources » is resource-centric » is a networked repository » is machine-friendly » is active (notify other systems, allow local active interaction)

### How to contribute?

Support the implementation of the identified behaviours and technologies in your community (DSpace, Eprints, Fedora, Dataverse, Samvera, etc., etc.) Join the conversation on GitHub https://github.com/coar-repositories/ngr
