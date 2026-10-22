# Read-only stack exposure review

Use only within the user's owned or explicitly authorized target scope. This is ordinary-response and supplied-inventory review, not an exploitation or vulnerability-scanning mandate.

Read normal allowed responses and available authorized runtime/hosting inventory. Record the source, date, visible product/version, confidence, proxy/CDN ambiguity, and origin visibility. Do not fuzz, send attack payloads, enumerate sensitive endpoints, or bypass the bounded fetcher's network restrictions.

Headers, cookies, framework assets, and generator tags are hints. A web server name is not proof of a language/runtime version; a hidden banner, missing PHP signal, static frontend, or blocked path cannot establish that no PHP/backend exists anywhere. Mark the runtime/version unknown until supported by inventory, the hosting panel, or an authorized owner check.

For a relevant advisory, verify current vendor release notes, affected version/configuration prerequisites, fixed branch, maintained distribution backports, and mitigation status. A version-looking banner alone is not proof of exploitability; a distributor's patched package may retain a base version string. Distinguish possible exposure, confirmed affected inventory, and verified remediation.

At the October 22, 2026 review, PHP's October 21 security announcements identify CVE-2026-109618 and CVE-2026-109619. Treat that as dated advisory context, not an evergreen scanner rule or a complete affected-version map. Recheck the current branch-specific releases and hosting/distribution guidance before recommending a patch.

Return the evidence, limitations, advisory source/date, relevant patch/hosting owner, urgency supported by the advisory, and next verification. Upgrades, service shutdowns, account/host changes, and remediation require separate authority. Do not mark a stack safe merely because an external observation found no signal.

Primary sources: [PHP security releases](https://www.php.net/archive/2026.php), [PHP 8.5.12 announcement](https://news-web.php.net/php.announce/513), and [NSA's October 21 advisory](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4630238/nsa-advisory-php-updates/). Check the vendor and hosting provider for the actual deployment.
