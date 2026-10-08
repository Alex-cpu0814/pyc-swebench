# Python-C to SWE-bench Case 015

## Identity

- Instance ID: `numpy__numpy-14240`
- Source case: `15`
- Repository: `numpy/numpy`
- Base: `965ea2ff417bcb285beca5c36cd02a8790a3d8f6`
- Fix: `4246ce2a391314acc1da90d56ff4f995d45e18a9`
- Upstream PR: <https://github.com/numpy/numpy/pull/14240>

## Verified relation

Base: 2 official nodes fail with MemoryError; Gold: both targets pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-015-numpy:benchmark-v1`
with image ID `sha256:f2da0afcaca3b41ce053ae0355187005b364e3490eda7dbeecac6561e03d5967`.
