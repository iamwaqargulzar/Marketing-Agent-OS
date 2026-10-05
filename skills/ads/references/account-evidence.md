# Paid Account Evidence

Use before classifying spend as waste or recommending changes to a live account. Record the account, currency, timezone, report date/window, filters, and data freshness.

## Reconcile what the report measures

- Compare disclosed search-term clicks with campaign clicks for the same scope and window. Missing queries are unavailable data; do not infer their text from analytics or CRM activity. Report the coverage ratio without treating it as total waste.
- Check actual keywords, match types, destinations, and serving/experiment status. Campaign names are labels, not proof of intent, duplicate serving, or landing-page exposure.
- Segment conversions by action and inspect campaign goals. Verify what counts in conversions versus all-conversions, primary/secondary actions, attribution model, and reporting date basis. A page-view proxy is not a qualified lead.
- Check conversion lag, recent versus longer-term performance, and configuration changes. Avoid pooling materially different settings into one experiment. Learning-phase uncertainty does not prevent fixing verified tracking or destination breakage.
- Recheck current API support, reporting fields, pagination, limits, and change-history retention. A missing historical edit is not evidence that nobody changed the account; client type does not identify a person's motive.
- Open the actual serving landing pages when conclusions depend on them. Static HTML cannot establish whether a JavaScript widget or embedded calendar is absent.

## Interpret small samples

Expose click and conversion counts, not only rates. Under an independent binomial model, zero conversions in N clicks gives a one-sided 95% upper CVR bound of `1 - 0.05 ** (1 / N)` for N greater than zero. This is a model-dependent bound; attribution gaps, lag, and unequal click quality can invalidate its assumptions.

Compare observed evidence with the CVR required by the chosen CPA target: `CPC / target CPA`, with positive inputs and matching currency/units. A target CPA is a business constraint, not automatically a profit break-even point. Use margin/customer value when estimating actual break-even economics.

Do not prescribe a fixed kill threshold from a few clicks. Give a measurable next decision point, expected sample/lag, and an estimated time to reach it, or explain that volume is too low for the proposed test.

## Keep demand and incrementality separate

Split branded and non-branded search before interpreting efficiency. Report blended business economics alongside acquisition-segment results. Cheap branded conversions do not prove incremental lift; use a suitable holdout or other causal evidence for that claim. Select bidding/budget recommendations against the user's actual objective and unit economics rather than imposing a universal non-brand ROAS target.

Never add conversion credits across incompatible windows or platforms as though they were unique sales. Reconcile against order/CRM truth where available and distinguish observed, calculated, estimated, and stale evidence. Draft changes with their scope and expected downside; execute only under the granted authorization and record receipts.
