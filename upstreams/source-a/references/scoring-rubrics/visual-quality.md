# Visual Quality Rubric (0-100)

Advisory check for charts, data visualizations, infographics, diagrams, and slide graphics inside content. Used by `content-quality-auditor` as a flag, not a veto — a low score never blocks publish on its own, but it should be reported alongside CORE-EEAT findings. Score four dimensions at ~25 points each from the rendered image, exported file, or pasted asset the user provides.

## Dimensions

| Dimension | Points | What to check |
|-----------|--------|---------------|
| Data accuracy & integrity | 0-25 | Numbers match the cited source; axes labeled with units; scale not misleading (no truncated y-axis, no cherry-picked window); source named on or near the chart |
| Visual clarity | 0-25 | Main point readable in ~5 seconds; labels legible at the size it will display; color set works for colorblind viewers; no chart junk (3D, heavy gridlines, decoration) |
| Insight delivery | 0-25 | Shows a point, not just data; the "so what" is obvious without the caption; an annotation marks the key takeaway; title states the finding, not the topic |
| Design & polish | 0-25 | Consistent type and color palette; aligned and evenly spaced; styling matches the brand; still readable as a thumbnail or on mobile if it ships there |

## Scoring bands

| Band | Range | Read |
|------|-------|------|
| Ship | 80-100 | Accurate, clear, makes a point. No changes needed |
| Minor fixes | 60-79 | Sound data, but clarity or polish gaps. Annotate or relabel |
| Rework | 40-59 | Point is buried or styling is off. Redo before publish |
| Hold | 0-39 | Misleading scale, wrong numbers, or unreadable. Do not ship |

## Title test

A topic title names the subject; an insight title states the finding. Prefer the second.

- Weak: "Revenue by quarter"
- Strong: "Revenue doubled in Q3"

If the chart needs a paragraph to explain what it shows, the chart is doing the work the title should do.

## Integrity red flags (call these out explicitly)

- Y-axis starts above zero on a bar chart, inflating differences
- Time window trimmed to the stretch that supports the claim
- Dual axes scaled to imply correlation that the raw numbers do not show
- Percentages with no base count, or a pie chart that sums past 100%
- No source on a chart that makes a factual claim

## How to run it (Tier-1, keyless)

- Score from what the user gives you: the image, an exported PNG/SVG/PDF, a screenshot, or the live page URL. No paid design or analytics tool is required.
- Cross-check the plotted numbers against the user's own source — the spreadsheet, dashboard export, or the cited public page — rather than trusting the chart at face value.
- For accessibility, eyeball the palette for red/green-only contrasts and check label size against the stated display context. A formal contrast audit needs a separate tool and is out of scope here; flag it as a suggestion, not a score input.

## Honesty note

A clean chart helps readers and reviewers, but visual polish has no proven direct ranking effect — search and AI-answer systems read the surrounding text, alt text, and table data, not the pixels. Treat this rubric as a credibility and clarity check for human readers, and make sure any data shown also exists as text or a table so it is machine-readable.

## Handoff

Report as `Visual: <0-100> (D:<n> C:<n> I:<n> P:<n>)` with the top one or two fixes. Pairs with the publish-readiness output of [content-quality-auditor](../auditor-runbook.md).
