# Analysis

This directory preserves source Case 22, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.

On the unpatched Base, 3 parameterizations fail because the float64 dtype reference count drops by one (for example, ACTUAL 67 versus DESIRED 66), followed by CPython debug-build 'Reference count error detected' messages.
