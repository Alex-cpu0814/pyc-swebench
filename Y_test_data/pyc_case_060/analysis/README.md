# Analysis

Source Case 59 maps to benchmark Case 060, spreadsheet row 61. Base d0612030a0ba7aed533e1f9115bbf4bd1019f48e is the verified first parent of merge 9a683db33945aacf2fa9a277f680e29d54685930. Product changes are confined to native C src/libImaging/Fill.c: 8-bit storage retains byte writes, I uses INT32 pixels and F uses FLOAT32 pixels for linear/radial gradients. The exact protected upstream Tests/test_image.py patch extends both mode loops from L/P to L/P/I/F. Existing reference PNGs are unchanged.

On Base, both official linear_gradient and radial_gradient test subprocesses terminate with SIGSEGV (returncode -11) at the I-mode call after their L/P iterations. The isolated runner records each signal and reports two node failures, aggregate exit 1; both unchanged RGB wrong-mode ValueError regressions pass. Gold-v2 passes all four unchanged official nodes, including I/F reference-pixel checks. The first Gold attempt timed out before the first wrong-mode result; it remains separate infrastructure evidence and is not a product failure. The product fix changes native C Fill.c storage writes.

The exact upstream linear/radial tests loop L, P, I and F, compare generated pixels against existing PNG references and check key pixels/modes. Base terminates at I, so F is not reached on Base; Gold verifies both I and F. Two unchanged RGB wrong-mode nodes preserve ValueError behavior. Official test logic is unmodified. Each node runs in a separate subprocess; native SIGSEGV is recorded as process failure rather than an assertion, aggregate exit 1 permits complete node grading. The product patch changes C Fill.c only; no binary asset changes.

Original source row 59 records segment fault (crash) and a mixed ImagingFillLinearGradient/ImagingError/ImagingTransform/_transform2/Python __transformer chain. This is preserved source metadata. Actual official stacks enter Image.linear_gradient/radial_gradient and terminate with SIGSEGV in Base; the unrelated transform chain is not this runtime trace.

PR opening 2021-02-19T08:12:52Z and merge 2021-03-28T13:35:22Z are separately recorded UTC dates. Source: https://api.github.com/repos/python-pillow/Pillow/pulls/5274.
