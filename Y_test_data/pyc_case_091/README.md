# Python-C to SWE-bench case091

Instance: pygame__pygame-95bf5012. Repository: pygame/pygame. Upstream issue: https://github.com/pygame/pygame/issues/243.

Base: e26f569b1f3e28d935327b7dfc4cb10e722a9d09. Source fix: 95bf50120604bf9367f2df043d57f7fda81d49ba.

Base: complete official issue243 fails its first one-space width assertion; three regressions pass. Gold: all four complete official methods pass, including one-space/two-space widths and the upstream-modified issue242.

Base complete official test_issue_243 stops at its first assertion in test/freetype_test.py:1351: self.assertTrue(r1.width > 1), AssertionError: None, child exit1, testsRun1/failures1/errors0. Its later two-space assertions are not reached on Base. Gold completes the original one-space and two-space boundary assertions. The three complete get_rect, mono-render and issue242 regression methods pass both; issue242 includes the exact upstream two-space to one-space underline-input change.

Complete original test_issue_243 uses self._TEST_FONTS[fixed] at size64, calls get_rect for one space and asserts width>1, then calls get_rect for two spaces and asserts twice the one-space width. Base stops at the first width assertion; Gold completes both assertions. Three complete official regression methods cover get_rect geometry, monochrome rendering, and all four issue242 style comparisons. The complete upstream test patch modifies issue242 underline input from two spaces to one. Official test bodies/inputs/assertions and Base font fixtures are preserved exactly as upstream. No full freetype suite, independent Base failure of the later two-space assertion, crash, or other fonts/platforms is claimed.

Source case90 traces position_glyphs through _PGFT_LoadLayout, _PGFT_GetTextRect and _ftfont_getrect to test_freetype_Font_resolution. Actual selected target is the exact newly added official test_issue_243; no failure of the original resolution caller is claimed. Full product patch includes native layout change and documentation edit; complete test patch includes upstream issue242 two-space to one-space edit. Issue243 opening and source UTC date are2015-04-14, separately from local commit2015-04-13; no migrated closure is a merge date.

Complete native src/freetype/ft_layout.c and docs/reST/ref/freetype.rst product changes plus complete official test patch are preserved byte-for-byte. Original bundled unittest Revision1.63 TestLoader selects each complete official TestCase method and checks suite count1. TextTestRunner supplies true testsRun/wasSuccessful outcomes in separate children; stdout/stderr bytes and returncodes are preserved losslessly in OFFICIAL_PROCESS_RECORD. Scoring accepts exactly four anchored full test/freetype_test.py terminal node lines and excludes duplicate human-readable unittest aliases. Missing/error/skipped expectations do not resolve.

analysis/ preserves source/workbook/provenance; patches/ exact diffs; official_swebench/ consistent tasks/full-file SHA; evaluator/ clean public image/runtime harness; verification/ original prototype/formal/control/publication evidence. Image: yutu0814/pyc-case-091-pygame:benchmark-v1.
