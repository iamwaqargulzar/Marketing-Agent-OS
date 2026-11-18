# Video Production Workflows

Use when a product demo must be repeatable or an HTML/code composition needs rendering. Prefer a short human recording for a one-off walkthrough when it meets the request.

## Repeatable product demos

1. Define the audience, feature flow, scene list, viewport/aspect ratio, captions, and output. Narration is optional; use the user's connected tool or installed stack.
2. Record a user-authorized local/staging build with a disposable or approved test account. Verify the page actually renders and session state survives navigation. Do not inherit production database credentials into seed/reset commands.
3. Use stable accessible locators and state-based waits. Capture a diagnostic image on a failed step. Keep captions/cursor overlays clear of the active controls; do not silently bypass security controls on a live system for recording convenience.
4. Associate each scene with action and caption/audio timings. For navigation, finish describing the old scene before leaving it; in-place actions may run during narration. Measure actual audio durations when available.
5. Export video and a timing sidecar when useful. Verify the beginning/end, all interactions, readable captions, audio alignment, aspect ratio, and private-data redaction. Keep recording-only overrides out of product commits.
6. Reset only the explicitly scoped test data. Preserve the user's files and require authorization for account writes, paid narration, deployment, and publication.

## Programmatic compositions

Verify the installed framework's version and official examples. Do not invent a render function from its package name. Hyperframes' official CLI documentation currently describes `npx hyperframes render --output output.mp4`; its HTML composition and programmatic producer interface need their own current documentation. Keep CLI commands distinct from SDK imports.

For deterministic rerenders, pin the chosen dependencies and assets and record the viewport, timing, fonts, and renderer version. Inspect the actual export; identical input alone does not establish identical output across operating systems, browser/font versions, or hardware.

For generated footage, confirm current provider/model availability, cost, rights, and capabilities before choosing it. Upstream model lists and prices may be stale. Use runtime-managed credentials; do not place secrets in captions, source files, chat, or rendered artifacts.

First-party reference: [Hyperframes CLI](https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx). Recheck it for the selected version before running examples.
