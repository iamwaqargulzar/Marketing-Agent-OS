# Meta Ads (Facebook/Instagram)

Advertising platform for Facebook, Instagram, Messenger, and Audience Network.

## Capabilities

| Integration | Available | Notes |
|-------------|-----------|-------|
| API | ✓ | Marketing API for campaigns, audiences, reporting |
| MCP | ✓ | Official remote server at `mcp.facebook.com/ads` (Meta Ads AI Connectors), open beta since 2026-04-29, read and write; see [Official MCP server](#official-mcp-server) |
| CLI | - | Not available |
| SDK | ✓ | Official SDKs for Python, PHP, Node.js |

## Authentication

- **Type**: OAuth 2.0 Access Token
- **Header**: Access token as query parameter
- **Setup**: Create app in Meta Business Suite, generate System User token

## Official MCP server

Meta hosts an official ads MCP server, part of **Meta Ads AI Connectors** (open beta since 2026-04-29, checked 2026-10-15). It works with any MCP client, including Claude and ChatGPT. Meta also ships a local ads CLI with the same tool surface for terminal agents.

- **Endpoint:** `https://mcp.facebook.com/ads`
- **Claude setup:** Settings → Connectors → Add custom connector, paste the endpoint, then sign in with Facebook Login for Business (a Facebook account or Meta Managed Account) and approve permissions. No Meta developer app or system user token is needed.
- **Access:** you see the ad accounts your Facebook profile can access through its Business Portfolio. The open beta isn't enabled for every advertiser yet; if the connector authenticates but returns no ads tools, access hasn't reached that account.
- **Tools:** 29 at launch, across performance and insights, campaign creation and management, catalog management, accounts and assets, and dataset/signal diagnostics. Meta adds tools as products leave beta, so treat any count as a floor.
- **Cost:** free during the beta, within normal Marketing API rate limits.

**Start read-only.** The connector includes write tools (create campaigns, edit budgets and status). Run reporting and diagnostics for the first few weeks and check the answers against Ads Manager before allowing any write. After that, apply changes only as a reviewed plan (current state → change → expected effect → rollback) with explicit approval of that specific change. See the ads skill's [audit guardrails](../../skills/ads/references/audit-guardrails.md).

Use the Marketing API below when you need endpoints the connector doesn't expose, scheduled jobs without a chat client, or the repository CLI.

## Common Agent Operations

### Get ad accounts

```bash
GET https://graph.facebook.com/v18.0/me/adaccounts?access_token={access_token}&fields=id,name,account_status
```

### Get campaigns

```bash
GET https://graph.facebook.com/v18.0/act_{ad_account_id}/campaigns?access_token={access_token}&fields=id,name,status,objective,daily_budget
```

### Get campaign insights

```bash
GET https://graph.facebook.com/v18.0/{campaign_id}/insights?access_token={access_token}&fields=impressions,clicks,spend,actions,cost_per_action_type&date_preset=last_30d
```

### Get ad sets

```bash
GET https://graph.facebook.com/v18.0/act_{ad_account_id}/adsets?access_token={access_token}&fields=id,name,status,targeting,daily_budget,bid_amount
```

### Get ads

```bash
GET https://graph.facebook.com/v18.0/{ad_set_id}/ads?access_token={access_token}&fields=id,name,status,creative
```

### Create campaign

```bash
POST https://graph.facebook.com/v18.0/act_{ad_account_id}/campaigns

access_token={access_token}
&name=Campaign Name
&objective=CONVERSIONS
&status=PAUSED
&special_ad_categories=[]
```

### Update campaign status

```bash
POST https://graph.facebook.com/v18.0/{campaign_id}

access_token={access_token}
&status=ACTIVE
```

### Get custom audiences

```bash
GET https://graph.facebook.com/v18.0/act_{ad_account_id}/customaudiences?access_token={access_token}&fields=id,name,approximate_count
```

### Create lookalike audience

```bash
POST https://graph.facebook.com/v18.0/act_{ad_account_id}/customaudiences

access_token={access_token}
&name=Lookalike - Top Customers
&subtype=LOOKALIKE
&origin_audience_id={source_audience_id}
&lookalike_spec={"type":"similarity","country":"US"}
```

## Key Metrics

| Metric | Description |
|--------|-------------|
| `impressions` | Ad impressions |
| `clicks` | All clicks |
| `spend` | Amount spent |
| `reach` | Unique people reached |
| `frequency` | Avg impressions per person |
| `cpm` | Cost per 1000 impressions |
| `cpc` | Cost per click |
| `actions` | Conversions array |
| `cost_per_action_type` | CPA by action |

## Campaign Objectives

- `AWARENESS` - Brand awareness
- `TRAFFIC` - Website traffic
- `ENGAGEMENT` - Post engagement
- `LEADS` - Lead generation
- `APP_PROMOTION` - App installs
- `SALES` - Conversions/catalog sales

## Targeting Options

```json
{
  "geo_locations": {
    "countries": ["US"],
    "cities": [{"key": "2420379"}]
  },
  "age_min": 25,
  "age_max": 45,
  "genders": [1, 2],
  "interests": [{"id": "6003139266461", "name": "Marketing"}],
  "behaviors": [{"id": "6002714895372"}]
}
```

## When to Use

- Creating/managing Facebook and Instagram ads
- Audience targeting and lookalikes
- Campaign performance analysis
- Retargeting setup

## Rate Limits

- 200 calls/hour per ad account
- 60 calls/hour for marketing API
- Use batch requests for efficiency

## Relevant Skills

- ads
- analytics
- cro
