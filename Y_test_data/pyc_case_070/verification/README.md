# Verification evidence

Gold passes the official four-space indentation target and all three unchanged regressions. The README-only negative leaves the same one-space output assertion failing while those three regressions pass. Candidate modification of the official test insertion context is rejected with candidate_conflicts_with_test_patch before build/grading.

The exact protected upstream test decodes the JSON object {"obj":31337} and compares its indent=4 encoded text with the original four-space formatting. Three unchanged official regressions cover ordinary dictionary/list conversion and Unicode decoding. Tests execute normally in one pytest process, without altered values, assertions or thresholds. Product patch is the single native C argument-format change; vendored C++ double-conversion is compiled but unchanged.

Tests run normally in one pytest process using pytest_no_dump.py only to disable core dumps. No legacy assertion counter wrapper, artificial warm-up, instrumentation or test body changes are used. Parser reads four explicit tests/... PASSED/FAILED lines and preserves full pytest output.

Prototype and formal audits verify local /testbed/ujson native extension hash, observed SCM/module3.2.1.dev2, exact source/tag/vendor Git identity and GCC/G++/Python build dependencies. Both clean Base audits observe the actual indent4 one-space output. Forced candidate rebuilds apply the native C patch before testing. Official source and test patches, raw collection/Base/Gold/build/controls, API dates and workbook inspections/previews remain covered by SHA256SUMS.
