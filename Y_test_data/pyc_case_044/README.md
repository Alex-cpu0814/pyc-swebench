# Python-C to SWE-bench Case 044

## Identity

- Instance ID: `scipy__scipy-4143`
- Source case: `43`
- Repository: `scipy/scipy`
- Base: `fc6b387bc0c51b5b252712584580b4f0975498fb`
- Fix: `88d625fc451d3714e640bbec693bb31abb6a05f5`
- Upstream PR: <https://github.com/scipy/scipy/pull/4143>

## Verified relation

Base passes both neighboring regressions, then the official large-array map_coordinates target terminates with SIGSEGV (exit 139). Gold passes all three selected official nodes. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, SciPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-044-scipy:benchmark-v1`.

## Test scope

Candidate Case 044 maps to source Case 43 by the full fix hash. The source row
describes `NI_Select`/`NI_RankFilter`, whereas the exact upstream added test
exercises large-array `map_coordinates` in `ni_interpolation.c`. It checks that
interpolation completes without crashing. It does not independently assert the
rank-filter path or numerical output of the large-array interpolation.

## Local verification

- Base probe: two regressions pass, then the target terminates with SIGSEGV (139).
- Gold: one target and two regressions pass in the formal evaluator.
- Negative: a README-only change must remain unresolved at the target test.
- Tamper: rejected as `candidate_conflicts_with_test_patch` before building.
- Image audit: exact first-parent Base, clean tracked tree, no fix commit or
  protected evaluation assets in the image.

Raw probe logs are in `verification/probes/`; formal build and control logs are
in `verification/builds/` and `verification/runs/`. The image is verified locally;
external publication has not been performed for this case.
