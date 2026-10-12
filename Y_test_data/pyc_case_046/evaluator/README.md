# Evaluator

The evaluator applies the candidate patch first, then the protected official
test patch, rebuilds tskit's C extension in `python/`, and runs 2 FAIL_TO_PASS
plus 2 PASS_TO_PASS nodes. Test paths are reported from `/testbed` with the
`python/` prefix so that pytest collection and grading identify both files.

The runtime-only `pytest_no_dump.py` wrapper invokes the unchanged official
tests with pytest. It disables dumpability only for that test process. Candidate
patches, protected tests, adapter and wrapper are read-only bind mounts and are
not baked into the Base image.
