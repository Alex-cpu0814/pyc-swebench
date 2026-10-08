# Python-C to SWE-bench Case 022

## Identity

- Instance ID: `numpy__numpy-12805`
- Source case: `22`
- Repository: `numpy/numpy`
- Base: `99953e494aa3be5ae8385d8461b9e4dfbeec43ec`
- Fix: `2b05f3e38431842ff06df9b2958d22c5a0588767`
- Upstream PR: <https://github.com/numpy/numpy/pull/12805>

## Verified relation

Base: 3 of 10 official target parameterizations fail with dtype reference-count drops; Gold: all 10 target parameterizations pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, NumPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-022-numpy:benchmark-v1`
with image ID `sha256:7e54bbcd8594c941e1ee9e41ea15905787d0bca6fb8085b4523d5069737d6de8`.
