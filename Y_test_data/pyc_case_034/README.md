# Python-C to SWE-bench Case 034

## Identity

- Instance ID: `scipy__scipy-8822`
- Source case: `34`
- Repository: `scipy/scipy`
- Base: `9529e47630be8f2345fd3d54302f248ce309d8cd`
- Fix: `0aee4a24bedb154d07a3b5ba016a385b1ac2910c`
- Upstream PR: <https://github.com/scipy/scipy/pull/8822>

## Verified relation

Base cannot complete the official repeated-time test, while Gold passes it. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, SciPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-034-scipy:benchmark-v1`.
