"""Prepare exact-source native candidates using the already reviewed ordinary toolchain."""
import datetime,json,pathlib,subprocess,sys
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');n=sys.argv[1]
state=json.loads((w/'batch_state.json').read_text(encoding='utf-8'));candidate=next(c for c in state['candidates']if c['caseNumber']==n)
assert candidate['status']=='pending' and n in ['174','175']
source=w/'spglib'
def git(*args):return subprocess.check_output(['git','-C',str(source),*args],text=True).strip()
s=json.loads((w/'case173_spec.json').read_text(encoding='utf-8'))
fix=candidate['fixCommit'];base=git('rev-parse',fix+'^1');short=fix[:8]
for key in ['candidateFailToPass']:s.pop(key,None)
for key,value in list(s.items()):
 if isinstance(value,str):s[key]=value.replace('173',n).replace('36d570bc',short)
s.update(caseNumber=n,sourceCase=candidate['sourceCase'],fixCommit=fix,baseCommit=base,issueId='195' if n=='174' else '187',fixCommittedAt=git('show','-s','--format=%cs',fix),validationStatus='pending_original_native_probe',expectedBaseExitCode=None)
s['issueUrl']='https://github.com/spglib/spglib/pull/'+s['issueId']
target='test_spg_get_symmetry_with_tensors_rough_mag_symprec'if n=='174'else'test_spg_get_symmetry_with_tensors_rough_symprec'
prefix='test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.'
s['failToPass']=[prefix+target];s['probeNodes']=s['passToPass']+s['failToPass'];s['testNodeOrder']=s['probeNodes']
changed=git('diff','--name-only',base,fix).splitlines();product=[p for p in changed if p not in s['testFiles']]
s['problemStatement']='Handle rough magnetic symmetry tolerances without aborting symmetry search.'if n=='174'else'Handle magnetic dataset failure paths without segmentation faults.'
s['upstreamDescription']='Complete exact upstream change: '+', '.join(changed)
p=s['provenance'];p.update(upstream_url=s['issueUrl'],base_commit=base,fix_commit=fix,source_parents=git('show','-s','--format=%P',fix).split(),source_commit_timestamp_original_offset=git('show','-s','--format=%cI',fix),native_product_files_changed=[f for f in product if f.startswith('src/')],native_package_versions={})
p['native_source_git_blobs']={f:git('rev-parse',base+':'+f)for f in dict.fromkeys([f for f in product if f.startswith('src/')]+['src/version.h','test/CMakeLists.txt',s['testFile']])}
p['tool_dependency_selection']='Reuse public pinned cmake3.22.6 wheel after case173 Debian package404; original standalone CMake/default Release settings retained.'
(w/f'case{n}_spec.json').write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode())
docker=(w/'Dockerfile.spglib173-local').read_text(encoding='utf-8').replace('9218fa14771d967a20f00764b335bc2a265790a1',base).replace('36d570bc',short)
(w/f'Dockerfile.spglib{n}-local').write_bytes(docker.encode())
for pattern in ['build_case173_prototype.mjs','audit_case173.mjs']:
 (w/pattern.replace('173',n)).write_bytes((w/pattern).read_text(encoding='utf-8').replace('173',n).encode())
candidate.update(status='preparing_prototype',baseCommit=base,image=s['image'],updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
(w/'batch_state.json').write_bytes((json.dumps(state,ensure_ascii=False,indent=2)+'\n').encode())
(w/f'case{n}_progress.md').write_bytes((f'# Case{n}\n\nExact original C++ GoogleTest -> C API; pending Base/Gold measurement.\n').encode())
print(json.dumps({'case':n,'base':base,'target':target,'files':changed}))
