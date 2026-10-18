import pathlib
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');old=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_174/analysis/creation_tools')
t=(old/'stage_case174.py').read_text(encoding='utf-8').replace('174','175').replace('pr195','pr187').replace('PR195','PR187').replace('rough-mag-symprec','rough-symprec')
a=t.index("testScope='");b=t.index("',passingRegressionDescription=",a)
t=t[:a]+"testScope='The complete original C++ GoogleTest uses the original three-atom lattice, tensors [0.005,0.002,0.002], and symprec=mag_symprec=1e-2. It calls spg_get_symmetry and spgms_get_symmetry_with_site_tensors, asserts size==4 after each, prints the original operations and frees all original arrays. Base starts this target and receives SIGSEGV without a terminal status. Gold completes both assertions and all cleanup. Three complete existing native methods cover database operations, spacegroup type and type4 dataset. The actual C API is executed; Python binding and the full source-row trace are not executed.'"+t[b+1:]
t=t.replace("'// TODO: test get_magnetic_dataset with distorted positions'","'// Local functions'")
(w/'stage_case175.py').write_bytes(t.encode())
for name in ['audit_publication174.mjs','cleanup_case174.ps1']:
 t=(old/name).read_text(encoding='utf-8').replace('174','175').replace('pr195','pr187')
 (w/name.replace('174','175')).write_bytes(t.encode())
print('175-specific native scope and helpers prepared.')
