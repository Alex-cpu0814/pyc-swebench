# Evaluator

Candidate patch is applied before the exact protected upstream test patch. The evaluator forces a rebuild of Pillow C extensions and runs two native radius regressions followed by the single official negative-radius test. The Tests/ pytest parser requires actual terminal node statuses; a process termination yields an explicit MISSING result.

One unchanged official target body checks construction and then filtering after radius mutation. Two unchanged regressions validate native numerical blur results for radius zero and one. The exact protected upstream patch retains the added BoxBlur(0) sanity parameter, outside graded scope. A Python-only partial control runs the same three nodes with regressions first: two pass, then the target process aborts with exit 134 and no terminal pytest status. The observed native guard is necessary in addition to constructor validation.

Build audit verifies the actual Pillow version and source import path. NumPy is not needed; its inherited template config argument is unused.
