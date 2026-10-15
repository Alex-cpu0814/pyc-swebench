"""Independent exact-node, native-source and saved workbook verification."""
import ast,datetime,hashlib,json,sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
r=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_086');read=lambda p:p.read_text(encoding='utf-8')
records=list(r.rglob('*.json'))+list(r.rglob('*.jsonl'))
for p in records:
    for v in [read(p)] if p.suffix=='.json' else read(p).splitlines():
        if v.strip():json.loads(v)
for p in (r/'evaluator').glob('*.py'):ast.parse(read(p))
s=json.loads(read(r/'analysis/creation_tools/case086_spec.json'));m=json.loads(read(r/'official_swebench/metadata.json'));assert m['product_files']==['src_c/draw.c'] and m['test_files']==['test/draw_test.py'];assert m['product_patch_languages']==['C'];nodes=s['failToPass']+s['passToPass'];assert len(nodes)==len(set(nodes))==4 and len(s['failToPass'])==2
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(r/'analysis/source_material/single_pyc_case_086.xlsx')as b:
    assert [x.attrib['name'] for x in ET.fromstring(b.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns)]==['Source Record','SWE-bench Record'];sheet=ET.fromstring(b.read('xl/worksheets/sheet2.xml'))
    for cell,date in [('B6',datetime.date(2018,8,30)),('B9',datetime.date(2018,9,3))]:
        c=sheet.find('.//s:c[@r="'+cell+'"]',ns);assert c.attrib.get('t')not in('s','inlineStr','str');assert float(c.find('s:v',ns).text)==(date-datetime.date(1899,12,30)).days
    for idx,node in enumerate(nodes,12):assert sheet.find('.//s:c[@r="B'+str(idx)+'"]/s:v',ns).text==node
    for name in b.namelist():
        if name.startswith('xl/worksheets/sheet')and name.endswith('.xml'):assert all(x.attrib.get('t')!='e' for x in ET.fromstring(b.read(name)).findall('.//s:c',ns))
assert 'matched 0 entries' in json.loads(read(r/'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson'];api=json.loads(read(r/'analysis/source_material/upstream_pr_api.json'));assert api['merge_commit_sha']==s['provenance']['api_merge_sha'] and s['fixCommit'] in [c['sha'] for c in json.loads(read(r/'analysis/source_material/upstream_pr_commits.json'))] and api['created_at']=='2018-08-30T15:02:44Z' and api['merged_at']=='2018-09-03T16:22:00Z';assert s['provenance']['source_commit_utc_timestamp']=='2018-08-30T16:17:53Z'
assert [x for x in read(r/'verification/probes/collect/stdout.raw.log').splitlines()if x.startswith('test/draw_test.py::')]==s['probeNodes'];sys.dont_write_bytecode=True;sys.path.insert(0,str(r/'evaluator'));import evaluate_model_patch as evaluator
for label in['gold','negative']:
    raw=read(r/('verification/runs/case-086-final-'+label+'/tests.raw.log'));expected={n:('FAILED'if label=='negative'and n in s['failToPass']else'PASSED')for n in nodes};assert evaluator.parse_test_log(raw)==expected;assert('4 passed'if label=='gold'else'2 failed, 2 passed')in raw
    summary=json.loads(read(r/('verification/runs/case-086-final-'+label+'/summary.json')));assert summary['grading']['tests_observed']==4;assert summary['status']==('resolved'if label=='gold'else'unresolved')
assert json.loads(read(r/'verification/runs/case-086-final-tamper/summary.json'))['reason']=='candidate_conflicts_with_test_patch'
audits=[json.loads(read(r/('verification/'+p+'/summary.json')))for p in['runtime-audit','prototype-runtime-audit']]
for a in audits:
    v=a['runtime_audit'];assert a['exitCode']==0 and v['pygame_version']=='1.9.5.dev0'and v['pygame_revision']=='';assert v['draw_extension'].startswith('/testbed/build/local/pygame/')and v['sdl_compiled']==v['sdl_linked']==[2,0,14];assert a['native_package_versions']==s['provenance']['native_package_versions']
assert audits[0]['runtime_audit']==audits[1]['runtime_audit'];raw=(r/'official_swebench/SHA256SUMS.txt').read_bytes();assert b'\\n'not in raw and b'\r'not in raw;lines=raw.decode().splitlines();assert len(lines)==len(set(lines))
for line in lines:
    expected,name=line.split('  ',1);assert hashlib.sha256((r/name).read_bytes()).hexdigest()==expected,name
assert {x.split('  ',1)[1]for x in lines}=={x.relative_to(r).as_posix()for x in r.rglob('*')if x.is_file()and x.relative_to(r).as_posix()!='official_swebench/SHA256SUMS.txt'}
print('Verified {} JSON/JSONL, {} unique all-file SHA entries, exact4nodes,2F2P/2P2P, native/SDL and typed XLSX dates.'.format(len(records),len(lines)))

prior=r/'analysis/prior_candidate_reviews/case083'
for line in read(prior/'SHA256SUMS.txt').splitlines():
    expected,name=line.split('  ',1);assert hashlib.sha256((prior/name).read_bytes()).hexdigest()==expected
review=json.loads(read(prior/'duplicate_review.json'));assert review['is_second_parent_of_case081_fix'] and all(v['exact_bytes_equal_to_case081'] for v in review['comparisons'].values())
