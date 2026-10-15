# Python-C to SWE-bench case088

Instance: pygame__pygame-0e7f7b83. Repository: pygame/pygame. Upstream issue: https://github.com/pygame/pygame/issues/180.

Base: cd173f0ebf77e2b652de1a20a5f3eccf78e8cf12. Source fix: 0e7f7b8327a18386843cf7baf4c24f07d826520e.

Base: one official bounding-rectangle method terminates with SIGABRT after pygame reports Segmentation Fault; three regressions pass. Gold: all four official methods pass.

Base completes test_copy, test_get_bytesize and test_get_rect. In the unchanged complete test_get_bounding_rect, the official added 4 by 1, 8-bit filled Surface call triggers pygame parachute Segmentation Fault at test/surface_test.py:173 and ends the child with return code -6 (SIGABRT). The wrapper records native failure and exits 1. Gold completes all four original methods with testsRun=1, wasSuccessful and normal child exits.

The full official test_get_bounding_rect method first retains existing alpha/color-key rectangle assertions, then initializes the display, creates the exact 4 by 1, 8-bit Surface, fills white and calls get_bounding_rect within the original try/finally pygame.quit. This added call asserts completion, with no new returned-rectangle assertion. Unchanged test_copy, test_get_bytesize and test_get_rect provide three regressions. Product patch changes four native bounding scans to handle 1/2/3/4 bytes per pixel with endian-aware 24-bit assembly. Only this original 8-bit failure and the complete selected methods are measured; other bit depths, endian systems and scan branches are not separately claimed.

Source case87 names surf_get_bounding_rect through test_get_bounding_rect; this complete original method is actually observed failing in the source first parent and passing with the full exact product patch. Issue180 opened2013-10-21; source fix committed2013-10-28. Associated PR lookup is empty and no merge date exists. Issue migration closure2017-03-26 is not a merge date.

Complete C product patch and complete original official test diff are preserved. The2013 project uses its own bundled unittest Revision1.63, so stdlib/pytest discovery does not recognize its TestCase class. legacy_unittest088.py loads each complete original official method with its own module.unittest.TestLoader and runs its TextTestRunner in a fresh child. A successful record requires testsRun=1, wasSuccessful and normal exit. Child stdout/stderr bytes and true return code are saved losslessly in OFFICIAL_PROCESS_RECORD; original readable output remains. SIGABRT/SIGSEGV is a target failure only after the actual official test-start record. Missing records or framework errors remain infrastructure failures. Four anchored complete test/ node terminal lines alone supply the evaluator score. No input/body/assertion/allocator/compiler flag changes.

analysis/ contains source mapping, workbook and provenance; patches/ contains exact diffs; official_swebench/ contains consistent task records and full-file SHA checksums; evaluator/ contains the clean image builder and runtime harness; verification/ contains complete raw historical/formal/control/publication evidence.

Image: yutu0814/pyc-case-088-pygame:benchmark-v1.
