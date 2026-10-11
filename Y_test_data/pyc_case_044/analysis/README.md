# Analysis

This directory preserves source Case 43, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.

The untouched first-parent Base with the exact upstream test patch passes test_map_coordinates01 and test_map_coordinates02, then test_map_coordinates_large_data terminates with Segmentation fault (exit 139). Applying the four-file upstream product patch and rebuilding yields 3 passed on Python 3.6.15 / NumPy 1.17.5.
