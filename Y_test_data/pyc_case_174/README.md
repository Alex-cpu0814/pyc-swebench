# Python-C to SWE-bench case 174

Instance spglib__spglib-9218fa14; repository spglib/spglib; upstream https://github.com/spglib/spglib/pull/195. Base 9458171a2eb9bea9036632a408da7b269ea07bbb; fix 9218fa14771d967a20f00764b335bc2a265790a1.

Base: 3 regressions PASSED, target starts then SIGSEGV with no terminal status (MISSING), exit139. Gold: 4 complete original methods PASSED, exit0.

Base passes three complete original native regressions, starts the complete rough-mag-symprec target, then its native GoogleTest child exits on SIGSEGV (returncode -11, shell exit139). The target has no terminal test result and is graded MISSING. Full exact upstream Gold completes all four methods with PASSED and exit0. No FAILED terminal line is invented.

The complete new original C++ GoogleTest calls spg_get_symmetry and spgms_get_symmetry_with_site_tensors for the original four-atom lattice, symprec=mag_symprec=0.1, prints symmetry operations, and frees the original arrays. It adds no numerical assertions. Its measured oracle is native completion versus SIGSEGV. Three complete existing methods cover database operations, spacegroup type and type4 dataset. C++ invokes the actual C API. Python binding is not executed. Preserve this completion-only scope rather than claiming numerical-result validation.

Original Python-C taxonomy and source-row trace are retained verbatim. The source trace ends at Python get_symmetry_dataset; the measured complete official regression uses native C++ GoogleTest directly calling the C API. No Python binding or full original source trace is executed by this test.

Complete exact upstream change: .github/ISSUE_TEMPLATE/bug_report.md, doc/magnetic_symmetry_flags.md, src/overlap.c, src/spin.c, test/test_magnetic_symmetry.cpp

The same audited formal image runs complete original methods in this order: test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_magnetic_symmetry_from_database, test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_magnetic_spacegroup_type, test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_magnetic_dataset_type4, test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_symmetry_with_tensors_rough_mag_symprec. Gold completes all methods; README-only negative retains the measured Base process failure; a protected-test-context conflict is rejected before grading. Anchored canonical terminal lines determine statuses. A started target without a terminal line remains MISSING, accompanied by the original native signal/exit record.

Image yutu0814/pyc-case-174-spglib:benchmark-v1. Exact complete upstream patches, workbook, raw evidence and full-file SHA256 are retained.
