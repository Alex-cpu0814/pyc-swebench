# Python-C SWE-bench Cases

This repository contains deduplicated Python-C cross-language bug records that
have official upstream regression tests and have been converted to a
SWE-bench-compatible layout.

## Completed cases

| Case | Repository | Upstream record | Verification |
| --- | --- | --- | --- |
| `pyc_case_002` | `scipy/scipy` | PR #13095 / merge `60dc9730` | Base: 42 failed, 921 passed; Gold: 963 passed |
| `pyc_case_007` | `numpy/numpy` | PR #16351 / commit `a9652077` | Base: official test LEAKED; Gold: target and regression passed |
| `pyc_case_010` | `numpy/numpy` | PR #16276 / merge `8cb86fd7` | Base: 6 target failures; Gold: 6 targets and 3 regressions passed |
| `pyc_case_011` | `numpy/numpy` | PR #15164 / merge `21e796e1` | Base: target failed; Gold: target and 2 regressions passed |
| `pyc_case_013` | `numpy/numpy` | PR #14585 / merge `3d31770c` | Base: ValueError missing / SIGFPE; Gold: 2 targets and 2 regressions passed |

Source Cases 2 and 38 refer to the same commit. Only Case 2 is materialized.
Cases 7, 10, 11, and 13 are unique by their full fix commits.

Each case keeps the upstream product patch and test patch separate, provides a
clean Docker evaluator, and stores private/public task records under
`official_swebench/`.
