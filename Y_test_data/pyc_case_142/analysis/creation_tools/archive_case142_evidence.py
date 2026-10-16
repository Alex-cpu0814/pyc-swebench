import json,pathlib,shutil
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');r=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_142')
values=json.loads((w/'source_values.json').read_text(encoding='utf-8'));row=next(v for v in values['values'][1:]if str(v[0])=='141')
(r/'analysis/source_material/original_source_row_141.json').write_bytes((json.dumps({'sheet':values['sheet'],'excel_row':143,'headers':values['values'][0],'row':row},ensure_ascii=False,indent=2)+'\n').encode())
(w/'document_case142.mjs').write_bytes(b"process.argv[2]='142';\nawait import('./document_pycairo_case.mjs');\n")
(r/'analysis/creation_tools').mkdir(exist_ok=True)
shutil.copy2(w/'independent_case_review.py',r/'analysis/creation_tools/independent_case_review.py')
print('Original142 source row and reproducible review archived.')
