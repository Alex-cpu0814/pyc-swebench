# Verification evidence

Gold passes the frame-count FAIL_TO_PASS and two unchanged normal-PSD PASS_TO_PASS nodes. A README-only negative control reaches tests and leaves the UnidentifiedImageError unresolved while preserving both regressions. A candidate changing the protected frame-count-test context applies to Base but is rejected before build and grading with candidate_conflicts_with_test_patch.

The exact upstream frame-count test checks normal and negative-count PSD files for two frames and animation. Two unchanged regressions exercise normal PSD pixel decoding and layer seeking. The 5492-byte official PSD fixture is preserved by an exact binary test patch and checked against its upstream Git blob and SHA256. Product changes are Python-only; no hang or native C defect was observed.

## Fixture and language scope

Prototype and formal audits check clean Base, absence of the new fixture before the test patch, exact upstream Git blob b111c2d5675ab2eec3bf2df52d2af603e006d2a3, SHA256 b968a3619fe49f5c2078db5451057642188d7333a8644a90b3ca9a36efe79765 and size 5492. At offset 824 the signed count is -2 while the unsigned value is 65534; the layer-info size is 3066. The valid negative count represents two layers. Runtime package versions and Pillow source/core version are recorded. Product changes are Python-only; the actual Base failure is UnidentifiedImageError, with no observed hang.

The clean image contains fixed Base and built native extensions without the fix commit, answer, protected patch or injected evaluator assets. Builds use python setup.py build_ext -i --force and PYTHONPATH=/testbed/src.

probes/base, probes/gold and probes/collect preserve official tests and collection; prototype-build and prototype-fixture-audit preserve initial build and fixture evidence. fixture-audit is the formal fixture audit, covered by SHA256SUMS. builds/case-057-final-build and runs/case-057-final-{gold,negative,tamper} preserve formal controls.
