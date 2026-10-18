import pathlib
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_175/analysis/creation_tools')
p=w/'cleanup_case176.ps1';text=(old/'cleanup_case175.ps1').read_text(encoding='utf-8').replace('175','176');p.write_bytes(text.encode())
print('Exact archive-before-removal cleanup prepared.')
