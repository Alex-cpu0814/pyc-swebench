"""Freeze actual case140 results without converting a process timeout to a node failure."""
import datetime,hashlib,json,pathlib,shutil,subprocess
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');out=w/'case140-deferred-review'
out.mkdir()
s=json.loads((w/'case140_spec.json').read_text(encoding='utf-8'))
base=json.loads((w/'case140-probe-base/summary.json').read_text(encoding='utf-8'))
gold=json.loads((w/'case140-probe-gold/summary.json').read_text(encoding='utf-8'))
assert base['exitCode'] is None and 'ETIMEDOUT' in base['error'] and gold['exitCode']==0
for phase in ['base','gold']:
 raw=(w/f'case140-probe-{phase}/stdout.raw.log').read_text(encoding='utf-8')
 for node in s['probeNodes']:assert node+' PASSED' in raw
 assert '5 passed' in raw
prs=json.loads((w/'case140_upstream_associated_prs.json').read_text(encoding='utf-8'))
pr=next(p for p in prs if p['merge_commit_sha']==s['fixCommit'])
status='deferred_no_node_failure_with_post_suite_process_timeout'
s.update(validationStatus=status,expectedBaseExitCode=None,createdAt=pr['created_at'][:10],mergedAt=pr['merged_at'][:10],candidateFailToPass=s.pop('failToPass'),failToPass=[],observedBaseProcess=base,observedGoldProcess=gold)
(w/'case140_spec.json').write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode())
for p in sorted(w.iterdir()):
 if p==out:continue
 if p.name.startswith('case140') or p.name in ['Dockerfile.pycairo140-local','initialize_case140.mjs','build_case140_prototype.mjs','fetch_case140_sources.py','audit_case140.mjs','capture_case140_process.mjs','stop_case140_timeout.mjs','defer_case140.py','probe_case.mjs','prepare_case.mjs','pytest_no_dump.py']:
  if p.is_dir():shutil.copytree(p,out/p.name)
  else:shutil.copy2(p,out/p.name)
for name,files in [('complete',None),('product',['cairo/pattern.c','cairo/surface.c']),('test',['tests/test_api.py'])]:
 command=['git','-C',str(w/'pycairo'),'diff',s['baseCommit'],s['fixCommit']]+(['--']+files if files else [])
 (out/f'{name}_patch.diff').write_bytes(subprocess.check_output(command))
source=json.loads((w/'source_values.json').read_text(encoding='utf-8'))
rows=[r for r in source['values'][1:] if str(r[0])=='139'];assert len(rows)==1
(out/'original_source_row.json').write_bytes((json.dumps({'sheet':source['sheet'],'excel_row':141,'headers':source['values'][0],'row':rows[0]},ensure_ascii=False,indent=2)+'\n').encode())
decision={'case_number':'140','repo':s['repo'],'fix_commit':s['fixCommit'],'base_commit':s['baseCommit'],'product_files':['cairo/pattern.c','cairo/surface.c'],'test_files':['tests/test_api.py'],'status':status,'runtime_verified':True,'formal_benchmark_created':False,'formal_workbook_created':False,'formal_image_published':False,'publication_performed':False,'reason':'The complete two new official methods and three original regressions all emitted PASSED on both Base and Gold. Base Python stayed running after the pytest 5 passed summary and the preconfigured 600000ms Docker client timeout expired. Gold completed normally with exit0. No node failed or went missing; no admissible node-level FAIL_TO_PASS was measured. Preserve the process nonexit separately without claiming its cause or assigning a native exit code. Only the verified test container was externally removed after timeout.','observed_nodes':{'base':'5 PASSED','gold':'5 PASSED'},'base_process':{'exitCode':base['exitCode'],'signal':base['signal'],'error':base['error']},'gold_process_exit':gold['exitCode'],'pr_url':pr['html_url'],'pr_created_at':pr['created_at'],'pr_merged_at':pr['merged_at'],'source_trace':'Original139/Excel141 image_surface_create_for_data trace retained separately from the PDF/PS lifetime targets.','archive_destination':'Next suitable formal case under analysis/prior_candidate_reviews/case140','future_admission':'Require genuine complete-original-method node failure on Base and Gold pass in a supported environment. Do not convert PASSED to FAILED, introduce assertions, or alter inputs, ordering, allocator, loops or compiler settings to manufacture an outcome.'}
(out/'decision.json').write_bytes((json.dumps(decision,ensure_ascii=False,indent=2)+'\n').encode())
(out/'SHA256SUMS.txt').write_bytes(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(out).as_posix()+'\n'for p in sorted(out.rglob('*'))if p.is_file()).encode())
state=json.loads((w/'batch_state.json').read_text(encoding='utf-8'));c=next(c for c in state['candidates']if c['caseNumber']=='140');c.update(status=status,reviewEvidence=str(out),note=decision['reason'],updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
(w/'batch_state.json').write_bytes((json.dumps(state,ensure_ascii=False,indent=2)+'\n').encode())
(w/'case140_progress.md').write_bytes(('# Case140 deferred\n\n'+decision['reason']+'\n\nEvidence: '+str(out)+'\nNext pending141. Root is the sole active writer; previous continuation clients remain stopped.\n').encode())
handoff=w/'CONTINUATION.md';text=handoff.read_text(encoding='utf-8');text=text.replace('The root agent performs independent read-only reviews; the assigned continuation agent is the sole new-case writer.','The root agent is the sole active writer after prior continuation clients stopped.');text+='\n## Current authoritative update: case140 deferred; next141\n\n'+decision['reason']+'\nEvidence: '+str(out)+'. Root owns mutations directly. Previous continuation clients must remain stopped. Archive140 in the next suitable formal case and verify exact-byte copies before cleanup. Continue141 and the remaining queue serially.\n';handoff.write_bytes(text.encode())
print(json.dumps({'case':'140','status':status,'evidence':str(out),'files':len(list(out.rglob('*'))),'next':'141'}))
