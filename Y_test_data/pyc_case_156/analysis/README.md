# Analysis

Original source155 / Excel row157; source classification and trace retained separately from measured target scope.

Base passes3 complete original regressions. Both complete new LimitTests methods emit unittestERROR because the first con.get_limit call raises AttributeError: Connection has no attribute get_limit, at built original hooks.py lines161 and169; actual process exit1. CheckSetLimit never reaches set_limit on Base. Gold completes both original limit methods and all3 regressions,5PASSED/exit0. Original unittestERROR remains ERROR in raw canonical statuses and grading, never relabeled as an assertionFAILED.

Complete original CheckGetLimit opens an in-memory connection, queries SQLITE_LIMIT_VARIABLE_NUMBER and requires a positive value. CheckSetLimit opens its own connection, reads the original limit, sets oldval-1 and requires the next read to equal oldval-1. Base stops at the first get_limit in each method; Gold completes both. Three unchanged complete regressions require a callable collation callback, record progress callback invocation, and verify nonzero progress return cancels execution with OperationalError. Original fixtures, assertions, SQL and inputs remain unchanged; no external datastore caller, full suite, invalid-ID or set_limit return-value check is claimed.

Original source155/Excel157 records missing functionality and traces pysqlite_connection_set_limit to external datastore csp_crc32_verify. That external caller is not in this repository. Preserve it separately from the actually executed original hooks LimitTests.

Complete upstream product patch adds the get_limit/set_limit C methods and documents them; exact official test patch adds complete LimitTests.CheckGetLimit/CheckSetLimit and adds that class to the original suite.

Created at is actual issue33 opening 2013-10-14T14:31:11Z; associated-PR API returned[]. No PR merge date established, so merged_at remains absent. Issue close 2015-08-01T22:23:52Z and source Git timestamp 2015-08-02T00:21:37+02:00 are distinct and are not substituted for a merge date.

Actual pysqlite2.6.3, CPython2.7.17 standard unittest. Exact pinned public Ubuntu18.04 base and standard Python2.7-dev/GCC/SQLite development/runtime packages. Ordinary upstream distutils build_ext --force build_py --force compiles pysqlite2._sqlite and copies original package/tests under build/lib.linux-x86_64-2.7 on both Base/Gold. Audited original Git blobs, actual module path/hash, SQLite header/linked versions and all dependency package versions. Wrapper invokes whole original unittest TestCase methods with fixtures and preserves real ERROR versus FAILED statuses; no method-body extraction or test/compiler/allocator changes.
