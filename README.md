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
| `pyc_case_014` | `numpy/numpy` | PR #14393 / merge `f786041d` | Base: ValueError not raised; Gold: target and 2 regressions passed |
| `pyc_case_015` | `numpy/numpy` | PR #14240 / merge `4246ce2a` | Base: 2 MemoryError failures; Gold: 2 targets and 2 regressions passed |
| `pyc_case_022` | `numpy/numpy` | PR #12805 / merge `2b05f3e3` | Base: 3 dtype reference-count failures; Gold: 3 targets and 2 regressions passed |
| `pyc_case_023` | `numpy/numpy` | PR #12814 / merge `74f3d07a` | Base: target aborts with exit 134; Gold: target and 2 regressions passed |
| `pyc_case_027` | `numpy/numpy` | PR #11684 / merge `842970f1` | Base: empty-index diagnostic failed; Gold: target and 2 regressions passed |
| `pyc_case_031` | `numpy/numpy` | ticket #925 / commit `a0e082a0` | Base: 2 choose-broadcast targets failed; Gold: 2 targets and 1 regression passed |
| `pyc_case_034` | `scipy/scipy` | PR #8822 / merge `0aee4a24` | Base: repeated-time target terminates early; Gold: target and 2 regressions passed |
| `pyc_case_037` | `scipy/scipy` | ticket #742 / commit `2a2d8be5` | Base: label target SIGSEGV (139); Gold: target and 2 regressions passed |
| `pyc_case_041` | `scipy/scipy` | PR #12562 / merge `e2091e9e` | Base: fixed-knots `splprep` target SIGSEGV (139); Gold: target and 2 regressions passed |
| `pyc_case_042` | `scipy/scipy` | PR #12703 / merge `3f4396e7` | Base: even-length `sepfir2d` validation target failed; Gold: target and 2 regressions passed |
| `pyc_case_044` | `scipy/scipy` | PR #4143 / merge `88d625fc` | Base: large-array `map_coordinates` target SIGSEGV (139); Gold: target and 2 regressions passed |
| `pyc_case_046` | `tskit-dev/tskit` | Issue #453 / PR #637 / commit `568a9a95` | Base: large-time Newick buffer and buffer-size API targets fail; Gold: 2 targets and 2 regressions pass |
| `pyc_case_048` | `scipy/scipy` | PR #14327 / commit `ed220ccd` | Bounds-instrumented Base: float16 target fails; Gold: target and 2 regressions pass |
| `pyc_case_049` | `CheetahTemplate3/cheetah3` | Issue / PR #26 / commit `31574d60` | Base: 1 target failures; Gold: 1 targets and 2 regressions pass |
| `pyc_case_053` | `python-pillow/Pillow` | Issue / PR #7257 / commit `6f736915` | Base: 2 target failures; Gold: 2 targets and 2 regressions pass |

Source Cases 2 and 38 refer to the same commit. Only Case 2 is materialized.
Source Cases 15 and 16 refer to the same full fix commit. Only Case 15 is materialized.
Cases 7, 10, 11, 13, 14, 15, 22, 23, 27, 31, 34, 37, 41, and 42 are unique by their full fix commits.
Candidate-table Case 37 maps to original source row 36 by fix commit `2a2d8be5f52481938c817eb7150fe7152958853d`.
Candidate-table Case 41 maps to original source Case 40 by fix commit `e2091e9e4be2dffed8c6535547e8519dc002fa74`.
Candidate-table Case 42 maps to original source Case 41 by fix commit `3f4396e7c8e21ea0c432c1747b221e64c162b6f5`.
Candidate-table Case 44 maps to original source Case 43 by fix commit `88d625fc451d3714e640bbec693bb31abb6a05f5`.
Case 44's official test covers `map_coordinates`; the source record describes `NI_Select`/`NI_RankFilter` from the same fix commit. The rank-filter path is not independently verified by this test.
Candidate-table Case 46 maps to original source Case 45 by fix commit `568a9a953d549ae9a48f0f6d98435249841b7b5e`.

Each case keeps the upstream product patch and test patch separate, provides a
clean Docker evaluator, and stores private/public task records under
`official_swebench/`.
