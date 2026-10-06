# Case analysis

The source workbook records the same SciPy merge commit in Python-C Cases 2
and 38. Deduplication uses the full commit SHA, so this directory represents it
once as `pyc_case_002`.

The upstream PR contains concrete trace evidence in addition to the source
row's `incorrect results/output` symptom: an ARM test worker crashed while
running `test_zoom_grid_by_int_order0`. Debugging found a coordinate near zero
that rounded to exactly `-1`, selected an invalid constant-mode path, and wrote
through an uninitialized `zeros` array. The protected tests also exercise the
new grid-based behavior and mode warnings on the local Linux evaluator.

`source_row_002.json` preserves the source classification and upstream trace.
`environment_spec.json` records the verified build and test environment.
