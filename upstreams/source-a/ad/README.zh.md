<div align="center">

# 付费广告 — ROAS

**从你自己账户的导出来打分的付费获客 —— 无需任何带 key 的广告 API。**

[English](README.md) | 简体中文

</div>

> 这是 **[Aaron 营销技能库](../docs/README.zh.md)** 中的一个学科 —— 全库 120 个技能、七个学科、共享一套契约。要看整套体系、四层地图与安装步骤，请从[主 README](../docs/README.zh.md) 开始。

付费广告是一个常态 **L2 · 频道** —— 购买触达的引擎，快速把品牌叙事摆到需求面前。十六个技能跑通 **ROAS** 循环 —— **R**esearch 调研账户结构与受众，**O**rchestrate 编排创意与出价，**A**ctivate 在启动门下激活账户，再 **S**cale 靠度量与配速放量。已接受的 offer 与声明实证存在 [`offer-claims-registry`](../protocol/offer-claims-registry/SKILL.md)；质量门是 [`ad-account-auditor`](activate/ad-account-auditor/SKILL.md)。一切都从你**自己账户的手动导出**打分 —— 带 key 的广告 API 从不是前置条件。

## 循环 — Research → Orchestrate → Activate → Scale

- **Research（调研）** —— 打地基：账户/campaign 结构与 campaign 类型匹配、种子与排除受众、搜索词挖掘，以及 Shopping/PMax feed 卫生。
- **Orchestrate（编排）** —— 造单元：RSA 标题与角度矩阵、A/B/增量测试设计、出价策略选择，以及点击后落地页 QA。
- **Activate（激活）** —— 花钱前先过门：RQS 启动 go/no-go 审查、转化信号 QA、版位/受众排除，以及转化价值映射。
- **Scale（放量）** —— 不浪费地增长：读单次改动的度量、对电商真相集的归因对账、预算配速，以及疲劳/频次管理。

> 注：这里的 **Activate** 指*账户放行（account-gating）* —— 同一个阶段词在红人学科里指*创作者触达*。

## 16 个技能

链接指向各自的 `SKILL.md`。⛩ 标记本学科的 auditor 级质量门。**ROAS 维度**列标出主要维度（**R**eturn 回报 · **O**ffer 报价 · **A**udience 受众 · **S**pend-efficiency 花费效率）。

| 阶段 | 技能 | ROAS | 作用 |
|------|------|:----:|------|
| **Research** | [campaign-architect](research/campaign-architect/SKILL.md) | A | 账户/campaign 结构、campaign 类型匹配、匹配类型、否定词/排除、付费↔自然的自我蚕食；带一个常态搜索词挖掘模式。 |
| **Research** | [audience-segment-builder](research/audience-segment-builder/SKILL.md) | A | 把你自己的客户/CRM/GA4 导出变成种子受众、lookalike 种子、排除分群，以及漏斗阶段定向图。 |
| **Research** | [search-term-miner](research/search-term-miner/SKILL.md) | A | 从搜索词报告中挖否定词、新关键词候选与匹配类型微调。 |
| **Research** | [product-feed-optimizer](research/product-feed-optimizer/SKILL.md) | O | Shopping/PMax feed 卫生 —— 标题、属性、GTIN、类目映射、拒登修复。 |
| **Orchestrate** | [ad-creative-builder](orchestrate/ad-creative-builder/SKILL.md) | O | RSA 标题/描述、钩子与角度矩阵，与落地页信息匹配。 |
| **Orchestrate** | [ad-test-designer](orchestrate/ad-test-designer/SKILL.md) | O·S | 设计 A/B/n 与增量测试（假设、变体矩阵、样本量/功效），读出显著性 → promote/kill。 |
| **Orchestrate** | [bid-strategy-planner](orchestrate/bid-strategy-planner/SKILL.md) | S | 依目标选择并配置出价策略（tCPA/tROAS/max-conversions）、设定种子目标、规划学习期过渡。 |
| **Orchestrate** | [landing-experience-checker](orchestrate/landing-experience-checker/SKILL.md) | O | 点击后页面 QA —— 广告相关性、加载速度、移动端与政策 —— 即广告↔页面信息匹配检查。 |
| **Activate** | ⛩ [ad-account-auditor](activate/ad-account-auditor/SKILL.md) | R·O·A·S | Auditor 级 ROAS 门：计算 RQS，执行 R1/R2/O1/O2/A1，产出 SHIP/FIX/BLOCK；带启动 go/no-go 模式。 |
| **Activate** | [conversion-signal-qa](activate/conversion-signal-qa/SKILL.md) | R | 上线前追踪 QA（事件触发、UTM 卫生、去重、窗口对齐、iOS-ATT 标记）—— 构建门要打分的 R1/R2 信号。 |
| **Activate** | [placement-exclusion-manager](activate/placement-exclusion-manager/SKILL.md) | A | 版位/受众排除清单 —— 品牌安全屏蔽、垃圾版位清理、无效花费抑制。 |
| **Activate** | [conversion-value-mapper](activate/conversion-value-mapper/SKILL.md) | R | 把转化动作映射到价值/权重与价值规则，让 tROAS 按真实毛利出价，而非原始计数。 |
| **Scale** | [paid-measurement-loop](scale/paid-measurement-loop/SKILL.md) | R·S | 在一个窗口内把一次已上线改动对照对照组回读 → Promote / Keep-testing / Rollback / Unproven。 |
| **Scale** | [attribution-reconciler](scale/attribution-reconciler/SKILL.md) | R | 对 GA4/电商真相集做常态订单号去重、窗口/币种归一、模型对比、增量。 |
| **Scale** | [budget-pacing-monitor](scale/budget-pacing-monitor/SKILL.md) | S | 在整个投放期追踪花费配速对照预算，标记欠投/超投，给出配速纠正建议。 |
| **Scale** | [fatigue-frequency-manager](scale/fatigue-frequency-manager/SKILL.md) | O | 盯频次与创意衰减信号，标记疲劳广告，排期刷新/轮换。 |

## 质量门 — ROAS

[ROAS](../references/roas-benchmark.md) 从四个维度评估付费广告 —— **R**eturn 回报 · **O**ffer 报价 · **A**udience 受众 · **S**pend-efficiency 花费效率。只有门会计算档加权的 **RQS = floor(档加权平均)** —— 其余每个技能只做一个维度然后交接。否决项 `R1`/`R2`/`O1`/`O2`/`A1` 会硬顶或阻断。门为 [`ad-account-auditor`](activate/ad-account-auditor/SKILL.md) → 在预算放量前给出 SHIP/FIX/BLOCK；共享机制见 [auditor-runbook.md](../references/auditor-runbook.md)。

## 快速开始

```text
/aaron-marketing:ad              # 从你的输入推断 ROAS 阶段
/aaron-marketing:ad --phase research | orchestrate | activate | scale
```

```text
/aaron-marketing:ad 放量之前先审查这个 Google Ads 账户 —— 导出已附上
```

每个技能都在 **Tier 1** 从你**自己账户的导出**打分 —— 无需任何带 key 的广告 API。

## 推荐场景

| 你的处境 | 从这里开始 | 得到什么 |
|---|---|---|
| 放量这个账户之前 | `/aaron-marketing:ad --phase activate` → `ad-account-auditor` | RQS 启动 go/no-go + 动预算前的修复清单 |
| 花费浪费在垃圾版位上 | `--phase activate` → `placement-exclusion-manager` | 排除清单 + 无效花费抑制 |
| 转化追踪看起来不对 | `conversion-signal-qa` | 事件触发 / UTM / 去重 / 窗口 QA（R1/R2 前置） |
| 广告在疲劳 | `--phase scale` → `fatigue-frequency-manager` | 疲劳广告标记 + 刷新/轮换排期 |
| 到底哪个创意赢了？ | `--phase orchestrate` → `ad-test-designer` | A/B/增量设计 + 显著性读数 → promote/kill |

## 复用自其他学科

以下技能计入各自的主场阶段，此处不重复计数：[budget-optimizer](../influencer/target/budget-optimizer/SKILL.md)（花费 + 出价配速/学习期模式）、[landing-optimizer](../influencer/report/landing-optimizer/SKILL.md)（点击后）、[roi-calculator](../influencer/report/roi-calculator/SKILL.md)（回报算法）、[report-generator](../influencer/report/report-generator/SKILL.md)，以及 [performance-analyzer](../influencer/report/performance-analyzer/SKILL.md)。

## 连接器

付费广告刻意**自有数据优先** —— 每个分数都来自你自己账户的手动导出，因此从不要求任何带 key 的广告平台 API。`advertools`（开源）帮你在本地解析并结构化这些导出；带 key 的广告平台 MCP 服务器仍是可选的 Tier 2/3 便利项，编目在插件之外。见 [CONNECTORS.md](../CONNECTORS.md)。

---

<sub>属于 [Aaron 营销技能库](../docs/README.zh.md) · [系统架构](../docs/system-architecture.md) · [ROAS 基准](../references/roas-benchmark.md) · [贡献指南](../CONTRIBUTING.md)</sub>
