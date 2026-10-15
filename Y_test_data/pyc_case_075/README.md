# Python-C to SWE-bench Case 075

## Identity

- Instance ID: `pygame__pygame-2398`
- Source case: `74`
- Repository: `pygame/pygame`
- Base: `0589ca062fa624f4bf2a9ebea7aedb2a08b37780`
- Fix: `f3ac656da14e0a40335c54a6b453c2d15184d4a2`
- Upstream issue / PR: <https://github.com/pygame/pygame/pull/2398>

## Verified relation

Base: one official loops timer API target fails and three event regressions pass. Gold: all four official nodes pass. 3 regressions pass on Base and Gold.

## Directory contract

- `analysis/`: source-row mapping, trace evidence, environment, and source material.
- `patches/`: upstream product patch and exact official test patch.
- `official_swebench/`: private/public task records, metadata, and checksums.
- `evaluator/`: config-driven evaluator, pygame adapter, and clean Dockerfile.
- `verification/`: immutable image-build and patch-run evidence.

The verified evaluator image is `yutu0814/pyc-case-075-pygame:benchmark-v1`.

## Verified scope

Official test_set_timer preserves eight events at 100 ms intervals with a 50 ms tolerance, stops via millis=0, checks loops=True for one event, and checks loops=3 for plain custom, attributed custom and KEYDOWN event objects. Selected event regressions cover a 1024-character user payload, type-filtered retrieval including the upstream added ten-event sequence, and blocked-post boolean/event behavior. Complete two-file upstream protected patch is unchanged. Native event batching performance, RWops close handling and every window constant are not individually claimed as tested defects.

Source case 74 labels function lacking and traces time_set_timer to test_set_timer, classifying argument parsing through Python-to-C APIs. The measured task validates the official loops timer API and event regressions. Event batching performance, RWops close behavior and all renamed window constants are not individually claimed as reproduced defects.

Observed version 2.0.1.dev1 comes from official setup.py. SDL2 2.0.14 and dummy video/audio drivers are fixed. Prior074 was deferred for actual upstream Gold failure; all evidence and scoped prototype cleanup are retained in analysis/prior_candidate_reviews/case074.
