import difflib,json,pathlib,subprocess
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');p=w/'case175_spec.json';s=json.loads(p.read_text(encoding='utf-8'))
for label,code in [('base',139),('gold',0)]:
 a=json.loads((w/f'case175-probe-{label}/summary.json').read_text(encoding='utf-8'));raw=(w/f'case175-probe-{label}/stdout.raw.log').read_text(encoding='utf-8');assert a['exitCode']==code and not a['error']
 r=[json.loads(l.split(' ',1)[1])for l in raw.splitlines()if l.startswith('__NATIVE_PROCESS_RESULT__ ')];assert len(r)==1;r=r[0]
 assert r['observed_starts']==s['probeNodes'] and r['shell_exit_code']==code
 assert r['terminal_statuses']=={n:'PASSED'for n in(s['probeNodes']if label=='gold'else s['passToPass'])}
 assert r['returncode']==(0 if label=='gold'else -11)
pr=json.loads((w/'case175_pr187_api.json').read_text(encoding='utf-8'));assert pr['merge_commit_sha']==s['fixCommit']
s.update(expectedBaseExitCode=139,createdAt=pr['created_at'][:10],mergedAt=pr['merged_at'][:10],validationStatus='verified_base_gold',baseTargetStatus='MISSING terminal status after native SIGSEGV, exit139',verifiedError='Base passes three complete original native regressions, starts the complete rough-symprec target, then its native GoogleTest child exits on SIGSEGV (returncode -11, shell exit139). The target has no terminal test result and is graded MISSING. Full exact upstream Gold completes all four methods with PASSED and exit0. No FAILED terminal line is invented.',targetSummary='Base: 3 regressions PASSED, target starts then SIGSEGV with no terminal status (MISSING), exit139. Gold: 4 complete original methods PASSED, exit0.',verifiedTest=' and '.join(s['failToPass']+s['passToPass']),testScope='The complete original C++ GoogleTest uses the original three-atom lattice, tensors [0.005,0.002,0.002], and symprec=mag_symprec=1e-2. It calls spg_get_symmetry and spgms_get_symmetry_with_site_tensors, asserts size==4 after each, prints the original operations and frees all original arrays. Base starts this target and receives SIGSEGV without a terminal status. Gold completes both assertions and all cleanup. Three complete existing native methods cover database operations, spacegroup type and type4 dataset. The actual C API is executed; Python binding and the full source-row trace are not executed.',passingRegressionDescription='Three complete original native GoogleTest methods pass on Base and Gold in the same default Release build.')
s['sourceTraceNotes']='Original Python-C taxonomy and source-row trace are retained verbatim. The source trace ends at Python get_symmetry_dataset; the measured complete official regression uses native C++ GoogleTest directly calling the C API. No Python binding or full original source trace is executed by this test.'
s['provenance'].update(upstream_created_at_timestamp=pr['created_at'],upstream_merged_at_timestamp=pr['merged_at'],date_source=pr['url'],date_semantics=f"Created at is actual PR187 opening {pr['created_at']}; merged at is actual PR187 merge {pr['merged_at']}. Exact source commit timestamp is retained separately.",verified_scope=s['testScope'],source_trace_scope=s['sourceTraceNotes'])
def control(file,transform):
 before=subprocess.check_output(['git','-C',s['sourceRepo'],'show',s['baseCommit']+':'+file]).decode();after=transform(before);assert before!=after
 return 'diff --git a/'+file+' b/'+file+'\n'+''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+file,tofile='b/'+file))
s['negativePatch']=control('README.md',lambda t:t+'\nBenchmark documentation-only control.\n')
s['tamperPatch']=control(s['testFile'],lambda t:t.replace('// Local functions','// Protected official patch context conflict',1))
nodes=[l for l in(w/'case175-probe-collect/stdout.raw.log').read_text(encoding='utf-8').splitlines()if l.startswith('test/')];assert nodes==s['probeNodes']
(w/'case175_collected_nodes.json').write_bytes((json.dumps({'nodes':nodes,'count':len(nodes)},indent=2)+'\n').encode())
(w/'case175_date_evidence.json').write_bytes((json.dumps({'pr_url':pr['html_url'],'created_at':pr['created_at'],'merged_at':pr['merged_at'],'date_semantics':s['provenance']['date_semantics']},indent=2)+'\n').encode())
p.write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode())
old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_160/analysis/creation_tools')
for name in ['configure_case160_formal.mjs','refresh_case160.mjs','record_publication160.mjs','commit_case160.mjs','verify_committed_case160.mjs','push_case160_image.mjs']:
 text=(old/name).read_text(encoding='utf-8').replace('160','175').replace('fast-histogram','spglib')
 (w/name.replace('160','175')).write_bytes(text.encode())
print(s['targetSummary'])
