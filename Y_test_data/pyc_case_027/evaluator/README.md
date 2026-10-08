# Evaluator

The evaluator applies the candidate patch first, then the protected official test patch, force-rebuilds NumPy's native extensions, and runs 1 FAIL_TO_PASS plus 2 PASS_TO_PASS nodes.
