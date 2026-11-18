# Expert Panel — Multi-Persona Scoring Method

A documented method (not automated code) for scoring a draft against several named expert personas at once, then revising and rescoring until it clears a target. Shared by `creator-content-auditor` and `outreach-manager`. Adapted from the panel pattern in eric-osiu/ai-marketing-skills; rewritten and made vendor-neutral.

## What it is

You assemble 5–10 persona "lenses" — each a named expert with a background, one scoring angle, and the red flags they catch. The agent role-plays each lens against the draft, gives a 0–100 score with a one-line reason, averages them, then revises the weakest areas and rescores. Up to 3 rounds to hit the target. Every round's votes go in a table inside the deliverable so the human sees the reasoning trail, not just a final number.

This works on the user's own draft — paste the copy or content brief; no external tool, API, or account is needed.

## Run loop

1. **Pick the roster** for the content type (see examples below). Min 5 panelists, max 15 — more than 15 adds noise, not signal.
2. **Set the target** before round 1: default average ≥ 85, no single panelist below 70.
3. **Round 1 — score.** Each persona scores 0–100 with a one-line rationale. Record the vote table; compute the average.
4. **Revise.** Address the lowest scores and any specific red flags raised, smallest edit that fixes the issue.
5. **Rescore** with the same roster. Repeat revise→rescore up to 3 rounds.
6. **Stop** when the target is met, or after round 3. If still short, ship the best version and list the unresolved objections by panelist.

## Scoring bands (shared)

| Band | Meaning |
|------|---------|
| 90+ | Best-in-class for this lens; nobody would object |
| 80–89 | Strong; minor nits |
| 70–79 | Functional but forgettable / niche |
| <70 | Veto-level flaw — must fix before shipping |

## Example roster — content review (`creator-content-auditor`)

| Persona lens | Scores for | Red flags caught |
|--------------|------------|------------------|
| Viral Hook | Does the title/opening create a real curiosity gap? | Generic title, no specificity, no tension |
| Algorithm Fit | Will the platform recommend it (CTR, watch/read time, demand)? | Low-demand topic, no binge/rewatch pull |
| Brand Strategist | On-brand? Authentic to the founder's actual receipts? | Generic advice anyone could give |
| Differentiation | Is anyone else making this exact thing? Unique angle? | Crowded topic, commodity take |
| Engagement | Will it earn comments, shares, disagreement? | Consensus opinion, no stakes |
| Clip Potential | Can it be cut into 3+ short clips / quotable lines? | All framework, no emotional peaks |

## Example roster — outreach copy (`outreach-manager`)

| Persona lens | Scores for | Red flags caught |
|--------------|------------|------------------|
| Reply-rate | Does this earn a "tell me more"? Offer clarity, brevity | Vague value prop, walls of text |
| Frame & status | Positions sender as worth answering? Real proof? | Begging energy, "I just wanted to..." |
| Respect | Genuinely useful, or noise? Honest curiosity? | Fake personalization, presumptuous CTA |
| Pattern interrupt | Does the subject + first line stop the scroll? | "Hope this finds you well", predictable subject |
| Research depth | Proves the sender actually knows this prospect? | Surface-level research, generic compliment |
| Readability | Reads like a real person? Grade level, mobile render | Long sentences, passive voice, jargon |

## Swapping panelists

Match the roster to the offer or audience and define each new lens before round 1:
- Selling to a vertical → add a persona who lives in that vertical's buying language.
- Long email sequence → add a "sequence architecture" lens (does each follow-up add new value, not just bump?).
- Multi-channel → add a lens for the missing channel (LinkedIn warmup, phone layering).

## Vote table format (one per round)

| Panelist | Score | Rationale |
|----------|-------|-----------|
| [lens name] | XX | [one-line reason] |
| ... | XX | ... |
| **AVERAGE** | **XX** | |

Keep one such table per round in the deliverable so the revise→rescore trail is visible.

## Honesty notes

- These persona scores are structured judgment, not measured performance. A high panel average does not predict an actual reply rate, ranking, or view count — treat it as a pre-flight critique, then measure real results separately.
- The named-expert framing is a thinking device for forcing distinct lenses; it does not mean the named person endorsed anything.
- See `skill-contract.md` for how the scored draft and open objections hand off to the next skill.
