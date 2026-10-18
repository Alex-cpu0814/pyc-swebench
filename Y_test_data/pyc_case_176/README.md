# Python-C to SWE-bench case 176

Instance bcdev__jpy-81bfc112; repository bcdev/jpy; upstream https://github.com/bcdev/jpy/issues/52. Base 20cdbb714300bdb2502d9ac44740c85c64cce691; fix 81bfc112257504a3ab2cc3de3ae38ca6fa4bbf04.

Base: 3 regressions PASSED, deletion target starts then SIGABRT without terminal status (MISSING), exit134. Gold: all 4 complete original methods PASSED, exit0.

Base passes all three complete original regressions, starts the complete Java-array deletion method and terminates with SIGABRT (native returncode -6, shell exit134), without a terminal result for that target. Full exact upstream Gold completes all four methods with PASSED and exit0. The absent target terminal is recorded as MISSING.

The complete original test_array_item_del creates an Integer Java array of length 3 and executes del a[1]. Its original try/except checks the exact message only if RuntimeError is caught; it does not assert that an exception must be raised. This limited original oracle is retained unchanged. Three complete existing methods cover int arrays, Java object arrays and int memoryview buffers, including their original helper calls and assertions. Tests run Python2.7 through the actual compiled C/JNI module and OpenJDK8 JVM with original 512M JVM initialization.

Preserve the original Python-C taxonomy and source-row Python/C trace. The measured original Python unittest enters the actual jpy C extension and Java JVM; Java is an additional runtime, not a relabeling of the source dataset.

Complete upstream change: CHANGES.txt, src/main/c/jpy_jobj.c, src/test/python/jpy_array_test.py

The same audited formal image runs complete original methods in this order: src/test/python/jpy_array_test.py::TestJavaArrays::test_array_int, src/test/python/jpy_array_test.py::TestJavaArrays::test_array_object, src/test/python/jpy_array_test.py::TestJavaArrays::test_buffer_int, src/test/python/jpy_array_test.py::TestJavaArrays::test_array_item_del. Gold completes all methods; README-only negative retains the measured Base process failure; a protected-test-context conflict is rejected before grading. Anchored canonical terminal lines determine statuses. A started target without a terminal line remains MISSING, accompanied by the original native signal/exit record.

Image yutu0814/pyc-case-176-jpy:benchmark-v1. Exact complete upstream patches, workbook, raw evidence and full-file SHA256 are retained.
