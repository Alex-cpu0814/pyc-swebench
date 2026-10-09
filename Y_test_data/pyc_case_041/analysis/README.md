# Analysis

This directory preserves source Case 40, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.

On linux/amd64, Base passes both neighboring regressions and then aborts in the official test_splprep_segfault sequence, followed by a segmentation fault. The one-line C fix and native rebuild make the same three nodes pass.
