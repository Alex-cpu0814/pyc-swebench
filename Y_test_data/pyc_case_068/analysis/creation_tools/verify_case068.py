"""Verify persisted Case068 source identity, legacy tester scoring and workbook."""
import ast
import datetime
import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
root=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_068')
read=lambda p:p.read_text(encoding='utf-8')
records=list(root.rglob('*.json'))+list(root.rglob('*.jsonl'))
for p in records:
    for value in [read(p)] if p.suffix=='.json' else read(p).splitlines():
        if value.strip():json.loads(value)
for p in (root/'evaluator').glob('*.py'):ast.parse(read(p))
spec=json.loads(read(root/'analysis/creation_tools/case068_spec.json'))
meta=json.loads(read(root/'official_swebench/metadata.json'))
assert meta['product_files']==['CHANGES.rst','PIL/Image.py']
assert meta['product_patch_languages']==['Python'] and meta['native_product_files_changed']==[]
assert len(meta['FAIL_TO_PASS'])==5 and len(meta['PASS_TO_PASS'])==3
assert meta['source_classification'].startswith('Python-C')
assert meta['validation_type']=='official_legacy_tester'
assert 'no native crash' in spec['verifiedError']
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root/'analysis/source_material/single_pyc_case_068.xlsx') as book:
    assert [n.attrib['name'] for n in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns)]==['Source Record','SWE-bench Record']
    sheet=ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for cell,date in [('B6',datetime.date(2014,3,26)),('B9',datetime.date(2014,4,1))]:
        c=sheet.find('.//s:c[@r="'+cell+'"]',ns)
        assert c.attrib.get('t') not in ('s','inlineStr')
        assert float(c.find('s:v',ns).text)==(date-datetime.date(1899,12,30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t')!='e' for c in ET.fromstring(book.read(name)).findall('.//s:c',ns))
values=json.loads(read(root/'analysis/source_material/workbook_value_checks.json'))
assert 'matched 0 entries' in values['errorScanNdjson']
source_values=values['checks'][0]['ndjson']
assert all(x in source_values for x in ['PR merge identity limitation','fa165c8d','HTTP 422','162.9834'])
api=json.loads(read(root/'analysis/source_material/upstream_pr_api.json'))
commits=json.loads(read(root/'analysis/source_material/upstream_commit_api.json'))
assert api['merge_commit_sha']!=spec['fixCommit']
assert commits[0]['sha']==spec['fixCommit'] and commits[0]['parents'][0]==spec['baseCommit']
assert commits[0]['committer']['date']==api['merged_at'] and '#574' in commits[0]['message']
assert commits[1]['requested_sha']==api['merge_commit_sha'] and '422' in commits[1]['error']
sys.dont_write_bytecode=True
sys.path.insert(0,str(root/'evaluator'))
import evaluate_model_patch as evaluator
for label in ['gold','negative']:
    log=read(root/('verification/runs/case-068-final-'+label+'/tests.raw.log'))
    expected={n:('FAILED' if label=='negative' and n in spec['failToPass'] else 'PASSED') for n in spec['probeNodes']}
    assert evaluator.parse_test_log(log)==expected
    counts=[json.loads(x.split(' ',1)[1]) for x in log.splitlines() if x.startswith('OFFICIAL_TESTER_COUNTS ')]
    results=[json.loads(x.split(' ',1)[1]) for x in log.splitlines() if x.startswith('ISOLATED_NODE_RESULT ')]
    assert len(counts)==len(results)==8 and len({x['node'] for x in counts})==8
    for x in counts:
        if expected[x['node']]=='PASSED':assert x['assertions_passed']>0 and x['assertions_failed']==0
        else:assert x['assertions_failed']>0
    assert all(x['signal'] is None for x in results)
    assert all(x['returncode']==(1 if expected[x['node']]=='FAILED' else 0) for x in results)
audits=[json.loads(read(root/('verification/'+p+'/summary.json'))) for p in ['runtime-audit','prototype-runtime-audit']]
assert all(x['exitCode']==0 and x['runtime_audit']['pillow_version']=='2.3.0' for x in audits)
assert audits[0]['runtime_audit']['assets']==audits[1]['runtime_audit']['assets']
assert audits[0]['native_package_versions']==audits[1]['native_package_versions']
assets=audits[0]['runtime_audit']['assets']
assert assets['Images/lena.ppm']=={'size':49167,'sha256':'f258b4c65bd13ebff4df782016bac39d6775e0ce5eb5a13118ac541a56f10293'}
assert assets['Images/lena.jpg']=={'size':4788,'sha256':'54e97bc5e2a8744022f3c57c08d2a36566067866d9cabfbdde131e99a485134a'}
lines=read(root/'official_swebench/SHA256SUMS.txt').splitlines()
assert len(lines)==len(set(lines))
for line in lines:
    expected,name=line.split('  ',1)
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected
print('Parsed {} JSON/JSONL, {} unique hashes, official tester counters and node statuses, clean runtime/assets, numeric XLSX dates and merge-identity limitation verified.'.format(len(records),len(lines)))
