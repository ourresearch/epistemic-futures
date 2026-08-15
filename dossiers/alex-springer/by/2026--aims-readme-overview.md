---
title: "AIMS — Agent Identity Manifest Standard (repository overview)"
person: "alex-springer"
section: "by"
type: "report"
year: 2026
date: "2026-06-11"
venue: "OpenAttribution"
authors: "Alex Springer (sole repository contributor; document carries no byline)"
source_url: "https://raw.githubusercontent.com/openattribution-org/aims/main/README.md"
retrieved: "2026-08-13"
content: "full-text"
notes: "Technical specification document from a GitHub repository where jalexspringer (Alex Springer) is the only listed contributor; all commits are authored as 'Alex Springer <alex@spurcoalition.org>' or '<alex@openattribution.org>', some via an automation account ('NarrativAI Agent') using the same address. The document itself carries no personal byline. Text is the verbatim Markdown source. Date is the file's last commit date."
---

# AIMS — Agent Identity Manifest Standard (repository overview)

## Full text

# AIMS - Agent Identity and Manifest Standard

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**v0.1 - Draft specification, open for comment.**

Verifiable identity for AI agents that access web content.

Part of the [OpenAttribution](https://openattribution.org) project. See also the [Content Telemetry standard](https://github.com/SPUR-Coalition/telemetry) for the content usage reporting format.

AIMS is the identity layer in the four-layer content-agent stack. It provides:

- **Agent identity**: DID-based, using any W3C DID method
- **Content licences**: Machine-readable proof of what content this agent is licensed to access
- **Telemetry compliance**: Links the agent's identity to its OpenAttribution telemetry endpoint

## Installation

```bash
pip install openattribution-aims
```

## Quick start

```python
from openattribution.aims import AIMSManifest, Operator, Licence, TelemetryCompliance

manifest = AIMSManifest(
    id="did:web:example.com:agents:my-agent",
    operator=Operator(name="Example Corp", domain="example.com"),
    licences=[
        Licence(source="reuters.com", type="rsl", scope="inference"),
        Licence(source="wirecutter.com", type="partnership", scope="full"),
    ],
    telemetry=TelemetryCompliance(
        endpoint="https://api.openattribution.org/v1/events",
        agent_id="did:web:example.com:agents:my-agent",
    ),
)

# Resolve another agent's manifest
from openattribution.aims import resolve_manifest

other = await resolve_manifest("did:web:other.com:agents:search")
if other:
    print(other.licences)
```

## Specification

Full specification: [SPECIFICATION.md](./SPECIFICATION.md)

## Where AIMS fits

| Layer | Question | Standard |
|-------|----------|----------|
| Declaration | What are the terms? | RSL, robots.txt |
| Access control | Does this agent have permission? | RSL CAP/OLP |
| **Identity** | **Who is this agent?** | **AIMS** |
| Telemetry | What happened after access? | OA Telemetry |

Without identity, telemetry is anonymous. Without telemetry, identity is credentials with no audit trail.

## Licence

Apache 2.0
