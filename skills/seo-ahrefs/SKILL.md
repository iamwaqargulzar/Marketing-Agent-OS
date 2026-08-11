---
name: seo-ahrefs
description: "Analyze live Ahrefs backlink, referring-domain, organic-keyword, and content data when an authorized Ahrefs connector is available. Use for Ahrefs-specific SEO evidence, not for estimates when no live connection exists."
license: Apache-2.0
metadata:
  version: "1.0.0"
  domain: "seo-geo"
  provenance: "marketing-agent-os"
---

# Ahrefs SEO Analysis

Use this adapter only when an authorized Ahrefs tool is already available. Never request a raw API key when the host can provide a managed connector.

## Workflow

1. Confirm the property, URL mode, country/database, date, and requested metrics.
2. Verify the connector and metric definitions before calling tools.
3. Estimate metered usage before batches of 50 or more URLs and obtain approval for material cost.
4. Separate live vendor metrics from calculated values and independent observations.
5. Reconcile conflicting backlink or traffic estimates by definition and collection date; do not silently average them.
6. Route toxic-link conclusions through `seo-backlinks` and SERP conclusions through `serp-analysis`.

## Output

Label every metric with source, scope, date, and confidence. Include limitations, discrepancies, prioritized actions, and a validation method.
