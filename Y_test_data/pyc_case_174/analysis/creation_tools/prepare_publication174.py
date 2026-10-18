import pathlib
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_160/analysis/creation_tools')
t=(old/'audit_publication160.mjs').read_text(encoding='utf-8').replace('160','174')
a=t.index("payload_scope:'");b=t.index("',source_tree_clean",a)
t=t[:a]+"payload_scope:'Pinned public Python3.8.20-bullseye, public cmake3.22.6, exact public GoogleTest release-1.12.1 and spglib first-parent Base source with ordinary default Release C/C++ compilation. No host attachments, private files, credentials, candidate/Gold/test patches, fix object or evaluator runtime assets copied into image."+t[b:]
(w/'audit_publication174.mjs').write_bytes(t.encode())
t=(old/'cleanup_case160.ps1').read_text(encoding='utf-8').replace('160','174')
t=t.replace("'case174-prototype-build'='verification/prototype-build'","'case174-prototype-build'='verification/history/case174-prototype-build'")
(w/'cleanup_case174.ps1').write_bytes(t.encode())
print('Publication payload and scoped byte-checked cleanup prepared.')
