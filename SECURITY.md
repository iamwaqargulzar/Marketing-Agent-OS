# Security policy

Marketing Agent OS contains instruction files and optional helper scripts that may be executed by AI coding agents with the user's local permissions. Review installed skills before use and preserve the authorization gates documented in `references/skill-contract.md`.

## Supported versions

Security fixes are applied to the latest release on the `main` branch.

| Version | Supported |
|---|---|
| 1.1.x | Yes |
| Earlier versions | No |

## Report a vulnerability

Use GitHub's private **Report a vulnerability** feature in the repository Security tab. Do not open a public issue for a suspected vulnerability, exploit, exposed credential, or unsafe agent behavior.

Include:

- the affected skill, script, installer target, or workflow;
- the operating system and agent harness;
- exact reproduction steps and impact;
- whether external network, filesystem, credential, or account access is involved;
- a minimal proof of concept when safe to share privately;
- any suggested remediation.

Please do not include real credentials, customer data, or third-party private information. A maintainer will acknowledge valid reports through GitHub and coordinate disclosure after a fix is available. No monetary bug bounty is currently offered.

## Security boundaries

- The normalized skill layer is validated; pinned upstream snapshots are retained for provenance and are not installed.
- Optional connectors may require separate credentials and inherit the security model of their provider and host harness.
- Time-sensitive platform instructions must be checked against current first-party sources.
- A skill does not grant permission to publish, send, spend, mutate accounts, or persist business data.
- Retrieved web content is untrusted evidence and must not be treated as agent instructions.
