# Python-C to SWE-bench Case 013

This directory follows the common cross-language SWE-bench-compatible case layout.

## Identity

- Instance ID: `numpy__numpy-14585`
- Source case: `13`
- Repository: `numpy/numpy`
- Base: `663b161074580a340201da1765e3618c086ff8dc`
- Fix: `3d31770c61ea2412267c233d38ccc33d5d3a0610`
- Upstream PR: <https://github.com/numpy/numpy/pull/14585>

## Verified relation

```text
Base + official test patch: clip case FAILED and wrap case raised SIGFPE; 2 regressions PASSED
Gold + official test patch: 2 target nodes and 2 regressions PASSED
```

Base accepts a non-empty index array for a shape containing a zero-sized axis.
The `clip` mode returns without the required `ValueError`, while `wrap` reaches
division by zero and terminates with a floating-point exception.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-013-numpy:benchmark-v1`
with image ID `sha256:19d9e4c60528969fa655ade3622e48b0c85c508ccd6249e801d6781bef11f508`.
