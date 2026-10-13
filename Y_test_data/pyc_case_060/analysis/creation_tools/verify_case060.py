"""Independent Case 060 native process, runtime and artifact verification."""
import ast
import datetime
import hashlib
import json
from pathlib import Path
import re
import importlib.util
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile
root = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_060')
work = Path('E:/CLB_Swe-bench/_work/pyc_batch')
read = lambda p: p.read_text(encoding='utf-8')
records = list(root.rglob('*.json')) + list(root.rglob('*.jsonl'))
for p in records:
    for v in [read(p)] if p.suffix == '.json' else read(p).splitlines():
        if v.strip():
            json.loads(v)
for p in (root / 'evaluator').glob('*.py'):
    ast.parse(read(p))
ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root / 'analysis/source_material/single_pyc_case_060.xlsx') as book:
    names = [s.attrib['name'] for s in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet', ns)]
    assert names == ['Source Record', 'SWE-bench Record']
    sheet = ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for address, date in [('B6', datetime.date(2021, 2, 19)), ('B9', datetime.date(2021, 3, 28))]:
        c = sheet.find('.//s:c[@r="' + address + '"]', ns)
        assert c.attrib.get('t') not in ('s', 'inlineStr')
        assert float(c.find('s:v', ns).text) == (date - datetime.date(1899, 12, 30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t') != 'e' for c in ET.fromstring(book.read(name)).findall('.//s:c', ns))
assert 'matched 0 entries' in json.loads(read(root / 'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson']
source = json.loads(read(root / 'analysis/source_row_060.json'))
assert source['symptom'] == 'segment fault (crash).'
assert 'ImagingTransform' in source['bug_path'] and '__transformer' in source['bug_path']
assert 'SIGSEGV' in source['trace']['verified_error'] and 'I-mode' in source['trace']['verified_error']
m = json.loads(read(root / 'official_swebench/metadata.json'))
assert m['created_at'] == '2021-02-19' and m['merged_at'] == '2021-03-28'
assert m['product_files'] == m['native_product_files_changed'] == ['src/libImaging/Fill.c']
assert m['product_patch_languages'] == ['C'] and m['test_files'] == ['Tests/test_image.py']
assert m['source_classification'].startswith('Python-C')
audits = [json.loads(read(root / p / 'summary.json')) for p in ['verification/runtime-audit', 'verification/prototype-runtime-audit']]
for a in audits:
    assert a['exitCode'] == 0 and a['error'] is None
    f = a['runtime_audit']
    assert f['pillow_version'] == f['core_version'] == '8.2.0.dev0'
    assert f['pillow_file'].startswith('/testbed/src/PIL/') and f['core_file'].startswith('/testbed/src/PIL/')
    assert f['fill_source_sha256'] == 'bffdcd9ecb03814015ac37b977986b00cc2dede601aecc823ed9f7876869d0fc'
    assert f['gradient_references'] == {'Tests/images/linear_gradient.png': '3a93bdcd27d3737317d6f5444c387b6eec2a904819e36b0a6dcdd7a4571cf5f9', 'Tests/images/radial_gradient.png': '8b40e805ea57190ddca2a6b48d0cde375cd529f4c13e0bc1266717757df59bfb'}
assert audits[0]['native_package_versions'] == audits[1]['native_package_versions']
assert audits[0]['runtime_audit']['core_sha256'] == audits[1]['runtime_audit']['core_sha256']
for p, v in audits[0]['native_package_versions'].items():
    assert p + '=' + v in read(root / 'evaluator/image/Dockerfile')
config = json.loads(read(root / 'evaluator/case_config.json'))
sys.path.insert(0, str(root / 'evaluator'))
module_spec = importlib.util.spec_from_file_location('case060_evaluator', root / 'evaluator/evaluate_model_patch.py')
evaluator = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(evaluator)
targets = {a['target'] for a in config['runtime_assets']}
assert {'/benchmark/pytest_no_dump.py', '/benchmark/pytest_case060_isolated.py'} <= targets
runner = read(root / 'evaluator/pytest_case060_isolated.py')
assert "[sys.executable, '-m', 'pytest']" not in runner
assert runner.count("[sys.executable, '/benchmark/pytest_no_dump.py']") == 2
history = json.loads(read(root / 'verification/runner-history/summary.json'))
assert hashlib.sha256((root / 'verification/runner-history/pytest_case060_initial.py').read_bytes()).hexdigest() == history['initial_runner_sha256']
assert "[sys.executable, '-m', 'pytest']" in read(root / 'verification/runner-history/pytest_case060_initial.py')
spec = json.loads(read(work / 'case060_spec.json'))
for label, directory in [('base', 'case060-probe-base'), ('gold', 'case060-probe-gold-v2'), ('collect', 'case060-probe-collect')]:
    for p in (work / directory).iterdir():
        assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256((root / 'verification/probes' / label / p.name).read_bytes()).digest()
for directory, saved in [('case060-prototype-build', 'verification/prototype-build'), ('case060-runtime-audit', 'verification/prototype-runtime-audit'), ('case060-probe-gold', 'verification/probes/gold-initial-timeout'), ('case060-runner-history', 'verification/runner-history')]:
    for p in (work / directory).iterdir():
        assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256((root / saved / p.name).read_bytes()).digest()
timeout = json.loads(read(root / 'verification/probes/gold-initial-timeout/summary.json'))
assert timeout['exitCode'] is None and 'ETIMEDOUT' in timeout['error']
parser_history = json.loads(read(root / 'verification/parser-history/summary.json'))
assert hashlib.sha256((root / 'verification/parser-history/evaluate_model_patch_initial.py').read_bytes()).hexdigest() == parser_history['initial_sha256']
initial_negative = json.loads(read(root / 'verification/runs/case-060-final-negative-initial-parser/summary.json'))
assert initial_negative['grading']['FAIL_TO_PASS']['missing'] == 2
reparsed = evaluator.parse_test_log(read(root / 'verification/runs/case-060-final-negative-initial-parser/tests.raw.log'))
assert all(reparsed[n] == 'FAILED' for n in spec['failToPass'])
assert all(reparsed[n] == 'PASSED' for n in spec['passToPass'])
def results(text):
    return [json.loads(x) for x in re.findall(r'ISOLATED_NODE_RESULT (\{[^\n]+\})', text)]
for label, log in [('base', root / 'verification/probes/base/stdout.raw.log'), ('negative', root / 'verification/runs/case-060-final-negative/tests.raw.log'), ('gold', root / 'verification/runs/case-060-final-gold/tests.raw.log')]:
    r = results(read(log))
    assert len(r) == 4 and {x['node'] for x in r} == set(spec['probeNodes'])
    for x in r:
        if label in ['base', 'negative'] and x['node'] in spec['failToPass']:
            assert x['returncode'] == -11 and x['signal'] == 'SIGSEGV'
        else:
            assert x['returncode'] == 0 and x['signal'] is None
hashes = read(root / 'official_swebench/SHA256SUMS.txt').splitlines()
for line in hashes:
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
print('Parsed {} JSON/JSONL; evaluator syntax and {} hashes pass.'.format(len(records), len(hashes)))
print('Numeric UTC dates, XLSX cells and Artifact Tool error scan pass.')
print('Both official Base/negative targets SIGSEGV, two wrong-mode regressions pass, final Gold four passes; no Base F-mode coverage inferred.')
print('Native C scope/runtime/references/pins, initial runner SHA256, final per-child no-dump configuration, retained timeout and all evidence copies verified.')
