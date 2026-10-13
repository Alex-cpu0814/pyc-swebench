"""Independent artifact/language/codec checks for finalized Case 056."""
import ast
import datetime
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile

root = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_056')
work = Path('E:/CLB_Swe-bench/_work/pyc_batch')
read = lambda path: path.read_text(encoding='utf-8')
records = list(root.rglob('*.json')) + list(root.rglob('*.jsonl'))
for path in records:
    for value in [read(path)] if path.suffix == '.json' else read(path).splitlines():
        if value.strip():
            json.loads(value)
for path in (root / 'evaluator').glob('*.py'):
    ast.parse(read(path))
ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root / 'analysis/source_material/single_pyc_case_056.xlsx') as book:
    names = [s.attrib['name'] for s in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet', ns)]
    assert names == ['Source Record', 'SWE-bench Record']
    sheet = ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for address, expected in [('B6', datetime.date(2021, 7, 24)), ('B9', datetime.date(2021, 8, 6))]:
        cell = sheet.find('.//s:c[@r="' + address + '"]', ns)
        assert cell.attrib.get('t') not in ('s', 'inlineStr')
        assert float(cell.find('s:v', ns).text) == (expected - datetime.date(1899, 12, 30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t') != 'e' for c in ET.fromstring(book.read(name)).findall('.//s:c', ns))
inspection = json.loads(read(root / 'analysis/source_material/workbook_value_checks.json'))
assert 'matched 0 entries' in inspection['errorScanNdjson']
source = json.loads(read(root / 'analysis/source_row_056.json'))
assert source['symptom'] == 'error message (attribute error)'
assert 'test_write_encoding_error_message' in source['bug_path'] and '_copy' in source['bug_path']
assert 'before native encoding' in source['trace']['verified_error']
metadata = json.loads(read(root / 'official_swebench/metadata.json'))
assert metadata['created_at'] == '2021-07-24' and metadata['merged_at'] == '2021-08-06'
assert metadata['product_files'] == ['src/PIL/Image.py'] and metadata['test_files'] == ['Tests/test_image.py']
assert metadata['product_patch_languages'] == ['Python'] and metadata['native_product_files_changed'] == []
assert metadata['source_classification'].startswith('Python-C')
formal_audit = json.loads(read(root / 'verification/dependency-audit/summary.json'))
prototype_audit = json.loads(read(root / 'verification/prototype-dependency-audit/summary.json'))
for audit in [formal_audit, prototype_audit]:
    assert audit['exitCode'] == 0 and audit['error'] is None
    assert audit['codec_audit']['pillow_version'] == '8.4.0.dev0'
    assert audit['codec_audit']['pillow_file'].startswith('/testbed/src/PIL/')
    assert all(audit['codec_audit']['codec_support'][codec] for codec in ['jpg_2000', 'jpg', 'libtiff'])
assert formal_audit['native_package_versions'] == prototype_audit['native_package_versions']
dockerfile = read(root / 'evaluator/image/Dockerfile')
for package in ['libopenjp2-7-dev', 'libtiff-dev']:
    assert package + '=' + formal_audit['native_package_versions'][package] in dockerfile
for label in ['base', 'gold', 'collect']:
    for path in (work / ('case056-probe-' + label)).iterdir():
        saved = root / 'verification/probes' / label / path.name
        assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(saved.read_bytes()).digest()
for directory, saved_directory in [('case056-prototype-build', 'verification/prototype-build'), ('case056-dependency-audit', 'verification/prototype-dependency-audit')]:
    for path in (work / directory).iterdir():
        saved = root / saved_directory / path.name
        assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(saved.read_bytes()).digest()
for line in read(root / 'official_swebench/SHA256SUMS.txt').splitlines():
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
print('Parsed {} JSON/JSONL files; evaluator syntax OK.'.format(len(records)))
print('XLSX dates are numeric UTC opening/merge dates; no error cells; Artifact Tool error scan matched zero entries.')
print('Source Python-C taxonomy and original WebP/PyAccess trace preserved; product fix and verified failure are explicitly Python-only.')
print('Required OpenJPEG/JPEG/TIFF codecs enabled; native pins identical in prototype/formal audits; all saved probe/build/audit copies and final checksums match.')
