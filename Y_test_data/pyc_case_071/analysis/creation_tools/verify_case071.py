"""Verify exact official parameter IDs, native empty-container behavior and artifacts."""
import ast
import datetime
import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
root=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_071')
read=lambda p:p.read_text(encoding='utf-8')
records=list(root.rglob('*.json'))+list(root.rglob('*.jsonl'))
for p in records:
    for value in [read(p)] if p.suffix=='.json' else read(p).splitlines():
        if value.strip():json.loads(value)
for p in (root/'evaluator').glob('*.py'):ast.parse(read(p))
spec=json.loads(read(root/'analysis/creation_tools/case071_spec.json'))
meta=json.loads(read(root/'official_swebench/metadata.json'))
assert meta['product_files']==['lib/ultrajsonenc.c'] and meta['test_files']==['tests/test_ujson.py']
assert meta['product_patch_languages']==['C'] and len(meta['FAIL_TO_PASS'])==len(meta['PASS_TO_PASS'])==4
assert spec['version']=='4.0.2.dev3' and spec['pytestIdsContainSpaces'] is True
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root/'analysis/source_material/single_pyc_case_071.xlsx') as book:
    assert [n.attrib['name'] for n in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns)]==['Source Record','SWE-bench Record']
    sheet=ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for cell,date in [('B6',datetime.date(2020,11,10)),('B9',datetime.date(2020,11,15))]:
        c=sheet.find('.//s:c[@r="'+cell+'"]',ns)
        assert c.attrib.get('t') not in ('s','inlineStr')
        assert float(c.find('s:v',ns).text)==(date-datetime.date(1899,12,30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t')!='e' for c in ET.fromstring(book.read(name)).findall('.//s:c',ns))
assert 'matched 0 entries' in json.loads(read(root/'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson']
api=json.loads(read(root/'analysis/source_material/upstream_pr_api.json'))
assert api['merge_commit_sha']==spec['fixCommit']
assert api['created_at']=='2020-11-10T10:54:18Z' and api['merged_at']=='2020-11-15T17:15:24Z'
assert spec['provenance']['source_commit_utc_timestamp']=='2020-11-15T17:15:23Z'
collected=read(root/'verification/probes/collect/stdout.raw.log').splitlines()
collected=[n for n in collected if n.startswith('tests/test_ujson.py::')]
assert collected==spec['probeNodes'] and len(collected)==8 and len(set(collected))==8
assert len(spec['provenance']['official_parameter_nodes'])==5
assert any(' ' in n for n in collected) and any('\\n' in n for n in collected)
sys.dont_write_bytecode=True
sys.path.insert(0,str(root/'evaluator'))
import evaluate_model_patch as evaluator
for label in ['gold','negative']:
    log=read(root/('verification/runs/case-071-final-'+label+'/tests.raw.log'))
    expected={n:('FAILED' if label=='negative' and n in spec['failToPass'] else 'PASSED') for n in collected}
    assert evaluator.parse_test_log(log)==expected
    assert 'collected 8 items' in log
    assert ('8 passed' if label=='gold' else '4 failed, 4 passed') in log
    summary=json.loads(read(root/('verification/runs/case-071-final-'+label+'/summary.json')))
    assert summary['grading']['tests_observed']==8
audits=[json.loads(read(root/('verification/'+p+'/summary.json'))) for p in ['runtime-audit','prototype-runtime-audit']]
assert all(x['exitCode']==0 and x['runtime_audit']['ujson_version']=='4.0.2.dev3' for x in audits)
assert audits[0]['runtime_audit']==audits[1]['runtime_audit']
for a in audits:
    r=a['runtime_audit']
    assert r['ujson_file'].startswith('/testbed/ujson.') and r['scm_version']==r['ujson_version']
    assert r['base_empty_dict_output']=='{\n\n}' and r['base_empty_list_output']=='[\n\n]'
    assert a['source_git_identity']['base_distance']==3
    assert a['source_git_identity']['scm_tag']=='0b5b6358893a4b593c2f977f67f1f7cce0dce0ec'
assert 'nonempty parameter' in json.loads(read(root/'analysis/environment_spec.json'))['notes'][2]
hash_bytes=(root/'official_swebench/SHA256SUMS.txt').read_bytes()
assert b'\\n' not in hash_bytes and b'\r' not in hash_bytes
lines=hash_bytes.decode('utf-8').splitlines()
assert len(lines)==len(set(lines))
for line in lines:
    expected,name=line.split('  ',1)
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected
print('Parsed {} JSON/JSONL and {} unique hashes; exact8 IDs incl spaces/escapes, four F2P/four P2P, SCM4.0.2.dev3/native/source and saved XLSX dates verified.'.format(len(records),len(lines)))
