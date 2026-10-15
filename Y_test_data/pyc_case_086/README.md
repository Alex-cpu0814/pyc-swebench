# Python-C to SWE-bench case 086

Instance: pygame__pygame-d33b702d. Repository: pygame/pygame. Associated upstream: https://github.com/pygame/pygame/pull/515.

Base: 5f1d4528b46d7f3c368db6e1c395ffb0ae83623d. Source fix: d33b702dcfdc3b13479e490961b7f51c7e773d33.

Base: two existing official polygon tests fail and two regressions pass. Gold: all four official tests pass.

Official DrawPolygonTest uses a 20 by 20 pixel Surface. The cross method checks both width 1 outline and width 0 fill over a 10 by 10 pixel region. The illumine-shape method compares original four-vertex and six-vertex paths, checking top and internal horizontal edges. Square and diamond regressions retain their original pixels. The official test patch only deletes two FIXME comments; all assertion bodies and coordinates already exist on Base and are unchanged. No antialiasing, float coordinates, clipping or other drawing APIs are claimed.

Source case 85 traces native draw_fillpoly through polygon to test_1_pixel_high_or_wide_shapes. Actual failing targets here are existing cross and illumine-shape methods. Source branch commit d33b702d is listed in PR 515; PR merge 5590709b differs, and its opening/merge dates are recorded separately from the source commit date. No entire-PR equivalence or original caller failure is claimed.

Complete native C product patch and comment-only official test diff are preserved. Actual pygame 1.9.5.dev0 / SDL2 2.0.14 uses the audited local native draw module. analysis/ holds source/workbook/provenance and duplicate083 review; patches/ holds exact diffs; official_swebench/ holds task records and full-file checksums; evaluator/ holds clean image/runner; verification/ holds full raw evidence and publication.

Image: yutu0814/pyc-case-086-pygame:benchmark-v1.
