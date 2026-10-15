# Python-C to SWE-bench case077

Instance: pygame__pygame-2927. Repository: pygame/pygame. Upstream: https://github.com/pygame/pygame/pull/2927.

Base: c09d677a6c1c2e814683576035f13c6a07d64f67. Fix: ef30264c6c85d4eeebcbbf3c9b10106782ed4a0b.

Base: one official rectangle-border pixel target fails and three regressions pass. Gold: all four official nodes pass.

The active native DrawRectTest runs the complete upstream added test_rect__draw_line_width: a 100x100 surface, 80x50 rectangle, line width 10, 40 white corner diagonal samples and four black inner corners. Three unchanged neighboring methods cover filled rectangles, one-pixel lines and the width-omitted default. Commented PythonDrawRectTest is not executed. Original inputs/assertions are unchanged. Float anti-aliasing, every clipping case and other shape algorithms are not claimed as reproduced defects.

Source case 76 records incorrect result/output and a rect-to-test_anti_aliasing_float_coordinates trace with Python-to-C object/argument APIs. The measured official regression instead checks integer rectangle border width/corners; float anti-aliasing is not claimed as the reproduced defect.

The complete native C product patch and official unittest addition are preserved. Actual version 2.1.1.dev1 / SDL 2.0.14 uses the same local package path and dummy environment. analysis/ contains source mapping/workbook/provenance; patches/ contains exact upstream diffs; official_swebench/ contains task records and all-file checksums; evaluator/ contains clean recipe/runner; verification/ contains complete raw build, prototype, controls and publication evidence.

Image: yutu0814/pyc-case-077-pygame:benchmark-v1.
