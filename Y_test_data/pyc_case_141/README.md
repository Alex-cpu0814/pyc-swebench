# Python-C to SWE-bench case141

Instance pygobject__pycairo-e2154f11; repository pygobject/pycairo; issue https://github.com/pygobject/pycairo/issues/8. Base eeea4de31f9c8f4496f5695ee0258040b401f0b4; fix e2154f115d8ef32221f8a1fe08bdee49d23518ba.

Base: test_matrix FAILED (DID NOT RAISE TypeError),3 regressions PASSED. Gold: all4 complete methods PASSED.

Base passes the3 complete unchanged regressions, then complete original test_matrix fails its first new assertion because m * 42 does not raise TypeError; actual exit1 and terminalFAILED are retained. Gold completes all4 original methods normally/exit0. No crash occurred in this run; later matrix assertions were not reached on Base.

The complete official test_matrix rotates, scales and translates a Cairo Matrix, expects TypeError for m * 42 and m + 42, then checks unequal-to-42, equal-to-self and unequal-to-identity. Base stops at the first multiplication assertion; Gold reaches and passes all of them. Three unchanged complete methods cover Context paint, Cairo Error fields/subclass construction, and solid/linear/radial pattern API calls. No additional assertions, alternative operands, body extraction, allocator changes, Python2 execution or full-suite validation is claimed.

Original source140/Excel142 traces matrix_operator_multiply to test_matrix (original recorded line181). Preserve the original trace and Python-C taxonomy. The measured complete method fails at current tests/test_api.py:65 on m * 42; the recorded source line is not replaced with the measured line.

Exact upstream cairo/matrix.c type check and Python2 type flag change with the complete10-line official addition to test_matrix.

The same audited formal image runs exact full original methods in fixed order: tests/test_api.py::test_context, tests/test_api.py::test_error, tests/test_api.py::test_pattern, tests/test_api.py::test_matrix. Gold completes all4 original methods; README-negative retains the actual measured Base behavior; protected-test-context tamper rejects as candidate_conflicts_with_test_patch. Exact raw terminal/process evidence and per-node grading are retained. Only canonical anchored complete node terminal lines are counted. Pytest collection totals do not mean the unselected methods executed.

Image yutu0814/pyc-case-141-pycairo:benchmark-v1. Exact complete upstream product/test patches, two-sheet workbook and full-file SHA are retained.
