# Verification

Final Base and README-only negative fail exactly the official rotation metrics assertion, with three regression passes. Gold passes all four official nodes and all three size/rotation/oblique comparisons. Protected-test context tampering is rejected as candidate_conflicts_with_test_patch before build. Missing or skipped nodes cannot pass.

Official test_issue_565 creates a fresh test_sans.ttf Font at size 24 for each unchanged pipe-text comparison, in original size 36, rotation 90, oblique=True order. Base fails at rotation; Gold completes all three. Three unchanged official regressions exercise default-font size, scalable and fixed-width properties. Six tracked setUp fonts plus tracked packaged freesansbold.ttf are audited. The test module uses X11; pytest directly executes its unittest methods, while dummy ignore tags belong to the pygame project runner. Undefined-character behavior from the source trace is not claimed.

First exploratory Base/Gold default-font failures are packaging infrastructure, not extra product failures. Resource-complete Base/Gold retain exactly the same four official nodes. The separate Docker RPC EOF run did not reach the resource-copy/native-build stage. Full logs and original build-only recipe are preserved. Actual source/destination default-font bytes, all six original fixtures, native module/version/path and FreeType/SDL versions are audited.

The clean image contains only public pinned Base source/dependencies and tracked font data. Candidate, Gold/protected-test patches and evaluator runtime assets are absent. All normal force-build output is first buffered in Linux/tmp and copied verbatim into raw logs, preserving failure exit code before fixed font resource materialization. No custom assertions, warm-up, instrumentation or retries seeking chance passes. All saved records/workbook previews/helpers/logs and prior078 archive are covered by unique full-file SHA256 entries.

## Publication status

Publication is pending: formal verification and workbook checks passed, but Docker Desktop currently fails during sailor-ingest socket startup. Neither the 081 Docker Hub push nor Git remote push has been performed. The verified image and all original evidence are retained; cleanup waits until publication succeeds.
