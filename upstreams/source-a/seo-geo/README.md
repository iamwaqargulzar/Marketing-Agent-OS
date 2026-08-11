<div align="center">

# SEO/GEO — SITE

**Rank in classic search and get cited by AI engines — survey, implement, tune, evaluate.**

English | [简体中文](README.zh.md)

</div>

> One discipline inside **[Aaron Marketing Skills](../README.md)** — 120 skills across seven disciplines on one contract. For the whole system, the four-layer map, and install steps, start at the [main README](../README.md).

SEO/GEO is an always-on **L2 · Channel** — the owned-search engine that expresses the brand narrative where people (and AI assistants) look for answers. Sixteen skills run the **SITE** loop — **S**urvey the demand and the competition, **I**mplement the pages and markup, **T**une content and technical health, then **E**valuate rankings, authority, and off-site signals. Two quality frameworks sit on top: **CORE-EEAT** for content and **CITE** for domain trust — the loop brand and the benchmark names are deliberately separate.

## The loop — Survey → Implement → Tune → Evaluate

- **Survey** — read the landscape: keyword demand and intent, competitor strategy, the live SERP, and the topics you're missing.
- **Implement** — build the assets: SEO/GEO-optimized articles and pages, AI-engine optimization, title/meta/OG plus JSON-LD, and template-driven page plays.
- **Tune** — raise quality before and after publish: the 80-item CORE-EEAT publish gate, technical health, on-page hygiene, and site structure / internal linking.
- **Evaluate** — measure and defend: the 40-item CITE domain-trust gate, rank tracking, multi-metric monitoring with alerts, and off-site + AI-referral signal analysis.

## The 16 skills

Links open each `SKILL.md`. ⛩ marks the discipline's two auditor-class quality gates.

| Phase | Skill | What it does |
|-------|-------|--------------|
| **Survey** | [keyword-research](survey/keyword-research/SKILL.md) | Start keyword work for a page/topic/campaign — intent, demand, and striking-distance opportunities. |
| **Survey** | [competitor-analysis](survey/competitor-analysis/SKILL.md) | Analyze a competitor's SEO strategy, compare domains, surface their keywords and gaps. |
| **Survey** | [serp-analysis](survey/serp-analysis/SKILL.md) | Read a SERP — features, snippets, People Also Ask, ranking patterns for a query. |
| **Survey** | [content-gap-analysis](survey/content-gap-analysis/SKILL.md) | Find missing topics and coverage holes versus competitors. |
| **Implement** | [content-writer](implement/content-writer/SKILL.md) | Write and refresh SEO-optimized articles, landing pages, and product copy. |
| **Implement** | [geo-content-optimizer](implement/geo-content-optimizer/SKILL.md) | Optimize content for AI engines (ChatGPT, Perplexity, AI Overviews, Gemini, Claude, Copilot). |
| **Implement** | [serp-markup-builder](implement/serp-markup-builder/SKILL.md) | Title/meta/OG/Twitter tags plus JSON-LD / Schema.org structured data. |
| **Implement** | [page-play-builder](implement/page-play-builder/SKILL.md) | Template-driven page plays — programmatic, parasite, comparison, local/GBP *(4 modes)*. |
| **Tune** | ⛩ [content-quality-auditor](tune/content-quality-auditor/SKILL.md) | 80-item CORE-EEAT publish-readiness gate (SHIP/FIX/BLOCK). |
| **Tune** | [technical-seo-checker](tune/technical-seo-checker/SKILL.md) | Site speed, Core Web Vitals, indexing, crawlability, robots. |
| **Tune** | [on-page-seo-checker](tune/on-page-seo-checker/SKILL.md) | Audit page-level on-page health — headings, keyword placement, images, quality signals. |
| **Tune** | [site-structure-optimizer](tune/site-structure-optimizer/SKILL.md) | Internal links, anchor text, orphan pages, hierarchy, URL taxonomy, hub/spoke clusters. |
| **Evaluate** | ⛩ [domain-authority-auditor](evaluate/domain-authority-auditor/SKILL.md) | 40-item CITE domain-trust gate (TRUSTED/CAUTIOUS/UNTRUSTED). |
| **Evaluate** | [rank-tracker](evaluate/rank-tracker/SKILL.md) | Track keyword rankings, position changes, and drops. |
| **Evaluate** | [performance-monitor](evaluate/performance-monitor/SKILL.md) | Multi-metric SEO/GEO reports, dashboards, and threshold alerts. |
| **Evaluate** | [offsite-signal-analyzer](evaluate/offsite-signal-analyzer/SKILL.md) | Backlink profile + link quality, plus AI-assistant referral traffic from your own GA4/GSC/logs. |

## Quality gates — CORE-EEAT + CITE

| Framework | Scores | Rollup | Gate | Veto items |
|-----------|--------|--------|------|------------|
| [CORE-EEAT](../references/core-eeat-benchmark.md) | Content quality (80 items / 8 dims; diagnostic CORE→GEO + EEAT→SEO views) | complete profile-weighted result | ⛩ [content-quality-auditor](tune/content-quality-auditor/SKILL.md) → SHIP/FIX/BLOCK | `T04`, `C01`, `R10` |
| [CITE](../references/cite-domain-rating.md) | Domain authority & citation trust (40 items / 4 dims) | arithmetic weighted mean | ⛩ [domain-authority-auditor](evaluate/domain-authority-auditor/SKILL.md) → SHIP/FIX/BLOCK/UNDECIDED | `T03`, `T05`, `T09` |

One verified veto caps the final score at `min(raw, 59)`; two or more block it. Missing evidence is `Unknown` → `NEEDS_INPUT/UNDECIDED`, never an automatic fail. Shared gate mechanics: [auditor-runbook.md](../references/auditor-runbook.md).

## Quick start

```text
/aaron-marketing:seo-geo https://example.com/blog/my-article
/aaron-marketing:seo-geo --phase survey | implement | tune | evaluate
```

```text
/aaron-marketing:seo-geo turn our pricing page into an AI-citable comparison hub
```

Every skill runs at **Tier 1** with data you paste or pull from free/first-party sources (GSC/GA4, PageSpeed, Wikidata, Wayback). No paid SEO suite is ever required.

## Recommended plays

| Your situation | Start here | What you get |
|---|---|---|
| A page is slipping in rankings | `/aaron-marketing:seo-geo <url> --phase tune` | CORE-EEAT gate verdict (SHIP/FIX/BLOCK) + prioritized fix list |
| Nobody cites you in ChatGPT / Perplexity | `--phase implement` → `geo-content-optimizer` | AI-engine-optimized content + a citation-probe read |
| Planning content for a new topic | `--phase survey` | Keyword/intent map, competitor gaps, SERP shape |
| Shipping 500 programmatic pages | `page-play-builder` (programmatic mode) | Page template + data model + internal-linking plan |
| Is my domain trusted enough to rank? | `--phase evaluate` → `domain-authority-auditor` | 40-item CITE trust score + gap list |

## Connectors

Keyless / first-party recipes cover the whole loop: [`firecrawl.py`](../scripts/connectors/firecrawl.py) (live SERP + JS-rendered scrape), [`tavily.py`](../scripts/connectors/tavily.py) (scored search + AI-citation probe), [`psi.py`](../scripts/connectors/psi.py) (PageSpeed/CrUX), [`onpage.py`](../scripts/connectors/onpage.py) / [`schema_lint.py`](../scripts/connectors/schema_lint.py) / [`sitemap.py`](../scripts/connectors/sitemap.py) / [`robots.py`](../scripts/connectors/robots.py) (page + site hygiene), [`kg.py`](../scripts/connectors/kg.py) (Wikidata), [`wayback.py`](../scripts/connectors/wayback.py), [`openpagerank.py`](../scripts/connectors/openpagerank.py), and [`indexpush.py`](../scripts/connectors/indexpush.py) (IndexNow + 百度普通收录, mutation-class). Full recipe list: [CONNECTORS.md](../CONNECTORS.md).

---

<sub>Part of [Aaron Marketing Skills](../README.md) · [System architecture](../docs/system-architecture.md) · [CORE-EEAT](../references/core-eeat-benchmark.md) · [CITE](../references/cite-domain-rating.md) · [Contributing](../CONTRIBUTING.md)</sub>
