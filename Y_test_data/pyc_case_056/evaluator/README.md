# Evaluator

Candidate patch is applied before the exact protected official patch. The evaluator rebuilds Pillow native extensions and runs two unchanged file-object save regressions plus the pathlib target. Required JPEG2000/JPEG/TIFF support is checked by the image build, clean audit and standalone dependency audit.

The exact upstream target opens TIFF/JPEG through Path and saves JPEG/JP2 through Path. Two unchanged neighboring regressions exercise named file-object and temporary-file saving. JPEG2000, JPEG and TIFF codecs are enabled and audited; no tests are skipped. Source Python-C taxonomy is retained, but this product patch changes Python only and the verified failure precedes native JPEG2000 encoding.

NumPy is not required; its inherited template config argument is unused.
