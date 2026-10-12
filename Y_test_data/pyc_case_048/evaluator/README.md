# Evaluator

The evaluator applies the candidate patch, then the exact protected upstream test patch, rebuilds the target native source under non-recovering GCC bounds checks, and runs one FAIL_TO_PASS plus two PASS_TO_PASS official pytest nodes in isolated subprocesses. The per-node runner verifies both exit status and the exact expected PASSED line; emitted results are parsed by the SciPy pytest parser.

The exact upstream protected test patch retains all five dtype parameters. Formal grading selects only float16 (the discriminating comparator-table bounds case) plus test_basic and test_none. Ordinary builds passed on both revisions. The same non-recovering bounds configuration is applied to Base, Gold and candidate builds; each official pytest node runs in a separate subprocess to preserve neighboring results after the diagnostic.
