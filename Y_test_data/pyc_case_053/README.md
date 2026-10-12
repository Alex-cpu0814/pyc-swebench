# Python-C to SWE-bench Case 053

## Identity

- Instance ID: `python-pillow__Pillow-7257`
- Source case: `52`
- Repository: `python-pillow/Pillow`
- Base: `09605ff48e582fda6870a2c4c519650321f3f8de`
- Fix: `6f73691564908f70967cf76b8f4f88e390f57fe9`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/7257>

## Verified relation

Base: two I;16 target failures and two unchanged regressions pass; Gold: all four official nodes pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-053-pillow:benchmark-v1`.

## Official evaluation scope

Two FAIL_TO_PASS nodes cover independent native corrections: test_point_I16 (Draw.c) and test_I16[Layout.BASIC] (Paste.c). Two unchanged PASS_TO_PASS nodes cover normal drawing and BASIC font properties. The exact protected upstream patch also retains rectangle tests and their binary PNG. RAQM parameters are outside this minimal scope because RAQM is absent; BASIC FreeType nodes execute without skips.

Original source row 52 references the RGB test_modify_after_resizing path. It is retained as source metadata and is not the execution trace of the verified I;16 drawing/text regression.

The PR opening date is 2023-07-04, distinct from merge date 2023-10-05. Native dependency versions and binary reference-image integrity are recorded in analysis/upstream_provenance.json and verification/.
