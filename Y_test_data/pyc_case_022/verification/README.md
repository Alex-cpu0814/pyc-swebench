# Verification evidence

Required controls: Gold resolves FAIL_TO_PASS and preserves PASS_TO_PASS; negative remains unresolved; tamper is rejected before grading.

Formal results:

- `case-022-final-build`: clean Base image built and audited successfully.
- `case-022-final-gold`: resolved; 3/3 FAIL_TO_PASS and 2/2 PASS_TO_PASS passed.
- `case-022-final-negative`: unresolved; all three targets failed while both regressions passed.
- `case-022-final-tamper`: rejected with `candidate_conflicts_with_test_patch`.
