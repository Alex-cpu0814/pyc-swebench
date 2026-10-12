# Verification evidence

## Results

| Control | Target (`GetVar.test6`) | Regressions (`GetVar.test1`, `GetVar.test2`) | Outcome |
| --- | --- | --- | --- |
| Base with official test patch | Fails with `NameMapper.NotFound` instead of `ValueError` | 2 passed | Defect reproduced |
| Gold | 1 passed | 2 passed | Resolved |
| Negative (README-only patch) | 1 failed | 2 passed | Unresolved after test execution |
| Test tampering | Not run | Not run | Rejected: `candidate_conflicts_with_test_patch` |

The original issue reports a segfault with Python 2.7 on CentOS. This Python 3.8.20 environment reproduces the wrong exception; it does not independently reproduce that crash.

Evidence is preserved under `probes/`, `builds/case-049-final-build/`, and `runs/case-049-final-{gold,negative,tamper}/`. The earlier `case-049-negative-patch-precheck-failed` run is retained as an unsuccessful setup attempt; only `case-049-final-negative` is used as the negative control.

The final image audit confirms a clean Base working tree, with no Fix commit or candidate, Gold, or test patch present. Product and test diffs match the upstream Base-to-Fix diff byte for byte. `official_swebench/SHA256SUMS.txt` covers the task records, evaluator, patches, workbook, image audit, and final control summaries.

Upstream diffs and raw logs retain their original whitespace. Their whitespace checks are disabled in this case's `.gitattributes`; authored files remain subject to Git's normal checks.

Docker publication evidence is under `publication/`. A successful push returned the same digest as the formally verified image. Any independent registry recheck is recorded separately there.
