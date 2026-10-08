# Verification evidence

Required controls: Gold resolves FAIL_TO_PASS and preserves PASS_TO_PASS; negative remains unresolved; tamper is rejected before grading.

Formal results:

- `case-023-final-build`: clean Base image built and audited successfully.
- `case-023-final-gold`: resolved; 1/1 FAIL_TO_PASS and 2/2 PASS_TO_PASS passed.
- `case-023-final-negative`: unresolved; the target aborts with exit code 134 while both regressions pass.
- `case-023-final-tamper`: rejected with `candidate_conflicts_with_test_patch`.
