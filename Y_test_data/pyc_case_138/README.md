# Python-C to SWE-bench case138

Instance pygobject__pycairo-42eb8a30; repository pygobject/pycairo; issue https://github.com/pygobject/pycairo/issues/48. Base afee8cfba448e8c6c100afc6015d31c6aa37e172; fix 42eb8a30f57676e74a194be297d051f457cebf23.

Base: original raster-source test fails at missing API (AttributeError),3 unchanged regressions pass. Gold: all4 complete original methods pass.

Base fails at the first cairo.RasterSourcePattern(cairo.Content.COLOR,2,2) constructor lookup with AttributeError because this API is absent. No callback call or callback crash is reached on Base. Gold completes the full original test_raster_source and all3 unchanged regressions, normal exit0. Original source taxonomy says crash, but this measured admission establishes missing API support, not reproduction of its historical crash trace.

Full original test_raster_source constructs a2x2 COLOR pattern, checks instance/subclass identity, tests all4 set/get acquire/release combinations, paints a10x10ARGB32 surface to assert acquire then release ordering, and checks two invalid callback objects raise TypeError. Acquire creates the original requested-size similar image, sets original extents offset and paints red. Base stops at initial missing constructor and never reaches these later assertions; Gold completes every original assertion. Three unchanged methods test pattern equality/inequality, default extend type/value and default filter. No full Cairo suite, historical callback crash, leak/refcount guarantee, arbitrary dimensions or alternative error paths is claimed.

Original source137 taxonomy says crash and traces PycairoPattern_FromPattern through pycairo_get_source to unchanged test_cmp_hash. Preserve this source trace and include test_cmp_hash as a regression. The admitted distinguishing target is upstream newly added test_raster_source; if Base lacks the API, report that first constructor AttributeError rather than claiming an existing callback crash or a reproduced source-trace crash.

Complete upstream6-file diff is preserved:5 product files (NEWS, cairo/cairomodule.c, cairo/pattern.c, cairo/private.h, docs/reference/patterns.rst) and tests/test_pattern.py. Original product documentation and callback signatures are unchanged, including any upstream documentation/code differences. Added API and callback support is the measured fix; selected passing method does not prove all upstream paths.

All controls use the one audited formal image and exact original four-node order: test_raster_source, test_cmp_hash, test_get_extend, test_get_filter. Gold4PASS/exit0; README-only negative target FAILED at constructor AttributeError plus3P2P PASS/exit1; protected-test-context tamper rejected as candidate_conflicts_with_test_patch. Parser counts only canonical anchored complete file::function terminal lines. Other44 discovered file items do not mean44 methods executed.

Image yutu0814/pyc-case-138-pycairo:benchmark-v1. Exact patches, two-sheet workbook, full-file SHA and all native/process/control evidence are retained.
