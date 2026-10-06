# Python-C to SWE-bench Case 002

This directory follows the common cross-language SWE-bench-compatible case
layout used by the Java-C dataset.

## Identity

- Instance ID: `scipy__scipy-13095`
- Source case: `2` (source Case `38` is the same commit and was deduplicated)
- Repository: `scipy/scipy`
- Base: `ff177d92b79167eb5de593c9de41d3ceb97ab189`
- Fix merge: `60dc9730d5652f0632cd43caef437f01a734e374`

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, SciPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

## Verified relation

```text
Base + official test patch: 42 failed, 921 passed
Gold + official test patch: 963 passed
```

The evaluator runs the complete upstream file
`scipy/ndimage/tests/test_interpolation.py`. The image contains the Base
checkout and cached ignored build outputs, but no product patch, test patch, or
evaluation script. Those assets are mounted only after a fresh container
starts.

The verified local evaluator image is
`yutu0814/pyc-case-002-scipy:benchmark-v3` with digest
`sha256:a06dba0866df6cc6a1b517fb2516808a1afb412e1ced4adb6fec3518c33cc617`.
