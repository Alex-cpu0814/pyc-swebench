# Verification evidence

Gold passes two official gradient targets and two unchanged wrong-mode regressions. The README-only negative control leaves both official gradient subprocesses terminated by SIGSEGV and both wrong-mode nodes passing. Protected test-loop tampering is rejected before build and grading with candidate_conflicts_with_test_patch.

The exact upstream linear/radial tests loop L, P, I and F, compare generated pixels against existing PNG references and check key pixels/modes. Base terminates at I, so F is not reached on Base; Gold verifies both I and F. Two unchanged RGB wrong-mode nodes preserve ValueError behavior. Official test logic is unmodified. Each node runs in a separate subprocess; native SIGSEGV is recorded as process failure rather than an assertion, aggregate exit 1 permits complete node grading. The product patch changes C Fill.c only; no binary asset changes.

## Runtime and process evidence

Ordinary native builds use pinned Python 3.8.20, GCC10 and dependencies without instrumentation. Clean audit confirms fixed Base without answer/test/evaluator assets. Standalone prototype/formal runtime audits record Pillow8.2 source/core paths, compiled library hash, Base Fill.c hash and unchanged reference PNG hashes. Candidate builds force native recompilation with python setup.py build_ext -i --force.

Each official node runs in its own subprocess so one native termination does not mask the next. The runner logs ISOLATED_NODE_RESULT with exact returncode and signal; a native crash is emitted as a node FAILED process result, not an assertion. Aggregate exit1 permits complete grading. The initial prototype runner called python -m pytest after disabling dumpability in the parent; that parent setting was not assumed to persist through exec. Its exact contents and SHA256 remain in runner-history. Final formal runner calls pytest_no_dump.py inside every child, disabling dumpability after exec before pytest.main. Both helpers are explicit runtime assets. No official test logic changes.

The initial Gold probe timed out before the first wrong-mode result and is retained under probes/gold-initial-timeout. It is not classified as a product failure. Gold-v2 succeeded in17 seconds, retained as probes/gold. Formal controls use the final runner.

probes/{base,gold,collect}, prototype-build, prototype-runtime-audit and runner-history retain authoring evidence. runtime-audit, runner-history and initial timeout files are covered by SHA256SUMS alongside formal builds/case-060-final-build and runs/case-060-final-{gold,negative,tamper}.

## Process-result parsing

Final Case060 parser validates ISOLATED_NODE_RESULT SIGSEGV/-11 JSON and grades it as process failure. Initial negative parser omitted those targets; its exact source, SHA256 and original summary/tests/grading are preserved. Corrected final negative control reruns the same four official nodes. Native crashes remain process failures, not assertion failures. No official test or product patch was altered.
