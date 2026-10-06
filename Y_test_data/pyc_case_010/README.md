# Python-C to SWE-bench Case 010

This directory follows the common cross-language SWE-bench-compatible case layout.

## Identity

- Instance ID: `numpy__numpy-16276`
- Source case: `10`
- Repository: `numpy/numpy`
- Base: `5e8ad11b75245caf2d158eacf369b011ef262795`
- Fix: `8cb86fd7b454b40c7b822146d5e26c55fdc183ec`
- Upstream PR: <https://github.com/numpy/numpy/pull/16276>

## Verified relation

```text
Base + official test patch: 6 failed, 4 passed among 10 added nodes; 3 regressions passed
Gold + official test patch: 10 added nodes passed; 3 regressions passed
```

The six FAIL_TO_PASS nodes exercise zero-dimensional `out` arrays for `choose`,
`round`, `trace`, `argmax`, `argmin`, and `take`. On Base the returned object is
a converted scalar instead of the exact supplied `out` ndarray.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified local evaluator image is
`yutu0814/pyc-case-010-numpy:benchmark-v1` with image ID
`sha256:9c6264f39867c2376935e2c989a26c328eadb1b0f813d66291a224c84971e790`.
