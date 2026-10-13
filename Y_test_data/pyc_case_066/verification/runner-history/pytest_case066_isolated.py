"""Use fresh processes for unchanged official RSS tests and neighboring regressions."""
import json
import signal
import subprocess
import sys

args = sys.argv[1:]
nodes = [x for x in args if x.startswith('Tests/') and '::' in x]
options = [x for x in args if x not in nodes]
if '--collect-only' in args:
    sys.exit(subprocess.call([sys.executable, '/benchmark/pytest_no_dump.py'] + args))
failed = False
for node in nodes:
    print('ISOLATED_NODE_BEGIN ' + node, flush=True)
    result = subprocess.run([sys.executable, '/benchmark/pytest_no_dump.py'] + options + [node], timeout=120)
    detail = {'node': node, 'returncode': result.returncode, 'signal': signal.Signals(-result.returncode).name if result.returncode < 0 else None}
    print('ISOLATED_NODE_RESULT ' + json.dumps(detail), flush=True)
    if result.returncode < 0:
        print(node + ' FAILED', flush=True)
    elif result.returncode not in (0, 1):
        raise RuntimeError('Unexpected pytest exit: ' + json.dumps(detail))
    failed = failed or result.returncode != 0
sys.exit(1 if failed else 0)
