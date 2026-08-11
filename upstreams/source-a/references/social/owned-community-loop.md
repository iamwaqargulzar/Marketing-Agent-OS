# Owned-Community Loop — Entry, Lifecycle, and Share Instrumentation

Shared reference for brand-owned spaces such as Discord, Slack, Discourse, or 微信私域. [participation-warmup-planner](../../social/explore/participation-warmup-planner/SKILL.md) designs entry/lifecycle behavior and [dark-social-attributor](../../social/observe/dark-social-attributor/SKILL.md) consumes share instrumentation. Durable channel facts are submitted as authorized `operation: propose` events; [channel-registry](../../protocol/channel-registry/SKILL.md) owns acceptance and canonical transitions.

## The loop

```
entry → onboarding → participation → contribution → advocacy → renewal / clean exit
```

Each stage has a design decision (what the member gets and does) and a measurement seam (what the team can observe without surveillance). An owned space is judged on lifecycle health, not headcount: a 300-member space with rising contributor counts beats a 5,000-member ghost town on every ECHO read.

## Entry paths and incentives by space type

| Space type | Entry paths | Incentive patterns that hold | Access class |
|------------|------------|--------------------------------|--------------|
| Discord / Slack | per-surface invite links (docs, footer, launch posts, packaging inserts) | early-access channels, office hours, direct-line support, contributor roles | own space — full instrumentation |
| Self-hosted forum (Discourse-class) | open signup + trust-level ladder | badge ladder, answered-question service level, searchable archive as the public good | own space — `scripts/connectors/discourse.py` reads own data |
| 微信群 / 企业微信 私域 | per-surface QR 码, 客服号 handoff | 专属答疑, 资料包, 内测名额, 会员早鸟 | manual-package — per-surface QR codes are the only entry instrumentation; posting/DM automation is a hard red line (风控/封号) |

Entry incentives are promises — every one becomes a cadence or service commitment recorded against the space's dossier. An incentive the team cannot sustain (24/7 answers, weekly AMAs beyond capacity) is an over-commitment flag, not a growth idea.

## Member lifecycle stages

| Stage | Definition | Health signal (employee-excluded) |
|-------|-----------|-----------------------------------|
| Observer | joined, reads, has not posted | join→first-visit retention; onboarding completion |
| Participant | asks or reacts | time-to-first-response to their first post (Measured, own logs) |
| Contributor | answers others, shares work | contributor share of active members per period |
| Advocate | brings members, defends, reposts outward | referred joins via tagged invites; advocacy stays voluntary — roster rules in `memory/channels/advocate-roster.md` apply |

Orbit-level distribution and time-to-first-response are measured **without staff inflation** — employee and moderator activity is excluded from health counts (the ECHO `O` community-health sub-item). Stage-transition targets are Estimated heuristics with a named source (e.g. Discourse trust-level defaults, the team's own prior cohort), never scored rules.

## Exit hygiene

- Define dormancy per space (e.g. no visit in 60/90 days — Estimated, team-set) and use **one** re-engagement touch, then stop; repeated win-back pings in an owned space read as spam from the host.
- Keep the leave path clean: visible mute/leave options, no guilt copy, no re-invite loops. 企业微信 spaces follow the platform's 客户 opt-out rules — a removed member is a dated fact, not a re-add candidate.
- Prune dead channels/threads on a schedule; an owned space full of silent rooms fails the entry promise new members joined for.

## Share-loop instrumentation (the dark-social seam)

- **Tagged inbound**: every per-surface invite link and QR 码 carries the stable UTM taxonomy from the dark-social method doc (e.g. `utm_source=<surface>&utm_medium=community`); one taxonomy table, never changed mid-period.
- **Naked residue stays naked**: members who paste bare links into the space, DMs, or group chats are the dark social being *estimated*, not a defect to instrument away.
- **Second read**: a self-reported attribution field ("how did you hear about us" / 你从哪里看到我们) on signup or key forms — Estimated by nature, labeled as such, reconciled by [dark-social-attributor](../../social/observe/dark-social-attributor/SKILL.md).
- **Outbound legs**: newsletter and community cross-posts follow the same taxonomy so the community leg is separable from paid and feed legs in GA4/GSC exports (Measured, own data). Closed-platform legs (微信 group shares) enter only as QR-differentiated joins or user exports.

## Labeling discipline

Own-space analytics (join logs, response times, retention) are **Measured** with an as-of date. 微信/企业微信 numbers are user exports (**User-provided**). Every ratio, tenure, or dormancy threshold in this file's patterns is **Estimated** with a named source until the team's own cohort data replaces it. See [CONNECTORS.md](../../CONNECTORS.md) for the keyless reads.
