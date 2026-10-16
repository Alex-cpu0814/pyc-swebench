"""Verify exact full original-method results, saved workbook and all bytes."""
import sys
sys.dont_write_bytecode=True
import ast,datetime,hashlib,json,pathlib,xml.etree.ElementTree as ET,zipfile
r=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_138')
j=lambda p:json.loads((r/p).read_text(encoding='utf-8'))
s=j('analysis/creation_tools/case138_spec.json');target=s['failToPass'][0];p2p=s['passToPass'];nodes=[target]+p2p
assert nodes==s['probeNodes'] and len(set(nodes))==4
for p in (r/'evaluator').glob('*.py'):ast.parse(p.read_text(encoding='utf-8'))
sys.path.insert(0,str(r/'evaluator'));import evaluate_model_patch as e
for group,labels in [('verification/probes',[('base',1),('gold',0)]),('verification/runs',[('case-138-final-negative',1),('case-138-final-gold',0)])]:
 for label,code in labels:
  d=r/group/label;proto=group.endswith('probes');a=json.loads((d/'summary.json').read_text());raw=(d/('stdout.raw.log'if proto else'tests.raw.log')).read_text()
  assert(a['exitCode']if proto else a['phase']['test_exit_code'])==code
  expected={n:'PASSED'for n in p2p};expected[target]='FAILED'if code else'PASSED'
  assert e.parse_test_log(raw)==expected
  assert [n for n,status in e.parse_test_log(raw).items()]==nodes
  if code:assert "AttributeError: module 'cairo' has no attribute 'RasterSourcePattern'"in raw
  if not proto:assert a['grading']['tests_observed']==4
assert j('verification/runs/case-138-final-tamper/summary.json')['reason']=='candidate_conflicts_with_test_patch'
assert len({j('verification/runs/case-138-final-'+l+'/summary.json')['image']['id']for l in ['gold','negative','tamper']})==1
assert [l for l in(r/'verification/probes/collect/stdout.raw.log').read_text().splitlines()if l.startswith('tests/')]==nodes
for p in ['verification/runtime-audit','verification/prototype-runtime-audit']:
 a=j(p+'/summary.json');v=a['runtime_audit'];assert a['exitCode']==0 and v['pycairo_version']=='1.14.1'and v['cairo_headers']==[1,16,0]and v['cairo_linked_integer']==11600 and v['native_extension'].startswith('/testbed/cairo/_cairo.')and a['native_package_versions']==s['provenance']['native_package_versions']
assert j('analysis/source_material/case138_upstream_associated_prs.json')==[]
assert s['createdAt']=='2017-07-10'and s['mergedAt']is None and s['fixCommittedAt']=='2017-07-21'
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(r/'analysis/source_material/single_pyc_case_138.xlsx')as z:
 assert [x.attrib['name']for x in ET.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',ns)]==['Source Record','SWE-bench Record']
 x=ET.fromstring(z.read('xl/worksheets/sheet2.xml'));c=x.find('.//m:c[@r="B6"]',ns);assert c.attrib.get('t')not in('s','str','inlineStr')and float(c.find('m:v',ns).text)==(datetime.date(2017,7,10)-datetime.date(1899,12,30)).days
 for i,n in enumerate(nodes,11):assert x.find('.//m:c[@r="B'+str(i)+'"]/m:v',ns).text==n
 for p in z.namelist():
  if p.startswith('xl/worksheets/sheet')and p.endswith('.xml'):assert all(c.attrib.get('t')!='e'for c in ET.fromstring(z.read(p)).findall('.//m:c',ns))
assert 'matched 0 entries'in j('analysis/source_material/workbook_value_checks.json')['errorScanNdjson']
raw=(r/'official_swebench/SHA256SUMS.txt').read_bytes();assert b'\r'not in raw and b'\\n'not in raw
entries=[l.split('  ',1)for l in raw.decode().splitlines()];assert len(entries)==len(set(p for h,p in entries))
assert {p for h,p in entries}=={p.relative_to(r).as_posix()for p in r.rglob('*')if p.is_file()and p.relative_to(r).as_posix()!='official_swebench/SHA256SUMS.txt'}
for h,p in entries:assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h,p
print('138 verified actual constructor AttributeError, Gold4PASS/3P2P, exact typed workbook and {} unique full-file SHA.'.format(len(entries)))
