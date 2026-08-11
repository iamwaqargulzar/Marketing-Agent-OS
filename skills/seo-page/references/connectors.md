# Connector & Tool Layer

The core skills are dependency-free instruction packages. Optional connectors enrich evidence but must never become mandatory for portability.

## Search / SEO / web evidence
- Google Search Console, GA4, PageSpeed Insights / CrUX, IndexNow, Bing Webmaster equivalents
- DataForSEO, Ahrefs, Semrush, SERanking and other rank/backlink providers
- Firecrawl, Browserbase/Playwright-style rendering, Common Crawl, Wayback CDX
- Open PageRank, Wikidata, Wikipedia pageviews, GDELT, YouTube data, DNS-over-HTTPS

## Marketing execution / RevOps
- Google Ads, Meta Ads, LinkedIn Ads
- Resend, Mailchimp, Customer.io and comparable ESPs
- HubSpot, Salesforce, Stripe, Slack, Notion, Google Sheets
- Zapier / Composio-style integration layers
- Prospecting/enrichment providers such as Apollo, Clay, ZoomInfo, Hunter/Snov and GitHub public signals

## Rules
- Prefer native MCP/connectors when the coding agent already provides them.
- Keep API keys out of skills and source control.
- Default deterministic scripts to read-only/dry-run behavior.
- Respect source Terms of Service, rate limits, privacy/consent, robots directives and applicable law.
- Record source, timestamp and confidence for imported evidence.
