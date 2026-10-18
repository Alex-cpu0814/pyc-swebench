# Analysis

Original source 176, Excel row 178.

Base returns a Java String-array identity string from Object.toString instead of the expected '[A, B, C]', failing the original equality assertion. The full exact Gold returns '[A, B, C]'. Base preserves 3 complete original regression passes; target status FAILED, process exit1. Gold completes all 4 complete original methods with PASSED and exit0.

The complete original test_staticMethodIsFoundOverNonStatic constructs the original Java String array [A,B,C], calls java.util.Arrays.toString, and asserts the full original corrected result [A, B, C]. The complete upstream test edit, including its whitespace correction and commented diagnostic lines, is preserved. Three complete existing overload methods retain all original arguments, results and exception checks for two-argument, variable-argument and inherited overloads.

Preserve the original Python-C taxonomy and source-row Python/C trace. The measured original Python unittest enters the actual jpy C extension and Java JVM; Java is an additional runtime, not a relabeling of the source dataset.

Complete upstream change: CHANGES.txt, src/main/c/jpy_jmethod.c, src/main/c/jpy_jtype.c, src/main/c/jpy_jtype.h, src/test/python/jpy_overload_test.py

Created at is actual issue54 opening 2015-08-13T09:55:36Z. No associated merge PR is reported for this direct commit. Merged at is unknown and absent; issue closure is not substituted. The exact source Git timestamp is retained separately.

jpy 0.8-SNAPSHOT. Python2.7 bundled unittest via transparent original-method runner. Upstream README explicitly supports Python2.7 and Java7/8. Ubuntu18.04 Python2.7 headers, ordinary GCC and OpenJDK8 JDK/JNI headers. Original setup.py clean build_ext --inplace --force, then ordinary javac compiles unchanged annotations and fixture classes. The original clean command makes setup.py skip its unconditional custom packaging/post-build suite; all selected complete official methods are executed separately by the evaluator. No source, assertion, compiler flags or product macros are changed. Ordinary Ubuntu18.04 GCC with original setup.py flags; no source/test/compiler-macro/allocator changes. The audit loads the actual local compiled C/JNI module, initializes OpenJDK8, and records exact source blobs, module/fixture hashes, Python/JVM/compiler and package versions. Transparent child process metadata sets RLIMIT_CORE0 and PR_SET_DUMPABLE0. No source/signal handler/allocator/JVM options changed. JVM fatal reports, when emitted, are captured verbatim into raw stdout.
