#!/usr/bin/env python3
"""Optional PDF renderer. Uses reportlab if installed; otherwise emits an actionable error."""
import argparse
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('markdown'); p.add_argument('output'); a=p.parse_args()
try:
 from reportlab.lib.pagesizes import A4
 from reportlab.pdfgen import canvas
except Exception:
 raise SystemExit('PDF support is optional. Install reportlab (`python3 -m pip install reportlab`) or use generate_markdown_report.py.')
text=Path(a.markdown).read_text(errors='replace'); c=canvas.Canvas(a.output,pagesize=A4); w,h=A4; y=h-50
for raw in text.splitlines():
 line=raw.replace('#','').strip()
 if not line: y-=10; continue
 for start in range(0,len(line),95):
  c.drawString(50,y,line[start:start+95]); y-=14
  if y<50: c.showPage(); y=h-50
c.save(); print(a.output)
