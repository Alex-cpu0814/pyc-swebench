"""Run one complete original Python2/3 script with its own argv and no core dump."""
from __future__ import print_function
import ctypes
import resource
import runpy
import sys

resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
libc = ctypes.CDLL(None, use_errno=True)
if libc.prctl(4, 0, 0, 0, 0) != 0 or libc.prctl(3, 0, 0, 0, 0) != 0:
    raise RuntimeError('Could not disable process dumpability')
script = sys.argv[1]
sys.argv = [script]
runpy.run_path(script, run_name='__main__')
