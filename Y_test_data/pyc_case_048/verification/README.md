# Verification evidence

Gold resolves the selected float16 FAIL_TO_PASS and preserves two PASS_TO_PASS nodes. The README-only negative patch reaches tests and leaves float16 failed with an index-23/table-length-21 diagnostic. The candidate changing protected test context applies to Base but is rejected as candidate_conflicts_with_test_patch before build and grading.

The clean image contains only fixed Base source and its ordinary native build. The evaluator touches sigtoolsmodule.c and rebuilds with CFLAGS="-O0 -g -fsanitize=bounds -fno-sanitize-recover=bounds" and LDFLAGS="-fsanitize=bounds" for every candidate. UBSAN_OPTIONS=halt_on_error=1:print_stacktrace=1 is identical for all controls. Each official pytest node runs separately, and the runner requires the expected node PASSED line as well as exit zero.

The probes preserve identical instrumented Base/Gold execution. Ordinary uninstrumented Base and Gold both passed; this case establishes a regression under bounds instrumentation, not an independently reproduced ordinary-build crash. The exact upstream test patch retains all dtype parameters; only the discriminating float16 parameter is graded.

Initial controls in runs/case-048-rejected-control-negative and runs/case-048-rejected-control-tamper failed to apply because template/manual context did not match Base. They are retained for transparency and excluded from grading evidence. Final controls were regenerated from the actual Base files.

Build evidence is in builds/case-048-final-build. Final formal summaries are in runs/case-048-final-gold, runs/case-048-final-negative, and runs/case-048-final-tamper.
