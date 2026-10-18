import difflib,json,pathlib,re,subprocess,sys
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');n=sys.argv[1];p=w/f'case{n}_spec.json';s=json.loads(p.read_text(encoding='utf-8'));records={};raws={}
for label in ['base','gold']:
    summary=json.loads((w/f'case{n}-probe-{label}/summary.json').read_text(encoding='utf-8'));raws[label]=(w/f'case{n}-probe-{label}/stdout.raw.log').read_text(encoding='utf-8')
    found=[json.loads(line.split(' ',1)[1])for line in raws[label].splitlines()if line.startswith('__NATIVE_PROCESS_RESULT__ ')]
    assert len(found)==1 and not summary['error'];r=found[0];records[label]=r
    assert r['observed_starts']==s['probeNodes'] and r['requested_nodes']==s['probeNodes'] and summary['exitCode']==r['shell_exit_code']
    assert all(r['terminal_statuses'].get(node)=='PASSED'for node in(s['probeNodes']if label=='gold'else s['passToPass']))
assert records['gold']['returncode']==0
r=records['base'];code=r['shell_exit_code'];assert code in (1,134,139)
native=code in (134,139);target=s['failToPass'][0];status='MISSING'if native else r['terminal_statuses'][target];assert status in ('MISSING','FAILED','ERROR')
if native:assert target not in r['terminal_statuses'] and r['returncode']in(-6,-11)
else:assert r['returncode']==1
issue=json.loads((w/f'case{n}_issue_api.json').read_text(encoding='utf-8'));commit=json.loads((w/f'case{n}_upstream_commit_api.json').read_text(encoding='utf-8'));prs=json.loads((w/f'case{n}_upstream_associated_prs.json').read_text(encoding='utf-8'))
assert commit['sha']==s['fixCommit'] and commit['parents'][0]['sha']==s['baseCommit'] and issue['number']==int(s['issueId']) and prs==[]
details={'177':"Base returns a Java String-array identity string from Object.toString instead of the expected '[A, B, C]', failing the original equality assertion. The full exact Gold returns '[A, B, C]'."}
detail=details[n];count=len(s['passToPass']);total=len(s['probeNodes'])
s.update(expectedBaseExitCode=code,createdAt=issue['created_at'][:10],mergedAt=None,validationStatus='verified_base_gold',baseTargetStatus=status,verifiedError=detail+f' Base preserves {count} complete original regression passes; target status {status}, process exit{code}. Gold completes all {total} complete original methods with PASSED and exit0.',targetSummary=f'Base: target {status}, {count} regressions PASSED, exit{code}. Gold: all {total} complete original methods PASSED, exit0.',verifiedTest=' and '.join(s['failToPass']+s['passToPass']),testScope=s['testScopePlanned'],passingRegressionDescription=f'{count} complete original unittest methods pass on both Base and Gold with identical original builds and JVM initialization.')
if not native:s['expectedBaseNodeStatuses']={target:status}
s['provenance'].update(upstream_created_at_timestamp=issue['created_at'],upstream_issue_closed_at_timestamp=issue['closed_at'],associated_prs=prs,date_source=issue['url'],date_semantics=f'Created at is actual issue{s["issueId"]} opening {issue["created_at"]}. No associated merge PR is reported for this direct commit. Merged at is unknown and absent; issue closure is not substituted. The exact source Git timestamp is retained separately.',verified_scope=s['testScope'],source_trace_scope=s['sourceTraceNotes'])
s['runtimeDescription']='jpy '+s['version']+'. '+s['testRunnerVersion']+'. '+s['nativeRequirement']+' '+s['buildSystem']+' '+s['compilerToolchain']+' The audit loads the actual local compiled C/JNI module, initializes OpenJDK8, and records exact source blobs, module/fixture hashes, Python/JVM/compiler and package versions. '+s['provenance']['resource_guard']
def original(file):return subprocess.check_output(['git','-C',s['sourceRepo'],'show',s['baseCommit']+':'+file]).decode()
def diff(file,before,after):
    assert before!=after
    return 'diff --git a/'+file+' b/'+file+'\n'+''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+file,tofile='b/'+file))
before=original('README.md');s['negativePatch']=diff('README.md',before,before+'\nBenchmark documentation-only control.\n')
file=s['testFile'];before=original(file);lines=before.splitlines(True);old_index=None
for line in(w/f'case{n}_test.diff').read_text(encoding='utf-8').splitlines():
    if line.startswith('@@'):old_index=int(re.search(r'@@ -(\d+)',line).group(1))-1
    elif old_index is not None and line.startswith(' ')and line[1:].strip():
        assert lines[old_index].rstrip('\r\n')==line[1:];lines[old_index]=lines[old_index].rstrip('\r\n')+' # Protected official test context conflict\n';break
    elif old_index is not None and line.startswith((' ','-')):old_index+=1
else:raise AssertionError('No exact protected test context found')
s['tamperPatch']=diff(file,before,''.join(lines))
collected=[line for line in(w/f'case{n}-probe-collect/stdout.raw.log').read_text(encoding='utf-8').splitlines()if line.startswith('src/test/python/')];assert collected==s['probeNodes']
(w/f'case{n}_collected_nodes.json').write_bytes((json.dumps({'nodes':collected,'count':len(collected)},indent=2)+'\n').encode())
(w/f'case{n}_date_evidence.json').write_bytes((json.dumps({'issue_url':issue['html_url'],'created_at':issue['created_at'],'closed_at':issue['closed_at'],'merged_at':None,'date_semantics':s['provenance']['date_semantics']},indent=2)+'\n').encode())
p.write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode())
old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_176/analysis/creation_tools')
text=(old/'configure_case176_formal.mjs').read_text(encoding='utf-8').replace('176',n);text='\n'.join(line for line in text.splitlines()if not line.startswith('for(const n of '))+'\n'
text+="const builder=r+'/evaluator/build_model_evaluator.py';fs.writeFileSync(builder,fs.readFileSync(builder,'utf8').replace('python --version','python2.7 --version'));\n"
(w/f'configure_case{n}_formal.mjs').write_bytes(text.encode())
print(s['targetSummary'])
