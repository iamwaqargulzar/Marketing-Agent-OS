#!/usr/bin/env python3
"""Generate a conservative llms.txt draft from explicit site metadata."""
import argparse
p=argparse.ArgumentParser(); p.add_argument('--name',required=True); p.add_argument('--url',required=True); p.add_argument('--description',required=True); p.add_argument('--docs',action='append',default=[]); p.add_argument('--output'); a=p.parse_args()
lines=[f'# {a.name}','',f'> {a.description}','',f'- Website: {a.url}']
if a.docs:
 lines+=['','## Key resources']+[f'- {x}' for x in a.docs]
lines+=['','<!-- llms.txt is an interoperability aid. It does not replace robots.txt, sitemaps, indexable content, or platform-specific eligibility requirements. -->','']
text='\n'.join(lines)
if a.output: open(a.output,'w').write(text)
else: print(text)
