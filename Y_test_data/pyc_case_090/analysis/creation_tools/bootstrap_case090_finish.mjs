import fs from'node:fs';const w='E:/CLB_Swe-bench/_work/pyc_batch',prev='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_088/analysis/creation_tools';
for(const n of ['refresh_case088.mjs','audit_publication088.mjs','record_publication088.mjs','verify_committed_case088.mjs','cleanup_case088.ps1']){
 let t=fs.readFileSync(prev+'/'+n,'utf8').replaceAll('088','090');
 if(n==='cleanup_case088.ps1'){
  t=t.replaceAll('case090-probe-base-v3','case090-probe-base').replaceAll('case090-probe-gold-v3','case090-probe-gold').replaceAll('case090-probe-collect-v3','case090-probe-collect').replaceAll('case090-prototype-build-v3','case090-prototype-build-v2').replaceAll('case090-runtime-audit-v2','case090-runtime-audit');
 }
 fs.writeFileSync(w+'/'+n.replaceAll('088','090'),t);
}
let v=fs.readFileSync(prev+'/verify_case088.py','utf8').replaceAll('088','090').replaceAll('surface_extension','freetype_extension').replaceAll('2013,10,21','2015,4,7');
v=v.replace("if exitcode and v['node']in s['failToPass']:\n    assert v['returncode']==-6 and 'Segmentation Fault'in err and 'surface_test.py\", line 173'in err\n   else:","if exitcode and v['node']in s['failToPass']:\n    assert v['returncode']==1 and 'AssertionError: <rect(5, 44, 44, 44)> != <rect(5, 44, 46, 44)>'in err\n    result=[json.loads(l.removeprefix('OFFICIAL_RESULT '))for l in child.splitlines()if l.startswith('OFFICIAL_RESULT ')]\n    assert len(result)==1 and result[0]['testsRun']==1 and result[0]['status']=='FAILED' and result[0]['failures']==1 and result[0]['errors']==0\n   else:");
v=v.replace("assert json.loads(read(r/'analysis/source_material/case090_upstream_associated_prs.json'))==[]", "assert json.loads(read(r/'analysis/source_material/case090_upstream_associated_prs.json.unavailable.json'))['status']==403\nassert json.loads(read(r/'analysis/source_material/case090_html_date_evidence.json'))['created_at']=='2015-04-07T19:59:02Z'");
v=v.replace("s['createdAt']=='2013-10-21'","s['createdAt']=='2015-04-07'").replace("s['fixCommittedAt']=='2013-10-28'","s['fixCommittedAt']=='2015-04-08'");
v=v.replace('true -6 SIGABRT','true ordinary wide-M AssertionError');
fs.writeFileSync(w+'/verify_case090.py',v);console.log('090 full coverage, isolated publication, exact committed-blob and archive-only cleanup tools prepared.');
