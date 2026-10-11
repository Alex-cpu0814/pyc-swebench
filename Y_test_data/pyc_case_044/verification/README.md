# Verification evidence

Required controls: Gold resolves FAIL_TO_PASS and preserves PASS_TO_PASS; negative remains unresolved; tamper is rejected before grading.

## Verified results (2026-10-11)

| Run | Target | Regressions | Outcome |
| --- | --- | --- | --- |
| Base probe | SIGSEGV, exit 139 | 2 passed | Repair required |
| Gold probe | Passed | 2 passed | 3 passed |
| Formal Gold | Passed | 2 passed | resolved |
| Formal negative | SIGSEGV, test exit 139 | 2 passed | unresolved |
| Formal tamper | Not run | Not run | candidate_conflicts_with_test_patch |

The negative control modifies only `README.rst`, applies successfully and builds
successfully. The target crashes before pytest can emit its terminal status, so
the grading JSON records that target as `MISSING`; `phase.json` and
`tests.raw.log` record the actual SIGSEGV (139). This is distinct from a skipped
test or an infrastructure timeout.

The build `case-044-final-build` passed the clean-image audit. Runtime evaluation
uses no network and injects candidate/test patches and the case adapter through
bind mounts. The pure-Python Cython 0.21.2 compiler is a toolchain accommodation;
no tracked Base product source was edited for compilation.
