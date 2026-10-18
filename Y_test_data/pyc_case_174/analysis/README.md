# Analysis

Original source 173, Excel row 175.

Base passes three complete original native regressions, starts the complete rough-mag-symprec target, then its native GoogleTest child exits on SIGSEGV (returncode -11, shell exit139). The target has no terminal test result and is graded MISSING. Full exact upstream Gold completes all four methods with PASSED and exit0. No FAILED terminal line is invented.

The complete new original C++ GoogleTest calls spg_get_symmetry and spgms_get_symmetry_with_site_tensors for the original four-atom lattice, symprec=mag_symprec=0.1, prints symmetry operations, and frees the original arrays. It adds no numerical assertions. Its measured oracle is native completion versus SIGSEGV. Three complete existing methods cover database operations, spacegroup type and type4 dataset. C++ invokes the actual C API. Python binding is not executed. Preserve this completion-only scope rather than claiming numerical-result validation.

Original Python-C taxonomy and source-row trace are retained verbatim. The source trace ends at Python get_symmetry_dataset; the measured complete official regression uses native C++ GoogleTest directly calling the C API. No Python binding or full original source trace is executed by this test.

Complete exact upstream change: .github/ISSUE_TEMPLATE/bug_report.md, doc/magnetic_symmetry_flags.md, src/overlap.c, src/spin.c, test/test_magnetic_symmetry.cpp

Created at is actual PR195 opening 2022-10-30T06:25:21Z; merged at is actual PR195 merge 2022-10-30T10:33:14Z. Exact source commit timestamp is retained separately.

spglib 2.0.1. GoogleTest release-1.12.1 (58d77fa8070e8cec2dc1ed015d66b454c8d78850). Original standalone test/CMakeLists.txt default Release, C++11, exact original GoogleTest release-1.12.1. Ordinary CMake/GCC on public Debian bullseye. No sanitizer or additional compiler flags. Original standalone test/CMakeLists.txt with default Release; only standard FETCHCONTENT_SOURCE_DIR_GOOGLETEST selects preinstalled exact release-1.12.1 public dependency for offline evaluation. Ordinary public Python3.8.20-bullseye GCC/G++10.2 and CMake3.22.6, original default Release flags. No product/test/allocator/compiler-macro changes. Python3.8.20 orchestrates the evaluator only. The executable statically links the exact local C implementation. Source Git blobs, executable/library hashes, compiler flags, package versions and GoogleTest commit are audited. Runtime-only loader constructor sets RLIMIT_CORE=0 and PR_SET_DUMPABLE=0 for native child to avoid WSL piped core handler. No interposition, allocator/signal handlers, source or assertion changes; same Base/Gold.
