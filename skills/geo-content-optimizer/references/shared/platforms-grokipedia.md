# Grokipedia Playbook (AI-Citation Tactics)

Grokipedia is xAI's AI-generated encyclopedia (launched Oct 2025, ~6M+ articles). Users cannot edit pages directly — you suggest, Grok reviews. It matters here because ChatGPT, Perplexity, Gemini, Google AI Mode/Overviews, and Copilot cite Grokipedia for factual queries, so a citation there can surface your content inside AI answers. `geo-content-optimizer` references this file as the single Grokipedia home.

## Why it's worth a try (not a guarantee)

- The Verge (Jan 31 2026) reported ChatGPT, Gemini, AI Overviews, Perplexity, and Copilot all citing Grokipedia.
- Third-party SEO tools (Jan 2026) reported Grokipedia cited in roughly 263K ChatGPT responses vs Wikipedia's ~2.9M — far behind, but notable for a platform this new, with citation share trending up since mid-Nov 2025.
- Treat all figures as reported/estimated, not verified by us. There is no proven ranking effect; this is an opportunistic GEO channel, not a reliable one.

## How it works

| Action | What it is |
|--------|-----------|
| Suggest Article | Request a new topic; Grok web-searches for sources and may create it |
| Suggest Edit | Highlight text on an existing page, propose a richer/corrected version |
| Report Error | Flag wrong dates, outdated facts, broken citations, formatting bugs |

Prerequisite: a crawlable page (Google/X/Apple/email login at grokipedia.com to submit). Grok discovers sources by web search — if your page isn't indexable or doesn't mention the topic, it won't be found. Higher SEO rank helps discovery but isn't required. Review is AI-driven, typically within ~2 hours, with no guaranteed approval.

## The core constraint

Grok is strict and rejects promotional content and explicit "cite my URL" requests. Do not put your brand or URL in: Article Topic, Additional Details, Summary, or Edit content. The stealth approach below works by supplying genuinely useful, neutral facts and letting Grok rediscover your page on its own.

## Tactic 1 — Suggest Article (stealth)

Never put your own URL in a Suggest Article. Instead, rewrite your content's key concepts as neutral "aspects to cover" so Grok's web search rediscovers your page when it looks for sources.

1. Pull from your article: definitions, categories, use cases, technical terms, examples.
2. Rephrase them as encyclopedic "aspects to cover" and "areas of interest" — no brand, no URL.
3. Keep the topic specific. Vague topics ("Technology") get rejected; precise ones ("Virtual Staging Software") pass validation.

Paste-ready template:

```
Article Topic:
[Specific encyclopedic topic, e.g., 3D Model Generator]

Additional Details:
This topic matters because [neutral reason]. Please cover: [definition],
[types/categories], [common use cases], [how it differs from X].
Specific areas of interest: [subtopics drawn from your content, phrased neutrally].
```

## Tactic 2 — Suggest Edit

Keep Summary and Edit content brand-free and factual. Put your URL only in "Add another source," alongside 1-2 already-authoritative sources (industry report, trade publication) so it isn't a lone self-citation.

| Field | Do |
|-------|----|
| Summary | Brief, like a normal correction: "Expanded [section] with additional techniques" |
| Edit content | Substantive, neutral, accurate — expand a thin section into fuller subsections. Generic text gets rejected. |
| Add another source | Your URL + 1-2 authoritative sources |

Tip: wrap exact phrases you want inserted in "double quotes" so they're easy to Ctrl+F when applying.

Paste-ready template:

```
Target page: [Grokipedia page URL]

Summary:
Expanded [section] with [topic/techniques]

Edit content:
[Rich, neutral, encyclopedic prose. Use "double quotes" for exact phrases to add.]

Add another source:
- [your article URL]
- [1-2 authoritative sources]
```

## ToS / ethics

- Google's Site Reputation Abuse policy (2024) targets manipulative third-party content. Contributions should be genuinely accurate and useful, not pure link/mention manipulation.
- The "stealth" framing exists because Grok rejects overt promotion — but the line between neutral-and-useful and gaming the platform is real. If your page doesn't deserve the citation on the merits, don't force it.
- Don't submit false or unsupported claims to win an edit; Report Error and inaccurate edits both hurt the channel and your credibility.

## Quick checklist

- [ ] Source page is published and crawlable, and actually covers the topic
- [ ] Suggest Article: zero URLs, concepts rewritten as neutral "aspects to cover"
- [ ] Suggest Edit: brand-free Summary + Edit content; URL only in "Add another source" with 1-2 authoritative peers
- [ ] Topic is specific and encyclopedic, tone neutral
- [ ] Allow ~2 hours for AI review; approval not guaranteed

Related: `../core-eeat-benchmark.md` (content quality), `../../build/geo-content-optimizer/SKILL.md` (AI-visibility workflow).
