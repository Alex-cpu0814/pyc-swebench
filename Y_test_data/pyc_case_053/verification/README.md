# Verification evidence

Gold passes two FAIL_TO_PASS and two PASS_TO_PASS official nodes. A README-only negative control reaches tests, preserves both regressions and leaves both I;16 assertions failed. The candidate modifying the protected I;16 font-test context applies to Base but is rejected with candidate_conflicts_with_test_patch before build or grading.

The clean formal image contains pinned Base source and its native build. It does not contain the fix commit, solution patch, protected patch or evaluator assets. The candidate build uses python setup.py build_ext -i --force with PYTHONPATH=/testbed/src. Tests execute ordinary native code without instrumentation.

Two FAIL_TO_PASS nodes cover independent native corrections: test_point_I16 (Draw.c) and test_I16[Layout.BASIC] (Paste.c). Two unchanged PASS_TO_PASS nodes cover normal drawing and BASIC font properties. The exact protected upstream patch also retains rectangle tests and their binary PNG. RAQM parameters are outside this minimal scope because RAQM is absent; BASIC FreeType nodes execute without skips.

The protected binary image patch is independently applied and hashed against upstream blob a75f12c2e98f417e662f2661eab980b45b61cde1. Dependency-and-asset audits record exact GCC, JPEG, zlib and FreeType package versions and the actual source import path. Initial prototype dependency-and-asset audit reached the successful PNG/package checks but failed in its final Python diagnostic due to quoting; the initial raw logs are retained alongside successful v2/formal audits.

probes/base and probes/gold preserve the discriminating runs. probes/collect preserves official BASIC/RAQM parameter IDs. prototype-build preserves the original image build and auxiliary audits. builds/case-053-final-build records the pinned formal build and clean audit. runs/case-053-final-{gold,negative,tamper} contain the final controls.
