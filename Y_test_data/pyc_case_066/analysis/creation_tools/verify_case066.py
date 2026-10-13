"""Independent persisted Case066 evidence checks, usable after scratch cleanup."""
import ast
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
root = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_066')
read = lambda p: p.read_text(encoding='utf-8')
records = list(root.rglob('*.json')) + list(root.rglob('*.jsonl'))
for p in records:
    for v in [read(p)] if p.suffix == '.json' else read(p).splitlines():
        if v.strip(): json.loads(v)
for p in (root/'evaluator').glob('*.py'): ast.parse(read(p))
ns = {'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root/'analysis/source_material/single_pyc_case_066.xlsx') as book:
    names=[s.attrib['name'] for s in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns)]
    assert names==['Source Record','SWE-bench Record']
    sheet=ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for address,date in [('B6',datetime.date(2017,7,18)),('B9',datetime.date(2017,9,4))]:
        c=sheet.find('.//s:c[@r="'+address+'"]',ns)
        assert c.attrib.get('t') not in ('s','inlineStr')
        assert float(c.find('s:v',ns).text)==(date-datetime.date(1899,12,30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t')!='e' for c in ET.fromstring(book.read(name)).findall('.//s:c',ns))
assert 'matched 0 entries' in json.loads(read(root/'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson']
spec=json.loads(read(root/'analysis/creation_tools/case066_spec.json'))
m=json.loads(read(root/'official_swebench/metadata.json'))
assert len(m['FAIL_TO_PASS'])==1 and len(m['PASS_TO_PASS'])==3
assert m['product_files']==['_imaging.c','_imagingft.c']
assert m['validation_type']=='official_unittest'
for label in ['gold','negative']:
    log=read(root/('verification/runs/case-066-final-'+label+'/tests.raw.log'))
    import sys
    sys.path.insert(0,str(root/'evaluator'))
    import evaluate_model_patch as evaluator
    observed=evaluator.parse_test_log(log)
    expected={n:('FAILED' if label=='negative' and n in spec['failToPass'] else 'PASSED') for n in spec['probeNodes']}
    assert observed==expected
    results=[json.loads(line.split(' ',1)[1]) for line in log.splitlines() if line.startswith('ISOLATED_NODE_RESULT ')]
    assert len(results)==4 and all(r['signal'] is None for r in results)
    assert all(r['returncode']==(1 if expected[r['node']]=='FAILED' else 0) for r in results)
    summary=json.loads(read(root/('verification/runs/case-066-final-'+label+'/summary.json')))
    assert summary['grading']['tests_observed']==4
audit=json.loads(read(root/'verification/runtime-audit/summary.json'))
assert audit['exitCode']==0 and audit['runtime_audit']['pillow_version']=='4.3.0.dev0'
assert audit['runtime_audit']['font_sha256']=='54cf7fa374a13ddf6e927b515b75b39fad79f6d2cdd2789ad5bf69f207b88c2c'
assert audit['native_package_versions']==json.loads(read(root/'verification/prototype-runtime-audit/summary.json'))['native_package_versions']
limits=spec['provenance']['official_rss_limits']
assert limits=={'truetype':{'iterations':10,'mem_limit_kib':4096},'default_font':{'iterations':100,'mem_limit_kib':1024}}
config=json.loads(read(root/'evaluator/case_config.json'))
assert config['runtime_assets']==[{'source':'evaluator/case_adapter.sh','target':'/benchmark/case_adapter.sh'},{'source':'evaluator/unittest_case066_isolated.py','target':'/benchmark/unittest_case066_isolated.py'}]
lines=read(root/'official_swebench/SHA256SUMS.txt').splitlines()
for line in lines:
    expected,name=line.split('  ',1)
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected
print('Parsed {} JSON/JSONL and {} hashes; evaluator syntax, numeric workbook dates and no Excel errors verified.'.format(len(records),len(lines)))
print('Gold four passes; negative one genuine RSS assertion plus three passes. Official thresholds and runtime assets unchanged.')
