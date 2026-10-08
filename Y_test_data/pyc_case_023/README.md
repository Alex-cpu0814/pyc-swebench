# Python-C to SWE-bench Case 023

## Identity

- Instance ID: `numpy__numpy-12814`
- Source case: `23`
- Repository: `numpy/numpy`
- Base: `70b773e4015b4fbb61bc1f7bdffc9cc789d58e94`
- Fix: `74f3d07ab0bcfd63f42f62b26eeb6ce68efd4f21`
- Upstream PR: <https://github.com/numpy/numpy/pull/12814>

## Verified relation

Base: the official target aborts with a fatal NULL-without-error/SystemError trace; Gold: the target passes. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-023-numpy:benchmark-v1`
with image ID `sha256:8b841335373b60b3e3aa4c1cb856876881e173ce982971adaf302df454690fdf`.
