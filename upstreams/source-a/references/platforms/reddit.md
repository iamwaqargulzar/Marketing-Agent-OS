# Reddit Playbook

How an agent drafts Reddit posts and comments that survive moderation and earn upvotes. Reddit is also a GEO surface: its threads are heavily cited in AI answers, so a useful post can show up in LLM responses long after it drops off the feed. Work from the user's own account stats and the subreddit's public rules — no paid API needed.

## Rules first, every time
Read the target subreddit's sidebar and pinned mod posts before drafting. Each sub sets its own rules on self-promo, link drops, flair, and title format, and mods remove on sight. When in doubt, paste the sub's rules in and check the draft against them.

| Gate | What to confirm |
|------|-----------------|
| Self-promo policy | Many subs cap promo at 1-in-10 posts or ban links outright |
| Flair | Required in many subs; wrong/missing flair = auto-removal |
| Title format | Some subs require `[tags]` like `[Discussion]`, `[Help]` — copy the format from current top posts |
| Account gates | Some subs set minimum karma + account age before you can post or link |

## The 90/10 rule
Keep posting 90% genuine value (help, story, insight) and at most 10% promotional. The OSS source frames this as roughly 1 promotional post per 6; treat the exact ratio as a per-sub judgment call, not a fixed law. Accounts that only ever promote get shadow-flagged by users and mods.

## Karma and age before promotion
Build standing before you post anything self-serving. The source suggests 100–1000+ comment karma before promotional posts; the real bar is whatever the sub's rules state plus enough history that you don't read as a throwaway. Comment helpfully in the sub for a while first.

## What the algorithm actually weighs
- **Upvote/downvote ratio beats raw score.** A post at +20 with few downvotes outranks +50 that's heavily contested. Write for the ratio, not the number.
- **Early engagement is weighted.** The first hour matters most — post when the sub is active (check timestamps on current top posts).
- **Author replies boost ranking.** Stay in the thread and answer comments; it lifts visibility and signals you're a real participant.

## Title
- Concise, specific, accurate — no clickbait. Reddit punishes bait with downvotes.
- Match the sub's tag format if it uses one.
- Keep it factual; save opinions and the ask for the body or comments.

## Body
- Lead with the value (the help, the story, the data). Don't bury it under a pitch.
- Casual, friend-to-friend tone. Corporate voice gets downvoted.
- End with an open question to invite discussion.
- Use Markdown: `**bold**`, `*italic*`, `-` or `1.` lists, `[text](url)` links, headers for longer posts.

## Content types that work
| Type | Why it lands |
|------|--------------|
| Experience sharing | Highest engagement; authentic first-person stories |
| Q&A / helpful answers | Builds trust and karma before you ever promote |
| Case study | Shows product value — only works if fully transparent |
| Tool recommendation | Give context plus honest pros and cons, including yours |

## GEO angle
Reddit threads are frequently cited in AI-generated answers, so a clear, genuinely helpful post is a durable GEO asset. There's no confirmed way to "rank" inside an LLM, so treat this as a side benefit of writing for humans, not a tactic with a proven lever: answer a real question completely, in plain language, and the thread becomes quotable.

## Agent output format
When generating Reddit copy, return:
1. **Title** — in the sub's required format
2. **Body** — value-first, Markdown-formatted
3. **Suggested flair** — if the sub's flairs are known
4. **Rules reminder** — "Verify the subreddit's current rules and flair before posting"

## Related
- `../platforms/` — other platform playbooks
- `../star-benchmark.md` — influencer content scoring (Suitability/Trust/Appeal/Return)
