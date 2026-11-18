# AI Crawler Policy

Use for robots audits and access recommendations. Record the date, live response, relevant directives, and the owner's intended policy.

## Separate the purposes

- Search discovery: verify each provider's search crawler and indexing requirements.
- User-directed retrieval: verify the provider's user agent and its documented handling of robots directives.
- Model training: decide independently of citation goals. Training access does not establish search eligibility.
- Grounding and other uses: inspect their documented controls separately; some tokens cover multiple uses.

As checked on 2026-10-05, OpenAI distinguishes OAI-SearchBot, ChatGPT-User, and GPTBot; Anthropic distinguishes Claude-SearchBot, Claude-User, and ClaudeBot. Recheck the first-party documentation below before changing rules. Robots preferences do not replace authentication or technical access controls.

## Inspect the delivered robots response

Fetch `/robots.txt` from the public site, including redirects, status, and CDN behavior. Compare the delivered directives with the owner's origin file when available. Evaluate specific user-agent groups; a wildcard allowance does not establish access for a more specific blocked agent.

The bounded `scripts/fetch_page.py URL/robots.txt --json` helper reports `cloudflare_managed` when the response has the managed-content marker. This is marker detection, not a full robots parser or proof that a crawler is blocked.

Cloudflare can prepend managed rules to the origin response. A managed block is an issue only when its effective rules conflict with the owner's declared policy. Intentional training restrictions are compatible with a search-visibility objective. Do not rate every training restriction as a critical citation failure, and do not disable controls without authorization.

Retest the public response after an authorized change. Report robots preferences, CDN/WAF enforcement, indexing evidence, and observed citations as separate facts.

## First-party sources

- [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)
- [Anthropic crawler documentation](https://privacy.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [Cloudflare managed robots documentation](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/)
- [Google crawler controls](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
