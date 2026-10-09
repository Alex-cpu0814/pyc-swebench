# Analysis

This directory preserves source Case 36, the verified first-parent/fix mapping, upstream trace, environment requirements, and the generated workbook.

On linux/amd64, Base terminates during the official test_ticket_742 sequence. The target node has no completed pytest result and is graded MISSING/unresolved. The upstream C fix and native rebuild allow it to pass; both neighboring regressions pass on Base and Gold.
