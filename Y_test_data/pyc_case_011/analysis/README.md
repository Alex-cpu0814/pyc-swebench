# Analysis

This directory preserves source Case 11, the verified first-parent/fix mapping,
the upstream PR trace, environment requirements, and the generated one-row workbook.

The official test supplies the documented `v` keyword. Base incorrectly asks for
`keys` and raises a concrete TypeError; Gold accepts `v` and preserves neighboring
searchsorted behavior.
