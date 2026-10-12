# Python-C to SWE-bench Case 049

## Identity

- Instance ID: `CheetahTemplate3__cheetah3-26`
- Source case: `48`
- Repository: `CheetahTemplate3/cheetah3`
- Base: `c86628cad04edc5167f9a9c8999abc62c6558e7b`
- Fix: `31574d601ed6b675eb2fe8dc82659864bd3ace14`
- Upstream issue / PR: <https://github.com/CheetahTemplate3/cheetah3/issues/26>

## Verified relation

Base: official GetVar.test6 fails with NameMapper.NotFound; Gold: GetVar.test6 passes with ValueError. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Cheetah adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-049-cheetah:benchmark-v1`.

## Verification scope

The upstream issue reports a segfault on Python 2.7/CentOS. The fixed Python 3.8.20 environment reproduces an incorrect exception (`NameMapper.NotFound` instead of `ValueError`). Gold passes the official target and both regressions; the README-only negative control still fails the target, and test tampering is rejected. The original crash is not independently reproduced here.

The exact upstream diffs and raw logs are preserved. See `verification/README.md` for the controls and `official_swebench/SHA256SUMS.txt` for integrity checks.
