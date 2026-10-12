"""Independent consistency checks for the finalized Case 053 artifacts."""
import ast
import datetime
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile

root = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_053')
work = Path('E:/CLB_Swe-bench/_work/pyc_batch')
read = lambda path: path.read_text(encoding='utf-8')
records = list(root.rglob('*.json')) + list(root.rglob('*.jsonl'))
for path in records:
    texts = [read(path)] if path.suffix == '.json' else read(path).splitlines()
    for value in texts:
        if value.strip():
            json.loads(value)
for path in (root / 'evaluator').glob('*.py'):
    ast.parse(read(path))
ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root / 'analysis/source_material/single_pyc_case_053.xlsx') as book:
    names = [s.attrib['name'] for s in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet', ns)]
    assert names == ['Source Record', 'SWE-bench Record']
    sheet = ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for address, expected in [('B6', datetime.date(2023, 7, 4)), ('B9', datetime.date(2023, 10, 5))]:
        cell = sheet.find('.//s:c[@r="' + address + '"]', ns)
        assert cell.attrib.get('t') not in ('s', 'inlineStr')
        assert float(cell.find('s:v', ns).text) == (expected - datetime.date(1899, 12, 30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t') != 'e' for c in ET.fromstring(book.read(name)).findall('.//s:c', ns))
inspection = json.loads(read(root / 'analysis/source_material/workbook_value_checks.json'))
assert 'matched 0 entries' in inspection['errorScanNdjson']
source = json.loads(read(root / 'analysis/source_row_053.json'))
assert 'test_modify_after_resizing' in source['bug_path']
assert '0x3434' in source['trace']['verified_error']
metadata = json.loads(read(root / 'official_swebench/metadata.json'))
assert metadata['created_at'] == '2023-07-04' and metadata['merged_at'] == '2023-10-05'
assert metadata['product_files'] == ['src/libImaging/Draw.c', 'src/libImaging/Paste.c']
assert 'Tests/images/imagedraw_rectangle_I.png' in metadata['test_files']
assert 'GIT binary patch' in read(root / 'patches/test_patch.diff')
for label in ['base', 'gold', 'collect']:
    for path in (work / ('case053-probe-' + label)).iterdir():
        saved = root / 'verification/probes' / label / path.name
        assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(saved.read_bytes()).digest()
for path in (work / 'case053-prototype-build').iterdir():
    saved = root / 'verification/prototype-build' / path.name
    assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(saved.read_bytes()).digest()
print('Parsed {} JSON/JSONL files; evaluator syntax OK.'.format(len(records)))
print('XLSX two sheets, exact numeric opening/merge dates, no error cells; Artifact Tool error scan has zero matches.')
print('Original trace preserved and scope distinguished; binary PNG is protected test asset; all saved probe/build/auxiliary copies match SHA256.')
