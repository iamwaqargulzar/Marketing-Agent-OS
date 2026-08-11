#!/usr/bin/env python3
"""Scan a local text/HTML corpus for brand/entity mentions and context snippets."""
import argparse,re,json
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('brand'); p.add_argument('files',nargs='+'); p.add_argument('--window',type=int,default=100); a=p.parse_args(); out=[]
for fn in a.files:
 t=Path(fn).read_text(errors='replace');
 for m in re.finditer(re.escape(a.brand),t,re.I): out.append({'file':fn,'offset':m.start(),'snippet':re.sub(r'\s+',' ',t[max(0,m.start()-a.window):m.end()+a.window]).strip()})
print(json.dumps({'brand':a.brand,'mentions':len(out),'matches':out},indent=2,ensure_ascii=False))
