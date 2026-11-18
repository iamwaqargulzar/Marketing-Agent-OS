# WhatsApp Business Messaging

Use for channel selection, lifecycle flows, templates, and click-to-WhatsApp journeys. Distinguish the consumer app, Business app, and Business Platform/API; their capabilities and fees are not interchangeable.

## Plan from actual eligibility

- Establish the audience's location, relevant opt-in evidence, business identity, message purpose, and available provider. Do not infer marketing consent from a phone number, a past purchase, or an unrelated channel's permission.
- Verify the current customer-service window and the last customer message timestamp. Free-form replies and approved templates have different eligibility rules; an open service window does not mean every message is free.
- Distinguish marketing, utility, and authentication templates using current Meta definitions. Mixed promotional/transactional copy may be classified as marketing. Draft first; template creation/approval and sending are separate operations.
- Check market restrictions, template status, account quality, business-level messaging limits, opt-out suppression, and channel availability. Do not promise delivery from a successful API request alone.
- Model fees using the current recipient market, message category, delivery/billing basis, currency, volume tier, service-window rules, provider markup, and taxes. Verify effective dates. Do not carry forward a historical claim that all service replies or in-window utility messages are free.
- For click-to-WhatsApp journeys, verify entry-point qualification and any free-window conditions separately from ordinary service windows. An ad interaction alone is not evidence of permission for unrelated future campaigns.

## Choose the flow

Compare WhatsApp and SMS using audience adoption, supported message types, accessibility, cost, opt-in friction, and the user's actual deliverability data. Draft the trigger, segment, template/category, last-message/window test, suppression and exit rules, supported CTA, fallback, and success metric.

Collect actual delivery, failures, replies, opt-outs/blocks, qualified conversions, and cost. Separate channel-attributed conversions from incremental lift. Do not use automatic retries that bypass an opt-out or resend after an ambiguous receipt.

## Current documentation

Verify these sources at execution time and record the check date:

- [Meta pricing and rate cards](https://business.whatsapp.com/products/platform-pricing)
- [Meta Business Messaging documentation](https://developers.facebook.com/documentation/business-messaging/whatsapp/)
- The user's connected provider's first-party eligibility, billing, and delivery documentation.

If an authoritative rate card cannot be accessed, mark the budget unverified and state which rate is missing. Do not substitute an upstream skill or a third-party article for current pricing evidence.
