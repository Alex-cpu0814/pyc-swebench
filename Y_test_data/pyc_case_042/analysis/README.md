# Analysis

This directory preserves source Case 41, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.

On linux/amd64, Base passes both neighboring spline regressions but test_sepfir2d_invalid_filter fails because the even-length filter calls do not raise ValueError. Applying the C fix and rebuilding the native extension makes the target and both regressions pass.
