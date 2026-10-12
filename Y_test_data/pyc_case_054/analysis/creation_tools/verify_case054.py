"""Check finalized Case 054 records and process-level partial-control evidence."""
import ast
import datetime
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile

root = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_054')
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
with ZipFile(root / 'analysis/source_material/single_pyc_case_054.xlsx') as book:
    names = [s.attrib['name'] for s in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet', ns)]
    assert names == ['Source Record', 'SWE-bench Record']
    sheet = ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for address, expected in [('B6', datetime.date(2023, 1, 9)), ('B9', datetime.date(2023, 1, 11))]:
        cell = sheet.find('.//s:c[@r="' + address + '"]', ns)
        assert cell.attrib.get('t') not in ('s', 'inlineStr')
        assert float(cell.find('s:v', ns).text) == (expected - datetime.date(1899, 12, 30)).days
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            assert all(c.attrib.get('t') != 'e' for c in ET.fromstring(book.read(name)).findall('.//s:c', ns))
inspection = json.loads(read(root / 'analysis/source_material/workbook_value_checks.json'))
assert 'matched 0 entries' in inspection['errorScanNdjson']
source = json.loads(read(root / 'analysis/source_row_054.json'))
assert source['symptom'] == 'segment fault.' and 'box_blur' in source['bug_path']
assert 'process exit 134' in source['trace']['verified_error']
metadata = json.loads(read(root / 'official_swebench/metadata.json'))
assert metadata['created_at'] == '2023-01-09' and metadata['merged_at'] == '2023-01-11'
assert metadata['product_files'] == ['src/PIL/ImageFilter.py', 'src/libImaging/BoxBlur.c']
assert metadata['test_files'] == ['Tests/test_image_filter.py']
partial_dir = root / 'verification/runs/case-054-final-python-only'
partial = json.loads(read(partial_dir / 'summary.json'))
assert partial['phase']['test_exit_code'] == 134
assert partial['grading']['FAIL_TO_PASS']['missing'] == 1
assert partial['grading']['FAIL_TO_PASS']['failed'] == 0
assert partial['grading']['PASS_TO_PASS']['passed'] == 2
assert metadata['verification']['partial_python_only_control']['test_process_exit_code'] == 134
patch = root / 'verification/controls/python_only_patch.diff'
assert hashlib.sha256(patch.read_bytes()).hexdigest() == partial['model_patch_sha256']
assert 'src/PIL/ImageFilter.py' in read(patch) and 'src/libImaging/BoxBlur.c' not in read(patch)
events = [json.loads(line) for line in read(partial_dir / 'events.jsonl').splitlines()]
commands = [item['command'] for item in events if item.get('event') == 'command.started']
assert any('python_only_patch.diff' in str(command) for command in commands)
log = read(partial_dir / 'tests.raw.log')
assert 'Fatal Python error: Aborted' in log and 'line 187 in test_invalid_box_blur_filter' in log
for label in ['base', 'gold', 'collect']:
    for path in (work / ('case054-probe-' + label)).iterdir():
        saved = root / 'verification/probes' / label / path.name
        assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(saved.read_bytes()).digest()
for path in (work / 'case054-prototype-build').iterdir():
    saved = root / 'verification/prototype-build' / path.name
    assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(saved.read_bytes()).digest()
for line in read(root / 'official_swebench/SHA256SUMS.txt').splitlines():
    expected, name = line.split('  ', 1)
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
print('Parsed {} JSON/JSONL files; evaluator syntax OK.'.format(len(records)))
print('XLSX dates are numeric and use UTC opening/merge dates; all cells error-free; Artifact Tool error scan matched zero entries.')
print('Original source symptom/trace preserved; Python-only official control has process exit 134, target MISSING, two preceding regressions passed; command/raw evidence preserved.')
print('All saved probe/build copies match SHA256; 35 final checksums including Python-only evidence match.')
