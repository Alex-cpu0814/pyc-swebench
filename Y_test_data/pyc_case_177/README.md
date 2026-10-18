# Python-C to SWE-bench case 177

Instance bcdev__jpy-58f81d92; repository bcdev/jpy; upstream https://github.com/bcdev/jpy/issues/54. Base 7e58cea7c2551d0b590eff3959341ee823ec43c1; fix 58f81d92b6fdf4bf2623b88a1414ba64bfc18788.

Base: target FAILED, 3 regressions PASSED, exit1. Gold: all 4 complete original methods PASSED, exit0.

Base returns a Java String-array identity string from Object.toString instead of the expected '[A, B, C]', failing the original equality assertion. The full exact Gold returns '[A, B, C]'. Base preserves 3 complete original regression passes; target status FAILED, process exit1. Gold completes all 4 complete original methods with PASSED and exit0.

The complete original test_staticMethodIsFoundOverNonStatic constructs the original Java String array [A,B,C], calls java.util.Arrays.toString, and asserts the full original corrected result [A, B, C]. The complete upstream test edit, including its whitespace correction and commented diagnostic lines, is preserved. Three complete existing overload methods retain all original arguments, results and exception checks for two-argument, variable-argument and inherited overloads.

Preserve the original Python-C taxonomy and source-row Python/C trace. The measured original Python unittest enters the actual jpy C extension and Java JVM; Java is an additional runtime, not a relabeling of the source dataset.

Complete upstream change: CHANGES.txt, src/main/c/jpy_jmethod.c, src/main/c/jpy_jtype.c, src/main/c/jpy_jtype.h, src/test/python/jpy_overload_test.py

The same audited formal image runs complete original methods in this order: src/test/python/jpy_overload_test.py::TestMethodOverloads::test_2ArgOverloadsWithVaryingTypes, src/test/python/jpy_overload_test.py::TestMethodOverloads::test_nArgOverloads, src/test/python/jpy_overload_test.py::TestMethodOverloads::test_nArgOverloadsAreFoundInBaseClass, src/test/python/jpy_overload_test.py::TestStaticMethodOverloads::test_staticMethodIsFoundOverNonStatic. Gold completes all methods; README-only negative retains the measured Base failure; a protected-test-context conflict is rejected before grading. Anchored canonical terminal lines determine statuses. Complete FAILED or ERROR terminals are retained as emitted by original unittest; the true process exit is recorded separately.

Image yutu0814/pyc-case-177-jpy:benchmark-v1. Exact complete upstream patches, workbook, raw evidence and full-file SHA256 are retained.
