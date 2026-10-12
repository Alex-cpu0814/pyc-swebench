# Analysis

This directory preserves source Case 48, the verified Base/Fix mapping (Base is the sole parent of Fix), upstream trace, environment requirements, and the generated workbook.

Base with the exact official test patch: GetVar.test6 raises NameMapper.NotFound from Cheetah/Template.py:1446 instead of the expected ValueError. The native name mapper reads an uninitialized chunk when the stripped name is empty. The upstream report describes a Python 2.7/CentOS segfault; this Python 3.8.20 environment reproduces an incorrect exception, not that crash.
