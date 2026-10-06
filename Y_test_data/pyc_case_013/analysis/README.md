# Analysis

This directory preserves source Case 13, the verified first-parent/fix mapping,
the upstream PR trace, environment requirements, and the generated one-row workbook.

The official tests distinguish a valid empty-index operation from an invalid
non-empty index into a shape with a zero-sized axis. Base either returns an invalid
result or raises SIGFPE; Gold rejects the invalid operation with `ValueError`.
