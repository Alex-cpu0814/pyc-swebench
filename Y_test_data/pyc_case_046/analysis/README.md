# Analysis

This directory preserves source Case 45, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.

On Python 3.8.20 with NumPy 1.19.5 and msprime 0.7.4, the exact Base plus official test patch produces 2 failed, 2 passed (exit 1). test_newick_large_times raises _tskit.LibraryError: Supplied buffer is too small; test_newick_interface raises TypeError: buffer_size is an invalid keyword argument. The exact upstream product patch and native rebuild yield 4 passed (exit 0).
