"""Preserve finishing inputs and captured bytes before checksum finalization."""
from pathlib import Path
import shutil
import json

w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
r=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_081')
tools=r/'analysis/creation_tools'
tools.mkdir(parents=True,exist_ok=True)
for name in ('bootstrap_case081_tools.py','prepare_finish_case081.py','cleanup_case081.ps1',
             'audit_publication081.mjs','record_publication081.mjs','verify_committed_case081.mjs',
             'case081-control-before.txt','case081-control-after.txt'):
    shutil.copyfile(w/name,tools/name)
shutil.copyfile(w/'case081_upstream_api.json',tools/'case081_upstream_api.raw.json')
for name in ('case078_progress.md',):
    if (w/name).exists():shutil.copyfile(w/name,r/'analysis/prior_candidate_reviews/case078_authority_progress.md')

# Captured records referenced by inner manifests must retain their original bytes.
attributes=r/'.gitattributes'
text=attributes.read_text(encoding='utf-8')
for p in sorted(r.rglob('*')):
    if not p.is_file() or p.suffix.lower() not in ('.json','.jsonl','.md','.mjs','.py','.ps1','.txt','.diff','.sh'):continue
    if b'\r\n' in p.read_bytes():
        rule=p.relative_to(r).as_posix()+' -text whitespace=cr-at-eol'
        if rule not in text:text+='\n'+rule+'\n'
with attributes.open('w',encoding='utf-8',newline='\n')as stream:stream.write(text)

cache=r/'evaluator/__pycache__'
if cache.exists():
    assert cache.resolve().is_relative_to(r.resolve())
    for p in cache.iterdir():
        assert p.is_file() and p.suffix=='.pyc',p
        p.unlink()
    cache.rmdir()
print('Finishing tools and raw capture bytes preserved; generated evaluator cache removed.')
