# Evaluator

Candidate patch is applied before the exact protected upstream binary test patch. Pillow native extensions are rebuilt, and two unchanged JPEG regressions plus the APP14 target run. JPEG support is explicitly checked; the new JPEG asset is protected test material, excluded from gold.

The exact upstream APP14 test checks RGB transform 1, CMYK transform 2 and absence of transform for the shortened fixture. Two unchanged regressions cover normal JPEG decoding and CMYK roundtrip. The official 29342-byte JPEG fixture is preserved by an exact binary patch and audited against its upstream blob and SHA256. Its declared APP14 segment length is 13 bytes including the 2-byte length field, leaving an 11-byte payload with no index 11. The upstream comment is preserved verbatim. Product changes are Python-only.

NumPy is not required; the inherited template config argument is unused.
