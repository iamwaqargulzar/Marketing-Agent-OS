#!/usr/bin/env python3
"""Compute the Marketing Agent OS health score from evidence-backed category scores."""
import argparse,json
W={'technical':22,'content':23,'on_page':20,'schema':10,'performance':10,'ai_readiness':10,'images':5}
p=argparse.ArgumentParser()
for k in W: p.add_argument('--'+k.replace('_','-'),type=float)
a=p.parse_args(); vals=vars(a); missing=[k for k,v in vals.items() if v is None]
if missing: raise SystemExit('Missing category scores: '+', '.join(missing))
for k,v in vals.items():
 if not 0<=v<=100: raise SystemExit(f'{k} must be 0..100')
score=sum(vals[k]*W[k] for k in W)/100
print(json.dumps({'score':round(score,1),'weights':W,'inputs':vals,'warning':'Only use category scores backed by auditable evidence.'},indent=2))
