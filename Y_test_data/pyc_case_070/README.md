# Python-C to SWE-bench Case 070

## Identity

- Instance ID: `ultrajson__ultrajson-426`
- Source case: `69`
- Repository: `ultrajson/ultrajson`
- Base: `9c589d1cb5dc81552aa8ee72694cb830bed099c6`
- Fix: `335ac83c1308b928bb316eb302114d76543868cf`
- Upstream issue / PR: <https://github.com/ultrajson/ultrajson/pull/426>

## Verified relation

Base: 1 official indentation target fails and 3 regressions pass. Gold: all 4 official nodes pass.. 3 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, UltraJSON adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-070-ultrajson:benchmark-v1`.

## Measured native scope

The exact protected upstream test decodes the JSON object {"obj":31337} and compares its indent=4 encoded text with the original four-space formatting. Three unchanged official regressions cover ordinary dictionary/list conversion and Unicode decoding. Tests execute normally in one pytest process, without altered values, assertions or thresholds. Product patch is the single native C argument-format change; vendored C++ double-conversion is compiled but unchanged.

Original source case69 records incorrect result/output and an objToJSON/benchmark_medium_complex_object chain. This original source trace is retained separately from the actual official test_encode_indent output assertion measured here.

Runtime version3.2.1.dev2 is an observed SCM snapshot from exact Base history and pinned ancestor3.2.0 tag. Generated version.h is ignored; vendored double-conversion is ordinary tracked source. No release version or C++ product change is inferred.
