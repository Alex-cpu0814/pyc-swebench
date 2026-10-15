# Python-C to SWE-bench case081

Instance: pygame__pygame-702. Repository: pygame/pygame. Upstream: https://github.com/pygame/pygame/pull/702.

Base: 71c90cdb76cd8b12a0969f5d6314315bd0223c28. Fix: 1aeecd40314ec00c93d975b31a1f4518979d49a9.

Base: one official font-metrics rotation target fails and three regressions pass. Gold: all four official nodes pass.

Official test_issue_565 creates a fresh test_sans.ttf Font at size 24 for each unchanged pipe-text comparison, in original size 36, rotation 90, oblique=True order. Base fails at rotation; Gold completes all three. Three unchanged official regressions exercise default-font size, scalable and fixed-width properties. Six tracked setUp fonts plus tracked packaged freesansbold.ttf are audited. The test module uses X11; pytest directly executes its unittest methods, while dummy ignore tags belong to the pygame project runner. Undefined-character behavior from the source trace is not claimed.

Source case 80 records incorrect output and a native _ftfont_getmetrics trace ending in test_undefined_character_code. The measured official regression instead checks font size/rotation/oblique metrics changes using pipe text; undefined-character behavior is not claimed as reproduced.

Single native C product patch and complete official unittest patch preserved. Actual pygame1.9.5.dev0/FreeType2.10.4/SDL2.0.14 uses local native package and X11. Seven tracked font resources are audited; default package data is explicitly copied to its ordinary layout, with initial missing-resource evidence retained. Prior078 no-Base-failure evidence is archived separately.

analysis/ contains source mapping/workbook/provenance and creation tools; patches/ exact upstream diffs; official_swebench/ task records/all-file hashes; evaluator/ clean recipe/runner; verification/ all raw build/probe/control/publication evidence. Image: yutu0814/pyc-case-081-pygame:benchmark-v1.

## Publication status

Publication is pending: formal verification and workbook checks passed, but Docker Desktop currently fails during sailor-ingest socket startup. Neither the 081 Docker Hub push nor Git remote push has been performed. The verified image and all original evidence are retained; cleanup waits until publication succeeds.
