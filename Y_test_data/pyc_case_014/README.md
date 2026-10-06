# Python-C to SWE-bench Case 014

## Identity

- Instance ID: `numpy__numpy-14393`
- Source case: `14`
- Repository: `numpy/numpy`
- Base: `495d352bf325f44d78001f059d625123e49f027e`
- Fix: `f786041db9697f58b087e18198561db8b28235c4`
- Upstream PR: <https://github.com/numpy/numpy/pull/14393>

## Verified relation

Base: ValueError not raised by view; Gold: target passed. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-014-numpy:benchmark-v1`
with image ID `sha256:8ec3a832740cfffca716ebf9a7a1b9b324d57ca877843e324a74f53f49942c4d`.
