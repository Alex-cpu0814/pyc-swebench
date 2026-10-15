# Verification evidence

Prototype Base and the formal README-only negative control fail only the official loops timer API node. Prototype and formal Gold pass all four nodes. Protected-test tampering changes exact upstream hunk context and is rejected as candidate_conflicts_with_test_patch before build/grading.

Official test_set_timer preserves eight events at 100 ms intervals with a 50 ms tolerance, stops via millis=0, checks loops=True for one event, and checks loops=3 for plain custom, attributed custom and KEYDOWN event objects. Selected event regressions cover a 1024-character user payload, type-filtered retrieval including the upstream added ten-event sequence, and blocked-post boolean/event behavior. Complete two-file upstream protected patch is unchanged. Native event batching performance, RWops close handling and every window constant are not individually claimed as tested defects.

The target uses original timer intervals and event counts, including the 50 ms tolerance. Formal Gold/negative repeat the same official assertions and environment. Base reaches the loops keyword call and raises TypeError, rather than timing or display initialization failure. Three event regressions pass on Base and Gold under the complete original protected patch. No skip or missing status is treated as a pass.

Normal pytest runs the official unittest TestCase methods directly. Core dumps are disabled, with no instrumentation, warm-up or isolated retry of timing assertions. Runtime assets and candidate/test/gold patches are mounted only into evaluation containers. Published clean Base source is unmodified and the fix object is absent. All raw logs, helpers, exact source evidence, workbook checks/previews and prior074 deferral are covered by unique SHA256 entries.

Initial formal Gold/negative runs produced the correct test results but exceeded the 600-second overall timeout while direct build logging took about 598-600 seconds. These are preserved as initial-*-timeout infrastructure runs and are not counted as resolved. Buffering all compiler stdout/stderr in container /tmp then copying it verbatim to /results reduced formal build time to about 64 seconds, preserving the original compiler flags and exact build exit code. Final Gold/negative complete in about 68 seconds; tamper rejects before build.

Original captured API/cleanup JSON metadata and raw logs retain their exact recorded bytes via explicit -text attributes. Authored artifacts and checksum manifests use LF. This preserves the independent074 archive hashes and committed-blob correspondence.
