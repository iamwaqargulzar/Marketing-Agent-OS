# Xiaohongshu (小红书 / RedNote) Platform Card

Last verified: 2026-07-05 · Review by: 2026-10-05 — re-check composer limits, 薯条 eligibility rules, and 蒲公英 disclosure policy quarterly; XHS changes in-app limits without changelog announcements.

Xiaohongshu is a search-first, save-driven recommendation platform: users treat it as a lifestyle search engine, and the double-column feed rewards covers and titles that win the tap. Everything here works from the official app/web composer and the creator-center dashboard — there is **no legitimate third-party publishing or data API** for general use (see Red lines).

## Surface map: note anatomy + specs

| Element | Spec | Label / source |
|---------|------|----------------|
| 标题 (title) | Max 20 Chinese characters; counter enforced at publish | Measured — official composer limit |
| 正文 (body) | Max 1,000 characters | Measured — official composer limit |
| 话题 tags | Added inline with `#`; pick from the platform's suggested topics (typed free-text tags don't index the same way) | Measured — composer behavior; the "max 10 tags" figure is Estimated (creator-community consensus, e.g. 运营派/知乎 posts) |
| 图文 note images | Up to 18 images per note (expanded from 9) | Measured — official composer limit |
| Cover / artboard | 3:4 vertical fills the double-column feed card without cropping; 1242×1660 px is the standard artboard; 1:1 and 4:3 also accepted but render smaller | Measured (3:4 card render — product behavior) / Estimated (1242×1660 — designer-community convention) |
| Carousel norms | Image 1 = cover, decides the tap; text-on-image cover with a ≤13-char hook line; images 2-N carry the checklist/steps; last image = CTA or summary card | Estimated — creator folklore, consistent across 创作学院-style creator courses |
| Video note | Up to 5 min in the standard composer; longer unlocked for some creator tiers | Measured (composer default) / Estimated (tier extensions) |

## Organic engagement: official emphasis vs folklore

**What official communications actually say (Measured):**

- **Search is a first-class surface.** XHS executives (COO Conan/柯南, WILL 商业大会 2023) stated that ~70% of monthly active users use in-app search and positioned XHS as a "lifestyle search engine." Put target keywords in the title, first body line, and tags — notes keep earning search traffic for months.
- **Saves (收藏) are surfaced as a core metric** in the official creator-center analytics alongside likes/comments — the product treats save-worthiness (checklists, tutorials, price sheets) as the marker of long-term utility.

**Folklore (Estimated — marketing-blog consensus, never officially confirmed):**

- The **CES scoring formula** (like +1, save +1, comment +4, share +4, follow +8) circulating in Chinese marketing blogs (运营派, 知乎, 生财有术 threads). Directionally plausible (comments/saves > likes), numerically unverified.
- The **tiered traffic-pool model** (初级流量池 → escalating pools on engagement). Treat as a mental model, not a mechanic.

Practical takeaway: write for search intent + save utility; treat CES-style weights as a hypothesis to test against your own creator-center data.

## Posting norms

- **Cadence:** 3-5 notes/week is the common creator-course floor; consistency beats bursts (Estimated — creator folklore).
- **Comment culture is half the note.** Users ask specs/price/links in comments ("蹲一个链接", "求教程"); fast, substantive replies extend a note's life, and pinned self-comments carry the link/detail the body can't (Estimated — observed norm; comment velocity as a ranking factor is folklore).
- **Tone:** first-person experience ("亲测", real photos) outperforms brand-speak; overt ad tone triggers both user pushback and platform review.
- **One note = one job.** Single topic, single search intent; split multi-topic content into a series.

## 薯条 (paid boost) + brand-account rules

| Rule | Detail | Label / source |
|------|--------|----------------|
| 薯条 eligibility | Only original, review-passing notes can be boosted; medical/financial/exaggerated-claim content is ineligible | Measured — 薯条投放规则 (in-product rules page) |
| Commercial identity | Marketing accounts must upgrade to 专业号 (professional account) | Measured — 专业号 terms |
| Sponsored content | Brand-creator cooperation must be booked and declared through 蒲公英 (official creator marketplace); undeclared 软广 violates the 利益申报 (interest-disclosure) clause of the 社区公约 (Community Conventions, 2021) → 限流 or takedown, with periodic enforcement waves naming brands/agencies | Measured — 小红书社区公约 + 蒲公英 platform rules |

## Red lines (ToS / automation) — hard stop

- **No third-party API, no automation, no cookie-session tooling. Period.** XHS has no open publishing/data API for general third parties, and its 风控 (risk-control) system targets non-official clients, scripted engagement, scraping, and session reuse — penalties run from silent 限流 to permanent 封号. This is a **hard red line for any agent workflow**: manual publishing in the official app/web composer only; data comes from the user's own 创作中心 export or screenshots (manual-package lane).
- **No fake seeding (虚假种草):** buying engagement or undisclosed seeded reviews — official governance campaigns have publicly penalized brands and agencies (Measured — XHS governance announcements).
- **No off-platform diversion:** WeChat IDs/QR codes/external links in notes or comments trigger review (Measured — 社区公约; enforcement thresholds are Estimated).

## GEO/SEO relevance: effectively zero external index

`xiaohongshu.com` robots.txt disallows crawlers, and web note pages login-wall after minimal scrolling (Measured — checkable robots.txt + product behavior). Google/Baidu carry almost no XHS content, and external AI assistants rarely cite it. All SEO value is **in-app search** — keyword the title/body/tags for 搜一搜-style queries inside XHS itself, and don't count XHS notes as GEO-citable assets.

## Pre-publish checklist

- [ ] Title ≤ 20 chars, carries the primary search keyword
- [ ] Cover is 3:4 vertical with a ≤13-char hook line legible at feed size
- [ ] Body ≤ 1,000 chars, keyword in the first line, one topic per note
- [ ] 3-6 platform-suggested 话题 tags matching the search intent
- [ ] Save-worthy element present (checklist, steps, price sheet, template)
- [ ] Reply plan for the comment section (who answers "求链接/求教程", how fast)
- [ ] If sponsored: 专业号 active + cooperation declared via 蒲公英 — no undeclared 软广
- [ ] No WeChat IDs / QR codes / external links in note or planned comments
- [ ] Publishing manually in the official composer — no tooling touches the session

## Data access

Manual-package / user-export lane only — see `../social-platform-access.md` for the per-platform access matrix (creator-center export, screenshot packages; no scraper, no session tooling).

## Related

- `../social-platform-access.md` — data-access lanes per platform
- `../star-benchmark.md` — creator/content scoring when vetting XHS creators
