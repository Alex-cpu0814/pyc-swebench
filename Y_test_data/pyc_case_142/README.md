# Python-C to SWE-bench case142

Instance pygobject__pycairo-07ee64b3; repository pygobject/pycairo; issue https://github.com/pygobject/pycairo/issues/41. Base cd6b840aeab1515343a71a997b0a2ce48fce6d82; fix 07ee64b3fb51a16ded90822a0fb00cb8b180b839.

Base: original get_data refcount target FAILED (3 !=2 after del d),3 regressions PASSED. Gold: all4 complete methods PASSED.

Base passes3 complete unchanged regressions and the first2 original refcount assertions. After del d, complete original test_image_surface_get_data_refcount fails its final assertion: actual3 versus expected2 (tests/test_surface.py:20), terminalFAILED and process exit1. Gold satisfies the exact original2→3→2 sequence and all3 regressions, process exit0. No substituted counts, offsets, forced garbage collection, extra loops or modified object lifetimes.

Complete original7-line test_image_surface_get_data_refcount creates a10x10 ARGB32 ImageSurface, asserts getrefcount2, obtains get_data memoryview and asserts3, deletes that view and asserts2. All original dimensions, local lifetimes and assertions remain exact. Base observes2→3→3 and fails at the final assertion; Gold passes2→3→2. Unchanged complete tests verify surface Content enum, Format enum, and PNG BytesIO roundtrip including exact pixel-data equality. This is the selected surface/view lifetime check, not a general memory-use or full-suite guarantee.

Original source141/Excel143 traces image_surface_get_data to test_image_surface_get_data_refcount, classifies a memory leak and reference count misuse. Preserve original trace and taxonomy separately from actual measured assertion and runtime.

Complete5-file native/build product change introduces a bufferproxy object holding the surface exporter and uses it to produce memoryviews. The exact original test patch imports sys and adds the complete7-line refcount method with10x10 surface and exact2→3→2 counts.

The same audited formal image runs exact full original methods in fixed order: tests/test_surface.py::test_surface_get_content, tests/test_surface.py::test_surface_get_format, tests/test_surface.py::test_image_surface_png_obj_roundtrip, tests/test_surface.py::test_image_surface_get_data_refcount. Gold completes all4 original methods; README-negative retains the actual measured Base behavior; protected-test-context tamper rejects as candidate_conflicts_with_test_patch. Exact raw terminal/process evidence and per-node grading are retained. Only canonical anchored complete node terminal lines are counted. Pytest collection totals do not mean the unselected methods executed.

Image yutu0814/pyc-case-142-pycairo:benchmark-v1. Exact complete upstream product/test patches, two-sheet workbook and full-file SHA are retained.
