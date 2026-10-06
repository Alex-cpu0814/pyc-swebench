# Verification evidence

The case was first qualified in Docker Desktop on Linux/amd64:

- Base plus official test patch: `42 failed, 921 passed`.
- Gold product patch plus official test patch: `963 passed`.
- Expected Base error: `TypeError: zoom() got an unexpected keyword argument 'grid_mode'`.

Final evaluator build and control-run artifacts are stored under `builds/` and
`runs/`. The negative control is a harmless README change. The tamper control
overlaps the protected test hunk and must be rejected before execution.
