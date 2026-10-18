import pathlib
root=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_176').resolve()
source=(root/'verification/builds/case-176-final-build').resolve();target=(root/'verification/history/case176-initial-builder-audit').resolve()
assert source.is_relative_to(root) and target.is_relative_to(root) and source.is_dir() and not target.exists()
target.parent.mkdir(parents=True,exist_ok=True);source.rename(target)
print('Preserved initial builder audit failure before tests, exact original bytes.')
