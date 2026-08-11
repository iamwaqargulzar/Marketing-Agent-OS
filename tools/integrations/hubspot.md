# Hubspot Integration

Use this integration only when configured and relevant. Keep credentials out of prompts and files. Prefer read-only requests during diagnosis. Record timestamps, request scope, units and source limitations. For any mutation, spend, send, publish, delete or account change, obtain explicit authorization.

## Suggested capability mapping

- Discovery/read: evidence collection for relevant marketing skills
- Mutation/write: disabled by default; host permission + user authorization required
- Failure behavior: degrade gracefully to manual/user-provided evidence; never fabricate results
