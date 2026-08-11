# WeChat (微信公众号 + 视频号) Platform Card

Last verified: 2026-07-05 · Review by: 2026-10-05 — re-check 群发 quotas, 视频号 length limits, and API scopes quarterly against 微信开放文档 (developers.weixin.qq.com); WeChat ships rule changes via 公开课 keynotes and quiet doc edits.

One card, two surfaces: 公众号 (Official Accounts — long-form articles pushed to followers) and 视频号 (Channels — vertical video with social-graph distribution). Both live inside the WeChat ecosystem: distribution, search, and monetization happen in-app, and the endgame of most WeChat strategies is the 私域 (owned-community) handoff.

## 公众号: article norms

| Element | Spec | Label / source |
|---------|------|----------------|
| Article title | Max 64 characters | Measured — mp.weixin.qq.com editor limit |
| 摘要 (digest) | Max 120 characters; becomes the share-card description for single-article pushes | Measured — editor limit |
| First-article cover | 2.35:1 (900×383 recommended) | Measured — editor guidance |
| Secondary-article cover | 1:1 square (shown for articles 2-8 in a multi-article push) | Measured — editor behavior |
| 群发 (mass push) quota | 订阅号 (subscription account): 1 push/day; 服务号 (service account): 4 pushes/month | Measured — 微信公众平台 official docs |
| Articles per push | Up to 8 articles bundled in one 群发 | Measured — composer limit |
| 原创 declaration | Marks the article as original: enables plagiarism protection, 赞赏 (tipping), and 白名单 reprint permissions. Declaring 原创 on non-original content is a punishable violation | Measured — 微信公众平台运营规范 |

Body norms (Estimated — WeChat-operator folklore, e.g. 新榜/运营派 write-ups): mobile-first formatting — short paragraphs, generous spacing, section subheads; readers arrive from chat shares, so the first screen must justify the tap.

## 公众号: in-ecosystem distribution

| Channel | What drives it | Label / source |
|---------|----------------|----------------|
| Follower push + chat/朋友圈 shares | The classic loop; 张小龙 said (2016-era 公开课 remark) that ~80% of article reads came via 朋友圈/chats rather than the subscription list — dated, but the share-loop primacy persists | Estimated — dated official remark + operator consensus |
| 看一看 (Top Stories) | Friend "在看" endorsements + algorithmic picks | Measured (surface exists, official) / Estimated (ranking weights — folklore) |
| 搜一搜 (WeChat search) | WeChat disclosed ~800M monthly users for 搜一搜 (微信公开课 disclosure). Keywords in title, first paragraph, and account name matter; 原创 status and account history weigh in | Measured (scale figure — official 公开课) / Estimated (ranking factors — operator folklore) |
| 推荐 (algorithmic feed) | Since ~2022, 公众号 articles get recommendation traffic beyond the follower base; officials have said recommendation-driven reads are a growing share | Measured (surface + official statements) / Estimated (specific shares) |

## 视频号: vertical video norms

- **Format:** 9:16 vertical, 1080×1920 recommended; horizontal 16:9 accepted but renders smaller in feed (Measured — upload guidance / product behavior).
- **Length:** short clips (< 60s) dominate feed distribution; long uploads (30+ min) supported via 视频号助手 (PC upload tool). Length bands and the "under-1-minute favored" claim are Estimated — operator folklore; official docs don't publish a preferred length.
- **Distribution is social-graph-first:** friend likes (朋友♥) push videos into contacts' feeds — 张小龙's 2021 微信公开课 keynote framed 视频号 as social recommendation ahead of machine recommendation (Measured — keynote; current ratio between social/machine/follow traffic is Estimated).
- **Livestream:** 视频号直播 supports 预约 (reservation) cards embeddable in 公众号 articles and shareable to 朋友圈/groups; commerce runs through 微信小店. Livestream is the main monetization surface for Channels (Measured — product features; revenue claims Estimated).

## 私域 handoff (the reason WeChat content exists)

Articles and videos are top-of-funnel; the conversion move is pulling readers into owned surfaces: 公众号 menu/auto-reply → 企业微信 (WeCom) contact or QR → 微信群 → repeat reach without 群发 quotas. Design the loop per `../social/owned-community-loop.md` — that reference owns the 私域 playbook; this card only marks the handoff points (article footer CTA, 视频号 profile link, livestream comment pin).

## Official-API reality

- **Personal subscription accounts have no posting API.** The draft-box (草稿箱) and publish (发布能力) APIs require 微信认证 (verification), which individual/personal accounts cannot obtain — so **no third-party tool can legitimately post for a personal 订阅号** (Measured — 微信开放文档).
- **服务号 API scope** (enterprise-verified): template messages, customer-service messages, OAuth web login, custom menus, 微信支付 — plus the publish APIs. Built for service delivery, not content cadence (Measured — 微信开放文档).
- **视频号 has no public posting API at all** — uploads are manual, in-app or via 视频号助手 (Measured — absence in official docs).

## Red lines (ToS / automation) — hard stop

- **Automation / cookie-session tooling = hard red line.** 协议号 (protocol clients), hooked clients, itchat/wechaty-padlocal-style session bots, and any cookie/session reuse trip WeChat 风控 and risk permanent 封号 — of the account *and* linked accounts. Agent workflows use the official composer / 视频号助手 manually; data comes from the user's own backend exports (manual-package lane only).
- **诱导分享/诱导关注** (incentivized sharing/following) is banned and enforced (Measured — 微信公众平台运营规范).
- **标题党** (clickbait titles) and false 原创 declarations draw demotion and credit penalties (Measured — 运营规范).
- **External-link and QR rules** inside articles/chats change often; check the current 外链管理规范 before campaign links (Measured — the rule doc exists; current thresholds need per-campaign verification).

## GEO/SEO relevance: shareable, barely indexed

`mp.weixin.qq.com` robots.txt disallows crawlers (Measured — checkable). Article URLs are public and shareable outside WeChat, but Google/Baidu coverage is thin and unreliable; the legacy Sogou 微信搜索 gateway has faded since Tencent absorbed Sogou. Treat 公众号 articles as **in-ecosystem assets**: real discoverability lives in 搜一搜, not external SERPs — republish cornerstone content on an owned domain if GEO/SEO citation matters.

## Pre-publish checklist

- [ ] 公众号 title ≤ 64 chars, no 标题党 phrasing; 摘要 ≤ 120 chars written for the share card
- [ ] Covers prepared at 2.35:1 (first article) and 1:1 (secondary slots)
- [ ] 原创 declared only if genuinely original; reprint permissions via 白名单
- [ ] First screen justifies the tap (readers arrive from chat shares, not the feed)
- [ ] 搜一搜 keyword present in title + first paragraph
- [ ] 群发 quota confirmed (订阅号 1/day, 服务号 4/month) — this push is worth the slot
- [ ] 私域 handoff CTA in place (footer QR / menu path per `../social/owned-community-loop.md`)
- [ ] 视频号: 9:16 at 1080×1920, hook in the first 2 seconds, livestream 预约 card linked if applicable
- [ ] Current 外链管理规范 checked for any campaign links
- [ ] Publishing manually via official composer / 视频号助手 — no session tooling anywhere

## Data access

Manual-package / user-export lane only — see `../social-platform-access.md` for the access matrix (公众号 backend analytics export, 视频号助手 dashboard; no scraper, no session tooling).

## Related

- `../social/owned-community-loop.md` — 私域 (企业微信/群) loop design
- `../social-platform-access.md` — data-access lanes per platform
