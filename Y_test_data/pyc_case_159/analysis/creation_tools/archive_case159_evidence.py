import json,pathlib,shutil,subprocess
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');r=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_159');dest=r/'analysis/prior_candidate_reviews/case157';assert not dest.exists();shutil.copytree(w/'case157-deferred-review',dest)
subprocess.run(['C:/Users/玉兔/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',str(w/'independent_deferred_review.py'),str(dest),str(w/'pysqlite')],check=True)
values=json.loads((w/'source_values.json').read_text(encoding='utf-8'));row=next(v for v in values['values'][1:]if str(v[0])=='158');(r/'analysis/source_material/original_source_row_158.json').write_bytes((json.dumps({'sheet':values['sheet'],'excel_row':160,'headers':values['values'][0],'row':row},ensure_ascii=False,indent=2)+'\n').encode())
(r/'analysis/creation_tools').mkdir(exist_ok=True)
for name in ['independent_case_review.py','independent_deferred_review.py']:shutil.copy2(w/name,r/'analysis/creation_tools'/name)
print('159 original source row and exact72-entry case157 deferral archived.')
