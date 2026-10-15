# Python-C to SWE-bench case 082

Instance: pygame__pygame-804. Repository: pygame/pygame. Upstream: https://github.com/pygame/pygame/pull/804.

Base: 8a63c06f2e082b8c7e3c0fce035a0a7e4ca55d85. Fix: 20ff3f8e021d207b6053dd98eadf606c1eb8f451.

Base: two official event targets fail and two regressions pass. Gold: all four official nodes pass.

Complete official test_get_type posts one USEREVENT, retrieves it by numeric type and checks list length 1 and matching type. test_peek_empty clears the queue and asserts peek() is false. Existing test_get posts ten user events; test_peek checks three populated event types and their sequence. Tests run against SDL2 2.0.14 under X11. SDL1 code changes and get(type) sequence/invalid-type cases are not directly covered. No new custom inputs or assertion changes.

Source case 81 records incorrect result/output and a pg_event_get native trace ending in gen_stubs.get_callables. The measured regression executes official EventModuleTest get(type) and empty peek functions; the source stub-generation caller is not claimed as reproduced.

Complete native C product and official Python test patches are preserved. Pinned pygame 1.9.5.dev0 / SDL2 2.0.14 runs under Xvfb/X11 with an audited local native extension. Uninitialized empty-peek event numbers are not fixed expectations. analysis/ contains source mapping, workbook and provenance; patches/ holds exact upstream diffs; official_swebench/ holds task records and checksums; evaluator/ holds clean recipe/runner; verification/ holds complete logs and publication evidence.

Image: yutu0814/pyc-case-082-pygame:benchmark-v1.
