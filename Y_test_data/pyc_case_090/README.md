# Python-C to SWE-bench case090

Instance: pygame__pygame-4c23a6ce. Repository: pygame/pygame. Upstream issue: https://github.com/pygame/pygame/issues/242.

Base: 6e5ca4a046fde6c21b0386281e25a83b3c8f9ba3. Source fix: 4c23a6ce02e4fa25ee62ba3d996106dcfd7d3cd4.

Base: official issue242 fails the first wide-M rectangle comparison; three regressions pass. Gold: all four complete official methods pass, including the four style comparisons.

Base test_issue_242 fails its first wide-style M comparison at test/freetype_test.py:1286: get_rect returns <rect(5,44,44,44)> while render returns <rect(5,44,46,44)>. The complete original method stops at this first assertion, so later strong/oblique/underline steps are not observed on Base. Gold completes all four original style comparisons. Three unchanged get_rect, style-property and mono-render regressions pass both versions; each official method has testsRun=1 with true child exit and wasSuccessful outcome.

Complete original test_issue_242 at size64 sets wide=True for M, strong=True for Mm_, oblique=True for | and underline=True for two spaces, comparing get_rect to render(None) and restoring each property in finally. Base fails first wide-M equality only; Gold executes all four style blocks. Three complete original regression methods test explicit/default get_rect geometry, Font.style validation/assignment, and monochrome rendering. Official source fonts and all original inputs/assertions/bodies remain unchanged. No full freetype suite, independent failures of later style blocks, crash or other fonts/platforms are claimed.

Source case89 traces _ftfont_getrect via _ftfont_get to test_freetype_Font_resolution. The measured failing caller here is the exact newly added official test_issue_242; no failure of the original resolution caller is claimed. Pinned source first parent is verified. Issue242 opened2015-04-07; source commit UTC2015-04-08 is not an inferred merge date, and no associated merge is claimed.

Complete one-line native product fix and complete60-line official test addition are preserved byte-for-byte. Original bundled unittest Revision1.63 TestLoader selects each complete official TestCase method and checks suite count1. TextTestRunner supplies true testsRun/wasSuccessful outcomes in separate children; stdout/stderr bytes and returncodes are preserved losslessly in OFFICIAL_PROCESS_RECORD. The scorer accepts exactly four anchored full test/freetype_test.py node terminal lines and excludes duplicate human-readable unittest aliases. Missing/error/skipped expectations do not resolve. No stdlib unittest replacement or assertion-body extraction is used.

analysis/ holds source/workbook/provenance, patches/ exact diffs, official_swebench/ consistent tasks/full-file SHA, evaluator/ clean public image/runtime harness, verification/ full original historical/formal/control/publication evidence. Image: yutu0814/pyc-case-090-pygame:benchmark-v1.
