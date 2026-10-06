# Evaluator

Build the clean Base image from `image/Dockerfile`, then evaluate candidate patches with `evaluate_model_patch.py`.

The evaluator applies the candidate patch first, then the protected official test patch. It force-rebuilds NumPy's native extensions and runs three selected `test_multiarray.py` methods in one pytest session.

`test_searchsorted` is FAIL_TO_PASS. Two unmodified neighboring searchsorted tests form PASS_TO_PASS. A candidate resolves the task only when every declared test passes and the command exits successfully.
