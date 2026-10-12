# Analysis

Source Case 53 maps to benchmark Case 054. Base c683f048eb117c572b8b4eee47a324aca165fea1 is the verified first parent of merge eb89e3a2b1833eb12124fb5f1f26f78342286143. Exact product changes add negative-radius guards to Python ImageFilter.BoxBlur and native ImagingBoxBlur. The protected patch is the unmodified upstream test_image_filter.py diff.

Untouched Base fails the official constructor check because BoxBlur(-2) does not raise ValueError; two native radius regressions pass. Complete Gold passes all three nodes. With only the exact upstream Python-layer fix, the same official test reaches filtering after radius mutation and aborts (Fatal Python error: Aborted; process exit 134). Both preceding regressions pass, but the target has no terminal pytest result (MISSING). This run establishes an abort, not a reproduced SIGSEGV.

Original source row 53 records segment fault and a BoxBlur helper path. These remain original source metadata. Untouched Base fails before native filtering; the separate Python-only official-test control reaches the native filter call and observes an abort with process exit 134. No SIGSEGV is claimed for this environment.

The GitHub REST API records PR opening at 2023-01-09T17:13:55Z and merge at 2023-01-11T21:25:10Z. Dataset dates use UTC date precision. The commit display is January 12 in +11 timezone, representing January 11 UTC; the workbook keeps opening and merge dates separately. Source: https://api.github.com/repos/python-pillow/Pillow/pulls/6874 .
