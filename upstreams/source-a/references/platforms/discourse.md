# Discourse Community Forums Platform Norms

Last verified: 2026-07-05 · Review by: 2026-10-05 — Discourse is self-hosted and per-instance configurable; re-verify the trust-level rows and data-access rows quarterly, and always against the specific instance in play.

The forum platform class the devtool community lens lives on. Discourse powers most modern developer/community forums (meta.discourse.org, many product community sites), and its trust-level model, not a ranking algorithm, governs who can do what. There is no engagement-optimized feed to game — the currency is standing earned by participation. Labels: **Measured** = official Discourse doc or live-verified call (named). **Estimated** = community folklore (source named) — directional only.

## Surface map — formats + specs

| Surface | Spec | Evidence |
|---------|------|----------|
| Topic | a titled thread in a category; the unit of discussion | Measured — Discourse docs (topics/categories) |
| Reply ("post") | a post within a topic; Markdown + BBCode + limited HTML | Measured — Discourse docs (Markdown/CommonMark support) |
| Category / sub-category | hierarchical organization, per-category permissions | Measured — Discourse category-security docs |
| Tags | cross-category labels, followable/mutable per user | Measured — Discourse tags docs |
| Trust levels | TL0 (new) → TL1 (basic) → TL2 (member) → TL3 (regular) → TL4 (leader); capabilities unlock per level | Measured — Discourse trust-level docs |
| Solved / accepted answer | optional plugin marks a reply as the accepted solution | Measured — discourse-solved plugin (per-instance install) |
| Likes / reactions | a like is the base signal; reaction sets are a per-instance plugin | Measured — Discourse docs; reaction plugin per-instance |

## Trust-level model (TL0–TL4)

Discourse's spam and permission control is the trust-level ladder — automatic, activity-earned, not moderator-granted (except TL4):

- **TL0 (new user):** rate-limited, link/image-restricted, cannot PM freely — the anti-spam floor for accounts that just signed up (Measured — trust-level docs).
- **TL1 (basic):** granted after reading a handful of posts/topics; unlocks links, images, and basic PMs (Measured — trust-level docs; thresholds are per-instance defaults).
- **TL2 (member):** granted after sustained reading/posting over days; unlocks inviting others, more edit latitude (Measured — trust-level docs).
- **TL3 (regular):** earned on a rolling activity window (reading, posting, days-visited, low flag rate) — losable if activity drops; unlocks recategorize/rename, wiki editing, some moderation-lite powers (Measured — trust-level docs; TL3 requirements are configurable and revocable).
- **TL4 (leader):** manually granted by staff only — near-moderator standing (Measured — trust-level docs).

## Community-health signals

The metrics a healthy owned or watched instance is read against (all denominators must be named + period-stable — ECHO O1):

- **Time-to-first-response** — median wait for a first reply on new topics; the lead indicator of a living forum (Estimated — community-ops folklore; instrument it from the instance's own topic timestamps for a Measured local number).
- **Trust-level distribution** — the shape of the TL0→TL4 population; a top-heavy or bottom-heavy curve both signal trouble (few regulars vs. no onboarding) (Estimated — community-health folklore; TL counts are Measured from the admin dashboard).
- **Moderator bus-factor** — how many active TL4/staff carry moderation; a bus-factor of one is a standing risk to the community's continuity (Estimated — community-ops folklore).

## Participation norms

- **Give-before-ask.** Answer, correct, and thank before you post your own promotional topic; a first-post pitch from a TL0 account reads as spam and is often auto-held (Estimated — forum community folklore, reinforced by TL0 rate limits which are Measured).
- **Read-before-post.** Search existing topics first; duplicate-question topics get merged or closed, and the reflex is baked into TL1 (which requires reading before it unlocks) (Measured — TL1 read requirement; the etiquette itself is Estimated).
- **Owned instance vs. participating in others'.** On your **own** Discourse you set categories, trust thresholds, and rules and can post announcements freely. When **participating in someone else's** forum you are a guest under their rules and their TL ladder — earn standing there the same as any member; do not treat a third-party forum as an owned channel (Estimated — community-norm folklore). This is the E1 channel-truth split: record which class each forum is in `channel-registry`.
- **One topic per question, one category per topic.** Cross-posting the same topic into multiple categories reads as spam (Estimated — fediquette-style forum norms).

## Red lines (ToS / automation)

- **No astroturfing.** Sockpuppet accounts, fake questions staged to answer with your product, and coordinated upvote/like rings are ECHO H1 (manufactured/baited engagement) and violate essentially every forum's rules → ban + defederation of trust (Measured — ECHO H1 veto; per-forum rules Measured per instance).
- **No rep-farming.** Gaming trust levels or badges via low-value posts, like-trading, or automated activity to unlock TL powers is against Discourse's own guidelines and instance rules (Estimated — community norm; TL3 flag-rate/quality gates are Measured deterrents).
- **Honor per-forum rules.** Each instance publishes its own FAQ/guidelines (usually the pinned "FAQ" / "Community Guidelines" topic); those trump every global norm on this card — read them before the first post (Measured — each instance's published guidelines).
- **Automation is owner-scoped.** Any API write uses the account owner's own API key (admin- or user-issued), own-account only, never harvested credentials; this discipline ships no posting/engagement/DM automation regardless.

## Data access

- Discourse exposes a **public read JSON API by appending `.json`** to most URLs — `<forum>/latest.json`, `<forum>/t/<slug>/<id>.json`, `<forum>/c/<category>.json`, `<forum>/tag/<tag>.json` return public data with no key on instances that leave anonymous reads open (Measured — Discourse "reverse-engineered" public JSON convention; per-instance login-required setting can gate it).
- Connector: `scripts/connectors/discourse.py` — reads the `.json` endpoints above with a robots.txt pre-flight; **caveat:** instances that enable *login-required* (or aggressive rate/anti-scrape rules) return **403/redirect to login** for anonymous reads — the connector degrades gracefully (reports "instance requires auth / robots-disallowed" and moves on rather than erroring the run). Honor `robots.txt` and the instance's crawl-rate rules. Access classes: [social-platform-access.md](../social-platform-access.md).

## GEO/SEO relevance

- Public Discourse topics render logged-out and are strongly crawlable — forum threads are a durable long-tail SEO/GEO surface, frequently cited as answers for "how do I…" product/dev queries (Measured — public topics render server-side; SERP/citation presence Estimated — SERP observation). An accepted-solution reply on your own community forum is both a support artifact and a citable entity signal.
- On third-party forums the SEO value accrues to that forum, not to you — the win is community presence and the occasional linked/cited answer, not domain authority (Estimated — community-norm folklore).

## Related

- [social-platform-access.md](../social-platform-access.md) — access-class taxonomy these data-access lines cite
- [../echo-benchmark.md](../echo-benchmark.md) — social scoring framework
- [../../CONNECTORS.md](../../CONNECTORS.md) — connector setup + free-recipe registry
