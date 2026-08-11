# Social Platform Access Classes · 社媒平台接入分级

The access-class taxonomy cited by the channel portfolio matrix ([channel-portfolio-planner](../social/explore/channel-portfolio-planner/SKILL.md)), the channel dossiers ([channel-registry](../protocol/channel-registry/SKILL.md)), and the ECHO `E` *platform-capability fit* sub-item ([echo-benchmark.md](echo-benchmark.md)). Each class answers one question: **how may this platform's data be read, compliantly and keyless-first?** The publishing side needs no taxonomy because it is uniform: in this library every deliverable is a **ready-to-paste package a human ships** — there is no posting, engagement, or DM automation on any platform, open or closed.

## The five classes

| Class | Definition | Number labeling |
|-------|------------|-----------------|
| `api-keyless` | Documented public API or feed, no key or login — a connector or plain fetch may read it | Measured (with pull date) |
| `api-free-key` | Documented API behind a free developer key the user registers themselves | Measured (with pull date) |
| `user-export` | Closed platform — numbers enter only as the user's own native-analytics export or screenshot | Measured, as-of the export date, recorded as User-provided material |
| `manual-package` | No compliant programmatic surface at all — content is drafted here, published by a human in-app; metrics only via whatever the platform's own backstage exports | n/a for reads beyond the user's own export |
| `proxy-read` | Adjacent public signal standing in for a closed platform (GDELT news echo, Tavily web chatter, Wikipedia pageviews, Bluesky-as-adjacent-community) | **Always labeled proxy, never Measured** — the ECHO O1 red line |

## Per-platform read classes

| Platform | Read class | Notes |
|----------|-----------|-------|
| Bluesky | `api-keyless` | public AppView API — `scripts/connectors/bluesky.py` |
| Mastodon / Fediverse | `api-keyless` | public instance APIs — `scripts/connectors/fediverse.py` |
| Discourse forums | `api-keyless` | public JSON endpoints — `scripts/connectors/discourse.py` |
| Hacker News | `api-keyless` | Algolia + Firebase — `scripts/connectors/hn.py` |
| YouTube | `api-keyless` (RSS) / `api-free-key` (Data API) | `scripts/connectors/youtube.py`; shortlist-vetting scope per [CONNECTORS.md](../CONNECTORS.md) |
| Reddit | `user-export` | API access requires registration and terms review; no connector — treat reads as the user's own exports or a manual recipe |
| X / Twitter | `user-export` | native analytics export only; proxy reads allowed when labeled proxy |
| Instagram | `user-export` | native insights export only |
| TikTok | `user-export` | native analytics export only |
| LinkedIn | `user-export` | native analytics export only |
| Facebook | `user-export` | native insights export only |
| 小红书 | `manual-package` | 后台数据以用户自行导出为准；任何自动发布/自动互动都是硬红线（风控/封号） |
| 微信公众号 | `manual-package` | 公众号后台数据 = user-export；发布仅限人工在后台操作 |
| 视频号 | `manual-package` | 同上——助手后台导出为准，无合规程序化接口 |
| 抖音 | `manual-package` | 创作者后台/巨量算数导出 = user-export；发布仅限人工 |

## Rules of use

1. **Every matrix row and dossier records its class.** A channel without a recorded access class cannot satisfy the ECHO `E` platform-capability-fit sub-item.
2. **Proxy is never Measured.** A GDELT, Tavily, pageviews, or adjacent-platform read standing in for a closed platform is labeled proxy at every mention — presenting it as Measured trips the ECHO O1 veto.
3. **Classes are dated facts, not permanent truths.** Platforms open and close surfaces; when a class changes, the dated norm card under `references/platforms/` (maintained by platform-norm-profiler) and the dossier's rule-snapshot pointer record the change with a last-verified date.
4. **The automation red line is global.** `manual-package` marks platforms where automation additionally risks account survival (风控/封号), but no class — including `api-keyless` — permits automated posting, replies, or DMs anywhere in this library.
