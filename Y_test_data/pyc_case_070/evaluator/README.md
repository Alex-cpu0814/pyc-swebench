# Evaluator

Apply candidate product patch before the exact protected upstream test patch, rebuild ujson with python setup.py build_ext -i --force, then run four unmodified official pytest functions. Native runtime is locally compiled, SCM metadata comes from exact Base history and fixed ancestor tag, and all build dependencies are pinned. Test process signals and exit codes are retained.

The exact protected upstream test decodes the JSON object {"obj":31337} and compares its indent=4 encoded text with the original four-space formatting. Three unchanged official regressions cover ordinary dictionary/list conversion and Unicode decoding. Tests execute normally in one pytest process, without altered values, assertions or thresholds. Product patch is the single native C argument-format change; vendored C++ double-conversion is compiled but unchanged.

NumPy is not required. Source directory /testbed contains the root ujson extension. Explicit nativeAuditCommand checks ujson3.2.1.dev2 rather than inheriting another project audit. Runtime assets are mounted into evaluation containers and are absent from the published clean Base image.
