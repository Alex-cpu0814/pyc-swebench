"""Admit only the measured complete original Base/Gold distinction."""
import difflib,json,pathlib,subprocess
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');p=w/'case176_spec.json';s=json.loads(p.read_text(encoding='utf-8'))
records={}
for label in ['base','gold']:
    summary=json.loads((w/f'case176-probe-{label}/summary.json').read_text(encoding='utf-8'))
    raw=(w/f'case176-probe-{label}/stdout.raw.log').read_text(encoding='utf-8')
    found=[json.loads(line.split(' ',1)[1])for line in raw.splitlines()if line.startswith('__NATIVE_PROCESS_RESULT__ ')]
    assert len(found)==1 and not summary['error'];record=found[0];records[label]=record
    assert record['observed_starts']==s['probeNodes'] and record['requested_nodes']==s['probeNodes']
    assert record['terminal_statuses']=={node:'PASSED'for node in(s['probeNodes']if label=='gold'else s['passToPass'])}
    assert summary['exitCode']==record['shell_exit_code']
assert records['gold']['returncode']==0 and records['base']['returncode']in(-6,-11)
record=records['base'];code=record['shell_exit_code'];signal=record['signal']
issue=json.loads((w/'case176_issue52_api.json').read_text(encoding='utf-8'))
commit=json.loads((w/'case176_upstream_commit_api.json').read_text(encoding='utf-8'))
prs=json.loads((w/'case176_upstream_associated_prs.json').read_text(encoding='utf-8'))
assert commit['sha']==s['fixCommit'] and commit['parents'][0]['sha']==s['baseCommit']
assert issue['number']==52 and prs==[]
scope='The complete original test_array_item_del creates an Integer Java array of length 3 and executes del a[1]. Its original try/except checks the exact message only if RuntimeError is caught; it does not assert that an exception must be raised. This limited original oracle is retained unchanged. Three complete existing methods cover int arrays, Java object arrays and int memoryview buffers, including their original helper calls and assertions. Tests run Python2.7 through the actual compiled C/JNI module and OpenJDK8 JVM with original 512M JVM initialization.'
s.update(expectedBaseExitCode=code,createdAt=issue['created_at'][:10],mergedAt=None,validationStatus='verified_base_gold',testSourceLabel='Complete original Python unittest methods using the native C/JNI bridge',baseTargetStatus=f'MISSING terminal status after native {signal}, exit{code}',verifiedError=f'Base passes all three complete original regressions, starts the complete Java-array deletion method and terminates with {signal} (native returncode {record["returncode"]}, shell exit{code}), without a terminal result for that target. Full exact upstream Gold completes all four methods with PASSED and exit0. The absent target terminal is recorded as MISSING.',targetSummary=f'Base: 3 regressions PASSED, deletion target starts then {signal} without terminal status (MISSING), exit{code}. Gold: all 4 complete original methods PASSED, exit0.',verifiedTest=' and '.join(s['failToPass']+s['passToPass']),testScope=scope,passingRegressionDescription='Three complete original Python unittest methods pass on both Base and Gold with the same original build and JVM initialization.')
s['provenance'].update(upstream_created_at_timestamp=issue['created_at'],upstream_issue_closed_at_timestamp=issue['closed_at'],associated_prs=prs,date_source=issue['url'],date_semantics=f'Created at is issue52 opening {issue["created_at"]}. No associated merge PR is reported for this direct source commit. Merged at is unknown and left absent; issue closure is not used as a merge date. The exact Git commit timestamp is retained separately.',verified_scope=scope,source_trace_scope=s['sourceTraceNotes'])
s['runtimeDescription']='jpy '+s['version']+'. '+s['testRunnerVersion']+'. '+s['nativeRequirement']+' '+s['buildSystem']+' '+s['compilerToolchain']+' The audit verifies the Python2.7 module is loaded from /testbed, initializes the actual OpenJDK8 JVM, and records exact source blobs, compiled module/fixture hashes and package versions. '+s['provenance']['resource_guard']
def control(file,transform):
    before=subprocess.check_output(['git','-C',s['sourceRepo'],'show',s['baseCommit']+':'+file]).decode();after=transform(before);assert before!=after
    return 'diff --git a/'+file+' b/'+file+'\n'+''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+file,tofile='b/'+file))
s['negativePatch']=control('README.md',lambda text:text+'\nBenchmark documentation-only control.\n')
s['tamperPatch']=control(s['testFile'],lambda text:text.replace('    def do_test_basic_buffer_protocol(self, type, itemsize, values):','    # Protected official patch context conflict\n    def do_test_basic_buffer_protocol(self, type, itemsize, values):',1))
collected=[line for line in(w/'case176-probe-collect/stdout.raw.log').read_text(encoding='utf-8').splitlines()if line.startswith('src/test/python/')]
assert collected==s['probeNodes']
(w/'case176_collected_nodes.json').write_bytes((json.dumps({'nodes':collected,'count':len(collected)},indent=2)+'\n').encode())
(w/'case176_date_evidence.json').write_bytes((json.dumps({'issue_url':issue['html_url'],'created_at':issue['created_at'],'closed_at':issue['closed_at'],'merged_at':None,'date_semantics':s['provenance']['date_semantics']},indent=2)+'\n').encode())
p.write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode())
old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_175/analysis/creation_tools')
for name in ['configure_case175_formal.mjs','refresh_case175.mjs','record_publication175.mjs','commit_case175.mjs','verify_committed_case175.mjs','push_case175_image.mjs','audit_publication175.mjs']:
    text=(old/name).read_text(encoding='utf-8').replace('175','176').replace('spglib','jpy')
    if name=='configure_case175_formal.mjs':
        text='\n'.join(line for line in text.splitlines()if not line.startswith('for(const n of '))+'\n'
        text+="const builder=r+'/evaluator/build_model_evaluator.py';fs.writeFileSync(builder,fs.readFileSync(builder,'utf8').replace('python --version','python2.7 --version'));\n"
    if name=='audit_publication175.mjs':
        start=text.index("payload_scope:'");end=text.index("',source_tree_clean",start)
        text=text[:start]+"payload_scope:'Pinned public Ubuntu18.04, Python2.7 and OpenJDK8 packages, exact public jpy first-parent Base source with ordinary original setup.py C/JNI compilation and javac fixtures. No host attachments, private files, credentials, candidate/Gold/test patches, fix object or evaluator runtime assets copied into image."+text[end:]
    (w/name.replace('175','176')).write_bytes(text.encode())
print(s['targetSummary'])
