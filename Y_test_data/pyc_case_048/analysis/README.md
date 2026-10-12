# Analysis

Source Case 47 maps to benchmark Case 048. The Base is the verified first parent of the upstream merge. Product and protected test patches are the exact upstream changes.

With identical GCC 10 non-recovering bounds instrumentation, Base reports scipy/signal/sigtoolsmodule.c:903:34: runtime error: index 23 out of bounds for the comparator table (21 entries) on the official float16 node. Its subprocess exits 1, while two neighboring nodes pass. Gold passes all three. Ordinary uninstrumented Base and Gold both passed, so an uninstrumented crash was not independently reproduced.

The exact upstream protected test patch retains all five dtype parameters. Formal grading selects only float16 (the discriminating comparator-table bounds case) plus test_basic and test_none. Ordinary builds passed on both revisions. The same non-recovering bounds configuration is applied to Base, Gold and candidate builds; each official pytest node runs in a separate subprocess to preserve neighboring results after the diagnostic.

## Upstream dates

The GitHub REST API reports PR creation at 2021-06-30T12:41:18Z and merge at 2021-07-02T07:25:58Z. SWE-bench created_at uses the opening date 2021-06-30, with UTC date precision; the merge date 2021-07-02 is retained separately in provenance and metadata. Source: https://api.github.com/repos/scipy/scipy/pulls/14327 .
