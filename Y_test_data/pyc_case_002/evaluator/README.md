# Model evaluator

Build the configured image:

```powershell
python evaluator/build_model_evaluator.py --docker docker --build-id case-002-final-build
```

Evaluate a candidate patch:

```powershell
python evaluator/evaluate_model_patch.py `
  --docker docker `
  --patch patches/gold_patch.diff `
  --run-id case-002-final-gold
```

At runtime, a fresh immutable container verifies the Base commit and clean
working tree, applies the candidate patch, applies the protected test patch,
incrementally rebuilds SciPy, and runs the full official interpolation test
file with verbose pytest output. Structured logs use schema 3.0; see
`LOGGING.md`.
