---
name: seo-unlighthouse
description: "Run or interpret bounded multi-page Unlighthouse audits for local Lighthouse evidence. Use for site-wide performance, accessibility, best-practice, and SEO regression checks when field data or API quotas are insufficient."
license: Apache-2.0
metadata:
  version: "1.0.0"
  domain: "seo-geo"
  provenance: "marketing-agent-os"
---

# Unlighthouse Site Audit

Treat local Lighthouse results as laboratory measurements, not field Core Web Vitals.

## Workflow

1. Confirm authorization, start URL, device profile, route cap, concurrency, and output location.
2. Verify the current Unlighthouse installation and command from first-party documentation before running it.
3. Preview any package installation or network-intensive crawl and obtain approval.
4. Run in a temporary output directory unless the user requests persistent reports.
5. Report medians and distributions; retain route-level failures instead of dropping them.
6. Separate lab metrics from CrUX or other field data and explain meaningful differences.
7. Route page-level performance remediation to `seo-performance` and crawl/index findings to `seo-technical`.

## Output

Return environment, route count, failed routes, score distributions, worst templates, prioritized fixes, and rerun instructions.
