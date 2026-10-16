# Python-C to SWE-bench case160

Instance astrofrog__fast-histogram-e384cdf1; repository astrofrog/fast-histogram; issue https://github.com/astrofrog/fast-histogram/pull/21. Base 76b6f57a27f31cdefc23444f91611a00c9b4332d; fix e384cdf1fec4ee65a594ca4e91478eb3c98b2d18.

Base: complete nd_arrays target FAILED at1d reshape comparison;2 original5000-example methods PASSED. Gold: all3 complete methods PASSED.

With compatible coverage4.5.1 and original checks enabled, Base completes both original property methods, each recording5000 passing examples. It then fails the first exact array comparison in complete test_nd_arrays at line97: histogram1d of the1000-element vector differs from its10x10x10 reshape. The observed result bins sum to1000 versus10. Base terminalFAILED/exit1; its later2d target comparison is not reached. Gold completes both original property methods with5000 passing examples each plus the complete1d/2d target,3PASSED/exit0. Original random arrays,5000 settings, explicit examples, coverage and assertions are unchanged.

Complete original test_nd_arrays constructs1000 random x values, compares histogram1d(x) with histogram1d(x.reshape(10,10,10)), then constructs1000 y values and compares1d-input and reshaped-input histogram2d results. Base stops at the first1d comparison; Gold reaches both. Both unchanged complete Hypothesis methods retain max_examples5000, all internal array.example calls, assume checks and the two explicit2d examples; prototype Base/Gold each recorded5000 passing examples per method. Invalid-generation counts are preserved per run rather than forced equal. Original use_coverage=True remains enabled. Product fix is Python wrapper ravel plus changelog, with unchanged original native C source compiled and invoked. No new weighted-nd, overflow, memory-use or full floating-point coverage guarantee is claimed.

Original source159/Excel161 traces Python histogram1d to C _histogram1d and classifies Specail case handling (original spelling preserved). Actual new complete target is test_nd_arrays. Product changes are Python wrapper and changelog; native C module is compiled from unchanged original source and actually invoked.

Full upstream product patch changes CHANGES.rst and Python histogram1d/histogram2d wrappers to ravel multidimensional x/y. Native C extension remains unchanged. Exact18-line official test addition compares1000-element1d arrays with10x10x10 reshapes for both1d and2d histograms.

The same audited formal image runs exact full original methods in fixed order: fast_histogram/tests/test_histogram.py::test_1d_compare_with_numpy, fast_histogram/tests/test_histogram.py::test_2d_compare_with_numpy, fast_histogram/tests/test_histogram.py::test_nd_arrays. Gold completes all3 original methods; README-negative retains the actual measured Base behavior; protected-test-context tamper rejects as candidate_conflicts_with_test_patch. Exact raw terminal/process evidence and per-node grading are retained. Only canonical anchored complete node terminal lines are counted. Pytest collection totals do not mean the unselected methods executed.

Image yutu0814/pyc-case-160-fast-histogram:benchmark-v1. Exact complete upstream product/test patches, two-sheet workbook and full-file SHA are retained.
