# Python-C to SWE-bench case137

Instance pygobject__pycairo-065a7a7a. Repository pygobject/pycairo. Issue https://github.com/pygobject/pycairo/issues/50.

Base 9ebff889d4c68927ab1c152b6ae7c8327283b6ed. Fix 065a7a7aed9e5523dcbf41568d89e94fc0af44b9.

Base:3 regressions pass, complete official device-scale target starts then native aborts(exit134; no terminal target status). Gold:all4 complete methods pass normally.

Ordinary Base completes3 regressions, begins complete official tests/test_surface.py::test_surface_set_device_scale, then native process aborts; Docker process exit134 and original bash Aborted record are preserved. No target terminal FAILED/PASSED line exists, so canonical scorer status is MISSING rather than a fabricated failure line. The upstream issue reports Cairo matrix assertion; this run preserves actual abort but does not invent an assertion message absent from stderr. Gold completes all4 full methods with normal exit0, including exact100x100ARGB32 scale(1,0) raising cairo.Error.

Complete test_surface_set_device_scale retains existing10x10ARGB32 surface scale(5.0,3.0) call and ret-is-None assertion, then creates exact100x100ARGB32 surface and expects cairo.Error for scale(1,0). Base reaches target execution but abort prevents complete method return; no intermediate terminal completion is claimed. Gold completes all original assertions. Three unchanged complete regressions test get_device_scale tuplefloat values, get_content enum and get_format enum. No full Cairo suite, arbitrary negative/nonfinite input, alternate dimensions/platforms or internal downstream Cairo assertion text absent from raw logs is claimed.

Original source136 names native surface_set_device_scale through exact test_surface_set_device_scale; selected target is this complete original method with its existing valid-scale assertions and exact new invalid-scale check. Actual native failure behavior will be reported from logs; no independent coverage of arbitrary nonfinite/negative/matrix inputs is claimed.

Original complete pytest functions execute in fixed order: get_device_scale, get_content, get_format, then set_device_scale. Base/protected README-negative complete three P2P terminal PASSED lines and actually start the target before native abort134. The scorer correctly records F2P MISSING because no terminal status exists. Formal outer container exit1 means unresolved; phase.test_exit_code retains the actual test134. Gold completes all4methods/exit0. Parser accepts anchored complete file::function terminal lines only; no target FAILED line or downstream Cairo assertion text is invented. Pytest collection may count other discoverable items, but only the exact selected four functions run.

Eight earlier candidates are preserved under analysis/prior_candidate_reviews with original complete patches, source rows, raw evidence, dependency/authoring history and their frozen inner SHA manifests. Cases106/107/111/113 are native platform deferrals;114 repairs an alternate branch not compiled in the measured toolchain, with full preprocessor proof;128/132/134 preserve original Gold memory-decorator failures and are not claimed as admitted. Original CRLF/raw bytes remain intact and are also covered by the outer manifest. Current137 prototype/build/controls succeeded without repeating successful probes or altering any official methods.

Image yutu0814/pyc-case-137-pycairo:benchmark-v1. Exact upstream patches, two-sheet workbook, full-file SHA and formal native/process/control evidence are preserved.
