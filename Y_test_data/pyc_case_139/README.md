# Python-C to SWE-bench case139

Instance pygobject__pycairo-65aea3df; repository pygobject/pycairo; issue https://github.com/pygobject/pycairo/issues/57. Base b780969870a9dd8b42b88c8317679e125b5e2aae; fix 65aea3dfdc5b131bc39a69ba00062f799fd72489.

Base: original device-reference target fails with cairo.Error during its10-call loop;3 unchanged regressions pass. Gold: all4 complete methods pass.

Base completes3 original regressions, then the unchanged original test_script_device_device_ref fails during its10-call surface.get_device loop with cairo.Error: <unknown error status>; actual process exit1 and terminal FAILED are preserved. No native abort happened in this measured run, and the failing iteration index is not observed. Gold completes the full original10-call method and all3 regressions normally/exit0. No added return-value/refcount observations or forced crash are claimed.

Full original9-line test_script_device_device_ref constructs BytesIO, ScriptDevice and42x10 COLOR_ALPHA ScriptSurface, deletes the dev variable, then calls surface.get_device exactly10times. It has no explicit result/refcount assertion; normal completion is the regression condition. Base fails within this original loop, with no evidence of which iteration; Gold completes the method. Three unchanged regressions retain ImageSurface.get_device is None (source-trace caller), ScriptSurface paint/flush serialized42/paint checks, and create_for_target paint with exact pixel-data equality. No full Cairo suite, measured refcount/leak guarantee, forced crash, alternative dimensions or extra iterations is claimed.

Original source138 traces surface_get_device through unchanged test_get_device; that caller exercises the None-device ImageSurface path and is retained as a P2P. The actual distinguishing F2P is original test_script_device_device_ref on a ScriptSurface; actual native outcome must be reported without claiming return-value/refcount assertions absent from this method.

Full exact2-file fix wraps cairo_surface_get_device result in cairo_device_reference before PycairoDevice_FromDevice. Complete new official9-line test performs original ten calls after deleting the original device variable.

The same audited formal image runs exact full original methods in fixed order: tests/test_device.py::test_get_device, tests/test_surface.py::test_script_surface, tests/test_surface.py::test_script_surface_create_for_target, tests/test_surface.py::test_script_device_device_ref. Gold completes all4 original methods; README-negative retains the actual measured Base behavior; protected-test-context tamper rejects as candidate_conflicts_with_test_patch. Exact raw terminal/process evidence and per-node grading are retained. Only canonical anchored complete node terminal lines are counted. Pytest collection totals do not mean the unselected methods executed.

Image yutu0814/pyc-case-139-pycairo:benchmark-v1. Exact complete upstream product/test patches, two-sheet workbook and full-file SHA are retained.
