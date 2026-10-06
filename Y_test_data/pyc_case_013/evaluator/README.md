# Evaluator

Build the clean Base image from `image/Dockerfile`, then evaluate candidate patches with `evaluate_model_patch.py`.

The evaluator applies the candidate patch first, then the protected official test patch. It force-rebuilds NumPy's native extensions and runs two failing parameter nodes plus two unmodified neighboring tests. The `wrap` node runs separately so Base's expected SIGFPE cannot erase the preceding regression results.

Both parameter nodes are FAIL_TO_PASS. Two unmodified neighboring tests form PASS_TO_PASS. A candidate resolves the task only when every declared test passes and the command exits successfully.
