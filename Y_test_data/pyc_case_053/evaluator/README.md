# Evaluator

The evaluator applies a candidate patch, then the exact protected upstream test patch including the binary PNG, forces a rebuild of Pillow C extensions, and executes two I;16 FAIL_TO_PASS plus two unchanged PASS_TO_PASS pytest nodes. The pytest parser accepts Tests/ node paths.

Two FAIL_TO_PASS nodes cover independent native corrections: test_point_I16 (Draw.c) and test_I16[Layout.BASIC] (Paste.c). Two unchanged PASS_TO_PASS nodes cover normal drawing and BASIC font properties. The exact protected upstream patch also retains rectangle tests and their binary PNG. RAQM parameters are outside this minimal scope because RAQM is absent; BASIC FreeType nodes execute without skips.

The build audit verifies Pillow and FreeType2. NumPy is not required by these tests; its template config/build argument is unused.
