# Python-C to SWE-bench Case 048

## Identity

- Instance ID: `scipy__scipy-14327`
- Source case: `47`
- Repository: `scipy/scipy`
- Base: `018986cb0260881827c6ef33cd2d804f54e39c85`
- Fix: `ed220ccdf4bab8fd25293afec26a8cb321f12921`
- Upstream issue / PR: <https://github.com/scipy/scipy/pull/14327>

## Verified relation

Instrumented Base: official float16 node fails with comparator-table bounds diagnostic; instrumented Gold: that node and two unchanged regressions pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, SciPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-048-scipy:benchmark-v1`.

## Evaluation scope

The exact upstream protected test patch retains all five dtype parameters. Formal grading selects only float16 (the discriminating comparator-table bounds case) plus test_basic and test_none. Ordinary builds passed on both revisions. The same non-recovering bounds configuration is applied to Base, Gold and candidate builds; each official pytest node runs in a separate subprocess to preserve neighboring results after the diagnostic.

No ordinary-build crash was independently reproduced. Formal controls and clean-image audit are recorded under verification/.
