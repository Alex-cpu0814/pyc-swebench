# Python-C to SWE-bench Case 066

## Identity

- Instance ID: `python-pillow__Pillow-2634`
- Source case: `65`
- Repository: `python-pillow/Pillow`
- Base: `3fb62360e61949a2405db0771ad89f1c9a2b25e4`
- Fix: `e71757aa6f64f698a16acaece9bc5557302a1fe8`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/2634>

## Verified relation

Base: 1 font leak target fails and 3 regressions pass. Gold: all 4 official nodes pass without skips.. 3 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-066-pillow:benchmark-v1`.

## Verified execution scope

Original official unittest cases execute once each in fresh subprocesses. DefaultFont uses 100 iterations and 1024 KiB, TrueType uses 10 iterations and 4096 KiB. Thresholds, loops and test bodies are unchanged. TrueType Base pass does not independently verify the FreeType leak repair in this allocator/dependency environment. The complete two-file upstream C product patch is retained. Initial pytest PNG cleanup incompatibility and DefaultFont assertion, plus the sandbox Docker permission error, remain authoring evidence.

Original source row 65 records a memory leak and a _font_getmask/test_rotated_transposed_font_get_mask chain. This original source trace is retained separately from the official font-leak test paths measured in this case.

PR opening2017-07-18 and merge2017-09-04 are separately recorded UTC dates. The regression differentiates DefaultFont in this environment; TrueType is a passing regression on both revisions.
