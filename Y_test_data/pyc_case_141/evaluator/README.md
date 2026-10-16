# Evaluator

Candidate applies before the full protected official test patch. Native force rebuild uses ordinary identical dependency metadata.

The same audited formal image runs exact full original methods in fixed order: tests/test_api.py::test_context, tests/test_api.py::test_error, tests/test_api.py::test_pattern, tests/test_api.py::test_matrix. Gold completes all4 original methods; README-negative retains the actual measured Base behavior; protected-test-context tamper rejects as candidate_conflicts_with_test_patch. Exact raw terminal/process evidence and per-node grading are retained. Only canonical anchored complete node terminal lines are counted. Pytest collection totals do not mean the unselected methods executed.

Actual pycairo1.11.1, CPython3.6.15, pytest3.0.7/py1.4.34 and unmodified GCC8.3. Exact pinned public Python3.6.15-buster base already includes normal Cairo1.16.0 headers/runtime and development libraries. Ordinary upstream setup.py builds cairo._cairo in place on Base/Gold with identical metadata. Source Git blobs, module path/hash, generatedconfig.h, package versions and linked/header versions are audited. No test input/assertion/helper, compiler, allocator or instrumentation changes.

The complete official test_matrix rotates, scales and translates a Cairo Matrix, expects TypeError for m * 42 and m + 42, then checks unequal-to-42, equal-to-self and unequal-to-identity. Base stops at the first multiplication assertion; Gold reaches and passes all of them. Three unchanged complete methods cover Context paint, Cairo Error fields/subclass construction, and solid/linear/radial pattern API calls. No additional assertions, alternative operands, body extraction, allocator changes, Python2 execution or full-suite validation is claimed.
