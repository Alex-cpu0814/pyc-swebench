# Python-C to SWE-bench Case 011

This directory follows the common cross-language SWE-bench-compatible case layout.

## Identity

- Instance ID: `numpy__numpy-15164`
- Source case: `11`
- Repository: `numpy/numpy`
- Base: `2acfd9851b6a5246e5e5e3faa97c9e728e88f8a9`
- Fix: `21e796e159dd4865a265b94a044ddb144e4e0af1`
- Upstream PR: <https://github.com/numpy/numpy/pull/15164>

## Verified relation

```text
Base + official test patch: test_searchsorted FAILED; 2 regressions PASSED
Gold + official test patch: target and 2 regressions PASSED
```

Base raises `TypeError: searchsorted() missing required argument 'keys' (pos 1)`
when the documented `v` keyword is used.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-011-numpy:benchmark-v1`
with image ID `sha256:08f623a56a982260b08f7c3f5bfedf171de71ab39d2022e893e403887fd93873`.
