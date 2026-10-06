# Analysis

This directory preserves source Case 10, the verified first-parent/fix mapping,
the upstream PR trace, environment requirements, and the generated one-row workbook.

The source row classifies the defect as incorrect output in the Python-to-C path.
The official tests make the error concrete: when a zero-dimensional `out` array
is supplied, six methods return a scalar object instead of returning `out` itself.
Docker verification records six Base identity failures and complete Gold success.
