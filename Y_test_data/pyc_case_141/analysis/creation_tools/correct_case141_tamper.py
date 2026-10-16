"""Preserve an ineffective preliminary context control and target actual protected hunk context."""
import difflib,json,pathlib,shutil,subprocess
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');r=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_141').resolve();p=w/'case141_spec.json';s=json.loads(p.read_text(encoding='utf-8'))
source=(r/'verification/runs/case-141-final-tamper').resolve();dest=(r/'verification/history/initial-tamper-outside-protected-hunk').resolve()
assert source.is_relative_to(r)and dest.is_relative_to(r)and not dest.exists()
dest.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(source),str(dest))
shutil.copy2(r/'verification/controls/tamper_patch.diff',dest/'initial-control.diff')
file='tests/test_api.py';before=subprocess.check_output(['git','-C',s['sourceRepo'],'show',s['baseCommit']+':'+file]).decode();needle='    m.translate(10, 20)';assert before.count(needle)==1
after=before.replace(needle,needle+'  # Protected official test-patch context conflict')
s['tamperPatch']='diff --git a/'+file+' b/'+file+'\n'+''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+file,tofile='b/'+file))
p.write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode());(r/'verification/controls/tamper_patch.diff').write_bytes(s['tamperPatch'].encode())
(dest/'explanation.json').write_bytes((json.dumps({'observation':'Initial control changed the test_matrix def line, which lies outside the actual official test-patch hunk; it applied successfully and the original Base test failed normally. It was not a successful conflict control.','correction':'Change m.translate context inside the protected official hunk. No test body or evaluator rule changed; rerun only the corrected conflict control.','initial_reason':json.loads((dest/'summary.json').read_text())['reason']},indent=2)+'\n').encode())
print('Initial ineffective tamper preserved; corrected actual protected hunk context.')
