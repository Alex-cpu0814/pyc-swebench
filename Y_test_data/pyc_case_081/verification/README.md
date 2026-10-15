# Verification

Final Base and README-only negative fail exactly the official rotation metrics assertion, with three regression passes. Gold passes all four official nodes and all three size/rotation/oblique comparisons. Protected-test context tampering is rejected as candidate_conflicts_with_test_patch before build. Missing or skipped nodes cannot pass.

Official test_issue_565 creates a fresh test_sans.ttf Font at size 24 for each unchanged pipe-text comparison, in original size 36, rotation 90, oblique=True order. Base fails at rotation; Gold completes all three. Three unchanged official regressions exercise default-font size, scalable and fixed-width properties. Six tracked setUp fonts plus tracked packaged freesansbold.ttf are audited. The test module uses X11; pytest directly executes its unittest methods, while dummy ignore tags belong to the pygame project runner. Undefined-character behavior from the source trace is not claimed.

First exploratory Base/Gold default-font failures are packaging infrastructure, not extra product failures. Resource-complete Base/Gold retain exactly the same four official nodes. The separate Docker RPC EOF run did not reach the resource-copy/native-build stage. Full logs and original build-only recipe are preserved. Actual source/destination default-font bytes, all six original fixtures, native module/version/path and FreeType/SDL versions are audited.

The clean image contains only public pinned Base source/dependencies and tracked font data. Candidate, Gold/protected-test patches and evaluator runtime assets are absent. All normal force-build output is first buffered in Linux/tmp and copied verbatim into raw logs, preserving failure exit code before fixed font resource materialization. No custom assertions, warm-up, instrumentation or retries seeking chance passes. All saved records/workbook previews/helpers/logs and prior078 archive are covered by unique full-file SHA256 entries.

## Publication status

The exact verified image was successfully pushed to Docker Hub after Docker Engine recovered. Digest: sha256:4e5d69e396505fea954f28acb59dc90ef522bafab05dd484c0299e628f938720. Original startup failures and the data-preserving recovery are retained under verification/publication. Git remote confirmation and final cleanup are recorded in the batch progress after the source commit is published.
