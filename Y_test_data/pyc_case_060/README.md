# Python-C to SWE-bench Case 060

## Identity

- Instance ID: `python-pillow__Pillow-5274`
- Source case: `59`
- Repository: `python-pillow/Pillow`
- Base: `d0612030a0ba7aed533e1f9115bbf4bd1019f48e`
- Fix: `9a683db33945aacf2fa9a277f680e29d54685930`
- Upstream issue / PR: <https://github.com/python-pillow/Pillow/pull/5274>

## Verified relation

Base: both gradient targets SIGSEGV; Gold-v2: both targets and two wrong-mode regressions pass. 2 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, Pillow adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-060-pillow:benchmark-v1`.

## Verified execution scope

The exact upstream linear/radial tests loop L, P, I and F, compare generated pixels against existing PNG references and check key pixels/modes. Base terminates at I, so F is not reached on Base; Gold verifies both I and F. Two unchanged RGB wrong-mode nodes preserve ValueError behavior. Official test logic is unmodified. Each node runs in a separate subprocess; native SIGSEGV is recorded as process failure rather than an assertion, aggregate exit 1 permits complete node grading. The product patch changes C Fill.c only; no binary asset changes.

Original source row 59 records segment fault (crash) and a mixed ImagingFillLinearGradient/ImagingError/ImagingTransform/_transform2/Python __transformer chain. This is preserved source metadata. Actual official stacks enter Image.linear_gradient/radial_gradient and terminate with SIGSEGV in Base; the unrelated transform chain is not this runtime trace.

PR opening/merge dates are2021-02-19/2021-03-28 UTC. Initial Gold timeout is retained separately; successful Gold-v2 and final formal controls establish the result.
