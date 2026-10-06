# Evaluator

Build the clean Base image from `image/Dockerfile`, then evaluate candidate patches with `evaluate_model_patch.py`.

The evaluator applies the candidate patch first, then the protected official test patch. It force-rebuilds NumPy's native extensions and runs the selected `test_multiarray.py` nodes in one pytest session.

The six declared FAIL_TO_PASS nodes cover zero-dimensional `out` identity for `choose`, `round`, `trace`, `argmax`, `argmin`, and `take`. Three unmodified neighboring tests form PASS_TO_PASS. A candidate resolves the task only when every declared test passes and the test command exits successfully.
