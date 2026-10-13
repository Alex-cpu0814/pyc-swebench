"""Verify persisted native indent/SCM/source evidence and saved two-sheet workbook."""
import ast
import datetime
import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
root=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_070')
read=lambda p:p.read_text(encoding='utf-8')
records=list(root.rglob('*.json'))+list(root.rglob('*.jsonl'))
for p in records:
    for value in [read(p)] if p.suffix=='.json' else read(p).splitlines():
        if value.strip():json.loads(value)
for p in (root/'evaluator').glob('*.py'):ast.parse(read(p))
spec=json.loads(read(root/'analysis/creation_tools/case070_spec.json'))
meta=json.loads(read(root/'official_swebench/metadata.json'))
assert meta['product_files']==['python/objToJSON.c'] and meta['test_files']==['tests/test_ujson.py']
assert meta['product_patch_languages']==['C'] and meta['native_product_files_changed']==['python/objToJSON.c']
assert len(meta['FAIL_TO_PASS'])==1 and len(meta['PASS_TO_PASS'])==3
assert meta['validation_type']=='official_pytest' and spec['version']=='3.2.1.dev2'
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root/'analysis/source_material/single_pyc_case_070.xlsx') as book:
    assert [n.attrib['name'] for n in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns)]==['Source Record','SWE-bench Record']
    sheet=ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for cell,date in [('B6',datetime.date(2020,9,17)),('B9',datetime.date(2020,9,19))]:
        c=sheet.find('.//s:c[@r="'+cell+'"]',ns)
        assert c.attrib.get('t') not in ('s','inlineStr')
        assert float(c.find('s:v',ns).text)==(date-datetime.date(1899,12,30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t')!='e' for c in ET.fromstring(book.read(name)).findall('.//s:c',ns))
assert 'matched 0 entries' in json.loads(read(root/'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson']
api=json.loads(read(root/'analysis/source_material/upstream_pr_api.json'))
assert api['merge_commit_sha']==spec['fixCommit']
assert api['created_at']=='2020-09-17T14:47:08Z' and api['merged_at']=='2020-09-19T19:00:23Z'
assert spec['provenance']['source_commit_utc_timestamp']=='2020-09-19T19:00:22Z'
scm=spec['provenance']['scm_metadata']
assert scm['tag_commit']=='090d7412cf298085bd8f41cde9bf983f3038496f' and scm['base_distance']==2
sys.dont_write_bytecode=True
sys.path.insert(0,str(root/'evaluator'))
import evaluate_model_patch as evaluator
for label in ['gold','negative']:
    log=read(root/('verification/runs/case-070-final-'+label+'/tests.raw.log'))
    expected={n:('FAILED' if label=='negative' and n in spec['failToPass'] else 'PASSED') for n in spec['probeNodes']}
    assert evaluator.parse_test_log(log)==expected
    assert 'collected 4 items' in log
    assert ('4 passed' if label=='gold' else '1 failed, 3 passed') in log
    summary=json.loads(read(root/('verification/runs/case-070-final-'+label+'/summary.json')))
    assert summary['grading']['tests_observed']==4
audits=[json.loads(read(root/('verification/'+p+'/summary.json'))) for p in ['runtime-audit','prototype-runtime-audit']]
assert all(x['exitCode']==0 and x['runtime_audit']['ujson_version']=='3.2.1.dev2' for x in audits)
assert audits[0]['runtime_audit']==audits[1]['runtime_audit']
assert audits[0]['native_package_versions']=={'gcc':'4:10.2.1-1','g++':'4:10.2.1-1'}
for a in audits:
    r=a['runtime_audit']
    assert r['ujson_file'].startswith('/testbed/ujson.') and r['scm_version']==r['ujson_version']
    assert r['base_indent4_output']=='{\n "obj": 31337\n}'
    assert r['build_packages']=={'setuptools':'68.2.2','setuptools-scm':'6.4.2','wheel':'0.42.0','pytest':'7.4.4'}
    assert a['source_git_identity']['generated_version_header_is_ignored'] is True
config=json.loads(read(root/'evaluator/case_config.json'))
assert config['runtime_assets']==[{'source':'evaluator/case_adapter.sh','target':'/benchmark/case_adapter.sh'},{'source':'evaluator/pytest_no_dump.py','target':'/benchmark/pytest_no_dump.py'}]
lines=read(root/'official_swebench/SHA256SUMS.txt').splitlines()
assert len(lines)==len(set(lines))
for line in lines:
    expected,name=line.split('  ',1)
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected
print('Parsed {} JSON/JSONL and {} unique hashes; native p/i output assertion, local SCM3.2.1.dev2, vendored source pins, raw grades and numeric workbook dates verified.'.format(len(records),len(lines)))
