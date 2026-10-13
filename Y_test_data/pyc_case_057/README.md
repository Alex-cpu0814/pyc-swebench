# Python-C to SWE-bench Case 057

## Identity

- Instance ID: `python-pillow__Pillow-5613`
- Source case: `56`
- Repository: `python-pillow/Pillow`
- Base: `f0679aff4d43dbd595b98501dc7a8420550bf4e8`
- Fix: `5f39e8e60ae0662b850484b2ad7a1eaa83677dd3`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/5613>

## Verified relation

Base: negative-count PSD frame test raises UnidentifiedImageError; Gold: target and two unchanged PSD regressions pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-057-pillow:benchmark-v1`.

## Verified execution scope

The exact upstream frame-count test checks normal and negative-count PSD files for two frames and animation. Two unchanged regressions exercise normal PSD pixel decoding and layer seeking. The 5492-byte official PSD fixture is preserved by an exact binary test patch and checked against its upstream Git blob and SHA256. Product changes are Python-only; no hang or native C defect was observed.

Original source row 56 records hang and a mixed JPEG read/container seek/WalImageFile/native _split call chain. These remain original source metadata, not this official PSD test trace. This run observes PIL.UnidentifiedImageError opening the negative-count PSD, with no hang. The product patch changes Python parsing only; native C runtime presence does not prove a native C defect.

PR opening and merge dates are 2021-07-15 and 2021-07-28 (UTC).
