# Python-C to SWE-bench case 175

Instance spglib__spglib-c571f29d; repository spglib/spglib; upstream https://github.com/spglib/spglib/pull/187. Base 4afa84322f83b368dada7e3c6f64c3a17114aaa0; fix c571f29d57d51ed5d8efa1eb78e42e7f48082897.

Base: 3 regressions PASSED, target starts then SIGSEGV with no terminal status (MISSING), exit139. Gold: 4 complete original methods PASSED, exit0.

Base passes three complete original native regressions, starts the complete rough-symprec target, then its native GoogleTest child exits on SIGSEGV (returncode -11, shell exit139). The target has no terminal test result and is graded MISSING. Full exact upstream Gold completes all four methods with PASSED and exit0. No FAILED terminal line is invented.

The complete original C++ GoogleTest uses the original three-atom lattice, tensors [0.005,0.002,0.002], and symprec=mag_symprec=1e-2. It calls spg_get_symmetry and spgms_get_symmetry_with_site_tensors, asserts size==4 after each, prints the original operations and frees all original arrays. Base starts this target and receives SIGSEGV without a terminal status. Gold completes both assertions and all cleanup. Three complete existing native methods cover database operations, spacegroup type and type4 dataset. The actual C API is executed; Python binding and the full source-row trace are not executed.

Original Python-C taxonomy and source-row trace are retained verbatim. The source trace ends at Python get_symmetry_dataset; the measured complete official regression uses native C++ GoogleTest directly calling the C API. No Python binding or full original source trace is executed by this test.

Complete exact upstream change: src/magnetic_spacegroup.c, src/spin.c, test/README.md, test/test_magnetic_symmetry.cpp

The same audited formal image runs complete original methods in this order: test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_magnetic_symmetry_from_database, test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_magnetic_spacegroup_type, test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_magnetic_dataset_type4, test/test_magnetic_symmetry.cpp::test_magnetic_symmetry.test_spg_get_symmetry_with_tensors_rough_symprec. Gold completes all methods; README-only negative retains the measured Base process failure; a protected-test-context conflict is rejected before grading. Anchored canonical terminal lines determine statuses. A started target without a terminal line remains MISSING, accompanied by the original native signal/exit record.

Image yutu0814/pyc-case-175-spglib:benchmark-v1. Exact complete upstream patches, workbook, raw evidence and full-file SHA256 are retained.
