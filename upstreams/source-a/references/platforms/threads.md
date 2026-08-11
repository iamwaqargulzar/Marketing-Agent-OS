# Meta Threads Platform Norms

Last verified: 2026-07-05 · Review by: 2026-10-05 — Threads is algorithm-ranked and iterating fast (fediverse beta, ranking changes); re-verify the surface-map spec rows and the folklore rows quarterly.

Meta's text-first network, built on the Instagram graph and — unlike Bluesky and Mastodon — **algorithm-ranked, not chronological by default**. That single fact changes the play: reach is earned by the ranker, not by cadence into a chronological feed. Labels: **Measured** = official Meta/Threads doc or live-verified call (named). **Estimated** = community folklore (source named) — directional only.

## Surface map — formats + specs

| Surface | Spec | Evidence |
|---------|------|----------|
| Post | 500 characters max | Measured — Threads Help Center (post limits) |
| Image carousel | up to 10 images per post; a single-image post is the 1-image case | Measured — Threads Help Center (up to 10 photos) |
| Video | in-post video, short-form; length caps iterate — confirm in-app before planning video | Measured — Threads Help Center (video supported); current cap Estimated |
| Reply control | author sets who can reply (everyone / profiles you follow / mentioned only) | Measured — Threads Help Center (reply controls) |
| Quote / repost | quote-post and repost both distribute the original | Measured — Threads Help Center |
| Topic tags | one topic tag per post (a "tag," not free-form multi-hashtag) | Measured — Threads Help Center (add a topic tag) |
| Fediverse sharing | opt-in beta: posts federate to ActivityPub (Mastodon can follow/reply) | Measured — Meta fediverse-sharing announcement + Help Center (beta) |

## Organic engagement — algorithm-ranked, not chronological

- **The default feed is algorithm-ranked ("For You").** A chronological Following feed exists but is not the default surface — reach comes from the ranker, so a post that earns early replies/reposts gets amplified beyond your followers (Measured — Threads For You / Following feeds documented; ranking mechanics Estimated).
- **Replies are weighted heavily.** Threads folklore holds that conversation (replies, reply-to-reply) drives distribution more than likes — the network optimizes for discussion (Estimated — creator-community folklore; Meta has publicly emphasized "conversation," which is Measured framing, but exact ranking weights are unpublished).
- **One topic tag, not hashtag stacking.** Threads supports a single topic tag per post; stuffing multiple tags (X/Instagram-style) is neither supported nor rewarded (Measured — one-topic-tag UI; the "don't stack" norm is Estimated).
- **Early-window engagement matters** — the first replies/reposts in the minutes after posting are widely believed to set a post's trajectory (Estimated — creator folklore; no official ranking claim).

## Posting norms

- Write for replies, not broadcast: questions, takes, and prompts that invite genuine discussion outperform link-dumps (the ranker demotes bare outbound links per persistent creator folklore — Estimated).
- Use the single topic tag deliberately; treat it as categorization, not reach-hacking (Measured — one-tag limit).
- Set reply controls to match the post's risk (open for reach, restricted for sensitive/announcement posts) (Measured — reply-control feature).
- If federating, remember fediverse replies arrive from Mastodon-culture audiences with different norms — see [bluesky-fediverse.md](bluesky-fediverse.md) (Measured — fediverse beta interoperates).

## Red lines (ToS / automation)

- Threads runs under Meta's Terms + Community Guidelines — engagement pods, bought engagement, and automated reply/DM blasting are ECHO H1 violations and Meta-ToS violations → rate-limiting, shadow-limiting, or ban (Measured — Meta Community Guidelines; ECHO H1 veto).
- No undisclosed material connections and no realistic synthetic media passed as real — ECHO C2; Meta also has its own AI-content labeling rules (Measured — Meta AI-labeling policy; ECHO C2 veto).
- Automated posting, if any, must use the account owner's own official API token (see Data access) — own-account only, never harvested credentials; this discipline ships no posting/engagement/DM automation regardless.

## Data access

- **The official Threads API exists but is free-key-*with-Meta-app-setup*, not a simple free key.** To read/post you must: create a Meta developer app, add the **Threads use case** to it, and mint a long-lived **`$THREADS_TOKEN`** through Meta's OAuth flow (Measured — Meta Threads API docs / developer setup). This is a materially higher bar than a `resend.py`-class paste-in free key — it needs an app, a use-case grant, and a token exchange.
- **There is no keyless Threads read path.** Public post pages exist but there is no documented anonymous JSON read endpoint to build a keyless connector on (Measured — no public keyless read API documented as of 2026-07-05).
- **`threads.py` is RECIPE-ONLY for v15.0.0 — not a shipped connector.** It is deferred pending (a) the Meta-app + Threads-use-case + `$THREADS_TOKEN` setup above and (b) a live probe against that authenticated endpoint; until both land, Threads data pulls follow the documented manual recipe, not an in-repo connector. Access classes: [social-platform-access.md](../social-platform-access.md).

## GEO/SEO relevance

- Threads post pages render logged-out and are crawlable, so individual posts can surface in search and be cited — but the durable GEO value is community presence and conversation, not link authority (Measured — logged-out post pages render; SERP/citation presence Estimated — SERP observation).
- Fediverse-federated posts also appear on Mastodon instances, inheriting that surface's weak, per-instance indexing behavior (Measured — federation exists; indexing behavior per [bluesky-fediverse.md](bluesky-fediverse.md) is Estimated).

## Related

- [social-platform-access.md](../social-platform-access.md) — access-class taxonomy these data-access lines cite
- [../echo-benchmark.md](../echo-benchmark.md) — social scoring framework
- [../../CONNECTORS.md](../../CONNECTORS.md) — connector setup + free-recipe registry
