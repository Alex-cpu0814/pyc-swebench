# Python-C to SWE-bench Case 054

## Identity

- Instance ID: `python-pillow__Pillow-6874`
- Source case: `53`
- Repository: `python-pillow/Pillow`
- Base: `c683f048eb117c572b8b4eee47a324aca165fea1`
- Fix: `eb89e3a2b1833eb12124fb5f1f26f78342286143`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/6874>

## Verified relation

Base: negative-radius official target fails at Python construction; Gold: target and two unchanged native blur regressions pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-054-pillow:benchmark-v1`.

## Official scope and native partial control

One unchanged official target body checks construction and then filtering after radius mutation. Two unchanged regressions validate native numerical blur results for radius zero and one. The exact protected upstream patch retains the added BoxBlur(0) sanity parameter, outside graded scope. A Python-only partial control runs the same three nodes with regressions first: two pass, then the target process aborts with exit 134 and no terminal pytest status. The observed native guard is necessary in addition to constructor validation.

Original source row 53 records segment fault and a BoxBlur helper path. These remain original source metadata. Untouched Base fails before native filtering; the separate Python-only official-test control reaches the native filter call and observes an abort with process exit 134. No SIGSEGV is claimed for this environment.

The official PR opens on 2023-01-09 and merges on 2023-01-11 (UTC). Native partial-control evidence and process-level result interpretation are recorded under verification/.
