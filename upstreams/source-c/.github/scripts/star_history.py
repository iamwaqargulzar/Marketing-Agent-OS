#!/usr/bin/env python3
"""Generate a self-hosted star-history chart for the README.

Fetches stargazer timestamps from the GitHub API (works with the built-in
Actions GITHUB_TOKEN — no PAT needed) and renders assets/star-history.svg
plus a dark-mode variant. Run by .github/workflows/star-history.yml daily.

Usage: GITHUB_TOKEN=<token> python3 .github/scripts/star_history.py
"""

import datetime as dt
import json
import os
import sys
import urllib.request

REPO = os.environ.get("STAR_REPO", "zubair-trabzada/geo-seo-claude")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
PER_PAGE = 100
MAX_POINTS = 240  # sampled points in the rendered path


def fetch_page(page):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/stargazers?per_page={PER_PAGE}&page={page}",
        headers={
            "Accept": "application/vnd.github.star+json",
            "Authorization": f"Bearer {TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "star-history-generator",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_star_dates():
    dates, page = [], 1
    while True:
        batch = fetch_page(page)
        if not batch:
            break
        dates.extend(
            dt.datetime.fromisoformat(s["starred_at"].replace("Z", "+00:00"))
            for s in batch
            if s.get("starred_at")
        )
        if len(batch) < PER_PAGE:
            break
        page += 1
    return sorted(dates)


def sample(points, limit):
    if len(points) <= limit:
        return points
    step = (len(points) - 1) / (limit - 1)
    return [points[round(i * step)] for i in range(limit)]


def render_svg(dates, fg, grid, accent, fill_opacity):
    w, h = 800, 420
    ml, mr, mt, mb = 70, 30, 50, 60
    pw, ph = w - ml - mr, h - mt - mb

    total = len(dates)
    t0, t1 = dates[0], dates[-1]
    span = max((t1 - t0).total_seconds(), 1)

    pts = [(i + 1, d) for i, d in enumerate(dates)]
    pts = sample(pts, MAX_POINTS)
    xy = [
        (ml + pw * (d - t0).total_seconds() / span, mt + ph * (1 - count / total))
        for count, d in pts
    ]
    path = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in xy)
    area = path + f" L{xy[-1][0]:.1f},{mt + ph} L{xy[0][0]:.1f},{mt + ph} Z"

    y_ticks = 5
    y_labels = []
    for i in range(y_ticks + 1):
        val = round(total * i / y_ticks)
        y = mt + ph * (1 - i / y_ticks)
        y_labels.append(
            f'<line x1="{ml}" y1="{y:.1f}" x2="{ml + pw}" y2="{y:.1f}" stroke="{grid}" stroke-width="1"/>'
            f'<text x="{ml - 10}" y="{y + 4:.1f}" text-anchor="end" font-size="12" fill="{fg}" opacity="0.7">{val:,}</text>'
        )

    x_labels = []
    for i in range(5):
        d = t0 + (t1 - t0) * i / 4
        x = ml + pw * i / 4
        anchor = "start" if i == 0 else "end" if i == 4 else "middle"
        x_labels.append(
            f'<text x="{x:.1f}" y="{mt + ph + 24}" text-anchor="{anchor}" font-size="12" fill="{fg}" opacity="0.7">{d.strftime("%b %d, %Y")}</text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">
  <text x="{ml}" y="30" font-size="18" font-weight="600" fill="{fg}">Star History — {REPO}</text>
  <text x="{ml + pw}" y="30" text-anchor="end" font-size="14" fill="{accent}" font-weight="600">★ {total:,}</text>
  {''.join(y_labels)}
  <path d="{area}" fill="{accent}" opacity="{fill_opacity}"/>
  <path d="{path}" fill="none" stroke="{accent}" stroke-width="2.5" stroke-linejoin="round"/>
  {''.join(x_labels)}
  <text x="{w / 2}" y="{h - 8}" text-anchor="middle" font-size="11" fill="{fg}" opacity="0.5">Updated {dt.date.today().isoformat()} · generated in-repo, no external service</text>
</svg>
"""


def main():
    if not TOKEN:
        sys.exit("GITHUB_TOKEN is not set")
    dates = fetch_star_dates()
    if not dates:
        sys.exit("No stargazer data returned")
    os.makedirs(OUT_DIR, exist_ok=True)
    variants = {
        "star-history.svg": ("#24292f", "#d0d7de", "#e3a008", "0.12"),
        "star-history-dark.svg": ("#e6edf3", "#30363d", "#e3b341", "0.15"),
    }
    for name, (fg, grid, accent, op) in variants.items():
        with open(os.path.join(OUT_DIR, name), "w") as f:
            f.write(render_svg(dates, fg, grid, accent, op))
    print(f"Rendered {len(variants)} SVGs from {len(dates):,} stars")


if __name__ == "__main__":
    main()
