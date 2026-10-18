import datetime,json,pathlib,re,subprocess,sys
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_176/analysis/creation_tools');n=sys.argv[1]
configs={'177':{'issue':'54','file':'src/test/python/jpy_overload_test.py','target':'TestStaticMethodOverloads::test_staticMethodIsFoundOverNonStatic','regressions':['TestMethodOverloads::test_2ArgOverloadsWithVaryingTypes','TestMethodOverloads::test_nArgOverloads','TestMethodOverloads::test_nArgOverloadsAreFoundInBaseClass'],'problem':'Static Arrays.toString(String[]) must resolve the applicable static overload instead of confusing it with zero-argument Object.toString().','scope':'The complete original test_staticMethodIsFoundOverNonStatic constructs the original Java String array [A,B,C], calls java.util.Arrays.toString, and asserts the full original corrected result [A, B, C]. The complete upstream test edit, including its whitespace correction and commented diagnostic lines, is preserved. Three complete existing overload methods retain all original arguments, results and exception checks for two-argument, variable-argument and inherited overloads.'}}
cfg=configs[n];state=json.loads((w/'batch_state.json').read_text(encoding='utf-8'));item=next(c for c in state['candidates']if c['caseNumber']==n)
def git(*args):return subprocess.check_output(['git','-C',str(w/'jpy'),*args],text=True).strip()
s=json.loads((old/'case176_spec.json').read_text(encoding='utf-8'))
for key in ['additionalVerificationAssets','negativePatch','tamperPatch','verifiedError','targetSummary','testScope','passingRegressionDescription','baseTargetStatus','verifiedTest','runtimeDescription','expectedBaseNodeStatuses']:s.pop(key,None)
fix=item['fixCommit'];base=git('rev-parse',fix+'^1');version=re.search('__version__ = "([^"]+)"',git('show',base+':setup.py')).group(1)
s.update(caseNumber=n,sourceCase=item['sourceCase'],duplicateSourceCases=item['duplicateSourceCases'],sourceInstanceId='pyc_case_'+n,instanceId='bcdev__jpy-'+fix[:8],issueId=cfg['issue'],issueUrl='https://github.com/bcdev/jpy/issues/'+cfg['issue'],fixCommit=fix,baseCommit=base,createdAt=None,mergedAt=None,fixCommittedAt=git('show','-s','--format=%cs',fix),version=version,image=f'yutu0814/pyc-case-{n}-jpy:benchmark-v1',prototypeImage=f'pyc-case{n}-prototype-base:latest',testFiles=[cfg['file']],testFile=cfg['file'],goldPatchSource=str(w/f'case{n}_gold.diff'),testPatchSource=str(w/f'case{n}_test.diff'),dockerfileSource=str(w/f'Dockerfile.jpy{n}-local'),validationStatus='pending_original_native_probe',expectedBaseExitCode=None,problemStatement=cfg['problem'],testScopePlanned=cfg['scope'])
prefix=cfg['file']+'::';s['failToPass']=[prefix+cfg['target']];s['passToPass']=[prefix+node for node in cfg['regressions']];s['probeNodes']=s['passToPass']+s['failToPass'];s['testNodeOrder']=s['probeNodes']
changed=git('diff','--name-only',base,fix).splitlines();native=[f for f in changed if f.startswith('src/main/c/')]
s['upstreamDescription']='Complete upstream change: '+', '.join(changed)
s['provenance']={'upstream_url':s['issueUrl'],'base_commit':base,'fix_commit':fix,'source_parents':git('show','-s','--format=%P',fix).split(),'source_commit_timestamp_original_offset':git('show','-s','--format=%cI',fix),'source_classification':'Python-C (original taxonomy)','measured_test_language':'Python unittest -> actual C/JNI extension -> OpenJDK8 JVM','product_patch_languages':['C'],'native_product_files_changed':native,'native_source_git_blobs':{f:git('rev-parse',base+':'+f)for f in native+['setup.py','README.md',cfg['file']]},'native_package_versions':{},'resource_guard':s['provenance']['resource_guard']}
(w/f'case{n}_spec.json').write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode())
previous=json.loads((old/'case176_spec.json').read_text(encoding='utf-8'))
text=(old/'Dockerfile.jpy176-local').read_text(encoding='utf-8').replace(previous['baseCommit'],base).replace(previous['instanceId'],s['instanceId'])
(w/f'Dockerfile.jpy{n}-local').write_bytes(text.encode())
for name in ['build_case176_prototype.mjs','audit_case176.mjs','refresh_case176.mjs','record_publication176.mjs','commit_case176.mjs','verify_committed_case176.mjs','push_case176_image.mjs','audit_publication176.mjs','cleanup_case176.ps1']:
    text=(old/name).read_text(encoding='utf-8').replace('176',n)
    if name=='audit_case176.mjs':
        text=text.replace("version=='0.8-SNAPSHOT'","version=="+repr(version))
        text=text.replace("files=['src/main/c/jpy_jobj.c','setup.py','README.md','src/test/python/jpy_array_test.py',jpy.__file__]","files="+repr(list(s['provenance']['native_source_git_blobs']))+"+[jpy.__file__]")
    if name=='audit_publication176.mjs':
        text=text.replace("actual_read_only_recheck_performed:true","actual_read_only_recheck_performed:true,current_explicit_user_authorization:'Current user chose 授权本条及后续验证通过的案例 for exact Git remote main and yutu0814 namespace'")
    (w/name.replace('176',n)).write_bytes(text.encode())
item.update(status='preparing_prototype',baseCommit=base,image=s['image'],updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat());(w/'batch_state.json').write_bytes((json.dumps(state,ensure_ascii=False,indent=2)+'\n').encode())
(w/f'case{n}_progress.md').write_text('Original Python2.7/OpenJDK8 environment; pending full original Base/Gold methods.\n',encoding='utf-8')
print(json.dumps({'case':n,'base':base,'version':version,'nodes':s['probeNodes']}))
