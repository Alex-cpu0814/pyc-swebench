# Python-C to SWE-bench Case 068

## Identity

- Instance ID: `python-pillow__Pillow-574`
- Source case: `67`
- Repository: `python-pillow/Pillow`
- Base: `dc1664500be0135d83182d480af341d39b5c78d7`
- Fix: `6e2075e25d49fa0ffaec5892b64e3dd4cd39a9fd`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/574>

## Verified relation

Base: 5 official targets fail and 3 regressions pass. Gold: all 8 official nodes pass without skips.. 3 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-068-pillow:benchmark-v1`.

## Measured scope and source identity

Five unchanged upstream functions cover RGBA-to-palette similarity at epsilon 20, indexed P/L/RGB transparency conversion and saving, default RGBA quantization and rejection of unsupported method 0. Three unchanged regressions cover normal default conversion, 8-bit float conversion and 100-color octree quantization. Each function executes once in a fresh process; original tester assertion counters and yield_test callbacks are preserved. An explicit node status and positive assertion count are required for passing, so os._exit(0) skip cannot pass grading. No new assertions, thresholds, image assets or product changes beyond the exact upstream patch are introduced.

Product changes are Python-only PIL/Image.py plus CHANGES.rst. The provided source taxonomy remains Python-C. Original source case 67 records crash and a mixed Image.quantize/EpsImagePlugin/TiffImagePlugin/ImageOps/ImageDraw/SaneDev_close trace. This original source metadata is retained separately from actual official tester conversion/quantization outcomes; no native crash or C fix is claimed without runtime evidence.

The PR API merge commit fa165c8d70062d1dac943f51d861559b0433cf49 differs from the fixed source commit 6e2075e25d49fa0ffaec5892b64e3dd4cd39a9fd. The source commit API verifies PR574 merge subject, parents and the same UTC merge timestamp. The alternate fa165 object returns HTTP 422, so tree or content equivalence cannot be checked. All patches and tests use source 6e2075 and its verified first parent.
