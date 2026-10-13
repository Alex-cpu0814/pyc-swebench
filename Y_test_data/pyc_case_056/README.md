# Python-C to SWE-bench Case 056

## Identity

- Instance ID: `python-pillow__Pillow-5633`
- Source case: `55`
- Repository: `python-pillow/Pillow`
- Base: `6798c87caf25cedf0cef19245e7db1656aed8602`
- Fix: `2e5ce839babe540865445316e7abf1cecef97264`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/5633>

## Verified relation

Base: JP2 pathlib target fails with Python filename AttributeError; Gold: target and two unchanged file-object save regressions pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-056-pillow:benchmark-v1`.

## Verified language and execution scope

The exact upstream target opens TIFF/JPEG through Path and saves JPEG/JP2 through Path. Two unchanged neighboring regressions exercise named file-object and temporary-file saving. JPEG2000, JPEG and TIFF codecs are enabled and audited; no tests are skipped. Source Python-C taxonomy is retained, but this product patch changes Python only and the verified failure precedes native JPEG2000 encoding.

Original source row 55 is classified Python-C and records a WebP/PyAccess/_copy call chain. That chain is retained as source metadata, not the trace of the JP2 pathlib regression. This fix changes Python path adaptation only; the observed wrapper error occurs before native JPEG2000 encoding and does not establish a native C defect.

The product patch changes Python Image.py only. Source Python-C taxonomy is retained; this is a verified Python path-adaptation regression in a native-codec runtime. PR opening and merge dates are 2021-07-24 and 2021-08-06 (UTC).
