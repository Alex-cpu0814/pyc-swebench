# Python-C to SWE-bench case094

Instance pygame__pygame-c7ec1528. Repository pygame/pygame. Issue https://github.com/pygame/pygame/issues/93.

Base 2d7786bc2453561a696281299104f95814e676b3. Source fix c7ec15285c23ce54f466c9a3482b4d087eb8b0ff.

Base: complete official oversized-blend method fails with a native signal; initial run also records wrong returned-Rect assertion. Three regressions pass. Gold: all four complete methods pass with normal exit.

Initial ordinary Base target reports test/surface_test.py:1540 AssertionError: <rect(1,1,3,3)> != <rect(1,1,30,30)>, testsRun1/failures1/errors0, then childSIGSEGV(-11). Correctly classified Base-v2 target starts the same complete original method and terminatesSIGABRT(-6), stderr free(): invalid size, before a final result record. Original heap-failure timing differs naturally; no allocator/compiler/input edits. Both Base runs preserve3 regression passes. Gold completes all4 methods with normal exit0. Base initial first-return-rectangle failure prevents later pixel/subsurface assertions; no Base outcome for later assertions is claimed.

Complete official test_blit_blend_big_rect first additive-fills32-bit4x4 Surface with color(1,2,3,255), area(1,1,30,30), and asserts returned Rect(1,1,3,3) plus two pixels. It then checks black/red differ and, on a10x10 parent with10x8 subsurface at(0,1), verifies parent top/bottom pixels stay black after fills at(0,-1,10,1) and(0,8,10,1). Initial Base stops at the first Rect assertion; repeat Base aborts during that started method. Gold completes every original assertion. Three unchanged full copy/get_bytesize/get_rect methods pass both. No full surface suite, original transform caller failure, full directional clipping coverage, other bit-depth/platform coverage or timing guarantee is claimed.

Original source case93 traces surf_fill to test_threshold__honors_third_surface in transform_test.py. The actually selected failing candidate is the complete newly added official SurfaceBlendTest.test_blit_blend_big_rect; no failure of the original transform caller is claimed. Source commit is a two-parent merge; Base is actual first parent, and its complete diff has only src/surface.c and test/surface_test.py. Original source taxonomy remains Python-C; source-row broad test-file trace is not the set of files changed by this merge.

Complete C product patch and complete official36-line test addition are preserved byte-for-byte. Original bundled unittest TestLoader loads one complete method per fresh child; TextTestRunner determines true testsRun/wasSuccessful. PASSED requires a successful single-method result and normal exit. A real SIGSEGV/SIGABRT after OFFICIAL_TEST_START is FAILED even after a failed result was emitted; full result/stdout/stderr/signal/true returncode are preserved losslessly. Other unexpected/missing results remain ERROR. Canonical anchored full node terminal lines alone are scored, so human-readable aliases are never double-counted.

analysis/ preserves source/workbook/provenance, patches/ exact diffs, official_swebench/ consistent tasks/full-file SHA, evaluator/ clean public image/runtime harness, verification/ full prototype/formal/control/publication evidence. Image yutu0814/pyc-case-094-pygame:benchmark-v1.
