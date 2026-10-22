# Conversion delivery verification

Use authorized fixtures and the actual installed form/booking/store version. Agree what records may be created, whether an event can enter production reporting/bidding, who will reconcile it, and when observation is complete. Never silently purchase, book, or contact someone to test tracking.

Test the same outcome through four boundaries:

1. **Business truth:** the intended action was accepted/confirmed, with a stable record ID and correct time/value/currency. Validation failures and abandoned attempts must not count as the successful outcome.
2. **Detection:** the documented success event fires once for that record. Exercise invalid submit, repeated callback, refresh/direct thank-you visit, and retry. A local event proves only local detection.
3. **Delivery:** the actual request uses correct destination/property, event mapping, permitted identifiers, consent state, and replay-safe deduplication key. A debug preview or HTTP success alone does not prove final destination acceptance.
4. **Receipt:** inspect the destination's supported debug/test/diagnostic or received-event surface using the same IDs and timestamp. Allow the documented processing/attribution delay. Check duplicate browser/server paths and compare with the deduplicated business ledger.

Also test denied/withdrawn consent, blocked browser tags, absent click IDs, wrong account IDs, iframe-origin mismatch, backend failure, delayed callbacks, and duplicate webhook delivery when those paths exist. A detector must not prevent the actual form/checkout from completing if optional tracking fails.

Keep raw personal data out of test logs and screenshots. Query parameters and generic event payloads are not a secret store. Use destination-approved user-data fields only with the required permission and consent. Provider-specific hashing/normalization belongs at the documented boundary, not in every analytics event.

Report separately: confirmed business outcome, local detection, send attempt, received event, matched conversion, attributed credit, and bid eligibility. Mark missing account access, unavailable safe test, unsupported linkage, or an incomplete processing window as unverified. Reconcile production test artifacts only within the approved scope; never assume that every platform supports deletion or conversion retraction.
