# Python-C to SWE-bench Case 027

## Identity

- Instance ID: `numpy__numpy-11684`
- Source case: `27`
- Repository: `numpy/numpy`
- Base: `0fd5f2506bf2f41b023392c945312e5a1a3eb819`
- Fix: `842970f1aaa710b31ebd27427035b58b265e55a8`
- Upstream PR: <https://github.com/numpy/numpy/pull/11684>

## Verified relation

Base: official empty-index diagnostic assertion fails; Gold: target passes. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-027-numpy:benchmark-v1`
with image ID `sha256:71d2efe092c6ee64b8a0a6ef40ee58ca656c90a6a43fbd8fd3aa2f35833dfc02`.
