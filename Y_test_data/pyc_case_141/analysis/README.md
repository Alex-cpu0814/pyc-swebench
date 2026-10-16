# Analysis

Original source140 / Excel row142; source classification and trace retained separately from measured target scope.

Base passes the3 complete unchanged regressions, then complete original test_matrix fails its first new assertion because m * 42 does not raise TypeError; actual exit1 and terminalFAILED are retained. Gold completes all4 original methods normally/exit0. No crash occurred in this run; later matrix assertions were not reached on Base.

The complete official test_matrix rotates, scales and translates a Cairo Matrix, expects TypeError for m * 42 and m + 42, then checks unequal-to-42, equal-to-self and unequal-to-identity. Base stops at the first multiplication assertion; Gold reaches and passes all of them. Three unchanged complete methods cover Context paint, Cairo Error fields/subclass construction, and solid/linear/radial pattern API calls. No additional assertions, alternative operands, body extraction, allocator changes, Python2 execution or full-suite validation is claimed.

Original source140/Excel142 traces matrix_operator_multiply to test_matrix (original recorded line181). Preserve the original trace and Python-C taxonomy. The measured complete method fails at current tests/test_api.py:65 on m * 42; the recorded source line is not replaced with the measured line.

Exact upstream cairo/matrix.c type check and Python2 type flag change with the complete10-line official addition to test_matrix.

Created at is PR9 opening 2017-04-14T09:48:32Z; merged at is actual PR9 merge 2017-04-16T08:49:03Z. Issue8 opening 2017-04-14T09:21:35Z and Git commit timestamp 2017-04-16T10:49:02+02:00 are separate provenance dates.

Actual pycairo1.11.1, CPython3.6.15, pytest3.0.7/py1.4.34 and unmodified GCC8.3. Exact pinned public Python3.6.15-buster base already includes normal Cairo1.16.0 headers/runtime and development libraries. Ordinary upstream setup.py builds cairo._cairo in place on Base/Gold with identical metadata. Source Git blobs, module path/hash, generatedconfig.h, package versions and linked/header versions are audited. No test input/assertion/helper, compiler, allocator or instrumentation changes.
