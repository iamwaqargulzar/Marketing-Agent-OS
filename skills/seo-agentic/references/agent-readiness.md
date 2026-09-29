# Agent-Readiness Evidence Checklist

Use only the sections relevant to the requested site and mode.

## Perception and interaction

- Controls have programmatic names, correct roles, visible labels, and deterministic focus order.
- Important state is available without hover, animation timing, or visual position alone.
- Validation errors identify the field, problem, and recovery action.
- Dialogs, menus, and forms expose open/closed, required, invalid, busy, and completion states.
- Consequential actions have an explicit review or confirmation boundary.

## Delivery and navigation

- Primary content and links exist in delivered HTML or a reliably rendered accessibility tree.
- Canonical URLs and navigation do not depend on fragile client-only state.
- Unknown paths return an honest error status rather than a catch-all success page.
- Redirects, authentication, locale selection, consent, and bot/WAF handling do not create silent loops.
- Layout shifts do not move controls between discovery and activation.

## Access-policy matrix

Report these separately:

| Purpose | Questions |
|---|---|
| Search/indexing | Which crawlers may retrieve public pages, and do canonical/index directives agree? |
| Model training | What is the owner's declared policy, and where is it expressed? |
| User-triggered agents | Can an authenticated agent act for a user under the same authorization and rate limits as the UI? |

Robots rules are not authentication. Never recommend exposing a private route because a crawler is blocked, or blocking a public security boundary only through robots.txt.

## Optional discovery and tools

Check a discovery surface only when a target consumer is documented. Record its specification/version, observed consumer support, and whether it is required, optional, experimental, or unsupported.

For an agent-facing tool, review:

- one bounded operation and input schema;
- server-side authentication and authorization;
- validation and output limits;
- declared side effects and confirmation;
- idempotency or duplicate prevention;
- audit receipt and safe error behavior;
- protection against instructions embedded in page or tool data.

## Finding format

For each finding provide:

`Observation → Evidence/source and date → Impact → Fix → Permission dependency → Retest`

Use `not tested` when authorization or tooling is absent. Do not convert an unavailable check into a pass or failure.
