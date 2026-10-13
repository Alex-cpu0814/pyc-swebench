"""Independent finalized Case 057 artifact, binary-fixture and language checks."""
import ast
import datetime
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile

root = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_057')
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
with ZipFile(root / 'analysis/source_material/single_pyc_case_057.xlsx') as book:
    names = [s.attrib['name'] for s in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet', ns)]
    assert names == ['Source Record', 'SWE-bench Record']
    sheet = ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for address, expected in [('B6', datetime.date(2021, 7, 15)), ('B9', datetime.date(2021, 7, 28))]:
        cell = sheet.find('.//s:c[@r="' + address + '"]', ns)
        assert cell.attrib.get('t') not in ('s', 'inlineStr')
        assert float(cell.find('s:v', ns).text) == (expected - datetime.date(1899, 12, 30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t') != 'e' for c in ET.fromstring(book.read(name)).findall('.//s:c', ns))
inspection = json.loads(read(root / 'analysis/source_material/workbook_value_checks.json'))
assert 'matched 0 entries' in inspection['errorScanNdjson']
source = json.loads(read(root / 'analysis/source_row_057.json'))
assert source['symptom'] == 'hang'
assert all(x in source['bug_path'] for x in ['test_seek_mode_1', 'WalImageFile', '_split'])
assert 'UnidentifiedImageError' in source['trace']['verified_error'] and 'No hang' in source['trace']['verified_error']
meta = json.loads(read(root / 'official_swebench/metadata.json'))
assert meta['created_at'] == '2021-07-15' and meta['merged_at'] == '2021-07-28'
assert sorted(meta['product_files']) == ['src/PIL/PsdImagePlugin.py', 'src/PIL/_binary.py']
assert sorted(meta['test_files']) == ['Tests/images/negative_layer_count.psd', 'Tests/test_file_psd.py']
assert meta['product_patch_languages'] == ['Python'] and meta['native_product_files_changed'] == []
assert meta['source_classification'].startswith('Python-C')
assert 'GIT binary patch' in read(root / 'patches/test_patch.diff')
assert 'negative_layer_count.psd' not in read(root / 'patches/gold_patch.diff')
audits = [json.loads(read(root / x / 'summary.json')) for x in ['verification/fixture-audit', 'verification/prototype-fixture-audit']]
for audit in audits:
    assert audit['exitCode'] == 0 and audit['error'] is None
    f = audit['fixture_audit']
    assert f['pillow_version'] == f['core_version'] == '8.4.0.dev0'
    assert f['pillow_file'].startswith('/testbed/src/PIL/')
    assert f['fixture_size'] == 5492 and f['fixture_sha256'] == 'b968a3619fe49f5c2078db5451057642188d7333a8644a90b3ca9a36efe79765'
    assert (f['count_offset'], f['unsigned_count'], f['signed_count'], f['layer_info_size']) == (824, 65534, -2, 3066)
    assert audit['expected_git_blob'] == 'b111c2d5675ab2eec3bf2df52d2af603e006d2a3'
assert audits[0]['native_package_versions'] == audits[1]['native_package_versions']
dockerfile = read(root / 'evaluator/image/Dockerfile')
for package, version in audits[0]['native_package_versions'].items():
    assert package + '=' + version in dockerfile
for label in ['base', 'gold', 'collect']:
    for p in (work / ('case057-probe-' + label)).iterdir():
        assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256((root / 'verification/probes' / label / p.name).read_bytes()).digest()
for directory, saved in [('case057-prototype-build', 'verification/prototype-build'), ('case057-fixture-audit', 'verification/prototype-fixture-audit')]:
    for p in (work / directory).iterdir():
        assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256((root / saved / p.name).read_bytes()).digest()
hashes = read(root / 'official_swebench/SHA256SUMS.txt').splitlines()
for line in hashes:
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
print('Parsed {} JSON/JSONL files; evaluator syntax OK; {} final hashes match.'.format(len(records), len(hashes)))
print('Numeric UTC PR opening/merge dates, XLSX cells and Artifact Tool error scan pass.')
print('Original hang/mixed trace preserved; actual Python parser UnidentifiedImageError and no observed hang explicitly separated.')
print('Exact protected binary PSD blob/size/SHA256/signedness and fixed package versions verified; all probe/build/audit copies match.')
