# Analysis

Original source141 / Excel row143; source classification and trace retained separately from measured target scope.

Base passes3 complete unchanged regressions and the first2 original refcount assertions. After del d, complete original test_image_surface_get_data_refcount fails its final assertion: actual3 versus expected2 (tests/test_surface.py:20), terminalFAILED and process exit1. Gold satisfies the exact original2→3→2 sequence and all3 regressions, process exit0. No substituted counts, offsets, forced garbage collection, extra loops or modified object lifetimes.

Complete original7-line test_image_surface_get_data_refcount creates a10x10 ARGB32 ImageSurface, asserts getrefcount2, obtains get_data memoryview and asserts3, deletes that view and asserts2. All original dimensions, local lifetimes and assertions remain exact. Base observes2→3→3 and fails at the final assertion; Gold passes2→3→2. Unchanged complete tests verify surface Content enum, Format enum, and PNG BytesIO roundtrip including exact pixel-data equality. This is the selected surface/view lifetime check, not a general memory-use or full-suite guarantee.

Original source141/Excel143 traces image_surface_get_data to test_image_surface_get_data_refcount, classifies a memory leak and reference count misuse. Preserve original trace and taxonomy separately from actual measured assertion and runtime.

Complete5-file native/build product change introduces a bufferproxy object holding the surface exporter and uses it to produce memoryviews. The exact original test patch imports sys and adds the complete7-line refcount method with10x10 surface and exact2→3→2 counts.

Created at is actual PR42 opening 2017-05-31T19:16:01Z; merged at is PR merge 2017-05-31T19:35:43Z. Issue41 opening 2017-05-31T14:33:57Z and Git commit timestamp 2017-05-31T21:35:42+02:00 are distinct provenance dates.

Actual pycairo1.13.3, CPython3.6.15, pytest3.0.7/py1.4.34 and unmodified GCC8.3. Exact pinned public Python3.6.15-buster base already includes normal Cairo1.16.0 headers/runtime and development libraries. Ordinary upstream setup.py builds cairo._cairo in place on Base/Gold with identical metadata. Source Git blobs, module path/hash, generatedconfig.h, package versions and linked/header versions are audited. No test input/assertion/helper, compiler, allocator or instrumentation changes.
