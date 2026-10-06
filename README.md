# Python-C SWE-bench Cases

This repository contains deduplicated Python-C cross-language bug records that
have official upstream regression tests and have been converted to a
SWE-bench-compatible layout.

## Completed cases

| Case | Repository | Upstream record | Verification |
| --- | --- | --- | --- |
| `pyc_case_002` | `scipy/scipy` | PR #13095 / merge `60dc9730` | Base: 42 failed, 921 passed; Gold: 963 passed |

Source Cases 2 and 38 refer to the same commit. Only Case 2 is materialized.

Each case keeps the upstream product patch and test patch separate, provides a
clean Docker evaluator, and stores private/public task records under
`official_swebench/`.
