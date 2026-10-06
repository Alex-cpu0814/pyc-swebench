# Analysis

This directory preserves source Case 7, the verified parent/fix mapping, the upstream PR trace, environment requirements, and the generated one-row workbook.

The source row labels the defect as a reference-count misuse in `raise_memory_error`. The upstream PR explains that a test was needed so leak checking would exercise the error path. Local verification supplies the concrete trace: Base leaks two references and one memory block per measured run; Gold is stable.
