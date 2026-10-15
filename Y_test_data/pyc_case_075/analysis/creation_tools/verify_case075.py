"""Independent saved artifact and real official-result verification for075."""
import ast,datetime,hashlib,json,sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
root=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_075')
read=lambda p:p.read_text(encoding='utf-8')
records=list(root.rglob('*.json'))+list(root.rglob('*.jsonl'))
for p in records:
    for v in [read(p)] if p.suffix=='.json' else read(p).splitlines():
        if v.strip():json.loads(v)
for p in (root/'evaluator').glob('*.py'):ast.parse(read(p))
s=json.loads(read(root/'analysis/creation_tools/case075_spec.json'))
m=json.loads(read(root/'official_swebench/metadata.json'))
assert m['product_files']==['src_c/_pygame.h','src_c/constants.c','src_c/event.c','src_c/rwobject.c','src_c/time.c','src_py/locals.py']
assert m['test_files']==['test/time_test.py','test/event_test.py'] or m['test_files']==['test/event_test.py','test/time_test.py']
assert m['product_patch_languages']==['C','Python'] and len(m['FAIL_TO_PASS'])==1 and len(m['PASS_TO_PASS'])==3
nodes=s['failToPass']+s['passToPass'];assert len(nodes)==len(set(nodes))==4
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(root/'analysis/source_material/single_pyc_case_075.xlsx') as book:
    assert [n.attrib['name'] for n in ET.fromstring(book.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns)]==['Source Record','SWE-bench Record']
    sheet=ET.fromstring(book.read('xl/worksheets/sheet2.xml'))
    for cell,date in [('B6',datetime.date(2020,12,16)),('B9',datetime.date(2020,12,21))]:
        c=sheet.find('.//s:c[@r="'+cell+'"]',ns);assert c.attrib.get('t') not in ('s','inlineStr','str');assert float(c.find('s:v',ns).text)==(date-datetime.date(1899,12,30)).days
    for idx,node in enumerate(nodes,12):
        c=sheet.find('.//s:c[@r="B'+str(idx)+'"]',ns);assert c.attrib['t']=='str' and c.find('s:v',ns).text==node
    for name in book.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):assert all(c.attrib.get('t')!='e' for c in ET.fromstring(book.read(name)).findall('.//s:c',ns))
assert 'matched 0 entries' in json.loads(read(root/'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson']
api=json.loads(read(root/'analysis/source_material/upstream_pr_api.json'));assert api['merge_commit_sha']==s['fixCommit'] and api['created_at']=='2020-12-16T04:42:11Z' and api['merged_at']=='2020-12-21T16:19:15Z';assert s['provenance']['source_commit_utc_timestamp']=='2020-12-21T16:19:14Z'
assert [x for x in read(root/'verification/probes/collect/stdout.raw.log').splitlines() if x.startswith('test/')]==s['probeNodes']
sys.dont_write_bytecode=True;sys.path.insert(0,str(root/'evaluator'));import evaluate_model_patch as evaluator
for label in ['gold','negative']:
    log=read(root/('verification/runs/case-075-final-'+label+'/tests.raw.log'));expected={n:('FAILED' if label=='negative' and n in s['failToPass'] else 'PASSED') for n in nodes};assert evaluator.parse_test_log(log)==expected;assert 'collected 4 items' in log;assert ('4 passed' if label=='gold' else '1 failed, 3 passed') in log
    if label=='negative':assert "'loops' is an invalid keyword" in log
    summary=json.loads(read(root/('verification/runs/case-075-final-'+label+'/summary.json')));assert summary['grading']['tests_observed']==4
assert json.loads(read(root/'verification/runs/case-075-final-tamper/summary.json'))['reason']=='candidate_conflicts_with_test_patch'
audits=[json.loads(read(root/('verification/'+p+'/summary.json'))) for p in ['runtime-audit','prototype-runtime-audit']]
for a in audits:
    r=a['runtime_audit'];assert a['exitCode']==0 and r['pygame_version']=='2.0.1.dev1' and r['pygame_revision']=='';assert r['sdl_compiled']==r['sdl_linked']==[2,0,14];assert r['event_extension'].startswith('/testbed/build/local/pygame/') and r['time_extension'].startswith('/testbed/build/local/pygame/');assert a['native_package_versions']==s['provenance']['native_package_versions']
assert audits[0]['runtime_audit']==audits[1]['runtime_audit']
prior=root/'analysis/prior_candidate_reviews/case074';d=json.loads(read(prior/'deferral.json'));assert d['status']=='deferred_gold_official_regression_failure'
for label in ['base','gold','base-v2','gold-v3']:
    a=json.loads(read(prior/('case074-probe-'+label+'/summary.json')));assert a['exitCode']==1;assert '1 failed, 3 passed' in read(prior/('case074-probe-'+label+'/stdout.raw.log'))
for label in ['collect-v3','gold-v2']:
    a=json.loads(read(prior/('case074-probe-'+label+'/summary.json')));assert a['exitCode']==137;assert not read(prior/('case074-probe-'+label+'/stdout.raw.log')).strip()
for p in [prior/'SHA256SUMS.txt',root/'official_swebench/SHA256SUMS.txt']:
    b=p.read_bytes();assert b'\\n' not in b and b'\r' not in b;lines=b.decode().splitlines();assert len(lines)==len(set(lines));base=prior if p.parent==prior else root
    for line in lines:
        expected,name=line.split('  ',1);assert hashlib.sha256((base/name).read_bytes()).hexdigest()==expected,name
hashlines=read(root/'official_swebench/SHA256SUMS.txt').splitlines();assert set(x.split('  ',1)[1] for x in hashlines)==set(x.relative_to(root).as_posix() for x in root.rglob('*') if x.is_file() and x.name!='SHA256SUMS.txt')|{'analysis/prior_candidate_reviews/case074/SHA256SUMS.txt'}
print('Verified {} JSON/JSONL, {} unique hashes, official1F2P/3P2P, native/SDL/pinneddeps, typed XLSX dates/exactIDs and074 deferral.'.format(len(records),len(hashlines)))
