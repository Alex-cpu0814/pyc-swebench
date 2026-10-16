import pathlib
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_159/analysis/creation_tools')
for name in ['configure_case159_formal.mjs','audit_publication159.mjs']:
 text=(old/name).read_text(encoding='utf-8').replace('159','160')
 if name.startswith('audit'):
  text=text.replace('pinned public NumPy1.15.4/pytest5.4.2/hypothesis5.16.0/build dependencies','pinned public NumPy1.14.5/pytest3.6.3/Hypothesis3.66.32/coverage4.5.1/build dependencies').replace('first-parent Base with genuine matching v0.8 tag','first-parent Base at static source version0.5.dev0')
 (w/name.replace('159','160')).write_bytes(text.encode())
document=(old/'document_fast_histogram_case.mjs').read_text(encoding='utf-8');a=document.index('const env=');b=document.index('\nconst semantics=',a)
document=document[:a]+"const env='Actual '+s.projectName+s.version+', CPython'+s.pythonVersionLabel+', '+s.testRunnerVersion+'. '+s.nativeRequirement+' '+s.buildSystem+' '+s.compilerToolchain+' Actual source Git blobs, native module path/hash, NumPy header/runtime ABI and dependency versions audited. Original test methods,5000 max_examples settings, explicit examples, use_coverage=True and all assertions remain unchanged. Initial coverage6.2/Hypothesis internal Collector incompatibility is separately preserved; compatible period coverage4.5.1 fixes the dependency API without disabling checks. No source/test/compiler/allocator edits beyond exact upstream Gold.';"+document[b:]
(w/'document_fast_histogram_case.mjs').write_bytes(document.encode());(w/'document_case160.mjs').write_bytes(b"process.argv[2]='160';\nawait import('./document_fast_histogram_case.mjs');\n")
print('160 formal helpers prepared; no formal case or workbook authored before Base gate.')
