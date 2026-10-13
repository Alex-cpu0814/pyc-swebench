# Evaluator

Candidate patch is applied before the exact protected upstream binary test patch. The evaluator rebuilds Pillow native extensions, then runs two unchanged normal PSD regressions and the frame-count target. The binary PSD is protected test material and is excluded from the gold product patch.

The exact upstream frame-count test checks normal and negative-count PSD files for two frames and animation. Two unchanged regressions exercise normal PSD pixel decoding and layer seeking. The 5492-byte official PSD fixture is preserved by an exact binary test patch and checked against its upstream Git blob and SHA256. Product changes are Python-only; no hang or native C defect was observed.

NumPy is not required; its inherited template config argument is unused.
