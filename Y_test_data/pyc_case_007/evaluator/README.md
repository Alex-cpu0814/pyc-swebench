# Evaluator

Build the clean Base image from `image/Dockerfile`, then evaluate candidate patches with `evaluate_model_patch.py`.

The evaluator applies the candidate patch first, then the protected official test patch. It builds NumPy incrementally and runs two isolated pytest sessions: the new allocation-failure test with `pytest-leaks -R 3:3`, and `test_zeros` as PASS_TO_PASS without leak instrumentation.

The log parser treats pytest's `LEAKED` outcome as a failed test. A candidate resolves the task only when both declared tests pass and the test command exits successfully.
