# Analysis

Original source158 / Excel row160; source classification and trace retained separately from measured target scope.

Base passes3 complete unchanged regressions. Complete original test_mixed_strides reaches its weighted1d result_3/result_4 exact NumPy comparison and fails with arrays not equal at tests/test_histogram.py:224, terminalFAILED/process exit1. It passes the preceding shape/stride assertions and unweighted1d comparison, but does not reach the later2d comparisons. Gold completes all original comparisons plus3 regressions,4PASSED/exit0. Random samples and original shapes/slices/assertions remain unchanged; no fixed seed, extra sampling loop or compiler/allocator change.

Full original test_mixed_strides constructs the exact random arrays/slices from shapes(30,20,40,50),(30,40,50),(30,10,5,80,90), yielding matching shapes and pairwise distinct strides. It retains all shape/stride checks and exact NumPy comparisons for unweighted1d, weighted1d, unweighted2d and weighted2d. Base stops at weighted1d; Gold reaches and passes all4 paths. Complete unchanged test_nd_arrays, test_list and test_non_contiguous cover multidimensional reshaping, list conversion, and all4 histogram paths with equally strided noncontiguous inputs versus copies. No parameterized Hypothesis test or full suite executed; import-time Hypothesis presence is not a claim of running its500 examples.

Original source158/Excel160 traces native _histogram2d through Python histogram2d to a recorded py_velodyne test_mixed_strides caller. Preserve the original trace/module labels and taxonomy separately from the measured complete official fast_histogram/tests/test_histogram.py::test_mixed_strides function.

Full upstream product patch updates separate iterator strides in unweighted2d and weighted1d/2d native loops plus CHANGES.rst. Exact29-line official test addition preserves original random arrays and compares all4 histogram paths to NumPy.

Created at is actual PR52 opening 2020-05-24T15:49:13Z; merged at is actual PR52 merge 2020-05-24T16:51:01Z. Source commit time 2020-05-24T17:51:01+01:00 is separate provenance.

Actual fast-histogram0.8, CPython3.6.15, NumPy1.15.4, pytest5.4.2 and hypothesis5.16.0; original Azure Linux py36/numpy115 supported environment family. Exact pinned public Python3.6.15-buster and pinned public build/test dependencies, ordinary GCC8.3 original setup.py native build. Genuine upstream v0.8 tag equals Base, used for original setuptools_scm derivation; generated version is excluded from tracked source. Native module path/hash, NumPy header/runtime ABI, all original source blobs and actual dependency versions audited. No test dimensions, slices, random seed, assertions, sampling counts, compiler or allocator changes.
