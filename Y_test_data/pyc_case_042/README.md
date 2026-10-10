# Python-C to SWE-bench Case 042

## Identity

- Instance ID: `scipy__scipy-12703`
- Source case: `41`
- Repository: `scipy/scipy`
- Base: `8c7973148c5dea4a28e0e082f8c1f182313b72c1`
- Fix: `3f4396e7c8e21ea0c432c1747b221e64c162b6f5`
- Upstream PR: <https://github.com/scipy/scipy/pull/12703>

## Verified relation

Base fails the official even-length-filter validation target; Gold passes the target. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, SciPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-042-scipy:benchmark-v1`.
