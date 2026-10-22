---
name: conversion-tracking
description: "Set up, audit, verify, or fix conversion delivery for forms, bookings, signups, calls, and purchases across analytics and ad platforms. Use for GTM/pixels, CAPI, enhanced conversions, server-side delivery, missing or duplicate conversions. For tracking plans and UTMs use `analytics`; for assigning credit use `attribution`; for campaign strategy use `ads`."
license: Apache-2.0
metadata:
  version: "1.0.0"
  domain: "paid-measurement"
  provenance: "marketing-agent-os"
---

# Conversion Tracking

Measure the defined business outcome and verify its delivery, rather than equating a tag firing with a received conversion. Read `references/skill-contract.md` for evidence, permissions, and handoffs.

## Scope and permissions

Start with the exact user-named site/property, desired outcome, destinations, existing implementation, and available evidence. Read relevant product context when present; do not invent missing setup or explore unrelated connected accounts.

A diagnosis request authorizes investigation, not implementation. A live form submission, booking, order, test conversion, tag publication, account edit, or upload can change records and bidding signals. Use an authorized staging/sandbox fixture where possible; obtain explicit scope for real submissions and writes. Report a blocked validation step instead of manufacturing a receipt.

## Setup or audit

1. Define the conversion precisely: accepted lead, confirmed booking, account created, paid order, qualified opportunity, or another specified outcome. A phone-link click measures click intent, not a completed call; a file click does not prove a completed download.
2. Inventory existing browser tags, native platform integrations, backend events, CRM jobs, and offline uploads. Browser inspection cannot establish that no server-side sender exists. Ask for the unresolved sender inventory before adding another source.
3. Locate the authoritative success signal. Prefer the backend/order/accepted-submission record when available. Otherwise use the provider's documented success callback/event for the installed version. Do not substitute submit clicks, popup close, page exit, or an unguarded thank-you-page visit.
4. Check existing consent handling, destination eligibility, field provenance, event/value/currency mapping, identifiers, deduplication, and error/retry behavior. Do not put raw contact details in URLs, analytics events, console output, or generic dataLayer payloads. Hashing does not remove permission and data-use requirements.
5. Choose a delivery option from `references/delivery-options.md`; preserve a working native path when adequate. A server-side sender does not bypass consent, access restrictions, or a missing success signal.
6. For diagnosis, report the supported cause, excluded causes, unknowns, and smallest reversible proposed change. For an explicitly requested fix/setup, implement only the authorized change and retain a rollback path.
7. Follow `references/verification.md` to prove detection, sending, destination receipt, and deduplication separately. If account access, a safe test, or sufficient observation time is unavailable, name the exact unverified boundary.

## Platform-specific work

Check current first-party documentation for the destination and installed tool version before producing a snippet, GTM import, API payload, or consent configuration. Do not retrieve or execute unreviewed remote snippets. Validate identifiers and keep secrets out of generated public assets; import/preview is not publication.

Cross-origin iframe success notifications require documented origin/source/payload checks. The parent page cannot read arbitrary iframe contact fields. An exposed event is not permission to exfiltrate them; consider a supported native integration, provider webhook, or backend record instead.

Distinguish browser receipt, accepted platform event, matched/attributed conversion, and bidding eligibility. Refunds/cancellations and primary/secondary conversion settings depend on the destination's current supported behavior, not a universal recipe.

## Output and handoff

Return the conversion definition, sender inventory, source evidence, consent/data flow, cause or setup plan, exact authorized change, test record IDs/timestamps, destination receipt, rollback, and remaining unknowns. Label consequential evidence `measured`, `user-provided`, `calculated`, `estimated`, or `proxy`.

Do not report DONE for end-to-end tracking when only local firing is verified. Use DONE_WITH_CONCERNS for a useful partial result, BLOCKED for a hard dependency, or NEEDS_INPUT for a material choice. Hand general event/UTM design to `analytics`, credit reconciliation to `attribution`, and CRM lifecycle definitions to `revops`.
