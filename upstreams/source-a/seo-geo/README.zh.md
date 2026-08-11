<div align="center">

# SEO/GEO — SITE

**在传统搜索里排名，被 AI 引擎引用 —— survey、implement、tune、evaluate。**

[English](README.md) | 简体中文

</div>

> 这是 **[Aaron 营销技能库](../docs/README.zh.md)** 中的一个学科 —— 全库 120 个技能、七个学科、共享一套契约。要看整套体系、四层地图与安装步骤，请从[主 README](../docs/README.zh.md) 开始。

SEO/GEO 是一个常态 **L2 · 频道** —— 自有搜索引擎，把品牌叙事表达在人们（和 AI 助手）寻找答案的地方。十六个技能跑通 **SITE** 循环 —— **S**urvey 调研需求与竞争，**I**mplement 落地页面与标记，**T**une 打磨内容与技术健康，再 **E**valuate 评估排名、权威度与站外信号。上层有两套质量框架：内容用 **CORE-EEAT**，域名信任用 **CITE** —— 循环品牌名与基准名刻意分开。

## 循环 — Survey → Implement → Tune → Evaluate

- **Survey（调研）** —— 读懂全局：关键词需求与意图、竞品策略、真实 SERP，以及你缺失的选题。
- **Implement（落地）** —— 造资产：SEO/GEO 优化的文章与页面、AI 引擎优化、title/meta/OG 加 JSON-LD，以及模板化的 page play。
- **Tune（打磨）** —— 发布前后拉高质量：80 项 CORE-EEAT 发布门、技术健康、页面级卫生、站点结构与内链。
- **Evaluate（评估）** —— 度量并守住：40 项 CITE 域名信任门、排名追踪、带告警的多指标监测，以及站外 + AI 引荐信号分析。

## 16 个技能

链接指向各自的 `SKILL.md`。⛩ 标记本学科的两个 auditor 级质量门。

| 阶段 | 技能 | 作用 |
|------|------|------|
| **Survey** | [keyword-research](survey/keyword-research/SKILL.md) | 为某个页面/选题/campaign 启动关键词工作 —— 意图、需求，以及触手可及（striking-distance）的机会。 |
| **Survey** | [competitor-analysis](survey/competitor-analysis/SKILL.md) | 分析竞品的 SEO 策略、对比域名、挖出他们的关键词与缺口。 |
| **Survey** | [serp-analysis](survey/serp-analysis/SKILL.md) | 读懂一个 SERP —— 某查询的特性区块、摘要、People Also Ask、排名规律。 |
| **Survey** | [content-gap-analysis](survey/content-gap-analysis/SKILL.md) | 找出相对竞品缺失的选题与覆盖空洞。 |
| **Implement** | [content-writer](implement/content-writer/SKILL.md) | 撰写与刷新 SEO 优化的文章、落地页与产品文案。 |
| **Implement** | [geo-content-optimizer](implement/geo-content-optimizer/SKILL.md) | 为 AI 引擎优化内容（ChatGPT、Perplexity、AI Overviews、Gemini、Claude、Copilot）。 |
| **Implement** | [serp-markup-builder](implement/serp-markup-builder/SKILL.md) | Title/meta/OG/Twitter 标签，加 JSON-LD / Schema.org 结构化数据。 |
| **Implement** | [page-play-builder](implement/page-play-builder/SKILL.md) | 模板化 page play —— programmatic、parasite、对比页、本地/GBP *（4 种模式）*。 |
| **Tune** | ⛩ [content-quality-auditor](tune/content-quality-auditor/SKILL.md) | 80 项 CORE-EEAT 发布就绪门（SHIP/FIX/BLOCK）。 |
| **Tune** | [technical-seo-checker](tune/technical-seo-checker/SKILL.md) | 站点速度、Core Web Vitals、收录、可抓取性、robots。 |
| **Tune** | [on-page-seo-checker](tune/on-page-seo-checker/SKILL.md) | 审查页面级的 on-page 健康 —— 标题层级、关键词落位、图片、质量信号。 |
| **Tune** | [site-structure-optimizer](tune/site-structure-optimizer/SKILL.md) | 内链、锚文本、孤儿页、层级、URL 分类法、hub/spoke 集群。 |
| **Evaluate** | ⛩ [domain-authority-auditor](evaluate/domain-authority-auditor/SKILL.md) | 40 项 CITE 域名信任门（TRUSTED/CAUTIOUS/UNTRUSTED）。 |
| **Evaluate** | [rank-tracker](evaluate/rank-tracker/SKILL.md) | 追踪关键词排名、位次变化与掉排。 |
| **Evaluate** | [performance-monitor](evaluate/performance-monitor/SKILL.md) | 多指标 SEO/GEO 报表、仪表盘与阈值告警。 |
| **Evaluate** | [offsite-signal-analyzer](evaluate/offsite-signal-analyzer/SKILL.md) | 外链画像 + 链接质量，加上来自你自己 GA4/GSC/日志的 AI 助手引荐流量。 |

## 质量门 — CORE-EEAT + CITE

| 框架 | 评估 | 汇总 | 门 | 否决项 |
|------|------|------|----|--------|
| [CORE-EEAT](../references/core-eeat-benchmark.md) | 内容质量（80 项 / 8 维；诊断视图 CORE→GEO + EEAT→SEO） | 完整的档加权结果 | ⛩ [content-quality-auditor](tune/content-quality-auditor/SKILL.md) → SHIP/FIX/BLOCK | `T04`、`C01`、`R10` |
| [CITE](../references/cite-domain-rating.md) | 域名权威与引用信任（40 项 / 4 维） | 算术加权平均 | ⛩ [domain-authority-auditor](evaluate/domain-authority-auditor/SKILL.md) → SHIP/FIX/BLOCK/UNDECIDED | `T03`、`T05`、`T09` |

一个已核实的否决把终分封顶在 `min(raw, 59)`；两个及以上直接阻断。证据缺失记为 `Unknown` → `NEEDS_INPUT/UNDECIDED`，绝不自动判负。门的共享机制见 [auditor-runbook.md](../references/auditor-runbook.md)。

## 快速开始

```text
/aaron-marketing:seo-geo https://example.com/blog/my-article
/aaron-marketing:seo-geo --phase survey | implement | tune | evaluate
```

```text
/aaron-marketing:seo-geo 把我们的定价页做成一个能被 AI 引用的对比中枢
```

每个技能都在 **Tier 1** 用你粘贴或从免费/第一方来源（GSC/GA4、PageSpeed、Wikidata、Wayback）拉取的数据即可运行，永不要求付费 SEO 套件。

## 推荐场景

| 你的处境 | 从这里开始 | 得到什么 |
|---|---|---|
| 某个页面排名在下滑 | `/aaron-marketing:seo-geo <url> --phase tune` | CORE-EEAT 门判定（SHIP/FIX/BLOCK）+ 优先级修复清单 |
| ChatGPT / Perplexity 里没人引用你 | `--phase implement` → `geo-content-optimizer` | AI 引擎优化内容 + 引用探针读数 |
| 为新选题规划内容 | `--phase survey` | 关键词/意图地图、竞品缺口、SERP 形态 |
| 要上 500 个 programmatic 页面 | `page-play-builder`（programmatic 模式） | 页面模板 + 数据模型 + 内链方案 |
| 我的域名信任度够排名吗？ | `--phase evaluate` → `domain-authority-auditor` | 40 项 CITE 信任分 + 缺口清单 |

## 连接器

Keyless / 第一方方案覆盖整个循环：[`firecrawl.py`](../scripts/connectors/firecrawl.py)（实时 SERP + JS 渲染抓取）、[`tavily.py`](../scripts/connectors/tavily.py)（打分搜索 + AI 引用探针）、[`psi.py`](../scripts/connectors/psi.py)（PageSpeed/CrUX）、[`onpage.py`](../scripts/connectors/onpage.py) / [`schema_lint.py`](../scripts/connectors/schema_lint.py) / [`sitemap.py`](../scripts/connectors/sitemap.py) / [`robots.py`](../scripts/connectors/robots.py)（页面 + 站点卫生）、[`kg.py`](../scripts/connectors/kg.py)（Wikidata）、[`wayback.py`](../scripts/connectors/wayback.py)、[`openpagerank.py`](../scripts/connectors/openpagerank.py)，以及 [`indexpush.py`](../scripts/connectors/indexpush.py)（IndexNow + 百度普通收录，变更类）。完整方案清单见 [CONNECTORS.md](../CONNECTORS.md)。

---

<sub>属于 [Aaron 营销技能库](../docs/README.zh.md) · [系统架构](../docs/system-architecture.md) · [CORE-EEAT](../references/core-eeat-benchmark.md) · [CITE](../references/cite-domain-rating.md) · [贡献指南](../CONTRIBUTING.md)</sub>
