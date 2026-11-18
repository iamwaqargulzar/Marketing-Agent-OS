## Output Format

Generate **GEO-TECHNICAL-AUDIT.md** with:

```markdown
# GEO Technical SEO Audit — [Domain]
Date: [Date]

## Technical Score: XX/100

## Score Breakdown
| Category | Score | Status |
|---|---|---|
| Crawlability | XX/15 | Pass/Warn/Fail |
| Indexability | XX/12 | Pass/Warn/Fail |
| Security | XX/10 | Pass/Warn/Fail |
| URL Structure | XX/8 | Pass/Warn/Fail |
| Mobile Optimization | XX/10 | Pass/Warn/Fail |
| Core Web Vitals | XX/15 | Pass/Warn/Fail |
| Server-Side Rendering | XX/15 | Pass/Warn/Fail |
| Page Speed & Server | XX/15 | Pass/Warn/Fail |

Status: Pass = 80%+ of category points, Warn = 50-79%, Fail = <50%

## AI Crawler Access
| Crawler | User-Agent | Status | Recommendation |
|---|---|---|---|
| GPTBot | GPTBot | Allowed/Blocked | [Action] |
| Googlebot | Googlebot | Allowed/Blocked | [Action] |
[Continue for all AI crawlers]

## Critical Issues (fix immediately)
[List with specific page URLs and what is wrong]

## Warnings (fix this month)
[List with details]

## Recommendations (optimize this quarter)
[List with details]

## Agent-Readiness Signals (non-scoring)

### RFC 8288 Link Headers (Service Discovery)

**Status:** Present / Absent / Not Applicable

<!-- If present: -->
| Relation Type | URL | Meaning |
|---|---|---|
| api-catalog | /.well-known/api-catalog | Machine-readable index of available APIs |
| mcp-server-card | /.well-known/mcp.json | MCP server capability declaration |

AI agents and API clients can discover your services without parsing HTML.

<!-- If absent, API-first site only: -->
**Informational Recommendation:** This site has API/developer-oriented content but no `Link:` headers advertising discoverable services.

Example: `Link: </.well-known/api-catalog>; rel="api-catalog"`

Relevant for: sites with public APIs, OpenAPI docs, or MCP server integrations.
Reference: RFC 8288, RFC 9609.

<!-- If absent, standard business site: omit this section entirely -->

### Markdown Content Negotiation

**Status:** Supported / Not Supported
**Test:** GET [url] with `Accept: text/markdown`
**Response Content-Type:** [value]

<!-- If supported: -->
This site serves clean Markdown to AI agents on request. AI crawlers that support content negotiation receive formatted text without HTML boilerplate.

<!-- If not supported: -->
**Forward-Looking Recommendation:** Cloudflare Workers/Pages sites can enable Markdown content negotiation with a one-line configuration change. When an AI agent sends `Accept: text/markdown`, the server responds with clean Markdown instead of HTML.

- Currently Cloudflare-specific
- Relevant for: sites already on Cloudflare infrastructure
- Other CDNs and frameworks expected to adopt this pattern as AI agent traffic grows

## Detailed Findings
[Per-category breakdown with evidence]
```
