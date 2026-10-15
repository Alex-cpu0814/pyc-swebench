"""Verify original official child outcomes, exact scoring nodes and full archive."""
import ast,base64,datetime,hashlib,json,sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
r=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_088')
read=lambda p:p.read_text(encoding='utf-8')
s=json.loads(read(r/'analysis/creation_tools/case088_spec.json'))
nodes=s['passToPass']+s['failToPass']
assert len(nodes)==len(set(nodes))==4 and len(s['failToPass'])==1
for p in list(r.rglob('*.json'))+list(r.rglob('*.jsonl')):
 for v in [read(p)]if p.suffix=='.json'else read(p).splitlines():
  if v.strip():json.loads(v)
for p in (r/'evaluator').glob('*.py'):ast.parse(read(p))
sys.path.insert(0,str(r/'evaluator'));import evaluate_model_patch as evaluator
for group,labels in [('verification/probes',[('base',1),('gold',0)]),('verification/runs',[('case-088-final-negative',1),('case-088-final-gold',0)])]:
 for label,exitcode in labels:
  d=r/group/label;proto=group.endswith('probes');summ=json.loads(read(d/'summary.json'));raw=read(d/('stdout.raw.log'if proto else'tests.raw.log'))
  assert summ['exitCode'if proto else'container_exit_code']==exitcode
  expected={n:('FAILED'if exitcode and n in s['failToPass']else'PASSED')for n in nodes}
  assert evaluator.parse_test_log(raw)==expected
  records=[json.loads(l.removeprefix('OFFICIAL_PROCESS_RECORD '))for l in raw.splitlines()if l.startswith('OFFICIAL_PROCESS_RECORD ')]
  assert [v['node']for v in records]==nodes
  for v in records:
   child=base64.b64decode(v['stdout_base64']).decode();err=base64.b64decode(v['stderr_base64']).decode()
   assert 'OFFICIAL_TEST_START '+v['node']in child
   if exitcode and v['node']in s['failToPass']:
    assert v['returncode']==-6 and 'Segmentation Fault'in err and 'surface_test.py", line 173'in err
   else:
    result=[json.loads(l.removeprefix('OFFICIAL_RESULT '))for l in child.splitlines()if l.startswith('OFFICIAL_RESULT ')]
    assert v['returncode']==0 and len(result)==1 and result[0]['testsRun']==1 and result[0]['status']=='PASSED'and result[0]['errors']==result[0]['failures']==0
  if not proto:assert summ['grading']['tests_observed']==4
assert json.loads(read(r/'verification/runs/case-088-final-tamper/summary.json'))['reason']=='candidate_conflicts_with_test_patch'
assert [l for l in read(r/'verification/probes/collect/stdout.raw.log').splitlines()if l.startswith('test/')] == nodes
for p in ['verification/runtime-audit','verification/prototype-runtime-audit']:
 a=json.loads(read(r/p/'summary.json'));v=a['runtime_audit'];assert a['exitCode']==0 and v['pygame_version']=='1.9.2a0'and v['pygame_revision']==''and v['sdl_compiled']==v['sdl_linked']==[1,2,15]and v['surface_extension'].startswith('/testbed/build/local/pygame/')and a['native_package_versions']==s['provenance']['native_package_versions']
assert json.loads(read(r/'analysis/source_material/case088_upstream_associated_prs.json'))==[]
assert s['createdAt']=='2013-10-21'and s['mergedAt']is None and s['fixCommittedAt']=='2013-10-28'
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(r/'analysis/source_material/single_pyc_case_088.xlsx')as z:
 assert [x.attrib['name']for x in ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',ns)]==['Source Record','SWE-bench Record']
 sheet=ET.fromstring(z.read('xl/worksheets/sheet2.xml'));c=sheet.find('.//s:c[@r="B6"]',ns)
 assert c.attrib.get('t')not in('s','inlineStr','str')and float(c.find('s:v',ns).text)==(datetime.date(2013,10,21)-datetime.date(1899,12,30)).days
 for i,n in enumerate(s['failToPass']+s['passToPass'],11):assert sheet.find('.//s:c[@r="B'+str(i)+'"]/s:v',ns).text==n
 for n in z.namelist():
  if n.startswith('xl/worksheets/sheet')and n.endswith('.xml'):assert all(c.attrib.get('t')!='e'for c in ET.fromstring(z.read(n)).findall('.//s:c',ns))
assert 'matched 0 entries'in json.loads(read(r/'analysis/source_material/workbook_value_checks.json'))['errorScanNdjson']
raw=(r/'official_swebench/SHA256SUMS.txt').read_bytes();assert b'\r'not in raw and b'\\n'not in raw
lines=raw.decode().splitlines();assert len(lines)==len(set(lines))
for l in lines:
 expected,name=l.split('  ',1);assert hashlib.sha256((r/name).read_bytes()).hexdigest()==expected,name
assert {l.split('  ',1)[1]for l in lines}=={p.relative_to(r).as_posix()for p in r.rglob('*')if p.is_file()and p.relative_to(r).as_posix()!='official_swebench/SHA256SUMS.txt'}
print('088 verified original4methods, true -6 SIGABRT, exact4scores, native SDL1.2, typed XLSX date and {} all-file hashes.'.format(len(lines)))
