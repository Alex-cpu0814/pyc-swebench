# Python-C to SWE-bench Case 007

This directory follows the common cross-language SWE-bench-compatible case layout.

## Identity

- Instance ID: `numpy__numpy-16351`
- Source case: `7`
- Repository: `numpy/numpy`
- Base: `fc2518ba6b11fc52b0ff477b9e83576be90562d8`
- Fix: `a9652077be95f83f56c9b77e7ad1ed7710516626`
- Upstream PR: <https://github.com/numpy/numpy/pull/16351>

## Verified relation

```text
Base + official test patch: test_malloc_fails LEAKED; test_zeros PASSED
Gold + official test patch: test_malloc_fails PASSED; test_zeros PASSED
```

The target test requires a debug Python and `pytest-leaks`. Ordinary pytest only checks that `_ArrayMemoryError` is raised and cannot distinguish Base from Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified local evaluator image is
`yutu0814/pyc-case-007-numpy:benchmark-v1` with image ID
`sha256:ddbe5866e7eec2a3e12f4ebf75adf5c83c154c8ac15f049f3039395c37a8c617`.
