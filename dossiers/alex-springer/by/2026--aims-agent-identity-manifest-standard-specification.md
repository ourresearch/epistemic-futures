---
title: "AIMS — Agent Identity Manifest Standard, Specification"
person: "alex-springer"
section: "by"
type: "report"
year: 2026
date: "2026-05-14"
venue: "OpenAttribution"
authors: "Alex Springer (sole repository contributor; document carries no byline)"
source_url: "https://raw.githubusercontent.com/openattribution-org/aims/main/SPECIFICATION.md"
retrieved: "2026-08-13"
content: "full-text"
notes: "Technical specification document from a GitHub repository where jalexspringer (Alex Springer) is the only listed contributor; all commits are authored as 'Alex Springer <alex@spurcoalition.org>' or '<alex@openattribution.org>', some via an automation account ('NarrativAI Agent') using the same address. The document itself carries no personal byline. Text is the verbatim Markdown source. Date is the file's last commit date."
---

# AIMS — Agent Identity Manifest Standard, Specification

## Full text

---
layout: spec
title: "AIMS Specification"
description: "Agent Identity and Manifest Standard"
---

# Agent Identity and Manifest Standard (AIMS)

**Draft Specification v0.1** | March 2026 | openattribution.org

---

## Table of contents

1. [Introduction](#1-introduction)
2. [Identity](#2-identity)
3. [Manifest](#3-manifest)
4. [Discovery and resolution](#4-discovery-and-resolution)
5. [Verification](#5-verification)
6. [Standards integration](#6-standards-integration)
7. [Use cases](#7-use-cases)
8. [Open questions](#8-open-questions)
- [Appendix A: Compliant content access flow](#appendix-a-compliant-content-access-flow)
- [Appendix B: Related standards reference](#appendix-b-related-standards-reference)
- [Appendix C: Glossary](#appendix-c-glossary)

---

## 1. Introduction

### 1.1 What AIMS is

AIMS provides verifiable identity for AI agents that access web content. An agent publishes an AIMS manifest containing its identity, the content licences it holds, and the telemetry endpoint it reports to. Publishers and other agents resolve the manifest to verify the agent before granting access or establishing trust.

AIMS is the identity layer in the OpenAttribution ecosystem. It answers: **who is this agent, and can it prove its claims?**

### 1.2 The four-layer model

The standards governing the content-agent relationship form four layers. Each layer addresses a distinct question.

| Layer | Question | Standards |
|-------|----------|-----------|
| **Declaration** | What are the terms for using my content? | RSL, robots.txt (RFC 9309), IAB Comp Protocol, Creative Commons |
| **Access control** | Does this agent have permission right now? | RSL CAP, RSL OLP, CDN enforcement |
| **Identity** | Who is this agent, and can it prove its claims? | **AIMS**, W3C DIDs, A2A Agent Cards, ANP did:wba |
| **Telemetry** | What happened to my content after access? | OpenAttribution Telemetry |

AIMS occupies the Identity layer. It provides the verified subject that telemetry events are attributed to.

Without identity, telemetry is anonymous data. Without telemetry, identity is credentials with no audit trail. The two layers depend on each other.

### 1.3 What AIMS does not do

AIMS does not:

- **Declare licensing terms** - that is the publisher's job (RSL, robots.txt)
- **Enforce access control** - that happens at the gate (RSL CAP/OLP, CDN enforcement)
- **Track content usage** - that is the Telemetry layer (OpenAttribution Telemetry)
- **Describe agent capabilities** - that is A2A (Agent Cards)
- **Define agent-to-tool connections** - that is MCP
- **Document model performance** - that is Model Cards
- **Document dataset composition** - that is Dataset Cards

AIMS provides the identity and licence proof that makes these other standards enforceable and attributable.

### 1.4 Design principles

**Use existing standards.** Build on W3C DIDs and Verifiable Credentials. Do not invent parallel identity infrastructure.

**Start simple.** The minimum viable manifest is an identity and a list of licences held. Everything else is optional.

**Telemetry-first.** The primary purpose of AIMS identity is to provide an accountable subject for telemetry events. Design decisions favour this use case.

**Publisher-centric.** The primary relationship is publisher-to-agent: "Is this agent licensed to access my content, and can I hold it accountable?" Agent-to-agent trust is a secondary benefit.

---

## 2. Identity

### 2.1 DID-based identity

Every agent that publishes an AIMS manifest is identified by a W3C Decentralized Identifier (DID). AIMS does not define its own DID method. Any conformant W3C DID method can be used.

**Recommended methods:**

| Method | Resolution | Best for |
|--------|-----------|----------|
| `did:web` | HTTPS URL derived from the DID | Organisations with a web domain. Simple to implement. |
| `did:wba` | Web-based agent resolution (ANP) | Agents in decentralised networks. |
| `did:key` | Self-contained cryptographic key | Lightweight agents, ephemeral identities. |

**Examples:**

```
did:web:example.com:agents:shopping-assistant
did:web:perplexity.ai:agents:search
did:wba:forage.dev:agents:browser
did:key:z6MkhaXgBZDvotDkL5257faiztiGiC2QtKLGpbnnEGta2doK
```

### 2.2 DID resolution

The DID resolves to a DID Document containing the public keys needed to verify signed manifests. DID resolution follows the W3C DID Resolution specification. AIMS adds no custom resolution logic.

For `did:web`, resolution follows the did:web method specification: the DID maps to an HTTPS URL, and the DID Document is fetched from that URL.

### 2.3 Relationship to the AIMS manifest

The DID identifies the agent. The manifest describes the agent's licence status and telemetry compliance. These are separate documents:

- **DID Document** - public keys, verification methods, service endpoints (including the manifest URL)
- **AIMS Manifest** - licences held, telemetry endpoint, optional provenance and deployment context

The DID Document's `service` array SHOULD include an entry pointing to the manifest:

```json
{
  "id": "did:web:example.com:agents:search#aims",
  "type": "AIMSManifest",
  "serviceEndpoint": "https://example.com/.well-known/aims/search.json"
}
```

---

## 3. Manifest

The AIMS manifest is a JSON-LD document describing an agent's identity, content licences, and telemetry compliance. It can be packaged as a W3C Verifiable Credential for cryptographic signing and selective disclosure.

### 3.1 Core schema

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://openattribution.org/aims/v1"
  ],
  "type": "AIMSManifest",
  "id": "did:web:example.com:agents:search",
  "version": "2026-03-16T00:00:00Z",
  "operator": {
    "name": "Example Corp",
    "domain": "example.com"
  },
  "licences": [ ... ],
  "telemetry": { ... },
  "foundation": { ... },
  "deployment": { ... },
  "proof": { ... }
}
```

### 3.2 Required fields

| Field | Type | Description |
|-------|------|-------------|
| `@context` | array | JSON-LD context. MUST include the AIMS context URL. |
| `type` | string | Always `"AIMSManifest"`. |
| `id` | string | The agent's DID. |
| `version` | string | ISO 8601 timestamp of this manifest version. |
| `operator` | object | The organisation operating this agent. |

### 3.3 Content licences

The `licences` array declares what content this agent is licensed to access. This is the compliance proof that publishers and access control systems check.

```json
"licences": [
  {
    "source": "reuters.com",
    "type": "rsl",
    "scope": "inference",
    "rslLicenceId": "rsl:lic:reuters:ai-inference-2026",
    "expires": "2026-12-31"
  },
  {
    "source": "wirecutter.com",
    "type": "partnership",
    "scope": "full",
    "redistribution": "summary_only"
  },
  {
    "source": "gutenberg.org",
    "type": "public_domain",
    "scope": "unrestricted"
  }
]
```

**Licence entry fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `source` | string | Yes | Content source identifier. Domain for web publishers. |
| `type` | string | Yes | Licence type: `rsl`, `partnership`, `marketplace`, `public_domain`, `creative_commons`, `other`. |
| `scope` | string | Yes | Access scope: `training`, `inference`, `full`, `unrestricted`. |
| `rslLicenceId` | string | No | RSL licence identifier, if the licence was acquired via RSL OLP. |
| `redistribution` | string | No | Redistribution policy: `none`, `summary_only`, `attributed`, `unrestricted`. Default: `none`. |
| `expires` | string | No | ISO 8601 expiration date. |

### 3.4 Telemetry compliance

The `telemetry` object declares which OpenAttribution endpoint this agent reports to. This links the agent's identity to its accountability chain.

```json
"telemetry": {
  "endpoint": "https://api.openattribution.org/v1/events",
  "agentId": "did:web:example.com:agents:search",
  "events": ["content_retrieved", "content_cited", "content_engaged"]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `endpoint` | string | Yes | The OpenAttribution telemetry endpoint this agent reports to. |
| `agentId` | string | Yes | The identifier used in telemetry events. MUST match the manifest `id`. |
| `events` | array | No | Event types the agent reports. Default: all standard OA event types. |

When a publisher receives a telemetry event, the `agentId` in the event resolves to this manifest. The publisher can then verify: this agent holds a licence for my content, and it reports its usage to this endpoint.

### 3.5 Foundation (optional)

Training data provenance. Documents the licensing status of the data that trained the underlying model. This layer is optional - many agents will not disclose training data details.

```json
"foundation": {
  "baseModel": "Llama 3 70B",
  "baseModelDid": "did:web:meta.com:models:llama-3-70b",
  "rslCompliant": true,
  "trainingDataSummary": "Trained on publicly available web content, filtered to RSL-compliant sources.",
  "auditEndpoint": "https://api.example.com/aims/audit/v1"
}
```

The `baseModelDid` field enables provenance chains: a fine-tuned model references its base model's DID, and a consumer can trace the full lineage.

For detailed dataset composition (collection methodology, temporal distribution, annotation procedures), link to Dataset Cards rather than duplicating that information here.

### 3.6 Deployment context (optional)

Commercial and operational context that may affect agent behaviour. Useful for agent-to-agent trust decisions.

```json
"deployment": {
  "purpose": "Product recommendations for Example Corp customers",
  "brandAffiliation": "Example Corp",
  "biases": ["Recommendations prioritise Example Corp inventory"],
  "modelCardUrl": "https://example.com/model-card"
}
```

For comprehensive documentation of alignment methodology, safety training, and content policies, link to Model Cards via `modelCardUrl`.

### 3.7 Proof

The manifest SHOULD be signed. When packaged as a Verifiable Credential, the `proof` field contains the cryptographic signature over the manifest contents.

```json
"proof": {
  "type": "DataIntegrityProof",
  "cryptosuite": "eddsa-rdfc-2022",
  "created": "2026-03-16T00:00:00Z",
  "verificationMethod": "did:web:example.com#key-1",
  "proofPurpose": "assertionMethod",
  "proofValue": "z..."
}
```

Unsigned manifests are valid but untrusted. Consumers SHOULD treat unsigned manifests as self-reported claims with no cryptographic backing.

### 3.8 Complete example

A search agent operated by a company with licensed access to news content:

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://openattribution.org/aims/v1"
  ],
  "type": "AIMSManifest",
  "id": "did:web:searchco.com:agents:web-search",
  "version": "2026-03-01T00:00:00Z",
  "operator": {
    "name": "SearchCo",
    "domain": "searchco.com"
  },
  "licences": [
    {
      "source": "reuters.com",
      "type": "rsl",
      "scope": "inference",
      "rslLicenceId": "rsl:lic:reuters:ai-search-2026",
      "redistribution": "summary_only",
      "expires": "2026-12-31"
    },
    {
      "source": "theguardian.com",
      "type": "partnership",
      "scope": "inference",
      "redistribution": "attributed"
    }
  ],
  "telemetry": {
    "endpoint": "https://api.openattribution.org/v1/events",
    "agentId": "did:web:searchco.com:agents:web-search",
    "events": ["content_retrieved", "content_cited"]
  },
  "deployment": {
    "purpose": "AI-powered web search",
    "brandAffiliation": "SearchCo",
    "biases": [],
    "modelCardUrl": "https://searchco.com/model-card"
  },
  "proof": {
    "type": "DataIntegrityProof",
    "cryptosuite": "eddsa-rdfc-2022",
    "created": "2026-03-01T00:00:00Z",
    "verificationMethod": "did:web:searchco.com#key-1",
    "proofPurpose": "assertionMethod",
    "proofValue": "z3FXQjecWufY46..."
  }
}
```

---

## 4. Discovery and resolution

### 4.1 For did:web agents

Agents using `did:web` host their manifest at a well-known URL derived from the DID:

```
did:web:example.com:agents:search
  -> https://example.com/.well-known/aims/search.json
```

**Path derivation:** The DID's path components after the domain map to subdirectories under `/.well-known/aims/`, with the final component as the filename plus `.json`.

The DID Document (at `/.well-known/did.json` per the did:web spec) SHOULD include a service endpoint pointing to the manifest. The `.well-known/aims/` path is a convenience for direct resolution without a DID Document lookup.

### 4.2 For other DID methods

For non-web DID methods, resolution follows the standard DID Resolution specification. The DID Document's service array includes the manifest URL as described in section 2.3. There is no alternative discovery mechanism - the DID Document is the canonical pointer.

### 4.3 Caching

Consumers SHOULD cache resolved manifests. The `version` timestamp indicates freshness. Recommended TTL: 24 hours for production use, with shorter TTLs during onboarding or compliance audits.

### 4.4 No registry

AIMS does not define a centralised manifest registry. Discovery relies on DID resolution, which is inherently decentralised. Operators host their own manifests. Third-party aggregators or directories (such as AGNTCY's Agent Directory) may index manifests for convenience, but they are not authoritative.

---

## 5. Verification

### 5.1 What verification means

Verification answers two questions:

1. **Identity:** Is this agent who it claims to be? (Does it control the private key associated with its DID?)
2. **Manifest integrity:** Has the manifest been tampered with? (Does the signature verify against the DID Document's public key?)

Verification does NOT answer whether the manifest's claims are true. Licence claims are self-reported. Independent verification of licence validity is a trust-layer concern (see section 6.11).

### 5.2 Verification flow

1. Resolve the agent's DID to its DID Document
2. Retrieve the manifest (via service endpoint in the DID Document or `.well-known/aims/` path)
3. Verify the manifest's `proof` against the public key in the DID Document
4. Check the `version` timestamp for freshness
5. Parse licence and telemetry fields as needed

### 5.3 Identity challenge (future work)

For real-time agent-to-agent scenarios, a challenge-response protocol proves the agent controls its DID's private key at connection time. This prevents replay attacks where an agent presents a legitimate manifest it does not own.

The protocol binding (standalone handshake vs A2A authentication extension vs TSP transport) is an open design question. See section 8.

### 5.4 Trust decisions

Manifest contents inform trust decisions but do not prescribe them. A publisher might:

- Grant access only to agents with a valid AIMS manifest
- Require specific licence types in the `licences` array
- Require telemetry compliance (a `telemetry` field pointing to a recognised endpoint)
- Reject unsigned manifests
- Apply different access tiers based on licence scope

Trust policy is application-specific. AIMS provides the information.

---

## 6. Standards integration

### 6.1 W3C Decentralized Identifiers (DIDs)

**Relationship:** Dependency.

AIMS uses DIDs as the core identifier for agents. DID v1.0 is a W3C Recommendation (July 2022). DID v1.1 is a Candidate Recommendation (March 2026).

AIMS inherits the decentralisation, cryptographic verifiability, and cross-platform portability properties of the DID standard. Any conformant DID method can be used.

### 6.2 W3C Verifiable Credentials

**Relationship:** Packaging format.

AIMS manifests can be packaged as Verifiable Credentials (W3C Recommendation, May 2025), providing cryptographic signing, selective disclosure, revocation checking, and credential chaining for derivative models.

When packaged as a VC, the manifest issuer is the agent operator, the subject is the agent's DID, and the credential contains the licence and telemetry fields.

### 6.3 Really Simple Licensing (RSL)

**Relationship:** Complementary. RSL declares publisher terms; AIMS declares agent compliance.

RSL 1.0 (finalised December 2025) provides machine-readable licensing for web content. AIMS integrates with RSL at two levels:

- **Licence references:** The `licences` array in an AIMS manifest references RSL licence identifiers acquired via the Open Licence Protocol (OLP)
- **Compliance declaration:** The optional `foundation.rslCompliant` field declares whether the agent's training data respected RSL terms

**Telemetry directive (in progress):** OpenAttribution is working with the RSL Technical Steering Committee to define a telemetry directive within the RSL licence schema. The intent is that a future `<telemetry>` element in RSL licence XML would direct compliant agents to the publisher's OpenAttribution endpoint as a condition of the licence. When this ships, AIMS manifests become the mechanism by which agents prove they meet the telemetry requirement.

### 6.4 IAB Comp Protocol

**Relationship:** Complementary. Comp Protocol handles monetisation terms; AIMS provides compliance proof.

The IAB Tech Lab Comp Protocol defines monetisation flows for AI content access, tied to RSL. It sits at the intersection of the Declaration and Access Control layers.

**Telemetry integration (in progress):** A telemetry reporting requirement could be added alongside the Comp Protocol's monetisation terms. This would create a path where commercial licensing agreements (mediated by Comp Protocol) include telemetry obligations (mediated by AIMS + OA Telemetry).

### 6.5 Agent-to-Agent Protocol (A2A)

**Relationship:** Complementary. A2A describes capabilities; AIMS describes provenance and compliance.

A2A (Linux Foundation, TSC includes Microsoft, AWS, IBM, Salesforce, SAP) standardises communication between AI agents. Agents publish Agent Cards describing identity, capabilities, and authentication requirements.

**Integration points:**

- An A2A Agent Card can reference an AIMS manifest URL, allowing capability-discovery clients to also check licence compliance
- AIMS verification can extend A2A's authentication flow, adding licence and telemetry checks alongside the functional handshake
- Both standards use DIDs for agent identity

**Scope boundary:** A2A Agent Cards answer "What can this agent do?" AIMS manifests answer "What is this agent licensed to access, and where does it report usage?"

### 6.6 Agent Network Protocol (ANP)

**Relationship:** DID interoperability.

ANP uses a three-layer architecture: identity (W3C DID-based, with its own `did:wba` method), meta-protocol (natural-language negotiation), and application layer (JSON-LD agent descriptions). It is the most decentralisation-focused of the agent protocols.

**Integration:** Agents using `did:wba` can publish AIMS manifests referenced from their DID Document's service array. ANP agent descriptions could include AIMS compliance as a declared attribute.

### 6.7 Trust Spanning Protocol (TSP) / TA2A

**Relationship:** Potential transport layer.

TSP (Trust over IP Foundation, Linux Foundation Decentralised Trust) enables secure communication between endpoints using different identifier types. It provides authentication, confidentiality, and metadata privacy using public key cryptography with verifiable trust roots. TA2A runs A2A over TSP.

**Integration:** TSP addresses the same trust-without-prior-relationship problem that AIMS verification needs to solve when agents from different organisations interact without a shared identity provider. TSP could serve as the transport for AIMS identity challenge-response (section 5.3).

### 6.8 Cisco AGNTCY / OASF

**Relationship:** Directory and schema integration.

AGNTCY provides infrastructure for agent collaboration: discovery (Agent Directory), identity (decentralised verification), messaging (SLIM protocol), and observability. The Open Agent Schema Framework (OASF) provides a data model for describing agents.

**Integration:** AGNTCY's Agent Directory could index AIMS manifests. OASF agent descriptions could include AIMS compliance as a verified attribute, allowing directory queries like "show me agents with valid AIMS manifests and Reuters licences."

### 6.9 IETF Agent Name Service (ANS)

**Relationship:** Identity resolution complement.

The ANS draft maps agent identities to capabilities, cryptographic keys, and endpoints via a PKI-backed directory. If ANS is adopted, AIMS manifests could be referenced within ANS records, linking agent identity resolution to content compliance status.

AIMS discovery already follows the RFC 8615 (.well-known URIs) pattern, consistent with IETF conventions.

### 6.10 C2PA Content Credentials / CAWG

**Relationship:** Complementary provenance chain.

C2PA (Linux Foundation) provides cryptographic provenance for media files. CAWG (Creator Assertions Working Group, DIF) enables non-human actors to assert their role in relation to content.

C2PA tracks provenance of content creation: "this image was created by X and edited by Y." AIMS + OA Telemetry track provenance of content usage: "this article was retrieved by agent Z and cited in response W."

For brand use cases, both chains together provide end-to-end visibility from content creation through AI usage and presentation.

### 6.11 OpenAttribution Telemetry

**Relationship:** Primary integration. AIMS identity is the subject that telemetry events are attributed to.

OpenAttribution Telemetry defines an open schema for retrieval, citation, and engagement events. When an agent retrieves content, that is an event. When it cites that content in a response, that is a second event.

**How AIMS and Telemetry connect:**

- The `telemetry.agentId` in an AIMS manifest matches the `agent_id` field in OA telemetry events
- When a publisher receives a telemetry event, they resolve the `agent_id` to an AIMS manifest to verify the agent's identity and licence status
- The `telemetry.endpoint` field declares where the agent sends its events, providing a verifiable accountability chain

```
Agent retrieves content
  -> sends content_retrieved event to OA endpoint
  -> event includes agent_id = did:web:searchco.com:agents:web-search

Publisher receives event
  -> resolves did:web:searchco.com:agents:web-search to AIMS manifest
  -> checks: does this agent hold a licence for my domain?
  -> checks: does this agent report to a recognised telemetry endpoint?
```

Without AIMS, telemetry events are anonymous. Without telemetry, AIMS manifests are unverifiable claims. The two specs are designed to work together.

### 6.12 Complementary documentation standards

AIMS does not replace Model Cards, Dataset Cards, or A2A Agent Cards. It references them.

| Standard | What it documents | AIMS reference field |
|----------|------------------|---------------------|
| Model Cards | Performance, ethics, limitations | `deployment.modelCardUrl` |
| Dataset Cards | Training data composition, collection methodology | `foundation` links to external Dataset Card URLs |
| A2A Agent Cards | Functional capabilities, skills, I/O modes | DID Document service endpoint or `deployment` metadata |

Organisations deploying AI agents should publish AIMS manifests for compliance transparency alongside these other documentation standards.

---

## 7. Use cases

### 7.1 Publisher verifies agent compliance

A news publisher wants to know which AI agents are licensed to access their content and whether those agents report usage.

The publisher's access control system (CDN, server-side middleware, or RSL CAP) receives a request from an agent. The agent presents its DID. The publisher resolves the DID to an AIMS manifest and checks:

1. Does the `licences` array include an entry for the publisher's domain?
2. Does the `telemetry` field point to a recognised OA endpoint?
3. Is the manifest signed and current?

If all checks pass, the publisher grants access. Usage appears in their OA telemetry dashboard. If the agent has no manifest, the publisher can still detect the request server-side (Path 2) and log it as unidentified agent traffic.

### 7.2 Brand monitors content presentation

A brand (e.g. a credit card issuer) needs to know how AI agents present their products and terms. Misrepresentation of rates, fees, or features carries regulatory and reputational risk.

The brand registers their content domains with OpenAttribution. When agents cite their content, `content_cited` events flow through OA Telemetry. Each event includes the agent's AIMS identity. The brand can:

- See which agents cite their content and how often
- Resolve each agent's AIMS manifest to understand who operates it
- Cross-reference with an independent verification service to check whether content was faithfully represented

### 7.3 Licensing negotiation

An AI company wants to license content from a publisher consortium. The consortium requires telemetry reporting as part of the deal.

1. The consortium's RSL terms declare licensing conditions including access scope and pricing
2. The AI company acquires licences via RSL OLP
3. The AI company publishes an AIMS manifest listing the acquired licences and declaring its OA telemetry endpoint
4. The consortium's members verify compliance by checking AIMS manifests against telemetry data

The AIMS manifest is the machine-readable proof that the AI company holds the licences it claims and reports usage where it said it would.

### 7.4 Agentic browser identification

Agentic browsers and personal agents acting on behalf of users have no incentive to self-identify via user-agent strings. Many intentionally present standard browser fingerprints. AIMS provides an alternative: agents that want licensed access to content can present an AIMS identity voluntarily, in exchange for access that would otherwise be blocked or degraded.

This creates a two-tier system:
- **Identified agents** (with AIMS manifests) get licensed access and are accountable via telemetry
- **Unidentified agents** are detected server-side (Path 2) and logged as anonymous traffic

The incentive to adopt AIMS comes from the access it unlocks, not from a mandate.

---

## 8. Open questions

### 8.1 Identity challenge protocol

How should real-time identity verification work? Options:

- **Standalone challenge-response** - AIMS defines its own handshake protocol
- **A2A authentication extension** - AIMS verification piggybacks on A2A's existing auth flow
- **TSP transport** - identity challenge runs over TSP for cross-domain trust

The right answer likely depends on the deployment context. A standalone protocol is simpler but adds another integration point. An A2A extension leverages existing adoption. TSP provides the strongest cross-domain trust properties.

### 8.2 Attestation format

What is the minimal attestation schema for real-time identity proof? Candidates:

- **JWT** - widely supported, simple, good tooling
- **Verifiable Presentations** - W3C standard, supports selective disclosure
- **Signed HTTP headers** - lightweight, no separate exchange needed

### 8.3 Licence verification

AIMS manifests contain self-reported licence claims. How do we verify these claims independently?

- **RSL OLP verification** - query the publisher's OLP endpoint to confirm the licence exists
- **Trusted third-party attestation** - an independent service verifies licence claims and issues a Verifiable Credential
- **Publisher-side confirmation** - publisher signs the licence entry in the agent's manifest

This is closely related to the future OpenAttribution trust service described in the architecture.

### 8.4 Revocation

How do agents and publishers learn that a previously-valid manifest has been revoked? Options include Verifiable Credential status lists, short-lived manifests with frequent rotation, and revocation registries.

### 8.5 Transitive licensing

If Agent A has a licence and summarises content for Agent B, does the summary inherit licensing restrictions? The `redistribution` field in licence entries provides a starting point, but the mechanics of transitive licence enforcement across agent chains are unresolved.

---

## Appendix A: Compliant content access flow

The following describes a fully compliant content access event, showing which standard governs each step.

| Step | What happens | Standard | Layer |
|------|-------------|----------|-------|
| 1 | Publisher declares licensing terms | RSL + robots.txt | Declaration |
| 2 | Agent discovers terms and requests access with licence token | RSL OLP + CAP | Access control |
| 3 | Agent presents AIMS manifest proving identity and licensed status | AIMS | Identity |
| 4 | Publisher grants access; agent retrieves content | HTTP + RSL enforcement | Access control |
| 5 | Agent sends retrieval event to publisher's telemetry endpoint | OA Telemetry | Telemetry |
| 6 | Agent uses content in a response; sends citation event | OA Telemetry | Telemetry |
| 7 | User engages with the response; agent sends engagement event | OA Telemetry | Telemetry |
| 8 | Trusted service independently verifies telemetry accuracy and licence compliance | Future: OA Trust Service | Trust (future) |

Steps 1-2 exist today (RSL 1.0 shipped December 2025). Steps 3-4 are what this spec defines. Steps 5-7 are defined by the OA Telemetry spec. Step 8 is future work.

---

## Appendix B: Related standards reference

| Standard | Organisation | Status | Relevance to AIMS |
|----------|-------------|--------|-------------------|
| [W3C DIDs v1.1](https://www.w3.org/TR/did-core/) | W3C | CR March 2026 | Core identity format (dependency) |
| [W3C Verifiable Credentials v2.0](https://www.w3.org/TR/vc-data-model-2.0/) | W3C | Rec May 2025 | Manifest signing and packaging |
| [RSL v1.0](https://rslstandard.org/rsl) | RSL Collective | Finalised Dec 2025 | Publisher-side content licensing |
| [IAB Comp Protocol](https://iabtechlab.com) | IAB Tech Lab | Active | AI content monetisation |
| [A2A Protocol](https://github.com/a2aproject/A2A) | Linux Foundation | Active | Agent interoperability |
| [ANP](https://github.com/agent-network-protocol) | Open source | Active | Decentralised agent communication |
| [TSP](https://trustoverip.org/tsp/) | Trust over IP / LF | Active | Cross-domain trust transport |
| [AGNTCY OASF](https://agntcy.org) | Cisco / open source | Active | Agent directory and schema |
| [IETF ANS](https://datatracker.ietf.org) | IETF | Draft | Agent name resolution |
| [C2PA v2.2](https://c2pa.org/specifications/) | C2PA / Linux Foundation | Active | Media provenance |
| [CAWG](https://identity.foundation/creator-assertions/) | DIF | Active | Creator identity assertions |
| [OA Telemetry](https://openattribution.org/telemetry) | OpenAttribution | v0.1 | Content usage telemetry |
| [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309) | IETF | Standard | robots.txt |
| [RFC 8615](https://www.rfc-editor.org/rfc/rfc8615) | IETF | Standard | .well-known URIs |

---

## Appendix C: Glossary

| Term | Definition |
|------|-----------|
| **AIMS** | Agent Identity and Manifest Standard. This specification. |
| **A2A** | Agent-to-Agent Protocol. Agent interoperability standard (Linux Foundation). |
| **ANP** | Agent Network Protocol. Decentralised agent communication using W3C DIDs. |
| **ANS** | Agent Name Service. IETF draft for agent identity resolution. |
| **CAP** | Crawler Authorisation Protocol. RSL component for verifying licence tokens at access time. |
| **CAWG** | Creator Assertions Working Group (DIF). Identity assertions for content provenance. |
| **C2PA** | Coalition for Content Provenance and Authenticity. Media provenance standard. |
| **DID** | Decentralised Identifier. W3C standard for verifiable, self-sovereign digital identity. |
| **did:wba** | Web-Based Agent DID method (ANP). |
| **did:web** | Web-based DID method. Resolves to an HTTPS URL. |
| **OASF** | Open Agent Schema Framework. Cisco AGNTCY's data model for agent attributes. |
| **OLP** | Open Licence Protocol. RSL component for licence acquisition via OAuth 2.0. |
| **RSL** | Really Simple Licensing. Machine-readable content licensing standard. |
| **TSP** | Trust Spanning Protocol. Cross-domain trust transport (Trust over IP Foundation). |
| **TA2A** | A2A running over TSP for cross-domain trust. |
| **VC** | Verifiable Credential. W3C standard for cryptographically signed attestations. |
