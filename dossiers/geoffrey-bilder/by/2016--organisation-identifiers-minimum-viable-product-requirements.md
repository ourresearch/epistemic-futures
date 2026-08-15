---
title: "Organisation Identifiers — Minimum viable product requirements"
person: "geoffrey-bilder"
section: "by"
type: "report"
year: 2016
date: 2016-07-05
venue: "ORCID / DataCite / Crossref Organization Identifier Working Group"
authors: "Tom Demeranville, Josh Brown, Martin Fenner, Patricia Cruse, Laure Haak, Laura Paglione, Geoffrey Bilder, Jennifer Lin, Ed Pentz"
source_url: "https://doi.org/10.6084/m9.figshare.3479141.v1"
retrieved: "2026-08-13"
content: "full-text"
notes: "Working-group requirements document co-authored by Bilder. Text extracted from the figshare PDF."
---

# Organisation Identifiers — Minimum viable product requirements

## Full text

Organisation Identifiers
Minimum viable product requirements

(PUBLIC DRAFT FOR DISCUSSION)

Authors:
Tom Demeranville (ORCID), Josh Brown (ORCID), Laure Haak (ORCID), Laura Paglione
(ORCID), Patricia Cruse (Datacite), Martin Fenner (Datacite), Geoffrey Bilder (Crossref),
Jennifer Lin (Crossref), Ed Pentz (Crossref)

    Background / Problem Statement
    What makes a good identifier?
    Organisation identifier use cases
    Minimum requirements for organisation identifiers
       Descriptive metadata
    Governance and Sustainability
    Conclusions and future work
       Technical Requirements:
       Governance requirements:
       Sustainability requirements:

Background / Problem Statement
“The use of persistent identifiers for organisations lags behind the use of persistent identifiers
for research outputs and people.” ­​Project THOR, Artefact, Contributor, and Organisation
Relationship Data Schema 12

”Stakeholders interviewed for this study typically described identifying organisations as “a
nightmare”. Specifically, the nightmare is disambiguation (“Is this the right John Smith?”) and
deduplication (“Is Exampleton University the same as The University of Exampleton?”) of data
from multiple sources. The potential benefits from effective unique identifiers are primarily
realised when data is shared.“ ­​JISC/CASRAI Organisation ID study34

As these quotes demonstrate, there is a well documented need for a comprehensive, open, and
accessible organisation identifier infrastructure. While there is a lot of excellent work being done
in this space and examples of excellent services and providers tackling pieces of the problem,

1
  http://project­thor.eu
2
  http://dx.doi.org/10.5281/zenodo.30799
3
  http://jisccasraipilot.jiscinvolve.org/wp/working­groups/org­id/
4
  ​ttp://repository.jisc.ac.uk/id/eprint/5381
  h
gaps remain. These organisations, and others, work hard to serve their specific communities,
and are focussed, naturally, on meeting the needs of their own customers and partners.
However, there is a clear and definite need for the identifier schemes each provides to
interoperate with one another, even on a very basic level. In many ways, it is a similar
circumstance to the situation with researcher and author identifiers just before ORCID was
founded. Each scheme serves its community well, but does not work well across the research
community, This lack of interoperability acts to hinder scholarly communications. What we need
is an an open, interoperable, community­led infrastructure​  that widens c​
                                                                          overage and improves
accuracy outside of the specific domains which are currently served.

So how can we best work with the current providers to achieve these goals and better serve the
broader community?

Whatever the answer to this question might be, the need for organisation identifiers continues to
grow. Action is needed, and the community seems to be ready. The energy and commitment
exist. We also have a very good understanding of the requirements, thanks in large part to hard
work and insights of the organisations and collaborations referenced throughout this document.

This document sets out a number of use cases for organisational identifiers, from the
perspective of three PID providers that are also ‘consumers’ of organisation identifiers: Crossref,
DataCite and ORCID. The document draws together the products of several studies, working
groups and reports on the topic of organisation identifiers. It summarises the key observations
and recommendations from these reports and combines them into a single list of top level
requirements for a ‘minimum viable product’ to address the defined needs of the scholarly
communications and related communities for organisation identifiers.

Important questions remain, such as do we use a new ID or an existing ID? Should this
infrastructure form part of an existing organisation, or a new one? Who are the key
stakeholders? What level of granularity is needed in the data? Who controls the data? Who can
update it? What should be the business model? What about the scope of the service?
Governance?

This document is intended to provide the background for stakeholder discussions at a pair of
community workshops taking place in April 2016. The first, to be held at the Coalition for
Networked Information workshop in San Antonio, TX, will gather feedback on the top­level
requirements defined below5. The second, to be held at the FORCE 2016 conference in
Portland, OR, will set out the necessary steps to be taken to move forward towards a
sustainable, community­led, scalable solution to the organisation identifier problem6.

5
    https://www.cni.org/event/cni­spring­2016
6
    http://sched.co/5wKL
Small task groups will seek to evaluate options and possible responses to the open questions
raised by the requirements and by the workshops and will report back to the community at an
“identifier summit” to be held in Europe in November 2016.

What makes a good identifier?
To be truly useful, an identifier needs to be more than a simple label. It needs to compliment
and support the infrastructure that uses it by providing open, freely available, easily accessible
information about the entity it refers to. It needs to do this in perpetuity and in a trusted manner.
It should be both human and machine readable, ideally with API access, resolvability and
recognisable licence such as CC­0 for the identifier.

The ODIN project7 defined the term “trusted identifier” as part of a conceptual model of
interoperability.8 Within this model, trusted identifiers refer to those digital identifiers which are
unique, persistent/resolvable, descriptive/discoverable, interoperable a   ​nd​ governed.​ ODIN
defined these as:

      ●   Unique identifiers are unique on a global scale, allowing large numbers of unique
          identifiers
      ●   Persistent identifiers resolve as HTTP URIs with support for content negotiation, and
          these HTTP URIs should be persistent.
      ●   Descriptive identifiers come with metadata that describe their most relevant properties,
          including a minimum set of common metadata elements. A search of metadata
          elements across all trusted identifiers of that service should be possible [to aid
          discovery].
      ●   Interoperable identifiers are interoperable with other identifiers through metadata
          elements that describe their relationship.
      ●   Governed identifiers are issued and managed by an organization that focuses on that
          goal as its primary mission, has a sustainable business model and a critical mass of
          member organizations that have agreed to common procedures and policies, has a
          governing body, and is committed to using open technologies

These are the qualities that enable identifier infrastructure to meet the requirements of the
scholarly communication community and must be considered alongside organisational specific
demands.

                                                                                              ​nd
                     ​nique, persistent, resolvable, descriptive, discoverable, interoperable a
In addition to being u
governed,​project THOR recommended that organisational identifiers must be expressed as
HTTP URIs that resolve to a publicly available landing page with human and machine readable

7
    http://odin­project.eu/
8
    http://dx.doi.org/10.6084/m9.figshare.824314
information. It should noted that HTTPS are becoming prominent, so it may be simpler to
implement these from the start.

Organisation identifier use cases
There are a multitude of use cases from which requirements can be extracted. This section
contains an overview of PID provider use cases which are indicative of the problem space from
the PID infrastructure perspective. The JISC/CASRAI and NISO Institutional Identifier (I2)
Working Group I2910 studies contain use cases from the university, research, electronic resource
supply chain, institutional repositories and library resource management sectors.

ORCID Use Cases
Membership and Credentialing: O        ​RCID needs organization identifiers to be able to effectively
manage our membership accounts, correctly express the name of a member organization,
merge accounts when an organization is acquired (or split when divested), and connect that
identifier into both our financial/invoicing system and our API credentialing process (see below).
Ideally the member should be able to self­register and also self­update their listing, including
names, contact information, location, and hierarchies. This information should be available on a
webpage, resolvable from the identifier itself.

ORCID also needs organization identifiers to be able to manage the issuance of member API
credentials. These credentials are a key component of the ORCID Trust Framework, as they
are used to record the source of third­party assertions (see below).

These identifiers need to be associated with the following openly available (CC0) metadata:
Organization name/translated name, location (city/country). Not necessary but nice to have
would be financial liaison contact information, billing address, main phone number, and
CIO/CTO contact information. Coverage should be any organization that interacts with
researchers/scholars/innovators (universities, government labs, commercial entities, non­profit
entities, research funders, publishers, patent offices, third­party service providers…).

Assertions: O ​RCID needs organization identifiers to be able to record the source of
assertions, such as: this university with this name and organization identifier, asserts that this
person with this ORCID identifier have a specific role relationship (e.g., employee or student).

These assertions indicate associations between organization and the person (direct), as well as
the research activities attributed to the person (indirect.) For example:

       ●   Making ORCID iD/Organization ID pairs in the case of affiliations

9
     http://www.niso.org/workrooms/i2
10
     ​ttp://www.niso.org/publications/rp/rp­17­2013
     h
         ○ Connecting people directly to organisations via education and/or employment
   ●   Making ORCID iD/ Grant ID/ Organization ID connections
         ○ Connecting the grant ID to the funding organisation and indirectly linking the
             person to the organisation
   ●   Making ORCID iD/ peer review ID / Organization ID connections
         ○ Connecting the review to the organization that commissioned the review and
             indirectly linking the person to the organisation.
   ●   Making ORCID iD/ work ID/ Organization ID connections
         ○ Connecting the work to the organization publishing the work, indirectly linking the
             person to the organization.

These identifiers need to be associated with the following openly available (CC0) metadata:
Organization name/translated name, abbreviations, location (city/country). It would also be
useful to have data about hierarchies and relationships between organisations to enable
grouping by organization.

Self assertions and usability: I​ndividuals may also make self assertions, so the identifiers
need to be associated with human­readable metadata including alternate names and
abbreviations to enable user selection from a pre­populated list. This is currently hampered by
the lack of consistency in granularity and unclear specification of what is considered to be the
"main organization".

Our current "dropdown" list of organizations shown to end users includes confusing information
from their point of view. For example, if you work at UCLA, you will find an organization for the
University of California system (the umbrella organization) as well as individual departments at
UCLA. This makes it difficult for the individual to choose. To exacerbate the issue, only some of
the departments are included, so individuals in omitted departments sometimes contact ORCID,
asking to add their department.It would be better if ORCID were able to just present a list of
"main organizations", i.e., just the UCLA level, not the departments or the umbrella organisation.
Since this "main organization" isn't always at the top of the hierarchy, the problem is a non­trivial
one.

Matching Organization Identifiers:​     ORCID needs organization identifiers that can be
cross­referenced to identifiers used in other instances to understand that it is the same
organization. For example, in working with Identity Providers (IdP), which are often
organizations such as universities, it is helpful to have explicit connection between the IdP
unique name (for example, a SAML entityID), and organization identifiers used in other
instances. This connection would enable activities such as affiliation assertions on ORCID
records, and reciprocal connections for individuals between IdPs and ORCID Records.
DataCite Use Cases
Attribution​ : DataCite needs organizational identifiers to be able to unambiguously associate a
research output with an institution, either directly or using the contributors to the work as proxy.
This enables the unambiguous and automated linking of research outputs with contributors,
institutions, funders and funding, and other research outputs.

Attribution of publisher (repository)​ : DataCite also needs organizational identifiers to
unambiguously identify the publisher of a resource associated with a DataCite DOI. This is also
relevant for the DataCite re3data service, where we need organizational identifiers to connect
organizations with data repositories.

Membership​   : DataCite has members and members work with data centers. DataCite needs
organization identifiers to be able to effectively manage our membership accounts, correctly
express the name of a member organization, merge accounts when an organization is acquired
(or split when divested), and connect that identifier with user accounts. Ideally the member
should be able to self­register and also self­update their listing, including names, contact
information, location, and hierarchies. Organizational identifiers are also needed for the data
centers and other organizations that work with DataCite and its members and register DOIs.

Minimum requirements for organisation identifiers
Clearly there is a lot of work to be done, and a real opportunity for the organization that
manages to pull together a service that combines:

   1. Comprehensive lists that one can interrogate at a consistent granularity.
   2. Organizational input on what information is "correct"
   3. Coverage across an unlimited number of industries and regions, equivalent identifiers
      found in many popular organization databases
   4. An API that allows machine connections to this resource
   5. Organization listing resolvable through the identifier itself
   6. A set of embeddable widgets and tools that people can use in their sites when
      referencing organizations so that we don't all have to continue to invent things that
      others have already invented.

The NISO Institutional Identifier (I2) Working Group laid out their view on the mandatory
operational requirements for institutional identifiers as:

   ●   The identity of each organization must be unambiguous and clear, which requires
       metadata to identify the organization and to disambiguate it from other organizations.
   ●   Identifiers must be easily assigned to organizations at point of need so that digital
       information workflows are not disadvantaged by the need to discover or assign identifiers
   ●   A user, defined as any entity with a need to participate in a digital information workflow,
       must be able to readily discover and reuse identifiers.
   ●   The user must be able to trust that each unique organization has only one identifier, this
       identifier must be readily discoverable.
   ●   The organization identified with an identifier must authorize the assignment and reuse of
       the identifier, so that participants in an information workflow can trust the authenticity of
       the identifier.
   ●   As an organization changes, or develop relationships, such as membership in a
       purchasing consortium, the metadata must be able to be easily updated to reflect such
       changes.

This can be summarized in terms of the THOR recommendations as unique, descriptive and
discoverable. In addition, it stipulates that identifiers must be​unique­per­entity,​
created­by­the­entity­on­demand a   ​nd c​ontrolled­by­the­entity.​It also mentions the concept of
trust.​What it lacks are the concepts of persistence, resolvability/HTTP URIs, interoperability and
governance.

The Jisc/CASRAI Organisational ID landscape study noted the main challenges for any
organisational ID are disambiguation and deduplication, use cases that must be tackled
head­on by any identifier infrastructure. It described the key requirements to support the use
cases it encountered as:

   ●   Governance​    . An identifier and agreed metadata must be governed and maintained.
       Regardless of how this is done, it must be done effectively.
   ●   Trust​ . Parties that rely on an identifier must trust that identifier. There are several key
       areas of trust: firstly, the assertion that the identifier refers to an organisation of interest
       (which may be supported by making the identifier human­readable), secondly, the
       assertion that data associated with an identifier is correct and thirdly that the identifier
       will continue to be maintained to reflect changes in organisational structure and status,
       etc.
   ●   Transparency​    . It must be clear how identifiers are issued, and to which organisations.
       Processes for the management and governance of identifiers must be defined and must
       be conducted transparently.
   ●   Temporal​   . Many use cases require information not just about the current list of
       organisations, but also about their histories. Institutions are created, merge, split, acquire
       each other, change status and are renamed. None of the identifiers discovered during
       this study adequately meet this requirement, although some do store some historical
       information.
   ●   Appropriate metadata​      . A Names Authority can issue organisational identifiers
       associated with a short list of metadata (eg name, deprecated­name,
       deprecated­nameID, City, County, PostalCode, URI), or an extended metadata list (eg
          including classifiers and organisational hierarchies). It would probably be easier and
          more beneficial for an organisational identifier Names Authority to be limited to a small
          metadata set – the minimum required for effective identification.

The JISC/CASRAI study raises an important point not yet considered, the history of identifiers
and organisational change, stating that it is “deeply important to many of the use cases
identified“. Being able to query at a point in time is vital if the links created with organisational
identifiers are to endure and remain useful as part of the historical record. In addition to
expanding on requirements already discussed, it also recommends smaller, core metadata over
exhaustive information. This recommendation is shared by project THOR, who advocate
linking to detailed domain specific information via other identifiers rather than attempting to
solve all use cases in a single service.

The report also considered the definition of organisational entities, noting that while most
existing identifiers consider the “legal entity” to be the basic unit, this is insufficient in some
cases. Examples of this could be research centres wholly owned by funding bodies, or colleges
within a university, such as the University of Oxford. The ability to describe such entities would
enable a similar PID infrastructure to describe other non­legal entities, such as projects which
often share attributes with organisation (outputs, funding, time bounds etc.). The challenges
specific to project IDs were discussed in the THOR Artefact, Contributor, and Organisation
Relationship Data Schema report11.

Descriptive metadata
This document does not attempt to define organisation metadata requirements or an exhaustive
review of organisational metadata requirements. Neither does it attempt to describe the myriad
roles organisations and use­cases these roles contain. Instead it outlines high level
requirements and places the organisation in context so that it can be considered as part of a
wider ecosystem.

What is clear is that organisations must be responsible for managing and maintaining their own
metadata and there must be a sufficiently low barrier to facilitate widespread engagement, but
also sufficiently high as to establish and maintain trust. To be interoperable organization
identifiers must be able to reference other identifiers, including other organisational identifiers,
and must be freely resolvable to metadata (via an API) at the point of use.

The Jisc/CASRAI Organisational ID report identified organisations acting as publishers, funders,
regulators, service providers, repositories and intermediaries. Just as people can occupy many
roles simultaneously, organisations often serve many roles, defined by their relationships to
other organisations and individual people. This means that relationships between organisations
are multiple, and many­to­many, and can be succinctly expressed via typed relationships

11
     ​
     h ttp://dx.doi.org/10.5281/zenodo.30799
between two PIDs. This is a commonly encountered and described scenario requiring two
identifiers and a relationship type. In linked open data terms, it would be described as triple in
the form s​ ubject­predicate­object.​It is the use of the identifier that creates value, not just the
metadata that it references within its own domain.

Further to this, THOR identified relationship types involving organisations that are currently
modeled by ORCID and Datacite including contributors, creators, funders, educators and
employers. These are not exhaustive lists and others can easily be found in the academic
landscape, such as the organisations as equipment owners modeled by equipment.data.ac.uk.
What this means for identifiers is that they must be sufficiently flexible and/or lean in their
definition to encompass a wide range of use cases and emerging requirements. Any
infrastructure supporting these identifiers should be able to consider relationships beyond
scholarly communication, and be sufficiently extensible to address a wide range of present and
future challenges.

As long as the organisational identifier infrastructure is sufficiently open, relationship types can
be defined as­and­when by the communities that require them, increasing the identifiers value.
The use of these types and inclusion within the wider ecosystem should, once again, point to a
leaner rather than exhaustive set of metadata associated with an institution as recommended by
the JISC/CASRAI report

By leveraging relationship types between PIDs, complex hierarchies and graphs can be
described, including those between organisations, sub­organisations and unit, examples include
Parent­child, Sibling, PartOf, SameAs, FormerlyKnownAs and so on. With a sufficiently open
approach to defining and categorising relationships, this component of the infrastructure should
remain flexible and scalable and capable of adding new relationships and PID types as needed
in future.

Governance and Sustainability

“Everything we have gained by opening content and data will be under threat if we allow the
enclosure of scholarly infrastructures. We propose a set of principles by which Open
Infrastructures to support the research community could be run and sustained”​  – Geoffrey
Bilder, Jennifer Lin, Cameron Neylon. Principles for Open Scholarly Infrastructures. 12

“Trusted identifiers need the strong support of an organization to become sustainable. This
organization not only needs a sustainable business model, but also community support from a
critical number of member organizations, and a governing body with a common set of
                          ​ODIN project, Conceptual model of linkages.
procedures and policies.” ­

12
     https://dx.doi.org/10.6084/m9.figshare.1314859.v1
The paper Principles for Open Scholarly Infrastructures outline a number of aspirational
principles under three sections, Governance, sustainability and insurance. The principles are:

   ●   Governance
           ○ Coverage across the research enterprise
           ○ Stakeholder Governed
           ○ Non­discriminatory membership
           ○ Transparent operations
           ○ Cannot lobby
           ○ Living will
           ○ Formal incentives to fulfil mission & wind­down
   ●   Sustainability
           ○ Time­limited funds are used only for time­limited activities
           ○ Goal to generate surplus
           ○ Goal to create contingency fund to support operations for 12 months
           ○ Mission­consistent revenue generation
           ○ Revenue based on services, not data
   ●   Insurance
           ○ Open source
           ○ Open data (within constraints of privacy laws)
           ○ Available data (within constraints of privacy laws)
           ○ Patent non­assertion

These principles add a number of top­level requirements to the more technical requirements
specified in previously discussed reports. These are largely concerned with the governance and
sustainability model of any initiative to tackle organisation identifiers, although there are clear
overlaps between the categories. For example, the “insurance” principles (which provide for the
persistence and trust of the infrastructure) impose certain technical requirements, such as open
source code; enabling, for example, the forking of the software underlying the infrastructure
should that be necessary for its continuance.

Under the heading of sustainability, the emphasis on deriving income from services rather than
data implies a set of activities around adding value and ensuring access to the identifiers and
any associated data, rather than monetising the data itself. This implies a relationship to the raw
data of s​ tewardship,​rather than o
                                   ​wnership,​which therefore requires a strong degree of
community involvement in decision making and direction setting for the governance of the
initiative.

This requirement for stakeholder governance in turn imposes a stringent set of requirements
around organisational and technical transparency. The principles could be classified in various
ways, as they are more or less closely related to the requirements of any particular initiative, but
the key feature of these principles is their interrelatedness. They intersect at each point with
each other, and mean that any future organisation identifier initiative would be well advised to
consider them as a whole at each stage of its evolution, from the current phase of defining
requirements right through to implementation and institutional maturation.

Conclusions, aspirations and future work
This document defines a set of top­level requirements, derived from the reports and documents
cited above. There are inevitable overlaps between these requirements, and more than one
requirement could be served by single decisions. It is also worth noting that this ‘long list’ of
requirements is inevitably aspirational. In the interest of completeness and comprehensiveness
the ‘long list’ of requirements is given here, to ensure that issues foregrounded by specific
requirements are treated properly. This should help to ensure that each facet of the organisation
identifier challenge is considered. Since the aim of this document is to stimulate discussion and
to gather input from the community, a wider net is being cast at this stage, with the aim of
narrowing requirements down in the future after feedback.

Some of these requirements refer to the necessary attributes of a trusted, persistent identifier.
Other refer to essential functions for such an identifier to be used for organisations. Others still
touch upon the sustainability model for the infrastructure needed to provide organisation
identifiers. For clarity, these can be categorised under three distinct headings: Technical
requirements, Governance requirements and Sustainability.

Technical Requirements:

 Top­level requirement       Description

 Unique                      Identifiers are unique on a global scale, allowing large numbers of
                             unique identifiers

 Descriptive                 Organisational identifiers associated with a set of metadata
                             sufficient for organisational identification.

 Discoverable                A user, defined as any entity with a need to participate in a digital
                             information workflow, should be able to readily discover and reuse
                             identifiers.

 Unique per entity           A user should be able to trust that each unique organization has
                             only one identifier and that duplicate records will be managed.​

 Created on demand by        Identifiers should be easily assigned to organizations at point of
 the entity                  need so that digital information workflows are not disadvantaged by
                             the need to discover or assign identifiers
Human actionable          A user should be able to resolve the identifier into a web page
                          containing the descriptive metadata in a readable format.

Machine actionable        Identifiers should be resolvable as HTTP URI’s with support for
                          content negotiation, and these

Persistent                Identifiers and HTTP URI representations should be persistent

Interoperable             Identifiers should be interoperable with other identifiers through
                          metadata elements that describe their relationship.

Applicable to non legal   The definition of organisation should be broad enough to enable
entities                  entities such as research institutes and projects to participate. This
                          has implications for governance models. NB: This may not be a
                          core requirement for all, but it is a significant need. It may be
                          possible to address ‘related’ organisations via hierarchies and
                          graphs (below).

Temporal                  The identifier should continue to be maintained to reflect changes
                          in organisational structure and status, etc. This should include
                          preserving and exposing a historical record for the entity identified,
                          including previous identifiers. As an organization changes, or
                          develops relationships, the metadata must be able to be easily
                          updated to reflect such changes.

Appropriate metadata      Metadata should be a ​ppropriate, c​ontaining only necessary
                          information for deduplication and disambiguation.​A ​ppropriateness
                          should include timeliness, accuracy and currency.

Supports hierarchies      Organisational Identifiers should be able to be associated with one
and graphs                another using relationship types. A robust system for expressing
                          hierarchies and relationships between organisations should be able
                          to capture relationships below the level of the legal entity or
                          top­level organisation, such as parent­child, part­of or joint venture.
                          Any such systems should aim to maintain a consistent level of
                          granularity, and indicate the ‘main organisation’ as generally
                          understood. NB: It is worth noting that wider graphs may be best
                          maintained by a subsidiary or parallel service or system. For
                          example, relationship types such as funded­by and participates­in
                          could be represented by external systems, e.g. links to/from other
                          identifier systems, funding databases, etc.
Governance requirements:

Top­level requirement      Description

Controlled by the entity   The metadata associated with an identifier should be editable and
                           updatable by the entity that the identifier refers to, or by a trusted
                           third party with consent from the entity.​

Governed                   The identifiers should be issued and managed by an organization
                           that focuses on that goal as its primary mission, has a sustainable
                           business model and a critical mass of member organizations that
                           have agreed to common procedures and policies, and that has a
                           governing body. NB: the launch of a new initiative to govern an
                           infrastructure component brings significant overhead, it may be
                           faster and simpler to extend the remit of an existing provider.

Transparent                The workings of the organization, decision making process and
                           roadmap should be open to public scrutiny, within privacy laws.

Stakeholder                The organisation should not be co­optable by narrow interest
governed/community         groups. A balanced demographic representation of the
led                        membership should be maintained at the decision­making and
                           consultation levels.

Non discriminatory         The organisation should operate on an ‘opt­in’ basis, where any
membership                 stakeholder group may express an interest and be welcome.

Sustainability requirements:

Top­level requirement      Description

Trusted                    Parties that rely on an identifier should trust that identifier. There
                           are several key areas of trust: firstly, the assertion that the identifier
                           refers to an organisation of interest (which may be supported by
                           making the identifier human­readable), secondly, the assertion that
                           data associated with an identifier is correct and thirdly that the
                           identifier will continue to be maintained to reflect changes in
                           organisational structure and status, etc.​

Sustainable                The initiative maintaining the identifier infrastructure should be
                           sustainable, and provide assurances that transparent technical and
                           administrative plans are in place to ensure the persistence of the
                           infrastructure in the event of organisational demise.

 Open source               All software required to run the infrastructure should be available
                           under an open source license. This does not include other software
                           that may be involved with running the organisation.

 Open Data                 It should be possible to replicate all relevant data. The CC0 waiver
                           is best practice in making data legally available. Privacy and data
                           protection laws will limit the extent to which this is possible.

 Available data            Identifier metadata should be available through an open public API
                           and underlying data should be made easily available via periodic
                           data dumps.

 Cross sectoral            The initiative should serve each of the sectors active in, and
                           associated with, scholarly communications. Finance, pharma,
                           government agencies etc. all stand to benefit from engagement
                           with an organisation identifier infrastructure and as such should
                           provide input. This broader grouping will also provide a stronger
                           foundation for the initiative. NB: This will have potentially significant
                           implications for the stakeholder makeup and governance, however
                           the greater the number of challenges this solution can address, the
                           more likely that it will be adopted broadly and sustainable.

These three clusters of requirements can be treated as a coherent whole, and it is possible to
derive a number of open, practical questions, consequent upon them. These questions, and the
exploration of the various possible options and solutions to them, should form the focus of the
next steps. A stakeholder­balanced community discussion of these questions should be
conducted on a defined timescale, to ensure that a concrete proposal can be offered to the
wider community for discussion and implementation before the end of 2016.
