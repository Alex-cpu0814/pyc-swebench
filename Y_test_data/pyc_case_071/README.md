# Python-C to SWE-bench Case 071

## Identity

- Instance ID: `ultrajson__ultrajson-441`
- Source case: `70`
- Repository: `ultrajson/ultrajson`
- Base: `f26f9679f1b9d7fa2d0488e1e7b1256d9391a85f`
- Fix: `a920bfa9d85bcd78836b866d1be80c1e3dcca1da`
- Upstream issue / PR: <https://github.com/ultrajson/ultrajson/pull/441>

## Verified relation

Base: 4 official empty-container parameter targets fail and 4 regressions pass. Gold: all 8 official nodes pass.. 4 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, UltraJSON adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-071-ultrajson:benchmark-v1`.

## Verified scope and parameter identities

Exact upstream test_encode_indent inputs cover a nonempty object, {}, [], an object containing an empty object, and a list containing an empty list, at indent=4. Both original-format and stdlib-json equality assertions are retained. Four empty/nested inputs are measured FAIL_TO_PASS; the nonempty input and three unchanged dict/list encoding and Unicode decoding tests are PASS_TO_PASS. Real pytest parameter IDs containing spaces and literal escapes are kept exactly; the anchored result parser accepts spaces without decoding or normalizing IDs. No float-representation claim is made.

Original source case 70 records incorrect result/output and an encode/test_double_long_issue trace with buffer-management helpers. This supplied trace is retained separately from actual empty-container serialization assertions measured here; float representation is not claimed as the reproduced defect.

Runtime4.0.2.dev3 is an observed SCM snapshot from fixed Base and ancestor4.0.1 tag. Parameter IDs come from original official collection and remain literal, including spaces and escape characters.
