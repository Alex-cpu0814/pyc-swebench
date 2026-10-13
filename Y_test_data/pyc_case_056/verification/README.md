# Verification evidence

Gold passes the official pathlib FAIL_TO_PASS and two unchanged neighboring PASS_TO_PASS nodes. A README-only negative control reaches tests and leaves the JP2 pathlib AttributeError unresolved while preserving both regressions. A candidate changing the protected pathlib-test context applies to Base but is rejected before build and grading with candidate_conflicts_with_test_patch.

The exact upstream target opens TIFF/JPEG through Path and saves JPEG/JP2 through Path. Two unchanged neighboring regressions exercise named file-object and temporary-file saving. JPEG2000, JPEG and TIFF codecs are enabled and audited; no tests are skipped. Source Python-C taxonomy is retained, but this product patch changes Python only and the verified failure precedes native JPEG2000 encoding.

## Codec and language scope

The prototype and formal codec audits explicitly require jpg_2000, jpg and libtiff support and record native package versions. The formal Dockerfile pins OpenJPEG and TIFF development packages in addition to the fixed Python/JPEG/zlib/GCC environment. Missing codecs cannot be accepted as the target failure. The Base exception occurs at filename.endswith in the Python JPEG2000 wrapper before native encoding. Product changes are Python-only; native C is present in the runtime but no native C defect is independently established.

The clean image contains fixed Base and built native extensions, without the fix commit, answer, protected patch or injected evaluator assets. Candidate builds use python setup.py build_ext -i --force and PYTHONPATH=/testbed/src.

probes/base, probes/gold and probes/collect preserve the discriminating probes and official node collection. prototype-build preserves initial build logs; prototype-dependency-audit records resolved package pins and codec support. dependency-audit records the formal codec audit and is covered by SHA256SUMS. builds/case-056-final-build and runs/case-056-final-{gold,negative,tamper} preserve formal evidence.
