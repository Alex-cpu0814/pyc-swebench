# Analysis

Original source 175, Excel row 177.

Base passes all three complete original regressions, starts the complete Java-array deletion method and terminates with SIGABRT (native returncode -6, shell exit134), without a terminal result for that target. Full exact upstream Gold completes all four methods with PASSED and exit0. The absent target terminal is recorded as MISSING.

The complete original test_array_item_del creates an Integer Java array of length 3 and executes del a[1]. Its original try/except checks the exact message only if RuntimeError is caught; it does not assert that an exception must be raised. This limited original oracle is retained unchanged. Three complete existing methods cover int arrays, Java object arrays and int memoryview buffers, including their original helper calls and assertions. Tests run Python2.7 through the actual compiled C/JNI module and OpenJDK8 JVM with original 512M JVM initialization.

Preserve the original Python-C taxonomy and source-row Python/C trace. The measured original Python unittest enters the actual jpy C extension and Java JVM; Java is an additional runtime, not a relabeling of the source dataset.

Complete upstream change: CHANGES.txt, src/main/c/jpy_jobj.c, src/test/python/jpy_array_test.py

Created at is issue52 opening 2015-07-10T13:10:42Z. No associated merge PR is reported for this direct source commit. Merged at is unknown and left absent; issue closure is not used as a merge date. The exact Git commit timestamp is retained separately.

jpy 0.8-SNAPSHOT. Python2.7 bundled unittest via transparent original-method runner. Upstream README explicitly supports Python2.7 and Java7/8. Ubuntu18.04 Python2.7 headers, ordinary GCC and OpenJDK8 JDK/JNI headers. Original setup.py clean build_ext --inplace --force, then ordinary javac compiles unchanged annotations and fixture classes. The original clean command makes setup.py skip its unconditional custom packaging/post-build suite; all selected complete official methods are executed separately by the evaluator. No source, assertion, compiler flags or product macros are changed. Ordinary Ubuntu18.04 GCC with original setup.py flags; no source/test/compiler-macro/allocator changes. The audit verifies the Python2.7 module is loaded from /testbed, initializes the actual OpenJDK8 JVM, and records exact source blobs, compiled module/fixture hashes and package versions. Transparent child process metadata sets RLIMIT_CORE0 and PR_SET_DUMPABLE0. No source/signal handler/allocator/JVM options changed. JVM fatal reports, when emitted, are captured verbatim into raw stdout.
