# Python-C to SWE-bench Case 037

## Identity

- Instance ID: `scipy__scipy-742`
- Source case: `36`
- Repository: `scipy/scipy`
- Base: `bf05e8d3412e2d96ab6735b6935e2a65f2620c30`
- Fix: `2a2d8be5f52481938c817eb7150fe7152958853d`
- Upstream commit (ticket #742): <https://github.com/scipy/scipy/commit/2a2d8be5f52481938c817eb7150fe7152958853d>

## Verified relation

The official ticket_742 test terminates Base but passes after the upstream native-code fix. 2 regressions pass on Base and Gold.

Base exits with SIGSEGV (139); the target node has no completed pytest result
and is graded MISSING/unresolved. Gold passes all three nodes. The negative
control applies successfully and reproduces this Base result. The tamper
control applies successfully but conflicts with the protected official test
patch and is rejected before testing.

Candidate-table case 037 maps to original source row 36 by the full fix commit.
The image builds Python 3 converted sources under `/testbed/build/py3k`. An
environment-only compatibility adjustment removes the obsolete NumPy lazy
package loader from the generated SciPy initialization file after each build.
The upstream C product patch and regression test patch remain unchanged.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, SciPy adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-037-scipy:benchmark-v1`.
