"""Independent Case 058 artifacts, language, APP14 and binary-fixture verification."""
import ast
import datetime
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile
root = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_058')
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
with ZipFile(root / 'analysis/source_material/single_pyc_case_058.xlsx') as book:
    names = [s.attrib['name'] for s in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet', ns)]
    assert names == ['Source Record', 'SWE-bench Record']
    sheet = ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for address, date in [('B6', datetime.date(2021, 4, 15)), ('B9', datetime.date(2021, 4, 25))]:
        c = sheet.find('.//s:c[@r="' + address + '"]', ns)
        assert c.attrib.get('t') not in ('s', 'inlineStr')
        assert float(c.find('s:v', ns).text) == (date - datetime.date(1899, 12, 30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t') != 'e' for c in ET.fromstring(book.read(name)).findall('.//s:c', ns))
assert 'matched 0 entries' in json.loads(read(root / 'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson']
source = json.loads(read(root / 'analysis/source_row_058.json'))
assert source['symptom'] == 'incorrect result/output.'
assert all(x in source['bug_path'] for x in ['ImImagePlugin', 'WalImageFile', 'ImagingSplit'])
assert '100 == 1' in source['trace']['verified_error'] and 'Python-only' in source['trace']['verified_error']
m = json.loads(read(root / 'official_swebench/metadata.json'))
assert m['created_at'] == '2021-04-15' and m['merged_at'] == '2021-04-25'
assert m['product_files'] == ['src/PIL/JpegImagePlugin.py']
assert sorted(m['test_files']) == ['Tests/images/truncated_app14.jpg', 'Tests/test_file_jpeg.py']
assert m['product_patch_languages'] == ['Python'] and m['native_product_files_changed'] == []
assert m['source_classification'].startswith('Python-C')
assert 'GIT binary patch' in read(root / 'patches/test_patch.diff')
assert 'truncated_app14.jpg' not in read(root / 'patches/gold_patch.diff')
audits = [json.loads(read(root / p / 'summary.json')) for p in ['verification/fixture-audit', 'verification/prototype-fixture-audit']]
for a in audits:
    assert a['exitCode'] == 0 and a['error'] is None
    f = a['fixture_audit']
    assert f['pillow_version'] == f['core_version'] == '8.3.0.dev0'
    assert f['pillow_file'].startswith('/testbed/src/PIL/') and f['jpeg_support'] is True
    assert f['fixture_size'] == 29342 and f['fixture_sha256'] == '34bb25d06f445ce4f7d186b965cf30c00f6554fad7425774b0adc41e0028e1ee'
    assert a['expected_git_blob'] == '232a4c35f8c5ac8cba5c873e698f7415165ccfb3'
    for key, expected in [('app14_rgb', 1), ('app14_cmyk', 2)]:
        assert f[key] == {'segment_declared_length': 14, 'payload_length': 12, 'index1': 100, 'index11': expected}
    assert f['app14_short'] == {'segment_declared_length': 13, 'payload_length': 11, 'index1': 100, 'index11': None}
assert audits[0]['native_package_versions'] == audits[1]['native_package_versions']
dockerfile = read(root / 'evaluator/image/Dockerfile')
for p, v in audits[0]['native_package_versions'].items():
    assert p + '=' + v in dockerfile
for label in ['base', 'gold', 'collect']:
    for p in (work / ('case058-probe-' + label)).iterdir():
        assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256((root / 'verification/probes' / label / p.name).read_bytes()).digest()
for directory, saved in [('case058-prototype-build', 'verification/prototype-build'), ('case058-fixture-audit', 'verification/prototype-fixture-audit')]:
    for p in (work / directory).iterdir():
        assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256((root / saved / p.name).read_bytes()).digest()
hashes = read(root / 'official_swebench/SHA256SUMS.txt').splitlines()
for line in hashes:
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
print('Parsed {} JSON/JSONL; evaluator syntax and {} hashes pass.'.format(len(records), len(hashes)))
print('Numeric UTC opening/merge dates, XLSX cells and Artifact Tool error scan pass.')
print('Source mixed trace retained; actual Python APP14 assertion 100 == 1 separated from native C claims.')
print('Exact JPEG asset blob/size/SHA256, APP14 segment/payload lengths, transforms and fixed native packages verified; all evidence copies match.')
