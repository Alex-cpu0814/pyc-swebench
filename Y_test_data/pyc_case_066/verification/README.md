# Verification evidence

Final Gold: four official nodes passed. README-only negative: DefaultFont assertion1160 >=1024 KiB at iteration46; the three other nodes pass. Protected PNG test-import tampering is rejected with candidate_conflicts_with_test_patch before build/grading. All formal controls use the identical unittest runner mounted into a clean Base image.

Original official unittest cases execute once each in fresh subprocesses. DefaultFont uses 100 iterations and 1024 KiB, TrueType uses 10 iterations and 4096 KiB. Thresholds, loops and test bodies are unchanged. TrueType Base pass does not independently verify the FreeType leak repair in this allocator/dependency environment. The complete two-file upstream C product patch is retained. Initial pytest PNG cleanup incompatibility and DefaultFont assertion, plus the sandbox Docker permission error, remain authoring evidence.

Prototype Base-v3 and Gold-v3 are stored as probes/base and probes/gold. Initial pytest collection/base logs, incompatible PNG cleanup exception, default-font assertion1036 >=1024 KiB at iteration30, sandbox Docker API permission error and initial inherited NumPy audit failure are retained separately. The NumPy audit was corrected to verify native Pillow4.3.0.dev0. No infrastructure error is graded as a product failure.

Every final official node runs once in a fresh subprocess. Runner logs exact node, returncode and signal plus the original unittest output. It disables core dumps within each executed worker. Tests use upstream thresholds and iteration counts without warm-up or instrumentation. Formal runtime audit verifies local compiled PIL modules, FreeType2.10.4, native source hashes and the original FreeMono.ttf blob/SHA256. SHA256SUMS covers all retained raw evidence and final assets.
