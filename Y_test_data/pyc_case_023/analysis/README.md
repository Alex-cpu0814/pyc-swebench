# Analysis

This directory preserves source Case 23, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.

On the unpatched Base, the official empty-values assertion reaches ValueError: Cannot insert from an empty array!, then array_dealloc emits an ignored exception and CPython aborts with 'Fatal Python error: a function returned NULL without setting an error' and SystemError from _insert.
