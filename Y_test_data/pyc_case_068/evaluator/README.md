# Evaluator

Apply candidate product patch before the protected exact upstream test patch, rebuild native extensions with python setup.py build_ext -i --force, then execute eight original official tester functions using tester_case068_isolated.py. The wrapper reads original helper counters, catches escaping Python assertions and executes generated callbacks. Result parsing uses explicit Tests/file.py::function PASSED/FAILED/SKIPPED lines, with all raw tester output retained.

Five unchanged upstream functions cover RGBA-to-palette similarity at epsilon 20, indexed P/L/RGB transparency conversion and saving, default RGBA quantization and rejection of unsupported method 0. Three unchanged regressions cover normal default conversion, 8-bit float conversion and 100-color octree quantization. Each function executes once in a fresh process; original tester assertion counters and yield_test callbacks are preserved. An explicit node status and positive assertion count are required for passing, so os._exit(0) skip cannot pass grading. No new assertions, thresholds, image assets or product changes beyond the exact upstream patch are introduced.

NumPy is not required. Pillow 2.3.0 exposes PIL.PILLOW_VERSION rather than PIL.__version__; image audits use that version attribute. Product changes are Python-only; native compilation ensures the pinned runtime is real.
