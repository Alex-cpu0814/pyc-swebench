"""Verify exact original native-abort semantics, workbook and every saved byte."""
import sys
sys.dont_write_bytecode=True
import ast,datetime,hashlib,importlib.util,json,pathlib,xml.etree.ElementTree as ET,zipfile
r=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_137')
j=lambda p:json.loads((r/p).read_text(encoding='utf-8'))
s=j('analysis/creation_tools/case137_spec.json');target=s['failToPass'][0];p2p=s['passToPass'];nodes=p2p+[target]
assert nodes==s['probeNodes'] and len(set(nodes))==4
for p in (r/'evaluator').glob('*.py'):ast.parse(p.read_text(encoding='utf-8'))
sys.path.insert(0,str(r/'evaluator'));import evaluate_model_patch as e
for group,labels in [('verification/probes',[('base',134),('gold',0)]),('verification/runs',[('case-137-final-negative',134),('case-137-final-gold',0)])]:
 for label,code in labels:
  d=r/group/label;proto=group.endswith('probes');a=json.loads((d/'summary.json').read_text());raw=(d/('stdout.raw.log'if proto else'tests.raw.log')).read_text();err=(d/'stderr.raw.log').read_text()if proto else raw
  assert(a['exitCode']if proto else a['phase']['test_exit_code'])==code
  observed=e.parse_test_log(raw);expected={n:'PASSED'for n in p2p}
  if code:
   assert target not in observed and any(l.rstrip()==target or(l.startswith(target+' ')and 'Aborted'in l)for l in raw.splitlines())
   assert 'Aborted'in err
   if not proto:
    assert a['container_exit_code']==1 and a['grading']['FAIL_TO_PASS']['missing']==1 and a['grading']['tests_observed']==3
    assert json.loads((d/'grading.json').read_text())['FAIL_TO_PASS']=={target:'MISSING'}
  else:
   expected[target]='PASSED'
   if not proto:assert a['container_exit_code']==0 and a['grading']['tests_observed']==4
  assert observed==expected,(label,observed)
assert j('verification/runs/case-137-final-tamper/summary.json')['reason']=='candidate_conflicts_with_test_patch'
assert [l for l in (r/'verification/probes/collect/stdout.raw.log').read_text().splitlines()if l.startswith('tests/')]==nodes
for p in ['verification/runtime-audit','verification/prototype-runtime-audit']:
 a=j(p+'/summary.json');v=a['runtime_audit'];assert a['exitCode']==0 and v['pycairo_version']=='1.13.4'and v['cairo_headers']==[1,16,0]and v['cairo_linked_integer']==11600 and v['native_extension'].startswith('/testbed/cairo/_cairo.')and a['native_package_versions']==s['provenance']['native_package_versions']
assert j('analysis/source_material/case137_upstream_associated_prs.json')==[]
assert s['createdAt']=='2017-07-11'and s['mergedAt']is None and s['fixCommittedAt']=='2017-07-11'
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(r/'analysis/source_material/single_pyc_case_137.xlsx')as z:
 assert [x.attrib['name']for x in ET.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',ns)]==['Source Record','SWE-bench Record']
 x=ET.fromstring(z.read('xl/worksheets/sheet2.xml'));c=x.find('.//m:c[@r="B6"]',ns);assert c.attrib.get('t')not in('s','str','inlineStr')and float(c.find('m:v',ns).text)==(datetime.date(2017,7,11)-datetime.date(1899,12,30)).days
 for i,n in enumerate([target]+p2p,11):assert x.find('.//m:c[@r="B'+str(i)+'"]/m:v',ns).text==n
 for p in z.namelist():
  if p.startswith('xl/worksheets/sheet')and p.endswith('.xml'):assert all(c.attrib.get('t')!='e'for c in ET.fromstring(z.read(p)).findall('.//m:c',ns))
assert 'matched 0 entries'in j('analysis/source_material/workbook_value_checks.json')['errorScanNdjson']
reviews=j('analysis/prior_candidate_reviews/index.json')['cases'];assert [a['case_number']for a in reviews]==['106','107','111','113','114','128','132','134']
for a in reviews:
 root=r/a['archive'];entries=[l.split('  ',1)for l in(root/'SHA256SUMS.txt').read_text().splitlines()];assert len(entries)==a['inner_sha256_count']
 assert len(entries)==len(set(p for h,p in entries))
 assert {p for h,p in entries}=={p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p!=root/'SHA256SUMS.txt'}
 for h,p in entries:assert hashlib.sha256((root/p).read_bytes()).hexdigest()==h
raw=(r/'official_swebench/SHA256SUMS.txt').read_bytes();assert b'\r'not in raw and b'\\n'not in raw
entries=[l.split('  ',1)for l in raw.decode().splitlines()];assert len(entries)==len(set(p for h,p in entries))
assert {p for h,p in entries}=={p.relative_to(r).as_posix()for p in r.rglob('*')if p.is_file()and p.relative_to(r).as_posix()!='official_swebench/SHA256SUMS.txt'}
for h,p in entries:assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h,p
print('137 verified original native134/MISSING, 3actualP2P, Gold4pass, typed XLSX date, 8inner archives and {} unique full-file SHA.'.format(len(entries)))
