# Analysis

Source case 65 maps to benchmark 066 and source Excel row 67. The verified first parent and exact upstream C patch are recorded in upstream_provenance.json. _imaging.c copies and releases temporary text buffers and encoded bytes references. _imagingft.c adds PyMem_Free(glyph_info) to release the getsize glyph_info array. Tests/helper.py, Tests/test_file_png.py and Tests/test_font_leaks.py form the exact official test patch. No binary assets added.

Base original unittest DefaultFont leak fails: AssertionError 1164 not less than 1024, memory usage limit exceeded in iteration 46. Gold passes this target and all three regressions. TrueType leak passes on both Base and Gold at its original 4096 KiB / 10 iteration limit, so it is PASS_TO_PASS in this environment. Normal default-font and PNG sanity tests pass on both.

Original official unittest cases execute once each in fresh subprocesses. DefaultFont uses 100 iterations and 1024 KiB, TrueType uses 10 iterations and 4096 KiB. Thresholds, loops and test bodies are unchanged. TrueType Base pass does not independently verify the FreeType leak repair in this allocator/dependency environment. The complete two-file upstream C product patch is retained. Initial pytest PNG cleanup incompatibility and DefaultFont assertion, plus the sandbox Docker permission error, remain authoring evidence.

Original source row 65 records a memory leak and a _font_getmask/test_rotated_transposed_font_get_mask chain. This original source trace is retained separately from the official font-leak test paths measured in this case.

The PR opening and merge dates are separately retained as UTC values and numeric Excel dates. Prior candidate 061 was test-only and 063 was deferred for a Windows-only official test. Their original evidence is retained.
