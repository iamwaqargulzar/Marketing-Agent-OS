# Bluesky & Fediverse (Mastodon) Platform Norms

Last verified: 2026-07-05 · Review by: 2026-10-05 — open-protocol platforms ship fast; re-verify the API auth rows and folklore rows quarterly.

Two open-network platforms, one card. Both run on open protocols (AT Protocol / ActivityPub), both default to chronological feeds, and both punish broadcast-style marketing harder than any closed platform. Labels: **Measured** = official platform doc or live-verified call (named). **Estimated** = community folklore (source named) — directional only.

## Bluesky (AT Protocol)

### Surface map — formats + specs

| Surface | Spec | Evidence |
|---------|------|----------|
| Post | 300 graphemes max (≈300 chars for Latin text) | Measured — AT Protocol lexicon `app.bsky.feed.post` |
| Images | up to 4 per post, per-image alt-text field | Measured — lexicon `app.bsky.embed.images` |
| Native video | short-form; 60 s at launch, cap raised since — confirm in-app before planning video | Measured at launch (Bluesky blog, Sept 2024); current cap unverified |
| Link card | external embed (title/description captured at post time) | Measured — lexicon `app.bsky.embed.external` |
| Custom feeds | anyone can publish an algorithmic feed (feed generator) | Measured — Bluesky custom-feed docs |
| Starter packs | curated bundle of accounts + feeds, shared as one link | Measured — Bluesky blog (June 2024) |
| Handle = domain | a domain you control can be your handle (`@yourbrand.com`) | Measured — AT Protocol handle docs |

### Organic engagement — what the docs say vs folklore

- **The default Following feed is chronological.** There is no single engagement-optimized global feed to game (Measured — Bluesky feeds documentation). Reach comes from reposts, custom-feed inclusion, and starter-pack membership.
- **Custom feeds are the algorithm layer.** Getting picked up by popular topic feeds (many select on keywords/hashtags) is the closest thing to "going viral by algorithm" (Measured — feed-generator docs describe keyword/actor selection; which feeds matter is Estimated — community observation).
- **Starter packs drive follower growth.** Widely reported as the strongest onboarding-era growth lever (Estimated — creator-community folklore, Bluesky growth threads 2024–2025).
- **Alt text and link cards "boost reach"** — no official ranking claim exists; alt text is culture, not ranking (Estimated — community folklore). Do it anyway: the audience notices.

### Posting norms

- Chronological feeds reward posting cadence over single "optimized" posts; 1–3 posts/day beats weekly bursts (Estimated — community folklore).
- Culture is anti-engagement-bait: quote-dunking brands and "what's your favorite X?" prompts read as spam (Estimated — community norms).
- Set the domain handle for any brand account — it is the platform's built-in verification (Measured — handle docs).
- Label automated accounts as such in the bio/profile; undeclared bots get list-blocked fast (Estimated — community moderation culture).

### Red lines (ToS / automation)

- Spam, mass-follow/unfollow, and reply-blasting violate Bluesky Community Guidelines (Measured — Bluesky Community Guidelines).
- Moderation is composable: labelers and shared moderation lists propagate — one spammy campaign can get an account mass-blocked across thousands of subscribers (Measured — labeler/mod-list mechanics; blast radius Estimated).
- Posting via API needs the account owner's app password / OAuth session — own-account only, never harvested credentials.

### Data access

- Keyless reads: `getProfile` / `getAuthorFeed` / `getPostThread` on the public AppView `public.api.bsky.app` return public data with no auth (Measured — Bluesky "API Hosts and Auth" docs; live-verified 2026-07-05).
- `app.bsky.feed.searchPosts` returns **403 keyless** — it requires an authenticated session (app password) (Measured — live-verified 2026-07-05). Plan search-dependent work accordingly.
- Connector: `scripts/connectors/bluesky.py`. Access classes: [social-platform-access.md](../social-platform-access.md).

## Mastodon / fediverse

### Surface map — formats + specs

| Surface | Spec | Evidence |
|---------|------|----------|
| Post ("toot") | 500 chars default — per-instance configurable, some run 5,000+ | Measured — Mastodon docs (default); instance variance Measured per instance |
| Media | up to 4 attachments per post, alt-text supported | Measured — Mastodon API docs |
| Content warning | `spoiler_text` field folds the post behind a summary line | Measured — Mastodon API docs |
| Polls | built-in, per-post | Measured — Mastodon API docs |
| Hashtags | followable; the primary discovery surface | Measured — Mastodon docs (followed hashtags) |
| Trending | per-instance trending posts/tags/links, admin-reviewed before display by default | Measured — Mastodon admin docs (trends) |

### Organic engagement — hashtags are the algorithm

- **Home timeline is strictly chronological; there is no engagement-ranking feed** (Measured — Mastodon documentation). Discovery = hashtags people follow, boosts (reblogs), and local/federated timelines.
- Full-text search only covers accounts that opted in (Measured — Mastodon 4.2 release notes) — so hashtags carry discovery weight that search carries elsewhere. Use 2–4 relevant hashtags; camel-case them for screen readers (Estimated — fediquette guides).
- Boosts, not likes, spread posts — favourites are private appreciation with no distribution effect (Measured — Mastodon docs on boosts/favourites).

### Posting norms

- **Per-instance rules trump every global norm on this card.** Read the instance's `/about` rules before the first post; instances ban things as specific as unlabeled AI art or crossposted X content (Measured — each instance's published rules).
- CW conventions are real: many instances expect content warnings for politics, food, eye contact in photos — highly instance-specific (Estimated — fediquette guides + per-instance rules).
- Overt marketing is tolerated roughly nowhere and welcomed only on self-hosted or explicitly commercial-friendly instances; the durable play is a genuine participating account, or hosting your own instance under your own domain (Estimated — fediverse community folklore).

### Red lines (ToS / automation)

- Unsolicited commercial posting violates most major instances' rules → suspension, and repeat patterns get the *origin instance* defederated (fediblock) — collateral damage beyond your account (Measured — instance rules; fediblock dynamics Estimated — community practice).
- Automation itself is permitted via the official API with the account's own token, and bot accounts have an official flag — flag them (Measured — Mastodon API + bot flag). Cross-instance duplicate blasting is spam regardless of tooling.

### Data access

- Instance-local public APIs (`/api/v1/timelines/tag/<tag>`, public profiles/statuses) are keyless on most instances (Measured — Mastodon API docs; per-instance settings can restrict).
- `AUTHORIZED_FETCH` (secure mode) instances refuse anonymous fetches — the connector degrades gracefully: reports "instance requires auth" and moves on rather than erroring the run (Measured — Mastodon admin docs for the setting).
- Connector: `scripts/connectors/fediverse.py`. Access classes: [social-platform-access.md](../social-platform-access.md).

## GEO/SEO relevance (both networks)

- Bluesky: `bsky.app` profile/post pages render logged-out and are crawlable, unless the author enables the discourage-logged-out-visibility setting (Measured — Bluesky app setting exists; actual SERP presence Estimated — SERP observation). Domain handles double as an entity-consistency signal — align with `../entity-registry`-style `sameAs` data.
- Mastodon: per-user preference controls search-engine indexing and many users/instances opt out — treat Mastodon as a weak, per-instance SEO surface; the GEO value is community presence, not citations (Measured — the preference exists in Mastodon settings; aggregate behavior Estimated).

## Related

- [social-platform-access.md](../social-platform-access.md) — access-class taxonomy these data-access lines cite
- [../echo-benchmark.md](../echo-benchmark.md) — social scoring framework
- [../../CONNECTORS.md](../../CONNECTORS.md) — connector setup + free-recipe registry
