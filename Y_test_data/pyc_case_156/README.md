# Python-C to SWE-bench case156

Instance ghaering__pysqlite-9b23d8d2; repository ghaering/pysqlite; issue https://github.com/ghaering/pysqlite/issues/33. Base d7c44a6b62ccf27ae2a006d32dc25cd49ca45320; fix 9b23d8d2863715e3654a8bb4a33483aa5adf40fd.

Base:2 original limit methods ERROR (get_limit absent),3 regressions PASSED. Gold: all5 complete methods PASSED.

Base passes3 complete original regressions. Both complete new LimitTests methods emit unittestERROR because the first con.get_limit call raises AttributeError: Connection has no attribute get_limit, at built original hooks.py lines161 and169; actual process exit1. CheckSetLimit never reaches set_limit on Base. Gold completes both original limit methods and all3 regressions,5PASSED/exit0. Original unittestERROR remains ERROR in raw canonical statuses and grading, never relabeled as an assertionFAILED.

Complete original CheckGetLimit opens an in-memory connection, queries SQLITE_LIMIT_VARIABLE_NUMBER and requires a positive value. CheckSetLimit opens its own connection, reads the original limit, sets oldval-1 and requires the next read to equal oldval-1. Base stops at the first get_limit in each method; Gold completes both. Three unchanged complete regressions require a callable collation callback, record progress callback invocation, and verify nonzero progress return cancels execution with OperationalError. Original fixtures, assertions, SQL and inputs remain unchanged; no external datastore caller, full suite, invalid-ID or set_limit return-value check is claimed.

Original source155/Excel157 records missing functionality and traces pysqlite_connection_set_limit to external datastore csp_crc32_verify. That external caller is not in this repository. Preserve it separately from the actually executed original hooks LimitTests.

Complete upstream product patch adds the get_limit/set_limit C methods and documents them; exact official test patch adds complete LimitTests.CheckGetLimit/CheckSetLimit and adds that class to the original suite.

The same audited formal image runs exact full original methods in fixed order: lib/test/hooks.py::CollationTests::CheckCreateCollationNotCallable, lib/test/hooks.py::ProgressTests::CheckProgressHandlerUsed, lib/test/hooks.py::ProgressTests::CheckCancelOperation, lib/test/hooks.py::LimitTests::CheckGetLimit, lib/test/hooks.py::LimitTests::CheckSetLimit. Gold completes all5 original methods; README-negative retains the actual measured Base behavior; protected-test-context tamper rejects as candidate_conflicts_with_test_patch. Exact raw terminal/process evidence and per-node grading are retained. Only canonical anchored complete node terminal lines are counted. Pytest collection totals do not mean the unselected methods executed.

Image yutu0814/pyc-case-156-pysqlite:benchmark-v1. Exact complete upstream product/test patches, two-sheet workbook and full-file SHA are retained.
