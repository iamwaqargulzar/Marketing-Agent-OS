# Conversion Quality Rubric (0-100)

An advisory rubric for scoring landing pages, signup flows, pricing pages, ads, and standalone CTAs on how well the copy and layout move a visitor to act. Used by `landing-optimizer` and by `content-quality-auditor` when the artifact is a conversion page. This is advice, not a gate: it produces a score and fix list, never a veto, and does not replace any CORE-EEAT or CITE item.

## Scope and inputs

Works on the user's OWN page (pasted copy, a screenshot, or a public URL the agent reads). No paid CRO tool, analytics login, or A/B platform is required to score it — judgment is made from what is visible on the page. If the user also has their own funnel data (conversion rate, bounce, form drop-off from their own dashboard), use it to confirm a low band; never invent those numbers.

## Four dimensions (~25 pts each)

| Dimension | What it measures |
|-----------|------------------|
| Headline / Hero | Does the first screen state a specific, relevant value prop? |
| Clarity & Friction | Can a visitor understand the offer and act without confusion? |
| Social Proof & Trust | Is the claim backed by credible, specific evidence? |
| CTA Strength | Is there one obvious action with copy that fits it? |

## Band descriptors

### Headline / Hero (0-25)
| Band | Looks like |
|------|-----------|
| 0-5 | Generic slogan, no value prop. Visitor can't tell what's offered. |
| 6-15 | States the offer but it's flat — no specificity or reason to care. |
| 16-20 | Clear value prop with a concrete detail (who it's for, what result). |
| 21-25 | Specific and relevant to the visitor's exact problem; hard to bounce from. |

### Clarity & Friction (0-25)
- Passes the 3-second test: offer is obvious on first glance.
- Visitor can complete the action without re-reading or hunting.
- No needless form fields, steps, or competing distractions.
- Page copy matches the ad / link / email that sent the visitor (message match).

### Social Proof & Trust (0-25)
- Proof is specific: numbers, named people, real companies — not "great product, love it."
- Trust signals (customer logos, guarantees, security/privacy notes) are present and verifiable.
- At least one case study or data point that actually supports the headline claim.
- No fabricated urgency or fake scarcity countdowns (these erode trust and can backfire).

### CTA Strength (0-25)
- Button copy names the action ("Get my audit" beats "Submit").
- Primary CTA is visible without scrolling on a typical screen.
- One clear primary action per page — no two CTAs competing for the click.
- Anxiety-reducing micro-copy near the button ("No card required", "2-minute setup").

## Scoring and handoff

- Sum the four dimensions for a 0-100 total. Report each dimension separately so the weakest one is obvious — the dimension scores drive the fix list, not the total.
- Rough read: 80-100 strong, 60-79 workable with clear fixes, below 60 the page is likely leaking conversions.
- Output the score, the weakest dimension, and 2-3 concrete edits. Hand back to `landing-optimizer` (or the calling auditor) as advisory input, not a pass/fail verdict.

Notes:
- Band wording for specific tactics is judgment, not a measured lift. Any conversion-rate impact is a hypothesis to test on the user's own page, not a guaranteed gain.
- Pairs with the publish-readiness check in `../auditor-runbook.md`; this rubric covers conversion intent that CORE-EEAT does not score directly.
