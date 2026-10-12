# Analysis

Source Case 52 maps to benchmark Case 053. Base 09605ff48e582fda6870a2c4c519650321f3f8de is the verified first parent of merge 6f73691564908f70967cf76b8f4f88e390f57fe9. The exact upstream product patch changes only Draw.c and Paste.c. The protected test patch preserves both upstream pytest files and the binary rectangle reference image.

Ordinary native Base fails both official I;16 assertions: point produces 13364 (0x3434) instead of 4660 (0x1234), and BASIC-layout text produces 65278 (0xFEFE) instead of 65534 (0xFFFE). Gold passes those two nodes plus the unchanged drawing and font-property regressions.

Original source row 52 references the RGB test_modify_after_resizing path. It is retained as source metadata and is not the execution trace of the verified I;16 drawing/text regression.

The GitHub REST API records PR creation at 2023-07-04T12:34:55Z and merge at 2023-10-05T18:54:26Z. Dataset created_at is the opening date 2023-07-04 at UTC date precision; merge date 2023-10-05 is separate. Source: https://api.github.com/repos/python-pillow/Pillow/pulls/7257 .
