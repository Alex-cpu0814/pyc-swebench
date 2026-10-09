# Python-C to SWE-bench Case 041

## Identity

- Instance ID: `scipy__scipy-12562`
- Source case: `40`
- Repository: `scipy/scipy`
- Base: `e13278e712ac33c6110b5d48a8da0acfa7768b71`
- Fix: `e2091e9e4be2dffed8c6535547e8519dc002fa74`
- Upstream PR: <https://github.com/scipy/scipy/pull/12562>

## Verified relation

Base aborts and segfaults in the official fixed-knots splprep regression; Gold passes the target. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, SciPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-041-scipy:benchmark-v1`.
