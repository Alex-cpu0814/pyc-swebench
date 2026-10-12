# Python-C to SWE-bench Case 046

## Identity

- Instance ID: `tskit-dev__tskit-453`
- Source case: `45`
- Repository: `tskit-dev/tskit`
- Base: `eb8b4aebe42f39f7e536a603e8cd25d9cf104e22`
- Fix: `568a9a953d549ae9a48f0f6d98435249841b7b5e`
- Upstream issue: <https://github.com/tskit-dev/tskit/issues/453>
- Upstream PR: <https://github.com/tskit-dev/tskit/pull/637>

## Verified relation

Base: 2 failed and 2 passed; the large-time target raises LibraryError: Supplied buffer is too small, and the low-level target raises TypeError for the unsupported buffer_size keyword. Gold: all 4 official nodes pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, tskit adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-046-tskit:benchmark-v1`.

## Test scope and provenance

Candidate Case 046 maps to original source Case 45 (source workbook row 47) by
the complete fix hash. Candidate Case 045 has no official test-source change
and is not materialized. The issue was opened on 2020-01-12; the fix was committed
on 2020-05-23. The source row references `Tree_get_newick` and
`test_newick_precision`; that unchanged precision test is a PASS_TO_PASS node.

The two FAIL_TO_PASS nodes are the exact upstream added high-level large-time
test and changed low-level interface test. Only four official test nodes are
graded. The original issue reports msprime 0.6.1 on Python 3.6; this benchmark
validates the exact tskit parent using msprime 0.7.4 on Python 3.8.20, consistent
with the parent's CI Python support.

The high-level test compares C/Python output for 2, 10, 20 and 100 samples at
precision 0, 1 and 16. The protected test patch contains both upstream test-file
changes without edits. The product patch contains the remaining three upstream
files, including its changelog entry.

## Evaluation environment

The image fetches only the exact Base and the pinned kastore C submodule. Native
extensions are built in place under `python/`; generated build outputs and caches
are excluded through local `.git/info/exclude`, with no tracked source changes.
GSL 2.6 is required by msprime. The unavailable Bullseye security mirror was
excluded from dependency installation; Debian main supplies the pinned GSL
package, while the base image's Git and certificates are kept without upgrade.

Official tests run through `pytest_no_dump.py`, which sets the current test
process's Linux dumpability to zero and disables core files. This leaves official
tests intact and prevents the large Windows/WSL host dumps seen in Case 044.
Runtime containers have no network, 2 GiB RAM and 4 CPUs. No host-wide crash
reporting setting is changed.
