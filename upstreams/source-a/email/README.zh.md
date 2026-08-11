<div align="center">

# 邮件营销 — SEND

**面向自有受众的邮件 —— 通过认证、落进收件箱、带来转化。**

[English](README.md) | 简体中文

</div>

> 这是 **[Aaron 营销技能库](../docs/README.zh.md)** 中的一个学科 —— 全库 120 个技能、七个学科、共享一套契约。要看整套体系、四层地图与安装步骤，请从[主 README](../docs/README.zh.md) 开始。

邮件营销是一个常态 **L2 · 频道** —— 面向自有受众的引擎，把品牌叙事直送收件箱。十六个技能跑通 **SEND** 循环 —— **S**etup 搭好认证、名单与卫生，**E**ngage 用信息匹配的创意互动，**N**urture 沿生命周期培育，再 **D**eliver 在发送前质量门下投递。每个订阅者的同意与抑制由 [`consent-registry`](../protocol/consent-registry/SKILL.md)（邮件真相 SSOT）持有；质量门是 [`email-quality-auditor`](deliver/email-quality-auditor/SKILL.md)。

## 循环 — Setup → Engage → Nurture → Deliver

- **Setup（搭建）** —— 挣得发送资格：SPF/DKIM/DMARC/BIMI 认证预检、行为 + 生命周期分群与抑制、合规的名单增长采集，以及持续卫生。
- **Engage（互动）** —— 写出被打开、被点击的邮件：与落地页匹配的主题/预览文本/正文/CTA、主题行创意、HTML 渲染 QA，以及动态个性化。
- **Nurture（培育）** —— 搭生命周期：欢迎/购物车/购后/召回等自动化流加频次治理、newsletter 变现经济学、偏好中心设计，以及重新激活。
- **Deliver（投递）** —— 安全发送：EQS 发送前 go/no-go 门、A/B 与发送时段实验设计、收件箱落位监测，以及合规冷触达。

## 16 个技能

链接指向各自的 `SKILL.md`。⛩ 标记本学科的 auditor 级质量门。**SEND 维度**列标出主要维度（**S**ender-integrity 发件方诚信 · **E**ngagement 互动 · **N**urture 培育 · **D**irect-response 直接响应）。

| 阶段 | 技能 | SEND | 作用 |
|------|------|:----:|------|
| **Setup** | [deliverability-qa](setup/deliverability-qa/SKILL.md) | S | 预检 SPF/DKIM/DMARC/BIMI 认证、声誉、收件箱落位、垃圾内容与名单卫生（S1 检查）。 |
| **Setup** | [list-segment-builder](setup/list-segment-builder/SKILL.md) | E | 从你自己的名单/CRM/GA4 导出构建行为 + 生命周期阶段分群与抑制规则。 |
| **Setup** | [list-growth-designer](setup/list-growth-designer/SKILL.md) | S·N | 名单增长策略 —— 获客渠道、lead-magnet 概念、合规的 opt-in 采集流规格，以及裂变环机制。 |
| **Setup** | [list-hygiene-monitor](setup/list-hygiene-monitor/SKILL.md) | S | 持续的名单健康 —— 退信/投诉清理、sunset 策略、重新许可、沉默分群抑制。 |
| **Engage** | [email-creative-builder](engage/email-creative-builder/SKILL.md) | E·D | 主题/预览文本/正文/CTA，与落地页信息匹配，贴合声明台账。 |
| **Engage** | [subject-line-lab](engage/subject-line-lab/SKILL.md) | E | 主题/预览文本的创意与打分 —— 长度、垃圾触发词、好奇/清晰的平衡、用于测试的变体集。 |
| **Engage** | [email-render-builder](engage/email-render-builder/SKILL.md) | E | HTML 邮件构建/QA —— 客户端兼容、暗色模式、无障碍、纯文本替代、渲染测试清单。 |
| **Engage** | [dynamic-content-personalizer](engage/dynamic-content-personalizer/SKILL.md) | E | Merge-tag/liquid 个性化块、条件内容规则，以及兜底值安全。 |
| **Nurture** | [email-sequence-designer](nurture/email-sequence-designer/SKILL.md) | N | 生命周期/自动化流（欢迎、购物车、购后、召回）加频次治理。 |
| **Nurture** | [newsletter-monetization-planner](nurture/newsletter-monetization-planner/SKILL.md) | D | 付费订阅、赞助位 + 刊例价，以及推荐裂变环经济学。 |
| **Nurture** | [preference-frequency-manager](nurture/preference-frequency-manager/SKILL.md) | N | 偏好中心设计与发送频次治理，降低疲劳与退订。 |
| **Nurture** | [reactivation-specialist](nurture/reactivation-specialist/SKILL.md) | N | 面向沉默订阅者的召回/再互动流，带 sunset-或-recover 决策规则。 |
| **Deliver** | ⛩ [email-quality-auditor](deliver/email-quality-auditor/SKILL.md) | S·E·N·D | Auditor 级 SEND 门：计算 EQS，执行 S1/S2/N1/D1，产出 SHIP/FIX/BLOCK；带发送前 go/no-go 模式。 |
| **Deliver** | [send-experiment-designer](deliver/send-experiment-designer/SKILL.md) | E | A/B / 发送时段 / hold-out 设计，含样本量 + 显著性读数（promote/kill）。 |
| **Deliver** | [inbox-placement-monitor](deliver/inbox-placement-monitor/SKILL.md) | S | 通过 seed 名单与服务商信号持续追踪收件箱-vs-垃圾落位，带声誉漂移告警。 |
| **Deliver** | [cold-outbound-sequencer](deliver/cold-outbound-sequencer/SKILL.md) | D | 合规的 B2B 冷触达节奏 —— 送达安全的爬坡、个性化 token、回复处理步骤。 |

## 质量门 — SEND

[SEND](../references/send-benchmark.md) 从四个维度评估邮件 —— **S**ender-integrity 发件方诚信 · **E**ngagement 互动 · **N**urture 培育 · **D**irect-response 直接响应。只有门会从声明的 **promotional**、**retention**、**cold-outbound** 或 **newsletter** 档计算 **EQS = floor(档加权平均)** —— 其余每个技能只做一个维度然后交接。否决项 `S1`/`S2`/`N1`/`D1` 会硬顶或阻断。门为 [`email-quality-auditor`](deliver/email-quality-auditor/SKILL.md) → SHIP/FIX/BLOCK；共享机制见 [auditor-runbook.md](../references/auditor-runbook.md)。

## 快速开始

```text
/aaron-marketing:email              # 从你的输入推断 SEND 阶段
/aaron-marketing:email --phase setup | engage | nurture | deliver
```

```text
/aaron-marketing:email 给我们的 DTC 护肤名单设计一个 5 封的购后流
```

每个技能都在 **Tier 1** 用你粘贴的数据即可运行；连接器只自动化数据拉取，或一次经明确批准的发送。

## 推荐场景

| 你的处境 | 从这里开始 | 得到什么 |
|---|---|---|
| 邮件进了垃圾箱 | `/aaron-marketing:email --phase setup` → `deliverability-qa` | SPF/DKIM/DMARC/BIMI 认证读数 + 落位/卫生修复（S1） |
| 需要欢迎 / 购物车 / 召回流 | `--phase nurture` → `email-sequence-designer` | 生命周期流 + 频次治理 |
| 马上要群发整个名单 | `--phase deliver` → `email-quality-auditor` | EQS 发送前 go/no-go + 发送前修复清单 |
| 打开率在下滑 | `--phase engage` → `subject-line-lab` | 打分过的主题/预览文本变体，供测试 |
| 启动一条 B2B 冷序列 | `cold-outbound-sequencer` | 合规、送达安全的节奏 + 回复处理 |

## 复用自其他学科

以下技能计入各自的主场阶段，此处不重复计数：[audience-mapper](../influencer/scout/audience-mapper/SKILL.md)（人设 / 生命周期阶段）、[landing-optimizer](../influencer/report/landing-optimizer/SKILL.md)（点击后）、[roi-calculator](../influencer/report/roi-calculator/SKILL.md)（每次发送营收）、[report-generator](../influencer/report/report-generator/SKILL.md)、[performance-analyzer](../influencer/report/performance-analyzer/SKILL.md)，以及 [offer-claims-registry](../protocol/offer-claims-registry/SKILL.md)（D1 声明合规）。

## 连接器

[`doh.py`](../scripts/connectors/doh.py) 拉取发送域名的 SPF/DMARC/BIMI/MX 记录并探测常见 DKIM 选择器 —— 这是 keyless、适配任意 ESP 的 **S1 记录证据**（只给事实，不下判断）。[`resend.py`](../scripts/connectors/resend.py) 自动化唯一一个有免费额度 key 的 ESP：域名认证状态、按收件人 seed 测试发送、抑制同步与广播 —— **变更类子命令默认 dry-run，加 `--live` 才执行**。带 key 的 ESP 套件（Klaviyo、Mailchimp、HubSpot、Customer.io、Braze）仍在外部。完整清单见 [CONNECTORS.md](../CONNECTORS.md)。

---

<sub>属于 [Aaron 营销技能库](../docs/README.zh.md) · [系统架构](../docs/system-architecture.md) · [SEND 基准](../references/send-benchmark.md) · [贡献指南](../CONTRIBUTING.md)</sub>
