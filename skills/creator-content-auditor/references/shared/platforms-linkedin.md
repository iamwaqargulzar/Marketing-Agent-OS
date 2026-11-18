# LinkedIn Playbook (SEO/GEO Surface Map)

LinkedIn exposes some surfaces to Google and AI crawlers and login-gates the rest. This reference maps which is which, then gives format and cadence specs so you write each surface for the right audience. Work from the user's own profile/page and public LinkedIn pages — no paid API needed.

## Search Surface Map: Indexed vs Login-Gated

| Surface | Google indexed? | GEO (AI citation) value |
|---------|-----------------|-------------------------|
| Public profile (Headline, About, Experience) | Yes — for name/company/role queries | Strong entity signal; citable paragraphs |
| Articles (long-form editor, set public) | Yes | High — structured, keyword-rich paragraphs |
| Company Page | Yes — for brand queries | Medium — brand entity signal |
| Newsletter issues | Only if public; subscriber-only is gated | Depends on visibility setting |
| Short feed posts | No — login-gated | Low — cannot be cited behind login |

Takeaway: profile, public Articles, and the Company Page are the SEO/GEO assets. Short feed posts drive in-network engagement but carry near-zero off-site or AI-citation value. Do not rely on feed posts for GEO.

## Profile Fields That Rank

| Field | Treat it as | What to write |
|-------|-------------|---------------|
| Headline | Title tag | Primary keyword + value proposition (e.g. "B2B SaaS marketing — helping startups scale through content"). Most SEO-visible field; appears in search snippets. |
| About | Indexed body copy / AI-citable block | Answer-first paragraphs, 40-60 words each, with proof points and external links. Often surfaces in Google snippets. |
| Featured | Public link showcase | Site, case studies, press, portfolio. Adds reference links AI tools cite as supporting evidence. |
| Experience media | Thin indexed signal | Attach relevant docs/links/images per role. |
| Custom profile URL | Shareability | Set to firstname-lastname, not the default ID string. |

GEO note: AI search tools can cite a LinkedIn profile for "who is [person]" or "what does [company] do" queries. Answer-first About blocks (40-60 words) are extractable; long unbroken paragraphs are not. Keep name, company, and role identical across LinkedIn, the user's site, and other public bios for entity consistency (see `../entity-registry` analog: `sameAs` alignment).

## Post Types (organic)

| Type | Notes |
|------|-------|
| Text update | Short; pasting a URL adds a link preview. Feed-only, login-gated. |
| Photo / carousel | Single or multi-image (up to ~20). Vertical preferred — most browsing is mobile. |
| Video | Uploaded file; distinct from LinkedIn Live (separate gating). |
| Article | Long-form editor, separate from the post box. Indexed when public — the one feed-adjacent surface with off-site value. |
| Document | PDF/PPT/DOC shown as in-feed slides. Verify current limits at publish time (LinkedIn lists them in help). |
| Poll | Engagement driver; keep question and options scannable. |
| Newsletter | Subscription series; compounds reach. Indexed only if public. |

Match CTA and length to the form. A short hot take and a 1,200-word Article are not interchangeable.

## Character Limits and Length

| Element | Limit / target |
|---------|----------------|
| Post hard cap | 3,000 chars |
| Engagement sweet spot | 1,300-1,600 chars |
| First line (before "See more") | ~210 chars; put the key message in the first ~140 |
| Short post (poll/announcement/quote) | 100-200 chars |

The OSS source reports engagement drops sharply past ~2,000 chars and that most readers decide whether to expand at the first line. Treat both as the source's guidance, not a measured guarantee.

## Image Specs

| Format | Dimensions |
|--------|------------|
| Single / link preview | 1200×627 (1.91:1) |
| Square | 1200×1200 |
| Carousel | up to ~20 images |
| File | JPG/PNG, keep under ~10 MB |

Native uploads tend to outperform external links; vertical/mobile-first framing matters since most browsing is on phones.

## Cadence

- Company Pages: weekly minimum is a common floor.
- Individuals: several posts per week if sustainable beats erratic bursts.
- At least one public Article on a relevant topic gives you an indexed, citable asset that short posts cannot.

## Pre-Publish Checklist

- [ ] Headline = primary keyword + value proposition (read as a meta title)
- [ ] About written in answer-first 40-60 word blocks with proof points + links
- [ ] Featured section showcases site, case studies, key publications
- [ ] Name / company / role identical to the user's site and other bios
- [ ] At least one public Article published on a relevant topic
- [ ] Custom profile URL set (not the default ID string)
- [ ] First line of any post carries the message in ~140 chars

## How the Feed Ranks (for in-network posts)

Not reverse-chronological. It blends 1st-degree connections, follows, topic/company interest, and recommended out-of-network content, plus ads. Ranking signals are post context, profile/network fit, and behavior (reactions, comments, shares, dwell time). Recent public communications point toward more semantic understanding and less reward for engagement-bait or coordinated "pod" activity. Write a strong first line, add on-topic depth, and skip automated-looking templates.

## Related

- `../skill-contract.md` — shared handoff contract
- `../core-eeat-benchmark.md` — content quality scoring for Articles
