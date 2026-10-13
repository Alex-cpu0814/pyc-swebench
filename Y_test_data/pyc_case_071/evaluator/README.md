# Evaluator

Candidate native patch precedes the exact protected upstream test patch, then ujson is rebuilt with python setup.py build_ext -i --force. Eight measured original pytest IDs execute with their literal spaces/escapes intact. The anchored parser captures whole IDs including parameter content and ignores no missing/skipped results. Runtime assets are mounted only into evaluation containers, absent from the clean published Base image.

Exact upstream test_encode_indent inputs cover a nonempty object, {}, [], an object containing an empty object, and a list containing an empty list, at indent=4. Both original-format and stdlib-json equality assertions are retained. Four empty/nested inputs are measured FAIL_TO_PASS; the nonempty input and three unchanged dict/list encoding and Unicode decoding tests are PASS_TO_PASS. Real pytest parameter IDs containing spaces and literal escapes are kept exactly; the anchored result parser accepts spaces without decoding or normalizing IDs. No float-representation claim is made.

SCM metadata uses exact Base full history and only the fixed ancestor4.0.1 tag. Root /testbed/ujson extension version4.0.2.dev3 is audited. NumPy is not required.
