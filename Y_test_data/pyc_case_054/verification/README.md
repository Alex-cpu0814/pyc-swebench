# Verification evidence

Gold passes the one FAIL_TO_PASS and two PASS_TO_PASS official nodes. A README-only negative control reaches tests and fails the constructor ValueError assertion while preserving both regressions. A candidate changing protected test-patch context applies to Base but is rejected before build or scoring with candidate_conflicts_with_test_patch.

## Python-only partial control

The exact upstream src/PIL/ImageFilter.py-only patch is saved as controls/python_only_patch.diff. It uses the same formal image, full protected official test patch, forced native rebuild and three-node test command as the other controls, with both regressions listed first. Those regressions pass. The official constructor assertion succeeds, but the second block mutates radius to -2 and calls filter; the process aborts with Fatal Python error: Aborted at test_image_filter.py line 187. The shell test process exit is 134; the evaluator container exit is 1. The target has no terminal pytest status (MISSING), rather than an ordinary assertion failure. The native guard is therefore necessary. This is an independently observed abort, not a reproduced SIGSEGV.

The partial controls patch, summary, exact Docker command in events.jsonl, raw build/test/application/container logs, phase and grading are included in SHA256SUMS. All controls preserve exact upstream test logic.

## Environment and scope

The clean image contains fixed historical Base and native extensions; no fix commit, answer, protected patch or runtime evaluator assets are baked in. Every candidate uses python setup.py build_ext -i --force and PYTHONPATH=/testbed/src. No instrumentation is added.

One unchanged official target body checks construction and then filtering after radius mutation. Two unchanged regressions validate native numerical blur results for radius zero and one. The exact protected upstream patch retains the added BoxBlur(0) sanity parameter, outside graded scope. A Python-only partial control runs the same three nodes with regressions first: two pass, then the target process aborts with exit 134 and no terminal pytest status. The observed native guard is necessary in addition to constructor validation.

probes/base, probes/gold and probes/collect preserve the source probes and exact official node collection. prototype-build preserves the initial build. builds/case-054-final-build records the clean formal image audit. runs/case-054-final-{gold,negative,tamper,python-only} preserves formal evidence.
