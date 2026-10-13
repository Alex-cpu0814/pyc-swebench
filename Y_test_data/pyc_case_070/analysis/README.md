# Analysis

Source case 69 maps to benchmark case 070 and source Excel row 71. The exact first parent 9c589d1cb5dc81552aa8ee72694cb830bed099c6 precedes fix 335ac83c1308b928bb316eb302114d76543868cf, which is independently identical to the official PR426 merge SHA. Product patch changes only native C python/objToJSON.c: PyArg_ParseTupleAndKeywords format O|OOOOpii becomes O|OOOOiii, so encoder.indent is parsed as an integer rather than a boolean. The exact protected test patch adds test_encode_indent to tests/test_ujson.py. No binary assets are added.

Base fails the exact official test_encode_indent assertion: ujson.encode(obj, indent=4) emits one leading space instead of the expected four spaces. Native PyArg_ParseTupleAndKeywords parses indent using boolean format p, collapsing nonzero integer 4 to 1. Gold changes that format to integer i and passes the target plus all three unchanged dict/list encoding and Unicode decoding regressions. No skipped or missing nodes, process termination or instrumentation observed.

Original source case69 records incorrect result/output and an objToJSON/benchmark_medium_complex_object chain. This original source trace is retained separately from the actual official test_encode_indent output assertion measured here.

Version3.2.1.dev2 is an observed SCM development snapshot, not a claimed release. The image fetches full exact Base history and only the pinned ancestor3.2.0 tag090d7412cf298085bd8f41cde9bf983f3038496f. The two-commit distance and pinned setuptools_scm6.4.2 produce the native module and SCM version3.2.1.dev2 without a pretend-version override. python/version.h is generated and ignored; version_template.h is tracked.

The double-conversion dependency is an ordinary tracked vendored source tree, not a submodule or gitlink. Its exact tree and sample C++ blob/SHA256 are recorded. The product patch has no C++ file changes. Both PR opening and merge dates are separately retained UTC dates and numeric Excel values. REST merged_at19:00:23 is one second after source Git commit19:00:22; both originals remain in date evidence.
