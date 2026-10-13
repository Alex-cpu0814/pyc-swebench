# Python-C to SWE-bench Case 058

## Identity

- Instance ID: `python-pillow__Pillow-5408`
- Source case: `57`
- Repository: `python-pillow/Pillow`
- Base: `b21508798ab548ed90eb4d6bf01db14b880c9c91`
- Fix: `d3a3b6dddba4af1153aa6c01be6d3be5f43636ca`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/5408>

## Verified relation

Base: APP14 RGB transform incorrectly 100 rather than 1; Gold: target and two unchanged JPEG regressions pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-058-pillow:benchmark-v1`.

## Verified execution scope

The exact upstream APP14 test checks RGB transform 1, CMYK transform 2 and absence of transform for the shortened fixture. Two unchanged regressions cover normal JPEG decoding and CMYK roundtrip. The official 29342-byte JPEG fixture is preserved by an exact binary patch and audited against its upstream blob and SHA256. Its declared APP14 segment length is 13 bytes including the 2-byte length field, leaving an 11-byte payload with no index 11. The upstream comment is preserved verbatim. Product changes are Python-only.

Original source row 57 records incorrect result/output and a mixed APP/JPEG read/ImImagePlugin/ImageSequence/PNG/WalImageFile/native ImagingSplit chain. These remain original source metadata, not this official APP14 metadata test trace. This run observes AssertionError for adobe_transform 100 instead of 1 in Python JPEG metadata parsing; native C runtime presence does not prove a native C defect.

PR opening and merge dates are 2021-04-15 and 2021-04-25 (UTC).
