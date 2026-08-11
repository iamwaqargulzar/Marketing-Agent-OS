#!/usr/bin/env python3
"""Heuristic GEO citability scorer. Diagnostic, not a ranking predictor."""
import argparse, json, re
from pathlib import Path

def score(text):
 words=re.findall(r"\b\w+[\w'-]*\b",text); sentences=[s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()]
 metrics={
  'word_count':len(words),'sentence_count':len(sentences),
  'avg_sentence_words': round(len(words)/max(1,len(sentences)),1),
  'headings':len(re.findall(r'^#{1,6}\s+',text,re.M)),
  'lists':len(re.findall(r'^\s*[-*+]\s+',text,re.M)),
  'numeric_facts':len(re.findall(r'\b\d+(?:\.\d+)?%?\b',text)),
  'source_markers':len(re.findall(r'\b(source|according to|study|report|data|research|survey|documentation)\b',text,re.I)),
  'entity_markers':len(re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b',text)),
 }
 s=0
 s += min(20,metrics['headings']*4); s += min(15,metrics['lists']*2); s += min(20,metrics['numeric_facts']*2); s += min(20,metrics['source_markers']*4); s += min(15,metrics['entity_markers']*2)
 avg=metrics['avg_sentence_words']; s += 10 if 8<=avg<=24 else 5 if avg<=32 else 0
 return {'score':min(100,s),'metrics':metrics,'note':'Heuristic content-structure/citability diagnostic; not evidence of AI ranking or citation.'}
def main():
 p=argparse.ArgumentParser(); p.add_argument('file',nargs='?'); a=p.parse_args(); text=Path(a.file).read_text(errors='replace') if a.file else __import__('sys').stdin.read(); print(json.dumps(score(text),indent=2))
if __name__=='__main__': main()
