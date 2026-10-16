import json,pathlib,shutil,subprocess
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');r=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_141')
source=w/'case140-deferred-review';dest=r/'analysis/prior_candidate_reviews/case140';assert not dest.exists();shutil.copytree(source,dest)
subprocess.run(['C:/Users/玉兔/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',str(w/'independent_deferred_review.py'),str(dest),str(w/'pycairo')],check=True)
values=json.loads((w/'source_values.json').read_text(encoding='utf-8'));row=next(v for v in values['values'][1:]if str(v[0])=='140');(r/'analysis/source_material/original_source_row_140.json').write_bytes((json.dumps({'sheet':values['sheet'],'excel_row':142,'headers':values['values'][0],'row':row},ensure_ascii=False,indent=2)+'\n').encode())
(w/'document_case141.mjs').write_bytes(b"process.argv[2]='141';\nawait import('./document_pycairo_case.mjs');\n")
print('Exact case140 deferral and original141 source row preserved.')
