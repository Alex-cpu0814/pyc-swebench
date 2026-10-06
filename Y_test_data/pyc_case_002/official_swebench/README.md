# SWE-bench-compatible records

- `instance_002.json` is the private evaluator record and includes the product
  patch, protected test patch, FAIL_TO_PASS, and PASS_TO_PASS lists.
- `instance_002.jsonl` contains the same record as one JSONL line.
- `public_task_002.json` omits the answer and protected tests.
- `metadata.json` records provenance, deduplication, trace evidence, and runtime
  verification.

The declared PASS_TO_PASS list contains 100 deterministic representative tests
to keep portable records compact. The evaluator still runs all 963 tests in
the official test file and rejects any unexpected failure.
