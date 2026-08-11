# Entity to GEO Handoff Contract

This contract connects `entity-registry` to entity-aware content/schema builders. Canonical history is `memory/events/entities.ndjson`; current accepted records are in `memory/projections/entities.json`. Files under `memory/entities/` are optional generated views.

## Accepted Entity Data

```json
{
  "aggregate_id": "entity-acme-analytics",
  "revision": 4,
  "status": "active",
  "data": {
    "entity_type": "organization",
    "display_name": "Acme Analytics",
    "primary_domain": "acme.example",
    "aliases": ["Acme Analytics Inc"],
    "same_as": ["https://www.wikidata.org/wiki/Q123"],
    "wikidata_qid": "Q123",
    "schema_type": "Organization",
    "recognition_observations": [
      {
        "system": "wikidata",
        "state": "recognized",
        "source_ref": "kg-query-2026-07-10",
        "observed_at": "2026-07-10",
        "evidence_type": "measured"
      }
    ],
    "narrative_canon_id": "brand-acme",
    "narrative_canon_version": "3",
    "claims_projection_offset": 42
  }
}
```

## Required Fields

| Field | Required | Consumer behavior |
|---|---|---|
| aggregate ID/revision/status | yes | Trace source state and reject erased/tombstoned records |
| `entity_type` | yes | Select schema/entity behavior |
| `display_name` | yes | Canonical first mention |
| `primary_domain` | yes for organizations/products | First-party identity pointer |
| `aliases` | recommended | Disambiguation coverage |
| `same_as` | recommended | Verified identity links; never guessed |
| `schema_type` | recommended | JSON-LD type selection |
| recognition observations | yes | Per-system state/source/date; Unknown when unobserved |
| Narrative/claims tuple | required for descriptions | Prevent machine identity from inventing brand copy/claims |

## Producer Rules

1. `entity-registry` alone accepts/rejects/upserts entity state through `registry-events.py`.
2. Ordinary skills submit authorized `operation: propose` events with idempotency/source/date/current revision.
3. Natural-person records use pseudonymous aggregate IDs and minimum necessary professional facts. Keep direct contact PII out of events/views.
4. Never merge identities on name/logo similarity alone.
5. Recognition observations are per system/date. Unobserved is Unknown, not Partial/Fail.
6. Description text derives from accepted Narrative/claims state and carries the dependency tuple; entity state cannot redefine L1 canon.

## Consumer Rules

Before entity-aware content or schema generation:

1. Query the projection by aggregate ID and record revision/offset.
2. Reject erased/tombstoned records and surface stale/conflicting identity evidence.
3. Populate schema only from accepted fields; ask for missing required values rather than guessing.
4. For external copy, independently verify the Narrative/claims dependency tuple. A stale/missing tuple sets `dependency_status: blocked` or an explicitly authorized exploratory fallback.
5. Route durable corrections as proposals to `entity-registry`; do not edit JSON or Markdown views.

## Versioning

Contract version **2.0 (v17)**. New optional fields are backward-compatible. Field removal/type changes or authority changes require a major contract version plus migration and behavior tests.
