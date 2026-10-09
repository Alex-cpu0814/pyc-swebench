# Python-C to SWE-bench Case 031

## Identity

- Instance ID: `numpy__numpy-ticket-925`
- Source case: `31`
- Repository: `numpy/numpy`
- Base: `b65b21c397381351965bf3f590054d2bccdd03d2`
- Fix: `a0e082a087e9667e3805d3be859958a292e8f336`
- Upstream PR: <https://github.com/numpy/numpy/commit/a0e082a087e9667e3805d3be859958a292e8f336>

## Verified relation

Base raises ValueError in 2 broadcasting targets; Gold passes both targets and the basic regression. 1 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-031-numpy:benchmark-v1`.
