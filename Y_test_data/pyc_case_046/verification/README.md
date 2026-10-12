# Verification evidence

Required controls: Gold resolves FAIL_TO_PASS and preserves PASS_TO_PASS; negative remains unresolved; tamper is rejected before grading.

## Verified outcomes (2026-10-12)

| Evidence | Targets | Regressions | Outcome |
| --- | --- | --- | --- |
| Base probe | 2 failed | 2 passed | pytest exit 1 |
| Gold probe | 2 passed | 2 passed | pytest exit 0 |
| Formal Gold | 2 passed | 2 passed | resolved |
| Formal negative | 2 failed | 2 passed | unresolved |
| Formal tamper | Not run | Not run | candidate_conflicts_with_test_patch |

The negative patch changes only the README heading, applies successfully and
builds successfully. Its target failures match the Base LibraryError and
unsupported-keyword TypeError. Tamper changes a line inside the protected
test-patch context and is rejected before building.

`case-046-attempt-negative` and `case-046-attempt-tamper` retain the initial
control-construction attempts. They are not the final controls: the first
negative patch failed application, and the first tamper patch did not conflict
with the upstream test hunk. The final control directories above contain the
corrected results. Initial prototype collection errors are retained under the
task's temporary work directory; successful probes are copied here as Base/Gold.

The formal image audit confirms the exact Base, a clean tracked worktree and
absence of the fix commit and protected runtime assets. The C submodule is
pinned at 67c5a6af4b85ea263e5cab854d94b691949e88ae. No WSL host dump appeared
during the verified four-node test runs.
